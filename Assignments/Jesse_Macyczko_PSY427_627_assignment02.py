# %% Color patches at varying distances apart
from psychopy import visual, core, event
import colorsys
import random

# Function to generate two hues within a specified distance
def generate_hues(distance):
    hue = random.uniform(0, 1)
    hue2 = hue + random.uniform(-distance, distance)
    hue2 = hue2 % 1.0
    return hue, hue2

# Function to convert hue to RGB
def hue_to_rgb(hue):
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return r, g, b

# Function to display two squares for specified time
def color_squares(dist1, dist2, on, off, total_time): 
    iteration_time = on + off
    total_iterations = int(total_time / iteration_time)
    
    hue_distance = [random.uniform(dist1, dist2) for _ in range(total_iterations)]

    for x in range(total_iterations):
        hue1, hue2 = generate_hues(random.choice(hue_distance))
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

# Parameters
on = 1
off = .25
time = 6
between = 3

# Create a window
win = visual.Window(size=(600, 600), color=(1, 1, 1), units='norm')

color_squares(0, .1, on, off, time)
core.wait(between)
color_squares(.1, .2, on, off, time)
core.wait(between)
color_squares(.4, .5, on, off, time)

# %% Wait for a key press to close
event.waitKeys()
win.close()
core.quit()
