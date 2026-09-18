Command Line Interpreter Demo
=============================

The **ADuCM3029_demo_cli** is a Command Line Interpreter (CLI) demo project for the EVAL-ADICUP3029 base board, created using the GNU ARM Eclipse Plug-ins in Eclipse environment.

General Description/Overview
----------------------------

The purpose of this project is to help you to get used with UART peripheral of **ADuCM3029** microcontroller. The source code example can serve as a template for a resident command line interpreter, complementing any other user application functionality. Interrupt-based receiving of text commands from the UART is implemented. As soon as a command is entered, an execution request flag is raised to signal the main loop. The commands are recognised and may be executed immediately or later depending on the priority of the current tasks.

You can use any Terminal session you want, such as Putty or Serial Terminal with
Eclipse Kepler (incorporated in Eclipse environment).

A serial connection of a PC to the **EVAL-ADICUP3029** board using the user USB connector is required to test and use the CLI application (**EVAL-ADICUP3029** board incorporates an FTDI USB-to-serial converter). Any terminal application run on a PC at 9600-8-N-1 without flow control can be used to 'talk' to the **EVAL-ADICUP3029** board. After connecting and sending CR (by pressing Enter), the command prompt '»' and a welcome message should appear.

The user must type the word <help> in order to bring up the CLI menu shown
below.

|image1|

Available commands
~~~~~~~~~~~~~~~~~~

+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Command                  | Description                                                                                                                          |
+==========================+======================================================================================================================================+
| *help*                   | Display available commands                                                                                                           |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| *version*                | Display SW version of CLI project                                                                                                    |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| *dump [begaddr] [count]* | Display up to 0x40 consecutive byte-size                                                                                             |
|                          | locations from any address of the ADuCM360 memory space.                                                                             |
|                          | One should be careful not to request locations which are not decoded because the hardware_fault exception code will block the board. |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| *reset*                  | Perform a HW reset which also initialize the application                                                                             |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

|

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  ADICUP3029_demo_cli software
   -  CrossCore Embedded Studio (2.6.0 or higher)
   -  ADuCM302x DFP (2.0.0 or higher)
   -  ADICUP3029 BSP (1.0.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Ordered List ItemMake sure that the **S2** switch on the board is in position **1(USB)** as shown below. This will ensure that the UART module is routed to the USB connection.

.. image:: ../images/adicup3029_front_refrence_s2_position_for_usb.jpg
   :align: center
   :width: 800

-  Plug in the board.

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the CLI
Demo.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cli** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CLI Demo Hex File

   -  `ADuCM3029_demo_cli.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cli.hex>`_

   Complete CLI Demo Source Files

   -  :git-EVAL-ADICUP3029:`ADuCM3029_demo_cli Source Code <projects/ADuCM3029_demo_cli>`

.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>`

Configuring the Software
------------------------

-  Download and install :adi:`CrossCore Embedded Studio <en/design-center/processors-and-dsp/evaluation-and-development-software/adswt-cces.html#dsp-overview>` or other IDE of choice.
-  Download and install a terminal software of choice (e.g. PuTTY).
-  Download project from :git-EVAL-ADICUP3029:`Github <projects>`.
-  Import the project into workspace.
-  Baudrate can be selected by choosing one in file include/ADuCM3029_demo_cli.h.
-  Connect a terminal session to the appropriate port.
-  Compile, flash and execute.

Outputting Data
---------------

Data will be outputted to terminal screen by interacting with it.

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

*End of Document*

.. |image1| image:: ../images/terminal_cli_26_08_2015.png
   :width: 450
