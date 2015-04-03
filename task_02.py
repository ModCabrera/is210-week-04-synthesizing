#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module is an Alarm Clock"""

DAY = raw_input('What day is it?: ').strip().lower()[:3]
TIME = int(raw_input('What time is it?: '))
DAYS = ['Saturday', 'Sunday']

SNOOZE = (DAY == 'sun' or DAY == 'sun' or TIME < 600)

if SNOOZE:
    pass
else:
    print 'Beep!'* 5
