AD-FMCOMMS4-EBZ Functional Overview
===================================

A functional block diagram of the system is given below. The system consists of
four functional partitions - receive path, transmit path, clocking and power
supply. As mentioned earlier, the data path is fully integrated into AD9364. The
key features of receive and transmit paths are listed below. Please refer to the
device data sheet for more details.

.. image:: ../images/cf_ad9361_zc706_bd.jpg
   :width: 500

AD9364
------

Receive
~~~~~~~

-  Supports 1 direct conversion RF receive channels
-  Fully integrated synthesizers (including loop filter)
-  Data path consists of LNA, Demodulator, LPF, ADC and digital filters
-  AGC, Quadrature calibration and DC offset calibration
-  NF: 2.5dB @1GHz
-  ADC: Continuous time sigma-delta, 640MSPS
-  Digital Filters: 128 complex taps, decimation between 2 and 48
-  Gain: 1dB step size, 80dB analog range, 30dB digital range (post ADC scaling)
-  On-chip sensor for temperature-corrected RSSI

Transmit
~~~~~~~~

-  Supports 1 direct conversion RF receive channels
-  Fully integrated synthesizers (including loop filter)
-  Data path consists of digital filters, DAC and Modulators
-  Digital Filters: 128 complex taps, interpolation between 2 and 48
-  Gain: 0.25dB step size, 86dB range.
-  DAC: 320MSPS

Clocking
~~~~~~~~

The clocks are managed by the device and are software programmable. Please refer
to the device data sheet for the various clocks within the device. The board
provides a 40MHz crystal for the AD9364.

SPI
~~~

The SPI signals are directly passed to the FMC connector.

Control/Monitor
~~~~~~~~~~~~~~~

The device allows real-time control via dedicated pins. These signals are passed
to the FMC connector. The functionality of these pins are programmable and
includes gain, synchronization, state machine control etc. Please refer to the
data sheet for more details.

The device also allows real-time monitoring of internal signals via another set
of dedicated pins. Again, these signals are passed to the FMC connector. The
internal signals are multiplexed into these pins- and details of which are best
described in the data sheet.

Power
-----

Key components:

+----------------+-----------------------------------------------------------+
| :adi:`ADP1755` | Low dropout, linear regulator, 1.2A, 1.6 to 3.6V          |
+----------------+-----------------------------------------------------------+
| :adi:`ADP2164` | High Efficiency, Step-Down, DC-to-DC Regulator, 6.5V, 4 A |
+----------------+-----------------------------------------------------------+

The board receives all the power from the FPGA board through FMC.
