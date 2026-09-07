.. imported from: https://wiki.analog.com/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/digitizer-overview

.. _ad9081 2to24ghz-mxfe-rf-front-end digitizer-overview:

Digitizer Overview
===============================================================================

The :adi:`AD9081` or :adi:`AD9082` ("MxFE") are ideal digitizers for this
wideband RF front end due to their high level of integration, performance,
and RF sampling rates. The MxFE's high instantaneous and analog input
bandwidth enable RF sampling up to 8 GHz, providing architectural and
frequency planning flexibility at the system level. They also have highly
configurable, on-chip DSP capabilities (DDC/DUC channelizers, NCOs, and
programmable FIR filters) as well as four DAC channels and two-to-four
ADCs for use in multi-channel systems. 

.. list-table::
   :header-rows: 1

   - - Part number
     - Nb. of ADCs/DACs
     - ADC max. sample rate
     - DAC max. sample rate
   - - :adi:`AD9081`
     - 4 ADCs/4 DACs
     - 4 GSPS
     - 12 GSPS
   - - :adi:`AD9082`
     - 2 ADCs/2 DACs
     - 6 GSPS
     - 12 GSPS

The ADI Frequency Planning Utility tool was used to determine the optimal
:adi:`AD9082` ADC sample rate, IF sampling frequency, and IF bandwidth.
A 6 GSPS ADC rate allows for maximum instantaneous bandwidth (IBW) and complete
avoidance of HD2 aliasing in-band for a 1GHz signal bandwidth centered at 4.5 GHz
(2nd Nyquist). The figure below illustrates this. 

.. figure:: ../images/ad9082_freq_folding_graphic.png
   :align: center
   :width: 600

   AD9082 frequency folding at a 6 GSPS ADC sample rate
          

.. important::

   The receiver and transmitter front ends described in this CN use a frequency
   plan designed using the :adi:`AD9082`, specifically with 6 GSPS and 12 GSPS
   ADC and DAC sample rates, respectively. However, the RF components themselves
   are wideband enough to allow for flexibility in the frequency plan and
   filtering, which can be adjusted to work with the lower ADC sample rates.

The :adi:`ADF4377` integrated PLL/VCO is an ideal choice for generating the
MxFE sample clock. The :adi:`ADF4377` can generate a clean, low-jitter clock
from 800 MHz up to 12.8 GHz, and it's differential outputs are capable of
directly driving the MxFE clock pins.    
