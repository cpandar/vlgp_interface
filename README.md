# vlgp_interface

Code to interface with the variational Latent Gaussian Process (vLGP) model [1] - https://github.com/catniplab/vLGP.

Matlab code: 
vlgpi_export_spikes.m - outputs spikes to an hdf5 file for easy import in Python
vlgpi_import_results.m - takes the resulting output and makes it easily parse-able in Matlab

Python code:
run_vlgp.py - reads in data, calls vLGP, saves results to file

NOTE: You must edit run_vlgp.py to specify the path to the vLGP codepack

Usage example:

from Matlab:

vlgpi_export_spikes(outfile_for_spiking_data, y)
   where y: millisecond-binned spiketrains. should be a 3-D Matlab array, [nNeurons x nTimesteps x nTrials]

from the command line:

python run_vlgp outfile_for_spiking_data outfile_for_vlgp_results

from Matlab:
results = vlgpi_import_results(outfile_for_vlgp_results)





1. Yuan Zhao and Il Memming Park. Variational Latent Gaussian Process for Recovering Single-Trial Dynamics from Population Spike Trains. arXiv:1604.03053v1 [stat.ML]



