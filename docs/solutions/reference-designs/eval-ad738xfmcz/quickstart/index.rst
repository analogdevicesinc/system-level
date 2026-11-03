.. _eval-ad738xfmcz quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide simple step by step instructions on
how to do an initial system setup for the :adi:`EVAL-AD7380FMCZ <EVAL-AD738xFMCZ>` /
:adi:`EVAL-AD7381FMCZ <EVAL-AD738xFMCZ>` / :adi:`EVAL-AD7386FMCZ` boards.

FPGA-based evaluation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use these guides when evaluating with an FPGA carrier board. They
cover bitstream programming, no-OS programs and Linux boot.

.. toctree::

   On ZedBoard <zed>

.. _eval-ad738xfmcz carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7380FMCZ <EVAL-AD738xFMCZ>` / :adi:`EVAL-AD7381FMCZ <EVAL-AD738xFMCZ>` /
:adi:`EVAL-AD7386FMCZ` are, by definition, "FPGA mezzanine cards"
(FMC); that means they need a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD7380FMCZ
     - EVAL-AD7381FMCZ
     - EVAL-AD7386FMCZ
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC LPC
     - FMC LPC
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
   - - EVAL-AD7380FMCZ
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
   - - EVAL-AD7381FMCZ
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
   - - EVAL-AD7386FMCZ
     - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - No

Hardware setup
-------------------------------------------------------------------------------

On the ZedBoard, the AD738x evaluation boards connect to the FMC LPC
connector. The carrier setup requires power, UART (115200), Ethernet
(Linux), HDMI (if available) and/or JTAG (no-OS) connections. A few
typical setups are shown below.

ZedBoard + EVAL-AD7380FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad7380_setup.jpg
   :width: 800

ZedBoard + EVAL-AD7381FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad7381_setup.jpg
   :width: 800

ZedBoard + EVAL-AD7386FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad7386_setup.jpg
   :width: 800
