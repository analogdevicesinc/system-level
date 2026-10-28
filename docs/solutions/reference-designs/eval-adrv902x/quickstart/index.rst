.. _adrv902x quickstart:

Quick start
===============================================================================

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>`
boards on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On VCK190 <vck190>
   On ZCU102 <zcu102>

.. _adrv902x carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-ADRV9026
     - EVAL-ADRV9029
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - FMCA
     - FMCA
   - - :xilinx:`VCK190`
     - FMCP1
     - FMCP1
   - - :xilinx:`VCU118`
     - FMCP
     - FMCP
   - - :xilinx:`ZCU102`
     - FMC HPC1
     - FMC HPC1

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - HDL
     - Linux software
     - No-OS software
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - Yes
     - Yes
     - ---
   - - :xilinx:`VCK190`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`VCU118`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes

Hardware Setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-ADRV9026/ADRV9029 <EVAL-ADRV9026>` boards
connects to the HPC1 connector (unless otherwise noted). The carrier setup
requires power, UART (115200), Ethernet (Linux), HDMI (if available) and/or
JTAG (no-OS) connections. A few typical setups are shown below.

A10SoC + EVAL-ADRV9026/ADRV9029
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TO BE ADDED

VCK190 + EVAL-ADRV9026/ADRV9029
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/adrv9026_vck190_setup.jpg
   :width: 800

VCU118 + EVAL-ADRV9026/ADRV9029
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TO BE ADDED

ZCU102 + EVAL-ADRV9026/ADRV9029
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../images/adrv9026_zcu102_setup.jpg
   :width: 800

Unboxing guide
-------------------------------------------------------------------------------

:ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/5482.AD9371-and-ADRV9009-setup-with-ZCU102-or-ZC706-April2019.pdf>`
