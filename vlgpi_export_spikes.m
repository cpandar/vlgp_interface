function vlgpi_export_spikes(outfile, y, varargin)
%% exports spikes to an hdf5 file that can be easily read by python
%%
%% inputs: 
%%
%%   outfile: filename to output data to. it's reasonable to use the extension ".h5"
%%
%%   y: millisecond-binned spiketrains. in Matlab, it should be a 3-D array, [nNeurons x nTimesteps x nTrials]
%%
%%   varargin: 'name' - value pairs
%%         other variables you may want to pass into the python code
%%


    if exist(outfile,'file')
        warning(sprintf('warning - deleting file %s! any key to continue, ctrl-c to cancel'));
        pause
        delete(outfile);
    end

%% create an hdf5 file and add the variable y
    h5create(outfile, '/y', size(y));
    h5write(outfile, '/y', y);

    if exist('varargin','var') & ~isempty(varargin)
        %% assign the rest of the variables
        if mod(numel(varargin),2) ~= 0
            error('varargin should be name-value pairs')
        end

        nv = 1;
        while nv < numel(varargin)
            if ~ischar(varargin{nv})
                error('varargin should be name-value pairs');
            end
            
            h5create(outfile, sprintf('/%s', varargin{nv}), size(varargin{nv+1}));
            h5write(outfile, sprintf('/%s', varargin{nv}), varargin{nv+1});
            nv = nv+2;
        end
    end        
        

