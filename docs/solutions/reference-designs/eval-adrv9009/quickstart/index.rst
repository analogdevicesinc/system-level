.. _adrv9009 quickstart:

Quick Start
================================================================================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`,
:adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>` and
:adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>` boards on various FPGA development
boards. They will discuss how to program the bitstream, run a no-OS program or
boot a Linux distribution.

.. toctree::
   :maxdepth: 1

   On ZCU102 <zcu102>
   On ZC706 <zc706>
   On KCU105 <kcu105>
   On Arria 10 GX <a10gx>
   On Arria 10 SoC <a10soc>

.. _adrv9009 carriers:

Supported Carriers
--------------------------------------------------------------------------------

The :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`,
:adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>` and
:adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>` are, by definition, "FPGA mezzanine
cards" (FMC), which means it needs a carrier to plug into.
The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Board
     - ADRV9009-W/PCBZ
     - ADRV9008-1W/PCBZ
     - ADRV9008-2W/PCBZ
   * - :xilinx:`ZCU102`
     - FMC HPC1
     - FMC HPC1
     - FMC HPC1
   * - :xilinx:`ZC706`
     - FMC HPC
     - FMC HPC
     - FMC HPC
   * - :xilinx:`KCU105`
     - FMC HPC
     - ---
     - ---
   * - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - FMCA
     - FMCA
     - FMCA
   * - :intel:`Arria 10 GX <content/www/us/en/products/details/fpga/development-kits/arria/10.html>`
     - FMCA
     - FMCA
     - FMCA

Supported Environments
--------------------------------------------------------------------------------

The supported environments are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - no-OS software
   * - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`KCU105`
     - Yes
     - Yes
     - ---
   * - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
     - Yes
     - Yes
     - ---
   * - :intel:`Arria 10 GX <content/www/us/en/products/details/fpga/development-kits/arria/10.html>`
     - Yes
     - Yes
     - ---
   * - :intel:`Intel Stratix 10 SX SoC Development Kit <content/www/us/en/products/details/fpga/development-kits/stratix/10-sx.html>`
     - Yes
     - ---
     - ---

Hardware Setup
--------------------------------------------------------------------------------

In most carriers, the :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`,
:adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>` and
:adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>` boards connect to the HPC
connector (unless otherwise noted). The carrier setup requires power, UART
(115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections.
A few typical setups are shown below.

ZCU102 + ADRV9009/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9009_zcu102_quickstart.png
   :width: 800

ZC706 + ADRV9009/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9009_zc706.jpeg
   :width: 800

KCU105 + ADRV9009/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9009_kcu105_setup.jpeg
   :width: 800

Arria 10 SoC + ADRV9009/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9009_a10soc.jpeg
   :width: 800

Arria 10 GX + ADRV9009/PCBZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/arria10-fpga_adrv9009.jpg
   :width: 800
