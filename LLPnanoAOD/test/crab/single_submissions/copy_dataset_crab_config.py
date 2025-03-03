from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferLogs = False
config.General.requestName = 'LLPnanoAODv1_2016_TTToSemileptonic'
config.General.transferOutputs = True
config.General.workArea = '/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_13_0_20/src/LLPNanoAOD/LLPnanoAOD/test/crab/crab_projects/crab_copy_dataset'
config.section_('JobType')
config.JobType.maxMemoryMB = 1000
config.JobType.numCores = 4
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxJobRuntimeMin = 2750
config.JobType.pluginName = 'Analysis'
config.JobType.sendExternalFolder = False
config.JobType.psetName = '/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_13_0_20/src/LLPNanoAOD/LLPnanoAOD/test/LLPnanoAOD_copy_dataset.py'
config.section_('Data')
config.Data.unitsPerJob = 1
config.Data.userInputFiles = open('/afs/desy.de/user/l/lrygaard/TTALP/CMSSW_10_6_29/src/LLPNanoAOD/LLPnanoAOD/test/crab/file_inputs/TTToSemiLeptonic_LLPnanoAODv1_LLPminiAOD_2016.txt').readlines()
config.Data.outputDatasetTag = 'LLPnanoAODv1_RunIISummer20UL16RECO-106X_v13-v2'
config.Data.outputPrimaryDataset = 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8'
config.Data.outLFNDirBase = '/store/user/lrygaard/ttalps'
config.Data.allowNonValidInputDataset = False
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.publication = True
config.section_('Site')
config.Site.storageSite = 'T2_DE_DESY'
config.section_('User')
config.section_('Debug')