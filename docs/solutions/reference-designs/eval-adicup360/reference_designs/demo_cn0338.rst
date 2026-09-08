CO2 Gas Measurement Demo
========================

The **ADuCM360_demo_cn0338** is a CO2 gas measurement demo project for the EVAL-ADICUP360 base board with additional EVAL-CN0338-ARDZ shield, created using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General description
-------------------

This project is a good example for how to use :doc:`EVAL-ADICUP360 board </solutions/reference-designs/eval-adicup360/hardware/base_board>` in different combinations with shield boards. It expand the list of possible applications that can be done with the base board.

The **ADuCM360_demo_cn0338** project uses the :adi:`EVAL-CN0338-ARDZ shield <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0338>` which is a complete thermopile-based gas sensor using the nondispersive infrared (NDIR) principle.

.. image:: ../images/cn0338_hw_combined.png
   :align: left
   :width: 550

The CN0338 circuit uses **24-bit**, Σ-Δ **ADCs** of the ADuCM360 microcontroller for simultaneous sampling of a dual element thermopile at programmable rates of **3.5 Hz** to **3.906 kHz**.

.. image:: ../images/cn0338_demo_21.png
   :align: right
   :width: 650

The **ADuCM360_demo_cn0338** application perform ADC reads, processes them and make all necessary calculations in order to provide gas concentration. Beside this it provide an interactive **command line interpreter** which offer the possibility to the user to customize his CN0338 shield. The **UART interface** (1 start bit, 8-bits data length, no parity bits and 2 stop bits) is used to send(and to receive) data to (from) a terminal window. Default value of UART baud rate is **115200 Hz**, but you have the possibility to change it at run time from command line.

To start the application you need first to press ENTER key (CR) from the keyboard. A welcome message will pop-up, after that you can type '**help**' to find out which are the available commands.

The project offers two calibration techniques based on **Beer-Lambert Law**. Find which one is more closer to your application (see :doc:`Calibration Procedure </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0338>`).

.. note::

   When you will want to use for a first time CN0338 shield, please be aware
   that all environment variables are set to default and the CN0338 requires
   calibaration.

You can check current values of the system variables using '**printsettings**' command and also have the possibility to reset system variables to default values - '**resetTodefault**'.

.. note::

   The UART baud rate can be reset to default value using terminal command or
   pressing RESET button from EVAL-ADICUP360 board.

To start CN0338 measurements use '**run**' command. This one will display **CO2 concentration**; **temperature**; low, high and diff voltage values for **REF** (peak-to-peak output of the reference detector), **ACT** (peak-to-peak output of the active detector) and **FA** (fractional absorbance).

From command line you can set following parameters: ADC sample frequency; serial
port baud rate; falling and rising edge time for NDIR signal; NDIR light source
frequency.

.. note::

   To abort any running command you need to use 'Ctrl + c' key combination.

Calibration procedure
~~~~~~~~~~~~~~~~~~~~~

The CN0338 need to be calibrated before first use to archive best performance.
There have two calibrate algorithm in CN0338 firmware, customer can choice one
of algorithm to apply in calibrate procedure. The two algorithm is: Beer-Lambert
Law and Modified Beer-Lambert Law, for more details about those two algorithm,
please reference the circuit note in www.analog.com/cn0338.

**Beer-Lambert Law calibrate procedure**

-  input the command: **sbllcalibrate**
-  Inject low concentration or zero gas (nitrogen) to the chamber, please maker sure the gas is full filling with chamber.
-  wait for gas evenly dispersion
-  input the low concentration gas's concentration in terminal
-  Inject high concentration CO2 to the chamber, please maker sure the gas is full filling with chamber.
-  wait for gas evenly dispersion
-  input the high concentration gas's concentration in terminal
-  wait for the system to complete the calibration

**Modified Beer-Lambert Law calibrate procedure**

-  input the command: **mbllcalibrate**
-  input the constant parameter **b**
-  input the constant parameter **c**
-  Inject low concentration or zero gas (nitrogen) to the chamber, please maker sure the gas is full filling with chamber.
-  wait for gas evenly dispersion
-  input the low concentration gas's concentration in terminal
-  Inject high concentration CO2 to the chamber, please maker sure the gas is full filling with chamber.
-  wait for gas evenly dispersion
-  input the high concentration gas's concentration in terminal
-  wait for the system to complete the calibration

After above calibrate procedure the CN0338 is ready to use.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0338-ARDZ
   -  7V to 12V DC Power Supply
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADuCM360_demo_cn0338 software
   -  CrossCore Embedded Studio (2.7.0 or higher)
   -  ADuCM36x DFP (1.0.2 or higher)
   -  CMSIS ARM Pack (4.3.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the hardware
-----------------------

-  To program the base board, set the jumpers/switches as shown in the next
   figure. The important jumpers/switches are highlighted in red.

.. image:: ../images/cn0337_demo_3.png
   :align: center
   :width: 500

-  Connect the **EVAL-CN0338-ARDZ** to the Arduino connectors **P2, P3, P5, P6, P7, P8, P9** of the **EVAL-ADICUP360** board.
-  Plug in the DC Power supply into the DC barrel jack (P11) on the EVAL-ADICUP360.
-  Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB.(P14)

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
CN0338.

-  Dragging and Dropping the .Bin to the MBED drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_cn0338** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0338 Bin File

   
   -  `ADuCM360_demo_cn0338.Bin <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0338.bin>`_
   
   Complete CN0338 Source Files
   
   -  :git-EVAL-ADICUP360:`ADuCM360_demo_cn0338 Source Code <projects/ADuCM360_demo_cn0338>`
   

.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

-  **Thermopile output data processing algorithm** - ALGORITHM_PEAK2PEAK for peak-to-peak algorithm or ALGORITHM_AVERAGE for averaging algorithm(*ADC.h*).

::

      #define ALGORITHM_PEAK2PEAK

-  If the ALGORITHM_AVERAGE is defined, the system will use the average value of all ADC sample point in half IR chop period as the input.
-  If the ALGORITHM_PEAK2PEAK is defined, the system will use the maximum value
   of all ADC sample point in IR high period and minimum value of all ADC sample
   point in IR low period as the input.

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
     Baud rate: 115200
     Data: 8 bit
     Parity: none
     Start: 1 bit
     Stop: 2 bit
     Flow Control: none

-  The user must press the **<ENTER>** key to get the welcome message for this demo.
-  The user then must type in the word **<help>** to bring up the application menu.
-  The application must be calibrated before accurate reading can be taken. There are two calibration modes that you can choose from, and each one has a set of calibration steps required. Please see the :doc:`Calibration Procedure </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0338>` section on what to do for the calibration.
-  Once the calibration is complete, type **<run>** into the console window to get your results.

.. image:: ../images/cn0338_demo_21.png
   :align: center
   :width: 650

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP360 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup360/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>` section.

Project structure
-----------------

The **ADuCM360_demo_cn0338** is a C++ project that uses ADuCM36x C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for ADC, UART
via P0.1/P0.2; UART read/write functions; Memory read/write functions; NDIR
calculations; C02 concentration and temperature conversions.

.. image:: ../images/cn0338_demo_4.png
   :align: left
   :width: 310

In the **src** and **include** folders you will find the source and header files related to CN0338 software application. The *Communication.cpp/h* files contain UART specific data, meanwhile the *CN0338.cpp/h* files contain the calculation part, the *ADC.cpp/h* files contain ADC channels handling and *Flash.cpp/h* provide memory management. The entire '**command line interpreter**' is summarize in *Cmd.cpp/h*, *Cmd_settings.cpp/h* and *Cmd_calibrate.cpp/h* files. Because most of the parameters can be set at run time, not need to configure so much values before you start application.

The **RTE** folder contains device and system related files:

-  **Device Folder** – contains low levels drivers for ADuCM360 microcontroller.(try not to edit these files)
-  **system.rteconfig** - Allows the user to select the peripherial components they need, along with the startup and ARM cmsis files needed for the project.
