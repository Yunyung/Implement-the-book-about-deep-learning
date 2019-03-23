# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 03:39:58 2019

@author: Yunyung
"""
from XOR import XOR
from AND import AND
def halfAdder(x1, x2):
    c = AND(x1, x2)
    s = XOR(x1, x2)
    return s, c # return sum carryout
print("Half adder:")
print("               (s, c)")
print("input(0, 0) -> " + str(halfAdder(0, 0)))
print("input(0, 1) -> " + str(halfAdder(0, 1)))
print("input(1, 0) -> " + str(halfAdder(1, 0)))
print("input(1, 1) -> " + str(halfAdder(1, 1)))
print("--------------------------------------------------")

    