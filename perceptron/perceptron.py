# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 04:57:25 2019

@author: Yunyung
"""

import numpy as np
# AND gate
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
# NAND
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
# OR
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
# XOR
def XOR(x1, x2):
    s1 = OR(x1, x2)
    s2 = NAND(x1, x2)
    y  = AND(s1, s2)
    if (y <= 0):
        return 0
    else:
        return 1
    
# half Adder
def halfAdder(x1, x2):
    c = AND(x1, x2)
    s = XOR(x1, x2)
    return s, c # return sum carryout

# full Adder
def fullAdder(x1, x2, ci):  # input1, input2, carryIn
    s1, c1 = halfAdder(x1, x2)
    s,  c2 = halfAdder(s1, ci)
    co = OR(c1, c2)
    return s, co # return sum, carryout

# two bit full Adder
def twoBitFullAdder(y1, y2, x1, x2, ci):  
    s1, c1 = fullAdder(x1, x2, ci)
    s2, co = fullAdder(y1, y2, c1)
    return co, s2, s1        
    # return carryout,sum2, sum1, tranlate binary to Decimal for easy check(轉成十進位方便觀察結果)

def BinaryToDecimal(arr):
    return "          " + str(arr[0] * 4 + arr[1] * 2 + arr[2])

print("Half adder:")
print("               (s, c)")
print("input(0, 0) -> " + str(halfAdder(0, 0)))
print("input(0, 1) -> " + str(halfAdder(0, 1)))
print("input(1, 0) -> " + str(halfAdder(1, 0)))
print("input(1, 1) -> " + str(halfAdder(1, 1)))
print("--------------------------------------------------")


print("One bit Full adder:")
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


print("Two bit Full adder:")
print("     (y1,y2,x1,x2,ci)   (co,s2,s1) -> Decimal Value)")
print("input(0, 0, 0, 0, 0) -> " + str(twoBitFullAdder(0, 0, 0, 0, 0)) + BinaryToDecimal(twoBitFullAdder(0, 0, 0, 0, 0)) )
print("input(0, 0, 0, 0, 1) -> " + str(twoBitFullAdder(0, 0, 0, 0, 1)) + BinaryToDecimal(twoBitFullAdder(0, 0, 0, 0, 1)) )
print("input(0, 0, 0, 1, 0) -> " + str(twoBitFullAdder(0, 0, 0, 1, 0)) + BinaryToDecimal(twoBitFullAdder(0, 0, 0, 1, 0)) )
print("input(0, 0, 0, 1, 1) -> " + str(twoBitFullAdder(0, 0, 0, 1, 1)) + BinaryToDecimal(twoBitFullAdder(0, 0, 0, 1, 1)) )
print("input(0, 0, 1, 0, 0) -> " + str(twoBitFullAdder(0, 0, 1, 0, 0)) + BinaryToDecimal(twoBitFullAdder(0, 0, 1, 0, 0)) )
print("input(0, 0, 1, 0, 1) -> " + str(twoBitFullAdder(0, 0, 1, 0, 1)) + BinaryToDecimal(twoBitFullAdder(0, 0, 1, 0, 1)) )
print("input(0, 0, 1, 1, 0) -> " + str(twoBitFullAdder(0, 0, 1, 1, 0)) + BinaryToDecimal(twoBitFullAdder(0, 0, 1, 1, 0)) )
print("input(0, 0, 1, 1, 1) -> " + str(twoBitFullAdder(0, 0, 1, 1, 1)) + BinaryToDecimal(twoBitFullAdder(0, 0, 1, 1, 1)) )
print("input(0, 1, 0, 0, 0) -> " + str(twoBitFullAdder(0, 1, 0, 0, 0)) + BinaryToDecimal(twoBitFullAdder(0, 1, 0, 0, 0)) )
print("input(0, 1, 0, 0, 1) -> " + str(twoBitFullAdder(0, 1, 0, 0, 1)) + BinaryToDecimal(twoBitFullAdder(0, 1, 0, 0, 1)) )
print("input(0, 1, 0, 1, 0) -> " + str(twoBitFullAdder(0, 1, 0, 1, 0)) + BinaryToDecimal(twoBitFullAdder(0, 1, 0, 1, 0)) )
print("input(0, 1, 0, 1, 1) -> " + str(twoBitFullAdder(0, 1, 0, 1, 1)) + BinaryToDecimal(twoBitFullAdder(0, 1, 0, 1, 1)) )
print("input(0, 1, 1, 0, 0) -> " + str(twoBitFullAdder(0, 1, 1, 0, 0)) + BinaryToDecimal(twoBitFullAdder(0, 1, 1, 0, 0)) )
print("input(0, 1, 1, 0, 1) -> " + str(twoBitFullAdder(0, 1, 1, 0, 1)) + BinaryToDecimal(twoBitFullAdder(0, 1, 1, 0, 1)) )
print("input(0, 1, 1, 1, 0) -> " + str(twoBitFullAdder(0, 1, 1, 1, 0)) + BinaryToDecimal(twoBitFullAdder(0, 1, 1, 1, 0)) )
print("input(0, 1, 1, 1, 1) -> " + str(twoBitFullAdder(0, 1, 1, 1, 1)) + BinaryToDecimal(twoBitFullAdder(0, 1, 1, 1, 1)) )
print("input(1, 0, 0, 0, 0) -> " + str(twoBitFullAdder(1, 0, 0, 0, 0)) + BinaryToDecimal(twoBitFullAdder(1, 0, 0, 0, 0)) )
print("input(1, 0, 0, 0, 1) -> " + str(twoBitFullAdder(1, 0, 0, 0, 1)) + BinaryToDecimal(twoBitFullAdder(1, 0, 0, 0, 1)) )
print("input(1, 0, 0, 1, 0) -> " + str(twoBitFullAdder(1, 0, 0, 1, 0)) + BinaryToDecimal(twoBitFullAdder(1, 0, 0, 1, 0)) )
print("input(1, 0, 0, 1, 1) -> " + str(twoBitFullAdder(1, 0, 0, 1, 1)) + BinaryToDecimal(twoBitFullAdder(1, 0, 0, 1, 1)) )
print("input(1, 0, 1, 0, 0) -> " + str(twoBitFullAdder(1, 0, 1, 0, 0)) + BinaryToDecimal(twoBitFullAdder(1, 0, 1, 0, 0)) )
print("input(1, 0, 1, 0, 1) -> " + str(twoBitFullAdder(1, 0, 1, 0, 1)) + BinaryToDecimal(twoBitFullAdder(1, 0, 1, 0, 1)) )
print("input(1, 0, 1, 1, 0) -> " + str(twoBitFullAdder(1, 0, 1, 1, 0)) + BinaryToDecimal(twoBitFullAdder(1, 0, 1, 1, 0)) )
print("input(1, 0, 1, 1, 1) -> " + str(twoBitFullAdder(1, 0, 1, 1, 1)) + BinaryToDecimal(twoBitFullAdder(1, 0, 1, 1, 1)) )
print("input(1, 1, 0, 0, 0) -> " + str(twoBitFullAdder(1, 1, 0, 0, 0)) + BinaryToDecimal(twoBitFullAdder(1, 1, 0, 0, 0)) )
print("input(1, 1, 0, 0, 1) -> " + str(twoBitFullAdder(1, 1, 0, 0, 1)) + BinaryToDecimal(twoBitFullAdder(1, 1, 0, 0, 1)) )
print("input(1, 1, 0, 1, 0) -> " + str(twoBitFullAdder(1, 1, 0, 1, 0)) + BinaryToDecimal(twoBitFullAdder(1, 1, 0, 1, 0)) )
print("input(1, 1, 0, 1, 1) -> " + str(twoBitFullAdder(1, 1, 0, 1, 1)) + BinaryToDecimal(twoBitFullAdder(1, 1, 0, 1, 1)) )
print("input(1, 1, 1, 0, 0) -> " + str(twoBitFullAdder(1, 1, 1, 0, 0)) + BinaryToDecimal(twoBitFullAdder(1, 1, 1, 0, 0)) )
print("input(1, 1, 1, 0, 1) -> " + str(twoBitFullAdder(1, 1, 1, 0, 1)) + BinaryToDecimal(twoBitFullAdder(1, 1, 1, 0, 1)) )
print("input(1, 1, 1, 1, 0) -> " + str(twoBitFullAdder(1, 1, 1, 1, 0)) + BinaryToDecimal(twoBitFullAdder(1, 1, 1, 1, 0)) )
print("input(1, 1, 1, 1, 1) -> " + str(twoBitFullAdder(1, 1, 1, 1, 1)) + BinaryToDecimal(twoBitFullAdder(1, 1, 1, 1, 1)) )
