import sys
from DataFormats.FWLite import Handle, Events
import ROOT
from ROOT import TFile, edm
from collections import defaultdict
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.FWLiteEnabler.enable()

def process_root_file(file_path, file_lumi_map):
    xrootd_path = "root://xrootd-cms.infn.it/" + file_path
    print("Processing: ", xrootd_path)
    
    file = ROOT.TFile.Open(xrootd_path)
    if file and not file.IsZombie():
        try:
            print("File opened successfully.")
            events = Events(file)
            local_lumis = set()  # Track run-lumi pairs for this specific file

            # Collect all run-lumi pairs for the file
            for event in events:
                try:
                    aux = event.eventAuxiliary()
                    lumi = aux.luminosityBlock()
                    run = aux.run()
                    run_lumi = (run, lumi)
                    
                    # Track local run-lumi pairs for the file
                    local_lumis.add(run_lumi)

                except Exception as e:
                    print("Error reading run-lumi pair: {}".format(e))
            
            # After processing all events, store the run-lumi pairs in the file map
            file_lumi_map[file_path] = local_lumis

        except Exception as e:
            print("Error processing file: {}".format(e))
        finally:
            file.Close()
    else:
        print("Failed to open the file or the file is corrupted.")

def main(txt_file):
    file_lumi_map = defaultdict(set)  # Map of file paths to their run-lumi pairs
    files_to_process = []

    # Step 1: Collect run-lumi pairs from each file in the input list
    with open(txt_file, 'r') as file:
        for line in file:
            root_file_path = line.strip()
            if root_file_path:
                print("Processing file listed in text file: ", root_file_path)
                files_to_process.append(root_file_path)
                process_root_file(root_file_path, file_lumi_map)

    # Step 2: Check for duplicates within files and across all files
    seen_lumis = set()
    duplicates_in_files = defaultdict(set)  # Store duplicates found in each file
    for file_path, lumis in file_lumi_map.items():
        # Check for duplicates within the file
        for run_lumi in lumis:
            if run_lumi in seen_lumis:
                duplicates_in_files[file_path].add(run_lumi)
            else:
                seen_lumis.add(run_lumi)
    
    # Step 3: Output results for duplicates within files and across files
    print("\nDuplicates found within files:")
    for file_path, duplicates in duplicates_in_files.items():
        print("File: ", file_path)
        for run, lumi in sorted(duplicates):
            print("  Run: {}, Lumi: {}".format(run, lumi))

    print("\nDuplicates found across all files:")
    for run_lumi in seen_lumis:
        count = sum(1 for lumis in file_lumi_map.values() if run_lumi in lumis)
        if count > 1:
            print("  Run: {}, Lumi: {} appears in {} files.".format(run_lumi[0], run_lumi[1], count))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_lumis.py <txt_file>")
    else:
        main(sys.argv[1])
