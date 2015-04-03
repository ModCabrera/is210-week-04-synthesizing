#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""NEW PAINT COLOR SCHEME FOR ROOM IN HOME"""

BASE1 = 'Seattle Gray'
BASE2 = 'Manatee'
ACCENT_SAGE = 'Ceramic Glaze'
ACCENT_MANATEE = 'Platinum Mist'
BASEQ1 = 'Which accent color, "Ceramic Glaze" or "Cumulus Nimbus"?: '
HIGHLIGHTQ = 'Which Highlight color, "Basically White" or "White"?: '
HIGHLIGHTQ2 = 'Which Highlight color, "Off White" or "Paper White"?: '
ACCENTQ = 'Which accent color, "Platinum Mist", or "Spartan Sage"?: '
HIGHLIGHTQ3 = 'Which Highlight color, "Bone White" or "Just White"?: '
HIGHLIGHTQ4 = 'Which Highlight color, "Fractal White" or "Not White"?: '

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')


if BASE == BASE1:
    ACCENT = raw_input(BASEQ1)
    if ACCENT == ACCENT_SAGE:
        HIGHLIGHT = raw_input(HIGHLIGHTQ)
    else:
        HIGHLIGHT = raw_input(HIGHLIGHTQ2)
elif BASE == BASE2:
    ACCENT = raw_input(ACCENTQ)
    if ACCENT == ACCENT_MANATEE:
        HIGHLIGHT = raw_input(HIGHLIGHTQ3)
    else:
        HIGHLIGHT = raw_input(HIGHLIGHTQ4)

print 'Your selected colors are, {}, {},and {}'.format(BASE, ACCENT, HIGHLIGHT)
