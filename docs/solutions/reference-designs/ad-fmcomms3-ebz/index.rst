.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms3-ebz

.. _ad-fmcomms3-ebz:

AD-FMCOMMS3-EBZ
===============

AD9361 Wideband Software Defined Radio Board.

.. figure:: ad9361_top_layer.png
   :align: center
   :height: 400px
   :width: 400px

The :adi:`AD-FMCOMMS3-EBZ` is an FMC board for the
:adi:`AD9361`, a highly integrated RF Agile Transceiver™. 
Information on the card, and how to use it, the design package that
surrounds it, and the software which can make it work, can be found
here.

The purpose of the :adi:`AD-FMCOMMS3-EBZ` is to provide an RF platform to
software developers, system architects, etc, who want a single platform
which operates over a much wider tuning range (70 MHz – 6 GHz). It’s
expected that the RF performance of this platform can meet the datasheet
specifications at 2.4 GHz, but not at the entire RF tuning range that
the board supports (but it will work **much** better than the
:dokuwiki:`AD-FMCOMMS2-EBZ <resources/eval/user-guides/ad-fmcomms2-ebz>`
over the complete RF frequency). We will provide typical performance
data for the entire range (70 MHz – 6 GHz) which is supported by the
platform. This is primarily for system investigation and bring up of
various waveforms from a software team before their custom hardware is
complete, where they want to see waveforms, but are not concerned about
the last 1dB or 1% EVM of performance.

The :adi:`AD-FMCOMMS3-EBZ` board is very similar to the
:dokuwiki:`AD-FMCOMMS2-EBZ <resources/eval/user-guides/ad-fmcomms2-ebz>`
board with only one exception, the Rx/Tx RF differential to single ended
transformer. The AD-FMCOMMS3-EBZ is more targetted for wider tuning
range applications, that is why we use the
:download:`TCM1-63AX+ <tcm1-63ax+.pdf>` from
Mini-Circuits as the RF transformer of choice. We affectionately call
the AD-FMCOMMS3-EBZ the “Software Engineers” platform, and the
:adi:`AD-FMCOMMS2-EBZ`, the “RF Engineers” platform to denote 
the difference.

#. :adi:`Purchase <ad-fmcomms3-ebz#eb-buy>`

#. :dokuwiki:`Introduction
   <resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`

#. :dokuwiki:`FMCOMMS3 Hardware
   <resources/eval/user-guides/ad-fmcomms3-ebz/hardware>`:
   
   This provides a brief description of the AD-FMCOMMS3-EBZ board by
   itself, and is a good reference for those who want to understand a
   little more about the board. If you just want to use the board, you
   can skip this section, and come back to it when you want to
   incorporate the AD9361 into your product.

   #. :dokuwiki:`Hardware <resources/eval/user-guides/ad-fmcomms3-ebz/hardware>`
      (including
      :dokuwiki:`schematics
      <=resources/eval/user-guides/ad-fmcomms3-ebz/hardware#downloads>`)

   #. :dokuwiki:`Functional Overview & Specifications
      <resources/eval/user-guides/ad-fmcomms2-ebz/hardware/functional_overview>`

   #. :dokuwiki:`Characteristics & Performance
      <resources/eval/user-guides/ad-fmcomms3-ebz/hardware/card_specification>`

   #. :dokuwiki:`Configuration options
      <resources/eval/user-guides/ad-fmcomms3-ebz/hardware/configuration_options>`

   #. :dokuwiki:`FCC or CE certification
      <resources/eval/user-guides/ad-fmcomms2-ebz/certification>`

   #. :dokuwiki:`Tuning the system
      <resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`

   #. :dokuwiki:`Production Testing Process
      <resources/eval/user-guides/ad-fmcomms2-ebz/testing>`

#. Use the AD-FMCOMMS3-EBZ Board to better understand the AD9361

   #. :dokuwiki:`What you need to get started
      <resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`

   #. :dokuwiki:`Quick Start Guides
      <resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`

      #. :dokuwiki:`Linux on ZC702, ZC706, ZED
         <resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`

      #. :dokuwiki:`Linux on ZCU102
         <resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynqmp>`

      #. :dokuwiki:`Linux on KC705, VC707
         <resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/microblaze>`

      #. :dokuwiki:`Configure a pre-existing SD-Card
         <resources/tools-software/linux-software/zynq_images#preparing_the_image>`

      #. :dokuwiki:`Update the old card you received with your hardware
         <resources/tools-software/linux-software/zynq_images#staying_up_to_date>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

      #. :dokuwiki:`AD936X Control IIO Scope Plugin
         <resources/tools-software/linux-software/fmcomms2_plugin>`

      #. :dokuwiki:`AD936X Advanced Control IIO Scope Plugin
         <resources/tools-software/linux-software/fmcomms2_advanced_plugin>`

      #. :dokuwiki:`Command Line/Shell scripts
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   #. Push custom data into/out of the AD-FMCOMMS3-EBZ

      #. :doc:`Basic Data files and formats
         </solutions/reference-designs/fmcomms2/common/basic_iq_datafiles>`

      #. :dokuwiki:`Create and analyze data files in MATLAB
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`

      #. :dokuwiki:`Stream data into/out of MATLAB
         <resources/tools-software/transceiver-toolbox>`

      #. :dokuwiki:`AD9361 libiio streaming example
         <resources/tools-software/linux-software/libiio#libiio_-_ad9361_iio_streaming_example>`

      #. :dokuwiki:`Python Interfaces
         <resources/tools-software/linux-software/pyadi-iio>`

#. Design with the AD9361

   #. :dokuwiki:`Understanding the AD9361
      <resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`

      #. :adi:`AD9361 Product page <AD9361>`

      #. :adi:`Full Datasheet and chip design package
         <hrfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`

      #. :dokuwiki:`MATLAB Filter Design Wizard for AD9361
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`

   #. Simulation

      #. :dokuwiki:`MathWorks SimRF Models of the AD9361
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`

      #. :dokuwiki:`Installing RF Blockset Models for AD9361
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/rfblkset_mdls_install>`

      #. :dokuwiki:`Running the AD9361 Receive Testbench
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/rfblkset_mdls_run_testbench>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. :dokuwiki:`Analog Devices Transceiver Toolbox for MATLAB and Simulink
         <resources/tools-software/transceiver-toolbox>`

      #. MATLAB/Simulink Examples

         #. :dokuwiki:`Stream data into/out of MATLAB
            <resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`

         #. :dokuwiki:`Beacon Frame Receiver Example
            <resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink#beacon_frame_receiver_example>`

         #. :doc:`QPSK Transmit and Receive Example
            </solutions/reference-designs/fmcomms2/software/qpsk_example>`

         #. :doc:`LTE Transmit and Receive Example
            </solutions/reference-designs/fmcomms2/software/lte_example>`

         #. :dokuwiki:`ADS-B Airplane Tracking Example
            <resources/tools-software/linux-software/libiio/clients/adsb_example>`

      #. :dokuwiki:`GNU Radio
         <resources/tools-software/linux-software/gnuradio>`

      #. :dokuwiki:`FM Radio/Tuner <resources/tools-software/fm-radio>`
         (listen to FM signals on the HDMI monitor)

      #. :dokuwiki:`C example
         <resources/tools-software/linux-software/libiio#libiio_-_ad9361_iio_streaming_example>`

   #. Targeting

      #. :dokuwiki:`Analog Devices BSP for MathWorks HDL Workflow Advisor (To be depreciated)
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`

      #. :dokuwiki:`Analog Devices Transceiver Toolbox for MATLAB and Simulink
         <resources/tools-software/transceiver-toolbox>`

   #. Complete Workflow

      #. :dokuwiki:`ADS-B Airplane Tracking Tutorial
         <resources/eval/user-guides/picozed_sdr/tutorials/adsb>`

      #. :dokuwiki:`Frequency Hopping Controller
         <resources/eval/user-guides/adrv936x_rfsom/tutorials/frequency_hopping>`

   #. Design a custom AD9361 based platform

      #. :dokuwiki:`Linux software
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`

         #. :dokuwiki:`Linux Device Driver
            <resources/tools-software/linux-drivers/iio-transceiver/ad9361>`

         #. :dokuwiki:`Build the demo on ZC702, ZC706, or ZED from source
            <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`

         #. :dokuwiki:`Build ZynqMP/MPSoC Linux kernel and devicetrees from source
            <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`

         #. :dokuwiki:`Build the demo on KC705 or VC707 for Microblaze from source
            <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`

         #. :dokuwiki:`Build the 2015_R2 Release Linux kernel from source
            <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2015r2>`

         #. :doc:`Customizing the devicetree on the target
            </linux/kernel/zynq_tips_tricks>`

      #. :dokuwiki:`No-OS Driver
         <resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`

      #. :dokuwiki:`HDL Reference Design
         <resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`
         which you must use in your FPGA.

         #. :dokuwiki:`Digital Interface Timing Validation
            <resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`

#. Additional Documentation about SDR Signal Chains

   #. :doc:`The math behind the RF
      </solutions/reference-designs/fmcomms2/common/math>`

#. :dokuwiki:`Help and Support
   <resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`

Warning
-------

.. esd-warning::

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 1
   :glob:

   hardware-guide/index
   card-specifications/index
   hardware-guide/config-options/index