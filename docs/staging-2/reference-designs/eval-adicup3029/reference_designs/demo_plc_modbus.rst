.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029/reference_designs/demo_plc_modbus

.. _eval-adicup3029 reference_designs demo_plc_modbus:

Distributed Control System (DCS) Demo
=====================================

General Description/Overview
----------------------------

The Distributed Control System reference design is a hardware and software
platform for developing HART-enabled analog input and output modules (or nodes).
DCS Modules are assembled from several existing reference designs:

- EVAL-ADICUP3029 is the processor board that implements a MODBUS slave and
  controls the analog input / output boards.
- EVAL-CN0416-ARDZ provides robust RS485 connectivity between one or more nodes
  and a host computer
- EVAL-CN0414-ARDZ provides four group-isolated voltage inputs and four HART
  enabled current inputs.
- EVAL-CN0418-ARDZ provides four group-isolated voltage or HART-enabled current
  outputs

The reference design provides software connectivity using the MODBUS protocol.
Modbus is a ubiquitous, open, industrial communication protocol for which there
are numerous open-source and commercial software libraries and utilities. It is
a serial master-slave protocol where the master uses a set of standard commands
to read and write registers on the slave device, and CRC error detection ensures
data integrity. Reading a slave register can give information about the state
and inputs of the slave and writing registers can change the state or outputs of
the slave. The mapping of Modbus registers to application-specific functions is
dependent on the end application, and the DCS reference design provides
convenient access to all of the functionality of the analog input and output
boards.

Several options for communicating with the hardware are provided or
demonstrated:

- A command-line interface, requiring only a terminal program on the host PC and
  no additional software, useful for initial board bringup and debug.
- An open-source Modbus debug tool
- A set of command-line utilities (Windows only)
- Example applications in Python, using an open-source Modbus library

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

- Hardware

  - EVAL-ADICUP3029
  - EVAL-CN0414-ARDZ and/or EVAL-CN0418-ARDZ, up to 4 boards total, in any
    configuration
  - EVAL-CN0416-ARDZ (not needed for direct USB connection to a single node)
  - Additional EVAL-CN0416-ARDZ, ADALM-UARTJTAG, and 2x5, 100mil cable such as
    :digikey:`AMP A3AAH-1006G <A3AAH-1006G>` or:

    - other RS485 host adapter

  - Mirco USB to USB cable
  - PC or Laptop with a USB port

- Software

  - :git-EVAL-ADICUP3029:`ADuCM3029_demo_cn0435 demo application <projects/ADuCM3029_demo_cn0435+>`
  - CrossCore Embedded Studio (2.8.0 or higher)
  - ADuCM302x DFP (3.2.0 or higher)
  - ADICUP3029 BSP (1.1.0 or higher)
  - Serial Terminal Program (Required for running in CLI mode only)

    - Such as Putty or Tera Term

  - Python 3.6 (only required for modifying example applications)

Setting up the Hardware
-----------------------

.. important::

   Depending on the PLC/DCS Node configuration the power needs to be provided as
   follows:

   - If the PLC/DCS Node contain at least a CN0418 board, then the power will be
     provided through any CN0418 board (the jumper for P17 MUST to be placed for
     each board).
   - If the PLC/DCS Node contain only CN0414 boards, then the power can be
     provided through any CN0414 board.

   Refer to the
   :dokuwiki:`CN0414 </resources/eval/user-guides/eval-adicup3029/hardware/cn0414>`
   and
   :dokuwiki:`CN0418 </resources/eval/user-guides/eval-adicup3029/hardware/cn0418>`
   user guides for detailed information on power requirements.

PLC / Single or multi-node DCS System Setup Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Block diagrams for PLC / single-node DCS and multi-node DCS systems are shown
below. These systems differ slightly in their allowable configurations:

- A Single-node system can operate with either half-duplex or full-duplex
  RS-485. Termination must be enabled at both ends of the RS-485 line(s).
- Modbus address conflict is not a concern in a single-node system (but the
  address must be known to the host.)
- A Multi-node system can only operate in half-duplex mode.
- In a Multi-node system, termination must be enabled at the ends of the RS-485
  line, which is most often the host RS485 adapter and most distant node.
- Each node in a multi-node system must be set to a different address.

PLC / Single-node DCS System block diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/plc_block_diagram.png

DCS System block diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/dcs_block_diagram.png

RS485 Adapter Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An ADALM-UARTJTAG board and a spare CN0416 can function as a convenient USB
Virtual COM port to RS-485 adapter. Any RS485 adapter should work, if another is
available. Isolated / Non-Isolated depends on the application and difference in
ground potential between the host and nodes. Full-duplex operation is only
supported in the PLC/single-node DCS configuration, as both TX and RX signals
are driven continuously. Both single-node and multi-node configurations can use
half-duplex.

The ADALM-UARTJTAG Setup requires configuration. The CP2103 device must be programmed as follows to control the DE signal on the
CN0416. Configure Silicon Labs Xpress Configurator as follows to program the
device:

Configure the IO2 as follows: Mode: Push-Pull, Alternate Function: RS-485, Active High.

Once the CP2103 is programmed, unplug from the host computer and connect P1 on
the ADALM-UARTJTAG to P11 on the CN0416 with a 2x5-socket, 100mil cable such as
:digikey:`AMP A3AAH-1006G <A3AAH-1006G>`. Be sure to connect with proper
polarity - pin 1 on the ADALM-UARTJTAG must correspond to pin 1 on the CN0416.

.. list-table::
   :header-rows: 1

   * - CN0416 Setup
     -
     -
     -
     -
   * -
     - Isolated Full Duplex
     - Isolated Half Duplex
     - Non-Isolated Full Duplex
     - Non-isolated Half Duplex
   * - S1 position
     - NA
     - NA
     - NA
     - NA
   * - S2 position
     - 2
     - 1
     - 3
     - 4
   * - S4 position
     - NA
     - NA
     - 2
     - 1
   * - S5 position
     - 2
     - 1
     - NA
     - NA
   * - S6 position
     - NA
     - NA
     - 2
     - 2
   * - S7 position
     - 2
     - 2
     - NA
     - NA

Node Configuration
~~~~~~~~~~~~~~~~~~

Configuration for each node is similar, noting that each node must be set to a
different address (via S1 on the CN0416) and the most distant node must have its
termination enabled (via S6 or S7 on CN0416.)

**CN0416 Setup** (Full-duplex only valid in a single-node system.)

.. list-table::
   :header-rows: 1

   * -
     - Isolated Full Duplex
     - Isolated Half Duplex
     - Non-Isolated Full Duplex
     - Non-isolated Half Duplex
     -
   * - S1 position
     - :dokuwiki:`Any position but different from node to node </resources/eval/user-guides/eval-adicup3029/hardware/cn0416#summary_of_switch_configurations>`
     -
     -
     -
     -
   * - S2 position
     - 2
     - 1
     - 3
     - 4
     -
   * - S4 position
     - NA
     - NA
     - 2
     - 1
     -
   * - S5 position
     - 2
     - 1
     - NA
     - NA
     -
   * - S6 position
     - NA
     - NA
     - 2
     - 2
     -
   * - S7 position
     - 2
     - 2
     - NA
     - NA
     -
   * - CN0414 Setup (if available)
     -
     -
     -
     -
     -
   * - P1 position
     -
       :dokuwiki:`Any position from MULTI configuration </resources/eval/user-guides/eval-adicup3029/hardware/cn0414#multiple_boards_stacked>`
     -
     -
     -
     -
   * - P2 position
     -
     -
     -
     -
     -
   * - P10 position
     -
       :dokuwiki:`Any position to result a different EEPROM address from board to board </resources/eval/user-guides/eval-adicup3029/hardware/cn0414#eeprom_address_configurations>`
     -
     -
     -
     -
   * - P11 position
     -
     -
     -
     -
     -
   * - P12 position
     -
     -
     -
     -
     -
   * - JP1 position
     - :dokuwiki:`MULTI configuration position </resources/eval/user-guides/eval-adicup3029/hardware/cn0414#eeprom_configuration_for_single_or_multiple_boards_configuration_jp1>`
     -
     -
     -
     -
   * - CN0418 Setup (if available)
     -
     -
     -
     -
     -
   * - P10 position
     -
       :dokuwiki:`Any position from MULTI configuration </resources/eval/user-guides/eval-adicup3029/hardware/cn0418#general_setup>`
     -
     -
     -
     -
   * - P9 position
     -
     -
     -
     -
     -
   * - JP2 position
     -
       :dokuwiki:`Any position to result a different EEPROM address from board to board </resources/eval/user-guides/eval-adicup3029/hardware/cn0418#general_setup>`
     -
     -
     -
     -
   * - JP3 position
     -
     -
     -
     -
     -
   * - JP4 position
     -
     -
     -
     -
     -
   * - JP1 position
     - :dokuwiki:`MULTI configuration position </resources/eval/user-guides/eval-adicup3029/hardware/cn0418#general_setup>`
     -
     -
     -
     -
   * - P17 position
     - Jumper should be placed to power the whole system
     -
     -
     -
     -
   * - EVAL-ADICUP3029
     -
     -
     -
     -
     -
   * - S2 position
     - :dokuwiki:`ARDUINO position </resources/eval/user-guides/eval-adicup3029/hardware/adicup3029#uart_switch>`
     -
     -
     -
     -
   * - S5 position
     - :dokuwiki:`WALL/USB position </resources/eval/user-guides/eval-adicup3029/hardware/adicup3029#power_switch>`
     -
     -
     -
     -

Direct USB connection
~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0435_cli_setup.png

Direct USB Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

The CLI program does not need the **EVAL-CN0416-ARDZ** board and is not affected
by it"s presence either. Furthermore, the PLC/ single-node DCS configuration can
also operate with a direct connection, useful for testing out individual nodes
quickly.

.. list-table::
   :header-rows: 1

   * - EVAL-ADICUP3029
     -
     -
   * - S2 position
     - :dokuwiki:`USB position </resources/eval/user-guides/eval-adicup3029/hardware/adicup3029#uart_switch>`
     -
   * - S5 position
     - :dokuwiki:`WALL/USB position </resources/eval/user-guides/eval-adicup3029/hardware/adicup3029#power_switch>`
     -

MODBUS Implementation
---------------------

There are four types of standard registers in the MODBUS slave:

.. list-table::
   :header-rows: 1

   * - Coil/Register Number
     - Data addresses
     - Types
     - Names
   * - 1 - 9999
     - 0 to 270E
     - Read-Write
     - Discreet Output Coils
   * - 10001 - 19999
     - 0 to 270E
     - Read-Only
     - Discreet Input Contacts
   * - 30001 - 39999
     - 0 to 270E
     - Read-Only
     - Analog Input Registers
   * - 40001 - 49999
     - 0 to 270E
     - Read-Write
     - Output Holding Registers

Each of these registers have a 16-bit address and a 16-bit value.

The **Discreet Output Coils** are registers that control a single output wire
that has a binary value (high or low). Reading this register returns the output
value of the bit and writing to it will update the coil with either low value,
for writing 0, or high value, for writing anything else. The **Discreet Input
Contacts** are registers that represent the value of a single input logic wire.
The register can be only read and it is 0 if the wire is logic low and 0XFFFF if
the wire is logic high. The DCS reference design does not have any functions
that would map to **Discreet Output Coils** or **Discreet Input Contacts**. The
**Analog Input Registers** represent an analog value, usually from an analog
wire. This register can be only read and returns a 16-bit value. The **Output
Holding Registers** are registers that control an analog output or a state of
the slave. Reading this register returns the state of a process or an output and
writing to it may change them or start a process.

Each register can be accessed using a function code:

.. list-table::
   :header-rows: 1

   * - Function code
     - Action
     - Table name
   * - 1 (0x01)
     - Read
     - Discreet Output Coils
   * - 5 (0x05)
     - Write Single
     - Discreet Output Coils
   * - 15 (0x0F)
     - Write Multiple
     - Discreet Output Coils
   * - 2 (0x02)
     - Read
     - Discreet Input Contacts
   * - 4 (0x04)
     - Read
     - Analog Input Registers
   * - 3 (0x03)
     - Read
     - Output Holding Registers
   * - 6 (0x06)
     - Write Single
     - Output Holding Registers
   * - 16 (0x10)
     - Write Multiple
     - Output Holding Registers

DCS reference design MODBUS Register Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because the DCS reference design may contain any combination of up to four input
or output boards, as a **MODBUS slave**, it contains two type of **MODBUS
registers**: common and board specific.

The common registers are 5 read-only registers and 2 read-write registers. In
standard **MODBUS terminology** that translates to 5 analog input registers and
2 holding registers:

.. list-table::
   :header-rows: 1

   * - Name
     - Address
     - Type
     - Description
   * - Detected boards
     - 0x0000
     - Analog Input Register
     - Number of input and/or output boards present in the system.
   * - First board data
     - 0x0001
     - Analog Input Register
     - First board type (bit 0), First board CS address (bits 1,2)
   * - Second board data
     - 0x0002
     - Analog Input Register
     - Second board type (bit 0), Second board CS address (bits 1,2)
   * - Third board data
     - 0x0003
     - Analog Input Register
     - Third board type (bit 0), Third board CS address (bits 1,2)
   * - Fourth board data
     - 0x0004
     - Analog Input Register
     - Fourth board type (bit 0), Fourth board CS address (bits 1,2)
   * - Update rate MSW
     - 0x00FE
     - Output Holding Register
     - Most significant word of the update rate.
   * - Update rate LSW
     - 0x00FF
     - Output Holding Register
     - Least significant word of the update rate.

The **board type** bit is ``0`` for **CN0414** and ``1`` for **CN0418**.

The **update rate** is stored as:

::

   Update rate MSW = ((Actual update rate * 10000) & 0xFFFF0000) >> 16;
   Update rate LSW = ((Actual update rate * 10000) & 0x0000FFFF) >> 0;

So the equation used to retrieve the update rate is:

<m 16> Actual update rate = {(Update rate MSW \* 65536) + Update rate
LSW}/{10000} </m>

Or in code form:

::

   Actual update rate = (((Update rate MSW << 16) & 0xFFFF0000) | Update rate LSW) / 10000;

The register map is configured dynamically after power-up. Adding a board to the
system adds a number of board specific registers: 50 analog input registers and
7 output holding registers for each **EVAL-CN0414-ARDZ**, and 30 analog input
registers and 10 output holding registers for each **EVAL-CN0418-ARDZ**.

As stated before, adding an **EVAL-CN0414-ARDZ** adds 57 registers to the
device: 50 analog input registers and 7 output holding registers. The analog
input registers are: 16 for ADC input values, 4 for ADC input open wire
detection flags and 50 for HART receive buffer. The output holding registers
are: 1 for ADC output coding, 1 for ADC filter options, 1 for ADC postfilter
options, 1 for ADC output data rate options, 1 for ADC open wire detection
enable, 1 for HART command zero and 1 for HART channel select. The output
holding registers are: 16 for the channel registers, 4 for Open Wire Detection
and 30 for the HART input buffer. Adding an **EVAL-CN0418-ARDZ** adds 40
registers: 30 analog input registers and 10 output holding registers. There are
30 HART input registers as analog input registers. The output holding registers
are: 4 for channel ranges (one for each channel), 4 for the channels output (one
for each channel), 1 for the HART active channel and 1 for the HART command
zero.

.. tip::

   Note that being a dynamic system the registers presented below do not have an
   unique address, but have an address offset that can be used to calculate
   their address. The function is:

   ::

      Address = (ADC_CS_address << 12) + (MODBUS_slave_address << 8) + Address_offset;

Register map for the **EVAL-CN0414-ARDZ**:

.. list-table::
   :header-rows: 1

   * - Name
     - Address Offset
     - Type
     - Description
   * - Channel 1 MSW
     - 0x05
     - Analog Input Register
     - Most significant word of the first ADC channel.
   * - Channel 1 LSW
     - 0x06
     - Analog Input Register
     - Least significant word of the first ADC channel.
   * - Channel 2 MSW
     - 0x07
     - Analog Input Register
     - Most significant word of the second ADC channel.
   * - Channel 2 LSW
     - 0x08
     - Analog Input Register
     - Least significant word of the second ADC channel.
   * - …
     - …
     - …
     - …
   * - Channel 8 MSW
     - 0x13
     - Analog Input Register
     - Most significant word of the eighth ADC channel.
   * - Channel 8 LSW
     - 0x14
     - Analog Input Register
     - Least significant word of the eighth ADC channel.
   * - Channel 1 OWD
     - 0x15
     - Analog Input Register
     - Open wire detection flag of the first voltage channel.
   * - Channel 2 OWD
     - 0x16
     - Analog Input Register
     - Open wire detection flag of the second voltage channel.
   * - Channel 3 OWD
     - 0x17
     - Analog Input Register
     - Open wire detection flag of the third voltage channel.
   * - Channel 4 OWD
     - 0x18
     - Analog Input Register
     - Open wire detection flag of the fourth voltage channel.
   * - HART IN 1
     - 0x19
     - Analog Input Register
     - First word of the HART input buffer.
   * - HART IN 2
     - 0x1A
     - Analog Input Register
     - Second word of the HART input buffer.
   * - …
     - …
     - …
     - …
   * - HART IN 30
     - 0x36
     - Analog Input Register
     - 50th word of the HART input buffer.
   * - ADC Output Code
     - 0x00
     - Output Holding Register
     - Set the output coding for the ADC:
       0 - bipolar coding (default);
       1 - unipolar coding.
   * - ADC Filter
     - 0x01
     - Output Holding Register
     - Set the input filter for the ADC:
       0 - s5+s1 (default);
       1 - s3.
   * - ADC Postfilter
     - 0x02
     - Output Holding Register
     - Set the input postfilter for the ADC:
       0 - 27 SPS, 47 dB rejection, 36.7 ms settling;
       1 - 25 SPS, 62 dB rejection, 40 ms settling;
       2 - 20 SPS, 86 dB rejection, 50 ms settling;
       3 - 16.67 SPS, 92 dB rejection, 60 ms settling;
       4 - disable postfilter (default).
   * - ADC ODR
     - 0x03
     - Output Holding Register
     - Set the output data rate for the ADC:
       [0-5] - 31250 SPS (default);
       6 - 15625 SPS;
       7 - 10417 SPS;
       8 - 5208 SPS;
       9 - 2597 SPS;
       10 - 1007 SPS;
       11 - 503.8 SPS;
       12 - 381 SPS;
       13 - 200.3 SPS;
       14 - 100.5 SPS;
       15 - 59.52 SPS;
       16 - 49.68 SPS;
       17 - 20.01 SPS;
       18 - 16.63 SPS;
       19 - 10 SPS;
       20 - 5 SPS;
       21 - 2.5 SPS;
       22 - 1.25 SPS;
   * - ADC OWD EN
     - 0x04
     - Output Holding Register
     - Enable/disable open wire detection for the ADC:
       0 - disable OWD (default);
       1 - enable OWD.
   * - HART cmd 0
     - 0x05
     - Output Holding Register
     - Writing ``1`` to this register sends HART command 0 then the register
       resets to ``0``.
   * - HART CH select
     - 0x06
     - Output Holding Register
     - Select enable a current channel for HART communication:
       0 - Channel 1 (default);
       1 - Channel 2;
       2 - Channel 3;
       3 - Channel 4.

Register map for the **EVAL-CN0418-ARDZ**:

.. list-table::
   :header-rows: 1

   * - Name
     - Address Offset
     - Type
     - Description
   * - HART IN 1
     - 0x05
     - Analog Input Register
     - First word of the HART input buffer.
   * - HART IN 2
     - 0x06
     - Analog Input Register
     - Second word of the HART input buffer.
   * - …
     - …
     - …
     - …
   * - HART IN 30
     - 0x22
     - Analog Input Register
     - 50th word of the HART input buffer.
   * - Channel 1 range
     - 0x00
     - Output Holding Register
     - Output range for the first DAC channel:
       0 - 0V to 5V;
       1 - 0V to 10V;
       2 - -5V to 5V;
       3 - -10V to 10V;
       4 - 4ma to 20ma;
       5 - 0ma to 20ma;
       6 - 0ma to 24ma.
   * - Channel 2 range
     - 0x01
     - Output Holding Register
     - Output range for the second DAC channel:
       0 - 0V to 5V;
       1 - 0V to 10V;
       2 - -5V to 5V;
       3 - -10V to 10V;
       4 - 4ma to 20ma;
       5 - 0ma to 20ma;
       6 - 0ma to 24ma.
   * - Channel 3 range
     - 0x02
     - Output Holding Register
     - Output range for the third DAC channel:
       0 - 0V to 5V;
       1 - 0V to 10V;
       2 - -5V to 5V;
       3 - -10V to 10V;
       4 - 4ma to 20ma;
       5 - 0ma to 20ma;
       6 - 0ma to 24ma.
   * - Channel 4 range
     - 0x03
     - Output Holding Register
     - Output range for the fourth DAC channel:
       0 - 0V to 5V;
       1 - 0V to 10V;
       2 - -5V to 5V;
       3 - -10V to 10V;
       4 - 4ma to 20ma;
       5 - 0ma to 20ma;
       6 - 0ma to 24ma.
   * - Channel 1
     - 0x04
     - Output Holding Register
     - Output code of the first DAC channel.
   * - Channel 2
     - 0x05
     - Output Holding Register
     - Output code of the second DAC channel.
   * - Channel 3
     - 0x06
     - Output Holding Register
     - Output code of the third DAC channel.
   * - Channel 4
     - 0x07
     - Output Holding Register
     - Output code of the fourth DAC channel.
   * - HART cmd 0
     - 0x08
     - Output Holding Register
     - Writing ``1`` to this register sends HART command 0 then the register
       resets to ``0``.
   * - HART CH select
     - 0x09
     - Output Holding Register
     - Select enable a current channel for HART communication:
       0 - Channel A (default);
       1 - Channel B;
       2 - Channel C;
       3 - Channel D.

Configuring the Software
------------------------

The software can be set up to work in CLI debug mode or in MODBUS mode. To set
this make sure the relevant define in the **config.h** file is uncommented and
the other one is commented:

::

   //#define CLI_INTEFACE
   //#define MODBUS_INTERFACE

Communicating with the DCS reference design
-------------------------------------------

There are two interfaces available for this application: a **Command Line
Interface (CLI)** used mainly for debugging a single **PLC** node and a **MODBUS
interface** used for **PLC**/**DCS** operation for single and multiple nodes.

The **CLI** is implemented through **UART** and must be connected to a computer
via **USB cable**. A serial terminal program must run on the **host PC** to
display data and control the application.

The **MODBUS** is connected through the **EVAL-CN0416-ARDZ** **UART** to
**RS485** adapter and must communicate with a **MODBUS master** on the **RS485
line**.

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

Serial Terminal Output
^^^^^^^^^^^^^^^^^^^^^^

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-serial-terminal-setup
   :end-before: .. end-serial-terminal-setup

Available Commands
^^^^^^^^^^^^^^^^^^

Typing **help** or **h** after initial calibration sequence will display the
list of commands and their short versions. The **CLI mode** has a board command
menu which is only used to select the board. Each board present in the system
has it"s own command set based on the type.

Bellow is the short command list for the board menu:

.. list-table::
   :header-rows: 1

   * - Command
     - Description
   * - *h*
     - Display available commands.
   * - *bs*
     - Set the active board.
       <*board_no*> = de ID of the board assigned by the program. It its
       displayed at the start of the program. Calling this command without an
       argument displays available boards again.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0435_main_menu_cli.png

The specific commands for each of the types of boards is described in they
respective wiki pages:

- :dokuwiki:`EVAL-CN0414-ARDZ specific commands </resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0414#available_commands>`
- :dokuwiki:`EVAL-CN0418-ARDZ specific commands </resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0418#available_commands>`

Modbus Interface
~~~~~~~~~~~~~~~~

The Modbus protocol is not human-readable; as such, a Modbus master program is
required to interact with the design. QModMaster is a free and open-source
implementation of a Modbus master GUI application. This program is useful for
board bringup and debug, and during application development. QModMaster is
avalable at
`QModMaster on SourceForge <https://sourceforge.net/projects/qmodmaster/>`__

QModMaster is used to demonstrate several basic register operations below.

.. list-table::

   * - Common analog input registers read
     -
     -
   * - Reading these registers with 2 **EVAL-CN0414-ARDZ** and 2 **EVAL-CN0418-ARDZ** connected to the system it can be seen that 4 boards are found at address ``0000``.
     -

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0435_qmodmaster_general_reg.png
         :width: 1500px

     -
   * - The next address read ``0001`` indication that the board is a **EVAL-CN0418-ARDZ** and has address 0;
     -
     -
   * - The second address reads ``0003`` indication that the board is **EVAL-CN0418-ARDZ** and has the address 1;
     -
     -
   * - The third register read ``0004`` indicating that the board is **EVAL-CN0414-ARDZ** and has address 2;
     -
     -
   * - And the last register reads ``0006`` for **EVAL-CN0414-ARDZ** and address 3.
     -
     -
   * - ADC channels of one of the input boards with **MODBUS**
     -
     -
   * - The second read shows the input channels data for the last input board found. This is done by reading 16 analog input registers fount at address 0x3105.
     -

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0435_qmodmaster_adc_read.png

     -
   * - ADC change the output code
     -
     -
   * - This is an example on how to change the ADC output code of the third board (input board with address 3) by writing the output holding register at the address 0x3100.
     -

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0345_write_holding_register_1.png

     -
   * -
     -

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0345_write_holding_register_2.png

     -

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0435.

#. Dragging and Dropping the .Hex to the Daplink drive
#. Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0435** can be found here:

.. admonition:: Download

   Prebuilt CN0435 Hex File

   - :git-EVAL-ADICUP3029:`ADuCM3029_demo_cn0435.Hex <Latest/ADuCM3029_demo_cn0435.hex+>`

   Complete CN0435 Source Files

   - :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0435 Source Code <projects/ADuCM3029_demo_cn0435+>`

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore
Embedded Studio. For more information on downloading the tools and a quick start
guide on how to use the tool basics, please check out the
:dokuwiki:`Tools Overview page. </resources/eval/user-guides/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to import existing projects into your workspace </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_import_existing_projects_into_your_workspace>`
section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into
the CrossCore Embedded Studios tools, please view our
:dokuwiki:`How to configure the debug session </resources/eval/user-guides/eval-adicup3029/tools/cces_user_guide#how_to_configure_the_debug_session_for_an_aducm3029_application>`
section.

Project Structure
~~~~~~~~~~~~~~~~~

The application controls a dynamic system that can be physically different every
time it is run. to do this it has two parts:

#. The system initialization.
#. The system main process.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0435_main_flow.png

After getting parameters of the system supplied by the user in code the program
initializes the software modules common to all the boards: I2C, UART, SPI,
microcontroller power, software UART and the AD5700 HART modem. If the MODBUS
interface is used, the update timer for the input boards is also initialized in
this stage as a common module. If, by comparison, the CLI is used, each input
board present initializes its own version of the update timer driver.

After these initializations the system runs a board discovery routine. By using
the presence of I2C EEPROM memory and testing the SPI configuration, all boards
in the system are discovered and labeled as either CN0414 or CN0418. If the
MODBUS interface is used, the system also scans for its MODBUS slave address and
maps and initializes MODBUS registers.

After board discovery, if the CLI is used, no board is set as active and the
system manager loads the main menu process. If the MODBUS is used, the system
activates the first board it discovers.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0435_initialization.png

CLI Process
^^^^^^^^^^^

If the CLI is used, no board is active after the initialization and the system
stands by to receive commands. If the user sets one of the boards to be active,
the program loads the commands and process specific to that board and starts
sunning them until the application is stopped or the ``exit`` command is called.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0435_cli_process.png

MODBUS Interface Process
^^^^^^^^^^^^^^^^^^^^^^^^

If the MODBUS interface is used the first board discovered is the active board.
If it is a CN0414 the program runs its process until all channels are updated.
If it is a CN0418 the program runs its process only once. After this the system
deactivates the board and activates the next board discovered until all the
boards have been active and updated. The system than cycles back from the
beginning.

Meanwhile the system scans the MODBUS channel for commands and if one is found
that is addressed to this node it executes it and sends back a response.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/cn0435_modbus_process.png

Board Specific Processes
^^^^^^^^^^^^^^^^^^^^^^^^

The process and commands for each type of boards is described in the appropriate
application page:

- :dokuwiki:`EVAL-CN0414-ARDZ </resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0414#project_structure>`
- :dokuwiki:`EVAL-CN0418-ARDZ </resources/eval/user-guides/eval-adicup3029/reference_designs/demo_cn0418#project_structure>`

Example Applications and Utilities
----------------------------------

User DCS programs running on the host will be highly application-specific, and
written in any number of languages. This section presents several example
applications and utilities written in Python that perform basic functions such
as reading and writing analog voltages, detecting the configuration of a node,
and changing the data rate of an analog input channel.

Utility functions in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following utility functions are demonstrated using the single-node
configuration described above. It may be connected to the host either directly
via USB (no RS485 interface) or over a USB to RS485 bridge. Minimalmodbus is an
open-source (Apache license) Modbus RTU and Modbus ASCII implementation for
Python, and is used in these examples. Similar libraries exist for other
languages.

Read common analog input registers basic example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, consider an instrument (slave) with Modbus RTU and address number 1
to which we are to communicate via a serial port with the name ``COM12``. The
instrument stores the actual configuration in registers 0 to 4. To read data
from the instrument:

.. code:: python

   """Read common analog input registers to determine PLC/DCS configuration."""

   import minimalmodbus

   # declare an instrument object with port name, slave address as input arguments
   INSTRUMENT = minimalmodbus.Instrument('COM12', 1)

   # read 5 registers starting from address 0 by using function code 4
   COMMON_ANALOG_INPUT_REGISTERS = INSTRUMENT.read_registers(
       registeraddress=0, numberOfRegisters=5, functioncode=4)

   # result a list with 5 elements in decimal format
   print(COMMON_ANALOG_INPUT_REGISTERS)

::

   [4, 1, 3, 4, 6]

In this example, after we run the above piece of code it results that we have 4
boards connected. Two of this boards are **EVAL-CN0414-ARDZ** and other two are
**EVAL-CN0418-ARDZ**. The **EVAL-CN0414-ARDZ** boards have address 0b10 and 0b11
while **EVAL-CN0418-ARDZ** boards have address 0b00 and 0b01.

Read analog input registers basic example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, if we want to read all analog input channels from one **EVAL-CN0414-ARDZ**
we can use the following:

.. code:: python

   """Read analog input registers to determine ADC channels code."""

   import minimalmodbus

   # declare an instrument object with port name, slave address as input arguments
   INSTRUMENT = minimalmodbus.Instrument('COM12', 1)

   # read 16 registers starting from address 12549 by using function code 4
   ADC_CHANNELS_CODES = INSTRUMENT.read_registers(
       registeraddress=12549, numberOfRegisters=16, functioncode=4)

   # result a list with 16 elements in decimal format
   print(ADC_CHANNELS_CODES)

::

   [127, 65158, 127, 65514, 127, 65194, 127, 64995, 127, 65285, 127, 65244, 127, 65292, 127, 65278]

In this example, after we run the above piece of code it results a list of 16
elements in decimal format. First 8 values corespond to voltage channels and
last to current channels.

Read and write one output holding register for EVAL-CN0414-ARDZ example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, if we want to change the output code of one **EVAL-CN0414-ARDZ** ADC to be
unipolar instead of bipolar we can use the following:

.. code:: python

   """Read and write one output holding register to change ADC output code."""

   import minimalmodbus

   # declare an instrument object with port name, slave address as input arguments
   INSTRUMENT = minimalmodbus.Instrument('COM12', 1)

   # read a single register from address 12544 by using function code 3
   INITIAL_ADC_OUTPUT_CODE = INSTRUMENT.read_register(
       registeraddress=12544, functioncode=3)

   # result an integer
   print(INITIAL_ADC_OUTPUT_CODE)

   # wrie a single register from address 12544 by using function code 6
   INSTRUMENT.write_register(registeraddress=12544, value=1, functioncode=6)

   # read a single register from address 12544 by using function code 3
   FINAL_ADC_OUTPUT_CODE = INSTRUMENT.read_register(
       registeraddress=12544, functioncode=3)

   # result an integer
   print(FINAL_ADC_OUTPUT_CODE)

::

   0
   1

In this example, after we run the above piece of code it results an integer
which coresponds to ADC coding format. The default value 0, indicate that the
ADC is set to bipolar coding format, while a value of 1 will indicate an
unipolar coding format.

Read and write one output holding register for EVAL-CN0418-ARDZ example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, if we want to change the output code of one **EVAL-CN0418-ARDZ** DAC
channel we can use the following:

.. code:: python

   """Read and write one output holding register to change DAC channel voltage."""

   import minimalmodbus

   # declare an instrument object with port name, slave address as input arguments
   INSTRUMENT = minimalmodbus.Instrument('COM12', 1)

   # read a single register from address 4356 by using function code 3
   INITIAL_DAC_CHANNEL_1_CODE = INSTRUMENT.read_register(
       registeraddress=4356, functioncode=3)

   # result an integer
   print(INITIAL_DAC_CHANNEL_1_CODE)

   # wrie a single register from address 4356 by using function code 6
   INSTRUMENT.write_register(registeraddress=4356, value=65535, functioncode=6)

   # read a single register from address 4356 by using function code 3
   FINAL_DAC_CHANNEL_1_CODE = INSTRUMENT.read_register(
       registeraddress=4356, functioncode=3)

   # result an integer
   print(FINAL_DAC_CHANNEL_1_CODE)

::

   0
   65535

In this example, after we run the above piece of code it results an integer
which coresponds to DAC channel 1 output code. Depending on channel
configuration this output code will corespond to a voltage or a current value.
In this example the DAC channel output code is by default 0V because the default
channel range is set to 0V to 5V. The 65535 value will corespond in this case to
a 5V output.

Detect system configuration example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, if we want to determine the system configuration we can run the following
script from the attached archive.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/detect_configuration.zip`

For a PLC configuration the script output will look similarly like this:

::

   Welcome! Use 'CTRL+C' to go back from the current menu or exit!

   Available devices:
   1 -> Silicon Labs CP210x USB to UART Bridge (COM12)
   2 -> Intel(R) Active Management Technology - SOL (COM3)

   Enter detected device index, or press ENTER to use COM12:
   No boards at MODBUS address: 1 No communication with the instrument (no answer)

   Boards found at MODBUS address: 2
   Address        Name                 Value
   -------------  -----------------  -------
   0000 (0x0000)  Detected boards          2
   0001 (0x0001)  First board data         4
   0002 (0x0002)  Second board data        6
   0003 (0x0003)  Third board data     65535
   0004 (0x0004)  Fourth board data    65535
   Analog input board at address: 10
   Analog input board at address: 11
   No boards at MODBUS address: 3 No communication with the instrument (no answer)
   No boards at MODBUS address: 4 No communication with the instrument (no answer)
   No boards at MODBUS address: 5 No communication with the instrument (no answer)
   No boards at MODBUS address: 6 No communication with the instrument (no answer)
   No boards at MODBUS address: 7 No communication with the instrument (no answer)
   No boards at MODBUS address: 8 No communication with the instrument (no answer)
   No boards at MODBUS address: 9 No communication with the instrument (no answer)
   No boards at MODBUS address: 10 No communication with the instrument (no answer)
   No boards at MODBUS address: 11 No communication with the instrument (no answer)
   No boards at MODBUS address: 12 No communication with the instrument (no answer)
   No boards at MODBUS address: 13 No communication with the instrument (no answer)
   No boards at MODBUS address: 14 No communication with the instrument (no answer)
   No boards at MODBUS address: 15 No communication with the instrument (no answer)
   No boards at MODBUS address: 16 No communication with the instrument (no answer)

For a DCS configuration the script output will look similarly like this:

::

   Welcome! Use 'CTRL+C' to go back from the current menu or exit!

   Available devices:
   1 -> Silicon Labs CP210x USB to UART Bridge (COM12)
   2 -> Intel(R) Active Management Technology - SOL (COM3)

   Enter detected device index, or press ENTER to use COM12:

   Boards found at MODBUS address: 1
   Address        Name                 Value
   -------------  -----------------  -------
   0000 (0x0000)  Detected boards          2
   0001 (0x0001)  First board data         1
   0002 (0x0002)  Second board data        3
   0003 (0x0003)  Third board data     65535
   0004 (0x0004)  Fourth board data    65535
   Analog output board at address: 00
   Analog output board at address: 01

   Boards found at MODBUS address: 2
   Address        Name                 Value
   -------------  -----------------  -------
   0000 (0x0000)  Detected boards          2
   0001 (0x0001)  First board data         4
   0002 (0x0002)  Second board data        6
   0003 (0x0003)  Third board data     65535
   0004 (0x0004)  Fourth board data    65535
   Analog input board at address: 10
   Analog input board at address: 11
   No boards at MODBUS address: 3 No communication with the instrument (no answer)
   No boards at MODBUS address: 4 No communication with the instrument (no answer)
   No boards at MODBUS address: 5 No communication with the instrument (no answer)
   No boards at MODBUS address: 6 No communication with the instrument (no answer)
   No boards at MODBUS address: 7 No communication with the instrument (no answer)
   No boards at MODBUS address: 8 No communication with the instrument (no answer)
   No boards at MODBUS address: 9 No communication with the instrument (no answer)
   No boards at MODBUS address: 10 No communication with the instrument (no answer)
   No boards at MODBUS address: 11 No communication with the instrument (no answer)
   No boards at MODBUS address: 12 No communication with the instrument (no answer)
   No boards at MODBUS address: 13 No communication with the instrument (no answer)
   No boards at MODBUS address: 14 No communication with the instrument (no answer)
   No boards at MODBUS address: 15 No communication with the instrument (no answer)
   No boards at MODBUS address: 16 No communication with the instrument (no answer)

Change or check the system registers example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Next, if we want to check or change the system registers we can run the
following script from the attached archive.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/read_or_write_registers.zip`

Depending on the system configuration, one or more DCS nodes will be detected.
After the user selects a valid DCS node, a menu will appear which contain all
available system options. Now, depending on the node configuration, not all
option will be valid, even if they are shown. For example, if a DCS node doesn"t
contain CN0414 analog input board(s), any option which refers to CN0414 will do
nothing.

::

   Welcome! Use 'CTRL+C' to go back from the current menu or exit!

   Available devices:
   1 -> Silicon Labs CP210x USB to UART Bridge (COM12)
   2 -> Intel(R) Active Management Technology - SOL (COM3)

   Enter detected device index, or press ENTER to use COM12:
   Enter MODBUS timeout (0.05[s] to inf), or press ENTER to use 0.1[s] timeout:

   Boards found at MODBUS address: 1
   Address        Name                 Value
   -------------  -----------------  -------
   0000 (0x0000)  Detected boards          2
   0001 (0x0001)  First board data         1
   0002 (0x0002)  Second board data        3
   0003 (0x0003)  Third board data     65535
   0004 (0x0004)  Fourth board data    65535
   analog output board at address: 00
   analog output board at address: 01

   Boards found at MODBUS address: 2
   Address        Name                 Value
   -------------  -----------------  -------
   0000 (0x0000)  Detected boards          2
   0001 (0x0001)  First board data         4
   0002 (0x0002)  Second board data        6
   0003 (0x0003)  Third board data     65535
   0004 (0x0004)  Fourth board data    65535
   analog input board at address: 10
   analog input board at address: 11
   No boards at MODBUS address: 3 No communication with the instrument (no answer)
   No boards at MODBUS address: 4 No communication with the instrument (no answer)
   No boards at MODBUS address: 5 No communication with the instrument (no answer)
   No boards at MODBUS address: 6 No communication with the instrument (no answer)
   No boards at MODBUS address: 7 No communication with the instrument (no answer)
   No boards at MODBUS address: 8 No communication with the instrument (no answer)
   No boards at MODBUS address: 9 No communication with the instrument (no answer)
   No boards at MODBUS address: 10 No communication with the instrument (no answer)
   No boards at MODBUS address: 11 No communication with the instrument (no answer)
   No boards at MODBUS address: 12 No communication with the instrument (no answer)
   No boards at MODBUS address: 13 No communication with the instrument (no answer)
   No boards at MODBUS address: 14 No communication with the instrument (no answer)
   No boards at MODBUS address: 15 No communication with the instrument (no answer)
   No boards at MODBUS address: 16 No communication with the instrument (no answer)

   Enter MODBUS address from this list [1, 2], or press ENTER to use MODBUS address 1:
   Enter commands delay (0[s] to inf), or press ENTER to use 0.1[s] delay:

   Test options:
   1 - Read common analog input registers.
   2 - Read common output holding registers.
   3 - Read analog input registers.
   4 - Read output holding registers.
   5 - Write output holding register.
   q - Quit.

   Enter test option:

Example Applications in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following section presents several example top-level DCS applications. Like
the utilities, these are based on Minimalmodbus.

Simple DCS control
^^^^^^^^^^^^^^^^^^

This application provides a simple way to control a DCS system and also to
detect HART devices by using the HART protocol.

The HART protocol is proprietary, customers implementing a full HART stack
should refer to https://fieldcommgroup.org This reference design provides a
basic implementation of ``command zero`` that can be used to verify connectivity
with HART instruments. CN0267 is a Complete 4 mA to 20 mA Loop Powered Field
Instrument with HART Interface that can be used to test the DCS HART
functionality. This application allows to:

- detect sistem configuration;
- configure and read ADC channels;
- configure and write DAC channels;
- configure HART modems and send HART command zero.

:download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/reference_designs/dcs_cn0435.zip`

::

   Welcome! Use 'CTRL+C' to go back from the current menu or exit!

   Available devices:
   1 -> Silicon Labs CP210x USB to UART Bridge (COM12)
   2 -> Intel(R) Active Management Technology - SOL (COM3)

   Enter detected device index, or press ENTER to use COM12:
   Enter MODBUS timeout (0.05[s] to inf), or press ENTER to use 0.1[s] timeout:

   Boards found at MODBUS address: 1
   Address        Name                 Value
   -------------  -----------------  -------
   0000 (0x0000)  Detected boards          2
   0001 (0x0001)  First board data         1
   0002 (0x0002)  Second board data        3
   0003 (0x0003)  Third board data     65535
   0004 (0x0004)  Fourth board data    65535
   analog output board at address: 00
   analog output board at address: 01

   Boards found at MODBUS address: 2
   Address        Name                 Value
   -------------  -----------------  -------
   0000 (0x0000)  Detected boards          2
   0001 (0x0001)  First board data         4
   0002 (0x0002)  Second board data        6
   0003 (0x0003)  Third board data     65535
   0004 (0x0004)  Fourth board data    65535
   analog input board at address: 10
   analog input board at address: 11
   No boards at MODBUS address: 3 No communication with the instrument (no answer)
   No boards at MODBUS address: 4 No communication with the instrument (no answer)
   No boards at MODBUS address: 5 No communication with the instrument (no answer)
   No boards at MODBUS address: 6 No communication with the instrument (no answer)
   No boards at MODBUS address: 7 No communication with the instrument (no answer)
   No boards at MODBUS address: 8 No communication with the instrument (no answer)
   No boards at MODBUS address: 9 No communication with the instrument (no answer)
   No boards at MODBUS address: 10 No communication with the instrument (no answer)
   No boards at MODBUS address: 11 No communication with the instrument (no answer)
   No boards at MODBUS address: 12 No communication with the instrument (no answer)
   No boards at MODBUS address: 13 No communication with the instrument (no answer)
   No boards at MODBUS address: 14 No communication with the instrument (no answer)
   No boards at MODBUS address: 15 No communication with the instrument (no answer)
   No boards at MODBUS address: 16 No communication with the instrument (no answer)

   Enter MODBUS address from this list [1, 2], or press ENTER to use MODBUS address 1:
   Enter commands delay (0[s] to inf), or press ENTER to use 0.1[s] delay:

   Use CTRL+C to end a process or switch between nodes.
   CN0414                                 CN0418                        CN0435
   -------------------------------------  ----------------------------  ----------------------------------------
   1 - Read device voltage channel        e - Set DAC channel 1 output  o - Read common analog input registers
   2 - Read device current channel        f - Set DAC channel 2 output  p - Read common output holding registers
   3 - Read board voltage channels        g - Set DAC channel 3 output  r - Read analog input registers
   4 - Read board current channels        h - Set DAC channel 4 output  s - Read output holding registers
   5 - Read instrument voltage channels   i - Set DAC channel 1 range   t - Detect system configuration
   6 - Read instrument current channels   j - Set DAC channel 2 range
   7 - Set ADC output code                k - Set DAC channel 3 range
   8 - Set ADC filter                     l - Set DAC channel 4 range
   9 - Set ADC postfilter                 m - Send HART command zero
   a - Set ADC output data rate           n - Select HART channel
   b - Set ADC open wire detection state
   c - Send HART command zero
   d - Select HART channel                                              q - Quit

   Enter Option:


