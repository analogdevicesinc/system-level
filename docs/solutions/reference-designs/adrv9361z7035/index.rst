.. _adrv9361z7035:

ADRV9361-Z7035
==============

.. image:: images/picozed_hand.png
   :alt: PicoZed hand comparison
   :align: right

The :adi:`ADRV9361-Z7035` is built on a portfolio of highly integrated
System-On-Module (SOMs) based on the Xilinx Zynq®-7000 All Programmable (AP)SoC.
Starting with the AD9361, it is schematically & HDL similar to the
:external+hdl:ref:`AD-FMCOMMS3-EBZ <fmcomms2>`.

The purpose of the :adi:`ADRV9361-Z7035` RF SOM is to provide an RF platform to
software developers, system architects, product developers, etc, who want a
single platform operating over a wide tuning range (70 MHz - 6 GHz) that is
capable of being used for prototype, evaluation and reference design to help
with production volume.

.. toctree::
   :hidden:

   introduction
   prerequisites
   mechanical
   electrical-specifications
   performance
   quickstart
   revision-history

Table of Contents
-----------------

- :ref:`Introduction to the AD9361 <fmcomms2 common introduction>`
- :ref:`Introduction <fmcomms2>`
- :ref:`Tuning the system <fmcomms2 hardware tuning>`
- ADRV9361-Z7035 Hardware

   -  :ref:`Introduction <adrv9361z7035 introduction>`
   -  :ref:`Prerequisites <adrv9361z7035 prerequisites>`
   -  :ref:`Quick Start <adrv9361z7035 quickstart>`
   -  :ref:`Mechanical Design <adrv9361z7035 mechanical>`
   -  :ref:`Electrical Specifications <adrv9361z7035 electrical_specifications>`
   -  :ref:`Performance <adrv9361z7035 performance>`

      -  :doc:`Power and Sequencing </solutions/reference-designs/pzsdr/power-and-sequencing>`

   -  :ref:`Revision History <adrv9361z7035 revision_history>`

      -  including schematics and BOM

   -  Carriers

      -  :doc:`FMC Carrier (PZSDRCC-FMC) </solutions/reference-designs/pzsdr/carriers/fmc>`
      -  :doc:`Breakout Carrier (PZSDRCC-BRK) </solutions/reference-designs/pzsdr/carriers/brk>`
      -  :doc:`PCIe Carrier (PZSDRCC-PCIE) </solutions/reference-designs/pzsdr/carriers/pcie>`
      -  :doc:`PackRF Carrier (PZSDRCC-PackRF) </solutions/reference-designs/pzsdr/carriers/packrf>`

- Use the RF SOM Hardware to better understand the AD9361

   -  :ref:`What you need to get started <fmcomms2 prerequisites>`
   -  :ref:`Quick Start Guides <fmcomms2 quickstart>`

      -  :ref:`Linux on RF SOM <fmcomms2 quickstart zed>`
      -  :ref:`Configure a pre-existing SD-Card <kuiper>`
      -  :ref:`Update the old card you received with your hardware <kuiper>`

   -  Basic Applications

      -  :ref:`IIO Scope <iio-oscilloscope>`
      -  :ref:`AD9361 Control IIO Scope Plugin <fmcomms2 software ad9361-plugin>`
      -  :ref:`AD9361 Advanced Control IIO Scope Plugin <fmcomms2 software ad9361-advanced-plugin>`
      -  :ref:`Command Line/Shell scripts <software shell-scripts>`

   -  Push custom data into/out of the RF SOM SDR.

      -  :ref:`Basic Data files and formats <fmcomms2 common basic-iq-datafiles>`
      -  :ref:`Create and analyze data files in MATLAB <fmcomms2 common datafiles>`
      -  :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
      -  :ref:`AD9361 libiio streaming example <libiio>`

- Design with the AD9361

   -  :ref:`Understanding the AD9361 <fmcomms2 common ad9361>`

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  :ref:`MATLAB Filter Design Wizard for AD9361 <fmcomms2 software filters>`

   -  Simulation

      -  :ref:`MathWorks RF Blockset Models of the AD9361 <fmcomms2 software simrf>`

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
         -  :ref:`Beacon Frame Receiver Example <fmcomms2 software beacon-frame-receiver>`
         -  :ref:`QPSK Transmit and Receive Example <fmcomms2 software qpsk-example>`
         -  :ref:`LTE Transmit and Receive Example <fmcomms2 software lte-example>`
         -  :ref:`ADS-B Airplane Tracking Example <fmcomms2 software adsb-example>`

      -  :ref:`GNU Radio <software gnuradio>`
      -  :ref:`FM Radio/Tuner <fmcomms2 software fm-radio>` (listen to FM signals on the HDMI monitor)
      -  :ref:`C example <libiio>`

   -  Targeting

      -  :ref:`Analog Devices BSP for MathWorks HDL Workflow Advisor <matlab transceiver-toolbox>`

   -  Complete Workflow

      -  :ref:`ADS-B Airplane Tracking Tutorial <fmcomms2 software adsb-tutorial>`
      -  :dokuwiki:`QPSK Modem Design Workflow <resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem>`

   -  Design a custom AD9361 based platform

      -  :ref:`Linux software <fmcomms2 software linux>`

         -  Linux resources:

            - :external+linux:ref:`Linux AD9361 Device Driver <ad9361>`
            - :external+linux:ref:`Linux AD9361 Device Driver Customization <ad9361-customization>`

         -  :ref:`Building Zynq Linux kernel and devicetree <linux-kernel zynq>`
         -  :ref:`Customizing the devicetree on the target <linux-kernel zynq-tips-tricks>`

      -  :dokuwiki:`No-OS Driver <resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`

      -  :external+hdl:ref:`HDL Reference Design <adrv9361z7035>` which you must
         use in your FPGA.

         -  :ref:`Digital Interface Timing Validation <fmcomms2 common interface-timing-validation>`

- Additional Documentation about SDR Signal Chains

   -  :ref:`The math behind the RF <fmcomms2 common fmcomms-math>`

- :ref:`Help and Support <fmcomms2 help-and-support>`
- Videos and Webinars

   -  `Radio Deployment on SoC Platforms <https://www.mathworks.com/videos/radio-deployment-on-soc-platforms-1513346830203.html>`_

Warning
-------

.. esd-warning::
