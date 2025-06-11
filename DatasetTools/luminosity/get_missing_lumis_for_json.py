import os, sys
import json

# get input path
datasets = sys.argv[1]
golden_json_path = sys.argv[2]
json_dataset_string = sys.argv[3]

datasets = datasets.split(',')

def read_lumis_file(filename):
    """
    Reads the tmp.txt file and returns a dictionary with run numbers as keys
    and sorted lists of lumisections as values.
    """
    lumis = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(' ', 1)  # Split on the first space
            run_number = parts[0]
            lumisections = eval(parts[1])  # Convert the list string to a Python list

            valid_lumisections = [lumi for lumi in lumisections if is_in_golden(run_number, lumi)]

            if valid_lumisections:
                lumis[run_number] = sorted(set(valid_lumisections))
    return lumis


def list_to_ranges(lumisections):
    """
    Converts a sorted list of lumisections to a list of ranges.
    """
    if not lumisections:
        return []
    
    ranges = []
    start = lumisections[0]
    end = lumisections[0]
    
    for num in lumisections[1:]:
        if num == end + 1:
            end = num
        else:
            ranges.append([start, end])
            start = num
            end = num
            
    ranges.append([start, end])
    return ranges

with open(golden_json_path, 'r') as f:
    golden_data = json.load(f)

def is_in_golden(run_number, lumisection):
    """Check if a specific lumisection is in the allowed ranges for a given run number."""
    if run_number not in golden_data:
        return False
    # Retrieve the allowed ranges from golden data
    allowed_ranges = golden_data[run_number]
    # Check if the lumisection is in any of the allowed ranges
    for start, end in allowed_ranges:
        if start <= lumisection <= end:
            return True
    return False

def merge_lumis(target_lumis, new_lumis):
    """
    Merges lumisections from new_lumis into target_lumis.
    Ensures deduplication and sorting of lumisections for each run.
    Args:
        target_lumis (dict): The dictionary to merge into.
        new_lumis (dict): The dictionary to merge from.
    """
    for run_number, lumisections in new_lumis.items():
        if run_number in target_lumis:
            # Combine and deduplicate lumisections for the same run
            target_lumis[run_number] = sorted(set(target_lumis[run_number] + lumisections))
        else:
            # Add new run_number to target_lumis
            target_lumis[run_number] = lumisections

processed_lumis = {}
for dataset in datasets:
    dataset_string = dataset.replace('/', '_')
    outputLumis = './output_LLPminiAOD_dataset_lumi/'+dataset_string+'.txt'
    command = 'dasgoclient --query="run,lumi dataset=' + dataset + ' instance=prod/global" > ' + outputLumis
    print(command)
    os.system(command)
    dataset_lumis = read_lumis_file(outputLumis)
    merge_lumis(processed_lumis, dataset_lumis)


# Step 2: loop over lumisections in golden json and check if they are in the input lumis
missing_lumis = {}
for run, lumis in golden_data.items():
    if run not in processed_lumis:
        if run not in missing_lumis:
            missing_lumis[run] = []
        missing_lumis[run].append(lumis)
    else:
        for lumi in lumis:
            if lumi not in processed_lumis[run]:
                if run not in missing_lumis:
                    missing_lumis[run] = []
                missing_lumis[run].append(lumi)

# Save missing lumis to a file
output_file = './output_LLPminiAOD_dataset_lumi/'+json_dataset_string
f_out = open(output_file, 'w')
json.dump(missing_lumis, f_out, separators=(',', ':'))

f_out.close()
print('saved missing lumis to: ', output_file)
