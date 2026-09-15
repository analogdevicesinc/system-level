.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad9213_dual_ebz/introduction

.. _ad9213_dual_ebz introduction:

NO TITLE
========

Introduction
------------

The AD-9213-DUAL-EBZ platform includes two
:adi:`AD9213 <en/products/ad9213.html>`, single, 12-bit, 10 GSPS, radio
frequency (RF) analog-to-digital converters (ADC) with the JESD204B interface.
The two 10 GSPS data converters are interleaved to sample at 20 GSPS enabled by
their built-in multi-chip synchronization capability. The
:adi:`ADF4377 <en/products/adf4377.html#product-overview>`, high performance,
ultra-low jitter, dual output integer-N phased locked loop (PLL) with an
integrated voltage-controlled oscillator (VCO), supports the interleaving. The
:adi:`LTC6955 <en/products/ltc6955.html>`, low jitter, fanout clock buffer, and
the :adi:`LTC6952 <en/products/ltc6952.html>` JESD204B clock generation and
distribution IC enable a clocking architecture built for multi-channel
scalability. The platform allows users to direct sample L, S, and C bands, all
while supporting up to 8GHz of IBW per channel. It is a complete reference
design, from RF to bits: RF layouts, clocking architectures, power distribution
network designs, and a full software stack (HDL to MATLAB). It is designed to be
plug-and-play out of the box, enabling a reduction in design/prototype cycle
time and going to market faster.

Features
~~~~~~~~

- 20GSPS sample rate through interleaving supporting up to 8 GHz of
  instantaneous BW
- Multi-chip synchronization (MCS) at 10GSPS using a scalable reference
  distribution architecture
- Input network supporting a wide analog frequency range DC - 9GHz
- Compact layout scheme that can be quickly adopted into a customer application

Applications
~~~~~~~~~~~~

- EW
- ECM / ECCM
- Radar
- Instrumentation
- Multi-channel Wideband receivers
