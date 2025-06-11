import os

# Define the paths to the base directories
base_pnfs_path = '/pnfs/desy.de/cms/tier2'
input_file_with_paths = 'overlapping_files_to_remove/overlapping_files_to_invalidate_2018A.txt'
# input_file_with_paths = 'overlapping_files_test.txt'

# Define the output file path
output_file = 'overlapping_files_to_remove/overlapping_files_to_invalidate_2018A_size.txt'
# output_file = 'overlapping_files_test_size.txt'

total_size = 0

# open the file with the paths
with open(input_file_with_paths, 'r') as f:
    for line in f:
        # remove the newline character
        line = line.strip()
        # get the size of the file in GB with 2 decimal places
        size = round(os.path.getsize(f'{base_pnfs_path}/{line}') / 1024**3, 2)
        # write the size to the output file
        with open(output_file, 'a') as f_out:
            f_out.write(f'{line}\t{size}\n')
        total_size += os.path.getsize(f'{base_pnfs_path}/{line}')

with open(output_file, 'a') as f:
    f.write(f'Total size: {round(total_size / 1024**3, 2)} GB\n')

print(f"File sizes written to {output_file}.")
