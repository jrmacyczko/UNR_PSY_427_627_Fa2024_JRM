# Functions for event detection in python
import numpy as np
from psychopy import visual, core, event
import random

#%% Dot series
x1 = np.linspace(-300, 300, 6)
x = np.random.permutation(x1)
y = 0

# Open window
fullscr = True
screen_size = [600, 600]
max_wait = 3
method = 'getKeys'
win = visual.Window(size=screen_size, 
                    color=(0.5, 0.5, 0.5),
                    fullscr=fullscr, 
                    units='pix')

# Display message:
my_str = 'Press left or right arrow to indicate which side of the screen the dot is on, or press q to quit.'
txt_stim = visual.TextStim(win, text=my_str)
txt_stim.draw()
win.flip()
core.wait(1.0)

# Experiment
for n in range(len(x)):
    circ_pos = (x[n], y)  # Center of screen
    circ_stim = visual.Circle(win, radius=20,
                              units='pix',
                              fillColor=(1.0, 0.5, 0.0),
                              pos=circ_pos)
    circ_stim.draw()
    win.flip()
    t0 = core.getTime()
    
    # Initialize variable for storing response
    key_out = []
    
    # Get keypresses in buffer
    if method == 'waitKeys':
        key_out = event.waitKeys(maxWait=max_wait, keyList=['left', 'right', 'q'])
    elif method == 'getKeys':
        # Use a while loop
        while core.getTime() < (t0 + max_wait):
            key_out = event.getKeys(keyList=['left', 'right', 'q'], timeStamped=True)
            if len(key_out) > 0:
                break
    
    # Calculate reaction times
    reaction_times = []
    correct_response = None  # Track the correct response
    if x[n] < 0:
        correct_response = 'left'
    elif x[n] > 0:
        correct_response = 'right'

    if key_out:
        for key, time in key_out:
            rt = time - t0
            is_correct = (key == correct_response)
            correctness = "Correct" if is_correct else "Incorrect"
            print(f'Key: {key}, Reaction Time: {rt:.3f} seconds, {correctness}')

    else:
        print('Response timed out!')

    print('\n\n\n')
    win.color = (.5, .5, .5)
    win.flip()
    core.wait(random.uniform(0.5, 1))

win.close()
core.quit()
