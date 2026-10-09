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

   #. :dokuwiki:`Detailed Specifications <university/tools/m2k/devs/specs>`
   #. :dokuwiki:`Schematics <university/tools/m2k/hacking/hardware>`
   #. :dokuwiki:`Detailed Performance <university/tools/m2k/devs/performance>`
   #. :dokuwiki:`Accessing FPGA JTAG <university/tools/m2k/devs/fpga>` with the
      :dokuwiki:`ADALM-JTAGUART </university/tools/uartjtag>` adapter

#. C Applications or Shell scripts on the Pluto

   #. :dokuwiki:`Running Scripts from USB drive <university/tools/m2k/devs/usb_otg>`
   #. :dokuwiki:`Creating compiled apps to run on-device <university/tools/m2k/devs/embedded_code>`

#. :external+hdl:ref:`user_guide`

   #. :dokuwiki:`AD9361 HDL reference design </resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`
   #. :external+hdl:ref:`axi_ad9361`
   #. :external+hdl:ref:`axi_dmac`


   #. `AD9361 high performance, highly integrated RF Agile Transceiver™ Linux
      device driver </resources/tools-software/linux-drivers/iio-transceiver/ad9361>`__
   #. :external+linux:ref:`axi-adc-hdl`
   #. :external+linux:ref:`axi-dac-dds-hdl`
   #. :external+linux:ref:`axi-dmac`
   #. :adi:`ADM1177` Digital Power Monitor Linux Driver
   #. etc.

#. Building the Firmware image from source


#. :dokuwiki:`./devs/Controlling GPIOs <university/tools/m2k/devs/Controlling GPIOs>`
#. Accessing the AD9363 inside Pluto from userspace

   #. :git-libiio:`libiio local mode example <examples/ad9361-iiostream.c>`
   #. :external+linux:ref:`ad9361`

#. :dokuwiki:`Connecting the Pluto to the Internet <university/tools/m2k/devs/port_forwarding>`
#. :dokuwiki:`Using U-Boot's DFU modes </university/tools/pluto/users/firmware#dfu_update>`
#. :dokuwiki:`Boot magic explained <university/tools/m2k/devs/booting>`
#. :dokuwiki:`Reboot Modes <university/tools/m2k/devs/reboot>`

.. toctree::
   :hidden:
   :glob:

   *
