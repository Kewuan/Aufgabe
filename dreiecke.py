#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Dreiecke.py

def dreiecke(n=20):
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                if a**2 + b**2 == c**2:
                    yield(a,b,c)

result = dreiecke()
next(result)