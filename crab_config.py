import os
from CRABClient.UserUtilities import config, getUsernameFromSiteDB

N_PU = 20
maxtime = '10h'
st_seed = 0
njobs = 1000

###### Define the process name here only once ####################
# process_name = 'BPH_Tag-Probe_B0_JpsiKst-mumuKpi-kp_13TeV-pythia8_Hardbbbar_PTFilter5_0p0-evtgen_SVV'
# nev = 300000

process_name = 'BPH_Tag-Probe_B0_JpsiKst-mumuKpi-kp_13TeV-pythia8_SoftQCD_PTFilter5_0p0-evtgen_SVV'
nev = 50000

# process_name = 'BPH_Tag-B0_DmstHc-pD0bar-kp-Hc2mu_13TeV-pythia8_Hardbbbar_PTFilter5_0p0-evtgen'
# nev = 500000

import datetime
currentDT = str(datetime.datetime.now())
str2tail = '  '.join([currentDT, process_name, 'st_seed='+str(st_seed), 'n_ev='+str(nev), 'n_jobs='+str(njobs), 'maxtime='+str(maxtime)])
os.system('echo "{}" >> generationLog.txt'.format(str2tail))

time_scale = {'m':1, 'h':60, 'd':60*24}

config = config()

config.General.requestName     = process_name
config.General.workArea        = 'tmp'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'placeholder_cfg.py'
#These files will be placed in the starting directory
config.JobType.inputFiles = ['Configuration/GenProduction/python/{}_cfi.py'.format(process_name), 'job1023_gen_v1.sh']
# config.JobType.outputFiles = []
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 4000
config.JobType.maxJobRuntimeMin = int(maxtime[:-1]) * time_scale[maxtime[-1]]
config.JobType.scriptExe = 'crab_job.sh'
config.JobType.scriptArgs = ['nev='+str(nev), 'st_seed='+str(st_seed), 'process_name='+process_name, 'N_PU='+str(N_PU)]

config.Data.outputPrimaryDataset = 'cmsMC_private'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 10 #placeholder
config.Data.totalUnits           = njobs * config.Data.unitsPerJob
config.Data.publication          = True
config.Data.outputDatasetTag     = process_name

config.Site.storageSite = 'T2_US_Caltech'
config.Site.blacklist = ['T2_EE_*']
