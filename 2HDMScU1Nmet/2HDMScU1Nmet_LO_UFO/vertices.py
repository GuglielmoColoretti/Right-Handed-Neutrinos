# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 9 Jan 2025 17:47:22


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.G__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_151})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H__minus__, P.H__minus__, P.H__plus__, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_150})

V_3 = Vertex(name = 'V_3',
             particles = [ P.G__minus__, P.G__plus__, P.H__minus__, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_152})

V_4 = Vertex(name = 'V_4',
             particles = [ P.G__minus__, P.G__plus__, P.G__plus__, P.H__minus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_149})

V_5 = Vertex(name = 'V_5',
             particles = [ P.G__minus__, P.G__minus__, P.G__plus__, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_149})

V_6 = Vertex(name = 'V_6',
             particles = [ P.G__plus__, P.H__minus__, P.H__minus__, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_148})

V_7 = Vertex(name = 'V_7',
             particles = [ P.G__minus__, P.H__minus__, P.H__plus__, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_148})

V_8 = Vertex(name = 'V_8',
             particles = [ P.G__plus__, P.G__plus__, P.H__minus__, P.H__minus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_93})

V_9 = Vertex(name = 'V_9',
             particles = [ P.G__minus__, P.G__minus__, P.H__plus__, P.H__plus__ ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_93})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_92})

V_11 = Vertex(name = 'V_11',
              particles = [ P.a, P.a, P.H__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_92})

V_12 = Vertex(name = 'V_12',
              particles = [ P.a, P.G__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_91})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.H__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_91})

V_14 = Vertex(name = 'V_14',
              particles = [ P.csi__tilde__, P.csi, P.hs ],
              color = [ '1' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_532})

V_15 = Vertex(name = 'V_15',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_6})

V_16 = Vertex(name = 'V_16',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_8,(0,0):C.GC_8,(2,2):C.GC_8})

V_17 = Vertex(name = 'V_17',
              particles = [ P.t__tilde__, P.b, P.H__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_418,(0,1):C.GC_543})

V_18 = Vertex(name = 'V_18',
              particles = [ P.u__tilde__, P.d, P.H__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_438,(0,1):C.GC_565})

V_19 = Vertex(name = 'V_19',
              particles = [ P.c__tilde__, P.s, P.H__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_533,(0,1):C.GC_428})

V_20 = Vertex(name = 'V_20',
              particles = [ P.t__tilde__, P.b, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_427,(0,1):C.GC_552})

V_21 = Vertex(name = 'V_21',
              particles = [ P.u__tilde__, P.d, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_447,(0,1):C.GC_574})

V_22 = Vertex(name = 'V_22',
              particles = [ P.c__tilde__, P.s, P.G__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_542,(0,1):C.GC_437})

V_23 = Vertex(name = 'V_23',
              particles = [ P.nh1__tilde__, P.e__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_458,(0,1):C.GC_482})

V_24 = Vertex(name = 'V_24',
              particles = [ P.nle__tilde__, P.e__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_448})

V_25 = Vertex(name = 'V_25',
              particles = [ P.nh2__tilde__, P.mu__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_470,(0,1):C.GC_502})

V_26 = Vertex(name = 'V_26',
              particles = [ P.nlmu__tilde__, P.mu__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_460})

V_27 = Vertex(name = 'V_27',
              particles = [ P.nh3__tilde__, P.ta__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_563,(0,1):C.GC_522})

V_28 = Vertex(name = 'V_28',
              particles = [ P.nlta__tilde__, P.ta__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_553})

V_29 = Vertex(name = 'V_29',
              particles = [ P.nh1__tilde__, P.e__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_459,(0,1):C.GC_472})

V_30 = Vertex(name = 'V_30',
              particles = [ P.nle__tilde__, P.e__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_457})

V_31 = Vertex(name = 'V_31',
              particles = [ P.nh2__tilde__, P.mu__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_471,(0,1):C.GC_492})

V_32 = Vertex(name = 'V_32',
              particles = [ P.nlmu__tilde__, P.mu__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_469})

V_33 = Vertex(name = 'V_33',
              particles = [ P.nh3__tilde__, P.ta__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_564,(0,1):C.GC_512})

V_34 = Vertex(name = 'V_34',
              particles = [ P.nlta__tilde__, P.ta__minus__, P.G__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_562})

V_35 = Vertex(name = 'V_35',
              particles = [ P.s__tilde__, P.c, P.H__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_428,(0,1):C.GC_533})

V_36 = Vertex(name = 'V_36',
              particles = [ P.b__tilde__, P.t, P.H__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_543,(0,1):C.GC_418})

V_37 = Vertex(name = 'V_37',
              particles = [ P.d__tilde__, P.u, P.H__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_565,(0,1):C.GC_438})

V_38 = Vertex(name = 'V_38',
              particles = [ P.s__tilde__, P.c, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_437,(0,1):C.GC_542})

V_39 = Vertex(name = 'V_39',
              particles = [ P.b__tilde__, P.t, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_552,(0,1):C.GC_427})

V_40 = Vertex(name = 'V_40',
              particles = [ P.d__tilde__, P.u, P.G__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_574,(0,1):C.GC_447})

V_41 = Vertex(name = 'V_41',
              particles = [ P.e__plus__, P.nh1, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_472,(0,1):C.GC_459})

V_42 = Vertex(name = 'V_42',
              particles = [ P.e__plus__, P.nh1, P.H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_482,(0,1):C.GC_458})

V_43 = Vertex(name = 'V_43',
              particles = [ P.mu__plus__, P.nh2, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_492,(0,1):C.GC_471})

V_44 = Vertex(name = 'V_44',
              particles = [ P.mu__plus__, P.nh2, P.H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_502,(0,1):C.GC_470})

V_45 = Vertex(name = 'V_45',
              particles = [ P.ta__plus__, P.nh3, P.G__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_512,(0,1):C.GC_564})

V_46 = Vertex(name = 'V_46',
              particles = [ P.ta__plus__, P.nh3, P.H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFS2, L.FFS4 ],
              couplings = {(0,0):C.GC_522,(0,1):C.GC_563})

V_47 = Vertex(name = 'V_47',
              particles = [ P.G__minus__, P.G__plus__, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_407})

V_48 = Vertex(name = 'V_48',
              particles = [ P.hh, P.H__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_406})

V_49 = Vertex(name = 'V_49',
              particles = [ P.G__plus__, P.hh, P.H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_403})

V_50 = Vertex(name = 'V_50',
              particles = [ P.G__minus__, P.hh, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_403})

V_51 = Vertex(name = 'V_51',
              particles = [ P.nh1__tilde__, P.nh1, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_483})

V_52 = Vertex(name = 'V_52',
              particles = [ P.nle__tilde__, P.nh1, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_473})

V_53 = Vertex(name = 'V_53',
              particles = [ P.nh2__tilde__, P.nh2, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_503})

V_54 = Vertex(name = 'V_54',
              particles = [ P.nlmu__tilde__, P.nh2, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_493})

V_55 = Vertex(name = 'V_55',
              particles = [ P.nh3__tilde__, P.nh3, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_523})

V_56 = Vertex(name = 'V_56',
              particles = [ P.nlta__tilde__, P.nh3, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_513})

V_57 = Vertex(name = 'V_57',
              particles = [ P.G__minus__, P.G__plus__, P.hh, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_96})

V_58 = Vertex(name = 'V_58',
              particles = [ P.hh, P.hh, P.H__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_95})

V_59 = Vertex(name = 'V_59',
              particles = [ P.G__plus__, P.hh, P.hh, P.H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_94})

V_60 = Vertex(name = 'V_60',
              particles = [ P.G__minus__, P.hh, P.hh, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_94})

V_61 = Vertex(name = 'V_61',
              particles = [ P.hh, P.hh, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_373})

V_62 = Vertex(name = 'V_62',
              particles = [ P.hh, P.hh, P.hh, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_14})

V_63 = Vertex(name = 'V_63',
              particles = [ P.a, P.a, P.hh ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_10})

V_64 = Vertex(name = 'V_64',
              particles = [ P.g, P.g, P.hh ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_11})

V_65 = Vertex(name = 'V_65',
              particles = [ P.g, P.g, P.g, P.hh ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS1 ],
              couplings = {(0,0):C.GC_12})

V_66 = Vertex(name = 'V_66',
              particles = [ P.g, P.g, P.g, P.g, P.hh ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS2, L.VVVVS3 ],
              couplings = {(1,1):C.GC_13,(0,0):C.GC_13,(2,2):C.GC_13})

V_67 = Vertex(name = 'V_67',
              particles = [ P.b__tilde__, P.b, P.hh ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_419})

V_68 = Vertex(name = 'V_68',
              particles = [ P.d__tilde__, P.d, P.hh ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_439})

V_69 = Vertex(name = 'V_69',
              particles = [ P.s__tilde__, P.s, P.hh ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_534})

V_70 = Vertex(name = 'V_70',
              particles = [ P.e__plus__, P.e__minus__, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_449})

V_71 = Vertex(name = 'V_71',
              particles = [ P.mu__plus__, P.mu__minus__, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_461})

V_72 = Vertex(name = 'V_72',
              particles = [ P.ta__plus__, P.ta__minus__, P.hh ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_554})

V_73 = Vertex(name = 'V_73',
              particles = [ P.c__tilde__, P.c, P.hh ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_429})

V_74 = Vertex(name = 'V_74',
              particles = [ P.t__tilde__, P.t, P.hh ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_544})

V_75 = Vertex(name = 'V_75',
              particles = [ P.u__tilde__, P.u, P.hh ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_566})

V_76 = Vertex(name = 'V_76',
              particles = [ P.G__minus__, P.G__plus__, P.h ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_409})

V_77 = Vertex(name = 'V_77',
              particles = [ P.h, P.H__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_408})

V_78 = Vertex(name = 'V_78',
              particles = [ P.G__plus__, P.h, P.H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_404})

V_79 = Vertex(name = 'V_79',
              particles = [ P.G__minus__, P.h, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_404})

V_80 = Vertex(name = 'V_80',
              particles = [ P.nh1__tilde__, P.nh1, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_484})

V_81 = Vertex(name = 'V_81',
              particles = [ P.nle__tilde__, P.nh1, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_474})

V_82 = Vertex(name = 'V_82',
              particles = [ P.nh2__tilde__, P.nh2, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_504})

V_83 = Vertex(name = 'V_83',
              particles = [ P.nlmu__tilde__, P.nh2, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_494})

V_84 = Vertex(name = 'V_84',
              particles = [ P.nh3__tilde__, P.nh3, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS5 ],
              couplings = {(0,0):C.GC_524})

V_85 = Vertex(name = 'V_85',
              particles = [ P.nlta__tilde__, P.nh3, P.h ],
              color = [ '1' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_514})

V_86 = Vertex(name = 'V_86',
              particles = [ P.G__minus__, P.G__plus__, P.h, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_100})

V_87 = Vertex(name = 'V_87',
              particles = [ P.h, P.hh, P.H__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_99})

V_88 = Vertex(name = 'V_88',
              particles = [ P.G__plus__, P.h, P.hh, P.H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_97})

V_89 = Vertex(name = 'V_89',
              particles = [ P.G__minus__, P.h, P.hh, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_97})

V_90 = Vertex(name = 'V_90',
              particles = [ P.h, P.hh, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_375})

V_91 = Vertex(name = 'V_91',
              particles = [ P.h, P.hh, P.hh, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_19})

V_92 = Vertex(name = 'V_92',
              particles = [ P.G__minus__, P.G__plus__, P.h, P.h ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_102})

V_93 = Vertex(name = 'V_93',
              particles = [ P.h, P.h, P.H__minus__, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_101})

V_94 = Vertex(name = 'V_94',
              particles = [ P.G__plus__, P.h, P.h, P.H__minus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_98})

V_95 = Vertex(name = 'V_95',
              particles = [ P.G__minus__, P.h, P.h, P.H__plus__ ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_98})

V_96 = Vertex(name = 'V_96',
              particles = [ P.h, P.h, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_376})

V_97 = Vertex(name = 'V_97',
              particles = [ P.h, P.h, P.hh, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_20})

V_98 = Vertex(name = 'V_98',
              particles = [ P.h, P.h, P.h ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_377})

V_99 = Vertex(name = 'V_99',
              particles = [ P.h, P.h, P.h, P.hh ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_21})

V_100 = Vertex(name = 'V_100',
               particles = [ P.h, P.h, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_22})

V_101 = Vertex(name = 'V_101',
               particles = [ P.a, P.a, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS2 ],
               couplings = {(0,0):C.GC_15})

V_102 = Vertex(name = 'V_102',
               particles = [ P.g, P.g, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVS2 ],
               couplings = {(0,0):C.GC_16})

V_103 = Vertex(name = 'V_103',
               particles = [ P.g, P.g, P.g, P.h ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVVS1 ],
               couplings = {(0,0):C.GC_17})

V_104 = Vertex(name = 'V_104',
               particles = [ P.g, P.g, P.g, P.g, P.h ],
               color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
               lorentz = [ L.VVVVS1, L.VVVVS2, L.VVVVS3 ],
               couplings = {(1,1):C.GC_18,(0,0):C.GC_18,(2,2):C.GC_18})

V_105 = Vertex(name = 'V_105',
               particles = [ P.b__tilde__, P.b, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_420})

V_106 = Vertex(name = 'V_106',
               particles = [ P.d__tilde__, P.d, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_440})

V_107 = Vertex(name = 'V_107',
               particles = [ P.s__tilde__, P.s, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_535})

V_108 = Vertex(name = 'V_108',
               particles = [ P.e__plus__, P.e__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_450})

V_109 = Vertex(name = 'V_109',
               particles = [ P.mu__plus__, P.mu__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_462})

V_110 = Vertex(name = 'V_110',
               particles = [ P.ta__plus__, P.ta__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_555})

V_111 = Vertex(name = 'V_111',
               particles = [ P.c__tilde__, P.c, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_430})

V_112 = Vertex(name = 'V_112',
               particles = [ P.t__tilde__, P.t, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_545})

V_113 = Vertex(name = 'V_113',
               particles = [ P.u__tilde__, P.u, P.h ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_567})

V_114 = Vertex(name = 'V_114',
               particles = [ P.G__minus__, P.G__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_411})

V_115 = Vertex(name = 'V_115',
               particles = [ P.H__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_410})

V_116 = Vertex(name = 'V_116',
               particles = [ P.G__plus__, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_405})

V_117 = Vertex(name = 'V_117',
               particles = [ P.G__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_405})

V_118 = Vertex(name = 'V_118',
               particles = [ P.nh1__tilde__, P.nh1, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_485})

V_119 = Vertex(name = 'V_119',
               particles = [ P.nle__tilde__, P.nh1, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_475})

V_120 = Vertex(name = 'V_120',
               particles = [ P.nh2__tilde__, P.nh2, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_505})

V_121 = Vertex(name = 'V_121',
               particles = [ P.nlmu__tilde__, P.nh2, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_495})

V_122 = Vertex(name = 'V_122',
               particles = [ P.nh3__tilde__, P.nh3, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_525})

V_123 = Vertex(name = 'V_123',
               particles = [ P.nlta__tilde__, P.nh3, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_515})

V_124 = Vertex(name = 'V_124',
               particles = [ P.G__minus__, P.G__plus__, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_107})

V_125 = Vertex(name = 'V_125',
               particles = [ P.hh, P.H__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_106})

V_126 = Vertex(name = 'V_126',
               particles = [ P.G__plus__, P.hh, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_103})

V_127 = Vertex(name = 'V_127',
               particles = [ P.G__minus__, P.hh, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_103})

V_128 = Vertex(name = 'V_128',
               particles = [ P.hh, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_379})

V_129 = Vertex(name = 'V_129',
               particles = [ P.hh, P.hh, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_27})

V_130 = Vertex(name = 'V_130',
               particles = [ P.G__minus__, P.G__plus__, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_109})

V_131 = Vertex(name = 'V_131',
               particles = [ P.h, P.H__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_108})

V_132 = Vertex(name = 'V_132',
               particles = [ P.G__plus__, P.h, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_104})

V_133 = Vertex(name = 'V_133',
               particles = [ P.G__minus__, P.h, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_104})

V_134 = Vertex(name = 'V_134',
               particles = [ P.h, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_380})

V_135 = Vertex(name = 'V_135',
               particles = [ P.h, P.hh, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_28})

V_136 = Vertex(name = 'V_136',
               particles = [ P.h, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_381})

V_137 = Vertex(name = 'V_137',
               particles = [ P.h, P.h, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_29})

V_138 = Vertex(name = 'V_138',
               particles = [ P.h, P.h, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_30})

V_139 = Vertex(name = 'V_139',
               particles = [ P.G__minus__, P.G__plus__, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_111})

V_140 = Vertex(name = 'V_140',
               particles = [ P.H__minus__, P.H__plus__, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_110})

V_141 = Vertex(name = 'V_141',
               particles = [ P.G__plus__, P.H__minus__, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_105})

V_142 = Vertex(name = 'V_142',
               particles = [ P.G__minus__, P.H__plus__, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_105})

V_143 = Vertex(name = 'V_143',
               particles = [ P.hh, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_382})

V_144 = Vertex(name = 'V_144',
               particles = [ P.hh, P.hh, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_31})

V_145 = Vertex(name = 'V_145',
               particles = [ P.h, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_383})

V_146 = Vertex(name = 'V_146',
               particles = [ P.h, P.hh, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_32})

V_147 = Vertex(name = 'V_147',
               particles = [ P.h, P.h, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_33})

V_148 = Vertex(name = 'V_148',
               particles = [ P.hs, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_384})

V_149 = Vertex(name = 'V_149',
               particles = [ P.hh, P.hs, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_34})

V_150 = Vertex(name = 'V_150',
               particles = [ P.h, P.hs, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_35})

V_151 = Vertex(name = 'V_151',
               particles = [ P.hs, P.hs, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_36})

V_152 = Vertex(name = 'V_152',
               particles = [ P.a, P.a, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVS2 ],
               couplings = {(0,0):C.GC_23})

V_153 = Vertex(name = 'V_153',
               particles = [ P.g, P.g, P.hs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVS2 ],
               couplings = {(0,0):C.GC_24})

V_154 = Vertex(name = 'V_154',
               particles = [ P.g, P.g, P.g, P.hs ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVVS1 ],
               couplings = {(0,0):C.GC_25})

V_155 = Vertex(name = 'V_155',
               particles = [ P.g, P.g, P.g, P.g, P.hs ],
               color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
               lorentz = [ L.VVVVS1, L.VVVVS2, L.VVVVS3 ],
               couplings = {(1,1):C.GC_26,(0,0):C.GC_26,(2,2):C.GC_26})

V_156 = Vertex(name = 'V_156',
               particles = [ P.b__tilde__, P.b, P.hs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_421})

V_157 = Vertex(name = 'V_157',
               particles = [ P.d__tilde__, P.d, P.hs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_441})

V_158 = Vertex(name = 'V_158',
               particles = [ P.s__tilde__, P.s, P.hs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_536})

V_159 = Vertex(name = 'V_159',
               particles = [ P.e__plus__, P.e__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_451})

V_160 = Vertex(name = 'V_160',
               particles = [ P.mu__plus__, P.mu__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_463})

V_161 = Vertex(name = 'V_161',
               particles = [ P.ta__plus__, P.ta__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_556})

V_162 = Vertex(name = 'V_162',
               particles = [ P.c__tilde__, P.c, P.hs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_431})

V_163 = Vertex(name = 'V_163',
               particles = [ P.t__tilde__, P.t, P.hs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_546})

V_164 = Vertex(name = 'V_164',
               particles = [ P.u__tilde__, P.u, P.hs ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS5 ],
               couplings = {(0,0):C.GC_568})

V_165 = Vertex(name = 'V_165',
               particles = [ P.G0p, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_361})

V_166 = Vertex(name = 'V_166',
               particles = [ P.G0p, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_360})

V_167 = Vertex(name = 'V_167',
               particles = [ P.nh1__tilde__, P.nh1, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_487,(0,1):C.GC_486})

V_168 = Vertex(name = 'V_168',
               particles = [ P.nle__tilde__, P.nh1, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_477})

V_169 = Vertex(name = 'V_169',
               particles = [ P.nh2__tilde__, P.nh2, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_507,(0,1):C.GC_506})

V_170 = Vertex(name = 'V_170',
               particles = [ P.nlmu__tilde__, P.nh2, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_497})

V_171 = Vertex(name = 'V_171',
               particles = [ P.nh3__tilde__, P.nh3, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_527,(0,1):C.GC_526})

V_172 = Vertex(name = 'V_172',
               particles = [ P.nlta__tilde__, P.nh3, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_517})

V_173 = Vertex(name = 'V_173',
               particles = [ P.G0p, P.G__plus__, P.hh, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_112})

V_174 = Vertex(name = 'V_174',
               particles = [ P.G0p, P.G__minus__, P.hh, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_113})

V_175 = Vertex(name = 'V_175',
               particles = [ P.G0p, P.G__plus__, P.h, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_114})

V_176 = Vertex(name = 'V_176',
               particles = [ P.G0p, P.G__minus__, P.h, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_115})

V_177 = Vertex(name = 'V_177',
               particles = [ P.G0p, P.G__plus__, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_116})

V_178 = Vertex(name = 'V_178',
               particles = [ P.G0p, P.G__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_117})

V_179 = Vertex(name = 'V_179',
               particles = [ P.G0p, P.G0p, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_120})

V_180 = Vertex(name = 'V_180',
               particles = [ P.G0p, P.G0p, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_119})

V_181 = Vertex(name = 'V_181',
               particles = [ P.G0p, P.G0p, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_118})

V_182 = Vertex(name = 'V_182',
               particles = [ P.G0p, P.G0p, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_118})

V_183 = Vertex(name = 'V_183',
               particles = [ P.G0p, P.G0p, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_385})

V_184 = Vertex(name = 'V_184',
               particles = [ P.G0p, P.G0p, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_37})

V_185 = Vertex(name = 'V_185',
               particles = [ P.G0p, P.G0p, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_386})

V_186 = Vertex(name = 'V_186',
               particles = [ P.G0p, P.G0p, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_38})

V_187 = Vertex(name = 'V_187',
               particles = [ P.G0p, P.G0p, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_39})

V_188 = Vertex(name = 'V_188',
               particles = [ P.G0p, P.G0p, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_387})

V_189 = Vertex(name = 'V_189',
               particles = [ P.G0p, P.G0p, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_40})

V_190 = Vertex(name = 'V_190',
               particles = [ P.G0p, P.G0p, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_41})

V_191 = Vertex(name = 'V_191',
               particles = [ P.G0p, P.G0p, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_42})

V_192 = Vertex(name = 'V_192',
               particles = [ P.G0p, P.G0p, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_43})

V_193 = Vertex(name = 'V_193',
               particles = [ P.b__tilde__, P.b, P.G0p ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_422,(0,1):C.GC_423})

V_194 = Vertex(name = 'V_194',
               particles = [ P.d__tilde__, P.d, P.G0p ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_442,(0,1):C.GC_443})

V_195 = Vertex(name = 'V_195',
               particles = [ P.s__tilde__, P.s, P.G0p ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_537,(0,1):C.GC_538})

V_196 = Vertex(name = 'V_196',
               particles = [ P.e__plus__, P.e__minus__, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_452,(0,1):C.GC_453})

V_197 = Vertex(name = 'V_197',
               particles = [ P.mu__plus__, P.mu__minus__, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_464,(0,1):C.GC_465})

V_198 = Vertex(name = 'V_198',
               particles = [ P.ta__plus__, P.ta__minus__, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_557,(0,1):C.GC_558})

V_199 = Vertex(name = 'V_199',
               particles = [ P.c__tilde__, P.c, P.G0p ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_433,(0,1):C.GC_432})

V_200 = Vertex(name = 'V_200',
               particles = [ P.t__tilde__, P.t, P.G0p ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_548,(0,1):C.GC_547})

V_201 = Vertex(name = 'V_201',
               particles = [ P.u__tilde__, P.u, P.G0p ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_570,(0,1):C.GC_569})

V_202 = Vertex(name = 'V_202',
               particles = [ P.G0, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_363})

V_203 = Vertex(name = 'V_203',
               particles = [ P.G0, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_362})

V_204 = Vertex(name = 'V_204',
               particles = [ P.nh1__tilde__, P.nh1, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_489,(0,1):C.GC_488})

V_205 = Vertex(name = 'V_205',
               particles = [ P.nle__tilde__, P.nh1, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_479})

V_206 = Vertex(name = 'V_206',
               particles = [ P.nh2__tilde__, P.nh2, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_509,(0,1):C.GC_508})

V_207 = Vertex(name = 'V_207',
               particles = [ P.nlmu__tilde__, P.nh2, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_499})

V_208 = Vertex(name = 'V_208',
               particles = [ P.nh3__tilde__, P.nh3, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_529,(0,1):C.GC_528})

V_209 = Vertex(name = 'V_209',
               particles = [ P.nlta__tilde__, P.nh3, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_519})

V_210 = Vertex(name = 'V_210',
               particles = [ P.G0, P.G__plus__, P.hh, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_121})

V_211 = Vertex(name = 'V_211',
               particles = [ P.G0, P.G__minus__, P.hh, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_122})

V_212 = Vertex(name = 'V_212',
               particles = [ P.G0, P.G__plus__, P.h, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_123})

V_213 = Vertex(name = 'V_213',
               particles = [ P.G0, P.G__minus__, P.h, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_124})

V_214 = Vertex(name = 'V_214',
               particles = [ P.G0, P.G__plus__, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_125})

V_215 = Vertex(name = 'V_215',
               particles = [ P.G0, P.G__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_126})

V_216 = Vertex(name = 'V_216',
               particles = [ P.G0, P.G0p, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_130})

V_217 = Vertex(name = 'V_217',
               particles = [ P.G0, P.G0p, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_129})

V_218 = Vertex(name = 'V_218',
               particles = [ P.G0, P.G0p, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_127})

V_219 = Vertex(name = 'V_219',
               particles = [ P.G0, P.G0p, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_127})

V_220 = Vertex(name = 'V_220',
               particles = [ P.G0, P.G0p, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_388})

V_221 = Vertex(name = 'V_221',
               particles = [ P.G0, P.G0p, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_44})

V_222 = Vertex(name = 'V_222',
               particles = [ P.G0, P.G0p, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_389})

V_223 = Vertex(name = 'V_223',
               particles = [ P.G0, P.G0p, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_45})

V_224 = Vertex(name = 'V_224',
               particles = [ P.G0, P.G0p, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_46})

V_225 = Vertex(name = 'V_225',
               particles = [ P.G0, P.G0p, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_390})

V_226 = Vertex(name = 'V_226',
               particles = [ P.G0, P.G0p, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_47})

V_227 = Vertex(name = 'V_227',
               particles = [ P.G0, P.G0p, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_48})

V_228 = Vertex(name = 'V_228',
               particles = [ P.G0, P.G0p, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_49})

V_229 = Vertex(name = 'V_229',
               particles = [ P.G0, P.G0p, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_50})

V_230 = Vertex(name = 'V_230',
               particles = [ P.G0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_132})

V_231 = Vertex(name = 'V_231',
               particles = [ P.G0, P.G0, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_131})

V_232 = Vertex(name = 'V_232',
               particles = [ P.G0, P.G0, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_128})

V_233 = Vertex(name = 'V_233',
               particles = [ P.G0, P.G0, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_128})

V_234 = Vertex(name = 'V_234',
               particles = [ P.G0, P.G0, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_391})

V_235 = Vertex(name = 'V_235',
               particles = [ P.G0, P.G0, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_51})

V_236 = Vertex(name = 'V_236',
               particles = [ P.G0, P.G0, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_392})

V_237 = Vertex(name = 'V_237',
               particles = [ P.G0, P.G0, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_52})

V_238 = Vertex(name = 'V_238',
               particles = [ P.G0, P.G0, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_53})

V_239 = Vertex(name = 'V_239',
               particles = [ P.G0, P.G0, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_393})

V_240 = Vertex(name = 'V_240',
               particles = [ P.G0, P.G0, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_54})

V_241 = Vertex(name = 'V_241',
               particles = [ P.G0, P.G0, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_55})

V_242 = Vertex(name = 'V_242',
               particles = [ P.G0, P.G0, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_56})

V_243 = Vertex(name = 'V_243',
               particles = [ P.G0, P.G0, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_57})

V_244 = Vertex(name = 'V_244',
               particles = [ P.G0, P.G0, P.G0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_58})

V_245 = Vertex(name = 'V_245',
               particles = [ P.G0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_59})

V_246 = Vertex(name = 'V_246',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_424,(0,1):C.GC_425})

V_247 = Vertex(name = 'V_247',
               particles = [ P.d__tilde__, P.d, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_444,(0,1):C.GC_445})

V_248 = Vertex(name = 'V_248',
               particles = [ P.s__tilde__, P.s, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_539,(0,1):C.GC_540})

V_249 = Vertex(name = 'V_249',
               particles = [ P.e__plus__, P.e__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_454,(0,1):C.GC_455})

V_250 = Vertex(name = 'V_250',
               particles = [ P.mu__plus__, P.mu__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_466,(0,1):C.GC_467})

V_251 = Vertex(name = 'V_251',
               particles = [ P.ta__plus__, P.ta__minus__, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_559,(0,1):C.GC_560})

V_252 = Vertex(name = 'V_252',
               particles = [ P.c__tilde__, P.c, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_435,(0,1):C.GC_434})

V_253 = Vertex(name = 'V_253',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_550,(0,1):C.GC_549})

V_254 = Vertex(name = 'V_254',
               particles = [ P.u__tilde__, P.u, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_572,(0,1):C.GC_571})

V_255 = Vertex(name = 'V_255',
               particles = [ P.A0, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_365})

V_256 = Vertex(name = 'V_256',
               particles = [ P.A0, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_364})

V_257 = Vertex(name = 'V_257',
               particles = [ P.nh1__tilde__, P.nh1, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_491,(0,1):C.GC_490})

V_258 = Vertex(name = 'V_258',
               particles = [ P.nle__tilde__, P.nh1, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_481})

V_259 = Vertex(name = 'V_259',
               particles = [ P.nh2__tilde__, P.nh2, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_511,(0,1):C.GC_510})

V_260 = Vertex(name = 'V_260',
               particles = [ P.nlmu__tilde__, P.nh2, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_501})

V_261 = Vertex(name = 'V_261',
               particles = [ P.nh3__tilde__, P.nh3, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2, L.FFS4 ],
               couplings = {(0,0):C.GC_531,(0,1):C.GC_530})

V_262 = Vertex(name = 'V_262',
               particles = [ P.nlta__tilde__, P.nh3, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_521})

V_263 = Vertex(name = 'V_263',
               particles = [ P.A0, P.G__plus__, P.hh, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_133})

V_264 = Vertex(name = 'V_264',
               particles = [ P.A0, P.G__minus__, P.hh, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_134})

V_265 = Vertex(name = 'V_265',
               particles = [ P.A0, P.G__plus__, P.h, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_135})

V_266 = Vertex(name = 'V_266',
               particles = [ P.A0, P.G__minus__, P.h, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_136})

V_267 = Vertex(name = 'V_267',
               particles = [ P.A0, P.G__plus__, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_137})

V_268 = Vertex(name = 'V_268',
               particles = [ P.A0, P.G__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_138})

V_269 = Vertex(name = 'V_269',
               particles = [ P.A0, P.G0p, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_143})

V_270 = Vertex(name = 'V_270',
               particles = [ P.A0, P.G0p, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_142})

V_271 = Vertex(name = 'V_271',
               particles = [ P.A0, P.G0p, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_139})

V_272 = Vertex(name = 'V_272',
               particles = [ P.A0, P.G0p, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_139})

V_273 = Vertex(name = 'V_273',
               particles = [ P.A0, P.G0p, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_394})

V_274 = Vertex(name = 'V_274',
               particles = [ P.A0, P.G0p, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_60})

V_275 = Vertex(name = 'V_275',
               particles = [ P.A0, P.G0p, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_395})

V_276 = Vertex(name = 'V_276',
               particles = [ P.A0, P.G0p, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_61})

V_277 = Vertex(name = 'V_277',
               particles = [ P.A0, P.G0p, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_62})

V_278 = Vertex(name = 'V_278',
               particles = [ P.A0, P.G0p, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_396})

V_279 = Vertex(name = 'V_279',
               particles = [ P.A0, P.G0p, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_63})

V_280 = Vertex(name = 'V_280',
               particles = [ P.A0, P.G0p, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_64})

V_281 = Vertex(name = 'V_281',
               particles = [ P.A0, P.G0p, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_65})

V_282 = Vertex(name = 'V_282',
               particles = [ P.A0, P.G0p, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_66})

V_283 = Vertex(name = 'V_283',
               particles = [ P.A0, P.G0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_145})

V_284 = Vertex(name = 'V_284',
               particles = [ P.A0, P.G0, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_144})

V_285 = Vertex(name = 'V_285',
               particles = [ P.A0, P.G0, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_140})

V_286 = Vertex(name = 'V_286',
               particles = [ P.A0, P.G0, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_140})

V_287 = Vertex(name = 'V_287',
               particles = [ P.A0, P.G0, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_397})

V_288 = Vertex(name = 'V_288',
               particles = [ P.A0, P.G0, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_67})

V_289 = Vertex(name = 'V_289',
               particles = [ P.A0, P.G0, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_398})

V_290 = Vertex(name = 'V_290',
               particles = [ P.A0, P.G0, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_68})

V_291 = Vertex(name = 'V_291',
               particles = [ P.A0, P.G0, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_69})

V_292 = Vertex(name = 'V_292',
               particles = [ P.A0, P.G0, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_399})

V_293 = Vertex(name = 'V_293',
               particles = [ P.A0, P.G0, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_70})

V_294 = Vertex(name = 'V_294',
               particles = [ P.A0, P.G0, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_71})

V_295 = Vertex(name = 'V_295',
               particles = [ P.A0, P.G0, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_72})

V_296 = Vertex(name = 'V_296',
               particles = [ P.A0, P.G0, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_73})

V_297 = Vertex(name = 'V_297',
               particles = [ P.A0, P.G0, P.G0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_74})

V_298 = Vertex(name = 'V_298',
               particles = [ P.A0, P.G0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_75})

V_299 = Vertex(name = 'V_299',
               particles = [ P.A0, P.A0, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_147})

V_300 = Vertex(name = 'V_300',
               particles = [ P.A0, P.A0, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_146})

V_301 = Vertex(name = 'V_301',
               particles = [ P.A0, P.A0, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_141})

V_302 = Vertex(name = 'V_302',
               particles = [ P.A0, P.A0, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_141})

V_303 = Vertex(name = 'V_303',
               particles = [ P.A0, P.A0, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_400})

V_304 = Vertex(name = 'V_304',
               particles = [ P.A0, P.A0, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_76})

V_305 = Vertex(name = 'V_305',
               particles = [ P.A0, P.A0, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_401})

V_306 = Vertex(name = 'V_306',
               particles = [ P.A0, P.A0, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_77})

V_307 = Vertex(name = 'V_307',
               particles = [ P.A0, P.A0, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_78})

V_308 = Vertex(name = 'V_308',
               particles = [ P.A0, P.A0, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_402})

V_309 = Vertex(name = 'V_309',
               particles = [ P.A0, P.A0, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_79})

V_310 = Vertex(name = 'V_310',
               particles = [ P.A0, P.A0, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_80})

V_311 = Vertex(name = 'V_311',
               particles = [ P.A0, P.A0, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_81})

V_312 = Vertex(name = 'V_312',
               particles = [ P.A0, P.A0, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_82})

V_313 = Vertex(name = 'V_313',
               particles = [ P.A0, P.A0, P.G0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_83})

V_314 = Vertex(name = 'V_314',
               particles = [ P.A0, P.A0, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_84})

V_315 = Vertex(name = 'V_315',
               particles = [ P.A0, P.A0, P.A0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_85})

V_316 = Vertex(name = 'V_316',
               particles = [ P.A0, P.A0, P.A0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_86})

V_317 = Vertex(name = 'V_317',
               particles = [ P.A0, P.A0, P.A0, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_87})

V_318 = Vertex(name = 'V_318',
               particles = [ P.b__tilde__, P.b, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_426})

V_319 = Vertex(name = 'V_319',
               particles = [ P.d__tilde__, P.d, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_446})

V_320 = Vertex(name = 'V_320',
               particles = [ P.s__tilde__, P.s, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_541})

V_321 = Vertex(name = 'V_321',
               particles = [ P.e__plus__, P.e__minus__, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_456})

V_322 = Vertex(name = 'V_322',
               particles = [ P.mu__plus__, P.mu__minus__, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_468})

V_323 = Vertex(name = 'V_323',
               particles = [ P.ta__plus__, P.ta__minus__, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_561})

V_324 = Vertex(name = 'V_324',
               particles = [ P.c__tilde__, P.c, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_436})

V_325 = Vertex(name = 'V_325',
               particles = [ P.t__tilde__, P.t, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_551})

V_326 = Vertex(name = 'V_326',
               particles = [ P.u__tilde__, P.u, P.A0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_573})

V_327 = Vertex(name = 'V_327',
               particles = [ P.a, P.W__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_369})

V_328 = Vertex(name = 'V_328',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_4})

V_329 = Vertex(name = 'V_329',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_330 = Vertex(name = 'V_330',
               particles = [ P.a, P.W__minus__, P.hh, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_168})

V_331 = Vertex(name = 'V_331',
               particles = [ P.W__minus__, P.G__plus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_170})

V_332 = Vertex(name = 'V_332',
               particles = [ P.W__minus__, P.hh, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_167})

V_333 = Vertex(name = 'V_333',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_177})

V_334 = Vertex(name = 'V_334',
               particles = [ P.a, P.W__minus__, P.h, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_174})

V_335 = Vertex(name = 'V_335',
               particles = [ P.W__minus__, P.G__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_176})

V_336 = Vertex(name = 'V_336',
               particles = [ P.W__minus__, P.h, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_173})

V_337 = Vertex(name = 'V_337',
               particles = [ P.a, P.W__minus__, P.G__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_183})

V_338 = Vertex(name = 'V_338',
               particles = [ P.a, P.W__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_180})

V_339 = Vertex(name = 'V_339',
               particles = [ P.W__minus__, P.G__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_182})

V_340 = Vertex(name = 'V_340',
               particles = [ P.W__minus__, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_178})

V_341 = Vertex(name = 'V_341',
               particles = [ P.a, P.W__minus__, P.G0p, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_188})

V_342 = Vertex(name = 'V_342',
               particles = [ P.a, P.W__minus__, P.G0p, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_186})

V_343 = Vertex(name = 'V_343',
               particles = [ P.W__minus__, P.G0p, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_187})

V_344 = Vertex(name = 'V_344',
               particles = [ P.W__minus__, P.G0p, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_184})

V_345 = Vertex(name = 'V_345',
               particles = [ P.a, P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_194})

V_346 = Vertex(name = 'V_346',
               particles = [ P.a, P.W__minus__, P.G0, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_192})

V_347 = Vertex(name = 'V_347',
               particles = [ P.W__minus__, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_193})

V_348 = Vertex(name = 'V_348',
               particles = [ P.W__minus__, P.G0, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_190})

V_349 = Vertex(name = 'V_349',
               particles = [ P.a, P.W__minus__, P.A0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_200})

V_350 = Vertex(name = 'V_350',
               particles = [ P.a, P.W__minus__, P.A0, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_198})

V_351 = Vertex(name = 'V_351',
               particles = [ P.W__minus__, P.A0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_199})

V_352 = Vertex(name = 'V_352',
               particles = [ P.W__minus__, P.A0, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_196})

V_353 = Vertex(name = 'V_353',
               particles = [ P.a, P.W__plus__, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_369})

V_354 = Vertex(name = 'V_354',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_171})

V_355 = Vertex(name = 'V_355',
               particles = [ P.a, P.W__plus__, P.hh, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_168})

V_356 = Vertex(name = 'V_356',
               particles = [ P.W__plus__, P.G__minus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_169})

V_357 = Vertex(name = 'V_357',
               particles = [ P.W__plus__, P.hh, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_166})

V_358 = Vertex(name = 'V_358',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_177})

V_359 = Vertex(name = 'V_359',
               particles = [ P.a, P.W__plus__, P.h, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_174})

V_360 = Vertex(name = 'V_360',
               particles = [ P.W__plus__, P.G__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_175})

V_361 = Vertex(name = 'V_361',
               particles = [ P.W__plus__, P.h, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_172})

V_362 = Vertex(name = 'V_362',
               particles = [ P.a, P.W__plus__, P.G__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_183})

V_363 = Vertex(name = 'V_363',
               particles = [ P.a, P.W__plus__, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_180})

V_364 = Vertex(name = 'V_364',
               particles = [ P.W__plus__, P.G__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_181})

V_365 = Vertex(name = 'V_365',
               particles = [ P.W__plus__, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_179})

V_366 = Vertex(name = 'V_366',
               particles = [ P.a, P.W__plus__, P.G0p, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_189})

V_367 = Vertex(name = 'V_367',
               particles = [ P.a, P.W__plus__, P.G0p, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_185})

V_368 = Vertex(name = 'V_368',
               particles = [ P.W__plus__, P.G0p, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_187})

V_369 = Vertex(name = 'V_369',
               particles = [ P.W__plus__, P.G0p, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_184})

V_370 = Vertex(name = 'V_370',
               particles = [ P.a, P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_195})

V_371 = Vertex(name = 'V_371',
               particles = [ P.a, P.W__plus__, P.G0, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_191})

V_372 = Vertex(name = 'V_372',
               particles = [ P.W__plus__, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_193})

V_373 = Vertex(name = 'V_373',
               particles = [ P.W__plus__, P.G0, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_190})

V_374 = Vertex(name = 'V_374',
               particles = [ P.a, P.W__plus__, P.A0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_201})

V_375 = Vertex(name = 'V_375',
               particles = [ P.a, P.W__plus__, P.A0, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_197})

V_376 = Vertex(name = 'V_376',
               particles = [ P.W__plus__, P.A0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_199})

V_377 = Vertex(name = 'V_377',
               particles = [ P.W__plus__, P.A0, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_196})

V_378 = Vertex(name = 'V_378',
               particles = [ P.W__minus__, P.W__plus__, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_165})

V_379 = Vertex(name = 'V_379',
               particles = [ P.W__minus__, P.W__plus__, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_165})

V_380 = Vertex(name = 'V_380',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_5})

V_381 = Vertex(name = 'V_381',
               particles = [ P.W__minus__, P.W__plus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_366})

V_382 = Vertex(name = 'V_382',
               particles = [ P.W__minus__, P.W__plus__, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_153})

V_383 = Vertex(name = 'V_383',
               particles = [ P.W__minus__, P.W__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_367})

V_384 = Vertex(name = 'V_384',
               particles = [ P.W__minus__, P.W__plus__, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_154})

V_385 = Vertex(name = 'V_385',
               particles = [ P.W__minus__, P.W__plus__, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_155})

V_386 = Vertex(name = 'V_386',
               particles = [ P.W__minus__, P.W__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_368})

V_387 = Vertex(name = 'V_387',
               particles = [ P.W__minus__, P.W__plus__, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_156})

V_388 = Vertex(name = 'V_388',
               particles = [ P.W__minus__, P.W__plus__, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_157})

V_389 = Vertex(name = 'V_389',
               particles = [ P.W__minus__, P.W__plus__, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_158})

V_390 = Vertex(name = 'V_390',
               particles = [ P.W__minus__, P.W__plus__, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_159})

V_391 = Vertex(name = 'V_391',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_160})

V_392 = Vertex(name = 'V_392',
               particles = [ P.W__minus__, P.W__plus__, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_161})

V_393 = Vertex(name = 'V_393',
               particles = [ P.W__minus__, P.W__plus__, P.A0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_162})

V_394 = Vertex(name = 'V_394',
               particles = [ P.W__minus__, P.W__plus__, P.A0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_163})

V_395 = Vertex(name = 'V_395',
               particles = [ P.W__minus__, P.W__plus__, P.A0, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_164})

V_396 = Vertex(name = 'V_396',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_208})

V_397 = Vertex(name = 'V_397',
               particles = [ P.W__minus__, P.W__plus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.VVV1 ],
               couplings = {(0,0):C.GC_220})

V_398 = Vertex(name = 'V_398',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_202})

V_399 = Vertex(name = 'V_399',
               particles = [ P.e__plus__, P.nle, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_448})

V_400 = Vertex(name = 'V_400',
               particles = [ P.e__plus__, P.nle, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_457})

V_401 = Vertex(name = 'V_401',
               particles = [ P.mu__plus__, P.nlmu, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_460})

V_402 = Vertex(name = 'V_402',
               particles = [ P.mu__plus__, P.nlmu, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_469})

V_403 = Vertex(name = 'V_403',
               particles = [ P.ta__plus__, P.nlta, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_553})

V_404 = Vertex(name = 'V_404',
               particles = [ P.ta__plus__, P.nlta, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_562})

V_405 = Vertex(name = 'V_405',
               particles = [ P.nh1__tilde__, P.nle, P.hh ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_473})

V_406 = Vertex(name = 'V_406',
               particles = [ P.nh1__tilde__, P.nle, P.h ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_474})

V_407 = Vertex(name = 'V_407',
               particles = [ P.nh1__tilde__, P.nle, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_475})

V_408 = Vertex(name = 'V_408',
               particles = [ P.nh1__tilde__, P.nle, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_476})

V_409 = Vertex(name = 'V_409',
               particles = [ P.nh1__tilde__, P.nle, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_478})

V_410 = Vertex(name = 'V_410',
               particles = [ P.nh1__tilde__, P.nle, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_480})

V_411 = Vertex(name = 'V_411',
               particles = [ P.nh2__tilde__, P.nlmu, P.hh ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_493})

V_412 = Vertex(name = 'V_412',
               particles = [ P.nh2__tilde__, P.nlmu, P.h ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_494})

V_413 = Vertex(name = 'V_413',
               particles = [ P.nh2__tilde__, P.nlmu, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_495})

V_414 = Vertex(name = 'V_414',
               particles = [ P.nh2__tilde__, P.nlmu, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_496})

V_415 = Vertex(name = 'V_415',
               particles = [ P.nh2__tilde__, P.nlmu, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_498})

V_416 = Vertex(name = 'V_416',
               particles = [ P.nh2__tilde__, P.nlmu, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_500})

V_417 = Vertex(name = 'V_417',
               particles = [ P.nh3__tilde__, P.nlta, P.hh ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_513})

V_418 = Vertex(name = 'V_418',
               particles = [ P.nh3__tilde__, P.nlta, P.h ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_514})

V_419 = Vertex(name = 'V_419',
               particles = [ P.nh3__tilde__, P.nlta, P.hs ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_515})

V_420 = Vertex(name = 'V_420',
               particles = [ P.nh3__tilde__, P.nlta, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_516})

V_421 = Vertex(name = 'V_421',
               particles = [ P.nh3__tilde__, P.nlta, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_518})

V_422 = Vertex(name = 'V_422',
               particles = [ P.nh3__tilde__, P.nlta, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_520})

V_423 = Vertex(name = 'V_423',
               particles = [ P.a, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_232})

V_424 = Vertex(name = 'V_424',
               particles = [ P.a, P.Z, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_261})

V_425 = Vertex(name = 'V_425',
               particles = [ P.a, P.Z, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_218})

V_426 = Vertex(name = 'V_426',
               particles = [ P.a, P.Z, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_218})

V_427 = Vertex(name = 'V_427',
               particles = [ P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_228})

V_428 = Vertex(name = 'V_428',
               particles = [ P.Z, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_217})

V_429 = Vertex(name = 'V_429',
               particles = [ P.Z, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_216})

V_430 = Vertex(name = 'V_430',
               particles = [ P.Z, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_260})

V_431 = Vertex(name = 'V_431',
               particles = [ P.Z, P.G0p, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_233})

V_432 = Vertex(name = 'V_432',
               particles = [ P.Z, P.G0p, P.h ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_234})

V_433 = Vertex(name = 'V_433',
               particles = [ P.Z, P.G0p, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_235})

V_434 = Vertex(name = 'V_434',
               particles = [ P.Z, P.G0, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_236})

V_435 = Vertex(name = 'V_435',
               particles = [ P.Z, P.G0, P.h ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_237})

V_436 = Vertex(name = 'V_436',
               particles = [ P.Z, P.G0, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_238})

V_437 = Vertex(name = 'V_437',
               particles = [ P.Z, P.A0, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_239})

V_438 = Vertex(name = 'V_438',
               particles = [ P.Z, P.A0, P.h ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_240})

V_439 = Vertex(name = 'V_439',
               particles = [ P.Z, P.A0, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_241})

V_440 = Vertex(name = 'V_440',
               particles = [ P.W__minus__, P.Z, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_371})

V_441 = Vertex(name = 'V_441',
               particles = [ P.W__minus__, P.Z, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_359})

V_442 = Vertex(name = 'V_442',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_268})

V_443 = Vertex(name = 'V_443',
               particles = [ P.W__minus__, P.Z, P.hh, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_277})

V_444 = Vertex(name = 'V_444',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_269})

V_445 = Vertex(name = 'V_445',
               particles = [ P.W__minus__, P.Z, P.h, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_278})

V_446 = Vertex(name = 'V_446',
               particles = [ P.W__minus__, P.Z, P.G__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_270})

V_447 = Vertex(name = 'V_447',
               particles = [ P.W__minus__, P.Z, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_279})

V_448 = Vertex(name = 'V_448',
               particles = [ P.W__minus__, P.Z, P.G0p, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_271})

V_449 = Vertex(name = 'V_449',
               particles = [ P.W__minus__, P.Z, P.G0p, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_281})

V_450 = Vertex(name = 'V_450',
               particles = [ P.W__minus__, P.Z, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_273})

V_451 = Vertex(name = 'V_451',
               particles = [ P.W__minus__, P.Z, P.G0, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_283})

V_452 = Vertex(name = 'V_452',
               particles = [ P.W__minus__, P.Z, P.A0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_275})

V_453 = Vertex(name = 'V_453',
               particles = [ P.W__minus__, P.Z, P.A0, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_285})

V_454 = Vertex(name = 'V_454',
               particles = [ P.W__plus__, P.Z, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_371})

V_455 = Vertex(name = 'V_455',
               particles = [ P.W__plus__, P.Z, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_359})

V_456 = Vertex(name = 'V_456',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_268})

V_457 = Vertex(name = 'V_457',
               particles = [ P.W__plus__, P.Z, P.hh, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_277})

V_458 = Vertex(name = 'V_458',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_269})

V_459 = Vertex(name = 'V_459',
               particles = [ P.W__plus__, P.Z, P.h, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_278})

V_460 = Vertex(name = 'V_460',
               particles = [ P.W__plus__, P.Z, P.G__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_270})

V_461 = Vertex(name = 'V_461',
               particles = [ P.W__plus__, P.Z, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_279})

V_462 = Vertex(name = 'V_462',
               particles = [ P.W__plus__, P.Z, P.G0p, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_272})

V_463 = Vertex(name = 'V_463',
               particles = [ P.W__plus__, P.Z, P.G0p, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_280})

V_464 = Vertex(name = 'V_464',
               particles = [ P.W__plus__, P.Z, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_274})

V_465 = Vertex(name = 'V_465',
               particles = [ P.W__plus__, P.Z, P.G0, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_282})

V_466 = Vertex(name = 'V_466',
               particles = [ P.W__plus__, P.Z, P.A0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_276})

V_467 = Vertex(name = 'V_467',
               particles = [ P.W__plus__, P.Z, P.A0, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_284})

V_468 = Vertex(name = 'V_468',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_209})

V_469 = Vertex(name = 'V_469',
               particles = [ P.Z, P.Z, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_314})

V_470 = Vertex(name = 'V_470',
               particles = [ P.Z, P.Z, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_328})

V_471 = Vertex(name = 'V_471',
               particles = [ P.Z, P.Z, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_327})

V_472 = Vertex(name = 'V_472',
               particles = [ P.Z, P.Z, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_327})

V_473 = Vertex(name = 'V_473',
               particles = [ P.Z, P.Z, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_415})

V_474 = Vertex(name = 'V_474',
               particles = [ P.Z, P.Z, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_315})

V_475 = Vertex(name = 'V_475',
               particles = [ P.Z, P.Z, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_416})

V_476 = Vertex(name = 'V_476',
               particles = [ P.Z, P.Z, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_316})

V_477 = Vertex(name = 'V_477',
               particles = [ P.Z, P.Z, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_317})

V_478 = Vertex(name = 'V_478',
               particles = [ P.Z, P.Z, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_417})

V_479 = Vertex(name = 'V_479',
               particles = [ P.Z, P.Z, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_318})

V_480 = Vertex(name = 'V_480',
               particles = [ P.Z, P.Z, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_319})

V_481 = Vertex(name = 'V_481',
               particles = [ P.Z, P.Z, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_320})

V_482 = Vertex(name = 'V_482',
               particles = [ P.Z, P.Z, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_321})

V_483 = Vertex(name = 'V_483',
               particles = [ P.Z, P.Z, P.G0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_322})

V_484 = Vertex(name = 'V_484',
               particles = [ P.Z, P.Z, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_323})

V_485 = Vertex(name = 'V_485',
               particles = [ P.Z, P.Z, P.A0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_324})

V_486 = Vertex(name = 'V_486',
               particles = [ P.Z, P.Z, P.A0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_325})

V_487 = Vertex(name = 'V_487',
               particles = [ P.Z, P.Z, P.A0, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_326})

V_488 = Vertex(name = 'V_488',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_203})

V_489 = Vertex(name = 'V_489',
               particles = [ P.a, P.Zp, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_306})

V_490 = Vertex(name = 'V_490',
               particles = [ P.a, P.Zp, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_90})

V_491 = Vertex(name = 'V_491',
               particles = [ P.a, P.Zp, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_90})

V_492 = Vertex(name = 'V_492',
               particles = [ P.a, P.Zp, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_307})

V_493 = Vertex(name = 'V_493',
               particles = [ P.Zp, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_304})

V_494 = Vertex(name = 'V_494',
               particles = [ P.Zp, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_89})

V_495 = Vertex(name = 'V_495',
               particles = [ P.Zp, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_88})

V_496 = Vertex(name = 'V_496',
               particles = [ P.Zp, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_305})

V_497 = Vertex(name = 'V_497',
               particles = [ P.Zp, P.G0p, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_294})

V_498 = Vertex(name = 'V_498',
               particles = [ P.Zp, P.G0p, P.h ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_295})

V_499 = Vertex(name = 'V_499',
               particles = [ P.Zp, P.G0p, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_296})

V_500 = Vertex(name = 'V_500',
               particles = [ P.Zp, P.G0, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_297})

V_501 = Vertex(name = 'V_501',
               particles = [ P.Zp, P.G0, P.h ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_298})

V_502 = Vertex(name = 'V_502',
               particles = [ P.Zp, P.G0, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_299})

V_503 = Vertex(name = 'V_503',
               particles = [ P.Zp, P.A0, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_300})

V_504 = Vertex(name = 'V_504',
               particles = [ P.Zp, P.A0, P.h ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_301})

V_505 = Vertex(name = 'V_505',
               particles = [ P.Zp, P.A0, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_302})

V_506 = Vertex(name = 'V_506',
               particles = [ P.W__minus__, P.Zp, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_370})

V_507 = Vertex(name = 'V_507',
               particles = [ P.W__minus__, P.Zp, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_358})

V_508 = Vertex(name = 'V_508',
               particles = [ P.W__minus__, P.Zp, P.G__plus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_243})

V_509 = Vertex(name = 'V_509',
               particles = [ P.W__minus__, P.Zp, P.hh, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_242})

V_510 = Vertex(name = 'V_510',
               particles = [ P.W__minus__, P.Zp, P.G__plus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_245})

V_511 = Vertex(name = 'V_511',
               particles = [ P.W__minus__, P.Zp, P.h, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_244})

V_512 = Vertex(name = 'V_512',
               particles = [ P.W__minus__, P.Zp, P.G__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_247})

V_513 = Vertex(name = 'V_513',
               particles = [ P.W__minus__, P.Zp, P.H__plus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_246})

V_514 = Vertex(name = 'V_514',
               particles = [ P.W__minus__, P.Zp, P.G0p, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_250})

V_515 = Vertex(name = 'V_515',
               particles = [ P.W__minus__, P.Zp, P.G0p, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_249})

V_516 = Vertex(name = 'V_516',
               particles = [ P.W__minus__, P.Zp, P.G0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_254})

V_517 = Vertex(name = 'V_517',
               particles = [ P.W__minus__, P.Zp, P.G0, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_253})

V_518 = Vertex(name = 'V_518',
               particles = [ P.W__minus__, P.Zp, P.A0, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_258})

V_519 = Vertex(name = 'V_519',
               particles = [ P.W__minus__, P.Zp, P.A0, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_257})

V_520 = Vertex(name = 'V_520',
               particles = [ P.W__plus__, P.Zp, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_370})

V_521 = Vertex(name = 'V_521',
               particles = [ P.W__plus__, P.Zp, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_358})

V_522 = Vertex(name = 'V_522',
               particles = [ P.W__plus__, P.Zp, P.G__minus__, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_243})

V_523 = Vertex(name = 'V_523',
               particles = [ P.W__plus__, P.Zp, P.hh, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_242})

V_524 = Vertex(name = 'V_524',
               particles = [ P.W__plus__, P.Zp, P.G__minus__, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_245})

V_525 = Vertex(name = 'V_525',
               particles = [ P.W__plus__, P.Zp, P.h, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_244})

V_526 = Vertex(name = 'V_526',
               particles = [ P.W__plus__, P.Zp, P.G__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_247})

V_527 = Vertex(name = 'V_527',
               particles = [ P.W__plus__, P.Zp, P.H__minus__, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_246})

V_528 = Vertex(name = 'V_528',
               particles = [ P.W__plus__, P.Zp, P.G0p, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_251})

V_529 = Vertex(name = 'V_529',
               particles = [ P.W__plus__, P.Zp, P.G0p, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_248})

V_530 = Vertex(name = 'V_530',
               particles = [ P.W__plus__, P.Zp, P.G0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_255})

V_531 = Vertex(name = 'V_531',
               particles = [ P.W__plus__, P.Zp, P.G0, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_252})

V_532 = Vertex(name = 'V_532',
               particles = [ P.W__plus__, P.Zp, P.A0, P.G__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_259})

V_533 = Vertex(name = 'V_533',
               particles = [ P.W__plus__, P.Zp, P.A0, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_256})

V_534 = Vertex(name = 'V_534',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_221})

V_535 = Vertex(name = 'V_535',
               particles = [ P.Z, P.Zp, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_329})

V_536 = Vertex(name = 'V_536',
               particles = [ P.Z, P.Zp, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_342})

V_537 = Vertex(name = 'V_537',
               particles = [ P.Z, P.Zp, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_342})

V_538 = Vertex(name = 'V_538',
               particles = [ P.Z, P.Zp, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_343})

V_539 = Vertex(name = 'V_539',
               particles = [ P.Z, P.Zp, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_412})

V_540 = Vertex(name = 'V_540',
               particles = [ P.Z, P.Zp, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_330})

V_541 = Vertex(name = 'V_541',
               particles = [ P.Z, P.Zp, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_413})

V_542 = Vertex(name = 'V_542',
               particles = [ P.Z, P.Zp, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_331})

V_543 = Vertex(name = 'V_543',
               particles = [ P.Z, P.Zp, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_332})

V_544 = Vertex(name = 'V_544',
               particles = [ P.Z, P.Zp, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_414})

V_545 = Vertex(name = 'V_545',
               particles = [ P.Z, P.Zp, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_333})

V_546 = Vertex(name = 'V_546',
               particles = [ P.Z, P.Zp, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_334})

V_547 = Vertex(name = 'V_547',
               particles = [ P.Z, P.Zp, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_335})

V_548 = Vertex(name = 'V_548',
               particles = [ P.Z, P.Zp, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_336})

V_549 = Vertex(name = 'V_549',
               particles = [ P.Z, P.Zp, P.G0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_337})

V_550 = Vertex(name = 'V_550',
               particles = [ P.Z, P.Zp, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_338})

V_551 = Vertex(name = 'V_551',
               particles = [ P.Z, P.Zp, P.A0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_339})

V_552 = Vertex(name = 'V_552',
               particles = [ P.Z, P.Zp, P.A0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_340})

V_553 = Vertex(name = 'V_553',
               particles = [ P.Z, P.Zp, P.A0, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_341})

V_554 = Vertex(name = 'V_554',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_219})

V_555 = Vertex(name = 'V_555',
               particles = [ P.Zp, P.Zp, P.G__minus__, P.G__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_356})

V_556 = Vertex(name = 'V_556',
               particles = [ P.Zp, P.Zp, P.G__plus__, P.H__minus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_303})

V_557 = Vertex(name = 'V_557',
               particles = [ P.Zp, P.Zp, P.G__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_303})

V_558 = Vertex(name = 'V_558',
               particles = [ P.Zp, P.Zp, P.H__minus__, P.H__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_357})

V_559 = Vertex(name = 'V_559',
               particles = [ P.Zp, P.Zp, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_372})

V_560 = Vertex(name = 'V_560',
               particles = [ P.Zp, P.Zp, P.hh, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_344})

V_561 = Vertex(name = 'V_561',
               particles = [ P.Zp, P.Zp, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_374})

V_562 = Vertex(name = 'V_562',
               particles = [ P.Zp, P.Zp, P.h, P.hh ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_345})

V_563 = Vertex(name = 'V_563',
               particles = [ P.Zp, P.Zp, P.h, P.h ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_346})

V_564 = Vertex(name = 'V_564',
               particles = [ P.Zp, P.Zp, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_378})

V_565 = Vertex(name = 'V_565',
               particles = [ P.Zp, P.Zp, P.hh, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_347})

V_566 = Vertex(name = 'V_566',
               particles = [ P.Zp, P.Zp, P.h, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_348})

V_567 = Vertex(name = 'V_567',
               particles = [ P.Zp, P.Zp, P.hs, P.hs ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_349})

V_568 = Vertex(name = 'V_568',
               particles = [ P.Zp, P.Zp, P.G0p, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_350})

V_569 = Vertex(name = 'V_569',
               particles = [ P.Zp, P.Zp, P.G0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_351})

V_570 = Vertex(name = 'V_570',
               particles = [ P.Zp, P.Zp, P.G0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_352})

V_571 = Vertex(name = 'V_571',
               particles = [ P.Zp, P.Zp, P.A0, P.G0p ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_353})

V_572 = Vertex(name = 'V_572',
               particles = [ P.Zp, P.Zp, P.A0, P.G0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_354})

V_573 = Vertex(name = 'V_573',
               particles = [ P.Zp, P.Zp, P.A0, P.A0 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_355})

V_574 = Vertex(name = 'V_574',
               particles = [ P.W__minus__, P.W__plus__, P.Zp, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.VVVV2 ],
               couplings = {(0,0):C.GC_223})

V_575 = Vertex(name = 'V_575',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_576 = Vertex(name = 'V_576',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_577 = Vertex(name = 'V_577',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_3})

V_578 = Vertex(name = 'V_578',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_579 = Vertex(name = 'V_579',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_580 = Vertex(name = 'V_580',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_581 = Vertex(name = 'V_581',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_582 = Vertex(name = 'V_582',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_583 = Vertex(name = 'V_583',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1})

V_584 = Vertex(name = 'V_584',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_585 = Vertex(name = 'V_585',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_586 = Vertex(name = 'V_586',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_587 = Vertex(name = 'V_587',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_588 = Vertex(name = 'V_588',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_589 = Vertex(name = 'V_589',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_7})

V_590 = Vertex(name = 'V_590',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_204})

V_591 = Vertex(name = 'V_591',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_204})

V_592 = Vertex(name = 'V_592',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_204})

V_593 = Vertex(name = 'V_593',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_204})

V_594 = Vertex(name = 'V_594',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_204})

V_595 = Vertex(name = 'V_595',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_204})

V_596 = Vertex(name = 'V_596',
               particles = [ P.e__plus__, P.nh1, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_210})

V_597 = Vertex(name = 'V_597',
               particles = [ P.mu__plus__, P.nh2, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_211})

V_598 = Vertex(name = 'V_598',
               particles = [ P.ta__plus__, P.nh3, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_212})

V_599 = Vertex(name = 'V_599',
               particles = [ P.e__plus__, P.nle, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_205})

V_600 = Vertex(name = 'V_600',
               particles = [ P.mu__plus__, P.nlmu, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_206})

V_601 = Vertex(name = 'V_601',
               particles = [ P.ta__plus__, P.nlta, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_207})

V_602 = Vertex(name = 'V_602',
               particles = [ P.nh1__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_210})

V_603 = Vertex(name = 'V_603',
               particles = [ P.nle__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_205})

V_604 = Vertex(name = 'V_604',
               particles = [ P.nh2__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_211})

V_605 = Vertex(name = 'V_605',
               particles = [ P.nlmu__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_206})

V_606 = Vertex(name = 'V_606',
               particles = [ P.nh3__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_212})

V_607 = Vertex(name = 'V_607',
               particles = [ P.nlta__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_207})

V_608 = Vertex(name = 'V_608',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_225,(0,1):C.GC_227})

V_609 = Vertex(name = 'V_609',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_225,(0,1):C.GC_227})

V_610 = Vertex(name = 'V_610',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_225,(0,1):C.GC_227})

V_611 = Vertex(name = 'V_611',
               particles = [ P.c__tilde__, P.c, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_290})

V_612 = Vertex(name = 'V_612',
               particles = [ P.t__tilde__, P.t, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_290})

V_613 = Vertex(name = 'V_613',
               particles = [ P.u__tilde__, P.u, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_290})

V_614 = Vertex(name = 'V_614',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_224,(0,1):C.GC_226})

V_615 = Vertex(name = 'V_615',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_224,(0,1):C.GC_226})

V_616 = Vertex(name = 'V_616',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_224,(0,1):C.GC_226})

V_617 = Vertex(name = 'V_617',
               particles = [ P.b__tilde__, P.b, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_288})

V_618 = Vertex(name = 'V_618',
               particles = [ P.d__tilde__, P.d, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_288})

V_619 = Vertex(name = 'V_619',
               particles = [ P.s__tilde__, P.s, P.Zp ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_288})

V_620 = Vertex(name = 'V_620',
               particles = [ P.nh1__tilde__, P.nh1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_229,(0,1):C.GC_215})

V_621 = Vertex(name = 'V_621',
               particles = [ P.nle__tilde__, P.nh1, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_262})

V_622 = Vertex(name = 'V_622',
               particles = [ P.nh2__tilde__, P.nh2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_230,(0,1):C.GC_215})

V_623 = Vertex(name = 'V_623',
               particles = [ P.nlmu__tilde__, P.nh2, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_264})

V_624 = Vertex(name = 'V_624',
               particles = [ P.nh3__tilde__, P.nh3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_215})

V_625 = Vertex(name = 'V_625',
               particles = [ P.nlta__tilde__, P.nh3, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_266})

V_626 = Vertex(name = 'V_626',
               particles = [ P.nh1__tilde__, P.nle, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_262})

V_627 = Vertex(name = 'V_627',
               particles = [ P.nle__tilde__, P.nle, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_263})

V_628 = Vertex(name = 'V_628',
               particles = [ P.nh2__tilde__, P.nlmu, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_264})

V_629 = Vertex(name = 'V_629',
               particles = [ P.nlmu__tilde__, P.nlmu, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_265})

V_630 = Vertex(name = 'V_630',
               particles = [ P.nh3__tilde__, P.nlta, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_266})

V_631 = Vertex(name = 'V_631',
               particles = [ P.nlta__tilde__, P.nlta, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_267})

V_632 = Vertex(name = 'V_632',
               particles = [ P.nh1__tilde__, P.nh1, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_309,(0,1):C.GC_9})

V_633 = Vertex(name = 'V_633',
               particles = [ P.nle__tilde__, P.nh1, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_308})

V_634 = Vertex(name = 'V_634',
               particles = [ P.nh2__tilde__, P.nh2, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_311,(0,1):C.GC_9})

V_635 = Vertex(name = 'V_635',
               particles = [ P.nlmu__tilde__, P.nh2, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_310})

V_636 = Vertex(name = 'V_636',
               particles = [ P.nh3__tilde__, P.nh3, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_313,(0,1):C.GC_9})

V_637 = Vertex(name = 'V_637',
               particles = [ P.nlta__tilde__, P.nh3, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_312})

V_638 = Vertex(name = 'V_638',
               particles = [ P.nh1__tilde__, P.nle, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_308})

V_639 = Vertex(name = 'V_639',
               particles = [ P.nle__tilde__, P.nle, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_291})

V_640 = Vertex(name = 'V_640',
               particles = [ P.nh2__tilde__, P.nlmu, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_310})

V_641 = Vertex(name = 'V_641',
               particles = [ P.nlmu__tilde__, P.nlmu, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_292})

V_642 = Vertex(name = 'V_642',
               particles = [ P.nh3__tilde__, P.nlta, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_312})

V_643 = Vertex(name = 'V_643',
               particles = [ P.nlta__tilde__, P.nlta, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_293})

V_644 = Vertex(name = 'V_644',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_214,(0,1):C.GC_213})

V_645 = Vertex(name = 'V_645',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_214,(0,1):C.GC_213})

V_646 = Vertex(name = 'V_646',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_214,(0,1):C.GC_213})

V_647 = Vertex(name = 'V_647',
               particles = [ P.e__plus__, P.e__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_289,(0,1):C.GC_222})

V_648 = Vertex(name = 'V_648',
               particles = [ P.mu__plus__, P.mu__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_289,(0,1):C.GC_222})

V_649 = Vertex(name = 'V_649',
               particles = [ P.ta__plus__, P.ta__minus__, P.Zp ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_289,(0,1):C.GC_222})

