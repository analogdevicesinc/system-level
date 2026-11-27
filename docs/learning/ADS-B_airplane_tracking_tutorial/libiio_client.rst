ADS-B Example Using libiio
==========================

.. note::

   This page was migrated from the
   :dokuwiki:`ADI Wiki
   <resources/tools-software/linux-software/libiio/clients/adsb_example>`.

Overview
--------

This page documents an airplane tracking system using Automatic Dependent
Surveillance – Broadcast (ADS-B) signals. The technology allows aircraft to
broadcast their positions via satellite navigation at 1090 MHz, using the
AD-FMCOMMS3-EBZ RF transceiver board with MATLAB and Simulink.

Signal Characteristics
----------------------

-  Transmit Frequency: 1090 MHz
-  Modulation: Pulse Position Modulation (PPM)
-  Data Rate: 1 Mbit/s
-  Message Length: 56 μsec or 112 μsec
-  Error Detection: 24-bit CRC checksum

Requirements
------------

Software
~~~~~~~~

`MATLAB <https://www.mathworks.com/products/matlab/>`_ 2014b or later with:

-  `Communications System Toolbox
   <https://www.mathworks.com/products/communications/>`_
-  `DSP System Toolbox
   <https://www.mathworks.com/products/dsp-system/>`_
-  `Signal Processing Toolbox
   <https://www.mathworks.com/products/signal/>`_

For the Simulink version, additionally:

-  `Simulink <https://www.mathworks.com/products/simulink/>`_
-  `Stateflow <https://www.mathworks.com/products/stateflow/>`_
-  `LibIIO client for MATLAB & Simulink
   <https://wiki.analog.com/resources/tools-software/linux-software/libiio/
   clients/fmcomms2_3_simulink>`_

Hardware
~~~~~~~~

-  :adi:`AD-FMCOMMS3-EBZ` RF transceiver board
-  Xilinx development system (ZC706, ZC702, or Zedboard)
-  1090 MHz capable antenna (e.g.,
   `ADS-B Double 1/2 Wave Mobile Antenna
   <http://www.dpdproductions.com/page_vhf_air.html#adsmobilehalf>`_)
-  Recent Zynq Linux image for the board

MATLAB Implementation
---------------------

The ``ad9361_ModeS.m`` script performs three main operations:

1. Prepare the Mode S signal
2. Calculate the earth zone according to user input
3. Receive data via libiio and decode the ADS-B signals

The script supports two operating modes depending on how *TX_LO_FREQ* and
*RX_LO_FREQ* are configured.

Pre-captured Data
~~~~~~~~~~~~~~~~~

In this mode, the transmitter and receiver use matching local oscillator
frequencies for controlled testing. Any LO frequency supported by the board
is acceptable.

.. code-block:: matlab

   [rssi1,rssi2]=ad9361_ModeS('ip','pre-captured',channel);

For example, to receive pre-captured data on Channel 2:

.. code-block:: matlab

   [rssi1,rssi2]=ad9361_ModeS('192.168.10.2','pre-captured',2);

At the end of the simulation, RSSI values for both channels are shown in the
command window along with a result table listing decoded aircraft information:

.. figure:: images/result_libiio.png
   :width: 700

Live Data
~~~~~~~~~

In this mode, the receiver operates at 1090 MHz to capture real aircraft
signals. *TX_LO_FREQ* must be set far from 1090 MHz to avoid interference.
With a proper antenna, the system can decode signals from aircraft within
approximately 80 miles.

.. figure:: images/adsb_spec.png
   :width: 700
   :alt: ADS-B spectrum analyzer output

.. code-block:: matlab

   [rssi1,rssi2]=ad9361_ModeS('ip','live',channel);

The result table below shows decoded real-world aircraft information. With a
proper antenna, this model is able to capture and decode aircraft signals in
an 80 miles range with FMCOMMS3. Since there are two types of Mode S messages
(56 usec or 112 usec), some messages contain more information than others.

.. figure:: images/result_real.png
   :width: 700

Simulink Implementation
-----------------------

The Simulink model **ModeS_Simulink_libiio.slx** extends the original
MathWorks ADS-B example by adding an IIO System object block
(``iio_sys_obj``) for hardware-in-the-loop signal reception. The signal
detection and decoding subsystem is adapted directly from the MathWorks
reference implementation.

.. figure:: images/adsb_model.png
   :width: 700
   :alt: Simulink model with IIO System object

To make the original model compatible with the IIO System object (which
operates in buffer mode), two additional blocks are inserted:

-  *unbuffer* — converts the buffer output to frame size = 1
-  *rate transition* — adjusts sample time to 1

The model supports the same pre-captured and live data modes as the MATLAB
version. Output is displayed in text format in the command window (versus the
table format used in the MATLAB version):

.. figure:: images/fig13.png

Support
-------

For questions about FMCOMMS3, :adi:`AD9361`, or libiio, please ask on the
EngineerZone.
:ez:`ADI Support <microcontroller-no-os-drivers>`

For questions about the ADS-B algorithm, please contact MathWorks.
`MathWorks Support <https://www.mathworks.com/support/>`_
