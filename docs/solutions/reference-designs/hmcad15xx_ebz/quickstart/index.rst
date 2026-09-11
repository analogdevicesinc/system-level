.. _hmcad15xx quickstart:

Quick start
===============================================================================

The Quick start guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`HMCAD1511-EBZ/HMCAD1520-EBZ <HMCAD1520-EBZ>`
boards on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZedBoard <zed>

.. _hmcad15xx carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`HMCAD1511-EBZ/HMCAD1520-EBZ <HMCAD1520-EBZ>`, is, by definition a
"FPGA mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HMCAD1520-EBZ
     - HMCAD1511-EBZ
   - - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
     - FMC 
     - FMC 

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
     - Yes
     - Yes
     - ---

Hardware Setup
-------------------------------------------------------------------------------

On `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_ 
the board connects to the FMC connector. The carrier setup requires power,
UART(115200), Ethernet (Linux), HDMI (optional). The typical setup is shown
below.

ZedBoard + HMCAD1511-EBZ/HMCAD1520-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/hmcad1520_zed_setup.jpg
   :width: 600


