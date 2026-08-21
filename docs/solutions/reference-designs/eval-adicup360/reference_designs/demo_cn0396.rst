4 – Wire Electrochemical Dual Toxic Gas Demo
============================================

The **ADuCM360_demo_cn0396** is a dual toxic gas detector demo project, for the EVAL-ADICUP360 base board with additional EVAL-CN0396-ARDZ shield, created using the CrossCore Embedded Studios Interactive Development Environment.(IDE)

General description
-------------------

The **ADuCM360_demo_cn0396** project uses the :adi:`EVAL-CN0396-ARDZ shield <cn0396>` which is a single-supply, low noise, portable gas detector, using a **4-electrode electrochemical** sensor, for simultaneous detection of two distinct gases - for this example is used the Alphasense COH-A2 sensor, which detects carbon monoxide(**CO**) and hydrogen sulfide(**H2S**).

The **EVAL-CN0396-ARDZ** board provides a potentiostatic circuit for biasing the electrochemical sensor, along with dual programmable TIA's and 16-bit Sigma-Delta ADC. The TIA's convert the small currents passing in the sensor to a voltage that can be read by the :adi:`ad7798` a 3-channel, low noise, low power 16-bit ADC that converts the analog voltage into digital data. The **16-bit** ADC outputs are received via SPI interface of the EVAL-ADICUP360 board. An :adi:`ADT7310` digital **temperature sensor** is also included to measure ambient temperature in order for correction of temperature effects.

|image1| The **ADuCM360_demo_cn0396** application reads temperature value from ADT7310 and ADC values for each gas channel (CO and H2S), processes the values and make all necessary conversions in order to provide the gas concentrations. A **UART** interface (**115200** baud rate and **8-bits** data length) is used to send the results to terminal window. The output data will be displayed continuously considering a data refresh parameter (see *DISPLAY_REFRESH*).

Based on the **maximum sensor sensitivity** for each gas the system should be configured before using it. The application will calculate the gas concentration using sensor **gas sensitivity** and then compensate these values using measured temperature value.

.. note::

   Maximum sensitivity and gas sensitivity are dependent on sensor type. These
   value will need to be updated in case of using another sensor that the one
   presented here.

.. image:: ../images/cn0396_demo_3.png
   :align: center
   :width: 800

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0396-ARDZ
   -  Electrochemical Gas Sensor (included with CN0396)
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADuCM360_demo_cn0396 software
   -  CrossCore Embedded Studio (2.7.0 or higher)
   -  ADuCM36x DFP (1.0.2 or higher)
   -  CMSIS ARM Pack (4.3.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the hardware
-----------------------

-  To program the base board, set the jumpers/switches as shown in the next
   figure. The important jumpers/switches are highlighted in red.

.. image:: ../images/cn0216_hw_config.png
   :align: center
   :width: 500

-  Connect the **EVAL-CN0396-ARDZ** to the Arduino connectors **P2, P5, P6, P7, P8** of the **EVAL-ADICUP360** board.
-  Set the jumpers on EVAL-CN0396-ARDZ board, as shown in the picture below.

.. image:: ../images/cn0396_demo_4.png
   :align: center
   :width: 600

-  Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB.(P14)

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
CN0396.

-  Dragging and Dropping the .Bin to the MBED drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_cn0396** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0396 Bin File

   
   -  `ADuCM360_demo_cn0396.Bin <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0396.bin>`_
   
   Complete CN0396 Source Files
   
   -  :git-EVAL-ADICUP360:`ADuCM360_demo_cn0396 Source Code <projects/ADuCM360_demo_cn0396>`
   

.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

-  **Sensor Range** - CO_RANGE & H2S_RANGE - maximum value of the gas concentration (ppm) that can be detected by each of the electrodes of the electrochemical gas sensor being used (*CN0396.h*).

::

       #define CO_RANGE   1000
       #define H2S_RANGE  200

-  **Sensor Gas Sensitivity** - CO_SENS & H2S_SENS - sensitivity (nA/ppm) of each of the 2 electrodes of the electrochemical sensor being used (*CN0396.h*).

::

       #define CO_SENS    (75 * pow(10, -9))
       #define H2S_SENS   (800 * pow(10, -9))

-  **Maximum Sensor Gas Sensitivity** - MAX_CO_SENS & MAX_H2S_SENS - sensitivity (nA/ppm) of each of the 2 electrodes of the electrochemical sensor being used (*CN0396.h*).

::

       #define MAX_CO_SENS  (100 * pow(10, -9))
       #define MAX_H2S_SENS (1000 * pow(10, -9))

-  **Terminal refresh** - *DISPLAY_REFRESH* parameter - how often to refresh the output data - input time value in [msec] (*CN0396.h*).

::

       #define DISPLAY_REFRESH        500

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
     Stop: 1 bit
     Flow Control: none

-  The data output refreshes in the console window at the rate of the
   "display_refresh" parameter with the following results.

.. image:: ../images/cn0396_demo_3.png
   :align: center
   :width: 800

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

The **ADuCM360_demo_cn0396** is a C project which uses ADuCM36x C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for SPI1, UART
via P0.6/P0.7; SPI, UART read/write functions, AD7798 control, AD5270 and
ADT7310 control; gas concentration computation.

In the **src** and **include** folders you will find the source and header files related to CN0396 software application. The *Communication.c/h* files contain SPI and UART specific data, the *AD7798.c/h* files contain the ADC control, the *AD5270.c/h* files contain the rheostat control, the *ADT73100.c/h* files contain the temperature sensor control, and the *CN0396.c/h* files are for the gas calculations.

.. image:: ../images/cn0396_software_dir.png
   :align: left
   :width: 250

The **RTE** folder contains device and system related files:

-  **Device Folder** – contains low levels drivers for ADuCM360 microcontroller.(try not to edit these files)
-  **system.rteconfig** - Allows the user to select the peripherial components they need, along with the startup and ARM cmsis files needed for the project.

.. |image1| image:: ../images/cn0396_demo_1.png
   :width: 650
