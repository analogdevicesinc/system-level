.. _ad_fmcadc3_ebz eval:

AD-FMCADC3-EBZ (Obsolete)
===============================================================================

12-Bit, 2500 MSPS, JESD204B, RF Data Acquisition FMC Board.

.. warning::

   The :adi:`AD-FMCADC3-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCADC3-EBZ` is a high speed data
acquisition board featuring the :adi:`AD9625` single channel ADC at
2500 MSPS and the :adi:`ADA4961` Low Distortion, 3.2 GHz, RF Digital Gain
Amplifier (DGA) driving the converter. The FMC form factor supports the
JESD204B high speed serial interface. This board meets most of the FMC
specifications in terms of mechanical size, mounting hole locations, and more.

Although this board does meet most of the FMC specifications, it is not meant
as a commercial off the shelf (COTS) board. If you want a commercial, ready to
integrate product, please refer to one of the many FMC manufacturers and the
FMC specification (ANSI/VITA 57.1). This board is targeted to use the ADI
reference designs that work with Xilinx development systems. ADI provides
complete source (HDL and software) to re-create those projects (minus the IP
provided by the FPGA vendors, which we use), but may not provide enough info to
port this to your custom platform.

The design of the board is specifically tailored to synchronizing multiple
AD-FMCADC3-EBZ boards together. For more information on synchronization,
please refer to :adi:`A Test Method for Synchronizing Multiple GSPS Converters <en/resources/technical-articles/a-test-method-for-synchronizing-multiple-gsps-converters.html>`.

The card contains:

- :adi:`AD9625` 12-bit ADC with sampling speeds of up to 2500 MSPS, with a
  :adi:`JESD204B <JESD204>` digital interface.
- :adi:`ADA4961` Low Distortion, 3.2 GHz, RF Digital Gain Amplifier.
- :adi:`ADP7104` 20 V, 500 mA, low noise, CMOS LDO
- :adi:`ADP1753` low dropout linear regulator (1.6 V to 3.6 V, up to 800 mA)
- :adi:`ADP2119` 2 A, 1.2 MHz, synchronous step-down DC-to-DC regulator
- :adi:`ADP1741` 2 A, low V\ :sub:`IN`\, low dropout, CMOS linear regulator
- :adi:`ADR280` ultralow power, high PSRR voltage reference

.. figure:: images/ad-fmcadc3-ebz_board.jpeg
   :alt: AD-FMCADC3-EBZ evaluation board
   :align: center
   :width: 600

   AD-FMCADC3-EBZ Evaluation Board

.. figure:: images/ad-fmcadc3-ebz_board_rev.jpeg
   :alt: AD-FMCADC3-EBZ evaluation board (newer revision)
   :align: center
   :width: 600

   AD-FMCADC3-EBZ Evaluation Board (newer revision)

Features:

- 2.5 GSPS utilizing JESD204B high speed serial interface
- Driver amplifier interface with 21 dB voltage gain adjustment
- Optional on-board or external clocking
- Specific design and I/O added for multi-board synchronization

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

   #. :ref:`Prerequisites <ad_fmcadc3_ebz prerequisites>`
   #. :ref:`Quick start guides <ad_fmcadc3_ebz quickstart>`

      #. :ref:`Supported carriers <ad_fmcadc3_ebz carriers>`
      #. :ref:`Hardware setup <ad_fmcadc3_ebz hardware-setup>`

   #. :ref:`User guide <ad_fmcadc3_ebz user-guide>`

      #. :ref:`Hardware guide <ad_fmcadc3_ebz hardware-guide>`
      #. :ref:`Software guide <ad_fmcadc3_ebz software-guide>`

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
