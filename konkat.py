#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 15:11:51 2018

@author: qk
"""

#konkat.py

def konkat(*strs):
    """
    it will return the argument, that not string
    """
    result = []
    for st in strs:
        if not isinstance(st, str):
            result.append(st)
    return result

print(konkat(12,4,'er','df','cd',('d','f')))
