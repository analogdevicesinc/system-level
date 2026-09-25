ADRV9361-Z7035 User Guide - Additional Information
==================================================

Power Specs
-----------

Designers may find the following additional information valuable when
considering a power scheme for the ADRV9361-Z7035 SDR 2X2.

SOM Voltage Regulators and Rails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the voltages supplied to the SOM on the micro headers, the module
uses the 5.0V VIN input to regulate a variety of other voltages required by the
system, summarized in the following table.

Regulated Voltage Rails

+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| Schematic Voltage Name | Voltage(V)   | Schematic Symbol | Max Output Current (A) | Notes                                         |
+========================+==============+==================+========================+===============================================+
| VCCINT-0P95V           | 0.95         | U4               | 1.8                    | VCCINT                                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VCC-BRAM               | 0.95         | U4               | 1.8                    | VCCBRAM                                       |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VCCPINT                | 1.0          | U4               | 1.8                    | VCCPINT                                       |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VCC-1P35               | 1.35         | U4               | 1.8                    | DDR3L Zynq DDR Bank 502                       |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VCCO-DDR               | 1.35         | U4               | 1.8                    | Zynq DDR Bank 502                             |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VTT_0P75               |              | U14              | 2.0                    | DDR termination/reference                     |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VTTVREF                | 1/2 VCC-1P35 | U14              | 2.0                    | DDR termination/reference                     |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VCCPCOM-1P8V           | 1.8          | U18              | 4.0                    | Zynq PL Bank 35, Vccaux Zynq PS Bank 500/501  |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VCCO_1P8V              | 1.8          | U18              | 4.0                    | Zynq PL Bank 35, Vccaux Zynq PS Bank 500/501, |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDD_INTERFACE          | 1.8          | U18              | 4.0                    | AD9361 Data Interface to Zynq                 |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_GPO               | 2.5          | U6               | 0.3                    | AD9361 General Purpose Outputs                |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_GPO_PWR           | 2.5          | U6               | 0.3                    | AD9361 General Purpose Outputs                |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VCC-3P3V               | 3.3          | U9               | 0.5                    | Zynq Bank 0, USB, SDIO                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VCC-3P3V - IO          | 3.3          | U9               | 0.5                    | Zynq Bank 0, USB, SDIO                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| PHY1_VDD_3V3           | 3.3          | U9               | 0.5                    | Ethernet PHYs                                 |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| PHY2_VDD_3V3           | 3.3          | U9               | 0.5                    | Ethernet PHYs                                 |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| 1P3_SUPPLY_A           | 1.3          | U19              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_TX_LO             | 1.3          | U19              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_RX_LO             | 1.3          | U19              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_TX_SYNTH          | 1.3          | U19              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_RX_SYNTH          | 1.3          | U19              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| 1P3_SUPPLY_B           | 1.3          | U20              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_BB                | 1.3          | U20              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_DIG               | 1.3          | U20              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| VDDA_RX_TX             | 1.3          | U20              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| 1P3_TX1A               | 1.3          | U20              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| 1P3_TX2A               | 1.3          | U20              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| 1P3_TX1B               | 1.3          | U20              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+
| 1P3_TX2B               | 1.3          | U20              | 1.2                    | AD9361 Analog Supplies                        |
+------------------------+--------------+------------------+------------------------+-----------------------------------------------+

Updating the ADM1166 Sequencer Firmware
=======================================

Your system requirements may call for alternate timing, sequencing, and/or monitoring of the SOM power supplies. The :adi:`ADM1166 <en/products/power-management/sequencing/digital-sequencers/adm1166.html>` Super Sequencer firmware may be updated to accommodate these changes. Be advised that a number factors must be considered, including:

-  Resistor dividers (and their tolerances) at ADM1166 inputs
-  ADM1166 programmable input ranges
-  ADM1166 input impedance (voltage dependent)

An in depth analysis for `calculating ADM1166 thresholds <https://wiki.analog.com/resources/eval/user-guides/pzsdr/power-and-sequencing>`_ is found here.

Designers are strongly encouraged to start with the latest ADM166.txt file (on `Github <https://github.com/analogdevicesinc/PicoZed-SDR>`_) and make changes using the Analog Devices Super `Sequencer Configuration Tool <https://github.com/analogdevicesinc/PicoZed-SDR>`_. Consult the `Xilinx Zynq datasheet <https://www.xilinx.com/support/documentation/data_sheets/ds191-XC7Z030-XC7Z045-data-sheet.pdf>`_ before making any changes.

Important! Consult the Zynq AP SoC and AD9361 datasheets before updating
threshold windows for SOM voltage rails. Sequencing changes are strongly
discouraged.

Download the latest ADM1166 firmware repository from the GitHub link below. It’s
important to either clone or download the zip archive.

::

   `PicoZed-SDR <https://github.com/analogdevicesinc/PicoZed-SDR>`_.

Once you have made updates to the ADM1166 firmware file using the configuration
tool, there are two methods for programming the device.

-  Program the ADM1166 using the Zynq SoC to execute a Linux command line script (See the automated and manual update descriptions starting in section 7.2.1)
-  Purchase a :adi:`USB-SDP-CABLEZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval_usb-sdp-cablez.html>` Serial I/O Interface cable to program the SOM directly.

Automated Update Procedure
--------------------------

A simple Linux script executed on Zynq will download the latest ADM1166 firmware
and program the ADRV9361.

You will need a networked router with DHCP capability. Follow the instructions at `power-and-sequencing <https://wiki.analog.com/resources/eval/user-guides/pzsdr/power-and-sequencing>`_. Look for the section “Programming the ADM1166 Power Sequencer – Using Linux or HyperTerminal Program”.

This method clones the Analog Devices GIT repository to obtain the latest version of the HEX file for the ADM1166. Note that you need to login as root or use the ‘sudo’ command to execute the update. The GitHub repository for these files is at the following `github <https://github.com/analogdevicesinc/PicoZed-SDR>`_.

Alternatively, you may use the Manual Update Procedure.

Manual Update Procedure
-----------------------

This is an optional “manual” method to update the ADM1166 firmware, provided if
you are unable to connect your development kit to a DHCP networked router.

This method can also be used to program your own custom ADM1166 firmware,
however consider whether your custom thresholds will be compatible with the
carrier you are using during this process. Upon completion the board may
shutdown. The only way to recover from this situation is to use the USB adapter
to program the SOM standalone.

Standalone Programming with USB Adapter
---------------------------------------

The ADM1166 Super Sequencer non-volatile memory can be programmed by connecting
an Analog Devices USB-SDP-CABLEZ I2C/SMBus programmer to the SOM 5-pin P1
connector. Supplying 5.0V to VBUS pin P1-1 allows the device to be powered and
programmed without mating the SOM to a carrier. Software support for the
programmer can be found on the ADM1166 product page.

|USB-SDP-CABLEZ| USB-SDP-CABLEZ

Important! Damage may occur to the SOM if the ADM1166 sequencing state machine
is reprogrammed without regard for the required sequencing of the system.
Consult the Zynq-7000 SoC and Analog Devices AD9361 datasheets before modifying
the sequencing scheme.

.. image:: ../images/programming_header.png
   :align: center
   :width: 400

ADM1166 Programming Port (P1)

Instructions for programming: `power-and-sequencing <https://wiki.analog.com/resources/eval/user-guides/pzsdr/power-and-sequencing>`_ Look for the section titled “Using the USB-SDP-CABLEZ Serial I/O Interface”.

USB Power
=========

The ADRV9361 2X2 SOM cannot supply USB power. The USB PHY (U15) on the SOM
includes a CPEN signal which is brought to a micro header pin for use as an
enable for a USB t5V power supply on the carrier card. 7.4 XADC Power
Configuration The Zynq SoC’s XADC component is powered from the filtered 1.8V
VCCaux supply (VCCPCOM-1P8V) utilizing the on-chip reference as shown below:

|image1| XADC Power Configuration

Restoring the Analog Devices SD Card Image
------------------------------------------

During the course of development with the Analog Devices Linux reference design,
should your 8 GB SD card become corrupted or otherwise need to be updated, the
directions below will restore the system to the latest version. Instructions are
provided for both Linux and Windows hosts.

-  If you wish to completely overwrite the SD card, you may download the latest image `kuiper-linux <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

.. important::

   Important!

These steps will overwrite the contents of the SD card, so be certain there is
no existing data that needs to be retrieved from the SD card prior to following
these steps.

.. image:: ../images/requirements.png
   :align: center
   :width: 400

Otherwise, you may simply run the update scripts at the command line: `kuiper-linux <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

As a final step, make sure to copy the contents of the ‘zynq-picozed-sdr2’
folder to the BOOT partition of the SD card. PicoZed SDR is now fully updated
and ready to re-boot.

Board Revisions
===============

Rev A Description
-----------------

Internal only. None released. Identification – REV A printed in copper.

Rev B Description
-----------------

First hardware shipped to customers. Identification – Sticker printed with RFSOM REV B located on the bottom side just above the copper etch AES-PZSDR-Z7035-AD9361-G.

Rev C Description
-----------------

Small updates. Functionally is equivalent to Rev B (see list of changes below). Identification – Initial builds used a sticker printed with an Sxx-xxxx designator and an enumerated SN:xxxxxxx serial number, but no revision printed. Subsequent builds add a REVC revision text to the label.

Changes from Rev B to Rev C

-  Replaced on the schematic the Y1 crystal with equivalent part and added a pull-up and pull-down.
-  Replaced the 2 pin Ethernet Phy crystal (Y2) with a 4 pin.
-  Improved PCB layout of address lines between the FPGA and two DDR3 memory chips.
-  Replaced the six pin BGA (U23) ADP7112-3.3 with ADP7118 sot-23.
-  Pull up/down resistors (R26, R37) are now DNP.
-  50 ohm series (R60) is now 0ohm.

Rev D Description
-----------------

Moved GTX ports from Bank 111 to Bank 112 on the Zynq SoC, and modified the control for PG_MODULE. Otherwise, functionally is equivalent to Rev B and Rev C (see list of changes below). Identification – Sticker printed with an Sxx-xxxx designator, an enumerated SN:xxxxxxx serial number, board part number, and revision REVD.

Changes from Rev C to Rev D

-  Moved all (4) GTX ports from Bank 111 to Bank 112 on the Zynq SoC in order to be in compliance with Xilinx recommended PCIe design rules. The GTX signal assignments at the JX micro headers were unchanged in order to maintain compatibility with existing carrier boards.
-   Added revision and part number to the silkscreen and copper.
-  The LED (D3), used to illuminate when PG_MODULE is asserted, now has its
   anode connected to the 3V3_I2C supply (formerly connected to 3.3V supply).
   This was done to allow the LED to be used as a visual state indicator during
   SOM power up, reflecting different states of the ADM1166 sequencer. In
   addition, the ADM1166 firmware was updated to include LED toggling
   (slow/fast), corresponding to specific power up states.

DDR3L Trace Length
==================

The Xilinx Vivado tools allow entry of the DDR3L trace lengths in order to
optimize timing and performance of the PS-based memory controller. The trace
lengths for PicoZed SDR 2X2 are listed below. These are also found in the
reference design TCL build scripts available on the Analog Devices GitHub
repository.

|image2|

DDR3L Trace Lengths

.. |USB-SDP-CABLEZ| image:: ../images/usb-sdp-cablez-b.png
   :width: 400
.. |image1| image:: ../images/xadc_power_configuration.png
   :width: 400
.. |image2| image:: ../images/trace_lenghts.png
   :width: 400
