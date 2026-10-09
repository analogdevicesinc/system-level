.. _m2k devs:

For Developers
==============

.. image:: ../images/adalm2000.jpg
   :align: right
   :width: 400px

.. toctree::
   :maxdepth: 1
   :hidden:
   :glob:

   hardware

The people who typical read these pages are those who write custom software or
HDL (for the FPGA) that run directly on the M2K device. This may put the M2K in
different modes, and support different external USB devices (including USB/LAB,
or USB/WiFi), extending the capabilities of the device, or completely changing
the data that is transferred to the host. Since the goal of the project is to
keep things as open as possible, the details on how to compile kernels, create
bit files, assemble FIT files and load them into the device, should be found
here.

While we do have a few examples, and show how to re-create the default software
loads, since this the hardware can be nearly a blank slate for your project, you
can do anything you want.

Content
-------

..
   TODO Coming soon sections
   Make sure all things are in ./devs

#. :ref:`m2k intro`
#. Hardware

   #. Detailed Specifications
      #. :ref:`m2k hardware`
   #. Detailed Performance *(Coming soon)*
   #. Accessing the Console with the
      :dokuwiki:`ADALM-JTAGUART </university/tools/uartjtag>` adapter
   #. Accessing FPGA JTAG with the
      :dokuwiki:`ADALM-JTAGUART </university/tools/uartjtag>` adapter

#. :external+hdl:doc:`index`

   #. :external+hdl:ref:`m2k`
   #. :external+hdl:ref:`axi_ad9963`
   #. :external+hdl:ref:`axi_adc_decimate`
   #. :external+hdl:ref:`axi_dac_interpolate`
   #. :external+hdl:ref:`axi_logic_analyzer`
   #. :external+hdl:ref:`axi_adc_trigger`
   #. :external+hdl:ref:`util_var_fifo`
   #. :external+hdl:ref:`util_extract`

#. Device Drivers

   #. :external+linux:ref:`axi-adc-hdl`
   #. :external+linux:ref:`axi-dac-dds-hdl`
   #. :external+linux:ref:`axi-dmac`

#. Building the Firmware image from source

   #. :ref:`pluto-m2k obtaining_the_sources`
   #. :ref:`pluto-m2k building_the_image`

#. :ref:`pluto-m2k usb_otg_host`
#. :ref:`pluto-m2k firmware dfu_update`
#. :ref:`pluto-m2k reboot`
