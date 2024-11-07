# main_experiment.py
from psychopy import visual, core, event
import random
import os
import csv
from image_sequence import image_sequence  # Import the function from the other file

#%% Images
fdir = '/Users/jrmac/UNR_PSY_427_627_Fa2024_JRM/ClassDemos/fLoc_stimuli'
face_images = [f for f in os.listdir(fdir) if 'adult' in f or 'child' in f]
place_images = [f for f in os.listdir(fdir) if 'house' in f or 'corridor' in f]
body_images = [f for f in os.listdir(fdir) if 'body' in f or 'limb' in f]
text_images = [f for f in os.listdir(fdir) if 'number' in f or 'word' in f]
object_images = [f for f in os.listdir(fdir) if 'instrument' in f or 'car' in f]
scrambled_images = os.listdir(fdir)

#%% Open window
fullscr = True
screen_size = [600, 600]
win = visual.Window(size=screen_size, 
                    color=(0.5, 0.5, 0.5),
                    fullscr=fullscr, 
                    units='pix')

# Create a fixation dot
fixation_dot = visual.Circle(win, radius=7.5, fillColor='yellow', lineColor='yellow', pos=(0, 0), units='pix')

# Display message
my_str = 'In this experiment, you will see images of faces, places, bodies, objects, and text, along with scrambled images. Press any key to continue.'
txt_stim = visual.TextStim(win, text=my_str)
txt_stim.draw()
win.flip()
event.waitKeys()

my_str = 'Please select the button you would like to use to provide your response in the experiment. Once you select the button, the experiment will begin.'
txt_stim = visual.TextStim(win, text=my_str)
txt_stim.draw()
win.flip()
key_out = event.waitKeys()
resp = key_out[0]  # Capture the response button

fixation_dot.draw()
win.flip()
core.wait(1)
start_time = core.getTime()

#%% Initialize response lists
responses = []
image_time = []

# Display images
new_responses, new_image_time, end = image_sequence(win, face_images, start_time, resp, 'Faces', fdir)
responses.extend(new_responses)
image_time.extend(new_image_time)

new_responses, new_image_time, end = image_sequence(win, place_images, start_time, resp, 'Places', fdir)
responses.extend(new_responses)
image_time.extend(new_image_time)

new_responses, new_image_time, end = image_sequence(win, body_images, start_time, resp, 'Bodies', fdir)
responses.extend(new_responses)
image_time.extend(new_image_time)

new_responses, new_image_time, end = image_sequence(win, text_images, start_time, resp, 'Text', fdir)
responses.extend(new_responses)
image_time.extend(new_image_time)

new_responses, new_image_time, end = image_sequence(win, object_images, start_time, resp, 'Objects', fdir)
responses.extend(new_responses)
image_time.extend(new_image_time)

new_responses, new_image_time, end = image_sequence(win, scrambled_images, start_time, resp, 'Scrambled', fdir)
responses.extend(new_responses)
image_time.extend(new_image_time)
# Save responses to CSV file
with open('responses.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Result', 'Response Key', 'Response Time', 'Time Since Last', 'Condition'])
    csv_writer.writerows(responses)

# Save image times to CSV file
with open('image_time.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Image Duration'])  # Header
    csv_writer.writerows([[time] for time in image_time])

# Close the window
    win.close()
    core.quit()
