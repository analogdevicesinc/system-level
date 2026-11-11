.. _eval-adar3000 quickstart:

Quickstart
===============================================================================

The quick start guides provide simple step by step instructions on how to do
an initial system setup for the ADAR3000/3001-EVALZ board on the supported
FPGA development boards.

.. toctree::

   On ZCU102 <zcu102>

.. _eval-adar3000 carriers:

Supported carriers
-------------------------------------------------------------------------------

The ADAR3000/3001-EVALZ connects to the carrier through an SDP-I-FMC
interposer, which plugs into an FMC connector of the carrier.

.. list-table::
   :header-rows: 1

   - - FPGA board
     - ADAR3000/3001-EVALZ
   - - :xilinx:`ZCU102`
     - FMC HPC1, through the SDP-I-FMC interposer

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes

Hardware setup
-------------------------------------------------------------------------------

The carrier setup requires the bench supplies of the evaluation board, the
carrier's power supply, and UART and JTAG connections to the host PC.

ZCU102 + ADAR3000/3001-EVALZ
-------------------------------------------------------------------------------

.. image:: ../images/adar3000_zcu102_setup.jpg
   :alt: ZCU102 with the SDP-I-FMC interposer and the evaluation board
   :width: 800

Go to :ref:`the setup guide <eval-adar3000 quickstart zcu102>`.
