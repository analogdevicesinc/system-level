.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-freqcvt1-ebz/quickstart

.. _ad-freqcvt1-ebz quickstart:

AD-FREQCVT1-EBZ Quick Start Guide
=================================

The Quick Start Guide provides step by step instructions detailing how to plug
in, and set up the AD-FREQCVT1-EBZ board. The :xilinx:`ZC706 <ZC706>` and
:adi:`AD-FMCOMMS3-EBZ` platforms will be used to demonstrate the appropriate
board and cable connections.

Connecting to FMCOMMS3/4 and Cable Orienation
---------------------------------------------

The FREQCVT1-EBZ has four SMA connectors (TX_IN, RX_OUT, TX_OUT, RX_IN). 2 male
to male SMA connectors are required to connect the FREQCVT1-EBZ board to the
FMCOMMS3 platform.

To use the second channel of the FMCOMMS3, line up FREQCVT1 connectors RX_OUT
and TX_IN with FMCOMMS3 connectors TX2A and RX2A.

Power is brought to the FREQCVT1 board through a 3 pin cable. The connection is
made at P1 (pin1 = 3.3V, pin2 = GND, pin3 = 12V), which sits directly between
TX_IN and RX_OUT. The power originates from the FMCOMMS3 board, connector P301.
It is very important to properly plug in this cable on both ends, according to
the image below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-freqcvt1-ebz/dsc00053.jpg
   :width: 800px

To use the first channel of the FMCOMMS3, line up FREQCVT1 connectors RX_OUT and
TX_IN with FMCOMMS3 connectors RX1A and TX1A. This requires flipping the board
upside down.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-freqcvt1-ebz/12_pin_cable_orientation.jpg
   :width: 800px

The ZC706 board provides digital controls to the FREQCVT 1 board through a
12-pin ribbon cable. Be careful to properly plug in both ends of the cable
according to the above image.

Cable Connection and Orientation
--------------------------------

The FMCOMMS3 board provides power to the FREQCVT1 board. Connector P301 on the
FMCOMMS3 board provides 3.3V, GND and 12V to P1, a 3 pin connector on the
FREQCVT1 board. The connector on the FREQCVT1 board is keyed. Connector P301 on
the FMCOMMS3 board is not populated, and requires a 3 pin male header. The cable
must be carefully plugged into P301 to ensure the correct voltage.

A 12 pin connector on the Xilinx ZC706 provides digital controls to connector P2
on the FREQCVT1 board. These implement a SPI protocol, and some general purpose
IO"s. Reference the image below for correct cable connections.
