.. _ad_fmcadc2_ebz eval:

AD-FMCADC2-EBZ (Obsolete)
===============================================================================

12-Bit, 2500 MSPS, JESD204B, RF Data Acquisition FMC Board.

.. warning::

   The :adi:`AD-FMCADC2-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

.. note::

   Support was discontinued starting with the **2022_R2** Kuiper Linux release.
   The last release with pre-built files is **2021_r2** - see all releases at
   :git-kuiper:`releases+`.
   HDL source code is available on the
   :git-hdl:`hdl_2021_r2 <hdl_2021_r2:projects/fmcadc2>` branch.

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCADC2-EBZ` is a high speed single channel data acquisition
board featuring the :adi:`AD9625` 12-bit ADC at 2500 MSPS, in an FMC form
factor which supports the JESD204B high speed serial interface.

Although this board does meet most of the FMC specifications, it is not meant
as a commercial off the shelf (COTS) board. If a commercial, ready-to-integrate
product is required, please refer to one of the many FMC manufacturers.

ADI provides reference designs (HDL and software) for this board to work with
commonly available Xilinx development boards.

The card contains:

-  :adi:`AD9625` 12-bit single channel ADC with sampling speeds of up to
   2500 MSPS, with a :adi:`JESD204B <JESD204>` digital interface.
-  :adi:`ADP7104` - 20V, 500mA, low noise, CMOS LDO
-  :adi:`ADP1753` - low dropout linear regulator, 1.6V to 3.6V, up to 800mA
-  :adi:`ADP2119` - 2A, 1.2MHz, synchronous step-down DC-to-DC regulator
-  :adi:`ADP1741` - 2A, low Vin, low dropout, CMOS linear regulator
-  :adi:`ADR280` - ultralow power, high PSRR voltage reference

.. figure:: images/ad-fmcadc2-ebz-photo.jpg
   :alt: AD-FMCADC2-EBZ evaluation board
   :align: center
   :width: 420

   AD-FMCADC2-EBZ Evaluation Board

Features:

- 2500 MSPS sampling rate using the AD9625 with JESD204B high speed serial
  interface
- Self-powered and self-clocked when connected to an FMC carrier
- Multiple clocking options: on-board 2.5 GHz oscillator, external
  single-ended, or external differential clock
- Passive wideband front end (500 kHz to 6 GHz balun)
- SYSREF IN/OUT connectors for multi-board synchronization

Applications:

- Instrumentation and measurement
- Radar
- Healthcare
- Energy
- Industrial automation

.. toctree::
   :hidden:

   prerequisites
   user-guide
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete as
it should be. If you have any questions, feel free to ask on our
:ez:`/`, but before that, please make sure you read our documentation
thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <ad_fmcadc2_ebz prerequisites>`
   #. :ref:`Quick start guides <ad_fmcadc2_ebz quickstart>`

      #. :ref:`Supported carriers <ad_fmcadc2_ebz carriers>`
      #. :ref:`Hardware setup <ad_fmcadc2_ebz hardware-setup>`
      #. :ref:`Linux quick start (ZC706 / VC707) <ad_fmcadc2_ebz vc707_quickstart>`
      #. :ref:`No-OS quick start (ZC706 / VC707) <ad_fmcadc2_ebz baremetal_quickstart>`

   #. :ref:`User guide <ad_fmcadc2_ebz user-guide>`

      #. :ref:`Hardware guide <ad_fmcadc2_ebz hardware-guide>`
      #. :ref:`Software guide <ad_fmcadc2_ebz software-guide>`

#. Design with the AD9625

   - :adi:`AD9625` product page

   - Resources for designing a custom AD9625-based platform:

     #. For Linux software:

        - :external+linux:ref:`AD9625 AXI Linux driver <axi-adc-hdl>`
        - :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
        - :external+linux:ref:`JESD204B/C AXI_ADXCVR Linux driver <axi_adxcvr>`

#. :ref:`Help and Support <help-and-support>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
