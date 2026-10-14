.. _pluto devs specs:

Detailed Specifications
========================

.. figure:: ../users/images/intro/pluto_on_desk.png
   :width: 200

Features List:

- :adi:`ADI AD9363, RF Agile Transceiver <AD9363>`:

  - 1 Transmit, 1 Receive channel (with separate tuning frequencies)
  - Tuning range: 325 MHz - 3.8 GHz

    - 2.4 Hz LO step size

  - Tunable channel bandwidth: 200 kHz - 20 MHz
  - Integrated 12-bit DACs (Tx) and ADCs (Rx)
  - Variable output data rates: 61.44 MSPS - 65.1 kSPS
  - Modulation Accuracy (EVM): ≤−40 dB (typical, not measured on every unit)
  - Internal I/Q correction and calibration
  - Tx to Rx Isolation
  - Rx gain control: 0 to +74.5dB (800 MHz)

    - Manual Modes
    - Slow Attack
    - Fast Attack

  - Received Signal Strength Indicator: 100 dB (±2 dB)

- :xilinx:`Xilinx Zynq <products/silicon-devices/soc.html>` XC7Z010-1CLG225C

  - :xilinx:`Zynq-7000 All Programmable SoC Overview <support/documentation/data_sheets/ds190-Zynq-7000-Overview.pdf>`
  - :xilinx:`Datasheet <support/documentation/data_sheets/ds187-XC7Z010-XC7Z020-Data-Sheet.pdf>`
  - FPGA

    - Logic Cells: 28k
    - Block RAM: 2.1Mb
    - DSP Slices: 80

  - ARM Processing System

    - Single-core ARM® Cortex™-A9 MPCore™
    - 667 MHz

  - USB 2.0 (included in the Zynq)

    - streams up to 4MSPS with no dropped samples

- Memory

  - Micron DDR3L

    - `MT41K256M16TW-107 <https://www.micron.com/parts/dram/ddr3-sdram/mt41k256m16tw-107-it>`__
    - 1066 Mbps (16-bit interface)
    - 512 MBytes

  - Micron Serial Flash

    - `MT25QU256ABA8E12-1SIT <https://www.micron.com/products/nor-flash/serial-nor-flash/part-catalog/mt25qu256aba8e12-1sit>`__
    - 32 Mbyte
    - Quad I/O provides throughput up to 54 MBps
    - Minimum 100,000 ERASE cycles (don't update the firmware more times than this)

- Power

  - Completely self powered from USB
  - Optional power connector
