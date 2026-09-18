AD-PZSDR2400TDD-EB Introduction
===============================

The :adi:`AD-PZSDR2400TDD-EB` is affectionately dubbed the first
'RF personality card'. It plugs into the Avnet
:adi:`AES-PZSDRCC-FMC-G <adrv9361-z7035>` carrier card. 35mm U.FL coaxial
cables connect the card to the Avnet
`PicoZed SDR Z7035/AD9361 SOM <http://zedboard.org/product/picozed-sdr-som>`_
providing access to the transmit and receive inputs of the :adi:`AD9361`.
Information on the card, how to use it, the design package that surrounds it,
and the software which can make it work, can be found here.

The purpose of the :adi:`AD-PZSDR2400TDD-EB` is to provide the user with a
2.4GHz TDD path to condition the transmit or receive signals of the
:adi:`AD9361`. Selection of TX or RX path is achieved by the 200MHz to 2.7GHz
SPDT switch :adi:`HMC546LP2` controlled by the FPGA and accompanying software.
The transmit path consists of a 2.4GHz filter, half watt driver amplifier
:adi:`ADL5324` and 2 watt power amplifier :adi:`HMC921`. The receive path
consists of the same 2.4GHz filter as well as a low loss LNA :adi:`HMC669`.

The :adi:`AD-PZSDR2400TDD-EB` board has two identical TX/RX channels that
connect to the two channels of the AD9361. The power and control for this board
comes from the 40 pin connector that mates with the AES-PZSDRCC-FMC-G carrier.
The board has three settings: TX mode, RX mode or TDD mode. Both TX/RX channels
(1 & 2) have to be set in similar fashion. (Meaning you cannot transmit on
channel 1 and receive on Channel 2. They are either both in TX mode or both in
RX mode at each point in time.)
