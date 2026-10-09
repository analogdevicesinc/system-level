Volatile Organic Compounds (VOC) Measurement Demo
=================================================

The **CN0395_example** is a volatile organic compounds (VOC) detector
demo project for the Arduino Uno base board with additional
:doc:`EVAL-CN0395-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0395>`,
created using the Arduino Genuino IDE.

General description
-------------------

This project is a good example of using ADI shields with Arduino boards for fast
and easy prototyping.

The **CN0395_example** project uses the
:doc:`EVAL-CN0395-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0395>`
which is a portable VOC detector which comes with a Figaro TGS8100 MOX
sensor.

.. image:: ../images/eval-cn0395-ardz.jpg
   :align: center

The TGS8100 sensor requires two voltage inputs: heater voltage (VH) and
circuit voltage (VC). The heater voltage (VH) is applied to the
integrated heater in order to maintain the sensing element at a specific
temperature which is optimal for sensing. The
:doc:`EVAL-CN0395-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0395>`
circuit provides the heater voltage (VH), by using :adi:`ADN8810` IDAC
as a programmable current source. The default full scale current in the
IDAC is 9.94mA and the default value of the RSN resistors is 41.2Ω.

The hardware also allows for two main modes of operation: heater mode
and sensor resistance measurement mode. In heater mode, the
:adi:`AD7988-1` ADC receives as input the heater voltage (VH) while in
sensor mode the input is the voltage from the sense circuit (VRS). The
switching is done by using :adi:`ADG884`. The full scale voltage measured
by the ADC is 4.096 V.

Moreover, the hardware includes a gain select circuit which can add
additional overlapping ranges if needed when performing a resistance
sensor measurement. :adi:`ADG758` 8-channel multiplexer is used to
accomplish this task.

TGS8100 sensor has a temperature and humidity dependency, therefore
temperature compensation is performed. The **EVAL-CN0395-ARDZ** shield
includes a temperature and humidity sensor (Sensirion SHT-30), which
operates on I2C bus.

The **CN0395_example** uses a UART interface (9600 baud rate and 8-bits
data length), as a command line interpreter, to send the results to
terminal window. Beside the interpreter processes several commands.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Arduino Uno board
   -  EVAL-CN0395-ARDZ
   -  USB type A to USB type B cable
   -  PC or Laptop with a USB port

-  Software

   -  CN0395_example software
   -  Arduino/Genuino IDE
   -  Arduino AVR Boards Built-In by Arduino package (1.6.23 or higher)

Setting up the hardware
-----------------------

-  Connect the EVAL-CN0411-ARDZ Shield to the Arduino connectors DIGITAL
   (PWM~), POWER, ANALOG IN and ICSP of the Arduino Uno board.
-  Plug in the USB cable from the PC to the Arduino Uno base board via the type
   B port on the board.

Obtaining the source code
-------------------------

We recommend not opening the project directly, but rather make a local copy in
your workspace and open it using Arduino/Genuino IDE.

The source code and include files of the **CN0395_example** can be found
on Github:

.. admonition:: Download
   :class: download

   :git-arduino:`CN0395_example at Github <gui+master:Arduino%20Uno%20R3/examples/CN0395_example>`

Configuring the Software Parameters
-----------------------------------

There are no configurations needed for this demo example.

Outputting Data
---------------

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

-  In order to view the data, you must flash the program to the Arduino
   Uno board by pressing the Upload button in the IDE.
-  Once complete Press the serial monitor button.
-  Make sure the UART settings are “Carriage return” and “9600 baud”.

Following is the UART configuration.

::

     Carriage return
     9600 baud

The application allows the user to select between the two modes of operation:

-  Heater mode (RH)
-  Sensor Resistance mode (RS)

Heater Mode (RH)
~~~~~~~~~~~~~~~~

The user can further choose the subroutine which determines the heater current
(IH):

|image1|

**voltage** is the routine for setting heater voltage to constant
voltage VH (the default value is VH = 1.8V). The relationship between
heater resistance RH and heater current IH or heater voltage VH is
nonlinear. Therefore the software runs in background several iterations
in order to get VH to the desired accuracy with a 0.5% max error.

**resistance** is the routine for setting the heater resistance to
constant resistance RH (the default is RH = 225Ω). For a heater
resistance RH, set IH = (RH – 110Ω)/14375 [Note: The slope of the RH
vs. IH curve is 115Ω/8mA = 14375Ω/A]. The software runs in background
several iterations in order to get RH to the desired accuracy with a
0.5% max error.

**temperature** is the routine of setting the heater temperature to
constant temperature TH (the default is TH = 360 C). This is done in
three steps:

-  The desired heater resistance RH_T is computed from
   RH_T = RH_A [ 1 + ALPHA*(RH_0/RH_A)*(T – T_A)], where:

   -  RH_A is the heater ambient temperature (measured at power up)
   -  RH_0 is the default heater resistance (110Ω @ 20°C)
   -  T is the desired heater temperature (user input)
   -  T_A is the ambient temperature (measured at power up)
   -  ALPHA is the constant 0.003074

-  The resulted RH is used to calculate IH and VH with constant
   resistance routine.
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

Sensor measurement is performed. The application can switch at any time
to this mode by pressing the <ENTER> key. The :adi:`AD7988-1` ADC
receives the voltage from the sense circuit (VRS). The switching is done
by using :adi:`ADG884`.

In background every time the application runs the gain-ranging algorithm and
determines RS and the gas concentration (C) measured in PPM (parts per million):

|image4|

RS reading can also be performed by typing <operation RS>, but it does the same
thing as pressing the <ENTER> key.

**Factory Calibration** The IDAC current from the ADN8810 is 1%
accurate, therefore a factory calibration must be performed. The routine
loads code 4095 into ADN8810 and reads the ADC, which ideally should be
9.94mA × 71.5Ω = 0.71V, or code [0.71/4.096] x 65,535 = 11,360. The
gain correction factor k1 = 11,360/CODEFS. It is recommended that this
is done only once. Follow the procedure:

-  Type <calibrate w>
-  Connect jumper P2 between P2-1 and P2-2, this connects the IOUT to
   the precision 71.5Ω resistor.
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

Project structure
-----------------

The CN0411_example is a C++ Arduino sketch.

This project contains: system initialization part - setting Digital IO pins in
the right mode; port configuration for SPI1, UART via Digital pin 0/Digital pin
1, I2C via SDA/SCL pins; SPI, UART, I2C read/write functions; AD7988 control,
ADN8810 control, SHT30 control and VOC concentration computation.

All files are in the same folder as the .ino file and include the source
and header files related to CN0395 software application. The
*Communication.cpp/h* files contain SPI, UART and I2C specific data, the
*AD7988.cpp/h* files contain the ADC control, the *ADN8810.cpp/h* files
contain the IDAC control, the *SHT30.c/h* files contain the
temperature/humidity sensor control, and the *CN0395.cpp/h* files contain
commands, configurations and computations specific to the VOC detector
application.

*End of Document*

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
