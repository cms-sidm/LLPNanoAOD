import FWCore.ParameterSet.Config as cms

process = cms.Process("COPY")

process.options = cms.untracked.PSet(
    numberOfThreads = cms.untracked.uint32(4),  # Enable 4 threads
    numberOfStreams = cms.untracked.uint32(4)   # Use 4 parallel streams
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring()  # CRAB will override this with userInputFiles
)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("dummy.root")  # Won't actually be used
)

process.endpath = cms.EndPath(process.out)
