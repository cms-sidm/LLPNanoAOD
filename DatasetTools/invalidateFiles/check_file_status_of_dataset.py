import os

#####   SETTINGS   #####
dataset="/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/lrygaard-LLPnanoAODv1_Run3Summer22EEDRPremix-124X_postEE_v1-v2-00000000000000000000000000000000/USER"

base_pnfs_path="/pnfs/desy.de/cms/tier2/store/user/lrygaard/ttalps/"
## dataset_dir can be set to ""
# dataset_dir=""
dataset_dir="DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/LLPnanoAODv1_Run3Summer22EEDRPremix-124X_postEE_v1-v2"

## input_list_of_files_to_invalidate can be set to ""
# input_list_of_files_to_invalidate=""
input_list_of_files_to_invalidate="DYJetsToLL_M-50_2022_LLPnano.txt"

instance="prod/phys03"

def get_valid_files(dataset, instance):
    command = "dasgoclient -query='file dataset="+dataset+" instance="+instance+" status=valid'"
    valid_files = os.popen(command).read().split("\n")
    # check that no line is empty
    valid_files = [file for file in valid_files if file]
    return valid_files

def get_invalid_files(dataset, instance):
    command = "dasgoclient -query='file dataset="+dataset+" instance="+instance+" status=invalid'"
    invalid_files = os.popen(command).read().split("\n")
    # check that no line is empty
    invalid_files = [file for file in invalid_files if file]
    return invalid_files

def get_pnfs_files(base_pnfs_path, dataset_dir):
    pnfs_files = []
    for subdir in os.listdir(base_pnfs_path+dataset_dir):
        path = base_pnfs_path+dataset_dir+"/"+subdir
        for i in range(20):
            if os.path.exists(path+"/000"+str(i)):
                command = "ls "+path+"/000"+str(i)
                files = os.popen(command).read().split("\n")
                # check that no line is empty
                files = [file for file in files if file]
                for file in files:
                    pnfs_files.append(file)
    return pnfs_files

def get_files_to_invalidate(input_list_of_files_to_invalidate):
    files_to_invalidate = []
    with open(input_list_of_files_to_invalidate, 'r') as f:
        for line in f:
            files_to_invalidate.append(line.strip())
    return files_to_invalidate

#####   VALID FILES   #####
valid_files = get_valid_files(dataset, instance)
n_valid_files = len(valid_files)
print("Number of valid files: ", n_valid_files)

#####   INVALID FILES   #####
invalid_files = get_invalid_files(dataset, instance)
n_invalid_files = len(invalid_files)
print("Number of invalid files: ", n_invalid_files)

#####   PNFS FILES   #####
n_pnfs_files = 0
pnfs_files = []
if dataset_dir != "":
    if os.path.exists(base_pnfs_path+dataset_dir):
        pnfs_files = get_pnfs_files(base_pnfs_path, dataset_dir)
        n_pnfs_files = len(pnfs_files)
    else:
        print("Path does not exist: ", base_pnfs_path+dataset_dir)
print("Number of files on pnfs: ", n_pnfs_files)

#####   FILES TO INVALIDATE   #####
num_files_to_invalidate = 0
if input_list_of_files_to_invalidate != "":
    files_to_invalidate = get_files_to_invalidate(input_list_of_files_to_invalidate)
    num_files_to_invalidate = len(files_to_invalidate)
print("Number of files to invalidate: ", num_files_to_invalidate)

if n_pnfs_files == n_valid_files:
    print("All valid files are correctly stored on pnfs.")

overflow_files = []
#####   CASE 1: MORE VALID FILES THAN FILES ON PNFS   #####
if dataset_dir != "":
    if n_valid_files > n_pnfs_files:
        print("There are more valid files than files on pnfs.")        
        for file in valid_files:
            if file not in pnfs_files:
                overflow_files.append(file)

#####   CASE 2: FILES THAT SHOULD BE INVALIDATED ARE STILL VALID   #####
if input_list_of_files_to_invalidate != "":
    for file in files_to_invalidate:
        if file in valid_files:
            if file not in overflow_files:
                overflow_files.append(file)

print("Number of overflow files: ", len(overflow_files))
if len(overflow_files) > 0:
    dataset_str = dataset.replace("/", "_")
    output_file = "overflow_files_"+dataset_str+".txt"
    with open(output_file, 'w') as f:
        for file in overflow_files:
            f.write(file+"\n")
    print("Overflow files have been saved to ", output_file)
