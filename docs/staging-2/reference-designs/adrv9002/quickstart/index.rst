.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9002/quickstart

.. _adrv9002 quickstart:

ADRV9001/2 Quick Start Guides
=============================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and
:adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` boards on various FPGA development
boards. They will discuss how to program the bitstream, run a no-OS program or
boot a Linux distribution.

Supported Carriers
------------------

The :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and
:adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` is, by definition a ``FPGA mezzanine
card`` (FMC), that means it needs a carrier to plug into. The carriers we
support are:

.. list-table::
   :header-rows: 1

   * - Board
     - ADRV9002NP
     -
     -
   * -
     - **CMOS inteface**
     - **LVDS interface**
     -
   * - :xilinx:`ZCU102 <ZCU102>`
     - √
     - √
     -
   * - :xilinx:`ZC706 <ZC706>`
     - √ **:red:`VADJ 1.8V`**\ ¹
     - N/A²
     -
   * - `Zed Board <http://zedboard.org/product/zedboard>`__
     - √ **:red:`VADJ 1.8V`**
     - N/A²
     -
   * - `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__
     - √
     - N/A³
     -

¹ Instruction for reprogramming the VADJ can be found
:xilinx:`here <Attachment/ZC706_Power_Controllers_Reprogramming_Steps.pdf>` and
`here <https://forums.xilinx.com/t5/Xilinx-Evaluation-Boards/ZC706-Doesn-t-work-with-VADJ-at-1-8v/td-p/430086>`__
² See
:dokuwiki:`Cmos only operation </resources/eval/user-guides/adrv9002/quickstart##cmos_only_operation>`
section ³ Not supported due sub-optimal mapping of the clock pins from the
source synchronous interfaces.

CMOS only operation
-------------------

On the ZC706 / ZedBoard platforms the FMC connectors map to HR IO banks. The HR
banks have a limitation that when using LVDS I/O standard you must set the bank
VCCO voltage to 2.5V, however the ADRV9001 evaluation board is using IO supplies
of 1.8V and does not have level shifters for the single ended lines. Therefore
the VCCO of the banks must be set to 1.8 V (VADJ) and limiting the operation to
CMOS mode only. More information on the limitation see
`7 Series Select IO guide <https://www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`__
section "LVDS and LVDS_25" and Table 1-43

Supported Environments
----------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux Software
     - No-OS Software
     - Required Minimum Release
     -
   * - :xilinx:`ZCU102 <ZCU102>`
     - √
     - √
     - √
     - 2019-R2
     -
   * - :xilinx:`ZC706 <ZC706>`
     - √
     - √
     - √
     - 2020-R1
     -
   * - `Zed Board <http://zedboard.org/product/zedboard>`__
     - √
     - √
     - √
     - 2019-R2
     -
   * - `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`__
     - √
     - √
     - N/A
     - 2020-R1
     -

Hardware Setup
--------------

In most carriers, the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and
:adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` boards connects to the HPC1 connector
(unless otherwise noted). The carrier setup requires power, UART (115200),
ethernet (Linux), DisplayPort or HDMI (if available) and/or JTAG (no-OS)
connections. A few typical setups are shown below.

Identify your hardware
~~~~~~~~~~~~~~~~~~~~~~

Evaluation boards were equipped with different silicon revisions. All boards
built since the middle of December 2020 have C0 silicon, older ones use B0
silicon these are no longer shipped. You can identify the board you have based
on its label.

.. list-table::
   :header-rows: 1

   * - Label
     - Silicon Revision
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002_b0_np_w1.png

     - **B0**
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002_b0_np_w2.png

     - **B0**
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002xbcz_c0_np_w1.png

     - **C0**
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002xbcz_c0_np_w2.png

     - **C0**

.. tip::

   Each revision of silicon requires its corresponding software support files in
   the later steps.

ZCU102 + ADRV9002NP
-------------------

:dokuwiki:`ADRV9002 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </resources/eval/user-guides/adrv9002/quickstart/zynqmp>`

ZC706 + ADRV9002NP
------------------

:dokuwiki:`ADRV9002 Zynq SoC ZC706 Quick Start Guide </resources/eval/user-guides/adrv9002/quickstart/zynq>`

Zed Board + ADRV9002NP
----------------------

:dokuwiki:`ADRV9002 Zynq Zed Board Quick Start Guide </resources/eval/user-guides/adrv9002/quickstart/zed>`

============

.. todo:: .. include: /resources/eval/user-guides/adrv9002/common.rst

   :start-after: .. start-#more-information
   :end-before: .. end-#more-information

.. todo:: .. include: /resources/eval/user-guides/adrv9002/common.rst

   :start-after: .. start-#support
   :end-before: .. end-#support
