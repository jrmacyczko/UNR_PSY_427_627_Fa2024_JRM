# image_sequence.py
import numpy as np
from psychopy import visual, core, event
import random
import os
import csv

def image_sequence(win, files, start_time, resp, condition, fdir):
    fixation_dot = visual.Circle(win, radius=7.5, fillColor='yellow', lineColor='yellow', pos=(0, 0), units='pix')
    randsamp = random.choices(range(len(files)), k=24)
    # Track responses
    responses = []  # Store response results
    shown_images = []  # Track images shown
    image_time = []
    last_shown_time = {}
    for x in range(len(randsamp)):
        # Load the image using visual.ImageStim
        img_path = os.path.join(fdir, files[randsamp[x]])
        image_stim = visual.ImageStim(win, image=img_path, size=(500, 500))

        # Draw the image
        image_stim.draw()
        fixation_dot.draw()
        win.flip()

        # Record the time at which the image is shown
        image_start_time = core.getTime()

        # Wait for 0.5 seconds while checking for responses
        response_key = None  # Initialize response_key
        response_time = None  # Initialize reaction time

        while core.getTime() - image_start_time < 0.5:
            keys = event.getKeys()
            if 'escape' in keys:
                #return responses, image_time, end
                # Save responses to CSV file
                win.close()
                with open('responses.csv', 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(['Result', 'Response Key', 'Response Time', 'Time Since Last', 'Condition'])
                    csv_writer.writerows(responses)
    
                # Save image times to CSV file
                with open('image_time.csv', 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(['Image Duration'])  # Header
                    csv_writer.writerows([[time] for time in image_time])
                raise Exception("Manual quite by user")
            if resp in keys:
                response_key = resp  # Capture the response key if pressed
                response_time = core.getTime() - start_time
        
        # Calculate the duration the image was displayed
        image_duration = core.getTime() - image_start_time
        image_time.append(image_duration)

        # Calculate time since last presentation if the image was shown before
        time_since_last = None
        if files[randsamp[x]] in last_shown_time:
            time_since_last = response_time - last_shown_time[files[randsamp[x]]]
        
        # Check if the image has been shown before
        if files[randsamp[x]] in shown_images:
            if response_key == resp:
                responses.append(('correct', response_key, response_time, time_since_last, condition))
            else:
                responses.append(('incorrect', response_key, response_time, time_since_last, condition))
        else:
            if response_key == resp:
                responses.append(('incorrect', response_key, response_time, time_since_last, condition))
            else:
                responses.append(('correct', response_key, response_time, time_since_last, condition))
                
        # Mark the image as shown
        shown_images.append(files[randsamp[x]])
        last_shown_time[files[randsamp[x]]] = response_time

        # Briefly show a blank screen before the next image
        win.color = (0.5, 0.5, 0.5)
        fixation_dot.draw()
        win.flip()
        core.wait(0.1)

    return responses, image_time
