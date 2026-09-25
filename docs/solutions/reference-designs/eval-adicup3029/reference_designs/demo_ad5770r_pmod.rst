AD5770R PMOD Demo
=================

The **ADuCM3029_demo_ad5770rpmdz** project provides a solution to control the **EVAL-AD5770R-PMDZ** **PMOD** using a minimal **CLI** and the **no-OS** drivers for the **EVAL-ADICUP3029** platform.

General Description/Overview
----------------------------

The :adi:`AD5770R` is a 6-channel, 14-bit, multi-range, current output **DAC** designed for use in communications systems, instrumentation and industrial applications; specifically for photonics control and current mode biasing. It has 6 programmable output channels with 1 channel capable of sinking up to 60 mA of current. The **EVAL-AD5770R-PMDZ** is a board designed to be a compact and low cost solution to evaluate the part.

The application builds upon the **no-OS** device and platform drivers and a minimal **CLI** module to provide a robust command set to set the range and output value of the channels.

.. image:: ../images/ad5770r_layer.png
   :align: center

The program first initializes the hardware system as well as the driver handlers, then goes into the main process that just implements the **CLI** process and waits for user commands. If a command is received, it is executed and the program returns to the main loop.

.. image:: ../images/ad5770r_process.png
   :align: center

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-AD5770R-PMDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  :git-EVAL-ADICUP3029:`projects/ADuCM3029_demo_ad5770rpmdz`
   -  CrossCore Embedded Studio (2.9.1 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Connect **EVAL-AD5770R-PMDZ** board to the **EVAL-ADICUP3029** using connector **P8**.

.. image:: ../images/ad5770r_connect.jpg
   :align: center

-  Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer. The final setup should look similar to the picture below.

.. image:: ../images/ad5770r_pc.jpg
   :align: center

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

+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+
| Function         | Command | Description                                                                                                                             | Example     |
+==================+=========+=========================================================================================================================================+=============+
| General commands |         |                                                                                                                                         |             |
+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+
|                  | *h*     | Display available commands.                                                                                                             |             |
+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+
|                  | *t*     | Set channels at production test levels.                                                                                                 |             |
+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+
| DAC commands     |         |                                                                                                                                         |             |
+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+
|                  | *sir*   | Set the input register of the chosen DAC channel.                                                                                       | sir c0 8192 |
|                  |         | <*chan*> = channel to update; values are: c0, c1, c2, c3, c4, c5.                                                                       |             |
|                  |         | <*value*> = update value in decimal; between 0 and 16383.                                                                               |             |
+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+
|                  | *uo*    | Update the DAC output with the channel input registers value.                                                                           |             |
|                  |         | This is done with the nLDAC GPIO if it's available and with the SW register otherwise.                                                  |             |
+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+
|                  | *sc*    | Set the value of the chosen DAC channel.                                                                                                | sc c0 8192  |
|                  |         | <*chan*> = channel to update; values are: c0, c1, c2, c3, c4, c5;                                                                       |             |
|                  |         | <*value*> = update value in decimal; between 0 and 16383.                                                                               |             |
+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+
|                  | *sr*    | Set the range of the DAC output channels.                                                                                               | sr c0 opt1  |
|                  |         | <*chan*> = channel to update; values are: c0, c1, c2, c3, c4, c5;                                                                       |             |
|                  |         | <*opt*> = option chosen for the channel. values are: opt1 - only for channels 0 and 1, opt2, opt3.                                      |             |
|                  |         | Those correspond to the options in :adi:`the datasheet <media/en/technical-documentation/data-sheets/AD5770R.pdf>`.                     |             |
+------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+-------------+

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
AD5770 PMOD.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_ad5770** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt AD5770 PMOD Hex File

   -  `AduCM3029_demo_ad5770rpmdz.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_ad5770rpmdz.hex>`_

   Complete AD5770 PMOD Source Files

   -  :git-EVAL-ADICUP3029:`ADuCM3029_demo_ad5770rpmdz Source Code <projects/ADuCM3029_demo_ad5770rpmdz>`

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

Beside the IDE generated sources the project structure is divided into high
level software modules and low level software modules.

The high level modules are in the **src** folder and are:

-  AD5770R device driver;
-  CLI module;
-  AD5770R_PMDZ module (application source)
-  ADuCM3029_demo_ad5770rpmdz.c (main file)

The low level modules are the platform drivers and are included in the **platform_source** and **platform_include** folders.

.. image:: ../images/ad5770r_pmdz_project_struct.png
   :align: center

*End of Document*
