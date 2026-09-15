.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/card_specification

.. _ad-fmcomms1-ebz hardware card_specification:

AD-FMCOMMS1-EBZ Specifications
==============================

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-retired
   :end-before: .. end-retired

Transmit Specs
--------------

There are many specifications on the Transmit side of a RF system

- :adi:`Evaluating High Speed DAC Performance <static/imported-files/tutorials/MT-013.pdf>`

Theoretical specs
~~~~~~~~~~~~~~~~~

Bandwidth
^^^^^^^^^

Determining overall channel bandwidth is a little complex, since many devices
don"t have a meaningful (in this aspect) bandwidth number.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/ad9122_fig10.png
   :width: 250px

   AD9122 frequency response

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/adl5375-05_fig63.png
   :width: 250px

   ADL5375 frequency response

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/adl5602.png
   :width: 250px

   ADL5602 frequency response

- In the AD9122, the above figure shows an fDATA of 400MHz, creating a waveform
  over 350MHz.
- The ADL5375 does include a baseband bandwidth specification - depending on the
  flatness you require, could be 200MHz (+/- 0.1dB) or 500MHz (+/- 0.5dB).
- the ADL5602 has different gain, depending on the RF frequency (but over
  250MHz, you will still notice).

So, transmit bandwidth can be as high as 250 MHz, depending on if the flatness
of the ADL5602 and ADL5375 works for your application.

LO BW (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/tx_bw_0.4to4ghz_scale_0.5.png
   :width: 200px

   LO BW with full output power

Adjacent Channel Power (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`ACP <https://en.wikipedia.org/wiki/Adjacent_channel_power_ratio>`__

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/acp_1.24ghz_rx_lo_off_scale0.5.png
   :width: 200px

   ACP with LO of 1.2GHZ and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/acp_1.24ghz_rx_lo_off_scale0.25.png
   :width: 200px

   ACP with LO of 1.2GHZ and Tone of 40MHz with half power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/acp_2.44ghz_rx_lo_off_scale0.5.png
   :width: 200px

   ACP with LO of 2.4GHZ and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/acp_2.44ghz_rx_lo_off_scale0.25.png
   :width: 200px

   ACP with LO of 2.4GHZ and Tone of 40MHz with half power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/acp_3.64ghz_rx_lo_off_scale0.5.png
   :width: 200px

   ACP with LO of 3.6GHZ and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/acp_3.64ghz_rx_lo_off_scale0.25.png
   :width: 200px

   ACP with LO of 3.6GHZ and Tone of 40MHz with half power out.

Phase Noise (RevB unmodified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Phase noise <https://en.wikipedia.org/wiki/Phase noise>`__

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_at_440mhz_rx_lo_off.png
   :width: 200px

   Phase Noise at LO of 400MHz and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_at_940mhz_rx_lo_off.png
   :width: 200px

   Phase Noise at LO of 900MHz and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_at_1.84ghz_rx_lo_off.png
   :width: 200px

   Phase Noise at LO of 1.8GHz and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_at_2.44ghz_rx_lo_off.png
   :width: 200px

   Phase Noise at LO of 2.4GHz and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_at_3.54ghz_rx_lo_off.png
   :width: 200px

   Phase Noise at LO of 3.5GHz and Tone of 40MHz with full power out.

Phase Noise (RevB Modified Board & RevC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_1.24ghz_rx_lo_off_scale0.5_new.png
   :width: 200px

   Phase Noise at LO of 1.2GHz and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_1.24ghz_rx_lo_off_scale0.25_new.png
   :width: 200px

   Phase Noise at LO of 1.2GHz and Tone of 40MHz with half power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_2.44ghz_rx_lo_off_scale0.5_new.png
   :width: 200px

   Phase Noise at LO of 2.4GHz and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_2.44ghz_rx_lo_off_scale0.25_new.png
   :width: 200px

   Phase Noise at LO of 2.4GHz and Tone of 40MHz with half power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_3.64ghz_rx_lo_off_scale0.5_new.png
   :width: 200px

   Phase Noise at LO of 3.6GHz and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/phase_noise_3.64ghz_rx_lo_off_scale0.25_new.png
   :width: 200px

   Phase Noise at LO of 3.6GHz and Tone of 40MHz with half power out.

Output power (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Transmitter power output <https://en.wikipedia.org/wiki/Transmitter power output>`__

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/cp_1.24ghz_rx_lo_off_scale0.5.png
   :width: 200px

   CP with LO of 1.2GHZ and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/cp_2.44ghz_rx_lo_off_scale0.5.png
   :width: 200px

   CP with LO of 2.4GHZ and Tone of 40MHz with full power out.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/cp_3.64ghz_rx_lo_off_scale0.5.png
   :width: 200px

   CP with LO of 3.6GHZ and Tone of 40MHz with full power out.

Intermodulation Distortion (Old Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Intermodulation_Distortion <https://en.wikipedia.org/wiki/Intermodulation#Measurement>`__
or IMD

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd_450mhz_vs_output_power.png
   :width: 200px

   Intermodulation Distortion showing 3rd and 5th order products at 450MHz
   for 3 power levels

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd_950mhz_vs_output_power.png
   :width: 200px

   Intermodulation Distortion showing 3rd and 5th order products at 950MHz
   for 3 power levels

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd_1.85ghz_vs_output_power.png
   :width: 200px

   Intermodulation Distortion showing 3rd and 5th order products at 1.85GHz
   for 3 power levels

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd_2.45ghz_vs_output_power.png
   :width: 200px

   Intermodulation Distortion showing 3rd and 5th order products at 2.45GHz
   for 3 power levels

Intermodulation Distortion (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_1.24ghz_rx_lo_off_scale0.5.png
   :width: 200px

   1MHz Offset, LO 1.2GHz, Scale of 0.5

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_1.24ghz_rx_lo_off_scale0.25.png
   :width: 200px

   1MHz Offset, LO 1.2GHz, Scale of 0.25

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_1.24ghz_rx_lo_off_scale0.125.png
   :width: 200px

   1MHz Offset, LO 1.2GHz, Scale of 0.125
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_2.44ghz_rx_lo_off_scale0.5.png
   :width: 200px

   1MHz Offset, LO 2.4GHz, Scale of 0.5

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_2.44ghz_rx_lo_off_scale0.25.png
   :width: 200px

   1MHz Offset, LO 2.4GHz, Scale of 0.25

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_2.44ghz_rx_lo_off_scale0.125.png
   :width: 200px

   1MHz Offset, LO 2.4GHz, Scale of 0.125

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_3.64ghz_rx_lo_off_scale0.5.png
   :width: 200px

   1MHz Offset, LO 3.6GHz, Scale of 0.5

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_3.64ghz_rx_lo_off_scale0.25.png
   :width: 200px

   1MHz Offset, LO 3.6GHz, Scale of 0.25

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_3.64ghz_rx_lo_off_scale0.125.png
   :width: 200px

   1MHz Offset, LO 3.6GHz, Scale of 0.125

bandwidth (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~

`Bandwidth <https://en.wikipedia.org/wiki/Bandwidth_(signal_processing)>`__

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bw_rx_lo_off_scale0.5_tx_lo_1.2ghz.png
   :width: 200px

   BW with LO of 1.2GHZ with full power out. (20dB external attenuation)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bw_rx_lo_off_scale0.5_tx_lo_2.4ghz.png
   :width: 200px

   BW with LO of 2.4GHZ with full power out. (20dB external attenuation)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/bw_rx_lo_off_scale0.5_tx_lo_3.6ghz.png
   :width: 200px

   BW with LO of 3.6GHZ with full power out. (20dB external attenuation)

Receive Specs
-------------

Response to a ``chirp``
~~~~~~~~~~~~~~~~~~~~~~~

Although this doesn"t have a specific number associated with it, many RF systems
are ``chirpy`` - and linear response to these RF pulses is very important.

Here is a 2.4GHz waveform, input at -60dbB, with the VGA gain turned up to
+20dB. Although this does have some DC offset (the card was not calibrated), the
response is very linear over time, even when zoomed in. (Clicking on either
picture will open it up in a larger window)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/chirp_2.4ghz.png
   :width: 200px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/chirp_zoom_2.4ghz.png
   :width: 200px

And with a larger input - it looks similar. This is with an input of +6.0dBm,
with the VGA set to 4.5dB.\|

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/chirp_2.4ghz_6dbm.png
   :width: 200px

   Chirp at 2.4GHz with +6.0dBm input

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/chirp_2.4ghz_6dbm_zoom.png
   :width: 200px

   Chirp at 2.4GHz with +6.0dBm input (zoomed)

The results are similar at different frequencies.\|

Signal to Noise
~~~~~~~~~~~~~~~

`SNR <https://en.wikipedia.org/wiki/Signal-to-noise_ratio>`__

Noise floor
~~~~~~~~~~~

`Noise floor <https://en.wikipedia.org/wiki/Noise floor>`__

Input sensitivity
~~~~~~~~~~~~~~~~~

`Input sensitivity <https://en.wikipedia.org/wiki/Sensitivity_(electronics)>`__

Dynamic range
~~~~~~~~~~~~~

`Dynamic range <https://en.wikipedia.org/wiki/Dynamic range>`__

LO BW (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/rx_lo_bw_0.4to4ghz.png
   :width: 200px

   LO Sweep from 400 MHz to 4GHz, with 0dBm input signal (Low frequency
   roll-off is due to Balun 3600BL14M050)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/with_new_balun_tc1-1-43a.png
   :width: 200px

   LO Sweep from 400 MHz to 4GHz, with 0dBm input signal (With new Balun
   TC1-1-43A)

Intermodulation Distortion (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_0dbm_1.2ghzlo.png
   :width: 200px

   1MHz Offset, LO 1.2GHz, 0dBm input

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_-6dbm_1.2ghzlo.png
   :width: 200px

   1MHz Offset, LO 1.2GHz, -6dBm input

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_-12dbm_1.2ghzlo.png
   :width: 200px

   1MHz Offset, LO 1.2GHz, -12dBm input
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_0dbm_2.4ghzlo.png
   :width: 200px

   1MHz Offset, LO 2.4GHz, 0dBm input

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_-6dbm_2.4ghzlo.png
   :width: 200px

   1MHz Offset, LO 2.4GHz, -6dBm input

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_-12dbm_2.4ghzlo.png
   :width: 200px

   1MHz Offset, LO 2.4GHz, -12dBm input
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_0dbm_3.6ghzlo.png
   :width: 200px

   1MHz Offset, LO 3.6GHz, 0dBm input

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_-6dbm_3.6ghzlo.png
   :width: 200px

   1MHz Offset, LO 3.6GHz, -6dBm input

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/imd3_rx_-12dbm_3.6ghzlo.png
   :width: 200px

   1MHz Offset, LO 3.6GHz, -12dBm input

Bandwidth (Modified Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~

`Bandwidth <https://en.wikipedia.org/wiki/Bandwidth_(signal_processing)>`__

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/rx_bw_lo_1.2ghz_0dbm_input.png
   :width: 200px

   BW with 1.2GHz LO and 0dBm input (Ch1).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/rx_bw_lo_1.2ghz_0dbm_input_ch2.png
   :width: 200px

   BW with 1.2GHz LO and 0dBm input (Ch2).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/rx_bw_lo_2.4ghz_0dbm_input.png
   :width: 200px

   BW with 2.4GHz LO and 0dBm input (Ch1).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/rx_bw_lo_2.4ghz_0dbm_input_ch2.png
   :width: 200px

   BW with 2.4GHz LO and 0dBm input (Ch2).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/rx_bw_lo_3.6chz_0dbm_input.png
   :width: 200px

   BW with 3.6GHz LO and 0dBm input (Ch1).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/rx_bw_lo_3.6ghz_0dbm_input_ch2.png
   :width: 200px

   BW with 3.6GHz LO and 0dBm input (Ch2).
