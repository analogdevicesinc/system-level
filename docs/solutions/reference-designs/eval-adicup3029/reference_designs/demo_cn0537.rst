Smoke Detector Demo (w/ EVAL-CN0537-ADRZ)
=========================================

The **ADuCM3029_demo_cn0537** project provides a solution to implement a smoke detector with the capability to pass **UL-217 specification**, using the **EVAL-CN0537-ARDZ** and the **EVAL-ADICUP3029**. The Arduino shield uses a \**ADPD188BI** to control the LEDs and photodiodes, a temperature sensor for compensation, heater resistors to correct condensation and an SD card adapter to log operation data when not attended by a user terminal. The program can be controlled using a **UART** **CLI**.

General Description/Overview
----------------------------

The **ADuCM_demo_cn0537** project uses **EVAL-CN0537-ARDZ** and **EVAL-ADICUP3029** to provide an **UL-217 compliant** solution to smoke detection. The application gives user access to the **ADPD188BI** registers and other software defined application parameters to get smoke data at the desired rate and use it to calculate the **Power Transfer Ratio (PTR)** that directly correlates to the amount of smoke in the chamber. The alarm algorithm then takes the **PTR measurement** and measures it against a calculated baseline to determine if the alarm should trigger or not.

The application has two main stages:

-  Initialization
-  Main process

In the initialization process the software modules and part drivers are
instantiated and set to initial values.

|image1|

The application initializes the **CLI** process on top of the **UART core** and then sets up the **ADPD188BI** for smoke detection measurements. The program then reads calibration data from the part and uses them to set up the **PTR measurements**. After the **PTR measurements** are ready the application initializes the algorithm. This process may take a few seconds to complete. The application finishes initialization by setting up **temperature compensation** and real time clock counter. The main process is then started in **idle mode**.

The main process has two modes of operation: **idle** and **streaming**. In **idle mode** the serial **CLI** may be used to alter functionality parameters like **ADPD188BI** registers and output data rate. The **CLI** can also be used to set up **SD card logging** by creating a file on it.

.. note::

   Note that for the log to be complete, the file opened on the card must also
   be closed for the data to be saved.

Using the **'stream'** command the process switches to **streaming mode** where smoke data is taken out at the set sampling rate. After **temperature compensation** and **PTR calculation**, data is fed to the algorithm to determine the alarm state. If the alarm is triggered the buzzer is activated and the alarm can only be reset by pressing the button on the shield or calling the **'reset_alarm'** command on the **CLI**. If working parameters need to be adjusted, it is recommended to return to **idle mode** by calling the **'idle'** command and adjusting as necessary and then return to the **stream mode**.

In **streaming mode**, if the serial terminal is connected, the application will display **temperature compensated** code values or **PTR values** at users' choice, timestamped. The **timestamp** is in seconds relative to the start of the application. The alarm state is also displayed on the terminal while streaming.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0537-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port

-  Software

   -  :download:`Smoke Detector Demo Software for UL-217 Standard (.hex file and copyrights) <../resources/aducm3029_demo_cn0537_hex.zip>`
   -  :download:`Smoke Detector Demo Software for EN-14604 Standard (.hex file and copyrights) <../resources/aducm3029_demo_cn0537_en14604.zip>`

Setting up the Hardware
-----------------------

-  Set up the **EVAL-CN0537-ARDZ** as shown in the :dokuwiki:`Hardware User Guide <resources/eval/user-guides/circuits-from-the-lab/cn0537>`.
-  Connect **EVAL-CN0537-ARDZ** board to the **EVAL-ADICUP3029**.

.. image:: ../images/cn0537_arduino.jpg
   :align: center

-  Connect a micro-USB cable to P10 connector of the EVAL-ADICUP3029 and connect
   it to a computer. The final setup should look similar to the picture below.

.. image:: ../images/cn0537_system_pc.jpg
   :align: center

Programming the Firmware
------------------------

This application software is used with the ADICUP3029 to demonstrate the
capabilities of the CN0537 evaluation board. To upload the CN0537 software to
the ADICUP3029, connect both boards together through the Arduino form factor
connectors (P1 to P4 on the CN0537) and plug them to a computer through USB.

Upon connection, the hardware should appear as a DAPLINK drive on the computer.
Drag and drop the ADuCM3029_demo_cn0537.hex file to the DAPLINK drive to program
the ADICUP3029.

|image2|

.. admonition:: Download
   :class: download

   Available .hex files for CN0537:

   -  :download:`Smoke Detector Demo Software for UL-217 Standard (.hex file) <../resources/aducm3029_demo_cn0537_hex.zip>`
   -  :download:`Smoke Detector Demo Software for EN-14604 (.hex file) <../resources/aducm3029_demo_cn0537_en14604.zip>`

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

Typing **help** or **h** after initial calibration sequence will display the list of commands and their short versions. Below is the short command list:

+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Function             | Command | Description                                                                                                                                                                                  | Example                                                                     |
+======================+=========+==============================================================================================================================================================================================+=============================================================================+
| Application commands |         |                                                                                                                                                                                              |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *h*     | Display available commands.                                                                                                                                                                  |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *s*     | Put the device in GO mode and stream data from the device to the terminal.                                                                                                                   |                                                                             |
|                      |         | <*no*> = number of samples to be displayed. If not specified stream indefinitely. After the selected number of samples have been streamed the device will still sample, but not output data. |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *i*     | Stop the stream.                                                                                                                                                                             |                                                                             |
|                      |         | <*opt*> = 1 to put the program in idle mode, 0 to keep the program in streaming mode, but stop streaming.                                                                                    |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *ms*    | Set the output mode.                                                                                                                                                                         |                                                                             |
|                      |         | <*opt*> = 'CODE' to stream data in codes; 'PTR' to stream PTR data.                                                                                                                          |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *os*    | Set output data rate. <*odr*> = new sample rate.                                                                                                                                             | os 2.45 = set sample rate to 2.45 samples per second.                       |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *og*    | Get current output data rate.                                                                                                                                                                |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *ra*    | Stop the alarm if triggered.                                                                                                                                                                 |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *n*     | Insert a note into the stream and also the SD card log if started.                                                                                                                           | n Note 1 = print 'Note 1' on th terminal stream and SD card log if started. |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *ar*    | Redo initialization of the algorithm. Useful if conditions changed significantly since start of the program.                                                                                 |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *hc*    | Heater resistors control.                                                                                                                                                                    |                                                                             |
|                      |         | <*opt*> = 1 to turn heater resistors on; 0 to turn the heater resistors off.                                                                                                                 |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| SD card commands     |         |                                                                                                                                                                                              |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *fo*    | Open a file on the SD card. If the file does not exist it is created.                                                                                                                        | fo file1 = a file named 'file1.txt' is opened on the card.                  |
|                      |         | If the file exists and has information the new information will be appended.                                                                                                                 |                                                                             |
|                      |         | <*name*> = name of the file to be opened.                                                                                                                                                    |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *fc*    | Close the last file open on the SD card. This also saves the latest content to memory.                                                                                                       |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Device commands      |         |                                                                                                                                                                                              |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *rr*    | Read device register.                                                                                                                                                                        | rr a = read register 0xA                                                    |
|                      |         | <*addr*> = address of the register to be read in hexadecimal.                                                                                                                                |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *rw*    | Write device register.                                                                                                                                                                       | rw a 12c = write 0x12C to register 0xA                                      |
|                      |         | <*addr*> = address of the register to be read in hexadecimal.                                                                                                                                |                                                                             |
|                      |         | <*val*> = value to be written to the register in hexadecimal.                                                                                                                                |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|                      | *rd*    | Read and display all device registers in one command.                                                                                                                                        |                                                                             |
+----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. image:: ../images/cn0537_putty_update.png
   :align: center

UL-217 Testing Results
----------------------

Using both the EVAL-CN0537-ARDZ and the EVAL-CN0537-ALGO (now referred as
ADSW-SMOKEALGO-PRODLIC), the setup was tested at a certified testing facility
(Intertek) and passed all the smoke sensor aspects of the UL-217 8th Ed.
standards. You can view the entire report here.

.. admonition:: Download
   :class: download

   :download:`UL-217 8th Ed. testing and results document <../resources/intertek_test_report_on_eval-cn0537-algo.pdf>`

*End of Document*

.. |image1| image:: ../images/cn0537_initialization.png
.. |image2| image:: ../images/cn0537_uploading_hex_file.png
   :width: 600
