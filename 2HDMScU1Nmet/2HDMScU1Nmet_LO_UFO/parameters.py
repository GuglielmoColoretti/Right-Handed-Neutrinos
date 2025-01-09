# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 9 Jan 2025 17:47:22



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

a1 = Parameter(name = 'a1',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\alpha _1',
               lhablock = 'THDMSBLOCK',
               lhacode = [ 1 ])

a2 = Parameter(name = 'a2',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\alpha _2',
               lhablock = 'THDMSBLOCK',
               lhacode = [ 2 ])

a3 = Parameter(name = 'a3',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\alpha _3',
               lhablock = 'THDMSBLOCK',
               lhacode = [ 3 ])

tanb = Parameter(name = 'tanb',
                 nature = 'external',
                 type = 'real',
                 value = 15,
                 texname = 't_{\\beta }',
                 lhablock = 'THDMSBLOCK',
                 lhacode = [ 4 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

sw = Parameter(name = 'sw',
               nature = 'external',
               type = 'real',
               value = 0.4722287581247038,
               texname = 's_w',
               lhablock = 'FRBlock',
               lhacode = [ 1 ])

theta1N = Parameter(name = 'theta1N',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{$\\theta $1}_n',
                    lhablock = 'FRBlock',
                    lhacode = [ 2 ])

theta2N = Parameter(name = 'theta2N',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{$\\theta $2}_n',
                    lhablock = 'FRBlock',
                    lhacode = [ 3 ])

theta3N = Parameter(name = 'theta3N',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{$\\theta $3}_n',
                    lhablock = 'FRBlock',
                    lhacode = [ 4 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.406,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

MZP = Parameter(name = 'MZP',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MZP}',
                lhablock = 'MASS',
                lhacode = [ 9000023 ])

Mnh1 = Parameter(name = 'Mnh1',
                 nature = 'external',
                 type = 'real',
                 value = 100.,
                 texname = '\\text{Mnh1}',
                 lhablock = 'MASS',
                 lhacode = [ 9000012 ])

Mnh2 = Parameter(name = 'Mnh2',
                 nature = 'external',
                 type = 'real',
                 value = 100.,
                 texname = '\\text{Mnh2}',
                 lhablock = 'MASS',
                 lhacode = [ 9000014 ])

Mnh3 = Parameter(name = 'Mnh3',
                 nature = 'external',
                 type = 'real',
                 value = 100.,
                 texname = '\\text{Mnh3}',
                 lhablock = 'MASS',
                 lhacode = [ 9000016 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Mcsi = Parameter(name = 'Mcsi',
                 nature = 'external',
                 type = 'real',
                 value = 50,
                 texname = '\\text{Mcsi}',
                 lhablock = 'MASS',
                 lhacode = [ 9900012 ])

Mhh = Parameter(name = 'Mhh',
                nature = 'external',
                type = 'real',
                value = 270,
                texname = '\\text{Mhh}',
                lhablock = 'MASS',
                lhacode = [ 9000026 ])

Mh = Parameter(name = 'Mh',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{Mh}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

Mhs = Parameter(name = 'Mhs',
                nature = 'external',
                type = 'real',
                value = 150,
                texname = '\\text{Mhs}',
                lhablock = 'MASS',
                lhacode = [ 9000027 ])

MA0 = Parameter(name = 'MA0',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MA0}',
                lhablock = 'MASS',
                lhacode = [ 9000001 ])

MHP = Parameter(name = 'MHP',
                nature = 'external',
                type = 'real',
                value = 1000.,
                texname = '\\text{MHP}',
                lhablock = 'MASS',
                lhacode = [ 9000002 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WZP = Parameter(name = 'WZP',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = '\\text{WZP}',
                lhablock = 'DECAY',
                lhacode = [ 9000023 ])

Wnh1 = Parameter(name = 'Wnh1',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{Wnh1}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000012 ])

Wnh2 = Parameter(name = 'Wnh2',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{Wnh2}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000014 ])

Wnh3 = Parameter(name = 'Wnh3',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{Wnh3}',
                 lhablock = 'DECAY',
                 lhacode = [ 9000016 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Whh = Parameter(name = 'Whh',
                nature = 'external',
                type = 'real',
                value = 0.00407,
                texname = '\\text{Whh}',
                lhablock = 'DECAY',
                lhacode = [ 9000026 ])

Wh = Parameter(name = 'Wh',
               nature = 'external',
               type = 'real',
               value = 0.006382339,
               texname = '\\text{Wh}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

Whs = Parameter(name = 'Whs',
                nature = 'external',
                type = 'real',
                value = 0.4952,
                texname = '\\text{Whs}',
                lhablock = 'DECAY',
                lhacode = [ 9000027 ])

WA0 = Parameter(name = 'WA0',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = '\\text{WA0}',
                lhablock = 'DECAY',
                lhacode = [ 9000001 ])

WHP = Parameter(name = 'WHP',
                nature = 'external',
                type = 'real',
                value = 0.1,
                texname = '\\text{WHP}',
                lhablock = 'DECAY',
                lhacode = [ 9000002 ])

cb = Parameter(name = 'cb',
               nature = 'internal',
               type = 'real',
               value = '1/cmath.sqrt(1 + tanb**2)',
               texname = 'c_{\\beta }')

ccp1 = Parameter(name = 'ccp1',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.cos(a1)',
                 texname = 'c_{\\text{$\\alpha $1}}')

ccp2 = Parameter(name = 'ccp2',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.cos(a2)',
                 texname = 'c_{\\text{$\\alpha $2}}')

ccp3 = Parameter(name = 'ccp3',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.cos(a3)',
                 texname = 'c_{\\text{$\\alpha $3}}')

cn1 = Parameter(name = 'cn1',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(theta1N)',
                texname = 'c_{\\text{$\\theta $1}}')

cn2 = Parameter(name = 'cn2',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(theta2N)',
                texname = 'c_{\\text{$\\theta $2}}')

cn3 = Parameter(name = 'cn3',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(theta3N)',
                texname = 'c_{\\text{$\\theta $3}}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw**2)',
               texname = 'c_w')

Reta1x2 = Parameter(name = 'Reta1x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{Reta1x2}')

sb = Parameter(name = 'sb',
               nature = 'internal',
               type = 'real',
               value = 'tanb/cmath.sqrt(1 + tanb**2)',
               texname = 's_{\\beta }')

scp1 = Parameter(name = 'scp1',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sin(a1)',
                 texname = 's_{\\text{$\\alpha $1}}')

scp2 = Parameter(name = 'scp2',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sin(a2)',
                 texname = 's_{\\text{$\\alpha $2}}')

scp3 = Parameter(name = 'scp3',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sin(a3)',
                 texname = 's_{\\text{$\\alpha $3}}')

sn1 = Parameter(name = 'sn1',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sin(theta1N)',
                texname = 's_{\\text{$\\theta $1}}')

sn2 = Parameter(name = 'sn2',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sin(theta2N)',
                texname = 's_{\\text{$\\theta $2}}')

sn3 = Parameter(name = 'sn3',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sin(theta3N)',
                texname = 's_{\\text{$\\theta $3}}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

Rcp1x1 = Parameter(name = 'Rcp1x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'ccp1*ccp2',
                   texname = '\\text{Rcp1x1}')

Rcp1x2 = Parameter(name = 'Rcp1x2',
                   nature = 'internal',
                   type = 'real',
                   value = 'ccp2*scp1',
                   texname = '\\text{Rcp1x2}')

Rcp1x3 = Parameter(name = 'Rcp1x3',
                   nature = 'internal',
                   type = 'real',
                   value = 'scp2',
                   texname = '\\text{Rcp1x3}')

Rcp2x1 = Parameter(name = 'Rcp2x1',
                   nature = 'internal',
                   type = 'real',
                   value = '-(ccp3*scp1) - ccp1*scp2*scp3',
                   texname = '\\text{Rcp2x1}')

Rcp2x2 = Parameter(name = 'Rcp2x2',
                   nature = 'internal',
                   type = 'real',
                   value = 'ccp1*ccp3 - scp1*scp2*scp3',
                   texname = '\\text{Rcp2x2}')

Rcp2x3 = Parameter(name = 'Rcp2x3',
                   nature = 'internal',
                   type = 'real',
                   value = 'ccp2*scp3',
                   texname = '\\text{Rcp2x3}')

Rcp3x1 = Parameter(name = 'Rcp3x1',
                   nature = 'internal',
                   type = 'real',
                   value = '-(ccp1*ccp3*scp2) + scp1*scp3',
                   texname = '\\text{Rcp3x1}')

Rcp3x2 = Parameter(name = 'Rcp3x2',
                   nature = 'internal',
                   type = 'real',
                   value = '-(ccp3*scp1*scp2) - ccp1*scp3',
                   texname = '\\text{Rcp3x2}')

Rcp3x3 = Parameter(name = 'Rcp3x3',
                   nature = 'internal',
                   type = 'real',
                   value = 'ccp2*ccp3',
                   texname = '\\text{Rcp3x3}')

sx = Parameter(name = 'sx',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt((MW**2/cw**2 - MZ**2)/(-MZ**2 + MZP**2))',
               texname = 's_x')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

ynv1x1 = Parameter(name = 'ynv1x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'cn1*Mnh1',
                   texname = '\\text{ynv1x1}')

ynv2x2 = Parameter(name = 'ynv2x2',
                   nature = 'internal',
                   type = 'real',
                   value = 'cn2*Mnh2',
                   texname = '\\text{ynv2x2}')

ynv3x3 = Parameter(name = 'ynv3x3',
                   nature = 'internal',
                   type = 'real',
                   value = 'cn3*Mnh3',
                   texname = '\\text{ynv3x3}')

cx = Parameter(name = 'cx',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sx**2)',
               texname = 'c_x')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = 'v')

AH1 = Parameter(name = 'AH1',
                nature = 'internal',
                type = 'real',
                value = '(47*ee**2*(1 - (2*Mh**4)/(987.*MT**4) - (14*Mh**2)/(705.*MT**2) + (213*Mh**12)/(2.634632e7*MW**12) + (5*Mh**10)/(119756.*MW**10) + (41*Mh**8)/(180950.*MW**8) + (87*Mh**6)/(65800.*MW**6) + (57*Mh**4)/(6580.*MW**4) + (33*Mh**2)/(470.*MW**2)))/(72.*cmath.pi**2*sb*vev)',
                texname = 'A_{\\text{H1}}')

AH2 = Parameter(name = 'AH2',
                nature = 'internal',
                type = 'real',
                value = '(47*ee**2*(1 - (2*Mhh**4)/(987.*MT**4) - (14*Mhh**2)/(705.*MT**2) + (213*Mhh**12)/(2.634632e7*MW**12) + (5*Mhh**10)/(119756.*MW**10) + (41*Mhh**8)/(180950.*MW**8) + (87*Mhh**6)/(65800.*MW**6) + (57*Mhh**4)/(6580.*MW**4) + (33*Mhh**2)/(470.*MW**2)))/(72.*cb*cmath.pi**2*vev)',
                texname = 'A_{\\text{H2}}')

GH1 = Parameter(name = 'GH1',
                nature = 'internal',
                type = 'real',
                value = '-0.08333333333333333*(G**2*(1 + (13*Mh**6)/(16800.*MT**6) + Mh**4/(168.*MT**4) + (7*Mh**2)/(120.*MT**2)))/(cmath.pi**2*sb*vev)',
                texname = 'G_{\\text{H1}}')

GH2 = Parameter(name = 'GH2',
                nature = 'internal',
                type = 'real',
                value = '-0.08333333333333333*(G**2*(1 + (13*Mhh**6)/(16800.*MT**6) + Mhh**4/(168.*MT**4) + (7*Mhh**2)/(120.*MT**2)))/(cb*cmath.pi**2*vev)',
                texname = 'G_{\\text{H2}}')

gp = Parameter(name = 'gp',
               nature = 'internal',
               type = 'real',
               value = '(gw*cmath.sqrt((MW**2/cw**2 - MZ**2)*(-(MW**2/cw**2) + MZP**2)))/(2.*cb**2*cw**2*MW**2)',
               texname = 'g_p')

vevs = Parameter(name = 'vevs',
                 nature = 'internal',
                 type = 'real',
                 value = 'cmath.sqrt((cb**2*(MZ**2*MZP**2 + ((1 - cb**2)*MW**2*(MW**2/cw**2 - MZ**2 - MZP**2))/cw**2)*vev**2)/((MW**2/cw**2 - MZ**2)*(-(MW**2/cw**2) + MZP**2)))',
                 texname = 'v_s')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/(sb*vev)',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/(sb*vev)',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/(sb*vev)',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/(sb*vev)',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/(sb*vev)',
               texname = '\\text{ym}')

yneu1x1 = Parameter(name = 'yneu1x1',
                    nature = 'internal',
                    type = 'real',
                    value = '(Mnh1*sn1*cmath.sqrt(2))/(cb*vev)',
                    texname = '\\text{yneu1x1}')

yneu2x2 = Parameter(name = 'yneu2x2',
                    nature = 'internal',
                    type = 'real',
                    value = '(Mnh2*sn2*cmath.sqrt(2))/(cb*vev)',
                    texname = '\\text{yneu2x2}')

yneu3x3 = Parameter(name = 'yneu3x3',
                    nature = 'internal',
                    type = 'real',
                    value = '(Mnh3*sn3*cmath.sqrt(2))/(cb*vev)',
                    texname = '\\text{yneu3x3}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/(sb*vev)',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/(sb*vev)',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/(sb*vev)',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/(sb*vev)',
                texname = '\\text{yup}')

Reta1x1 = Parameter(name = 'Reta1x1',
                    nature = 'internal',
                    type = 'real',
                    value = '(cb*vev)/cmath.sqrt(cb**2*vev**2 + vevs**2)',
                    texname = '\\text{Reta1x1}')

Reta1x3 = Parameter(name = 'Reta1x3',
                    nature = 'internal',
                    type = 'real',
                    value = 'vevs/cmath.sqrt(cb**2*vev**2 + vevs**2)',
                    texname = '\\text{Reta1x3}')

Reta2x1 = Parameter(name = 'Reta2x1',
                    nature = 'internal',
                    type = 'real',
                    value = '(cb*vevs**2)/(cmath.sqrt(cb**2*vev**2 + vevs**2)*cmath.sqrt(cb**2*sb**2*vev**2 + vevs**2))',
                    texname = '\\text{Reta2x1}')

Reta2x2 = Parameter(name = 'Reta2x2',
                    nature = 'internal',
                    type = 'real',
                    value = 'cmath.sqrt(cb**2*sb**2*vev**2 + sb**2*vevs**2)/cmath.sqrt(cb**2*sb**2*vev**2 + vevs**2)',
                    texname = '\\text{Reta2x2}')

Reta2x3 = Parameter(name = 'Reta2x3',
                    nature = 'internal',
                    type = 'real',
                    value = '-((cb**2*vev*vevs)/(cmath.sqrt(cb**2*vev**2 + vevs**2)*cmath.sqrt(cb**2*sb**2*vev**2 + vevs**2)))',
                    texname = '\\text{Reta2x3}')

Reta3x1 = Parameter(name = 'Reta3x1',
                    nature = 'internal',
                    type = 'real',
                    value = '-((sb*vevs)/cmath.sqrt(cb**2*sb**2*vev**2 + vevs**2))',
                    texname = '\\text{Reta3x1}')

Reta3x2 = Parameter(name = 'Reta3x2',
                    nature = 'internal',
                    type = 'real',
                    value = '(cb*vevs)/cmath.sqrt(cb**2*sb**2*vev**2 + vevs**2)',
                    texname = '\\text{Reta3x2}')

Reta3x3 = Parameter(name = 'Reta3x3',
                    nature = 'internal',
                    type = 'real',
                    value = '(cb*sb*vev)/cmath.sqrt(cb**2*sb**2*vev**2 + vevs**2)',
                    texname = '\\text{Reta3x3}')

AH3 = Parameter(name = 'AH3',
                nature = 'internal',
                type = 'real',
                value = '(47*ee**2*(1 - (2*Mhs**4)/(987.*MT**4) - (14*Mhs**2)/(705.*MT**2) + (213*Mhs**12)/(2.634632e7*MW**12) + (5*Mhs**10)/(119756.*MW**10) + (41*Mhs**8)/(180950.*MW**8) + (87*Mhs**6)/(65800.*MW**6) + (57*Mhs**4)/(6580.*MW**4) + (33*Mhs**2)/(470.*MW**2)))/(72.*cmath.pi**2*vevs)',
                texname = 'A_{\\text{H3}}')

GH3 = Parameter(name = 'GH3',
                nature = 'internal',
                type = 'real',
                value = '-0.08333333333333333*(G**2*(1 + (13*Mhs**6)/(16800.*MT**6) + Mhs**4/(168.*MT**4) + (7*Mhs**2)/(120.*MT**2)))/(cmath.pi**2*vevs)',
                texname = 'G_{\\text{H3}}')

lam1 = Parameter(name = 'lam1',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mhh**2*Rcp1x1**2 + Mh**2*Rcp2x1**2 + Mhs**2*Rcp3x1**2 + (MA0**2*vevs**2)/(cb**2*vev**2 + vevs**2/sb**2))/(cb**2*vev**2)',
                 texname = '\\lambda _1')

lam1s = Parameter(name = 'lam1s',
                  nature = 'internal',
                  type = 'real',
                  value = '(Mhh**2*Rcp1x1*Rcp1x3 + Mh**2*Rcp2x1*Rcp2x3 + Mhs**2*Rcp3x1*Rcp3x3)/(cb*vev*vevs) - (MA0**2*sb**2)/(cb**2*sb**2*vev**2 + vevs**2)',
                  texname = '\\lambda _s')

lam2 = Parameter(name = 'lam2',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mhh**2*Rcp1x2**2 + Mh**2*Rcp2x2**2 + Mhs**2*Rcp3x2**2 + (MA0**2*vevs**2)/(sb**2*vev**2 + vevs**2/cb**2))/(sb**2*vev**2)',
                 texname = '\\lambda _2')

lam2s = Parameter(name = 'lam2s',
                  nature = 'internal',
                  type = 'real',
                  value = '(Mhh**2*Rcp1x2*Rcp1x3 + Mh**2*Rcp2x2*Rcp2x3 + Mhs**2*Rcp3x2*Rcp3x3)/(sb*vev*vevs) - (cb**2*MA0**2)/(cb**2*sb**2*vev**2 + vevs**2)',
                  texname = '\\lambda _{2 s}')

lama = Parameter(name = 'lama',
                 nature = 'internal',
                 type = 'real',
                 value = '-((cb*MA0**2*sb*vevs*cmath.sqrt(2))/(cb**2*sb**2*vev**2 + vevs**2))',
                 texname = '\\lambda _a')

lamd = Parameter(name = 'lamd',
                 nature = 'internal',
                 type = 'real',
                 value = '(-2*MHP**2 + (Mhh**2*Rcp1x1*Rcp1x2 + Mh**2*Rcp2x1*Rcp2x2 + Mhs**2*Rcp3x1*Rcp3x2)/(cb*sb))/vev**2 + MA0**2*(vev**(-2) - (cb**2*sb**2)/(cb**2*sb**2*vev**2 + vevs**2))',
                 texname = '\\lambda _d')

lamm = Parameter(name = 'lamm',
                 nature = 'internal',
                 type = 'real',
                 value = '(2*(MHP**2 - (MA0**2*vevs**2)/(cb**2*sb**2*vev**2 + vevs**2)))/vev**2',
                 texname = '\\lambda _m')

lams = Parameter(name = 'lams',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mhh**2*Rcp1x3**2 + Mh**2*Rcp2x3**2 + Mhs**2*Rcp3x3**2 + (cb**2*MA0**2*sb**2*vev**2)/(cb**2*sb**2*vev**2 + vevs**2))/vevs**2',
                 texname = '\\lambda _s')

yns = Parameter(name = 'yns',
                nature = 'internal',
                type = 'real',
                value = '(Mcsi*cmath.sqrt(2))/vevs',
                texname = 'Y^s')

mu1 = Parameter(name = 'mu1',
                nature = 'internal',
                type = 'real',
                value = '(cb**2*lam1*vev**2)/2. + ((lamd + lamm)*sb**2*vev**2)/2. + (lam1s*vevs**2)/2. + (lama*tanb*vevs)/cmath.sqrt(2)',
                texname = '\\mu _1')

mu2 = Parameter(name = 'mu2',
                nature = 'internal',
                type = 'real',
                value = '(cb**2*(lamd + lamm)*vev**2)/2. + (lam2*sb**2*vev**2)/2. + (lam2s*vevs**2)/2. + (lama*vevs)/(tanb*cmath.sqrt(2))',
                texname = '\\mu _2')

mus = Parameter(name = 'mus',
                nature = 'internal',
                type = 'real',
                value = '(cb**2*lam1s*vev**2)/2. + (lam2s*sb**2*vev**2)/2. + (lams*vevs**2)/2. + (cb*lama*sb*vev**2)/(vevs*cmath.sqrt(2))',
                texname = '\\mu _s')

