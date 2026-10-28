.. _fmcomms2 common datafiles:

AD-FMCOMMS2/3/4 Datafiles
===============================================================================

.. important::

   This is work in progress, and is not yet 100% complete.

In this section, we provide the reference data files of several frequently used
digital baseband modulation schemes and their corresponding Simulink models.
With these data files, you are ready to transmit them using the AD9361 found on
the AD-FMCOMMS2-EBZ / AD-FMCOMMS3-EBZ and test your board. By changing the given
Simulink models, you can easily generate your own data files.

.. note::

   In order to run the models on this page, your MATLAB license needs to include
   the following components:

   - MATLAB Version 8.2
   - Simulink Version 8.2
   - Communications System Toolbox Version 5.5
   - DSP System Toolbox Version 8.5

Data transfer
-------------------------------------------------------------------------------

Once files have been created by MATLAB/Simulink, they can be
:external+kuiper:doc:`transferred to the target <index>`.

QPSK
-------------------------------------------------------------------------------

PSK is one type of the phase modulation (PM) schemes. In this section, two
flavors of QPSK data are generated, one with raised cosine pulse shaping
filters, and the other one without.

Since we would like to transmit the QPSK at a sample rate of 20 M Symbols/s with
AD9361, the sample time specified in "Random-Integer Generator" block is
1/(20e6). The users can specify their own sample rate.

QPSK without Pulse Shaping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The figure below shows a QPSK transmission model without any pulse shaping
filter. Since there are two independent channels on the Tx paths, we model both
of them. However, for simplicity, we make them identical. The transmitted
signals are saved to workspace.

Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../images/qpsknofilt.png
   :alt: QPSKnofilt.png

.. admonition:: Download
   :class: download

   You can download the Simulink model from below:

   - :dokuwiki:`qpsknofilt_model.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qpsknofilt_model.zip>`

In order to observe the transmitted spectrum, we use a "Spectrum Analyzer"
block. Since there is no pulse shaping on the Tx path, observe how
rectangular-pulse QPSK symbols occupy the entire signal bandwidth in the
frequency domain, potentially disturbing adjacent channels in the RF spectrum.
Clearly this is not an efficient use of signal bandwidth.

.. image:: ../images/resultnofilt.png
   :alt: resultnofilt.png
   :width: 900

Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   Once the transmitted signals are in workspace, we use the following two lines
   to write them to a text file:

   .. code:: matlab

      newdata = [I1 Q1 I2 Q2];

      dlmwrite('qpsk.txt',newdata,',');

   You open this text file and manually add the word "TEXT" at the very
   beginning, and then save the file.

.. admonition:: Download
   :class: download

   You can download the generated data from below:

   - :dokuwiki:`qpsknofilt_data.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qpsknofilt_data.zip>`

.. tip::

   - For each line, the data is in the order of [I1, Q1, I2, Q2].
   - The first line must be the word "TEXT".
   - In Windows, you are suggested to open the txt file using WordPad to show
     the line breaks properly.

QPSK with Pulse Shaping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QPSK symbols observed in the previous model cannot be transmitted over the
air as perfect rectangular pulses, which would require infinite signal
bandwidth. They must first be smoothed in the time domain, in order to limit the
signal bandwidth in the frequency domain. Consequently, the first stage of the
Tx signal chain is often a pulse-shaping filter, followed by subsequent stages
of interpolation filters to increase the sampling rate to the DAC.

In this section, we will employ a root-raised cosine pulse-shaping filter to
smooth the QPSK pulses in the time domain, limiting the signal bandwidth to 10
MHz in the frequency domain.

Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The figure below shows a QPSK transmission model with the pulse shaping filters.
Since pulse shaping filters are often distributed as a matched pair between
transmitter and receiver, we use the filter shape of 'Square root' [1]_.

.. image:: ../images/qpskwithfilter.png
   :width: 900

.. admonition:: Download
   :class: download

   You can download the Simulink model from below:

   - :dokuwiki:`qpskwithfilt_model.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qpskwithfilt_model.zip>`

   The data rate is defined in the parameter ``Fs``.

.. tip::

   - When the 'square root raised cosine' response of the transmit filter is
     convolved in the time domain with that of the receive filter, the aggregate
     response is a 'raised cosine'.
   - It is the 'raised cosine' that has the desirable quality of mitigating
     inter-symbol interference in the time domain.

In order to observe the effect of the pulse shaping filters, we use a "Spectrum
Analyzer" block, as well as several "Constellation" blocks.

.. image:: ../images/resultwithfilt.png
   :width: 900

.. note::

   We have the following observations:

   - The transmitted signal bandwidth is constrained to 10 MHz in the frequency
     domain.
   - Given the transmit filter, if there is no matched receive filter, the
     received symbols are completely noise (refer to "Rx Without Receive
     Filter").
   - Given the transmit filter, if there exists matched receive filter, the
     received symbols are perfect (refer to "Rx With Receive Filter").

Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: Download
   :class: download

   You can download the generated data from below:

   - :dokuwiki:`qpskwithfilt_txt.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qpskwithfilt_txt.zip>`

   The data rate is 30.72 MSPS.

   It is in the same format as the data in previous section.

Data Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before you look at the IIO Oscilloscope [2]_, make sure the sampling rate of ADC
and DAC is set at 30.72 MSPS, as shown in the figure below. Otherwise, it may
incur some problems. In this panel, there are quite a few other parameters you
can tune (DCXO, RF Bandwidth, LO Frequency), in order to get the optimal
transmission and reception performance for your system.

.. image:: ../images/iiosetting_new.png
   :width: 500

.. note::

   The DCXO setting can be different from board to board. You are suggested to
   find a proper setting using signal generator and spectrum analyzer in the
   lab.

Since there is no match filter on AD9361 receive path, the data obtained from
AD9361 receiver side does not show the constellation of QPSK clearly. Therefore,
by simply looking at the ADI IIO Oscilloscope, it is difficult to see whether
the received data is valid or not, as shown in the figure below.

.. image:: ../images/qpsk_osc_new.png
   :alt: qpsk_osc_new.png
   :width: 500

However, with the ``save data`` function of the IIO application, we can now save
the received data in MATLAB compatible format (.mat file), let the data pass
through a match filter in Simulink, and then verify whether the received data is
a QPSK or not. The ``save data`` function can be accessed via "File"-"Save As",
as shown in the figure below. There are several data formats available. Since we
want the data to be used in MATLAB, we will pick up the .mat format.

.. image:: ../images/savedata.png
   :alt: savedata.png
   :width: 450

Given the received data, we can now proceed to the Simulink receiver model to
verify the data. After you launch MATLAB and the receiver model
``qpsk_receiver.slx``, the next step is to load the .mat file in workspace,
because the ``Signal From Workspace`` blocks use the data as input. In this
model, the data rate is the same as the generated data rate (30.72 MSPS), and
the receive filter is the match of the transmit filter. When looking at the IIO
scope, we found the constellation of the received signal from the AD9361 shows a
rotation compared to the transmitted signal, so a ``Phase/Frequency Offset``
block is employed here to compensate for the phase offset. The value of the
phase offset is calculated in Simulink Callbacks. According to the constellation
plot below, it is very clear that the received data is a QPSK, so the AD9361
Tx/Rx chain gets verified.

.. image:: ../images/qpsk_waveform_verify_new.png
   :width: 450

.. admonition:: Download
   :class: download

   You can download the saved mat data file from below:

   - :dokuwiki:`qpskwithfilt_mat.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qpskwithfilt_mat.zip>`

   You can download the receiver model from below:

   - :dokuwiki:`qpsk_receiver_new.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qpsk_receiver_new.zip>`

   Make sure you load the mat data file in the workspace first. Otherwise, the
   model will not run.

   The data rate is defined in the parameter ``Fs`` and the phase offset is
   defined in the parameter ``PhaseOffset``.

.. tip::

   A few tips for verification, which can be applied to the other modulation
   cases:

   - Make the data rate consistent in data generation and receiver.
   - Set the IIO parameters properly, such as ADC and DAC sample rate.
   - Compensate for the phase offset occurred in AD9361.

16-QAM
-------------------------------------------------------------------------------

QAM is one type of the amplitude modulation (AM) schemes. In this section, we
use "Rectangular QAM Modulator Baseband" block to modulate the input random
integer. If you would like a lower or higher order of QAM modulation, you only
need to change the "M-ary number" of this block.

Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The figure below shows a 16-QAM transmission model with the square root raised
cosine pulse shaping filters. In order to observe the effect of the pulse
shaping filters, we use a "Spectrum Analyzer" block, as well as several
"Constellation" blocks on one of the channels.

.. image:: ../images/16qam.png
   :width: 900

.. admonition:: Download
   :class: download

   You can download the Simulink model from below:

   - :dokuwiki:`qam16_model.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qam16_model.zip>`

   The data rate is defined in the parameter ``Fs``.

Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   You can download the generated 16-QAM data from below:

   - :dokuwiki:`qam16_20mdata.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qam16_20mdata.zip>`

   It is in the same format as the data in previous sections and the data rate
   is 20 M.

Data Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since there is no match filter on AD9361 receive path, the data obtained from
AD9361 receiver side does not show a clear constellation of 16-QAM. Actually,
since the order of 16-QAM is higher than that of QPSK in the previous section,
the constellation here is even more noisy compared to QPSK, as shown in the
figure below.

.. image:: ../images/qam16.png
   :alt: qam16.png
   :width: 600

However, with the ``save data`` function of the IIO application, we can now save
the received data in MATLAB compatible format (.mat file), let the data pass
through a match filter in Simulink, and then verify whether the received data is
a 16-QAM or not. Before you save the data, make sure the sampling rate of ADC
and DAC is set properly. In this example, we set the sample rate of ADC and DAC
5 times of the generated data rate (20 MSPS), which is 100 MSPS.

.. admonition:: Download
   :class: download

   You can download the saved mat data file from below:

   - :dokuwiki:`qam16_20.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qam16_20.zip>`

Given the received data, we can now proceed to the Simulink receiver model to
verify the data. After you launch MATLAB and the receiver model
``qam16_receiver.slx``, the next step is to load the .mat file in workspace,
because the ``Signal From Workspace`` blocks use the data as input. In this
model, the data rate is the same as the generated data rate (20 MSPS), and the
receive filter is the match of the transmit filter. When looking at the IIO
scope, we found the received signal from AD9361 shows a 45 degree rotation
compared to the transmitted signal, so a ``Phase/Frequency Offset`` block is
employed here to compensate for the phase offset. According to the constellation
plot, it is very clear that the received data is a 16-QAM, so the AD9361 Tx/Rx
chain gets verified.

.. image:: ../images/qam16_verified.png
   :width: 700

.. admonition:: Download
   :class: download

   You can download the receiver model from below:

   - :dokuwiki:`qam16_receiver.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/qam16_receiver.zip>`

   The data rate is defined in the parameter ``Fs`` and the phase offset is
   defined in the parameter ``PhaseOffset``.

MSK
-------------------------------------------------------------------------------

MSK stands for minimum shift keying. It is one type of the continuous phase
modulation (CPM) schemes [3]_. In this section, we use "MSK Modulator Baseband"
block to modulate the input random binary bits. In other words, the input is
either 0 or 1.

Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The figure below shows a MSK transmission model with the square root raised
cosine pulse shaping filters. In order to observe the effect of the pulse
shaping filters, we use a "Spectrum Analyzer" block, as well as several
"Constellation" blocks on one of the channels.

.. image:: ../images/msk.png
   :width: 900

.. admonition:: Download
   :class: download

   You can download the Simulink model from below:

   - :dokuwiki:`msk_model.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/msk_model.zip>`

   The data rate is defined in the parameter ``Fs``.

Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   You can download the generated MSK data from below:

   - :dokuwiki:`msk_20mdata.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/msk_20mdata.zip>`

   It is in the same format as the data in previous sections and the data rate
   is 20 M.

Data Verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since there is no match filter on AD9361 receive path, the data obtained from
AD9361 receiver side does not show a clear constellation of MSK signals, as
shown in the figure below. However, it matches the "Rx Without Receive Filter"
plot from Simulink.

.. image:: ../images/msk_osc.png
   :alt: msk_osc.png
   :width: 600

With the ``save data`` function of the IIO application, we can now save the
received data in MATLAB compatible format (.mat file), let the data pass through
a match filter in Simulink, and then verify whether the received data is a MSK
or not. Before you save the data, make sure the sampling rate of ADC and DAC is
set properly. In this example, we set the sample rate of ADC and DAC 5 times of
the generated data rate (20 MSPS), which is 100 MSPS.

.. admonition:: Download
   :class: download

   You can download the saved mat data file from below:

   - :dokuwiki:`msk_20.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/msk_20.zip>`

Given the received data, we can now proceed to the Simulink receiver model to
verify the data. After you launch MATLAB and the receiver model
``msk_receiver.slx``, the next step is to load the .mat file in workspace,
because the ``Signal From Workspace`` blocks use the data as input. In this
model, the data rate is the same as the generated data rate (20 MSPS), and the
receive filter is the match of the transmit filter. According to the
constellation plot, it is very clear that the received data is a MSK, so the
AD9361 Tx/Rx chain gets verified.

.. image:: ../images/msk_receiver.png
   :width: 700

.. admonition:: Download
   :class: download

   You can download the receiver model from below:

   - :dokuwiki:`msk_receiver.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/msk_receiver.zip>`

   The data rate is defined in the parameter ``Fs`` and the phase offset is
   defined in the parameter ``PhaseOffset``. In this example, there is no
   rotation shown by the received signal, so ``PhaseOffset=0``.

LTE
-------------------------------------------------------------------------------

Besides the data generated by the basic modulation schemes, it is also possible
to transmit the data from some more advanced wireless communication standards.
In this section, we will generate some LTE (Long Term Evolution) data from an
existing Simulink example.

.. tip::

   - You can open the example by typing "LTEPDSCHExample" in the command window.
   - You must have Communications System Toolbox license in order to run this
     example.

Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The figure below shows a LTE example according to the specifications developed
by the Third Generation Partnership Project (3GPP). It highlights only the
downlink physical channel (PDSCH) processing. In order to obtain the transmitted
data, we add a "Signal to Workspace" block on the transmitter side (circled in
red). By double clicking the "Model Parameters" block, we can change the model
settings such as channel bandwidth, antenna configuration and etc.

Since LTE is a sophisticated standard, you are encouraged to read the Help
Document of this example and its related references to get more information
[4]_.

.. image:: ../images/lte.png
   :alt: Subsystem diagram
   :width: 900

After you run the model, the transmitted data named "Tx" will be saved in
workspace. Since it is a Nx2 complex vector, we need to do some processing on it
to make the data format compatible with AD9361 transmission.

.. admonition:: Download
   :class: download

   You can download the Simulink model and the post-processing m-file from
   below:

   - :dokuwiki:`lte_model.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/lte_model.zip>`

When the data is transmitted and received by real-world hardware, like AD9361,
it is difficult to observe the clear constellation without proper
synchronization techniques. However, even with the basic settings, you are still
expected to observe the transmit and receive spectrum, which is similar to the
following:

.. image:: ../images/ltespectrum.png
   :alt: LTEspectrum.png

Note that the bandwidth shown in the spectrum is approximately 10 MHz, which is
consistent with the "Channel bandwidth" setting of the model parameters.

Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   You can download the generated LTE data from below:

   - :dokuwiki:`lte_data.zip <_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/lte_data.zip>`

   It is in the same format as the data in previous sections.

.. [1]
   `Root-raised-cosine filter
   <https://en.wikipedia.org/wiki/Root-raised-cosine_filter>`_

.. [2]
   :ref:`ADI IIO Oscilloscope <iio-oscilloscope>`

.. [3]
   `Minimum-shift keying <https://en.wikipedia.org/wiki/Minimum-shift_keying>`_

.. [4]
   :mw:`LTE PHY Downlink with Spatial Multiplexing <help/lte/index.html>`
