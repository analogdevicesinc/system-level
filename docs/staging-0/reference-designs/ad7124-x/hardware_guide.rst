.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad7124-x/hardware_guide

.. _ad7124-x hardware_guide:

Hardware Guide
==============

This section of the user guide will go through the hardware on the
Eval-AD7124-xASDZ board and will provide an explanation of the AD7124 itself,
the hardware link options available on the board, how to power the part etc.,
with Schematics and a Bill of Materials available at the end of the chapter.

Set-up Procedures
-----------------

After following the instructions in the Software Installation Procedures section, set up the evaluation and SDP boards as detailed in this section. .. note::

   The evaluation software and drivers must be installed before connecting the EVAL-AD7124-xASDZ evaluation board and EVAL-SDP-CB1Z board to the USB port of the PC to ensure the PC correctly recognizes the evaluation system.

Follow the below 2 steps to configure the Evaluation and SDP Boards:

#. Connect the SDP-B board to Connector A or Connector B on the
   EVAL-AD7124-xASDZ evaluation board. Screw the two boards together using the
   plastic screw and washer set included in the evaluation board kit to connect
   the boards firmly together.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/quick_start.jpg
      :width: 600px

#.  Connect the SDP-B board to the PC using the supplied USB cable.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/img_0569_rot.jpeg
      :width: 300px

Block Diagram
-------------

Hardware Link Options
---------------------

.. list-table::
   :header-rows: 1

   * - Link Number
     - Default Position
     - Description
   * - LK1
     - Inserted
     - This link shorts AIN0 to AIN1. This is useful to perform noise tests on
       the AD7124-X. The internal bias can be enabled on AIN0 or AIN1 so that
       AIN0 and AIN1 are at an appropriate voltage for the noise test.
   * - LK2
     - Inserted
     - This link bypasses the Cold Junction R28. When inserted, it allows AIN4
       and AIN5 to be used as regular analog input pins. This link should be
       removed for the thermocouple demo.
   * - LK3
     - A
     - Used for selecting either J1 or J2 as the external REFIN+. Position A
       sets it to J2. Position B sets it to J1.
   * - LK4
     - Inserted
     - Used to connect REFIN- to AVSS
   * - LK5
     - A
     - Used for selecting either J1 or J2 as the external REFIN-. Position A
       sets it to J2. Position B sets it to J1.
   * - LK6
     - A
     - This link sets the source for REFIN+. Position A sets it to 2.5V from on
       board LDO. Position B sets it to the REFOUT bin of the AD7124. When
       removed, REFIN+ comes from either J1 or J2 depending on the position of
       LK3.
   * - LK7
     - Inserted
     - Used for 4 wire bridge demos. Ties GND to REFIN-.
   * - LK8
     - Inserted
     - Used for 4 wire bridge demos. Ties REFIN- to PSW.
   * - LK9
     - Inserted
     - Used for 4 wire bridge demos. Ties REFIN+ to AVDD
   * - LK10
     - Inserted
     - This link allows the user to use an external excitation source for bridge
       demos
   * - LK11 - 14
     - Uninserted
     - When these links are inserted, T_AVDD and T_IOVDD are in Position B and
       R96 and R97 are stuffed the AD4130 can measure its own current
       consumption.
   * - LK15
     - A
     - This link sets the value of AVDD. When in position A, AVDD is set by the
       onboard LDOs. When in position B, it is set to the external AVDD source.
   * - LK16
     - A
     - This link sets the value of AVSS. When in position A, AVSS is set to
       -1.8V via onboard LDO. When in position B, it is set to the external AVSS
       source. (LK31-33 must be removed for both positions)
   * - LK17
     - B
     - When in Position A, AVSS is connected to -1.8V (LK 31-33 need to be
       disconnected). When in Position B, AVSS is connected to AGND
   * - LK18
     - A
     - This link sets the value of coming out of the LDO supplying AVDD (if LK15
       is in position A). In position A, AVDD == 3.3V. In position B, AVDD ==
       1.8V.
   * - LK19
     - B
     - When in Position A, an external IOVDD can be supplied to power the part.
       When in Position B, IOVDD is connected to an LDO supply
   * - LK27-30
     - A
     - With this link in Position A, Arduino communication comes through the
       standard connector (P4). With this link in Position B, Arduino
       communication comes through the alternative connector (P3).
   * - LK31-33
     - Inserted
     - Ties AVSS and DGND together.
   * - T_AVDD, T_IOVDD
     - A
     - When these links are in Position A, AVDD and IOVDD are connect directly
       to the supply rails. When these links are in Position B and R96 and R97
       are stuffed, the AD4130 can measure its own current consumption when LK8
       to LK11 are inserted

On Board Connections
====================

Connector A2: Thermocouple Connection
-------------------------------------

Connector J1: RTD Connection
----------------------------

.. list-table::
   :header-rows: 1

   * - Connector
     - Function
   * - 1
     - AIN0, Excitation Current IOUT0, Nosie test
   * - 2
     - AIN1, - Excitation Current IOUT1, Nosie test
   * - 3
     - AIN2, RTD+
   * - 4
     - AIN3, RTD-
   * - 5
     - AIN4, TC+
   * - 6
     - AIN5, TC-
   * - 7
     - REFIN1+
   * - 8
     - REFIN1-

Connector J2: Bridge Connection
-------------------------------

.. list-table::
   :header-rows: 1

   * - Connector
     - Function
   * - 1
     - GND/SHIELD
   * - 2
     - Power Switch, Excitation-
   * - 3
     - REFIN-/ SENSE-
   * - 4
     - AIN6, AINN
   * - 5
     - AIN5, AINP
   * - 6
     - REFIN+/ SENSE+
   * - 7
     - AVDD, Excitation+
   * - 8
     - GND/SHIELD

Connector J3: SPD-120 pin connector
-----------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/ad4170_sdp_connection.png
   :width: 400px

Connector J4: AIN8-AIN15 connection
-----------------------------------

.. list-table::
   :header-rows: 1

   * - Connector
     - Function
   * - 1
     - AIN8
   * - 2
     - AIN9
   * - 3
     - AIN10
   * - 4
     - AIN11
   * - 5
     - AIN12
   * - 6
     - AIN13
   * - 7
     - AIN14
   * - 8
     - AIN15

Connector J5/J6/J9:
-------------------

.. list-table::
   :header-rows: 1

   * - Connector
     - Function
   * - J5
     - Optional external connector for a -1.8V supply, allowing external bench
       top or alternative supply for AVSS when using a split supply to power
       AD7124
   * - J6
     - Optional external connector, allowing external bench top or alternative
       supply for AVDD.
   * - J9
     - Optional external connector, allowing external bench top or alternative
       supply for IOVDD.

Connector J7:
-------------

.. list-table::
   :header-rows: 1

   * - Connector
     - Function
   * - 1
     - IOVDD
   * - 2
     - GND
   * - 3
     - AVSS
   * - 3
     - AVDD

Connector J8 SMB:
-----------------

Straight PCB mount SMB/SMA jack for master clock (not inserted). The EVAL board
has the footprint to include an SMA/SMB connector, if using an external clock
source to provide the master clock to the ADC.

Connector J11 PMOD (DNI):
-------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/ad7124_pmod_connection.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/ad7124_silk_connectors.png
   :width: 600px

Power Supplies
==============

The evaluation board receives power through the EVAL-SDP board when connected to
the PC via USB.

- Linear regulators generate the required power supply levels from the applied
  VIN rail.
- Each supply is decoupled at the point where it enters the board and again at
  the point where it connects to each device.

AVDD
----

#. **3.3V** supplied by ADP1720-3.3 (LK15, Pos A)(LK18, Pos A)
#. **1.8V**, split supply supplied by ADP1720-1.8 (LK15, Pos A)(LK18, Pos B)
#. EXT AVDD (LK15, Pos B). Connector J7

.. list-table::
   :header-rows: 1

   * - Supply
     - Regulator
     -
   * - 3.3V regulator
     - :adi:`ADP1720-3.3 <en/products/ADP1720.html>`
     -
   * - 1.8V regulator
     - :adi:`ADP1720-1.8 <en/products/ADP1720.html>`
     -

AVSS
----

#. AVSS shorted to GND via LK31/32/33 (LK17, Pos B)
#. **-1.8V**, split supply supplied from external connector J7. (LK17, Pos A)

IOVDD
-----

#. **3.3V**, supplied by ADP150ACBZ-3.3 (LK19, Pos B)
#. EXT IOVDD (LK19, Pos B)

.. list-table::
   :header-rows: 1

   * - Supply
     - Regulator
     -
   * - 3.3V regulator
     - :adi:`ADP150 <en/products/adp150.html>`
     -

Serial Interface
================

The evaluation board connects via the serial peripheral interface (SPI) to the
Blackfin® :adi:`ADSP-BF527 <en/products/adsp-bf527.html>` on the SDP-B board.
There are four primary signals: CS, SCLK, DIN, and DOUT/RDY (all are inputs,
except for DOUT/RDY, which is an output). To operate the evaluation board in
standalone mode, the AD7124 serial interface lines can be disconnected from the
120-pin header by removing the links LK21-24. The pins from these links can then
be used to fly-wire the signals to an alternative digital capture setup.

For an introduction to the Serial Peripheral Interface (SPI), click
:adi:`here <en/analog-dialogue/articles/introduction-to-spi-interface.html>`

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/spi_pic.png
   :width: 600px

Reference Options
=================

The Eval-AD7124-xASDZ includes an external 2.5 V reference (the ADR4525) and an
internal 2.5 V reference. The default operation is to use the external reference
input, which is set to accept the 2.5 V ADR4525 on the evaluation board. The
reference used for a conversion is selected by choosing the reference in the
Config registers associated with Setup 0 to Setup 7. Switch between using the
internal reference and external reference by accessing the AD7124-X registers
through the pop-ups via the evaluation software. Figure 1 (below) shows how to
select the reference source for Setup 0 to Setup 7. Figure 2 shows the
ADC_Control register setting that enables the internal reference.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/ref_source_pop_ups.png
   :width: 600px

   Figure 1: Reference Menu from Eval+ Software.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/eval-ad7124/hardware_guide/int_red.png
   :width: 200px

   Figure 2: Enabling the 2.5V Reference through pop-ups.

Schematics
==========

.. admonition:: Download

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/7124_schematic.pdf`

Bill of Materials
=================

.. admonition:: Download

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad7124/ad7124_bom.pdf`

:dokuwiki:`Continue to Software Guide </resources/eval/user-guides/ad7124-x/software>`
:dokuwiki:`Return to Homepage </resources/eval/user-guides/ad7124-x>`
