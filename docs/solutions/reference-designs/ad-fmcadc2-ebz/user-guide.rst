.. _ad_fmcadc2_ebz user-guide:

User guide
===============================================================================

.. warning::

   The :adi:`AD-FMCADC2-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

.. _ad_fmcadc2_ebz hardware-guide:

Hardware guide
-------------------------------------------------------------------------------

.. _ad_fmcadc2_ebz specifications:

Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD-FMCADC2-EBZ` board's primary purpose is to quickly and easily
connect to an FMC carrier platform and start collecting data using the
:adi:`AD9625`. The board is designed to be easy to use. Out of the box the
board will self power and self clock when connected to an FMC carrier. The
only other required equipment is a signal source to provide an input signal
to "Ain".

This rapid prototyping board also has 4 vertically mounted SMA connectors
labeled SYSREF IN and SYSREF OUT. These enable synchronization of multiple
AD-FMCADC2-EBZ boards using the characteristics of the JESD204B high speed
serial interface between the AD9625 and the FPGA.

.. note::

   If you have a revision C board, as indicated by the etch next to the white
   scratch pad area of the PCB, it is recommended to write to the Serial Output
   Adjust Register. If you are using the reference design this is done
   automatically. Otherwise, when configuring the AD9625, increase the serial
   output emphasis by writing to register 0x015 bits 5:4 with either 10 or 11.

The AD-FMCADC2-EBZ provides multiple options for clocking the AD9625. The
default configuration clocks the ADC using an on-board 2.5 GHz, low noise,
crystal oscillator. This oscillator is routed through a wide band transformer
producing the differential clock for the ADC.

Alternatively, the oscillator can be disconnected and an external clock source
connected by changing two components on the board. A single-ended clock
connected to the CLK+ input is then routed through the transformer in the
same way.

A differential clock can also be connected to the board using both the CLK+
and CLK- inputs. Referencing the schematic, make the component changes to
directly route the differential input bypassing the transformer.

The AD-FMCADC2-EBZ uses a passive front end designed for very wide bandwidth.
A single-ended input must be provided to "Ain". A 500 kHz to 6 GHz broadband
balun converts the input signal to differential.

.. _ad_fmcadc2_ebz software-guide:

Software guide
-------------------------------------------------------------------------------

FPGA Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-FMCADC2-EBZ HDL reference design is available at
:git-hdl:`projects/fmcadc2 <hdl_2021_r2:projects/fmcadc2>`.

Eye Scan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eye scan information for this board can be found at
:git-jesd-eye-scan-gtk:`JESD Eye Scan GTK <>`.

No-OS Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-FMCADC2-EBZ No-OS software source can be found at
:git-no-OS:`fmcadc2 project <2018_R1:fmcadc2>`.

Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+linux:ref:`AD9625 AXI Linux driver <axi-adc-hdl>`
- :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
- :external+linux:ref:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux driver <axi_adxcvr>`
- :external+kuiper:doc:`Kuiper Linux <index>`
- :ref:`Linux on the VC707 <ad_fmcadc2_ebz vc707_quickstart>`

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
