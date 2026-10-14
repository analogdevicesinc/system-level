.. _pluto users receiver_sensitivity:

ADALM-PLUTO Receiver Sensitivity
=================================

Receiver sensitivity is a measure of the ability of a receiver to demodulate and
get information from a signal. Most people quantify *sensitivity* as the lowest
signal power level from which we can get useful information.

Since the above definition uses "demodulate", you should immediately understand,
this is a meaningless specification for a pure radio. There is no demodulation
in the base design, and we pass samples around. The actual receiver sensitivity
will depend on channel bandwidth, temperature, modulation scheme, how robust the
demodulator is, something that we just don't control (that's all up to you).

What is specified, and measured, is noise:

* Tx noise: ≤−157 dBm/Hz noise floor
* Rx noise figure : 2.5 dB @ Maximum Rx gain
* Integrated Phase Noise : 0.3 ° rms, 100 Hz to 100 MHz

These noise numbers can be used to calculate the min received power to decode
something.

Rx Noise Figure
---------------

The IEEE Standard definition of noise figure, states that:

  "The noise factor, at a specified input frequency, is defined as the ratio of:
  (1) the total noise power per unit bandwidth available at the output port when
  noise temperature of the input termination is standard (290 K) to (2) that
  portion of (1) engendered at the input frequency by the input termination."

.. math::

   NF = \frac{N_{a} + kT_{0}BG}{kT_{0}BG}

* NF = Noise Figure
* N\ :sub:`a` = noise added by the device under test
* k = Boltzmann's Constant (1.38 x 10\ :sup:`-23` joules/K)
* T\ :sub:`0` = temperature in Kelvin (in this case 290 K)
* B = bandwidth of the device
* G = gain of the device

This is measured using test equipment, as specified in
`Agilent Fundamentals of RF and Microwave Noise Figure Measurements <http://literature.cdn.keysight.com/litweb/pdf/5952-8255E.pdf>`_.