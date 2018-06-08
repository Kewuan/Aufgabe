#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

class FastaSeq():
    
    def __init__(self, header='>', sequence=''):
        self.header = header
        self.sequence = sequence
        
    def save(self, path):
        pickle.dump(self.header, open(path, 'wb'))
        pickle.dump(self.sequence, open(path, 'ab'))
    
    def load(self, path):
        daten = pickle.load(open(path, 'rb'))
    
    def alpha():
        pass
    
    #magical method
    def __len__(self):
        return(len(self.sequence))
        
    def __str__(self):
        return(self.header + '\n' +self.sequence)
        
    def __add__(self):
        return(FastaSeq(self.header))


class NucFastaSeq(FastaSeq):
    
    def translate():
        pass
    

class ProtFastaSeq(FastaSeq):
    pass

