.. _pluto users phase_noise:

ADALM-PLUTO Phase Noise and Frequency Accuracy
===============================================

In any transmitter (or receiver) design, frequency stability is of critical
importance. Many are interested in both long-term and short-term stability.
Long-term frequency stability is concerned with how the output signal varies
over a long period of time (minutes, hours, days, or months). It is usually
specified as the ratio, Δf/f for a given period of time, expressed as a
percentage or in dB. These changes can be the results of thermal, aging, or
voltage variations.

Short-term stability, on the other hand, is concerned with variations that occur
over a period of seconds or less. These variations can be random or periodic and
are normally referred to as phase noise, measured in dBc/Hz.

Frequency Stability
-------------------

Frequency stability is a measure of how well a device is able to produce its a
specific frequency over time without drifting from that frequency. Due to the
noise characteristics of oscillators, standard variance is not the traditional
specification, neither is phase noise since the time periods are longer. Instead
`Allan variance <https://en.wikipedia.org/wiki/Allan_variance>`_ is the tool of
choice for these statistical evaluations. Like the standard deviation, the Allan
variance shows how much the frequency of the device deviates from its specified
(or average) value.

.. figure:: images/phase_noise/pluto_allen_variance.png

The point of interest in the Allan Variance plot is the minimum of the curve.
Normally in plots like this, the deviation is high, because of noise. Over
longer observations times, the noise averages out until the minimum is reached.
The minimum thus corresponds to the point in time when the deviation from the
specified frequency is at its lowest. After that, the stability deteriorates due
to drift, temperature effects, and aging. In this case, we can see that the time
that the Pluto SDR is most stable is over 10ms (100Hz) to 1 second (1Hz). Over
this, there can be a slow drift that will affect the "average" output.

The logarithmic x-axis corresponds to the observation time ("Tau"). Note that
Tau is not the measurement time, but the evaluated time - the measurement lasts
longer than Tau. Since the Rohde & Schwarz FSWP Phase Noise instrument
calculates the Allan variance based on the measurement range of the phase noise
measurement (offset frequency), the observation time corresponds to the
measurement range and vice versa.

An alternative view of this is to look at stability over time with a
`Spectrogram <https://en.wikipedia.org/wiki/Spectrogram>`_. A spectrogram is a
visual representation of the spectrum of frequencies of a signal as it varies
with time. This is a very intuitive way to look at things, but it is not
numerically precise and is only a qualitative way to investigate things. For
example, in the spectrogram below, a 502.001 MHz signal was output in the Pluto,
we can see the signal drift over time. This drift is a measurement of the
difference between the instrument (Tektronix
`RSA5126B <https://www.tek.com/spectrum-analyzer/rsa5126b>`_ Real Time Signal
Analyzer, which has ±1ppm initial accuracy) and the Pluto (which is ±25ppm
initial accuracy). The Pluto could be drifting, or the instrument could be
drifting. The width of the drift is ~ 100 Hz over 60 minutes. For 500,000,000 Hz
carrier, a 100 Hz drift is under 0.2 ppm. It should be noted that this is while
the ADALM-PLUTO was allowed to warm up (via self-heating) for 20 min before this
measurement was recorded. This was approximately 1 hour of measurement.

.. figure:: images/phase_noise/pluto_drift.png

Phase Noise
-----------

The `phase noise <https://en.wikipedia.org/wiki/Phase_noise>`_ spectrum of an
oscillator shows the noise power in a 1 Hz bandwidth as a function of frequency.
Phase noise is defined as the ratio of the noise in a 1 Hz bandwidth at a
specified frequency offset, fm, to the oscillator signal amplitude at frequency
fo. It is customary to characterize an oscillator in terms of its
single-sideband phase noise, where the phase noise in dBc/Hz is plotted as a
function of frequency offset, fm, with the frequency axis on a log scale.

.. figure:: images/phase_noise/phase_noise_vs_offset.png

Note the curve is approximated by a number of regions, each having a slope of
1/fX, where x = 0 corresponds to the "white" phase noise region (slope =
0dB/decade), and x = 1, corresponds to the "flicker" phase noise region (slope =
–20 dB/decade). There are also regions where x = 2, 3, 4, and these regions
occur progressively closer to the carrier frequency.

In modern communications algorithms, the phase noise is much more important than
frequency stability, as carrier offset and timing correction algorithms will
eliminate most frequency accuracy/stability issues. This is why most people look
at phase noise from 10kHz to 10 MHz. In the below tests, we can see things from
100 Hz to 100 MHz, which covers more than what most people are interested in.

.. figure:: images/phase_noise/pluto_phase_noise_100hz2100mhz.png

However, at lower frequencies (100 mHz, or over 10 seconds) to 100 kHz, we can
see that the noise, or in this case drift, can vary quite a bit. This sub 100
kHz offset/noise/drift can normally be resolved by signal processing algorithms
where carrier offset correction algorithms have specifically been designed to
reduce this drift.

.. figure:: images/phase_noise/pluto_phase_noise_100mhz2100khz.png

Summary
-------

Phase noise and drift are key parameters for many oscillators and signal sources
as it governs many aspects of the overall performance. In modern communication
systems, many drift issues can be overcome with various signal processing
algorithms.

More information
----------------

There are a few great tutorials and writeups including:

* `Mini-Tutorial 086 : Fundamentals of Phase Locked Loops (PLLs) <https://www.analog.com/media/en/training-seminars/tutorials/MT-086.pdf>`_

* `Webcast : Explaining Phase Noise <https://www.analog.com/en/education/education-library/webcasts/explaining-phase-noise.html>`_

* `AN-741 Little Known Characteristics of Phase Noise <https://www.analog.com/media/en/technical-documentation/application-notes/589324855748812403694448557703434217045254275316215330254506699244016AN741_0.pdf>`_

* `Rohde & Schwarz FSWP Phase Noise Analyzer User Manual <https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_common_library/dl_manuals/gb_1/f/fswp_1/FSWP_UserManual_en_10.pdf>`_

* `Software-Defined Radio for Engineers, Chapter 7, Carrier Synchronization <https://www.analog.com/media/en/training-seminars/design-handbooks/Software-Defined-Radio-for-Engineers-2018/SDR4Engineers_CH07.pdf#page%3D14>`_

* `Software-Defined Radio for Engineers, Chapter 6, Timing Synchronization <https://www.analog.com/media/en/training-seminars/design-handbooks/Software-Defined-Radio-for-Engineers-2018/SDR4Engineers_CH06.pdf#page%3D14>`_