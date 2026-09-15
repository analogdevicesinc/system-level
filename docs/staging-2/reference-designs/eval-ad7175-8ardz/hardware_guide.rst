.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ad7175-8ardz/hardware_guide

.. _eval-ad7175-8ardz hardware_guide:

Hardware Guide
==============

Device Description
------------------

The :adi:`AD7175-8 <en/products/ad7175-8.html>` a highly accurate, high
resolution, multiplexed, 8-/16-channel (full/pseudo differential) Σ-Δ ADC. The
:adi:`AD7175-8 <en/products/ad7175-8.html>` has a maximum channel-to-channel
scan rate of 50 kSPS (20 µs) for fully settled data The output data rates range
from 5 SPS to 250 kSPS. The device includes integrated analog input and
reference buffers, an integrated precision 2.5 V reference, and an integrated
oscillator.

Set-up Procedures
-----------------

After following the instructions in the Software Installation Procedures
section, set up the evaluation board and the SDP-K1 board as detailed in this
section.

.. important::

   The ACE software and drivers must be installed before connecting the
   EVAL-AD7175-8ARDZ and the EVAL-SDP-CK1Z board to the USB port of the PC to
   ensure that the PC correctly recognizes the evaluation system

**Configuring the Evaluation and SDP Boards** Use the following procedure to
configure the boards

#. Connect the SDP-K1 to the Arduino headers of the evaluation board.
#. If using the SDP-K1 board the Arduino headers can also be used to connect to
   the board
#. Connect the SDP board to the PC using the USB cable.

Evaluation Board
----------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7175-8/65002_2.jpg
   :width: 600px

Hardware Link Options
---------------------

.. list-table::
   :header-rows: 1

   * - Link Number
     - Default Position
     - Description
     -
     -
   * - LK1
     - B
     - Selects the voltage applied to the AVDD1 pin. Operates using the AVDD 5V supply (default). When inserted in **Position A**, sets the AVDD1 voltage to the 3.3V supply from the ADP150 (U6) regulator. Setting AVDD1 = 3.3V is not allowed when AVSS = -2.5V.
     -
     -
   * - LK2
     - B
     - Selects the voltage applied to the AVDD2 pin. Operates using the AVDD 5V supply (default). When inserted in **Position A**, sets the AVDD2 voltage to the 3.3V supply from the ADP150 (U6) regulator. Setting AVDD2 = 3.3V is not allowed when AVSS = -2.5V.
     -
     -
   * - LK3
     - B
     - Selects the external clock input or internal clock output (default). When inserted in **Position A**, selects the CRYSTAL OPTION.
     -
     -
   * - LK4
     - Inserted
     - Insert to connect REF- to AVSS.
     -
     -
   * - LK5
     - B
     - Connects REF+ to 5V external reference (default). When inserted in **Position A**, REF+ is connected to 2.5V internal reference.
     -
     -
   * - LK6
     - A
     - Turns ON the :adi:`LTC3129 <en/products/LTC3129.html>` (U3) to supply 7V to the LDO linear regulators (default). When inserted in **Position B**, turns OFF the :adi:`LTC3129 <en/products/LTC3129.html>` (U3).
     -
     -
   * - LK7
     - B
     - Shifts the voltage of AVDD 5.5V to 7V when inserted in **Position A**. When inserted in **Position B**, AVDD 5.5V is set to 5.5V (default).
     -
     -
   * - LK8
     - A
     - Turns ON the :adi:`ADP7118 <en/products/ADP7118.html>` (U10) to supply for AVDD 5.5V. The AVDD 5.5V is supplied with 5.5V from ADP7118 regulator (default). When inserted in **Position B**, turns OFF the :adi:`ADP7118 <en/products/ADP7118.html>` (U10).
     -
     -
   * - LK9
     - A
     - Turns ON the 5V LDO to supply for AVDD 5V. The AVDD 5V is supplied with 5V from :adi:`ADP7118 <en/products/ADP7118.html>` (U11) regulator (default). When inserted in **Position B**, turns OFF the :adi:`ADP7118 <en/products/ADP7118.html>` (U11).
     -
     -
   * - LK10
     - A
     - Turns ON the 2.5V LDO to supply for AVDD 2.5V. The AVDD 2.5V is supplied with 2.5V from :adi:`LT1962 <en/products/LT1962.html>` (U4) regulator (default). When inserted in **Position B**, turns OFF the :adi:`LT1962 <en/products/LT1962.html>` (U4).
     -
     -
   * - LK11
     - A
     - Turns ON the :adi:`LT1983 <en/products/LT1983.html>` (U2) to supply for the ADP7182 (U5) 2.5V linear regulator (default). When inserted in **Position B**, turns OFF the :adi:`LT1983 <en/products/LT1983.html>` (U2).
     -
     -
   * - LK12
     - A
     - Turns ON the :adi:`ADP7182 <en/products/ADP7182.html>` (U5) to supply for -2.5V. The -2.5V is supplied with -2.5V from the ADP7182 regulator (default); AVSS can be connected to ground depending on S1. When inserted in **Position B**, turns OFF the :adi:`ADP7182 <en/products/ADP7182.html>` (U5).
     -
     -
   * - LK13
     - A
     - Turns ON the 3.3V LDO to supply for IOVDD 3.3V. The IOVDD 3.3V is supplied with 3.3V from :adi:`ADP150 <en/products/ADP150.html>` (U6) regulator (default). When inserted in **Position B**, turns OFF the :adi:`ADP150 <en/products/ADP150.html>` (U6).
     -
     -
   * - LK14
     - Removed
     - Insert LK14 when performing Noise Test.
     -
     -
   * - LK15
     - A
     - Set to **A**, connects REFOUT to VCM (default). Set to **B**, connects REFOUT to A0. **Remove** LK15 when using an external VCM from J15.
     -
     -
   * - LK16
     - B
     - Set to **A**, connects AIN0 to ADC Driver. Set to **B**, connects/directs AIN0 to ADC (default). **Remove** LK16 when connecting AIN0 to surfboard.
     -
     -
   * - LK17
     - B
     - Set to **A**, connects AIN1 to ADC Driver. Set to **B**, connects/directs AIN1 to ADC (default). **Remove** LK17 when connecting AIN0 to surfboard.
     -
     -
   * - LK18
     - A
     - Set to **A**, connects -VS to GND (default). Set to **B**, connects -VS to -2.5 V. **Remove** LK18 when using external supply.
     -
     -
   * - LK19
     - B
     - Set to **A**, connects +VS to AVDD 5 V. Set to **B**, connects +VS to AVDD 5.5 V (default). **Remove** LK19 when using external supply.
     -
     -
   * - LK20
     - Inserted
     - When **inserted**, initiates power down for the :adi:`ADA4945 <en/products/ADA4945.html>`/:adi:`ADA4940 <en/products/ADA4940.html>`. **Remove** when using the ADC DRIVER. **Insert** LK20 when performing Noise Test or when Surfboard is connected.
     -
     -
   * - LK21
     - A
     - Set to **A**, connects SCLK to standard Arduino connection (default). Set to **B** when using multiple boards; connects SCLK to alternative Arduino connection.
     -
     -
   * - LK22
     - A
     - Set to **A**, connects DOUT to standard Arduino connection (default). Set to **B** when using multiple boards; connects DOUT to alternative Arduino connection.
     -
     -
   * - LK23
     - A
     - Set to **A**, connects DIN to standard Arduino connection (default). Set to **B** when using multiple boards; connects DIN to alternative Arduino connection.
     -
     -
   * - LK24
     - A
     - Set to **A**, connects CS to standard Arduino connection (default). Otherwise, select different CS for stacking multiple boards.
     -
     -

On Board Connections
--------------------

.. list-table::
   :header-rows: 1

   * - Connector
     - Function
     - Connector Type
     -
   * - J1
     - External clock input or ADC internal clock output
     - SMB Connector Jack, Male Pin 50Ω Through Hole Solder
     -
   * - J2
     - External bench top voltage supply option for AVDD 5V, AVDD 2.5V, AVSS
       -2.5V, and IOVDD inputs on the
       :adi:`AD7175-8 <en/products/ad7175-8.html>`
     - Screw terminal block, 2.54 mm pitch
     -
   * - J4
     - Arduino Headers (Power)
     - 8 Position Receptacle Connector, 2.54mm pitch
     -
   * - J5
     - Arduino Header (Digital 1)
     - 10 Position Receptacle Connector, 2.54mm pitch
     -
   * - J6
     - Arduino Header (Analog)
     - 6 Position Receptacle Connector, 2.54mm pitch
     -
   * - J7
     - Arduino Header (Digital 0)
     - 8 Position Receptacle Connector, 2.54mm pitch
     -
   * - J8
     - PMOD form factor
     - 12-pin header, 2.54mm pitch
     -
   * - J9
     - Arduino Header (IFCSP)
     - 6 Position, 2 row, Receptable Connector, 2.54mm pitch
     -
   * - J15 and J17
     - Analog input terminal block; wired connection to external source or
       sensor
     - Power socket block, 8-pin, 2.54 mm pitch, 3.5mm solder tail
     -
   * - J16
     - Analog input terminal block; wired connection to external source or
       sensor
     - Power socket block, 6-pin, 2.54 mm pitch, 3.5mm solder tail
     -
   * - J18
     - GPIO terminal
     - 4 Position 1 Row vertical PCB header, 2.54mm pitch
     -
   * - J19
     - Surfboard header (optional)
     - 7-way, 2.54 mm pin socket
     -
   * - J20
     - Surfboard header (optional)
     - 7-way, 2.54 mm pin header
     -

Power Supplies
==============

The evaluation board receives power through the controller board when connected
to the PC via 5V USB. Linear regulators generate the required power supply
levels from the applied USB voltage.

- Each regulator can be shut down using their shut down links highlighted in
  orange below.

AVDD1 and AVSS selection (S1)
-----------------------------

#. **5V supply (DEFAULT)**

- Position switch (S1) to SINGLE on the board
- 5V regulator supplies AVDD1
- AVSS tied to AGND

#. **±2.5V split supply**

- Position switch (S1) to SPLIT on the board
- 2.5V regulator supplies AVDD1
- -3V regulator -2.5V regulator supplies AVSS

===AVDD1 and AVDD2 selection (LK1 and LK2)===

#. **5V supply (DEFAULT)**

- Set LK1 and/or LK2 to position B
- 5V regulator supplies AVDD1

#. **3.3V supply**

- Set LK1 and/or LK2 to position A
- 3.3V regulator supplies IOVDD

#. **External AVDD/AVSS**

- Set LK1, LK2, LK9, LK10, LK11, LK12, and LKL13 to position B
- When using external AVDD only, set S1 to SINGLE , and connect external AVDD
  pin 1 of J2.
- When using external AVDD and AVSS, set S1 to SPLIT , and connect external AVDD
  and AVSSS to pins 2 and 3 of J2 respectively.

.. list-table::
   :header-rows: 1

   * - Supply
     - Regulator
     - Shut down Link
     -
   * - 5V regulator
     - :adi:`ADP7118ACPZN5.0-R7 <en/products/adp7118.html>`
     - LK9
     -
   * - 2.5V regulator
     - :adi:`LT1962EMS8-2.5#PBF <en/products/ltc1962.html>`
     - L10
     -
   * - -2.5V regulator
     - :adi:`ADP7182AUJZ-2.5-R7 <en/products/adp7182.html>`
     - L12
     -
   * - 3.3V regulator
     - :adi:`ADP150ACBZ-3.3-R7 <en/products/adp150.html>`
     - LK13
     -

Serial Interface
================

There are four primary signals: CS, SCLK, MOSI/DIN, and MISO/DOUT (all are
inputs, except for MISO/DOUT, which is an output). The EVAL-AD7175-8ARDZ
evaluation board connects to any microcontroller board that uses the Arduino
standard headers. This can be developed user code in for a variety of platforms.

Serial communication options
----------------------------

#. Arduino connection using the SDP-K1
#. PMOD connector
#. Standalone mode

- Removing the links LK21, LK22, LK23, and LK24, then using J5 to access all SPI
  signals and set the input/output voltage levels.

For an introduction to the Serial Peripheral Interface (SPI), click
:adi:`here <en/analog-dialogue/articles/introduction-to-spi-interface.html>`

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7175-8/spi.png
   :width: 600px

Analog Inputs
-------------

The
:adi:`EVAL-AD7175-8ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD7175-8.html>`
primary analog inputs can be applied on J15, J16, and J17 which are at the left
side of the board. Differential analog inputs are applied on AIN0 and AIN1 when
using the ADC driver (when using ADC driver, enable AIN+/- buffers). The
:adi:`AD7175-8 <en/products/ad7175-8.html>` evaluation software is set up to
analyze dc inputs to the ADC. The AD7175-8 input buffers work for dc input
signals.

Reference Options
-----------------

#. :adi:`AD7175-8 <en/products/ad7175-8.html>` internal 2.5V reference.
#. **DEFAULT** :adi:`ADR4550 <en/products/ADR4550.html>` on board external
   reference.
#. External reference connector J17 through AIN1/REF2+ and AIN0/REF2− pins.

Selecting the reference source:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software
^^^^^^^^

Example shows setting reference for Channel 0, for channel n, go to register
SETUPCON[n]

#. Board should be correctly connected to ACE.
#. Open AD7175-8 memory map (Memory Map Side-By-Side)
#. Search for the SETUPCON[0] register
#. Set the REF_SEL_N[0] to the desired reference source or the Data(hex) to the
   relevant bits

::

   - **On board External reference 1** REF+/- (Hex value 00, Binary Value 00).
   - **External reference 2** REF2+/− (Hex value 01, Binary Value 01).
   - **Internal 2.5V reference** REFOUT, AVSS (Hex Value 02, Binary Value 10).
   - **AVDD to AVSS** (Hex Value 03, Binary Value 11).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7175-8/ref_figure.png
   :width: 600px

Hardware
^^^^^^^^

.. list-table::
   :header-rows: 1

   * - Link Numbers
     - Type
     - Default Position
     - Descirption
     -
   * - LK4
     - Link
     - Inserted
     - Inserted: Connects REF- to AVSS
       Removed: Disconnects REF- to AVSS
     -
   * - LK5
     - Link
     - B
     - REF+/- connections:
       Set to A: Connects REF+ to REFOUT
       Set to B: Connects REF+ to on board :adi:`ADR4550 <en/products/ADR4550.html>` external reference
     -

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   EVAL-AD7175-8ARDZ Rev B Design and Integration Files

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7175-8ardz/Schematic.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7175-8ardz/Layout.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7175-8ardz/Bill of Materials.xlsx`

:dokuwiki:`Continue to Software Guide </resources/eval/user-guides/eval-ad7175-8ardz/software>`
:dokuwiki:`Return to Homepage </resources/eval/eval-ad7175-8ardz>`
