.. _ad7606x quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide step-by-step instructions on how to do an
initial system setup for the :adi:`EVAL-AD7606B-FMCZ` /
:adi:`EVAL-AD7606C-18FMCZ <EVAL-AD7606C-18>` evaluation boards.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these guides when evaluating with an FPGA carrier board. They cover
bitstream programming, no-OS programs, and Linux boot.

.. toctree::

   On ZedBoard <zed>
   On CED1Z (Nios II) <ad7606_ced1z_fpga>

.. _ad7606x carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7606B-FMCZ` and :adi:`EVAL-AD7606C-18FMCZ <EVAL-AD7606C-18>` are FMC boards
that need a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD7606B-FMCZ
     - EVAL-AD7606C-18FMCZ
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC
     - FMC LPC

The :adi:`EVAL-AD7606EDZ` / :adi:`EVAL-AD7606-4EDZ` / :adi:`EVAL-AD7606-6EDZ`
boards are also supported via the :adi:`EVAL-CED Converter Evaluation and
Development (CED) Board` using an Altera Nios II processor. See
:ref:`ad7606_ced1z_fpga` for details.

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   - - Eval board
     - FPGA board
     - HDL
     - Linux
     - No-OS
   - - EVAL-AD7606B-FMCZ
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
   - - EVAL-AD7606C-18FMCZ
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
   - - EVAL-AD7606EDZ
     - CED1Z
     - Yes
     - No
     - Yes (Nios II)

Hardware setup
-------------------------------------------------------------------------------

On the ZedBoard, the evaluation board connects to the FMC LPC connector (J1).
The carrier setup requires power (12 V), UART (115200 baud), Ethernet (Linux
path), and JTAG (no-OS path) connections.

.. image:: ../images/zed_ad7606_setup.jpeg
   :width: 800
