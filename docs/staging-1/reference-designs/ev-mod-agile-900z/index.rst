.. imported from: https://wiki.analog.com/resources/eval/user-guides/ev-mod-agile-900z

.. _ev-mod-agile-900z:

EV-MOD-AGILE-900Z
=================

Features
--------

- Small form factor SMT module (2.5cm x 3.6cm)
- Internal MMCX for external 50Ω antenna
- 52 castellated SMT PCB connectors for rapid prototyping

  - UART, SPI and I2C comms interfaces
  - GPIO and analog input (AIN) pins
  - RF output pin
  - MCU and Radio reset pins
  - Supply pins

- Small number of external components needed

  - Internal by-pass capacitors, pull-up resistors, pull-down resistors,
    pull-down resistors, matching network circuit, harmonic filter circuit, TCXO
    and crystal reference clocks

Description
-----------

The EV-MOD-AGILE-900Z module is the hardware solution that runs the AgileNet IP,
a wireless mesh networking solution from Analog Devices.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig1.png
   :width: 400px

   Figure.1 EV-MOD-AGILE-900Z Module

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig2.png
   :width: 600px

   Figure 2. Functional Block Diagram

AGILENET IP OVERVIEW
--------------------

The AgileNet IP (Internet Protocol) is a sub-GHz wireless mesh networking
protocol solution. It is implemented by an embedded firmware designed to run on
the EV MOD AGILE 900z module. The module utilizes the ultralow power ARM
Cortex-M4F microcontroller (MCU) ADuCM4050 together with the high-performance
low power sub-GHz radio transceiver IC ADF7030-1 which allows for long range and
low power operation.

The Agilenet IP protocol stack has an industrial-grade reliability due to the
following features:

- 6LoWPAN and 6TiSCH standard based
- Avoids node communication dropouts
- Bidirectional communication with link-layer acknowledgements
- multi-hop
- self-healing

The network is designed to run on ISM global license-free bands i.e. US: 900MHz,
EU: 868MHz. The network can handle up to a thousand nodes. The data throughput
is typically 1 to 4 packets per second for 90bytes application payload per
packet. These features make the AgileNet IP suitable for networks with high node
count, long distance between nodes, low data rate, and medium latency
requirements.

Other notable features of AgileNet IP are:

- OTA (over-the-air) reprogramming/update
- Built-in network health statistics
- Simple API for writing custom application inside MCU
- AgileNet IP driven over Serial API

This module is connected to the EV-COG-AGILE-900Z base board through the
castellation pins. There are 51 castellation pins which are soldered down to the
EV-COG-AGILE-900Z board. These castellations bring out UART, I2C, SPI and GPIO
lines from the module to the COG board. The power supply from the COG is routed
to the module as well. The MMCX connector on the module is used to connect the
antenna.

EV-MOD-AGILE-900Z
~~~~~~~~~~~~~~~~~

In the EV-MOD-AGILE-900Z module, the ADuCM4050 is interfaced to the ADF7030-1
via SPI. The peripheral hardware configurations of both chipset fixed in the
module is shown in Figure 6 and Figure 7. The module is essentially the breakout
board of the EV-MTE-AGILE-900Z.

The module is a certified surface mount PCB. There are 51 castellation pins at
the edges of the module for soldering it to custom application PCB. It is
through these castellation pin that the module is soldered to EV-COG-AGILE-900Z.
The castellations pins bring out selected UART, I2C, SPI and GPIO lines from
both ADuCM4050 and ADF7030-1. There are also castellation pins provided for boot
mode selection, single wire debug, and RF output. The castellation pins are
detailed in Pin Configuration and Function Descriptions.

GENERAL OPERATION AND PERFORMANCE DATA
--------------------------------------

PIN CONFIGURATION AND FUNCTION DESCRIPTIONS
-------------------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig3.png
   :width: 400px

   Figure 3. EV-MOD-AGILE-900Z Pinout

Table 6

PERIPHERAL INTERFACING
----------------------

SUPPLY
~~~~~~

Power the EV-MOD-AGILE-900Z module by connecting PIN14 and/or PIN15 (VDD_SUPPLY)
to a 3V source. PIN14 and PIN15 by default supplies both ADuCM4050 and ADF7030-1
as can be seen in Figure 9. The 3V supply can be sourced from the output of a
voltage regulator (i.e. ADP5300 as shown in Figure 4).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig4.png
   :width: 400px

   Figure 4. Supply Circuit using ADP5300

NOTE: that the EV-MOD-AGILE-900Z consumes >80mA of current, not exceeding 150mA.
PIN3 - VDD_ADF7030-1 by default is not an input supply pin and will show a
voltage equal to VDD_SUPPLY. To use the VDD_ADF7030-1 to separately supply radio
from the MCU, desolder R23 (see Figure 9) from the board. WARNING: NEVER connect
a supply to VDD_SUPPLY and VDD_ADF7030-1 at the same time without removing R23
or E2.

SENSOR INTEGRATION
~~~~~~~~~~~~~~~~~~

The EV-MOD-AGILE-900z can be operated in two distinct modes, namely, On-Chip SDK
(OCSDK) mode and Slave mode (see the Applications Information section). In OCSDK
mode, the GPIO, UART, SPI, ADC, I2C and AIN pins could be used for sensor
integration. In Slave mode, sensor integration is done using an external
controller.

COMMUNICATIONS PERIPHERALS
~~~~~~~~~~~~~~~~~~~~~~~~~~

The EV-MOD-AGILE-900z provides two SPIs, two UART ports, and an I2C bus from the
ADuCM4050 MCU for communications. Refer to the ADuCM4050 datasheet and hardware
reference manual for more details on these peripherals. Note that I2C0_SCL and
I2C02_SDA has internal pull up resistors.

GPIO
~~~~

GPIO ports are available from the on-board ADuCM4050 MCU and ADF7030-1 radio for
general purpose input/output. The MCU GPIO pins are also multiplexed for
different functionality. Refer to the ADuCM4050 Hardware Reference Manual for
more details. Note that ADF7030-1_GPIO2 has an internal pull down resistor as
seen in Figure 7.

PROGRAMMING OPTIONS
~~~~~~~~~~~~~~~~~~~

Flash programming the ADuCM4050 MCU in the module is typically done through
SWD0_DATA, SWD0_CLK, and SYS_HWRST_N pins. By using a header as seen in Figure
5, connecting a ribbon cable to the header will allow programming using the
EV-COG-AGILE-900Z. Refer to the AgileNet-6T User Guide for details on how to
program with this method.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig5.png
   :width: 400px

   Figure 5. Programming Interface

This setup also allows the use of other flash programmers such as JLink and
ICE2000, as well as serial flash programming through the UART pins.

MODULE REFERENCE CIRCUIT
------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig6.png
   :width: 600px

   Figure 6. ADuCM4050 Circuit

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig6.png

   Figure 7. ADF7030-1 Circuit

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig8.png

   Figure 8. Castellation Pin Mapping

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig9.png
   :width: 600px

   Figure 9. Power Supply Circuit

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig10.png
   :width: 400px

   Figure 10. RF Shield

APPLICATIONS INFORMATION
------------------------

MODES OF OPERATION
~~~~~~~~~~~~~~~~~~

The EV-MOD-AGILE-900z can be operated in two distinct modes, namely, On-Chip SDK
mode and Slave mode. Mode selection should be considered during the design phase
of the development process.

On-Chip SDK (OCSDK) Mode
^^^^^^^^^^^^^^^^^^^^^^^^

The EV-MOD-AGILE-900z On-Chip Software Development Kit (On-Chip SDK) enables
development of C-code applications for execution on the AgileNet mote. AgileNet
motes have an on-board ADuCM4050 paired with the ADF7030-1. With the On-Chip
SDK, users may quickly and easily develop application code without the need for
an external microprocessor.

Applications written within the On-Chip SDK may send and receive wireless
messages through the mesh network; process data, such as statistical analysis;
execute local decision-making and control; and manage the following peripherals:

- General Purpose Input-Output (GPIO) pins
- Analog-to-Digital Converter (ADC)
- Universal Asynchronous Receiver/ Transmitter (UART)
- Serial Peripheral Interface (SPI) Master
- Inter-Integrated Circuit (I2C) Master

Network connectivity and quality of service is handled by the AgileNet IP
protocol stack. Unlike typical "chip and stack" solutions, the AgileNet protocol
stack comes as a pre-compiled library.

Slave Mode
^^^^^^^^^^

In Slave mode, the EV-MOD-AGILE-900z is connected to an external microprocessor
through the serial UART interface and is solely used as a networking device.
Note that the built in I/Os are disabled in this mode.

TYPICAL APPLICATION CIRCUIT
~~~~~~~~~~~~~~~~~~~~~~~~~~~

On-Chip SDK (OCSDK) Mode OCSDK Mode – NO external MCU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig11.png

   Figure 11. OCSDK Mode Typical Application Circuit

With External MCU (Slave Mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig12.png

   Figure 12. Slave Mode Typical Application Circuit.

OUTLINE DIMENSIONS AND PCB FOOTPRINT
------------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-mod-agile-900z/fig13.png
   :width: 600px

Figure 13. Outline Dimension of the Module. Note: measurement unit is in
millimeters

Additional resources
~~~~~~~~~~~~~~~~~~~~

:dokuwiki:`AgileNet-6T wiki page </resources/eval/user-guides/agilenet6t>`
