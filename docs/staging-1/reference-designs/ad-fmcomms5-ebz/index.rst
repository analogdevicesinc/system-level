.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms5-ebz

.. _ad-fmcomms5-ebz:

AD-FMCOMMS5-EBZ User Guide
==========================

For many Broadband Wireless Access (BWA) systems, Multi Input – Multi Output
(`SIMO / MISO / SU-MIMO / MU-MIMO <https://en.wikipedia.org/wiki/MIMO>`__)
operation and RF beamforming are proven techniques for maximizing throughput and
efficient spectrum utilization. Modern integrated devices with multi-channel RX
and multi-channel TX capability such as the AD9361 make developing MIMO systems
with high performance and linearity utilizing integrated receivers,
transmitters, and synthesizers a simpler task.

Some systems may require more complex configurations that combine multiple
devices. Operating multiple devices while trying to coordinate data for each
channel of each device is not practical for devices that operate independently
without any mechanism for aligning data timing. Data synchronization into and
out of multiple devices is required to implement such configurations. The
:adi:`AD-FMComms5-EBZ` is a FMC board for the :adi:`AD9361`, a highly integrated
RF Agile Transceiver™, which demonstrates how to design a platform based on
multiple devices.

For MIMO systems requiring more than two input or two output channels, multiple
AD9361 devices and a common reference oscillator are required. The AD9361
provides the capability to accept an external reference clock and synchronize
operation with other devices using simple control logic. Each AD9361 includes
its own baseband PLL that generates sampling and data clocks from the reference
clock input, so an additional control mechanism is required to synchronize
multiple devices.

The complete chip level design package can be found on the
:adi:`the ADI web site <ad9361_design_files>`. Information on the card, and how
to use it, the design package that surrounds it, and the software which can make
it work, can be found below in the Table of Contents.

The purpose of the AD-FMCOMMS5-EBZ is to provide a platform to which shows how
to connect and synchronize (at the RF side) multiple AD9361s for
`SIMO / MISO / SU-MIMO / MU-MIMO <https://en.wikipedia.org/wiki/MIMO>`__
applications. To help with algorithm array processing development, there are a
variety of things that can be done, from purchasing complete solutions:

- :xilinx:`MIMO receiver <products/intellectual-property/do-di-mimoenc-lte.html>`
- :xilinx:`MIMO transmitter <products/intellectual-property/ef-di-mimodec-lte.html>`

To creating your own with something like
:mw:`Phased Array System Toolbox <products/phased-array/>`.

If you are just starting a design, or investigating the AD9361 for the first
time, it"s suggested to get familiar with the single AD9361 based platforms
(:dokuwiki:`./AD-FMCOMMS2-EBZ </AD-FMCOMMS2-EBZ>` or
:dokuwiki:`./AD-FMCOMMS3-EBZ </AD-FMCOMMS3-EBZ>`) first.

Note that the AD-FMCOMMS5-EBZ uses a dual FMC connector. This means the base
board requires two adjacent FMC connectors. Suitable base boards for example are
ZC702 and ZC706.

Table of Contents
-----------------

.. figure:: http://www.analog.com/-/media/analog/en/evaluation-board-images/images/ad-fmcomms5-ebz.ashx

#. :dokuwiki:`Introduction <ad-fmcomms2-ebz/introduction>`
#. :dokuwiki:`FMCOMMS5 Hardware <ad-fmcomms5-ebz/hardware>`: This provides a
   brief description of the AD-FMCOMMS5-EBZ board by itself, and is a good
   reference for those who want to understand a little more about the board. If
   you just want to use the board, you can skip this section, and come back to
   it when you want to incorporate the AD9361 into your product.

   #. :dokuwiki:`Hardware <ad-fmcomms5-ebz/hardware>` (including
      :dokuwiki:`schematics </ad-fmcomms5-ebz/hardware#downloads>`)

      #. :dokuwiki:`Functional Overview & Specifications <ad-fmcomms2-ebz/hardware/functional_overview>`
      #. :dokuwiki:`Characteristics & Performance <ad-fmcomms2-ebz/hardware/card_specification>`
      #. :dokuwiki:`Configuration options <ad-fmcomms5-ebz/hardware/configuration_options>`

   #.  :dokuwiki:`Production Testing Process <ad-fmcomms2-ebz/testing>`

#. Use the AD-FMCOMMS5-EBZ Board to better understand the AD9361

   #. :dokuwiki:`What you need to get started <ad-fmcomms2-ebz/prerequisites>`
   #. :dokuwiki:`Quick Start Guides <ad-fmcomms2-ebz/quickstart>`

      #. :dokuwiki:`Linux on ZC702, ZC706, ZED <ad-fmcomms2-ebz/quickstart/zynq>`
      #. :dokuwiki:`Linux on KC705, VC707 <ad-fmcomms2-ebz/quickstart/microblaze>`
      #. :dokuwiki:`Configure a pre-existing SD-Card </resources/tools-software/linux-software/zynq_images#preparing_the_image>`
      #. :dokuwiki:`Update the old card you received with your hardware </resources/tools-software/linux-software/zynq_images#staying_up_to_date>`

   #. Linux Applications

      #. :dokuwiki:`IIO Scope <resources/tools-software/linux-software/iio_oscilloscope>`
      #. :dokuwiki:`FMCOMMS5 Control IIO Scope Plugin <resources/tools-software/linux-software/fmcomms5_plugin>`
      #. :dokuwiki:`FMCOMMS2/3/4/5 Advanced Control IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      #. :dokuwiki:`FMComms5 Phase Sync Procedure </resources/eval/user-guides/ad-fmcomms5-ebz/phase-sync>`
      #. :dokuwiki:`Command Line/Shell scripts <ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   #. Push custom data into/out of the AD-FMCOMMS5-EBZ

      #. :dokuwiki:`Basic Data files and formats <ad-fmcomms2-ebz/software/basic_iq_datafiles>`
      #. :dokuwiki:`Create and analyze data files in MATLAB <ad-fmcomms2-ebz/software/datafiles>`
      #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      #. :dokuwiki:`AD9361 libiio streaming example </resources/tools-software/linux-software/libiio#libiio_-_ad9361_iio_streaming_example>`

#. Design with the AD9361

   #. :dokuwiki:`Understanding the AD9361 <ad-fmcomms2-ebz/ad9361>`

      #. :adi:`AD9361 Product page <AD9361>`
      #. :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      #. :dokuwiki:`MATLAB Filter Design Wizard for AD9361 <ad-fmcomms2-ebz/software/filters>`

   #. Designing with multiple AD9361s.

      #. :dokuwiki:`Multi-Chip Sync(MCS) <ad-fmcomms5-ebz/multi-chip-sync>`,
         synchronization of multiple devices

   #. Simulation

      #. :dokuwiki:`MathWorks SimRF Models of the AD9361 <ad-fmcomms2-ebz/software/simrf>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. MATLAB/Simulink Examples

         #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         #. :dokuwiki:`Beacon Frame Receiver Example </resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink#beacon_frame_receiver_example>`
         #. :dokuwiki:`QPSK Transmit and Receive Example </resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         #. :dokuwiki:`LTE Transmit and Receive Example </resources/tools-software/linux-software/libiio/clients/lte_example>`

      #. :dokuwiki:`GNU Radio </resources/tools-software/linux-software/gnuradio>`
      #. :dokuwiki:`FM Radio/Tuner </resources/tools-software/fm-radio>` (listen
         to FM signals on the HDMI monitor)
      #. :dokuwiki:`C example </resources/tools-software/linux-software/libiio#libiio_-_ad9361_iio_streaming_example>`

   #. Design a custom AD9361 based platform

      #. :dokuwiki:`Linux software <ad-fmcomms2-ebz/software/linux>`

         #. :dokuwiki:`Linux Device Driver </resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         #. :dokuwiki:`Build the demo on ZC702, ZC706, or ZED from source <ad-fmcomms2-ebz/software/linux/zynq>`
         #. :dokuwiki:`Build the demo on KC705 or VC707 for Microblaze from source <ad-fmcomms2-ebz/software/linux/microblaze>`
         #. :dokuwiki:`Build the 2014_R2 Release Linux kernel from source <ad-fmcomms2-ebz/software/linux/zynq_2014r2>`
         #. :dokuwiki:`Customizing the devicetree on the target <ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

      #. :dokuwiki:`No-OS Driver <ad-fmcomms2-ebz/software/baremetal>`
      #. :dokuwiki:`HDL Reference Design <ad-fmcomms2-ebz/reference_hdl>` which
         you must use in your FPGA.

         #. :dokuwiki:`Digital Interface Timing Validation <ad-fmcomms2-ebz/interface_timing_validation>`

#. Additional Documentation about SDR Signal Chains

   #. :dokuwiki:`The math behind the RF <ad-fmcomms1-ebz/math>`
   #. :dokuwiki:`IQ rotation, and phase sync <ad-fmcomms2-ebz/iq_rotation>`

#. :dokuwiki:`Help and Support <ad-fmcomms2-ebz/help_and_support>`

Videos
------

.. todo:: .. include: /ad-fmcomms2-ebz.rst

   :start-after: .. start-videos
   :end-before: .. end-videos

Presentations
-------------

-
  :adi:`Developing Multiple-Input Multiple-Output (MIMO) Systems with the AD9361 <en/education/education-library/webcasts/developing-multiple-input-multiple-output.html>`
  As Software Defined Radio (SDR) and Multiple-Input Multiple-Output (MIMO)
  become more prevalent there is a need for more channel diversity. This webcast
  will detail how to use multiple AD9361 devices to create an NxN MIMO system,
  as well as explore the available tradeoffs in the design. The AD9361 is a
  fully integrated 2x2 MIMO transceiver. Its programmability and wideband
  capability make it ideal for a broad range of transceiver applications.

Warning
~~~~~~~

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning
