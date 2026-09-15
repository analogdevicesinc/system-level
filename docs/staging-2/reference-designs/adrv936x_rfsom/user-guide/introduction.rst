.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/user-guide/introduction

.. _adrv936x_rfsom user-guide introduction:

ADRV9361-Z7035 User Guide - Introduction
========================================

The ADRV9361-Z7035 is a Software Defined Radio (SDR) that combines the Analog
Devices AD9361 integrated RF Agile Transceiver™ with the Xilinx Z7035 Zynq®-7000
All Programmable SoC in a small system-on-module (SOM) footprint suitable for
end-product integration.

Analog Devices carrier cards are available for fast prototype and are supported
by robust simulation and code generation tools that integrate seamlessly with
Xilinx Vivado® Design Suite. The final step for most applications includes
designing a custom carrier card to mate with the ADRV9361 SDR SOM for end
product deployment.

Key Features
------------

- *Low-power:* Designed with a -2LI version of the Zynq SoC (low power, mid
  speed, industrial temp), DDR3L, and high-efficiency voltage regulators with
  margining capability to scale power with performance. Built-in sequencing and
  monitoring make it easy to power to the module.
- *High bandwidth data connectivity:* Move data quickly with dual Gigabit
  Ethernet, USB2.0, four 6.6 Gb/s serial links (PCIe x4, SFP+, others), and
  high-speed LVDS I/O for custom interfaces.
- *Wideband, frequency agile RF:* Uses the AD9361 to provide a highly integrated
  radio that enables wideband 2x2 MIMO receive and transmit paths from 70 MHz to
  6.0 GHz with tunable channel bandwidth <200kHz to 56MHz.
- *Programmable SoC:* Embedded processing with the Zynq Z-7035 SoC provides a
  Dual ARM® Cortex™-A9 MPCore™ running at 800MHz, with built in peripherals like
  USB, Gigabit Ethernet, and memory interfaces.
- *Small form factor:* 100mm x 62mm footprint, compliant with `DP10062
  ``Sick of Beige v1.0 <http://dangerousprototypes.com/docs/Sick_of_Beige_standard_PCB_sizes_v1.0>`__
  DP10062 ``Sick of Beige v1.0`` enclosures from
  `dangerousprototypes.com <http://dangerousprototypes.com/docs/Sick_of_Beige_standard_PCB_sizes_v1.0>`__.
- *Production-ready module:* System-on-Module designed for immediate prototype
  and quick integration in your end application. Industrial temperature rated
  and tested against MIL-STD 202G methods for Thermal, Vibration, and Shock.
- *Operating systems:* Comes with Analog Devices Linux reference design for
  Zynq, bootable from an SD card. Also supports Linux, Android, FreeRTOS, eCos,
  VxWorks, and others listed here.
- *Development tools:* A broad range of SDR prototype and development
  environments are supported, including Analog Devices Linux Applications, and
  MATLAB® and Simulink® for data streaming and Zynq targeting.
- *Open-source code:* Analog Devices provides precompiled reference designs on
  the
  :dokuwiki:`ADRV9361 Wiki Page </resources/eval/user-guides/adrv936x_rfsom>`
  and a source code support package hosted on Github, including the HDL and
  software code.

Module Specs
------------

The module specifications are summarized below. The rest of the document
provides details.

.. list-table::
   :header-rows: 1

   * - Radio
     - Analog Devices AD9361 integrated RF Agile Transceiver™
   * - RF Band
     - 70MHz to 6.0GHz
   * - Tunable Channel BW
     - <200kHz to 56MHz
   * - RF Connections
     - 4 TX, 4RX, 2 TX monitor
   * - Max output power
     - 6.5 – 8.0 dBm (typical) – see AD9361 datasheet for details
   * - Max input power (RX)
     - 2.5 dBm (peak)
   * - Max input power (TX mon.)
     - 9 dBm (peak)
   * - **Processing**
     - Xilinx Zynq XC7Z035-L2 FBG676I AP SoC
   * - Processor
     - Dual ARM® Cortex™-A9 MPCore™ running at 800MHz
   * - Programmable Logic
     - 275K Kintex-7 logic cells with 900 DSP48 slices
   * - **Interface**
     - Four 100-pin Micro Headers
   * - Peripherals
     - ARM: Gigabit Ethernet, USB2.0, UART, SDIO
   * - User I/O
     - 209 single-ended or 93 LVDS (up to 1250 or 1400 Mb/s DDR)
   * - Serial transceivers
     - 4 Zynq GTX channels @ 6.6Gb/s
   * - **Memory**
     -
   * - DDR3L
     - 1GB DDR3L (low power) @ 1,066 Mb/s
   * - Flash
     - 256 Mb QSPI Flash (bootable) @ 400Mb/s
   * - SD card
     - Lockable Micro SD Card cage (bootable) @ 25MB/s
   * - **Power Consumption**
     - < 5Watts (typical)
   * - Main Module Supply
     - 4.5V – 5.5V (5.0V nominal)
   * - Module I/O Supplies
     - 1.0V – 3.3V
   * - **Operating system support**
     - Linux, Android, FreeRTOS, eCos, VxWorks, and others
   * - **Debug**
     - JTAG
   * - **Dimensions**
     - 100mm x 62mm
   * - **Operating Temp Industrial**
     - -40°C to +85°C (1)

(1) uSD cage rated to -25°C to +85°C operating temperature

Important! ADRV9361-Z7035 is not pin compatible with standard PicoZed (non-SDR)
carrier cards. New pinouts were required mainly for the Zynq Z-7035 and AD9361
digital I/O.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/user-guide/simplified_system_diagram.png
   :width: 800px

Simplified System Diagram

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/user-guide/adrv9361-z7035_device_callout.png
   :width: 800px

ADRV9361-Z7035 SOM Device Callout
