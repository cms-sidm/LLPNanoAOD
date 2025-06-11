#!/bin/bash

user_path="/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src/LLPNanoAOD/DatasetTools/luminosity"

#####  2016  #####

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2016B-21Feb2020_ver1_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# parent_dataset="/SingleMuon/Run2016B-21Feb2020_ver1_UL2016_HIPM-v1/AOD"

# dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2016B-21Feb2020_ver2_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# dataset2="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2016B-21Feb2020_ver2_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# parent_dataset="/SingleMuon/Run2016B-21Feb2020_ver2_UL2016_HIPM-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2016C-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# parent_dataset="/SingleMuon/Run2016C-21Feb2020_UL2016_HIPM-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_Run2016C-21Feb2020_UL2016_HIPM-v1-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD"

# dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2016D-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# dataset2="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2016D-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/SingleMuon/Run2016D-21Feb2020_UL2016_HIPM-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_LLPminiAODv1_Run2016D-21Feb2020_UL2016_HIPM-v1-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2016D-21Feb2020_UL2016_HIPM-v1/AOD"
# parent_dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2016D-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# parent_dataset="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2016D-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2016E-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# parent_dataset="/SingleMuon/Run2016E-21Feb2020_UL2016_HIPM-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_Run2016E-21Feb2020_UL2016_HIPM-v1-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2016E-21Feb2020_UL2016_HIPM-v1/AOD"
# parent_dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2016E-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"

# dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2016F-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# dataset2="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2016F-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/SingleMuon/Run2016F-21Feb2020_UL2016_HIPM-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_LLPminiAODv1_Run2016F-21Feb2020_UL2016_HIPM-v1-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2016F-21Feb2020_UL2016_HIPM-v1/AOD"

# dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2016F-21Feb2020_UL2016-v1-e8b05bf423a072ce8e514b113ad393f0/USER"
# dataset2="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2016F-21Feb2020_UL2016-v1-e8b05bf423a072ce8e514b113ad393f0/USER"
# parent_dataset="/SingleMuon/Run2016F-21Feb2020_UL2016-v1/AOD"

# dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2016G-21Feb2020_UL2016-v1-e8b05bf423a072ce8e514b113ad393f0/USER"
# dataset2="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2016G-21Feb2020_UL2016-v1-e8b05bf423a072ce8e514b113ad393f0/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/SingleMuon/Run2016G-21Feb2020_UL2016-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_LLPminiAODv1_Run2016G-21Feb2020_UL2016-v1-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

# datasets="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2016H-21Feb2020_UL2016-v1-e8b05bf423a072ce8e514b113ad393f0/USER"
# parent_dataset="/SingleMuon/Run2016H-21Feb2020_UL2016-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_Run2016H-21Feb2020_UL2016-v1-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD"

# golden_json_path="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"

#####  2017  #####

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2017B-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"
# parent_dataset="/SingleMuon/Run2017B-09Aug2019_UL2017-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2017C-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"
# parent_dataset="/SingleMuon/Run2017C-09Aug2019_UL2017-v1/AOD"

# dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2017D-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"
# dataset2="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2017D-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/SingleMuon/Run2017D-09Aug2019_UL2017-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_LLPminiAODv1_Run2017D-09Aug2019_UL2017-v1-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD"
# parent_dataset="/SingleMuon/Run2017D-09Aug2019_UL2017-v1/AOD"
# parent_dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2017D-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"
# parent_dataset="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2017D-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2017E-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"
# parent_dataset="/SingleMuon/Run2017E-09Aug2019_UL2017-v1/AOD"

datasets="/SingleMuon/lrygaard-LLPnanoAODv1_Run2017E-09Aug2019_UL2017-v1-00000000000000000000000000000000/USER"
parent_dataset="/SingleMuon/Run2017E-09Aug2019_UL2017-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2017F-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER"
# parent_dataset="/SingleMuon/Run2017F-09Aug2019_UL2017-v1/AOD"

golden_json_path="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt"

#####  2018  #####

# datasets="/SingleMuon/lrygaard-LLPminiAODv1_Run2018A-12Nov2019_UL2018-v5-9cdbfc999b77f606d32dabc67655eebd/USER"
# parent_dataset="/SingleMuon/Run2018A-12Nov2019_UL2018-v5/AOD"

# datasets="/SingleMuon/lrygaard-crab_SingleMuonB_LLPminiAOD-9cdbfc999b77f606d32dabc67655eebd/USER"
# parent_dataset="/SingleMuon/Run2018B-12Nov2019_UL2018-v3/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_lrygaard-crab_SingleMuonB_LLPminiAOD-9cdbfc999b77f606d32dabc67655eebd-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD"

# datasets="/SingleMuon/lrygaard-crab_SingleMuonC_LLPminiAOD-9cdbfc999b77f606d32dabc67655eebd/USER"
# parent_dataset="/SingleMuon/Run2018C-12Nov2019_UL2018-v3/AOD"

# dataset="/SingleMuon/lrygaard-LLPminiAODv1D_Run2018D-12Nov2019_UL2018-v8-9cdbfc999b77f606d32dabc67655eebd/USER"
# dataset2="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2018D-12Nov2019_UL2018-v8-9cdbfc999b77f606d32dabc67655eebd/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/SingleMuon/Run2018D-12Nov2019_UL2018-v8/AOD"

# datasets="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/lrygaard-LLPminiAODv1_RunIISummer20UL18RECO-106X_v11-v2-c15273f0b6812ff053a850f456209388/USER"

# golden_json_path="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"

#####  2022  #####

# dataset="/SingleMuon/lrygaard-LLPminiAODv1_Run2022C-27Jun2023-v1-38ef38690661ea445a2643bbff3790b7/USER"
# dataset2="/SingleMuon/lrygaard-LLPminiAODv1-1_Run2022C-27Jun2023-v1-38ef38690661ea445a2643bbff3790b7/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/SingleMuon/Run2022C-27Jun2023-v1/AOD"

# datasets="/SingleMuon/lrygaard-LLPnanoAODv1_LLPminiAODv1_Run2022C-27Jun2023-v1-00000000000000000000000000000000/USER"
# parent_dataset="/SingleMuon/Run2022C-27Jun2023-v1/AOD"

# datasets="/Muon/lrygaard-LLPnanoAODv1_Run2022C-27Jun2023-v1-00000000000000000000000000000000/USER"
# parent_dataset="/Muon/Run2022C-27Jun2023-v1/AOD"

# datasets="/Muon/lrygaard-LLPminiAODv1_Run2022D-27Jun2023-v2-38ef38690661ea445a2643bbff3790b7/USER"
# parent_dataset="/Muon/Run2022D-27Jun2023-v2/AOD"

# datasets="/Muon/lrygaard-LLPnanoAODv1_Run2022D-27Jun2023-v2-00000000000000000000000000000000/USER"
# parent_dataset="/Muon/Run2022D-27Jun2023-v2/AOD"

# dataset="/Muon/lrygaard-LLPminiAODv1_Run2022E-27Jun2023-v1-38ef38690661ea445a2643bbff3790b7/USER"
# dataset2="/Muon/lrygaard-LLPminiAODv1-1_Run2022E-27Jun2023-v1-38ef38690661ea445a2643bbff3790b7/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/Muon/Run2022E-27Jun2023-v1/AOD"

# datasets="/Muon/lrygaard-LLPnanoAODv1_LLPminiAODv1_Run2022E-27Jun2023-v1-00000000000000000000000000000000/USER"
# parent_dataset="/Muon/Run2022E-27Jun2023-v1/AOD"

# datasets="/Muon/lrygaard-LLPminiAODv1-1_Run2022F-PromptReco-v1-d28583fd5c19cd9d96cc0a9145178f7d/USER"
# parent_dataset="/Muon/Run2022F-PromptReco-v1/AOD"

# datasets="/Muon/lrygaard-LLPminiAODv-1_Run2022G-PromptReco-v1-d28583fd5c19cd9d96cc0a9145178f7d/USER"
# parent_dataset="/Muon/Run2022G-PromptReco-v1/AOD"

# golden_json_path="Cert_Collisions2022_355100_362760_Golden.json"

#####  2023  #####

# dataset="/Muon0/lrygaard-LLPminiAODv1_Run2023C-PromptReco-v4-905bc08224124a8af93cb10065c39aca/USER"
# dataset2="/Muon0/lrygaard-LLPminiAODv1-1_Run2023C-PromptReco-v4-905bc08224124a8af93cb10065c39aca/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/Muon0/Run2023C-PromptReco-v4/AOD"

# datasets="/Muon0/lrygaard-LLPnanoAODv1_Run2023C-PromptReco-v1-00000000000000000000000000000000/USER"
# parent_dataset="/Muon0/Run2023C-PromptReco-v1/AOD"

# datasets="/Muon0/lrygaard-LLPnanoAODv1_LLPminiAODv1_Run2023C-PromptReco-v4-00000000000000000000000000000000/USER"
# parent_dataset="/Muon0/Run2023C-PromptReco-v4/AOD"

# datasets="/Muon1/lrygaard-LLPnanoAODv1_Run2023C-PromptReco-v1-00000000000000000000000000000000/USER"
# parent_dataset="/Muon1/Run2023C-PromptReco-v1/AOD"

# datasets="/Muon1/lrygaard-LLPnanoAODv1_LLPminiAODv1_Run2023C-PromptReco-v4-00000000000000000000000000000000/USER"
# parent_dataset="/Muon1/Run2023C-PromptReco-v4/AOD"

# dataset="/Muon1/lrygaard-LLPminiAODv1_Run2023C-PromptReco-v4-905bc08224124a8af93cb10065c39aca/USER"
# dataset2="/Muon1/lrygaard-LLPminiAODv1-1_Run2023C-PromptReco-v4-905bc08224124a8af93cb10065c39aca/USER"
# datasets="${dataset},${dataset2}"
# parent_dataset="/Muon1/Run2023C-PromptReco-v4/AOD"

# datasets="/Muon0/lrygaard-LLPminiAODv1_Run2023D-PromptReco-v2-905bc08224124a8af93cb10065c39aca/USER"
# # dataset2="/Muon0/lrygaard-LLPminiAODv1-1_Run2023D-PromptReco-v2-905bc08224124a8af93cb10065c39aca/USER"
# # datasets="${dataset},${dataset2}"
# parent_dataset="/Muon0/Run2023D-PromptReco-v2/AOD"

# datasets="/Muon0/lrygaard-LLPnanoAODv1_Run2023D-PromptReco-v1-00000000000000000000000000000000/USER"
# parent_dataset="/Muon0/Run2023D-PromptReco-v1/AOD"

# datasets="/Muon1/lrygaard-LLPnanoAODv1_Run2023D-PromptReco-v1-00000000000000000000000000000000/USER"
# parent_dataset="/Muon1/Run2023D-PromptReco-v1/AOD"

# datasets="/Muon1/lrygaard-LLPminiAODv1_Run2023D-PromptReco-v2-905bc08224124a8af93cb10065c39aca/USER"
# parent_dataset="/Muon1/Run2023D-PromptReco-v2/AOD"

# datasets="/Muon1/lrygaard-LLPnanoAODv1_Run2023D-PromptReco-v2-00000000000000000000000000000000/USER"
# parent_dataset="/Muon1/Run2023D-PromptReco-v2/AOD"

# datasets="/Muon0/lrygaard-LLPnanoAODv1_Run2023D-PromptReco-v2-00000000000000000000000000000000/USER"
# parent_dataset="/Muon0/Run2023D-PromptReco-v2/NANOAOD"

# golden_json_path="Cert_Collisions2023_366442_370790_Golden.json"

# make datasets list:
# datasets="${dataset},${dataset2}"

python_script="get_missing_lumis_for_dataset.py"  

python "$python_script" "$datasets" "$parent_dataset" "$golden_json_path"