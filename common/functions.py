# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:59:35 2019

@author: Yunyung
"""

import numpy as np

def identity_function(x):
    return x

def step_function(x):
    return np.array(x > 0, dtype = np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)