import os


# Define the paths to the base directories
base_pnfs_path = '/pnfs/desy.de/cms/tier2'
# dataset_dir = '/store/user/lrygaard/ttalps/SingleMuon/LLPminiAODv1_Run2016B-21Feb2020_ver2_UL2016_HIPM-v1'
# dataset_dir = '/store/user/lrygaard/ttalps/SingleMuon/LLPminiAODv1_Run2016D-21Feb2020_UL2016_HIPM-v1'
# dataset_dir = '/store/user/lrygaard/ttalps/SingleMuon/LLPminiAODv1_Run2016G-21Feb2020_UL2016-v1'
# dataset_dir = '/store/user/lrygaard/ttalps/SingleMuon/LLPminiAODv1_Run2017D-09Aug2019_UL2017-v1'
# dataset_dir = '/store/user/lrygaard/ttalps/SingleMuon/LLPminiAODv1_Run2017E-09Aug2019_UL2017-v1'
# dataset_dir = '/store/user/lrygaard/ttalps/Muon/LLPminiAODv1_Run2022F-PromptReco-v1'
dataset_dir = '/store/user/lrygaard/ttalps/Muon/LLPminiAODv1_Run2022G-PromptReco-v1'
dir_to_keep = f'{base_pnfs_path}{dataset_dir}/240724_124728'
dir_to_remove = f'{base_pnfs_path}{dataset_dir}/240809_125933'

# Define the output file path
output_file = 'overlapping_files_to_invalidate_2022G.txt'

print(f"Comparing files in {dir_to_keep} and {dir_to_remove}.")

# Create a list for storing paths of overlapping files
overlapping_files = []

# Loop through directories 0000 to 0008
for i in range(9):  # X = 0 to 8
    dir_1 = os.path.join(dir_to_keep, f'000{i}')
    dir_2 = os.path.join(dir_to_remove, f'000{i}')

    # Check if both directories exist
    if os.path.exists(dir_1) and os.path.exists(dir_2):
        # List files in both directories
        files_dir_1 = set(os.listdir(dir_1))
        files_dir_2 = set(os.listdir(dir_2))

        # Find overlapping files
        common_files = files_dir_1 & files_dir_2

        # Append the full paths of overlapping files to the list
        for file in common_files:
            full_path = f'{dataset_dir}/240809_125933/000{i}/{file}'
            overlapping_files.append(full_path)

# Save the overlapping files with complete paths in double quotes
with open(output_file, 'w') as f:
    for file_path in overlapping_files:
        f.write(f'{file_path}\n')

print(f"Overlapping files have been saved to {output_file}.")

