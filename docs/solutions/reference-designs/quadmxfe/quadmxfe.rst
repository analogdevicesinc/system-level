.. _quadmxfe user-guide:

Quad-MxFE Prototyping Platform User Guide
=========================================

Features
--------

-  Multi-channel, wideband system development platform for the :adi:`AD9081` :adi:`MxFE™ <en/products/digital-to-analog-converters/high-speed-da-converters/mixed-signal-frontends.html>`
-  Mates with Xilinx :xilinx:`VCU118` Evaluation Board (Not Included)
-  16x RF Receive (Rx) Channels (32x Digital Rx Channels)

   -  Total 16x 1.5GSPS to 4GSPS ADC
   -  48x Digital Down Converters (DDCs), Each Including Complex Numerically-Controlled Oscillators (NCOs)
   -  16x Programmable Finite Impulse Response Filters (pFIRs)

-  16x RF Transmit (Tx) Channels (32x Digital Tx Channels)

   -  Total 16x 3GSPS to 12GSPS DAC
   -  48x Digital Up Converters (DUCs) , Each Including Complex
      Numerically-Controlled Oscillators (NCOs)

-  Flexible Rx & Tx RF Front-Ends

   -  Rx: Filtering, Amplification, Digital Step Attenuation for Gain Control
   -  Tx: Filtering, Amplification

-  Multiple System Control and Analysis Tools

   -  IIO Oscilloscope GUI
   -  MATLAB Add-Ons & Example Scripts
   -  HDL and Embedded Software Solutions for JESD204b/JESD204c Bring-Up

-  Provided Application-Specific Examples

   -  Multi-Chip Synchronization for Power-Up Phase Determinism
   -  System-Level Amplitude/Phase Alignment Using NCOs
   -  Low-Latency ADC-to-DAC Loopback Bypassing JESD Interface
   -  pFIR Control for Broadband Channel-to-Channel Amplitude/Phase Alignment
   -  Fast-Frequency Hopping

-  On-Board Power Regulation from Single 12V Power Adapter (Included)
-  Flexible Clock Distribution

   -  On-Board Clock Distribution from Single External 500MHz Reference
   -  Support for External Converter Clock

--------------

General Description
-------------------

This user guide serves as the main source of information for system engineers and software developers using the Quad-MxFE System Evaluation Board, which contains four :adi:`AD9081` software defined, direct RF sampling transceivers, as well as associated RF front-end, clocking, and power circuitry. The target application is phased array radars, electronic warfare, and ground-based SATCOM, specifically a 16 transmit/16 receive channel direct sampling phased array at L/S/C band (0.1 GHz to ~5GHz). The Rx & Tx RF front-end has drop-in configurations that allow for customized frequency ranges, depending on the user’s application.

The Quad-MxFE System Evaluation Board highlights a complete system solution. It is intended as a testbed for demonstrating multi-chip synchronization as well as implementation of system level calibrations, beam forming algorithms, and other signal processing algorithms. The board is designed to mate with a :xilinx:`VCU118` Evaluation Board from Xilinx®, which features the Virtex® UltraScale+™ XCVU9P FPGA, with provided reference software and HDL code.

High-Level Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quadmxfe_highlevelblockdiagram.png
   :width: 1000

System Integration
~~~~~~~~~~~~~~~~~~

Below is the full integrated system including the :xilinx:`VCU118`, ADQUADMXFE1EBZ, and :ref:`ADQUADMXFE-CAL <quadmxfe calboard>` in full operation.

.. image:: images/quadfull_edit.jpg

Key Component Locations
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quad_mxfe_labels_top.jpg

.. image:: images/quad_mxfe_labels_bottom.jpg

LED Status Indicators
~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quadfullleds.jpg
   :align: center

-  :ref:`Quad MxFE Power (Green) LED Information <quadmxfe boardhardwaredetails>`
-  :ref:`Quad MxFE Clock (Blue) LED Information <quadmxfe boardhardwaredetails>`
-  :ref:`Calibration Board LED Information <quadmxfe calboard>`
-  `VCU118 LED Information (pg. 85) <https://docs.amd.com/v/u/en-US/ug1224-vcu118-eval-bd>`_

--------------

Related Documents
-----------------

Publications
~~~~~~~~~~~~

-  :adi:`Multichannel RF to Bits Development Platform <en/design-notes/multichannel-rf-to-bits-development-platform.html>`
-  :adi:`Power-Up Phase Determinism Using Multichip Synchronization Features in Integrated Wideband DACs and ADCs <en/technical-articles/power-up-phase-determinism-using-multichip-synchronization.html>`
-  :adi:`Integrated Hardened DSP on DAC/ADC ICs Improves Wideband Multichannel Systems <en/technical-articles/integrated-hardened-dsp-on-dac-adc-ics-improves-wideband-multichannel-systems.html>`
-  :adi:`Multi-Channel System Improvements Using Hardened DSP in Digitizer ICs <en/education/education-library/webcasts/multi-channel-system-improvements-using-hardened-dsp-digitizer-ics.html>`
-  :adi:`Empirically Based Multichannel Phase Noise Model Validated in a 16-Channel Demonstrator <en/technical-articles/empirical-based-multichannel-phase-noise-model.html>`

Related Part Pages
~~~~~~~~~~~~~~~~~~

MxFE
^^^^

-  :adi:`AD9081 <en/products/ad9081.html>`
-  :adi:`AD9082 <en/products/ad9082.html>`
-  :ref:`AD9081/AD9082 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide <ad9081 quickstart zcu102>`
-  :adi:`UG-1578 User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`

ADF4371
^^^^^^^

-  :adi:`ADF4371 <en/products/adf4371.html>`
-  :external+linux:ref:`ADF4371 IIO Wideband Synthesizer Linux Driver <adf4371>`

HMC7043
^^^^^^^

-  :adi:`HMC7043 <en/products/hmc7043.html>`
-  :external+linux:ref:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <hmc7044>`

LTM4633
^^^^^^^

-  :adi:`LTM4633 <en/products/ltm4633.html>`

LTM8063
^^^^^^^

-  :adi:`LTM8063 <en/products/ltm8063.html>`

LTM8053
^^^^^^^

-  :adi:`LTM8053 <en/products/ltm8053.html>`

FPGA Evaluation Board Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :xilinx:`Xilinx Virtex UltraScale+ FPGA VCU118 <VCU118>`

--------------

Questions
---------

For additional questions or support, please visit the Engineering Zone forum at :ez:`adef-system-platforms/ <adef-system-platforms>`.
