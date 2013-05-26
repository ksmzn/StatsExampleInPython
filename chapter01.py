#! /usr/bin/env python
#-*- encoding:utf-8 -*-
"""
    Rによるやさしい統計学
    第一章
"""

import math
import numpy as np

print math.sqrt(16)
print 2**2
height = np.array([173,178,180,183,182,174,179,179,174,192,17000,14000,9000,50000,30000,12000,900,2100,1000,25000])
hawks = height.reshape(2,10).transpose()
print hawks

def varp(x):
    samplevar = np.var(x) * len(x) / (len(x) - 1)
    return samplevar

x = np.array([10,13,8,15,8])
# numpy.var()は標本分散
print np.var(x)
# 不偏分散
print varp(x)



