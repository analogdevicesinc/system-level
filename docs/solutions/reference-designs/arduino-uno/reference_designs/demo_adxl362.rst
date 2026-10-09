Acceleration Measurement Demo using the Arduino Uno
===================================================

The **ADXL362_example** is an acceleration measurement demo project for
the Arduino Uno base board with additional EVAL-ADXL362-ARDZ shield,
created using the Arduino IDE.

General Description/Overview
----------------------------

The **ADXL362_example** uses the
:doc:`EVAL-ADXL362-ARDZ shield </solutions/reference-designs/eval-adicup360/hardware/adxl362>`
which has an **ADXL362 3-axis MEMS accelerometer** and a incorporated
**NHD-C12832A1Z-NSW-BBW display** (128x32).

.. image:: ../images/img_20180123_170819.jpg
   :align: left
   :width: 400

The application reads the **X**, **Y**, and **Z** acceleration registers
each **500 [ms]**. The acceleration in the 3 axes is displayed in **[mG]**
on the LCD. Also this application demonstrates the usage of the motion
switch. Movement zones - **UP**, **DOWN**, **RIGHT**, **LEFT**, **CENTER**
- are displayed in the right side of the LCD.

The **EVAL-ADXL362-ARDZ** shield provide an internal temperature sensor
as an additional features which is read in the same software loop. The
value is displayed in ADC codes or in Celsius degrees. The temperature
**Treal** is derived from the ADC readings **Tadc** using the predefined
formula:

::

       Treal = (Tadc + ACC_TEMP_BIAS)/(1 / ACC_TEMP_SENSITIVITY)

Each **ADXL362** chip requires individual calibration which can be done
by setting the definitions *ACC_TEMP_BIAS* and *ACC_TEMP_SENSITIVITY*
parameters. Once the **ADXL362** chip is calibrated, the software can be
changed to display the actual temperature by selecting to display the
temperature in degrees.

.. image:: ../images/adxl362-demo.jpg
   :align: right
   :width: 300

The software puts the LCD in a "sleep" mode after **10 sec** if no
movement of the boards is present. The system "wakes-up" if the
acceleration on any axes is greater than **50 [mG]**. The threshold values
can be adjusted by the user.

The acceleration axes, the temperature values and the motion grid are displayed
as is presented in the picture on the right.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Arduino Uno Rev 3
   -  EVAL-ADXL362-ARDZ
   -  Type B to Type A USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADXL362_example sketch
   -  Arduino Interactive Development Environment(IDE)

Setting up the Hardware
-----------------------

-  Plug the **EVAL-ADXL362-ARDZ** shield on top of the **Arduino Uno**
   development board by matching up the **POWER, ANALOG, DIGI0, DIGI1**
   connectors.

   -  Note, the boards should only plug together one way, preventing reverse
      connections.

-  Set the jumpers on the EVAL-ADXL362-ARDZ shield as shown in the next figure.

|image1|

-  Plug in the Type B USB cable into the USB port on the Arduino Uno, and the
   other end into the PC or laptop.

Obtaining the Source Code
-------------------------

The source code and include files of the **ADXL362_example** can be found here:

.. admonition:: Download
   :class: download


   :git-arduino:`ADXL362_example at Github <gui+master:Arduino%20Uno%20R3/examples/ADXL362_example>`


Project Structure
-----------------

.. image:: ../images/drawing3.png
   :align: center
   :width: 700

The Arduino Sketch is used to load the example into Arduino IDE. The project is
composed of three main parts:

-  the main program (arduino sketch)
-  application layer (IC drivers and sensor data)
-  communication layer

Configuring the Software Parameters
-----------------------------------

Configure the temperature units in the *ADXL362.h* file.

::

   #define TEMP_ADC        1        /* 1 for ADC units or 0 for Celsius degrees */

Configure the ADXL362 Calibration Values in the *ADXL362.h* file. These
values will vary from sensor to sensor, but these are typical values from
the datasheet.

::

   #define ACC_TEMP_BIAS             (float)350
   #define ACC_TEMP_SENSITIVITY      (float)0.065

Set the Accelerometer Scan Time in the *ADXL362.h* file. This is how
often you read your axis and temperature data.(in ms)

::

   #define SCAN_SENSOR_TIME   500

Set the activity and inactivity thresholds for the ADXL362 in the
*ADXL362.h* file. These values are used to determine which acceleration
values the sensor can react at sleep/wake-up commands.(in mG)

::

   #define ACT_VALUE          50
   #define INACT_VALUE        50

Set the activity and inactivity time for the ADXL362 in the *ADXL362.h*
file. These values are used to determine sleep/wake-up intervals.(in ms)

::

   #define ACT_TIMER          50
   #define INACT_TIMER        50

Configure the Chip Select(CS) Pin for the ADXL362 in the
*Communication.h* file. Position of P9 header

::

   #define ADXL_CS_SEL     CSACC_PIN_P0_4     /* CSACC_PIN_P0_3 or CSACC_PIN_P0_4 */

Configure the Interrupt Pin from the ADXL362 in the *Communication.h*
file. Position of P7 header

::

   #define ADXL_INT_SEL     INTACC_PIN_1    /* INTACC_PIN_1 or INTACC_PIN_2 */

Configure the Chip Select(CS) Pin for the LCD Screen in the
*Communication.h* file. Position of P8 header

::

   #define LCD_CS_SEL      CSLCD_PIN_P1_4     /* CSLCD_PIN_P2_2 or CSLCD_PIN_P1_4 */

Configure the Reset Pin from the LCD Screen in the *Communication.h*
file. Position of P6 header

::

   #define LDC_RST_SEL     RSLCD_PIN_IOREF    /* RSLCD_PIN_IOREF or RSLCD_PIN_P1_1 */

Compiling, Verifying, and Programming
-------------------------------------

-  Once the project has been imported and the software parameters have
   been appropriately configured, you must Compile/Verify the project
   within the Arduino IDE. You can do this by clicking on the Sketch
   menu, and then on the *Compile/Verify* option.
-  Once the project is compiled and free of errors, you can now upload
   the project to the Arduino Uno. Click on the Sketch menu item, and
   then click *Upload*.

These two steps can also be done using the quick buttons on the Arduino sketch.
Check out the image below for locations of the quick buttons.

.. image:: ../images/arduino_ide_verify_upload_buttons.png
   :align: center
   :width: 500

Outputting Data
---------------

Data is output using the USB cable from the Arduino to the PC. The USB port acts
as a serial terminal to display the data being transmitted via UART. Opening the
serial terminal window from the Arduino IDE is very easy, simply click on the
button shown in the picture below.

.. image:: ../images/arduino_ide_serial_terminal_button.png
   :align: center
   :width: 500

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

You may need to configure the serial terminal depending on the current settings
of the Arduino IDE. Make sure the settings are as follows:

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

Tools Download and Help
-----------------------

The Arduino tools are easy to use, and there are many tutorials and users guides
to help learn how to use the Arduino IDE.

For more information on how to use the tool basics, please check out the
`Arduino tutorials page. <https://www.arduino.cc/en/Tutorial/HomePage>`_

.. admonition:: Download
   :class: download

   To download the Arduino tools, check out the
   `Arduino software page. <https://www.arduino.cc/en/Main/Software>`_

*End of Document*

.. |image1| image:: ../images/eval-adxl362-ardz_default_software_config.png
   :width: 360
