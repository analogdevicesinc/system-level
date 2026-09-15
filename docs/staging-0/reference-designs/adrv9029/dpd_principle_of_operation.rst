.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9029/dpd_principle_of_operation

.. _adrv9029 dpd_principle_of_operation:

DPD INTRODUCTION
================

DPD is a technique for improving the linearity of a non-linear system such as a
power amplifier by introducing precise anti-distortion into the input waveform
that compensates for the PA"s in-band nonlinear products. DPD works on the
principle of pre-distorting the transmit data in the digital domain to cancel
the distortion caused by PA compression in the analog domain. In this way, DPD
can improve PA power-added efficiency by double or more, allowing the PA to be
pushed further into saturation while maintaining linearity requirements.

A baseband model of the power amplifier is created and trained on the input and
output digital-baseband samples that pass through the PA as shown in the figure
below. The pre-distorter then applies an inverse of the PA model function to
input samples before passing them to the transmitter output. The cascade of the
pre-distorter response and the PA response becomes a nearly-linear system.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpd_principleofoperation.png
   :width: 400px

The intermodulation distortion products between various subcarriers due to PA
non-linearities in a wideband transmission protocol such as LTE/NR manifest as
power leaked into adjacent channels. Adjacent Channel Leakage Ratio (ACLR) is
defined as the ratio of the transmitted power on the assigned channel to the
power leaked in the adjacent radio channel. The ACLR performance improvement
following the application of DPD to the baseband data is captured in the figure
below. These plots illustrate how the out of band non-linearities due to
intermodulation products of an LTE 20 MHz signal are reduced by 15-20 dB after
the application of DPD.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpd_prepostdpd_comparisonlte20.png
   :width: 400px
