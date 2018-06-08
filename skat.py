#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:06:42 2018

@author: qk
"""

# Skat.py

colors = ('Kreuz','Pik','Herz','Karo')
values = ('Ass','König','Dame','Bube','Zahn','Neun','Acht','Sieben')

def generieren_skat():
    for color in colors:
        for value in values:
            yield(color, value)
            
g = generieren_skat()

next(g)