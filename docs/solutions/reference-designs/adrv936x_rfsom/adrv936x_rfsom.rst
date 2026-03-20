ADI ADRV936x System on Module (SOM) SDR
=======================================

.. image:: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png
   :alt: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png
   :align: right

The :adi:`ADRV9361-Z7035` and :adi:`ADRV9364-Z7020` are built on a portfolio of highly integrated System-On-Module (SOMs) based on the Xilinx Zynq®-7000 All Programmable (AP)SoC.

:adi:`ADRV9361-Z7035` is built on the Analog Devices :adi:`AD9361` and the Xilinx XC7Z035-L2FBG676I, it is schematically & HDL similar to the `ad-fmcomms3-ebz <https://wiki.analog.com/ad-fmcomms3-ebz>`_. It requires Vivado license.

:adi:`ADRV9364-Z7020` is built on the :adi:`AD9361` and the Xilinx XC7Z020-1CLG400I, it is schematically & HDL similar to the `ad-fmcomms4-ebz <https://wiki.analog.com/ad-fmcomms4-ebz>`_.

The purpose of the RF SOM is to provide an RF platform to software developers, system architects, product developers, etc, who want a single platform which operates over a wide tuning range (70 MHz – 6 GHz) that is capable of both being used for prototype, evaluation and reference design to help with production volume.

Table of Contents
-----------------

-  Introduction

   -  `Introduction to boards based on the AD9361 <https://wiki.analog.com/resources/eval/user-guides/adrv936x/introduction>`_
   -  :doc:`Introduction to ADRV9361-Z7035 </solutions/reference-designs/adrv936x_rfsom/user-guide/introduction>`
   -  `ADRV9361-Z7035 Quick start guide <https://wiki.analog.com/resources/eval/user-guides/adrv9361-z7035/quickstart>`_

-  Hardware

   -  :doc:`Schematic and Layout revisions </solutions/reference-designs/adrv936x_rfsom/hardware>`
   -  `Power and Sequencing <https://wiki.analog.com/resources/eval/user-guides/pzsdr/power-and-sequencing>`_
   -  `Performance <https://wiki.analog.com/resources/eval/user-guides/adrv9361-z7035/performance>`_
   -  `Electrical specifications <https://wiki.analog.com/resources/eval/user-guides/adrv9361-z7035/electrical-specifications>`_
   -  `Cable brackets <https://wiki.analog.com/resources/eval/user-guides/pzsdr/cable-brackets>`_
   -  :doc:`Additional information </solutions/reference-designs/adrv936x_rfsom/user-guide/additional-information>`
   -  :doc:`Certifications and Environmental Testing </solutions/reference-designs/adrv936x_rfsom/testing>`

-  Carriers

   -  `FMC Carrier (ADRV1CRR-FMC) <https://wiki.analog.com/resources/eval/user-guides/pzsdr/carriers/fmc>`_
   -  `Breakout Carrier (ADRV1CRR-BOB) <https://wiki.analog.com/resources/eval/user-guides/pzsdr/carriers/brk>`_
   -  `PCIe Carrier (PZSDRCC-PCIE) <https://wiki.analog.com/resources/eval/user-guides/pzsdr/carriers/pcie>`_
   -  `PackRF Carrier (PZSDRCC-PackRF) <https://wiki.analog.com/resources/eval/user-guides/pzsdr/carriers/packrf>`_

-  Use the RF SOM Hardware to better understand the AD9361

   -  `What you need to get started <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`_
   -  `Quick Start Guides <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`_

      -  `Linux on RF SOM <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`_
      -  `Configure a pre-existing SD-Card <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
      -  `Update the old card you received with your hardware <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_
      -  `AD9361 Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_plugin>`_
      -  `AD9361 Advanced Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`_
      -  `Command Line/Shell scripts <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`_

   -  Push custom data into/out of the RF SOM SDR.

      -  `Basic Data files and formats <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`_
      -  `Create and analyze data files in MATLAB <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`_
      -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`_
      -  `AD9361 libiio streaming example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

-  Design with the AD9361

   -  `Understanding the AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`_

      -  :adi:`AD9361 Product page <AD9361>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  `MATLAB Filter Design Wizard for AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`_

   -  `Tuning the AD9361/AD9364 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`_
   -  Simulation

      -  `MathWorks SimRF Models of the AD9361 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`_

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`_
         -  `Beacon Frame Receiver Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`_
         -  `QPSK Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/qpsk_example>`_
         -  `LTE Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/lte_example>`_
         -  `ADS-B Airplane Tracking Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/adsb_example>`_
         -  `AGC Optimization Example <https://wiki.analog.com/resources/eval/user-guides/ad9361_agc_tuning>`_

      -  `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_
      -  `FM Radio/Tuner <https://wiki.analog.com/resources/tools-software/fm-radio>`_ (listen to FM signals on the HDMI monitor)
      -  `C example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

   -  Targeting

      -  `Analog Devices BSP for MathWorks HDL Workflow Advisor <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`_

   -  Complete Workflow

      -  `ADS-B Airplane Tracking Tutorial <https://wiki.analog.com/resources/eval/user-guides/picozed_sdr/tutorials/adsb>`_
      -  :doc:`Frequency Hopping Controller </solutions/reference-designs/adrv936x_rfsom/tutorials/frequency_hopping>`
      -  `QPSK Modem Design Workflow <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem>`_
      -  :doc:`Implementing a Loopback Delay Estimation Algorithm </solutions/reference-designs/adrv936x_rfsom/tutorials/loopback_delay_estimation>`

   -  Design a custom AD9361 based platform

      -  `Linux software <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`_

         -  `Linux Device Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`_
         -  `Build the demo on ZC702, ZC706, or ZED from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`_
         -  `Build the demo on KC705 or VC707 for Microblaze from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`_
         -  `Build the 2014_R2 Release Linux kernel from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`_
         -  `Customizing the devicetree on the target <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`_

      -  `No-OS Driver <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`_
      -  `HDL Reference Design <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`_ which you must use in your FPGA.

         -  `Digital Interface Timing Validation <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`_

-  Additional Documentation about SDR Signal Chains

   -  `The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/math>`_

-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_
-  Videos and Webinars

   -  `Radio Deployment on SoC Platforms <https://www.mathworks.com/videos/radio-deployment-on-soc-platforms-1513346830203.html>`_

Warning
-------

.. esd-warning::
