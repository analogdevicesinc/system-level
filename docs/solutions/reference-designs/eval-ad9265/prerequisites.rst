.. _eval_ad9265 prerequisites:

Prerequisites
===============================================================================

Hardware prerequisites
-------------------------------------------------------------------------------

#. :adi:`EVAL-AD9265` FMC evaluation board (AD9265-FMC-125EBZ)
#. One of the supported FPGA carrier boards and its power supply:

   - AMD Xilinx :xilinx:`ZC706` Rev 1.1 or higher — 12 V power supply,
     Mini-USB for UART (J21), Micro-USB for JTAG, LAN for Ethernet (J45)
   - AMD Xilinx `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__ — 12 V power supply,
     Micro-USB for UART (J14), LAN for Ethernet (J11)

#. SMA cables for analog input connection to the evaluation board (J100)
#. Signal generator (low-jitter, low-phase-noise recommended for ADC
   evaluation)
#. SD card with at least 16 GB of storage -- required for Linux boot

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.

Software prerequisites
-------------------------------------------------------------------------------

**For Linux (Kuiper)**

#. SD card imaged with :external+kuiper:doc:`Kuiper Linux <index>`
#. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
#. :external+scopy:doc:`Scopy <index>` v2.0 or later (requires the IIO plugin)
#. UART terminal application (PuTTY/Tera Term/Minicom), 115200 8N1

**For no-OS** (ZC706 only)

#. AMD Xilinx Vitis 2025.1 or later (includes Vivado)
#. Python 3, CMake, and Ninja (required by the ``no_os_build.py`` build script)
#. UART terminal application (PuTTY/Tera Term/Minicom), 115200 8N1
