.. _arduino-uno reference_designs demo_cn0397:

RGB Visible Light Detection Demo using the Arduino Uno
======================================================

The **CN0397_example** is a RGB light detection demo project for the
**Arduino Uno** base board with additional **EVAL-CN0397-ARDZ** shield,
using the Arduino IDE.

General Description/Overview
----------------------------

The **CN0397_example** project uses the
:adi:`EVAL-CN0397-ARDZ shield <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0397>`
which is a single-supply, low power, low noise, 16-bit light detector
utilizing wavelength specific photodiodes. The photodiodes used in this
circuit are sensitive at different wavelengths, to read light intensity
levels over the visible light spectrum where the plants are
photosynthetically active.

The **EVAL-CN0397-ARDZ** board uses :adi:`ad8500`, a low power,
precision CMOS op amp with a low input bias current of a typical 1pA
which is used in a transimpedance amplifier configuration to convert the
current output of the photodiodes into voltage. It also features
:adi:`ad7798` a 3-channel, low noise, low power 16-bit ADC that converts
the analog voltage into digital data in for the processing of data into
light intensity. The circuit utilizes RGB photodiodes from Everlight with
their peak sensitivities 620nm (**R**), 550nm (**G**) and 470nm (**B**).

The **CN0397_example** application perform ADC readings for all 3
channels, processes them and make all necessary calculations in order to
provide light intensity and light concentration for each color.

.. image:: ../images/img_20180123_171237.jpg
   :align: left
   :width: 500

The 16-bits ADC data are received using **SPI interface** of the
EVAL-ADICUP360 board. The **UART interface** (**9600** baud rate and
**8-bits** data length) is used to send(and to receive) data to (from)
a terminal window.

**Light intensity** [Lux] is calculated using ADC output value for
selected channel and a constant value for each color:

::

   Light Intensity = CODE * Light intensity Constant

**Light Concentration** [%] is calculated based on the light intensity
and optimal level for each color:

::

   Light concentration = Intensity*100/Optimal Level

Beside **light intensity** and **light concentration** values, for each
channel will be displayed a **colored bar** in [0%, 100%] format for
light concentration representation. It will inform the user when the
concentration for a specific channel will reach **100%**. Application
offer the possibility to perform a system offset calibration for each
**RGB channel**. All calculation are using data specific to each color
of the used LEDs:

.. image:: ../images/table.png
   :align: center
   :width: 600

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  Arduino Uno Rev 3
   -  EVAL-CN0397-ARDZ
   -  Type B to Type A USB cable
   -  PC or Laptop with a USB port

-  Software

   -  CN0397_example sketch
   -  Arduino Interactive Development Environment(IDE)

Setting up the Hardware
-----------------------

-  Plug the **EVAL-CN0397-ARDZ** shield on top of the **Arduino Uno**
   development board by matching up the **POWER, ANALOG, DIGI0, DIGI1**
   connectors.

   -  Note, the boards should only plug together one way, preventing reverse
      connections.

-  Connect a jumper on **P1** between position **1-2** on
   EVAL-CN0397-ARDZ.
-   Plug in the Type B USB cable into the USB port on the Arduino Uno, and the
    other end into the PC or laptop.

Obtaining the Source Code
-------------------------

The source code and include files of the **CN0397_example** can be found here:

.. admonition:: Download
   :class: download


   :git-arduino:`CN0397_example at Github <gui+master:Arduino%20Uno%20R3/examples/CN0397_example>`


Project Structure
-----------------

.. image:: ../images/arduino2.png
   :align: center
   :width: 700

The Arduino Sketch is used to open the example into Arduino IDE. The project is
composed of three main parts:

-  the main program (arduino sketch)
-  application layer
-  communication layer
-  driver layer (IC drivers and sensor data)

Configuring the Software Parameters
-----------------------------------

There are no software configurations for this particular project.

Calibration procedure
---------------------

The **CN0397_example** needs to be calibrated first before using it in
order to achieve best performance. A system zero offset calibration needs
to be run to cancel the offset for all of the channels.

Calibration, which is enabled by default, can be done by covering and not
allowing any light to reach the photodiodes within the first 5 second of the
program start.

Once all the channels have been calibrated, the circuit is now ready for use.
The output data will be available for each LED on android device if enabled.

.. image:: ../images/calibration_1.png
   :align: center

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
