# vlgp_interface

Code to interface between Matlab and the variational Latent Gaussian Process (vLGP) model [1] python implementation - https://github.com/catniplab/vLGP.

### Usage example:

From Matlab:

```vlgpi_export_spikes(outfile_for_spiking_data, y)```

- *outfile_for_spiking_data* - filename, will be written, store spiketrains in an HDF5 file 
- *y* -  millisecond-binned spiketrains. 3-D Matlab array [nNeurons x nTimesteps x nTrials]

From the command line:

```python run_vlgp.py outfile_for_spiking_data outfile_for_vlgp_results n_latents```

- *outfile_for_spiking_data* - filename, output from previous step
- *outfile_for_vlgp_results* - filename, will be written, stores the results of vLGP in an HDF5 file
- *n_latents* - dimensionality of the LDS to fit


Back in Matlab:

```results = vlgpi_import_results(outfile_for_vlgp_results)```

- *outfile_for_vlgp_results* - filename, output from previous step


## Components
### Matlab code: 
`vlgpi_export_spikes.m` - outputs spikes to an hdf5 file for easy import in Python

`vlgpi_import_results.m` - takes the resulting output and makes it easily parse-able in Matlab

### Python code:
`run_vlgp.py` - reads in data, calls vLGP, saves results to file

NOTE: You must edit run_vlgp.py to specify the path to the vLGP codepack



> 1. Yuan Zhao and Il Memming Park. *Variational Latent Gaussian Process for Recovering Single-Trial Dynamics from Population Spike Trains.* <br>
> arXiv:1604.03053v1 [stat.ML]

