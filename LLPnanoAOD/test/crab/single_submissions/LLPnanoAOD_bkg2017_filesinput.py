from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.transferOutputs = True
config.General.workArea = '/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src/LLPNanoAOD/LLPnanoAOD/test/crab/crab_projects/crab_bkg_2017_LLPminiAOD_v1'
config.General.requestName = 'W1JetsToLNu_LLPnanoAODv1'
config.section_('JobType')
config.JobType.numCores = 8
config.JobType.sendExternalFolder = False
config.JobType.pyCfgParams = ['nEvents=0', 'runOnData=False', 'nThreads=8', 'year=2017', 'includeDSAMuon=True', 'includeBS=True', 'includeGenPart=True', 'includeDGLMuon=False']
config.JobType.pluginName = 'Analysis'
config.JobType.allowUndistributedCMSSW = True
config.JobType.psetName = '/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src/LLPNanoAOD/LLPnanoAOD/test/LLPnanoAOD_cfg.py'
config.JobType.maxJobRuntimeMin = 2750
config.JobType.maxMemoryMB = 8000
config.section_('Data')
config.Data.outputDatasetTag = 'LLPnanoAODv1_RunIISummer20UL17RECO-106X_v6-v1'
config.Data.outputPrimaryDataset = "W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8"
config.Data.userInputFiles = open('/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src/LLPNanoAOD/LLPnanoAOD/test/crab/file_inputs/W1JetsToLNu_2017_LLPminiAOD_input_example.txt').readlines()
config.Data.publication = True
config.Data.unitsPerJob = 1
config.Data.ignoreLocality = True
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.allowNonValidInputDataset = False
config.Data.outLFNDirBase = '/store/user/lrygaard/ttalps'
config.section_('Site')
config.Site.whitelist = ['T2_CH_*', 'T2_IT_*', 'T2_FR_*', 'T2_DE_*', 'T2_ES_*', 'T2_UK_*']
config.Site.storageSite = 'T2_DE_DESY'
config.section_('User')
config.section_('Debug')
