#! /usr/bin/env python
#-*- encoding:utf-8 -*-
"""
    Rによるやさしい統計学
    第二章
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("p38.csv")
print data["心理学テスト"].hist()
#plt.show()

testa = np.array([10,13,8,15,8])
print np.sum(testa)
#print testa.sum()
print np.mean(testa)
#print testa.mean()
print np.median(testa)
print np.var(testa)
print np.std(testa)
print np.max(testa)
print np.min(testa)

psy_test = np.array([13,14,7,12,10,6,8,15,4,14,9,6,10,12,5,12,8,8,12,15])
psy_mean = np.mean(psy_test)
psy_std = math.sqrt(np.mean((psy_test - psy_mean)**2))
psy_z = (psy_test - psy_mean) / psy_std
psy_z_mean = np.mean(psy_z)
psy_z_std = math.sqrt(np.mean((psy_z - psy_z_mean)**2))
psy_dev = 10 * psy_z + 50

psy_dev_mean = np.mean(psy_dev)
psy_dev_std = math.sqrt(np.mean((psy_dev - psy_dev_mean)**2))

print psy_dev_mean
print psy_dev_std
