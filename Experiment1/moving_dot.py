#%%Imports 
from psychopy import visual, core
import os
import matplotlib.pyplot as plt
import numpy as np

#%% Useful functions 
def cart_to_pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return theta, rho

def pol_to_cart(theta, rho):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y

# Define parameters
max_radius = 150
min_radius = 10
fps = 60
n_seconds = 5
n_revolutions = 20
n_steps = fps * n_seconds
rho = np.linspace(max_radius, min_radius, n_steps)
theta = np.linspace(0, np.pi * 2 * n_revolutions, n_steps)

#%% Set up screen

# Create a small screen window, 
screen_size = [400,400]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')

#%% 
#%% Draw dot

for frame in range(n_steps):
    circ_pos = pol_to_cart(theta[frame], rho[frame])
    circ_stim = visual.Circle(win, radius=12,
                              units='pix',
                              fillColor=(1.0, 0.0, 0.0),
                              pos=circ_pos)
    circ_stim.draw()
    win.flip()

core.wait(1)    
win.close()
