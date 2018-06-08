#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:11:23 2018

@author: qk
"""

#dna.py

Sequenzen = ('AT','TA','GC','CG',)

def dna():
    for a in Sequenzen:
        for b in Sequenzen:
            for c in Sequenzen:
                for d in Sequenzen:
                    for e in Sequenzen:
                        print(a,b,c,d,e)

dna()