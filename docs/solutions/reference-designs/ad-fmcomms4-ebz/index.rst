.. _fmcomms4:

AD-FMCOMMS4-EBZ
===============================================================================

1x1 RF Agile Transceiver, 70 MHz to 6.0 GHz.

.. image:: ../fmcomms2/images/ad9364_chip.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD-FMCOMMS4` is an FMC board for the :adi:`AD9364`, a highly
integrated RF Agile Transceiver. While the complete chip level design package
can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information
on the card, and how to use it, the design package that surrounds it, and the
software which can make it work, can be found here.

The purpose of the AD-FMCOMMS4-EBZ is to provide an RF platform to software
developers, system architects, etc, who want a single platform which operates
over a much wider tuning range (70 MHz – 6 GHz).

The AD-FMCOMMS4-EBZ is very similar to the :ref:`AD-FMCOMMS2-EBZ <fmcomms2>` and
:ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>` boards, but instead of the
:adi:`AD9361` (2 Rx, 2 Tx), it uses the :adi:`AD9364`, a lower cost 1 Rx, 1 Tx
device. The board includes both types of external baluns: one targeted for wider
tuning range applications (Mini-Circuits
`TCM1-63AX+ <http://www.minicircuits.com/pdfs/TCM1-63AX+.pdf>`_), and one
optimized for 2.4 GHz performance.

Features:

- 1x1 transceiver with integrated 12-bit DACs and ADCs
- Tunable frequency range: 70 MHz to 6.0 GHz
- Adjustable channel bandwidth: 200 kHz to 56 MHz
- Dual balun options: wideband (TCM1-63AX+) and 2.4 GHz optimized
- FMC-LPC system board connector
- On-board power solution

Applications:

- Software-defined radio (SDR)
- Point-to-point communication
- Wireless LAN (2.4 GHz)
- General-purpose radio experimentation

.. figure:: images/ad-fmcomms4-ebz-ev-board.jpg
   :align: center
   :width: 500

.. toctree::
   :hidden:

   user-guide
   hardware
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the :ref:`Help and Support <fmcomms2
help-and-support>` page.

To better understand the :adi:`AD9364`, we recommend to use the
:adi:`EVAL-AD-FMCOMMS4` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. :adi:`Purchase <ad-fmcomms4-ebz#eb-buy>`
#. :ref:`Introduction <fmcomms2 common introduction>`
#. :ref:`User guide <fmcomms4 user-guide>`
#. Hardware: This provides a brief description of
   the board by itself, and is a good reference for those who want to
   understand a little more about the board. If you just want to use the board,
   you can skip this section, and come back to it when you want to incorporate
   the AD9364 into your product.

   #. :ref:`Hardware <fmcomms4 hardware>`

      #. :ref:`Characteristics & Performance <fmcomms2 hardware card-specification>`
      #. :ref:`Configuration options <fmcomms2 hardware configuration-options>`
      #. :ref:`FCC or CE certification <fmcomms2 hardware certification>`
      #. :ref:`Tuning the system <fmcomms2 hardware tuning>`

   #. :ref:`Production Testing Process <fmcomms2 common testing>`

#. Use the AD-FMCOMMS4-EBZ Board to better understand the AD9364

   #. :ref:`What you need to get started <fmcomms4 prerequisites>`
   #. :ref:`Quick Start Guides <fmcomms4 quickstart>`

      #. :ref:`On ZCU102 <fmcomms4 quickstart zcu102>`
      #. :ref:`On KCU105 <fmcomms4 quickstart kcu105>`
      #. :ref:`On ZC706 <fmcomms4 quickstart zc706>`
      #. :ref:`On ZC702 <fmcomms4 quickstart zc702>`
      #. :ref:`On ZED <fmcomms4 quickstart zed>`
      #. :external+kuiper:doc:`Configure a pre-existing SD-Card <index>`

   #. Linux Applications

      #. :ref:`Using the IIO Oscilloscope <fmcomms2 software using-iio-osc>`

         #. :ref:`AD936x Control in the IIO Scope Plugin <fmcomms2 software ad9361-plugin>`
         #. :ref:`Advanced AD936x Control IIO Scope Plugin <fmcomms2 software ad9361-advanced-plugin>`

      #. :ref:`Shell scripts <software shell-scripts>`
      #. :ref:`FRU EEPROM Utility <software fru-dump>`

   #. Push custom data into/out of the AD9364

      #. :ref:`Basic Data files and formats <fmcomms2 common basic-iq-datafiles>`
      #. :ref:`Create and analyze data files in MATLAB <fmcomms2 common datafiles>`
      #. :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
      #. :ref:`AD9361 libiio streaming example <libiio>`
      #. :external+pyadi-iio:doc:`Python Interfaces <index>`

#. Design with the AD9364

   #. :ref:`Understanding the AD9364 <fmcomms2 common ad9361>`

      #. :adi:`AD9361 Product page <AD9364>`
      #. :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      #. :ref:`MATLAB Filter Design Wizard for AD9361 <fmcomms2 software filters>`

   #. Simulation

      #. :ref:`MathWorks RF Blockset (formerly SimRF) Models of the AD9361 <fmcomms2 software simrf>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. MATLAB/Simulink Examples

         #. :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
         #. :ref:`Beacon Frame Receiver Example <fmcomms2 software beacon-frame-receiver>`
         #. :ref:`QPSK Transmit and Receive Example <fmcomms2 software qpsk-example>`
         #. :ref:`LTE Transmitter and Receiver Example <fmcomms2 software lte-example>`
         #. :ref:`ADS-B Airplane Tracking Example <fmcomms2 software adsb-example>`

      #. :ref:`GNU Radio <software gnuradio>`
      #. :ref:`FM Radio/Tuner <fmcomms2 software fm-radio>`
         (listen to FM signals on the HDMI monitor)
      #. :ref:`C example <libiio>`

   #. Design a custom AD9364 based platform

      #. Linux software

         #. :ref:`AD-FMCOMMS2/3/4-EBZ on Microblaze <linux-kernel microblaze>`
         #. :external+linux:doc:`Linux Device Driver <drivers/iio-transceiver/ad9361>`
         #. :ref:`Build the demo on ZC702, ZC706, ZED from source <linux-kernel zynq>`
         #. :ref:`Linux with HDMI video output on Zynq <linux-kernel zynq-hdmi>`
         #. :ref:`Build the demo on KC705 or VC707 for Microblaze from source <linux-kernel microblaze>`
         #. :ref:`Build ZynqMP/MPSoC Linux kernel and devicetrees from source <linux-kernel zynqmp>`
         #. :ref:`Customizing the devicetree on the target <linux-kernel zynq-tips-tricks>`

      #. No-OS Software

         - :external+no-OS:doc:`No-OS AD9361 project <projects/rf-transceiver/ad9361>`

      #. :external+hdl:ref:`HDL reference design <fmcomms2>` which you must use
         in your FPGA.

         - :ref:`Digital Interface Timing Validation <fmcomms2 common interface-timing-validation>`

#. Additional Documentation about SDR Signal Chains

   #. :ref:`The math behind the RF <fmcomms2 common fmcomms-math>`
   #. :ref:`I/Q Correction <fmcomms2 common iq-correction>`
   #. :ref:`IQ rotation and phase sync <fmcomms2 common iq-rotation>`

#. :ref:`Help and Support <fmcomms4 help-and-support>`

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

- `Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and RF Blockset (formerly SimRF) <https://www.mathworks.com/videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`_
- `Getting Started with Software-Defined Radio using MATLAB and Simulink <https://www.mathworks.com/videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`_

Warning
-------------------------------------------------------------------------------

.. esd-warning::

.. _fmcomms4 help-and-support:

Help and support
-------------------------------------------------------------------------------

For questions and more information, please visit the :ez:`/` technical support
community.
