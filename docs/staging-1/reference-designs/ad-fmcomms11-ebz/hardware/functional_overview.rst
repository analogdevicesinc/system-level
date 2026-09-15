.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms11-ebz/hardware/functional_overview

.. _ad-fmcomms11-ebz hardware functional_overview:

AD-FMCOMMS11-EBZ Functional Overview
====================================

A functional block diagram of the system is given below. The system consists of
two transmit paths, receive paths, clock management and power supply.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/system_block_diagram.png

Transmit
--------

Key component:

   * - :adi:`AD9162`
     - The AD9162 is a high performance, 16-bit digital-to-analog converter
       (DAC) that supports data rates to 6 GSPS. The DAC core is based on a
       quad-switch architecture coupled with a 2× interpolator filter that
       enables an effective DAC update rate of up to 12 GSPS in some modes. The
       high dynamic range and bandwidth makes these DACs ideally suited for the
       most demanding high speed radio frequency (RF) DAC applications.

   * - :adi:`ADL5240`
     - The ADL5240 is a high performance, digitally controlled variable gain
       amplifier (VGA) operating from 100 MHz to 4000 MHz. The VGA integrates a
       high performance, 20 dB gain, internally matched amplifier (AMP) with a
       6-bit digital step attenuator (DSA) that has a gain control range of 31.5
       dB in 0.5 dB steps with ±0.25 dB step accuracy. The attenuation of the
       DSA can be controlled using a serial or parallel interface.

Receive
-------

Key component:

   * - :adi:`AD9625`
     - The AD9625 is a 12-bit monolithic sampling analog-to-digital converter
       (ADC) that operates at conversion rates of up to 2.6 giga samples per
       second (GSPS). This product is designed for sampling wide bandwidth
       analog signals up to the second Nyquist zone. The combination of wide
       input bandwidth, high sampling rate, and excellent linearity of the
       AD9625 is ideally suited for spectrum analyzers, data acquisition
       systems, and a wide assortment of military electronics applications, such
       as radar and jamming/antijamming measures.

   * - :adi:`HMC1119`
     - The HMC1119 is a broadband, highly accurate, 7-bit digital attenuator,
       operating from 0.1 GHz to 6.0 GHz with 31.5 dB attenuation control range
       in 0.25 dB steps.

Clock
-----

Key component:

   * - :adi:`ADF4355`
     - The ADF4355 allows implementation of fractional-N or integer-N
       phase-locked loop (PLL) frequency synthesizers when used with an external
       loop filter and an external reference frequency. A series of frequency
       dividers permits operation from 54 MHz to 6800 MHz.It has an integrated
       VCO with a fundamental output frequency ranging from 3400 MHz to 6800
       MHz. In addition, the VCO frequency is connected to divide by 1, 2, 4, 8,
       16, 32, or 64 circuits that allow the user to generate radio frequency
       (RF) output frequencies as low as 54 MHz. For applications that require
       isolation, the RF output stage can be muted. The mute function is both
       pin and software controllable.

   * - :adi:`HMC361`
     - The HMC361S8G(E) is a low noise Divide-by-2 Static Divider with InGaP
       GaAs HBT technology in an 8 lead surface mount plastic package. This
       device operates from DC (with a square wave input) to 10 GHz input
       frequency with a single +5.0V DC supply. The low additive SSB phase noise
       of -148 dBc/Hz at 100 kHz offset helps the user maintain good system
       noise performance.

Power
-----

Key component:

   * - :adi:`ADM7170`
     - 6.5 V, 500 mA, Ultralow Noise, High PSRR, Fast Transient Response CMOS
       LDO
   * - :adi:`ADM7150`
     - 800 mA, Ultra Low Noise/High PSRR LDO
   * - :adi:`ADM7154`
     - 600 mA, Ultralow Noise, High PSRR, RF Linear Regulator
   * - :adi:`ADM1184`
     - 0.8% Accurate Quad Voltage Monitor
   * - :adi:`ADP1740`
     - 2 A, Low VIN Dropout, Linear Regulator
   * - :adi:`ADP1761`
     - 1 A, Low VIN, Low Noise, CMOS Linear Regulator
   * - :adi:`ADP2370`
     - High Voltage, 1.2 MHz/600 kHz, 800 mA, Low Quiescent Current Buck
       Regulator
   * - :adi:`ADP5073`
     - 1.2 A, DC-to-DC Inverting Regulator
   * - :adi:`ADP2165`
     - 5.5 V, 5 A, High Efficiency, Step-Down DC-to-DC Regulators with Output
       Tracking
   * - :adi:`ADP196`
     - 5 V, 3 A Logic Controlled High-Side Power Switch
   * - :adi:`ADP1741`
     - 2 A, Low VIN, Dropout, CMOS Linear Regulator
   * - :adi:`ADP2384`
     - 20 V, 4 A, Synchronous Step-Down DC-to-DC Regulator
   * - :adi:`ADP7182`
     - –28 V, −200 mA, Low Noise, Linear Regulator

Power Level Monitoring
----------------------

Key component:

   * - :adi:`AD7291`
     - 8-Channel, I2C, 12-Bit SAR ADC with Temperature Sensor
