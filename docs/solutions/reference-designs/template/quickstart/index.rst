.. _template quickstart:

Quick start guide
===============================================================================

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`EVALUATION BOARD`
boards on various FPGA development boards. In these guides, we will discuss how
to program the bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::

   On A10SoC <a10soc>
   On VCK190 <versal>
   On ZCU102 <zynqmp>

.. _template carriers:

Supported carriers
-------------------------------------------------------------------------------

.. Say also the FMC port where it should be connected

The :adi:`EVALUATION BOARD`, is, by definition a "FPGA
mezzanine card" (FMC); that means it needs a carrier to plug into.

The carriers we support are:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD9081
     - EVAL-AD9082
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - FMCA
     - ---
   - - `FM87 <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1305>`__
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

Supported environments
-------------------------------------------------------------------------------

.. Say on which carrier is Linux supported and on which is no-OS supported

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
   - - `FM87 <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1305>`__
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

.. Describe in general, few words

On most carriers, the :adi:`EVALUATION BOARD` boards
connects to the HPC1 connector (unless otherwise noted). The carrier setup
requires power, UART (115200), Ethernet (Linux), HDMI (if available) and/or
JTAG (no-OS) connections. A few typical setups are shown below.

ZCU102 + EVALUATION BOARD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..
  Add image here with the setup on ZCU102. The file should be named like this:
  evaluationboard_carrier_setup.jpg or .png. The order should be followed!
  The images should all be stored in docs/solutions/reference-designs/images

.. image:: ../../images/adrv9026_zcu102_setup.jpg
   :width: 800

..
  Link the zynqmp.rst

Go to :ref:`the setup guide <template quickstart zynqmp>`.

.. Add link to an unboxing guide, if exists
.. Unboxing guide
.. -------------------------------------------------------------------------------
..
.. :ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/AD9371-and-ADRV9026-setup-with-ZCU102-or-ZC706-April2019.pdf>`
