.. _fmcomms2:

AD-FMCOMMS2-EBZ
===============================================================================

2x2 MIMO RF Agile Transceiver™, 70 MHz to 6.0 GHz.

.. image:: images/ad9361_chip.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD-FMCOMMS2` is an FMC board for the :adi:`AD9361`
(:adi:`design package <en/license/licensing-agreement/ad9361.html>`), a highly
integrated RF Agile Transceiver™. While the complete chip level design package
can be found on the :adi:`ADI web site <ad9361_design_files>`, information on
the card, and how to use it, the design package that surrounds it, and the
software which can make it work, can be found here.

The purpose of the AD-FMCOMMS2-EBZ is to provide an RF platform which shows
maximum performance of the AD9361. It's expected that the RF performance of
this platform can meet the datasheet specifications without issues at 2.4 GHz,
and not much anywhere else. This is due to the external Johanson Technology's
`2450BL15B050E <https://www.johansontechnology.com/datasheets/2450BL15B050/2450BL15B050.pdf>`_
2.45 GHz Balun that is on the board. This balun is rated for an operating
frequency of 2400~2500 MHz.

This platform is primarily for hardware / RF investigation and bring up of
various waveforms from a RF team before their custom hardware is complete,
where they want to see waveforms at their frequency of interest, and are not
afraid of changing out the balun if necessary. (Have a look in the
:ref:`Configuration <fmcomms2 hardware configuration-options>`
sections).

The AD-FMCOMMS2-EBZ board is very similar to the
:ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>`
board with only one exception, the RX/TX RF differential to single ended
balun/transformer. The AD-FMCOMMS3-EBZ is more targeted for wider tuning range
applications, that is why we use the
`TCM1-63AX+ <http://www.minicircuits.com/pdfs/TCM1-63AX+.pdf>`_ from Mini
Circuits as the RF transformer of choice. We affectionately call the
FMCOMMS3-EBZ the "Software Engineers" platform, and the FMCOMMS2-EBZ, the
"RF Engineers" platform to denote the difference.

Features:

- 2x2 MIMO transceiver with integrated 12-bit DACs and ADCs
- Tunable frequency range: 70 MHz to 6.0 GHz
- Adjustable channel bandwidth: 200 kHz to 56 MHz
- Johanson Technology 2.45 GHz balun (optimized for 2.4 GHz)
- FMC-LPC system board connector
- On-board power solution

Applications:

- Software-defined radio (SDR)
- Point-to-point communication
- Wireless LAN (2.4 GHz)
- LTE/3G femtocell base stations
- General-purpose radio experimentation

.. figure:: images/eval-ad-fmcomms2.jpg
   :width: 500

   AD-FMCOMMS2-EBZ

.. toctree::
   :hidden:

   common/index
   hardware/index
   help_and_support
   partial_reconfiguration
   prerequisites
   quickstart/index
   software/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the :ref:`Help and Support <fmcomms2 help-and-support>` page.

To better understand the :adi:`AD9361`, we recommend to use the
:adi:`EVAL-AD-FMCOMMS2` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. :ref:`Introduction <fmcomms2 common introduction>`
#. Hardware: This provides a brief description of
   the board by itself, and is a good reference for those who want to
   understand a little more about the board. If you just want to use the board,
   you can skip this section, and come back to it when you want to incorporate
   the AD9361 into your product.

   #. :ref:`Hardware <fmcomms2 hardware>`

      #. :ref:`Characteristics & Performance <fmcomms2 hardware card-specification>`
      #. :ref:`Configuration options <fmcomms2 hardware configuration-options>`
      #. :ref:`FCC or CE certification <fmcomms2 hardware certification>`
      #. :ref:`Tuning the system <fmcomms2 hardware tuning>`

   #. :ref:`Production Testing Process <fmcomms2 common testing>`

#. Use the board to better understand the AD9361

   #. :ref:`What you need to get started <fmcomms2 prerequisites>`
   #. :ref:`Quick Start Guides <fmcomms2 quickstart>`

      #. :ref:`On ZC702 <fmcomms2 quickstart zc702>`
      #. :ref:`On ZC706 <fmcomms2 quickstart zc706>`
      #. :ref:`On ZED <fmcomms2 quickstart zed>`
      #. :ref:`On ZCU102 <fmcomms2 quickstart zcu102>`
      #. :ref:`On KCU105 <fmcomms2 quickstart kcu105>`
      #. :ref:`On KC705, VC707 (Obsolete) <fmcomms2 quickstart microblaze>`
      #. :external+kuiper:doc:`Configure a pre-existing SD-Card <index>`

   #. Linux Applications

      #. :ref:`Using the IIO Oscilloscope <fmcomms2 software using-iio-osc>`

         #. :ref:`AD9361 Control in the IIO Scope Plugin <fmcomms2 software ad9361-plugin>`
         #. :ref:`Advanced AD9361 Control IIO Scope Plugin <fmcomms2 software ad9361-advanced-plugin>`

      #. :ref:`Shell scripts <software shell-scripts>`
      #. :ref:`FRU EEPROM Utility <software fru-dump>`

   #. Push custom data into/out of the AD9361

      #. :ref:`Basic Data files and formats <fmcomms2 common basic-iq-datafiles>`
      #. :ref:`Create and analyze data files in MATLAB <fmcomms2 common datafiles>`
      #. :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
      #. :ref:`AD9361 libiio streaming example <libiio>`
      #. :external+pyadi-iio:doc:`Python Interfaces <index>`

#. Design with the AD9361

   #. :ref:`Understanding the AD9361 <fmcomms2 common ad9361>`

      - :adi:`AD9361 Product page <AD9361>`
      - :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      - :ref:`MATLAB Filter Design Wizard for AD9361 <fmcomms2 software filters>`
      - :ref:`Filter response <fmcomms2 software baremetal-filter>`
      - :ref:`AD9361 Filter Design license <fmcomms2 software filters license>`

   #. Simulation

      #. :ref:`MathWorks RF Blockset (formerly SimRF) Models of the AD9361 <fmcomms2 software simrf>`
      #. :ref:`Installing RF Blockset Models <fmcomms2 software rfblkset-mdls-install>`
      #. :ref:`How to run the AD9361 Receive Testbench <fmcomms2 software rfblkset-mdls-run-testbench>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. MATLAB/Simulink Examples

         - :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
         - :ref:`Beacon Frame Receiver Example <fmcomms2 software beacon-frame-receiver>`
         - :ref:`QPSK Transmit and Receive Example <fmcomms2 software qpsk-example>`
         - :ref:`LTE Transmitter and Receiver Example <fmcomms2 software lte-example>`
         - :ref:`ADS-B Airplane Tracking Example <fmcomms2 software adsb-example>`

      #. :ref:`GNU Radio <software gnuradio>`
      #. :ref:`FM Radio/Tuner <fmcomms2 software fm-radio>`
         (listen to FM signals on the HDMI monitor)
      #. :ref:`C example <libiio>`

   #. Targeting

      #. :ref:`Analog Devices Transceiver Toolbox for MATLAB and Simulink <matlab transceiver-toolbox>`
      #. :mw:`QPSK Modem Design Workflow <help/comm/ug/hdlqpsktransmitterreceiver.html>`

   #. Complete Workflow

      #. :ref:`ADS-B Airplane Tracking Tutorial <fmcomms2 software adsb-tutorial>`

   #. Design a custom AD9361 based platform

      #. Linux software

         - :ref:`AD-FMCOMMS2/3/4-EBZ on Microblaze <linux-kernel microblaze>`
         - :external+linux:doc:`Linux Device Driver <drivers/iio-transceiver/ad9361>`
         - :ref:`Build the demo on ZC702, ZC706, ZED from source <linux-kernel zynq>`
         - :ref:`Linux with HDMI video output on Zynq <linux-kernel zynq-hdmi>`
         - :ref:`Build the demo on KC705 or VC707 for Microblaze from source <linux-kernel microblaze>`
         - :ref:`Build ZynqMP/MPSoC Linux kernel and devicetrees from source <linux-kernel zynqmp>`
         - :ref:`Customizing the devicetree on the target <linux-kernel zynq-tips-tricks>`

      #. No-OS Software

         - :external+no-OS:doc:`No-OS AD9361 project <projects/rf-transceiver/ad9361>`

      #. :external+hdl:ref:`HDL reference design <fmcomms2>` which you must use
         in your FPGA.

         - :ref:`Digital Interface Timing Validation <fmcomms2 common interface-timing-validation>`
         - :ref:`Partial Reconfiguration with FMCOMMS2 <fmcomms2 partial-reconfiguration>`

#. Additional Documentation about SDR Signal Chains

   - :ref:`The math behind the RF <fmcomms2 common fmcomms-math>`
   - :ref:`I/Q Correction <fmcomms2 common iq-correction>`
   - :ref:`IQ rotation and phase sync <fmcomms2 common iq-rotation>`

#. :ref:`Help and Support <fmcomms2 help-and-support>`

Videos
-------------------------------------------------------------------------------

Introduction to the AD9361
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`AD9361 RF Agile Transceiver <en/education/education-library/videos/2752786084001.html>`

Introduction to the AD9361 based ecosystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`AD9361 RF Transceiver and Support Ecosystem <en/education/education-library/videos/2753072929001.html>`

Digital Filter Wizard for the AD9361
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`Digital Filter Design For Integrated RF Transceivers <en/education/education-library/videos/3845680080001.html>`

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`iiosdr.mp4 <http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4>`_

ADI Articles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Four Quick Steps to Production: Using Model-Based Design for
  Software-Defined Radio

  - :adi:`Part 1 - the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
  - :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
  - :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
  - :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :mw:`Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and RF Blockset (formerly SimRF) <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
- :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/software-defined-radio-using-matlab-and-simulink-1601496230597.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <fmcomms2 help-and-support>` page.
