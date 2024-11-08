import os, sys

job_nr = int(sys.argv[1])
number_of_lines_to_read = int(sys.argv[2])
file_with_paths_to_invalidate = sys.argv[3]

# file_with_paths_to_invalidate = "overlapping_files_to_invalidate_2022G.txt"

base_path_to_files = "/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src/LLPNanoAOD/DatasetTools/invalidateFiles"
cmssw_path = "/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src"
base_command = f"cd {cmssw_path}; cmssw-el7 --command-to-run \"cmsenv; cd {base_path_to_files};"

start_index = job_nr * number_of_lines_to_read
end_index = start_index + number_of_lines_to_read

print(f"Start index: {start_index}")
print(f"End index: {end_index}")

commands = []

# open file
with open(file_with_paths_to_invalidate, "r") as file:
    for current_index, line in enumerate(file):
        if current_index >= start_index and current_index < end_index:
            commands.append(f"{base_command} crab-dev setfilestatus --status INVALID --file {line.strip()}\"")
        elif current_index >= end_index:
            break 

for command in commands:
    print(command)
    os.system(command)
