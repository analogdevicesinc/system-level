Volatile Organic Compounds (VOC) Measurement Demo
=================================================

The **ADuCM360_demo_cn0395** is a volatile organic compounds (VOC) detector demo project for the EVAL-ADICUP360 base board with additional :adi:`EVAL-CN0395-ARDZ shield <CN0395>`, created using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General description
-------------------

This project is a good example for how to use :doc:`EVAL-ADICUP360 board </solutions/reference-designs/eval-adicup360/hardware/base_board>` in different combinations with various shield boards. It expand the list of possible applications that can be done with the base board.

The **ADuCM360_demo_cn0395** project uses the :adi:`EVAL-CN0395-ARDZ shield <CN0395>` which is a portable VOC detector which comes with a Figaro TGS8100 MOX sensor.

.. image:: ../images/eval-cn0395-ardz.jpg
   :align: center

The TGS8100 sensor requires two voltage inputs: heater voltage (VH) and circuit voltage (VC). The heater voltage (VH) is applied to the integrated heater in order to maintain the sensing element at a specific temperature which is optimal for sensing. The :adi:`CN0395` circuit provides the heater voltage (VH), by using :adi:`ADN8810` IDAC as a programmable current source. The default full scale current in the IDAC is 9.94mA and the default value of the RSN resistors is 41.2Ω.

The hardware also allows for two main modes of operation: heater mode and sensor resistance measurement mode. In heater mode, the :adi:`AD7988-1` ADC receives as input the heater voltage (VH) while in sensor mode the input is the voltage from the sense circuit (VRS). The switching is done by using :adi:`ADG884`. The full scale voltage measured by the ADC is 4.096 V.

Moreover, the hardware includes a gain select circuit which can add additional overlapping ranges if needed when performing a resistance sensor measurement. :adi:`ADG758` 8-channel multiplexer is used to accomplish this task.

TGS8100 sensor has a temperature and humidity dependency, therefore temperature compensation is performed. The **ADuCM360_demo_cn0395** shield includes a temperature and humidity sensor (Sensirion SHT-30), which operates on I2C bus.

The **ADuCM360_demo_cn0395** uses a UART interface (9600 baud rate and 8-bits data length), as a command line interpreter, to send the results to terminal window. Beside the interpreter processes several commands.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0395-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADuCM360_demo_cn0395 software
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
   :width: 600

-  Connect the **EVAL-CN0395-ARDZ** to the Arduino connectors **P2, P5, P6, P7, P8** of the **EVAL-ADICUP360** board.
-  Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB.(P14)

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
CN0395.

-  Dragging and Dropping the .Bin to the MBED drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_cn0395** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0395 Bin File

   
   -  `ADuCM360_demo_cn0395.Bin <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0395.bin>`_
   
   Complete CN0395 Source Files
   
   -  :git-EVAL-ADICUP360:`ADuCM360_demo_cn0395 Source Code <projects/ADuCM360_demo_cn0395>`
   

.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>`

Configuring the Software Parameters
-----------------------------------

There are no configurations needed for this demo example.

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

The application allows the user to select between the two modes of operation:

-  Heater mode (RH)
-  Sensor Resistance mode (RS)

Heater Mode (RH)
~~~~~~~~~~~~~~~~

The user can further choose the subroutine which determines the heater current
(IH):

|image1|

**voltage** is the routine for setting heater voltage to constant voltage VH (the default value is VH = 1.8V). The relationship between heater resistance RH and heater current IH or heater voltage VH is nonlinear. Therefore the software runs in background several iterations in order to get VH to the desired accuracy with a 0.5% max error.

**resistance** is the routine for setting the heater resistance to constant resistance RH (the default is RH = 225Ω). For a heater resistance RH, set IH = (RH – 110Ω)/14375 [Note: The slope of the RH vs. IH curve is 115Ω/8mA = 14375Ω/A]. The software runs in background several iterations in order to get RH to the desired accuracy with a 0.5% max error.

**temperature** is the routine of setting the heater temperature to constant temperature TH (the default is TH = 360 C). This is done in three steps:

-  The desired heater resistance RH_T is computed from RH_T = RH_A [ 1 + ALPHA*(RH_0/RH_A)*(T – T_A)], where:

   -  RH_A is the heater ambient temperature (measured at power up)
   -  RH_0 is the default heater resistance (110Ω @ 20°C)
   -  T is the desired heater temperature (user input)
   -  T_A is the ambient temperature (measured at power up)
   -  ALPHA is the constant 0.003074

-  The resulted RH is used to calculate IH and VH with constant resistance routine.
-  The resulted VH is further adjusted by using the constant heater voltage
   routine.

**current** simply sets the IDAC to the desired current.

After the completion of the routine, the application displays the measured
values: RH_A (Ambient Heater Res ), VH (heater voltage), IH (heater current), RH
(heater resistance), T_A (ambient temperature), HUM (ambient humidity), PH
(heater power consumption), TH (heater temperature), ADC data (raw data read
from ADC in hex), Ro ( sensor resistance measured in clean air).

|image2|

At power up, the application starts in constant current mode and sets the
default current to 8mA. Furthermore, it is assumed that the measurement circuit
is placed in clean air, therefore we measure and store the sensor resistance in
clean air (Ro). After each heater measurement mode change, it is assumed that
the board is placed in clean air, and the Ro value is updated. This is required,
because Ro is a function of the heater temperature.

|image3|

Sensor Resistance mode (RS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sensor measurement is performed. The application can switch at any time to this mode by pressing the <ENTER> key. The :adi:`AD7988-1` ADC receives the voltage from the sense circuit (VRS). The switching is done by using :adi:`ADG884`.

In background every time the application runs the gain-ranging algorithm and
determines RS and the gas concentration (C) measured in PPM (parts per million):

|image4|

RS reading can also be performed by typing <operation RS>, but it does the same
thing as pressing the <ENTER> key.

**Factory Calibration** The IDAC current from the ADN8810 is 1% accurate, therefore a factory calibration must be performed. The routine loads code 4095 into ADN8810 and reads the ADC, which ideally should be 9.94mA × 71.5Ω = 0.71V, or code [0.71/4.096] x 65,535 = 11,360. The gain correction factor k1 = 11,360/CODEFS. It is recommended that this is done only once. Follow the procedure:

-  Type <calibrate w>
-  Connect jumper P2 between P2-1 and P2-2, this connects the IOUT to the precision 71.5Ω resistor.
-  Press <c> key when ready
-  Power Off -> On

.. image:: ../images/calibrate_w.jpg
   :align: center
   :width: 850

From this point on, K1 is stored in permanent memory and applied to currents
that are input. To read the gain correction factor from memory, type <calibrate
r>.

|image5|

**Help**

Type <help> to see the available commands:

|image6|

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

The **ADuCM360_demo_cn0395** project use ADuCM36x C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, setting
system clock, enabling clock for peripherals; port configuration for SPI1, UART
via P0.6/P0.7, I2C via P2.0/P2.1; SPI, UART, I2C read/write functions; Flash
read/write functions, AD7988 control, ADN8810 control, SHT30 control and VOC
concentration computation.

In the **src** and **include** folders you will find the source and header files related to CN0395 software application. The *Communication.c/h* files contain SPI, UART and I2C specific data, the *AD7988.c/h* files contain the ADC control, the *ADN8810.c/h* files contain the IDAC control, the *SHT30.c/h* files contain the temperature/humidity sensor control, the *Flash.c/h* files contain helper functions to read/write to the permanent memory, and the *CN0395.c/h* files contain commands, configurations and computations specific to the VOC detector application.

.. image:: ../images/proj_struct.jpg
   :align: left
   :width: 340

The **RTE** folder contains device and system related files:

-  **Device Folder** – contains low levels drivers for ADuCM360 microcontroller.(try not to edit these files)
-  **system.rteconfig** - Allows the user to select the peripherial components they need, along with the startup and ARM cmsis files needed for the project.

.. |image1| image:: ../images/rh_mode.jpg
   :width: 850

.. |image2| image:: ../images/constant_voltage.jpg
   :width: 850

.. |image3| image:: ../images/power_up.jpg
   :width: 850

.. |image4| image:: ../images/rs_mode_new.png
   :width: 850

.. |image5| image:: ../images/calibrate_read.jpg
   :width: 850

.. |image6| image:: ../images/help.jpg
   :width: 850
