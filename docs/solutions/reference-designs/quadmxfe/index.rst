.. _quadmxfe:

AD-QUADMXFE1-EBZ
===============================================================================

Quad-MxFE System Development Platform: Four :adi:`AD9081` MxFE™ Direct RF
Sampling Transceivers, 16Tx/16Rx Channels.

.. image:: images/adquadmxfe1ebztop-web.gif
   :align: left
   :width: 250

Overview
-------------------------------------------------------------------------------

The :adi:`ADQUADMXFE1EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>`
is a multi-channel, wideband system development platform featuring four
:adi:`AD9081` MxFE™ software-defined, direct RF sampling transceivers, along
with associated RF front-ends, clocking, and power circuitry. It delivers
16 transmit and 16 receive RF channels (32 digital channels each), exploiting
the :adi:`AD9081`'s 12 GSPS DAC and 4 GSPS ADC cores.

The platform mates with the :xilinx:`VCU118` Evaluation Board featuring the
Virtex® UltraScale+™ XCVU9P FPGA and targets phased array radar, electronic
warfare, and ground-based SATCOM applications at L/S/C band (0.1 GHz to
~5 GHz). An optional :ref:`16Tx/16Rx Calibration Board (ADQUADMXFE-CAL)
<quadmxfe calboard>` enables system-level calibration algorithm development.

Features:

- 4x :adi:`AD9081` MxFE™ transceivers — 16x RF Tx and 16x RF Rx channels
- 48x Digital Up Converters (DUCs) with complex NCOs
- 48x Digital Down Converters (DDCs) with complex NCOs
- 16x Programmable Finite Impulse Response Filters (pFIRs) on Rx
- Flexible Rx & Tx RF front-ends (filtering, amplification, digital step attenuation)
- JESD204B/C interface support (up to 24.75 Gbps/lane)
- Multi-chip synchronization (MCS) for power-up phase determinism
- Flexible clock distribution from single external 500 MHz reference
- On-chip PLL support (Rev. C)
- On-board power regulation from single 12V supply

Applications:

- Phased array radar, electronic warfare (EW), and SATCOM (ADEF)
- Multi-band 5G and mmWave communications infrastructure
- Electronic test and measurement
- Wideband, multi-channel direct RF sampling systems

.. image:: images/quadmxfe_highlevelblockdiagram.png
   :align: center
   :width: 700

.. toctree::
   :hidden:

   quadmxfe
   boardhardwaredetails
   calboard
   multichipsynchronization
   quick-start
   quickbringup

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Quad-MxFE User Guide <quadmxfe user-guide>` — system overview, block diagram,
      features, and related documents
   #. :ref:`Board Hardware Details <quadmxfe boardhardwaredetails>` — Tx/Rx signal
      paths, clocking architecture, JESD interface, and power distribution
   #. :ref:`Calibration Board (ADQUADMXFE-CAL) <quadmxfe calboard>` — 16Tx/16Rx
      splitter/combiner, loopback paths, and power analysis add-on
   #. :ref:`Multi-Chip Synchronization Guide <quadmxfe multichipsynchronization>` — MCS
      theory, One-Shot Sync, NCO Master-Slave Sync, and PLL phase adjustment
   #. Getting started:

      #. :ref:`Quick Start: Physical Setup <quadmxfe quickbringup>` — equipment list,
         fan/heat-sink installation, IIO Oscilloscope, MATLAB, and XSCT
      #. :ref:`Quick Start: Software & Bitstreams <quadmxfe quick-start>` —
         JESD204B/C testcases, boot files, device trees, and IIO bring-up

Videos
-------------------------------------------------------------------------------

- :adi:`Quad MxFE Product Video <en/education/education-library/videos/6184061669001.html>`
- :adi:`Quad MxFE Unboxing Video <en/education/education-library/videos/6257116746001.html>`
- :adi:`Calibration Board Unboxing <en/education/education-library/videos/6257116696001.html>`

Publications
-------------------------------------------------------------------------------

- :adi:`Multichannel RF to Bits Development Platform <en/design-notes/multichannel-rf-to-bits-development-platform.html>`
- :adi:`Power-Up Phase Determinism Using Multichip Synchronization Features in Integrated Wideband DACs and ADCs <en/technical-articles/power-up-phase-determinism-using-multichip-synchronization.html>`
- :adi:`Integrated Hardened DSP on DAC/ADC ICs Improves Wideband Multichannel Systems <en/technical-articles/integrated-hardened-dsp-on-dac-adc-ics-improves-wideband-multichannel-systems.html>`
- :adi:`Multi-Channel System Improvements Using Hardened DSP in Digitizer ICs <en/education/education-library/webcasts/multi-channel-system-improvements-using-hardened-dsp-digitizer-ics.html>`
- :adi:`Empirically Based Multichannel Phase Noise Model Validated in a 16-Channel Demonstrator <en/technical-articles/empirical-based-multichannel-phase-noise-model.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
