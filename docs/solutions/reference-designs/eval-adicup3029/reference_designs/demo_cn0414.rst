PLC Arduino Shield Input Demo
=============================

The **ADuCM3029_demo_cn0414** project provides a solution to control a **PLC** or **DCS** input system using the **EVAL-CN0414-ARDZ** and the **EVAL-ADICUP3029**. It uses an **ADC** with 4 differential voltage channels and 4 current channels and boasts low power **Open-Wire Detection** capabilities and **HART** communication. It has a 32kb EEPROM memory that can also be used to identify the board and is controlled via a command line interface (**CLI**).

General Description/Overview
----------------------------

The **ADuCM_demo_cn0414** project uses **EVAL-CN0414-ARDZ** to provide a complete, fully isolated and highly flexible, four channel analog input system. The **EVAL-CN0414-ARDZ** is suitable for programmable logic controllers (**PLC**) and distributed control system (**DCS**) applications that require multiple voltage inputs. It boasts **open wire detection** and has **HART**-compatible, 4 mA to 20 mA current inputs, all protected from transient overvoltage or overcurrent events, suitable for the most harsh industrial environments.

The circuit can be divided into the following parts: the ADC, the input
channels, the HART modem and the memory.

The **ADC** is the core of the **EVAL-CN0414-ARDZ** shield. It is an :adi:`AD4111` with 8 single or 4 differential voltage channels and 4 current channels. The input channels in this application are configured as 4 differential voltage channels and the current channels. The application maintains 8 internal registers, one for each channel, that are updated periodically, on a timer interrupt, with the latest conversion results. This way, on a single read, the user can have the data on a channel without waiting for a conversion. |Timer diagram| Alternatively the user can request a burst read of up to 2000 samples returned at the ADC output data rate. The application uses the **ADCs Open-Wire Detection** capabilities for the voltage channels. When activated this option also tracks the state of the channel connection on every read and gives a warning when a channel is disconnected.

The **EVAL-CN0414-ARDZ** is **HART** capable. When this option is activated the current channels can be used to transmit or receive **HART** messages or command zero and receive response. The system is capable of receiving messages asynchronously using a **GPIO** interrupt.

The system also includes an EEPROM memory that communicates with the controller via **I2C** and can be used to store data or identification information for the board. The memory can be used to uniquely identify the board in a system of 4 similar boards (**EVAL-CN0414-ARDZ** or **EVAL-CN0418-ARDZ**) controlled by the same **EVAL-ADICUP3029**.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0414-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  24V and 1A limited power supply (**optional**)

-  Software

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0414 demo application <projects/ADuCM3029_demo_cn0414>`
   -  CrossCore Embedded Studio (2.8.0 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Connect **EVAL-CN0414-ARDZ** board to the **EVAL-ADICUP3029**.
-  Set the jumpers into the position shown below. This is the standard position
   and only works for one board systems.

.. image:: ../images/cn0414_jumper_pos2.jpg
   :alt: Standard jumper position
   :align: center

-  Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer. The final setup should look similar to the picture below.

.. image:: ../images/eval_cn0414_ardz_hard_setup3.jpg
   :alt: Hardware setup example
   :align: center

Configuring the Software
------------------------

The configuration parameters can be found in the **config.h** file.

**vref** - Reference voltage of the **ADC**. If the internal reference is used this value must be **2.5V**. If an external reference is used then this value must be the value of the external reference.

======== ========================
Referece vref value
======== ========================
internal 2.5
external Actual reference voltage
======== ========================

::

      /* Reference voltage of the ADC */
      float vref = 2.5;

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

+----------------------------+-----------------------------------------------------------------------------------------------+
| Command                    | Description                                                                                   |
+============================+===============================================================================================+
| General commands           |                                                                                               |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *h*                        | Display available commands.                                                                   |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *stts*                     | Display parameters of the application.                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------+
| Internal register commands |                                                                                               |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *r*                        | Display voltage or current on the selected channel.                                           |
|                            | <*chan*> = channel to be shown                                                                |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *sur*                      | Change channel update rate.                                                                   |
|                            | <rate> = new channel update rate in Hz.                                                       |
|                            | If it is bigger than output data rate divided by 80 can cause unpredictable behaviour.        |
+----------------------------+-----------------------------------------------------------------------------------------------+
| HART commands              |                                                                                               |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *he*                       | Enable HART channel.                                                                          |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *hd*                       | Disable HART channel.                                                                         |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *hcc*                      | Select wanted channel.                                                                        |
|                            | <*chan*> = Channel to be selected.                                                            |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *ht*                       | Transmit string through HART.                                                                 |
|                            | <*string*> = string to be transmitted.                                                        |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *hg*                       | Send the received buffer through UART connection.                                             |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *hcz*                      | Send command zero with the specified number of FFs in the preambule.                          |
|                            | <*pbsize*> = size of the preambule (no. of 0xFFs in the beginning).                           |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *hpt*                      | Send command zero with the specified number of FFs in the preambule.                          |
|                            | <*byte*> = byte to send in loop.                                                              |
+----------------------------+-----------------------------------------------------------------------------------------------+
| ADC commands               |                                                                                               |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *arr*                      | Display value of ADC register of the given address.                                           |
|                            | <*reg*> = address of the register.                                                            |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *awr*                      | Change value of the ADC register of the given address.                                        |
|                            | <*reg*> = address of the register.                                                            |
|                            | <*val*> = new value of the register.                                                          |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *ags*                      | Get a specific number of samples from the given channel.                                      |
|                            | <*ch*> = selected chanel.                                                                     |
|                            | <*nr*> = number of channels; cannot exceed 2048.                                              |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *aso*                      | Set sample rate.                                                                              |
|                            | <*sps*> = selected sample rate option.                                                        |
|                            | If it is smaller than channel update rate multiplied by 80 can cause unpredictable behaviour. |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *asf*                      | Set filter option.                                                                            |
|                            | <*filter*> = selected filter option.                                                          |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *aep*                      | Enable post filter.                                                                           |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *adp*                      | Select postfilter.                                                                            |
|                            | <*opt*> = selected postfilter option.                                                         |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *asp*                      | Reset controller, parameters and faults                                                       |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *aowe*                     | Enable open wire detection.                                                                   |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *aowd*                     | Disable open wire detection.                                                                  |
+----------------------------+-----------------------------------------------------------------------------------------------+
| EEPROM commands            |                                                                                               |
+----------------------------+-----------------------------------------------------------------------------------------------+
| *de*                       | Discover EEPROM I2C addresses if there are any.                                               |
+----------------------------+-----------------------------------------------------------------------------------------------+

.. image:: ../images/eval_cn0414_console.png
   :alt: Terminal example
   :align: center

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0414.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0414** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0414 Hex File

   -  `AduCM3029_demo_cn0414.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0414.hex>`_

   Complete CN0414 Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0414 Source Code <projects/ADuCM3029_demo_cn0414>`

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

Board setup initializes **UART**, **SPI** and **I2C** communication and verifies if there is an active **EVAL-CN0414-ARDZ** board connected by reading the AD4111 ID register. Here is also initialized the update timer for the internal channel registers.

.. image:: ../images/cn0414_board_setup_flow.png
   :alt: Board setup flow chart
   :align: center

The main process routine implements the **CLI** and calls the commands input by the user. This routine also checks the flags asserted in the asynchronous events (the update channel register flag, the HART received flag and the floating channel flags) and calls the appropriate handler methods. There is also a flag asserted by the channel register update rate and the **ADC** output data rate. If the update rate would be too close to the output data rate, the actual update rate might slow down to be possible for the program to maintain all functionality. The update rate may never be bigger or equal to the **ADC** output data rate divided by 8 (for 8 channels).

.. image:: ../images/cn0414_process_flow.png
   :alt: Process flow chart
   :align: center

The flow chart below represents the way the channel registers are updated. Only
one channel is active at any one time (the channel that must be read).

.. image:: ../images/cn0414_update_channel_flow.png
   :alt: Update channel flow chart
   :align: center

*End of Document*

.. |Timer diagram| image:: ../images/cn0414_timer_diagram.png
