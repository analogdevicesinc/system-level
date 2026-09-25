Loopback Delay Estimation Design
================================

This article will explain an example design that estimates the RF loopback delay
when a transmit and a receive port of the AD9361 transceiver are connected using
a cable. This design is useful when AD9361 is used as part of a hardware-in-loop
test setup with transmit and receive ports connected to the input and the output
of the device under test. For instance, in a digital predistortion application
where the transmit port of AD9361 is connected to the input port of a PA and the
output of the PA is connected to the receive port of AD9361 (via an
appropriately chosen attenuator), this design will help align the transmit and
the receive streams. Since this example focuses on achieving tightly time
aligned transmit and receive streams, the design will be built around logic for
the FPGA fabric with software control interfaces. Users can perform algorithmic
processing on the obtained aligned data streams in the host computer or extend
the design in the logic depending on their requirements.

Requirements:

-  MATLAB, Simulink, HDL Coder
-  `Communications Toolbox Support Package for Xilinx Zynq-Based Radio <https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/index.html>`_
-  Xilinx Vivado (Tested 2018.2)
-  :doc:`ADI AD9361 System on Module (SOM) SDR </solutions/reference-designs/adrv936x_rfsom/adrv936x_rfsom>`
-  A loopback cable with UFL female ports on both ends

To build and run the demo:

-  Create a MathWorks HSP compatible SD card by running the `Guided Host-Radio Hardware Setup <https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/ug/guided-host-radio-hardware-setup.html>`_ from within MATLAB.
-  Build the image for the design from MATLAB using the provided :git-TransceiverToolbox:`hdlworkflow <trx_examples/targeting/loopback-delay-estimation/hdlworkflow.m>` script
-  Download the generated image onto the SD card.

Now the ADRV9361-Z7035 can be booted from the built SD card, the :git-TransceiverToolbox:`trx_examples/targeting/loopback-delay-estimation/find_corr_threshold.m` and :git-TransceiverToolbox:`trx_examples/targeting/loopback-delay-estimation/run_loopback_tests.m` examples can be run from MATLAB. To see a simulation run of the design, open :git-TransceiverToolbox:`trx_examples/targeting/loopback-delay-estimation/loopback_delay_estimation.slx` and hit the play button.

Determining the Correlation Threshold For Integer Delay Estimation
------------------------------------------------------------------

With the ADI RF SOM connected to your host and with the TX1A and RX1A ports connected by a loopback cable, the first step in running the loopback delay estimation is finding the threshold value needed in the integer delay estimation piece of the model. This subsystem is based on correlating the result of a magnitude difference function applied to the received and reference waveforms. Specifically, the Zadoff-Chu (ZC) sequence portion of the synchronizing sequence is used for loopback delay estimation. See :git-TransceiverToolbox:`trx_examples/targeting/loopback-delay-estimation/initScript.m` for details on how the ZC-sequence is generated. Since the SNR of the received waveform (dependent on the cable used) affects this correlation operation, the threshold cannot be a fixed quantity and needs to be determined depending on the loopback cable used. Furthermore, selecting the right threshold is crucial for the overall design to work correctly since the subsystems that are downstream with respect to the integer delay estimation block are fired based on the identification of the correlation peak. In our experiments, we found that the peak corresponding to the integer delay is quite sharp and therefore, identifying the threshold is fairly straight-forward. You will observe that running :git-TransceiverToolbox:`trx_examples/targeting/loopback-delay-estimation/find_corr_threshold.m` will generate a plot similar to the one shown below.

.. image:: ../images/correlation_plot.png
   :align: center

By zooming into the peak seen in the second subplot, you should observe that the peak is quite clearly defined. You can modify this script to instrument tests that run over several iterations and then select the threshold after recording the histogram of the peak values observed. Note that the transmission of the synchronizing sequence occurs by pulsing a certain register in the model. Since it takes a finite amount of time for the pulse to occur after running the script, when you run :git-TransceiverToolbox:`trx_examples/targeting/loopback-delay-estimation/find_corr_threshold.m` repeatedly, you will see from the first subplot that the receive buffer contains the previously recorded integer delay, followed a bunch of zeros and then the current integer delay estimate. This is unavoidable and you can safely ignore this behavior. It will not have any effect on the logic designed to perform loopback delay estimation.

Integer and Fractional Delay Estimation
---------------------------------------

Use the correlation threshold determined in the previous step to modify the ``hw_tests`` struct member ``corr_thresh`` in :git-TransceiverToolbox:`trx_examples/targeting/loopback-delay-estimation/run_loopback_tests.m`. Now, run this script. You should observe that the DVB-S2 transmit and receive waveforms are captured after compensating for the corresponding integer and fractional delays and saved to ``hw_tests.txIQ`` and ``hw_tests.rxIQ`` respectively. The time-series plot of an arbitrary window of 200 samples generated by running script should look similar to the plot shown below.

.. image:: ../images/time_series_txiq_rxiq.png
   :align: center

In our experiments, we found that the fractional delay estimation algorithm is sensitive to magnitude and phase offsets between the received and reference ZC-sequence waveforms. Consequently, we implemented a magnitude and phase offset compensation subsystem that utilizes one cycle of a complex exponential waveform prepended to the ZC-sequence. Update the script to transmit a waveform of your choice. Note that the scale factor chosen is a value slightly smaller than the full-scale possible over 16-bits. This is due to the fact that the signal undergoes a small bitgrowth when passed through the Farrow-filter used for fractional delay compensation. The estimated fractional delay and the complex scale factor to match the received waveform with the transmitted waveform are also read from certain AXI4-Lite registers as shown in :git-TransceiverToolbox:`trx_examples/targeting/loopback-delay-estimation/run_loopback_tests.m`.
