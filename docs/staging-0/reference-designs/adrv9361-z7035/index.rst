.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9361-z7035

.. _adrv9361-z7035:

ADRV9361-Z7035 System on Module (SOM) SDR
=========================================

.. figure:: http://picozed.org/sites/default/files/styles/product_slider/public/product/hand.png

The :adi:`ADRV9361-Z7035` is built on a portfolio of highly integrated
System-On-Module (SOMs) based on the Xilinx Zynq®-7000 All Programmable (AP)SoC.
Starting with the AD9361, it is schematically & HDL similar to the
:dokuwiki:`AD-FMCOMMS3-EBZ </resources/eval/user-guides/AD-FMCOMMS3-EBZ>`.

The purpose of the :adi:`ADRV9361-Z7035` RF SOM is to provide an RF platform to
software developers, system architects, product developers, etc, who want a
single platform operating over a wide tuning range (70 MHz – 6 GHz) that is
capable of being used for prototype, evaluation and reference design to help
with production volume.

Table of Contents
-----------------

#. :dokuwiki:`Introduction to the AD9361. </resources/eval/user-guides/AD9361>`
#. :dokuwiki:`Introduction <ad-fmcomms2-ebz/introduction>`
#. :dokuwiki:`Tuning the system <ad-fmcomms2-ebz/hardware/tuning>`
#. :dokuwiki:`Introduction to Boards Based on the AD9361. </adrv9361-Z7035/introduction>`
#. ADRV9361-Z7035 Hardware

   #. :dokuwiki:`Mechanical Design </adrv9361-Z7035/Mechanical>`
   #. :dokuwiki:`Electrical Specifications </adrv9361-Z7035/Electrical-Specifications>`
   #. :dokuwiki:`Performance </adrv9361-Z7035/Performance>`

      #. :dokuwiki:`Power and Sequencing <pzsdr/power-and-sequencing>`

   #. :dokuwiki:`Revision History </adrv9361-Z7035/Revision-History>`

      #. including schematics and BOM

   #. Carriers

      #. :dokuwiki:`FMC Carrier (PZSDRCC-FMC) <pzsdr/carriers/fmc>`
      #. :dokuwiki:`Breakout Carrier (PZSDRCC-BRK) <pzsdr/carriers/brk>`
      #. :dokuwiki:`PCIe Carrier (PZSDRCC-PCIE) <pzsdr/carriers/pcie>`
      #. :dokuwiki:`PackRF Carrier (PZSDRCC-PackRF) <pzsdr/carriers/packrf>`

#. Use the RF SOM Hardware to better understand the AD9361

   #. :dokuwiki:`What you need to get started <ad-fmcomms2-ebz/prerequisites>`
   #. :dokuwiki:`Quick Start Guides <ad-fmcomms2-ebz/quickstart>`

      #. :dokuwiki:`Linux on RF SOM <ad-fmcomms2-ebz/quickstart/zynq>`
      #. :ref:`kuiper`
      #. :ref:`kuiper`

   #. Basic Applications

      #. :dokuwiki:`IIO Scope <resources/tools-software/linux-software/iio_oscilloscope>`
      #. :dokuwiki:`AD9361 Control IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_plugin>`
      #. :dokuwiki:`AD9361 Advanced Control IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      #. :dokuwiki:`Command Line/Shell scripts <ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   #. Push custom data into/out of the RF SOM SDR.

      #. :dokuwiki:`Basic Data files and formats <ad-fmcomms2-ebz/software/basic_iq_datafiles>`
      #. :dokuwiki:`Create and analyze data files in MATLAB <ad-fmcomms2-ebz/software/datafiles>`
      #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      #. :dokuwiki:`AD9361 libiio streaming example </resources/tools-software/linux-software/libiio#libiio_-_ad9361_iio_streaming_example>`

#. Design with the AD9361

   #. :dokuwiki:`Understanding the AD9361 <ad-fmcomms2-ebz/ad9361>`

      #. :adi:`AD9361 Product page <AD9361>`
      #. :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      #. :dokuwiki:`MATLAB Filter Design Wizard for AD9361 <ad-fmcomms2-ebz/software/filters>`

   #. Simulation

      #. :dokuwiki:`MathWorks RF Blockset Models of the AD9361 <ad-fmcomms2-ebz/software/simrf>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. MATLAB/Simulink Examples

         #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         #. :dokuwiki:`Beacon Frame Receiver Example </resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink#beacon_frame_receiver_example>`
         #. :dokuwiki:`QPSK Transmit and Receive Example </resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         #. :dokuwiki:`LTE Transmit and Receive Example </resources/tools-software/linux-software/libiio/clients/lte_example>`
         #. :dokuwiki:`ADS-B Airplane Tracking Example </resources/tools-software/linux-software/libiio/clients/adsb_example>`

      #. :dokuwiki:`GNU Radio </resources/tools-software/linux-software/gnuradio>`
      #. :dokuwiki:`FM Radio/Tuner </resources/tools-software/fm-radio>` (listen
         to FM signals on the HDMI monitor)
      #. :dokuwiki:`C example </resources/tools-software/linux-software/libiio#libiio_-_ad9361_iio_streaming_example>`

   #. Targeting

      #. :dokuwiki:`Analog Devices BSP for MathWorks HDL Workflow Advisor </resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`

   #. Complete Workflow

      #. :dokuwiki:`ADS-B Airplane Tracking Tutorial </resources/eval/user-guides/picozed_sdr/tutorials/adsb>`
      #. :dokuwiki:`QPSK Modem Design Workflow </resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem>`

   #. Design a custom AD9361 based platform

      #. :dokuwiki:`Linux software <ad-fmcomms2-ebz/software/linux>`

         #. :dokuwiki:`Linux Device Driver </resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         #. :dokuwiki:`Build the 2014_R2 Release Linux kernel from source <ad-fmcomms2-ebz/software/linux/zynq_2014r2>`
         #. :dokuwiki:`Customizing the devicetree on the target <ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

      #. :dokuwiki:`No-OS Driver <ad-fmcomms2-ebz/software/baremetal>`
      #. :dokuwiki:`HDL Reference Design <ad-fmcomms2-ebz/reference_hdl>` which
         you must use in your FPGA.

         #. :dokuwiki:`Digital Interface Timing Validation <ad-fmcomms2-ebz/interface_timing_validation>`

#. Additional Documentation about SDR Signal Chains

   #. :dokuwiki:`The math behind the RF <ad-fmcomms1-ebz/math>`

#. :dokuwiki:`Help and Support <ad-fmcomms2-ebz/help_and_support>`
#. Videos and Webinars

   #. :mw:`Radio Deployment on SoC Platforms </videos/radio-deployment-on-soc-platforms-1513346830203.html>`

Warning
-------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning
