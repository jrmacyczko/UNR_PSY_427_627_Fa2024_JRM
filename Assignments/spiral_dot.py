# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:12:13 2024

@author: jrmac
"""
import numpy as np
from psychopy import visual, core
# %% (2) Make a spiral line plot.
theta = np.linspace(0,10*np.pi, 100)
r = np.linspace(5,150,100)
x = r*np.cos(theta)
y = r*np.sin(theta)

# Create a small screen window, 
win = visual.Window([400,400])

for i in range(len(x)):
    circ_pos = (x[i], y[i]) # Center of screen
    circ_stim = visual.Circle(win, radius=12,
                          units='pix',
                          fillColor=(1.0, 0.5, 0.0),
                          pos=circ_pos)
    circ_stim.draw()
    win.flip()
    core.wait(.01)

core.wait(1)
win.close()