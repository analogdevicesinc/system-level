.. _ad7175-mcu-driver:

AD7175-2 Microcontroller No-OS Driver
===============================================================================

.. warning::

   This page is provided for reference only. The Renesas RL78G13 driver
   described here is no longer actively maintained.

Supported Devices
-------------------------------------------------------------------------------

- :adi:`AD7175-2`

Evaluation Boards
-------------------------------------------------------------------------------

- :adi:`EVAL-AD7175-2SDZ`

Overview
-------------------------------------------------------------------------------

.. image:: images/eval_ad7175_sdz.jpg

The :adi:`AD7175-2` is a low noise, fast settling, multiplexed, 2/4 channel
(fully/pseudo-differential) sigma delta analog-to-digital converter (ADC)
for DC inputs. It has a maximum channel scan rate of 50 kSPS (20 µs) for
fully settled data. The output data rates range from 5 SPS to 250 kSPS.
The AD7175-2 integrates key analog and digital signal conditioning blocks
to allow users to configure an individual setup for each analog input
channel in use. Each feature can be user selected on a per channel basis.
Integrated fully rail-to-rail buffers on the analog inputs and external
reference inputs provide easy-to-drive high impedance inputs.

The goal of this project (Microcontroller No-OS) is to provide reference
projects for lower-end processors which can't run Linux, or aren't running
a specific operating system, to help customers using microcontrollers with
ADI parts. A generic driver is provided which can be used as a base for any
microcontroller platform, along with specific drivers for Renesas platforms.

**Supported Hardware Platforms:**

- `Renesas Demo Kit for RL78G13
  <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_

Driver Description
-------------------------------------------------------------------------------

The driver contains two parts:

- The driver for the AD7175-2 part, which may be used, without
  modifications, with any microcontroller.
- The Communication Driver, where the specific communication functions for
  the desired type of processor and communication protocol have to be
  implemented. This driver implements the communication with the device and
  hides the actual details of the communication protocol from the ADI
  driver.

The Communication Driver has a standard interface, so the AD7175-2 driver
can be used exactly as it is provided.

There are three functions which are called by the AD7175-2 driver:

- ``SPI_Init()`` — initializes the communication peripheral.
- ``SPI_Write()`` — writes data to the device.
- ``SPI_Read()`` — reads data from the device.

.. image:: images/spi_architecture.png

*SPI driver architecture*

The following functions are implemented in this version of the AD7175-2
driver:

.. list-table::
   :header-rows: 1

   * - Function
     - Description
   * - ``int32_t AD7175_ReadRegister(st_reg* pReg)``
     - Reads the value of the specified register.
   * - ``int32_t AD7175_WriteRegister(st_reg reg)``
     - Writes the value of the specified register.
   * - ``int32_t AD7175_WaitForReady(uint32_t timeout)``
     - Waits until a new conversion result is available.
   * - ``int32_t AD7175_ReadData(int32_t* pData)``
     - Reads the conversion result from the device.
   * - ``uint8_t AD7175_ComputeCRC(uint8_t* pBuf, uint8_t bufSize)``
     - Computes the CRC for a data buffer.
   * - ``int32_t AD7175_Setup(void)``
     - Initializes the AD7175-2.

Renesas RL78G13 Quick Start Guide
-------------------------------------------------------------------------------

This section contains a description of the steps required to run the
AD7175-2 demonstration project on a Renesas RL78G13 platform.

Required Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Renesas Demo Kit for RL78G13
  <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
- :adi:`EVAL-AD7175-2SDZ`

Required Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `IAR Embedded Workbench for Renesas RL78 Kickstart
  <https://www.iar.com/embedded-development-tools/iar-embedded-workbench>`_

Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An EVAL-AD7175-2SDZ board has to be interfaced with the Renesas
Demonstration Kit (RDK) for RL78G13:

.. code-block:: none

   EVAL-AD7175-2SDZ Pin CS    ->  YRDKRL78G13 J11 connector Pin 1
   EVAL-AD7175-2SDZ Pin DIN   ->  YRDKRL78G13 J11 connector Pin 2
   EVAL-AD7175-2SDZ Pin DOUT  ->  YRDKRL78G13 J11 connector Pin 3
   EVAL-AD7175-2SDZ Pin SCLK  ->  YRDKRL78G13 J11 connector Pin 4
   EVAL-AD7175-2SDZ Pin GND1  ->  YRDKRL78G13 J11 connector Pin 5

.. image:: images/ad7175_rl78g13.jpg

.. esd-warning::

Reference Project Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The reference project reads data from the AD7175-2 and displays it on the
LCD.

.. image:: images/ad7175_rl78g13_screen.jpg

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

