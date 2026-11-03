.. _eval-ad7124-x quickstart nucleo:

Nucleo-L476RG Quick Start (STM32)
===============================================================================

.. esd-warning::

This guide describes how to use the :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` or
:adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>` evaluation board with the STM32 Nucleo-L476RG using
STM32CubeIDE. The general procedure can be applied to other STM32 processors
and IDEs.

.. important::

   The example code was developed and tested using the Nucleo-L476RG with
   version 1.14.0 of the STM32 firmware libraries, and STM32CubeIDE v1.0.0.
   It may be retargeted to other STM32 processors/boards through the use of
   appropriate ST firmware HAL libraries. <web>

Prerequisites
-------------------------------------------------------------------------------

See :ref:`eval-ad7124-x prerequisites` for the full list.

**Hardware:**

- :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` or :adi:`EVAL-AD7124-8SDZ <EVAL-AD7124-8>` evaluation board
- `STM32 Nucleo-L476RG <https://www.st.com/en/evaluation-tools/nucleo-l476rg.html>`_
- :adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>` (for convenient SPI
  connections)
- 7--9 V DC power supply for the evaluation board
- Micro USB cable

**Software:**

- `STM32CubeIDE <https://www.st.com/en/development-tools/stm32cubeide.html>`_

.. admonition:: Download

   - `ad7124_stm32_example.zip <https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad7124_example/ad7124_stm32_example.zip>`_ <web>

Software integration guide
-------------------------------------------------------------------------------

Project creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Install STM32CubeIDE if not already installed.
#. In the Firmware Update section of STM32CubeIDE preferences, set the
   firmware package storage location (e.g., ``C:\ST\Repository``).

   .. tip::

      Place this in a common location, not under your home directory, to avoid
      user-specific paths in shared configuration files.

#. Select **File >> New >> STM32 project**.
#. Select the MCU part number or board (Nucleo-L476RG).
#. Give the project a name, select target language, and project type of
   STM32Cube.
#. Verify the Target Reference and firmware package repository path. Set the
   Code Generator Options to reference or copy library files as desired.
#. Click **Finish**. STM32CubeIDE will download and unzip the firmware library
   (typically hundreds of MB; this takes several minutes).

Device configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Device Configuration Tool with automatic code generation defines pin usage
and default modes of operation for the Nucleo-L476RG.

.. important::

   The pins and configuration provided here need to be tailored to the
   specific board/processor being used.

SPI configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SPI1 port is used to communicate with the AD7124. Pin PB10 is used as a
software-controlled chip select for SPI1. Its mode must be set to
**GPIO_output** with user label **SPI1_NSS** to match the platform driver file.

.. tip::

   It is recommended to use a pull-up resistor on the SPI MOSI to ensure it
   is never floating in an undefined logic state. This can be a resistor on
   the board to the logic supply, or internal to the processor if available.

DMA and interrupts are not used and do not need to be configured.

Serial UART configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The serial port uses USART2. No DMA or interrupts need to be configured.

GPIO configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An LED is toggled on the Nucleo-L476RG to indicate sampling activity. The
activity LED is controlled by Port A, Pin 5, and needs to be enabled as a
digital output.

Build settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``printf()`` function is used to print floating-point values in the
terminal. As this feature is often disabled by default, floating-point support
must be enabled:

In **Project Properties >> C/C++ Build >> Settings >> MCU GCC Linker >>
Miscellaneous >> Other Flags**, add ``-u _printf_float``.

.. tip::

   There is also a checkbox option in the MCU Settings view. Enabling it in
   the linker section prevents the code analysis feature from reporting ``%f``
   as unsupported.

Linker files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default value for ``_estack`` may be incorrect in the ``.ld`` files. This
can cause ``printf()`` with ``%f`` to output ``0.00`` instead of the correct
value.

For the Nucleo-L476RG, change:

.. code-block:: c

   /* Highest address of the user mode stack */
   _estack = 0x20017fff; /* end of "RAM" Ram type memory */

to:

.. code-block:: c

   /* Highest address of the user mode stack */
   _estack = 0x20018000; /* end of "RAM" Ram type memory */

Source file edits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

main.c
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the following to integrate the AD7124 example application:

.. code-block:: c

   #include "ad7124_console_app.h"

   /* Initialize the AD7124 application before the main loop */
   int32_t setupResult;
   if ((setupResult = ad7124_app_initialize(AD7124_CONFIG_A)) < 0) {
       // Handle error setting up AD7124 here
   }

   while(1) {
       // display the console menu for the AD7124 application
       adi_do_console_menu(&ad7124_main_menu);
   }

main.h
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add extern declarations for the SPI and serial port handles:

.. code-block:: c

   extern SPI_HandleTypeDef hspi1;
   extern UART_HandleTypeDef huart2;

.. important::

   The names of the port handles are defined by the Device Configuration Tool
   based on the selected processor and pin choices. If using a different
   processor or pins, these may need to be changed in ``platform_drivers.c``
   and ``platform_support.c``.

syscalls.c
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the ``_read()`` function, the ``len`` parameter may always be 1024. To
support ``getchar()``, add ``len = 1;`` immediately before the for loop. This
does not support other ``stdio.h`` functions such as ``scanf()``.

Adding AD7124 example files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the AD7124 source and header files from the distribution to the project.
Files can be placed in a dedicated ``adi`` directory, or in the main ``src``
directory, or split between ``src`` and ``inc`` directories. If adding new
source/header locations, add them to the build settings in the relevant
**Include paths** in the MCU GCC Compiler configuration.

.. important::

   The ``platform_support.c/.h`` files provide ``io_getchar()`` and
   ``io_putchar()`` for serial I/O. If using a compiler other than GCC or a
   different serial port than USART2, additional changes may be required.

Hardware connections
-------------------------------------------------------------------------------

Power and USB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A 9 V DC supply (barrel jack, center pin positive) is required to power the
:adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` evaluation board. The Nucleo-L476RG is
powered via the USB connection to the PC, which also provides the serial UART
connection.

.. tip::

   If you are unsure which COM port to use, open Device Manager and look under
   the **Ports (COM & LPT)** node.

SPI interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SPI connections from the :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>` to the
Nucleo-L476RG can be made via the :adi:`SDP Breakout Board <SDP-BREAKOUT-BOARD>`.

.. list-table:: SPI Wiring (via SDP Breakout Board)
   :header-rows: 1
   :widths: 25 25 30

   * - AD7124 SPI Signal
     - SDP Breakout Board Pin
     - Nucleo-L476RG Pin
   * - GND
     - 81
     - GND on CN5.7
   * - SCLK
     - 82
     - D3 (PB3) on CN9.4
   * - DOUT/RDYB
     - 83
     - D5 (PB4) on CN9.6
   * - DIN
     - 84
     - D4 (PB5) on CN9.5
   * - CSB
     - 85
     - D6 (PB10) on CN9.7

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The screw terminal connections on J6 and J11 on the :adi:`EVAL-AD7124-4SDZ <EVAL-AD7124-8>`
board can be used to connect analog input signals.

**Configuration A:**

- AIN0/AIN1 are used for channel 0, simple voltage measurement

**Configuration B:**

- AIN2/AIN3 connect to the A2 thermocouple connector (channel 0, internal
  reference, bias voltage on AIN2)
- AIN4/AIN5 are an RTD1000 measurement on channel 1 (excitation from AIN1,
  requires external RTD and reference resistor)

Console application
-------------------------------------------------------------------------------

Once the hardware connections are made and the compiled code is programmed into
the board, open a terminal program and reset the hardware to see the AD7124
menu. The menu allows:

- Resetting the device
- Programming pre-defined configurations
- Sampling data displayed on screen or streamed for capture
