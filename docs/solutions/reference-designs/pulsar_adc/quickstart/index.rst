.. _pulsar-adc quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide a simple step by step instruction on how to do
an initial system setup for the PulSAR ADC evaluation boards on various FPGA
development boards. They will discuss how to program the bitstream, run a no-OS
program or boot a Linux distribution.

.. toctree::
   :glob:

   ZedBoard <zedboard>
   CoraZ7-07S <coraz7s>

.. _pulsar-adc carriers:

Supported carriers
-------------------------------------------------------------------------------

The carriers we support are:

- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__ on FMC connector (for EVAL-AD400x-FMCZ)
- `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__ on PMOD connector (for EVAL-ADAQ40xx)

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - Board
     - HDL
     - Linux Software
     - No-OS Software
   - - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - Yes
     - Yes
   - - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     - Yes
     - Yes
     - No

Hardware Setup
-------------------------------------------------------------------------------

The PulSAR ADC evaluation boards connect to the FMC or PMOD connector
(depending on the variant). The carrier setup requires power,
UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS)
connections.

A few typical setups are shown below.

ZedBoard + EVAL-AD400x-FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad4020_zed.jpg
   :align: center
   :width: 500

CoraZ7-07S + EVAL-ADAQ40xx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adaq4003_coraz7s.jpg
   :align: center
   :width: 500
