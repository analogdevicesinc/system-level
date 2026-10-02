.. _quadmxfe:

AD-QUADMXFE1-EBZ
===============================================================================

Quad-MxFE System Development Platform: Four :adi:`AD9081` MxFE™ Direct RF
Sampling Transceivers, 16Tx/16Rx Channels.

.. image:: images/adquadmxfe1ebztop-web.gif
   :align: center
   :width: 250

Overview
-------------------------------------------------------------------------------

The :adi:`ADQUADMXFE1EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>`
is a multi-channel, wideband system development platform featuring four
:adi:`AD9081` MxFE™ software-defined, direct RF sampling transceivers, along
with associated RF front-ends, clocking, and power circuitry. It delivers
16 transmit and 16 receive RF channels (32 digital channels each), exploiting
the :adi:`AD9081`'s 12 GSPS DAC and 4 GSPS ADC cores.

The platform highlights a complete system solution. It is intended as a testbed
for demonstrating multi-chip synchronization as well as the implementation of
system level calibrations, beamforming algorithms, and other signal processing
algorithms. The system is designed to mate with a :xilinx:`VCU118` Evaluation
Board (not included) from AMD Xilinx, which features the Virtex® UltraScale+™
XCVU9P FPGA, with provided reference software, HDL code, and MATLAB
system-level interfacing.

The Rx & Tx RF front-end has drop-in configurations that allow for customized
frequency ranges, depending on the user's application, covering L/S/C band
(0.1 GHz to ~5 GHz).

In addition to the Quad-MxFE Digitizing Card, the kit also contains a
:ref:`16Tx/16Rx Calibration Board (ADQUADMXFE-CAL) <quadmxfe calboard>` that is
used to develop system-level calibration algorithms, or otherwise more easily
demonstrate power-up phase determinism. The Calibration Board also allows the
user to demonstrate combined-channel dynamic range, spurious, and phase noise
improvements and can be controlled via a free MATLAB add-on when connected to
the PMOD interface of the :xilinx:`VCU118`.

Features:

- Multi-channel, wideband system development platform for the :adi:`AD9081`
  MxFE™
- Mates with :xilinx:`VCU118` Evaluation Board (not included)
- 16x RF Receive (Rx) Channels (32x Digital Rx Channels)

  - Total 16x 1.5GSPS to 4GSPS ADC
  - 48x Digital Down Converters (DDCs), each including complex NCOs
  - 16x Programmable Finite Impulse Response Filters (pFIRs)

- 16x RF Transmit (Tx) Channels (32x Digital Tx Channels)

  - Total 16x 3GSPS to 12GSPS DAC
  - 48x Digital Up Converters (DUCs), each including complex NCOs

- Flexible Rx & Tx RF front-ends

  - Rx: Filtering, amplification, digital step attenuation for gain control
  - Tx: Filtering, amplification

- Multiple system control and analysis tools

  - :ref:`IIO Oscilloscope <quadmxfe iio-oscilloscope>` GUI
  - MATLAB add-ons & example scripts
  - HDL and embedded software solutions for JESD204B/JESD204C bring-up

- JESD204B/C interface support (up to 24.75 Gbps/lane)
- On-chip PLL support (Rev. C)
- On-board power regulation from single 12V power adapter (included)
- Flexible clock distribution

  - On-board clock distribution from single external 500 MHz reference
  - Support for external converter clock

Applications:

- Phased array radar, electronic warfare (EW), and SATCOM (ADEF)
- Communications infrastructure (multiband and mmWave 5G)
- Electronic test and measurement
- Multi-chip synchronization for power-up phase determinism
- System-level amplitude/phase alignment using NCOs
- Low-latency ADC-to-DAC loopback bypassing JESD interface
- pFIR control for broadband channel-to-channel amplitude/phase alignment
- Fast-frequency hopping

High-level block diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quadmxfe_highlevelblockdiagram.png
   :align: center
   :width: 700

System integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is the full integrated system including the :xilinx:`VCU118`,
ADQUADMXFE1EBZ, and :ref:`ADQUADMXFE-CAL <quadmxfe calboard>` in full
operation.

.. image:: images/quadfull_edit.jpg

Key component locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quad_mxfe_labels_top.jpg

.. image:: images/quad_mxfe_labels_bottom.jpg

LED status indicators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/quadfullleds.jpg
   :align: center

- :ref:`Quad MxFE Power (Green) LED Information <quadmxfe boardhardwaredetails>`
- :ref:`Quad MxFE Clock (Blue) LED Information <quadmxfe boardhardwaredetails>`
- :ref:`Calibration Board LED Information <quadmxfe calboard>`
- `VCU118 LED Information (pg. 85) <https://docs.amd.com/v/u/en-US/ug1224-vcu118-eval-bd>`_

.. toctree::
   :hidden:

   prerequisites
   boardhardwaredetails
   calboard
   multichipsynchronization
   quickstart/index
   iio-oscilloscope

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`Help and Support <quadmxfe help-and-support>`, but before that, please
make sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <quadmxfe prerequisites>` — what you need to get
      started with the setup
   #. :ref:`Board Hardware Details <quadmxfe boardhardwaredetails>` — Tx/Rx signal
      paths, clocking architecture, JESD interface, and power distribution
   #. :ref:`Calibration Board (ADQUADMXFE-CAL) <quadmxfe calboard>` — 16Tx/16Rx
      splitter/combiner, loopback paths, and power analysis add-on
   #. :ref:`Multi-Chip Synchronization Guide <quadmxfe multichipsynchronization>` —
      MCS theory, One-Shot Sync, NCO Master-Slave Sync, and PLL phase adjustment
   #. :ref:`Quick start guides <quadmxfe quickstart>`:

      #. Using the :ref:`VCU118/Virtex UltraScale+ <quadmxfe quickstart vcu118>`
      #. :ref:`Bring-up guide <quadmxfe quickbringup>` — software setup, power-up
         sequence, FPGA programming, and MATLAB control

   #. :ref:`IIO Oscilloscope & Software <quadmxfe iio-oscilloscope>` — software
      architecture, IIO device mapping, GUI usage, and IIO commands

#. Design with the :adi:`AD9081`

   - :adi:`AD9081 product page <en/products/ad9081.html>`
   - :adi:`UG-1578 User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`

   - HDL reference designs:

     - :external+hdl:ref:`ADQUADMXFE1EBZ HDL project <ad_quadmxfe1_ebz>`
     - :external+hdl:ref:`QUAD-QUAD-MXFE HDL project <quad_quad_mxfe>`

   - Resources for designing a custom platform:

     #. Linux drivers:

        - :external+linux:ref:`AD9081 MxFE Linux Driver <ad9081>`
        - :external+linux:ref:`ADF4371 IIO Wideband Synthesizer Linux Driver <adf4371>`
        - :external+linux:ref:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <hmc7044>`
        - :external+linux:ref:`HMC425A Digital Step Attenuator Linux Driver <hmc425a>`
        - :external+linux:ref:`AXI ADC HDL Linux Driver <axi-adc-hdl>`
        - :external+linux:ref:`AXI DAC HDL Linux Driver <axi-dac-dds-hdl>`
        - :external+linux:ref:`AXI DMA Controller Linux Driver <axi-dmac>`

     #. About the JESD204 utilities:

        - :external+linux:ref:`jesd204-fsm-framework`
        - :dokuwiki:`JESD204 status utility <resources/tools-software/linux-software/jesd_status>`
        - :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`
        - :external+hdl:ref:`jesd204`

#. :adi:`UG-1578, Device User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
#. :ref:`Help and Support <quadmxfe help-and-support>`

Related part pages
-------------------------------------------------------------------------------

- :adi:`AD9081 <en/products/ad9081.html>` — MxFE transceiver
- :adi:`ADF4371 <en/products/adf4371.html>` — wideband synthesizer
- :adi:`HMC7043 <en/products/hmc7043.html>` — clock jitter attenuator
- :adi:`LTM4633 <en/products/ltm4633.html>` — triple output DC/DC module
- :adi:`LTM8063 <en/products/ltm8063.html>` — silent switcher DC/DC module
- :adi:`LTM8053 <en/products/ltm8053.html>` — silent switcher DC/DC module
- :xilinx:`Xilinx Virtex UltraScale+ FPGA VCU118 <VCU118>`

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

.. _quadmxfe help-and-support:

Help and Support
-------------------------------------------------------------------------------

For additional questions or support, please visit the Engineering Zone forum at
:ez:`adef-system-platforms/ <adef-system-platforms>`.
