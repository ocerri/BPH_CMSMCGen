import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
	maxEventsToPrint = cms.untracked.int32(1),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	filterEfficiency = cms.untracked.double(0.00300),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	comEnergy = cms.double(13000.0),

	crossSection = cms.untracked.double(1.27319e+09),

	PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CP5SettingsBlock,
	        processParameters = cms.vstring(
            		'ParticleDecays:limitTau0 = off',
			        'ParticleDecays:limitCylinder = on',
            		'ParticleDecays:xyMax = 2000',
            		'ParticleDecays:zMax = 4000',
			        'HardQCD:all = on',
			        'PhaseSpace:pTHatMin = 15',
			        'PhaseSpace:pTHatMax = 20',
           		    '130:mayDecay = on',
            		'211:mayDecay = on',
            		'321:mayDecay = on'
	        ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CP5Settings',
                                        'processParameters',
           )
	)
)


mugenfilter = cms.EDFilter("MCSmartSingleParticleFilter",
                           MinPt = cms.untracked.vdouble(5.,5.),
                           MinEta = cms.untracked.vdouble(-2.5,-2.5),
                           MaxEta = cms.untracked.vdouble(2.5,2.5),
                           ParticleID = cms.untracked.vint32(13,-13),
                           Status = cms.untracked.vint32(1,1),
                           # Decay cuts are in mm
                           MaxDecayRadius = cms.untracked.vdouble(2000.,2000.),
                           MinDecayZ = cms.untracked.vdouble(-4000.,-4000.),
                           MaxDecayZ = cms.untracked.vdouble(4000.,4000.)
)


configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\$Revision$'),
    name = cms.untracked.string('\$Source$'),
    annotation = cms.untracked.string('QCD dijet production, pThat 15to20 GeV, with INCLUSIVE muon preselection (pt(mu) > 5 GeV), 13 TeV, TuneCP5')
)

ProductionFilterSequence = cms.Sequence(generator*mugenfilter)