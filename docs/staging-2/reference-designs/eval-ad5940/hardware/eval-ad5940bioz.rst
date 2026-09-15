.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ad5940/hardware/eval-ad5940bioz

.. _eval-ad5940 hardware eval-ad5940bioz:

AD5940 Bio-Electric Shield User Guide
=====================================

Introduction
------------

The EVAL-AD5940BIOZ shield was designed specifically for carrying out
bio-electric measurements. These include:

- Electrodermal Activity (EDA)
- Body Impedance Analysis (4-wire) (BIA) with Z-board
- Electrocardiogram (ECG)
- Body Impedance Analysis (2-wire) (BIOZ-2Wire)

The platform is an Arduino UNO form factorbase board. This section describes the
key features of the board and how to set it up to take measurements.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/eval-ad5940bioz.jpg
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/bioz_block_diagram.jpg
   :width: 600px

Connectors and Jumpers
----------------------

All the connectors and their default configurations are described in the table
below.

.. list-table::
   :header-rows: 1

   * - Connector
     - Jmpr Position.
     - Description
   * - JP1 (DVDD)
     - A
     - DVDD powered from 3.3V on Arduino Header (Default)
   * -
     - B
     - DVDD powered from LDO
   * -
     - C
     - DVDD powered from external source connected to P11
   * - JP2 (AVDD)
     - A
     - AVDD powered from 3.3V on Arduino Header (Default)
   * -
     - B
     - AVDD powered from LDO
   * -
     - C
     - AVDD powered from external source connected to P8
   * - JP3 (Reset)
     - A
     - Reset pin connected to ARST Button (Default)
   * -
     - B
     - Reset pin connected to Arduino Header Reset pin
   * -
     - C
     - Reset pin connected to Arduino header P1.3 (Default)
   * - P9 (LDO Enable)
     - 1-2
     - LDO Enabled
   * -
     - 2-3
     - LDO Disabled (Default)
   * - P15 (LDO Aux Enable)
     - 1-2
     - LDO Enabled
   * -
     - 2-3
     - LDO Disabled (Default)
   * - JP5 (Default DNI)
     - A
     - Pull up resistor (R25) connected to electrode bias
   * -
     - B
     - Pull down resistor (R25)connected electrode bias
   * - JP6 (Default DNI)
     - A
     - Pull up resistor (R42) connected to electrode bias
   * -
     - B
     - Pull down resistor (R42)connected electrode bias
   * - JP7 (Bias Select)
     - 3-1
     - Electrode bias connected to REFOUTS
   * -
     - 3-4
     - Electrode bias connected RLD
   * -
     - 3-5
     - Electrode bias connected to VDD
   * - JP8
     - A
     - Connected. EEPROM write protect
   * - P16
     - 1-2
     - Pull up resistor R46 for ECG_P to electrode bias (Default)
   * -
     - 2-3
     - Pull down resistor R46 for ECG_P to GND
   * - P17
     - 1-2
     - Pull up resistor R23 for ECG_P to electrode bias (Defaut)
   * -
     - 2-3
     - Pull down resistor R23 for ECG_P to GND

USB Connector
-------------

The Micro USB connector, P6, on the EVAL-AD5940BIOZ board serves 2 functions.

- The provided ECG cables can be connected to a human body simulator which can
  be used to verify ECG, body composition etc. Note: The EVAL-AD5940BIOZ must
  never be connected to the human body while the board is connected to a PC or
  Laptop
- The provided AD5940 Z Test board can also be connected to the Micro USB
  connecter. This board contains a number of banks of resistors and capacitors
  which can be used to model Body Impedance, Skin Impedance, Electrode
  impedances and Contact impedance. These resistor values are configured with
  the various switches.

Note, P6 USB connector must only be used with the supplied AD5940 Z Test board
or the provided ECG Cables. No other cable should ever be connected.

Micro USB pinout for connecting ECG Cables:

3-wire ECG cable:

.. list-table::
   :header-rows: 1

   * - USB pin
     - Function
     - Cable color
   * - 1
     - F+
     - RED
   * - 2
     - S+ (ECG IN+)
     - N/C
   * - 3
     - S- (ECG IN-)
     - BLUE/GREEN
   * - 4
     - N/C
     - N/C
   * - 5
     - F- (ECG RLD)
     - BLACK

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download

   EVAL-AD5940BIOZ Rev B Design Files

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/02_049988b_top.pdf`
   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/08-049988-01-b.pdf`
   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/eval-ad5940bioz_bom.xlsx`
   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/hardware/eval-ad5940bioz_fabrication.zip`
