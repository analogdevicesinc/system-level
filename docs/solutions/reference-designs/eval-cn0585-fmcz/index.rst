.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0585

.. _eval-cn0585-fmcz:

EVAL-CN0585-FMCZ
==================

.. toctree::
   :hidden:

   power_tree

Quad Channel, Low Latency, Data Acquisition and Signal Generation Module.

The :adi:`EVAL-CN0585-FMCZ <CN0585>` Low Latency Development Kit (LLDK) board
is a development board consisting of 4 x 16-bit ADC channels and 4 x 16-bit DAC
channels that are interfaced with an FPGA through the FMC Low Pin Count (LPC)
Connector. Current revision of :adi:`EVAL-CN0585-FMCZ <CN0585>` is Rev B.
:adi:`EVAL-CN0585-FMCZ <CN0585>`, :adi:`EVAL-CN0584-EBZ <CN0584>` and ZedBoard
are connected together to build a development system setup as shown in Figure 1.

.. figure:: images/setup_cn0585_diagram.png

   CN0585 Development Platform Setup

.. note::

   The current LLDK system setup includes the CN0585 revB board, which has a USB-C power connector.

The :adi:`EVAL-CN0585-FMCZ <CN0585>` board provides a complete data acquisition
and signal generation platform with onboard power rails, voltage monitoring,
logic level translation, general purpose I/O, I2C, SPI, and an analog front
end (AFE) board connector.

The key performance benefit of the :adi:`EVAL-CN0585-FMCZ <CN0585>` is the
ability to perform a complete capture and conversion of precision analog input
data in <70ns with the ADC module and generate a settled full-scale analog
output in <200ns from initial data written to the DAC.

.. grid::
   :widths: 50 50

   .. figure:: images/eval-cn0585-fmcz_top-web.jpg
      :width: 400 px

      EVAL-CN0585-FMCZ Board (Top)

   .. figure:: images/eval-cn0585-fmcz_bottom-web.jpg
      :width: 400 px

      EVAL-CN0585-FMCZ Board (Bottom)

.. figure:: images/cn0585.png

   EVAL-CN0585-FMCZ Simplified Block Diagram

Connections and Configurations
------------------------------

Receive Channel
~~~~~~~~~~~~~~~

The :adi:`EVAL-CN0585-FMCZ <CN0585>` board has four :adi:`ADAQ23876`
16-Bit 15 MSPS Data Acquisition µModules to capture analog data
from the AFE board connector. The Data Acquisition µModules are
configured to simultaneously sample the four input channels. The data acquired
by the :adi:`ADAQ23876` is routed to the FPGA through the FMC LPC
connector using a serial low voltage differential signaling (LVDS) digital
interface in a two-lane output mode. The :adi:`ADAQ23876` has pin
configurable input voltage span with configurable gain/attenuation options:
0.37, 0.73, 0.87, 1.38, and 2.25, providing input voltage span ranges of ±10V,
±5V, ±4.096V, ±2.5V, and ±1.5V. The gain/attenuation functions are
accessible through the AFE board connector pins. As an example the
:adi:`EVAL-CN0584-EBZ <CN0584>` is available for hardware in loop (HIL) applications.

Transmit Channel
~~~~~~~~~~~~~~~~

The :adi:`EVAL-CN0585-FMCZ <CN0585>` board has two :adi:`AD3552R`
16-bit 33 MUPS DACs that provide four analog output signals to the AFE board
connector. Data is transferred to the :adi:`AD3552R` DAC from the
FPGA through the FMC LPC connector using a Quad-SPI dual data rate interface.

The :adi:`AD3552R` has a pin-configurable output voltage span that
can be configured through the AFE board connector. Multiple output span ranges
can be configured, such as 0V to 2.5V, 0V to 5V, −5V to +5V, −10V to +10V,
and custom intermediate ranges with full 16-bit resolution.

Voltage Reference
~~~~~~~~~~~~~~~~~

The default ADC reference configuration uses the internal 2.048 V, ±0.1%
accurate, 20 ppm/°C max voltage reference. For more stringent use cases where
the accuracy and temperature drift is an issue, an external
:adi:`LTC6655` 2.048V, ±0.025% accurate, 2 ppm/°C max voltage
reference can be used.

The default DAC reference configuration uses the internal 2.5V, ±0.3% accurate,
10 ppm/°C max voltage reference. For more stringent use cases where the accuracy
and temperature drift is an issue, an external :adi:`ADR4525` 2.5V,
±0.02% accurate, 2 ppm/°C max voltage reference can be used.

.. table:: Voltage Reference Settings

   +----------+-----------------+
   | VREF     | Jumper Settings |
   +----------+-----------------+
   | ADC_VREF | Short P5        |
   +----------+-----------------+
   | DAC_VREF | Short P4        |
   +----------+-----------------+

Voltage Monitoring
~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-CN0585-FMCZ <CN0585>` board provides voltage monitoring
capability for the power supply rails. The circuit consists of an
:adi:`AD7291` 8-Channel, I2C, 12-Bit SAR ADC, and resistive dividers.
Each power rail is connected to AD7291 by resistive dividers as shown in Figure 5.

.. figure:: images/cn0585_voltage_monitoring.png

   Power Supply Voltage Monitor Circuit

The negative power supply rails are biased positive with a buffered 2.5V
reference supplied by the :adi:`AD7291`.

Calculating the supply voltage from the positive voltage rails can be
accomplished using the following equation:

.. math::

   V_{\text{RAIL-POS}} = \text{Scale Factor} \times \text{IIO Measured Voltage}

Calculating the supply voltage from the negative voltage rails can be
accomplished using the following equation:

.. math::

   V_{\text{RAIL-NEG}} = \text{Scale Factor} \times (2.5 - \text{IIO Measured Voltage}) + 2.5

.. table:: Voltage Scaling

   +--------------+--------------+--------------+--------------+--------------+
   | Monitored    | CN0585 Power | Scale Factor | IIO Measured | Actual       |
   | Rail         | Rail         |              | Voltage      | Voltage      |
   +==============+==============+==============+==============+==============+
   | voltage0     | +12 V        | 5.3          | 2.26 V       | 11.98 V      |
   |              | (AD8065 DAC  |              |              |              |
   |              | amp)         |              |              |              |
   +--------------+--------------+--------------+--------------+--------------+
   | voltage1     | -12 V        | -7.81        | 0.65 V       | -11.95 V     |
   |              | (AD8065 DAC  |              |              |              |
   |              | amp)         |              |              |              |
   +--------------+--------------+--------------+--------------+--------------+
   | voltage2     | +5 V         | 2.43         | 2.06 V       | 5.00 V       |
   |              | (ADAQ23876   |              |              |              |
   |              | amp)         |              |              |              |
   +--------------+--------------+--------------+--------------+--------------+
   | voltage3     | -5 V         | -4.32        | 0.76 V       | -5.02 V      |
   |              | (ADAQ23876   |              |              |              |
   |              | amp)         |              |              |              |
   +--------------+--------------+--------------+--------------+--------------+
   | voltage4     | +5 V (DAC)   | 2.43         | 2.06 V       | 5.00 V       |
   +--------------+--------------+--------------+--------------+--------------+
   | voltage5     | +5 V (DAC)   | 2.43         | 2.06 V       | 5.00 V       |
   +--------------+--------------+--------------+--------------+--------------+
   | voltage6     | +2.5 V       | 1.11         | 2.25 V       | 2.50 V       |
   |              | (digital)    |              |              |              |
   +--------------+--------------+--------------+--------------+--------------+
   | voltage7     | +1.8 V       | 1            | 1.80 V       | 1.80 V       |
   |              | (digital)    |              |              |              |
   +--------------+--------------+--------------+--------------+--------------+

The default I2C address of the :adi:`AD7291` is 0x20. Resistors R13,
R14, R17, and R18 can be used to select alternate addressing.

Logic Level Translators
~~~~~~~~~~~~~~~~~~~~~~~

Several logic-level translators are used on the board to interface with the FMC
connector signals and the various logic levels used on the board. The FMC
connector signal levels are driven by the VIO voltage supplied from the FPGA
board.

GPIO
^^^^

A GPIO interface is provided by a MAX7301ATL+ I/O Expander connected to the SPI
interface on the SPIO_CSB0 chip select interface. The GPIO outputs are
controlled by writing to the MAX7301ATL+ via the SPI interface provided on the
FMC connector. Four GPIO signals are utilized on the
:adi:`EVAL-CN0585-FMCZ <CN0585>` board to control the power-down interface of
the ADAQ23875 Data Acquisition µModules. Eight GPIO signals are level-shifted
and provided to the AFE board connector for control signals on the AFE board.

I2C
^^^

The I2C interface is provided from the FPGA FMC connector and is made available
to the :adi:`EVAL-CN0585-FMCZ <CN0585>` board and the user via the AFE board
connector. On the :adi:`EVAL-CN0585-FMCZ <CN0585>` board the I2C interface is
used to communicate with an EEPROM that is required by the Vita 57.1 Standard
for board identification and IO characteristics, and the AD7291 voltage
monitoring ADC.

SPI
^^^

The :adi:`EVAL-CN0585-FMCZ <CN0585>` board provides an SPI interface for the
user on SPI0 from the FMC connector. Communication with the MAX7301ATL+ GPIO
expander is enabled by chip select SPIO_CSB0. A second chip select, SPI_CSB1
originates from the FMC interface and connects to the AFE board connector so
that the user can attach a custom secondary SPI device to the AFE board. This
second SPI0_CSB1 is not initialized in the Linux device tree, as the
initialization requires additional information such as SPI transmission mode,
phase, and polarity. Two Quad-SPI interfaces (DAC0/1 and DAC2/3) are provided by
the FMC interface to handle communications and data transfer to the four AD3552R
DAC channels.

Application-specific Analog Front-End Connector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AFE connector interface provides six signal connections for each of the four
:adi:`ADAQ23876` Data Acquisition µModules. The six signal
connections allow the user to set the input voltage range of the differential
amplifier input. Configuration resistors, if used, should be placed as close as
possible to the AFE board connector. Please refer to the ADAQ23876 data sheet for
more configuration details.

.. table:: ADAQ23876 Connections for Input Configuration

   +------------+------------------------+--------------+---------------------+---------------+
   | Monitored  | CN0585 Power Rail      | Scale Factor | IIO Measured        | Actual        |
   | Rail       |                        |              | Voltage             | Voltage       |
   +============+========================+==============+=====================+===============+
   | voltage0   | +12 V (AD8065 DAC amp) | 5.3          | 2.26 V              | 11.98 V       |
   +------------+------------------------+--------------+---------------------+---------------+
   | voltage1   | -12 V (AD8065 DAC amp) | -7.81        | 0.65 V              | -11.95 V      |
   +------------+------------------------+--------------+---------------------+---------------+
   | voltage2   | +5 V (ADAQ23876 amp)   | 2.43         | 2.06 V              | 5.00 V        |
   +------------+------------------------+--------------+---------------------+---------------+
   | voltage3   | -5 V (ADAQ23876 amp)   | -4.32        | 0.76 V              | -5.02 V       |
   +------------+------------------------+--------------+---------------------+---------------+
   | voltage4   | +5 V (DAC)             | 2.43         | 2.06 V              | 5.00 V        |
   +------------+------------------------+--------------+---------------------+---------------+
   | voltage5   | +5 V (DAC)             | 2.43         | 2.06 V              | 5.00 V        |
   +------------+------------------------+--------------+---------------------+---------------+
   | voltage6   | +2.5 V (digital)       | 1.11         | 2.25 V              | 2.50 V        |
   +------------+------------------------+--------------+---------------------+---------------+
   | voltage7   | +1.8 V (digital)       | 1            | 1.80 V              | 1.80 V        |
   +------------+------------------------+--------------+---------------------+---------------+

The AFE connector interface provides three signal connections for each of the
four DAC output channels. The three signal connections allow the user to set the
output voltage range of the :adi:`AD3552R` DAC. Configuration
resistors, if used, should be placed as close as possible to the AFE board
connector. The AD3552R uses a current steering DAC architecture with a VREF
voltage of 2.5V. The DAC current is converted to a voltage using an external
TIA. The DAC outputs are observed on signals DAC0, DAC1, DAC2, and DAC3. The
DACx outputs are fed back into the :adi:`AD3552R` gain configuration
pins for each DAC channel. The table below details the configuration connections
for each of the output voltage ranges of each of the DAC output channels. Please
refer to the :adi:`AD3552R` data sheet for more configuration details.

.. table:: AD3552R Connections for Output Configuration

   +-------------------+-----------------------------------------------+------------------------------------------+
   | Input Range       | Input Signal on Pins                          | Feedback Connections                     |
   +===================+===============================================+==========================================+
   | +/- 10V (Default) | ADCx_IN2P, ADCx_IN2N                          | ADCx_OUTP and ADCx_IN1N pins Shorted;    |
   |                   |                                               | ADCx_OUTN and ADCx_IN1P pins Shorted     |
   +-------------------+-----------------------------------------------+------------------------------------------+
   | +/- 5V            | ADCx_IN1P, ADCx_IN1N                          | ADCx_OUTP and ADCx_IN2N pins Shorted;    |
   |                   |                                               | ADCx_OUTN and ADCx_IN2P pins Shorted     |
   +-------------------+-----------------------------------------------+------------------------------------------+
   | +/- 4.096V        | ADCx_IN2P, ADCx_IN2N                          | No Connect                               |
   +-------------------+-----------------------------------------------+------------------------------------------+
   | +/- 2.5V          | ADCx_IN1P, ADCx_IN1N                          | No Connect                               |
   +-------------------+-----------------------------------------------+------------------------------------------+
   | +/- 1.5V          | ADCx_IN1P/ADCx_IN2P Shorted;                  | No Connect                               |
   |                   | ADCx_IN1N/ADCx_IN2N Shorted                   |                                          |
   +-------------------+-----------------------------------------------+------------------------------------------+

The AFE board connector provides an input/output interface to the
:adi:`EVAL-CN0585-FMCZ <CN0585>` board. The interface provides connections to
the analog I/O, ADC/DAC gain settings, GPIO, I2C, SPI, aux power, and four direct
FMC connections to allow system flexibility interfacing with custom AFE designs
that are provided by ADI or can be custom designed by the user. Currently, ADI
provides the :adi:`EVAL-CN0584-EBZ <CN0584>` as an analog front-end board.

.. table:: AD3552R Register Settings

   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       |  Hardware Settings  |         |         |                             | AD3552R       |             |            |
   |       |                     |         |         |                             | Register      | Settings    |            |
   |       |                     |         |         |                             | Address       |             |            |
   +=======+=====================+=========+=========+=============================+===============+=============+============+
   |Channel| Output Span         | VZS (V) | VFS (V) | Feedback Connection         | CH0_CH1       | CHx_GAIN    | CHx_OFFSET |
   |       |                     |         |         |                             | _OUTPUT_Range | _SCALING_N  |            |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   | CH0   | +/- 10V (Default)   | -10.382 | 10.380  | DAC0 to DAC0_RFB0           | 0x100         | 0           | -245       |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | +/- 5V              | -5.165  | 5.166   | DAC0 to DAC0_RFB0_X2        | 0x011         | 0           | -495       |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 10V                 | -0.165  | 10.163  | DAC0 to DAC0_RFB0_X2        | 0x010         | 0           | 495        |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 5V                  | -0.078  | 5.077   | DAC0 to DAC0_RFB0_X1        | 0x001         | 0           | 0          |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 2.5V                | -0.198  | 2.701   | DAC0 to DAC0_RFB0_X1        | 0x000         | 3           | -48        |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   | CH1   | +/- 10V (Default)   | -10.382 | 10.380  | DAC1 to DAC1_RFB1           | 0x100         | 0           | -245       |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | +/- 5V              | -5.165  | 5.166   | DAC1 to DAC1_RFB1_X2        | 0x011         | 0           | -495       |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 10V                 | -0.165  | 10.163  | DAC1 to DAC1_RFB0_X2        | 0x010         | 0           | 495        |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 5V                  | -0.078  | 5.077   | DAC1 to DAC1_RFB1_X1        | 0x001         | 0           | 0          |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 2.5V                | -0.198  | 2.701   | DAC1 to DAC1_RFB1_X1        | 0x000         | 3           | -48        |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   | CH2   | +/- 10V (Default)   | -10.382 | 10.380  | DAC2 to DAC2_RFB0           | 0x100         | 0           | -245       |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | +/- 5V              | -5.165  | 5.166   | DAC2 to DAC2_RFB0_X2        | 0x011         | 0           | -495       |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 10V                 | -0.165  | 10.163  | DAC2 to DAC2_RFB0_X2        | 0x010         | 0           | 495        |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 5V                  | -0.078  | 5.077   | DAC2 to DAC2_RFB0_X1        | 0x001         | 0           | 0          |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 2.5V                | -0.198  | 2.701   | DAC2 to DAC2_RFB0_X1        | 0x000         | 3           | -48        |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   | CH3   | +/- 10V (Default)   | -10.382 | 10.380  | DAC3 to DAC3_RFB1           | 0x100         | 0           | -245       |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | +/- 5V              | -5.165  | 5.166   | DAC3 to DAC3_RFB1_X2        | 0x011         | 0           | -495       |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 10V                 | -0.165  | 10.163  | DAC3 to DAC3_RFB1_X2        | 0x010         | 0           | 495        |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 5V                  | -0.078  | 5.077   | DAC3 to DAC3_RFB1_X1        | 0x001         | 0           | 0          |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+
   |       | 2.5V                | -0.198  | 2.701   | DAC3 to DAC3_RFB1_X1        | 0x000         | 3           | -48        |
   +-------+---------------------+---------+---------+-----------------------------+---------------+-------------+------------+

The AFE board connector on the :adi:`EVAL-CN0585-FMCZ <CN0585>` board is a
Samtec high-density socket connector.

FMC LPC Connector Pinout for LLDK Board (Rev B)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FMC LPC connector routes the data acquired by the ADAQ23876 to FPGA and
transfers the data from FPGA to AD3552R DAC.

.. figure:: images/connector_pinout_revb.png

   FMC LPC Connector Pinout

LED Indicators
~~~~~~~~~~~~~~

Once the board is connected to the host and powered on, the green LED (DS1)
will illuminate to indicate that the board is receiving power and is operating correctly.

Power Supply Considerations and Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Rev. B of the :adi:`EVAL-CN0585-FMCZ <CN0585>` board is powered through the
USB-C connector of the board.

.. important::

   The board can also be powered from the FMC connector by adding resistor R9
   and removing resistor R10, but it is not recommended as the current
   consumption exceeds the FMC standard current limit.

System Setup Using a ZedBoard
-----------------------------

The :adi:`EVAL-CN0585-FMCZ (Rev B) <CN0585>` connected to
:adi:`EVAL-CN0584-EBZ <CN0584>` is fully supported using a ZedBoard.
For description of system setup and functionality using the
:adi:`EVAL-CN0584-EBZ <CN0584>` / :adi:`EVAL-CN0585-FMCZ <CN0585>` and a
ZedBoard, refer to :ref:`CN0584 User Guide <eval-cn0584-ebz>`
System Setup Using a ZedBoard section.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`EVAL-CN0585-FMCZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/cn0585-designsupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information and Useful Links
---------------------------------------

- :adi:`CN0585 Circuit Note Page <CN0585>`
- :adi:`ADAQ23876 Product Page <ADAQ23876>`
- :adi:`AD3552R Product Page <AD3552R>`
- :adi:`LTC6655 Product Page <LTC6655>`
- :adi:`ADR4525 Product Page <ADR4525>`
- :adi:`AD7291 Product Page <AD7291>`

Reference Demos & Software
--------------------------

- :external+hdl:ref:`axi_ad35xxr`
- :external+hdl:ref:`axi_ltc2387`
- :external+linux:ref:`ad3552r-hs`
- :external+linux:ref:`ltc2387`
- :ref:`hsx-toolbox`
- :ref:`pyadi-iio`
- :ref:`iio-oscilloscope`
- :ref:`kuiper`