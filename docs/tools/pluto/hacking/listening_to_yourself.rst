.. _pluto hacking listening_to_yourself:

Self Reception
==============

Everyone has sung to a song on the radio, and it sounds great, as long as the
radio is loud enough to drown out your terrible voice (or is that just me?).
This is a phenomenon known as self reception - when the signal you want to
receive is being overloaded by something else.

The ADALM-PLUTO can do this too if you are not careful. The device will have Tx
LO Leakage, and the receiver will pick that up and may swamp out the signal you
desire to actually receive.

Tx On, and sending a signal
---------------------------

It's easy to see this with offset tuning. Here is the ADALM-PLUTO with the Rx
set to 2400 MHZ, and the Tx set to 2402 MHz, with the internal DDS, set to 3
MHz, and -30dB down (which would put things at 2405 MHz), with the default
antennas connected, and the LTE20 Filters loaded.

.. figure:: tx_lo_dds.png
   :width: 600

This shows the peak at the signal (at 2405 MHz, where we expect it), and a LO
leakage at 2402 MHz. It's difficult to see what this really means in terms of
signal power, so we can look at the actual gain is set to by the Automatic Gain
Control (AGC), and the Receive Signal Strength Indicator (RSSI).

.. figure:: tx_lo_dds_rx1.png
   :width: 200

We can see the RSSI is 66.25 dB, and the Hardware Gain is set to 43 dB.

Tx On, and not sending a signal
-------------------------------

If we simply disable the DSS, this is what we see:

.. grid::
   :widths: 50 50

   .. figure:: tx_lo_leakage.png
      :width: 600

   .. figure:: tx_lo_leakage_rx1.png
      :width: 200

Now our RSSI has gone to 90.5 dB and the hardware gain is set to 68 dB (which is
still not at the max gain of the device), we are listening to our own LO
leakage, not the actual RF signal.

Tx Off
------

If we power down the Tx LO with (``0`` is on, ``1`` is powerdown):

.. code:: console

   analog@analog:~$ iio_attr -c ad9361-phy TX_LO powerdown 1
   dev 'ad9361-phy', channel 'altvoltage1' (output), id 'TX_LO', attr 'powerdown', value '0'
   wrote 2 bytes to powerdown
   dev 'ad9361-phy', channel 'altvoltage1' (output), id 'TX_LO', attr 'powerdown', value '1'

This is the equivalent C source of:

.. code:: c

   / Create IIO Context /
   ctx = iio_create_context_from_uri("usb:1.3.5");

   / Find IIO device in current context /
   dev = iio_context_find_device(ctx, "ad9361-phy");

   / Find the IIO output channel in the current device /
   ch = iio_device_find_channel(dev, "TX_LO", true);

   / Write a one into the IIO channel attribute /
   ret = iio_channel_attr_write_longlong(dev, "powerdown", 1);

Then we get:

.. grid::
   :widths: 50 50

   .. figure:: tx_lo_off.png
      :width: 500

   .. figure:: tx_lo_off_rx1.png
      :width: 200

Tx On, but offset more than your channel
----------------------------------------

If we shift things around a bit - if we configure things for an LTE10 signal,
(LTE10 filter, with an LTE10 signal going out the DAC at full scale), and set
the Tx and Rx to the same (2400 MHz), we can see this:

.. grid::
   :widths: 50 50

   .. figure:: tx_lo_lte10.png
      :width: 500

   .. figure:: tx_lo_lte10_rx1.png
      :width: 200

By offsetting things in 10 MHz steps, how far do things need to be away, so that
it stops affecting the receiver:

.. list-table::
   :header-rows: 1

   - - offset
     - 0 MHz
     - 10 MHz
     - 20 MHz
     - 30 MHz
     - 40 MHz
     - 50 MHz
     - 60 MHz
   - - RSSI
     - 48.50 dB
     - 86.75 dB
     - 105.00 dB
     - 112.75 dB
     - 116.75 dB
     - 117.00 dB
     - 117.5 dB
   - - ACG Gain
     - 25 dB
     - 32 dB
     - 59 dB
     - 62 dB
     - 67 dB
     - 69 dB
     - 71 dB

This doesn't mean that you can't transmit/receive on adjacent channels, it just
means that the receiver noise floor will not be higher and therefore the
receiver will not appear as sensitive when you are doing this.

Conclusion
----------

If you aren't using the transmitter - turn it off, your receiver noise floor
will decrease, increasing your receive sensitivity, allowing you to pick up
smaller signals from the air.

.. list-table::
   :header-rows: 1

   - - Test Case
     - RSSI
     - AGC Setting
   - - Tx On, with Signal
     - 66.25 dB
     - 43 dB
   - - Tx On, without signal
     - 90.50 dB
     - 68 dB
   - - Tx Off
     - 113.75 dB
     - 71 dB

