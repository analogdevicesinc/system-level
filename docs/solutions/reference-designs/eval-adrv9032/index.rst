.. _adrv9032:

EVAL-ADRV9032
===============================================================================

Integrated 2T2R TDD and FDD RadioVerse Transceiver with Dual Observation Paths.

Overview
-------------------------------------------------------------------------------

.. image:: evaluation-board-angle.webp
   :align: right
   :width: 500

The :adi:`EVAL-ADRV903x <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adrv903x.html>`, is an FMC radio card
designed to showcase the :adi:`ADRV9032 <ADRV9032R>` and :adi:`ADRV9032R`, highly
integrated, radio frequency (RF) agile transceivers offering 2 independently
controlled transmitters, dual observation receiver inputs for monitoring
transmitter channels, 2 independently controlled receivers, integrated
local oscillator (LO) and clock synthesizers, and digital signal processing
functions providing a complete transceiver solution.

The device provides the high radio performance and low-power consumption
demanded by cellular infrastructure applications, software-defined radios,
portable instruments, and military communications.

Features:

- Both chips feature:

  - 2 differential transmitters & 2 differential receivers
  - 2 differential observation receivers
  - Support for TDD and FDD applications
  - LO tunable range: 450 MHz to 7125 MHz
  - RF range: 350 MHz to 7225 MHz
  - Maximum transmitter large-signal bandwidth: 200 MHz
  - Maximum transmitter synthesis bandwidth: 450 MHz
  - Maximum receiver signal bandwidth: 200 MHz
  - Maximum observation receiver signal bandwidth: 450 MHz
  - JESD204B and JESD204C digital interface: up to 16.5 Gbps
  - Low power consumption: 4.82 W for TDD mode with 200 MHz bandwidth

- Complete ADRV9032/ADRV9032R radio cards for evaluation

  - FMC connector for FPGA integration
  - Fully integrated fractional-N RF synthesizer
  - Fully integrated clock synthesizer
  - Dual external LO inputs supporting operation up to 6 GHz (ADRV9032R)

Applications:

- Software defined radios
- Portable instrumentation
- Military communications
- General-purpose radios
- Wireless infrastructure
- 3G/4G/5G TDD and FDD base stations

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   ram-capture

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`ADRV9032 <ADRV9032R>` / :adi:`ADRV9032R`, we recommend to use
the :adi:`EVAL-ADRV903x <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/eval-adrv903x.html>` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <adrv9032 prerequisites>` - what you need to get started
   #. :ref:`Quick start guides <adrv9032 quickstart>`:

      #. Using the :ref:`ZCU102/Zynq UltraScale+ MP SoC <adrv9032 quickstart zcu102>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :ref:`RAM Capture <adrv9032 ram-capture>`

#. Design with the ADRV9032/ADRV9032R

   - :ref:`adrv9032 block-diagram`

     - :adi:`ADRV9032R product page <ADRV9032R>`
     - :adi:`Full data sheet and chip design package <en/products/adrv9032r.html>`

   - Hardware in the Loop / How to design your own custom BaseBand

     - :ref:`GNU Radio <software gnuradio>`
     - :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   - Resources for designing a custom ADRV9032/ADRV9032R-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`axi_jesd204_tx`
           - :external+linux:ref:`axi_jesd204_rx`
           - :external+hdl:ref:`axi_adxcvr`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dac-dds-hdl`
           - :external+linux:ref:`ad9528`
           - :external+linux:ref:`axi-dac-dds-hdl`
           - ADRV9032/ADRV9032R Linux device driver (in-tree at :git-linux:`main:drivers/iio/trx-rf/adrv903x/adrv903x.c`)

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

        #. About the JESD204 utilities:

           - :external+linux:ref:`jesd204-fsm-framework`
           - :ref:`JESD204 status utility <software jesd-status>`
           - :ref:`JESD204 Eye Scan <software jesd-eye-scan>`
           - :external+hdl:ref:`jesd204`

     #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile <resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
     #. :git-hdl:`HDL reference design <projects/adrv903x>` which you must use in your FPGA.
        More HDL build details at :external+hdl:ref:`build_hdl`.

#. :doc:`Additional documentation about SDR Signal Chains - The math behind the RF </solutions/reference-designs/fmcomms2/common/math>`
#. :ref:`Help and Support <help-and-support>`

.. _adrv9032 block-diagram:

Block diagram
-------------------------------------------------------------------------------

The ADRV9032/ADRV9032R features a zero-IF (ZIF) architecture that provides
wide bandwidth with dynamic range suitable for non-contiguous multicarrier
applications. The transceiver includes:

- 2 transmitter channels with integrated DACs
- 2 receiver channels with integrated ADCs
- 2 observation receiver channels for transmitter monitoring
- Integrated RF and clock synthesizers
- JESD204B/C digital interface (up to 16.5 Gbps)
- SPI control interface
- General purpose I/O and interrupts

.. image:: block-diagram.png
   :align: center
   :width: 800

Pictures
-------------------------------------------------------------------------------

.. figure:: evaluation-board-top.webp

   ADRV903X evaluation board - top view

.. figure:: evaluation-board-bottom.webp

   ADRV903X evaluation board - bottom view

Videos
-------------------------------------------------------------------------------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI articles
-------------------------------------------------------------------------------

Four Quick Steps to Production: Using Model-Based Design for Software-Defined
Radio:

#. :adi:`Part 1 - The Analog Devices/AMD Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
#. :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
#. :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
#. :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

About JESD standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

MathWorks webinars
-------------------------------------------------------------------------------

#. :mw:`Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
#. :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
