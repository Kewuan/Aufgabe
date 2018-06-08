#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#listenspeicherung.py

def save_list(liste, path):
    f = open(path, 'w')
    for item in liste:
        f.write(str(item))
        f.write('\n')
    f.close()

def load_list(path):
    als = []
    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.rstrip('\n')
            als.append(line)
    return als

test_list = ['this is a test list.','0000000011111111',
             123,456,789,
             1.23,4.56,7.89,
             False, True,
             None]

test_path = '/Users/qk/Documents/program/Python/Aufgabe/test_sp.txt'

save_list(test_list, test_path)
loadlist = load_list(test_path)
print(loadlist)
