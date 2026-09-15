.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-trxboost1-ebz/quickstart

.. _ad-trxboost1-ebz quickstart:

AD-TRXBOOST1-EBZ Quick Start Guide
==================================

The Quick Start Guide provides step by step instructions detailing how to plug
in, and set up the AD-TRXBOOST1-EBZ board. The :xilinx:`ZC706 <ZC706>` and
:adi:`AD-FMCOMMS3-EBZ` platforms will be used to demonstrate the appropriate
board and cable connections.

Connecting to FMCOMMS2/3/4
--------------------------

The TRXBOOST1-EBZ has four SMA connectors (TX_IN, RX_OUT, TX_OUT, RX_IN). 2 male
to male SMA connectors are required to connect the TRXBOOST1-EBZ board to the
FMCOMMS3 platform.

Start by lining up TRXBOOST1 connectors RX_OUT and TX_IN with FMCOMMS3
connectors TX1A and RX1A. This alignment requires you to flip the TRXBOOST1
board upside down (Secondary side facing up!).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-trxboost1-ebz/trxboost1_-_ch1.jpg
   :width: 600px

To use the second channel of the FMCOMMS3, line up TRXBOOST1 connectors RX_OUT
and TX_IN with FMCOMMS3 connectors TX2A and RX2A. This alignment requires you to
flip the TRXBOOST1 board right side up (Primary side facing up!).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-trxboost1-ebz/trxboost1_-_ch2.jpg
   :width: 600px

Power Cable Connection and Orientation
--------------------------------------

Power supply is brought to the TRXBOOST1 through a 3 pin cable. The connection
is made at P2 (pin1 = 3.3V, pin2 = GND, pin3 = 12V), which sits directly between
TX_IN and RX_OUT.

The power can originates from the FMCOMMS3 board, connector P301. It is very
important to properly plug in this cable on both ends, according to the image
below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-trxboost1-ebz/trxboost1_-_close_crop_-_copy.jpg
   :width: 800px

It can also come from an external power supply as long as it"s connected as
shown.

RF Input / Output Power Limitations
-----------------------------------

Due to the high gain that the TX and RX paths exert, it is important to know
what is the Max RF input power that should be applied to the TX and RX to allow
the max gain before hitting the 1dB compression point.

For the TX path: Because the TX gain is around 17dB at 2.45GHz, and the output
1dB compression point of the ADL5610 is around 18dBm at 2.45GHz, that means that
the TX input should not exceed 1dB.

For the RX path: Because the RX gain is around 13dB at 2.45GHz, and the output
1dB compression point of the ADL5521 is around 21dB at 2.45GHz, that means that
the RX input should not exceed 8dB.
