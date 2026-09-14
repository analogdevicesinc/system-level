.. _ad9081 quickstart:

Quick start guides
===============================================================================

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVAL-AD9081` / :adi:`EVAL-AD9082`
boards on various FPGA development boards. In these guides, we will discuss
how to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On A10SoC <a10soc>
   On VCK190 <vck190>
   On ZC706 <zc706>
   On VCU118 <vcu118>
   On ZCU102 <zcu102>

.. _ad9081 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9081` / :adi:`EVAL-AD9082`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

.. note::

   :adi:`EVAL-AD9988` can be an alternative to
   :adi:`AD9081-FMCA-EBZ <EVAL-AD9081>` and :adi:`EVAL-AD9986`
   can be an alternative to :adi:`AD9082-FMCA-EBZ <EVAL-AD9082>`.

   Both :adi:`AD9081` and :adi:`AD9988` have MxFE Quad, 16-bit, 12 GSPS RF DAC
   & Quad, 12-bit, 4 GSPS RF ADC,

   The same goes for :adi:`AD9082` and :adi:`AD9986`, both have MxFE Quad,
   16-bit, 12 GSPS RF DAC & Dual, 12-bit, 6 GSPS RF ADC.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD9081
     - EVAL-AD9082
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - FMCA
     - ---
   - - :intel:`FM87 <content/www/us/en/products/details/fpga/development-kits/agilex/si-agi027.html>`
     - FMCA
     - ---
   - - :xilinx:`VCK190`
     - FMCP1 (J51)
     - FMCP1 (J51)
   - - :xilinx:`VPK180`
     - FMCP1
     - FMCP1
   - - :xilinx:`VCU118`
     - FMC+
     - FMC+
   - - :xilinx:`ZC706`
     - FMC HPC
     - FMC HPC
   - - :xilinx:`ZCU102`
     - FMC HPC0
     - FMC HPC0

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
   - - :intel:`FM87 <content/www/us/en/products/details/fpga/development-kits/agilex/si-agi027.html>`
     - ---
     - ---
     - ---
   - - :xilinx:`VCK190`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`VPK180`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`VCU118`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   - - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes

Hardware setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`EVAL-AD9081` / :adi:`EVAL-AD9082` boards
connect to the HPC1 connector (unless otherwise noted). The carrier setup
requires power, UART (115200), Ethernet (Linux), HDMI (if available) and/or
JTAG (no-OS) connections. A few typical setups are shown below.

ZCU102 + EVAL-AD9081
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../images/ad9081_zcu102_setup.png
   :width: 800

   ZCU102 + EVAL-AD9081 setup

VCK190 + EVAL-AD9081
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../images/ad9081_vck190_setup.jpg
   :width: 800

   VCK190 + EVAL-AD9081 setup
