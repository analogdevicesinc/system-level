.. _adrv9002 quickstart:

ADRV9001/2 Quick Start Guides
================================================================================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>`
and :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` boards on various FPGA
development boards. They will discuss how to program the bitstream, run a
no-OS program or boot a Linux distribution.

.. note::

   The ADRV9002 evaluation boards come in two variants:

   - **W1**: Narrowband variant
   - **W2**: Wideband variant

.. toctree::
    zcu102
    zc706
    zed
    a10soc

.. _adrv9002 carriers:

Supported Carriers
--------------------------------------------------------------------------------

The :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and
:adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` is, by definition a "FPGA
mezzanine card" (FMC), that means it needs a carrier to plug into. The
carriers we support are:

.. list-table::
   :header-rows: 2
   :widths: 40 15 15 15

   * - Board
     - ADRV9002/*
     -
     -
   * -
     - **FMC Connector**
     - **CMOS interface**
     - **LVDS interface**
   * - `ZCU102 <https://www.xilinx.com/ZCU102>`_
     - HPC0
     - Yes
     - Yes
   * - `ZC706 <https://www.xilinx.com/ZC706>`_
     - LPC
     - Yes **VADJ 1.8V**\ ¹
     - N/A²
   * - `Zed Board <http://zedboard.org/product/zedboard>`_
     - LPC
     - Yes **VADJ 1.8V**
     - N/A²
   * - `Arria 10 SoC <https://www.altera.com/products/devkit/po-3006/arria-10-sx-soc-development-kit>`__
     - FMCA
     - Yes
     - N/A³

| ¹ Instruction for reprogramming the VADJ can be found in the `official guide <https://www.xilinx.com/Attachment/ZC706_Power_Controllers_Reprogramming_Steps.pdf>`_ and in this `forum thread <https://forums.xilinx.com/t5/Xilinx-Evaluation-Boards/ZC706-Doesn-t-work-with-VADJ-at-1-8v/td-p/430086>`_
| ² Cmos only operation
| ³ Not supported due sub-optimal mapping of the clock pins from the
    source synchronous interfaces.

CMOS only operation
--------------------------------------------------------------------------------

On the ZC706 / ZedBoard platforms the FMC connectors map to HR IO banks.
The HR banks have a limitation that when using LVDS I/O standard you must
set the bank VCCO voltage to 2.5V, however the ADRV9001 evaluation board
is using IO supplies of 1.8V and does not have level shifters for the
single ended lines. Therefore the VCCO of the banks must be set to 1.8 V
(VADJ) and limiting the operation to CMOS mode only. More information on
the limitation see `7 Series Select IO guide <https://www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`_
section 'LVDS and LVDS_25' and Table 1-43

Supported Environments
--------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1
   :widths: 50 10 15 15 10

   * - Board
     - HDL
     - Linux Software
     - No-OS Software
     - Required Minimum Release
   * - `ZCU102 <https://www.xilinx.com/ZCU102>`_
     - Yes
     - Yes
     - Yes
     - 2019-R2
   * - `ZC706 <https://www.xilinx.com/ZC706>`_
     - Yes
     - Yes
     - Yes
     - 2020-R1
   * - `Zed Board <http://zedboard.org/product/zedboard>`_
     - Yes
     - Yes
     - Yes
     - 2019-R2
   * - `Arria 10 SoC <https://www.altera.com/products/devkit/po-3006/arria-10-sx-soc-development-kit>`__
     - Yes
     - Yes
     - ---
     - 2020-R1

Hardware Setup
--------------------------------------------------------------------------------

The carrier setup requires power, UART (115200), ethernet (Linux), DisplayPort
or HDMI (if available) or JTAG (no-OS) connections. A few typical setups are
shown below.

ZedBoard + EVAL-ADRV9002
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9002_zed_quickstart.png
   :align: center
   :width: 900

ZCU102 + EVAL-ADRV9002
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9002_zcu102_quickstart.png
   :align: center
   :width: 900

ZC706 + EVAL-ADRV9002
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9002_zc706_quickstart.png
   :align: center
   :width: 900

A10SOC + EVAL-ADRV9002
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/adrv9002_a10soc_quickstart.png
   :align: center
   :width: 900

Identify your hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Evaluation boards were equipped with different silicon revisions. All
boards built since the middle of December 2020 have C0 silicon, older ones
use B0 silicon these are no longer shipped. You can identify the board you
have based on its label.

.. list-table::
   :header-rows: 1
   :widths: 50 25 25

   * - Label
     - Silicon Revision
     - Variant
   * - .. image:: ../images/adrv9002_b0_np_w1.png
          :width: 100
     - **B0**
     - **W1** (Narrowband)
   * - .. image:: ../images/adrv9002_b0_np_w2.png
          :width: 100
     - **B0**
     - **W2** (Wideband)
   * - .. image:: ../images/adrv9002xbcz_c0_np_w1.png
          :width: 100
     - **C0**
     - **W1** (Narrowband)
   * - .. image:: ../images/adrv9002xbcz_c0_np_w2.png
          :width: 100
     - **C0**
     - **W2** (Wideband)

.. tip::

   Each revision of silicon requires its corresponding software support
   files in the later steps.
