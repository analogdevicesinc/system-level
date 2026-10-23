.. _pluto users antennas:

Antennas
========

The antennas connectors on the ADALM-PLUTO are standard polarity
`SubMiniature version A <https://en.wikipedia.org/wiki/SMA_connector>`__ (SMA) connectors.
There are many ways to
`characterize <https://en.wikipedia.org/wiki/Antenna_measurement>`__ an antenna,
from gain (or loss), radiation pattern, beamwidth, polarization, and impedance.

The actual antennas included with the ADALM-PLUTO are
`Jinchang Electron <https://www.jinchanggps.com/JCG401-GSM-Antenna-pd45551675.html>`__ JCG401.
While the JCG401 is specified for 824-894 and 1710-2170MHz, they do
operate over a much wider range, but it should be understood that all antennas
are filters. They will have some frequency selectivity (however, they are not
brick wall filters). Just because something is specified for 824 MHz, does not
mean that it will not pick up something at 600MHz, or even 87MHz, or it might
not.

The :download:`JCG401 datasheet <downloads/jcg401.pdf>`
does spec radiation pattern, beamwidth, polarization, and
impedance, but leaves out performance (gain or loss) over frequency - since it
is spec'ed for 824-894 and 1710-2170MHz. We can quickly do that ourselves with
the help of a `E5071C ENA Series Network Analyzer <http://www.keysight.com/find/E5071C>`__.
We connect the two antennas to the two ports, calibrate with a wire, and then run a S\ :sub:`21` test.

`S-parameters <https://en.wikipedia.org/wiki/Scattering_parameters>`__ describe
the input-output relationship between ports (or terminals) in an electrical
system. For instance, if we have 2 ports (intelligently called Port 1 and Port
2), then S\ :sub:`12` represents the power transferred from Port 2 to Port 1.
S\ :sub:`21` represents the power transferred from Port 1 to Port 2. In general,
S\ :sub:`NM` represents the power transferred from Port M to Port N in a
multi-port network. For an excellent side view into antennas check out Peter
Joseph Bevelacqua's excellent reference: http://antenna-theory.com

Running an S\ :sub:`21` test on the E5071C will broadcast a tone from one
antenna (on port 2), and receive it on the other (port 1), and plot the results
(in dB) compared to a wire that was used during the calibration on the
instrument. It's interesting note that we are measuring both Rx and Tx
capabilities. It is possible that the Rx at sub 600MHz could be fine, and it is
just a Tx problem (unlikely, but I just wanted to point it out).

.. figure:: images/antennas/jcg401_full_range.png
   :width: 500

You can see thing over 625 MHz, the antenna has pretty good performance, with
the exception of a tight notch at 1.12 GHz. This means unless you are really
close to an FM broadcast station, you will not be able to receive FM with this
antenna. (it has been done, and it does work - it just limits the distance
between you and the antenna. Remember that most terrestrial FM broadcast
stations are 10,000 to 20,000 watts).

At the popular `ISM bands <https://en.wikipedia.org/wiki/ISM_band>`__ of 900
MHz, 2400 MHz, and 5725 MHz, performance is quite good. (click on the image to
make it larger).

.. grid::
   :widths: 50 50

   .. figure:: images/antennas/jcg401_900ism.png
      :width: 400

      902 - 928 MHz ISM Band

   .. figure:: images/antennas/jcg401_2400ism.png
      :width: 400

      2.4 -2.5 GHz ISM Band

   .. figure:: images/antennas/jcg401_5725ism.png
      :width: 400

      5.725 - 5.875 GHz ISM Band
