.. _eval-adaq7980-sdz user-guide:

User guide
===============================================================================

The complete user guide of the evaluation board can be found at
:adi:`EVAL-ADAQ7980 <EVAL-ADAQ7980>`.

Hardware guide
-------------------------------------------------------------------------------

General Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Board Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-ADAQ7980-SDZ <EVAL-ADAQ7980>` Shield (**ADAQ7980 Board**) is a compact evaluation
board designed to interface with the ZedBoard via the FMC connector. The board
provides access to all the key features of the :adi:`ADAQ7980`/:adi:`ADAQ7988`
16-bit SAR ADC subsystems.

Power Supply
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-ADAQ7980-SDZ <EVAL-ADAQ7980>` is powered through the FMC connector from the
ZedBoard. The board requires the following supply voltages:

- VDD (Analog supply)
- VDRIVE (Digital I/O supply)
- VCC (Internal regulator supply)
- VREF (Reference voltage supply)

All necessary power supplies are provided by the ZedBoard through the FMC
connector. Ensure the ZedBoard is properly powered before connecting the
evaluation board.

Analog Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The main analog input on the :adi:`EVAL-ADAQ7980-SDZ <EVAL-ADAQ7980>` is available through an
SMA connector on the board. The input can accept single-ended or differential
signals depending on the configuration. The integrated ADC driver provides
signal conditioning and buffering for optimal ADC performance.

The input voltage range is configurable through the ADC driver feedback loop,
allowing for gain and common-mode adjustments to match your application
requirements.

LED Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`EVAL-ADAQ7980-SDZ <EVAL-ADAQ7980>` board includes LED indicators for:

- Power status
- Communication activity
- Conversion ready signals

FMC Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The board connects to the ZedBoard via the FMC (FPGA Mezzanine Card) connector.
The FMC interface provides:

- SPI communication signals (SCLK, MOSI, MISO, CS)
- Control signals (CNV, BUSY)
- Power supply connections
- Ground connections

Ensure proper alignment and secure connection of the FMC connector before
powering on the system.

Signal Chain Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADAQ7980`/:adi:`ADAQ7988` integrate four key signal chain blocks:

#. **ADC Driver**: High bandwidth, high input impedance driver with configurable
   gain and common-mode adjustment
#. **Reference Buffer**: Low power, stable voltage reference buffer
#. **SAR ADC**: 16-bit, high accuracy analog-to-digital converter
#. **Power Management**: Efficient power management circuitry

This integration simplifies the design by incorporating critical passive
components and eliminating many traditional signal chain challenges.

Configuration Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sampling Rate Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The sampling rate is configured in the HDL design through the integrated pulse
generator. See the :ref:`eval-adaq7980-sdz quickstart zedboard` guide for
details on configuring the sampling rate in the HDL project.

The default sampling rate is 1 MSPS, but can be adjusted to meet your
application requirements up to the maximum specified in the datasheet.

SPI Interface Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :adi:`ADAQ7980`/:adi:`ADAQ7988` use a SPI-compatible serial interface with
the following features:

- Daisy-chain capability for multiple devices
- Optional busy indicator
- Compatible with 1.8 V, 2.5 V, 3 V, or 5 V logic levels

The SPI interface is configured through the HDL design and no-OS driver. Default
settings provide optimal performance for most applications.

Operating Tips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For best performance:

#. Ensure stable power supplies with adequate decoupling
#. Use proper grounding techniques to minimize noise
#. Keep analog input signal paths short and well-shielded
#. Allow adequate warm-up time before critical measurements
#. Follow the recommended sampling rate limits in the datasheet

Hardware Setup Checklist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before beginning evaluation:

- [ ] ZedBoard is available and functional
- [ ] EVAL-ADAQ7980-SDZ board is properly connected to FMC connector
- [ ] Power supply connections are secure
- [ ] Signal source is connected to analog input SMA
- [ ] USB cable is connected for UART and JTAG programming

References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For detailed hardware specifications, schematics, and design files, refer to:

- :adi:`ADAQ7980 Datasheet <ADAQ7980>`
- :adi:`ADAQ7988 Datasheet <ADAQ7988>`
- :adi:`EVAL-ADAQ7980 Evaluation Board <EVAL-ADAQ7980>`
