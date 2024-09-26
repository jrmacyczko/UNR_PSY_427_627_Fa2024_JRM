#%% Psychopy demo script 2
#from psychopy import sound

# %%
from psychopy import visual, core, event
import colorsys
import random

# Function to generate two hues within a specified distance
def generate_hues(distance):
    # Generate a random hue (0 to 1)
    hue = random.uniform(0, 1)
    # Generate a second hue within the specified distance in hue space
    hue2 = hue + random.uniform(-distance, distance)
    # Wrap around to stay within [0, 1]
    hue2 = hue2 % 1.0
    return hue, hue2

# Function to convert hue to RGB
def hue_to_rgb(hue):
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return r, g, b

# Function to display two squares within a specified distance, time on and off, and number of colors
def color_squares(dist1, dist2, on, off, number): #time):
    hue_distance = [random.uniform(dist1, dist2) for _ in range(number)]
    #number = ((time+off)/(on+off))
    for x in range(len(hue_distance)):
        hue1, hue2 = generate_hues(hue_distance[x])
        rgb1 = hue_to_rgb(hue1)
        rgb2 = hue_to_rgb(hue2)
        
        square1 = visual.Rect(win, width=0.5, height=0.5, fillColor=rgb1, lineColor=rgb1, pos=(-0.5, 0))
        square2 = visual.Rect(win, width=0.5, height=0.5, fillColor=rgb2, lineColor=rgb2, pos=(0.5, 0))
        
        square1.draw()
        square2.draw()
        win.flip()
        core.wait(on)
        win.color = (1, 1, 1)
        win.flip()
        core.wait(off)
# t = o*n + ((i*n)-i)
# n = (t+i)/(o+i)
# %%

on = 1
off = .25
number = 3
between = 3-off

# Create a window
win = visual.Window(size=(600, 600), color=(1, 1, 1), units='norm')

color_squares(0, .1, on, off, number)
core.wait(between)
color_squares(.1, .2, on, off, number)
core.wait(between)
color_squares(.4, .5, on, off, number)
# %% Wait for a key press to close
event.waitKeys()
win.close()
core.quit()
# %%
# hue_distance = [random.uniform(0, 0.1) for _ in range(3)]

# for x in range(len(hue_distance)):
#     hue1, hue2 = generate_hues(hue_distance[x])
#     rgb1 = hue_to_rgb(hue1)
#     rgb2 = hue_to_rgb(hue2)
    
#     square1 = visual.Rect(win, width=0.4, height=0.4, fillColor=rgb1, lineColor=rgb1, pos=(-0.5, 0))
#     square2 = visual.Rect(win, width=0.4, height=0.4, fillColor=rgb2, lineColor=rgb2, pos=(0.5, 0))
    
#     square1.draw()
#     square2.draw()
#     win.flip()
#     core.wait(1)
#     win.color = (1, 1, 1)
#     win.flip()
#     core.wait(.25)
    
# core.wait(3)
# # %%
# hue_distance = [random.uniform(0.1, 0.2) for _ in range(3)]

# for x in range(len(hue_distance)):
#     hue1, hue2 = generate_hues(hue_distance[x])
#     rgb1 = hue_to_rgb(hue1)
#     rgb2 = hue_to_rgb(hue2)
    
#     square1 = visual.Rect(win, width=0.4, height=0.4, fillColor=rgb1, lineColor=rgb1, pos=(-0.5, 0))
#     square2 = visual.Rect(win, width=0.4, height=0.4, fillColor=rgb2, lineColor=rgb2, pos=(0.5, 0))
    
#     square1.draw()
#     square2.draw()
#     win.flip()
#     core.wait(1)
#     win.color = (1, 1, 1)
#     win.flip()
#     core.wait(.25)
    
# core.wait(3)
# # %%
# hue_distance = [random.uniform(0.4, 0.5) for _ in range(3)]

# for x in range(len(hue_distance)):
#     hue1, hue2 = generate_hues(hue_distance[x])
#     rgb1 = hue_to_rgb(hue1)
#     rgb2 = hue_to_rgb(hue2)
    
#     square1 = visual.Rect(win, width=0.4, height=0.4, fillColor=rgb1, lineColor=rgb1, pos=(-0.5, 0))
#     square2 = visual.Rect(win, width=0.4, height=0.4, fillColor=rgb2, lineColor=rgb2, pos=(0.5, 0))
    
#     square1.draw()
#     square2.draw()
#     win.flip()
#     core.wait(1)
#     win.color = (1, 1, 1)
#     win.flip()
#     core.wait(.25)
    
# # %% Wait for a key press to close
# event.waitKeys()
# win.close()
# core.quit()
