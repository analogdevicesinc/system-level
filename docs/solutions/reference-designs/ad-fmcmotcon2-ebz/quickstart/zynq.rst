.. _ad_fmcmotcon2_ebz zedboard_quickstart:

Linux on ZedBoard Quick Start Guide
===============================================================================

This guide provides instructions on how to set up the AD-FMCMOTCON2-EBZ on
the `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_
(Rev C or later).

Requirements
-------------------------------------------------------------------------------

- A host PC (Windows or Linux)
- An SD card writer connected to the host PC (USB SD readers/writers are OK)
- USB keyboard and mouse for the ZedBoard
- HDMI display (monitor or TV)

Creating the SD Card
-------------------------------------------------------------------------------

:external+kuiper:doc:`Create SD Image for Zynq Boards <index>`

Connecting the hardware
-------------------------------------------------------------------------------

Hardware connection instructions can be found in the
:ref:`Hardware Setup <ad_fmcmotcon2_ebz hardware-setup>` section.

Booting the SD Card
-------------------------------------------------------------------------------

- Interact with the ZedBoard using the USB mouse and keyboard
- You should see the IIO Scope tool on the display:

.. figure:: ../images/iio_scope.jpg
   :alt: IIO Oscilloscope on ZedBoard
   :align: center
   :width: 200

   IIO Oscilloscope on ZedBoard

- Learn more about :ref:`iio-oscilloscope`.
- You can interact with the GUI either over the network or with the HDMI
  monitor and USB keyboard/mouse.

Using IIO Oscilloscope
-------------------------------------------------------------------------------

See the :ref:`IIO Oscilloscope section <ad_fmcmotcon2_ebz iio-scope>` in
the user guide for details on monitoring and controlling the
AD-FMCMOTCON2-EBZ.

.. important::

   This Linux installation uses a persistent file system. Do not corrupt the
   file system by turning off power abruptly — always shut down properly.
   You can shut down from the terminal with: ``sudo shutdown -h now``

.. figure:: ../images/shutdown.jpg
   :alt: Shutdown dialog
   :align: center
   :width: 300

   Shutdown dialog
