Visible Light Detection Demo [with EVAL-CN0397-ARDZ]
====================================================

The **ADICUP3029_CN0397** is a RGB light detection demo project for the **EVAL-ADICUP3029** base board with additional **EVAL-CN0397-ARDZ** shield, created using the Analog Devices Cross Core Embedded Studio.

General Description/Overview
----------------------------

The **ADICUP3029_CN0397** project uses the :adi:`EVAL-CN0397-ARDZ shield <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0397>` which is a single-supply, low power, low noise, 16-bit light detector utilizing wavelength specific photodiodes. The photodiodes used in this circuit are sensitive at different wavelengths, to read light intensity levels over the visible light spectrum where the plants are photosynthetically active.

The **EVAL-CN0397-ARDZ** board uses :adi:`ad8500`, a low power, precision CMOS op amp with a low input bias current of a typical 1pA which is used in a transipedance amplifier configuration to convert the current output of the photodiodes into voltage. It also features :adi:`ad7798` a 3-channel, low noise, low power 16-bit ADC that converts the analog voltage into digital data in for the processing of data into light intensity. The circuit utilizes RGB photodiodes from Everlight with their peak sensitivities 620nm (**R**), 550nm (**G**) and 470nm (**B**).

The **ADICUP3029_CN0397** application perform ADC readings for all 3 channels, processes them and make all necessary calculations in order to provide light intensity and light concentration for each color.

.. image:: ../images/board.png
   :align: left
   :width: 440

The 16-bits ADC data are received using **SPI interface** of the EVAL-ADICUP3029 board. The **UART interface** (**9600** baud rate and **8-bits** data length) is used to send(and to receive) data to (from) a terminal window.

**Light intensity** [Lux] is calculated using ADC output value for selected channel and a constant value for each color:

::

   Light Intensity = CODE * Light intensity Constant

**Light Concentration** [%] is calculated based on the light intensity and optimal level for each color:

::

   Light concentration = Intensity\*100/Optimal Level

Beside **light intensity** and **light concentration** values, for each channel will be displayed a **colored bar** in [0%, 100%] format for light concentration representation. It will inform the user when the concentration for a specific channel will reach **100%**. Application offer the possibility to perform a system offset calibration for each **RGB channel**. All calculation are using data specific to each color of the used LEDs:

.. image:: ../images/table.png
   :align: center
   :width: 600

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0397-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADICUP3029_CN0397 software

      -  Inside Sensor_Sw Pack (1.0.0 or higher)

   -  CrossCore Embedded Studio (2.6.0 or higher)
   -  ADuCM302x DFP (2.0.0 or higher)
   -  ADICUP3029 BSP (1.0.0 or higher)
   -  Android IoTNode App (optional)
   -  Serial Terminal Program (Required for running in release mode only)

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Place the **(S5)** switch position to read "Wall/USB", and the **(S2)** switch position to read "USB".

.. image:: ../images/adicup3029_uart_switch_usb_revc.png
   :align: center
   :width: 200

-  Connect a jumper on **P1** between position **1-2** on EVAL-CN0397-ARDZ.
-  Plug the **EVAL-CN0397-ARDZ** shield into the **EVAL-ADICUP3029** board, using (P3), (P4), (P5), (P6), and (P7).
-   Plug in the micro USB cable into the **(P10)** USB port on the EVAL-ADICUP3029, and the other end into the PC or laptop.

Configuring the Software
------------------------

In the *cn0397_app.h* header files you can configure the following parameters:

-  **ADI_APP_DISPATCH_TIMEOUT** - *DISPATCH TIMEOUT* will define how often the data is sent over Bluetooth.
-  **ADI_APP_USE_BLUETOOTH** - *ENABLE BLUETOOTH* parameter - will either use Bluetooth or will have the option to print to console window in debug mode or terminal in release mode.

Calibration procedure
---------------------

The **CN0397** needs to be calibrated first before using it in order to achieve best performance. A system zero offset calibration needs to be run to cancel the offset for all of the channels.

Calibration, which is enabled by default, can be done by covering and not
allowing any light to reach the photodiodes within the first 5 second of the
program start.

Once all the channels have been calibrated, the circuit is now ready for use.
The output data will be available for each LED on android device if enabled.

.. image:: ../images/calibration_1.png
   :align: center

Outputting Data
---------------

Once the hardware setupand software is configured, user needs to select how they
want to view the data coming from Visible Light Detection\\Measurement
demo.(CN0397)

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

Debug Launch Mode
~~~~~~~~~~~~~~~~~

**Debug launch mode** is used when connected to the debugger. In debug mode, all the outputs are directed to the console window of the CrossCore tools via semihosting. The data is also sent by default to the IoTNode smart app (ADI_APP_USE_BLUETOOTH =1), but can be turned of if desired by setting ADI_APP_USE_BLUETOOTH = 0.

.. image:: ../images/debug_mode_ble.png
   :align: center

Figure shows when ADI_APP_USE_BLUETOOTH is set to 1, sensor data is sent to the
smart app. If you have the app installed on your phone, these figure shows the
output on android device.

.. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your
   phone.

   -  Simply open up the IoTNode application on your phone.
   -  "Scan" for nearby demos.
   -  Once you find your demo, click on it to open it up.

|image2| |image3|

Figure shows when ADI_APP_USE_BLUETOOTH is set to 0.

.. image:: ../images/debug_noble.png
   :align: center

Release Launch Mode
~~~~~~~~~~~~~~~~~~~

**Release launch mode** is used for running without the debugger connected. When in release mode, console output is redirected to UART. Bluetooth is enabled, and sensor data is sent to android application. If disabled, sensor data is directed only to the UART. If you are using the UART to make print to the PC/laptop, here are the settings your TCP client must be set too. Following is the UART configuration.

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

If *ADI_APP_USE_BLUETOOTH* is set to 1, BLE will advertise and UART terminal will wait for an connection. Now start the Android App and tap scan. Once device is found, App will show **CN0397 Light Demo** which is the Bluetooth device name for **ADICUP3029_CN0397** demo. Tap on it to connect. Sensor data can now be seen on Android App as well as terminal. If you have the app installed on your phone, these figure shows the output on android device.

.. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your
   phone.

   -  Simply open up the IoTNode application on your phone.
   -  "Scan" for nearby demos.
   -  Once you find your demo, click on it to open it up.

.. image:: ../images/release_mode_ble.png
   :align: center

|image4| |image5|

.. important::

   Visible Light Detection Demo (ADICUP3029_CN0397) only works with Android App.

Obtaining the Sotware
---------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0397.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0397** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0414 Hex File

   -  `AduCM3029_demo_cn0397.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0397.hex>`_

   Complete CN0414 Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0397 Source Code <projects/ADuCM3029_demo_cn0397>`

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

-  Make sure the target board is connected to workstation (via **USB** at P10) and using the tool bar, navigate to the small Debug icon\ |image6| and select the debugging session you created. The application will programmed and the program execution will stop at the beginning of the main() function.
-  Use step-by-step execution or directly run the program.

After completion of the steps above the program will be loaded onto the system
FLASH and it will run by default every time the board is powered up.

Project Structure
~~~~~~~~~~~~~~~~~

The **ADICUP3029_CN0397** is a C project that uses ADuCM3029 C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for ADC, SPI
read/write; configuring and reading from AD7798, UART read/write functions;
calibration and calculation of light information.

.. image:: ../images/c_1.png
   :align: left

cn0397_app.cpp and cn0397.h are the main source and header files related to **ADICUP3029_CN0397** application. Visible light sensor (CN0397) drivers are located in RTE/Sensor folder. All ADuCM3029 related drivers can be found under RTE/ADuCM3029 folder. BLE related files can be seen under RTE/Board_Support folder.

**pinmux.c** – contains GPIO pinmuxing for UART and SPI.

*End of Document*

.. |image1| image:: ../images/adt7420_demo_launch_configurations.png
   :width: 200

.. |image2| image:: ../images/screenshot_20170526-134458.png
   :width: 450

.. |image3| image:: ../images/screenshot_20170526-140134.png
   :width: 400

.. |image4| image:: ../images/screenshot_20170526-134458.png
   :width: 450

.. |image5| image:: ../images/screenshot_20170526-140134.png
   :width: 400

.. |image6| image:: ../images/bug.png
   :width: 30
