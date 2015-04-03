#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mortgage Loan Calculator"""
import decimal

NAME = raw_input('What is your Name?: ')
PRINCIPAL = int(raw_input('What is the Ammount of your Principal?: '))
YEARS = int(raw_input('For how many years is Loan borrowed?: '))
PREQUALIFIED = raw_input('Are you Pre-qualified?: ').lower()
PREAPROVED = ('yes')
RATE = None
TOTAL = None


if 0 <= PRINCIPAL <= 199999:
    if 1 <= YEARS <= 15:
        if PREQUALIFIED == PREAPROVED[0][:1]:
            RATE = float('0.0363')
        else:
            RATE = float('0.0465')
    elif 16 <= YEARS <= 20:
        if PREQUALIFIED == PREAPROVED[0][:1]:
            RATE = float('0.0404')
        else:
            RATE = float('0.0498')
    elif 21 <= YEARS <= 30:
        if PREQUALIFIED == PREAPROVED[0][:1]:
            RATE = float('0.0577')
        else:
            RATE = float('0.0639')
elif 200000 <= PRINCIPAL <= 999999:
    if 1 <= YEARS <= 15:
        if PREQUALIFIED == PREAPROVED[0][:1]:
            RATE = float('0.0302')
        else:
            RATE = float('0.0398')
    elif 16 <= YEARS <= 20:
        if PREQUALIFIED == PREAPROVED[0][:1]:
            RATE = float('0.0327')
        else:
            RATE = float('0.0408')
    elif 21 <= YEARS <= 30:
        if PREQUALIFIED == PREAPROVED[0][:1]:
            RATE = float('0.0466')
elif PRINCIPAL >= 1000000:
    if  1 <= YEARS <= 15:
        if PREQUALIFIED == PREAPROVED[0][:1]:
            RATE = float('0.0205')
    elif 16 <= YEARS <= 20:
        if PREQUALIFIED == PREAPROVED[0][:1]:
            RATE = float('0.0262')


if RATE != None:
    AMMOUNT = PRINCIPAL * ((1 + decimal.Decimal(RATE) / 12) ** (12 * YEARS))
    TOTAL = int(round(AMMOUNT))
    if PREQUALIFIED == PREAPROVED:
        PREQUALIFIED = 'Yes'
    else:
        PREQUALIFIED = 'No'
REPORT = """    Loan Report for: {}
--------------------------------------------------------------------------------
                Principal: ${}
                Duration: {} Years
                Prequalified:{}
                Total: ${}
         """.format(NAME, PRINCIPAL, YEARS, PREQUALIFIED, TOTAL)
print REPORT
