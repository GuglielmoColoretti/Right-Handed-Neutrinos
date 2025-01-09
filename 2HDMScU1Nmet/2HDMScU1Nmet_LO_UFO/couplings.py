# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 9 Jan 2025 17:47:22


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'cx*complex(0,1)*gp',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(AH2*complex(0,1)*Rcp1x2)',
                 order = {'HA':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*GH2*Rcp1x2)',
                 order = {'HG':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-(G*GH2*Rcp1x2)',
                 order = {'HG':1,'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*G**2*GH2*Rcp1x2',
                 order = {'HG':1,'QCD':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-3*complex(0,1)*lam1*Rcp1x1**4 - 6*complex(0,1)*lamd*Rcp1x1**2*Rcp1x2**2 - 6*complex(0,1)*lamm*Rcp1x1**2*Rcp1x2**2 - 3*complex(0,1)*lam2*Rcp1x2**4 - 6*complex(0,1)*lam1s*Rcp1x1**2*Rcp1x3**2 - 6*complex(0,1)*lam2s*Rcp1x2**2*Rcp1x3**2 - 3*complex(0,1)*lams*Rcp1x3**4',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(AH1*complex(0,1)*Rcp2x2)',
                 order = {'HA':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(complex(0,1)*GH1*Rcp2x2)',
                 order = {'HG':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(G*GH1*Rcp2x2)',
                 order = {'HG':1,'QCD':1})

GC_18 = Coupling(name = 'GC_18',
                 value = 'complex(0,1)*G**2*GH1*Rcp2x2',
                 order = {'HG':1,'QCD':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '-3*complex(0,1)*lam1*Rcp1x1**3*Rcp2x1 - 3*complex(0,1)*lamd*Rcp1x1*Rcp1x2**2*Rcp2x1 - 3*complex(0,1)*lamm*Rcp1x1*Rcp1x2**2*Rcp2x1 - 3*complex(0,1)*lam1s*Rcp1x1*Rcp1x3**2*Rcp2x1 - 3*complex(0,1)*lamd*Rcp1x1**2*Rcp1x2*Rcp2x2 - 3*complex(0,1)*lamm*Rcp1x1**2*Rcp1x2*Rcp2x2 - 3*complex(0,1)*lam2*Rcp1x2**3*Rcp2x2 - 3*complex(0,1)*lam2s*Rcp1x2*Rcp1x3**2*Rcp2x2 - 3*complex(0,1)*lam1s*Rcp1x1**2*Rcp1x3*Rcp2x3 - 3*complex(0,1)*lam2s*Rcp1x2**2*Rcp1x3*Rcp2x3 - 3*complex(0,1)*lams*Rcp1x3**3*Rcp2x3',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-3*complex(0,1)*lam1*Rcp1x1**2*Rcp2x1**2 - complex(0,1)*lamd*Rcp1x2**2*Rcp2x1**2 - complex(0,1)*lamm*Rcp1x2**2*Rcp2x1**2 - complex(0,1)*lam1s*Rcp1x3**2*Rcp2x1**2 - 4*complex(0,1)*lamd*Rcp1x1*Rcp1x2*Rcp2x1*Rcp2x2 - 4*complex(0,1)*lamm*Rcp1x1*Rcp1x2*Rcp2x1*Rcp2x2 - complex(0,1)*lamd*Rcp1x1**2*Rcp2x2**2 - complex(0,1)*lamm*Rcp1x1**2*Rcp2x2**2 - 3*complex(0,1)*lam2*Rcp1x2**2*Rcp2x2**2 - complex(0,1)*lam2s*Rcp1x3**2*Rcp2x2**2 - 4*complex(0,1)*lam1s*Rcp1x1*Rcp1x3*Rcp2x1*Rcp2x3 - 4*complex(0,1)*lam2s*Rcp1x2*Rcp1x3*Rcp2x2*Rcp2x3 - complex(0,1)*lam1s*Rcp1x1**2*Rcp2x3**2 - complex(0,1)*lam2s*Rcp1x2**2*Rcp2x3**2 - 3*complex(0,1)*lams*Rcp1x3**2*Rcp2x3**2',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-3*complex(0,1)*lam1*Rcp1x1*Rcp2x1**3 - 3*complex(0,1)*lamd*Rcp1x2*Rcp2x1**2*Rcp2x2 - 3*complex(0,1)*lamm*Rcp1x2*Rcp2x1**2*Rcp2x2 - 3*complex(0,1)*lamd*Rcp1x1*Rcp2x1*Rcp2x2**2 - 3*complex(0,1)*lamm*Rcp1x1*Rcp2x1*Rcp2x2**2 - 3*complex(0,1)*lam2*Rcp1x2*Rcp2x2**3 - 3*complex(0,1)*lam1s*Rcp1x3*Rcp2x1**2*Rcp2x3 - 3*complex(0,1)*lam2s*Rcp1x3*Rcp2x2**2*Rcp2x3 - 3*complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Rcp2x3**2 - 3*complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Rcp2x3**2 - 3*complex(0,1)*lams*Rcp1x3*Rcp2x3**3',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-3*complex(0,1)*lam1*Rcp2x1**4 - 6*complex(0,1)*lamd*Rcp2x1**2*Rcp2x2**2 - 6*complex(0,1)*lamm*Rcp2x1**2*Rcp2x2**2 - 3*complex(0,1)*lam2*Rcp2x2**4 - 6*complex(0,1)*lam1s*Rcp2x1**2*Rcp2x3**2 - 6*complex(0,1)*lam2s*Rcp2x2**2*Rcp2x3**2 - 3*complex(0,1)*lams*Rcp2x3**4',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(AH3*complex(0,1)*Rcp3x2)',
                 order = {'HA':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(complex(0,1)*GH3*Rcp3x2)',
                 order = {'HG':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(G*GH3*Rcp3x2)',
                 order = {'HG':1,'QCD':1})

GC_26 = Coupling(name = 'GC_26',
                 value = 'complex(0,1)*G**2*GH3*Rcp3x2',
                 order = {'HG':1,'QCD':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-3*complex(0,1)*lam1*Rcp1x1**3*Rcp3x1 - 3*complex(0,1)*lamd*Rcp1x1*Rcp1x2**2*Rcp3x1 - 3*complex(0,1)*lamm*Rcp1x1*Rcp1x2**2*Rcp3x1 - 3*complex(0,1)*lam1s*Rcp1x1*Rcp1x3**2*Rcp3x1 - 3*complex(0,1)*lamd*Rcp1x1**2*Rcp1x2*Rcp3x2 - 3*complex(0,1)*lamm*Rcp1x1**2*Rcp1x2*Rcp3x2 - 3*complex(0,1)*lam2*Rcp1x2**3*Rcp3x2 - 3*complex(0,1)*lam2s*Rcp1x2*Rcp1x3**2*Rcp3x2 - 3*complex(0,1)*lam1s*Rcp1x1**2*Rcp1x3*Rcp3x3 - 3*complex(0,1)*lam2s*Rcp1x2**2*Rcp1x3*Rcp3x3 - 3*complex(0,1)*lams*Rcp1x3**3*Rcp3x3',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-3*complex(0,1)*lam1*Rcp1x1**2*Rcp2x1*Rcp3x1 - complex(0,1)*lamd*Rcp1x2**2*Rcp2x1*Rcp3x1 - complex(0,1)*lamm*Rcp1x2**2*Rcp2x1*Rcp3x1 - complex(0,1)*lam1s*Rcp1x3**2*Rcp2x1*Rcp3x1 - 2*complex(0,1)*lamd*Rcp1x1*Rcp1x2*Rcp2x2*Rcp3x1 - 2*complex(0,1)*lamm*Rcp1x1*Rcp1x2*Rcp2x2*Rcp3x1 - 2*complex(0,1)*lam1s*Rcp1x1*Rcp1x3*Rcp2x3*Rcp3x1 - 2*complex(0,1)*lamd*Rcp1x1*Rcp1x2*Rcp2x1*Rcp3x2 - 2*complex(0,1)*lamm*Rcp1x1*Rcp1x2*Rcp2x1*Rcp3x2 - complex(0,1)*lamd*Rcp1x1**2*Rcp2x2*Rcp3x2 - complex(0,1)*lamm*Rcp1x1**2*Rcp2x2*Rcp3x2 - 3*complex(0,1)*lam2*Rcp1x2**2*Rcp2x2*Rcp3x2 - complex(0,1)*lam2s*Rcp1x3**2*Rcp2x2*Rcp3x2 - 2*complex(0,1)*lam2s*Rcp1x2*Rcp1x3*Rcp2x3*Rcp3x2 - 2*complex(0,1)*lam1s*Rcp1x1*Rcp1x3*Rcp2x1*Rcp3x3 - 2*complex(0,1)*lam2s*Rcp1x2*Rcp1x3*Rcp2x2*Rcp3x3 - complex(0,1)*lam1s*Rcp1x1**2*Rcp2x3*Rcp3x3 - complex(0,1)*lam2s*Rcp1x2**2*Rcp2x3*Rcp3x3 - 3*complex(0,1)*lams*Rcp1x3**2*Rcp2x3*Rcp3x3',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-3*complex(0,1)*lam1*Rcp1x1*Rcp2x1**2*Rcp3x1 - 2*complex(0,1)*lamd*Rcp1x2*Rcp2x1*Rcp2x2*Rcp3x1 - 2*complex(0,1)*lamm*Rcp1x2*Rcp2x1*Rcp2x2*Rcp3x1 - complex(0,1)*lamd*Rcp1x1*Rcp2x2**2*Rcp3x1 - complex(0,1)*lamm*Rcp1x1*Rcp2x2**2*Rcp3x1 - 2*complex(0,1)*lam1s*Rcp1x3*Rcp2x1*Rcp2x3*Rcp3x1 - complex(0,1)*lam1s*Rcp1x1*Rcp2x3**2*Rcp3x1 - complex(0,1)*lamd*Rcp1x2*Rcp2x1**2*Rcp3x2 - complex(0,1)*lamm*Rcp1x2*Rcp2x1**2*Rcp3x2 - 2*complex(0,1)*lamd*Rcp1x1*Rcp2x1*Rcp2x2*Rcp3x2 - 2*complex(0,1)*lamm*Rcp1x1*Rcp2x1*Rcp2x2*Rcp3x2 - 3*complex(0,1)*lam2*Rcp1x2*Rcp2x2**2*Rcp3x2 - 2*complex(0,1)*lam2s*Rcp1x3*Rcp2x2*Rcp2x3*Rcp3x2 - complex(0,1)*lam2s*Rcp1x2*Rcp2x3**2*Rcp3x2 - complex(0,1)*lam1s*Rcp1x3*Rcp2x1**2*Rcp3x3 - complex(0,1)*lam2s*Rcp1x3*Rcp2x2**2*Rcp3x3 - 2*complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Rcp2x3*Rcp3x3 - 2*complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Rcp2x3*Rcp3x3 - 3*complex(0,1)*lams*Rcp1x3*Rcp2x3**2*Rcp3x3',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '-3*complex(0,1)*lam1*Rcp2x1**3*Rcp3x1 - 3*complex(0,1)*lamd*Rcp2x1*Rcp2x2**2*Rcp3x1 - 3*complex(0,1)*lamm*Rcp2x1*Rcp2x2**2*Rcp3x1 - 3*complex(0,1)*lam1s*Rcp2x1*Rcp2x3**2*Rcp3x1 - 3*complex(0,1)*lamd*Rcp2x1**2*Rcp2x2*Rcp3x2 - 3*complex(0,1)*lamm*Rcp2x1**2*Rcp2x2*Rcp3x2 - 3*complex(0,1)*lam2*Rcp2x2**3*Rcp3x2 - 3*complex(0,1)*lam2s*Rcp2x2*Rcp2x3**2*Rcp3x2 - 3*complex(0,1)*lam1s*Rcp2x1**2*Rcp2x3*Rcp3x3 - 3*complex(0,1)*lam2s*Rcp2x2**2*Rcp2x3*Rcp3x3 - 3*complex(0,1)*lams*Rcp2x3**3*Rcp3x3',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-3*complex(0,1)*lam1*Rcp1x1**2*Rcp3x1**2 - complex(0,1)*lamd*Rcp1x2**2*Rcp3x1**2 - complex(0,1)*lamm*Rcp1x2**2*Rcp3x1**2 - complex(0,1)*lam1s*Rcp1x3**2*Rcp3x1**2 - 4*complex(0,1)*lamd*Rcp1x1*Rcp1x2*Rcp3x1*Rcp3x2 - 4*complex(0,1)*lamm*Rcp1x1*Rcp1x2*Rcp3x1*Rcp3x2 - complex(0,1)*lamd*Rcp1x1**2*Rcp3x2**2 - complex(0,1)*lamm*Rcp1x1**2*Rcp3x2**2 - 3*complex(0,1)*lam2*Rcp1x2**2*Rcp3x2**2 - complex(0,1)*lam2s*Rcp1x3**2*Rcp3x2**2 - 4*complex(0,1)*lam1s*Rcp1x1*Rcp1x3*Rcp3x1*Rcp3x3 - 4*complex(0,1)*lam2s*Rcp1x2*Rcp1x3*Rcp3x2*Rcp3x3 - complex(0,1)*lam1s*Rcp1x1**2*Rcp3x3**2 - complex(0,1)*lam2s*Rcp1x2**2*Rcp3x3**2 - 3*complex(0,1)*lams*Rcp1x3**2*Rcp3x3**2',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-3*complex(0,1)*lam1*Rcp1x1*Rcp2x1*Rcp3x1**2 - complex(0,1)*lamd*Rcp1x2*Rcp2x2*Rcp3x1**2 - complex(0,1)*lamm*Rcp1x2*Rcp2x2*Rcp3x1**2 - complex(0,1)*lam1s*Rcp1x3*Rcp2x3*Rcp3x1**2 - 2*complex(0,1)*lamd*Rcp1x2*Rcp2x1*Rcp3x1*Rcp3x2 - 2*complex(0,1)*lamm*Rcp1x2*Rcp2x1*Rcp3x1*Rcp3x2 - 2*complex(0,1)*lamd*Rcp1x1*Rcp2x2*Rcp3x1*Rcp3x2 - 2*complex(0,1)*lamm*Rcp1x1*Rcp2x2*Rcp3x1*Rcp3x2 - complex(0,1)*lamd*Rcp1x1*Rcp2x1*Rcp3x2**2 - complex(0,1)*lamm*Rcp1x1*Rcp2x1*Rcp3x2**2 - 3*complex(0,1)*lam2*Rcp1x2*Rcp2x2*Rcp3x2**2 - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*Rcp3x2**2 - 2*complex(0,1)*lam1s*Rcp1x3*Rcp2x1*Rcp3x1*Rcp3x3 - 2*complex(0,1)*lam1s*Rcp1x1*Rcp2x3*Rcp3x1*Rcp3x3 - 2*complex(0,1)*lam2s*Rcp1x3*Rcp2x2*Rcp3x2*Rcp3x3 - 2*complex(0,1)*lam2s*Rcp1x2*Rcp2x3*Rcp3x2*Rcp3x3 - complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Rcp3x3**2 - complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Rcp3x3**2 - 3*complex(0,1)*lams*Rcp1x3*Rcp2x3*Rcp3x3**2',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-3*complex(0,1)*lam1*Rcp2x1**2*Rcp3x1**2 - complex(0,1)*lamd*Rcp2x2**2*Rcp3x1**2 - complex(0,1)*lamm*Rcp2x2**2*Rcp3x1**2 - complex(0,1)*lam1s*Rcp2x3**2*Rcp3x1**2 - 4*complex(0,1)*lamd*Rcp2x1*Rcp2x2*Rcp3x1*Rcp3x2 - 4*complex(0,1)*lamm*Rcp2x1*Rcp2x2*Rcp3x1*Rcp3x2 - complex(0,1)*lamd*Rcp2x1**2*Rcp3x2**2 - complex(0,1)*lamm*Rcp2x1**2*Rcp3x2**2 - 3*complex(0,1)*lam2*Rcp2x2**2*Rcp3x2**2 - complex(0,1)*lam2s*Rcp2x3**2*Rcp3x2**2 - 4*complex(0,1)*lam1s*Rcp2x1*Rcp2x3*Rcp3x1*Rcp3x3 - 4*complex(0,1)*lam2s*Rcp2x2*Rcp2x3*Rcp3x2*Rcp3x3 - complex(0,1)*lam1s*Rcp2x1**2*Rcp3x3**2 - complex(0,1)*lam2s*Rcp2x2**2*Rcp3x3**2 - 3*complex(0,1)*lams*Rcp2x3**2*Rcp3x3**2',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '-3*complex(0,1)*lam1*Rcp1x1*Rcp3x1**3 - 3*complex(0,1)*lamd*Rcp1x2*Rcp3x1**2*Rcp3x2 - 3*complex(0,1)*lamm*Rcp1x2*Rcp3x1**2*Rcp3x2 - 3*complex(0,1)*lamd*Rcp1x1*Rcp3x1*Rcp3x2**2 - 3*complex(0,1)*lamm*Rcp1x1*Rcp3x1*Rcp3x2**2 - 3*complex(0,1)*lam2*Rcp1x2*Rcp3x2**3 - 3*complex(0,1)*lam1s*Rcp1x3*Rcp3x1**2*Rcp3x3 - 3*complex(0,1)*lam2s*Rcp1x3*Rcp3x2**2*Rcp3x3 - 3*complex(0,1)*lam1s*Rcp1x1*Rcp3x1*Rcp3x3**2 - 3*complex(0,1)*lam2s*Rcp1x2*Rcp3x2*Rcp3x3**2 - 3*complex(0,1)*lams*Rcp1x3*Rcp3x3**3',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-3*complex(0,1)*lam1*Rcp2x1*Rcp3x1**3 - 3*complex(0,1)*lamd*Rcp2x2*Rcp3x1**2*Rcp3x2 - 3*complex(0,1)*lamm*Rcp2x2*Rcp3x1**2*Rcp3x2 - 3*complex(0,1)*lamd*Rcp2x1*Rcp3x1*Rcp3x2**2 - 3*complex(0,1)*lamm*Rcp2x1*Rcp3x1*Rcp3x2**2 - 3*complex(0,1)*lam2*Rcp2x2*Rcp3x2**3 - 3*complex(0,1)*lam1s*Rcp2x3*Rcp3x1**2*Rcp3x3 - 3*complex(0,1)*lam2s*Rcp2x3*Rcp3x2**2*Rcp3x3 - 3*complex(0,1)*lam1s*Rcp2x1*Rcp3x1*Rcp3x3**2 - 3*complex(0,1)*lam2s*Rcp2x2*Rcp3x2*Rcp3x3**2 - 3*complex(0,1)*lams*Rcp2x3*Rcp3x3**3',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '-3*complex(0,1)*lam1*Rcp3x1**4 - 6*complex(0,1)*lamd*Rcp3x1**2*Rcp3x2**2 - 6*complex(0,1)*lamm*Rcp3x1**2*Rcp3x2**2 - 3*complex(0,1)*lam2*Rcp3x2**4 - 6*complex(0,1)*lam1s*Rcp3x1**2*Rcp3x3**2 - 6*complex(0,1)*lam2s*Rcp3x2**2*Rcp3x3**2 - 3*complex(0,1)*lams*Rcp3x3**4',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(complex(0,1)*lam1*Rcp1x1**2*Reta1x1**2) - complex(0,1)*lamd*Rcp1x2**2*Reta1x1**2 - complex(0,1)*lamm*Rcp1x2**2*Reta1x1**2 - complex(0,1)*lam1s*Rcp1x3**2*Reta1x1**2 - complex(0,1)*lamd*Rcp1x1**2*Reta1x2**2 - complex(0,1)*lamm*Rcp1x1**2*Reta1x2**2 - complex(0,1)*lam2*Rcp1x2**2*Reta1x2**2 - complex(0,1)*lam2s*Rcp1x3**2*Reta1x2**2 - complex(0,1)*lam1s*Rcp1x1**2*Reta1x3**2 - complex(0,1)*lam2s*Rcp1x2**2*Reta1x3**2 - complex(0,1)*lams*Rcp1x3**2*Reta1x3**2',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp2x1*Reta1x1**2) - complex(0,1)*lamd*Rcp1x2*Rcp2x2*Reta1x1**2 - complex(0,1)*lamm*Rcp1x2*Rcp2x2*Reta1x1**2 - complex(0,1)*lam1s*Rcp1x3*Rcp2x3*Reta1x1**2 - complex(0,1)*lamd*Rcp1x1*Rcp2x1*Reta1x2**2 - complex(0,1)*lamm*Rcp1x1*Rcp2x1*Reta1x2**2 - complex(0,1)*lam2*Rcp1x2*Rcp2x2*Reta1x2**2 - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*Reta1x2**2 - complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Reta1x3**2 - complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Reta1x3**2 - complex(0,1)*lams*Rcp1x3*Rcp2x3*Reta1x3**2',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(complex(0,1)*lam1*Rcp2x1**2*Reta1x1**2) - complex(0,1)*lamd*Rcp2x2**2*Reta1x1**2 - complex(0,1)*lamm*Rcp2x2**2*Reta1x1**2 - complex(0,1)*lam1s*Rcp2x3**2*Reta1x1**2 - complex(0,1)*lamd*Rcp2x1**2*Reta1x2**2 - complex(0,1)*lamm*Rcp2x1**2*Reta1x2**2 - complex(0,1)*lam2*Rcp2x2**2*Reta1x2**2 - complex(0,1)*lam2s*Rcp2x3**2*Reta1x2**2 - complex(0,1)*lam1s*Rcp2x1**2*Reta1x3**2 - complex(0,1)*lam2s*Rcp2x2**2*Reta1x3**2 - complex(0,1)*lams*Rcp2x3**2*Reta1x3**2',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp3x1*Reta1x1**2) - complex(0,1)*lamd*Rcp1x2*Rcp3x2*Reta1x1**2 - complex(0,1)*lamm*Rcp1x2*Rcp3x2*Reta1x1**2 - complex(0,1)*lam1s*Rcp1x3*Rcp3x3*Reta1x1**2 - complex(0,1)*lamd*Rcp1x1*Rcp3x1*Reta1x2**2 - complex(0,1)*lamm*Rcp1x1*Rcp3x1*Reta1x2**2 - complex(0,1)*lam2*Rcp1x2*Rcp3x2*Reta1x2**2 - complex(0,1)*lam2s*Rcp1x3*Rcp3x3*Reta1x2**2 - complex(0,1)*lam1s*Rcp1x1*Rcp3x1*Reta1x3**2 - complex(0,1)*lam2s*Rcp1x2*Rcp3x2*Reta1x3**2 - complex(0,1)*lams*Rcp1x3*Rcp3x3*Reta1x3**2',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(complex(0,1)*lam1*Rcp2x1*Rcp3x1*Reta1x1**2) - complex(0,1)*lamd*Rcp2x2*Rcp3x2*Reta1x1**2 - complex(0,1)*lamm*Rcp2x2*Rcp3x2*Reta1x1**2 - complex(0,1)*lam1s*Rcp2x3*Rcp3x3*Reta1x1**2 - complex(0,1)*lamd*Rcp2x1*Rcp3x1*Reta1x2**2 - complex(0,1)*lamm*Rcp2x1*Rcp3x1*Reta1x2**2 - complex(0,1)*lam2*Rcp2x2*Rcp3x2*Reta1x2**2 - complex(0,1)*lam2s*Rcp2x3*Rcp3x3*Reta1x2**2 - complex(0,1)*lam1s*Rcp2x1*Rcp3x1*Reta1x3**2 - complex(0,1)*lam2s*Rcp2x2*Rcp3x2*Reta1x3**2 - complex(0,1)*lams*Rcp2x3*Rcp3x3*Reta1x3**2',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(complex(0,1)*lam1*Rcp3x1**2*Reta1x1**2) - complex(0,1)*lamd*Rcp3x2**2*Reta1x1**2 - complex(0,1)*lamm*Rcp3x2**2*Reta1x1**2 - complex(0,1)*lam1s*Rcp3x3**2*Reta1x1**2 - complex(0,1)*lamd*Rcp3x1**2*Reta1x2**2 - complex(0,1)*lamm*Rcp3x1**2*Reta1x2**2 - complex(0,1)*lam2*Rcp3x2**2*Reta1x2**2 - complex(0,1)*lam2s*Rcp3x3**2*Reta1x2**2 - complex(0,1)*lam1s*Rcp3x1**2*Reta1x3**2 - complex(0,1)*lam2s*Rcp3x2**2*Reta1x3**2 - complex(0,1)*lams*Rcp3x3**2*Reta1x3**2',
                 order = {'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '-3*complex(0,1)*lam1*Reta1x1**4 - 6*complex(0,1)*lamd*Reta1x1**2*Reta1x2**2 - 6*complex(0,1)*lamm*Reta1x1**2*Reta1x2**2 - 3*complex(0,1)*lam2*Reta1x2**4 - 6*complex(0,1)*lam1s*Reta1x1**2*Reta1x3**2 - 6*complex(0,1)*lam2s*Reta1x2**2*Reta1x3**2 - 3*complex(0,1)*lams*Reta1x3**4',
                 order = {'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(complex(0,1)*lam1*Rcp1x1**2*Reta1x1*Reta2x1) - complex(0,1)*lamd*Rcp1x2**2*Reta1x1*Reta2x1 - complex(0,1)*lamm*Rcp1x2**2*Reta1x1*Reta2x1 - complex(0,1)*lam1s*Rcp1x3**2*Reta1x1*Reta2x1 - complex(0,1)*lamd*Rcp1x1**2*Reta1x2*Reta2x2 - complex(0,1)*lamm*Rcp1x1**2*Reta1x2*Reta2x2 - complex(0,1)*lam2*Rcp1x2**2*Reta1x2*Reta2x2 - complex(0,1)*lam2s*Rcp1x3**2*Reta1x2*Reta2x2 - complex(0,1)*lam1s*Rcp1x1**2*Reta1x3*Reta2x3 - complex(0,1)*lam2s*Rcp1x2**2*Reta1x3*Reta2x3 - complex(0,1)*lams*Rcp1x3**2*Reta1x3*Reta2x3',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp2x1*Reta1x1*Reta2x1) - complex(0,1)*lamd*Rcp1x2*Rcp2x2*Reta1x1*Reta2x1 - complex(0,1)*lamm*Rcp1x2*Rcp2x2*Reta1x1*Reta2x1 - complex(0,1)*lam1s*Rcp1x3*Rcp2x3*Reta1x1*Reta2x1 - complex(0,1)*lamd*Rcp1x1*Rcp2x1*Reta1x2*Reta2x2 - complex(0,1)*lamm*Rcp1x1*Rcp2x1*Reta1x2*Reta2x2 - complex(0,1)*lam2*Rcp1x2*Rcp2x2*Reta1x2*Reta2x2 - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*Reta1x2*Reta2x2 - complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Reta1x3*Reta2x3 - complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Reta1x3*Reta2x3 - complex(0,1)*lams*Rcp1x3*Rcp2x3*Reta1x3*Reta2x3',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(complex(0,1)*lam1*Rcp2x1**2*Reta1x1*Reta2x1) - complex(0,1)*lamd*Rcp2x2**2*Reta1x1*Reta2x1 - complex(0,1)*lamm*Rcp2x2**2*Reta1x1*Reta2x1 - complex(0,1)*lam1s*Rcp2x3**2*Reta1x1*Reta2x1 - complex(0,1)*lamd*Rcp2x1**2*Reta1x2*Reta2x2 - complex(0,1)*lamm*Rcp2x1**2*Reta1x2*Reta2x2 - complex(0,1)*lam2*Rcp2x2**2*Reta1x2*Reta2x2 - complex(0,1)*lam2s*Rcp2x3**2*Reta1x2*Reta2x2 - complex(0,1)*lam1s*Rcp2x1**2*Reta1x3*Reta2x3 - complex(0,1)*lam2s*Rcp2x2**2*Reta1x3*Reta2x3 - complex(0,1)*lams*Rcp2x3**2*Reta1x3*Reta2x3',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp3x1*Reta1x1*Reta2x1) - complex(0,1)*lamd*Rcp1x2*Rcp3x2*Reta1x1*Reta2x1 - complex(0,1)*lamm*Rcp1x2*Rcp3x2*Reta1x1*Reta2x1 - complex(0,1)*lam1s*Rcp1x3*Rcp3x3*Reta1x1*Reta2x1 - complex(0,1)*lamd*Rcp1x1*Rcp3x1*Reta1x2*Reta2x2 - complex(0,1)*lamm*Rcp1x1*Rcp3x1*Reta1x2*Reta2x2 - complex(0,1)*lam2*Rcp1x2*Rcp3x2*Reta1x2*Reta2x2 - complex(0,1)*lam2s*Rcp1x3*Rcp3x3*Reta1x2*Reta2x2 - complex(0,1)*lam1s*Rcp1x1*Rcp3x1*Reta1x3*Reta2x3 - complex(0,1)*lam2s*Rcp1x2*Rcp3x2*Reta1x3*Reta2x3 - complex(0,1)*lams*Rcp1x3*Rcp3x3*Reta1x3*Reta2x3',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(complex(0,1)*lam1*Rcp2x1*Rcp3x1*Reta1x1*Reta2x1) - complex(0,1)*lamd*Rcp2x2*Rcp3x2*Reta1x1*Reta2x1 - complex(0,1)*lamm*Rcp2x2*Rcp3x2*Reta1x1*Reta2x1 - complex(0,1)*lam1s*Rcp2x3*Rcp3x3*Reta1x1*Reta2x1 - complex(0,1)*lamd*Rcp2x1*Rcp3x1*Reta1x2*Reta2x2 - complex(0,1)*lamm*Rcp2x1*Rcp3x1*Reta1x2*Reta2x2 - complex(0,1)*lam2*Rcp2x2*Rcp3x2*Reta1x2*Reta2x2 - complex(0,1)*lam2s*Rcp2x3*Rcp3x3*Reta1x2*Reta2x2 - complex(0,1)*lam1s*Rcp2x1*Rcp3x1*Reta1x3*Reta2x3 - complex(0,1)*lam2s*Rcp2x2*Rcp3x2*Reta1x3*Reta2x3 - complex(0,1)*lams*Rcp2x3*Rcp3x3*Reta1x3*Reta2x3',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(complex(0,1)*lam1*Rcp3x1**2*Reta1x1*Reta2x1) - complex(0,1)*lamd*Rcp3x2**2*Reta1x1*Reta2x1 - complex(0,1)*lamm*Rcp3x2**2*Reta1x1*Reta2x1 - complex(0,1)*lam1s*Rcp3x3**2*Reta1x1*Reta2x1 - complex(0,1)*lamd*Rcp3x1**2*Reta1x2*Reta2x2 - complex(0,1)*lamm*Rcp3x1**2*Reta1x2*Reta2x2 - complex(0,1)*lam2*Rcp3x2**2*Reta1x2*Reta2x2 - complex(0,1)*lam2s*Rcp3x3**2*Reta1x2*Reta2x2 - complex(0,1)*lam1s*Rcp3x1**2*Reta1x3*Reta2x3 - complex(0,1)*lam2s*Rcp3x2**2*Reta1x3*Reta2x3 - complex(0,1)*lams*Rcp3x3**2*Reta1x3*Reta2x3',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-3*complex(0,1)*lam1*Reta1x1**3*Reta2x1 - 3*complex(0,1)*lamd*Reta1x1*Reta1x2**2*Reta2x1 - 3*complex(0,1)*lamm*Reta1x1*Reta1x2**2*Reta2x1 - 3*complex(0,1)*lam1s*Reta1x1*Reta1x3**2*Reta2x1 - 3*complex(0,1)*lamd*Reta1x1**2*Reta1x2*Reta2x2 - 3*complex(0,1)*lamm*Reta1x1**2*Reta1x2*Reta2x2 - 3*complex(0,1)*lam2*Reta1x2**3*Reta2x2 - 3*complex(0,1)*lam2s*Reta1x2*Reta1x3**2*Reta2x2 - 3*complex(0,1)*lam1s*Reta1x1**2*Reta1x3*Reta2x3 - 3*complex(0,1)*lam2s*Reta1x2**2*Reta1x3*Reta2x3 - 3*complex(0,1)*lams*Reta1x3**3*Reta2x3',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(complex(0,1)*lam1*Rcp1x1**2*Reta2x1**2) - complex(0,1)*lamd*Rcp1x2**2*Reta2x1**2 - complex(0,1)*lamm*Rcp1x2**2*Reta2x1**2 - complex(0,1)*lam1s*Rcp1x3**2*Reta2x1**2 - complex(0,1)*lamd*Rcp1x1**2*Reta2x2**2 - complex(0,1)*lamm*Rcp1x1**2*Reta2x2**2 - complex(0,1)*lam2*Rcp1x2**2*Reta2x2**2 - complex(0,1)*lam2s*Rcp1x3**2*Reta2x2**2 - complex(0,1)*lam1s*Rcp1x1**2*Reta2x3**2 - complex(0,1)*lam2s*Rcp1x2**2*Reta2x3**2 - complex(0,1)*lams*Rcp1x3**2*Reta2x3**2',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp2x1*Reta2x1**2) - complex(0,1)*lamd*Rcp1x2*Rcp2x2*Reta2x1**2 - complex(0,1)*lamm*Rcp1x2*Rcp2x2*Reta2x1**2 - complex(0,1)*lam1s*Rcp1x3*Rcp2x3*Reta2x1**2 - complex(0,1)*lamd*Rcp1x1*Rcp2x1*Reta2x2**2 - complex(0,1)*lamm*Rcp1x1*Rcp2x1*Reta2x2**2 - complex(0,1)*lam2*Rcp1x2*Rcp2x2*Reta2x2**2 - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*Reta2x2**2 - complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Reta2x3**2 - complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Reta2x3**2 - complex(0,1)*lams*Rcp1x3*Rcp2x3*Reta2x3**2',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(complex(0,1)*lam1*Rcp2x1**2*Reta2x1**2) - complex(0,1)*lamd*Rcp2x2**2*Reta2x1**2 - complex(0,1)*lamm*Rcp2x2**2*Reta2x1**2 - complex(0,1)*lam1s*Rcp2x3**2*Reta2x1**2 - complex(0,1)*lamd*Rcp2x1**2*Reta2x2**2 - complex(0,1)*lamm*Rcp2x1**2*Reta2x2**2 - complex(0,1)*lam2*Rcp2x2**2*Reta2x2**2 - complex(0,1)*lam2s*Rcp2x3**2*Reta2x2**2 - complex(0,1)*lam1s*Rcp2x1**2*Reta2x3**2 - complex(0,1)*lam2s*Rcp2x2**2*Reta2x3**2 - complex(0,1)*lams*Rcp2x3**2*Reta2x3**2',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp3x1*Reta2x1**2) - complex(0,1)*lamd*Rcp1x2*Rcp3x2*Reta2x1**2 - complex(0,1)*lamm*Rcp1x2*Rcp3x2*Reta2x1**2 - complex(0,1)*lam1s*Rcp1x3*Rcp3x3*Reta2x1**2 - complex(0,1)*lamd*Rcp1x1*Rcp3x1*Reta2x2**2 - complex(0,1)*lamm*Rcp1x1*Rcp3x1*Reta2x2**2 - complex(0,1)*lam2*Rcp1x2*Rcp3x2*Reta2x2**2 - complex(0,1)*lam2s*Rcp1x3*Rcp3x3*Reta2x2**2 - complex(0,1)*lam1s*Rcp1x1*Rcp3x1*Reta2x3**2 - complex(0,1)*lam2s*Rcp1x2*Rcp3x2*Reta2x3**2 - complex(0,1)*lams*Rcp1x3*Rcp3x3*Reta2x3**2',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(complex(0,1)*lam1*Rcp2x1*Rcp3x1*Reta2x1**2) - complex(0,1)*lamd*Rcp2x2*Rcp3x2*Reta2x1**2 - complex(0,1)*lamm*Rcp2x2*Rcp3x2*Reta2x1**2 - complex(0,1)*lam1s*Rcp2x3*Rcp3x3*Reta2x1**2 - complex(0,1)*lamd*Rcp2x1*Rcp3x1*Reta2x2**2 - complex(0,1)*lamm*Rcp2x1*Rcp3x1*Reta2x2**2 - complex(0,1)*lam2*Rcp2x2*Rcp3x2*Reta2x2**2 - complex(0,1)*lam2s*Rcp2x3*Rcp3x3*Reta2x2**2 - complex(0,1)*lam1s*Rcp2x1*Rcp3x1*Reta2x3**2 - complex(0,1)*lam2s*Rcp2x2*Rcp3x2*Reta2x3**2 - complex(0,1)*lams*Rcp2x3*Rcp3x3*Reta2x3**2',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(complex(0,1)*lam1*Rcp3x1**2*Reta2x1**2) - complex(0,1)*lamd*Rcp3x2**2*Reta2x1**2 - complex(0,1)*lamm*Rcp3x2**2*Reta2x1**2 - complex(0,1)*lam1s*Rcp3x3**2*Reta2x1**2 - complex(0,1)*lamd*Rcp3x1**2*Reta2x2**2 - complex(0,1)*lamm*Rcp3x1**2*Reta2x2**2 - complex(0,1)*lam2*Rcp3x2**2*Reta2x2**2 - complex(0,1)*lam2s*Rcp3x3**2*Reta2x2**2 - complex(0,1)*lam1s*Rcp3x1**2*Reta2x3**2 - complex(0,1)*lam2s*Rcp3x2**2*Reta2x3**2 - complex(0,1)*lams*Rcp3x3**2*Reta2x3**2',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '-3*complex(0,1)*lam1*Reta1x1**2*Reta2x1**2 - complex(0,1)*lamd*Reta1x2**2*Reta2x1**2 - complex(0,1)*lamm*Reta1x2**2*Reta2x1**2 - complex(0,1)*lam1s*Reta1x3**2*Reta2x1**2 - 4*complex(0,1)*lamd*Reta1x1*Reta1x2*Reta2x1*Reta2x2 - 4*complex(0,1)*lamm*Reta1x1*Reta1x2*Reta2x1*Reta2x2 - complex(0,1)*lamd*Reta1x1**2*Reta2x2**2 - complex(0,1)*lamm*Reta1x1**2*Reta2x2**2 - 3*complex(0,1)*lam2*Reta1x2**2*Reta2x2**2 - complex(0,1)*lam2s*Reta1x3**2*Reta2x2**2 - 4*complex(0,1)*lam1s*Reta1x1*Reta1x3*Reta2x1*Reta2x3 - 4*complex(0,1)*lam2s*Reta1x2*Reta1x3*Reta2x2*Reta2x3 - complex(0,1)*lam1s*Reta1x1**2*Reta2x3**2 - complex(0,1)*lam2s*Reta1x2**2*Reta2x3**2 - 3*complex(0,1)*lams*Reta1x3**2*Reta2x3**2',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-3*complex(0,1)*lam1*Reta1x1*Reta2x1**3 - 3*complex(0,1)*lamd*Reta1x2*Reta2x1**2*Reta2x2 - 3*complex(0,1)*lamm*Reta1x2*Reta2x1**2*Reta2x2 - 3*complex(0,1)*lamd*Reta1x1*Reta2x1*Reta2x2**2 - 3*complex(0,1)*lamm*Reta1x1*Reta2x1*Reta2x2**2 - 3*complex(0,1)*lam2*Reta1x2*Reta2x2**3 - 3*complex(0,1)*lam1s*Reta1x3*Reta2x1**2*Reta2x3 - 3*complex(0,1)*lam2s*Reta1x3*Reta2x2**2*Reta2x3 - 3*complex(0,1)*lam1s*Reta1x1*Reta2x1*Reta2x3**2 - 3*complex(0,1)*lam2s*Reta1x2*Reta2x2*Reta2x3**2 - 3*complex(0,1)*lams*Reta1x3*Reta2x3**3',
                 order = {'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '-3*complex(0,1)*lam1*Reta2x1**4 - 6*complex(0,1)*lamd*Reta2x1**2*Reta2x2**2 - 6*complex(0,1)*lamm*Reta2x1**2*Reta2x2**2 - 3*complex(0,1)*lam2*Reta2x2**4 - 6*complex(0,1)*lam1s*Reta2x1**2*Reta2x3**2 - 6*complex(0,1)*lam2s*Reta2x2**2*Reta2x3**2 - 3*complex(0,1)*lams*Reta2x3**4',
                 order = {'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(complex(0,1)*lam1*Rcp1x1**2*Reta1x1*Reta3x1) - complex(0,1)*lamd*Rcp1x2**2*Reta1x1*Reta3x1 - complex(0,1)*lamm*Rcp1x2**2*Reta1x1*Reta3x1 - complex(0,1)*lam1s*Rcp1x3**2*Reta1x1*Reta3x1 - complex(0,1)*lamd*Rcp1x1**2*Reta1x2*Reta3x2 - complex(0,1)*lamm*Rcp1x1**2*Reta1x2*Reta3x2 - complex(0,1)*lam2*Rcp1x2**2*Reta1x2*Reta3x2 - complex(0,1)*lam2s*Rcp1x3**2*Reta1x2*Reta3x2 - complex(0,1)*lam1s*Rcp1x1**2*Reta1x3*Reta3x3 - complex(0,1)*lam2s*Rcp1x2**2*Reta1x3*Reta3x3 - complex(0,1)*lams*Rcp1x3**2*Reta1x3*Reta3x3',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp2x1*Reta1x1*Reta3x1) - complex(0,1)*lamd*Rcp1x2*Rcp2x2*Reta1x1*Reta3x1 - complex(0,1)*lamm*Rcp1x2*Rcp2x2*Reta1x1*Reta3x1 - complex(0,1)*lam1s*Rcp1x3*Rcp2x3*Reta1x1*Reta3x1 - complex(0,1)*lamd*Rcp1x1*Rcp2x1*Reta1x2*Reta3x2 - complex(0,1)*lamm*Rcp1x1*Rcp2x1*Reta1x2*Reta3x2 - complex(0,1)*lam2*Rcp1x2*Rcp2x2*Reta1x2*Reta3x2 - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*Reta1x2*Reta3x2 - complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Reta1x3*Reta3x3 - complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Reta1x3*Reta3x3 - complex(0,1)*lams*Rcp1x3*Rcp2x3*Reta1x3*Reta3x3',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(complex(0,1)*lam1*Rcp2x1**2*Reta1x1*Reta3x1) - complex(0,1)*lamd*Rcp2x2**2*Reta1x1*Reta3x1 - complex(0,1)*lamm*Rcp2x2**2*Reta1x1*Reta3x1 - complex(0,1)*lam1s*Rcp2x3**2*Reta1x1*Reta3x1 - complex(0,1)*lamd*Rcp2x1**2*Reta1x2*Reta3x2 - complex(0,1)*lamm*Rcp2x1**2*Reta1x2*Reta3x2 - complex(0,1)*lam2*Rcp2x2**2*Reta1x2*Reta3x2 - complex(0,1)*lam2s*Rcp2x3**2*Reta1x2*Reta3x2 - complex(0,1)*lam1s*Rcp2x1**2*Reta1x3*Reta3x3 - complex(0,1)*lam2s*Rcp2x2**2*Reta1x3*Reta3x3 - complex(0,1)*lams*Rcp2x3**2*Reta1x3*Reta3x3',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp3x1*Reta1x1*Reta3x1) - complex(0,1)*lamd*Rcp1x2*Rcp3x2*Reta1x1*Reta3x1 - complex(0,1)*lamm*Rcp1x2*Rcp3x2*Reta1x1*Reta3x1 - complex(0,1)*lam1s*Rcp1x3*Rcp3x3*Reta1x1*Reta3x1 - complex(0,1)*lamd*Rcp1x1*Rcp3x1*Reta1x2*Reta3x2 - complex(0,1)*lamm*Rcp1x1*Rcp3x1*Reta1x2*Reta3x2 - complex(0,1)*lam2*Rcp1x2*Rcp3x2*Reta1x2*Reta3x2 - complex(0,1)*lam2s*Rcp1x3*Rcp3x3*Reta1x2*Reta3x2 - complex(0,1)*lam1s*Rcp1x1*Rcp3x1*Reta1x3*Reta3x3 - complex(0,1)*lam2s*Rcp1x2*Rcp3x2*Reta1x3*Reta3x3 - complex(0,1)*lams*Rcp1x3*Rcp3x3*Reta1x3*Reta3x3',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(complex(0,1)*lam1*Rcp2x1*Rcp3x1*Reta1x1*Reta3x1) - complex(0,1)*lamd*Rcp2x2*Rcp3x2*Reta1x1*Reta3x1 - complex(0,1)*lamm*Rcp2x2*Rcp3x2*Reta1x1*Reta3x1 - complex(0,1)*lam1s*Rcp2x3*Rcp3x3*Reta1x1*Reta3x1 - complex(0,1)*lamd*Rcp2x1*Rcp3x1*Reta1x2*Reta3x2 - complex(0,1)*lamm*Rcp2x1*Rcp3x1*Reta1x2*Reta3x2 - complex(0,1)*lam2*Rcp2x2*Rcp3x2*Reta1x2*Reta3x2 - complex(0,1)*lam2s*Rcp2x3*Rcp3x3*Reta1x2*Reta3x2 - complex(0,1)*lam1s*Rcp2x1*Rcp3x1*Reta1x3*Reta3x3 - complex(0,1)*lam2s*Rcp2x2*Rcp3x2*Reta1x3*Reta3x3 - complex(0,1)*lams*Rcp2x3*Rcp3x3*Reta1x3*Reta3x3',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '-(complex(0,1)*lam1*Rcp3x1**2*Reta1x1*Reta3x1) - complex(0,1)*lamd*Rcp3x2**2*Reta1x1*Reta3x1 - complex(0,1)*lamm*Rcp3x2**2*Reta1x1*Reta3x1 - complex(0,1)*lam1s*Rcp3x3**2*Reta1x1*Reta3x1 - complex(0,1)*lamd*Rcp3x1**2*Reta1x2*Reta3x2 - complex(0,1)*lamm*Rcp3x1**2*Reta1x2*Reta3x2 - complex(0,1)*lam2*Rcp3x2**2*Reta1x2*Reta3x2 - complex(0,1)*lam2s*Rcp3x3**2*Reta1x2*Reta3x2 - complex(0,1)*lam1s*Rcp3x1**2*Reta1x3*Reta3x3 - complex(0,1)*lam2s*Rcp3x2**2*Reta1x3*Reta3x3 - complex(0,1)*lams*Rcp3x3**2*Reta1x3*Reta3x3',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '-3*complex(0,1)*lam1*Reta1x1**3*Reta3x1 - 3*complex(0,1)*lamd*Reta1x1*Reta1x2**2*Reta3x1 - 3*complex(0,1)*lamm*Reta1x1*Reta1x2**2*Reta3x1 - 3*complex(0,1)*lam1s*Reta1x1*Reta1x3**2*Reta3x1 - 3*complex(0,1)*lamd*Reta1x1**2*Reta1x2*Reta3x2 - 3*complex(0,1)*lamm*Reta1x1**2*Reta1x2*Reta3x2 - 3*complex(0,1)*lam2*Reta1x2**3*Reta3x2 - 3*complex(0,1)*lam2s*Reta1x2*Reta1x3**2*Reta3x2 - 3*complex(0,1)*lam1s*Reta1x1**2*Reta1x3*Reta3x3 - 3*complex(0,1)*lam2s*Reta1x2**2*Reta1x3*Reta3x3 - 3*complex(0,1)*lams*Reta1x3**3*Reta3x3',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(complex(0,1)*lam1*Rcp1x1**2*Reta2x1*Reta3x1) - complex(0,1)*lamd*Rcp1x2**2*Reta2x1*Reta3x1 - complex(0,1)*lamm*Rcp1x2**2*Reta2x1*Reta3x1 - complex(0,1)*lam1s*Rcp1x3**2*Reta2x1*Reta3x1 - complex(0,1)*lamd*Rcp1x1**2*Reta2x2*Reta3x2 - complex(0,1)*lamm*Rcp1x1**2*Reta2x2*Reta3x2 - complex(0,1)*lam2*Rcp1x2**2*Reta2x2*Reta3x2 - complex(0,1)*lam2s*Rcp1x3**2*Reta2x2*Reta3x2 - complex(0,1)*lam1s*Rcp1x1**2*Reta2x3*Reta3x3 - complex(0,1)*lam2s*Rcp1x2**2*Reta2x3*Reta3x3 - complex(0,1)*lams*Rcp1x3**2*Reta2x3*Reta3x3',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp2x1*Reta2x1*Reta3x1) - complex(0,1)*lamd*Rcp1x2*Rcp2x2*Reta2x1*Reta3x1 - complex(0,1)*lamm*Rcp1x2*Rcp2x2*Reta2x1*Reta3x1 - complex(0,1)*lam1s*Rcp1x3*Rcp2x3*Reta2x1*Reta3x1 - complex(0,1)*lamd*Rcp1x1*Rcp2x1*Reta2x2*Reta3x2 - complex(0,1)*lamm*Rcp1x1*Rcp2x1*Reta2x2*Reta3x2 - complex(0,1)*lam2*Rcp1x2*Rcp2x2*Reta2x2*Reta3x2 - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*Reta2x2*Reta3x2 - complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Reta2x3*Reta3x3 - complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Reta2x3*Reta3x3 - complex(0,1)*lams*Rcp1x3*Rcp2x3*Reta2x3*Reta3x3',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(complex(0,1)*lam1*Rcp2x1**2*Reta2x1*Reta3x1) - complex(0,1)*lamd*Rcp2x2**2*Reta2x1*Reta3x1 - complex(0,1)*lamm*Rcp2x2**2*Reta2x1*Reta3x1 - complex(0,1)*lam1s*Rcp2x3**2*Reta2x1*Reta3x1 - complex(0,1)*lamd*Rcp2x1**2*Reta2x2*Reta3x2 - complex(0,1)*lamm*Rcp2x1**2*Reta2x2*Reta3x2 - complex(0,1)*lam2*Rcp2x2**2*Reta2x2*Reta3x2 - complex(0,1)*lam2s*Rcp2x3**2*Reta2x2*Reta3x2 - complex(0,1)*lam1s*Rcp2x1**2*Reta2x3*Reta3x3 - complex(0,1)*lam2s*Rcp2x2**2*Reta2x3*Reta3x3 - complex(0,1)*lams*Rcp2x3**2*Reta2x3*Reta3x3',
                 order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp3x1*Reta2x1*Reta3x1) - complex(0,1)*lamd*Rcp1x2*Rcp3x2*Reta2x1*Reta3x1 - complex(0,1)*lamm*Rcp1x2*Rcp3x2*Reta2x1*Reta3x1 - complex(0,1)*lam1s*Rcp1x3*Rcp3x3*Reta2x1*Reta3x1 - complex(0,1)*lamd*Rcp1x1*Rcp3x1*Reta2x2*Reta3x2 - complex(0,1)*lamm*Rcp1x1*Rcp3x1*Reta2x2*Reta3x2 - complex(0,1)*lam2*Rcp1x2*Rcp3x2*Reta2x2*Reta3x2 - complex(0,1)*lam2s*Rcp1x3*Rcp3x3*Reta2x2*Reta3x2 - complex(0,1)*lam1s*Rcp1x1*Rcp3x1*Reta2x3*Reta3x3 - complex(0,1)*lam2s*Rcp1x2*Rcp3x2*Reta2x3*Reta3x3 - complex(0,1)*lams*Rcp1x3*Rcp3x3*Reta2x3*Reta3x3',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '-(complex(0,1)*lam1*Rcp2x1*Rcp3x1*Reta2x1*Reta3x1) - complex(0,1)*lamd*Rcp2x2*Rcp3x2*Reta2x1*Reta3x1 - complex(0,1)*lamm*Rcp2x2*Rcp3x2*Reta2x1*Reta3x1 - complex(0,1)*lam1s*Rcp2x3*Rcp3x3*Reta2x1*Reta3x1 - complex(0,1)*lamd*Rcp2x1*Rcp3x1*Reta2x2*Reta3x2 - complex(0,1)*lamm*Rcp2x1*Rcp3x1*Reta2x2*Reta3x2 - complex(0,1)*lam2*Rcp2x2*Rcp3x2*Reta2x2*Reta3x2 - complex(0,1)*lam2s*Rcp2x3*Rcp3x3*Reta2x2*Reta3x2 - complex(0,1)*lam1s*Rcp2x1*Rcp3x1*Reta2x3*Reta3x3 - complex(0,1)*lam2s*Rcp2x2*Rcp3x2*Reta2x3*Reta3x3 - complex(0,1)*lams*Rcp2x3*Rcp3x3*Reta2x3*Reta3x3',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '-(complex(0,1)*lam1*Rcp3x1**2*Reta2x1*Reta3x1) - complex(0,1)*lamd*Rcp3x2**2*Reta2x1*Reta3x1 - complex(0,1)*lamm*Rcp3x2**2*Reta2x1*Reta3x1 - complex(0,1)*lam1s*Rcp3x3**2*Reta2x1*Reta3x1 - complex(0,1)*lamd*Rcp3x1**2*Reta2x2*Reta3x2 - complex(0,1)*lamm*Rcp3x1**2*Reta2x2*Reta3x2 - complex(0,1)*lam2*Rcp3x2**2*Reta2x2*Reta3x2 - complex(0,1)*lam2s*Rcp3x3**2*Reta2x2*Reta3x2 - complex(0,1)*lam1s*Rcp3x1**2*Reta2x3*Reta3x3 - complex(0,1)*lam2s*Rcp3x2**2*Reta2x3*Reta3x3 - complex(0,1)*lams*Rcp3x3**2*Reta2x3*Reta3x3',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '-3*complex(0,1)*lam1*Reta1x1**2*Reta2x1*Reta3x1 - complex(0,1)*lamd*Reta1x2**2*Reta2x1*Reta3x1 - complex(0,1)*lamm*Reta1x2**2*Reta2x1*Reta3x1 - complex(0,1)*lam1s*Reta1x3**2*Reta2x1*Reta3x1 - 2*complex(0,1)*lamd*Reta1x1*Reta1x2*Reta2x2*Reta3x1 - 2*complex(0,1)*lamm*Reta1x1*Reta1x2*Reta2x2*Reta3x1 - 2*complex(0,1)*lam1s*Reta1x1*Reta1x3*Reta2x3*Reta3x1 - 2*complex(0,1)*lamd*Reta1x1*Reta1x2*Reta2x1*Reta3x2 - 2*complex(0,1)*lamm*Reta1x1*Reta1x2*Reta2x1*Reta3x2 - complex(0,1)*lamd*Reta1x1**2*Reta2x2*Reta3x2 - complex(0,1)*lamm*Reta1x1**2*Reta2x2*Reta3x2 - 3*complex(0,1)*lam2*Reta1x2**2*Reta2x2*Reta3x2 - complex(0,1)*lam2s*Reta1x3**2*Reta2x2*Reta3x2 - 2*complex(0,1)*lam2s*Reta1x2*Reta1x3*Reta2x3*Reta3x2 - 2*complex(0,1)*lam1s*Reta1x1*Reta1x3*Reta2x1*Reta3x3 - 2*complex(0,1)*lam2s*Reta1x2*Reta1x3*Reta2x2*Reta3x3 - complex(0,1)*lam1s*Reta1x1**2*Reta2x3*Reta3x3 - complex(0,1)*lam2s*Reta1x2**2*Reta2x3*Reta3x3 - 3*complex(0,1)*lams*Reta1x3**2*Reta2x3*Reta3x3',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '-3*complex(0,1)*lam1*Reta1x1*Reta2x1**2*Reta3x1 - 2*complex(0,1)*lamd*Reta1x2*Reta2x1*Reta2x2*Reta3x1 - 2*complex(0,1)*lamm*Reta1x2*Reta2x1*Reta2x2*Reta3x1 - complex(0,1)*lamd*Reta1x1*Reta2x2**2*Reta3x1 - complex(0,1)*lamm*Reta1x1*Reta2x2**2*Reta3x1 - 2*complex(0,1)*lam1s*Reta1x3*Reta2x1*Reta2x3*Reta3x1 - complex(0,1)*lam1s*Reta1x1*Reta2x3**2*Reta3x1 - complex(0,1)*lamd*Reta1x2*Reta2x1**2*Reta3x2 - complex(0,1)*lamm*Reta1x2*Reta2x1**2*Reta3x2 - 2*complex(0,1)*lamd*Reta1x1*Reta2x1*Reta2x2*Reta3x2 - 2*complex(0,1)*lamm*Reta1x1*Reta2x1*Reta2x2*Reta3x2 - 3*complex(0,1)*lam2*Reta1x2*Reta2x2**2*Reta3x2 - 2*complex(0,1)*lam2s*Reta1x3*Reta2x2*Reta2x3*Reta3x2 - complex(0,1)*lam2s*Reta1x2*Reta2x3**2*Reta3x2 - complex(0,1)*lam1s*Reta1x3*Reta2x1**2*Reta3x3 - complex(0,1)*lam2s*Reta1x3*Reta2x2**2*Reta3x3 - 2*complex(0,1)*lam1s*Reta1x1*Reta2x1*Reta2x3*Reta3x3 - 2*complex(0,1)*lam2s*Reta1x2*Reta2x2*Reta2x3*Reta3x3 - 3*complex(0,1)*lams*Reta1x3*Reta2x3**2*Reta3x3',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '-3*complex(0,1)*lam1*Reta2x1**3*Reta3x1 - 3*complex(0,1)*lamd*Reta2x1*Reta2x2**2*Reta3x1 - 3*complex(0,1)*lamm*Reta2x1*Reta2x2**2*Reta3x1 - 3*complex(0,1)*lam1s*Reta2x1*Reta2x3**2*Reta3x1 - 3*complex(0,1)*lamd*Reta2x1**2*Reta2x2*Reta3x2 - 3*complex(0,1)*lamm*Reta2x1**2*Reta2x2*Reta3x2 - 3*complex(0,1)*lam2*Reta2x2**3*Reta3x2 - 3*complex(0,1)*lam2s*Reta2x2*Reta2x3**2*Reta3x2 - 3*complex(0,1)*lam1s*Reta2x1**2*Reta2x3*Reta3x3 - 3*complex(0,1)*lam2s*Reta2x2**2*Reta2x3*Reta3x3 - 3*complex(0,1)*lams*Reta2x3**3*Reta3x3',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(complex(0,1)*lam1*Rcp1x1**2*Reta3x1**2) - complex(0,1)*lamd*Rcp1x2**2*Reta3x1**2 - complex(0,1)*lamm*Rcp1x2**2*Reta3x1**2 - complex(0,1)*lam1s*Rcp1x3**2*Reta3x1**2 - complex(0,1)*lamd*Rcp1x1**2*Reta3x2**2 - complex(0,1)*lamm*Rcp1x1**2*Reta3x2**2 - complex(0,1)*lam2*Rcp1x2**2*Reta3x2**2 - complex(0,1)*lam2s*Rcp1x3**2*Reta3x2**2 - complex(0,1)*lam1s*Rcp1x1**2*Reta3x3**2 - complex(0,1)*lam2s*Rcp1x2**2*Reta3x3**2 - complex(0,1)*lams*Rcp1x3**2*Reta3x3**2',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp2x1*Reta3x1**2) - complex(0,1)*lamd*Rcp1x2*Rcp2x2*Reta3x1**2 - complex(0,1)*lamm*Rcp1x2*Rcp2x2*Reta3x1**2 - complex(0,1)*lam1s*Rcp1x3*Rcp2x3*Reta3x1**2 - complex(0,1)*lamd*Rcp1x1*Rcp2x1*Reta3x2**2 - complex(0,1)*lamm*Rcp1x1*Rcp2x1*Reta3x2**2 - complex(0,1)*lam2*Rcp1x2*Rcp2x2*Reta3x2**2 - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*Reta3x2**2 - complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Reta3x3**2 - complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Reta3x3**2 - complex(0,1)*lams*Rcp1x3*Rcp2x3*Reta3x3**2',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(complex(0,1)*lam1*Rcp2x1**2*Reta3x1**2) - complex(0,1)*lamd*Rcp2x2**2*Reta3x1**2 - complex(0,1)*lamm*Rcp2x2**2*Reta3x1**2 - complex(0,1)*lam1s*Rcp2x3**2*Reta3x1**2 - complex(0,1)*lamd*Rcp2x1**2*Reta3x2**2 - complex(0,1)*lamm*Rcp2x1**2*Reta3x2**2 - complex(0,1)*lam2*Rcp2x2**2*Reta3x2**2 - complex(0,1)*lam2s*Rcp2x3**2*Reta3x2**2 - complex(0,1)*lam1s*Rcp2x1**2*Reta3x3**2 - complex(0,1)*lam2s*Rcp2x2**2*Reta3x3**2 - complex(0,1)*lams*Rcp2x3**2*Reta3x3**2',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(complex(0,1)*lam1*Rcp1x1*Rcp3x1*Reta3x1**2) - complex(0,1)*lamd*Rcp1x2*Rcp3x2*Reta3x1**2 - complex(0,1)*lamm*Rcp1x2*Rcp3x2*Reta3x1**2 - complex(0,1)*lam1s*Rcp1x3*Rcp3x3*Reta3x1**2 - complex(0,1)*lamd*Rcp1x1*Rcp3x1*Reta3x2**2 - complex(0,1)*lamm*Rcp1x1*Rcp3x1*Reta3x2**2 - complex(0,1)*lam2*Rcp1x2*Rcp3x2*Reta3x2**2 - complex(0,1)*lam2s*Rcp1x3*Rcp3x3*Reta3x2**2 - complex(0,1)*lam1s*Rcp1x1*Rcp3x1*Reta3x3**2 - complex(0,1)*lam2s*Rcp1x2*Rcp3x2*Reta3x3**2 - complex(0,1)*lams*Rcp1x3*Rcp3x3*Reta3x3**2',
                 order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(complex(0,1)*lam1*Rcp2x1*Rcp3x1*Reta3x1**2) - complex(0,1)*lamd*Rcp2x2*Rcp3x2*Reta3x1**2 - complex(0,1)*lamm*Rcp2x2*Rcp3x2*Reta3x1**2 - complex(0,1)*lam1s*Rcp2x3*Rcp3x3*Reta3x1**2 - complex(0,1)*lamd*Rcp2x1*Rcp3x1*Reta3x2**2 - complex(0,1)*lamm*Rcp2x1*Rcp3x1*Reta3x2**2 - complex(0,1)*lam2*Rcp2x2*Rcp3x2*Reta3x2**2 - complex(0,1)*lam2s*Rcp2x3*Rcp3x3*Reta3x2**2 - complex(0,1)*lam1s*Rcp2x1*Rcp3x1*Reta3x3**2 - complex(0,1)*lam2s*Rcp2x2*Rcp3x2*Reta3x3**2 - complex(0,1)*lams*Rcp2x3*Rcp3x3*Reta3x3**2',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '-(complex(0,1)*lam1*Rcp3x1**2*Reta3x1**2) - complex(0,1)*lamd*Rcp3x2**2*Reta3x1**2 - complex(0,1)*lamm*Rcp3x2**2*Reta3x1**2 - complex(0,1)*lam1s*Rcp3x3**2*Reta3x1**2 - complex(0,1)*lamd*Rcp3x1**2*Reta3x2**2 - complex(0,1)*lamm*Rcp3x1**2*Reta3x2**2 - complex(0,1)*lam2*Rcp3x2**2*Reta3x2**2 - complex(0,1)*lam2s*Rcp3x3**2*Reta3x2**2 - complex(0,1)*lam1s*Rcp3x1**2*Reta3x3**2 - complex(0,1)*lam2s*Rcp3x2**2*Reta3x3**2 - complex(0,1)*lams*Rcp3x3**2*Reta3x3**2',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-3*complex(0,1)*lam1*Reta1x1**2*Reta3x1**2 - complex(0,1)*lamd*Reta1x2**2*Reta3x1**2 - complex(0,1)*lamm*Reta1x2**2*Reta3x1**2 - complex(0,1)*lam1s*Reta1x3**2*Reta3x1**2 - 4*complex(0,1)*lamd*Reta1x1*Reta1x2*Reta3x1*Reta3x2 - 4*complex(0,1)*lamm*Reta1x1*Reta1x2*Reta3x1*Reta3x2 - complex(0,1)*lamd*Reta1x1**2*Reta3x2**2 - complex(0,1)*lamm*Reta1x1**2*Reta3x2**2 - 3*complex(0,1)*lam2*Reta1x2**2*Reta3x2**2 - complex(0,1)*lam2s*Reta1x3**2*Reta3x2**2 - 4*complex(0,1)*lam1s*Reta1x1*Reta1x3*Reta3x1*Reta3x3 - 4*complex(0,1)*lam2s*Reta1x2*Reta1x3*Reta3x2*Reta3x3 - complex(0,1)*lam1s*Reta1x1**2*Reta3x3**2 - complex(0,1)*lam2s*Reta1x2**2*Reta3x3**2 - 3*complex(0,1)*lams*Reta1x3**2*Reta3x3**2',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-3*complex(0,1)*lam1*Reta1x1*Reta2x1*Reta3x1**2 - complex(0,1)*lamd*Reta1x2*Reta2x2*Reta3x1**2 - complex(0,1)*lamm*Reta1x2*Reta2x2*Reta3x1**2 - complex(0,1)*lam1s*Reta1x3*Reta2x3*Reta3x1**2 - 2*complex(0,1)*lamd*Reta1x2*Reta2x1*Reta3x1*Reta3x2 - 2*complex(0,1)*lamm*Reta1x2*Reta2x1*Reta3x1*Reta3x2 - 2*complex(0,1)*lamd*Reta1x1*Reta2x2*Reta3x1*Reta3x2 - 2*complex(0,1)*lamm*Reta1x1*Reta2x2*Reta3x1*Reta3x2 - complex(0,1)*lamd*Reta1x1*Reta2x1*Reta3x2**2 - complex(0,1)*lamm*Reta1x1*Reta2x1*Reta3x2**2 - 3*complex(0,1)*lam2*Reta1x2*Reta2x2*Reta3x2**2 - complex(0,1)*lam2s*Reta1x3*Reta2x3*Reta3x2**2 - 2*complex(0,1)*lam1s*Reta1x3*Reta2x1*Reta3x1*Reta3x3 - 2*complex(0,1)*lam1s*Reta1x1*Reta2x3*Reta3x1*Reta3x3 - 2*complex(0,1)*lam2s*Reta1x3*Reta2x2*Reta3x2*Reta3x3 - 2*complex(0,1)*lam2s*Reta1x2*Reta2x3*Reta3x2*Reta3x3 - complex(0,1)*lam1s*Reta1x1*Reta2x1*Reta3x3**2 - complex(0,1)*lam2s*Reta1x2*Reta2x2*Reta3x3**2 - 3*complex(0,1)*lams*Reta1x3*Reta2x3*Reta3x3**2',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-3*complex(0,1)*lam1*Reta2x1**2*Reta3x1**2 - complex(0,1)*lamd*Reta2x2**2*Reta3x1**2 - complex(0,1)*lamm*Reta2x2**2*Reta3x1**2 - complex(0,1)*lam1s*Reta2x3**2*Reta3x1**2 - 4*complex(0,1)*lamd*Reta2x1*Reta2x2*Reta3x1*Reta3x2 - 4*complex(0,1)*lamm*Reta2x1*Reta2x2*Reta3x1*Reta3x2 - complex(0,1)*lamd*Reta2x1**2*Reta3x2**2 - complex(0,1)*lamm*Reta2x1**2*Reta3x2**2 - 3*complex(0,1)*lam2*Reta2x2**2*Reta3x2**2 - complex(0,1)*lam2s*Reta2x3**2*Reta3x2**2 - 4*complex(0,1)*lam1s*Reta2x1*Reta2x3*Reta3x1*Reta3x3 - 4*complex(0,1)*lam2s*Reta2x2*Reta2x3*Reta3x2*Reta3x3 - complex(0,1)*lam1s*Reta2x1**2*Reta3x3**2 - complex(0,1)*lam2s*Reta2x2**2*Reta3x3**2 - 3*complex(0,1)*lams*Reta2x3**2*Reta3x3**2',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '-3*complex(0,1)*lam1*Reta1x1*Reta3x1**3 - 3*complex(0,1)*lamd*Reta1x2*Reta3x1**2*Reta3x2 - 3*complex(0,1)*lamm*Reta1x2*Reta3x1**2*Reta3x2 - 3*complex(0,1)*lamd*Reta1x1*Reta3x1*Reta3x2**2 - 3*complex(0,1)*lamm*Reta1x1*Reta3x1*Reta3x2**2 - 3*complex(0,1)*lam2*Reta1x2*Reta3x2**3 - 3*complex(0,1)*lam1s*Reta1x3*Reta3x1**2*Reta3x3 - 3*complex(0,1)*lam2s*Reta1x3*Reta3x2**2*Reta3x3 - 3*complex(0,1)*lam1s*Reta1x1*Reta3x1*Reta3x3**2 - 3*complex(0,1)*lam2s*Reta1x2*Reta3x2*Reta3x3**2 - 3*complex(0,1)*lams*Reta1x3*Reta3x3**3',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '-3*complex(0,1)*lam1*Reta2x1*Reta3x1**3 - 3*complex(0,1)*lamd*Reta2x2*Reta3x1**2*Reta3x2 - 3*complex(0,1)*lamm*Reta2x2*Reta3x1**2*Reta3x2 - 3*complex(0,1)*lamd*Reta2x1*Reta3x1*Reta3x2**2 - 3*complex(0,1)*lamm*Reta2x1*Reta3x1*Reta3x2**2 - 3*complex(0,1)*lam2*Reta2x2*Reta3x2**3 - 3*complex(0,1)*lam1s*Reta2x3*Reta3x1**2*Reta3x3 - 3*complex(0,1)*lam2s*Reta2x3*Reta3x2**2*Reta3x3 - 3*complex(0,1)*lam1s*Reta2x1*Reta3x1*Reta3x3**2 - 3*complex(0,1)*lam2s*Reta2x2*Reta3x2*Reta3x3**2 - 3*complex(0,1)*lams*Reta2x3*Reta3x3**3',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '-3*complex(0,1)*lam1*Reta3x1**4 - 6*complex(0,1)*lamd*Reta3x1**2*Reta3x2**2 - 6*complex(0,1)*lamm*Reta3x1**2*Reta3x2**2 - 3*complex(0,1)*lam2*Reta3x2**4 - 6*complex(0,1)*lam1s*Reta3x1**2*Reta3x3**2 - 6*complex(0,1)*lam2s*Reta3x2**2*Reta3x3**2 - 3*complex(0,1)*lams*Reta3x3**4',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '-(cb*cx*complex(0,1)*gp*sb)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = 'cb*cx*complex(0,1)*gp*sb',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-2*cb*cx*ee*complex(0,1)*gp*sb',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '-(cb**2*ee*complex(0,1)) - ee*complex(0,1)*sb**2',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '2*cb**2*ee**2*complex(0,1) + 2*ee**2*complex(0,1)*sb**2',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '-2*cb**2*complex(0,1)*lam1*sb**2 - 2*cb**2*complex(0,1)*lam2*sb**2 + 4*cb**2*complex(0,1)*lamd*sb**2 + 4*cb**2*complex(0,1)*lamm*sb**2',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '-(cb**2*complex(0,1)*lamm*Rcp1x1*Rcp1x2) + cb*complex(0,1)*lam1*Rcp1x1**2*sb - cb*complex(0,1)*lamd*Rcp1x1**2*sb - cb*complex(0,1)*lam2*Rcp1x2**2*sb + cb*complex(0,1)*lamd*Rcp1x2**2*sb + cb*complex(0,1)*lam1s*Rcp1x3**2*sb - cb*complex(0,1)*lam2s*Rcp1x3**2*sb + complex(0,1)*lamm*Rcp1x1*Rcp1x2*sb**2',
                 order = {'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '-(cb**2*complex(0,1)*lamd*Rcp1x1**2) - cb**2*complex(0,1)*lam2*Rcp1x2**2 - cb**2*complex(0,1)*lam2s*Rcp1x3**2 + 2*cb*complex(0,1)*lamm*Rcp1x1*Rcp1x2*sb - complex(0,1)*lam1*Rcp1x1**2*sb**2 - complex(0,1)*lamd*Rcp1x2**2*sb**2 - complex(0,1)*lam1s*Rcp1x3**2*sb**2',
                 order = {'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(cb**2*complex(0,1)*lam1*Rcp1x1**2) - cb**2*complex(0,1)*lamd*Rcp1x2**2 - cb**2*complex(0,1)*lam1s*Rcp1x3**2 - 2*cb*complex(0,1)*lamm*Rcp1x1*Rcp1x2*sb - complex(0,1)*lamd*Rcp1x1**2*sb**2 - complex(0,1)*lam2*Rcp1x2**2*sb**2 - complex(0,1)*lam2s*Rcp1x3**2*sb**2',
                 order = {'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '-0.5*(cb**2*complex(0,1)*lamm*Rcp1x2*Rcp2x1) - (cb**2*complex(0,1)*lamm*Rcp1x1*Rcp2x2)/2. + cb*complex(0,1)*lam1*Rcp1x1*Rcp2x1*sb - cb*complex(0,1)*lamd*Rcp1x1*Rcp2x1*sb - cb*complex(0,1)*lam2*Rcp1x2*Rcp2x2*sb + cb*complex(0,1)*lamd*Rcp1x2*Rcp2x2*sb + cb*complex(0,1)*lam1s*Rcp1x3*Rcp2x3*sb - cb*complex(0,1)*lam2s*Rcp1x3*Rcp2x3*sb + (complex(0,1)*lamm*Rcp1x2*Rcp2x1*sb**2)/2. + (complex(0,1)*lamm*Rcp1x1*Rcp2x2*sb**2)/2.',
                 order = {'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '-(cb**2*complex(0,1)*lamm*Rcp2x1*Rcp2x2) + cb*complex(0,1)*lam1*Rcp2x1**2*sb - cb*complex(0,1)*lamd*Rcp2x1**2*sb - cb*complex(0,1)*lam2*Rcp2x2**2*sb + cb*complex(0,1)*lamd*Rcp2x2**2*sb + cb*complex(0,1)*lam1s*Rcp2x3**2*sb - cb*complex(0,1)*lam2s*Rcp2x3**2*sb + complex(0,1)*lamm*Rcp2x1*Rcp2x2*sb**2',
                 order = {'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(cb**2*complex(0,1)*lamd*Rcp1x1*Rcp2x1) - cb**2*complex(0,1)*lam2*Rcp1x2*Rcp2x2 - cb**2*complex(0,1)*lam2s*Rcp1x3*Rcp2x3 + cb*complex(0,1)*lamm*Rcp1x2*Rcp2x1*sb + cb*complex(0,1)*lamm*Rcp1x1*Rcp2x2*sb - complex(0,1)*lam1*Rcp1x1*Rcp2x1*sb**2 - complex(0,1)*lamd*Rcp1x2*Rcp2x2*sb**2 - complex(0,1)*lam1s*Rcp1x3*Rcp2x3*sb**2',
                 order = {'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(cb**2*complex(0,1)*lam1*Rcp1x1*Rcp2x1) - cb**2*complex(0,1)*lamd*Rcp1x2*Rcp2x2 - cb**2*complex(0,1)*lam1s*Rcp1x3*Rcp2x3 - cb*complex(0,1)*lamm*Rcp1x2*Rcp2x1*sb - cb*complex(0,1)*lamm*Rcp1x1*Rcp2x2*sb - complex(0,1)*lamd*Rcp1x1*Rcp2x1*sb**2 - complex(0,1)*lam2*Rcp1x2*Rcp2x2*sb**2 - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*sb**2',
                  order = {'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '-(cb**2*complex(0,1)*lamd*Rcp2x1**2) - cb**2*complex(0,1)*lam2*Rcp2x2**2 - cb**2*complex(0,1)*lam2s*Rcp2x3**2 + 2*cb*complex(0,1)*lamm*Rcp2x1*Rcp2x2*sb - complex(0,1)*lam1*Rcp2x1**2*sb**2 - complex(0,1)*lamd*Rcp2x2**2*sb**2 - complex(0,1)*lam1s*Rcp2x3**2*sb**2',
                  order = {'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(cb**2*complex(0,1)*lam1*Rcp2x1**2) - cb**2*complex(0,1)*lamd*Rcp2x2**2 - cb**2*complex(0,1)*lam1s*Rcp2x3**2 - 2*cb*complex(0,1)*lamm*Rcp2x1*Rcp2x2*sb - complex(0,1)*lamd*Rcp2x1**2*sb**2 - complex(0,1)*lam2*Rcp2x2**2*sb**2 - complex(0,1)*lam2s*Rcp2x3**2*sb**2',
                  order = {'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '-0.5*(cb**2*complex(0,1)*lamm*Rcp1x2*Rcp3x1) - (cb**2*complex(0,1)*lamm*Rcp1x1*Rcp3x2)/2. + cb*complex(0,1)*lam1*Rcp1x1*Rcp3x1*sb - cb*complex(0,1)*lamd*Rcp1x1*Rcp3x1*sb - cb*complex(0,1)*lam2*Rcp1x2*Rcp3x2*sb + cb*complex(0,1)*lamd*Rcp1x2*Rcp3x2*sb + cb*complex(0,1)*lam1s*Rcp1x3*Rcp3x3*sb - cb*complex(0,1)*lam2s*Rcp1x3*Rcp3x3*sb + (complex(0,1)*lamm*Rcp1x2*Rcp3x1*sb**2)/2. + (complex(0,1)*lamm*Rcp1x1*Rcp3x2*sb**2)/2.',
                  order = {'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '-0.5*(cb**2*complex(0,1)*lamm*Rcp2x2*Rcp3x1) - (cb**2*complex(0,1)*lamm*Rcp2x1*Rcp3x2)/2. + cb*complex(0,1)*lam1*Rcp2x1*Rcp3x1*sb - cb*complex(0,1)*lamd*Rcp2x1*Rcp3x1*sb - cb*complex(0,1)*lam2*Rcp2x2*Rcp3x2*sb + cb*complex(0,1)*lamd*Rcp2x2*Rcp3x2*sb + cb*complex(0,1)*lam1s*Rcp2x3*Rcp3x3*sb - cb*complex(0,1)*lam2s*Rcp2x3*Rcp3x3*sb + (complex(0,1)*lamm*Rcp2x2*Rcp3x1*sb**2)/2. + (complex(0,1)*lamm*Rcp2x1*Rcp3x2*sb**2)/2.',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(cb**2*complex(0,1)*lamm*Rcp3x1*Rcp3x2) + cb*complex(0,1)*lam1*Rcp3x1**2*sb - cb*complex(0,1)*lamd*Rcp3x1**2*sb - cb*complex(0,1)*lam2*Rcp3x2**2*sb + cb*complex(0,1)*lamd*Rcp3x2**2*sb + cb*complex(0,1)*lam1s*Rcp3x3**2*sb - cb*complex(0,1)*lam2s*Rcp3x3**2*sb + complex(0,1)*lamm*Rcp3x1*Rcp3x2*sb**2',
                  order = {'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '-(cb**2*complex(0,1)*lamd*Rcp1x1*Rcp3x1) - cb**2*complex(0,1)*lam2*Rcp1x2*Rcp3x2 - cb**2*complex(0,1)*lam2s*Rcp1x3*Rcp3x3 + cb*complex(0,1)*lamm*Rcp1x2*Rcp3x1*sb + cb*complex(0,1)*lamm*Rcp1x1*Rcp3x2*sb - complex(0,1)*lam1*Rcp1x1*Rcp3x1*sb**2 - complex(0,1)*lamd*Rcp1x2*Rcp3x2*sb**2 - complex(0,1)*lam1s*Rcp1x3*Rcp3x3*sb**2',
                  order = {'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(cb**2*complex(0,1)*lam1*Rcp1x1*Rcp3x1) - cb**2*complex(0,1)*lamd*Rcp1x2*Rcp3x2 - cb**2*complex(0,1)*lam1s*Rcp1x3*Rcp3x3 - cb*complex(0,1)*lamm*Rcp1x2*Rcp3x1*sb - cb*complex(0,1)*lamm*Rcp1x1*Rcp3x2*sb - complex(0,1)*lamd*Rcp1x1*Rcp3x1*sb**2 - complex(0,1)*lam2*Rcp1x2*Rcp3x2*sb**2 - complex(0,1)*lam2s*Rcp1x3*Rcp3x3*sb**2',
                  order = {'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(cb**2*complex(0,1)*lamd*Rcp2x1*Rcp3x1) - cb**2*complex(0,1)*lam2*Rcp2x2*Rcp3x2 - cb**2*complex(0,1)*lam2s*Rcp2x3*Rcp3x3 + cb*complex(0,1)*lamm*Rcp2x2*Rcp3x1*sb + cb*complex(0,1)*lamm*Rcp2x1*Rcp3x2*sb - complex(0,1)*lam1*Rcp2x1*Rcp3x1*sb**2 - complex(0,1)*lamd*Rcp2x2*Rcp3x2*sb**2 - complex(0,1)*lam1s*Rcp2x3*Rcp3x3*sb**2',
                  order = {'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(cb**2*complex(0,1)*lam1*Rcp2x1*Rcp3x1) - cb**2*complex(0,1)*lamd*Rcp2x2*Rcp3x2 - cb**2*complex(0,1)*lam1s*Rcp2x3*Rcp3x3 - cb*complex(0,1)*lamm*Rcp2x2*Rcp3x1*sb - cb*complex(0,1)*lamm*Rcp2x1*Rcp3x2*sb - complex(0,1)*lamd*Rcp2x1*Rcp3x1*sb**2 - complex(0,1)*lam2*Rcp2x2*Rcp3x2*sb**2 - complex(0,1)*lam2s*Rcp2x3*Rcp3x3*sb**2',
                  order = {'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(cb**2*complex(0,1)*lamd*Rcp3x1**2) - cb**2*complex(0,1)*lam2*Rcp3x2**2 - cb**2*complex(0,1)*lam2s*Rcp3x3**2 + 2*cb*complex(0,1)*lamm*Rcp3x1*Rcp3x2*sb - complex(0,1)*lam1*Rcp3x1**2*sb**2 - complex(0,1)*lamd*Rcp3x2**2*sb**2 - complex(0,1)*lam1s*Rcp3x3**2*sb**2',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(cb**2*complex(0,1)*lam1*Rcp3x1**2) - cb**2*complex(0,1)*lamd*Rcp3x2**2 - cb**2*complex(0,1)*lam1s*Rcp3x3**2 - 2*cb*complex(0,1)*lamm*Rcp3x1*Rcp3x2*sb - complex(0,1)*lamd*Rcp3x1**2*sb**2 - complex(0,1)*lam2*Rcp3x2**2*sb**2 - complex(0,1)*lam2s*Rcp3x3**2*sb**2',
                  order = {'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cb**2*lamm*Rcp1x2*Reta1x1)/2. - (cb**2*lamm*Rcp1x1*Reta1x2)/2. + (lamm*Rcp1x2*Reta1x1*sb**2)/2. - (lamm*Rcp1x1*Reta1x2*sb**2)/2.',
                  order = {'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '-0.5*(cb**2*lamm*Rcp1x2*Reta1x1) + (cb**2*lamm*Rcp1x1*Reta1x2)/2. - (lamm*Rcp1x2*Reta1x1*sb**2)/2. + (lamm*Rcp1x1*Reta1x2*sb**2)/2.',
                  order = {'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '(cb**2*lamm*Rcp2x2*Reta1x1)/2. - (cb**2*lamm*Rcp2x1*Reta1x2)/2. + (lamm*Rcp2x2*Reta1x1*sb**2)/2. - (lamm*Rcp2x1*Reta1x2*sb**2)/2.',
                  order = {'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '-0.5*(cb**2*lamm*Rcp2x2*Reta1x1) + (cb**2*lamm*Rcp2x1*Reta1x2)/2. - (lamm*Rcp2x2*Reta1x1*sb**2)/2. + (lamm*Rcp2x1*Reta1x2*sb**2)/2.',
                  order = {'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '(cb**2*lamm*Rcp3x2*Reta1x1)/2. - (cb**2*lamm*Rcp3x1*Reta1x2)/2. + (lamm*Rcp3x2*Reta1x1*sb**2)/2. - (lamm*Rcp3x1*Reta1x2*sb**2)/2.',
                  order = {'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '-0.5*(cb**2*lamm*Rcp3x2*Reta1x1) + (cb**2*lamm*Rcp3x1*Reta1x2)/2. - (lamm*Rcp3x2*Reta1x1*sb**2)/2. + (lamm*Rcp3x1*Reta1x2*sb**2)/2.',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '-(cb**2*complex(0,1)*lamm*Reta1x1*Reta1x2) + cb*complex(0,1)*lam1*Reta1x1**2*sb - cb*complex(0,1)*lamd*Reta1x1**2*sb - cb*complex(0,1)*lam2*Reta1x2**2*sb + cb*complex(0,1)*lamd*Reta1x2**2*sb + cb*complex(0,1)*lam1s*Reta1x3**2*sb - cb*complex(0,1)*lam2s*Reta1x3**2*sb + complex(0,1)*lamm*Reta1x1*Reta1x2*sb**2',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '-(cb**2*complex(0,1)*lamd*Reta1x1**2) - cb**2*complex(0,1)*lam2*Reta1x2**2 - cb**2*complex(0,1)*lam2s*Reta1x3**2 + 2*cb*complex(0,1)*lamm*Reta1x1*Reta1x2*sb - complex(0,1)*lam1*Reta1x1**2*sb**2 - complex(0,1)*lamd*Reta1x2**2*sb**2 - complex(0,1)*lam1s*Reta1x3**2*sb**2',
                  order = {'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(cb**2*complex(0,1)*lam1*Reta1x1**2) - cb**2*complex(0,1)*lamd*Reta1x2**2 - cb**2*complex(0,1)*lam1s*Reta1x3**2 - 2*cb*complex(0,1)*lamm*Reta1x1*Reta1x2*sb - complex(0,1)*lamd*Reta1x1**2*sb**2 - complex(0,1)*lam2*Reta1x2**2*sb**2 - complex(0,1)*lam2s*Reta1x3**2*sb**2',
                  order = {'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '(cb**2*lamm*Rcp1x2*Reta2x1)/2. - (cb**2*lamm*Rcp1x1*Reta2x2)/2. + (lamm*Rcp1x2*Reta2x1*sb**2)/2. - (lamm*Rcp1x1*Reta2x2*sb**2)/2.',
                  order = {'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '-0.5*(cb**2*lamm*Rcp1x2*Reta2x1) + (cb**2*lamm*Rcp1x1*Reta2x2)/2. - (lamm*Rcp1x2*Reta2x1*sb**2)/2. + (lamm*Rcp1x1*Reta2x2*sb**2)/2.',
                  order = {'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '(cb**2*lamm*Rcp2x2*Reta2x1)/2. - (cb**2*lamm*Rcp2x1*Reta2x2)/2. + (lamm*Rcp2x2*Reta2x1*sb**2)/2. - (lamm*Rcp2x1*Reta2x2*sb**2)/2.',
                  order = {'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '-0.5*(cb**2*lamm*Rcp2x2*Reta2x1) + (cb**2*lamm*Rcp2x1*Reta2x2)/2. - (lamm*Rcp2x2*Reta2x1*sb**2)/2. + (lamm*Rcp2x1*Reta2x2*sb**2)/2.',
                  order = {'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(cb**2*lamm*Rcp3x2*Reta2x1)/2. - (cb**2*lamm*Rcp3x1*Reta2x2)/2. + (lamm*Rcp3x2*Reta2x1*sb**2)/2. - (lamm*Rcp3x1*Reta2x2*sb**2)/2.',
                  order = {'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '-0.5*(cb**2*lamm*Rcp3x2*Reta2x1) + (cb**2*lamm*Rcp3x1*Reta2x2)/2. - (lamm*Rcp3x2*Reta2x1*sb**2)/2. + (lamm*Rcp3x1*Reta2x2*sb**2)/2.',
                  order = {'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-0.5*(cb**2*complex(0,1)*lamm*Reta1x2*Reta2x1) - (cb**2*complex(0,1)*lamm*Reta1x1*Reta2x2)/2. + cb*complex(0,1)*lam1*Reta1x1*Reta2x1*sb - cb*complex(0,1)*lamd*Reta1x1*Reta2x1*sb - cb*complex(0,1)*lam2*Reta1x2*Reta2x2*sb + cb*complex(0,1)*lamd*Reta1x2*Reta2x2*sb + cb*complex(0,1)*lam1s*Reta1x3*Reta2x3*sb - cb*complex(0,1)*lam2s*Reta1x3*Reta2x3*sb + (complex(0,1)*lamm*Reta1x2*Reta2x1*sb**2)/2. + (complex(0,1)*lamm*Reta1x1*Reta2x2*sb**2)/2.',
                  order = {'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(cb**2*complex(0,1)*lamm*Reta2x1*Reta2x2) + cb*complex(0,1)*lam1*Reta2x1**2*sb - cb*complex(0,1)*lamd*Reta2x1**2*sb - cb*complex(0,1)*lam2*Reta2x2**2*sb + cb*complex(0,1)*lamd*Reta2x2**2*sb + cb*complex(0,1)*lam1s*Reta2x3**2*sb - cb*complex(0,1)*lam2s*Reta2x3**2*sb + complex(0,1)*lamm*Reta2x1*Reta2x2*sb**2',
                  order = {'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(cb**2*complex(0,1)*lamd*Reta1x1*Reta2x1) - cb**2*complex(0,1)*lam2*Reta1x2*Reta2x2 - cb**2*complex(0,1)*lam2s*Reta1x3*Reta2x3 + cb*complex(0,1)*lamm*Reta1x2*Reta2x1*sb + cb*complex(0,1)*lamm*Reta1x1*Reta2x2*sb - complex(0,1)*lam1*Reta1x1*Reta2x1*sb**2 - complex(0,1)*lamd*Reta1x2*Reta2x2*sb**2 - complex(0,1)*lam1s*Reta1x3*Reta2x3*sb**2',
                  order = {'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(cb**2*complex(0,1)*lam1*Reta1x1*Reta2x1) - cb**2*complex(0,1)*lamd*Reta1x2*Reta2x2 - cb**2*complex(0,1)*lam1s*Reta1x3*Reta2x3 - cb*complex(0,1)*lamm*Reta1x2*Reta2x1*sb - cb*complex(0,1)*lamm*Reta1x1*Reta2x2*sb - complex(0,1)*lamd*Reta1x1*Reta2x1*sb**2 - complex(0,1)*lam2*Reta1x2*Reta2x2*sb**2 - complex(0,1)*lam2s*Reta1x3*Reta2x3*sb**2',
                  order = {'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(cb**2*complex(0,1)*lamd*Reta2x1**2) - cb**2*complex(0,1)*lam2*Reta2x2**2 - cb**2*complex(0,1)*lam2s*Reta2x3**2 + 2*cb*complex(0,1)*lamm*Reta2x1*Reta2x2*sb - complex(0,1)*lam1*Reta2x1**2*sb**2 - complex(0,1)*lamd*Reta2x2**2*sb**2 - complex(0,1)*lam1s*Reta2x3**2*sb**2',
                  order = {'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(cb**2*complex(0,1)*lam1*Reta2x1**2) - cb**2*complex(0,1)*lamd*Reta2x2**2 - cb**2*complex(0,1)*lam1s*Reta2x3**2 - 2*cb*complex(0,1)*lamm*Reta2x1*Reta2x2*sb - complex(0,1)*lamd*Reta2x1**2*sb**2 - complex(0,1)*lam2*Reta2x2**2*sb**2 - complex(0,1)*lam2s*Reta2x3**2*sb**2',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '(cb**2*lamm*Rcp1x2*Reta3x1)/2. - (cb**2*lamm*Rcp1x1*Reta3x2)/2. + (lamm*Rcp1x2*Reta3x1*sb**2)/2. - (lamm*Rcp1x1*Reta3x2*sb**2)/2.',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '-0.5*(cb**2*lamm*Rcp1x2*Reta3x1) + (cb**2*lamm*Rcp1x1*Reta3x2)/2. - (lamm*Rcp1x2*Reta3x1*sb**2)/2. + (lamm*Rcp1x1*Reta3x2*sb**2)/2.',
                  order = {'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '(cb**2*lamm*Rcp2x2*Reta3x1)/2. - (cb**2*lamm*Rcp2x1*Reta3x2)/2. + (lamm*Rcp2x2*Reta3x1*sb**2)/2. - (lamm*Rcp2x1*Reta3x2*sb**2)/2.',
                  order = {'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '-0.5*(cb**2*lamm*Rcp2x2*Reta3x1) + (cb**2*lamm*Rcp2x1*Reta3x2)/2. - (lamm*Rcp2x2*Reta3x1*sb**2)/2. + (lamm*Rcp2x1*Reta3x2*sb**2)/2.',
                  order = {'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '(cb**2*lamm*Rcp3x2*Reta3x1)/2. - (cb**2*lamm*Rcp3x1*Reta3x2)/2. + (lamm*Rcp3x2*Reta3x1*sb**2)/2. - (lamm*Rcp3x1*Reta3x2*sb**2)/2.',
                  order = {'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '-0.5*(cb**2*lamm*Rcp3x2*Reta3x1) + (cb**2*lamm*Rcp3x1*Reta3x2)/2. - (lamm*Rcp3x2*Reta3x1*sb**2)/2. + (lamm*Rcp3x1*Reta3x2*sb**2)/2.',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '-0.5*(cb**2*complex(0,1)*lamm*Reta1x2*Reta3x1) - (cb**2*complex(0,1)*lamm*Reta1x1*Reta3x2)/2. + cb*complex(0,1)*lam1*Reta1x1*Reta3x1*sb - cb*complex(0,1)*lamd*Reta1x1*Reta3x1*sb - cb*complex(0,1)*lam2*Reta1x2*Reta3x2*sb + cb*complex(0,1)*lamd*Reta1x2*Reta3x2*sb + cb*complex(0,1)*lam1s*Reta1x3*Reta3x3*sb - cb*complex(0,1)*lam2s*Reta1x3*Reta3x3*sb + (complex(0,1)*lamm*Reta1x2*Reta3x1*sb**2)/2. + (complex(0,1)*lamm*Reta1x1*Reta3x2*sb**2)/2.',
                  order = {'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '-0.5*(cb**2*complex(0,1)*lamm*Reta2x2*Reta3x1) - (cb**2*complex(0,1)*lamm*Reta2x1*Reta3x2)/2. + cb*complex(0,1)*lam1*Reta2x1*Reta3x1*sb - cb*complex(0,1)*lamd*Reta2x1*Reta3x1*sb - cb*complex(0,1)*lam2*Reta2x2*Reta3x2*sb + cb*complex(0,1)*lamd*Reta2x2*Reta3x2*sb + cb*complex(0,1)*lam1s*Reta2x3*Reta3x3*sb - cb*complex(0,1)*lam2s*Reta2x3*Reta3x3*sb + (complex(0,1)*lamm*Reta2x2*Reta3x1*sb**2)/2. + (complex(0,1)*lamm*Reta2x1*Reta3x2*sb**2)/2.',
                  order = {'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '-(cb**2*complex(0,1)*lamm*Reta3x1*Reta3x2) + cb*complex(0,1)*lam1*Reta3x1**2*sb - cb*complex(0,1)*lamd*Reta3x1**2*sb - cb*complex(0,1)*lam2*Reta3x2**2*sb + cb*complex(0,1)*lamd*Reta3x2**2*sb + cb*complex(0,1)*lam1s*Reta3x3**2*sb - cb*complex(0,1)*lam2s*Reta3x3**2*sb + complex(0,1)*lamm*Reta3x1*Reta3x2*sb**2',
                  order = {'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '-(cb**2*complex(0,1)*lamd*Reta1x1*Reta3x1) - cb**2*complex(0,1)*lam2*Reta1x2*Reta3x2 - cb**2*complex(0,1)*lam2s*Reta1x3*Reta3x3 + cb*complex(0,1)*lamm*Reta1x2*Reta3x1*sb + cb*complex(0,1)*lamm*Reta1x1*Reta3x2*sb - complex(0,1)*lam1*Reta1x1*Reta3x1*sb**2 - complex(0,1)*lamd*Reta1x2*Reta3x2*sb**2 - complex(0,1)*lam1s*Reta1x3*Reta3x3*sb**2',
                  order = {'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '-(cb**2*complex(0,1)*lam1*Reta1x1*Reta3x1) - cb**2*complex(0,1)*lamd*Reta1x2*Reta3x2 - cb**2*complex(0,1)*lam1s*Reta1x3*Reta3x3 - cb*complex(0,1)*lamm*Reta1x2*Reta3x1*sb - cb*complex(0,1)*lamm*Reta1x1*Reta3x2*sb - complex(0,1)*lamd*Reta1x1*Reta3x1*sb**2 - complex(0,1)*lam2*Reta1x2*Reta3x2*sb**2 - complex(0,1)*lam2s*Reta1x3*Reta3x3*sb**2',
                  order = {'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '-(cb**2*complex(0,1)*lamd*Reta2x1*Reta3x1) - cb**2*complex(0,1)*lam2*Reta2x2*Reta3x2 - cb**2*complex(0,1)*lam2s*Reta2x3*Reta3x3 + cb*complex(0,1)*lamm*Reta2x2*Reta3x1*sb + cb*complex(0,1)*lamm*Reta2x1*Reta3x2*sb - complex(0,1)*lam1*Reta2x1*Reta3x1*sb**2 - complex(0,1)*lamd*Reta2x2*Reta3x2*sb**2 - complex(0,1)*lam1s*Reta2x3*Reta3x3*sb**2',
                  order = {'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(cb**2*complex(0,1)*lam1*Reta2x1*Reta3x1) - cb**2*complex(0,1)*lamd*Reta2x2*Reta3x2 - cb**2*complex(0,1)*lam1s*Reta2x3*Reta3x3 - cb*complex(0,1)*lamm*Reta2x2*Reta3x1*sb - cb*complex(0,1)*lamm*Reta2x1*Reta3x2*sb - complex(0,1)*lamd*Reta2x1*Reta3x1*sb**2 - complex(0,1)*lam2*Reta2x2*Reta3x2*sb**2 - complex(0,1)*lam2s*Reta2x3*Reta3x3*sb**2',
                  order = {'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '-(cb**2*complex(0,1)*lamd*Reta3x1**2) - cb**2*complex(0,1)*lam2*Reta3x2**2 - cb**2*complex(0,1)*lam2s*Reta3x3**2 + 2*cb*complex(0,1)*lamm*Reta3x1*Reta3x2*sb - complex(0,1)*lam1*Reta3x1**2*sb**2 - complex(0,1)*lamd*Reta3x2**2*sb**2 - complex(0,1)*lam1s*Reta3x3**2*sb**2',
                  order = {'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '-(cb**2*complex(0,1)*lam1*Reta3x1**2) - cb**2*complex(0,1)*lamd*Reta3x2**2 - cb**2*complex(0,1)*lam1s*Reta3x3**2 - 2*cb*complex(0,1)*lamm*Reta3x1*Reta3x2*sb - complex(0,1)*lamd*Reta3x1**2*sb**2 - complex(0,1)*lam2*Reta3x2**2*sb**2 - complex(0,1)*lam2s*Reta3x3**2*sb**2',
                  order = {'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '-2*cb**3*complex(0,1)*lam2*sb + 2*cb**3*complex(0,1)*lamd*sb + 2*cb**3*complex(0,1)*lamm*sb + 2*cb*complex(0,1)*lam1*sb**3 - 2*cb*complex(0,1)*lamd*sb**3 - 2*cb*complex(0,1)*lamm*sb**3',
                  order = {'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '2*cb**3*complex(0,1)*lam1*sb - 2*cb**3*complex(0,1)*lamd*sb - 2*cb**3*complex(0,1)*lamm*sb - 2*cb*complex(0,1)*lam2*sb**3 + 2*cb*complex(0,1)*lamd*sb**3 + 2*cb*complex(0,1)*lamm*sb**3',
                  order = {'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '-2*cb**4*complex(0,1)*lam2 - 4*cb**2*complex(0,1)*lamd*sb**2 - 4*cb**2*complex(0,1)*lamm*sb**2 - 2*complex(0,1)*lam1*sb**4',
                  order = {'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '-2*cb**4*complex(0,1)*lam1 - 4*cb**2*complex(0,1)*lamd*sb**2 - 4*cb**2*complex(0,1)*lamm*sb**2 - 2*complex(0,1)*lam2*sb**4',
                  order = {'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '-(cb**4*complex(0,1)*lamd) - cb**4*complex(0,1)*lamm - 2*cb**2*complex(0,1)*lam1*sb**2 - 2*cb**2*complex(0,1)*lam2*sb**2 + 2*cb**2*complex(0,1)*lamd*sb**2 + 2*cb**2*complex(0,1)*lamm*sb**2 - complex(0,1)*lamd*sb**4 - complex(0,1)*lamm*sb**4',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '(ee**2*complex(0,1)*Rcp1x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp1x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '(ee**2*complex(0,1)*Rcp1x1*Rcp2x1)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp1x2*Rcp2x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '(ee**2*complex(0,1)*Rcp2x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp2x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '(ee**2*complex(0,1)*Rcp1x1*Rcp3x1)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp1x2*Rcp3x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '(ee**2*complex(0,1)*Rcp2x1*Rcp3x1)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp2x2*Rcp3x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '(ee**2*complex(0,1)*Rcp3x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp3x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '(ee**2*complex(0,1)*Reta1x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta1x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '(ee**2*complex(0,1)*Reta1x1*Reta2x1)/(2.*sw**2) + (ee**2*complex(0,1)*Reta1x2*Reta2x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '(ee**2*complex(0,1)*Reta2x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta2x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '(ee**2*complex(0,1)*Reta1x1*Reta3x1)/(2.*sw**2) + (ee**2*complex(0,1)*Reta1x2*Reta3x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '(ee**2*complex(0,1)*Reta2x1*Reta3x1)/(2.*sw**2) + (ee**2*complex(0,1)*Reta2x2*Reta3x2)/(2.*sw**2)',
                  order = {'QED':2})

GC_164 = Coupling(name = 'GC_164',
                  value = '(ee**2*complex(0,1)*Reta3x1**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta3x2**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_165 = Coupling(name = 'GC_165',
                  value = '(cb**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sb**2)/(2.*sw**2)',
                  order = {'QED':2})

GC_166 = Coupling(name = 'GC_166',
                  value = '(cb*ee*complex(0,1)*Rcp1x2)/(2.*sw) - (ee*complex(0,1)*Rcp1x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-0.5*(cb*ee*complex(0,1)*Rcp1x2)/sw + (ee*complex(0,1)*Rcp1x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(cb*ee**2*complex(0,1)*Rcp1x2)/(2.*sw) - (ee**2*complex(0,1)*Rcp1x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '-0.5*(cb*ee*complex(0,1)*Rcp1x1)/sw - (ee*complex(0,1)*Rcp1x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(cb*ee*complex(0,1)*Rcp1x1)/(2.*sw) + (ee*complex(0,1)*Rcp1x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '(cb*ee**2*complex(0,1)*Rcp1x1)/(2.*sw) + (ee**2*complex(0,1)*Rcp1x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '(cb*ee*complex(0,1)*Rcp2x2)/(2.*sw) - (ee*complex(0,1)*Rcp2x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-0.5*(cb*ee*complex(0,1)*Rcp2x2)/sw + (ee*complex(0,1)*Rcp2x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '(cb*ee**2*complex(0,1)*Rcp2x2)/(2.*sw) - (ee**2*complex(0,1)*Rcp2x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '-0.5*(cb*ee*complex(0,1)*Rcp2x1)/sw - (ee*complex(0,1)*Rcp2x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '(cb*ee*complex(0,1)*Rcp2x1)/(2.*sw) + (ee*complex(0,1)*Rcp2x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '(cb*ee**2*complex(0,1)*Rcp2x1)/(2.*sw) + (ee**2*complex(0,1)*Rcp2x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = '(cb*ee*complex(0,1)*Rcp3x2)/(2.*sw) - (ee*complex(0,1)*Rcp3x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-0.5*(cb*ee*complex(0,1)*Rcp3x2)/sw + (ee*complex(0,1)*Rcp3x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(cb*ee**2*complex(0,1)*Rcp3x2)/(2.*sw) - (ee**2*complex(0,1)*Rcp3x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '-0.5*(cb*ee*complex(0,1)*Rcp3x1)/sw - (ee*complex(0,1)*Rcp3x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '(cb*ee*complex(0,1)*Rcp3x1)/(2.*sw) + (ee*complex(0,1)*Rcp3x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '(cb*ee**2*complex(0,1)*Rcp3x1)/(2.*sw) + (ee**2*complex(0,1)*Rcp3x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '(cb*ee*Reta1x2)/(2.*sw) - (ee*Reta1x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '(cb*ee**2*Reta1x2)/(2.*sw) - (ee**2*Reta1x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '-0.5*(cb*ee**2*Reta1x2)/sw + (ee**2*Reta1x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '(cb*ee*Reta1x1)/(2.*sw) + (ee*Reta1x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '-0.5*(cb*ee**2*Reta1x1)/sw - (ee**2*Reta1x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(cb*ee**2*Reta1x1)/(2.*sw) + (ee**2*Reta1x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '(cb*ee*Reta2x2)/(2.*sw) - (ee*Reta2x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '(cb*ee**2*Reta2x2)/(2.*sw) - (ee**2*Reta2x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_192 = Coupling(name = 'GC_192',
                  value = '-0.5*(cb*ee**2*Reta2x2)/sw + (ee**2*Reta2x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_193 = Coupling(name = 'GC_193',
                  value = '(cb*ee*Reta2x1)/(2.*sw) + (ee*Reta2x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-0.5*(cb*ee**2*Reta2x1)/sw - (ee**2*Reta2x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_195 = Coupling(name = 'GC_195',
                  value = '(cb*ee**2*Reta2x1)/(2.*sw) + (ee**2*Reta2x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_196 = Coupling(name = 'GC_196',
                  value = '(cb*ee*Reta3x2)/(2.*sw) - (ee*Reta3x1*sb)/(2.*sw)',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(cb*ee**2*Reta3x2)/(2.*sw) - (ee**2*Reta3x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_198 = Coupling(name = 'GC_198',
                  value = '-0.5*(cb*ee**2*Reta3x2)/sw + (ee**2*Reta3x1*sb)/(2.*sw)',
                  order = {'QED':2})

GC_199 = Coupling(name = 'GC_199',
                  value = '(cb*ee*Reta3x1)/(2.*sw) + (ee*Reta3x2*sb)/(2.*sw)',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '-0.5*(cb*ee**2*Reta3x1)/sw - (ee**2*Reta3x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '(cb*ee**2*Reta3x1)/(2.*sw) + (ee**2*Reta3x2*sb)/(2.*sw)',
                  order = {'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = '(cw**2*cx**2*ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(cn1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(cn2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '(cn3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '(cw*cx*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(-2*cw*cx*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '(ee*complex(0,1)*sn1)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(ee*complex(0,1)*sn2)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '(ee*complex(0,1)*sn3)/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(cx*ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '-0.5*(cw*cx*ee*complex(0,1))/sw + (cx*ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = 'complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '-(cb*complex(0,1)*gp*sb*sx)',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = 'cb*complex(0,1)*gp*sb*sx',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-2*cb*ee*complex(0,1)*gp*sb*sx',
                  order = {'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '-((cw**2*cx*ee**2*complex(0,1)*sx)/sw**2)',
                  order = {'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '-((cw*ee*complex(0,1)*sx)/sw)',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '(2*cw*ee**2*complex(0,1)*sx)/sw',
                  order = {'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((ee*complex(0,1)*sw*sx)/cw)',
                  order = {'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '(cw**2*ee**2*complex(0,1)*sx**2)/sw**2',
                  order = {'QED':2})

GC_224 = Coupling(name = 'GC_224',
                  value = '-0.5*(cw*cx*ee*complex(0,1))/sw - (cx*ee*complex(0,1)*sw)/(6.*cw) + complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(cw*cx*ee*complex(0,1))/(2.*sw) - (cx*ee*complex(0,1)*sw)/(6.*cw) + complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '(cx*ee*complex(0,1)*sw)/(3.*cw) + complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '(-2*cx*ee*complex(0,1)*sw)/(3.*cw) + complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-0.5*(cb**2*cw*cx*ee*complex(0,1))/sw - (cw*cx*ee*complex(0,1)*sb**2)/(2.*sw) + (cb**2*cx*ee*complex(0,1)*sw)/(2.*cw) + (cx*ee*complex(0,1)*sb**2*sw)/(2.*cw) - cb**2*complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '(cw*cx*ee*complex(0,1)*sn1**2)/(2.*sw) + (cx*ee*complex(0,1)*sn1**2*sw)/(2.*cw) + cn1**2*complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(cw*cx*ee*complex(0,1)*sn2**2)/(2.*sw) + (cx*ee*complex(0,1)*sn2**2*sw)/(2.*cw) + cn2**2*complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(cw*cx*ee*complex(0,1)*sn3**2)/(2.*sw) + (cx*ee*complex(0,1)*sn3**2*sw)/(2.*cw) + cn3**2*complex(0,1)*gp*sx',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(cb**2*cw*cx*ee**2*complex(0,1))/sw + (cw*cx*ee**2*complex(0,1)*sb**2)/sw - (cb**2*cx*ee**2*complex(0,1)*sw)/cw - (cx*ee**2*complex(0,1)*sb**2*sw)/cw + 2*cb**2*ee*complex(0,1)*gp*sx',
                  order = {'QED':2})

GC_233 = Coupling(name = 'GC_233',
                  value = '-0.5*(cw*cx*ee*Rcp1x1*Reta1x1)/sw - (cw*cx*ee*Rcp1x2*Reta1x2)/(2.*sw) - (cx*ee*Rcp1x1*Reta1x1*sw)/(2.*cw) - (cx*ee*Rcp1x2*Reta1x2*sw)/(2.*cw) + gp*Rcp1x1*Reta1x1*sx + gp*Rcp1x3*Reta1x3*sx',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '-0.5*(cw*cx*ee*Rcp2x1*Reta1x1)/sw - (cw*cx*ee*Rcp2x2*Reta1x2)/(2.*sw) - (cx*ee*Rcp2x1*Reta1x1*sw)/(2.*cw) - (cx*ee*Rcp2x2*Reta1x2*sw)/(2.*cw) + gp*Rcp2x1*Reta1x1*sx + gp*Rcp2x3*Reta1x3*sx',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '-0.5*(cw*cx*ee*Rcp3x1*Reta1x1)/sw - (cw*cx*ee*Rcp3x2*Reta1x2)/(2.*sw) - (cx*ee*Rcp3x1*Reta1x1*sw)/(2.*cw) - (cx*ee*Rcp3x2*Reta1x2*sw)/(2.*cw) + gp*Rcp3x1*Reta1x1*sx + gp*Rcp3x3*Reta1x3*sx',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '-0.5*(cw*cx*ee*Rcp1x1*Reta2x1)/sw - (cw*cx*ee*Rcp1x2*Reta2x2)/(2.*sw) - (cx*ee*Rcp1x1*Reta2x1*sw)/(2.*cw) - (cx*ee*Rcp1x2*Reta2x2*sw)/(2.*cw) + gp*Rcp1x1*Reta2x1*sx + gp*Rcp1x3*Reta2x3*sx',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '-0.5*(cw*cx*ee*Rcp2x1*Reta2x1)/sw - (cw*cx*ee*Rcp2x2*Reta2x2)/(2.*sw) - (cx*ee*Rcp2x1*Reta2x1*sw)/(2.*cw) - (cx*ee*Rcp2x2*Reta2x2*sw)/(2.*cw) + gp*Rcp2x1*Reta2x1*sx + gp*Rcp2x3*Reta2x3*sx',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '-0.5*(cw*cx*ee*Rcp3x1*Reta2x1)/sw - (cw*cx*ee*Rcp3x2*Reta2x2)/(2.*sw) - (cx*ee*Rcp3x1*Reta2x1*sw)/(2.*cw) - (cx*ee*Rcp3x2*Reta2x2*sw)/(2.*cw) + gp*Rcp3x1*Reta2x1*sx + gp*Rcp3x3*Reta2x3*sx',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '-0.5*(cw*cx*ee*Rcp1x1*Reta3x1)/sw - (cw*cx*ee*Rcp1x2*Reta3x2)/(2.*sw) - (cx*ee*Rcp1x1*Reta3x1*sw)/(2.*cw) - (cx*ee*Rcp1x2*Reta3x2*sw)/(2.*cw) + gp*Rcp1x1*Reta3x1*sx + gp*Rcp1x3*Reta3x3*sx',
                  order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '-0.5*(cw*cx*ee*Rcp2x1*Reta3x1)/sw - (cw*cx*ee*Rcp2x2*Reta3x2)/(2.*sw) - (cx*ee*Rcp2x1*Reta3x1*sw)/(2.*cw) - (cx*ee*Rcp2x2*Reta3x2*sw)/(2.*cw) + gp*Rcp2x1*Reta3x1*sx + gp*Rcp2x3*Reta3x3*sx',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-0.5*(cw*cx*ee*Rcp3x1*Reta3x1)/sw - (cw*cx*ee*Rcp3x2*Reta3x2)/(2.*sw) - (cx*ee*Rcp3x1*Reta3x1*sw)/(2.*cw) - (cx*ee*Rcp3x2*Reta3x2*sw)/(2.*cw) + gp*Rcp3x1*Reta3x1*sx + gp*Rcp3x3*Reta3x3*sx',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((cx*ee*complex(0,1)*gp*Rcp1x1*sb)/sw) + (cb*ee**2*complex(0,1)*Rcp1x2*sx)/(2.*cw) - (ee**2*complex(0,1)*Rcp1x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_243 = Coupling(name = 'GC_243',
                  value = '(cb*cx*ee*complex(0,1)*gp*Rcp1x1)/sw + (cb*ee**2*complex(0,1)*Rcp1x1*sx)/(2.*cw) + (ee**2*complex(0,1)*Rcp1x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_244 = Coupling(name = 'GC_244',
                  value = '-((cx*ee*complex(0,1)*gp*Rcp2x1*sb)/sw) + (cb*ee**2*complex(0,1)*Rcp2x2*sx)/(2.*cw) - (ee**2*complex(0,1)*Rcp2x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_245 = Coupling(name = 'GC_245',
                  value = '(cb*cx*ee*complex(0,1)*gp*Rcp2x1)/sw + (cb*ee**2*complex(0,1)*Rcp2x1*sx)/(2.*cw) + (ee**2*complex(0,1)*Rcp2x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_246 = Coupling(name = 'GC_246',
                  value = '-((cx*ee*complex(0,1)*gp*Rcp3x1*sb)/sw) + (cb*ee**2*complex(0,1)*Rcp3x2*sx)/(2.*cw) - (ee**2*complex(0,1)*Rcp3x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_247 = Coupling(name = 'GC_247',
                  value = '(cb*cx*ee*complex(0,1)*gp*Rcp3x1)/sw + (cb*ee**2*complex(0,1)*Rcp3x1*sx)/(2.*cw) + (ee**2*complex(0,1)*Rcp3x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((cx*ee*gp*Reta1x1*sb)/sw) + (cb*ee**2*Reta1x2*sx)/(2.*cw) - (ee**2*Reta1x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_249 = Coupling(name = 'GC_249',
                  value = '(cx*ee*gp*Reta1x1*sb)/sw - (cb*ee**2*Reta1x2*sx)/(2.*cw) + (ee**2*Reta1x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_250 = Coupling(name = 'GC_250',
                  value = '-((cb*cx*ee*gp*Reta1x1)/sw) - (cb*ee**2*Reta1x1*sx)/(2.*cw) - (ee**2*Reta1x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '(cb*cx*ee*gp*Reta1x1)/sw + (cb*ee**2*Reta1x1*sx)/(2.*cw) + (ee**2*Reta1x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '-((cx*ee*gp*Reta2x1*sb)/sw) + (cb*ee**2*Reta2x2*sx)/(2.*cw) - (ee**2*Reta2x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '(cx*ee*gp*Reta2x1*sb)/sw - (cb*ee**2*Reta2x2*sx)/(2.*cw) + (ee**2*Reta2x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_254 = Coupling(name = 'GC_254',
                  value = '-((cb*cx*ee*gp*Reta2x1)/sw) - (cb*ee**2*Reta2x1*sx)/(2.*cw) - (ee**2*Reta2x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '(cb*cx*ee*gp*Reta2x1)/sw + (cb*ee**2*Reta2x1*sx)/(2.*cw) + (ee**2*Reta2x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '-((cx*ee*gp*Reta3x1*sb)/sw) + (cb*ee**2*Reta3x2*sx)/(2.*cw) - (ee**2*Reta3x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(cx*ee*gp*Reta3x1*sb)/sw - (cb*ee**2*Reta3x2*sx)/(2.*cw) + (ee**2*Reta3x1*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '-((cb*cx*ee*gp*Reta3x1)/sw) - (cb*ee**2*Reta3x1*sx)/(2.*cw) - (ee**2*Reta3x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(cb*cx*ee*gp*Reta3x1)/sw + (cb*ee**2*Reta3x1*sx)/(2.*cw) + (ee**2*Reta3x2*sb*sx)/(2.*cw)',
                  order = {'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '-0.5*(cb**2*cw*cx*ee*complex(0,1))/sw - (cw*cx*ee*complex(0,1)*sb**2)/(2.*sw) + (cb**2*cx*ee*complex(0,1)*sw)/(2.*cw) + (cx*ee*complex(0,1)*sb**2*sw)/(2.*cw) - complex(0,1)*gp*sb**2*sx',
                  order = {'QED':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '(cb**2*cw*cx*ee**2*complex(0,1))/sw + (cw*cx*ee**2*complex(0,1)*sb**2)/sw - (cb**2*cx*ee**2*complex(0,1)*sw)/cw - (cx*ee**2*complex(0,1)*sb**2*sw)/cw + 2*ee*complex(0,1)*gp*sb**2*sx',
                  order = {'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '(cn1*cw*cx*ee*complex(0,1)*sn1)/(2.*sw) + (cn1*cx*ee*complex(0,1)*sn1*sw)/(2.*cw) - cn1*complex(0,1)*gp*sn1*sx',
                  order = {'QED':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(cn1**2*cw*cx*ee*complex(0,1))/(2.*sw) + (cn1**2*cx*ee*complex(0,1)*sw)/(2.*cw) + complex(0,1)*gp*sn1**2*sx',
                  order = {'QED':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '(cn2*cw*cx*ee*complex(0,1)*sn2)/(2.*sw) + (cn2*cx*ee*complex(0,1)*sn2*sw)/(2.*cw) - cn2*complex(0,1)*gp*sn2*sx',
                  order = {'QED':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '(cn2**2*cw*cx*ee*complex(0,1))/(2.*sw) + (cn2**2*cx*ee*complex(0,1)*sw)/(2.*cw) + complex(0,1)*gp*sn2**2*sx',
                  order = {'QED':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '(cn3*cw*cx*ee*complex(0,1)*sn3)/(2.*sw) + (cn3*cx*ee*complex(0,1)*sn3*sw)/(2.*cw) - cn3*complex(0,1)*gp*sn3*sx',
                  order = {'QED':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '(cn3**2*cw*cx*ee*complex(0,1))/(2.*sw) + (cn3**2*cx*ee*complex(0,1)*sw)/(2.*cw) + complex(0,1)*gp*sn3**2*sx',
                  order = {'QED':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '-0.5*(cb*cx*ee**2*complex(0,1)*Rcp1x1)/cw - (cx*ee**2*complex(0,1)*Rcp1x2*sb)/(2.*cw) + (cb*ee*complex(0,1)*gp*Rcp1x1*sx)/sw',
                  order = {'QED':2})

GC_269 = Coupling(name = 'GC_269',
                  value = '-0.5*(cb*cx*ee**2*complex(0,1)*Rcp2x1)/cw - (cx*ee**2*complex(0,1)*Rcp2x2*sb)/(2.*cw) + (cb*ee*complex(0,1)*gp*Rcp2x1*sx)/sw',
                  order = {'QED':2})

GC_270 = Coupling(name = 'GC_270',
                  value = '-0.5*(cb*cx*ee**2*complex(0,1)*Rcp3x1)/cw - (cx*ee**2*complex(0,1)*Rcp3x2*sb)/(2.*cw) + (cb*ee*complex(0,1)*gp*Rcp3x1*sx)/sw',
                  order = {'QED':2})

GC_271 = Coupling(name = 'GC_271',
                  value = '(cb*cx*ee**2*Reta1x1)/(2.*cw) + (cx*ee**2*Reta1x2*sb)/(2.*cw) - (cb*ee*gp*Reta1x1*sx)/sw',
                  order = {'QED':2})

GC_272 = Coupling(name = 'GC_272',
                  value = '-0.5*(cb*cx*ee**2*Reta1x1)/cw - (cx*ee**2*Reta1x2*sb)/(2.*cw) + (cb*ee*gp*Reta1x1*sx)/sw',
                  order = {'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(cb*cx*ee**2*Reta2x1)/(2.*cw) + (cx*ee**2*Reta2x2*sb)/(2.*cw) - (cb*ee*gp*Reta2x1*sx)/sw',
                  order = {'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '-0.5*(cb*cx*ee**2*Reta2x1)/cw - (cx*ee**2*Reta2x2*sb)/(2.*cw) + (cb*ee*gp*Reta2x1*sx)/sw',
                  order = {'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '(cb*cx*ee**2*Reta3x1)/(2.*cw) + (cx*ee**2*Reta3x2*sb)/(2.*cw) - (cb*ee*gp*Reta3x1*sx)/sw',
                  order = {'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '-0.5*(cb*cx*ee**2*Reta3x1)/cw - (cx*ee**2*Reta3x2*sb)/(2.*cw) + (cb*ee*gp*Reta3x1*sx)/sw',
                  order = {'QED':2})

GC_277 = Coupling(name = 'GC_277',
                  value = '-0.5*(cb*cx*ee**2*complex(0,1)*Rcp1x2)/cw + (cx*ee**2*complex(0,1)*Rcp1x1*sb)/(2.*cw) - (ee*complex(0,1)*gp*Rcp1x1*sb*sx)/sw',
                  order = {'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '-0.5*(cb*cx*ee**2*complex(0,1)*Rcp2x2)/cw + (cx*ee**2*complex(0,1)*Rcp2x1*sb)/(2.*cw) - (ee*complex(0,1)*gp*Rcp2x1*sb*sx)/sw',
                  order = {'QED':2})

GC_279 = Coupling(name = 'GC_279',
                  value = '-0.5*(cb*cx*ee**2*complex(0,1)*Rcp3x2)/cw + (cx*ee**2*complex(0,1)*Rcp3x1*sb)/(2.*cw) - (ee*complex(0,1)*gp*Rcp3x1*sb*sx)/sw',
                  order = {'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '-0.5*(cb*cx*ee**2*Reta1x2)/cw + (cx*ee**2*Reta1x1*sb)/(2.*cw) - (ee*gp*Reta1x1*sb*sx)/sw',
                  order = {'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(cb*cx*ee**2*Reta1x2)/(2.*cw) - (cx*ee**2*Reta1x1*sb)/(2.*cw) + (ee*gp*Reta1x1*sb*sx)/sw',
                  order = {'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '-0.5*(cb*cx*ee**2*Reta2x2)/cw + (cx*ee**2*Reta2x1*sb)/(2.*cw) - (ee*gp*Reta2x1*sb*sx)/sw',
                  order = {'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(cb*cx*ee**2*Reta2x2)/(2.*cw) - (cx*ee**2*Reta2x1*sb)/(2.*cw) + (ee*gp*Reta2x1*sb*sx)/sw',
                  order = {'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '-0.5*(cb*cx*ee**2*Reta3x2)/cw + (cx*ee**2*Reta3x1*sb)/(2.*cw) - (ee*gp*Reta3x1*sb*sx)/sw',
                  order = {'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '(cb*cx*ee**2*Reta3x2)/(2.*cw) - (cx*ee**2*Reta3x1*sb)/(2.*cw) + (ee*gp*Reta3x1*sb*sx)/sw',
                  order = {'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = 'cx*complex(0,1)*gp - (cw*ee*complex(0,1)*sx)/(2.*sw) + (ee*complex(0,1)*sw*sx)/(6.*cw)',
                  order = {'QED':1})

GC_287 = Coupling(name = 'GC_287',
                  value = 'cx*complex(0,1)*gp + (cw*ee*complex(0,1)*sx)/(2.*sw) + (ee*complex(0,1)*sw*sx)/(6.*cw)',
                  order = {'QED':1})

GC_288 = Coupling(name = 'GC_288',
                  value = 'cx*complex(0,1)*gp - (ee*complex(0,1)*sw*sx)/(3.*cw)',
                  order = {'QED':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '(cw*ee*complex(0,1)*sx)/(2.*sw) - (ee*complex(0,1)*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_290 = Coupling(name = 'GC_290',
                  value = 'cx*complex(0,1)*gp + (2*ee*complex(0,1)*sw*sx)/(3.*cw)',
                  order = {'QED':1})

GC_291 = Coupling(name = 'GC_291',
                  value = 'cx*complex(0,1)*gp*sn1**2 - (cn1**2*cw*ee*complex(0,1)*sx)/(2.*sw) - (cn1**2*ee*complex(0,1)*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_292 = Coupling(name = 'GC_292',
                  value = 'cx*complex(0,1)*gp*sn2**2 - (cn2**2*cw*ee*complex(0,1)*sx)/(2.*sw) - (cn2**2*ee*complex(0,1)*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_293 = Coupling(name = 'GC_293',
                  value = 'cx*complex(0,1)*gp*sn3**2 - (cn3**2*cw*ee*complex(0,1)*sx)/(2.*sw) - (cn3**2*ee*complex(0,1)*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_294 = Coupling(name = 'GC_294',
                  value = 'cx*gp*Rcp1x1*Reta1x1 + cx*gp*Rcp1x3*Reta1x3 + (cw*ee*Rcp1x1*Reta1x1*sx)/(2.*sw) + (cw*ee*Rcp1x2*Reta1x2*sx)/(2.*sw) + (ee*Rcp1x1*Reta1x1*sw*sx)/(2.*cw) + (ee*Rcp1x2*Reta1x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_295 = Coupling(name = 'GC_295',
                  value = 'cx*gp*Rcp2x1*Reta1x1 + cx*gp*Rcp2x3*Reta1x3 + (cw*ee*Rcp2x1*Reta1x1*sx)/(2.*sw) + (cw*ee*Rcp2x2*Reta1x2*sx)/(2.*sw) + (ee*Rcp2x1*Reta1x1*sw*sx)/(2.*cw) + (ee*Rcp2x2*Reta1x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_296 = Coupling(name = 'GC_296',
                  value = 'cx*gp*Rcp3x1*Reta1x1 + cx*gp*Rcp3x3*Reta1x3 + (cw*ee*Rcp3x1*Reta1x1*sx)/(2.*sw) + (cw*ee*Rcp3x2*Reta1x2*sx)/(2.*sw) + (ee*Rcp3x1*Reta1x1*sw*sx)/(2.*cw) + (ee*Rcp3x2*Reta1x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_297 = Coupling(name = 'GC_297',
                  value = 'cx*gp*Rcp1x1*Reta2x1 + cx*gp*Rcp1x3*Reta2x3 + (cw*ee*Rcp1x1*Reta2x1*sx)/(2.*sw) + (cw*ee*Rcp1x2*Reta2x2*sx)/(2.*sw) + (ee*Rcp1x1*Reta2x1*sw*sx)/(2.*cw) + (ee*Rcp1x2*Reta2x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_298 = Coupling(name = 'GC_298',
                  value = 'cx*gp*Rcp2x1*Reta2x1 + cx*gp*Rcp2x3*Reta2x3 + (cw*ee*Rcp2x1*Reta2x1*sx)/(2.*sw) + (cw*ee*Rcp2x2*Reta2x2*sx)/(2.*sw) + (ee*Rcp2x1*Reta2x1*sw*sx)/(2.*cw) + (ee*Rcp2x2*Reta2x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_299 = Coupling(name = 'GC_299',
                  value = 'cx*gp*Rcp3x1*Reta2x1 + cx*gp*Rcp3x3*Reta2x3 + (cw*ee*Rcp3x1*Reta2x1*sx)/(2.*sw) + (cw*ee*Rcp3x2*Reta2x2*sx)/(2.*sw) + (ee*Rcp3x1*Reta2x1*sw*sx)/(2.*cw) + (ee*Rcp3x2*Reta2x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_300 = Coupling(name = 'GC_300',
                  value = 'cx*gp*Rcp1x1*Reta3x1 + cx*gp*Rcp1x3*Reta3x3 + (cw*ee*Rcp1x1*Reta3x1*sx)/(2.*sw) + (cw*ee*Rcp1x2*Reta3x2*sx)/(2.*sw) + (ee*Rcp1x1*Reta3x1*sw*sx)/(2.*cw) + (ee*Rcp1x2*Reta3x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_301 = Coupling(name = 'GC_301',
                  value = 'cx*gp*Rcp2x1*Reta3x1 + cx*gp*Rcp2x3*Reta3x3 + (cw*ee*Rcp2x1*Reta3x1*sx)/(2.*sw) + (cw*ee*Rcp2x2*Reta3x2*sx)/(2.*sw) + (ee*Rcp2x1*Reta3x1*sw*sx)/(2.*cw) + (ee*Rcp2x2*Reta3x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_302 = Coupling(name = 'GC_302',
                  value = 'cx*gp*Rcp3x1*Reta3x1 + cx*gp*Rcp3x3*Reta3x3 + (cw*ee*Rcp3x1*Reta3x1*sx)/(2.*sw) + (cw*ee*Rcp3x2*Reta3x2*sx)/(2.*sw) + (ee*Rcp3x1*Reta3x1*sw*sx)/(2.*cw) + (ee*Rcp3x2*Reta3x2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_303 = Coupling(name = 'GC_303',
                  value = '-2*cb*cx**2*complex(0,1)*gp**2*sb + (2*cb*cw*cx*ee*complex(0,1)*gp*sb*sx)/sw - (2*cb*cx*ee*complex(0,1)*gp*sb*sw*sx)/cw',
                  order = {'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '-(cb**2*cx*complex(0,1)*gp) + (cb**2*cw*ee*complex(0,1)*sx)/(2.*sw) + (cw*ee*complex(0,1)*sb**2*sx)/(2.*sw) - (cb**2*ee*complex(0,1)*sw*sx)/(2.*cw) - (ee*complex(0,1)*sb**2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '-(cx*complex(0,1)*gp*sb**2) + (cb**2*cw*ee*complex(0,1)*sx)/(2.*sw) + (cw*ee*complex(0,1)*sb**2*sx)/(2.*sw) - (cb**2*ee*complex(0,1)*sw*sx)/(2.*cw) - (ee*complex(0,1)*sb**2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '2*cb**2*cx*ee*complex(0,1)*gp - (cb**2*cw*ee**2*complex(0,1)*sx)/sw - (cw*ee**2*complex(0,1)*sb**2*sx)/sw + (cb**2*ee**2*complex(0,1)*sw*sx)/cw + (ee**2*complex(0,1)*sb**2*sw*sx)/cw',
                  order = {'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '2*cx*ee*complex(0,1)*gp*sb**2 - (cb**2*cw*ee**2*complex(0,1)*sx)/sw - (cw*ee**2*complex(0,1)*sb**2*sx)/sw + (cb**2*ee**2*complex(0,1)*sw*sx)/cw + (ee**2*complex(0,1)*sb**2*sw*sx)/cw',
                  order = {'QED':2})

GC_308 = Coupling(name = 'GC_308',
                  value = '-(cn1*cx*complex(0,1)*gp*sn1) - (cn1*cw*ee*complex(0,1)*sn1*sx)/(2.*sw) - (cn1*ee*complex(0,1)*sn1*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_309 = Coupling(name = 'GC_309',
                  value = 'cn1**2*cx*complex(0,1)*gp - (cw*ee*complex(0,1)*sn1**2*sx)/(2.*sw) - (ee*complex(0,1)*sn1**2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '-(cn2*cx*complex(0,1)*gp*sn2) - (cn2*cw*ee*complex(0,1)*sn2*sx)/(2.*sw) - (cn2*ee*complex(0,1)*sn2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_311 = Coupling(name = 'GC_311',
                  value = 'cn2**2*cx*complex(0,1)*gp - (cw*ee*complex(0,1)*sn2**2*sx)/(2.*sw) - (ee*complex(0,1)*sn2**2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_312 = Coupling(name = 'GC_312',
                  value = '-(cn3*cx*complex(0,1)*gp*sn3) - (cn3*cw*ee*complex(0,1)*sn3*sx)/(2.*sw) - (cn3*ee*complex(0,1)*sn3*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_313 = Coupling(name = 'GC_313',
                  value = 'cn3**2*cx*complex(0,1)*gp - (cw*ee*complex(0,1)*sn3**2*sx)/(2.*sw) - (ee*complex(0,1)*sn3**2*sw*sx)/(2.*cw)',
                  order = {'QED':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '-(cb**2*cx**2*ee**2*complex(0,1)) - cx**2*ee**2*complex(0,1)*sb**2 + (cb**2*cw**2*cx**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*cx**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2) + (2*cb**2*cw*cx*ee*complex(0,1)*gp*sx)/sw - (2*cb**2*cx*ee*complex(0,1)*gp*sw*sx)/cw + 2*cb**2*complex(0,1)*gp**2*sx**2',
                  order = {'QED':2})

GC_315 = Coupling(name = 'GC_315',
                  value = 'cx**2*ee**2*complex(0,1)*Rcp1x1**2 + cx**2*ee**2*complex(0,1)*Rcp1x2**2 + (cw**2*cx**2*ee**2*complex(0,1)*Rcp1x1**2)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp1x2**2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Rcp1x1**2*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp1x2**2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Rcp1x1**2*sx)/sw - (2*cx*ee*complex(0,1)*gp*Rcp1x1**2*sw*sx)/cw + 2*complex(0,1)*gp**2*Rcp1x1**2*sx**2 + 2*complex(0,1)*gp**2*Rcp1x3**2*sx**2',
                  order = {'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = 'cx**2*ee**2*complex(0,1)*Rcp1x1*Rcp2x1 + cx**2*ee**2*complex(0,1)*Rcp1x2*Rcp2x2 + (cw**2*cx**2*ee**2*complex(0,1)*Rcp1x1*Rcp2x1)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp1x2*Rcp2x2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Rcp1x1*Rcp2x1*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp1x2*Rcp2x2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Rcp1x1*Rcp2x1*sx)/sw - (2*cx*ee*complex(0,1)*gp*Rcp1x1*Rcp2x1*sw*sx)/cw + 2*complex(0,1)*gp**2*Rcp1x1*Rcp2x1*sx**2 + 2*complex(0,1)*gp**2*Rcp1x3*Rcp2x3*sx**2',
                  order = {'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = 'cx**2*ee**2*complex(0,1)*Rcp2x1**2 + cx**2*ee**2*complex(0,1)*Rcp2x2**2 + (cw**2*cx**2*ee**2*complex(0,1)*Rcp2x1**2)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp2x2**2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Rcp2x1**2*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp2x2**2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Rcp2x1**2*sx)/sw - (2*cx*ee*complex(0,1)*gp*Rcp2x1**2*sw*sx)/cw + 2*complex(0,1)*gp**2*Rcp2x1**2*sx**2 + 2*complex(0,1)*gp**2*Rcp2x3**2*sx**2',
                  order = {'QED':2})

GC_318 = Coupling(name = 'GC_318',
                  value = 'cx**2*ee**2*complex(0,1)*Rcp1x1*Rcp3x1 + cx**2*ee**2*complex(0,1)*Rcp1x2*Rcp3x2 + (cw**2*cx**2*ee**2*complex(0,1)*Rcp1x1*Rcp3x1)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp1x2*Rcp3x2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Rcp1x1*Rcp3x1*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp1x2*Rcp3x2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Rcp1x1*Rcp3x1*sx)/sw - (2*cx*ee*complex(0,1)*gp*Rcp1x1*Rcp3x1*sw*sx)/cw + 2*complex(0,1)*gp**2*Rcp1x1*Rcp3x1*sx**2 + 2*complex(0,1)*gp**2*Rcp1x3*Rcp3x3*sx**2',
                  order = {'QED':2})

GC_319 = Coupling(name = 'GC_319',
                  value = 'cx**2*ee**2*complex(0,1)*Rcp2x1*Rcp3x1 + cx**2*ee**2*complex(0,1)*Rcp2x2*Rcp3x2 + (cw**2*cx**2*ee**2*complex(0,1)*Rcp2x1*Rcp3x1)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp2x2*Rcp3x2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Rcp2x1*Rcp3x1*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp2x2*Rcp3x2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Rcp2x1*Rcp3x1*sx)/sw - (2*cx*ee*complex(0,1)*gp*Rcp2x1*Rcp3x1*sw*sx)/cw + 2*complex(0,1)*gp**2*Rcp2x1*Rcp3x1*sx**2 + 2*complex(0,1)*gp**2*Rcp2x3*Rcp3x3*sx**2',
                  order = {'QED':2})

GC_320 = Coupling(name = 'GC_320',
                  value = 'cx**2*ee**2*complex(0,1)*Rcp3x1**2 + cx**2*ee**2*complex(0,1)*Rcp3x2**2 + (cw**2*cx**2*ee**2*complex(0,1)*Rcp3x1**2)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp3x2**2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Rcp3x1**2*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp3x2**2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Rcp3x1**2*sx)/sw - (2*cx*ee*complex(0,1)*gp*Rcp3x1**2*sw*sx)/cw + 2*complex(0,1)*gp**2*Rcp3x1**2*sx**2 + 2*complex(0,1)*gp**2*Rcp3x3**2*sx**2',
                  order = {'QED':2})

GC_321 = Coupling(name = 'GC_321',
                  value = 'cx**2*ee**2*complex(0,1)*Reta1x1**2 + cx**2*ee**2*complex(0,1)*Reta1x2**2 + (cw**2*cx**2*ee**2*complex(0,1)*Reta1x1**2)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Reta1x2**2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Reta1x1**2*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Reta1x2**2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Reta1x1**2*sx)/sw - (2*cx*ee*complex(0,1)*gp*Reta1x1**2*sw*sx)/cw + 2*complex(0,1)*gp**2*Reta1x1**2*sx**2 + 2*complex(0,1)*gp**2*Reta1x3**2*sx**2',
                  order = {'QED':2})

GC_322 = Coupling(name = 'GC_322',
                  value = 'cx**2*ee**2*complex(0,1)*Reta1x1*Reta2x1 + cx**2*ee**2*complex(0,1)*Reta1x2*Reta2x2 + (cw**2*cx**2*ee**2*complex(0,1)*Reta1x1*Reta2x1)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Reta1x2*Reta2x2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Reta1x1*Reta2x1*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Reta1x2*Reta2x2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Reta1x1*Reta2x1*sx)/sw - (2*cx*ee*complex(0,1)*gp*Reta1x1*Reta2x1*sw*sx)/cw + 2*complex(0,1)*gp**2*Reta1x1*Reta2x1*sx**2 + 2*complex(0,1)*gp**2*Reta1x3*Reta2x3*sx**2',
                  order = {'QED':2})

GC_323 = Coupling(name = 'GC_323',
                  value = 'cx**2*ee**2*complex(0,1)*Reta2x1**2 + cx**2*ee**2*complex(0,1)*Reta2x2**2 + (cw**2*cx**2*ee**2*complex(0,1)*Reta2x1**2)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Reta2x2**2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Reta2x1**2*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Reta2x2**2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Reta2x1**2*sx)/sw - (2*cx*ee*complex(0,1)*gp*Reta2x1**2*sw*sx)/cw + 2*complex(0,1)*gp**2*Reta2x1**2*sx**2 + 2*complex(0,1)*gp**2*Reta2x3**2*sx**2',
                  order = {'QED':2})

GC_324 = Coupling(name = 'GC_324',
                  value = 'cx**2*ee**2*complex(0,1)*Reta1x1*Reta3x1 + cx**2*ee**2*complex(0,1)*Reta1x2*Reta3x2 + (cw**2*cx**2*ee**2*complex(0,1)*Reta1x1*Reta3x1)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Reta1x2*Reta3x2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Reta1x1*Reta3x1*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Reta1x2*Reta3x2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Reta1x1*Reta3x1*sx)/sw - (2*cx*ee*complex(0,1)*gp*Reta1x1*Reta3x1*sw*sx)/cw + 2*complex(0,1)*gp**2*Reta1x1*Reta3x1*sx**2 + 2*complex(0,1)*gp**2*Reta1x3*Reta3x3*sx**2',
                  order = {'QED':2})

GC_325 = Coupling(name = 'GC_325',
                  value = 'cx**2*ee**2*complex(0,1)*Reta2x1*Reta3x1 + cx**2*ee**2*complex(0,1)*Reta2x2*Reta3x2 + (cw**2*cx**2*ee**2*complex(0,1)*Reta2x1*Reta3x1)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Reta2x2*Reta3x2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Reta2x1*Reta3x1*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Reta2x2*Reta3x2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Reta2x1*Reta3x1*sx)/sw - (2*cx*ee*complex(0,1)*gp*Reta2x1*Reta3x1*sw*sx)/cw + 2*complex(0,1)*gp**2*Reta2x1*Reta3x1*sx**2 + 2*complex(0,1)*gp**2*Reta2x3*Reta3x3*sx**2',
                  order = {'QED':2})

GC_326 = Coupling(name = 'GC_326',
                  value = 'cx**2*ee**2*complex(0,1)*Reta3x1**2 + cx**2*ee**2*complex(0,1)*Reta3x2**2 + (cw**2*cx**2*ee**2*complex(0,1)*Reta3x1**2)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Reta3x2**2)/(2.*sw**2) + (cx**2*ee**2*complex(0,1)*Reta3x1**2*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Reta3x2**2*sw**2)/(2.*cw**2) - (2*cw*cx*ee*complex(0,1)*gp*Reta3x1**2*sx)/sw - (2*cx*ee*complex(0,1)*gp*Reta3x1**2*sw*sx)/cw + 2*complex(0,1)*gp**2*Reta3x1**2*sx**2 + 2*complex(0,1)*gp**2*Reta3x3**2*sx**2',
                  order = {'QED':2})

GC_327 = Coupling(name = 'GC_327',
                  value = '(-2*cb*cw*cx*ee*complex(0,1)*gp*sb*sx)/sw + (2*cb*cx*ee*complex(0,1)*gp*sb*sw*sx)/cw - 2*cb*complex(0,1)*gp**2*sb*sx**2',
                  order = {'QED':2})

GC_328 = Coupling(name = 'GC_328',
                  value = '-(cb**2*cx**2*ee**2*complex(0,1)) - cx**2*ee**2*complex(0,1)*sb**2 + (cb**2*cw**2*cx**2*ee**2*complex(0,1))/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*sb**2)/(2.*sw**2) + (cb**2*cx**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*sb**2*sw**2)/(2.*cw**2) + (2*cw*cx*ee*complex(0,1)*gp*sb**2*sx)/sw - (2*cx*ee*complex(0,1)*gp*sb**2*sw*sx)/cw + 2*complex(0,1)*gp**2*sb**2*sx**2',
                  order = {'QED':2})

GC_329 = Coupling(name = 'GC_329',
                  value = '(cb**2*cw*cx**2*ee*complex(0,1)*gp)/sw - (cb**2*cx**2*ee*complex(0,1)*gp*sw)/cw + cb**2*cx*ee**2*complex(0,1)*sx + 2*cb**2*cx*complex(0,1)*gp**2*sx + cx*ee**2*complex(0,1)*sb**2*sx - (cb**2*cw**2*cx*ee**2*complex(0,1)*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*sb**2*sx)/(2.*sw**2) - (cb**2*cx*ee**2*complex(0,1)*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*sb**2*sw**2*sx)/(2.*cw**2) - (cb**2*cw*ee*complex(0,1)*gp*sx**2)/sw + (cb**2*ee*complex(0,1)*gp*sw*sx**2)/cw',
                  order = {'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Rcp1x1**2)/sw) - (cx**2*ee*complex(0,1)*gp*Rcp1x1**2*sw)/cw - cx*ee**2*complex(0,1)*Rcp1x1**2*sx + 2*cx*complex(0,1)*gp**2*Rcp1x1**2*sx - cx*ee**2*complex(0,1)*Rcp1x2**2*sx + 2*cx*complex(0,1)*gp**2*Rcp1x3**2*sx - (cw**2*cx*ee**2*complex(0,1)*Rcp1x1**2*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp1x2**2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Rcp1x1**2*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp1x2**2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Rcp1x1**2*sx**2)/sw + (ee*complex(0,1)*gp*Rcp1x1**2*sw*sx**2)/cw',
                  order = {'QED':2})

GC_331 = Coupling(name = 'GC_331',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Rcp1x1*Rcp2x1)/sw) - (cx**2*ee*complex(0,1)*gp*Rcp1x1*Rcp2x1*sw)/cw - cx*ee**2*complex(0,1)*Rcp1x1*Rcp2x1*sx + 2*cx*complex(0,1)*gp**2*Rcp1x1*Rcp2x1*sx - cx*ee**2*complex(0,1)*Rcp1x2*Rcp2x2*sx + 2*cx*complex(0,1)*gp**2*Rcp1x3*Rcp2x3*sx - (cw**2*cx*ee**2*complex(0,1)*Rcp1x1*Rcp2x1*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp1x2*Rcp2x2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Rcp1x1*Rcp2x1*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp1x2*Rcp2x2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Rcp1x1*Rcp2x1*sx**2)/sw + (ee*complex(0,1)*gp*Rcp1x1*Rcp2x1*sw*sx**2)/cw',
                  order = {'QED':2})

GC_332 = Coupling(name = 'GC_332',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Rcp2x1**2)/sw) - (cx**2*ee*complex(0,1)*gp*Rcp2x1**2*sw)/cw - cx*ee**2*complex(0,1)*Rcp2x1**2*sx + 2*cx*complex(0,1)*gp**2*Rcp2x1**2*sx - cx*ee**2*complex(0,1)*Rcp2x2**2*sx + 2*cx*complex(0,1)*gp**2*Rcp2x3**2*sx - (cw**2*cx*ee**2*complex(0,1)*Rcp2x1**2*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp2x2**2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Rcp2x1**2*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp2x2**2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Rcp2x1**2*sx**2)/sw + (ee*complex(0,1)*gp*Rcp2x1**2*sw*sx**2)/cw',
                  order = {'QED':2})

GC_333 = Coupling(name = 'GC_333',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Rcp1x1*Rcp3x1)/sw) - (cx**2*ee*complex(0,1)*gp*Rcp1x1*Rcp3x1*sw)/cw - cx*ee**2*complex(0,1)*Rcp1x1*Rcp3x1*sx + 2*cx*complex(0,1)*gp**2*Rcp1x1*Rcp3x1*sx - cx*ee**2*complex(0,1)*Rcp1x2*Rcp3x2*sx + 2*cx*complex(0,1)*gp**2*Rcp1x3*Rcp3x3*sx - (cw**2*cx*ee**2*complex(0,1)*Rcp1x1*Rcp3x1*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp1x2*Rcp3x2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Rcp1x1*Rcp3x1*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp1x2*Rcp3x2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Rcp1x1*Rcp3x1*sx**2)/sw + (ee*complex(0,1)*gp*Rcp1x1*Rcp3x1*sw*sx**2)/cw',
                  order = {'QED':2})

GC_334 = Coupling(name = 'GC_334',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Rcp2x1*Rcp3x1)/sw) - (cx**2*ee*complex(0,1)*gp*Rcp2x1*Rcp3x1*sw)/cw - cx*ee**2*complex(0,1)*Rcp2x1*Rcp3x1*sx + 2*cx*complex(0,1)*gp**2*Rcp2x1*Rcp3x1*sx - cx*ee**2*complex(0,1)*Rcp2x2*Rcp3x2*sx + 2*cx*complex(0,1)*gp**2*Rcp2x3*Rcp3x3*sx - (cw**2*cx*ee**2*complex(0,1)*Rcp2x1*Rcp3x1*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp2x2*Rcp3x2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Rcp2x1*Rcp3x1*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp2x2*Rcp3x2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Rcp2x1*Rcp3x1*sx**2)/sw + (ee*complex(0,1)*gp*Rcp2x1*Rcp3x1*sw*sx**2)/cw',
                  order = {'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Rcp3x1**2)/sw) - (cx**2*ee*complex(0,1)*gp*Rcp3x1**2*sw)/cw - cx*ee**2*complex(0,1)*Rcp3x1**2*sx + 2*cx*complex(0,1)*gp**2*Rcp3x1**2*sx - cx*ee**2*complex(0,1)*Rcp3x2**2*sx + 2*cx*complex(0,1)*gp**2*Rcp3x3**2*sx - (cw**2*cx*ee**2*complex(0,1)*Rcp3x1**2*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp3x2**2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Rcp3x1**2*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp3x2**2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Rcp3x1**2*sx**2)/sw + (ee*complex(0,1)*gp*Rcp3x1**2*sw*sx**2)/cw',
                  order = {'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Reta1x1**2)/sw) - (cx**2*ee*complex(0,1)*gp*Reta1x1**2*sw)/cw - cx*ee**2*complex(0,1)*Reta1x1**2*sx + 2*cx*complex(0,1)*gp**2*Reta1x1**2*sx - cx*ee**2*complex(0,1)*Reta1x2**2*sx + 2*cx*complex(0,1)*gp**2*Reta1x3**2*sx - (cw**2*cx*ee**2*complex(0,1)*Reta1x1**2*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Reta1x2**2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Reta1x1**2*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Reta1x2**2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Reta1x1**2*sx**2)/sw + (ee*complex(0,1)*gp*Reta1x1**2*sw*sx**2)/cw',
                  order = {'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Reta1x1*Reta2x1)/sw) - (cx**2*ee*complex(0,1)*gp*Reta1x1*Reta2x1*sw)/cw - cx*ee**2*complex(0,1)*Reta1x1*Reta2x1*sx + 2*cx*complex(0,1)*gp**2*Reta1x1*Reta2x1*sx - cx*ee**2*complex(0,1)*Reta1x2*Reta2x2*sx + 2*cx*complex(0,1)*gp**2*Reta1x3*Reta2x3*sx - (cw**2*cx*ee**2*complex(0,1)*Reta1x1*Reta2x1*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Reta1x2*Reta2x2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Reta1x1*Reta2x1*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Reta1x2*Reta2x2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Reta1x1*Reta2x1*sx**2)/sw + (ee*complex(0,1)*gp*Reta1x1*Reta2x1*sw*sx**2)/cw',
                  order = {'QED':2})

GC_338 = Coupling(name = 'GC_338',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Reta2x1**2)/sw) - (cx**2*ee*complex(0,1)*gp*Reta2x1**2*sw)/cw - cx*ee**2*complex(0,1)*Reta2x1**2*sx + 2*cx*complex(0,1)*gp**2*Reta2x1**2*sx - cx*ee**2*complex(0,1)*Reta2x2**2*sx + 2*cx*complex(0,1)*gp**2*Reta2x3**2*sx - (cw**2*cx*ee**2*complex(0,1)*Reta2x1**2*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Reta2x2**2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Reta2x1**2*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Reta2x2**2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Reta2x1**2*sx**2)/sw + (ee*complex(0,1)*gp*Reta2x1**2*sw*sx**2)/cw',
                  order = {'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Reta1x1*Reta3x1)/sw) - (cx**2*ee*complex(0,1)*gp*Reta1x1*Reta3x1*sw)/cw - cx*ee**2*complex(0,1)*Reta1x1*Reta3x1*sx + 2*cx*complex(0,1)*gp**2*Reta1x1*Reta3x1*sx - cx*ee**2*complex(0,1)*Reta1x2*Reta3x2*sx + 2*cx*complex(0,1)*gp**2*Reta1x3*Reta3x3*sx - (cw**2*cx*ee**2*complex(0,1)*Reta1x1*Reta3x1*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Reta1x2*Reta3x2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Reta1x1*Reta3x1*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Reta1x2*Reta3x2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Reta1x1*Reta3x1*sx**2)/sw + (ee*complex(0,1)*gp*Reta1x1*Reta3x1*sw*sx**2)/cw',
                  order = {'QED':2})

GC_340 = Coupling(name = 'GC_340',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Reta2x1*Reta3x1)/sw) - (cx**2*ee*complex(0,1)*gp*Reta2x1*Reta3x1*sw)/cw - cx*ee**2*complex(0,1)*Reta2x1*Reta3x1*sx + 2*cx*complex(0,1)*gp**2*Reta2x1*Reta3x1*sx - cx*ee**2*complex(0,1)*Reta2x2*Reta3x2*sx + 2*cx*complex(0,1)*gp**2*Reta2x3*Reta3x3*sx - (cw**2*cx*ee**2*complex(0,1)*Reta2x1*Reta3x1*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Reta2x2*Reta3x2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Reta2x1*Reta3x1*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Reta2x2*Reta3x2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Reta2x1*Reta3x1*sx**2)/sw + (ee*complex(0,1)*gp*Reta2x1*Reta3x1*sw*sx**2)/cw',
                  order = {'QED':2})

GC_341 = Coupling(name = 'GC_341',
                  value = '-((cw*cx**2*ee*complex(0,1)*gp*Reta3x1**2)/sw) - (cx**2*ee*complex(0,1)*gp*Reta3x1**2*sw)/cw - cx*ee**2*complex(0,1)*Reta3x1**2*sx + 2*cx*complex(0,1)*gp**2*Reta3x1**2*sx - cx*ee**2*complex(0,1)*Reta3x2**2*sx + 2*cx*complex(0,1)*gp**2*Reta3x3**2*sx - (cw**2*cx*ee**2*complex(0,1)*Reta3x1**2*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Reta3x2**2*sx)/(2.*sw**2) - (cx*ee**2*complex(0,1)*Reta3x1**2*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Reta3x2**2*sw**2*sx)/(2.*cw**2) + (cw*ee*complex(0,1)*gp*Reta3x1**2*sx**2)/sw + (ee*complex(0,1)*gp*Reta3x1**2*sw*sx**2)/cw',
                  order = {'QED':2})

GC_342 = Coupling(name = 'GC_342',
                  value = '-((cb*cw*cx**2*ee*complex(0,1)*gp*sb)/sw) + (cb*cx**2*ee*complex(0,1)*gp*sb*sw)/cw - 2*cb*cx*complex(0,1)*gp**2*sb*sx + (cb*cw*ee*complex(0,1)*gp*sb*sx**2)/sw - (cb*ee*complex(0,1)*gp*sb*sw*sx**2)/cw',
                  order = {'QED':2})

GC_343 = Coupling(name = 'GC_343',
                  value = '(cw*cx**2*ee*complex(0,1)*gp*sb**2)/sw - (cx**2*ee*complex(0,1)*gp*sb**2*sw)/cw + cb**2*cx*ee**2*complex(0,1)*sx + cx*ee**2*complex(0,1)*sb**2*sx + 2*cx*complex(0,1)*gp**2*sb**2*sx - (cb**2*cw**2*cx*ee**2*complex(0,1)*sx)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*sb**2*sx)/(2.*sw**2) - (cb**2*cx*ee**2*complex(0,1)*sw**2*sx)/(2.*cw**2) - (cx*ee**2*complex(0,1)*sb**2*sw**2*sx)/(2.*cw**2) - (cw*ee*complex(0,1)*gp*sb**2*sx**2)/sw + (ee*complex(0,1)*gp*sb**2*sw*sx**2)/cw',
                  order = {'QED':2})

GC_344 = Coupling(name = 'GC_344',
                  value = '2*cx**2*complex(0,1)*gp**2*Rcp1x1**2 + 2*cx**2*complex(0,1)*gp**2*Rcp1x3**2 + (2*cw*cx*ee*complex(0,1)*gp*Rcp1x1**2*sx)/sw + (2*cx*ee*complex(0,1)*gp*Rcp1x1**2*sw*sx)/cw + ee**2*complex(0,1)*Rcp1x1**2*sx**2 + ee**2*complex(0,1)*Rcp1x2**2*sx**2 + (cw**2*ee**2*complex(0,1)*Rcp1x1**2*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp1x2**2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp1x1**2*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp1x2**2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '2*cx**2*complex(0,1)*gp**2*Rcp1x1*Rcp2x1 + 2*cx**2*complex(0,1)*gp**2*Rcp1x3*Rcp2x3 + (2*cw*cx*ee*complex(0,1)*gp*Rcp1x1*Rcp2x1*sx)/sw + (2*cx*ee*complex(0,1)*gp*Rcp1x1*Rcp2x1*sw*sx)/cw + ee**2*complex(0,1)*Rcp1x1*Rcp2x1*sx**2 + ee**2*complex(0,1)*Rcp1x2*Rcp2x2*sx**2 + (cw**2*ee**2*complex(0,1)*Rcp1x1*Rcp2x1*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp1x2*Rcp2x2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp1x1*Rcp2x1*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp1x2*Rcp2x2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '2*cx**2*complex(0,1)*gp**2*Rcp2x1**2 + 2*cx**2*complex(0,1)*gp**2*Rcp2x3**2 + (2*cw*cx*ee*complex(0,1)*gp*Rcp2x1**2*sx)/sw + (2*cx*ee*complex(0,1)*gp*Rcp2x1**2*sw*sx)/cw + ee**2*complex(0,1)*Rcp2x1**2*sx**2 + ee**2*complex(0,1)*Rcp2x2**2*sx**2 + (cw**2*ee**2*complex(0,1)*Rcp2x1**2*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp2x2**2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp2x1**2*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp2x2**2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '2*cx**2*complex(0,1)*gp**2*Rcp1x1*Rcp3x1 + 2*cx**2*complex(0,1)*gp**2*Rcp1x3*Rcp3x3 + (2*cw*cx*ee*complex(0,1)*gp*Rcp1x1*Rcp3x1*sx)/sw + (2*cx*ee*complex(0,1)*gp*Rcp1x1*Rcp3x1*sw*sx)/cw + ee**2*complex(0,1)*Rcp1x1*Rcp3x1*sx**2 + ee**2*complex(0,1)*Rcp1x2*Rcp3x2*sx**2 + (cw**2*ee**2*complex(0,1)*Rcp1x1*Rcp3x1*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp1x2*Rcp3x2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp1x1*Rcp3x1*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp1x2*Rcp3x2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_348 = Coupling(name = 'GC_348',
                  value = '2*cx**2*complex(0,1)*gp**2*Rcp2x1*Rcp3x1 + 2*cx**2*complex(0,1)*gp**2*Rcp2x3*Rcp3x3 + (2*cw*cx*ee*complex(0,1)*gp*Rcp2x1*Rcp3x1*sx)/sw + (2*cx*ee*complex(0,1)*gp*Rcp2x1*Rcp3x1*sw*sx)/cw + ee**2*complex(0,1)*Rcp2x1*Rcp3x1*sx**2 + ee**2*complex(0,1)*Rcp2x2*Rcp3x2*sx**2 + (cw**2*ee**2*complex(0,1)*Rcp2x1*Rcp3x1*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp2x2*Rcp3x2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp2x1*Rcp3x1*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp2x2*Rcp3x2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_349 = Coupling(name = 'GC_349',
                  value = '2*cx**2*complex(0,1)*gp**2*Rcp3x1**2 + 2*cx**2*complex(0,1)*gp**2*Rcp3x3**2 + (2*cw*cx*ee*complex(0,1)*gp*Rcp3x1**2*sx)/sw + (2*cx*ee*complex(0,1)*gp*Rcp3x1**2*sw*sx)/cw + ee**2*complex(0,1)*Rcp3x1**2*sx**2 + ee**2*complex(0,1)*Rcp3x2**2*sx**2 + (cw**2*ee**2*complex(0,1)*Rcp3x1**2*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp3x2**2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp3x1**2*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp3x2**2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_350 = Coupling(name = 'GC_350',
                  value = '2*cx**2*complex(0,1)*gp**2*Reta1x1**2 + 2*cx**2*complex(0,1)*gp**2*Reta1x3**2 + (2*cw*cx*ee*complex(0,1)*gp*Reta1x1**2*sx)/sw + (2*cx*ee*complex(0,1)*gp*Reta1x1**2*sw*sx)/cw + ee**2*complex(0,1)*Reta1x1**2*sx**2 + ee**2*complex(0,1)*Reta1x2**2*sx**2 + (cw**2*ee**2*complex(0,1)*Reta1x1**2*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Reta1x2**2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta1x1**2*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Reta1x2**2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_351 = Coupling(name = 'GC_351',
                  value = '2*cx**2*complex(0,1)*gp**2*Reta1x1*Reta2x1 + 2*cx**2*complex(0,1)*gp**2*Reta1x3*Reta2x3 + (2*cw*cx*ee*complex(0,1)*gp*Reta1x1*Reta2x1*sx)/sw + (2*cx*ee*complex(0,1)*gp*Reta1x1*Reta2x1*sw*sx)/cw + ee**2*complex(0,1)*Reta1x1*Reta2x1*sx**2 + ee**2*complex(0,1)*Reta1x2*Reta2x2*sx**2 + (cw**2*ee**2*complex(0,1)*Reta1x1*Reta2x1*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Reta1x2*Reta2x2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta1x1*Reta2x1*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Reta1x2*Reta2x2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_352 = Coupling(name = 'GC_352',
                  value = '2*cx**2*complex(0,1)*gp**2*Reta2x1**2 + 2*cx**2*complex(0,1)*gp**2*Reta2x3**2 + (2*cw*cx*ee*complex(0,1)*gp*Reta2x1**2*sx)/sw + (2*cx*ee*complex(0,1)*gp*Reta2x1**2*sw*sx)/cw + ee**2*complex(0,1)*Reta2x1**2*sx**2 + ee**2*complex(0,1)*Reta2x2**2*sx**2 + (cw**2*ee**2*complex(0,1)*Reta2x1**2*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Reta2x2**2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta2x1**2*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Reta2x2**2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_353 = Coupling(name = 'GC_353',
                  value = '2*cx**2*complex(0,1)*gp**2*Reta1x1*Reta3x1 + 2*cx**2*complex(0,1)*gp**2*Reta1x3*Reta3x3 + (2*cw*cx*ee*complex(0,1)*gp*Reta1x1*Reta3x1*sx)/sw + (2*cx*ee*complex(0,1)*gp*Reta1x1*Reta3x1*sw*sx)/cw + ee**2*complex(0,1)*Reta1x1*Reta3x1*sx**2 + ee**2*complex(0,1)*Reta1x2*Reta3x2*sx**2 + (cw**2*ee**2*complex(0,1)*Reta1x1*Reta3x1*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Reta1x2*Reta3x2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta1x1*Reta3x1*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Reta1x2*Reta3x2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_354 = Coupling(name = 'GC_354',
                  value = '2*cx**2*complex(0,1)*gp**2*Reta2x1*Reta3x1 + 2*cx**2*complex(0,1)*gp**2*Reta2x3*Reta3x3 + (2*cw*cx*ee*complex(0,1)*gp*Reta2x1*Reta3x1*sx)/sw + (2*cx*ee*complex(0,1)*gp*Reta2x1*Reta3x1*sw*sx)/cw + ee**2*complex(0,1)*Reta2x1*Reta3x1*sx**2 + ee**2*complex(0,1)*Reta2x2*Reta3x2*sx**2 + (cw**2*ee**2*complex(0,1)*Reta2x1*Reta3x1*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Reta2x2*Reta3x2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta2x1*Reta3x1*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Reta2x2*Reta3x2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_355 = Coupling(name = 'GC_355',
                  value = '2*cx**2*complex(0,1)*gp**2*Reta3x1**2 + 2*cx**2*complex(0,1)*gp**2*Reta3x3**2 + (2*cw*cx*ee*complex(0,1)*gp*Reta3x1**2*sx)/sw + (2*cx*ee*complex(0,1)*gp*Reta3x1**2*sw*sx)/cw + ee**2*complex(0,1)*Reta3x1**2*sx**2 + ee**2*complex(0,1)*Reta3x2**2*sx**2 + (cw**2*ee**2*complex(0,1)*Reta3x1**2*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Reta3x2**2*sx**2)/(2.*sw**2) + (ee**2*complex(0,1)*Reta3x1**2*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*Reta3x2**2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_356 = Coupling(name = 'GC_356',
                  value = '2*cb**2*cx**2*complex(0,1)*gp**2 - (2*cb**2*cw*cx*ee*complex(0,1)*gp*sx)/sw + (2*cb**2*cx*ee*complex(0,1)*gp*sw*sx)/cw - cb**2*ee**2*complex(0,1)*sx**2 - ee**2*complex(0,1)*sb**2*sx**2 + (cb**2*cw**2*ee**2*complex(0,1)*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2*sx**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = '2*cx**2*complex(0,1)*gp**2*sb**2 - (2*cw*cx*ee*complex(0,1)*gp*sb**2*sx)/sw + (2*cx*ee*complex(0,1)*gp*sb**2*sw*sx)/cw - cb**2*ee**2*complex(0,1)*sx**2 - ee**2*complex(0,1)*sb**2*sx**2 + (cb**2*cw**2*ee**2*complex(0,1)*sx**2)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*sb**2*sx**2)/(2.*sw**2) + (cb**2*ee**2*complex(0,1)*sw**2*sx**2)/(2.*cw**2) + (ee**2*complex(0,1)*sb**2*sw**2*sx**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_358 = Coupling(name = 'GC_358',
                  value = '-((cb*cx*ee*complex(0,1)*gp*sb*vev)/sw)',
                  order = {'QED':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '-((cb*ee*complex(0,1)*gp*sb*sx*vev)/sw)',
                  order = {'QED':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(cb**3*lamm*Reta1x2*vev)/2. - (cb**2*lamm*Reta1x1*sb*vev)/2. + (cb*lamm*Reta1x2*sb**2*vev)/2. - (lamm*Reta1x1*sb**3*vev)/2. - (cb**2*lama*Reta1x3)/cmath.sqrt(2) - (lama*Reta1x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-0.5*(cb**3*lamm*Reta1x2*vev) + (cb**2*lamm*Reta1x1*sb*vev)/2. - (cb*lamm*Reta1x2*sb**2*vev)/2. + (lamm*Reta1x1*sb**3*vev)/2. + (cb**2*lama*Reta1x3)/cmath.sqrt(2) + (lama*Reta1x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(cb**3*lamm*Reta2x2*vev)/2. - (cb**2*lamm*Reta2x1*sb*vev)/2. + (cb*lamm*Reta2x2*sb**2*vev)/2. - (lamm*Reta2x1*sb**3*vev)/2. - (cb**2*lama*Reta2x3)/cmath.sqrt(2) - (lama*Reta2x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '-0.5*(cb**3*lamm*Reta2x2*vev) + (cb**2*lamm*Reta2x1*sb*vev)/2. - (cb*lamm*Reta2x2*sb**2*vev)/2. + (lamm*Reta2x1*sb**3*vev)/2. + (cb**2*lama*Reta2x3)/cmath.sqrt(2) + (lama*Reta2x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(cb**3*lamm*Reta3x2*vev)/2. - (cb**2*lamm*Reta3x1*sb*vev)/2. + (cb*lamm*Reta3x2*sb**2*vev)/2. - (lamm*Reta3x1*sb**3*vev)/2. - (cb**2*lama*Reta3x3)/cmath.sqrt(2) - (lama*Reta3x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '-0.5*(cb**3*lamm*Reta3x2*vev) + (cb**2*lamm*Reta3x1*sb*vev)/2. - (cb*lamm*Reta3x2*sb**2*vev)/2. + (lamm*Reta3x1*sb**3*vev)/2. + (cb**2*lama*Reta3x3)/cmath.sqrt(2) + (lama*Reta3x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(cb*ee**2*complex(0,1)*Rcp1x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp1x2*sb*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '(cb*ee**2*complex(0,1)*Rcp2x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp2x2*sb*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '(cb*ee**2*complex(0,1)*Rcp3x1*vev)/(2.*sw**2) + (ee**2*complex(0,1)*Rcp3x2*sb*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '(cb**2*ee**2*complex(0,1)*vev)/(2.*sw) + (ee**2*complex(0,1)*sb**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_370 = Coupling(name = 'GC_370',
                  value = '(cb**2*cx*ee*complex(0,1)*gp*vev)/sw + (cb**2*ee**2*complex(0,1)*sx*vev)/(2.*cw) + (ee**2*complex(0,1)*sb**2*sx*vev)/(2.*cw)',
                  order = {'QED':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '-0.5*(cb**2*cx*ee**2*complex(0,1)*vev)/cw - (cx*ee**2*complex(0,1)*sb**2*vev)/(2.*cw) + (cb**2*ee*complex(0,1)*gp*sx*vev)/sw',
                  order = {'QED':1})

GC_372 = Coupling(name = 'GC_372',
                  value = '2*cb*cx**2*complex(0,1)*gp**2*Rcp1x1*vev + (2*cb*cw*cx*ee*complex(0,1)*gp*Rcp1x1*sx*vev)/sw + (2*cb*cx*ee*complex(0,1)*gp*Rcp1x1*sw*sx*vev)/cw + cb*ee**2*complex(0,1)*Rcp1x1*sx**2*vev + ee**2*complex(0,1)*Rcp1x2*sb*sx**2*vev + (cb*cw**2*ee**2*complex(0,1)*Rcp1x1*sx**2*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp1x2*sb*sx**2*vev)/(2.*sw**2) + (cb*ee**2*complex(0,1)*Rcp1x1*sw**2*sx**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp1x2*sb*sw**2*sx**2*vev)/(2.*cw**2) + 2*cx**2*complex(0,1)*gp**2*Rcp1x3*vevs',
                  order = {'QED':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '-3*cb*complex(0,1)*lam1*Rcp1x1**3*vev - 3*cb*complex(0,1)*lamd*Rcp1x1*Rcp1x2**2*vev - 3*cb*complex(0,1)*lamm*Rcp1x1*Rcp1x2**2*vev - 3*cb*complex(0,1)*lam1s*Rcp1x1*Rcp1x3**2*vev - 3*complex(0,1)*lamd*Rcp1x1**2*Rcp1x2*sb*vev - 3*complex(0,1)*lamm*Rcp1x1**2*Rcp1x2*sb*vev - 3*complex(0,1)*lam2*Rcp1x2**3*sb*vev - 3*complex(0,1)*lam2s*Rcp1x2*Rcp1x3**2*sb*vev - 3*complex(0,1)*lam1s*Rcp1x1**2*Rcp1x3*vevs - 3*complex(0,1)*lam2s*Rcp1x2**2*Rcp1x3*vevs - 3*complex(0,1)*lams*Rcp1x3**3*vevs - 3*complex(0,1)*lama*Rcp1x1*Rcp1x2*Rcp1x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_374 = Coupling(name = 'GC_374',
                  value = '2*cb*cx**2*complex(0,1)*gp**2*Rcp2x1*vev + (2*cb*cw*cx*ee*complex(0,1)*gp*Rcp2x1*sx*vev)/sw + (2*cb*cx*ee*complex(0,1)*gp*Rcp2x1*sw*sx*vev)/cw + cb*ee**2*complex(0,1)*Rcp2x1*sx**2*vev + ee**2*complex(0,1)*Rcp2x2*sb*sx**2*vev + (cb*cw**2*ee**2*complex(0,1)*Rcp2x1*sx**2*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp2x2*sb*sx**2*vev)/(2.*sw**2) + (cb*ee**2*complex(0,1)*Rcp2x1*sw**2*sx**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp2x2*sb*sw**2*sx**2*vev)/(2.*cw**2) + 2*cx**2*complex(0,1)*gp**2*Rcp2x3*vevs',
                  order = {'QED':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '-3*cb*complex(0,1)*lam1*Rcp1x1**2*Rcp2x1*vev - cb*complex(0,1)*lamd*Rcp1x2**2*Rcp2x1*vev - cb*complex(0,1)*lamm*Rcp1x2**2*Rcp2x1*vev - cb*complex(0,1)*lam1s*Rcp1x3**2*Rcp2x1*vev - 2*cb*complex(0,1)*lamd*Rcp1x1*Rcp1x2*Rcp2x2*vev - 2*cb*complex(0,1)*lamm*Rcp1x1*Rcp1x2*Rcp2x2*vev - 2*cb*complex(0,1)*lam1s*Rcp1x1*Rcp1x3*Rcp2x3*vev - 2*complex(0,1)*lamd*Rcp1x1*Rcp1x2*Rcp2x1*sb*vev - 2*complex(0,1)*lamm*Rcp1x1*Rcp1x2*Rcp2x1*sb*vev - complex(0,1)*lamd*Rcp1x1**2*Rcp2x2*sb*vev - complex(0,1)*lamm*Rcp1x1**2*Rcp2x2*sb*vev - 3*complex(0,1)*lam2*Rcp1x2**2*Rcp2x2*sb*vev - complex(0,1)*lam2s*Rcp1x3**2*Rcp2x2*sb*vev - 2*complex(0,1)*lam2s*Rcp1x2*Rcp1x3*Rcp2x3*sb*vev - 2*complex(0,1)*lam1s*Rcp1x1*Rcp1x3*Rcp2x1*vevs - 2*complex(0,1)*lam2s*Rcp1x2*Rcp1x3*Rcp2x2*vevs - complex(0,1)*lam1s*Rcp1x1**2*Rcp2x3*vevs - complex(0,1)*lam2s*Rcp1x2**2*Rcp2x3*vevs - 3*complex(0,1)*lams*Rcp1x3**2*Rcp2x3*vevs - complex(0,1)*lama*Rcp1x2*Rcp1x3*Rcp2x1*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x1*Rcp1x3*Rcp2x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x1*Rcp1x2*Rcp2x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '-3*cb*complex(0,1)*lam1*Rcp1x1*Rcp2x1**2*vev - 2*cb*complex(0,1)*lamd*Rcp1x2*Rcp2x1*Rcp2x2*vev - 2*cb*complex(0,1)*lamm*Rcp1x2*Rcp2x1*Rcp2x2*vev - cb*complex(0,1)*lamd*Rcp1x1*Rcp2x2**2*vev - cb*complex(0,1)*lamm*Rcp1x1*Rcp2x2**2*vev - 2*cb*complex(0,1)*lam1s*Rcp1x3*Rcp2x1*Rcp2x3*vev - cb*complex(0,1)*lam1s*Rcp1x1*Rcp2x3**2*vev - complex(0,1)*lamd*Rcp1x2*Rcp2x1**2*sb*vev - complex(0,1)*lamm*Rcp1x2*Rcp2x1**2*sb*vev - 2*complex(0,1)*lamd*Rcp1x1*Rcp2x1*Rcp2x2*sb*vev - 2*complex(0,1)*lamm*Rcp1x1*Rcp2x1*Rcp2x2*sb*vev - 3*complex(0,1)*lam2*Rcp1x2*Rcp2x2**2*sb*vev - 2*complex(0,1)*lam2s*Rcp1x3*Rcp2x2*Rcp2x3*sb*vev - complex(0,1)*lam2s*Rcp1x2*Rcp2x3**2*sb*vev - complex(0,1)*lam1s*Rcp1x3*Rcp2x1**2*vevs - complex(0,1)*lam2s*Rcp1x3*Rcp2x2**2*vevs - 2*complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Rcp2x3*vevs - 2*complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Rcp2x3*vevs - 3*complex(0,1)*lams*Rcp1x3*Rcp2x3**2*vevs - complex(0,1)*lama*Rcp1x3*Rcp2x1*Rcp2x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x2*Rcp2x1*Rcp2x3*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x1*Rcp2x2*Rcp2x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '-3*cb*complex(0,1)*lam1*Rcp2x1**3*vev - 3*cb*complex(0,1)*lamd*Rcp2x1*Rcp2x2**2*vev - 3*cb*complex(0,1)*lamm*Rcp2x1*Rcp2x2**2*vev - 3*cb*complex(0,1)*lam1s*Rcp2x1*Rcp2x3**2*vev - 3*complex(0,1)*lamd*Rcp2x1**2*Rcp2x2*sb*vev - 3*complex(0,1)*lamm*Rcp2x1**2*Rcp2x2*sb*vev - 3*complex(0,1)*lam2*Rcp2x2**3*sb*vev - 3*complex(0,1)*lam2s*Rcp2x2*Rcp2x3**2*sb*vev - 3*complex(0,1)*lam1s*Rcp2x1**2*Rcp2x3*vevs - 3*complex(0,1)*lam2s*Rcp2x2**2*Rcp2x3*vevs - 3*complex(0,1)*lams*Rcp2x3**3*vevs - 3*complex(0,1)*lama*Rcp2x1*Rcp2x2*Rcp2x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_378 = Coupling(name = 'GC_378',
                  value = '2*cb*cx**2*complex(0,1)*gp**2*Rcp3x1*vev + (2*cb*cw*cx*ee*complex(0,1)*gp*Rcp3x1*sx*vev)/sw + (2*cb*cx*ee*complex(0,1)*gp*Rcp3x1*sw*sx*vev)/cw + cb*ee**2*complex(0,1)*Rcp3x1*sx**2*vev + ee**2*complex(0,1)*Rcp3x2*sb*sx**2*vev + (cb*cw**2*ee**2*complex(0,1)*Rcp3x1*sx**2*vev)/(2.*sw**2) + (cw**2*ee**2*complex(0,1)*Rcp3x2*sb*sx**2*vev)/(2.*sw**2) + (cb*ee**2*complex(0,1)*Rcp3x1*sw**2*sx**2*vev)/(2.*cw**2) + (ee**2*complex(0,1)*Rcp3x2*sb*sw**2*sx**2*vev)/(2.*cw**2) + 2*cx**2*complex(0,1)*gp**2*Rcp3x3*vevs',
                  order = {'QED':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '-3*cb*complex(0,1)*lam1*Rcp1x1**2*Rcp3x1*vev - cb*complex(0,1)*lamd*Rcp1x2**2*Rcp3x1*vev - cb*complex(0,1)*lamm*Rcp1x2**2*Rcp3x1*vev - cb*complex(0,1)*lam1s*Rcp1x3**2*Rcp3x1*vev - 2*cb*complex(0,1)*lamd*Rcp1x1*Rcp1x2*Rcp3x2*vev - 2*cb*complex(0,1)*lamm*Rcp1x1*Rcp1x2*Rcp3x2*vev - 2*cb*complex(0,1)*lam1s*Rcp1x1*Rcp1x3*Rcp3x3*vev - 2*complex(0,1)*lamd*Rcp1x1*Rcp1x2*Rcp3x1*sb*vev - 2*complex(0,1)*lamm*Rcp1x1*Rcp1x2*Rcp3x1*sb*vev - complex(0,1)*lamd*Rcp1x1**2*Rcp3x2*sb*vev - complex(0,1)*lamm*Rcp1x1**2*Rcp3x2*sb*vev - 3*complex(0,1)*lam2*Rcp1x2**2*Rcp3x2*sb*vev - complex(0,1)*lam2s*Rcp1x3**2*Rcp3x2*sb*vev - 2*complex(0,1)*lam2s*Rcp1x2*Rcp1x3*Rcp3x3*sb*vev - 2*complex(0,1)*lam1s*Rcp1x1*Rcp1x3*Rcp3x1*vevs - 2*complex(0,1)*lam2s*Rcp1x2*Rcp1x3*Rcp3x2*vevs - complex(0,1)*lam1s*Rcp1x1**2*Rcp3x3*vevs - complex(0,1)*lam2s*Rcp1x2**2*Rcp3x3*vevs - 3*complex(0,1)*lams*Rcp1x3**2*Rcp3x3*vevs - complex(0,1)*lama*Rcp1x2*Rcp1x3*Rcp3x1*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x1*Rcp1x3*Rcp3x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x1*Rcp1x2*Rcp3x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '-3*cb*complex(0,1)*lam1*Rcp1x1*Rcp2x1*Rcp3x1*vev - cb*complex(0,1)*lamd*Rcp1x2*Rcp2x2*Rcp3x1*vev - cb*complex(0,1)*lamm*Rcp1x2*Rcp2x2*Rcp3x1*vev - cb*complex(0,1)*lam1s*Rcp1x3*Rcp2x3*Rcp3x1*vev - cb*complex(0,1)*lamd*Rcp1x2*Rcp2x1*Rcp3x2*vev - cb*complex(0,1)*lamm*Rcp1x2*Rcp2x1*Rcp3x2*vev - cb*complex(0,1)*lamd*Rcp1x1*Rcp2x2*Rcp3x2*vev - cb*complex(0,1)*lamm*Rcp1x1*Rcp2x2*Rcp3x2*vev - cb*complex(0,1)*lam1s*Rcp1x3*Rcp2x1*Rcp3x3*vev - cb*complex(0,1)*lam1s*Rcp1x1*Rcp2x3*Rcp3x3*vev - complex(0,1)*lamd*Rcp1x2*Rcp2x1*Rcp3x1*sb*vev - complex(0,1)*lamm*Rcp1x2*Rcp2x1*Rcp3x1*sb*vev - complex(0,1)*lamd*Rcp1x1*Rcp2x2*Rcp3x1*sb*vev - complex(0,1)*lamm*Rcp1x1*Rcp2x2*Rcp3x1*sb*vev - complex(0,1)*lamd*Rcp1x1*Rcp2x1*Rcp3x2*sb*vev - complex(0,1)*lamm*Rcp1x1*Rcp2x1*Rcp3x2*sb*vev - 3*complex(0,1)*lam2*Rcp1x2*Rcp2x2*Rcp3x2*sb*vev - complex(0,1)*lam2s*Rcp1x3*Rcp2x3*Rcp3x2*sb*vev - complex(0,1)*lam2s*Rcp1x3*Rcp2x2*Rcp3x3*sb*vev - complex(0,1)*lam2s*Rcp1x2*Rcp2x3*Rcp3x3*sb*vev - complex(0,1)*lam1s*Rcp1x3*Rcp2x1*Rcp3x1*vevs - complex(0,1)*lam1s*Rcp1x1*Rcp2x3*Rcp3x1*vevs - complex(0,1)*lam2s*Rcp1x3*Rcp2x2*Rcp3x2*vevs - complex(0,1)*lam2s*Rcp1x2*Rcp2x3*Rcp3x2*vevs - complex(0,1)*lam1s*Rcp1x1*Rcp2x1*Rcp3x3*vevs - complex(0,1)*lam2s*Rcp1x2*Rcp2x2*Rcp3x3*vevs - 3*complex(0,1)*lams*Rcp1x3*Rcp2x3*Rcp3x3*vevs - (complex(0,1)*lama*Rcp1x3*Rcp2x2*Rcp3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x2*Rcp2x3*Rcp3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x3*Rcp2x1*Rcp3x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x1*Rcp2x3*Rcp3x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x2*Rcp2x1*Rcp3x3)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x1*Rcp2x2*Rcp3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '-3*cb*complex(0,1)*lam1*Rcp2x1**2*Rcp3x1*vev - cb*complex(0,1)*lamd*Rcp2x2**2*Rcp3x1*vev - cb*complex(0,1)*lamm*Rcp2x2**2*Rcp3x1*vev - cb*complex(0,1)*lam1s*Rcp2x3**2*Rcp3x1*vev - 2*cb*complex(0,1)*lamd*Rcp2x1*Rcp2x2*Rcp3x2*vev - 2*cb*complex(0,1)*lamm*Rcp2x1*Rcp2x2*Rcp3x2*vev - 2*cb*complex(0,1)*lam1s*Rcp2x1*Rcp2x3*Rcp3x3*vev - 2*complex(0,1)*lamd*Rcp2x1*Rcp2x2*Rcp3x1*sb*vev - 2*complex(0,1)*lamm*Rcp2x1*Rcp2x2*Rcp3x1*sb*vev - complex(0,1)*lamd*Rcp2x1**2*Rcp3x2*sb*vev - complex(0,1)*lamm*Rcp2x1**2*Rcp3x2*sb*vev - 3*complex(0,1)*lam2*Rcp2x2**2*Rcp3x2*sb*vev - complex(0,1)*lam2s*Rcp2x3**2*Rcp3x2*sb*vev - 2*complex(0,1)*lam2s*Rcp2x2*Rcp2x3*Rcp3x3*sb*vev - 2*complex(0,1)*lam1s*Rcp2x1*Rcp2x3*Rcp3x1*vevs - 2*complex(0,1)*lam2s*Rcp2x2*Rcp2x3*Rcp3x2*vevs - complex(0,1)*lam1s*Rcp2x1**2*Rcp3x3*vevs - complex(0,1)*lam2s*Rcp2x2**2*Rcp3x3*vevs - 3*complex(0,1)*lams*Rcp2x3**2*Rcp3x3*vevs - complex(0,1)*lama*Rcp2x2*Rcp2x3*Rcp3x1*cmath.sqrt(2) - complex(0,1)*lama*Rcp2x1*Rcp2x3*Rcp3x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp2x1*Rcp2x2*Rcp3x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '-3*cb*complex(0,1)*lam1*Rcp1x1*Rcp3x1**2*vev - 2*cb*complex(0,1)*lamd*Rcp1x2*Rcp3x1*Rcp3x2*vev - 2*cb*complex(0,1)*lamm*Rcp1x2*Rcp3x1*Rcp3x2*vev - cb*complex(0,1)*lamd*Rcp1x1*Rcp3x2**2*vev - cb*complex(0,1)*lamm*Rcp1x1*Rcp3x2**2*vev - 2*cb*complex(0,1)*lam1s*Rcp1x3*Rcp3x1*Rcp3x3*vev - cb*complex(0,1)*lam1s*Rcp1x1*Rcp3x3**2*vev - complex(0,1)*lamd*Rcp1x2*Rcp3x1**2*sb*vev - complex(0,1)*lamm*Rcp1x2*Rcp3x1**2*sb*vev - 2*complex(0,1)*lamd*Rcp1x1*Rcp3x1*Rcp3x2*sb*vev - 2*complex(0,1)*lamm*Rcp1x1*Rcp3x1*Rcp3x2*sb*vev - 3*complex(0,1)*lam2*Rcp1x2*Rcp3x2**2*sb*vev - 2*complex(0,1)*lam2s*Rcp1x3*Rcp3x2*Rcp3x3*sb*vev - complex(0,1)*lam2s*Rcp1x2*Rcp3x3**2*sb*vev - complex(0,1)*lam1s*Rcp1x3*Rcp3x1**2*vevs - complex(0,1)*lam2s*Rcp1x3*Rcp3x2**2*vevs - 2*complex(0,1)*lam1s*Rcp1x1*Rcp3x1*Rcp3x3*vevs - 2*complex(0,1)*lam2s*Rcp1x2*Rcp3x2*Rcp3x3*vevs - 3*complex(0,1)*lams*Rcp1x3*Rcp3x3**2*vevs - complex(0,1)*lama*Rcp1x3*Rcp3x1*Rcp3x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x2*Rcp3x1*Rcp3x3*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x1*Rcp3x2*Rcp3x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '-3*cb*complex(0,1)*lam1*Rcp2x1*Rcp3x1**2*vev - 2*cb*complex(0,1)*lamd*Rcp2x2*Rcp3x1*Rcp3x2*vev - 2*cb*complex(0,1)*lamm*Rcp2x2*Rcp3x1*Rcp3x2*vev - cb*complex(0,1)*lamd*Rcp2x1*Rcp3x2**2*vev - cb*complex(0,1)*lamm*Rcp2x1*Rcp3x2**2*vev - 2*cb*complex(0,1)*lam1s*Rcp2x3*Rcp3x1*Rcp3x3*vev - cb*complex(0,1)*lam1s*Rcp2x1*Rcp3x3**2*vev - complex(0,1)*lamd*Rcp2x2*Rcp3x1**2*sb*vev - complex(0,1)*lamm*Rcp2x2*Rcp3x1**2*sb*vev - 2*complex(0,1)*lamd*Rcp2x1*Rcp3x1*Rcp3x2*sb*vev - 2*complex(0,1)*lamm*Rcp2x1*Rcp3x1*Rcp3x2*sb*vev - 3*complex(0,1)*lam2*Rcp2x2*Rcp3x2**2*sb*vev - 2*complex(0,1)*lam2s*Rcp2x3*Rcp3x2*Rcp3x3*sb*vev - complex(0,1)*lam2s*Rcp2x2*Rcp3x3**2*sb*vev - complex(0,1)*lam1s*Rcp2x3*Rcp3x1**2*vevs - complex(0,1)*lam2s*Rcp2x3*Rcp3x2**2*vevs - 2*complex(0,1)*lam1s*Rcp2x1*Rcp3x1*Rcp3x3*vevs - 2*complex(0,1)*lam2s*Rcp2x2*Rcp3x2*Rcp3x3*vevs - 3*complex(0,1)*lams*Rcp2x3*Rcp3x3**2*vevs - complex(0,1)*lama*Rcp2x3*Rcp3x1*Rcp3x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp2x2*Rcp3x1*Rcp3x3*cmath.sqrt(2) - complex(0,1)*lama*Rcp2x1*Rcp3x2*Rcp3x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '-3*cb*complex(0,1)*lam1*Rcp3x1**3*vev - 3*cb*complex(0,1)*lamd*Rcp3x1*Rcp3x2**2*vev - 3*cb*complex(0,1)*lamm*Rcp3x1*Rcp3x2**2*vev - 3*cb*complex(0,1)*lam1s*Rcp3x1*Rcp3x3**2*vev - 3*complex(0,1)*lamd*Rcp3x1**2*Rcp3x2*sb*vev - 3*complex(0,1)*lamm*Rcp3x1**2*Rcp3x2*sb*vev - 3*complex(0,1)*lam2*Rcp3x2**3*sb*vev - 3*complex(0,1)*lam2s*Rcp3x2*Rcp3x3**2*sb*vev - 3*complex(0,1)*lam1s*Rcp3x1**2*Rcp3x3*vevs - 3*complex(0,1)*lam2s*Rcp3x2**2*Rcp3x3*vevs - 3*complex(0,1)*lams*Rcp3x3**3*vevs - 3*complex(0,1)*lama*Rcp3x1*Rcp3x2*Rcp3x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '-(cb*complex(0,1)*lam1*Rcp1x1*Reta1x1**2*vev) - cb*complex(0,1)*lamd*Rcp1x1*Reta1x2**2*vev - cb*complex(0,1)*lamm*Rcp1x1*Reta1x2**2*vev - cb*complex(0,1)*lam1s*Rcp1x1*Reta1x3**2*vev - complex(0,1)*lamd*Rcp1x2*Reta1x1**2*sb*vev - complex(0,1)*lamm*Rcp1x2*Reta1x1**2*sb*vev - complex(0,1)*lam2*Rcp1x2*Reta1x2**2*sb*vev - complex(0,1)*lam2s*Rcp1x2*Reta1x3**2*sb*vev - complex(0,1)*lam1s*Rcp1x3*Reta1x1**2*vevs - complex(0,1)*lam2s*Rcp1x3*Reta1x2**2*vevs - complex(0,1)*lams*Rcp1x3*Reta1x3**2*vevs - complex(0,1)*lama*Rcp1x3*Reta1x1*Reta1x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x2*Reta1x1*Reta1x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp1x1*Reta1x2*Reta1x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '-(cb*complex(0,1)*lam1*Rcp2x1*Reta1x1**2*vev) - cb*complex(0,1)*lamd*Rcp2x1*Reta1x2**2*vev - cb*complex(0,1)*lamm*Rcp2x1*Reta1x2**2*vev - cb*complex(0,1)*lam1s*Rcp2x1*Reta1x3**2*vev - complex(0,1)*lamd*Rcp2x2*Reta1x1**2*sb*vev - complex(0,1)*lamm*Rcp2x2*Reta1x1**2*sb*vev - complex(0,1)*lam2*Rcp2x2*Reta1x2**2*sb*vev - complex(0,1)*lam2s*Rcp2x2*Reta1x3**2*sb*vev - complex(0,1)*lam1s*Rcp2x3*Reta1x1**2*vevs - complex(0,1)*lam2s*Rcp2x3*Reta1x2**2*vevs - complex(0,1)*lams*Rcp2x3*Reta1x3**2*vevs - complex(0,1)*lama*Rcp2x3*Reta1x1*Reta1x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp2x2*Reta1x1*Reta1x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp2x1*Reta1x2*Reta1x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '-(cb*complex(0,1)*lam1*Rcp3x1*Reta1x1**2*vev) - cb*complex(0,1)*lamd*Rcp3x1*Reta1x2**2*vev - cb*complex(0,1)*lamm*Rcp3x1*Reta1x2**2*vev - cb*complex(0,1)*lam1s*Rcp3x1*Reta1x3**2*vev - complex(0,1)*lamd*Rcp3x2*Reta1x1**2*sb*vev - complex(0,1)*lamm*Rcp3x2*Reta1x1**2*sb*vev - complex(0,1)*lam2*Rcp3x2*Reta1x2**2*sb*vev - complex(0,1)*lam2s*Rcp3x2*Reta1x3**2*sb*vev - complex(0,1)*lam1s*Rcp3x3*Reta1x1**2*vevs - complex(0,1)*lam2s*Rcp3x3*Reta1x2**2*vevs - complex(0,1)*lams*Rcp3x3*Reta1x3**2*vevs - complex(0,1)*lama*Rcp3x3*Reta1x1*Reta1x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp3x2*Reta1x1*Reta1x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp3x1*Reta1x2*Reta1x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '-(cb*complex(0,1)*lam1*Rcp1x1*Reta1x1*Reta2x1*vev) - cb*complex(0,1)*lamd*Rcp1x1*Reta1x2*Reta2x2*vev - cb*complex(0,1)*lamm*Rcp1x1*Reta1x2*Reta2x2*vev - cb*complex(0,1)*lam1s*Rcp1x1*Reta1x3*Reta2x3*vev - complex(0,1)*lamd*Rcp1x2*Reta1x1*Reta2x1*sb*vev - complex(0,1)*lamm*Rcp1x2*Reta1x1*Reta2x1*sb*vev - complex(0,1)*lam2*Rcp1x2*Reta1x2*Reta2x2*sb*vev - complex(0,1)*lam2s*Rcp1x2*Reta1x3*Reta2x3*sb*vev - complex(0,1)*lam1s*Rcp1x3*Reta1x1*Reta2x1*vevs - complex(0,1)*lam2s*Rcp1x3*Reta1x2*Reta2x2*vevs - complex(0,1)*lams*Rcp1x3*Reta1x3*Reta2x3*vevs - (complex(0,1)*lama*Rcp1x3*Reta1x2*Reta2x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x2*Reta1x3*Reta2x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x3*Reta1x1*Reta2x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp1x1*Reta1x3*Reta2x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x2*Reta1x1*Reta2x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp1x1*Reta1x2*Reta2x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '-(cb*complex(0,1)*lam1*Rcp2x1*Reta1x1*Reta2x1*vev) - cb*complex(0,1)*lamd*Rcp2x1*Reta1x2*Reta2x2*vev - cb*complex(0,1)*lamm*Rcp2x1*Reta1x2*Reta2x2*vev - cb*complex(0,1)*lam1s*Rcp2x1*Reta1x3*Reta2x3*vev - complex(0,1)*lamd*Rcp2x2*Reta1x1*Reta2x1*sb*vev - complex(0,1)*lamm*Rcp2x2*Reta1x1*Reta2x1*sb*vev - complex(0,1)*lam2*Rcp2x2*Reta1x2*Reta2x2*sb*vev - complex(0,1)*lam2s*Rcp2x2*Reta1x3*Reta2x3*sb*vev - complex(0,1)*lam1s*Rcp2x3*Reta1x1*Reta2x1*vevs - complex(0,1)*lam2s*Rcp2x3*Reta1x2*Reta2x2*vevs - complex(0,1)*lams*Rcp2x3*Reta1x3*Reta2x3*vevs - (complex(0,1)*lama*Rcp2x3*Reta1x2*Reta2x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x2*Reta1x3*Reta2x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x3*Reta1x1*Reta2x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp2x1*Reta1x3*Reta2x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x2*Reta1x1*Reta2x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp2x1*Reta1x2*Reta2x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '-(cb*complex(0,1)*lam1*Rcp3x1*Reta1x1*Reta2x1*vev) - cb*complex(0,1)*lamd*Rcp3x1*Reta1x2*Reta2x2*vev - cb*complex(0,1)*lamm*Rcp3x1*Reta1x2*Reta2x2*vev - cb*complex(0,1)*lam1s*Rcp3x1*Reta1x3*Reta2x3*vev - complex(0,1)*lamd*Rcp3x2*Reta1x1*Reta2x1*sb*vev - complex(0,1)*lamm*Rcp3x2*Reta1x1*Reta2x1*sb*vev - complex(0,1)*lam2*Rcp3x2*Reta1x2*Reta2x2*sb*vev - complex(0,1)*lam2s*Rcp3x2*Reta1x3*Reta2x3*sb*vev - complex(0,1)*lam1s*Rcp3x3*Reta1x1*Reta2x1*vevs - complex(0,1)*lam2s*Rcp3x3*Reta1x2*Reta2x2*vevs - complex(0,1)*lams*Rcp3x3*Reta1x3*Reta2x3*vevs - (complex(0,1)*lama*Rcp3x3*Reta1x2*Reta2x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x2*Reta1x3*Reta2x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x3*Reta1x1*Reta2x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp3x1*Reta1x3*Reta2x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x2*Reta1x1*Reta2x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp3x1*Reta1x2*Reta2x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '-(cb*complex(0,1)*lam1*Rcp1x1*Reta2x1**2*vev) - cb*complex(0,1)*lamd*Rcp1x1*Reta2x2**2*vev - cb*complex(0,1)*lamm*Rcp1x1*Reta2x2**2*vev - cb*complex(0,1)*lam1s*Rcp1x1*Reta2x3**2*vev - complex(0,1)*lamd*Rcp1x2*Reta2x1**2*sb*vev - complex(0,1)*lamm*Rcp1x2*Reta2x1**2*sb*vev - complex(0,1)*lam2*Rcp1x2*Reta2x2**2*sb*vev - complex(0,1)*lam2s*Rcp1x2*Reta2x3**2*sb*vev - complex(0,1)*lam1s*Rcp1x3*Reta2x1**2*vevs - complex(0,1)*lam2s*Rcp1x3*Reta2x2**2*vevs - complex(0,1)*lams*Rcp1x3*Reta2x3**2*vevs - complex(0,1)*lama*Rcp1x3*Reta2x1*Reta2x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x2*Reta2x1*Reta2x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp1x1*Reta2x2*Reta2x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '-(cb*complex(0,1)*lam1*Rcp2x1*Reta2x1**2*vev) - cb*complex(0,1)*lamd*Rcp2x1*Reta2x2**2*vev - cb*complex(0,1)*lamm*Rcp2x1*Reta2x2**2*vev - cb*complex(0,1)*lam1s*Rcp2x1*Reta2x3**2*vev - complex(0,1)*lamd*Rcp2x2*Reta2x1**2*sb*vev - complex(0,1)*lamm*Rcp2x2*Reta2x1**2*sb*vev - complex(0,1)*lam2*Rcp2x2*Reta2x2**2*sb*vev - complex(0,1)*lam2s*Rcp2x2*Reta2x3**2*sb*vev - complex(0,1)*lam1s*Rcp2x3*Reta2x1**2*vevs - complex(0,1)*lam2s*Rcp2x3*Reta2x2**2*vevs - complex(0,1)*lams*Rcp2x3*Reta2x3**2*vevs - complex(0,1)*lama*Rcp2x3*Reta2x1*Reta2x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp2x2*Reta2x1*Reta2x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp2x1*Reta2x2*Reta2x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_393 = Coupling(name = 'GC_393',
                  value = '-(cb*complex(0,1)*lam1*Rcp3x1*Reta2x1**2*vev) - cb*complex(0,1)*lamd*Rcp3x1*Reta2x2**2*vev - cb*complex(0,1)*lamm*Rcp3x1*Reta2x2**2*vev - cb*complex(0,1)*lam1s*Rcp3x1*Reta2x3**2*vev - complex(0,1)*lamd*Rcp3x2*Reta2x1**2*sb*vev - complex(0,1)*lamm*Rcp3x2*Reta2x1**2*sb*vev - complex(0,1)*lam2*Rcp3x2*Reta2x2**2*sb*vev - complex(0,1)*lam2s*Rcp3x2*Reta2x3**2*sb*vev - complex(0,1)*lam1s*Rcp3x3*Reta2x1**2*vevs - complex(0,1)*lam2s*Rcp3x3*Reta2x2**2*vevs - complex(0,1)*lams*Rcp3x3*Reta2x3**2*vevs - complex(0,1)*lama*Rcp3x3*Reta2x1*Reta2x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp3x2*Reta2x1*Reta2x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp3x1*Reta2x2*Reta2x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '-(cb*complex(0,1)*lam1*Rcp1x1*Reta1x1*Reta3x1*vev) - cb*complex(0,1)*lamd*Rcp1x1*Reta1x2*Reta3x2*vev - cb*complex(0,1)*lamm*Rcp1x1*Reta1x2*Reta3x2*vev - cb*complex(0,1)*lam1s*Rcp1x1*Reta1x3*Reta3x3*vev - complex(0,1)*lamd*Rcp1x2*Reta1x1*Reta3x1*sb*vev - complex(0,1)*lamm*Rcp1x2*Reta1x1*Reta3x1*sb*vev - complex(0,1)*lam2*Rcp1x2*Reta1x2*Reta3x2*sb*vev - complex(0,1)*lam2s*Rcp1x2*Reta1x3*Reta3x3*sb*vev - complex(0,1)*lam1s*Rcp1x3*Reta1x1*Reta3x1*vevs - complex(0,1)*lam2s*Rcp1x3*Reta1x2*Reta3x2*vevs - complex(0,1)*lams*Rcp1x3*Reta1x3*Reta3x3*vevs - (complex(0,1)*lama*Rcp1x3*Reta1x2*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x2*Reta1x3*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x3*Reta1x1*Reta3x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp1x1*Reta1x3*Reta3x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x2*Reta1x1*Reta3x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp1x1*Reta1x2*Reta3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_395 = Coupling(name = 'GC_395',
                  value = '-(cb*complex(0,1)*lam1*Rcp2x1*Reta1x1*Reta3x1*vev) - cb*complex(0,1)*lamd*Rcp2x1*Reta1x2*Reta3x2*vev - cb*complex(0,1)*lamm*Rcp2x1*Reta1x2*Reta3x2*vev - cb*complex(0,1)*lam1s*Rcp2x1*Reta1x3*Reta3x3*vev - complex(0,1)*lamd*Rcp2x2*Reta1x1*Reta3x1*sb*vev - complex(0,1)*lamm*Rcp2x2*Reta1x1*Reta3x1*sb*vev - complex(0,1)*lam2*Rcp2x2*Reta1x2*Reta3x2*sb*vev - complex(0,1)*lam2s*Rcp2x2*Reta1x3*Reta3x3*sb*vev - complex(0,1)*lam1s*Rcp2x3*Reta1x1*Reta3x1*vevs - complex(0,1)*lam2s*Rcp2x3*Reta1x2*Reta3x2*vevs - complex(0,1)*lams*Rcp2x3*Reta1x3*Reta3x3*vevs - (complex(0,1)*lama*Rcp2x3*Reta1x2*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x2*Reta1x3*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x3*Reta1x1*Reta3x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp2x1*Reta1x3*Reta3x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x2*Reta1x1*Reta3x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp2x1*Reta1x2*Reta3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '-(cb*complex(0,1)*lam1*Rcp3x1*Reta1x1*Reta3x1*vev) - cb*complex(0,1)*lamd*Rcp3x1*Reta1x2*Reta3x2*vev - cb*complex(0,1)*lamm*Rcp3x1*Reta1x2*Reta3x2*vev - cb*complex(0,1)*lam1s*Rcp3x1*Reta1x3*Reta3x3*vev - complex(0,1)*lamd*Rcp3x2*Reta1x1*Reta3x1*sb*vev - complex(0,1)*lamm*Rcp3x2*Reta1x1*Reta3x1*sb*vev - complex(0,1)*lam2*Rcp3x2*Reta1x2*Reta3x2*sb*vev - complex(0,1)*lam2s*Rcp3x2*Reta1x3*Reta3x3*sb*vev - complex(0,1)*lam1s*Rcp3x3*Reta1x1*Reta3x1*vevs - complex(0,1)*lam2s*Rcp3x3*Reta1x2*Reta3x2*vevs - complex(0,1)*lams*Rcp3x3*Reta1x3*Reta3x3*vevs - (complex(0,1)*lama*Rcp3x3*Reta1x2*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x2*Reta1x3*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x3*Reta1x1*Reta3x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp3x1*Reta1x3*Reta3x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x2*Reta1x1*Reta3x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp3x1*Reta1x2*Reta3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '-(cb*complex(0,1)*lam1*Rcp1x1*Reta2x1*Reta3x1*vev) - cb*complex(0,1)*lamd*Rcp1x1*Reta2x2*Reta3x2*vev - cb*complex(0,1)*lamm*Rcp1x1*Reta2x2*Reta3x2*vev - cb*complex(0,1)*lam1s*Rcp1x1*Reta2x3*Reta3x3*vev - complex(0,1)*lamd*Rcp1x2*Reta2x1*Reta3x1*sb*vev - complex(0,1)*lamm*Rcp1x2*Reta2x1*Reta3x1*sb*vev - complex(0,1)*lam2*Rcp1x2*Reta2x2*Reta3x2*sb*vev - complex(0,1)*lam2s*Rcp1x2*Reta2x3*Reta3x3*sb*vev - complex(0,1)*lam1s*Rcp1x3*Reta2x1*Reta3x1*vevs - complex(0,1)*lam2s*Rcp1x3*Reta2x2*Reta3x2*vevs - complex(0,1)*lams*Rcp1x3*Reta2x3*Reta3x3*vevs - (complex(0,1)*lama*Rcp1x3*Reta2x2*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x2*Reta2x3*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x3*Reta2x1*Reta3x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp1x1*Reta2x3*Reta3x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp1x2*Reta2x1*Reta3x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp1x1*Reta2x2*Reta3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '-(cb*complex(0,1)*lam1*Rcp2x1*Reta2x1*Reta3x1*vev) - cb*complex(0,1)*lamd*Rcp2x1*Reta2x2*Reta3x2*vev - cb*complex(0,1)*lamm*Rcp2x1*Reta2x2*Reta3x2*vev - cb*complex(0,1)*lam1s*Rcp2x1*Reta2x3*Reta3x3*vev - complex(0,1)*lamd*Rcp2x2*Reta2x1*Reta3x1*sb*vev - complex(0,1)*lamm*Rcp2x2*Reta2x1*Reta3x1*sb*vev - complex(0,1)*lam2*Rcp2x2*Reta2x2*Reta3x2*sb*vev - complex(0,1)*lam2s*Rcp2x2*Reta2x3*Reta3x3*sb*vev - complex(0,1)*lam1s*Rcp2x3*Reta2x1*Reta3x1*vevs - complex(0,1)*lam2s*Rcp2x3*Reta2x2*Reta3x2*vevs - complex(0,1)*lams*Rcp2x3*Reta2x3*Reta3x3*vevs - (complex(0,1)*lama*Rcp2x3*Reta2x2*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x2*Reta2x3*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x3*Reta2x1*Reta3x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp2x1*Reta2x3*Reta3x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp2x2*Reta2x1*Reta3x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp2x1*Reta2x2*Reta3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '-(cb*complex(0,1)*lam1*Rcp3x1*Reta2x1*Reta3x1*vev) - cb*complex(0,1)*lamd*Rcp3x1*Reta2x2*Reta3x2*vev - cb*complex(0,1)*lamm*Rcp3x1*Reta2x2*Reta3x2*vev - cb*complex(0,1)*lam1s*Rcp3x1*Reta2x3*Reta3x3*vev - complex(0,1)*lamd*Rcp3x2*Reta2x1*Reta3x1*sb*vev - complex(0,1)*lamm*Rcp3x2*Reta2x1*Reta3x1*sb*vev - complex(0,1)*lam2*Rcp3x2*Reta2x2*Reta3x2*sb*vev - complex(0,1)*lam2s*Rcp3x2*Reta2x3*Reta3x3*sb*vev - complex(0,1)*lam1s*Rcp3x3*Reta2x1*Reta3x1*vevs - complex(0,1)*lam2s*Rcp3x3*Reta2x2*Reta3x2*vevs - complex(0,1)*lams*Rcp3x3*Reta2x3*Reta3x3*vevs - (complex(0,1)*lama*Rcp3x3*Reta2x2*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x2*Reta2x3*Reta3x1)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x3*Reta2x1*Reta3x2)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp3x1*Reta2x3*Reta3x2)/cmath.sqrt(2) - (complex(0,1)*lama*Rcp3x2*Reta2x1*Reta3x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp3x1*Reta2x2*Reta3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '-(cb*complex(0,1)*lam1*Rcp1x1*Reta3x1**2*vev) - cb*complex(0,1)*lamd*Rcp1x1*Reta3x2**2*vev - cb*complex(0,1)*lamm*Rcp1x1*Reta3x2**2*vev - cb*complex(0,1)*lam1s*Rcp1x1*Reta3x3**2*vev - complex(0,1)*lamd*Rcp1x2*Reta3x1**2*sb*vev - complex(0,1)*lamm*Rcp1x2*Reta3x1**2*sb*vev - complex(0,1)*lam2*Rcp1x2*Reta3x2**2*sb*vev - complex(0,1)*lam2s*Rcp1x2*Reta3x3**2*sb*vev - complex(0,1)*lam1s*Rcp1x3*Reta3x1**2*vevs - complex(0,1)*lam2s*Rcp1x3*Reta3x2**2*vevs - complex(0,1)*lams*Rcp1x3*Reta3x3**2*vevs - complex(0,1)*lama*Rcp1x3*Reta3x1*Reta3x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp1x2*Reta3x1*Reta3x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp1x1*Reta3x2*Reta3x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '-(cb*complex(0,1)*lam1*Rcp2x1*Reta3x1**2*vev) - cb*complex(0,1)*lamd*Rcp2x1*Reta3x2**2*vev - cb*complex(0,1)*lamm*Rcp2x1*Reta3x2**2*vev - cb*complex(0,1)*lam1s*Rcp2x1*Reta3x3**2*vev - complex(0,1)*lamd*Rcp2x2*Reta3x1**2*sb*vev - complex(0,1)*lamm*Rcp2x2*Reta3x1**2*sb*vev - complex(0,1)*lam2*Rcp2x2*Reta3x2**2*sb*vev - complex(0,1)*lam2s*Rcp2x2*Reta3x3**2*sb*vev - complex(0,1)*lam1s*Rcp2x3*Reta3x1**2*vevs - complex(0,1)*lam2s*Rcp2x3*Reta3x2**2*vevs - complex(0,1)*lams*Rcp2x3*Reta3x3**2*vevs - complex(0,1)*lama*Rcp2x3*Reta3x1*Reta3x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp2x2*Reta3x1*Reta3x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp2x1*Reta3x2*Reta3x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '-(cb*complex(0,1)*lam1*Rcp3x1*Reta3x1**2*vev) - cb*complex(0,1)*lamd*Rcp3x1*Reta3x2**2*vev - cb*complex(0,1)*lamm*Rcp3x1*Reta3x2**2*vev - cb*complex(0,1)*lam1s*Rcp3x1*Reta3x3**2*vev - complex(0,1)*lamd*Rcp3x2*Reta3x1**2*sb*vev - complex(0,1)*lamm*Rcp3x2*Reta3x1**2*sb*vev - complex(0,1)*lam2*Rcp3x2*Reta3x2**2*sb*vev - complex(0,1)*lam2s*Rcp3x2*Reta3x3**2*sb*vev - complex(0,1)*lam1s*Rcp3x3*Reta3x1**2*vevs - complex(0,1)*lam2s*Rcp3x3*Reta3x2**2*vevs - complex(0,1)*lams*Rcp3x3*Reta3x3**2*vevs - complex(0,1)*lama*Rcp3x3*Reta3x1*Reta3x2*cmath.sqrt(2) - complex(0,1)*lama*Rcp3x2*Reta3x1*Reta3x3*cmath.sqrt(2) + complex(0,1)*lama*Rcp3x1*Reta3x2*Reta3x3*cmath.sqrt(2)',
                  order = {'QED':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '-0.5*(cb**3*complex(0,1)*lamm*Rcp1x2*vev) + cb**2*complex(0,1)*lam1*Rcp1x1*sb*vev - cb**2*complex(0,1)*lamd*Rcp1x1*sb*vev - (cb**2*complex(0,1)*lamm*Rcp1x1*sb*vev)/2. - cb*complex(0,1)*lam2*Rcp1x2*sb**2*vev + cb*complex(0,1)*lamd*Rcp1x2*sb**2*vev + (cb*complex(0,1)*lamm*Rcp1x2*sb**2*vev)/2. + (complex(0,1)*lamm*Rcp1x1*sb**3*vev)/2. + cb*complex(0,1)*lam1s*Rcp1x3*sb*vevs - cb*complex(0,1)*lam2s*Rcp1x3*sb*vevs - (cb**2*complex(0,1)*lama*Rcp1x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp1x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '-0.5*(cb**3*complex(0,1)*lamm*Rcp2x2*vev) + cb**2*complex(0,1)*lam1*Rcp2x1*sb*vev - cb**2*complex(0,1)*lamd*Rcp2x1*sb*vev - (cb**2*complex(0,1)*lamm*Rcp2x1*sb*vev)/2. - cb*complex(0,1)*lam2*Rcp2x2*sb**2*vev + cb*complex(0,1)*lamd*Rcp2x2*sb**2*vev + (cb*complex(0,1)*lamm*Rcp2x2*sb**2*vev)/2. + (complex(0,1)*lamm*Rcp2x1*sb**3*vev)/2. + cb*complex(0,1)*lam1s*Rcp2x3*sb*vevs - cb*complex(0,1)*lam2s*Rcp2x3*sb*vevs - (cb**2*complex(0,1)*lama*Rcp2x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp2x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_405 = Coupling(name = 'GC_405',
                  value = '-0.5*(cb**3*complex(0,1)*lamm*Rcp3x2*vev) + cb**2*complex(0,1)*lam1*Rcp3x1*sb*vev - cb**2*complex(0,1)*lamd*Rcp3x1*sb*vev - (cb**2*complex(0,1)*lamm*Rcp3x1*sb*vev)/2. - cb*complex(0,1)*lam2*Rcp3x2*sb**2*vev + cb*complex(0,1)*lamd*Rcp3x2*sb**2*vev + (cb*complex(0,1)*lamm*Rcp3x2*sb**2*vev)/2. + (complex(0,1)*lamm*Rcp3x1*sb**3*vev)/2. + cb*complex(0,1)*lam1s*Rcp3x3*sb*vevs - cb*complex(0,1)*lam2s*Rcp3x3*sb*vevs - (cb**2*complex(0,1)*lama*Rcp3x3)/cmath.sqrt(2) + (complex(0,1)*lama*Rcp3x3*sb**2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '-(cb**3*complex(0,1)*lamd*Rcp1x1*vev) - cb**2*complex(0,1)*lam2*Rcp1x2*sb*vev + cb**2*complex(0,1)*lamm*Rcp1x2*sb*vev - cb*complex(0,1)*lam1*Rcp1x1*sb**2*vev + cb*complex(0,1)*lamm*Rcp1x1*sb**2*vev - complex(0,1)*lamd*Rcp1x2*sb**3*vev - cb**2*complex(0,1)*lam2s*Rcp1x3*vevs - complex(0,1)*lam1s*Rcp1x3*sb**2*vevs + cb*complex(0,1)*lama*Rcp1x3*sb*cmath.sqrt(2)',
                  order = {'QED':1})

GC_407 = Coupling(name = 'GC_407',
                  value = '-(cb**3*complex(0,1)*lam1*Rcp1x1*vev) - cb**2*complex(0,1)*lamd*Rcp1x2*sb*vev - cb**2*complex(0,1)*lamm*Rcp1x2*sb*vev - cb*complex(0,1)*lamd*Rcp1x1*sb**2*vev - cb*complex(0,1)*lamm*Rcp1x1*sb**2*vev - complex(0,1)*lam2*Rcp1x2*sb**3*vev - cb**2*complex(0,1)*lam1s*Rcp1x3*vevs - complex(0,1)*lam2s*Rcp1x3*sb**2*vevs - cb*complex(0,1)*lama*Rcp1x3*sb*cmath.sqrt(2)',
                  order = {'QED':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '-(cb**3*complex(0,1)*lamd*Rcp2x1*vev) - cb**2*complex(0,1)*lam2*Rcp2x2*sb*vev + cb**2*complex(0,1)*lamm*Rcp2x2*sb*vev - cb*complex(0,1)*lam1*Rcp2x1*sb**2*vev + cb*complex(0,1)*lamm*Rcp2x1*sb**2*vev - complex(0,1)*lamd*Rcp2x2*sb**3*vev - cb**2*complex(0,1)*lam2s*Rcp2x3*vevs - complex(0,1)*lam1s*Rcp2x3*sb**2*vevs + cb*complex(0,1)*lama*Rcp2x3*sb*cmath.sqrt(2)',
                  order = {'QED':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '-(cb**3*complex(0,1)*lam1*Rcp2x1*vev) - cb**2*complex(0,1)*lamd*Rcp2x2*sb*vev - cb**2*complex(0,1)*lamm*Rcp2x2*sb*vev - cb*complex(0,1)*lamd*Rcp2x1*sb**2*vev - cb*complex(0,1)*lamm*Rcp2x1*sb**2*vev - complex(0,1)*lam2*Rcp2x2*sb**3*vev - cb**2*complex(0,1)*lam1s*Rcp2x3*vevs - complex(0,1)*lam2s*Rcp2x3*sb**2*vevs - cb*complex(0,1)*lama*Rcp2x3*sb*cmath.sqrt(2)',
                  order = {'QED':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '-(cb**3*complex(0,1)*lamd*Rcp3x1*vev) - cb**2*complex(0,1)*lam2*Rcp3x2*sb*vev + cb**2*complex(0,1)*lamm*Rcp3x2*sb*vev - cb*complex(0,1)*lam1*Rcp3x1*sb**2*vev + cb*complex(0,1)*lamm*Rcp3x1*sb**2*vev - complex(0,1)*lamd*Rcp3x2*sb**3*vev - cb**2*complex(0,1)*lam2s*Rcp3x3*vevs - complex(0,1)*lam1s*Rcp3x3*sb**2*vevs + cb*complex(0,1)*lama*Rcp3x3*sb*cmath.sqrt(2)',
                  order = {'QED':1})

GC_411 = Coupling(name = 'GC_411',
                  value = '-(cb**3*complex(0,1)*lam1*Rcp3x1*vev) - cb**2*complex(0,1)*lamd*Rcp3x2*sb*vev - cb**2*complex(0,1)*lamm*Rcp3x2*sb*vev - cb*complex(0,1)*lamd*Rcp3x1*sb**2*vev - cb*complex(0,1)*lamm*Rcp3x1*sb**2*vev - complex(0,1)*lam2*Rcp3x2*sb**3*vev - cb**2*complex(0,1)*lam1s*Rcp3x3*vevs - complex(0,1)*lam2s*Rcp3x3*sb**2*vevs - cb*complex(0,1)*lama*Rcp3x3*sb*cmath.sqrt(2)',
                  order = {'QED':1})

GC_412 = Coupling(name = 'GC_412',
                  value = '-((cb*cw*cx**2*ee*complex(0,1)*gp*Rcp1x1*vev)/sw) - (cb*cx**2*ee*complex(0,1)*gp*Rcp1x1*sw*vev)/cw - cb*cx*ee**2*complex(0,1)*Rcp1x1*sx*vev + 2*cb*cx*complex(0,1)*gp**2*Rcp1x1*sx*vev - cx*ee**2*complex(0,1)*Rcp1x2*sb*sx*vev - (cb*cw**2*cx*ee**2*complex(0,1)*Rcp1x1*sx*vev)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp1x2*sb*sx*vev)/(2.*sw**2) - (cb*cx*ee**2*complex(0,1)*Rcp1x1*sw**2*sx*vev)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp1x2*sb*sw**2*sx*vev)/(2.*cw**2) + (cb*cw*ee*complex(0,1)*gp*Rcp1x1*sx**2*vev)/sw + (cb*ee*complex(0,1)*gp*Rcp1x1*sw*sx**2*vev)/cw + 2*cx*complex(0,1)*gp**2*Rcp1x3*sx*vevs',
                  order = {'QED':1})

GC_413 = Coupling(name = 'GC_413',
                  value = '-((cb*cw*cx**2*ee*complex(0,1)*gp*Rcp2x1*vev)/sw) - (cb*cx**2*ee*complex(0,1)*gp*Rcp2x1*sw*vev)/cw - cb*cx*ee**2*complex(0,1)*Rcp2x1*sx*vev + 2*cb*cx*complex(0,1)*gp**2*Rcp2x1*sx*vev - cx*ee**2*complex(0,1)*Rcp2x2*sb*sx*vev - (cb*cw**2*cx*ee**2*complex(0,1)*Rcp2x1*sx*vev)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp2x2*sb*sx*vev)/(2.*sw**2) - (cb*cx*ee**2*complex(0,1)*Rcp2x1*sw**2*sx*vev)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp2x2*sb*sw**2*sx*vev)/(2.*cw**2) + (cb*cw*ee*complex(0,1)*gp*Rcp2x1*sx**2*vev)/sw + (cb*ee*complex(0,1)*gp*Rcp2x1*sw*sx**2*vev)/cw + 2*cx*complex(0,1)*gp**2*Rcp2x3*sx*vevs',
                  order = {'QED':1})

GC_414 = Coupling(name = 'GC_414',
                  value = '-((cb*cw*cx**2*ee*complex(0,1)*gp*Rcp3x1*vev)/sw) - (cb*cx**2*ee*complex(0,1)*gp*Rcp3x1*sw*vev)/cw - cb*cx*ee**2*complex(0,1)*Rcp3x1*sx*vev + 2*cb*cx*complex(0,1)*gp**2*Rcp3x1*sx*vev - cx*ee**2*complex(0,1)*Rcp3x2*sb*sx*vev - (cb*cw**2*cx*ee**2*complex(0,1)*Rcp3x1*sx*vev)/(2.*sw**2) - (cw**2*cx*ee**2*complex(0,1)*Rcp3x2*sb*sx*vev)/(2.*sw**2) - (cb*cx*ee**2*complex(0,1)*Rcp3x1*sw**2*sx*vev)/(2.*cw**2) - (cx*ee**2*complex(0,1)*Rcp3x2*sb*sw**2*sx*vev)/(2.*cw**2) + (cb*cw*ee*complex(0,1)*gp*Rcp3x1*sx**2*vev)/sw + (cb*ee*complex(0,1)*gp*Rcp3x1*sw*sx**2*vev)/cw + 2*cx*complex(0,1)*gp**2*Rcp3x3*sx*vevs',
                  order = {'QED':1})

GC_415 = Coupling(name = 'GC_415',
                  value = 'cb*cx**2*ee**2*complex(0,1)*Rcp1x1*vev + cx**2*ee**2*complex(0,1)*Rcp1x2*sb*vev + (cb*cw**2*cx**2*ee**2*complex(0,1)*Rcp1x1*vev)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp1x2*sb*vev)/(2.*sw**2) + (cb*cx**2*ee**2*complex(0,1)*Rcp1x1*sw**2*vev)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp1x2*sb*sw**2*vev)/(2.*cw**2) - (2*cb*cw*cx*ee*complex(0,1)*gp*Rcp1x1*sx*vev)/sw - (2*cb*cx*ee*complex(0,1)*gp*Rcp1x1*sw*sx*vev)/cw + 2*cb*complex(0,1)*gp**2*Rcp1x1*sx**2*vev + 2*complex(0,1)*gp**2*Rcp1x3*sx**2*vevs',
                  order = {'QED':1})

GC_416 = Coupling(name = 'GC_416',
                  value = 'cb*cx**2*ee**2*complex(0,1)*Rcp2x1*vev + cx**2*ee**2*complex(0,1)*Rcp2x2*sb*vev + (cb*cw**2*cx**2*ee**2*complex(0,1)*Rcp2x1*vev)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp2x2*sb*vev)/(2.*sw**2) + (cb*cx**2*ee**2*complex(0,1)*Rcp2x1*sw**2*vev)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp2x2*sb*sw**2*vev)/(2.*cw**2) - (2*cb*cw*cx*ee*complex(0,1)*gp*Rcp2x1*sx*vev)/sw - (2*cb*cx*ee*complex(0,1)*gp*Rcp2x1*sw*sx*vev)/cw + 2*cb*complex(0,1)*gp**2*Rcp2x1*sx**2*vev + 2*complex(0,1)*gp**2*Rcp2x3*sx**2*vevs',
                  order = {'QED':1})

GC_417 = Coupling(name = 'GC_417',
                  value = 'cb*cx**2*ee**2*complex(0,1)*Rcp3x1*vev + cx**2*ee**2*complex(0,1)*Rcp3x2*sb*vev + (cb*cw**2*cx**2*ee**2*complex(0,1)*Rcp3x1*vev)/(2.*sw**2) + (cw**2*cx**2*ee**2*complex(0,1)*Rcp3x2*sb*vev)/(2.*sw**2) + (cb*cx**2*ee**2*complex(0,1)*Rcp3x1*sw**2*vev)/(2.*cw**2) + (cx**2*ee**2*complex(0,1)*Rcp3x2*sb*sw**2*vev)/(2.*cw**2) - (2*cb*cw*cx*ee*complex(0,1)*gp*Rcp3x1*sx*vev)/sw - (2*cb*cx*ee*complex(0,1)*gp*Rcp3x1*sw*sx*vev)/cw + 2*cb*complex(0,1)*gp**2*Rcp3x1*sx**2*vev + 2*complex(0,1)*gp**2*Rcp3x3*sx**2*vevs',
                  order = {'QED':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '-(cb*complex(0,1)*yb)',
                  order = {'QED':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '-((complex(0,1)*Rcp1x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '-((complex(0,1)*Rcp2x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_421 = Coupling(name = 'GC_421',
                  value = '-((complex(0,1)*Rcp3x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '-((Reta1x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_423 = Coupling(name = 'GC_423',
                  value = '(Reta1x2*yb)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_424 = Coupling(name = 'GC_424',
                  value = '-((Reta2x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_425 = Coupling(name = 'GC_425',
                  value = '(Reta2x2*yb)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '-((Reta3x2*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_427 = Coupling(name = 'GC_427',
                  value = '-(complex(0,1)*sb*yb)',
                  order = {'QED':1})

GC_428 = Coupling(name = 'GC_428',
                  value = 'cb*complex(0,1)*yc',
                  order = {'QED':1})

GC_429 = Coupling(name = 'GC_429',
                  value = '-((complex(0,1)*Rcp1x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_430 = Coupling(name = 'GC_430',
                  value = '-((complex(0,1)*Rcp2x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_431 = Coupling(name = 'GC_431',
                  value = '-((complex(0,1)*Rcp3x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_432 = Coupling(name = 'GC_432',
                  value = '-((Reta1x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '(Reta1x2*yc)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '-((Reta2x2*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '(Reta2x2*yc)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '(Reta3x2*yc)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_437 = Coupling(name = 'GC_437',
                  value = 'complex(0,1)*sb*yc',
                  order = {'QED':1})

GC_438 = Coupling(name = 'GC_438',
                  value = '-(cb*complex(0,1)*ydo)',
                  order = {'QED':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '-((complex(0,1)*Rcp1x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_440 = Coupling(name = 'GC_440',
                  value = '-((complex(0,1)*Rcp2x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_441 = Coupling(name = 'GC_441',
                  value = '-((complex(0,1)*Rcp3x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_442 = Coupling(name = 'GC_442',
                  value = '-((Reta1x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '(Reta1x2*ydo)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '-((Reta2x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '(Reta2x2*ydo)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '-((Reta3x2*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '-(complex(0,1)*sb*ydo)',
                  order = {'QED':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '-3*cb*cn1*complex(0,1)*ye',
                  order = {'QED':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '-((complex(0,1)*Rcp1x2*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_450 = Coupling(name = 'GC_450',
                  value = '-((complex(0,1)*Rcp2x2*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_451 = Coupling(name = 'GC_451',
                  value = '-((complex(0,1)*Rcp3x2*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_452 = Coupling(name = 'GC_452',
                  value = '-((Reta1x2*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_453 = Coupling(name = 'GC_453',
                  value = '(Reta1x2*ye)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_454 = Coupling(name = 'GC_454',
                  value = '-((Reta2x2*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_455 = Coupling(name = 'GC_455',
                  value = '(Reta2x2*ye)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_456 = Coupling(name = 'GC_456',
                  value = '-((Reta3x2*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '-3*cn1*complex(0,1)*sb*ye',
                  order = {'QED':1})

GC_458 = Coupling(name = 'GC_458',
                  value = '-3*cb*complex(0,1)*sn1*ye',
                  order = {'QED':1})

GC_459 = Coupling(name = 'GC_459',
                  value = '-3*complex(0,1)*sb*sn1*ye',
                  order = {'QED':1})

GC_460 = Coupling(name = 'GC_460',
                  value = '-3*cb*cn2*complex(0,1)*ym',
                  order = {'QED':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '-((complex(0,1)*Rcp1x2*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '-((complex(0,1)*Rcp2x2*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '-((complex(0,1)*Rcp3x2*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_464 = Coupling(name = 'GC_464',
                  value = '-((Reta1x2*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '(Reta1x2*ym)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '-((Reta2x2*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_467 = Coupling(name = 'GC_467',
                  value = '(Reta2x2*ym)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '-((Reta3x2*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '-3*cn2*complex(0,1)*sb*ym',
                  order = {'QED':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '-3*cb*complex(0,1)*sn2*ym',
                  order = {'QED':1})

GC_471 = Coupling(name = 'GC_471',
                  value = '-3*complex(0,1)*sb*sn2*ym',
                  order = {'QED':1})

GC_472 = Coupling(name = 'GC_472',
                  value = 'cb*complex(0,1)*yneu1x1',
                  order = {'QED':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '-((cn1*complex(0,1)*Rcp1x1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_474 = Coupling(name = 'GC_474',
                  value = '-((cn1*complex(0,1)*Rcp2x1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '-((cn1*complex(0,1)*Rcp3x1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_476 = Coupling(name = 'GC_476',
                  value = '-((cn1*Reta1x1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '(cn1*Reta1x1*yneu1x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_478 = Coupling(name = 'GC_478',
                  value = '-((cn1*Reta2x1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_479 = Coupling(name = 'GC_479',
                  value = '(cn1*Reta2x1*yneu1x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_480 = Coupling(name = 'GC_480',
                  value = '-((cn1*Reta3x1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '(cn1*Reta3x1*yneu1x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '-(complex(0,1)*sb*yneu1x1)',
                  order = {'QED':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '-((complex(0,1)*Rcp1x1*sn1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_484 = Coupling(name = 'GC_484',
                  value = '-((complex(0,1)*Rcp2x1*sn1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '-((complex(0,1)*Rcp3x1*sn1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '-((Reta1x1*sn1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '(Reta1x1*sn1*yneu1x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '-((Reta2x1*sn1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '(Reta2x1*sn1*yneu1x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '-((Reta3x1*sn1*yneu1x1)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '(Reta3x1*sn1*yneu1x1)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_492 = Coupling(name = 'GC_492',
                  value = 'cb*complex(0,1)*yneu2x2',
                  order = {'QED':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '-((cn2*complex(0,1)*Rcp1x1*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '-((cn2*complex(0,1)*Rcp2x1*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '-((cn2*complex(0,1)*Rcp3x1*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '-((cn2*Reta1x1*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '(cn2*Reta1x1*yneu2x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '-((cn2*Reta2x1*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '(cn2*Reta2x1*yneu2x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '-((cn2*Reta3x1*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '(cn2*Reta3x1*yneu2x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '-(complex(0,1)*sb*yneu2x2)',
                  order = {'QED':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '-((complex(0,1)*Rcp1x1*sn2*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '-((complex(0,1)*Rcp2x1*sn2*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '-((complex(0,1)*Rcp3x1*sn2*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '-((Reta1x1*sn2*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '(Reta1x1*sn2*yneu2x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '-((Reta2x1*sn2*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '(Reta2x1*sn2*yneu2x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '-((Reta3x1*sn2*yneu2x2)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '(Reta3x1*sn2*yneu2x2)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_512 = Coupling(name = 'GC_512',
                  value = 'cb*complex(0,1)*yneu3x3',
                  order = {'QED':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '-((cn3*complex(0,1)*Rcp1x1*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '-((cn3*complex(0,1)*Rcp2x1*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '-((cn3*complex(0,1)*Rcp3x1*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_516 = Coupling(name = 'GC_516',
                  value = '-((cn3*Reta1x1*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '(cn3*Reta1x1*yneu3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '-((cn3*Reta2x1*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '(cn3*Reta2x1*yneu3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '-((cn3*Reta3x1*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '(cn3*Reta3x1*yneu3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '-(complex(0,1)*sb*yneu3x3)',
                  order = {'QED':1})

GC_523 = Coupling(name = 'GC_523',
                  value = '-((complex(0,1)*Rcp1x1*sn3*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '-((complex(0,1)*Rcp2x1*sn3*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_525 = Coupling(name = 'GC_525',
                  value = '-((complex(0,1)*Rcp3x1*sn3*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '-((Reta1x1*sn3*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_527 = Coupling(name = 'GC_527',
                  value = '(Reta1x1*sn3*yneu3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '-((Reta2x1*sn3*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '(Reta2x1*sn3*yneu3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '-((Reta3x1*sn3*yneu3x3)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '(Reta3x1*sn3*yneu3x3)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '-0.5*(complex(0,1)*yns)',
                  order = {'QED':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '-(cb*complex(0,1)*ys)',
                  order = {'QED':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '-((complex(0,1)*Rcp1x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '-((complex(0,1)*Rcp2x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '-((complex(0,1)*Rcp3x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '-((Reta1x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '(Reta1x2*ys)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '-((Reta2x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_540 = Coupling(name = 'GC_540',
                  value = '(Reta2x2*ys)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '-((Reta3x2*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '-(complex(0,1)*sb*ys)',
                  order = {'QED':1})

GC_543 = Coupling(name = 'GC_543',
                  value = 'cb*complex(0,1)*yt',
                  order = {'QED':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '-((complex(0,1)*Rcp1x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_545 = Coupling(name = 'GC_545',
                  value = '-((complex(0,1)*Rcp2x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '-((complex(0,1)*Rcp3x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '-((Reta1x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '(Reta1x2*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '-((Reta2x2*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(Reta2x2*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '(Reta3x2*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_552 = Coupling(name = 'GC_552',
                  value = 'complex(0,1)*sb*yt',
                  order = {'QED':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '-3*cb*cn3*complex(0,1)*ytau',
                  order = {'QED':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '-((complex(0,1)*Rcp1x2*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '-((complex(0,1)*Rcp2x2*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '-((complex(0,1)*Rcp3x2*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '-((Reta1x2*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '(Reta1x2*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '-((Reta2x2*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '(Reta2x2*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '-((Reta3x2*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '-3*cn3*complex(0,1)*sb*ytau',
                  order = {'QED':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '-3*cb*complex(0,1)*sn3*ytau',
                  order = {'QED':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '-3*complex(0,1)*sb*sn3*ytau',
                  order = {'QED':1})

GC_565 = Coupling(name = 'GC_565',
                  value = 'cb*complex(0,1)*yup',
                  order = {'QED':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '-((complex(0,1)*Rcp1x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '-((complex(0,1)*Rcp2x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '-((complex(0,1)*Rcp3x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '-((Reta1x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '(Reta1x2*yup)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '-((Reta2x2*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_572 = Coupling(name = 'GC_572',
                  value = '(Reta2x2*yup)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_573 = Coupling(name = 'GC_573',
                  value = '(Reta3x2*yup)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_574 = Coupling(name = 'GC_574',
                  value = 'complex(0,1)*sb*yup',
                  order = {'QED':1})

