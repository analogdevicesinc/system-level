.. _eval-ad9783 quickstart:

Quick start
===============================================================================

The quick start guide provides step-by-step instructions on how to do
an initial system setup for the :adi:`EVAL-AD9783` evaluation board on the 
supported FPGA carrier or controller boards. This guide covers how to
prepare the SD card, program the bitstream, and boot Kuiper Linux.

.. toctree::

   On ZCU102 (ZynqMP) <zcu102>
   On SDP-H1 <sdp-h1-ace>

.. _eval-ad9783 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9783` connect to the FPGA carrier via SPI and GPIO signals,
routed through an :adi:`AD-DAC-FMC` adapter board.

.. list-table::
   :header-rows: 1

   * - FPGA board
     - :adi:`EVAL-AD9783`
   * - ZCU102 (ZynqMP)
     - SPI

Supported controller boards
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9783` connect to the high speed controller borards via SPI and 
GPIO signals, routed through an :adi:`AD-DAC-FMC` adapter board.


Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - ZCU102 (ZynqMP)
     - Yes
     - Yes
     - ---
   * - :adi:`SDP-H1`
     - FMC LPC
     - FMC LPC
     - FMC LPC