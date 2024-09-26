# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:27:48 2024

@author: jrmac
"""

# %% (1) Add functionality to the make_circle function we defined in the class demo
import matplotlib.pyplot as plt
import numpy as np
def cart_to_pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return theta, rho
def make_circle(size,radius):
    """This is a docstring! Provide useful information here.
    
    Parameters
    ----------
    size : scalar
        How large the circle image should be on one side.
    """

    t = np.linspace(-1, 1, size)
    x, y = np.meshgrid(t, t);
    theta, rho = cart_to_pol(x, y)
    circle_out = rho < radius;
    return circle_out

circ = make_circle(101,1)
plt.imshow(circ)
plt.show()

# %% (2) Make a spiral line plot.
theta = np.linspace(0,10*np.pi, 1000)
r = np.linspace(0,1,1000)
x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x,y)

# %% (3) Make a Gaussian blob image
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x,y)
d = np.sqrt(X*X + Y*Y)
mu = 0
sigma = 1
g = np.exp(-((d - mu)**2 / (2.0 * sigma**2)))
plt.imshow(g)
plt.show()