.. _quadmxfe calboard:

Calibration Board
=================

Splitter/Combiner, Calibration, Power Analyzer
----------------------------------------------

.. image:: images/adquadmxfe-calangle-web.gif
   :align: center

Features
--------

-  Mates to Quad-MxFE Digitizing Card & VCU118 PMOD Interface (Cable Included)
-  MATLAB Control Enables System-Level Calibration Algorithm Development
-  Provides Both Individual Adjacent Channel Loopback and Combined Channel Loopback Options
-  Combined Tx Channels Out Via SMA Option
-  Combined Rx Channels In Via SMA Option
-  On-Board Log Power Detectors With AD5592R Output To VCU118 Over PMOD
-  On-Board Power Regulation from Single 12V Power Adapter (Included)

Below is the full integrated system including the Xilinx :xilinx:`VCU118`, ADQUADMXFE1EBZ, and :ref:`ADQUADMXFE-CAL <quadmxfe calboard>` in full operation. For LED identification please see `LED Identification`_.

.. image:: images/quadfull_edit.jpg

--------------

General Description
-------------------

This page serves to inform system engineers and software developers about the calibration board addition kit that pairs with the :adi:`Quad-MxFE <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>`. This board directly aligns with the 16 Rx and 16 Tx ports on the output of the Quad MxFE and includes power detectors and loopback configurations for the system-level calibration of the Quad MxFE. The board contains a PMOD 2A interface that connects the :xilinx:`VCU118` Evaluation Board from Xilinx®. A DIP switch and multi-channel ADC/DAC, :adi:`AD5592R`, are also included for additional control and power readings. The goal of this kit is to enable users to demonstrate combined-channel dynamic range, spurious, and phase noise improvements, develop system-level calibration algorithms, and demonstrate immediate phase determinism.

High Level Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/blckdiagram_edit.png
   :align: center
   :width: 600

Key Component Location
~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/cal_brd_labels.png

.. image:: images/cal_brd_labels2.png

LED Identification
~~~~~~~~~~~~~~~~~~

LED Status Indicators

====== =============================================
LED    Function
====== =============================================
DS601  ``1.9V @ 1.2mA`` Good From ADM7150 (LDO)
DS602  ``1.9V @ 1.2mA`` Good From ADM7150 (LDO)
DS603  ``3.3V_FPGA`` Good From VCU118 PMOD 2A
====== =============================================

Equipment Needed
----------------

-  PMOD Cable

   -  `Cable Assembly <https://www.samtec.com/products/idsd-06-d-15.00>`__

-  12V (150W) Wall Supply

   -  `Power Brick Assembly <https://www.digikey.com/TE150A1251F01>`_

-  2x SMA Cables (50 Ω)
-  MMCX to SMA cables
-  MMCX to MMCX cables

   -  `Cable Assembly <https://www.samtec.com/products/rf316-03sp1-03sp1-0100>`_

-  Board Standoffs

   -  `Standoff Assembly <https://www.mcmaster.com/catalog/127/3467/>`_

-  Static Shielding Bag
-  Packaging (Box, Foam)
-  Startup Documentation
-  VCU118 FPGA Board (optional)

   -  :xilinx:`VCU118`

-  Quad MxFE Board (optional)

   -  :adi:`Quad MxFE <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>`

--------------

Control Interfaces
------------------

The calibration board can be controlled in multiple ways including a DIP Switch and 2A PMOD Interface. The board can be controlled with 4 main signals: 5045 V1 and 5045 V2 which control an ADRF5045 which switches the transmit path between combined loopback, low frequency path, high frequency path, and power detection path, CTLR IND which turns off and on adjacent individual loopback for each Rx and Tx channel, and CTRL RX COMB which turns off and on the combined receive loopback path. The DIP Switch controls 4 signals: 5045 V1, 5045 V2, CTRL IND, and CTRL RX COMB. The PMOD Interface has 8 signals: 5045 V1, 5045 V2, CTRL IND, CTRL RX COMB, and 4 SPI Communications signals. The AD5592R is an 8 channel GPIO/ADC/DAC and it is connected the same control signals as the DIP switch as well as the three power detectors (:adi:`AD8318 <en/products/ad8318.html>`, :adi:`HMC948 <en/products/hmc948.html>`, :adi:`LTC5596 <en/products/ltc5596.html>`), plus a temperature sensor on the AD8318. Below is a tabular representation of these control signals.

.. image:: images/capture.png
   :width: 400

Software Needed
---------------

The following link contains the MATLAB driver for controlling the 16 Tx / 16 Rx Calibration board via the VCU118 PMOD interface. The driver may be used to configure the Quad MxFE platform in a Combined Loopback, Individual Loopback, Combined Tx to SMA, Combined Rx from SMA, Combined Tx Power reading, and Power readings from the :adi:`AD5592R <en/products/ad5592r.html>` and subsequent (:adi:`AD8318 <en/products/ad8318.html>`, :adi:`HMC948 <en/products/hmc948.html>`, :adi:`LTC5596 <en/products/ltc5596.html>`).

-  :ref:`Cal Board VCU118 PMOD <quadmxfe quickbringup>`

Related Documents
-----------------

Related Parts Pages
~~~~~~~~~~~~~~~~~~~

-  :adi:`AD5592R <ad5592r>` 8 Channel, 12-Bit, Configurable ADC/DAC with on-chip Reference, SPI interface
-  :adi:`HMC948 <hmc948>` 54 dB Logarithmic Detector SMT, 1 - 23 GHz
-  :adi:`LTC5596 <ltc5596>` 100MHz to 40GHz Linear-in-dB RMS Power Detector with 35dB Dynamic Range
-  :adi:`AD8318 <ad8318>` 1 MHz to 8 GHz, 70 dB Logarithmic Detector/Controller
-  :adi:`ADP5020 <adp5020>` Power Management Unit for Imaging Modules
-  :adi:`ADRF5045 <adrf5045>` SPDT RF Switch, 9 kHz to 13 GHz

Schematic
~~~~~~~~~

-  `ADQUADMXFE-CAL <resources/02-064888-01-b_2_.pdf>`_

