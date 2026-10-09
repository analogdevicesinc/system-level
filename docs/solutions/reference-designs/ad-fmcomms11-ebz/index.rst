.. _fmcomms11:

AD-FMCOMMS11-EBZ
================================================================================

16-Bit, 12 GSPS RF DAC and 12-Bit, 2.5 GSPS RF ADC Development Platform.

.. image:: images/AD9625-TR-TAG-chip-illustration.png
   :align: left
   :width: 150

.. image:: images/AD9162-TR-chip-illustration.png
   :align: left
   :width: 150

Overview
--------------------------------------------------------------------------------

The :adi:`AD-FMCOMMS11-EBZ` board is a system platform board for communication
infrastructure applications that demonstrates the Direct to RF (DRF) transmitter
and observation receiver architecture. Using high sample rate RFDAC(s)
and RFADC(s), a number of components in previous generation transmitters can be
eliminated, such as mixers, modulators, IF amplifiers and filters. The objective
being to bring the ADC or DAC as close to the antenna as possible, leading to
possibly more cost effective and efficient communications solution.
It is composed of multi-GSps RF ADC :adi:`AD9625` and DAC :adi:`AD9162`, Cheetah
and Barium respectively. The transmit path contains a balun, low pass filter,
gain block and variable attenuation to produce an output appropriate for a power
amplifier module. Along the observation path, the PA output is coupled back into
the board through a variable attenuator, a balun and finally the ADC. Clock
management is taken care of on board; all the necessary clocks are generated
from a reference. Power management is present as well. We will provide typical
performance data for the entire range (70 MHz – 6 GHz) which is
supported by the platform. This is primarily for system investigation and bring
up of various waveforms from a software team before their custom hardware is
complete, where they want to see waveforms, but are not concerned about the last
1dB or 1% EVM of performance.

Features:

- TX
   - 16-bit 12GSPS RFDAC
   - JESD204B Interface
      - 8 lanes up to 12.5Gbps
   - 1x/2x/4x/6x/8x/12x/16x/24x/32x Interpolation
   - 64-bit NCO at max rate
   - Analog Modes of Operation:
      - Normal Mode: 6GSPS DAC rate
         - Synthesis up to 2.5GHz (1st Nyquist)
      - Mix Mode: 6GSPS DAC rate
         - Synthesis in 2nd & 3rd Nyquist zones
      - 2X Normal Mode: 12GSPS DAC rate
         - Synthesis up to 6GHz (1st Nyquist)
      - Excellent dynamic performance
- RX
   - 3.2GHz full power bandwidth at 2.5GSPS
      - Noise Density = -149.5dBFs/Hz, ENOB = 9.5 bits
      - SFDR = 77 dBc at 1GHz Ain (2.5Gsps)
      - SFDR = 77dBc at 1.8GHz Ain (2.5Gsps)
   - +/-0.3 LSB DNL, +/-1.0 LSB INL
   - Dual supplies : 1.3V and 2.5V
   - 8 or 6 Lane JESD204B Outputs
   - Programmable clipping threshold for Fast Detect output
   - Two Integrated wide band digital down converters (DDC) per channel
      - 10-bit complex NCO
      - 2 cascaded half band filters (dec/8, dec/16)
   - Timestamp for synchronous processing alignment
      - SYSREF Setup/Hold detector
   - Programmable Interrupt (IRQ) event monitor

Applications:

- TX
   - Broadband communications systems
   - DOCSIS 3.1 cable modem termination system (CMTS)/video on demand
     (VOD)/edge quadrature amplitude modulation (EQAM)
   - Wireless communications infrastructure
   - W-CDMA, LTE, LTE-A, point to point
   - Instrumentation, automatic test equipment (ATE)
   - Radars and jammers
- RX
   - Spectrum analyzers
   - Military communications
   - Radar
   - High performance digital storage oscilloscopes
   - Active jamming/antijamming
   - Electronic surveillance and countermeasures

.. image:: images/fmcomms11_image.png
   :align: center
   :width: 600

Recommendation
-------------------------------------------------------------------------------

To better understand the :adi:`AD9625` and :adi:`AD9162`, we recommend to use
the :adi:`AD-FMCOMMS11-EBZ` evaluation board.

Table of Contents
--------------------------------------------------------------------------------

#. :ref:`FMCOMMS11 Hardware <fmcomms11 hardware>`:
   This provides a brief description of the AD-FMCOMMS11-EBZ
   board by itself, and is a good reference for those who want
   to understand a little more about the board. If you just
   want to use the board, you can skip this section, and come
   back to it when you want to incorporate one of the devices
   into your product.

   #. :doc:`Functional Overview & Specifications <hardware/functional_overview>`
   #. :doc:`Characteristics & Performance <hardware/card_specification>`

#. :doc:`FCC or CE certification <certification>`
#. :doc:`Production Testing Process <testing>`

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`fmcomms11 user-guide`- what you need to know about the
      evaluation board
   #. :ref:`fmcomms11 prerequisites`- what you need to get started
   #. :ref:`Quick-Start Guide <fmcomms11 quickstart>`:

      #. Using the :ref:`ZC706 <fmcomms11 quickstart zc706>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`
   #. Software Solutions

       #. :ref:`iio-oscilloscope`
       #. :ref:`fmcomms11-plugin`
       #. :external+scopy:doc:`Scopy <index>`
       #. :ref:`IIO Command Line Tools <libiio cli>`
       #. :ref:`Python Interfaces <pyadi-iio>`
       #. :git-pyadi-iio:`FMCOMMS11 Python Example <main:examples/fmcomms11.py>`

#. Design with the FMCOMMS11

  #. :ref:`fmcomms11 block-diagram`

      #. :adi:`AD-FMCOMMS11-EBZ Product page <ad-fmcomms11-ebz>`
      #. :adi:`AD9162 Product page <AD9162>`
      #. :adi:`AD9625 Product page <AD9625>`

   #. Resources for designing a custom AD9625/AD9162-based platform software

      #. For Linux software:

         #. About the device driver:

            #. :external+linux:doc:`JESD204B Transmit Linux driver <drivers/jesd204/axi_jesd204_tx>`
            #. :external+linux:doc:`JESD204B Receive Linux driver <drivers/jesd204/axi_jesd204_rx>`
            #. :external+linux:doc:`JESD204B/C AXI_ADXCVR High-speed transceivers Linux driver <drivers/jesd204/axi_adxcvr>`
            #. :external+linux:doc:`AXI ADC HDL Linux driver <drivers/iio-adc/axi-adc-hdl>`
            #. :external+linux:doc:`AXI DAC HDL Linux driver <drivers/iio-dds/axi-dac-dds-hdl>`
            #. :external+linux:doc:`AXI-DMAC DMA Controller Linux driver <drivers/dma/axi-dmac>`
            #. :external+linux:doc:`AD9162 Linux driver <drivers/iio-pll/ad9162>`

         #. About the device tree:

            #. :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

         #. About the JESD204 utilities:

            #. :external+linux:doc:`JESD204 (FSM) interface Linux Kernel framework <drivers/jesd204/jesd204-fsm-framework>`
            #. :ref:`JESD204 status utility <software jesd-status>`
            #. :ref:`JESD204 Eye Scan <software jesd-eye-scan>`
            #. :external+hdl:ref:`jesd204`

      #. FPGA Resources:

         #. :external+hdl:doc:`FMCOMMS11 HDL reference design <projects/fmcomms11/index>`
         #. :external+hdl:ref:`HDL User Guide <user_guide>`
         #. :external+hdl:doc:`HDL Customize Guide <user_guide/customize_hdl>`

.. _fmcomms11 block-diagram:

Block diagram
--------------------------------------------------------------------------------

.. image:: images/AD-FMCOMMS11-EBZ-block-diagram.png
   :align: center
   :width: 800

ADI Articles
--------------------------------------------------------------------------------

- Four Quick Steps to Production: Using Model-Based Design for
  Software-Defined Radio

  - :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
  - :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
  - :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
  - :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

Videos
--------------------------------------------------------------------------------

- :adi:`Silent Switcher µModule Regulators Powering GSPS Sampling ADC <en/products/ad9625.html#product-recommendations>`

MathWorks Webinars
--------------------------------------------------------------------------------

- `Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`_
- `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`_

Help and support
--------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience.
However, like many things, documentation is never as complete as it should be.
If you have any questions, feel free to ask on the :ez:`/` technical support
community, but before that, please make sure you read our documentation
thoroughly.

Warning
--------------------------------------------------------------------------------

.. esd-warning::

.. toctree::
   :hidden:

   certification
   fmcomms11_plugin
   hardware
   hardware/card_specification
   hardware/functional_overview
   prerequisites
   quickstart/index
   testing
   user-guide
