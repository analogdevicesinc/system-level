.. _xbdp:

X-Band Phased Array Development Platform
===============================================================================

Overview
-------------------------------------------------------------------------------

The :adi:`X-Band Development Platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/x-band-development-platform.html>`
contains one :adi:`AD9081-FMCA-EBZ <eval-ad9081>` AD9081 MxFE Evaluation Board,
one :ref:`xud1a`, and one :ref:`stingray`. The target application is phased
array radars, electronic warfare, and ground-based SATCOM, specifically an X Band
32 transmit/32 receive channel hybrid beamforming phased array.

The X-Band Development Platform highlights a complete system solution. It is
intended as a testbed for demonstrating hybrid beamforming phased array radar as
well as the implementation of system level calibrations, beamforming algorithms,
and other signal processing algorithms. The system is designed to mate with a
:xilinx:`ZCU102` Evaluation Board from AMD Xilinx®, featuring the Zynq® UltraScale+™
ZU9EG FPGA, with provided reference software, HDL code, and MATLAB system-level
interfacing.

.. image:: images/xbdp-system-block-diagram.png
   :width: 800

The system can be used to enable quick time-to-market development programs for
applications like:

-  ADEF (Phased-Array, RADAR, EW, SATCOM)
-  Hybrid Beamforming
-  Electronic Test and Measurement

Features:

- ADAR1000EVAL1Z (Stingray) X/Ku-Band Analog Beamforming Front-End

   -  32 Channel Analog Phased Array Prototyping Platform
   -  8x ADAR1000 Analog Phased Array Beamforming ICs
   -  32x ADTR1107 Transmit/Receive ICs
   -  RF In, RF Out Design
   -  Individual RFIO for each BFIC
   -  10 GHz Lattice Spacing
   -  Stand-Alone RF Detector/ADC Combo for Calibration
   -  PMOD and SDP Connectors for Programming
   -  On-Board Power Regulation from Single 12V Power Adapter (Included)

- ADXUD1AEBZ X/C Band Up/Down Converter

   -  X Band (RF) to C Band (IF) up/down converter
   -  4 Tx/Rx RF Input/Output via SMA
   -  4 Tx IF Inputs via SMPM
   -  4 Rx IF Output via SMPM
   -  External LO or Internal pll Options
   -  PMOD Connector for Programming
   -  Interposer Board via PMOD to allow SDP and FMC Connectors for Programming
   -  On-Board Power Regulation from Single 12V Power Adapter (Included)

- AD9081-FMCA-EBZ MxFE Evaluation Board

   -  Mates with AMD Xilinx ZCU102 Evaluation Board (Not Included)

      -  On-Board Power Regulation Powered by ZCU102 Evaluation Board via FMC Connector

   -  4x RF Receive (Rx) Channels (8x Digital Rx Channels)
   -  Total 4x 12-bit 4GSPS ADC
   -  8x Digital Down Converters (DDCs), Each Including Complex Numerically-Controlled Oscillators (NCOs)
   -  8x Programmable Finite Impulse Response Filters (pFIRs)
   -  4x RF Transmit (Tx) Channels (8x Digital Tx Channels)
   -  Total 4x 16-bit 12GSPS DAC
   -  8x Digital Up Converters (DUCs), Each Including Complex Numerically-Controlled Oscillators (NCOs)
   -  Flexible Clock Distribution

      -   On-Board Clock Distribution from Single External 100MHz Reference
      -   Support for External Converter Clock

Table of contents
-------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 2

   quickstart/index
   hardware
   software
   xud1a
   stingray

Related Documents
-------------------------------------------------------------------------------

Publications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`Hybrid Beamforming Receiver Dynamic Range Theory to Practice <en/technical-articles/hybrid-beamforming-receiver-dynamic-range.html>`
-  :adi:`Hybrid Beamforming Transmit Calibration with SFDR Optimization <en/resources/technical-articles/hybrid-beamforming-transmit-calibration-with-sfdr-optimization.html>`
-  :adi:`Over-the-Air Pattern Measurements for Hybrid Beamforming Phased Array <en/resources/technical-articles/over-the-air-pattern-measurements-for-hybrid-beamforming-phased-array.html>`

Related Part Pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MxFE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :adi:`AD9081 </en/products/ad9081.html>`
-  :doc:`AD9081/AD9082 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </solutions/reference-designs/eval-ad9081/quickstart/zcu102>`
-  :adi:`UG-1578 User Guide </media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`

ADXUD1AEBZ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :ref:`ADXUD1AEBZ <xud1a>`

ADAR1000EVAL1Z
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :ref:`ADAR1000EVAL1Z <stingray>`

FPGA Evaluation Board Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :xilinx:`Zynq UltraScale+ FPGA ZCU102 <ZCU102>`

Help and Support
-------------------------------------------------------------------------------

For additional questions or support, please visit the Engineering Zone forum at
:ez:`ADEF <adef-system-platforms>`.
