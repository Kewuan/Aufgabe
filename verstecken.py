#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 22:55:09 2018

@author: qk
"""

# verstecken.py
import random

def addLetter(astr,n=1):
    counter = 1
    while counter <= n:
        x = chr(random.randint(65,90))
        astr = astr + x
        counter += 1
    return(astr)

def verstecken(s,n=1):
    s = s.split()
    ls = []
    for i in s:
        i = i.upper()
        i = addLetter(i)
        ls.append(i)
    ls = ' '.join(ls)
    return ls

st = "Durch Verschlüsselung mittels eines Verschlüsselungsverfahrens und eines Schlüssels wird der Klartext in einen Geheimtext umgewandelt. Umgekehrt, wird aus einem Geheimtext durch Entschlüsselung der Klartext wieder zurückgewonnen." 

print(verstecken(st))