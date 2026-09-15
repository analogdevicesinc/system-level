.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv904x/quickstart

.. _adrv904x quickstart-DUPLICATED:

ADRV904x Quick Start Guides
===========================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the
:adi:`ADRV904x-HB/PCBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV904x.html>`
boards on various FPGA development boards. They will discuss how to program the
bitstream, run a no-OS program, or boot a Linux distribution.

Supported Carriers
------------------

The
:adi:`ADRV904x-HB/PCBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV904x.html>`
is, by definition a ``FPGA mezzanine card`` (FMC), that means it needs a carrier
to plug into. The carriers we support are:

.. list-table::
   :header-rows: 1

   * - Board
     - ADRV904x-HB/PCBZ
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
:adi:`ADRV904x-HB/PCBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV904x.html>`
boards connects to the HPC2 connector (unless otherwise noted). The carrier
setup requires power (12VDC 3A MAX), UART (115200), ethernet (Linux), HDMI (if
available) and/or JTAG (no-OS) connections. A few typical setups are shown
below.

.. tip::

   NOTE: Three jumpers must be mounted on the board on the following headers
   with the following settings:

   #. P209 - GPIO4_FMC
   #. P216 - GPIO11_FMC
   #. P2021 - TEST connected to GND

ZCU102 + EVAL
~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv904x/adrv904x-zcu102-quickstart.jpeg
   :width: 600px

Unboxing guide
~~~~~~~~~~~~~~

Detailed description of the setup procedure for ADRV9009 (similar procedure for
ADRV904x):

:ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/AD9371-and-ADRV9009-setup-with-ZCU102-or-ZC706-April2019.pdf>`
