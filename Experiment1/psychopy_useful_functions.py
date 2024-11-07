#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:54:31 2024

@author: mark
"""
#%%Imports 
from psychopy import visual, core
import os
import matplotlib.pyplot as plt

#%% Set up screen

# Create a small screen window, 
screen_size = [400,400]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')


#%% Draw text
message = visual.TextStim(win, text='hello world!')
# Drawtrext
message.draw()
win.flip()
core.wait(1.0)


#%% Draw dot
screen_size = [400,400]
circ_pos = (0, 0) # Center of screen
print(circ_pos)
circ_stim = visual.Circle(win, radius=12,
                          units='pix',
                          fillColor=(1.0, 0.5, 0.0),
                          pos=circ_pos)
circ_stim.draw()
win.flip()

#%% Draw image
image_dir = '/Users/mark/Teaching/PSY427_627/datasets/fLoc_stimuli/';
image_file = os.path.join(face_images, 'instrument-85.jpg')
img = visual.ImageStim(win, image=image_file, units='pix', size=(300,300))
img.draw()
win.flip()

#%% Close screen
win.close()

