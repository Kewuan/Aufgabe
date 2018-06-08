#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:12:23 2018

@author: qk
"""

#schaltjahr.py

def schaltjahr(jahr):
        jahr = eval(jahr)
        if (jahr % 4 == 0) and (jahr % 100 != 0):
                print("{} is a leapyear".format(jahr))
        elif (jahr % 400 == 0):
                print("{} is a leapyear".format(jahr))
        else:
                print("{} is not a leapyear".format(jahr))
                
year = input("give a year:>  ")

schaltjahr(year)
