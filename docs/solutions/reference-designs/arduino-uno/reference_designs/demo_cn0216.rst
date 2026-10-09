Weigh Scale Measurement Demo using Arduino Uno
==============================================

The **CN0216_example** is a weigh scale measurement demo project for the
Arduino Uno base board with additional
:adi:`EVAL-CN0216-ARDZ shield <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0216-ARDZ.html>`,
created using the Arduino IDE.

General Description/Overview
----------------------------

The **CN0216_example** project uses the
:adi:`EVAL-CN0216-ARDZ shield <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0216-ARDZ.html>`
which is a precision weigh scale system using a **24-bits** sigma-delta
converter, and auto-zero amplifiers providing high gain for the bridge
sensor input

.. image:: ../images/cn0216_hw_stacked.jpg
   :align: left
   :width: 550

The CN0216 circuit translates the resistance changes on the bridge into very
small voltages. The bridge is excited by a regulated 5V and that determines the
full scale range of the bridge output. Those values are passed through very low
noise, auto zero amplifiers to remove as many error sources as possible before
being gained up to levels that will be compatible with the ADC. The 24-bit ADC
value is received via SPI interface of the EVAL-ADICUP360 board.

.. image:: ../images/cn0216_putty_output.png
   :align: right
   :width: 550

The **CN0216_example** application processes ADC output value and make
all necessary conversions in order to provide the weight results. A UART
interface (9600 baud rate and 8-bits data length) is used to send the
results to terminal window: ADC Data Register **codes**, ADC Input
Voltage **volts**, and Sensor Input Weight **grams** are the outputs
provided in the terminal window.

At the start of the project, a calibration of the upper and lower input
range of the weigh scale is taken to remove both offset and gain errors in
the circuit, providing the most accurate weigh scale measurements possible.
Make sure you open up the serial terminal to your PC in order to do the
calibration. Once the program is running, it will ask you to make the zero
scale calibration, you **MUST** press <ENTER> to begin the zero scale
calibration(takes about 5 seconds). Once that calibration has taken place,
the serial terminal will prompt you to add the calibration weight to the
scale and then press <ENTER> to make the full scale calibration(again
takes about 5 seconds). Those measurements are averaged over 100 samples
and then stored into memory as the upper and lower calibration
coefficients.

Once calibration is complete, measurements of the output values (weights and
conversion information) are displayed every time you press <ENTER> key from the
keyboard. Measurements should be between the lower and upper calibration limit
can be made at the beginning of the program.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Arduino Uno Rev 3
   -  EVAL-CN0216-ARDZ
   -  4- or 6- Wire wheatstone bridge weigh scale
   -  Type B to Type A USB cable
   -  PC or Laptop with a USB port

-  Software

   -  CN0396_example sketch
   -  Arduino Interactive Development Environment(IDE)

Setting up the Hardware
-----------------------

-  Plug the **EVAL-CN0216-ARDZ** shield on top of the **Arduino Uno**
   development board by matching up the **POWER, ANALOG, DIGI0, DIGI1**
   connectors.

   -  Note, the boards should only plug together one way, preventing reverse
      connections.

-  Connect your weigh scale to the EVAL-CN0216-ARDZ via **()**, make
   sure you pay attention to the pinout which can be found on the
   :doc:`CN0216 hardware page </solutions/reference-designs/eval-adicup360/hardware/cn0216>`.
-  Connect an acceptable 7V-12V power supply into the power jack of the Arduino
   Uno

.. important::

   Extremely important to plug in an acceptable power supply to the power jack
   for the EVAL-CN0216-ARDZ. The boards will not work if you try only to power
   it from the USB.

-   Plug in the Type B USB cable into the USB port on the Arduino Uno, and the
    other end into the PC or laptop.

Obtaining the Source Code
-------------------------

The source code and include files of the **CN0216_example** can be found here:

.. admonition:: Download
   :class: download


   :git-arduino:`CN0216_example at Github <gui+master:Arduino%20Uno%20R3/examples/CN0216_example>`


Project Structure
-----------------

.. image:: ../images/drawing2.png
   :align: center
   :width: 700

The Arduino Sketch is used to load the example into Arduino IDE. The project is
composed of three main parts:

-  the main program (arduino sketch)
-  application layer (IC drivers and sensor data)

Configuring the Software Parameters
-----------------------------------

There are no software configurations for this particular project.

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
