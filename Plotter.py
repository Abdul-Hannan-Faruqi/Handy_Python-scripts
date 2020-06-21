# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 ‏‎21:15:42 2020

@author: Abdul Hannan
"""

import numpy as np
from math import *
import matplotlib.pyplot as plt

def Plot(f, l, u):
    f = "y[i] = " + f
    le = u-l+1
    xdata = np.arange(l, u, le/1000)
    y = np.ndarray(len(xdata))
    i = 0
    for x in xdata:
        exec(f)
        i = i+1
    plt.plot(xdata, y)
    plt.show()

if __name__ == "__main__":
    print("Plot a function f(x) from x = i to x = f")
    f = input("f(x) = ")
    l = float(input("i = "))
    u = float(input("f = "))
    Plot(f, l, u)