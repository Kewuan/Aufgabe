#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 16:39:25 2018

@author: qk
"""

#wurzel()
def f(x,n = 10):
    if n == 1:
        return 1
    else:
        return 0.5*(f(x, n-1) + (x/f(x, n-1)))

print(f(2))