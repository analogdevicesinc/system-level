.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad2s1210_sdz

.. _ad2s1210_sdz:

EVAL-AD2S1210SDZ Evaluation Board on ZedBoard User Guide
========================================================

**Evaluation Board for the AD2S1210 Variable Resolution, 10-Bit to 16-Bit R/D
Converter with Reference Oscillator**

ADD PIC

Features
--------

- Complete monolithic resolver-to-digital converter
- Is supported on
  `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__

Hardware Required
-----------------

- 16GB (or larger) Class 10 (or faster) micro-SD card
-
  `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__
  Rev D or later board
- :dokuwiki:`SDP to FMC Interposer </resources/eval/sdp/sdp-fmc>`
- 12Vdc, 3A power supply
- Micro-USB cable
- Ethernet cable
- User interface setup (choose one):
- HDMI monitor, keyboard, and mouse plugged directly into the Zedboard
- Host Windows/Linux/Mac computer on the same network as the Zedboard

Software Required
-----------------

- You need a Host PC (Windows or Linux)
- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
- IIO Scope Download
- :ref:`kuiper`

General Description
-------------------

The EVAL-AD2S1210SDZ is a full featured evaluation board designed to allow the
user to easily evaluate all the features of the AD2S1210 resolver-to-digital
converter (RDC).

Quick Start Guide
-----------------

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

To boot the Zedboard and control the :adi:`EVAL-AD2S1210SDZ`, you will need to
install ADI Kuiper Linux on an SD card. Complete instructions, including where
to download the SD card image, how to write it to the SD card, and how to
configure the system are provided on the :ref:`kuiper`.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~

Follow the configuration procedure under **Configuring the SD Card for FPGA
Projects** on the :ref:`kuiper` page. Copy the following files onto the boot
directory to configure the SD card:

- uImage file for Zynq
- BOOT.BIN specific to your :adi:`EVAL-AD2S1210SDZ` + ZedBoard
- devicetree.dtb for Zynq specific to your :adi:`EVAL-AD2S1210SDZ` + ZedBoard

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

You will need to:

- Get the
  `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__.

  .. figure:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/AD777x-ARDZ/zedboard.png
     :width: 600px

- Insert the SD-CARD into the SD Card Interface Connector (J12).
- Connect the :adi:`EVAL-AD2S1210SDZ` board to the SDP adaptor and into the
  ZedBoard FMC connector.
- Connect USB UART J14 (Micro USB) to your host PC.
- Plug your ethernet cable into the RJ45 ethernet connector(J11).
- Plug the Power Supply into the 12V Power input connector (J20) (DO NOT turn
  the device on).

- Set the jumpers as seen in the below picture:

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/jumpers_boot_sd_zedboard.jpg
    :width: 400px

::

   .. tip::

 Before executing the below steps, make sure that VADJ jumper is set to 3.3V.
 * Connect the oscilloscope probes to the SMB connectors.
 * Turn it on.
 * Wait ~30 seconds for the ``DONE`` LED to turn blue. This is near the DISP1.

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

Application Software (both locally and remotely on the FPGA)
------------------------------------------------------------

Hardware Connection
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - FPGA
     -
     - SDP ADAPTER
     -
     -
     - EVAL-AD2S1210SDZ
   * - Connected to
     - FMC NAME
     - FMC PIN
     - SCH SIG NAME
     - SDP(J2) PIN
     - SCH NAME
   * - PS SPI 0 SDI
     - FMC_LPC_LA01_CC_P
     - D08
     - CON_PAR_DATA[15]
     - 110
     - SDO
   * - PS SPI 0 SDO
     - FMC_LPC_CLK0_M2C_P
     - H04
     - CON_PAR_DATA[14]
     - 12
     - SDI
   * - PS SPI 0 CLK
     - FMC_LPC_CLK0_M2C_N
     - H05
     - CON_PAR_DATA[13]
     - 13
     - SCLK
   * - Logic low
     - FMC_LPC_LA04_N
     - H11
     - CON_PAR_CS
     - 22
     - PAR_CS_n
   * - PS SPI 0 CSn 0
     - FMC_LPC_LA09_N
     - D15
     - CON_PAR_WR
     - 100
     - PAR_WR_n
   * - PS EMIO 32 (Linux 86)
     - FMC_LPC_LA13_N
     - D18
     - CON_PAR_ADDR[0]
     - 96
     - PAR_A0
   * - PS EMIO 33 (Linux 87)
     - FMC_LPC_LA07_P
     - H13
     - CON_PAR_ADDR[1]
     - 25
     - PAR_A1
   * - PS EMIO 34 (Linux 88)
     - FMC_LPC_LA21_P
     - H25
     - CON_GPIO[0]
     - 43
     - SDP_RES_0
   * - PS EMIO 35 (Linux 89)
     - FMC_LPC_LA26_P
     - D26
     - CON_GPIO[1]
     - 78
     - SDP_RES_1
   * - PS EMIO 36 (Linux 90)
     - FMC_LPC_LA27_P
     - C26
     - CON_GPIO[3]
     - 77
     - TMR_A (SAMPLE)

SPI connections

.. list-table::
   :header-rows: 1

   * - SPI manager instance
     - Alias
     - SPI address
     - SPI subordinate
     - CSn
   * - psu spi 0
     - spi_fpga
     - 0xFF040000
     - AD2S1210
     - 0

GPIO signals(schematic)
^^^^^^^^^^^^^^^^^^^^^^^

Ps8 EMIO offset = 54

.. list-table::
   :header-rows: 1

   * - GPIO Signal
     - GPIO
     - HDL GPIO EMIOn
   * - TMR_A (SAMPLE)
     - 90
     - 36
   * - SDP_RES_1
     - 89
     - 35
   * - SDP_RES_0
     - 88
     - 34
   * - A1
     - 87
     - 33
   * - A0
     - 86
     - 32

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO-Oscilloscope found
   on this link\ :git-iio-oscilloscope:`releases\+`

- Once done with the installation or an update of the latest IIO-Oscilloscope,
  open the application. The user needs to supply a URI which will be used in the
  context creation of the IIO Oscilloscope and the instructions can be seen in
  the previous section.

- Press refresh to display available IIO Devices and press connect.

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/dac/ad3552r_eval_zed/iio_connect.png
    :width: 700px
