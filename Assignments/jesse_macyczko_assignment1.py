# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:10:24 2024

@author: jrmac
"""
import numpy as np
import os
import random
import matplotlib.pyplot as plt

# %% Code assignment one, display 12 random images from fLoc_stimuli
fdir = '/Users/jrmac/Downloads/UNR_PSY_427_627_Fa2024-main/ClassDemos/fLoc_stimuli'
os.chdir(fdir)
print(fdir)
files = os.listdir(fdir)
length = len(files)
randsamp = random.sample(range(length), 12)

for x in range(len(randsamp)):
    im = plt.imread(files[randsamp[x]])
    plt.imshow(im, cmap = 'gray')
    plt.show()
    plt.axis('off')

imgarray = [plt.imread(files[randsamp[x]]) for x in range(len(randsamp))]
imgcon=np.concatenate(imgarray)
plt.imshow(imgcon, cmap = 'gray')
plt.axis('off')
plt.show()

np.save('randomly_selected_images.npy', imgarray)
a=np.load('randomly_selected_images.npy')

fig, axs = plt.subplots(3, 4, figsize=(16, 12))
for i, ax in enumerate(axs.flat):
    ax.imshow(imgarray[i], cmap = 'gray')
    ax.axis('off')
plt.show()   