.. _ad_fmcadc3_ebz user-guide:

User guide
===============================================================================

.. warning::

   The :adi:`AD-FMCADC3-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

.. _ad_fmcadc3_ebz hardware-guide:

Hardware guide
-------------------------------------------------------------------------------

Revision A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The revision A board has the amplifier gain control via SPI. When powering up
the FMCADC3 board, the gain of the amplifier will default to an attenuated
state. When applying a signal source to the FMCADC3 at the analog input
connector J201, use a low jitter, low noise signal source with a level at
-20 dBm. Apply a signal source no greater than -8 dBm when achieving
full-scale of the converter and maximum gain of the amplifier is applied.

Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-FMCADC3-EBZ board's primary purpose is to quickly and easily connect
to an FMC carrier platform and start collecting data using the AD9625. The
board is designed to be easy to use. Out of the box the board will self power
and self clock when connected to an FMC carrier. The only other required
equipment is your chosen signal source to provide an input signal to "Ain".

This rapid prototyping board also has 4 vertically mounted SMA connectors.
These are labeled SYSREF IN and SYSREF OUT. These are to enable
synchronization of multiple AD-FMCADC3-EBZ boards together using
characteristics of the JESD204B high speed serial interface between the AD9625
and FPGA.

Clocking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AD-FMCADC3-EBZ provides multiple options for clocking the AD9625. The
default configuration of the board clocks the ADC using an on-board 2.5 GHz,
low noise, crystal oscillator from Crystek. This oscillator is then routed
through a wide band transformer producing the differential clock for the ADC.
Alternatively, the oscillator can be disconnected and an external clock source
connected by only changing two components on the board. A single ended clock
connected to the CLK+ input would then be routed through the transformer in
the same way.

Finally, the option exists to connect a differential clock to the board using
both the CLK+ and CLK- inputs. Then referencing the schematic make the
component changes to directly route the differential input bypassing the
transformer.

Front End
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AD-FMCADC3-EBZ uses a passive front end designed for very wide bandwidth.
A single ended input needs to be provided to "Ain". A 1:2 impedance ratio
broadband balun then converts the input signal differentially to the ADA4961
inputs and has a 1.6 GHz bandwidth at -3 dB.


.. _ad_fmcadc3_ebz software-guide:

Software guide
-------------------------------------------------------------------------------

FPGA Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD-FMCADC2-EBZ` and the :adi:`AD-FMCADC3-EBZ` use common HDL.
Library cores used:

- :git-hdl:`axi_adcfifo <library/xilinx/axi_adcfifo>`
- :git-hdl:`axi_adxcvr <library/xilinx/axi_adxcvr>`
- :git-hdl:`axi_clkgen <library/axi_clkgen>`
- :git-hdl:`axi_dmac <library/axi_dmac>`
- :git-hdl:`axi_hdmi_tx <library/axi_hdmi_tx>`
- :git-hdl:`axi_jesd204_rx <library/jesd204/axi_jesd204_rx>`
- :git-hdl:`axi_spdif_tx <library/axi_spdif_tx>`
- :git-hdl:`axi_sysid <library/axi_sysid>`
- :git-hdl:`jesd204_rx <library/jesd204/jesd204_rx>`
- :git-hdl:`sysid_rom <library/sysid_rom>`
- :git-hdl:`util_adcfifo <library/util_adcfifo>`


Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+linux:ref:`AD9625 AXI Linux driver <axi-adc-hdl>`
- :dokuwiki:`ADA4961 Low Distortion, 3.2 GHz, RF DGA Linux driver <resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
- :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
- :external+linux:ref:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux driver <axi_adxcvr>`
- :dokuwiki:`ZC706 Linux image <resources/tools-software/linux-software/kuiper-linux>`
- :dokuwiki:`Linux on the VC707 <resources/eval/user-guides/ad-fmcadc2-ebz/quickstart/microblaze>`

Help & Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   - The :dokuwiki:`HDL user guide <resources/fpga/docs/hdl>`
     contains all the documentation, build instructions and register map
     tables.
   - The following quick links allow you to browse the GitHub repository for
     a list of current
     `branches <http://github.com/analogdevicesinc/hdl/branches/active>`_,
     :git-hdl:`library components <library>`,
     and :git-hdl:`projects <projects>`.
   - Questions? We can help with
     :ez:`FPGA questions <community/fpga>`,
     :ez:`Linux driver questions <linux-software-drivers/>`,
     :ez:`No-OS Drivers questions <microcontroller-no-os-drivers/>`.
