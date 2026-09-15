.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-cn0363-pmdz/introduction

.. _eval-cn0363-pmdz introduction:

EVAL-CN0363-PMDZ Introduction
=============================

:adi:`CN0363` is a dual-channel colorimeter featuring a modulated light source
transmitter, programmable gain transimpedance amplifiers on each channel, and a
very low noise, 24-bit Σ-Δ analog-to-digital converter (ADC). The output of the
ADC connects to a standard FPGA mezzanine card. The FPGA takes the sampled data
from the ADC and implements a synchronous detection algorithm. By using
modulated light and digital synchronous detection rather than a constant (dc)
source, the system strongly rejects any noise sources at frequencies other than
the modulation frequency, providing excellent accuracy. The dual-channel circuit
measures the ratio of light absorbed by the liquids in the sample and reference
containers at three different wavelengths. This measurement forms the basis of
many chemical analysis and environmental monitoring instruments used to measure
concentrations and characterize materials through absorption spectroscopy.

|
| .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cn0363-pmdz/CN0363_sch.jpg
   :width: 1000px

A clock set to a user-programmable frequency modulates one of the three LED
colors (R,G,B) with a constant current driver built around the :adi:`AD8615` op
amp, the :adi:`ADG819` switch, and the :adi:`AD5201` digital potentiometer. The
beam splitter sends half the light through the sample container and half through
the reference container. The :adi:`ADA4528-1`, configured as a transimpedance
amplifier, then converts the photodiode current into an output voltage square
wave, whose amplitude is proportional to the light transmitted through the
sample or reference containers. The transimpedance amplifiers use the ADG633
single-pole, double-throw (SPDT) switches to select one of two transimpedance
gains. The :adi:`AD7175-2` Σ-Δ ADC samples the voltage and sends the digital
data to an FPGA for digital demodulation.

For a thorough circuit description, please visit
:adi:`CN0363 Circuit Note </media/en/reference-design-documentation/reference-designs/CN0363.pdf>`.

More Information
----------------

.. - `EVAL-CN0363-PMDZ User Guide <>`__
