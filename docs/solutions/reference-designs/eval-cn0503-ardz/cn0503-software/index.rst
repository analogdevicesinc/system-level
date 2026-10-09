.. _cn0503-software:

Software User Guide
====================

The **ADuCM3029_demo_cn0503** project provides a solution to get multiple
liquid parameters (for example, turbidity, pH, fluorescence, etc.) using the
**EVAL-CN0503-ARDZ** and the **EVAL-ADICUP3029**. It uses a complete multimodal
sensor front end, stimulating up to eight LEDs and measuring the return signal
on up to eight separate current inputs using photo-diodes. The board is
controlled via a command line interface (**CLI**), Python scripts that provide
high level functions or a Python **GUI** that communicates with the firmware
via **serial terminal**.

General Description
--------------------

The **ADuCM_demo_cn0503** project uses **EVAL-CN0503-ARDZ** to provide a method
to determine properties of liquids, for example, turbidity, fluorescence, and pH.
To do this, the application must configure the :adi:`ADPD4101`
sensor, read the data from it and perform calculations on the data to improve
**SNR** and pre-process it to units as close to the desired measurement as
possible.

The application configures the device to stimulate **LEDs** and read the
**PDs** in 4 time slots, each corresponding to one of the optical paths
present on the board. It enables 2 ADC channels per time slot to measure the
light beam before and after passing through the substance. This means that a
packet of 8 samples of data come from the **ADC** once per sampling period.

.. image:: cn0503_data_gather.png

The samples can then be plugged into a user defined equation that can include
any of the samples and any random constant to generate a ratio, which the
application defines as the **absolute ratio**. Before being displayed or used
any further the **absolute ratio** is filtered by a **block average filter** and
a **rolling average filter** to digitally increase the **SNR** and take out
unwanted frequencies. The bandwidth of the **rolling average filter** can be set
by the user. After getting the **absolute ratio** that describes the liquid that
is now in the vat, it can be used to compare it to the **baseline measurement**
using either 1 - (absolute ratio / baseline) or (absolute ratio / baseline)
equations. The user has to input the **baseline** for each optical path as well
as the equation from these options. The application defines this result as the
**relative ratio**. The application then has 2 more options of processing the
information in the form of two **5th order polynomials** in which the **relative
ratio** can be inserted as the variable. The coefficients of each of the
**polynomial** members are also input by the user via the **CLI**. To be noted
that the result of the first equation is the variable for the second equation.
This gives the user a high degree of flexibility in getting data out of the
platform.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

**Hardware**

  - :adi:`EVAL-ADICUP3029`
  - :adi:`EVAL-CN0503-ARDZ`
  - Micro USB to USB cable
  - PC or Laptop with a USB port
  - 3D printed mechanical fixtures described in the :ref:`Hardware User Guide<eval-cn0503-ardz>`

**Software**

  - :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0503 demo application <projects/ADuCM3029_demo_cn0503>`
  - :adi:`CrossCore Embedded Studio (2.8.0 or higher) <resources/evaluation-hardware-and-software/embedded-development-software/adswt-cces.html>`
  - `ADuCM302x DFP (3.2.0 or higher) <https://www.keil.arm.com/packs/aducm302x_dfp-analogdevices/boards/>`_
  - :doc:`ADICUP3029 BSP (1.1.0 or higher) </solutions/reference-designs/eval-adicup3029/software/adicup3029>`
  - Serial Terminal Program such as Putty or Tera Term

Setting up the Hardware
-----------------------

#. Set up the the **EVAL-CN0503-ARDZ** as shown in the
   :ref:`Hardware User Guide<eval-cn0503-ardz>`.

#. Connect the board to the **EVAL-ADICUP3029** via the Arduino headers.

   .. image:: cn0503_arduino.jpg

#. Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer. The final setup should look similar to the picture below.

   .. image:: cn0503_system_pc.jpg

Configuring the Software
------------------------

The **ADuCM3029_demo_cn0503** does not need any software configuration. It can
be built and run as is.

Outputting Data
---------------

A serial terminal is an application that runs on a PC or laptop that is used to
display data and interact with a connected device (including many of the Circuits
from the Lab reference designs). The device's UART peripheral is most often
connected to a UART to USB interface IC, which appears as a traditional COM port
on the host PC/laptop. (Traditionally, the device's UART port would have been
connected to an RS-232 line driver/receiver and connected to the PC via a 9-pin
or 25-pin serial port). There are many open-source applications, and while there
are many choices, typically we use one of the following:

 - `Tera Term <https://ttssh2.osdn.jp/index.html.en>`__
 - `Putty <https://www.putty.org/>`__
 - `Real Term <https://realterm.sourceforge.io/>`__

Before continuing, please make sure you download and install one of the above
programs.

There are several parameters on all serial terminal programs that must be setup
properly in order for the PC and the connected device to communicate. Below are
the common settings that must match on both the PC side and the connected UART
device.

#.  **COM Port** - This is the physical connection made to your PC or Laptop, typically
    made through a USB cable but can be any serial communications cable. You can
    determine the COM port assigned to your device by visiting the device manager on
    your computer. Another method for identifying which COM port is associated with
    a USB-based device is to look at which COM ports are present before plugging in
    your device, then plug in your device, and look for a new COM port.

#.  **Baud Rate** - This is the speed at which data is being transferred from the
    connected device to your PC. These parameters must be the same on both devices
    or data will be corrupted. The default setting for most of the reference designs
    is 115200.

#.  **Data Bits** - The number of data bits per transfer. Typically UART transmits ASCII
    codes back to the serial port so by default this is almost always set to 8-Bits.

#.  **Stop Bits** - The number of “stop” conditions per transmission. This usually set to
    1, but can be set to 2 for redundancy.

#.  **Parity** - Is a way to check for errors during the UART transmission. Unless
    otherwise specified, set parity to “none”.

#.  **Flow Control** - Is a way to ensure that data lose between fast and slow devices on
    the same UART bus are not lost during transmission. This is typically not
    implemented in a simple system, and unless otherwise specified, set to “none”.

In many instances there are other options that each of the different serial
terminal applications provide, such as local line echo or local line editing, and
features like this can be turned on or off depending on your preferences. This
setup guide will not go over all the options of each tool, but just the minor
features that will make it easier to read back data from the connected devices.

**Example Setup using Putty**

#. Plug in your connected device using a USB cable or other serial cable.
#. Wait for the device driver of the connected device to be installed on your PC.
#. Open your device manager and check which COM port was assigned to your
   device.

.. image:: device_manager.png

Open up your serial terminal program (Putty for this example). Click on the serial
configuration tab or window, and input the settings to match the requirements of
your connected device. The default baud rate for most of the reference designs is
**115200**. Make sure that you use the correct baud rate for your application.

.. image:: putty_serial_config.png

Ensure you click on the checkboxes for Implicit CR in every LF and Implicit LF in
every CF. Ensure that local echo and line editing are enabled, so that you can
see what you type and are able to correct mistakes. (Some devices may echo typed
characters - if so, you will see each typed character twice. If this happens,
turn off local echo.)

.. image:: putty_terminal_options.png

Click on the open button, and as long as your connected device and serial
terminal program are setup the same, then you should see data displaying.

.. tip::

   If you see nothing in the serial terminal, try hitting the reset button on
   the embedded development board.

Available Commands
~~~~~~~~~~~~~~~~~~

Typing **help** after the application has started will display the list of
commands:

.. csv-table::
   :file: commands.csv

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0503.

#. Dragging and Dropping the .Hex file to the DAPlink drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0503** can be found here:

.. admonition:: Download

   Prebuilt CN0503 Hex File :
   :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0503.hex <releases/download/Latest/aducm3029_demo_cn0503.hex+>`

   Complete CN0503 Source Files :
   :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0503 Source Code <master:projects/ADuCM3029_demo_cn0503>`

How to Use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore
Embedded Studio. For more information on downloading the tools and a quick start
guide on how to use the tool basics, please check out the :doc:`Tools Overview page </solutions/reference-designs/eval-adicup3029/tools>`.

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>`
section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>`
section.

Project Structure
~~~~~~~~~~~~~~~~~

The program is composed of two main parts:

#. Initialization routine
#. Main process

.. image:: cn0503_main.png

The platform initialization includes the carrier clock and power initialization
as well as initialization for **DMA**, **GPIO**, **SPI**, **I2C**, **UART**, and
**flash** cores. Then the program initializes the ADPD device driver with
default values and applies this configuration to the chip. After this it will
perform the clock calibration for the ADPD device and will apply the
configuration saved in the flash pages in the following order: manufacturer page
and user page. If the manufacturer page is not initialized it will initialize
it. Applying the user page after the manufacturer default will only change the
specific configurations mentioned in the user page, leaving the rest untouched.

.. image:: cn0503_intialization.png

The main process of the application runs into a loop and is responsible for
taking data out of the device and displaying it and for implementing the user
**CLI** using the serial **UART** interface.

.. image:: cn0503_main_process.png

Interacting with the CLI
~~~~~~~~~~~~~~~~~~~~~~~~

#. Run commands directly from Putty.
#. Use example scripts from :git-EVAL-ADICUP3029:`this folder <master:projects/ADuCM3029_demo_cn0503/scripts>`
   and see the :git-EVAL-ADICUP3029:`readme file <master:projects/ADuCM3029_demo_cn0503/scripts/README.md>`
   to learn how to use them.

Hardware User Guide and Demo Guides
-----------------------------------

- :ref:`EVAL-CN0503-ARDZ Hardware User Guide <eval-cn0503-ardz>`
- :ref:`Optical Platform: Fluorescence Measurement Demo (ADICUP3029 + EVAL-CN0503-ADRZ) <fluorescence-measurement>`
- :ref:`Optical Platform: pH Measurement Demo (ADICUP3029 + EVAL-CN0503-ADRZ) <ph-measurement>`
- :ref:`Optical Platform: Turbidity Measurement Demo (ADICUP3029 + EVAL-CN0503-ADRZ) <turbidity>`
- :ref:`Optical Platform: Nitrate Measurement Demo (ADICUP3029 + EVAL-CN0503-ADRZ) <nitrate-measurement>`
