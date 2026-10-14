.. _pluto users non_quad:

Dealing with non-Quadrature Signals
====================================

`Quadrature <https://en.wikipedia.org/wiki/Quadrature_amplitude_modulation>`_
signals can be broken down into two orthogonal components, I (in-phase) and Q
(quadrature). Real or non-quadrature signals are technically a subset of
quadrature when the components are in-phase or one of the components is zero.

Creating and Transmitting a "real" signal
------------------------------------------

There are two main ways to create and transmit a "real" signal:

1. Sending in-phase (or identical) I & Q signals
2. Sending just I or Q

Sending the same signal on I and Q
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using IIO-Scope, we can generate two tones, one on each DAC, both at the same
frequency and magnitude.

.. figure:: images/non_quad/dds-real.png

.. figure:: images/non_quad/loopback.png

According to `Euler's formula <https://en.wikipedia.org/wiki/Euler%27s_formula>`_,
this should generate an equal-sized tone on each side of the LO. Using digital
loopback, we can see that the math holds true.

.. figure:: images/non_quad/dds_lookback_time.png

.. figure:: images/non_quad/dds_loopback.png

Sending only I or only Q
~~~~~~~~~~~~~~~~~~~~~~~~~

We can achieve the same thing, by only sending I or Q. In this case, we set the
Q magnitude to -99 (or infinite attenuation).

.. figure:: images/non_quad/i_only.png

We can see the same thing in the digital loopback.

.. figure:: images/non_quad/dds_loopback_time_i.png

.. figure:: images/non_quad/dds_looback_i.png

The one thing to notice is that the power in the signal is less (the peaks in
the FFT drop), since we are sending half the power.

Receiving a "real" signal
--------------------------

Most (all) integrated transceivers include some sort of Quadrature tracking
corrections which try to ensure the signals are correct. There is no way for a
Quadrature tracking correction algorithm to understand if a "real" signal is
being sent (rather than an unwanted image). When the Rx and Tx LO are at the
same frequency, this causes the amplitude is jumping up and down by a few dB.

.. figure:: images/non_quad/rf_lo_same.png

.. figure:: images/non_quad/lo_same_time.png

The amplitude difference between I & Q is random based on the random difference
between the phase of the Rx and Tx PLL. Every time you change the
LO-frequencies, it changes.

If you calculate magnitude with: ``sign(I) * sqrt(I² + Q²)`` you can ignore the
difference between I and Q, and remove any I/Q imbalance.

.. figure:: images/non_quad/rx_rot.png

========  ========== ========== ===========
Rotation  0          50 degrees 70 degrees
========  ========== ========== ===========
I/Q Plot  |rot0|     |rot52|    |rot77|
Mag only  |mag|
========  ========== ========== ===========

.. |rot0| image:: images/non_quad/lo_same_time_0_offset.png
.. |rot52| image:: images/non_quad/lo_same_time_52_offset.png
.. |rot77| image:: images/non_quad/lo_same_time_77offset.png
.. |mag| image:: images/non_quad/lo_same_time_mag_only.png

However, the magnitude still has a step in it. This is because the RX Quadrature
tracking state machine may or may not interact with the AGC state machine. It
can be hard to tell what is causing the changes.

.. figure:: images/non_quad/acg_q_on.png

If we turn the AGC off (and use manual mode), we can see that it's just the
Quadrature tracking that is causing the issue.

.. figure:: images/non_quad/off_iq_on.png

Removing issues
---------------

The easiest way to remove this error is to simply turn off Quadrature tracking
corrections. There are two main ways to do this:

1. Turning Quadrature tracking off
2. Offset Tuning

Turning Quadrature tracking off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In IIO-Scope, this is done with a single attribute, called
``quadrature_tracking_en``.

.. figure:: images/non_quad/tracking_off.png

This removes the magnitude step.

.. figure:: images/non_quad/fixed.png

On `USRP <https://www.ettus.com/>`_ and
`UHD <http://files.ettus.com/manual/>`_, there is a
`method <http://files.ettus.com/manual/classuhd_1_1usrp_1_1multi__usrp.html#a2fb85eca93c18f1920cf3ee8de2b6da9>`_
called ``set_rx_iq_balance()`` which does the same thing as the
:adi:`AD9361` PHY ``quadrature_tracking_en`` attribute.

Offset Tuning
~~~~~~~~~~~~~

Instead of turning off Quadrature tracking (which is normally required), we can
make sure that the Rx and Tx PLLs have a frequency offset greater than 10 Hz.
For most standards, there is always a frequency offset in place, so this won't
be an issue. For simple loopback - it can be a PITA.

To check the offset, you can use:

.. code:: console

   analog@analog:~$ iio_attr -a -c ad9361-phy RX_LO frequency
   dev 'ad9361-phy', channel 'altvoltage0' (output), id 'RX_LO', attr 'frequency', value '2400000000'
   analog@analog:~$ iio_attr -a -c ad9361-phy TX_LO frequency
   dev 'ad9361-phy', channel 'altvoltage1' (output), id 'TX_LO', attr 'frequency', value '2400000000'

To manually make an offset:

.. code:: console

   analog@analog:~$ iio_attr -D ad9361-phy loopback 1
   iio_attr -D ad9361-phy loopback : SUCCESS (1)
   analog@analog:~$ iio_attr -c ad9361-phy voltage0 gain_control_mode manual
   dev 'ad9361-phy', channel 'voltage0' (input), attr 'gain_control_mode', value 'manual'
   analog@analog:~$ iio_attr -c ad9361-phy voltage0 quadrature_tracking_en 1
   dev 'ad9361-phy', channel 'voltage0' (input), attr 'quadrature_tracking_en', value '1'

.. figure:: images/non_quad/0khz_offset.png

With a 1kHz offset:

.. figure:: images/non_quad/mag_1khz_offset.png

We can see that at 10 Hz offset, the Quadrature tracking correction works
properly.

========== ==================== ====================
Offset     Quadrature           Quadrature
           Tracking Off         Tracking On
========== ==================== ====================
0 Hz       |0hz_off|            |0hz_on|
5 Hz       |5hz_off|            |5hz_on|
10 Hz      |10hz_off|           |10hz_on|
20 Hz      |20hz_off|           |20hz_on|
========== ==================== ====================

.. |0hz_off| image:: images/non_quad/0hz_offset_iq_off.png
.. |0hz_on| image:: images/non_quad/0hz_offset_iq_on.png
.. |5hz_off| image:: images/non_quad/5hz_offset_iq_off.png
.. |5hz_on| image:: images/non_quad/5hz_offset_iq_on.png
.. |10hz_off| image:: images/non_quad/10hz_offset_iq_off.png
.. |10hz_on| image:: images/non_quad/10hz_offset_iq_on.png
.. |20hz_off| image:: images/non_quad/20hz_offset_iq_off.png
.. |20hz_on| image:: images/non_quad/20hz_offset_iq_on.png

At 2.4 GHz, a sub 10 Hz offset would be better than 4 parts per billion (or
0.004 ppm) offset. This is pretty good.

Conclusion
----------

This is not an :adi:`ADALM-PLUTO` issue. It will be an issue with all
integrated devices which have some sort of Quadrature tracking feature (not just
from ADI - but from all manufactures). The easiest thing to do is check your
settings (to make sure it's off, or on - if you know you need it).

SDRangel
~~~~~~~~

With `SDRangel <https://github.com/f4exb/sdrangel>`_, there are easy to use
buttons:

.. figure:: images/non_quad/sdrangel_controls.png

* **RFDC** - RF DC correction
* **BBDC** - Baseband DC correction
* **IQ** - RX Quadrature correction