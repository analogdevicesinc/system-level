.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9026/quickstart

.. _adrv9026 quickstart:

ADRV9026 Quick Start Guides
===========================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page
   is outdated and the new one can be found at

   https://analogdevicesinc.github.io/documentation/eval/user-guide/transceiver/adrv9026/quickstart/index.html

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the
:adi:`EVAL-ADRV9026/ADRV9029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV9026.html>`
boards on various FPGA development boards. They will discuss how to program the
bitstream, run a no-OS program, or boot a Linux distribution.

Supported Carriers
------------------

The
:adi:`EVAL-ADRV9026/ADRV9029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV9026.html>`
is, by definition a ``FPGA mezzanine card`` (FMC), that means it needs a carrier
to plug into. The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Board
     - EVAL-ADRV9026/ADRV9029
     -
   * - :xilinx:`ZCU102 <ZCU102>`
     - √
     -
   * - `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__
     - WIP
     -

Supported Environments
----------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux Software
     - No-OS Software
     -
   * - :xilinx:`ZCU102 <ZCU102>`
     - √
     - √
     - √
     -
   * - `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__
     - WIP
     - WIP
     - WIP
     -

Hardware Setup
--------------

The
:adi:`EVAL-ADRV9026/ADRV9029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV9026.html>`
boards connects to the HPC1 connector (unless otherwise noted). The carrier
setup requires power (12VDC 3A MAX), UART (115200), ethernet (Linux), HDMI (if
available) and/or JTAG (no-OS) connections. A few typical setups are shown
below.

ZCU102 + EVAL
~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/adrv9009_zcu102_quickstart.png
   :width: 800px

Unboxing guide
~~~~~~~~~~~~~~

Detailed description of the setup procedure for ADRV9009 (similar procedure for
ADRV9026/9029):

:ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/AD9371-and-ADRV9009-setup-with-ZCU102-or-ZC706-April2019.pdf>`
