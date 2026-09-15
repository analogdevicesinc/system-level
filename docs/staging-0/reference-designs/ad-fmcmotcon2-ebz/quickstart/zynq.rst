.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon2-ebz/quickstart/zynq

.. _ad-fmcmotcon2-ebz quickstart zynq:

AD-FMCMOTCON2-EBZ Linux on Zynq Quick Start Guide
=================================================

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the AD-FMCMOTCON2-EBZ on either:

- `ZED Board <http://zedboard.org/product/zedboard>`__, Rev C or later

Requirements
------------

- You need a Host PC (Windows or Linux).
- You need a SD card writer connected to above PC (Supported USB SD
  readers/writers are OK).
- USB keyboard/mouse for the Zynq Device
- HDMI Display (monitor or TV)

Creating the SD Card
--------------------

:dokuwiki:`Create SD Image for Zynq Boards <resources/tools-software/linux-software/zynq_images>`

Connecting the hardware together
--------------------------------

Instruction regarding the hardware connection can be found at:
:dokuwiki:`Hardware connection user guide ZED board </resources/eval/user-guides/ad-fmcmotcon2-ebz/quickstart/lv_setup_guide>`

Booting the SD Card
-------------------

#. ignore your PC, and now interact on the USB mouse/keyboard on the Zynq device
#. You should see one screen:

   .. figure:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/iio_scope.png

      IIO Scope tool

   Learn more about the :ref:`iio-oscilloscope`

#. You are now done with booting from the SD card. You can interact with the GUI
   either over the network, or with the HDMI monitor/USB keyboard mouse.

Using IIO SCOPE for AD-FMCMOTCON2-EBZ
-------------------------------------

:dokuwiki:`Software user guide </resources/eval/user-guides/ad-fmcmotcon2-ebz/software/iio_scope>`

.. important::

   Even thought this is Linux, this is a persistent file system. Care should be
   taken not to corrupt the file system – please shut down things, don"t just
   turn off the power switch. Depending on your monitor, the standard power off
   could be hiding. You can do this from the terminal as well with: ""sudo
   shutdown -h now""

   .. figure:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
      :width: 300px
