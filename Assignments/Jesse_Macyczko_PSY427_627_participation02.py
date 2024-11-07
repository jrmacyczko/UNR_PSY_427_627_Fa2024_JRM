# Participation code 2
import psychopy
from psychopy import visual, core
import numpy as np

#%% Find difference in timings
# input variables
# for loop for number of repeats
# time 1, wait time, time 2, find difference
# save each difference as a new vairable name
# after the loop, find std dev

my_clock = psychopy.clock.Clock()
num_repeats = 10
wait_duration = .5
time_list = np.zeros((num_repeats, ))
for repeat in range(num_repeats):
    t1 = my_clock.getTime()
    core.wait(0.1); 
    t2 = my_clock.getTime()
    d = (t2 - t1)
    time_list[repeat] = d

np.std(time_list)

#%% Timing difference for screen flips
my_clock2 = psychopy.clock.Clock()
win = visual.Window([400,400])
flipt1 = win.flip()
core.wait(0)
flipt2 = win.flip()
win.close()
d = (flipt2-flipt1)
print(d)
