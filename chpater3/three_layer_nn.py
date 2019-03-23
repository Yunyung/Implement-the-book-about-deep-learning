# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:33:32 2019

@author: Yunyung
"""
import numpy as np
import sys
sys.path.insert(0, r'C:\Users\Yunyung\Dropbox\機器學習\code\common')
from functions import identity_function, sigmoid

def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network
    
def forword(network, Input):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(Input, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    Output = identity_function(a3)
    
    return Output



network = init_network()
Input = np.array([1.0, 0.5])
Output = forword(network, Input) 
print(Output)