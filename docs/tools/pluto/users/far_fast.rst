.. _pluto users far_fast:

How far/fast?
=============

The first two questions asked by many novice users of wireless communications
are always:

1. *How fast does it go?*
2. *How far does it cover?*

The answers are not practical to answer for a device like the ADALM-PLUTO, or
any other SDR since you can gain distance by giving up datarate, gain data rate
by increasing bandwidth, gain data rate by changing modulation scheme. The
performance (how far/fast) of the system will depend heavily on everything from
the choice of carrier frequency, modulation type, bandwidth, antennas, local
environment (topography, vegetation, weather), just to name a few.

Data Links vs Radios
---------------------

One of the first things to understand from a novice standpoint is the difference
between a data link and a radio.

At the top level, a `data link <https://en.wikipedia.org/wiki/Data_link>`_
connects one location to another for the purpose of transmitting and receiving
digital information. In most instances, we have a transmitter and a receiver and
the channel. These are governed by a link protocol enabling digital data to be
transferred from a data source (transmitter) to a data sink (receiver). The data
link specifies everything that both the transmitter and a receiver need to know
to communicate effectively. This includes such things as:

* `Simplex <https://en.wikipedia.org/wiki/Simplex_communication>`_,
  `Half-duplex <https://en.wikipedia.org/wiki/Duplex_(telecommunications)#HALF-DUPLEX>`_
  or `Duplex <https://en.wikipedia.org/wiki/Duplex_(telecommunications)>`_
  communication links
* occupied bandwidth
* center frequency
* modulation types supported
* negotiation of modulation types (if supported)
* MAC protocol (multi-master, master-slave, CSMA, etc)

When asking questions about how far, how fast, bit error rate - these are
characteristics of a data link, not a radio.

Since the ADALM-PLUTO is a radio, not a datalink, it is difficult to answer
those questions.

For analyzing data links, there is a great article at
`AFAR Communications <http://www.afar.net/tutorials/how-far/>`_ which reviews
these sorts of things.