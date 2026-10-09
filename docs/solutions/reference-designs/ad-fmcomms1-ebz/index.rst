.. _ad_fmcomms1_ebz:

AD-FMCOMMS1-EBZ (Obsolete)
===============================================================================

.. warning::

   Analog Devices uses six designations to inform our customers where a
   semiconductor product is in its
   :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`.
   From emerging innovations to products which have been in production for
   twenty years, we understand that insight into life cycle status is important.
   Device life cycles are tracked on their individual product pages on
   `analog.com <https://www.analog.com/>`_, and should always be consulted
   before making any design decisions.

   This particular article/document/design has been retired or deprecated,
   which means it is no longer maintained or actively updated, even though the
   devices themselves may be Recommended for New Designs or in
   Production. This page is here for historical/reference purposes only.

.. warning::

   Last stable version for Vivado 2015.4:
   :git-hdl:`hdl_2016_r1 <hdl_2016_r1:projects/fmcomms1>`

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCOMMS1-EBZ <eval-fmcomms>` high-speed analog module is designed
to showcase the latest generation high-speed data converters. It provides the
analog front-end for a wide range of compute-intensive FPGA-based radio
applications.

The AD-FMCOMMS1-EBZ is an analog front end hardware platform that addresses a
broad range of research, academic, industrial and defense applications. It
enables RF applications from 400 MHz to 4 GHz. The module is customizable to a
wide range of frequencies by software without any hardware changes, providing
options for GPS or IEEE 1588 Synchronization, and MIMO configurations.

When combined with the Xilinx ZYNQ® Software-Defined Radio Kit,
:adi:`AD-FMCOMMS1-EBZ <eval-fmcomms>` enables a variety of wireless
communications functions at the physical layer, from baseband to RF. With up to
4 GB of flash storage space, 512 MB of RAM, Gigabit Ethernet interface
(depending on the base platform) and a Linux image built specifically for the
:adi:`AD-FMCOMMS1-EBZ <eval-fmcomms>`, you can get everything you need for a
easy out of the box experience. The platform offers enough flexibility for many
applications, and supports streaming data, and standard web interfaces to
analyze transmitted RF data.

.. image:: images/dscn1188.png
   :align: center
   :width: 500


.. warning::

   The AD-FMCOMMS1-EBZ FMC Card is not fully ANSI/VITA 57.1 compatible:

   - does not meet the mechanical form factor (too tall, too long),

   It was designed, and meets the needs of prototyping platforms, and will work
   with FPGA Development systems which include an FMC connector. It may not
   mechanically fit on other ANSI/VITA 57.1 carrier cards.

Features:

- General purpose design suitable for any application
- Software tunable across wide frequency range (400 MHz to 4 GHz) with 125 MHz
  channel bandwidth (250 MSPS ADC, 1 GSPS DAC)
- RF section bypass for baseband sampling
- Phase and frequency synchronization on both transmit and receive paths
- Allows high channel density
- LPC FMC compatible, meets VITA specifications except card length
- Powered from single FMC connector
- Supports MIMO radio, with less than 1 sample sync on both ADC and DAC
- Includes schematics, layout, BOM, HDL, Linux drivers and application software
- Common I\ :sup:`2`\ C access for all device registers

Applications:

- Wireless communications demonstration and learning tool
- Remote radio head
- Software-defined radio
- Satellite modems
- Test and measurement equipment
- Radar and advanced imaging
- General purpose data acquisition

.. image:: images/fmcomms1_top_v.jpg
   :align: left
   :width: 150

.. toctree::
   :hidden:

   quickstart/index
   hardware/index
   interface_timing_validation
   software/index
   testing
   help_and_support

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the
:ref:`Help and Support <ad_fmcomms1_ebz help-and-support>` page.

To better understand the AD-FMCOMMS1-EBZ, we recommend reading the
:ref:`Functional Overview <ad_fmcomms1_ebz hardware functional_overview>`.

Table of contents
-------------------------------------------------------------------------------

#. Introduction

   - :ref:`The math behind the RF <fmcomms2 common fmcomms-math>`
   - :ref:`I/Q Correction <fmcomms2 common iq-correction>`

#. :ref:`Quick Start Guides <ad_fmcomms1_ebz quickstart>`:

   - :ref:`Linux on ZC702, ZC706, ZED <ad_fmcomms1_ebz quickstart zynq>`
   - :ref:`Linux on KC705, VC707 <ad_fmcomms1_ebz quickstart microblaze-kc705>`
   - :ref:`no-OS Drivers <ad_fmcomms1_ebz quickstart no-os-microblaze>`

#. :ref:`Hardware <ad_fmcomms1_ebz hardware>` (including schematics)

   - :ref:`Functional Overview <ad_fmcomms1_ebz hardware functional_overview>`
   - :ref:`Card specifications <ad_fmcomms1_ebz hardware card-specification>`
   - :ref:`Configuration options <ad_fmcomms1_ebz hardware configuration_options>`
   - :ref:`BOM Improvements <ad_fmcomms1_ebz hardware bom_improvements>`

#. :external+hdl:ref:`Reference HDL Design <fmcomms1>`

   - :ref:`Digital Interface Timing Validation <ad_fmcomms1_ebz interface-timing-validation>`

#. :ref:`Software <ad_fmcomms1_ebz software>`

   - :ref:`Linux <ad_fmcomms1_ebz software linux>`

     - :ref:`ZC702, ZC706, ZED <linux-kernel zynq-hdmi>`
     - :doc:`ML605 (Microblaze) </solutions/reference-designs/ad-fmcomms1-ebz/quickstart/microblaze_ml605>`
     - :doc:`KC705 (Microblaze) </solutions/reference-designs/ad-fmcomms1-ebz/quickstart/microblaze_kc705>`

   - :dokuwiki:`No-OS drivers <resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/reference_design_no_os>`
   - :ref:`FMCOMMS1 IIO Oscilloscope Plugin <fmcomms1-plugin>`
   - :ref:`I2C-to-SPI-bridge <ad_fmcomms1_ebz software i2c_to_spi_bridge>`

#. :ref:`Production Testing Process <ad_fmcomms1_ebz testing>`
#. :ref:`Help and Support <ad_fmcomms1_ebz help-and-support>`

.. _ad_fmcomms1_ebz block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/cf_xcomm_kc705_bd.jpg
   :align: center
   :width: 800

ADI Documentation on SDR Signal Chains
-------------------------------------------------------------------------------

- :adi:`Interfacing the ADL5375 I/Q Modulator to the AD9122 Dual Channel, 1.2 GSPS High Speed DAC (CN0205) <cn0205>`
- :adi:`Software calibrated, 1 MHZ to 8 GHZ, 60 DB RF Power Measurement System using the AD8318 Logarithmic Detector (CN0150) <cn0150>`
- :adi:`Software calibrated, 50 MHZ TO 9 GHZ, RF Power Measurement System (CN0178) <cn0178>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <ad_fmcomms1_ebz help-and-support>` page.
