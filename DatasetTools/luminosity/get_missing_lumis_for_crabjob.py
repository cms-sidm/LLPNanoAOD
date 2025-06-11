import os, sys
import json

# get input path
input_path = sys.argv[1]
dataset = sys.argv[2]
parent_dataset = sys.argv[3]
processedLumis = input_path + '/results/processedLumis.json'

def read_lumis_file(filename):
    """
    Reads a lumisection file and returns a dictionary with run numbers as keys
    and sorted lists of lumisections as values.
    """
    lumis = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(' ', 1)  # Split on the first space
            run_number = parts[0]
            lumisections = eval(parts[1])  # Convert the list string to a Python list
            lumis[run_number] = sorted(set(lumisections))  # Store sorted unique lumisections
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

outputLumis = input_path + '/results/outputDatasetLumis.txt'
command = 'dasgoclient --query="run,lumi dataset=' + dataset + ' instance=prod/phys03" > ' + outputLumis
print(command)
if not os.path.exists(outputLumis):
    os.system(command)

inputLumis = input_path + '/results/inputLumis.txt'
command = 'dasgoclient --query="run,lumi dataset=' + parent_dataset + '" > ' + inputLumis
print(command)
if not os.path.exists(inputLumis):
    os.system(command)

input_lumis = read_lumis_file(inputLumis)
processed_lumis = read_lumis_file(outputLumis)

# print('input_lumis:', input_lumis)
# print('processed_lumis:', processed_lumis)

# Step 2: Find missing lumisections
missing_lumis = {}
for run_number, input_lumisections in input_lumis.items():
    processed_lumisections = processed_lumis.get(run_number, [])
    
    # Find the missing lumisections
    missing = [lumi for lumi in input_lumisections if lumi not in processed_lumisections]
    # missing = sorted(set(input_lumisections) - set(processed_lumisections))
    if missing:  # Only add to the output if there are missing lumisections
        missing_lumis[run_number] = list_to_ranges(missing)
        # print('Run', run_number, 'is missing lumisections:', missing_lumis[run_number])

# Save missing lumis to a file
output_file = input_path + '/results/missingLumis.json'
f_out = open(output_file, 'w')
json.dump(missing_lumis, f_out, separators=(',', ':'))

f_out.close()
print('saved failed files to: ', output_file)
