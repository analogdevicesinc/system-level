.. _eval-ad5529r-ardz user-guide:

User Guide
==========

This guide covers the hardware configuration and software setup for the
:adi:`EVAL-AD5529R-ARDZ` evaluation board.

Hardware Guide
--------------

Connectors and Pinout
~~~~~~~~~~~~~~~~~~~~~

The EVAL-AD5529R-ARDZ connects to the Cora Z7 via Arduino-compatible headers.

Pin definitions are in the HDL constraints file:
:git-hdl:`system_constr.xdc <projects/ad5529r_ardz/coraz7s/system_constr.xdc>`

**SPI Interface (Arduino Header)**

.. list-table:: SPI Pin Mapping
   :header-rows: 1
   :widths: 20 20 30 30

   * - Signal
     - Arduino Pin
     - Cora Z7 Pin
     - Description
   * - SCLK
     - D13
     - G15
     - SPI clock (up to 35 MHz)
   * - MISO
     - D12
     - J18
     - SPI data - DAC to FPGA (read from ad5529r)
   * - MOSI
     - D11
     - K18
     - SPI data - FPGA to DAC (write to ad5529r)
   * - CS
     - D10
     - U15
     - Chip select (active low)

**Control Signals**

.. list-table:: Control Pin Mapping
   :header-rows: 1
   :widths: 15 15 15 55

   * - Signal
     - Arduino
     - Cora Z7 Pin
     - Description
   * - RESET
     - D8
     - N18
     - Hardware reset (active-low, edge-triggered).
   * - CLEAR
     - D7
     - R14
     - Clear all outputs (active-low, level-triggered). Hold low to clear.
   * - ALARM
     - D4
     - V17
     - Fault indicator input. See warning below.

.. warning::

   **ALARM Signal Level Issue**

   The ALARM signal path uses a 1.8V inverter (NC7SZ04) without level
   translation to 3.3V. The FPGA may not detect the ALARM high level reliably
   due to LVCMOS33 input threshold requirements.

**Toggle Pins (TG0-TG3)**

The toggle pins enable synchronized multi-channel updates:

.. list-table:: Toggle Pin Mapping
   :header-rows: 1
   :widths: 15 15 15 55

   * - Signal
     - Arduino Pin
     - Cora Z7 Pin
     - Description
   * - TG0
     - D9
     - M18
     - Toggle group 0 (channels 0-3)
   * - TG1
     - D6
     - R17
     - Toggle group 1 (channels 4-7)
   * - TG2
     - D5
     - V18
     - Toggle group 2 (channels 8-11)
   * - TG3
     - D3
     - T15
     - Toggle group 3 (channels 12-15)

**LDAC**

- Function: Load DAC (update outputs simultaneously)
- Directly controlled by SPI Engine offload trigger

Test Points
~~~~~~~~~~~

.. TODO:: Add test point location photo (images/test-points.png)

The evaluation board provides test points for key signals:

- **VREF**: Internal/external voltage reference (2.5V default)
- **VOUT0-VOUT15**: Individual DAC channel outputs
- **VDD_HV_A/B**: High-voltage positive supplies
- **VSS_HV_A/B**: High-voltage negative supplies
- **GND**: Ground reference

Configuration Jumpers
~~~~~~~~~~~~~~~~~~~~~

.. TODO:: Add jumper configuration photo (images/jumper-config.png)

**VREF Selection (JP1)**

.. list-table:: Reference Voltage Configuration
   :header-rows: 1
   :widths: 30 70

   * - Jumper Position
     - Description
   * - Internal (default)
     - Use AD5529R internal 2.5V reference
   * - External
     - Use external reference via VREF_EXT pin

**VDD_IO Selection (JP2)**

.. list-table:: I/O Voltage Configuration
   :header-rows: 1
   :widths: 30 70

   * - Jumper Position
     - Description
   * - 1.8V
     - 1.8V logic level (default for AD5529R)
   * - 3.3V
     - 3.3V logic level (requires level translators)

.. note::

   The EVAL-AD5529R-ARDZ includes onboard 74AVC8T245 level translators for
   3.3V operation. VDD_IO is set to 1.8V on the DAC side.

LED Indicators
~~~~~~~~~~~~~~


.. TODO:: Verify if ALARM LED present - Fault indicator

- **PWR LED**: Power supply status (green = powered)
- **ALARM LED**: TODO: Verify if present - Fault indicator

Power Supply
~~~~~~~~~~~~

The EVAL board requires the following supplies:

**From Cora Z7 (via Arduino headers):**

- VDD: 5V (main supply for DC-DC converters)
- VDD_IO: 3.3V (logic level supply)

**Generated on-board:**

The board includes an ADP5070 DC-DC converter with LDO post-regulation:

.. list-table:: High-Voltage Supply Options
   :header-rows: 1
   :widths: 20 40 40

   * - Supply
     - Range Options
     - Channels
   * - VDD_HV_A
     - +5.5V / +10.5V / +15.5V / +20.5V
     - DAC0-DAC7
   * - VSS_HV_A
     - -5.5V / -10.5V / -15.5V
     - DAC0-DAC7
   * - VDD_HV_B
     - +5.5V / +10.5V / +15.5V / +20.5V
     - DAC8-DAC15
   * - VSS_HV_B
     - -5.5V / -10.5V / -15.5V
     - DAC8-DAC15

Software Guide
--------------

Device Driver Support
~~~~~~~~~~~~~~~~~~~~~

**Linux IIO Driver**

The AD5529R is supported by the Linux IIO subsystem:

- :git-linux:`AD5529R Linux Driver <main:drivers/iio/dac/ad5529r.c>`

The driver exposes each DAC channel as an IIO output channel with attributes:

- ``raw``: 16-bit DAC code (0-65535)
- ``scale``: Voltage scaling factor
- ``offset``: Voltage offset

**no-OS Driver**

For bare-metal applications:

- :git-no-OS:`AD5529R no-OS Driver <drivers/dac/ad552xr>`

HDL Reference Design
~~~~~~~~~~~~~~~~~~~~

The HDL project implements high-throughput DAC streaming:

- :external+hdl:ref:`AD5529R HDL Project Documentation <ad5529r_ardz>`
- :git-hdl:`HDL Source Code <projects/ad5529r_ardz/>`

**Architecture:**

- **SPI Engine**: 16-bit data width, offload with streaming
- **AXI DMA**: Memory-to-stream for waveform playback
- **PWM Generators**: Hardware trigger (SPI) + Toggle pins (TG0-TG3)
- **Clock Generator**: 140 MHz for 35 MHz SCLK

**AXI Address Map:**

.. list-table:: Peripheral Base Addresses
   :header-rows: 1
   :widths: 30 30 40

   * - Base Address
     - Peripheral
     - Purpose
   * - 0x44A0_0000
     - spi_ad5529r_axi_regmap
     - SPI Engine control registers
   * - 0x44A4_0000
     - ad5529r_dma
     - DMA controller
   * - 0x44B0_0000
     - trig_gen
     - Hardware trigger generator
   * - 0x44B1_0000
     - axi_ad5529r_clkgen
     - SPI clock generator
   * - 0x44B2_0000
     - toggle_gen
     - Toggle pin generators

Kuiper Linux
~~~~~~~~~~~~

:external+kuiper:doc:`ADI Kuiper Linux <index>` provides a ready-to-use Linux
distribution with IIO tools and drivers pre-installed.

The AD5529R device appears as an IIO device:

.. code-block:: console

   root@analog:~# iio_info | grep ad5529r
   iio:device0: ad5529r

DMA Streaming Mode
~~~~~~~~~~~~~~~~~~

For high-throughput waveform playback, the HDL design supports DMA streaming:

1. Prepare waveform data in memory (16-bit samples)
2. Configure DMA transfer parameters
3. Enable SPI Engine offload
4. Trigger transfer via hardware PWM or software

Maximum throughput: TODO kSPS (verify with actual measurements)

Schematic, PCB Layout, Bill of Materials
----------------------------------------

- :adi:`EVAL-AD5529R-ARDZ Schematic <EVAL-AD5529R-ARDZ>`
- :adi:`EVAL-AD5529R-ARDZ PCB Layout <EVAL-AD5529R-ARDZ>`
- :adi:`EVAL-AD5529R-ARDZ Bill of Materials <EVAL-AD5529R-ARDZ>`

.. TODO:: Add direct links to design files when available
