#!usr/env/bin/ python
# -*- code: utf-8 -*-
"""NEW PAINT COLOR SCHEME FOR ROOM IN HOME"""

BASE1= 'Seattle Gray'
BASE2= 'Manatee'
ACCENT_SG= 'Ceramic Glaze'
ACCENT_SG2= 'Cumulus Nimbus'
ACCENT_MN= 'Platinum Mist'
ACCENT_MN2= 'Spartan Sage'

BASE= raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')

if BASE == str(BASE1):
    ACCENT = raw_input('Which accent color, "Ceramic Glaze" or "Cumulus Nimbus"?: ')
else:
     ACCENT = raw_input('Which accent color, "Platinum Mist" or "Spartan Sage"?: ')

if ACCENT == str(ACCENT_MN2):
    HIGHLIGHT= raw_input('Which Highlight color, "Fractal White", or "Not White"')
elif ACCENT == str(ACCENT_SG2):
    HIGHLIGHT= raw_input('Which Highlight color, "Off-White", or "Paper White"')
elif ACCENT == str(ACCENT_SG):
    HIGHLIGHT= raw_input('Which Highlight color, "Basically White", or "White"')
else:
    HIGHLIGHT= raw_input('WHich Highlight color, "Bone White", or "Just White"')
print 'Your selected colors are {} {} {}.'.format( BASE, ACCENT, HIGHLIGHT)

