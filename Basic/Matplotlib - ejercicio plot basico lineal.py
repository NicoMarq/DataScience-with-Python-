# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 15:17:02 2021

@author: Nico
"""

import matplotlib.pyplot as plt

fig1 = plt.figure()

ax = fig1.subplots()

x = [1,2,3,4,5]
y = x

ax.plot(x,y)

plt.show()

