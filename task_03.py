#!usr/bin/env/ python
# -*- coding: utf-8 -*-
"""Compounding Interest Calculator"""


NAME_1= raw_input('What is your name?')

P_AMMNT = raw_input('What is the ammount of your principal? ')
P_AMMNT= int(Ammount)
PR_P= P_AMMNT <= 199999
PR_N=(2000000 <= P_AMMNT <= 999999)
PR_L= (P_AMMNT >= 1000000)
DUR_TN= raw_input('for how many years is this loan being borrowed? ')
DUR_TN = int(DUR_TN)
DUR_R = (DUR_TN <= 15)
DUR_N = (16 <= DUR_TN <= 20)
DUR_T = (21 <= DUR_TN <= 30)
PREQUAL= raw_input('Are you pre=qualified for this loan? ')
PREQL= PREQUAL == 'YES' or PREQUAL == 'Y'
PRECUAL = PREQUAL == 'NO' or 'N'
