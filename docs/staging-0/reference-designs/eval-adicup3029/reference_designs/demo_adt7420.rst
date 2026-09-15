.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_adt7420

.. _eval-adicup3029 reference_designs demo_adt7420:

ADT7420 Temperature Sensor Demo [with EVAL-ADT7420-PMDZ]
========================================================

The **ADICUP3029_ADT7420** is a temperature sensor demo project for the
**EVAL-ADICUP3029** base board with additional **EVAL-ADT7420-PMDZ** shield,
created using the Analog Devices Cross Core Embedded Studio.

General Description/Overview
----------------------------

The **ADICUP3029_ADT7420** project uses
:adi:`EVAL-ADT7420-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADT7420-PMDZ.html/>`
PMOD which is a 16-bit ambient temperature sensor. It requires no calibration.

Demo Video
----------

.. todo:: .. figure: analogTV>5554821977001

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- Hardware

  - EVAL-ADICUP3029
  - EVAL-ADT7420-PMDZ
  - Mirco USB to USB cable
  - PC or Laptop with a USB port

- Software

  - ADICUP3029_ADT7420 software

    - Inside Sensor_Sw Pack (1.0.0 or higher)

  - CrossCore Embedded Studio (2.6.0 or higher)
  - ADuCM302x DFP (2.0.0 or higher)
  - ADICUP3029 BSP (1.0.0 or higher)
  - Android IoTNode App (optional - For Bluetooth transmission only)
  - Serial Terminal Program (Required for running in release mode only)

    - Such as Putty or Tera Term

Setting up the Hardware
-----------------------

#. Plug the **EVAL-ADT7420-PMDZ** PMOD into the **EVAL-ADICUP3029** board"s I2C
   PMOD connector\ **(P9)**.
#. Place the **(S5)** switch position to read ``Wall/USB``, and the **(S2)**
   switch position to read ``USB``.
#. Plug in the micro USB cable into the **(P10)** USB port on the
   EVAL-ADICUP3029, and the other end into the PC or laptop.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adicup3029_adt7420.jpg
   :width: 650px

Configuring the Software
------------------------

In the *adt7420_app.h* header files you can configure the following parameters:

- ADI_APP_DISPATCH_TIMEOUT - *DISPATCH TIMEOUT* will define how often the data
  is sent over Bluetooth.
- ADI_APP_USE_BLUETOOTH - *ENABLE BLUETOOTH* parameter - will either use
  Bluetooth or will have the option to print to console window in debug mode or
  terminal in release mode.

Outputting Data
---------------

Once the hardware is setup and software is configured, user needs to select how
they want to view the data coming from the temperature sensor(ADT7420).

There are **three** different ways to visualize the data:

- CrossCore Embedded Studio Console Window (through semihosting)
- Serial Terminal Program (such as Putty or Tera Term)
- IoTNode Smart Device App

Depending on how you want to operate the board and visualize the data, there are
two different options that must be selected from. Below is a table outlining the
general operation, and you need to click on which **launch** file you need to
program onto the EVAL-ADICUP3029, and hit the **<F5>** key on your keyboard.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adt7420_demo_launch_configurations.png
   :width: 200px

.. list-table::
   :header-rows: 1

   * - Data Output Destination
     - Connected to Debugger
     - Configuration File
   * - CCES Console Window
     - Yes
     - ADICUP3029_Debug.launch
   * - PC/Laptop Serial Terminal
     - No
     - ADICUP3029_Release.launch
   * - IoTNode Smart App
     - Yes
     - ADICUP3029_Debug.launch
   * - IoTNode Smart App
     - No
     - ADICUP3029_Release.launch

Debug Launch Mode
~~~~~~~~~~~~~~~~~

**Debug launch mode** is used when connected to the debugger. In debug mode, all
the outputs are directed to the console window of the CrossCore tools via
semihosting. The data is also sent by default to the IoTNode smart app
(ADI_APP_USE_BLUETOOTH =1), but can be turned of if desired by setting
ADI_APP_USE_BLUETOOTH = 0.

Figure shows when ADI_APP_USE_BLUETOOTH is set to 1, sensor data is sent to
android application.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad7420_debug_outputble.png
   :width: 920px

If you have the app installed on your phone, these figure shows the output on android device. .. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your phone.

   #. Simply open up the IoTNode application on your phone.
   #. ``Scan`` for nearby demos.
   #. Once you find your demo, click on it to open it up.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adt7420_adv.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/screenshot_2017-05-28-15-43-32.png
   :width: 300px

It"s important to remember that when you use the Debug.launch file that you hit
the ``play`` button when using the tools or else your program will not run.

Release Launch Mode
~~~~~~~~~~~~~~~~~~~

**Release launch mode** is used for running without the debugger connected. When
in release mode, console output is redirected to UART. Bluetooth is enabled, and
sensor data is sent to android application. If disabled, sensor data is directed
only to the UART. If you are using the UART to make print to the PC/laptop, here
are the settings your TCP client must be set too. Following is the UART
configuration.

::

   Select COM Port
   Baud rate: 9600
   Data: 8 bit
   Parity: none
   Stop: 1 bit
   Flow Control: none

Figure shows when ADI_APP_USE_BLUETOOTH is set to 1

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adt7420_release_outputble.png
   :width: 920px

If you have the app installed on your phone, these figure shows the output on android device. .. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your phone.

   #. Simply open up the IoTNode application on your phone.
   #. ``Scan`` for nearby demos.
   #. Once you find your demo, click on it to open it up.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adt7420_adv.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/screenshot_2017-05-28-15-43-32.png
   :width: 300px

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
ADT7420.

#. Dragging and Dropping the .Hex to the Daplink drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain. Below screen shot
shows how to open project from CCES Example browser.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/adt7420_example_selection.png
   :width: 920px

The software for the **ADuCM3029_demo_adt7420** demo can be found here:

.. admonition:: Download

   Prebuilt ADT7420 Hex File

   - :git-EVAL-ADICUP3029:`AduCM3029_demo_adt7420.Hex <Latest/ADuCM3029_demo_adt7420.hex+>`

   Complete ADT7420 Source Files

   - :git-EVAL-ADICUP3029:`AduCM3029_demo_adt7420 Source Code <projects/ADuCM3029_demo_adt7420+>`

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore
Embedded Studio. For more information on downloading the tools and a quick start
guide on how to use the tool basics, please check out the
:dokuwiki:`Tools Overview page. </resources/eval/user-guides/eval-adicup3029/tools>`

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

Project Structure
~~~~~~~~~~~~~~~~~

The **ADICUP3029_ADT7420** is a C project that uses ADuCM3029 C/C++ Project
structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for I2C
read/write; configuring and reading from ADT7420, UART read/write functions;

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/ad7420_project_directory.png
   :width: 650px

adt7420_app.cpp and adt7420_app.h are the main source and header files related
to **ADICUP3029_ADT7420** be found under RTE/ADuCM3029 folder.ADT7420 sensor
software drivers are located in RTE/Sensor folder. All ADuCM3029 related drivers
can BLE related files can be seen under RTE/Board_Support folder.

**pinmux.c** – contains GPIO pinmuxing for UART and SPI.

More Information
================

.. todo:: .. include: /resources/eval/user-guides/eval-adicup3029/reference_designs/ble_packet.rst


