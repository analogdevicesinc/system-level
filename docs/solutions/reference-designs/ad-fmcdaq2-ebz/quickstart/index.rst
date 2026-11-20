.. _ad_fmcdaq2_ebz quickstart:

Quickstart
===============================================================================

The Quick start guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`AD-FMCDAQ2-EBZ` boards on various FPGA
development boards. In these guides, we will discuss how to program the
bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::
   :maxdepth: 1

   On A10SOC <a10soc>
   On MICROBLAZE <microblaze>
   On ZC706  <zc706>
   On ZCU102 <zcu102>

.. _ad_fmcdaq2_ebz carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`AD-FMCDAQ2-EBZ` is an FMC (FPGA Mezzanine Card), meaning it requires a
compatible carrier board. The officially supported carriers are listed below, as
documented in the ADI Quick Start Guides.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board:

.. list-table::
   :header-rows: 1

   - - FPGA board
     - EVAL-AD-FMCDAQ2-EBZ
   - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - FMC HPC1
   - - :xilinx:`KCU105`
     - FMC HPC
   - - :xilinx:`ZC706`
     - FMC HPC
   - - :xilinx:`ZCU102`
     - FMC0 HPC0

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
   - - :xilinx:`KCU105`
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

Hardware Setup
-------------------------------------------------------------------------------

On most carriers, the :adi:`AD-FMCDAQ2-EBZ` board connects to the HPC connector
(unless otherwise noted). The carrier setup requires power, UART (115200),
ethernet (for Linux), HDMI (if available) and/or JTAG (for no‑OS). A few typical
setups are shown below.

A10SOC + AD-FMCDAQ2-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./../images/ad-fmcdaq2-ebz_a10soc_setup.jpg

KCU105 + AD-FMCDAQ2-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./../images/ad-fmcdaq2-ebz_kcu105_setup.jpg

ZC706 + AD-FMCDAQ2-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./../images/ad-fmcdaq2-ebz_zc706_linux.jpg

ZCU102 + AD-FMCDAQ2-EBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./../images/ad-fmcdaq2-ebz_zcu102_setup_linux.png
