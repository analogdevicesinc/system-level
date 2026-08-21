pH Monitor with Temperature Compensation Demo
=============================================

The **ADuCM360_demo_cn0326** is a pH monitor with automatic temperature compensation demo project, for the EVAL-ADICUP360 base board with additional EVAL-CN0326-PMDZ pmod, created using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General description
-------------------

This project is a good example for how to use :doc:`EVAL-ADICUP360 board </solutions/reference-designs/eval-adicup360/hardware/base_board>` in different combinations with pmod boards. It expand the list of possible applications that can be done with the base board.

The **ADuCM360_demo_cn0326** project uses the :adi:`EVAL-CN0326-PMDZ pmod <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0326>` which is a pH sensor signal conditioner and digitizer with automatic temperature compensation.

.. image:: ../images/cn0326_hw_connected.jpg
   :align: left
   :width: 600

The CN0326 circuit provides a complete solution for pH sensors with internal resistance between **1 MΩ** and several **GΩ**. It consist of **pH probe** buffer, **Pt1000 RTD** for temperature compensation and **24-bits ADC** with 3 differential analog inputs.

The pH probe consists of a glass measuring electrode and a reference electrode, which is analogous to a battery. When the probe is place in a solution, the measuring electrode generates a voltage depending on the hydrogen activity of the solution, which is compared to the potential of the reference electrode. As the solution becomes more **acidic** (pH < 7) the potential of the glass electrode becomes more positive (**+mV**) in comparison to the reference electrode; and as the solution becomes more **alkaline** (pH > 7) the potential of the glass electrode becomes more negative (**−mV**) in comparison to the reference electrode.

The change in temperature of the solution changes the activity of its hydrogen ions. When the solution is heated, the hydrogen ions move faster which result in an increase in potential difference across the two electrodes. In addition, when the solution is cooled, the hydrogen activity decreases causing a decrease in the potential difference. Electrodes are designed ideally to produce a zero volt (**0 V**) potential when placed in a buffer solution with a pH of 7 (**neutral** pH).

The **EVAL-CN0326-PMDZ** comes with an evaluation software which can help you to test and to calibrate your pmod before you use it.

.. note::

   Please visit `CN0326 Software User Guide page <https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0326>`_ to find out how to get and how to use the CN0326 evaluation software.

The potential changes are outputted as ADC 24-bits value which is received via
SPI interface of the EVAL-ADICUP360 board. The ADC analog differential channels
are:

-  **AIN1(+)/AIN1(-)** - pH probe (voltage full range: ±414 mV at 25°C to ±490 mV at 80°C)
-  **AIN2(+)/AIN2(-)** - Pt1000 RTD (voltage full range: 210 mV to 290 mV with 210 μA excitation current)
-  **AIN3(+)/AIN3(-)** - Bias current (used to minimized tne voltage errors)

.. image:: ../images/cn0326_demo_2.png
   :align: right
   :width: 549

The **ADuCM360_demo_cn0326** application purchase ADC outputs from input channels, calculates voltage, temperature and pH values. You can choose to use internal excitation current of the ADC (IOUT2) or calculate bias current of the circuit (see *USE_IOUT2* parameter).

A UART interface (9600 baud rate and 8-bits data length) is used, as a command line interpreter, to send the results to terminal window: **temperature** and **ph** values. Beside this two the interpreter process other three commands: **help**, **calibrate** channel/channels and ADC **reset**.

To start the command line interpreter you need to press ENTER key (CR) from the
keyboard and after that just type in <help> to see available commands. The
output data are send via UART using semihosting.

.. note::

   The calibrate command perform an internal zero and full scale calibration of the selected channel/channels (:adi:`AD7793 Datasheet <media/en/technical-documentation/data-sheets/AD7792_7793.pdf>`).

The project uses below formula to determine output **ADC code** for an input voltage on either channel:

.. image:: ../images/cn0326_demo_2_1.png
   :align: left
   :width: 250

**AIN** - analog input voltage

**GAIN** - gain value in the in-amp setting

**N** - ADC resolution (24)

The **temperature** value is calculated using RTD resistance value and it varies from 0°C (1000 Ω) to 100°C (1385 Ω):

.. image:: ../images/cn0326_demo_2_2.png
   :align: left
   :width: 240

**Rrtd** - RTD resistance at T°C

**Rmin** - RTD resistance at 0°C

**α** - temperature coefficient (0.00385 Ω/Ω/°C)

To calculate **pH** value is used Nernst equation:

|image1| **E** - voltage of the hydrogen electrode with unknown activity

**α** - zero point tolerance (±30 mV)

**T** - ambient temperature in °C

**n** - valence, number of charges on ion (1 at 25 °C)

**F** - Faraday constant (96485 coulombs/mol)

**R** - Avogadro's number (8314 mV-coulombs /°K mol)

**pHiso** - reference hydrogen ion concentration (7)

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0326-PMDZ
   -  pH Probe
   -  PT100 Temperature Probe
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADuCM360_demo_cn0326 software
   -  CrossCore Embedded Studio (2.7.0 or higher)
   -  ADuCM36x DFP (1.0.2 or higher)
   -  CMSIS ARM Pack (4.3.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the hardware
-----------------------

-  To program the base board, set the jumpers/switches as shown in the next
   figure. The important jumpers/switches are highlighted in red.

.. image:: ../images/cn0336_demo_3.png
   :align: center
   :width: 500

-  Connect the **EVAL-CN0326-PMDZ** to the SPI PMOD connector **P4** of the **EVAL-ADICUP360** board.
-  Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB.(P14)

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
CN0326.

-  Dragging and Dropping the .Bin to the MBED drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_cn0326** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0326 Bin File

   
   -  `ADuCM360_demo_cn0326.Bin <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0326.bin>`_
   
   Complete CN0326 Source Files
   
   -  :git-EVAL-ADICUP360:`ADuCM360_demo_cn0326 Source Code <projects/ADuCM360_demo_cn0326>`
   

.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

-  **ADC gain** - AD7793_GAIN - set gain value for AD7793 converter (*AD7793.h*).

::

      #define AD7793_GAIN              AD7793_GAIN_1

-  **Excitation current** - USE_IOUT2 - select if you want to use bias current from the AIN3 channel: YES or you want to use internal excitation current, 210 µA: NO(*CN0326.h*).

::

      #define  USE_IOUT2         NO

-  **Zero point tolerance** - TOLERANCE - tolerance used in Nernst equation (*CN0326.h*).

::

       #define  TOLERANCE            0

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

-  The user must press the **<ENTER>** key to start the program.
-  To get to the command menu the user must type **<help>** into the serial program.
-  Semihosting must be enabled to see data at the console window.

Available commands
~~~~~~~~~~~~~~~~~~

============= ===========================================
Command       Description
============= ===========================================
*help*        Display available commands
*calibrate*   Calibrate selected channels or all channels
              <*ch*> = AIN1, AIN2, AIN3, or all
*ph*          Display pH value
*temperature* Display temperature value
*reset*       Reset ADC converter
============= ===========================================

.. image:: ../images/cn0326_demo_2.png
   :align: center
   :width: 549

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

The **ADuCM360_demo_cn0326** project use ADuCM36x C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for SPI0, UART
via P0.6/P0.7; SPI, UART read/write functions; AD7793 control, voltage
conversion, command interpreter, temperature and pH calculations.

In the **src** and **include** folders you will find the source and header files related to CN0326 software application. The *Communication.c/h* files contain SPI and UART specific data, meanwhile the *AD7793.c/h* files contain the ADC control data and the *CN0326.c/h* files contain the pH monitor application data.

.. image:: ../images/cn0326_demo_5.png
   :align: left
   :width: 330

The **RTE** folder contains device and system related files:

-  **Device Folder** – contains low levels drivers for ADuCM360 microcontroller.(try not to edit these files)
-  **system.rteconfig** - Allows the user to select the peripherial components they need, along with the startup and ARM cmsis files needed for the project.

.. |image1| image:: ../images/cn0326_demo_2_3.png
   :width: 361
