# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 03:11:46 2019

@author: Yunyung
"""

import numpy as np
#OR
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
