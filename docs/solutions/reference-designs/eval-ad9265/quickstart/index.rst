.. _eval_ad9265 quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD9265` board.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these guides when evaluating with an FPGA carrier board. They cover
bitstream programming, no-OS programs and Linux boot.

.. toctree::

   On ZC706 <zc706>
   On ZedBoard <zed>
   On SDP-H1 <sdp-h1-evaluation>

.. _eval_ad9265 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9265` is, by definition, a "FPGA mezzanine card" (FMC);
that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD9265
   - - :xilinx:`ZC706`
     - FMC LPC
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Eval Board
     - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - EVAL-AD9265
     - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   - - EVAL-AD9265
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

On all carriers, the :adi:`EVAL-AD9265` board connects to the FMC LPC
connector. The carrier setup requires power, UART (115200), Ethernet (Linux),
and/or JTAG (no-OS) connections. A few typical setups are shown below.

ZC706 + EVAL-AD9265
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad9265_setup_zc706.jpg
   :width: 800

ZedBoard + EVAL-AD9265
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad9265_zed_setup.jpg
   :width: 800
