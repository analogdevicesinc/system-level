.. _pluto devs:

For Developers
==============

The people who typical read these pages are those who write custom software or
HDL (for the FPGA) that run directly on the Pluto device. This may put the Pluto
in different modes, and support different external USB devices (including
USB/LAB, or USB/WiFi), extending the capabilities of the device, or completely
changing the data that is transferred to the host. Since the goal of the project
is to keep things as open as possible, the details on how to compile kernels,
create bit files, assemble FIT files and load them into the device, should be
found here.

While we do have a few examples, and show how to re-create the default software
loads, since this the hardware can be nearly a blank slate for your project, you
can do anything you want.

Content
-------

..
   Please make sure that all these are in ./devs

#. Hardware

   #. :ref:`Detailed Specifications <pluto devs specs>`
   #. :ref:`Schematics <pluto hacking hardware>`
   #. :ref:`Performance Metrics <pluto devs performance>`
   #. :ref:`Accessing FPGA JTAG <pluto devs fpga>` with the
      :ref:`ADALM-JTAGUART <uartjtag>` adapter

#. C Applications or Shell scripts on the Pluto

   #. :ref:`Running Scripts from USB drive <pluto devs usb_otg>`
   #. :ref:`Creating compiled apps to run on-device <pluto devs embedded_code>`

#. :external+hdl:doc:`ADI Reference Designs HDL User Guide <index>`

   #. AD9361 HDL reference design
   #. :external+hdl:ref:`axi_ad9361`
   #. :external+hdl:ref:`axi_dmac`


   #. :external+linux:ref:`ad9361`
   #. :external+linux:ref:`axi-adc-hdl`
   #. :external+linux:ref:`axi-dac-dds-hdl`
   #. :external+linux:ref:`axi-dmac`
   #. :adi:`ADM1177` Digital Power Monitor Linux Driver
   #. etc.

#. Building the Firmware image from source


#. :ref:`Controlling GPIOs <pluto devs controlling_gpios>`
#. Accessing the AD9363 inside Pluto from userspace

   #. :git-libiio:`libiio local mode example <examples/ad9361-iiostream.c>`
   #. :external+linux:ref:`ad9361`

#. :ref:`Connecting the Pluto to the Internet <pluto devs port_forwarding>`
#. :ref:`Using U-Boot's DFU modes <pluto-m2k firmware dfu_update>`
#. :ref:`Boot magic explained <pluto devs booting>`
#. :ref:`Reboot Modes <pluto-m2k reboot>`

.. toctree::
   :hidden:
   :glob:

   *
