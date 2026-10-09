.. _ad_fmcadc7_ebz user-guide:

User guide
===============================================================================

.. warning::

   The :adi:`AD-FMCADC7-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

.. _ad_fmcadc7_ebz hardware-guide:

Hardware guide
-------------------------------------------------------------------------------

Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-FMCADC7-EBZ board's primary purpose is to quickly and easily connect
to an FMC carrier platform and start collecting data using the :adi:`AD9625`
ADC. The board is designed to self power and self clock when connected to the
FMC carrier. The analog signals (AIN+ and AIN-) are connected to J202 and
J201. This rapid prototyping board is default set up to utilize input J202 for
a single-ended connection from a signal generator.

Clocking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-FMCADC7-EBZ includes various clocking options:

- 2.5 GHz Crystek on-board oscillator (Y401) connected via a differential
  balun directly to the converter's clock input pins.
- An external reference supplied at J301 for use with the :adi:`ADF4355-2`.
- 122.88 MHz Crystek on-board oscillator reference to the :adi:`ADF4355-2`.

Analog Front End
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-FMCADC7-EBZ uses an active front end designed for very wide bandwidth.
A single-ended input needs to be provided to the analog inputs at -15 dBm.
The broadband :adi:`ADL5567` amplifier gains and converts the analog input
signal differentially to the converter's inputs and has a 1.8 GHz bandwidth
at -3 dB. The amplifier's gain can be adjusted independently with simple
resistor modifications.

The revision B board is default set for the amplifier to be at maximum gain
with DC coupling. Hardware changes are required to change either the gain or
to switch from DC coupling to AC coupling.

.. _ad_fmcadc7_ebz software-guide:

Software guide
-------------------------------------------------------------------------------

Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+linux:ref:`AD9625 AXI Linux driver <axi-adc-hdl>`
- :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
- :external+linux:ref:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux
  driver <axi_adxcvr>`
- :external+kuiper:doc:`Kuiper Linux <index>`

Help & Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   - :external+hdl:ref:`build_hdl` contains all the documentation, build
     instructions and register map tables.
   - Browse the HDL GitHub repository:
     :git-hdl:`library components <library>`
     and :git-hdl:`projects <projects>`.
   - Questions? Ask on :ez:`FPGA questions <community/fpga>`,
     :ez:`Linux driver questions <linux-software-drivers/>`,
     or :ez:`No-OS Drivers questions <microcontroller-no-os-drivers/>`.
