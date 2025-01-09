# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: signal -s PAT,NANO --mc --conditions 130X_mcRun3_2022_realistic_postEE_v6 --era Run3 --eventcontent NANOAOD --datatier NANOAOD --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000 -n 100 --no_exec
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

# Input arguments
options = VarParsing('analysis')
options.register('nEvents',
                    100,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.int,
                    "Number of events to process"
                )
options.register('runOnData',
                    False,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "If running on data"
                )
options.register('includeDSAMuon',
                    False,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "Flag to include Displaced StandAlone muon information"
                )
options.register('includeBS',
                    False,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "Flag to include BeamSpot information"
                )
options.register('includeGenPart',
                    False,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "Flag to include extended GenPart information"
                )
options.register('includeDGLMuon',
                    False,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "Flag to include Displaced GLobal Muon information"
                )
options.register('includeRefittedTracks',
                    False,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.bool,
                    "Flag to include Refitted Tracks information of Muon Vertex fits"
                )
options.register('nThreads',
                    1,
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.int,
                    "Number of threads to use"
                )
options.register('year',
                    "2022PostEE",
                    VarParsing.multiplicity.singleton,
                    VarParsing.varType.string,
                    "Year of the dataset"
                )
options.parseArguments()

runRefittedTracks_=options.includeRefittedTracks
nevents = options.nEvents
if nevents == 0:
    nevents=-1
    
print('Running LLPnanoAOD_Run3_cfg.py')
print('-- Running on '+str(nevents)+' number of events')
if options.runOnData:
    print('-- Running on data')
else:
    print('-- Running on mc')

if options.runOnData:
    if options.year == "2022ReReco":
        process = cms.Process('NANO',Run3)
    if options.year == "2022Prompt":
        process = cms.Process('NANO',Run3)
    if options.year == "2023":
        process = cms.Process('NANO',Run3_2023)
        
else:
    if options.year == "2022PreEE":
        process = cms.Process('NANO',Run3)
    if options.year == "2022PostEE":
        process = cms.Process('NANO',Run3)
    if options.year == "2023PreBPix":
        process = cms.Process('NANO',Run3_2023)
    if options.year == "2023PostBPix":
        process = cms.Process('NANO',Run3_2023) 

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
process.load('TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi')

if not options.runOnData:
    process.load('SimGeneral.MixingModule.mixNoPU_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(nevents),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(options.nThreads),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string(f'PAT_NANO nevts:{nevents}'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

datatier = 'NANOAOD'
outputcommands = process.NANOAODSIMEventContent.outputCommands
if options.runOnData:
    datatier = 'NANOAODSIM'
    outputcommands = process.NANOAODEventContent.outputCommands

process.NANOAODoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(datatier),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(f'file:{options.outputFile}'),
    outputCommands = outputcommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
globalTag = ""
if options.runOnData:
    if options.year == "2022ReReco":
        globalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_v2', '')
    if options.year == "2022Prompt":
        globalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_PromptAnalysis_v1', '')
    if options.year == "2023":
        globalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_PromptAnalysis_v1', '')
else:
    if options.year == "2022PreEE":
        globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2022_realistic_v5', '')
    if options.year == "2022PostEE":
        globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2022_realistic_postEE_v6', '')
    if options.year == "2023PreBPix":
        globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_v14', '')
    if options.year == "2023PostBPix":
        globalTag = GlobalTag(process.GlobalTag, '130X_mcRun3_2023_realistic_postBPix_v2', '')
process.GlobalTag = globalTag


# LLPnanoAOD custom producers
from TrackPropagation.SteppingHelixPropagator.SteppingHelixPropagatorAny_cfi import *
from TrackingTools.TransientTrack.TransientTrackBuilder_cfi import *

# DisplacedStandAlone (DSA) Muon table
process.dSAMuonsTable = cms.EDProducer("DSAMuonTableProducer",
    dsaMuons=cms.InputTag("displacedStandAloneMuons"),
    muons=cms.InputTag("linkedObjects","muons"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    beamspot = cms.InputTag("offlineBeamSpot")
)
# DisplacedGLobal (DGL) Muon table
process.dGlMuonsTable = cms.EDProducer("DGLMuonTableProducer",
    dglMuons=cms.InputTag("displacedGlobalMuons"),
    muons=cms.InputTag("linkedObjects","muons"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    beamspot = cms.InputTag("offlineBeamSpot")
)
# BeamSpot table
process.beamSpotTable = cms.EDProducer("BeamSpotTableProducer",
    beamSpot = cms.InputTag("offlineBeamSpot")
)
# GenPart table
process.genPartExtendedTable = cms.EDProducer("GenParticlesExtendedTableProducer",
    genparticles = cms.InputTag("finalGenParticles")
)
# Vertex between two muons (pat-pat, pat-dsa or dsa-dsa)
process.muonVertexTable = cms.EDProducer("MuonVertexTableProducer",
    dsaMuons=cms.InputTag("displacedStandAloneMuons"),
    patMuons=cms.InputTag("linkedObjects","muons"),
    beamspot=cms.InputTag("offlineBeamSpot"),
    generalTracks=cms.InputTag("generalTracks"),
    primaryVertex=cms.InputTag("offlineSlimmedPrimaryVertices")
    # runRefittedTracks=cms.bool(runRefittedTracks_)
)
# Vertex between two muons (pat-pat, pat-dgl or dgl-dgl)
process.dGlMuonVertexTable = cms.EDProducer("MuonVertexTableProducer",
    dsaMuons=cms.InputTag("displacedGlobalMuons"),
    patMuons=cms.InputTag("linkedObjects","muons"),
    beamspot=cms.InputTag("offlineBeamSpot"),
    generalTracks=cms.InputTag("generalTracks"),
    primaryVertex=cms.InputTag("offlineSlimmedPrimaryVertices")
    # runRefittedTracks=cms.bool(runRefittedTracks_)
)
# LLPnanoAOD Muon extended table
process.muonExtendedTable = cms.EDProducer("MuonExtendedTableProducer",
    name=cms.string("Muon"),
    muons=cms.InputTag("linkedObjects","muons"),
    dsaMuons=cms.InputTag("displacedStandAloneMuons"),
    primaryVertex=cms.InputTag("offlineSlimmedPrimaryVertices"),
    beamspot=cms.InputTag("offlineBeamSpot"),
    generalTracks=cms.InputTag("generalTracks")
)

# Path and EndPath definitions

process.nanoAOD_step = cms.Path(process.nanoSequenceMC)

if options.runOnData:
    process.nanoAOD_step = cms.Path(process.nanoSequence)
else:
    process.nanoAOD_step = cms.Path(process.nanoSequenceMC)

if options.includeDSAMuon:
    process.nanoAOD_step += process.dSAMuonsTable
    process.nanoAOD_step += process.muonExtendedTable
    process.nanoAOD_step += process.muonVertexTable
if options.includeDGLMuon:
    process.nanoAOD_step += process.dGlMuonsTable
    process.nanoAOD_step += process.dGlMuonVertexTable
if options.includeBS:
    process.nanoAOD_step += process.beamSpotTable
if options.includeGenPart and not options.runOnData:
    process.nanoAOD_step += process.genPartExtendedTable

process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_BadPFMuonDzFilter = cms.Path(process.BadPFMuonDzFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_hfNoisyHitsFilter = cms.Path(process.hfNoisyHitsFilter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadPFMuonDzFilter,process.Flag_hfNoisyHitsFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.nanoAOD_step,process.endjob_step,process.NANOAODoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeCommon 

#call to customisation function nanoAOD_customizeCommon imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeCommon(process)

# End of customisation functions

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=1000
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
