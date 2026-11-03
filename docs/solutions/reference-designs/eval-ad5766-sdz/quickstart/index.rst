.. _ad5766 quickstart:

Quickstart
===============================================================================

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD5766/67-SD2Z <EVAL-AD5766>`
boards on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On ZedBoard <zed>

.. _ad5766 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD5766/67-SD2Z <EVAL-AD5766>`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - :adi:`EVAL-AD5766/67-SD2Z <EVAL-AD5766>`
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC

Supported environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - no-OS software
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - No
     - Yes

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD5766/67-SD2Z <EVAL-AD5766>` boards
connects to the FMC connector (unless otherwise noted). The carrier setup
requires power, UART (115200), Ethernet (if Linux available), HDMI (if available)
and/or JTAG (if no-OS available) connections. A few typical setups are shown
below.

ZedBoard + EVAL-AD5766/67-SD2Z
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/eval_ad5766_zed_setup.jpg
   :width: 800

Go to :ref:`the setup guide <ad5766 zed>`.
