.. imported from: https://wiki.analog.com/resources/eval/user-guides/pmd-ard-intz

.. _pmd-ard-intz:

PMD-ARD-INTZ Hardware User Guide
================================

Overview
--------

Arduino interface is found on many development platforms and is used on many
prototype designs. The Pmod standard is a 6,8, or 12-pin standard that carries
GPIO and/or serial communication protocols. PMD-ARD-INTZ enables four Pmod
modules to interface with :adi:`EVAL-ADICUP3029` / :adi:`EVAL-ADICUP360`
development boards or any equivalent Arduino MCU boards. Out of the four Pmod
ports, two is configured as SPI Pmod, one is I²C Pmod, the other one can be
configured as either SPI or UART Pmod.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/board.png
   :width: 650px

General Setup
-------------

Power Source Settings
~~~~~~~~~~~~~~~~~~~~~

The circuit is powered either by the voltages coming from the Arduino headers or
the input DC voltage supplied from the barrel jack of the MCU baseboard. Switch
S1 is used to choose where the system voltages (3.3V and 5V) is sourced from.

Positioning S1 to ARD will cause the board to use voltage supplied from the MCU
baseboard headers. Positioning S2 to LDO uses the DC voltage supplied from the
barrel jack of the MCU baseboard, then regulated by LT1763-3.3 and LT1763-5 to
provide the 3.3V and 5V system voltage respectively.

A green LED (labeled DS1) should be lit to indicate that the board is powered
up.

.. important::

   Recommended external supply voltage is 7 to 13 volts.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/powersource.png
   :width: 200px

Logic Voltage Settings
~~~~~~~~~~~~~~~~~~~~~~

Each Pmod port has bidirectional voltage level translators. This enables
compatibility with Pmod modules and MCU baseboards that has different logic
voltage levels.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/logic_voltage.png
   :width: 300px

The logic voltage level of each Pmod port can be set to either 3.3V or 5V using
the shunt connectors P4,P5,P6, and P7.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/vlogic.png
   :width: 250px

Meanwhile, the logic voltage source of the MCU baseboard can be chosen from the
IOREF from the MCU baseboard header and the 3.3V and 5V system voltages using
the shunt connector between P22 and P21 (encircled blue in Fig D). Preferably,
this should be set to IOREF to ensure a proper voltage setting.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/ioref.png
   :width: 200px

Reset Logic Active State
~~~~~~~~~~~~~~~~~~~~~~~~

The reset button (S2) on PMD-ARD-INTZ resets the MCU baseboard and all of the
Pmod ports simultaneously. By default, the reset pins are **Active Low** and can
be changed to an **Active High** using solder jumpers JP1, JP2, JP3, JP4 for the
Pmod ports and JP5 for the MCU.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/reset.png
   :width: 400px

Pmod Interface Types
--------------------

The Pmod connectors on the PMD-ARD-INTZ follow the latest
`Digilent Pmod Interface Specifications-1.2.0 <https://reference.digilentinc.com/_media/reference/pmod/pmod-interface-specification-1_2_0.pdf?_ga=2.175543138.1114585894.1586850120-1554022246.1542436433>`__.
Pin assignments are adapted from Arduino UNO pin assignments. Different MCU
baseboards have different pinouts. If a different MCU baseboard is used, use the
Arduino UNO pinout as a reference to determine the proper pin number for your
MCU baseboard.

SPI Ports
~~~~~~~~~

Pmod ports (P11,P12, and P13) follows the expanded SPI interface. P11 and P12
are dedicated SPI ports while P13 can be configured to either expanded SPI or
expanded UART. To configure P13 as expanded SPI, set the shunt connectors P8,
P9, and P10 similiar to the encircled in Figure A.

.. list-table::
   :header-rows: 1

   * - Pin No.
     - P11: SPI 0
     - P12: SPI 1
     - P13: SPI 2
   * - 1
     - D10 (CS)
     - D9 (CS)
     - D8 (CS)
   * - 2
     - D11 (MOSI)
     - D11 (MOSI)
     - D11 (MOSI)
   * - 3
     - D12 (MISO)
     - D12 (MISO)
     - D12 (MISO)
   * - 4
     - D13 (SCK)
     - D13 (SCK)
     - D13 (SCK)
   * - 5
     - GND
     - GND
     - GND
   * - 6
     - VCC
     - VCC
     - VCC
   * - 7
     - D6 (GPIO/INT)
     - D5 (GPIO/INT)
     - D4 (GPIO/INT)
   * - 8
     - RST
     - RST
     - RST
   * - 9
     - A5 (GPIO/CS2)
     - A3 (GPIO/CS2)
     - A1 (GPIO/CS2)
   * - 10
     - A4 (GPIO/CS3)
     - A2 (GPIO/CS3)
     - A0 (GPIO/CS3)
   * - 11
     - GND
     - GND
     - GND
   * - 12
     - VCC
     - VCC
     - VCC

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/p13_spi.png
   :width: 200px

I²C Port
~~~~~~~~

Pmod port (P16) is designed to interface to both old and new I²C modules. The
older versions of I²C pmod (2×4 connector) should be attached to pins 3-4 and
9-10 of P16 and new versions of I²C pmod (1×6 connector) should be attached to
pins 1-6 or pins 7-12 of P16 as shown in the table below.

.. list-table::
   :header-rows: 1

   * - Pin No.
     - P16: New I²C
     - P16: Old I²C
   * - 1
     - D3 (INT)
     - -
   * - 2
     - RST
     - -
   * - 3
     - D19 (SCL)
     - D19 (SCL)
   * - 4
     - D18 (SDA)
     - D18 (SDA)
   * - 5
     - GND
     - GND
   * - 6
     - VCC
     - VCC
   * - 7
     - D3 (INT)
     - -
   * - 8
     - RST
     - -
   * - 9
     - D19 (SCL)
     - D19 (SCL)
   * - 10
     - D18 (SDA)
     - D18 (SDA)
   * - 11
     - GND
     - GND
   * - 12
     - VCC
     - VCC

Pull-up resistors (4.7 kΩ) for SCL and SDA lines are also provided. Apply a
short on solder jumpers P14, P15, P17, and P18 to use the pull-up resistors.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/i2c_pullup.png
   :width: 300px

UART Port
~~~~~~~~~

Pmod port (P13) can be reconfigured between an expanded SPI and expanded UART.
To configure P13 as expanded UART, set the shunt connectors P8, P9, and P10.

.. list-table::
   :header-rows: 1

   * - Pin No.
     - P13: UART
   * - 1
     - D8 (CTS)
   * - 2
     - D1 (RX)
   * - 3
     - D0 (TX)
   * - 4
     - D2
   * - 5
     - GND
   * - 6
     - VCC
   * - 7
     - D4 (GPIO/INT)
   * - 8
     - RST
   * - 9
     - A1 (GPIO)
   * - 10
     - A0 (GPIO)
   * - 11
     - GND
   * - 12
     - VCC

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pmd-ard-intz/p13_uart.png
   :width: 200px

--------------

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`PMD-ARD-INTZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/pmd-ard-intz-designsupport.zip>`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you register your hardware.
   :reg:`Register <PMD-ARD-INTZ?&v=Rev D>` to receive all these great benefits
   and more!

// End of document //
