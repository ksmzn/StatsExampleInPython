#! /usr/bin/env python
#-*- encoding:utf-8 -*-
"""
    Rによるやさしい統計学
    第三章
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stats1 = np.array([6,10,6,10,5,3,5,9,3,3,11,6,11,9,7,5,8,7,7,9])
stats2 = np.array([10,13,8,15,8,6,9,10,7,3,18,14,18,11,12,5,7,12,7,7])

plt.plot(stats1,stats2,'r*')
#plt.show()

#共分散行列
cov1_2 = np.cov(stats1, stats2)
print cov1_2

#不偏共分散
cov1_2 = np.cov(stats1, stats2, bias=1)
print cov1_2

#相関係数
cor = np.corrcoef(stats1,stats2)
print cor

"""
Pythonで、Rのtable関数のような表示をするにはどうすればよいのだろう。
"""
