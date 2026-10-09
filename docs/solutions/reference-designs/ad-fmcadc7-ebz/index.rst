.. _ad_fmcadc7_ebz eval:

AD-FMCADC7-EBZ (Obsolete)
===============================================================================

12-Bit, 2500 MSPS, JESD204B, RF Data Acquisition FMC Board.

.. warning::

   The :adi:`AD-FMCADC7-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

.. note::

   Support was discontinued starting with the **2022_R2** Kuiper Linux release.
   The last release with pre-built files is **2021_r2** - see all releases at
   :git-kuiper:`releases+`.
   HDL source code is available on the
   :git-hdl:`hdl_2021_r2 <hdl_2021_r2:projects/fmcadc7>` branch.

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCADC7-EBZ` is a high speed single channel data acquisition
board featuring the :adi:`AD9625` 12-bit single channel differential
Analog-to-Digital converter at 2.5 GHz and an :adi:`ADL5567` dual channel
differential 4.8 GHz amplifier. The board is FMC compatible. Clocking can be
done three different ways: on-board 2.5 GHz Crystek oscillator, on-board
122.88 MHz Crystek oscillator reference to the :adi:`ADF4355-2`, or an
external reference at J301.

Although this board does meet most of the FMC specifications, it is not meant
as a commercial off the shelf (COTS) board. If a commercial, ready to integrate
product is required, please refer to one of the many FMC manufacturers.

ADI also provides reference designs (HDL and software) for this board to work
with commonly available Altera and Xilinx development boards.

The card contains:

- :adi:`AD9625` 12-bit single channel ADC with sampling speeds of up to
  2500 MSPS, with a :adi:`JESD204B <JESD204>` digital interface.
- :adi:`ADL5567` 4.8 GHz Ultrahigh Dynamic Range, Dual Differential Amplifier
- :adi:`ADF4355-2` Microwave Wideband Synthesizer with Integrated VCO
- :adi:`ADR280` 1.2 V Ultralow Power, High PSRR Voltage Reference
- :adi:`AD7291` 8-Channel, I2C, 12-Bit SAR ADC with Temperature Sensor
- :adi:`ADP1753` 0.8 A, Low V\ :sub:`IN`\, Low Dropout Linear Regulator
- :adi:`ADP7104` 20 V, 500 mA, Low Noise, CMOS LDO
- :adi:`ADP1741` 2 A, Low V\ :sub:`IN`\, Low Dropout, CMOS Linear Regulator
- :adi:`ADP2119` 2 A/1.25 A, 1.2 MHz, Synchronous, Step-Down DC-to-DC
  Regulator
- :adi:`ADP2442` 36 V, 1 A, Synchronous, Step-Down, DC-to-DC Regulator with
  External Clock Synchronization

.. figure:: images/fmcadc7-top.jpg
   :alt: AD-FMCADC7-EBZ evaluation board (top view)
   :align: center
   :width: 600

   AD-FMCADC7-EBZ Evaluation Board (top view)

.. figure:: images/fmcadc7-bot.jpg
   :alt: AD-FMCADC7-EBZ evaluation board (bottom view)
   :align: center
   :width: 600

   AD-FMCADC7-EBZ Evaluation Board (bottom view)

Features:

- 2500 MSPS sampling rate using the AD9625 with JESD204B high speed serial
  interface
- Active wideband front end (1.8 GHz bandwidth at -3 dB) with adjustable gain
- Multiple clocking options: on-board 2.5 GHz oscillator, on-board 122.88 MHz
  reference to ADF4355-2, or external reference at J301
- Self-powered and self-clocked when connected to an FMC carrier

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

   #. :ref:`Prerequisites <ad_fmcadc7_ebz prerequisites>`
   #. :ref:`Quick start guides <ad_fmcadc7_ebz quickstart>`

      #. :ref:`Supported carriers <ad_fmcadc7_ebz carriers>`
      #. :ref:`Hardware setup <ad_fmcadc7_ebz hardware-setup>`
      #. :ref:`ZC706 quick start <ad_fmcadc7_ebz zc706_quickstart>`

   #. :ref:`User guide <ad_fmcadc7_ebz user-guide>`

      #. :ref:`Hardware guide <ad_fmcadc7_ebz hardware-guide>`
      #. :ref:`Software guide <ad_fmcadc7_ebz software-guide>`

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
