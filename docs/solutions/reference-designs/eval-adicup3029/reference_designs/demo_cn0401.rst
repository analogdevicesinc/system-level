CN0401 SPI to CAN FD Transceiver Demo
=====================================

The **ADuCM3029_demo_cn0401** project provides a solution to adding isolated fieldbus communication to a microcontroller circuit. The project demonstrates basic CAN FD communication, transmission and response to the ISO11898-2:2016 remote wake-up pattern, and control of switchable termination circuitry. The example code is written for the **EVAL-ADICUP3029** development platform to control the **EVAL-ADM3055E-ARDZ** daughter board over the SPI bus interface. The daughter boards main component is the :adi:`ADM3055E <en/products/adm3055e.html>`, an isolated signal and power CAN FD transceiver with integrated auxiliary channel.

General Description/Overview
----------------------------

The **ADuCM3029_demo_cn0401** project uses the **EVAL-ADM3055E-ARDZ** to provide CAN FD bus connectivity to underlying development board that it may be added to an existing CAN FD bus as another node. This example demonstrates the **EVAL-ADM3055E-ARDZ** circuit features using two nodes, each a **EVAL-ADM3055E-ARDZ** and **EVAL-ADICUP3029** development board.

The node is at first in low power mode by putting the CAN controller and transceiver to standby mode. The user can then issue a command to transmit an ASCII message on the bus. the message is repeated for 5 seconds or until it is acknowledged by another node, then the transmitting node goes to standby. If the system receives a message, particularly the slower baud rate arbitration phase, it wakes up, receives the message and displays it on the CLI terminal, then goes back to standby. A node not connected to a CAN bus can also run a self-test routine on the command of the user, in which it transmits and receives a message in loopback mode and displays a PASS of FAIL message. The initial baud rate is 500KHz for the arbitration phase and 2MHz for the data phase and the application acknowledges messages with the **Standard ID (SID)** of 0x300. The **SID** can be changed by user commands.

The application is controlled by the user with a CLI implemented using the
serial UART core in the ADuCM3029 controller. The CLI is displayed on a
connected PC using a serial terminal connection.

The program is divided in 2 parts: the setup part in which the present module is
discovered and the main process.

|Main flow chart|

To replicate the CAN FD bus described in the example both boards need to be
connected to each other via the P1 or P4 connectors on the board and each in
turn connected to the Arduino form factor headers of the ADICUP3029. Then each
ADICUP3029 needs to be connected to the PC via USB to provide serial terminal
CLI interface for each node.

|image1|

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029 (Qty 2)
   -  EVAL-ADM3055E-ARDZ (Qty 2)
   -  Micro USB to USB cable
   -  Dual WR-DSUB connector cable or twisted pair cable
   -  PC or Laptop with a USB port

.. note::

   The circuit might need an external power supply of 5V to run in some
   circumstances.

-  Software

   -  :git-EVAL-ADICUP3029:`ADuCM3029_demo_cn0401 demo application <projects/ADuCM3029_demo_cn0401>`
   -  CrossCore Embedded Studio (2.8.0 or higher)
   -  ADuCM302x DFP (3.2.0 or higher)
   -  ADICUP3029 BSP (1.1.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the Hardware
-----------------------

-  Connect **EVAL-ADM3055E-PMDZ** board to the **EVAL-ADICUP3029** as seen in the pictures below:

.. image:: ../images/cn0401_single_node.jpg
   :align: center

-  Connect the boards with each other with either a **WR-DSUB** cable or a pair of wires:

.. image:: ../images/cn0401_bus_connection.jpg
   :align: center

-  Connect a micro-USB cable to P10 connector of each of the the EVAL-ADICUP3029
   boards and connect them to a computer.

Configuring the Software
------------------------

Most of the configuration parameters can be found in the CAN controller API
module. The CAN controller API will instantiate a handler that will determine
the initial configuration of the node. The handler is instantiated by the
initialization structure with the following form:

::

   struct can_ctrl_init_param {
       struct spi_init_param can_ctrl_spi_init;
       bool con_iso_crc_en;
       bool con_store_in_tef_en;
       bool con_txq_en;
       uint8_t tef_fifo_size; /* Number of messages in TEF FIFO*/
       bool tef_time_stamp_en;
       enum can_ctrl_fifo_plsize txq_plsize;
       uint8_t txq_fifo_size; /* Number of messages in TXQ FIFO */
       uint8_t txq_tx_priority; /* 0 is lowest; 0x1f is highest */

       uint8_t tx_fifo_nr;
       enum can_ctrl_fifo_plsize tx_fifo_plsize;
       uint8_t tx_fifo_size; /* Number of messages in FIFO */
       uint8_t tx_fifo_priority; /* 0 is lowest; 0x1f is highest */

       uint8_t rx_fifo_nr;
       enum can_ctrl_fifo_plsize rx_fifo_plsize;
       uint8_t rx_fifo_size; /* Number of messages in FIFO */
       bool rx_fifo_tsen;

       uint8_t rx_flt_nr;
       uint16_t rx_sid_addr;

       enum can_ctrl_nominal_bitrate can_nbt;
       enum can_ctrl_data_bitrate can_dbt;
       enum can_ctrl_ssp_mode ssp_mode;
   };

The following is a non-exhaustive list that contains the most important
parameters and their values:

-  **can_dbt** - Data bit rate; values are contained into the following enum:

<code> enum can_ctrl_data_bitrate {

::

     BITRATE_DBT_500K,
     BITRATE_DBT_833K,
     BITRATE_DBT_1M,
     BITRATE_DBT_1M5,
     BITRATE_DBT_2M,
     BITRATE_DBT_3M,
     BITRATE_DBT_4M,
     BITRATE_DBT_5M,
     BITRATE_DBT_6M7,
     BITRATE_DBT_8M,
     BITRATE_DBT_10M

}; </code>

-  **can_nbt** - Nominal bit rate; values are contained into the following enum:

<code> enum can_ctrl_nominal_bitrate {

::

     BITRATE_NBT_125K,
     BITRATE_NBT_250K,
     BITRATE_NBT_500K,
     BITRATE_NBT_1M

}; </code>

-  **rx_fifo_nr** - Number of the FIFO that will function as a RX FIFO. Between 1 and 31 when using TXQ and 0 and 31 hen not using TXQ.
-  **rx_fifo_plsize** - Payload size for input messages. CAN FD supports up to 64 bytes.
-  **rx_fifo_size** - Number of messages that will trigger an interrupt. Set to 1 to interrupt after every message.
-  **rx_fifo_tsen** - Enable/Disable timestamp for messages received in this FIFO.
-  **rx_flt_nr** - ID of the input filter active for this FIFO. can be between 0 and 7.
-  **rx_sid_addr** - SID value of the input filter. Only messages that contain this specific SID will be received in the attached FIFO. Can be between 0 and 0x3FF.
-  **tx_fifo_nr** - Number of the FIFO that will function as a TX FIFO. Between 1 and 31 when using TXQ and 0 and 31 hen not using TXQ.
-  **tx_fifo_plsize** - Payload size for output messages. CAN FD supports up to 64 bytes.
-  **tx_fifo_size** - Number of messages that need to be setup before transmission starts. Set to 1 to interrupt after every message.

These parameters can be changed in the **can_ctrl_get_config** function from the **can_obj_layer.c** file.

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

+------------------------+-----------------+----------------------------------------------------------------+
| Command                | Example         | Description                                                    |
+========================+=================+================================================================+
| General commands       |                 |                                                                |
+------------------------+-----------------+----------------------------------------------------------------+
| *h*                    | h               | Display available commands.                                    |
+------------------------+-----------------+----------------------------------------------------------------+
| Communication commands |                 |                                                                |
+------------------------+-----------------+----------------------------------------------------------------+
| *ct* <*msg*>           | ct Hello world! | Send a message through the CAN bus.                            |
|                        |                 | <*msg*> = Message to be sent.                                  |
+------------------------+-----------------+----------------------------------------------------------------+
| *css* <*sid*>          | css 245         | Set standard ID for the CAN messages sent.                     |
|                        |                 | <*sid*> = Standard ID in hexadecimal; between 0x000 and 0x3FF. |
+------------------------+-----------------+----------------------------------------------------------------+
| *cg*                   | ct              | Get received messages if any.                                  |
+------------------------+-----------------+----------------------------------------------------------------+
| *test*                 | test            | Perform a loopback test.                                       |
+------------------------+-----------------+----------------------------------------------------------------+

-  For the "h", "cg" and "test" commands press Enter without inserting any space afterwards.
-  For the "ct" and "css" commands, to invoke in application instructions, write
   just the command without parameters, insert a space afterwards and press
   Enter.

.. image:: ../images/cn0401_terminal_example.png
   :align: center

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0401.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0401** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0401 Hex File

   -  `AduCM3029_demo_cn0401.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0401.hex>`_

   Complete CN0401 Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0401 Source Code <projects/ADuCM3029_demo_cn0401>`

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

.. image:: ../images/cn0401_project_structure.png
   :align: center

Project structure includes:

-  CAN controller API module: can_obj_layer.c, can_obj_layer.h;
-  Main file ADuCM3029_demo_cn0401.c
-  Application module with files: cn0401.c, cn0401.h;
-  CLI module with files: cli.c, cli.h;
-  SPI platform driver module: spi.c, spi.h;
-  System delays module: delay.c, delay.h;
-  GPIO platform driver module: gpio.c, gpio.h;
-  External interrupts module: interrupt.c, interrupt.h;
-  UART platform driver module: uart.c, uart.h;
-  Platform drivers header: platform_drivers.h;
-  Error header: error.h;
-  Power core initialization module with files: power.c, power.h;
-  Timer and delay driver module with files: timer.c, timer.h.

*End of Document*

.. |Main flow chart| image:: ../images/cn0414_main_flowchart.png
.. |image1| image:: ../images/cn0401_can_bus_connect.png
