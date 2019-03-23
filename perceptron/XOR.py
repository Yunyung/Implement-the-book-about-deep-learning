# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 03:11:46 2019

@author: Yunyung
"""
from OR import OR
from NAND import NAND
from AND import AND
def XOR(x1, x2):
    s1 = OR(x1, x2)
    s2 = NAND(x1, x2)
    y  = AND(s1, s2)
    if (y <= 0):
        return 0
    else:
        return 1
    
    