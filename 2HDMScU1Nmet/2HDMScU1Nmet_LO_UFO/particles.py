# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Linux x86 (64-bit) (July 16, 2024)
# Date: Thu 9 Jan 2025 17:47:22


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1,
                     LeptonNumber = 0,
                     X = 0,
                     Y = 0)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

Zp = Particle(pdg_code = 9000023,
              name = 'Zp',
              antiname = 'Zp',
              spin = 3,
              color = 1,
              mass = Param.MZP,
              width = Param.WZP,
              texname = 'Zp',
              antitexname = 'Zp',
              charge = 0,
              LeptonNumber = 0,
              X = 0,
              Y = 0)

nle = Particle(pdg_code = 12,
               name = 'nle',
               antiname = 'nle~',
               spin = 2,
               color = 1,
               mass = Param.ZERO,
               width = Param.ZERO,
               texname = 'nle',
               antitexname = 'nle~',
               charge = 0,
               LeptonNumber = 1,
               X = 0,
               Y = 0)

nle__tilde__ = nle.anti()

nlmu = Particle(pdg_code = 14,
                name = 'nlmu',
                antiname = 'nlmu~',
                spin = 2,
                color = 1,
                mass = Param.ZERO,
                width = Param.ZERO,
                texname = 'nlmu',
                antitexname = 'nlmu~',
                charge = 0,
                LeptonNumber = 1,
                X = 0,
                Y = 0)

nlmu__tilde__ = nlmu.anti()

nlta = Particle(pdg_code = 16,
                name = 'nlta',
                antiname = 'nlta~',
                spin = 2,
                color = 1,
                mass = Param.ZERO,
                width = Param.ZERO,
                texname = 'nlta',
                antitexname = 'nlta~',
                charge = 0,
                LeptonNumber = 1,
                X = 0,
                Y = 0)

nlta__tilde__ = nlta.anti()

nh1 = Particle(pdg_code = 9000012,
               name = 'nh1',
               antiname = 'nh1~',
               spin = 2,
               color = 1,
               mass = Param.Mnh1,
               width = Param.Wnh1,
               texname = 'nh1',
               antitexname = 'nh1~',
               charge = 0,
               LeptonNumber = 1,
               X = 0,
               Y = 0)

nh1__tilde__ = nh1.anti()

nh2 = Particle(pdg_code = 9000014,
               name = 'nh2',
               antiname = 'nh2~',
               spin = 2,
               color = 1,
               mass = Param.Mnh2,
               width = Param.Wnh2,
               texname = 'nh2',
               antitexname = 'nh2~',
               charge = 0,
               LeptonNumber = 1,
               X = 0,
               Y = 0)

nh2__tilde__ = nh2.anti()

nh3 = Particle(pdg_code = 9000016,
               name = 'nh3',
               antiname = 'nh3~',
               spin = 2,
               color = 1,
               mass = Param.Mnh3,
               width = Param.Wnh3,
               texname = 'nh3',
               antitexname = 'nh3~',
               charge = 0,
               LeptonNumber = 1,
               X = 0,
               Y = 0)

nh3__tilde__ = nh3.anti()

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      LeptonNumber = 1,
                      X = 0,
                      Y = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       LeptonNumber = 1,
                       X = 0,
                       Y = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       LeptonNumber = 1,
                       X = 0,
                       Y = 0)

ta__plus__ = ta__minus__.anti()

u = Particle(pdg_code = 2,
             name = 'u',
             antiname = 'u~',
             spin = 2,
             color = 3,
             mass = Param.MU,
             width = Param.ZERO,
             texname = 'u',
             antitexname = 'u~',
             charge = 2/3,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

u__tilde__ = u.anti()

c = Particle(pdg_code = 4,
             name = 'c',
             antiname = 'c~',
             spin = 2,
             color = 3,
             mass = Param.MC,
             width = Param.ZERO,
             texname = 'c',
             antitexname = 'c~',
             charge = 2/3,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

c__tilde__ = c.anti()

t = Particle(pdg_code = 6,
             name = 't',
             antiname = 't~',
             spin = 2,
             color = 3,
             mass = Param.MT,
             width = Param.WT,
             texname = 't',
             antitexname = 't~',
             charge = 2/3,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

t__tilde__ = t.anti()

d = Particle(pdg_code = 1,
             name = 'd',
             antiname = 'd~',
             spin = 2,
             color = 3,
             mass = Param.MD,
             width = Param.ZERO,
             texname = 'd',
             antitexname = 'd~',
             charge = -1/3,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

d__tilde__ = d.anti()

s = Particle(pdg_code = 3,
             name = 's',
             antiname = 's~',
             spin = 2,
             color = 3,
             mass = Param.MS,
             width = Param.ZERO,
             texname = 's',
             antitexname = 's~',
             charge = -1/3,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

s__tilde__ = s.anti()

b = Particle(pdg_code = 5,
             name = 'b',
             antiname = 'b~',
             spin = 2,
             color = 3,
             mass = Param.MB,
             width = Param.ZERO,
             texname = 'b',
             antitexname = 'b~',
             charge = -1/3,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

b__tilde__ = b.anti()

csi = Particle(pdg_code = 9900012,
               name = 'csi',
               antiname = 'csi~',
               spin = 2,
               color = 1,
               mass = Param.Mcsi,
               width = Param.ZERO,
               texname = 'csi',
               antitexname = 'csi~',
               charge = 0,
               LeptonNumber = 0,
               X = 0,
               Y = 0)

csi__tilde__ = csi.anti()

hh = Particle(pdg_code = 9000026,
              name = 'hh',
              antiname = 'hh',
              spin = 1,
              color = 1,
              mass = Param.Mhh,
              width = Param.Whh,
              texname = 'hh',
              antitexname = 'hh',
              charge = 0,
              LeptonNumber = 0,
              X = 0,
              Y = 0)

h = Particle(pdg_code = 25,
             name = 'h',
             antiname = 'h',
             spin = 1,
             color = 1,
             mass = Param.Mh,
             width = Param.Wh,
             texname = 'h',
             antitexname = 'h',
             charge = 0,
             LeptonNumber = 0,
             X = 0,
             Y = 0)

hs = Particle(pdg_code = 9000027,
              name = 'hs',
              antiname = 'hs',
              spin = 1,
              color = 1,
              mass = Param.Mhs,
              width = Param.Whs,
              texname = 'hs',
              antitexname = 'hs',
              charge = 0,
              LeptonNumber = 0,
              X = 0,
              Y = 0)

G0 = Particle(pdg_code = 250,
              name = 'G0',
              antiname = 'G0',
              spin = 1,
              color = 1,
              mass = Param.MZ,
              width = Param.WZ,
              texname = 'G0',
              antitexname = 'G0',
              goldstone = True,
              charge = 0,
              LeptonNumber = 0,
              X = 0,
              Y = 0)

G0p = Particle(pdg_code = 9000028,
               name = 'G0p',
               antiname = 'G0p',
               spin = 1,
               color = 1,
               mass = Param.MZP,
               width = Param.WZP,
               texname = 'G0p',
               antitexname = 'G0p',
               goldstone = True,
               charge = 0,
               LeptonNumber = 0,
               X = 0,
               Y = 0)

A0 = Particle(pdg_code = 9000001,
              name = 'A0',
              antiname = 'A0',
              spin = 1,
              color = 1,
              mass = Param.MA0,
              width = Param.WA0,
              texname = 'A0',
              antitexname = 'A0',
              charge = 0,
              LeptonNumber = 0,
              X = 0,
              Y = 0)

G__plus__ = Particle(pdg_code = 251,
                     name = 'G+',
                     antiname = 'G-',
                     spin = 1,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'G+',
                     antitexname = 'G-',
                     goldstone = True,
                     charge = 1,
                     LeptonNumber = 0,
                     X = 0,
                     Y = 0)

G__minus__ = G__plus__.anti()

H__plus__ = Particle(pdg_code = 9000002,
                     name = 'H+',
                     antiname = 'H-',
                     spin = 1,
                     color = 1,
                     mass = Param.MHP,
                     width = Param.WHP,
                     texname = 'H+',
                     antitexname = 'H-',
                     charge = 1,
                     LeptonNumber = 0,
                     X = 0,
                     Y = 0)

H__minus__ = H__plus__.anti()

