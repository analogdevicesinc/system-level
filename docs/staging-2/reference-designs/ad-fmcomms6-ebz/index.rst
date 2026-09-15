.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms6-ebz

.. _ad-fmcomms6-ebz:

AD-FMCOMMS6-EBZ User Guide
==========================

The
:adi:`AD-FMCOMMS6-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD-FMCOMMS6-EBZ.html>`
eval board is a 400MHz to 4.4GHz receiver based on the :adi:`AD9652` dual 16bit
analog to digital converter, the :adi:`ADL5566` High Dynamic Range RF/IF Dual
Differential Amplifier and the :adi:`ADL5380` quadrature demodulator.

This is an I and Q demodulation approach to direct convert (also known as a
homodyne or zero IF) receiver architecture. Direct conversion radios perform
just one frequency translation compared to a super-heterodyne receiver that can
perform several frequency translations. One frequency translation is
advantageous because it:

- Reduces receiver complexity and the number of stages needed, increasing
  performance and reducing power consumption
- Avoids image rejection issues and unwanted mixing

This topology will provide image rejection and early implementation of the
differential signal environment. There is an amplification stage to maintain the
full-scale input to the ACD. The local oscillator and ADC clock are on board and
share the same reference signal prevent smearing. The form factor is VITA57
compliant and all of the DC power is routed from the data capture board through
an FMC connector. This evaluation board demonstrates a high performance receiver
signal chain aimed at military and commercial radar using ``commercial off the
shelf`` (COTS) components. The overall circuit has a bandwidth of 220MHz with a
pass band flatness of +/- 1.0 dB. The SNR and SFDR measured at an IF of 145MHz
are 64dB and 75dBc, respectively.

Contains
--------

.. figure:: https://wiki.analog.com/_media/resources/fpga/Xilinx/fmc/fmcomms6/top_view_main_page.png
   :width: 400px

The card contains:

- :adi:`AD9652` two 16-bit ADC with sampling speeds of up to 310 MSPS
- :adi:`ADL5380`, a broadband quadrature I-Q demodulator that covers an RF/IF
  input frequency range from 400 MHz to 6 GHz.
- :adi:`ADL5566` a high performance, dual differential amplifier optimized for
  IF and dc applications.
- :adi:`ADP2370` high efficiency, low quiescent current, 800 mA buck (step-down)
  dc-to-dc converters in small 8-lead, 3 mm × 3 mm LFCSP (QFN) packages.
- :adi:`AD9517-4` provides a multi-output clock distribution function with
  subpicosecond jitter performance, along with an on-chip PLL and VCO.
- :adi:`ADF4351` allows implementation of fractional-N or integer-N phase-locked
  loop (PLL) frequency synthesizers if used with an external loop filter and
  external reference frequency.
- :adi:`ADM7150` is a low dropout linear regulator that operates from 4.5 V to
  16 V and provides up to 800 mA of output current.

- :dokuwiki:`Hardware <ad-fmcomms6-ebz/hardware>` (including schematics)
- :dokuwiki:`hardware#picture and main components <ad-fmcomms6-ebz/hardware#picture and main components>`
- :dokuwiki:`hardware#outline <ad-fmcomms6-ebz/hardware#outline>`
- :dokuwiki:`hardware#size <ad-fmcomms6-ebz/hardware#size>`
- :dokuwiki:`hardware#downloads <ad-fmcomms6-ebz/hardware#downloads>`
