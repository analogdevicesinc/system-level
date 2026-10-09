.. _ad_fmcadc4_ebz user-guide:

User guide
===============================================================================

.. warning::

   The :adi:`AD-FMCADC4-EBZ` is a **legacy product** that has been retired
   and is no longer available for sale. It has been removed from the HDL and
   software repositories, but is still available in the git history. This
   documentation is provided for reference only.

.. _ad_fmcadc4_ebz hardware-guide:

Hardware guide
-------------------------------------------------------------------------------

The :adi:`AD-FMCADC4-EBZ` board's primary purpose is to demonstrate the
capabilities of the devices on board quickly and easily by providing a seamless
interface to an FMC carrier platform and running the reference design on the
carrier FPGA. The board is designed to self power and self clock when connected
to the FMC carrier. The analog signals (up to four) are connected to J301A,
J301B, J301C and J301D. This rapid prototyping board can also be synchronized
across channels.

Clocking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD-FMCADC4-EBZ` includes an on-board 80 MHz reference oscillator
from Crystek. This feature can be disconnected and an external reference can
be applied through J901. When referencing the schematic make sure the proper
component changes are made in order to directly route the input into the
:adi:`AD9528`.

Analog Front End
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD-FMCADC4-EBZ` uses a passive front end designed for very wide
bandwidth. A single ended input needs to be provided to the analog inputs
mentioned earlier. A 1:2 impedance ratio broadband balun then converts the
input signal differentially to the :adi:`ADA4961` inputs and has a 1.6 GHz
bandwidth at -3 dB. Each channel amplifier can be adjusted independently in
terms of gain.

Revision A
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The revision A board supports amplifier gain control via SPI. After power-up,
the gain of the amplifier defaults to an attenuated state. Use a low jitter,
low noise signal source with a level at -20 dBm to the analog inputs
(J301-A/B/C/D). Apply a signal source no greater than -10 dBm to achieve
full-scale of the converter when maximum gain of the amplifier is applied.


.. _ad_fmcadc4_ebz software-guide:

Software guide
-------------------------------------------------------------------------------

FPGA Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD-FMCADC4-EBZ` HDL project has been removed from the repository
but is still available in the git history. Library cores previously used:

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

.. note::

   ILA was supported in reference designs prior to the ``hdl_2016_r1`` release.

.. figure:: images/fmcadc4_ila.png
   :alt: FMCADC4 ILA plot
   :align: center
   :width: 600

   FMCADC4 ILA plot screen capture

Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+linux:ref:`AD9680 AXI Linux driver <axi-adc-hdl>`
- :dokuwiki:`ADA4961 Low Distortion, 3.2 GHz, RF DGA Linux driver <resources/tools-software/linux-drivers/iio-amplifiers/ad8366>`
- :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
- :external+linux:ref:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux driver <axi_adxcvr>`
- :dokuwiki:`ZC706 Linux image <resources/tools-software/linux-software/kuiper-linux>`

Help & Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   - The :dokuwiki:`HDL user guide <resources/fpga/docs/hdl>`
     contains all the documentation, build instructions and register map
     tables.
   - The following quick links allow you to browse the GitHub repository:
     :git-hdl:`library components <library>`
     and :git-hdl:`projects <projects>`.
   - Questions? We can help with
     :ez:`FPGA questions <community/fpga>`,
     :ez:`Linux driver questions <linux-software-drivers/>`,
     :ez:`No-OS Drivers questions <microcontroller-no-os-drivers/>`.
