#!/bin/bash

user_path="/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src/LLPNanoAOD/DatasetTools/luminosity"

#####  2016  #####

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2016B-21Feb2020_ver1_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"

# golden_json_path="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"

#####  2017  #####

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2017F-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"

# golden_json_path="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt"

#####  2018  #####

dataset="/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"
dataset2="/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"
dataset3="/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"
dataset4="/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD"
datasets="${dataset},${dataset2}",${dataset3}",${dataset4}"

golden_json_path="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"

#####  2022  #####

# datasets="/Muon/lrygaard-LLPminiAODv-1_Run2022G-PromptReco-v1-d28583fd5c19cd9d96cc0a9145178f7d/USER"

# golden_json_path="Cert_Collisions2022_355100_362760_Golden.json"

#####  2023  #####

# datasets="/Muon0/lrygaard-LLPnanoAODv1_Run2023D-PromptReco-v2-00000000000000000000000000000000/USER"

# golden_json_path="Cert_Collisions2023_366442_370790_Golden.json"

# make datasets list:
# datasets="${dataset},${dataset2}"

python_script="get_missing_lumis_for_json.py"  

output_name="missing_lumis_from_golden_json_2018.json"

python "$python_script" "$datasets" "$golden_json_path" "$output_name"