Toxic Gas (CO) Measurement Demo
===============================

The **ADuCM360_demo_cn0357** is a toxic gas(CO) detector demo project for the EVAL-ADICUP360 base board with additional :adi:`EVAL-CN0357-ARDZ shield <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>`, created using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General description
-------------------

This project is a good example for how to use :doc:`EVAL-ADICUP360 board </solutions/reference-designs/eval-adicup360/hardware/base_board>` in different combinations with various shield boards. It expand the list of possible applications that can be done with the base board.

The **ADuCM360_demo_cn0357** project uses the :adi:`EVAL-CN0357-ARDZ shield <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>` which is a single-supply, low noise, portable gas detector circuit using an electrochemical sensor.

.. image:: ../images/cn0357_demo_board.png
   :align: center
   :width: 550

The :adi:`EVAL-CN0357-ARDZ shield <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>` circuit provides a potentiostatic circuit for biasing the electrochemical sensor, along with a programmable TIA and 16-bit Sigma-Delta ADC. The TIA converts the small currents passing in the sensor to a voltage that can be read by the ADC. The 16-bit ADC value is received via SPI interface of the EVAL-ADICUP360 board, where the gas concentration is computed.

.. image:: ../images/cn0357_demo_terminalwindow1.png
   :align: right
   :width: 550

The **ADuCM360_demo_cn0357** application configures the necessary components, processes ADC output value and make all necessary conversions in order to provide the gas concentration. A UART interface (9600 baud rate and 8-bits data length) is used to send the results to terminal window: ADC Data Register **codes**, ADC Input Voltage **volts**, and Gas Concentration **Parts Per Million(PPM)** are the outputs provided in the terminal window.

At the start of the project, the software computes the necessary parameters and configure the digital rheostat(AD5270) of the TIA. The required parameters are the sensor sensitivity and sensor range. These can be modified by changing the values of the constants **SENSOR_SENSITIVITY** and **SENSOR_RANGE** found in the **CN0357.h** header file of the project. See the "*Project Structure*" section for more details.

Once configuration is complete, the software remains in a loop and continuously reads data from the ADC. Data can be read from a terminal by pressing the **<Enter>** key on the computer's keyboard.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0357-ARDZ
   -  Electrochemical Gas Sensor (included with CN0357)
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADuCM360_demo_cn0357 software
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

-  Connect the **EVAL-CN0357-ARDZ** to the Arduino connectors **P2, P5, P6, P7, P8** of the **EVAL-ADICUP360** board.
-  Connect an acceptable 7V-12V power supply into the P11 barrel jack of the
   EVAL-ADICUP360

.. important::

   Extremely important to plug in an acceptable power supply to the barrel jack
   P11 to supply power for the EVAL-CN0357-ARDZ. The boards will not work if you
   try only to power it from the DEBUG_USB or the USER_USB.

-  Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB.(P14)

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
CN0357.

-  Dragging and Dropping the .Bin to the MBED drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_cn0357** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0357 Bin File

   
   -  `ADuCM360_demo_cn0357.Bin <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0357.bin>`_
   
   Complete CN0357 Source Files
   
   -  :git-EVAL-ADICUP360:`ADuCM360_demo_cn0357 Source Code <projects/ADuCM360_demo_cn0357>`
   

.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

-  **Sensor Range** - SENSOR_RANGE - maximum value of the gas conentration (ppm) that can be detected by the electrochemical gas sensor being used (*CN0357.h*).

::

       #define SENSOR_RANGE     2000

-  **Sensor Sensitivity** - SENSOR_SENSITIVITY - sensitivity (nA/ppm) of the electrochemical sensor being used (*CN0357.h*).

::

       #define SENSOR_SENSITIVITY  65

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

-  The user must press the **<ENTER>** key every time they want new results.

.. image:: ../images/cn0357_demo_terminalwindow1.png
   :align: center
   :width: 550

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

The **ADuCM360_demo_cn0357** project use ADuCM36x C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for SPI1, UART
via P0.6/P0.7; SPI, UART read/write functions, AD7790 control, AD5270 control
and gas concentration computation.

In the **src** and **include** folders you will find the source and header files related to CN0357 software application. The *Communication.c/h* files contain SPI and UART specific data, the *AD7790.c/h* files contain the ADC control, the *AD5270.c/h* files contain the rheostat control and the *CN0357.c/h* files contain configurations and computations specific to the gas detector application.

.. image:: ../images/cn0357_demo_projecttree1.png
   :align: left
   :width: 340

The **RTE** folder contains device and system related files:

-  **Device Folder** – contains low levels drivers for ADuCM360 microcontroller.(try not to edit these files)
-  **system.rteconfig** - Allows the user to select the peripherial components they need, along with the startup and ARM cmsis files needed for the project.

