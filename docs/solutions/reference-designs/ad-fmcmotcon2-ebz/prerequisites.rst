.. _ad_fmcmotcon2_ebz prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The controller board: :adi:`AD-FMCMOTCON2-EBZ`
#. The low voltage drive board: :adi:`AD-DRVLV2-EBZ`
#. An FPGA carrier platform. Supported carriers can be found
   :ref:`here <ad_fmcmotcon2_ebz carriers>`.
#. A BLDC motor with Hall effect sensors or compatible encoder.
#. A 12 V-48 V capable DC lab power supply.
#. A UART/USB cable for serial console access (115200 baud, 8N1).
#. An Ethernet cable (required for Linux remote access).
#. :adi:`AD-DYNO2-EBZ` - Dynamometer drive system (optional).

Software prerequisites
-------------------------------------------------------------------------------

#. An SD card loaded with the ADI Kuiper Linux distribution.
   See :external+kuiper:doc:`Kuiper Linux <index>` for flashing instructions.
#. :ref:`iio-oscilloscope`, a graphical tool for monitoring and controlling
   IIO devices.

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
