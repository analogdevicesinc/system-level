ADXL362 Accelerometer Demo [with PmodACL2]
==========================================

The **ADICUP3029_ADXL362** is a accelerometer demo project for the **EVAL-ADICUP3029** base board with additional **PmodACL2** shield, created using the Analog Devices Cross Core Embedded Studio.

General Description/Overview
----------------------------

The **ADICUP3029_ADXL362** project uses `PmodACL2 PMOD <http://store.digilentinc.com/pmod-acl2-3-axis-mems-accelerometer/>`_ which is a 3-axis MEMS accelerometer powered by ADXL362. The accelerometer is interfaced via SPI protocol and users may receive up to 12-bits of resolution for each axis of acceleration. ADXL362 supports freefall detection as well as motion activated sleep and wakeup modes.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  PmodACL2 - from Digilent
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADICUP3029_ADXL362 software

      -  Inside Sensor_Sw Pack (1.0.0 or higher)

   -  CrossCore Embedded Studio (2.6.0 or higher)
   -  ADuCM302x DFP (2.0.0 or higher)
   -  ADICUP3029 BSP (1.0.0 or higher)
   -  Android IoTNode App (optional)
   -  Serial Terminal Program (Required for running in release mode only)

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Plug the **Pmod ACL2** PMOD into the **EVAL-ADICUP3029** board's SPI1 PMOD connector (P8)
-  Place the **(S5)** switch position to read "Wall/USB", and the **(S2)** switch position to read "USB".
-  Plug in the micro USB cable into the **(P10)** USB port on the EVAL-ADICUP3029, and the other end into the PC or laptop.

.. image:: ../images/adicup3029_pmodacl2.jpg
   :width: 650

Configuring the Software
------------------------

In the *adxl362_app.h* header files you can configure the following parameters:

-  **ADI_APP_DISPATCH_TIMEOUT** - *DISPATCH TIMEOUT* will define how often the data is sent over Bluetooth.
-  **ADI_APP_USE_BLUETOOTH** - *ENABLE BLUETOOTH* parameter - will either use Bluetooth or will have the option to print to console window in debug mode or terminal in release mode.

Outputting Data
---------------

Once the hardware is setup and software is configured, user needs to select how
they want to view the data coming from the accelerometer sensor(ADXL362).

There are **three** different ways to visualize the data:

-  CrossCore Embedded Studio Console Window (through semihosting)
-  Serial Terminal Program (such as Putty or Tera Term)
-  IoTNode Smart Device App

Depending on how you want to operate the board and visualize the data, there are two different options that must be selected from. Below is a table outlining the general operation, and you need to click on which **launch** file you need to program onto the EVAL-ADICUP3029, and hit the **<F5>** key on your keyboard.

|image1|

+---------------------------+-----------------------+---------------------------+
| Data Output Destination   | Connected to Debugger | Configuration File        |
+===========================+=======================+===========================+
| CCES Console Window       | Yes                   | ADICUP3029_Debug.launch   |
+---------------------------+-----------------------+---------------------------+
| PC/Laptop Serial Terminal | No                    | ADICUP3029_Release.launch |
+---------------------------+-----------------------+---------------------------+
| IoTNode Smart App         | Yes                   | ADICUP3029_Debug.launch   |
+---------------------------+-----------------------+---------------------------+
| IoTNode Smart App         | No                    | ADICUP3029_Release.launch |
+---------------------------+-----------------------+---------------------------+

|

Debug Mode
~~~~~~~~~~

**Debug launch mode** is used when connected to the debugger. In debug mode, all the outputs are directed to the console window of the CrossCore tools via semihosting. The data is also sent by default to the IoTNode smart app (ADI_APP_USE_BLUETOOTH =1), but can be turned of if desired by setting ADI_APP_USE_BLUETOOTH = 0.

Figure shows when ADI_APP_USE_BLUETOOTH is set to 1, sensor data is sent to
android application.

.. image:: ../images/adxl362_debug_ouputble.png
   :width: 920

If you have the app installed on your phone, these figure shows the output on
android device.

.. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your
   phone.

   -  Simply open up the IoTNode application on your phone.
   -  "Scan" for nearby demos.
   -  Once you find your demo, click on it to open it up.

|image2| |image3|

It's important to remember that when you use the Debug.launch file that you hit
the "play" button when using the tools or else your program will not run.

Figure shows when ADI_APP_USE_BLUETOOTH is set to 0, Sensor data is printed on
to console.

.. image:: ../images/adxl362_debug_ouput.png
   :width: 920

Release Mode
~~~~~~~~~~~~

**Release launch mode** is used for running without the debugger connected. When in release mode, console output is redirected to UART. Bluetooth is enabled, and sensor data is sent to android application. If disabled, sensor data is directed only to the UART. If you are using the UART to make print to the PC/laptop, here are the settings your TCP client must be set too. Following is the UART configuration.

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

Figure shows when ADI_APP_USE_BLUETOOTH is set to 1

.. image:: ../images/adx362_reease_output.png
   :width: 920

If you have the app installed on your phone, these figure shows the output on
android device.

.. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your
   phone.

   -  Simply open up the IoTNode application on your phone.
   -  "Scan" for nearby demos.
   -  Once you find your demo, click on it to open it up.

|image4| |image5|

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
ADXL362 PmodACL2.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain. Below screen shot
shows how to open project from CCES Example browser.

.. image:: ../images/sensorexampleselection.jpg
   :width: 920

The source code and include files of the **ADuCM3029_demo_adxl362** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt ADXL362 PMOD Hex File

   -  `AduCM3029_demo_adxl362.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_adxl362.hex>`_

   Complete ADXL362 PMOD Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_adxl362 Source Code <projects/ADuCM3029_demo_adxl362>`

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Project Structure
~~~~~~~~~~~~~~~~~

The **ADICUP3029_ADXL362** is a C project that uses ADuCM3029 C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for SPI
read/write; configuring and reading from ADXL362, UART read/write functions;

.. image:: ../images/adxl362_project.jpg
   :width: 300

adxl362_app.cpp and adxl362_app.h are the main source and header files related to **ADICUP3029_ADXL362** be found under RTE/ADuCM3029 folder.ADXL362 sensor software drivers are located in RTE/Sensor folder. All ADuCM3029 related drivers can BLE related files can be seen under RTE/Board_Support folder.

**pinmux.c** – contains GPIO pinmuxing for UART and SPI.

*End of Document*

.. |image1| image:: ../images/adt7420_demo_launch_configurations.png
   :width: 200

.. |image2| image:: ../images/adxl362_dev.png
   :width: 600

.. |image3| image:: ../images/adxl362_screen2.png
   :width: 300

.. |image4| image:: ../images/adxl362_dev.png
   :width: 600

.. |image5| image:: ../images/adxl362_screen2.png
   :width: 300
