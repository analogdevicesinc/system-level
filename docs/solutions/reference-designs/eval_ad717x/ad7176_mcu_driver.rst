.. _ad7176-mcu-driver:

AD7176-2 Microcontroller No-OS Driver
===============================================================================

.. warning::

   This page is provided for reference only. The Renesas RL78G13 driver
   described here is no longer actively maintained.

Supported Devices
-------------------------------------------------------------------------------

- :adi:`AD7176-2`

Evaluation Boards
-------------------------------------------------------------------------------

- :adi:`EVAL-AD7176-2SDZ <en/products/ad7176-2.html>`

Overview
-------------------------------------------------------------------------------

.. image:: images/ad7176_eval_sdz.jpg

The :adi:`AD7176-2` is a fast settling, highly accurate, high resolution,
multiplexed Σ-Δ analog-to-digital converter (ADC) for low bandwidth input
signals. Its inputs can be configured as two fully differential or four
pseudo differential inputs via the integrated crosspoint multiplexer. An
integrated precision, 2.5 V, low drift (2 ppm/°C), band gap internal
reference (with an output reference buffer) adds functionality and reduces
the external component count.

The maximum channel scan data rate is 50 kSPS (with a settling time of
20 μs), resulting in fully settled data of 17 noise free bits.
User-selectable output data rates range from 5 SPS to 250 kSPS. The
resolution increases at lower speeds.

The AD7176-2 offers three key digital filters. The fast settling filter
maximizes the channel scan rate. The Sinc3 filter maximizes the resolution
for single-channel, low speed applications. For 50 Hz and 60 Hz
environments, the AD7176-2 specific filter minimizes the settling times or
maximizes the rejection of the line frequency. These enhanced filters enable
simultaneous 50 Hz and 60 Hz rejection with a 27 SPS output data rate (with
a settling time of 36 ms).

System offset and gain errors can be corrected on a per channel basis. This
per channel configurability extends to the type of filter and output data
rate used for each channel. All switching of the crosspoint multiplexer is
controlled by the ADC and can be configured to automatically control an
external multiplexer via the GPIO pins.

The specified operating temperature range is −40°C to +105°C. The
:adi:`AD7176-2` is housed in a 24-lead TSSOP package.

Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Process control: PLC/DCS modules
- Temperature and pressure measurement
- Medical and scientific multichannel instrumentation
- Chromatography

The goal of this project (Microcontroller No-OS) is to provide reference
projects for lower-end processors which can't run Linux, or aren't running
a specific operating system, to help customers using microcontrollers with
ADI parts. A generic driver is provided which can be used as a base for any
microcontroller platform, along with specific drivers for different
microcontroller platforms.

**Supported Hardware Platforms:**

- `Renesas Demo Kit for RL78G13
  <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_

Driver Description
-------------------------------------------------------------------------------

The driver contains two parts:

- The driver for the AD7176-2 part, which may be used, without
  modifications, with any microcontroller.
- The Communication Driver, where the specific communication functions for
  the desired type of processor and communication protocol have to be
  implemented. This driver implements the communication with the device and
  hides the actual details of the communication protocol from the ADI
  driver.

The Communication Driver has a standard interface, so the AD7176-2 driver
can be used exactly as it is provided.

There are three functions which are called by the AD7176-2 driver:

- ``SPI_Init()`` — initializes the communication peripheral.
- ``SPI_Write()`` — writes data to the device.
- ``SPI_Read()`` — reads data from the device.

.. image:: images/spi_architecture.png

*SPI driver architecture*

The following functions are implemented in this version of the AD7176-2
driver:

.. list-table::
   :header-rows: 1

   * - Function
     - Description
   * - ``int32_t AD7176_ReadRegister(st_reg* pReg)``
     - Reads the value of the specified register.
   * - ``int32_t AD7176_WriteRegister(st_reg reg)``
     - Writes the value of the specified register.
   * - ``int32_t AD7176_Reset(void)``
     - Resets the device.
   * - ``int32_t AD7176_WaitForReady(uint32_t timeout)``
     - Waits until a new conversion result is available.
   * - ``int32_t AD7176_ReadData(int32_t* pData)``
     - Reads the conversion result from the device.
   * - ``uint8_t AD7176_ComputeCRC8(uint8_t* pBuf, uint8_t bufSize)``
     - Computes the CRC checksum for a data buffer.
   * - ``uint8_t AD7176_ComputeXOR8(uint8_t* pBuf, uint8_t bufSize)``
     - Computes the XOR checksum for a data buffer.
   * - ``void AD7176_UpdateCRCSetting(void)``
     - Updates the CRC settings.
   * - ``int32_t AD7176_Setup(void)``
     - Initializes the AD7176-2.

Renesas RL78G13 Quick Start Guide
-------------------------------------------------------------------------------

This section contains a description of the steps required to run the
AD7176-2 demonstration project on a Renesas RL78G13 platform.

Required Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Renesas Demo Kit for RL78G13
  <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
- :adi:`EVAL-AD7176-2SDZ <en/products/ad7176-2.html>`

Required Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `IAR Embedded Workbench for Renesas RL78 Kickstart
  <https://www.iar.com/embedded-development-tools/iar-embedded-workbench>`_

Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An EVAL-AD7176-2SDZ board has to be interfaced with the Renesas
Demonstration Kit (RDK) for RL78G13:

.. code-block:: none

   EVAL-AD7176-2SDZ Pin CS    ->  YRDKRL78G13 J11 connector Pin 1
   EVAL-AD7176-2SDZ Pin DIN   ->  YRDKRL78G13 J11 connector Pin 2
   EVAL-AD7176-2SDZ Pin DOUT  ->  YRDKRL78G13 J11 connector Pin 3
   EVAL-AD7176-2SDZ Pin SCLK  ->  YRDKRL78G13 J11 connector Pin 4
   EVAL-AD7176-2SDZ Pin GND1  ->  YRDKRL78G13 J11 connector Pin 5

.. image:: images/ad7176_rl78g13.jpg

.. esd-warning::

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The reference project reads data from the AD7176-2 and displays it on the
LCD.

.. image:: images/ad7176_rl78g13_screen.jpg

Software Project Tutorial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section presents the steps for developing a software application that
will run on the **Renesas Demo Kit for RL78G13** for controlling and
monitoring the operation of the ADI part.

- Run the **IAR Embedded Workbench for Renesas RL78** integrated
  development environment.
- Choose to create a new project (**Project → Create New Project**).
- Select the **RL78** tool chain, the **Empty project** template and click
  **OK**.

.. image:: images/rl78g13_software_tutorial_without_applilet3_01.png

- Select a location and a name for the project (**ADIEvalBoard** for
  example) and click **Save**.

.. image:: images/rl78g13_software_tutorial_without_applilet3_02.png

- Open the project's options window (**Project → Options**).
- From the **Target** tab of the **General Options** category select the
  **RL78 – R5F100LE** device.

.. image:: images/rl78g13_software_tutorial_without_applilet3_03.png

- From the **Setup** tab of the **Debugger** category select the **TK**
  driver and click **OK**.

.. image:: images/rl78g13_software_tutorial_without_applilet3_04.png

- The source files have to be included into the project. Open the
  **Add Files…** window (**Project → Add Files…**), select all the files
  and click **Open**.

.. image:: images/rl78g13_software_tutorial_without_applilet3_06.png

- At this moment, all the files are included into the project.
- The project is ready to be compiled and downloaded on the board. Press
  **F7** to compile it. Press **Ctrl+D** to download and debug the
  project.
- A window will appear asking to configure the emulator. Keep the default
  settings and press **OK**.

.. image:: images/rl78g13_software_tutorial_without_applilet3_07.png

- To run the project press **F5**.

.. image:: images/rl78g13_software_tutorial_without_applilet3_08.png

More Information
-------------------------------------------------------------------------------

- :ez:`Ask questions about the Microcontroller no-OS Drivers
  <microcontroller-no-os-drivers>`

