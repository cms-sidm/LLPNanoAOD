# Dataset Tools

Tools for handling datasets and dataset files

## Invalidate Files
In the [invalidateFiles folder](invalidateFiles/) there are tools to invalidate files on DAS.
The command to invalidate a file is:
```
crab-dev setfilestatus --status INVALID --file {filepath}
```

The command to validate a file is:
```
crab-dev setfilestatus --status VALID --file {filepath}
```

The `crab-dev` command which currently only allows for one file as input, so you have to do it separetly for each file you want to invalidate. This is why we run it on condor.

These are the main files:
* [invalidate_dbs_files.py](invalidateFiles/invalidate_dbs_files.py) - python script to invalidate a file. You need to CHECK:
    * `base_path_to_files` = base path to where your .txt file with a list of all files to invalidate
    * `cmssw_path` = path to your CMSSW src directory
* [invalidate_dbs_files.sh](invalidateFiles/invalidate_dbs_files.sh) - bash script for condor. You need to CHECK:
    * `file_with_paths_to_invalidate` = name of your .txt file with a list of all files to invalidate
* [invalidate_dbs_files.sub](invalidateFiles/invalidate_dbs_files.sub) - conodor submission script. You need to CHECK:
    * the second value in `arguments` is the number of files to read per job = `n_files_to_read` in `invalidate_dbs_files.sh`
    * `queue` = number of jobs to run
    * Note `n_files_to_read` times `queue` should be equal to number of lines in your input .txt file with a list of all files to invalidate. For example for an input with 100 files: if `n_files_to_read` = 2 then `queue` = 100/2 = 50

You also need to create `log`, `error`, `output` directories for the condor jobs.

At least on DESY sites we observed failed jobs due to the site connection. Therefore, it's possible to check the number of valid/invalid files in the dataset and compare it to number of files stored on pnfs:
```
python3 check_file_status_of_dataset.py
```
Just specify the dataset and the path to the pnfs storage in `check_file_status_of_dataset.py`. If there are more valid files compared to number of files on pnfs these missing (valid) files will be saved in the output named `overflow_files_[datasetname]`.

## Get overlapping files
In the [invalidateFiles folder](invalidateFiles/) there is also a script to get overlapping files in /pnfs/ for a dataset.

Use the script [get_overlapping_dbs_files](invalidateFiles/get_overlapping_dbs_files.py), and CHECK:
* `base_pnfs_path` = base path to (desy) pnfs
* `dataset_dir`= to the dataset directory on pnfs
* `dir_to_keep` = the directory with all files you which to keep
* `dir_to_remove` = the directory to check if any files overlap with the files in `dir_to_keep`
* `output_file` = name of the output file with the list of overlapping files
