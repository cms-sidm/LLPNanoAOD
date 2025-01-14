#!/bin/bash

job_nr=$1
n_lines_to_read=$2

source /cvmfs/cms.cern.ch/cmsset_default

python_script="invalidate_dbs_files.py"  

file_with_paths_to_invalidate="files_to_invalidate.txt"

python "$python_script" "$job_nr" "$n_lines_to_read" "$file_with_paths_to_invalidate"
