#!/usr/bin/python

## must specify where the vlgp code is
#  (pull it from https://github.com/catniplab/vLGP)
PATH_TO_VLGP = 'submodules/vLGP.git'

# add vlgp to module import path
import sys
sys.path.append(PATH_TO_VLGP)

import os
from os import path

import numpy as np
from scipy import stats
from scipy import linalg


# handlle command line args
# caller should pass in a filename for data to be loaded
assert len(sys.argv)>=3, 'need to pass in a filename to load and an output filename'
spikefile = sys.argv[1]
outfile = sys.argv[2]


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

nlatent = 3
np.random.seed(0)
sigma = np.full(nlatent, fill_value=1.0)
omega = np.full(nlatent, fill_value=1e-5)
fitted, _ = vlgp.fit(sample['y'], ['spike']*sample['y'].shape[-1], 
                     sigma, omega, 
                     lag=10, rank=100, 
                     niter=300, tol=1e-6, adjhess=True, decay=0, verbose=False, learn_post=True, learn_param=True,
                     learn_sigma=True, learn_omega=True, nhyper=5)

## if you want to pass in other variables, easy to add, e.g. add these lines above 
#                     x=sample['x'],
#                     alpha=sample['alpha'],
#                     beta=sample['beta'],  

fitted.pop('channel', None)

print("--- execution took %s seconds ---" % (time.time() - start_time))

print('saving fit to: ' + outfile)
util.save(fitted, outfile)
