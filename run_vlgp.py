#!/usr/bin/python3

# calling syntax:
# run_vlgp infile.hf5 outfile.hf5 [num_latents] [sigma] [omega]

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
    sigma_val = float(sys.argv[4])
else:
    sigma_val = 1.0;


if len(sys.argv)>5:
    omega_val = float(sys.argv[5])
else:
    omega_val = 1e-5;

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
#sigma = np.full(nlatent, fill_value=sigma_val)
#omega = np.full(nlatent, fill_value=omega_val)
#fitted, _ = vlgp.fit(sample['y'], ['spike']*sample['y'].shape[-1], 
#                     sigma, omega, 
#                     lag=10, rank=100, 
#                     niter=300, tol=1e-5, adjhess=True, decay=0, verbose=False, learn_post=True, learn_param=True,
#                     learn_sigma=True, learn_omega=True, nhyper=5)

binwidth = 1
tau = 100
dyn_ndim=nlatent
fitted, _ = vlgp.fit(sample['y'], ['spike']*sample['y'].shape[-1],
                     dyn_ndim,
                     sigma=np.ones(dyn_ndim) * (1 - 1e-3), omega=np.ones(dyn_ndim)*(2*(binwidth/tau)**2),
                     lag=0, rank=500,
                     method='VB',
                     niter=100, tol=1e-5, verbose=False,
                     learn_param=True, learn_post=True, e_niter=5, m_niter=5,
                     adjust_hessian=False, decay=0,Adam=False,
                     learn_hyper=True, nhyper=5, subsample_size=200, hyper_obj='ELBO',
                     gp_noise=1e-3, successive=False)
#                     x=dyn, alpha=a, beta=b,


## if you want to pass in other variables, easy to add, e.g. add these lines above 
#                     x=sample['x'],
#                     alpha=sample['alpha'],
#                     beta=sample['beta'],  

fitted.pop('channel', None)

print("--- execution took %s seconds ---" % (time.time() - start_time))

print('saving fit to: ' + outfile)
util.save(fitted, outfile)
