.. _adrv9361z7035 prerequisites:

Prerequisites
=============

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
----------------------

#. The ADRV9361 System on Module (SOM) board: :adi:`ADRV9361-Z7035`

#. An FPGA carrier platform. The ADRV936x RF SOM family supports multiple
   carrier boards:

   - :adi:`ADRV1CRR-FMC` - FMC Carrier with LVDS interface
   - :adi:`ADRV1CRR-BOB` - Breakout Carrier with LVDS or CMOS interface
   - Additional carriers listed in the :ref:`main documentation <adrv9361z7035>`

#. Some way to interact with the platform:

   #. For the Zynq SoC platforms, this normally includes:

      - HDMI or DisplayPort monitor
      - USB Keyboard
      - USB Mouse
      - Ethernet connection

   #. Alternatively:

      - Serial UART connection (USB to UART cable)
      - Host PC (Windows or Linux)

#. Internet connection (without proxies makes things much easier) to update
   the scripts/binaries on the SD card that came with the ADI evaluation board
   (firewalls are OK, proxies make things a pain).

#. RF Test equipment for evaluation and testing.

#. An SD card with at least 16GB of memory. You should have received one when
   purchasing the evaluation board.

Board Variants and Device Trees
--------------------------------

The ADRV9361Z7035 HDL project supports three carrier board configurations, each
with its corresponding Linux device tree:

+------------------------------------------------------+------------------------------------------------------+
| Board Variant                                        | Device Tree File                                     |
+======================================================+======================================================+
| :git-hdl:`CCBOB-CMOS                                 | :git-linux:`arch/arm/boot/dts/xilinx/                |
| <projects/adrv9361z7035/ccbob_cmos>`                 | zynq-adrv9361-z7035-bob-cmos.dts`                    |
|                                                      |                                                      |
| ADRV1CRR-BOB with CMOS interface                     |                                                      |
+------------------------------------------------------+------------------------------------------------------+
| :git-hdl:`CCBOB-LVDS                                 | :git-linux:`arch/arm/boot/dts/xilinx/                |
| <projects/adrv9361z7035/ccbob_lvds>`                 | zynq-adrv9361-z7035-bob.dts`                         |
|                                                      |                                                      |
| ADRV1CRR-BOB with LVDS interface                     |                                                      |
+------------------------------------------------------+------------------------------------------------------+
| :git-hdl:`CCFMC-LVDS                                 | :git-linux:`arch/arm/boot/dts/xilinx/                |
| <projects/adrv9361z7035/ccfmc_lvds>`                 | zynq-adrv9361-z7035-fmc.dts`                         |
|                                                      |                                                      |
| ADRV1CRR-FMC with LVDS interface                     |                                                      |
+------------------------------------------------------+------------------------------------------------------+

For detailed information about each variant, refer to the
:external+hdl:ref:`HDL Reference Design <adrv9361z7035>`.

Software prerequisites
----------------------

For basic functionalities regarding visualizing and analyzing the data received
from the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain the IIO
   plugin), or :ref:`IIO Oscilloscope <iio-oscilloscope>`

#. :ref:`Kuiper Linux <kuiper>` - ADI's customized Linux distribution for SDR
   platforms (recommended)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
