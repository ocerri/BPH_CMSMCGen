import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13000.0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            operates_on_particles = cms.vint32(511),
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring(
"""
Alias      MyD0   D0
Alias      Myanti-D0   anti-D0
ChargeConj MyD0   Myanti-D0
#
Decay MyD0
1.000      K-  pi+                PHSP;
Enddecay
CDecay Myanti-D0
#
#
#
Alias     MyD*-    D*-
Decay MyD*-
1.000      Myanti-D0 pi-          VSS;
Enddecay
#
Decay B0
1.00  MyD*-  pi0   mu+  nu_mu      PHOTOS GOITY_ROBERTS;
Enddecay
#
End
"""
                                            )
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring('HardQCD:hardbbbar = on'),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
    )
)


###### Filters ##########
tagfilter = cms.EDFilter(
    "PythiaDauVFilter",
    ParticleID         = cms.untracked.int32(511),  ## B0
    ChargeConjugation  = cms.untracked.bool(False),
    NumberDaughters    = cms.untracked.int32(4),
    DaughterIDs        = cms.untracked.vint32(-413, 111, -13, 14),
    MinPt              = cms.untracked.vdouble(-1., -1, 6.7, -1.),
    MinEta             = cms.untracked.vdouble(-9999999., -9999, -1.6, -9999999.),
    MaxEta             = cms.untracked.vdouble( 9999999., 9999, 1.6, 9999999.)
)


ProductionFilterSequence = cms.Sequence(generator + tagfilter)
