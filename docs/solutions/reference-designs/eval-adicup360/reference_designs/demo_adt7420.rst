ADT7420 PMOD Temperature Demo
=============================

The **ADuCM360_demo_adt7420_pmdz** is a temperature demo project for the EVAL-ADICUP360 base board with an EVAL-ADT7420-PMDZ PMOD board from Analog Devices, using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General description
-------------------

This project is an example for how to use :doc:`EVAL-ADICUP360 board </solutions/reference-designs/eval-adicup360/hardware/base_board>` in combination with the :doc:`EVAL-ADT7420-PMDZ Temperature PMOD. </solutions/reference-designs/eval-adicup360/hardware/adt7420>`

The ADuCM360_demo_adt7420_pmdz project uses the :adi:`EVAL-ADT7420-PMDZ` which has the **ADT7420 0.25 degree accurate digital temperature sensor** on board.

.. image:: ../images/adicup360_adt7420_user_powered.jpg
   :align: center
   :width: 600

The application reads the temperature data from the ADT7420 and displays the temperature in **[codes]** and **[C]** on a serial terminal. The temperature data can be changed between 16-bit(0.0078 C/LSB) and 13-bit(0.0625 C/LSB) accurate depending on the resolution needed. The application also prints out the device ID register, which is just a quick and easy check to ensure the reads are working properly.

All the outputs are printed from the UART to the USER USB port using P0.6 and P0.7, and can be read on the PC using a serial terminal program, such as Putty or Tera Term. The user must ensure that the USB cable is connected to the USER USB port in order to read back values in Putty. Also, the user must press the **<ENTER>** key in order to refresh the results.

.. image:: ../images/putty_output_display.png
   :align: center
   :width: 600

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-ADT7420-PMDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADuCM360_demo_adt7420_pmdz software
   -  CrossCore Embedded Studio (2.7.0 or higher)
   -  ADuCM36x DFP (1.0.2 or higher)
   -  CMSIS ARM Pack (4.3.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the hardware
-----------------------

- To program the base board, set the jumpers/switches as shown in the next figure. The important jumpers/switches are highlighted in red.

.. image:: ../images/aduicup360_switch_config.png
   :align: center
   :width: 500

- Plug the EVAL-ADT7420-PMDZ PMOD in the EVAL-ADICUP360 base board, via the PMOD_I2C port (P10).
- Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the Debug USB.(P14)

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
ADT7420.

-  Dragging and Dropping the .Bin to the MBED drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_adt7420** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt ADT7420 Bin File

   
   -  `AduCM3029_demo_adt7420_pmdz.Bin <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_adt7420_pmdz.bin>`_
   
   Complete ADT7420 Source Files
   
   -  :git-EVAL-ADICUP360:`AduCM3029_demo_adt7420 Source Code <projects/ADuCM360_demo_adt7420_pmdz>`
   

.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

Configure the ADT7420 I2C address in the *ADT7420.h* file to match the hardware.

::

   /* ADT7420 I2C Address */
   #define ADT7420_ADDRESS    0x48      /* Default I2C Address of EVAL-ADT7420-PMDZ */

Configure the ADT7420 in the operating mode you want using the *ADT7420.c* file

::

   uint8_t ui8configAdt7420 = (FAULT_TRIGGER_4 | CT_PIN_POLARITY | INT_PIN_POLARITY | INT_CT_MODE |CONTINUOUS_CONVERSION_MODE | RESOLUTION_13_BITS);

   /* False Trigger Count */
   #define FAULT_TRIGGER_1      /* 1 fault reading triggers an interrupt */
   #define FAULT_TRIGGER_2      /* 2 fault readings triggers an interrupt */
   #define FAULT_TRIGGER_3      /* 3 fault readings triggers an interrupt */
   #define FAULT_TRIGGER_4      /* 4 fault readings triggers an interrupt */

   /* Alarm Logic Levels */
   #define CT_PIN_POLARITY      /* Critical temp active logic level */
   #define INT_PIN_POLARITY     /* Interrupt temp active logic level */

   /* Interrupt Mode */
   #define INT_CT_MODE      /* Selects comparator or interrupt mode */

   /* Conversion Mode */
   #define CONTINUOUS_CONVERSION_MODE   /* Continuous conversion */
   #define ONE_SHOT_MODE                /* One shot conversion, then shuts down */
   #define ONE_SAMPLE_PER_SECOND_MODE   /* One second between readings */
   #define SHUTDOWN_MODE                /* Power down mode activated */

   /* Resolution */
   #define RESOLUTION_13_BITS    /* 13-bit Temperature data */
   #define RESOLUTION_16_BITS    /* 16-bit Temperature data */

Assign values to your different temperature setpoints and alarms/interrupts in the *ADT7420.h* file

::

   /* Temperature monitoring parameters */
   #define TEMP_HIGH_SETPOINT             75          /* Value in Degree C */
   #define TEMP_LOW_SETPOINT              0           /* Value in Degree C */
   #define TEMP_CRITICAL_SETPOINT         100         /* Value in Degree C */
   #define TEMP_HYSTERSIS_SETPOINT        5           /* Value in Degree C */

Outputting Data
---------------

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

-  In order to view the data, you must flash the program to the EVAL-ADICUP360.
-  Once complete you will need to switch the USB cable from the DEBUG USB (P14) to the USER USB (P13).
-  Then follow the UART settings below with the serial terminal program.

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

The user must press the **<ENTER>** key each time they want to display the results.

.. image:: ../images/putty_output_display.png
   :align: center
   :width: 600

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP360 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup360/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>` section.

Project Structure
~~~~~~~~~~~~~~~~~

This is the **ADuCM360_demo_adt7420_pmdz** project structure. This project contains: system initialization part - disabling watchdog, setting system clock, enabling clock for peripheral; port configuration for I2C, temperature sensor data; I2C read/write functions; threshold monitoring.

.. image:: ../images/adumc360_ide_project_structure.png
   :align: left
   :width: 400

In the **src** and **include** folders you will find the source and header files related to adt7420_pmdz application. You can modify those files as appropriate for your application. The *Communication.c/h* files contain I2C and UART specific data, meanwhile the *ADT7420.c/h* files contain the temperature information data and threshold registers. Here are parameters you can configure:

The **RTE** folder contains device and system related files:

-  **Device Folder** – contains low levels drivers for ADuCM360 microcontroller.(try not to edit these files)
-  **system.rteconfig** - Allows the user to select the peripherial components they need, along with the startup and ARM cmsis files needed for the project.
