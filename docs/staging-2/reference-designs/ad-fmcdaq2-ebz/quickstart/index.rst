.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart

.. _ad-fmcdaq2-ebz quickstart:

AD-FMCDAQ2-EBZ Quick Start Guides
=================================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the AD-FMCDAQ2-EBZ boards on various FPGA development
boards. They will discuss how to program the bitstream, run a no-OS program or
boot a Linux distribution.

Supported Carriers
------------------

The AD-FMCDAQ2-EBZ is, by definition a ``FPGA mezzanine card`` (FMC), that means
it needs a carrier to plug into. The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Board
     - Quickstart Guide
     -
     -
   * - `Arria10 SoC Dev Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__
     - :dokuwiki:`AD-FMCDAQ2-EBZ Arria10 SoC Development Kit Quick Start Guide </quickstart/a10soc>`
     -
     -
   * - `Arria10 GX FPGA Dev Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/kit-a10-gx-fpga.html>`__
     - :dokuwiki:`AD-FMCDAQ2-EBZ Arria10 GX FPGA Development Kit Quick Start Guide </quickstart/a10soc>`
     -
     -
   * - :xilinx:`KC705 <KC705>`
     - :dokuwiki:`AD-FMCDAQ2-EBZ Microblaze Quick Start Guide </quickstart/microblaze>`
     -
     -
   * - :xilinx:`KCU105 <KCU105>`
     - :dokuwiki:`AD-FMCDAQ2-EBZ Microblaze Quick Start Guide </quickstart/microblaze>`
     -
     -
   * - :xilinx:`VC707 <VC707>`
     - :dokuwiki:`AD-FMCDAQ2-EBZ Microblaze Quick Start Guide </quickstart/microblaze>`
     -
     -
   * - :xilinx:`ZC706 <ZC706>`
     - :dokuwiki:`AD-FMCDAQ2-EBZ Zynq ZC706 Quick Start Guide </quickstart/zynq>`
     -
     -
   * - :xilinx:`ZCU102 <ZCU102>`
     - :dokuwiki:`AD-FMCDAQ2-EBZ ZynqMP ZCU102 Quick Start Guide </resources/eval/user-guides/ad-fmcdaq2-ebz/quickstart/zcu102>`
     -
     -

The supported OS are:

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux Software
     - No-OS Software
     -
     -
   * - `Arria10 SoC Dev Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__
     - YES
     - NO
     - YES
     -
     -
   * - `Arria10 GX FPGA Dev Kit <https://www.altera.com/products/boards_and_kits/dev-kits/altera/kit-a10-gx-fpga.html>`__
     - NO (only until
       :git-hdl:`hdl_2021_r1 <tree/hdl_2021_r1/projects/daq2/a10gx+>` branch)
     - NO
     - YES
     -
     -
   * - :xilinx:`KC705 <KC705>`
     - YES
     - YES
     - YES
     -
     -
   * - :xilinx:`KCU105 <KCU105>`
     - YES
     - YES
     - YES
     -
     -
   * - :xilinx:`VC707 <VC707>`
     - NO (only until
       :git-hdl:`hdl_2018_r2 <tree/hdl_2018_r2/projects/daq2/vc707+>` branch)
     - YES
     - YES
     -
     -
   * - :xilinx:`ZC706 <ZC706>`
     - YES
     - YES
     - YES
     -
     -
   * - :xilinx:`ZCU102 <ZCU102>`
     - YES
     - YES
     - YES
     -
     -

Hardware Setup
--------------

In most carriers, the AD-FMCDAQ2-EBZ board connects to the HPC connector (unless
otherwise noted). The carrier setup requires power, UART (115200), ethernet
(Linux), HDMI (if available) and/or JTAG (no-OS) connections. A typical setup is
shown below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/ad-fmcdaq2-ebz_zc706.png
   :width: 800px
