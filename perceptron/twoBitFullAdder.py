# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 04:10:57 2019
implement double bit full adder
@author: Yunyung
"""
from fullAdder import fullAdder
def twoBitFullAdder(y1, y2, x1, x2, ci):  
    s1, c1 = fullAdder(x1, x2, ci)
    s2, co = fullAdder(y1, y2, c1)
    return co, s2, s1, co * 4 + s2 * 2 + s1        
    # return carryout,sum2, sum1, tranlate binary to Decimal for easy check(轉成十進位方便觀察結果)
print("two bit Full adder:")
print("     (y1,y2,x1,x2,ci)   (co,s2,s1,Decimal Value)")
print("input(0, 0, 0, 0, 0) -> " + str(twoBitFullAdder(0, 0, 0, 0, 0)))
print("input(0, 0, 0, 0, 1) -> " + str(twoBitFullAdder(0, 0, 0, 0, 1)))
print("input(0, 0, 0, 1, 0) -> " + str(twoBitFullAdder(0, 0, 0, 1, 0)))
print("input(0, 0, 0, 1, 1) -> " + str(twoBitFullAdder(0, 0, 0, 1, 1)))
print("input(0, 0, 1, 0, 0) -> " + str(twoBitFullAdder(0, 0, 1, 0, 0)))
print("input(0, 0, 1, 0, 1) -> " + str(twoBitFullAdder(0, 0, 1, 0, 1)))
print("input(0, 0, 1, 1, 0) -> " + str(twoBitFullAdder(0, 0, 1, 1, 0)))
print("input(0, 0, 1, 1, 1) -> " + str(twoBitFullAdder(0, 0, 1, 1, 1)))
print("input(0, 1, 0, 0, 0) -> " + str(twoBitFullAdder(0, 1, 0, 0, 0)))
print("input(0, 1, 0, 0, 1) -> " + str(twoBitFullAdder(0, 1, 0, 0, 1)))
print("input(0, 1, 0, 1, 0) -> " + str(twoBitFullAdder(0, 1, 0, 1, 0)))
print("input(0, 1, 0, 1, 1) -> " + str(twoBitFullAdder(0, 1, 0, 1, 1)))
print("input(0, 1, 1, 0, 0) -> " + str(twoBitFullAdder(0, 1, 1, 0, 0)))
print("input(0, 1, 1, 0, 1) -> " + str(twoBitFullAdder(0, 1, 1, 0, 1)))
print("input(0, 1, 1, 1, 0) -> " + str(twoBitFullAdder(0, 1, 1, 1, 0)))
print("input(0, 1, 1, 1, 1) -> " + str(twoBitFullAdder(0, 1, 1, 1, 1)))
print("input(1, 0, 0, 0, 0) -> " + str(twoBitFullAdder(1, 0, 0, 0, 0)))

print("input(1, 0, 0, 0, 1) -> " + str(twoBitFullAdder(1, 0, 0, 0, 1)))
print("input(1, 0, 0, 1, 0) -> " + str(twoBitFullAdder(1, 0, 0, 1, 0)))
print("input(1, 0, 0, 1, 1) -> " + str(twoBitFullAdder(1, 0, 0, 1, 1)))
print("input(1, 0, 1, 0, 0) -> " + str(twoBitFullAdder(1, 0, 1, 0, 0)))
print("input(1, 0, 1, 0, 1) -> " + str(twoBitFullAdder(1, 0, 1, 0, 1)))
print("input(1, 0, 1, 1, 0) -> " + str(twoBitFullAdder(1, 0, 1, 1, 0)))
print("input(1, 0, 1, 1, 1) -> " + str(twoBitFullAdder(1, 0, 1, 1, 1)))
print("input(1, 1, 0, 0, 0) -> " + str(twoBitFullAdder(1, 1, 0, 0, 0)))
print("input(1, 1, 0, 0, 1) -> " + str(twoBitFullAdder(1, 1, 0, 0, 1)))
print("input(1, 1, 0, 1, 0) -> " + str(twoBitFullAdder(1, 1, 0, 1, 0)))
print("input(1, 1, 0, 1, 1) -> " + str(twoBitFullAdder(1, 1, 0, 1, 1)))
print("input(1, 1, 1, 0, 0) -> " + str(twoBitFullAdder(1, 1, 1, 0, 0)))
print("input(1, 1, 1, 0, 1) -> " + str(twoBitFullAdder(1, 1, 1, 0, 1)))
print("input(1, 1, 1, 1, 0) -> " + str(twoBitFullAdder(1, 1, 1, 1, 0)))
print("input(1, 1, 1, 1, 1) -> " + str(twoBitFullAdder(1, 1, 1, 1, 1)))

    
    


