.. imported from: https://wiki.analog.com/resources/eval/user-guides/ev-cog-bleintp1z

.. _ev-cog-bleintp1z:

EV-COG-BLEINTP1Z Connectivity Cog
=================================

Introduction
------------

EV-COG-BLEINTP1Z board is a connectivity Cog board for MCU Cogs (EV-COG-AD3029LZ
and EV-COG-AD4050LZ). This board enables wireless RF transceiver connectivity,
Bluetooth Low Energy connectivity and WIFI connectivity for various IoT
applications.

- The following ADI wireless RF daughter boards are supported via SPI interface
- :adi:`ADF7023 <en/products/rf-microwave/integrated-transceivers-transmitters-receivers/low-power-rf-transceivers/adf7023.html>`
- :adi:`ADF7024 <en/products/rf-microwave/integrated-transceivers-transmitters-receivers/low-power-rf-transceivers/adf7024.html>`
- :adi:`ADF7030-1 <en/products/rf-microwave/integrated-transceivers-transmitters-receivers/low-power-rf-transceivers/adf7030-1.html>`
- :adi:`ADF7242 <en/products/rf-microwave/integrated-transceivers-transmitters-receivers/low-power-rf-transceivers/adf7242.html>`
- BTLE - available on board and can be communicated via SPI interface
- WIFI - provision to support
  `ESP8266 <http://espressif.com/en/products/hardware/esp8266ex/overview>`__ via
  UART (not available in the kit)

This user guide describes the connector pin out, power options and jumper
settings available on board.

Hardware details
================

Board image
-----------

Primary-side
~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/picture1.png
   :width: 590px

Secondary-side
~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/picture2.png
   :width: 610px

The board consists of

- 32 pin Hirose connector (P1)
- Power header (P5)
- Wireless RF transceiver connector (P2, P3, P4)
- Bluetooth Low Energy Chipset
- WIFI module connector (P9)
- Debug header/test points

Power options
=============

The EV-COG-BLEINTP1Z board is powered up by means of the VDD supply from the MCU
cog through the 32 pin connector (P1). The VDD supply is shared between RF
transceiver, BLE and WIFI via jumper P5. Shunts must be placed in appropriate
positions as shown in the following figure to power up different blocks.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/picture4.png
   :width: 250px

.. tip::

   P5 can also be used for measuring current flowing through different rails by
   connecting an ammeter between VDD and VDD_RF/VDD_BLE/VDD_WIFI.

32 pin Hirose connector
-----------------------

The Hirose connector P1 interfaces the EV-COG-BLEINTP1Z board with the MCU Cog.
The connector carries VDD, UART, SPI2 and GPIO signals from MCU cog board. The
pinout details are given in the following table

.. list-table::
   :header-rows: 1

   * - Hirose connector (P1) pin number
     - pin name
     - MCU Cog signal name
   * - 1
     - VDD
     - VDD_RF
   * - 2
     - VDD
     - VDD_RF
   * - 3
     - GND
     - GND
   * - 4
     - GND
     - GND
   * - 5
     - WIFI_TX
     - MCU/UART0_RX
   * - 6
     - RF_INT
     - RF_INT
   * - 7
     - WIFI_RX
     - MCU/UART0_TX
   * - 8
     - SPI2_CS3_RF
     - MCU/SPI2_CS3
   * - 9
     - GND
     - GND
   * - 10
     - SPI2_MISO
     - MCU/SPI2_MISO
   * - 11
     - ADF7030_EEPROM_CSN
     - RF_SYS_WAKE
   * - 12
     - SPI2_MOSI
     - MCU/SPI2_MOSI
   * - 13
     - ADF7030_EEPROM_VDD
     - MCU/GPIO08
   * - 14
     - SPI2_CLK
     - MCU/SPI2_CLK
   * - 15
     - GND
     - P.D [GND, 100K]
   * - 16
     - GND
     - GND
   * - 17
     - N.C.
     - P.U [VDD_RF, 100K]
   * - 18
     - SPI2_RDY
     - SPI2_RDY
   * - 19
     - N.C.
     - N.C
   * - 20
     - RF_SS
     - SS_TO_RF
   * - 21
     - BLE_CHIP_ENABLE
     - GPIO27
   * - 22
     - RF_RESET
     - GPIO_RF_RESET
   * - 23
     - RF_GPIO0
     - C2/54
   * - 24
     - RF_GPIO1
     - C2/55
   * - 25
     - RF_GPIO5
     - C2/58
   * - 26
     - N.C.
     - RF_SYS_WAKE
   * - 27
     - RF_GPIO4
     - C2/59
   * - 28
     - SPI2_CS0_BLE
     - SPI2_CS0
   * - 29
     - GND
     - GND
   * - 30
     - GND
     - GND
   * - 31
     - VDD
     - VDD_RF
   * - 32
     - VDD
     - VDD_RF

Wireless RF transceiver connectors
----------------------------------

The wireless RF transceiver connectors consist of three connectors P1, P2 and
P3, which support ADF7023, ADF7024, ADF7030, ADF7030-1 and ADF7242 RF
transceiver daughter boards. Pinout details are given in the following table.

.. list-table::
   :header-rows: 1

   * - Connector
     - Pin number
     - Signal name
     - ADF7023 signal name
     - ADF7024 signal name
     - ADF7242 signal name
     - ADF7030-1 signal name
   * - P2
     - 1
     - N.C
     - GND
     - NC
     - DGUARD (VDD_DIG)
     - NC
   * -
     - 2
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 3
     - XOSC26N
     - Xosc26N
     - Xosc26N
     - Xosc26N
     - Xosc26N
   * -
     - 4
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 5
     - N.C
     - NC
     - NC
     - NC
     - NC
   * -
     - 6
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 7
     - VDD_RF
     - VDD
     - VDD
     - NC
     - NC
   * -
     - 8
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 9
     - VDD_RF
     - VDD
     - VDD
     - NC
     - NC
   * -
     - 10
     - GND
     - GND
     - GND
     - GND
     - GND
   * - P3
     - 1
     - ATB1/GPIO6
     - ATB1/OSC32P/GP5
     - ATB1/GP5
     - GP7/XOSC32K
     - GPIO6
   * -
     - 2
     - ATB2/GPIO7
     - ATB2/OSC32N
     - ATB2
     - ATB2/XOSC32K
     - GPIO7
   * -
     - 3
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 4
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 5
     - VDD_RF
     - VDD
     - NC
     - VDD
     - VDD
   * -
     - 6
     - VDD_RF
     - VDD
     - NC
     - VDD
     - VDD
   * -
     - 7
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 8
     - ATB3
     - ATB3
     - ATB3
     - ATB3
     - NC
   * -
     - 9
     - VREF
     - ADCVREF
     - NC
     - NC
     - NC
   * -
     - 10
     - ATB4
     - ATB4
     - ATB4
     - ATB4
     - NC
   * - P4
     - 1
     - RF_RESET
     - NC
     - NC
     - RXEN_GP6
     - RSTN
   * -
     - 2
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 3
     - RF_GPIO4
     - GP4
     - GP4
     - TXEN_GP5
     - GPIO3
   * -
     - 4
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 5
     - SPI2_CS3_RF
     - CSN
     - CSN
     - CSN
     - CSN
   * -
     - 6
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 7
     - SPI2_MOSI
     - MOSI
     - MOSI
     - MOSI
     - MOSI
   * -
     - 8
     - ADF7030-1_EEPROM_CSN
     - NC
     - GND
     - NC
     - EEPROM_CSN
   * -
     - 9
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 10
     - ADF7030-1_EEPROM_VDD
     - NC
     - NC
     - NC
     - EEPROM_VDD
   * -
     - 11
     - SPI2_CLK
     - SCLK
     - SCLK
     - SCLK
     - SCLK
   * -
     - 12
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 13
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 14
     - GND
     - GND
     - GND
     - GND
     - GND
   * -
     - 15
     - SPI2_MISO
     - MISO
     - MISO
     - MISO
     - MISO
   * -
     - 16
     - RF_GPIO0
     - GP0
     - GP0
     - DR_GP0
     - GPIO1
   * -
     - 17
     - RF_INT
     - IRQ_GP3
     - IRQ_GP3
     - IRQ_GP4
     - GPIO4
   * -
     - 18
     - RF_GPIO1
     - GP1
     - GP1
     - DT_GP1
     - GPIO0
   * -
     - 19
     - RF_SS
     - GP2
     - GP2
     - TRCLK_CKO_GP3
     - GPIO2
   * -
     - 20
     - RF_GPIO5
     - NC
     - NC
     - TRFS_GP2
     - GPIO5

The following figure shows EV-COG-BLEINTP1Z connected to ADF7023DBExZ daughter
board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/picture5.png
   :width: 300px

.. note::

   Install the jumper between VDD_BLE and VDD in addition to VDD_RF

Bluetooth Low Energy Chipset
----------------------------

The EV-COG-BLEINTP1Z has a Bluetooth low energy chipset EM9304 from EM
Microlectronic. The chipset contains BLE protocol stack along with some
profiles. The MCU cog communicates to EM9304 by means of SPI2. The user will
need to send BLE configuration commands and data over SPI. The following table
captures the signals connected to EM9304

.. list-table::
   :header-rows: 1

   * - Component
     - EM9304 pin number
     - EM9304 pin name
     - MCU cog signal
   * - U1
     - 4
     - ENABLE
     - GPIO27
   * -
     - 15
     - GPIO0
     - SPI2_CS0
   * -
     - 16
     - GPIO1
     - SPI2_CLK
   * -
     - 17
     - GPIO2
     - SPI2_MISO
   * -
     - 18
     - GPIO3
     - SPI2_MOSI
   * -
     - 20
     - GPIO4
     - SPI2_RDY

.. important::

   The Jumpers P6 and P7 are provided to isolate SPI_CS and SPI_CLK lines
   connected to BLE while working with RF transceiver daughter cards. But shunts
   must be placed on these jumpers for BLE to work.

WIFI module connector
---------------------

The connector P9 supports the WIFI module ESP8266. The ESP8266 WiFi Module is a
self contained SOC with integrated TCP/IP protocol stack. The module
communicates to MCU cog via UART TX and UART RX lines. Each ESP8266 module comes
pre-programmed with an AT command set firmware which allows easy programing over
UART. For more information & support concerning the WiFi module please follow
the links below:

- `Product Page/Details <https://www.sparkfun.com/products/13678>`__
- `AT Command List <https://cdn.sparkfun.com/datasheets/Wireless/WiFi/Command%20Doc.pdf>`__
- `Hardware/Software Details <https://nurdspace.nl/ESP8266>`__
- `Github Details <https://github.com/esp8266/esp8266-wiki/wiki/Hardware_versions>`__

The following figure shows the orientation of the module.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/picture3.png
   :width: 500px

Pinout details of the module connector are given below.

.. list-table::
   :header-rows: 1

   * - Component
     - module pin number
     - Module pin function
     - cog signal
   * - P9
     - 1
     - DGND
     - GND
   * -
     - 2
     - WIFI TX
     - MCU/UART0_RX
   * -
     - 3
     - GPIO0
     - WIFI_GPIO0
   * -
     - 4
     - Chip enable
     - VDD_WIFI
   * -
     - 5
     - GPIO2
     - WIFI_GPIO2
   * -
     - 6
     - WIFI Reset
     - WIFI_RESET
   * -
     - 7
     - WIFI RX
     - MCU/UART0_TX
   * -
     - 8
     - DVDD
     - VDD_WIFI

.. note::

   This WiFi module is NOT developed by Analog Devices and it will not be
   shipped along with this board.

Debug header
------------

Test points are provided to probe some specify signals w.r.t RF transceiver
daughter cards, BLE and WIFI module. The pinout details are given in the
following table.

.. list-table::
   :header-rows: 1

   * - Test point/Debug header
     - pin number
     - Cog signal
   * - TP1
     - 1
     - SPI2_CS3_RF
   * - TP2
     - 1
     - SPI2_CS0_BLE
   * - TP3
     - 1
     - ADF7030-1_EEPROM_CSN
   * - TP4
     - 1
     - ADF7030-1_EEPROM_VDD
   * - TP5
     - 1
     - BLE_CHIP_ENABLE
   * - P8
     - 1
     - WIFI_GPIO0
   * -
     - 2
     - WIFI_GPIO2
   * - P10
     - 1
     - XOSC26N
   * -
     - 2
     - ATB1/GPIO6
   * -
     - 3
     - ATB2/GPIO7
   * -
     - 4
     - ATB3
   * -
     - 5
     - ATB4
   * -
     - 6
     - VREF
   * -
     - 7
     - RF_GPIO0
   * -
     - 8
     - RF_GPIO1
   * -
     - 9
     - RF_GPIO4
   * -
     - 10
     - RF_GPIO5
   * -
     - 11
     - RF_SS
   * -
     - 12
     - GND

Schematics, PCB layout, Bill of materials
-----------------------------------------

.. admonition:: Download

   EV-COG-BLEINTP1Z Rev A Design and Integration Files

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/02-046704-01-a-1_2_.pdf`
   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/05-046704-01-a.zip`
   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/09-046704-01a.zip`
   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad3029lz/09-046704-01a.zip`

:dokuwiki:`Back </resources/eval/user-guides/ev-cog-ad3029lz>`
