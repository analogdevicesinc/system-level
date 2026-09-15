.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/reference_designs/demo_adxl362

.. _eval-adicup360 reference_designs demo_adxl362:

Accelerometer Demo
==================

The **ADuCM360_demo_adxl362** is an accelerometer demo project for the
EVAL-ADICUP360 base board with additional EVAL-ADXL362-ARDZ shield, created
using Eclipse based CrossCore Embedded Studios interactive development
environment.

General description
-------------------

The ADuCM360_demo_adxl362 project uses the
:dokuwiki:`EVAL-ADXL362-ARDZ shield </resources/eval/user-guides/eval-adicup360/hardware/adxl362>`
which has an **ADXL362 3-axis MEMS accelerometer** and a incorporated
**NHD-C12832A1Z-NSW-BBW display** (128x32).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/adlx362_adicup360.jpg
   :width: 450px

The application reads the **X** , **Y**, and **Z** acceleration registers each
**500 [ms]**. The acceleration in the 3 axes is displayed in **[mG]** on the
LCD. Also this application demonstrates the usage of the motion switch. Movement
zones - **UP**, **DOWN**, **RIGHT**, **LEFT**, **CENTER** - are displayed in the
right side of the LCD.

The **EVAL-ADXL362-ARDZ** shield provide an internal temperature sensor as an
additional features which is read in the same software loop. The value is
displayed in ADC codes or in Celsius degrees. The temperature **Treal** is
derived from the ADC readings **Tadc** using the predefined formula:

::

   Treal = (Tadc + ACC_TEMP_BIAS)/(1 / ACC_TEMP_SENSITIVITY)

Each **ADXL362** chip requires individual calibration which can be done by
setting the definitions // ACC_TEMP_BIAS// and // ACC_TEMP_SENSITIVITY//
parameters. Once the **ADXL362** chip is calibrated, the software can be changed
to display the actual temperature by selecting to display the temperature in
degrees.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-aducm360-ardz/reference_designs/adxl362-demo.jpg
   :width: 300px

The software puts the LCD in a ``sleep`` mode after **10 sec** if no movement of
the boards is present. The system ``wakes-up`` if the acceleration on any axes
is greater than **50 [mG]**. The threshold values can be adjusted by the user
(:dokuwiki:`See the configuration part </resources/eval/user-guides/eval-adicup360/reference_designs/demo_adxl362#project_structure>`).

The acceleration axes, the temperature values and the motion grid are displayed
as is presented in the picture on the right.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- Hardware

  - EVAL-ADICUP360
  - EVAL-ADXL362-ARDZ
  - Mirco USB to USB cable
  - PC or Laptop with a USB port

- Software

  - ADuCM360_demo_adxl362 software
  - CrossCore Embedded Studio (2.7.0 or higher)
  - ADuCM36x DFP (1.0.2 or higher)
  - CMSIS ARM Pack (4.3.0 or higher)

Setting up the hardware
-----------------------

#. To program the base board, set the jumpers as shown in the next figure. The
   important jumpers are highlighted in red.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/cn0216_hw_config.png
      :width: 500px

#. Set the jumpers on the EVAL-ADXL362-ARDZ shield as shown in the next figure.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/eval-adxl362-ardz_default_software_config.png
      :width: 360px

   .. note::

      It"s is recommended to select P1.4 pin for LCD_CS_SEL when using ADXL362 shield with ADICUP360 base board because P2.2 is also the BM pin and it can create problems in debug session.

#. Plug the EVAL-ADXL362-ARDZ shield in the EVAL-ADICUP360 base board.
#. Power EVAL-ADICUP360 base board via the DEBUG USB port (P14).

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
ADXL362.

#. Dragging and Dropping the .Bin to the MBED drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_adxl362** demo can be found here:

.. admonition:: Download

   Prebuilt ADXL362 Bin File

   - :git-EVAL-ADICUP360:`AduCM3029_demo_adxl362.Bin <Release-1.0/ADuCM360_demo_adxl362.bin+>`

   Complete ADXL362 Source Files

   - :git-EVAL-ADICUP360:`ADuCM360_demo_adxl362 Source Code <projects/ADuCM360_demo_adxl362+>`

.. note::

   For more information on importing, debugging, or other tools related
   questions, please see the
   :dokuwiki:`tools user guide. </resources/eval/user-guides/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

Configure the temperature units in the *ADXL362.h* file.

::

   #define TEMP_ADC        1        /*0 for ADC units or 1 for Celsius degrees*/

Configure the ADXL362 Calibration Values in the *ADXL362.h* file. These values
will vary from sensor to sensor, but these are typical values from the
datasheet.

::

   #define ACC_TEMP_BIAS             (float)350
   #define ACC_TEMP_SENSITIVITY      (float)0.065

Set the Accelerometer Scan Time in the *ADXL362.h* file. This is how often you
read your axis and temperature data.(in ms)

::

   #define SCAN_SENSOR_TIME   500

Set the activity and inactivity thresholds for the ADXL362 in the *ADXL362.h*
file. These values are used to determine which acceleration values the sensor
can react at sleep/wake-up commands.(in mG)

::

   #define ACT_VALUE          50
   #define INACT_VALUE        50

Set the activity and inactivity time for the ADXL362 in the *ADXL362.h* file.
These values are used to determine sleep/wake-up intervals.(in ms)

::

   #define ACT_TIMER          50
   #define INACT_TIMER        50

Configure the Chip Select(CS) Pin for the ADXL362 in the *Communication.h* file.
Position of P9 header

::

   #define ADXL_CS_SEL     CSACC_PIN_P0_4     /*CSACC_PIN_P0_3 or CSACC_PIN_P0_4*/

Configure the Interrupt Pin from the ADXL362 in the *Communication.h* file.
Position of P7 header

::

   #define ADXL_INT_SEL     INTACC_PIN_1    /*INTACC_PIN_1 or INTACC_PIN_2*/

Configure the Chip Select(CS) Pin for the LCD Screen in the *Communication.h*
file. Position of P8 header

::

   #define LCD_CS_SEL      CSLCD_PIN_P1_4     /*CSLCD_PIN_P2_2 or CSLCD_PIN_P1_4*/

Configure the Reset Pin from the LCD Screen in the *Communication.h* file.
Position of P6 header

::

   #define LDC_RST_SEL     RSLCD_PIN_IOREF    /*RSLCD_PIN_IOREF or RSLCD_PIN_P1_1*/

Outputting Data
---------------

LCD Screen on EVAL-ADXL362-ARDZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The application reads the **X** , **Y**, and **Z** acceleration registers and
the **t** temperature register every **500 [ms]**. The acceleration in the 3
axes is displayed in **[mG]** on the LCD, and the temperature can be displayed
in both **[ADC]** codes or degrees **[C]** depending on how the software is
configured.

There is a movement plane offset to the right of the LDC screen which shows
which direction the board is currently tiled.( **UP**, **DOWN**, **RIGHT**,
**LEFT**, **CENTER**)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-aducm360-ardz/reference_designs/adxl362-demo.jpg
   :width: 300px

Also this application demonstrates the usage of the motion switch. The software
puts the LCD in a ``sleep`` mode after **10 sec** if no movement of the boards
is present. The system ``wakes-up`` if the acceleration on any axes is greater
than **50 [mG]**. The threshold values can be adjusted by the user
(:dokuwiki:`by configurating the software </resources/eval/user-guides/eval-adicup360/reference_designs/demo_adxl362#configuring_the_software_parameters>`).

The acceleration axes, the temperature values and the motion grid are displayed
as is presented in the picture on the right.

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP360 is CrossCore
Embedded Studio. For more information on downloading the tools and a quick start
guide on how to use the tool basics, please check out the
:dokuwiki:`Tools Overview page. </resources/eval/user-guides/eval-adicup360/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to import existing projects into your workspace </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_import_existing_projects_into_your_workspace>`
section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to configure the debug session </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_configure_the_debug_session_for_an_aducm3029_application>`
section.

Project structure
-----------------

The **ADuCM360_demo_adxl362** project use basic ARM Cortex-M C/C++ Project
structure. This project contains: system initialization part - disabling
watchdog, setting system clock, enabling clock for peripheral; port
configuration for SPI1, accelerometer sensor and LCD use; SPI read/write
functions; sensor monitoring and LCD handle parts.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-aducm360-ardz/reference_designs/structure_adxl362_03_09_2015.png
   :width: 400px

In the **src** and **include** folders you will find the source and header files
related to adxl362 application. You can modify as you wanted those files. The
*Communication.c/h* files contain SPI specific data, meanwhile the *ADXL362.c/h*
files contain the accelerometer data and the *Lcd.c/h* files contain the LCD
related information. Here you can configure:

The **RTE** folder contains device and system related files:

- Device Folder – contains low levels drivers for ADuCM360 microcontroller.(try
  not to edit these files)
- system.rteconfig - Allows the user to select the peripherial components they
  need, along with the startup and ARM cmsis files needed for the project.

*End of Document*
