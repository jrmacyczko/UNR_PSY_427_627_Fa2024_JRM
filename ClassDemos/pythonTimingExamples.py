# Python tiing functions
import psychopy
from psychopy import core
import numpy as np

#%% Get system timestamp
tx = psychopy.clock.getTime()
# Note that this is in WHOLE SECONDS...

#%% Get time with a clock, starting at a time
# Create a clock object
my_clock = psychopy.clock.Clock()
# Get the time! 
t0 = my_clock.getTime()

#%% Wait a specified duration
t1 = my_clock.getTime(); 
core.wait(2); 
t2 = my_clock.getTime()
print(t2-t1)

#%% Wait for a specified interval
wait_seconds = 3
my_clock2 = psychopy.clock.Clock()
t3 = my_clock2.getTime()
my_timer = core.CountdownTimer(wait_seconds)
while my_timer.getTime() > 0:
    # Do something
    pass
t4 = my_clock2.getTime()

#%% Participation code
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
    t1 = my_clock.getTime(); 
    core.wait(0.1); 
    t2 = my_clock.getTime()
    d = (t2 - t1)
    time_list[repeat] = d

np.std(time_list)
