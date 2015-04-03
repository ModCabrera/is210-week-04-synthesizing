#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""NEW PAINT COLOR SCHEME FOR ROOM IN HOME"""

BASE1 = 'Seattle Gray'
BASE2 = 'Manatee'
ACCENT_SAGE = 'Ceramic Glaze'
ACCENT_MANATEE = 'Platinum Mist'



BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')


if BASE == BASE1:
    ACCENT = raw_input('Which accent color, "Ceramic Glaze" or "Cumulus Nimbus"?: ')
    if ACCENT == ACCENT_SAGE:
        HIGHLIGHT = raw_input('Which Highlight color, "Basically White" or "White"?: ')
    else:
        HIGHLIGHT = raw_input('Which Highlight color, "Off White" or "Paper White"?: ')
elif BASE == BASE2:
    ACCENT = raw_input('Which accent color, "Platinum Mist", or "Spartan Sage"?: ')
    if ACCENT == ACCENT_MANATEE:
        HIGHLIGHT = raw_input('Which Highlight color, "Bone White" or "Just White"?: ')
    else:
        HIGHLIGHT = raw_input('Which Highlight color, "Fractal White" or "Not White"?: ')

print 'Your selected colors are, {}, {},and {}'.format(BASE, ACCENT, HIGHLIGHT)
