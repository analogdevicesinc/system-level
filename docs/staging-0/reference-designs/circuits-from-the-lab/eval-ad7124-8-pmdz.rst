.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/eval-ad7124-8-pmdz

.. _circuits-from-the-lab eval-ad7124-8-pmdz:

EVAL-AD7124-8-PMDZ Overview
===========================

The :adi:`EVAL-AD7124-8-PMDZ` is a minimalist 8-channel, low noise, low power,
24-Bit, sigma-delta ADC with PGA and reference, SPI Pmod board for the
:adi:`AD7124-8`. This module is designed as a low-cost alternative to the
fully-featured :adi:`AD7124-8` evaluation board and has no extra signal
conditioning for the ADC.

All pins of the :adi:`AD7124-8` are exposed, which makes the
:adi:`EVAL-AD7124-8-PMDZ` very flexible and easy to use.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad7124-8-pmdz_top.jpg
   :width: 600px

Functional block diagram
------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad7124-8_functional_block_diagram.png

About the AD7124-8
------------------

The :adi:`AD7124-8` is a low power, low noise, completely integrated analog
front end for high precision measurement applications. The device contains a low
noise, 24-bit Σ-Δ analog-to-digital converter (ADC), and can be configured to
have 8 differential inputs or 15 single-ended or pseudo-differential inputs. The
on-chip programmable gain amplifier (PGA) allows small amplitude signals to be
interfaced directly to the ADC.

One of the major advantages of the :adi:`AD7124-8` is that it gives the user the
flexibility to employ one of three integrated power modes. The current
consumption, range of output data rates, and RMS noise can be tailored with the
power mode selected. The device also offers a multitude of filter options,
ensuring that the user has the highest degree of flexibility.

The :adi:`AD7124-8` establishes the highest degree of signal chain integration.
The device includes a precision, low noise, low drift internal bandgap
reference, and accepts an external differential reference, which can be
internally buffered. Other key integrated features include programmable low
drift excitation current sources, burnout detection currents, and a bias voltage
generator, which sets the common-mode voltage of a channel to AVDD/2. The
low-side power switch enables the user to power down bridge sensors between
conversions, ensuring the absolute minimal power consumption of the system. The
device also allows the user the option of operating with either an internal
clock or an external clock.

The integrated channel sequencer allows several channels to be enabled
simultaneously, and the :adi:`AD7124-8` sequentially converts on each enabled
channel, simplifying communication with the device. As many as 16 channels can
be enabled at any time, where a channel is defined as an analog input or a
diagnostic function such as a power supply check or a reference check. This
unique feature allows diagnostics to be interleaved with conversions. The
:adi:`AD7124-8` also supports per channel configuration. The device allows eight
configurations or setups. Each configuration consists of PGA gain, filter type,
output data rate, buffering, and reference source. The user can assign any of
these setups on a channel-by-channel basis.

The :adi:`AD7124-8` also has extensive diagnostic functionality integrated as
part of its comprehensive feature set. These diagnostics include a cyclic
redundancy check (CRC) on the SPI data, signal chain checks, and serial
interface checks, which lead to a more robust solution. These diagnostics reduce
the need for external components to implement diagnostics, resulting in reduced
board space needs, reduced design cycle times and cost savings. The failure
modes effects and diagnostic analysis (FMEDA) of a typical application has shown
a safe failure fraction (SFF) greater than 90% according to IEC 61508.

The device operates with a single analog power supply from 2.7 V to 3.6 V or a
dual 1.8 V power supply. The digital supply has a range of 1.65 V to 3.6 V,
eliminating the need for external logic level shifters.

Connectors and Configuration
----------------------------

By default, the :adi:`EVAL-AD7124-8-PMDZ` is configured to be controlled and
power from the PMOD connector using standard connections. So no additional
configuration is required, unless you want to customize it.

AD7124-8 Inputs/Outputs Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All the analog and digital input/output pins available on the
:adi:`EVAL-AD7124-8-PMDZ` are brought out to two (2) separate 16 row 0.1`` gold
plated through holes.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad7124-8-pmdz_top.jpg
   :width: 700px

.. list-table::
   :header-rows: 1

   * - Connector P2
     -
     - Connector P3
     -
   * - Description
     - Pin(s)
     - Description
     - Pin(s)
   * - GND
     - 1, 3, 5, 16
     - GND
     - 1, 14, 16
   * - AVSS
     - 2
     - REFIN1(-)
     - 2
   * - IOVDD
     - 4
     - AIN8
     - 3
   * - CLK
     - 6
     - AIN9
     - 4
   * - AIN0
     - 7
     - AIN10
     - 5
   * - AIN1
     - 8
     - AIN11
     - 6
   * - AIN2
     - 9
     - AIN12
     - 7
   * - AIN3
     - 10
     - AIN13
     - 8
   * - AIN4
     - 11
     - AIN14
     - 9
   * - AIN5
     - 12
     - AIN15
     - 10
   * - AIN6
     - 13
     - REFOUT
     - 11
   * - AIN7
     - 14
     - SYNC
     - 12
   * - REFIN1(+)
     - 15
     - PSW
     - 13
   * -
     -
     - AVDD
     - 15

.. tip::

   Note: Not all pins require inputs. The following pins are exposed and can be
   used if necessary if they are first disconnected from their default onboard
   connection if that connection exists. (AVSS, AVDD, REFIN1(+), REFIN1(-), CLK,
   REFOUT, SYNC, PSW). Please refer to the datasheet to learn more about their
   function

Digital Communications
~~~~~~~~~~~~~~~~~~~~~~

The Digital communication on the EVAL-AD7124-8-PMDZ is accomplished using a
standard expanded SPI PMOD port.

.. list-table::
   :header-rows: 1

   * - Connector P1
     -
   * - Description
     - Pin(s)
   * - CS
     - 1
   * - SDIN
     - 2
   * - SDO
     - 3
   * - SCLK
     - 4
   * - GND
     - 5, 11
   * - IOVDD
     - 6, 12
   * - SDO
     - 7
   * - Open or SDO
     - 8
   * - Open or SDO
     - 9
   * - Open or SDO
     - 10

Solder Jumpers
~~~~~~~~~~~~~~

Eight solder jumpers are available at the bottom of the board, if you want to
change the operating modes. See the schematic for more details.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad7124-8-pmdz_bottom.jpg
   :width: 700px

.. list-table::
   :header-rows: 1

   * - Description and default connection
     - Solder Jumper
     - Default Position
   * - ADC REFIN1(-) connection (connect GND and P3 pin 2)
     - P4
     - Shorted
   * - ADC REFIN1(+) connection (connect ADC REFOUT and P2 pin 15)
     - P7
     - Shorted
   * - ADC AVDD connection (connect ADC IOVDD and P3 pin 15)
     - P5
     - Shorted
   * - ADC AVSS connection (connect GND and P2 pin 2)
     - P6
     - Shorted
   * - ADC SDO connection (connected to P1 pin 7, default)
     - P8
     - Shorted
   * - ADC SDO connection (connected to P1 pin 8)
     - P9
     - Open
   * - ADC SDO connection (connected to P1 pin 9)
     - P10
     - Open
   * - ADC SDO connection (connected to P1 pin 10)
     - P11
     - Open

Test Points
~~~~~~~~~~~

Also, four test points are available to probe the SPI interface.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`EVAL-AD7124-8-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7124-8-pmdz-designsupport.zip>`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information and Useful Links
---------------------------------------

- :adi:`AD7124-8 Product Page <AD7124-8>`

Reference Demos & Software
--------------------------

- :dokuwiki:`ADICUP3029 + EVAL-AD7124-8-PMDZ Demo </resources/eval/user-guides/eval-adicup3029/reference_designs/demo_ad7124-8>`
- :dokuwiki:`AD7124 IIO Sigma-Delta ADC Linux Driver </resources/tools-software/linux-drivers/iio-adc/ad7124>`
- :dokuwiki:`AD7124 No-OS Software </resources/tools-software/uc-drivers/ad7124>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you register your hardware.
   :reg:`Register <EVAL-AD7124-8-PMDZ?&v=RevB>` to receive all these great
   benefits and more!


