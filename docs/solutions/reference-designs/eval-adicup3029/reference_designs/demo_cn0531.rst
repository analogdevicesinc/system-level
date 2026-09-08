AD5791 PMOD Application with EVAL-ADICUP3029 (w/ EVAL-CN0531-ADRZ)
==================================================================

The **ADuCM3029_demo_cn0531** project provides a solution to control a AD5791 DAC PMOD using the **EVAL-ADICUP3029**. The **AD5791** is a high precision, 1ppm, voltage output **DAC** that can be controlled in this application using a serial UART CLI connected to a host PC.

General Description/Overview
----------------------------

:adi:`EVAL-CN0531-PMDZ <CN0531>` is a minimalist 1 **ppm**, 20-Bit, ±1 **LSB INL**, **DAC SPI PMOD** board suitable for medical instrumentation, test and measurement equipment, industrial control or high end scientific and aerospace instrumentation. Multiple voltage references and power options are available to adapt this module depending on the application. With this module, the user is capable to use the onboard positive voltage reference or to connect external references.

The **ADuCM3029_demo_cn0531** project uses this PMOD with the :adi:`EVAL-ADICUP3029` board to bring up the **DAC**, control it's internal registers and control it's voltage output. This control is done using a minimalist **CLI** interface enabled over the **UART** controller of the board. This **CLI** can be used by a host **PC** connected via **USB** cable to the system.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0531-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0531 demo application <projects/ADuCM3029_demo_cn0531>`
   -  CrossCore Embedded Studio (2.9.1 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Connect **EVAL-CN0414-ARDZ** board to the **EVAL-ADICUP3029**.

.. image:: ../images/cn0531_adicup_conn.jpg
   :align: center

-  Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer. The final setup should look similar to the picture below.

.. image:: ../images/cn0531_system_host.jpg
   :alt: FIXME - PICTURE
   :align: center

Configuring the Software
------------------------

Software does not need configuration to work.

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

+-----------------------+---------+------------------------------------------------------------------+-------------------------------------+
| Function              | Command | Description                                                      | Example                             |
+=======================+=========+==================================================================+=====================================+
| General commands      |         |                                                                  |                                     |
+-----------------------+---------+------------------------------------------------------------------+-------------------------------------+
| Help                  | *h*     | Display available commands.                                      |                                     |
+-----------------------+---------+------------------------------------------------------------------+-------------------------------------+
| DAC specific commands |         |                                                                  |                                     |
+-----------------------+---------+------------------------------------------------------------------+-------------------------------------+
| DAC register read     | *drr*   | Read a DAC register.                                             | drr 1 - read register 1             |
|                       |         | <*addr*> = address of the register to be read in hexadecimal.    |                                     |
+-----------------------+---------+------------------------------------------------------------------+-------------------------------------+
| DAC register write    | *drw*   | Write a DAC register.                                            | drw 1 18c - set register 1 to 0x18C |
|                       |         | <*addr*> = address of the register to be written in hexadecimal. |                                     |
|                       |         | <*val*> = value to be written to the register in hexadecimal.    |                                     |
+-----------------------+---------+------------------------------------------------------------------+-------------------------------------+
| DAC set output        | *do*    | Update the DAC output voltage.                                   | do -2.3 - set DAC output to -2.3V   |
|                       |         | <*volt*> = new voltage value expressed in volts.                 |                                     |
+-----------------------+---------+------------------------------------------------------------------+-------------------------------------+

.. image:: ../images/cn0531_terminal_example.png
   :align: center

Note that the 'do' command for setting the output voltage works on the
assumption that the on board 5V reference is used.

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0531.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0531** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0531 Hex File

   -  `AduCM3029_demo_cn0531.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0531.hex>`_

   Complete CN0531 Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0531 Source Code <projects/ADuCM3029_demo_cn0531>`

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

The program is composed of two main parts:

-  Board setup with initial values.
-  Main process.

.. image:: ../images/cn0414_main_flowchart.png
   :alt: Main flow chart
   :align: center

Board setup initializes UART and SPI communications and sets the DAC value
register to 0. The DAC RBUF bit is also set to 0 to provide the widest voltage
range for the application. The DAC output will be between -5V and 5V and coded
in two's complement. The coding can be changed to offset binary and the 'do' CLI
command will take that into consideration, as it will also take into
consideration the RBUF bit. If the RBUF is changed to narrow the output field to
0V - 5V the coding will not change. As such the 0x00000 value of the DAC
register will correspond to the middle range value of 2.5V. If not using the
'do' command to change the output, this will have to be taken into
consideration.

*End of Document*
