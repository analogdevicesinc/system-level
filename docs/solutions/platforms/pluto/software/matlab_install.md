# MATLAB Installation and Examples

MATLAB is another popular choice for working with PlutoSDR, especially for those who are already familiar with MATLAB's signal processing capabilities. You can use the `Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio` in MATLAB to interface with PlutoSDR. This toolbox provides functions for configuring Pluto and accessing its data. 


## MATLAB Pluto Toolbox Installation

To use PlutoSDR with MATLAB, you need to install:
1. [Communications Toolbox](https://www.mathworks.com/products/communications.html)
2. [DSP System Toolbox](https://www.mathworks.com/products/dsp-system.html)
3. [Signal Processing Toolbox](https://www.mathworks.com/products/signal.html)
4. [The Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio](https://www.mathworks.com/matlabcentral/fileexchange/61624-communications-toolbox-support-package-for-analog-devices-adalm-pluto-radio)  

These can all be found in the MATLAB "Add-Ons":

```{image} resources/matlab1.svg
:width: 450px
:align: center
```  
Then search for the desired toolbox:

```{image} resources/matlab2.svg
:width: 400px
:align: center
```  
When installing the Pluto Toolbox, a "Connect Hardware" window will open.  Just select cancel.  Do not allow MATLAB to update Pluto's firmware.  

```{image} resources/matlab3.svg
:width: 400px
:align: center
```  
```{caution} 
When installing this Pluto Toolbox, MATLAB may prompt you to update or reinstall Pluto's firmware.  
⚠️**Do not allow MATLAB to modify Pluto's firmware!**⚠️  
Instead, follow {ref}`pluto getstarted firmware_upgrade_section` to update Pluto's firmware.
```


## MATLAB Pluto (2T/2R) Installation

If you are using Pluto in the {ref}`2T2R configuration <pluto setup adding-a-second-rx-and-tx-channel>`, then you'll also need to install the toolboxes necessary for the AD9361 control. They are found in the MATLAB Add On manager. The toolboxes to install are:

1. [Analog Devices, Inc. Transceiver Toolbox](https://www.mathworks.com/matlabcentral/fileexchange/72645-analog-devices-inc-transceiver-toolbox)
2. [MATLAB Support for MinGW-w64 C/C++ Compiler](https://www.mathworks.com/matlabcentral/fileexchange/52848-matlab-support-for-mingw-w64-c-c-fortran-compiler)

After installing these toolboxes, you need to run these commands from a MATLAB prompt:

```{code-block} matlab
A=adi.utils.libad9361
A.download_libad9361
```



## Test MATLAB Pluto (1T/1R) Installation

Once you have the Pluto Toolbox installed, perform a simple test just to make sure everything is working.  With Pluto connected to the center USB port, type:

```{code-block} matlab
rx = sdrrx('Pluto', 'RadioID', 'ip:192.168.2.1');
data = rx();
data(1:10)
```

This first creates a Pluto receive object ("rx").  For the context, it is best to use the ip address of Pluto -- which by default is 192.168.2.1.  Then the rx() command grabs one buffer of receive data from Pluto.  Finally, the first 10 samples are printed out.  The results should look like this:

```{image} resources/matlab4.svg
:width: 400px
:align: center
```  
Here's another example, this time setting more attributes and plotting the result:

```{code-block} matlab   
% Create PlutoSDR receiver
rx = sdrrx('Pluto', ...
    'RadioID', 'ip:192.168.2.1', ...
    'CenterFrequency',      2.4e9, ...      % 2.4 GHz
    'BasebandSampleRate',   1e6, ...        % 1 MSPS
    'SamplesPerFrame',      4096, ...
    'OutputDataType',       'double');      % convenient for plotting/processing

% Optional: verify connection and settings
info(rx)

% Receive one frame of samples
samples = rx();   % Complex baseband I/Q

% Plot first 1000 samples (real part)
N = min(1000, numel(samples));
plot(real(samples(1:N)));
xlabel('Sample Index');
ylabel('Amplitude');
title('Received Samples from PlutoSDR (Real Part)');
grid on

% Cleanup (recommended when done)
release(rx);
```


You should see something like the plot below (Pluto is just measuring noise):

```{image} resources/matlab5.svg
:width: 400px
:align: center
```  

## Test MATLAB Pluto (2T/2R) Installation

If you are using Pluto as a 2T/2R device, then you need to address it as a AD9361, and not as a Pluto.  That means that instead of using the Pluto Toolbox, you'll use the Analog Devices Transceiver Toolbox. The setup is very similar though. Here are some examples:


Simple example (just a check that you've installed the Transceiver Toolbox)

```{code-block} matlab
sdr = adi.AD9361.Rx;
sdr.uri = 'ip:192.168.2.1';
data = sdr();
data(1:10)
```


Here's a more complete example showing how to create a waveform, transmit it, and process both channels of receive data:

```{code-block} matlab
clear all;

amplitude = 2^15; frequency = 0.12e6;
swv1 = dsp.SineWave(amplitude, frequency);
swv1.ComplexOutput = true;
swv1.SamplesPerFrame = 1024;
swv1.SampleRate = 3e6;
y = swv1();

% Setup receive
rx = adi.AD9361.Rx('uri', 'ip:192.168.2.1');
rx.EnabledChannels = [1,2];
rx.CenterFrequency = 2.e9;
rx.kernelBuffersCount = 2;
rx.GainControlModeChannel0 = 'slow_attack';
rx.GainControlModeChannel1 = 'slow_attack';
rx.SamplingRate = 3e6;
rx.SamplesPerFrame = 1024;

% Setup transmit
tx = adi.AD9361.Tx('uri', 'ip:192.168.2.1');
tx.EnabledChannels = [1,2];
tx.CenterFrequency = rx.CenterFrequency;
tx.AttenuationChannel0 = -10;
tx.AttenuationChannel1 = -10;
tx.DataSource = "DMA";
tx.EnableCyclicBuffers = true;

tx([y,y]);

%% Run
for k=1:10
    valid = false;
    while ~valid
        [data, valid] = rx();
    end
end
%tx.release();
%rx.release();

rx1 = data(:,1);
rx2 = data(:,2);
num_points = numel(rx1);

figure(1); 
plot(0:num_points-1, real(rx1), 'r', 0:num_points-1, imag(rx1), 'b'); 
xlim([0 250]); title("Rx1");
figure(2); 
plot(0:num_points-1, real(rx2), 'r', 0:num_points-1, imag(rx2), 'b'); 
xlim([0 250]); title("Rx2"); xlabel('sample index'); 
```

```{image} resources/matlab6.svg
:width: 300px
:align: center
```  

## Useful Pluto MATLAB Links
- [Additional Examples](https://github.com/analogdevicesinc/TransceiverToolbox/tree/master/trx_examples/streaming/ad936x)
- [Pluto Toolbox](https://www.mathworks.com/matlabcentral/fileexchange/61624-communications-toolbox-support-package-for-analog-devices-adalm-pluto-radio)
- [Test and Troubleshooting](https://www.mathworks.com/help/comm/plutoradio/ug/manual-host-radio-hardware-setup.html)
- [MATLAB Pluto Examples](https://www.mathworks.com/help/comm/plutoradio/ug/what-to-do-after-installation.html)
- [Analog Devices Labs with MATLAB and Pluto](https://github.com/tfcollins/RFSOM-Seminar2018-Labs)
- [Intro to Comms Systems Using Pluto](https://www.mathworks.com/matlabcentral/fileexchange/69417-introductory-communication-systems-course-using-sdr)
- [Chapter 5: Pluto Hardware and MATLAB](https://www.analog.com/en/resources/technical-books/software-defined-radio-for-engineers.html)

```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```
