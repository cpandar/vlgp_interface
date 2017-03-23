#!/usr/bin/python3

# calling syntax:
# run_vlgp vlgp_results.hf5 outfile.hf5

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
resultsfile = sys.argv[1]
outfile = sys.argv[2]


import vlgp
from vlgp import util, simulation, math, plot

print('loading results from: ' + resultsfile)
results = util.load(resultsfile)




## time the execution
import time
start_time = time.time()

np.random.seed(0)
# YUAN: v needs be a named argument
predictions = vlgp.predict(results['mu'], results['a'], results['b'], v=results['v'])


print("--- execution took %s seconds ---" % (time.time() - start_time))

print('saving fit to: ' + outfile)
# YUAN: only support saving dict now
util.save({'predictions': predictions}, outfile)
