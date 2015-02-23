#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Alarm Clock"""


day= raw_input('What day is it?')
weekday = day =='sat' or day=='sun' or day=='Saturday' or day=='Sunday'
time= raw_input('What time is it, enter 4 digits format? ')
time= int(time)
display_time = time < '0600'

if weekday and display_time:
    snooze= True
else:
    snooze= False
if snooze is True:
    print ('Beep! Beep! Beep! Beep! Beep!')
