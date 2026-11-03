.. _eval-ad7124-4-8asdz_hardware:

EVAL-AD7124-4ASDZ / EVAL-AD7124-8ASDZ Hardware Guide
===============================================================================

Set-up Procedures
-------------------------------------------------------------------------------

After reviewing the :ref:`prerequisites <eval-ad7124-x prerequisites>`, set up
the evaluation board as detailed in this section.

#. Connect the :adi:`SDP-B` to the evaluation board via the
   120-pin SDP connector (J3).
#. Screw the two boards together using the plastic screw and washer set.
#. Connect the :adi:`SDP-B` to the PC using a USB cable.

.. note::

   No external power supply is required. The evaluation board is powered
   through the :adi:`SDP-B` via USB from the PC. On-board regulators generate
   all required supply voltages.

Power Supplies
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7124-4ASDZ<EVAL-AD7124>`/:adi:`EVAL-AD7124-8ASDZ <EVAL-AD7124>`
receives power through the controller
board when connected to the PC via USB. Linear regulators generate the required
power supply levels from the applied USB voltage.

AVDD and AVSS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**3.3 V supply (default):**

- 3.3 V ADP150A regulator supplies AVDD
- AVSS connected to GND (LK31 to LK33 inserted)

**+/- 1.8 V split supply:**

- +1.8 V ADP150A regulator supplies AVDD
- -1.8 V ADP7182 regulator supplies AVSS
- Remove LK31 to LK33 when using split supply

**External AVDD/AVSS:**

- External supply connections available on connector J7

.. list-table:: AVDD/AVSS Regulators
   :header-rows: 1

   * - Supply
     - Regulator
     - Shutdown Resistor
   * - +3.3 V
     - ADP150A
     - R42
   * - +1.8 V
     - ADP150A
     - R44
   * - -1.8 V
     - ADP7182
     - R3

IOVDD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**3.3 V supply (default):**

- 3.3 V ADP150A regulator supplies IOVDD
- GND connected to AVSS (LK31 to LK33 inserted)

**External IOVDD:**

- External supply connections available on connector J7

Link and Jumper Settings
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 10 10 70

   * - Link
     - Color
     - Default
     - Description
   * - LK1
     - Red
     - Inserted
     - Noise test: shorts AIN0 to AIN1
   * - LK2
     - Red
     - 1 Pin
     - Thermocouple cold junction resistor bypass
   * - LK3
     - Black
     - A
     - Pos A: REFIN+ to J2; Pos B: REFIN+ to J1
   * - LK4
     - Red
     - Inserted
     - Shorts REFIN- to AVSS
   * - LK5
     - Black
     - A
     - Pos A: REFIN+ to J2; Pos B: REFIN+ to J1
   * - LK6
     - Black
     - A
     - Pos A: REFIN+ to ADR4525 (external 2.5 V reference);
       Pos B: REFIN+ to INTREF
   * - LK7
     - Red
     - 1 Pin
     - Short REFIN-/AVSS (inserted = 4-wire bridge)
   * - LK8
     - Red
     - 1 Pin
     - Short REFIN-/PSW (inserted = 4-wire bridge)
   * - LK9
     - Red
     - 1 Pin
     - Short REFIN+/AVDD (inserted = 4-wire bridge)
   * - LK10
     - Black
     - Inserted
     - Short EXC+/AVDD (inserted = 4-wire bridge)
   * - LK11, LK12
     - Black
     - 1 Pin
     - Insert R97 into AVDD path for AVDD current test
   * - LK13, LK14
     - Black
     - 1 Pin
     - Insert R96 into IOVDD path for IOVDD current test
   * - LK15
     - Black
     - A
     - Pos A: AVDD to 3.3 V LDO; Pos B: AVDD to external AVDD
   * - LK16
     - Black
     - A
     - Pos A: AVSS to -1.8 V LDO; Pos B: AVSS to external AVSS
   * - LK17
     - Black
     - B
     - Pos A: AVSS to -1.8 V LDO (disconnect LK31--LK33);
       Pos B: AVSS to DGND
   * - LK18
     - Black
     - A
     - Pos A: AVDD to 3.3 V LDO; Pos B: AVDD to +1.8 V LDO
       (if LK15 in Pos A)
   * - LK19
     - Black
     - B
     - Pos A: IOVDD to external IOVDD; Pos B: IOVDD to LDO supply
   * - LK27--LK30
     - Black
     - A
     - Pos A: Arduino communication to P4;
       Pos B: Arduino communication to P3 (standalone SPI breakout)
   * - LK31--LK33
     - Black
     - Inserted
     - Short AVSS to DGND
   * - T_AVDD
     - Black
     - A
     - Pos A: AVDD direct; Pos B: AVDD through R97 (with LK11/LK12)
   * - T_IOVDD
     - Black
     - A
     - Pos A: IOVDD direct; Pos B: IOVDD through R96 (with LK13/LK14)

On-Board Connectors
-------------------------------------------------------------------------------

Analog Input Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Connector
     - Function
     - Pin Details
   * - A2
     - Thermocouple
     - Pin 1: AIN2 (TC+), Pin 2: AIN3 (TC-)
   * - J1
     - Analog inputs, RTD, thermocouple
     - Pin 1: AIN0/IOUT0 (noise test), Pin 2: AIN1/IOUT1 (noise test),
       Pin 3: AIN2 (RTD+), Pin 4: AIN3 (RTD-), Pin 5: AIN4 (TC+),
       Pin 6: AIN5 (TC-), Pin 7: REFIN1+, Pin 8: REFIN1-
   * - J2
     - Analog inputs, wire bridge
     - Pin 1: GND, Pin 2: EXC-/PSW, Pin 3: REF-/sense-,
       Pin 4: AIN6 (AINN, DC filtered), Pin 5: AIN5 (AINP, DC filtered),
       Pin 6: REF+/sense+, Pin 7: EXC+/AVDD, Pin 8: GND
   * - J4
     - Additional inputs (AD7124-8 only)
     - Pin 1--8: AIN8 through AIN15

Digital and Power Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - Connector
     - Function
   * - J3
     - 120-pin SDP connector for :adi:`SDP-B`
   * - J5
     - DGND and external AVSS
   * - J6
     - External AVDD and DGND
   * - J7
     - External power: IOVDD, GND, AVSS, AVDD
   * - J8
     - External MCLK input (Pin 1: MCLK, Pins 2--5: DGND)
   * - J9
     - External IOVDD and DGND
   * - J11
     - PMOD connector
   * - P1--P5
     - Arduino connectors

Serial Interface
-------------------------------------------------------------------------------

The AD7124-4/AD7124-8 communicates via a 4-wire SPI interface: CS (active low),
SCLK, SDI, and SDO/RDY. By default, the RDY function is also available on the
SDO pin.

Serial communication options:

- **SDP-120 pin connection** -- via :adi:`SDP-B` (default)
- **PMOD connector** (J11)
- **Standalone mode** -- move LK27--LK30 from Pos A to Pos B to expose SPI
  signals on the P3 connector for fly-wiring to an alternative digital capture
  setup

Reference Options
-------------------------------------------------------------------------------

The evaluation board includes an on-board 2.5 V ADR4525 precision voltage
reference and the AD7124's internal 2.5 V reference.

The default configuration uses the external ADR4525 reference. The reference
source for each conversion is selected through the configuration registers
(Setup 0 to Setup 7) in the evaluation software.

Design and Integration Files
-------------------------------------------------------------------------------

Schematics, layout files, and bill of materials are available on the
:adi:`EVAL-AD7124-4ASDZ <EVAL-AD7124>` product page.
