EVAL-AD5676RARDZ Evaluation Board User Guide
============================================

**Evaluation Board for the AD5676R WLCSP**

Features
--------

-  Full featured evaluation board for the :adi:`AD5676R` WLCSP
-  On-board or external power supply
-  On-board or external voltage reference
-  Arduino® Uno form-factor, mates with :adi:`SDP-K1`
-  PC control via :adi:`Analysis \| Control \| Evaluation (ACE) Software <ACE>`

Evaluation Kit Contents
-----------------------

-  EVAL-AD5676RARDZ

Hardware Required
-----------------

-  :adi:`SDP-K1` board - must be purchased separately
-  PC running on Windows 7 or later with USB 2.0 port

Software Required
-----------------

-  Latest :adi:`ACE` Software
-  NanoDAC ACE plugin - downloadable within ACE
-   :adi:`Link to Nanodac v1.2021.432000 Plugin <plugins/ace/board.nanodac.1.2021.43200.acezip>` - Check for the latest plugin

General Description
-------------------

This user guide details the operation of the EVAL-AD5676RARDZ for the AD5676R
WLCSP 16-bit, octal, voltage output, digital-to-analog converter (DAC).

The EVAL-AD5676RARDZ allows users to quickly prototype AD5676R circuits and
reduce design time. The AD5676R operates from a single 2.7 V to 5.5 V supply.
The AD5676R incorporates an internal 2.5 V reference to give a full-scale output
voltage of 2.5 V or 5 V. An ADR4525 is also provided on-board as a 2.5V
reference source. A different external reference voltage can be applied via the
EXT_REF SMB connector or test pin if needed.

The EVAL-AD5676RARDZ interfaces to the USB port of a PC via a system
demonstration platform board (SDP-K1 ). The Analysis \| Control \| Evaluation
(ACE) software is available for download from the EVAL-AD5676RARDZ product page
to use with the evaluation board to allow the user to program the AD5676R. A
peripheral module interface (PMOD) connection is also available to allow the
connection of microcontrollers to the evaluation board without the SDP-K1 board.
When a microcontroller is used through the PMOD connection, the SDP-K1 board
must be disconnected, and the user is unable to operate the ACE software.

The EVAL-AD5676RARDZ is compatible with the EVAL-SDP-CK1Z (SDP-K1), which should
be purchased separately. A typical connection between the EVAL-AD5676RARDZ and
the SDP-B controller board is shown below. For full details, see the AD5676R
data sheet, which must be used in conjunction with this user guide when using
the EVAL-AD5676RARDZ.

Evaluation Board Photograph
---------------------------

|Evaluation Board Photograph| |Evaluation Board Photograph with SDP-K1|

Evaluation Board Software Quick Start Procedure
-----------------------------------------------

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-AD5676RARDZ uses the ACE evaluation software, which allows the
evaluation and control of multiple evaluation systems.

The ACE installer installs the necessary SDP-K1 drivers and the Microsoft® .NET Framework 4 by default. The ACE software must be installed before connecting the SDP-K1 board to the USB port of the PC to ensure that the SDP-K1 board is recognized properly. For full instructions on how to install and use this software, see the :adi:`ACE` software page on the Analog Devices website.

After the installation is finished, the EVAL-AD5676RARDZ plug-in appears when
the ACE software is opened.

Initial Setup
~~~~~~~~~~~~~

To set up the evaluation board, take the following steps:

-  Connect the evaluation board to the SDP-K1 board, and then connect the USB cable between the SDP-K1 board and the PC.
-  Run the ACE application. The EVAL-AD5676RARDZ plug-ins appear in the attached hardware section of the Start tab.
-  Double-click the board plug-in to open the board view.
-  Double-click the AD5676R chip to access the chip block diagram. This view
   provides a basic representation of the functionality of the board.

**EVAL-AD5676RARDZ and SDP-K1 Board Connection**

.. image:: images/eval-ad5676rardz_and_sdp-k1_connection.png
   :alt: EVAL-AD5676RARDZ and SDP-K1 Board Connection
   :width: 400

**EVAL-AD5676RARDZ Plugin - Board View**

.. image:: images/plugin_board_view.png
   :alt: ACE Plugin - Board View
   :width: 400

**EVAL-AD5676RARDZ Plugin - Chip View**

.. image:: images/plugin_chip_view.png
   :alt: ACE Plugin - Chip View
   :width: 400

Functional Block Diagram and Description
----------------------------------------

The EVAL-AD5676RARDZ software is organized to appear similar to the functional
block diagram shown in the AD5676R datasheet, which simplifies correlating the
functions on the EVAL-AD5676RARDZ with the description in the AD5676R datasheet.

For a full description of each block, register, and its settings, see the
AD5676R datasheet.

Some of the blocks and their functions are described in this section as they
pertain to the evaluation board. The full-screen block diagram UI is shown
below.

.. image:: images/plugin_bd_with_labels.png
   :alt: Plugin - Block Diagram with Labels
   :width: 600

**Block Diagram Functions**

+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Label | Button/Function              | Function/Description                                                                                                                                                                                                                                                                               |
+=======+==============================+====================================================================================================================================================================================================================================================================================================+
| **A** | General Commands             | These consist of general command buttons with functions as follows.                                                                                                                                                                                                                                |
|       |                              | **Apply Changes** - Applies user inputs in the text fields, such as Label D, to the device.                                                                                                                                                                                                        |
|       |                              | **Read All** - Reads the AD5676R's registers. Applicable only to select registers.                                                                                                                                                                                                                 |
|       |                              | **Reset Chip** - Initiates the software reset sequence for AD5676R.                                                                                                                                                                                                                                |
|       |                              | **Diff** - Shows the registers that are different on the device.                                                                                                                                                                                                                                   |
|       |                              | **Software Defaults** - Returns all fields to the default settings.                                                                                                                                                                                                                                |
|       |                              | **Memory Map side-by-side** - Launches the Memory Map window side-by-side in the same window with the block diagram UI.                                                                                                                                                                            |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **B** | Configuration WIndow         | Used to set the configuration for the board. Select the gain setting from the **Output Gain** drop-down menu. A gain of 1 is the default. After setting up the initial configuration, click **Apply** to apply the values. These settings can be modified at any stage while evaluating the board. |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **C** | Select a Command             | Contains command drop-down menus as described below.                                                                                                                                                                                                                                               |
|       |                              | **Command option** drop-down menu selects how the user input data in **Label D** is transferred to the device. The user input data can be **(Option 1)** written to the input registers only or **(Option 2)** written to the input register and the DAC register **(Label E)**.                   |
|       |                              | **Channel group** drop-down menu selects which channels are displayed in the **Input Register** block **(Label D)**. **(Option1)** displays DAC Channel 0 to 3 while **(Option 2)** displays DAC Channel 4 to 7.                                                                                   |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **D** | Input Register               | 16-bit data word to be transferred to the device. Data word should be in hexadecimal format. Select the channel group **(Label C)** to write to from the drop-down menu. Click **Apply Changes (Label A)** to transfer this 16-bit data word to the device.                                        |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **E** | DAC Register                 | Displays the value that is currently present in the DAC register on the device. Update the DAC registers by selecting the appropriate command option or by toggling **Load DAC (Label G)** for specific channels or **Software LDAC (Label J)** for all channels.                                  |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **F** | Software RESET               | Returns the evaluation board and software to default values.                                                                                                                                                                                                                                       |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **G** | Load DAC                     | Users can individually control which channel loads the values from the input registers field **(Label D)** to the DAC register. Click this button to initiate the software LDAC function and transfer the contents of the channel input register to the channel DAC register.                      |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **H** | DAC Config                   | DAC configuration options provide access to individual channel configuration, mainly, the power-down option, which can be set to either of the 3 states: **Normal**, **1kΩ to GND**, or **Tri-state**. See datasheet for more info.                                                                |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **I** | Internal Reference           | Configuration to **Enable**/**Disable** the on-chip reference. Note that the on-chip reference is enabled by default. Make sure to disable the on-chip reference when using an external reference source.                                                                                          |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **J** | Software LDAC (All Channels) | Loads the data word entered in the Input Registers field **(Label D)** to the device's DAC Register. Unlike the **Load DAC (Label G)**, this command applies to all 8 channels of the AD5676R.                                                                                                     |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **K** | Memory Map                   | Launches the Memory Map window in a separate tab as the Block Diagram window. See Memory Map for more details.                                                                                                                                                                                     |
+-------+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Memory Map
~~~~~~~~~~

All registers are fully accessible from the **AD5676R Memory Map** tab as shown below. This tab allows registers to be edited at the bit level. The bits shaded in dark gray are read-only bits and cannot be accessed from the ACE software. All other bits can be toggled.

.. image:: images/plugin_memory_map.png
   :alt: Plugin - Memory Map
   :width: 800

All changes made in the memory map tab correspond to the block diagram. For example, if the internal register bit is enabled, it displays as enabled on the block diagram. Any bits or registers that are shown in bold in the memory map tab are modified values that have not been transferred to the evaluation board. Click **Apply Changes** to transfer the data to the evaluation board.

.. image:: images/plugin_memory_map_unsaved.png
   :alt: Plugin - Memory Map with Unsaved Changes
   :width: 800

Evaluation Board Hardware
-------------------------

Power Supplies
~~~~~~~~~~~~~~

The EVAL-AD5676RARDZ provides an onboard 3.3 V regulator powered through the USB
supply for the AD5676R main supply. If a different supply is required or if the
evaluation board is controlled through the PMOD connector, an external supply
must be provided by the external supply voltage (P8) connector. See the below
table for more details.

An onboard 2.5V reference (ADR4525) is also provided. Every supply is decoupled
to the ground with 10 µF tantalum and 0.1 µF ceramic capacitors.

**PowerSupply Connectors**

=============== =================================================
Connector Label External Voltage Supplies Description
=============== =================================================
P8, Pin 1       External analog power supply from 2.7 V to 5.5 V.
P8, Pin 2       Analog ground.
EXT_REF         External voltage reference.
=============== =================================================

Link Options
~~~~~~~~~~~~

Several link options are incorporated on the EVAL-AD5676RARDZ and must be set
for the required operating conditions before using the board. The functions of
these link options are described in the table below.

**Link Functions**

+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Link Name    | Description                                                                                                                                                   |
+==============+===============================================================================================================================================================+
| VDD_SEL, P10 | This link selects the analog voltage source for the AD5676R. There are three options, as follows:                                                             |
|              | **5V0** - 5V supply from the SDP-K1 or the PMOD connectors.                                                                                                   |
|              | **3V3** - 3.3V supply from onboard LDO powered by the 5V0 supply.                                                                                             |
|              | **EXT** - 2.7V to 5.5V supply from an external source connected to P8.                                                                                        |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REF_LDO_SEL  | This link selects the analog voltage source for the onboard 2.5V reference :adi:`ADM7160`. There are three options, as follows:                               |
|              | **5V0** - 5V supply from the SDP-K1 or the PMOD connectors.                                                                                                   |
|              | **3V3** - 3.3V supply from onboard LDO powered by the 5V0 supply.                                                                                             |
|              | **EXT** - 2.7V to 5.5V supply from an external source connected to P8.                                                                                        |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| REF, JP2     | This link selects the external voltage source for the AD5676R. There are two options, as follows:                                                             |
|              | **2V5** - 2.5V supply from the onboard reference :adi:`ADM7160`.                                                                                              |
|              | **EXT** - External supply coming from EXT_REF connector.                                                                                                      |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| P1           | This link connects the corresponding DAC output channel to the SMB connector.                                                                                 |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

On-Board Connectors
~~~~~~~~~~~~~~~~~~~

+-----+-----------------+---------------------------------------------------------------+
| Ref | Connector Label | Function                                                      |
+=====+=================+===============================================================+
| A   | P8              | External analog power supply from 2.7 V to 5.5 V.             |
+-----+-----------------+---------------------------------------------------------------+
| B   | TP1 (GND)       | Analog ground Testpoint.                                      |
+-----+-----------------+---------------------------------------------------------------+
| C   | EXT_REF, J1     | External voltage reference input port.                        |
+-----+-----------------+---------------------------------------------------------------+
| D   | P2, P3, P5, P6  | Connector for SDP-K1 using standard Arduino form factor.      |
+-----+-----------------+---------------------------------------------------------------+
| E   | SPI_PMOD        | External SPI input using the PMOD standard pin configuration. |
+-----+-----------------+---------------------------------------------------------------+
| F   | I2C_PMOD        | External I2C input using the PMOD standard pin configuration. |
+-----+-----------------+---------------------------------------------------------------+
| G   | P11             | DAC outputs from V\ :sub:`OUT`\ 0 to V\ :sub:`OUT`\ 7.        |
+-----+-----------------+---------------------------------------------------------------+

| |image1|
| ===== Schematic, Layout, Bill of Materials & Board Photos =====

.. admonition:: Download
   :class: download

   
   -  `eval-ad5676rardz_schematic.pdf <resources/eval-ad5676rardz_schematic.pdf>`_
   -  `eval-ad5676rardz_layout.pdf <resources/eval-ad5676rardz_layout.pdf>`_
   -  `eval-ad5676rardz_bom.xlsx <images/eval-ad5676rardz_bom.xlsx>`_
   -  ` </resources/eval/user-guides/dac/eval-ad5676r-ardz/eval-ad5676rardz_board_photograph.png>`__
   -  ` </resources/eval/user-guides/dac/eval-ad5676r-ardz/eval-ad5676rardz_board_photograph_bottom.png>`__
   -  ` </resources/eval/user-guides/dac/eval-ad5676r-ardz/eval-ad5676rardz_kit_board_photograph.png>`__
   -  ` </resources/eval/user-guides/dac/eval-ad5676r-ardz/eval-ad5676rardz_kit_board_photograph_top.png>`__
   

*End of Document*

.. |Evaluation Board Photograph| image:: images/eval-ad5676rardz_board_photograph.png
   :width: 400
.. |Evaluation Board Photograph with SDP-K1| image:: images/eval-ad5676rardz_kit_board_photograph.png
   :width: 600
.. |image1| image:: images/eval-ad5676rardz_connectors.png
   :width: 600
