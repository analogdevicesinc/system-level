.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv904x

.. _adrv904x:

EVAL-ADRV904x
===============================================================================

Integrated 8T8R RF Transceiver with Digital Pre-Distortion and Crest Factor
Reduction.

.. image:: images/adrv904x.jpeg
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-ADRV904x`, is an FMC radio card designed to showcase the
:adi:`ADRV9040` and :adi:`ADRV9044`, highly integrated, radio frequency (RF)
agile transceivers offering 8 independently controlled transmitters, 2
observation receiver inputs for monitoring transmitter channels, 8 independently
controlled receivers, integrated local oscillator (LO) and clock synthesizers,
digital front-end (DFE) with crest factor reduction (CFR) and digital
pre-distortion (DPD), and digital signal processing functions providing a
complete transceiver solution.

The device provides the high radio performance and low-power consumption
demanded by cellular infrastructure applications and massive MIMO base stations,
offering advanced DFE capabilities on an integrated ARM Cortex-A55 quad-core
processor.

Features:

- Both chips feature:

  - 8 differential transmitters & 8 differential receivers
  - 2 differential observation receivers
  - Support for TDD and FDD applications
  - LO tunable range: 450 MHz to 7100 MHz
  - RF frequency bands:

    - Low Band (LB): 600 MHz to 2800 MHz
    - Mid Band (MB): 1.8 GHz to 4.8 GHz
    - High Band (HB): 4.5 GHz to 6 GHz

  - Integrated Digital Front-End (DFE) with CFR and digital pre-distortion
  - ARM Cortex-A55 quad-core processor for DFE algorithms (DPD, CLGC, VSWR)
  - JESD204B and JESD204C digital interface with fixed and floating-point data
    format support
  - Zero-IF (ZIF) architecture

- Complete ADRV9040/ADRV9044 radio cards for evaluation

  - FMC connector for FPGA integration
  - Fully integrated fractional-N RF synthesizer
  - Fully integrated clock synthesizer

Applications:

- 3G/4G/5G TDD and FDD massive MIMO
- Macro and small cell base stations
- Software defined radios
- Wireless infrastructure

.. image:: images/adrv904x-evaluation-board.png
   :align: center
   :width: 500

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   adrv904x_osc_main
   dpd/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the :ref:`Help and Support <adrv904x
help_and_support>` section at the bottom of the page.

To better understand the :adi:`ADRV9040` / :adi:`ADRV9044`, we recommend to use
the :adi:`EVAL-ADRV904x` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`User guide <adrv904x user-guide>`
   #. :ref:`Prerequisites <adrv904x prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guides <adrv904x quickstart>`:

      #. Using the :ref:`ZCU102 (ZynqMP) <adrv904x quickstart zcu102>`

   #. Configure an SD Card with :external+kuiper:ref:`Kuiper <use-kuiper-image>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the ADRV9040/ADRV9044

   #. :ref:`adrv904x block-diagram`

     #. :adi:`ADRV9040 product page <ADRV9040>`
     #. :adi:`ADRV9044 product page <ADRV9044>`
     #. :adi:`Full data sheet and chip design package <en/products/adrv9040.html>`

   #. Hardware in the Loop / How to design your own custom BaseBand

     #. :ref:`GNU Radio <software gnuradio>`
     #. :ref:`Transceiver Toolbox <matlab transceiver-toolbox>`

   #. Resources for designing a custom ADRV9040/ADRV9044-based platform software

     #. For Linux software:

        #. About the device driver:

           #. :external+hdl:ref:`axi_jesd204_tx` / :git-linux:`JESD204B Transmit Linux driver <main:drivers/iio/jesd204/axi_jesd204_tx.c>`
           #. :external+hdl:ref:`axi_jesd204_rx` / :git-linux:`JESD204B Receive Linux driver <main:drivers/iio/jesd204/axi_jesd204_rx.c>`
           #. :external+hdl:ref:`axi_adxcvr` / :git-linux:`AXI_ADXCVR High-speed transceivers Linux driver <main:drivers/iio/jesd204/axi_adxcvr.c>`
           #. :external+linux:ref:`AXI ADC HDL Linux driver <axi-adc-hdl>`
           #. :external+linux:ref:`AXI DAC HDL Linux driver <axi-dac-dds-hdl>`
           #. :external+linux:ref:`AD9528 Low Jitter Clock Generator Linux driver <ad9528>`
           #. :external+hdl:ref:`axi_dmac` / :git-linux:`AXI-DMAC DMA Controller Linux driver <main:drivers/dma/dma-axi-dmac.c>`
           #. :external+linux:ref:`ADRV904x Linux device driver <adrv904x>`

        #. About the device tree:

           #. :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

        #. About the JESD204 utilities:

           #. :external+linux:ref:`JESD204 FSM <jesd204-fsm-framework>`
           #. :ref:`JESD204 status utility <software jesd-status>`
           #. :ref:`JESD204 Eye Scan <software jesd-eye-scan>`
           #. :external+hdl:ref:`jesd204`

     #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile <resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
     #. :git-hdl:`HDL reference design <projects/adrv904x>`
        which you must use in your FPGA.

#. Digital Pre-Distortion (DPD)

   #. :ref:`ADRV904x DPD User Guide <adrv904x dpd user-guide>`
   #. :ref:`DPD Introduction <adrv904x dpd introduction>`
   #. :ref:`DFE System Overview <adrv904x dfe overview>`
   #. :ref:`DPD Capabilities <adrv904x dpd capabilities>`
   #. :ref:`High Level Development Flow <adrv904x dpd dev flow>`
   #. :ref:`DPD Evaluation Prerequisites <adrv904x dpd pre-requisites>`
   #. :ref:`Evaluating ADRV904x DPD <adrv904x dpd eval guide>`
   #. :ref:`DPD Error Troubleshooting <adrv904x dpd troubleshooting>`
   #. :ref:`DPD Analysis Tool <adrv904x dpd analysis tool>`

#. :doc:`SDR math </solutions/reference-designs/fmcomms2/common/math>`
#. :ref:`Help and Support <adrv904x help_and_support>`

.. _adrv904x block-diagram:

Block diagram
-------------------------------------------------------------------------------

The ADRV9040/ADRV9044 features a zero-IF (ZIF) architecture that provides wide
bandwidth with dynamic range suitable for contiguous and non-contiguous
multicarrier applications. The transceiver includes:

#. 8 transmitter channels with integrated DACs and DPD/CFR
#. 8 receiver channels with integrated ADCs
#. 2 observation receiver channels for transmitter monitoring
#. Integrated RF and clock synthesizers
#. Integrated ARM Cortex-A55 quad-core processor for DFE
#. JESD204B/C digital interface
#. SPI control interface
#. General purpose I/O and interrupts

.. image:: images/adrv904x_block_diagram.png
   :align: center
   :width: 800

Videos
-------------------------------------------------------------------------------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI articles
-------------------------------------------------------------------------------

Four Quick Steps to Production: Using Model-Based Design for Software-Defined
Radio:

#. :adi:`Part 1 <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
#. :adi:`Part 2 <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
#. :adi:`Part 3 <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
#. :adi:`Part 4 <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

About JESD standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

MathWorks webinars
-------------------------------------------------------------------------------

#. :mw:`Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
#. :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

.. _adrv904x unboxing:

Unboxing guide
-------------------------------------------------------------------------------
Detailed description of the setup procedure for ADRV9009 (similar procedure for ADRV904x):

:ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/AD9371-and-ADRV9009-setup-with-ZCU102-or-ZC706-April2019.pdf>`

Warning
-------------------------------------------------------------------------------
.. esd-warning::

.. _adrv904x help_and_support:

Help and support
-------------------------------------------------------------------------------

For questions and more information, please visit the :ez:`Help and Support <rf/wide-band-rf-transceivers/design-support-adrv904x>` technical support
community.
