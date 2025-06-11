#!/bin/bash


# File with sample list
INPUT=$1

if [ -z "$INPUT" ]; then
    echo "Missing input argument."
    exit 1
fi
filename=$(basename "$INPUT" .conf)

# Paths
crabWorkspace=$CMSSW_BASE/src/LLPNanoAOD/LLPnanoAOD/test/crab
configWorkspace=$CMSSW_BASE/src/LLPNanoAOD/LLPnanoAOD/test

runFile=LLPnanoAOD_cfg.py

source /cvmfs/cms.cern.ch/common/crab-setup.sh

nCores=8
maxMemory=$((500 * $nCores))
maxRuntime=2750
filePerJob=0
VERSION=1

whitelist="['T2_CH_*','T2_IT_*','T2_US_*','T2_FR_*','T2_DE_*','T2_ES_*','T2_UK_*']"

# Year options for MC: 2016, 2016PreVFP, 2017, 2018, 2022PreEE, 2022PostEE, 2023PreBPix, 2023PostBPix
# Year options for data: 2016HIPM, 2016 (no HIPM), 2017, 2018, 2022ReReco, 2022Prompt, 2023
year=2017

# json='https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt'
# json='https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
# json='https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
# json='https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_355100_362760_Golden.json'
# json='https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions23/Cert_Collisions2023_366442_370790_Golden.json'

python $crabWorkspace/crab.py \
-p $configWorkspace/$runFile \
--site T2_DE_DESY \
-o /store/user/$USER/ttalps \
-t LLPnanoAODv$VERSION \
-i $INPUT \
-s FileBased \
-n $filePerJob \
--num-cores $nCores \
--max-memory $maxMemory \
--max-runtime-min $maxRuntime \
--work-area $crabWorkspace/crab_projects/crab_${filename}_v$VERSION \
--includeDSAMuon \
--includeBS \
--includeGenPart \
--input-DBS 'phys03' \
--publication \
--year $year \
--ignore_locality \
--whitelist "$whitelist" \
--dryrun \
# --json "$json" \
# --runOnData \
# --includeDGLMuon \
# --set-input-dataset \
#--send-external \
