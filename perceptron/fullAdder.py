# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 03:43:49 2019

@author: Yunyung
"""

from halfAdder import halfAdder
from OR import OR
def fullAdder(x1, x2, ci):  #input1, input2, carryIn
    s1, c1 = halfAdder(x1, x2)
    s,  c2 = halfAdder(s1, ci)
    co = OR(c1, c2)
    return s, co # return sum, carryout
print("one bit Full adder:")
print("     (x1,x2,c)    (s, c)")
print("input(0, 0, 0) -> " + str(fullAdder(0, 0, 0)))
print("input(0, 0, 1) -> " + str(fullAdder(0, 0, 1)))
print("input(0, 1, 0) -> " + str(fullAdder(0, 1, 0)))
print("input(0, 1, 1) -> " + str(fullAdder(0, 1, 1)))
print("input(1, 0, 0) -> " + str(fullAdder(1, 0, 0)))
print("input(1, 0, 1) -> " + str(fullAdder(1, 0, 1)))
print("input(1, 1, 0) -> " + str(fullAdder(1, 1, 0)))
print("input(1, 1, 1) -> " + str(fullAdder(1, 1, 1)))
print("--------------------------------------------------")
