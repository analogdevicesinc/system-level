.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/pmd-rpi-intz

.. _circuits-from-the-lab pmd-rpi-intz:

PMD-RPI-INTZ Hardware User Guide
================================

Overview
--------

The :adi:`PMD-RPI-INTZ` is an add-on adapter board for the Raspberry Pi that
allows interfacing with up to 4 Pmod boards (2 SPI devices, 2 I2C devices), 1
QuikEval™ demonstration board and 1 :adi:`DC1613A`-compatible demonstration
board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intzangle.jpg
   :width: 400px

The :adi:`PMD-RPI-INTZ` follows the standard Raspberry Pi HAT mechanical
specifications, minus the cutouts for the camera and display flexis. An ID
EEPROM is also included on the board to allow auto-configuration.

.. note::

   **Evaluation Kit Contents:**

   - :adi:`PMD-RPI-INTZ` Adapter Board (Buy: PMD-RPI-INTZ)

Adapter Board Hardware
----------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-top-labels.png
   :width: 600px

.. important::

   There is no level translation provided on the :adi:`PMD-RPI-INTZ`. Only
   connect devices that operate with 3.3V logic levels. Do not apply higher
   logic levels on the IO pins to avoid damaging the Raspberry Pi.

SPI Pmod Connectors (P1 and P2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-spi-pmod-connectors.png
   :width: 250px

Pmod devices that use the SPI interface should be connected to either of the two
2x6 female headers located on the left-hand side of the :adi:`PMD-RPI-INTZ`.
Each header pin is connected to a Raspberry Pi GPIO pin through the 40 pin
connector (P9).

The table below lists the default Raspberry Pi GPIO pin assignments for the P1
pins and their corresponding functions.

.. list-table::
   :header-rows: 1

   * - SPI Pmod Connector #1 (P1) Pinout
     -
     -
   * - **Pin Number**
     - **Default Raspberry Pi Pin Assignment**
     - **Pin Function on the PMD-RPI-INTZ**
   * - 1
     - Pin 24 (GPIO8)¹
     - **SPI Pmod #1 CS1.** SPI Chip Select #1 from the Raspberry Pi to the Pmod
       device.
   * - 2
     - Pin 19 (SPI0 MOSI)²
     - **MOSI.** SPI Data from the Raspberry Pi to the Pmod device.
   * - 3
     - Pin 21 (SPI0 MISO)²
     - **MISO.** SPI Data from the Pmod device to the Raspberry Pi.
   * - 4
     - Pin 23 (SPI0 SCLK)²
     - **SCLK.** SPI Clock from the Raspberry Pi to the Pmod device.
   * - 5
     - GND
     - **Ground**
   * - 6
     - 3V3 Power
     - **SPI Pmod #1 VCC.** Connected to the 3.3V Regulator Output of the
       Raspberry Pi.
   * - 7
     - Pin 35 (GPIO19)
     - **SPI Pmod #1 INT.** Interrupt Signal from the Pmod device to the
       Raspberry Pi.
   * - 8
     - Pin 40 (GPIO21)
     - **SPI Pmod #1 RESET.** Reset Signal from the Raspberry Pi to the Pmod
       device.
   * - 9
     - Pin 38 (GPIO20)
     - **SPI Pmod #1 CS2.** SPI Chip Select #2 from the Raspberry Pi to the Pmod
       device.
   * - 10
     - Pin 12 (GPIO18)
     - **SPI Pmod #1 CS3.** SPI Chip Select #3 from the Raspberry Pi to the Pmod
       device.
   * - 11
     - GND
     - **Ground**
   * - 12
     - 3V3 Power
     - **SPI Pmod #1 VCC.** Connected to the 3.3V Regulator Output of the
       Raspberry Pi.

¹IO pin shared with the QuikEval™ Demo Board Connector (P5).

²IO pins shared with the SPI Pmod Connector #2 (P2) and the QuikEval™ Demo Board
Connector (P5).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-spi-pmod-labels.png
   :width: 200px

Similarly, the table below lists the default Raspberry Pi GPIO pin assignments
for the P2 pins and their corresponding functions.

.. list-table::
   :header-rows: 1

   * - SPI Pmod Connector #2 (P2) Pinout
     -
     -
   * - **Pin Number**
     - **Default Raspberry Pi Pin Assignment**
     - **Pin Function on the PMD-RPI-INTZ**
   * - 1
     - Pin 26 (GPIO7)
     - **SPI Pmod #2 CS1.** SPI Chip Select #1 from the Raspberry Pi to the Pmod
       device.
   * - 2
     - Pin 19 (SPI0 MOSI)¹
     - **MOSI.** SPI Data from the Raspberry Pi to the Pmod device.
   * - 3
     - Pin 21 (SPI0 MISO)¹
     - **MISO.** SPI Data from the Pmod device to the Raspberry Pi.
   * - 4
     - Pin 23 (SPI0 SCLK)¹
     - **SCLK.** SPI Clock from the Raspberry Pi to the Pmod device.
   * - 5
     - GND
     - **Ground**
   * - 6
     - 3V3 Power
     - **SPI Pmod #2 VCC.** Connected to the 3.3V Regulator Output of the
       Raspberry Pi.
   * - 7
     - Pin 22 (GPIO25)
     - **SPI Pmod #2 INT.** Interrupt Signal from the Pmod device to the
       Raspberry Pi.
   * - 8
     - Pin 32 (GPIO12)
     - **SPI Pmod #2 RESET.** Reset Signal from the Raspberry Pi to the Pmod
       device.
   * - 9
     - Pin 29 (GPIO5)
     - **SPI Pmod #2 CS2.** SPI Chip Select #2 from the Raspberry Pi to the Pmod
       device.
   * - 10
     - Pin 31 (GPIO6)
     - **SPI Pmod #2 CS3.** SPI Chip Select #3 from the Raspberry Pi to the Pmod
       device.
   * - 11
     - GND
     - **Ground**
   * - 12
     - 3V3 Power
     - **SPI Pmod #2 VCC.** Connected to the 3.3V Regulator Output of the
       Raspberry Pi.

¹IO pins shared with the SPI Pmod Connector #1 (P1) and the QuikEval™ Demo Board
Connector (P5).

I²C Pmod Connectors (P3 and P4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-i2c-pmod-connectors.png
   :width: 250px

Pmod devices that use the I²C interface should be connected to either of the two
2x6 female headers located on the lower side of the :adi:`PMD-RPI-INTZ`. Each
header pin is connected to a Raspberry Pi GPIO pin through the 40 pin connector
(P9).

The table below lists the default Raspberry Pi GPIO pin assignments for the P3
pins and their corresponding functions.

.. list-table::
   :header-rows: 1

   * - I²C Pmod Connector #1 (P3) Pinout
     -
     -
   * - **Pin Numbers**
     - **Default Raspberry Pi Pin Assignment**
     - **Pin Function on the PMD-RPI-INTZ**
   * - 1 & 7
     - Pin 37 (GPIO26)
     - **I²C Pmod #1 INT.** Interrupt Signal from the Pmod device to the
       Raspberry Pi.
   * - 2 & 8
     - Pin 33 (GPIO13)
     - **I²C Pmod #1 RESET.** Reset Signal from the Raspberry Pi to the Pmod
       device.
   * - 3 & 9
     - Pin 5 (I²C SCL)¹
     - **SCL.** I²C Clock from the Raspberry Pi to the Pmod device.
   * - 4 & 10
     - Pin 3 (I²C SDA)¹
     - **SDA.** I²C Data from the Raspberry Pi to the Pmod device.
   * - 5 & 11
     - GND
     - **Ground**
   * - 6 & 12
     - 3V3 Power
     - **I²C Pmod #1 VCC.** Connected to the 3.3V Regulator Output of the
       Raspberry Pi.

¹IO pins shared with the I2C Pmod Connector #2 (P4), the QuikEval™ Demo Board
Connector (P5) and the :adi:`DC1613A`-Compatible Demo Board Connector (P6).

Similarly, the table below lists the default Raspberry Pi GPIO pin assignments
for the P4 pins and their corresponding functions.

.. list-table::
   :header-rows: 1

   * - I²C Pmod Connector #2 (P4) Pinout
     -
     -
   * - **Pin Numbers**
     - **Default Raspberry Pi Pin Assignment**
     - **Pin Function on the PMD-RPI-INTZ**
   * - 1 & 7
     - Pin 13 (GPIO27)
     - **I²C Pmod #2 INT.** Interrupt Signal from the Pmod device to the
       Raspberry Pi.
   * - 2 & 8
     - Pin 11 (GPIO17)
     - **I²C Pmod #2 RESET.** Reset Signal from the Raspberry Pi to the Pmod
       device.
   * - 3 & 9
     - Pin 5 (I²C SCL)¹
     - **SCL.** I²C Clock from the Raspberry Pi to the Pmod device.
   * - 4 & 10
     - Pin 3 (I²C SDA)¹
     - **SDA.** I²C Data from the Raspberry Pi to the Pmod device.
   * - 5 & 11
     - GND
     - **Ground**
   * - 6 & 12
     - 3V3 Power
     - **I²C Pmod #2 VCC.** Connected to the 3.3V Regulator Output of the
       Raspberry Pi.

¹IO pins shared with the I2C Pmod Connector #1 (P3), the QuikEval™ Demo Board
Connector (P5) and the :adi:`DC1613A`-Compatible Demo Board Connector (P6).

.. note::

   **Connecting Hardware Designed for Digilent I²C Pmod Interface Specification
   Ver. 1.0.0:**

   Version 1.0.0 of the Digilent Pmod Interface Specification required 2×4
   headers to be used for I²C devices; Pmod boards that follow this old standard
   should be connected to either P3 or P4 as shown below:

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-i2c-pmod-2x4.png
      :width: 250px

QuikEval™ Demo Board Connector and SPI/I²C Switch (P5 and SW1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QuikEval™ demonstration boards should be connected to the 14-pin shrouded header
through a :adi:`CA2440` ribbon cable (included with each demo board). Each
header pin is connected to a Raspberry Pi GPIO pin through the 40 pin connector
(P9).

The table below lists the default Raspberry Pi GPIO pin assignments for the P5
pins and their corresponding functions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-quikeval-connector.png
   :width: 250px

.. list-table::
   :header-rows: 1

   * - QuikEval™ Demo Board Connector (P5) Pinout
     -
     -
   * - **Pin Number**
     - **Default Raspberry Pi Pin Assignment**
     - **Pin Function on the PMD-RPI-INTZ**
   * - 1
     - 5V Power
     - **QuikEval™ Demo Board Auxiliary Power.** Normally connected to 5V but
       external power can be applied using JP1 and EXT_V+.
   * - 2
     - 3V3 Power
     - **QuikEval™ Demo Board VCCIO.** Connected to the 3.3V Regulator Output of
       the Raspberry Pi.
   * - 3
     - GND
     - **Ground**
   * - 4
     - Pin 23 (SPI0 SCLK)¹ or Pin 5 (I2C1 SCL)²
     - **SCLK (SPI)** or **SCL (I²C).** Select the appropriate clock pin for the
       demo board using SW1.
   * - 5
     - Pin 21 (SPI0 MISO)¹
     - **MISO.** SPI Data from the Pmod device to the Raspberry Pi.
   * - 6
     - Pin 24 (GPIO8)¹
     - **QuikEval™ Demo Board CS.** SPI Chip Select Signal from the Raspberry Pi
       to the demo board.
   * - 7
     - Pin 19 (SPI0 MOSI)¹ or Pin 3 (I2C1 SDA)²
     - **MOSI (SPI)** or **SDA (I²C).** Select the appropriate data pin for the
       demo board using SW1.
   * - 8
     - GND
     - **Ground**
   * - 9
     - Pin 3 (I2C1 SDA)²
     - **QuikEval™ Demo Board EESDA.** I²C Data exchanged between the Raspberry
       Pi and the demo board EEPROM.
   * - 10
     - 5V Power
     - **QuikEval™ Demo Board EEVCC.** Connected to the 5V Input Power of the
       Raspberry Pi. Used to supply power to the demo board EEPROM.
   * - 11
     - Pin 5 (I2C1 SCL)²
     - **QuikEval™ Demo Board EESCL.** I²C Clock from the Raspberry Pi to the
       demo board EEPROM.
   * - 12
     - GND
     - **Ground**
   * - 13
     - GND
     - **Ground**
   * - 14
     - Pin 15 (GPIO22)
     - **QuikEval™ Demo Board GPIO.** Actual function depends on the demo board.

¹IO pins shared with the SPI Pmod Connector #1 (P1) and the SPI Pmod Connector
#2 (P2).

²IO pins shared with the I2C Pmod Connector #1 (P3), the I2C Pmod Connector #2
(P4) and the :adi:`DC1613A`-Compatible Demo Board Connector (P6).

QuikEval™ demonstration boards will use either the SPI or the I²C interface,
depending on the model. Change the setting of the slide switch SW1 accordingly.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-sw1.jpg
   :width: 150px

.. note::

   Some QuikEval™ demonstration boards have the option of being powered via an
   auxiliary power pin (Pin 1 of P6). To accomplish this with the
   :adi:`PMD-RPI-INTZ`, connect an external power supply to EXT_V+ and change
   the setting of the solder jumper JP1.

   .. list-table::
      :header-rows: 1

      * - JP1 Setting
        - EXT_V+ Configuration
      * - Open (Default)
        - Tied to +5 V power supply of the Raspberry Pi
      * - Shorted
        - Can use an external power supply via the EXT_V+ test point

DC1613A-Compatible Demo Board Connector (P6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`DC1613A`-Compatible demonstration boards should be connected to the 12-pin
shrouded header above P4. Each header pin is connected to a Raspberry Pi GPIO
pin through the 40 pin connector (P9).

The table below lists the default Raspberry Pi GPIO pin assignments for the P6
pins and their corresponding functions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-psm-connector.png
   :width: 250px

.. list-table::
   :header-rows: 1

   * - DC1613A-Compatible Demo Board Connector (P6) Pinout
     -
     -
   * - **Pin Number**
     - **Default Raspberry Pi Pin Assignment**
     - **Pin Function on the PMD-RPI-INTZ**
   * - 1
     - 5V Power
     - **DC1613A-Compatible Demo Board AUXP.** Connected to the 5V Input Power
       of the Raspberry Pi. Used to supply power to the demo board EEPROM.
   * - 2
     - Pin 3 (I²C1 SDA)¹
     - **SDA.** PMBus Data from the Raspberry Pi to the demo board. Connected to
       I²C1 SDA.
   * - 3
     - GND
     - **Ground**
   * - 4
     - Pin 5 (I²C1 SCL)¹
     - **SCL.** PMBus Clock from the Raspberry Pi to the demo board. Connected
       to I²C1 SCL.
   * - 5
     - 3V3 Power
     - **DC1613A-Compatible Demo Board LGKPWR.** Connected to the 3.3V Regulator
       Output of the Raspberry Pi.
   * - 6
     - Pin 7 (GPIO4)
     - **ALERTB.** PMBus/SMBus Interrupt Signal from the demo board to the
       Raspberry Pi.
   * - 7
     - Pin 16 (GPIO23)²
     - **DC1613A-Compatible Demo Board GPIO_1.** Actual function depends on the
       demo board.
   * - 8
     - Pin 18 (GPIO24)²
     - **DC1613A-Compatible Demo Board GPIO_2.** Actual function depends on the
       demo board.
   * - 9
     - Pin 36 (GPIO16)²
     - **DC1613A-Compatible Demo Board OUTEN.** Enable Signal from the Raspberry
       Pi to the demo board.
   * - 10
     - GND
     - **Ground**
   * - 11
     - Pin 5 (I²C1 SCL)¹
     - **DC1613A-Compatible Demo Board AUXEESCL.** I²C Clock from the Raspberry
       Pi to the demo board EEPROM.
   * - 12
     - Pin 3 (I²C1 SDA)¹
     - **DC1613A-Compatible Demo Board AUXSDA.** I²C Data exchanged between the
       Raspberry Pi and the demo board EEPROM.

¹IO pins shared with the I2C Pmod Connector #1 (P3), the I2C Pmod Connector #2
(P4) and the QuikEval™ Demo Board Connector (P5).

²IO pins normally disconnected from the Raspberry Pi. Short the appropriate
solder pads between P10 and P11 to enable these pins.

Changing the Raspberry Pi GPIO Assignments
------------------------------------------

The :adi:`PMD-RPI-INTZ` maps the GPIO pins of the Raspberry Pi as shown in the
table below. For easy access to these signals, the evaluation board uses a
stacking header for the Raspberry Pi connector.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-raspberry-pi-connector.jpg
   :width: 500px

.. list-table::
   :header-rows: 1

   * - Raspberry Pi Connector (P9) Pinout
     -
     -
     -
     -
     -
   * - **Pin Function on the PMD-RPI-INTZ**
     - **GPIO Pin**
     - **Pin Number**
     -
     - **GPIO Pin**
     - **Pin Function on the PMD-RPI-INTZ**
   * - 3.3V Power
     - 3V3 Power
     - 1
     - 2
     - 5V Power
     - 5V Power
   * - I²C SDA
     - GPIO 2
     - 3
     - 4
     - 5V Power
     - 5V Power
   * - I²C SCL
     - GPIO 3
     - 5
     - 6
     - Ground
     - Ground
   * - PMBus/SMBus ALERTB
     - GPIO 4
     - 7
     - 8
     - GPIO 14
     - No connection
   * - Ground
     - Ground
     - 9
     - 10
     - GPIO 15
     - No connection
   * - I²C Pmod #2 RESET
     - GPIO 17
     - 11
     - 12
     - GPIO 18
     - SPI Pmod #1 CS3
   * - I²C Pmod #2 INT
     - GPIO 27
     - 13
     - 14
     - Ground
     - Ground
   * - QuikEval™ Demo Board GPIO
     - GPIO 22
     - 15
     - 16
     - GPIO 23
     - DC1613A-Compatible Demo Board GPIO_1
   * - 3.3V Supply Voltage
     - 3V3 Power
     - 17
     - 18
     - GPIO 24
     - DC1613A-Compatible Demo Board GPIO_2
   * - SPI MOSI
     - GPIO 10
     - 19
     - 20
     - Ground
     - Ground
   * - SPI MISO
     - GPIO 9
     - 21
     - 22
     - GPIO 25
     - SPI Pmod #2 INT
   * - SPI SCLK
     - GPIO 11
     - 23
     - 24
     - GPIO 8
     - SPI Pmod #1 CS1 & QuikEval™ Demo Board CS
   * - Ground
     - Ground
     - 25
     - 26
     - GPIO 7
     - SPI Pmod #2 CS1
   * - ID EEPROM SDA
     - GPIO 0
     - 27
     - 28
     - GPIO 1
     - ID EEPROM SCL
   * - SPI Pmod #2 CS2
     - GPIO 5
     - 29
     - 30
     - Ground
     - Ground
   * - SPI Pmod #2 CS3
     - GPIO 6
     - 31
     - 32
     - GPIO 12
     - SPI Pmod #2 RESET
   * - I²C Pmod #1 RESET
     - GPIO 13
     - 33
     - 34
     - Ground
     - Ground
   * - SPI Pmod #1 INT
     - GPIO 19
     - 35
     - 36
     - GPIO 16
     - DC1613A-Compatible Demo Board OUTEN
   * - I²C Pmod #1 INT
     - GPIO 26
     - 37
     - 38
     - GPIO 20
     - SPI Pmod #1 CS2
   * - Ground
     - Ground
     - 39
     - 40
     - GPIO 21
     - SPI Pmod #1 RESET

The adapter board is designed so that most of these IO signals pass through the
rows of test points and solder jumpers at the center. This way, if a different
set of GPIO pin assignments is needed (or desired), the default connections can
be changed by simply removing the appropriate solder jumper(s) and then placing
a wire between the test points of interest.

Refer to below pictures and tables for the signal names available on each test
point. Raspberry Pi GPIO pins are connected to P8 and P10; PMD-RPI-INTZ Pmod and
demo board pins are connected to P7 and P11.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-gpio-jumpers.jpg
   :width: 400px

.. list-table::
   :header-rows: 1

   * - **P8 Pin Number**
     - **Raspberry Pi GPIO**
     - **Jumper**
     - **PMD-RPI-INTZ Signal**
     - **P7 Pin Number**
   * - 1
     - GPIO 4
     - JP2
     - PMBus/SMBus ALERTB
     - 1
   * - 2
     - GPIO 17
     - JP3
     - I²C Pmod #2 RESET
     - 2
   * - 3
     - GPIO 27
     - JP4
     - I²C Pmod #2 INT
     - 3
   * - 4
     - GPIO 22
     - JP5
     - QuikEval™ Demo Board GPIO
     - 4
   * - 5
     - GPIO 10
     - JP6
     - SPI MOSI
     - 5
   * - 6
     - GPIO 9
     - JP7
     - SPI MISO
     - 6
   * - 7
     - GPIO 11
     - JP8
     - SPI SCLK
     - 7
   * - 8
     - GPIO 5
     - JP9
     - SPI Pmod #2 CS2
     - 8
   * - 9
     - GPIO 6
     - JP10
     - SPI Pmod #2 CS3
     - 9
   * - 10
     - GPIO 13
     - JP11
     - I²C Pmod #1 RESET
     - 10
   * - 11
     - GPIO 19
     - JP12
     - SPI Pmod #1 INT
     - 11
   * - 12
     - GPIO 26
     - JP13
     - I²C Pmod #1 INT
     - 12

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pmd-rpi-intz/pmd-rpi-intz-gpio-jumpers-2.jpg
   :width: 400px

.. list-table::
   :header-rows: 1

   * - **P10 Pin Number**
     - **Raspberry Pi GPIO**
     - **Jumper**
     - **PMD-RPI-INTZ Signal**
     - **P11 Pin Number**
   * - 1
     - GPIO 14
     - JP14
     - No connection
     - 1
   * - 2
     - GPIO 15
     - JP15
     - No connection
     - 2
   * - 3
     - GPIO 18
     - JP16
     - SPI Pmod #1 CS3
     - 3
   * - 4
     - GPIO 23
     - JP17
     - DC1613A-Compatible Demo Board GPIO_1
     - 4
   * - 5
     - GPIO 24
     - JP18
     - DC1613A-Compatible Demo Board GPIO_2
     - 5
   * - 6
     - GPIO 25
     - JP19
     - SPI Pmod #2 INT
     - 6
   * - 7
     - GPIO 8
     - JP20
     - SPI Pmod #1 CS1 & QuikEval™ Demo Board CS
     - 7
   * - 8
     - GPIO 7
     - JP21
     - SPI Pmod #2 CS1
     - 8
   * - 9
     - GPIO 12
     - JP22
     - SPI Pmod #2 RESET
     - 9
   * - 10
     - GPIO 16
     - JP23
     - DC1613A-Compatible Demo Board OUTEN
     - 10
   * - 11
     - GPIO 20
     - JP24
     - SPI Pmod #1 CS2
     - 11
   * - 12
     - GPIO 21
     - JP25
     - SPI Pmod #1 RESET
     - 12

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`PMD-RPI-INTZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/pmd-rpi-intz-designsupport.zip>`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you register your hardware.
   :reg:`Register <PMD-RPI-INTZ?&v=Rev D>` to receive all these great benefits
   and more!

// End of document //
