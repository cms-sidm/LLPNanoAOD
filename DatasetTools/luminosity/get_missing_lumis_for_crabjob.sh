
user_path=/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src/LLPNanoAOD/DatasetTools/luminosity

# input_path=${user_path}/crab_projects/crab_data_2018_AOD_v1D/crab_SingleMuonDD_LLPminiAODv1D
# dataset=/SingleMuon/lrygaard-LLPminiAODv1D_Run2018D-12Nov2019_UL2018-v8-9cdbfc999b77f606d32dabc67655eebd/USER
# parent_dataset=/SingleMuon/Run2018D-12Nov2019_UL2018-v8/AOD

# input_path=${user_path}/crab_projects/crab_data_2017_AOD_v1/crab_SingleMuonD_LLPminiAODv1/
# dataset=/SingleMuon/lrygaard-LLPminiAODv1_Run2017D-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER
# parent_dataset=/SingleMuon/Run2017D-09Aug2019_UL2017-v1/AOD

# input_path=${user_path}/crab_projects/crab_data_2017_AOD_v1/crab_SingleMuonE_LLPminiAODv1/
# dataset=/SingleMuon/lrygaard-LLPminiAODv1_Run2017E-09Aug2019_UL2017-v1-bd7ae54c8e86ee21fea83cba264cd4d4/USER
# parent_dataset=/SingleMuon/Run2017E-09Aug2019_UL2017-v1/AOD

# input_path=${user_path}/crab_projects/crab_data_2016HIPM_AOD_v1/crab_SingleMuonBver2_LLPminiAODv1/
# dataset=/SingleMuon/lrygaard-LLPminiAODv1_Run2016B-21Feb2020_ver2_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER
# parent_dataset=/SingleMuon/Run2016B-21Feb2020_ver2_UL2016_HIPM-v1/AOD

# input_path=${user_path}/crab_projects/crab_data_2016HIPM_AOD_v1/crab_SingleMuonD_LLPminiAODv1
# dataset=/SingleMuon/lrygaard-LLPminiAODv1_Run2016D-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER
# parent_dataset=/SingleMuon/Run2016D-21Feb2020_UL2016_HIPM-v1/AOD

# input_path=${user_path}/crab_projects/crab_data_2016HIPM_AOD_v1/crab_SingleMuonF_LLPminiAODv1
# dataset=/SingleMuon/lrygaard-LLPminiAODv1_Run2016F-21Feb2020_UL2016_HIPM-v1-4d5adf68ed2927ce6cdc8fbe20819cac/USER
# parent_dataset=/SingleMuon/Run2016F-21Feb2020_UL2016_HIPM-v1/AOD

# input_path=${user_path}/crab_projects/crab_data_2016_AOD_v1/crab_SingleMuonF_LLPminiAODv1
# dataset=/SingleMuon/lrygaard-LLPminiAODv1_Run2016F-21Feb2020_UL2016-v1-e8b05bf423a072ce8e514b113ad393f0/USER
# parent_dataset=/SingleMuon/Run2016F-21Feb2020_UL2016-v1/AOD

input_path=${user_path}/crab_projects/crab_data_2016_AOD_v1/crab_SingleMuonG_LLPminiAODv1
dataset=/SingleMuon/lrygaard-LLPminiAODv1_Run2016G-21Feb2020_UL2016-v1-e8b05bf423a072ce8e514b113ad393f0/USER
parent_dataset=/SingleMuon/Run2016G-21Feb2020_UL2016-v1/AOD


python ${user_path}/get_missing_lumis_for_crabjob.py ${input_path} ${dataset} ${parent_dataset}