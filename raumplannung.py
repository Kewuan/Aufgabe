#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Raumplanung.py

kante12 = frozenset(('v1','v2'))
kante23 = frozenset(('v2','v3'))
kante24 = frozenset(('v2','v4'))
kante34 = frozenset(('v3','v4'))
kante45 = frozenset(('v4','v5'))
kante56 = frozenset(('v5','v6'))
kante57 = frozenset(('v5','v7'))
kante67 = frozenset(('v6','v7'))

e = {kante12, kante23, kante24, kante34,
        kante45, kante56, kante57, kante67}
#e:= die Kantenmenge, das Kanten(frozenset) enthält

v = {'v1','v2','v3','v4','v5','v6','v7'}
#v:= die Knotenmenge, das Zahlen enthält

g = (e,v)

