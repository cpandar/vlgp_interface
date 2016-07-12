#!/usr/bin/python

# calling syntax:
# run_vlgp infile.hf5 outfile.hf5 [num_latents] [sigma]

## must specify where the vlgp code is
#  (pull it from https://github.com/catniplab/vLGP)
PATH_TO_VLGP = 'submodules/vLGP'

# add vlgp to module import path
import sys
sys.path.append(PATH_TO_VLGP)

import os
from os import path

import numpy as np
from scipy import stats
from scipy import linalg


# handle command line args
# caller should pass in a filename for data to be loaded
assert len(sys.argv)>=3, 'need to pass in a filename to load and an output filename'
spikefile = sys.argv[1]
outfile = sys.argv[2]

if len(sys.argv)>3:
    nlatent = int(sys.argv[3])
else:
    nlatent = 3;

if len(sys.argv)>4:
    sigma_val = int(sys.argv[4])
else:
    sigma_val = 1.0;

import vlgp
from vlgp import util, simulation, math, plot

print('loading data from: ' + spikefile)
sample = util.load(spikefile)


# ## to verify things are formatted correctly, plot the data
# import matplotlib.pyplot as plt
# plot.spike(sample['y'], ncol=5, fontsize=30)
# plt.show()


## time the execution
import time
start_time = time.time()

np.random.seed(0)
sigma = np.full(nlatent, fill_value=sigma_val)
omega = np.full(nlatent, fill_value=1e-5)
fitted, _ = vlgp.fit(sample['y'], ['spike']*sample['y'].shape[-1], 
                     sigma, omega, 
                     lag=10, rank=100, 
                     niter=300, tol=1e-5, adjhess=True, decay=0, verbose=False, learn_post=True, learn_param=True,
                     learn_sigma=True, learn_omega=True, nhyper=5)

## if you want to pass in other variables, easy to add, e.g. add these lines above 
#                     x=sample['x'],
#                     alpha=sample['alpha'],
#                     beta=sample['beta'],  

fitted.pop('channel', None)

print("--- execution took %s seconds ---" % (time.time() - start_time))

print('saving fit to: ' + outfile)
util.save(fitted, outfile)
