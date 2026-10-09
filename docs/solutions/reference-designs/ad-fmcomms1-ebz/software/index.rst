.. _ad_fmcomms1_ebz software:
.. _ad_fmcomms1_ebz software linux:

Software
===============================================================================

Software for the AD-FMCOMMS1-EBZ.

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

.. image:: ../images/tux.png
   :align: right

Analog Devices provides full Linux support for the AD-FMCOMMS1-EBZ. Depending on
which FPGA platform you are using the steps to perform to setup the system
slightly differ:

- :doc:`ML605 (Microblaze) </solutions/reference-designs/ad-fmcomms1-ebz/quickstart/microblaze_ml605>`
- :doc:`KC705 (Microblaze) </solutions/reference-designs/ad-fmcomms1-ebz/quickstart/microblaze_kc705>`
- :ref:`ZC702, ZC706, ZED (Zynq) <linux-kernel zynq-hdmi>`

Descriptions of the individual Linux device drivers for the different parts on
the AD-FMCOMMS1-EBZ can be found at:

- :external+linux:doc:`AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29 LVCMOS Outputs <drivers/iio-pll/ad9523>`
- :external+linux:doc:`ADF4351: Wideband Synthesizer with Integrated VCO <drivers/iio-pll/adf4350>`
- :external+linux:doc:`AD8366: DC to 600 MHz, Dual-Digital Variable Gain Amplifiers <drivers/iio-amplifiers/ad8366>`
- :external+linux:doc:`AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual Analog-to-Digital Converter (ADC) <drivers/iio-adc/axi-adc-hdl>`
- :external+linux:doc:`AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter <drivers/iio-dds/axi-dac-dds-hdl>`

.. image:: ../images/fmcomms1_linux_dd.png
   :align: center

- :dokuwiki:`No-OS drivers <resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/reference_design_no_os>`
- :ref:`I2C-to-SPI-bridge <ad_fmcomms1_ebz software i2c_to_spi_bridge>`
- :ref:`FMCOMMS1 plugin <fmcomms1-plugin>`

.. toctree::
   :hidden:

   applications/index
   fmcomms1_plugin
   i2c_to_spi_bridge
