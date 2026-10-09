.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9026

.. _adrv902x:

EVAL-ADRV902X
===============================================================================

Integrated, Quad RF Transceiver with Observation Path.

.. image:: ../images/adrv9026.webp
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>`, are FMC radio cards
designed to showcase the :adi:`ADRV9026` and :adi:`ADRV9029`, highly
integrated, radio frequency (RF) agile transceivers offering 4 independently
controlled transmitters, dedicated observation receiver inputs for monitoring
each transmitter channel, 4 independently controlled receivers, integrated
synthesizers, and digital signal processing functions providing complete
transceiver solutions.

The devices provide the performance demanded by cellular infrastructure
applications, such as small cell base station radios, macro 3G/4G/5G systems,
and massive multiple in/multiple out (MIMO) base stations.

Features:

- Both chips feature:

  - 4 differential transmitters & 4 differential receivers
  - 2 observation receivers with 2 inputs each
  - Support for TDD and FDD applications
  - 24.33 Gbps JESD204B/JESD204C digital interface

- Complete ADRV9026 radio cards for evaluation

  - ADRV9026-HB/PCBZ for frequency band 2.8GHz to 6GHz
  - ADRV9026-MB/PCBZ for frequency band 650MHz to 2.8GHz
  - ADRV9026-LB/PCBZ for frequency band 75MHz to 1000MHz

- Complete ADRV9029 radio cards for evaluation

  - ADRV9029-HB/PCBZ (integrated DPD & CFR) for frequency band 2.8GHz to 6GHz
  - ADRV9029-MB/PCBZ (integrated DPD & CFR) for frequency band 650MHz to 2.8GHz

- A separate power daughter card provides reference design for high efficiency
  power supply solution
- FMC connector for FPGA

Applications:

- 3G/4G/5G TDD and FDD massive MIMO, macro and small cell base stations

.. image:: ../images/eval_adrv9026.png
   :align: center
   :width: 500

.. toctree::
   :hidden:

   adrv9026_osc_main
   prerequisites
   quickstart/index
   user-guide
   dpd/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`ADRV9026` / :adi:`ADRV9029`, we recommend to use
the :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <adrv902x prerequisites>` - what you need to get started
   #. :ref:`Quick start guides <adrv902x quickstart>`:

      #. Using the :ref:`VCK190/Versal <adrv902x quickstart vck190>`
      #. Using the :ref:`ZCU102/Zynq UltraScale+ MP SoC <adrv902x quickstart zcu102>`
 
   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the ADRV9026/ADRV9029

   - :ref:`adrv902x block-diagram`

     - :adi:`ADRV9026 product page <ADRV9026>`
     - :adi:`ADRV9029 product page <ADRV9029>`
     - :adi:`Full data sheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`

   - :ref:`Digital Pre-Distortion (DPD) user guide <adrv902x dpd>`

   - Hardware in the Loop / How to design your own custom BaseBand

     - :ref:`GNU Radio <software gnuradio>`
     - :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   - Resources for designing a custom ADRV9026/ADRV9029-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`axi_jesd204_tx`
           - :external+linux:ref:`axi_jesd204_rx`
           - :external+linux:ref:`axi_adxcvr`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dac-dds-hdl`
           - :external+linux:ref:`ad9528`
           - :external+linux:ref:`axi-dmac`
           - :external+linux:ref:`adrv9025`
             and :external+linux:ref:`adrv9025-customization`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

        #. About the JESD204 utilities:

           - :external+linux:ref:`jesd204-fsm-framework`
           - :ref:`JESD204 status utility <software jesd-status>`
           - :ref:`JESD204 Eye Scan <software jesd-eye-scan>`
           - :external+hdl:ref:`jesd204`

     #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile <resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
     #. :external+hdl:ref:`HDL reference design <adrv9026>` which you must use in your FPGA.

#. :doc:`Additional documentation about SDR Signal Chains - The math behind the RF </solutions/reference-designs/fmcomms2/common/math>`
#. :ref:`Help and Support <help-and-support>`

.. _adrv902x block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: ../images/adrv9026_block_diagram.png
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

#. :adi:`Part 1 - The Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
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

Additional information
-------------------------------------------------------------------------------

:ref:`Digital Pre-Distortion (DPD) user guide <adrv902x dpd>`
with the :adi:`ADRV9029`:

- :ref:`ADRV9029 DPD introduction <adrv902x dpd introduction>`

  - :ref:`ADRV9029 Digital Front End system overview <adrv902x dpd dfe-overview>`
  - :ref:`ADRV9029 DPD system overview <adrv902x dpd system-overview>`
  - :ref:`ADRV9029 DPD specifications <adrv902x dpd capabilities>`
  - :ref:`Typical high level DPD development flow with the ADRV9029 transceiver <adrv902x dpd development-flow>`

- :ref:`ADRV9029 DPD prerequisites <adrv902x dpd prerequisites>`
- `Unboxing ADRV902x Transceiver Eval Platform - Video <https://www.youtube.com/watch?v=Oq_9bl5f8fM>`_
- :ref:`Evaluating ADRV9029 through TES GUI <adrv902x dpd evaluation-tes>`
- :ref:`Evaluating ADRV9029 DPD through TES GUI <adrv902x dpd evaluating-dpd-tes>`
- :ref:`ADRV9029 DPD error troubleshooting <adrv902x dpd error-troubleshooting>`
- :ref:`ADRV9029 based DPD development flow <adrv902x dpd development-flow-low-level>`
- :ref:`ADRV9029 DPD model generation <adrv902x dpd model-optimization>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
