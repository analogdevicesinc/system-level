AD5592/AD5593 PMOD Demo
=======================

The **ADuCM3029_demo_ad5592r_ad5593r** project provides a solution to control a configurable input/output system using the **EVAL-AD5592R-PMDZ** or the **EVAL-AD5593R-PMDZ** and the **EVAL-ADICUP3029**. Both boards use a minimalist 8-channel, 12-bit, configurable ADC/DAC/GPIO device with either a SPI interface for **EVAL-AD5592R-PMDZ** and I2C interface for **EVAL-AD5593R-PMDZ**. The boards are SPI and I2C, respectively, PMOD form factor.

General Description/Overview
----------------------------

The **ADuCM3029_demo_ad5592r_ad5593r** project uses the **EVAL-AD5592R-PMDZ** or **EVAL-AD5593R-PMDZ** to provide a low-cost alternatives to the full-featured product evaluation boards, with terminal block connections and no extra signal conditioning. The application makes full use of the configurable 8 channels capability of the AD5592R and AD5593R, as every channel can be individually set to be either ADC, DAC, input GPIO or output GPIO. This provides a compact and highly flexible solution to signal acquisition and output control.

The application is controlled by the user with a CLI implemented using the
serial UART core in the ADuCM3029 controller. The CLI is displayed on a
connected PC using a serial terminal connection.

The program is divided in 2 parts: the setup part in which the present module is discovered and the main process. |Main flow chart| To do the discovery routine in the setup stage, the application first initializes the board SPI driver and tries to do a write and a read to a register to see if any device responds. If there is no SPI the application does the same test for the I2C device. If no device is found the application returns with an error message displayed on the serial connection. If any of the devices is found the program displays the active device and continues to the main process loop. If both PMODs are connected at the same time the one with SPI will be activated. |image1| The main process loop starts with the mirror mode. This mode sets up 4 channels as input and the other 4 as output, and then mirrors the inputs on the outputs. For example, if input channel 0 is driven externally to 1V the corresponding output channel, channel 7, will be driven to 1V as well by the application. The channels are linked as follows:

-  Channel 0 (ADC) -> Channel 7 (DAC);
-  Channel 1 (ADC) -> Channel 6 (DAC);
-  Channel 2 (input GPIO) -> Channel 5 (output GPIO);
-  Channel 3 (input GPIO) -> Channel 4 (output GPIO).

More information about the CLI commands can be found :doc:`here </solutions/reference-designs/eval-adicup3029/reference_designs/demo_ad5592r_ad5593r>`.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-AD5592R-PMDZ or EVAL-AD5593R-PMDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad5592r_ad5593r demo application <projects/ADuCM3029_demo_ad5592r_ad5593r>`
   -  CrossCore Embedded Studio (2.8.0 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Connect **EVAL-AD5592R-PMDZ** or **EVAL-AD5593R-PMDZ** board to the **EVAL-ADICUP3029** as seen in the pictures below: |AD5592R-PMDZ connect|

|AD5593R-PMDZ connect|

EVAL-AD5593R-PMDZ conforms to Pmod spec 1.1.0. This is physically
compatible with Pmod platforms conforming to earlier Pmod specifications,
provided that the VCC, GND, SDA, SCL pins are aligned with the
corresponding signals on the platform board, leaving INT and RESET
disconnected as shown.

-  Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer.

|PC connect|

Refer to https://blog.digilentinc.com/announcing-the-digilent-pmod-interface-specification-1-1-0/
for details on the Pmod specification.

Configuring the Software
------------------------

The configuration parameters can be found in the **config.h** file.

**AD5593R_A0_STATE** - This define contains the logic state of the A0 pin of the AD5593R device. This pin factors in the device I2C address and is by default logic "0" so no change is necessary to the define. If the pin state is changed by moving the pull-down resistor to be a pull-up resistor, this define needs to be changed to logic "1" too for the program to work.

::

      #define AD5593R_A0_STATE 0

Outputting Data
---------------

Serial Terminal Setup
~~~~~~~~~~~~~~~~~~~~~

A serial terminal is an application that runs on a PC or laptop that is used to
display data and interact with a connected device (including many of the
Circuits from the Lab reference designs). The device's UART peripheral is most
often connected to a UART to USB interface IC, which appears as a traditional
COM port on the host PC/ laptop. (Traditionally, the device's UART port would
have been connected to an RS-232 line driver / receiver and connected to the PC
via a 9-pin or 25-pin serial port.) There are many open-source applications,
and while there are many choices, typically we use one of the following:

- `Tera Term <https://ttssh2.osdn.jp/index.html.en>`_
- `PuTTY <https://www.putty.org/>`_
- `RealTerm <https://realterm.sourceforge.io/>`_

Before continuing, please make sure you download and install one of the above
programs.

There are several parameters on all serial terminal programs that must be setup
properly in order for the PC and the connected device to communicate. Below are
the common settings that must match on both the PC side and the connected UART
device.

- **COM Port** - This is the physical connection made to your PC or Laptop,
  typically made through a USB cable but can be any serial communications cable.
  You can determine the COM port assigned to your device by visiting the device
  manager on your computer. Another method for identifying which COM port is
  associated with a USB-based device is to look at which COM ports are present
  before plugging in your device, then plug in your device, and look for a new
  COM port.
- **Baud Rate** - This is the speed at which data is being transferred from the
  connected device to your PC. These parameters must be the same on both devices
  or data will be corrupted. The default setting for most of the reference
  designs is 115200.
- **Data Bits** - The number of data bits per transfer. Typically UART transmits
  ASCII codes back to the serial port so by default this is almost always set to
  8-Bits.
- **Stop Bits** - The number of "stop" conditions per transmission. This is
  usually set to 1, but can be set to 2 for redundancy.
- **Parity** - Is a way to check for errors during the UART transmission.
  Unless otherwise specified, set parity to "none".
- **Flow Control** - Is a way to ensure that data between fast and slow devices
  on the same UART bus is not lost during transmission. This is typically not
  implemented in a simple system, and unless otherwise specified, set to "none".

In many instances there are other options that each of the different serial
terminal applications provide, such as **local line echo** or **local line
editing**, and features like this can be turned on or off depending on your
preferences.

**Example setup using PuTTY**

#. Plug in your connected device using a USB cable or other serial cable.
#. Wait for the device driver of the connected device to install on your PC or
   Laptop.
#. Open your device manager, and find out which COM port was assigned to your
   device.
#. Open up your serial terminal program (PuTTY for this example).
#. Click on the serial configuration tab or window, and input the settings to
   match the requirements of your connected device. The default baud rate for
   most of the reference designs is 115200. Make sure that you use the correct
   baud rate for your application.
#. Ensure you click on the checkboxes for **Implicit CR in every LF** and
   **Implicit LF in every CF**.
#. Ensure that local echo and line editing are enabled, so that you can see what
   you type and are able to correct mistakes. (Some devices may echo typed
   characters - if so, you will see each typed character twice. If this happens,
   turn off local echo.)

.. tip::

   If you see nothing in the serial terminal, try hitting the reset button on
   the embedded development board.

Available commands
~~~~~~~~~~~~~~~~~~

Typing **help** or **h** after initial calibration sequence will display the list of commands and their short versions. Bellow is the short command list:

+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command                    | Example   | Description                                                                                                                                                                                                                                                                                                                                                |
+============================+===========+============================================================================================================================================================================================================================================================================================================================================================+
| General commands           |           |                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *h*                        | h         | Display available commands.                                                                                                                                                                                                                                                                                                                                |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *stts*                     | stts      | Display parameters of the application.                                                                                                                                                                                                                                                                                                                     |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Single channel commands    |           |                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *ao* <*chan*> <*dac_code*> | ao 0 2000 | Set a channel as analog output (DAC channel) and set the output code.                                                                                                                                                                                                                                                                                      |
|                            |           | <*chan*> = channel to be set (0-7);                                                                                                                                                                                                                                                                                                                        |
|                            |           | <*dac_code*> = DAC code in decimal integer format (0-4095).                                                                                                                                                                                                                                                                                                |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *ai* <*chan*>              | ai 0      | Change the channel to analog input and read the ADC channel.                                                                                                                                                                                                                                                                                               |
|                            |           | <*chan*> = channel to be changed and read. (0-7).                                                                                                                                                                                                                                                                                                          |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *do* <*chan*> <*val*>      | do 7 1    | Change the channel to digital output and set it's state to HIGH or LOW.                                                                                                                                                                                                                                                                                    |
|                            |           | <*chan*> = channel to be changed (0-7).                                                                                                                                                                                                                                                                                                                    |
|                            |           | <*val*> = '0' or '1' for LOW or HIGH, respectively.                                                                                                                                                                                                                                                                                                        |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *di* <*chan*>              | di 5      | Change the channel to digital input and read it's state.                                                                                                                                                                                                                                                                                                   |
|                            |           | <*chan*> = channel to be changed and read. (0-7).                                                                                                                                                                                                                                                                                                          |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Mode commands              |           |                                                                                                                                                                                                                                                                                                                                                            |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *m*                        | m         | Start mirror mode. This mode sets 4 channels as input and 4 channels as output. Then the application reads the input channels and drives the corresponding output channel to the value read on the input channel. For example, if channel 0 reads 1V then the corresponding channel, channel 7, will output 1V. The channels are linked the following way: |
|                            |           | \* Channel 0 (ADC) → Channel 7 (DAC);                                                                                                                                                                                                                                                                                                                      |
|                            |           | \* Channel 1 (ADC) → Channel 6 (DAC);                                                                                                                                                                                                                                                                                                                      |
|                            |           | \* Channel 2 (input GPIO) → Channel 5 (output GPIO);                                                                                                                                                                                                                                                                                                       |
|                            |           | \* Channel 3 (input GPIO) → Channel 4 (output GPIO).                                                                                                                                                                                                                                                                                                       |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *t*                        | t         | Start production test mode. The following connections must be made:                                                                                                                                                                                                                                                                                        |
|                            |           | \* Channel 0 → Channel 7;                                                                                                                                                                                                                                                                                                                                  |
|                            |           | \* Channel 1 → Channel 6;                                                                                                                                                                                                                                                                                                                                  |
|                            |           | \* Channel 2 → Channel 5;                                                                                                                                                                                                                                                                                                                                  |
|                            |           | \* Channel 3 → Channel 4.                                                                                                                                                                                                                                                                                                                                  |
|                            |           | Test mode sets CH0:3 to DAC mode, CH4:7 to ADC mode. CH0:3 are set to 0.5V, 1V, 1.5V, 2V, and the voltages at CH4:7 are read back and compared to the expected value. A pass message is then displayed if all the values are read back correctly.                                                                                                          |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *ais* <*ch_no*>            | ais a     | Start streaming mode. This mode reads the selected ADC channel twice a second and outputs the data to the terminal.                                                                                                                                                                                                                                        |
|                            |           | <*chan*> = channel to be read (0-7) or all channels simultaneously (a).                                                                                                                                                                                                                                                                                    |
|                            |           | If the channel picked is not an ADC channel the terminal will show an appropriate message.                                                                                                                                                                                                                                                                 |
|                            |           | This command does not change the setting of the channels. The desired channels need to be set as ADC separately.                                                                                                                                                                                                                                           |
+----------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  For the "h", "stts", "m" and "t" commands press Enter without inserting any space afterwards.
-  For the "ao", "ai", "do" and "di" commands, to invoke in application
   instructions, write just the command without parameters, insert a space
   afterwards and press Enter.

.. image:: ../images/ad5593r_cli_example.png
   :align: center

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
AD5592/AD5593 PMOD.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_ad5592r_ad5593r** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt AD5592/AD5593 PMOD Hex File

   -  `AduCM3029_demo_ad5592r_ad5593r.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_ad5592r_ad5593r.hex>`_

   Complete AD5592/AD5593 PMOD Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_ad5592r_ad5593r Source Code <projects/ADuCM3029_demo_ad5592r_ad5593r>`

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

.. image:: ../images/ad559xr_project_structure.png
   :align: center

Project structure includes:

-  AD559xR driver module with files: ad5592r-base.c, ad5592r-base.h, ad5592r.c, ad5592r.h, ad5593r.c, ad5593r.h;
-  Main file ADuCM3029_demo_aiodiopdmz.c
-  Application module with files: aio_dio_pdmz.c, aio_dio_pdmz.h;
-  CLI module with files: cli.c, cli.h;
-  Configuration file config.h
-  Communication and GPIO driver module with files: platform_drivers.c, platform_drivers.h;
-  Power core initialization module with files: power.c, power.h;
-  Timer and delay driver module with files: timer.c, timer.h.

*End of Document*

.. |Main flow chart| image:: ../images/cn0414_main_flowchart.png
.. |image1| image:: ../images/ad55923r_discovery_routine.png
.. |AD5592R-PMDZ connect| image:: ../images/ad5592r_adicup_connect-min.jpg
.. |AD5593R-PMDZ connect| image:: ../images/ad5593r_adicup_connect-min.jpg
.. |PC connect| image:: ../images/ad5593r_adicup_pc_connect-min.jpg
