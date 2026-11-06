.. _adrv9364z7020:

ADRV9364-Z7020 System on Module (SOM) SDR
===============================================================================

.. image:: images/adrv9364z7020.jpg
   :align: right
   :width: 400

The :adi:`ADRV9364-Z7020 <ADRV9364>` is built on a portfolio of highly
integrated System-On-Module (SOMs) based on the Xilinx Zynq®-7000 All
Programmable (AP)SoC. Built on the AD9364, it is schematically & HDL similar to
the :dokuwiki:`AD-FMCOMMS4-EBZ <resources/eval/user-guides/ad-fmcomms4-ebz>`.

The purpose of the SDR is to provide an RF platform to software developers,
system architects, product developers, etc, who want a single platform which
operates over a wide tuning range (70 MHz – 6 GHz) that is capable of being
used for prototyping, evaluation, and as a reference design to help with
production volume.

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Table of Contents
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to :ref:`ask <help-and-support>`.

#. :adi:`Purchase <ADRV9364>`

#. :ref:`Introduction to boards based on the AD9361 <fmcomms2 common introduction>`

#. :dokuwiki:`RF SOM Hardware <resources/eval/user-guides/adrv936x_rfsom/hardware>`

#. :ref:`Tuning the system <fmcomms2 hardware tuning>`

#. Use the RF SOM Hardware to better understand the AD9364

   #. :ref:`What you need to get started <fmcomms2 prerequisites>`
   #. :ref:`Quick Start Guides <adrv9364z7020 quickstart>`

      #. :ref:`Linux on RF SOM <adrv9364z7020 quickstart adrv1crr-bob>`
      #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :ref:`AD9361 Control IIO Scope Plugin <fmcomms2 software ad9361-plugin>`
      #. :ref:`AD9361 Advanced Control IIO Scope Plugin <fmcomms2 software ad9361-advanced-plugin>`
      #. :ref:`Command Line/Shell scripts <software shell-scripts>`

   #. Push custom data into/out of the RF SOM SDR

      #. :ref:`Basic Data files and formats <fmcomms2 common basic-iq-datafiles>`
      #. :ref:`Create and analyze data files in MATLAB <fmcomms2 common datafiles>`
      #. :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
      #. :ref:`AD9361 libiio streaming example <libiio>`
      #. :dokuwiki:`Python Support with AD9364 Interface Class <resources/tools-software/linux-software/pyadi-iio>`

#. Design with the AD9364

   #. :ref:`Understanding the AD9364 <fmcomms2 common ad9361>`

      #. :adi:`AD9364 Product page <AD9364>`
      #. :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      #. :ref:`MATLAB Filter Design Wizard for AD9361 <fmcomms2 software filters>`

   #. Simulation

      #. :ref:`MathWorks SimRF Models of the AD9361 <fmcomms2 software simrf>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. MATLAB/Simulink Examples

         #. :dokuwiki:`Stream data into/out of MATLAB <resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         #. :ref:`QPSK Transmit and Receive Example <fmcomms2 software qpsk-example>`

      #. :ref:`GNU Radio <software gnuradio>`
      #. :ref:`FM Radio/Tuner <fmcomms2 software fm-radio>`
         (listen to FM signals on the HDMI monitor)
      #. :ref:`C example <libiio>`

   #. Targeting

      #. :dokuwiki:`Analog Devices BSP for MathWorks HDL Workflow Advisor <resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`

   #. Design a custom AD9364-based platform

      #. :ref:`Linux software <fmcomms2 software linux>`

         #. :external+linux:doc:`Linux Device Driver <drivers/iio-transceiver/ad9361>`
         #. :ref:`Build the demo on ZC702, ZC706, or ZED from source <linux-kernel zynq-hdmi>`
         #. :ref:`Build the demo on KC705 or VC707 for Microblaze from source <linux-kernel microblaze>`
         #. :ref:`Build the 2014_R2 Release Linux kernel from source <linux-kernel zynq>`
         #. :ref:`Customizing the devicetree on the target <linux-kernel zynq-tips-tricks>`

      #. :external+no-OS:doc:`No-OS AD9361 project <projects/rf-transceiver/ad9361>`

      #. :external+hdl:ref:`HDL Reference Design <adrv9364z7020>` which you must use in your FPGA.

         #. :ref:`Digital Interface Timing Validation <fmcomms2 common interface-timing-validation>`

#. Additional Documentation about SDR Signal Chains

   #. :ref:`The math behind the RF <fmcomms2 common fmcomms-math>`

#. :ref:`Help and Support <help-and-support>`

ADI Articles
-------------------------------------------------------------------------------

Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio

#. :adi:`Part 1 - The Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
#. :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
#. :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
#. :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
