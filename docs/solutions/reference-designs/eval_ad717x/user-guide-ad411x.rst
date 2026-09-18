.. _ad411x-user-guide:

EVAL-AD411x User Guide
===============================================================================

The AD411x family evaluation boards are full-featured boards for evaluating
all the features of AD411x devices. These boards include voltage references,
power regulation, and data isolation, and connect to a PC via the
:adi:`SDP-K1` controller board (Arduino headers) or the
:adi:`SDP-B <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/SDP-B.html>` system demonstration platform. The SDP-B board
provides the USB connection to a PC and can supply power to the evaluation
board from the PC USB port.

Full specifications for each device are available in the respective product
data sheet, which should be consulted when working with the evaluation board.

Features
-------------------------------------------------------------------------------

- Full-featured evaluation board for the AD411x family
- PC control in conjunction with the :adi:`SDP-K1` or :adi:`SDP-B <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/SDP-B.html>`
- Standalone capability

Equipment Needed
-------------------------------------------------------------------------------

- AD411x evaluation board (see :ref:`prerequisites`)
- :adi:`SDP-K1` controller board or :adi:`SDP-B <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/SDP-B.html>`
- DC signal source
- USB cable
- PC with USB 2.0 port

Device Description
-------------------------------------------------------------------------------

The AD411x family comprises highly accurate, high resolution, multiplexed
Σ-Δ ADCs designed for high-impedance (≥10 MΩ) bipolar voltage inputs.
Depending on the specific device, these ADCs support a combination of
high-voltage single-ended or differential inputs (±10 V range) and lower-range
direct ADC inputs. All channels include on-board overvoltage and overcurrent
protection. The maximum channel-to-channel scan rate is 12.4 kSPS (80 µs) for
fully settled data. Output data rates range from 1.25 SPS to 62.5 kSPS. All
devices include integrated analog reference buffers, an integrated precision
2.5 V reference, and an integrated oscillator.

Evaluation boards in this family use an isoPower® digital isolator to isolate
power and data lines up to 2.5 kV rms.

Setup Procedures
-------------------------------------------------------------------------------

After following the software installation instructions, set up the evaluation
board and SDP board as follows.

.. note::

   Software and drivers must be installed before connecting the evaluation
   board and SDP board to the USB port of the PC to ensure that the PC
   correctly recognizes the evaluation system.

#. Connect the SDP board to the evaluation board using the appropriate
   connector. Fasten the two boards together firmly using the plastic screw
   and washer set included in the kit.
#. If using the SDP-K1, the Arduino headers can also be used to connect to
   the board.
#. Configure the power supply link to select USB power (see the Hardware Link
   Options section of your specific board's user manual).
#. Connect the SDP board to the PC using the USB cable.

Hardware Link Options
-------------------------------------------------------------------------------

.. note::

   Link options vary between boards. The table below shows a representative
   example for one board in this family. Refer to the user manual of your
   specific evaluation board for the correct link configuration.

.. list-table::
   :header-rows: 1

   * - Link
     - Default
     - Description
   * - LK1
     - Inserted
     - Connects the on-board external reference to the AD411x. Remove if
       using a different single-ended external reference.
   * - LK2
     - Inserted
     - Connects VINCOM to GND_ISO. Typical for single-ended measurement.
       Remove to set a custom common analog input for single-ended channels.
   * - LK3
     - B (USB)
     - Selects the power supply source. Position A: powered from the
       external DC supply connector. Position B: powered from USB through
       the SDP or Arduino connector.
   * - LK4 to LK6
     - STD
     - Selects which Arduino SPI lines to connect. STD: standard Arduino
       headers. ALT: alternate IFCSP header.
   * - LK9, LK10
     - Inserted
     - Connects high-voltage inputs to Zener diode protection. Remove to
       evaluate voltage inputs without external protection components.
   * - LK11, LK12
     - Removed
     - Bypasses series resistors on high-voltage inputs. Insert to remove
       the series resistor from the input path.
   * - LK13, LK14
     - Inserted
     - Connects direct ADC inputs to Zener diode protection. Remove to
       evaluate voltage inputs without external protection components.
   * - LK15, LK16
     - Removed
     - Bypasses series resistors on direct ADC inputs. Insert to remove
       the series resistor from the input path.
   * - J14
     - CS0
     - Selects which GPIO to use on the Arduino header as CS, to enable
       stacking boards.

On-Board Connectors
-------------------------------------------------------------------------------

.. note::

   Connector assignments vary between boards. The table below shows a
   representative example for one board in this family. Refer to the user
   manual of your specific evaluation board for the correct connector
   assignments.

.. list-table::
   :header-rows: 1

   * - Connector
     - Function
     - Type
   * - J1
     - Connects to GPIO pins of the AD411x
     - 4-pin header, 2.54mm pitch
   * - P1, P2, P3
     - High-voltage inputs to AD411x
     - Connector, header, 90°, 5 position, 3.81 mm
   * - P4
     - Direct ADC inputs to AD411x
     - Connector, header, 90°, 5 position, 3.81 mm
   * - J4
     - External supply voltage (optional)
     - Power socket block, 3-way, 3.81 mm pitch
   * - J7
     - Arduino Headers (Power)
     - 8 Position Receptacle Connector, 2.54mm pitch
   * - J8
     - Arduino Header (Analog)
     - 6 Position Receptacle Connector, 2.54mm pitch
   * - J9
     - Arduino Header (Digital 1)
     - 10 Position Receptacle Connector, 2.54mm pitch
   * - J10
     - Arduino Header (Digital 0)
     - 8 Position Receptacle Connector, 2.54mm pitch
   * - J11
     - Arduino Header (IFCSP)
     - 6 Position, 2 row, Receptacle Connector, 2.54mm pitch
   * - J12
     - SDP Connector
     - 120-way connector, 0.6 mm pitch
   * - J13
     - Earth for electromagnetic discharge (ESD testing)
     - Not applicable

Power Supplies
-------------------------------------------------------------------------------

By default, the board is powered from USB through the SDP or Arduino
connector. An optional external DC supply can also be used; refer to the
hardware link options in your specific board's user manual for configuration.

Serial Interface
-------------------------------------------------------------------------------

The evaluation board uses a 4-wire SPI interface: CS, SCLK, DIN, and
DOUT/RDY. It connects to any microcontroller board using the Arduino standard
headers.

To operate the evaluation board in standalone mode, disconnect any connected
SDP board and use the appropriate header to access SPI signals directly.

For an introduction to the SPI interface, see
:adi:`Introduction to SPI Interface <en/analog-dialogue/articles/introduction-to-spi-interface.html>`.

Analog Inputs
-------------------------------------------------------------------------------

AD411x evaluation boards provide high-voltage analog input connectors for
single-ended or differential measurements (±10 V range), plus additional
connectors for lower-range direct ADC inputs.

To use a custom common voltage for single-ended measurement, refer to your
board's user manual for the appropriate link configuration.

Reference Options
-------------------------------------------------------------------------------

The following reference sources are available:

- **Default:** on-board external 2.5V reference (connected via a link; see
  your board's user manual)
- Internal 2.5V reference (on-chip)
- External reference: disconnect the on-board reference link and connect an
  external single-ended reference

To select the reference source in software, use the setup configuration
controls in the evaluation software.

Schematic, PCB Layout, Bill of Materials
-------------------------------------------------------------------------------

Refer to the product page of your specific evaluation board on
`analog.com <https://www.analog.com>`_ to download the design files.
