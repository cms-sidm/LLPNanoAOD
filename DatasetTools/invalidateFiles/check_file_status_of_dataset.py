import os

dataset="/TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/lrygaard-LLPminiAODv1_Run3Summer22EEDRPremix-124X_v1-v3-c28c1b325b38cb5d3a9606ae5448d377/USER"

base_pnfs_path="/pnfs/desy.de/cms/tier2/store/user/lrygaard/ttalps/"
dataset_dir="TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8/LLPminiAODv1_Run3Summer22EEDRPremix-124X_v1-v3"

instance="prod/phys03"

# valid files
command = "dasgoclient -query='file dataset="+dataset+" instance="+instance+" status=valid' | wc -l"
valid_files = int(os.popen(command).read())
print("Number of valid files: ", valid_files)

# invalid files
command = "dasgoclient -query='file dataset="+dataset+" instance="+instance+" status=invalid' | wc -l"
invalid_files = int(os.popen(command).read())
print("Number of invalid files: ", invalid_files)

# number of files on pnfs
tot_num_files = 0
if os.path.exists(base_pnfs_path+dataset_dir):
    for subdir in os.listdir(base_pnfs_path+dataset_dir):
        path = base_pnfs_path+dataset_dir+"/"+subdir
        print("Checking ", path)
        for i in range(20):
            if os.path.exists(path+"/000"+str(i)):
                command = "ls "+path+"/000"+str(i)+" | wc -l"
                num_files = int(os.popen(command).read())
                tot_num_files += num_files
else:
    print("Path does not exist: ", base_pnfs_path+dataset_dir)

print("Number of files on pnfs: ", tot_num_files)

if tot_num_files == valid_files:
    print("All valid files are correctly stored on pnfs.")

if valid_files > tot_num_files:
    print("There are more valid files than files on pnfs.")
    # find the overflow files that should be invalid:
    command = "dasgoclient -query='file dataset="+dataset+" instance="+instance+" status=valid'"
    valid_files = os.popen(command).read().split("\n")

    # get files on pnfs
    pnfs_files = []
    if os.path.exists(base_pnfs_path+dataset_dir):
        for subdir in os.listdir(base_pnfs_path+dataset_dir):
            path = base_pnfs_path+dataset_dir+"/"+subdir
            for i in range(20):
                if os.path.exists(path+"/000"+str(i)):
                    command = "ls "+path+"/000"+str(i)
                    files = os.popen(command).read().split("\n")
                    for file in files:
                        pnfs_files.append(file)

    # find the overflow files
    overflow_files = []
    for file in valid_files:
        if file not in pnfs_files:
            overflow_files.append(file)
    
    print("Number of overflow files: ", len(overflow_files))
    dataset_dir_str = dataset_dir.replace("/", "_")
    output_file = "overflow_files_"+dataset_dir_str+".txt"
    with open(output_file, 'w') as f:
        for file in overflow_files:
            f.write(file+"\n")
    print("Overflow files have been saved to ", output_file)
