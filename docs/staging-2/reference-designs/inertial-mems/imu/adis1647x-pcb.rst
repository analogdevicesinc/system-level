.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/imu/adis1647x-pcb

.. _inertial-mems imu adis1647x-pcb:

ADIS1647x/PCBZ BREAKOUT BOARD WIKI GUIDE
========================================

OVERVIEW
========

There are seven (7) breakout boards that support ADIS1647x IMU products. These
breakout boards that provide a simple way to develop a prototype connection
between the ADIS1647x IMUs and an existing embedded processor platform. This
breakout board already contains the ADIS1647x IMU and one 16-pin header, which
mates to 2 mm ribbon cables. As a general guideline, these breakout boards will
support reliable communications over ribbon cables that are up to 20 cm in
length, but it is always a good idea to validate signal integrity before relying
on this type of connection to support a critical communication link.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16470pcbzangle_jpg.jpg
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16470pcbztop_jpg.jpg
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16470pcbzbottom_jpg.jpg
   :width: 400px

ORDERING GUIDE/MODEL NUMBER SUMMARY
===================================

Please see the follow table for a list of available breakout boards, along with
the IMU model number that is on each board.

.. list-table::
   :header-rows: 1

   * - MODEL NUMBERS
     -
     - MEASUREMENT RANGE
     -
     -
   * - BREAKOUT BOARD
     - IMU
     - GYROSCOPE
     - ACCELEROMETER
     -
   * - :adi:`ADIS16470/PCBZ <en/products/adis16470.html#product-samplebuy>`
     - ADIS16470AMLZ
     - +/-2000 dps
     - +/-40g
     -
   * - :adi:`ADIS16475-1/PCBZ <en/products/adis16475.html#product-samplebuy>`
     - ADIS16475-1BMLZ
     - +/-125 dps
     - +/-8g
     -
   * - :adi:`ADIS16475-2/PCBZ <en/products/adis16475.html#product-samplebuy>`
     - ADIS16475-2BMLZ
     - +/-500 dps
     - +/-8g
     -
   * - :adi:`ADIS16475-3/PCBZ <en/products/adis16475.html#product-samplebuy>`
     - ADIS16475-3BMLZ
     - +/-2000 dps
     - +/-8g
     -
   * - :adi:`ADIS16477-1/PCBZ <en/products/adis16477.html#product-samplebuy>`
     - ADIS16477-1BMLZ
     - +/-125 dps
     - +/-40g
     -
   * - :adi:`ADIS16477-2/PCBZ <en/products/adis16477.html#product-samplebuy>`
     - ADIS16477-2BMLZ
     - +/-500 dps
     - +/-40g
     -
   * - :adi:`ADIS16477-3/PCBZ <en/products/adis16477.html#product-samplebuy>`
     - ADIS16477-3BMLZ
     - +/-2000 dps
     - +/-40g
     -

EVAL-ADIS2 CONNECTION
=====================

The J1 connector on each ADIS1647x breakout board is pin-for-pin compatible with
the same connector (J1) on the :adi:`EVAL-ADIS2` evaluation system.

**UNDER CONSTRUCTION**

DIMENSTIONS/MOUNTING HOLES
==========================

These breakout boards, provide four mounting holes, one in each corner, which
support attachment to another surface with M2 machine screws. Please see the
following diagram for more details:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1647x/15343-313_pk.png
   :width: 600px

INTERFACE CONNECTOR
===================

Please see the following table for the pin assignments for the interface
connector (J1)

.. list-table::
   :header-rows: 1

   * - PIN
     - NAME
     - DESCRIPTION
   * - 1
     - ~RST
     - Reset, Active Low
   * - 2
     - SCLK
     - Serial Clock (Serial Peripheral Interface)
   * - 3
     - ~CS
     - Chip Select (Serial Peripheral Interface), Active Low
   * - 4
     - DOUT
     - Data Output (Serial Peripheral Interface)
   * - 5
     - DNC
     - Do not connect
   * - 6
     - DIN
     - Data Input (Serial Peripheral Interface)
   * - 7
     - GND
     - Ground
   * - 8
     - GND
     - Ground
   * - 9
     - GND
     - Ground
   * - 10
     - VDD
     - Power Supply, +3.3V
   * - 11
     - VDD
     - Power Supply, +3.3V
   * - 12
     - VDD
     - Power Supply, +3.3V
   * - 13
     - DR
     - Data Ready
   * - 14
     - SYNC
     - Sync Input
   * - 15
     - DNC
     - Do not connect
   * - 16
     - DNC
     - Do not connect

CABLING
=======

J1 supports connection with the following style of cables: 2.00 mm IDC Ribbon
Cable Assembly

TIP: Use ``2.00 mm IDC Ribbon Cable Assembly`` as search criteria to find the
latest options on the market.

At the time of initial release for these breakout boards, we were most familiar
with the `TCSD Series from Samtec <https://www.samtec.com/products/tcsd>`__.

ELECTRICAL SCHEMATIC
====================

The following diagram illustrates the electrical schematic for the
ADIS16470/PCBZ. Please note that the only difference in the other models will be
in the IMU (ADIS16470AMLZ listed in the following view). Click on this image to
access a higher-resolution view.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/47x_pcb_wikiguide_sch.jpg
   :width: 600px

REFERENCE DESIGNS & CODE EXAMPLES
=================================

For those who are ready to evaluate the ADIS1647x, this section provides a list
of reference designs. These references designs include one or both of the
following:

- Physical connection, between the ADIS1647x-x/PCB and a specific embedded
  processor platform/system

- Embedded code, which lists all ADIS1647x user registers, manages the
  ADIS1647x"s SPI protocol requirements and provides examples for reading from
  (and writing to) the user registers, within the ADIS1647x"s memory map.

`ADIS1647x with Teensy 3.2 (Arduino) <https://github.com/juchong/ADIS16470_Arduino_Teensy>`__
