.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv904x/dpd/dfe_system_overview

.. _adrv904x dpd dfe_system_overview:

ADRV904x DFE SYSTEM LEVEL OVERVIEW
==================================

The DPD feature on the ADRV904x transceiver enables users to offload power
amplifier linearization tasks from the baseband processor to the transceiver.
With DPD implemented on the transceiver, the user does not need to allocate JESD
serializer/de-serializer resources for observing power amplifier feedback data
through the ORx channels, resulting in significant system power savings. Digital
Up-Converters, Interpolators leading to the DPD actuator allow the baseband
processor to transmit data at a lower rate on the JESD204B/C link than is needed
for the full DPD correction bandwidth. The lower data rate at JESD translates
directly into power savings and less number of lanes. Integration of the DPD
into the transceiver chip results in significant system level cost, space, and
power savings when compared to conventional FPGA/ASIC based implementations.

The ADRV904x transceiver provides digital signal processing capabilities in the
embedded ARM quad core A55 processor + HW accelerators using closed-loop
feedback signals from the observation receiver channels. These functions improve
transmitter performance, measure system output, and reduce system power
consumption. The list of functions includes the following: digital
pre-distortion (DPD), closed-loop gain control (CLGC), voltage standing wave
ratio(VSWR) measurement and crest factor reduction (CFR). These functions are
collectively grouped together as the transceiver digital front end (DFE).

The figure shown below is a simplified system level overview of the transceiver
signal chain with DFE processing blocks highlighted. There are six main DFE
processing blocks:

#. CFR and hard clipper are used to reduce peak to average power ratio (PAPR) of
   the baseband signal, especially for multi-carrier waveforms such as OFDM.
   With reduced PAPR, the PA can operate at a higher output power, increasing
   the PA efficiency. This function is explained in the Crest Factor Reduction
   (CFR) section.
#. There is also an optional post-CFR gain block that can be used to increase
   the gain of signals post CFR clipping to compensate for reduced peak
   amplitude post CFR.
#. There are two half band filters with a total interpolation factor of 4x
   before the DPD actuator. These blocks can provide a total of 1x, 2x or 4x
   interpolation.
#. There are three DPD capture buffers, which include the pre-DPD actuator data,
   post-DPD actuator data, and observation buffers. Each buffer can capture a
   maximum of 4096 samples.
#. DPD actuator (max rate of 2GHz), which applies the inverse PA model to the
   baseband signal for power amplifier linearization. The DPD Actuator on
   ADRV904x comes with dedicated Charge Trapping Correction HW for GaN PAs.
#. DFE Processor is a Quad core embedded ARM A55 processor on which the DPD,
   VSWR and CLGC algorithms are deployed. Additionally, there are dedicated HW
   accelerators for signal processing intensive tasks such as cross correlation
   and feature filtering.

Please note that the observation path on ADRV904x consists of a direct RF
sampling ADC compared to regular ADCs in the previous generation ADRV902x
transceivers.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv904x/dpd/adrv904x_dfe_system_overview.jpg
