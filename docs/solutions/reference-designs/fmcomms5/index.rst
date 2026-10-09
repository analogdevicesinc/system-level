.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms5-ebz

.. _ad-fmcomms5-ebz:

AD-FMCOMMS5-EBZ
===============

.. image:: ../images/ad9361_chip_illustration.png
   :align: left
   :width: 150

For many Broadband Wireless Access (BWA) systems, Multi Input – Multi Output
(`SIMO / MISO / SU-MIMO / MU-MIMO <https://en.wikipedia.org/wiki/MIMO>`_)
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
`SIMO / MISO / SU-MIMO / MU-MIMO <https://en.wikipedia.org/wiki/MIMO>`_
applications. To help with algorithm array processing development, there are a
variety of things that can be done, from purchasing complete solutions:

- `MIMO receiver`_
- `MIMO transmitter`_

.. _MIMO receiver:
   https://www.xilinx.com/products/intellectual-property/do-di-mimoenc-lte.html
.. _MIMO transmitter:
   https://www.xilinx.com/products/intellectual-property/ef-di-mimodec-lte.html

To creating your own with something like `Phased Array System Toolbox`_.

.. _Phased Array System Toolbox:
   https://www.mathworks.com/products/phased-array/

If you are just starting a design, or investigating the AD9361 for the first
time, it's suggested to get familiar with the single AD9361 based platforms
(:dokuwiki:`AD-FMCOMMS2-EBZ </resources/eval/user-guides/ad-fmcomms2-ebz>`
or :ref:`AD-FMCOMMS3-EBZ <ad-fmcomms3-ebz>`) first.

Note that the AD-FMCOMMS5-EBZ uses a dual FMC connector. This means the base
board requires two adjacent FMC connectors. Suitable base boards for example are
ZC702, ZC706, and ZCU102.

.. image:: images/fmcomms5_board.jpg
   :align: center
   :width: 500

User Guide
----------

.. toctree::
   :titlesonly:

   user-guide
   prerequisites
   quickstart/index

Table of Contents
-----------------

#. :dokuwiki:`Introduction </resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`
#. Hardware

   #. :dokuwiki:`Functional Overview & Specifications </resources/eval/user-guides/ad-fmcomms2-ebz/hardware/functional_overview>`
   #. :dokuwiki:`Characteristics & Performance </resources/eval/user-guides/ad-fmcomms2-ebz/hardware/card_specification>`
   #. :dokuwiki:`Production Testing Process </resources/eval/user-guides/ad-fmcomms2-ebz/testing>`

#. Use the AD-FMCOMMS5-EBZ Board to better understand the AD9361

   #. Linux Applications

      #. :ref:`IIO Scope <iio-oscilloscope>`
      #. :doc:`FMCOMMS5 Control IIO Scope Plugin <fmcomms5_plugin>`
      #. :dokuwiki:`FMCOMMS2/3/4/5 Advanced Control IIO Scope Plugin </resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      #. :dokuwiki:`Command Line/Shell scripts </resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   #. Push custom data into/out of the AD-FMCOMMS5-EBZ

      #. :doc:`Basic Data files and formats </solutions/reference-designs/fmcomms2/common/basic_iq_datafiles>`
      #. :dokuwiki:`Create and analyze data files in MATLAB </resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`
      #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      #. :dokuwiki:`AD9361 libiio streaming example </resources/tools-software/linux-software/libiio>`

#. Design with the AD9361

   #. :dokuwiki:`Understanding the AD9361 </resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`

      #. :adi:`AD9361 Product page <AD9361>`
      #. :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      #. :dokuwiki:`MATLAB Filter Design Wizard for AD9361 </resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`

   #. Simulation

      #. :dokuwiki:`MathWorks SimRF Models of the AD9361 </resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. MATLAB/Simulink Examples

         #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         #. :dokuwiki:`Beacon Frame Receiver Example </resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`
         #. :doc:`QPSK Transmit and Receive Example </solutions/reference-designs/fmcomms2/software/qpsk_example>`
         #. :doc:`LTE Transmit and Receive Example </solutions/reference-designs/fmcomms2/software/lte_example>`

      #. :ref:`GNU Radio <software gnuradio>`
      #. :dokuwiki:`FM Radio/Tuner </resources/tools-software/fm-radio>` (listen to FM signals on the HDMI monitor)
      #. :dokuwiki:`C example </resources/tools-software/linux-software/libiio>`

   #. Design a custom AD9361 based platform

      #. :dokuwiki:`Linux software </resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`

         #. :dokuwiki:`Linux Device Driver </resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         #. :dokuwiki:`Build the demo on ZC702, ZC706, or ZED from source </resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`
         #. :dokuwiki:`Build the demo on KC705 or VC707 for Microblaze from source </resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`
         #. :dokuwiki:`Build the 2014_R2 Release Linux kernel from source </resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2014r2>`
         #. :doc:`Customizing the devicetree on the target </linux/kernel/zynq_tips_tricks>`

      #. :dokuwiki:`No-OS Driver </resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`
      #. :dokuwiki:`HDL Reference Design </resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>` which you must use in your FPGA.

         #. :dokuwiki:`Digital Interface Timing Validation </resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`

#. Additional Documentation about SDR Signal Chains

   #. :doc:`The math behind the RF </solutions/reference-designs/fmcomms2/common/math>`
   #. :dokuwiki:`IQ rotation, and phase sync </resources/eval/user-guides/ad-fmcomms2-ebz/iq_rotation>`

#. :dokuwiki:`Help and Support </resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`

Presentations
-------------

- :adi:`Developing Multiple-Input Multiple-Output (MIMO) Systems with the AD9361 <en/education/education-library/webcasts/developing-multiple-input-multiple-output.html>`
  As Software Defined Radio (SDR) and Multiple-Input Multiple-Output (MIMO)
  become more prevalent there is a need for more channel diversity. This
  webcast will detail how to use multiple AD9361 devices to create an NxN
  MIMO system, as well as explore the available tradeoffs in the design. The
  AD9361 is a fully integrated 2x2 MIMO transceiver. Its programmability and
  wideband capability make it ideal for a broad range of transceiver
  applications.

Warning
~~~~~~~

.. esd-warning::
