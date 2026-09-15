.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq2-ebz/introduction

.. _ad-fmcdaq2-ebz introduction:

Introduction
============

The
:adi:`AD-FMCDAQ2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad-fmcdaq2-ebz.html#eb-overview>`
module is comprised of the
:adi:`AD9680 <en/products/analog-to-digital-converters/high-speed-ad-10msps/high-if-ad-converters/ad9680.html>`
dual, 14-bit, 1.0 GSPS, JESD204B ADC, the
:adi:`AD9144 <en/products/digital-to-analog-converters/da-converters/ad9144.html>`
quad, 16-bit, 2.8 GSPS, JESD204B DAC, the
:adi:`AD9523-1 <en/products/clock-and-timing/clock-generation-distribution/ad9523-1.html#product-overview>`
clock, and power management components. It is clocked by an internally generated
carrier platform via the FMC connector, comprising a completely self contained
data acquisition and signal synthesis prototyping platform. In an FMC footprint
(84 mm × 69 mm), the module"s combination of wideband data conversion, clocking,
and power closely approximates real-world hardware and software for system
prototyping and design, with no compromise in signal chain performance. For
additional information or to purchase the AD-FMCDAQ2-EBZ, please visit:
www.analog.com/AD-FMCDAQ2-EBZ

Features
========

- Includes schematics, layout, BOM, Gerber files, HDL, Linux® drivers, IIO
  Oscilloscope, VisualANALOG,…
- FMC-compatible form factor
- Powered from single FMC connector
- Provides two channels of ADC and two channels of DAC with full synchronization
  capabilities

AD9680-1000 ADC
===============

- JESD204B (subclass 1) 4-lane coded serial digital outputs
- SFDR: 80 dBc at 1 GHz AIN, 1.0 GSPS
- Noise density: –154 dBFS/Hz @ 1.0 GSPS
- 2 GHz of usable analog input full power bandwidth
- Two integrated DDCs per channel

AD9144 DAC
==========

- JESD204B (subclass 1) coded serial digital outputs
- Supports complex signal bandwidths up to 800 MHz
- 6-carrier GSM IMD = 75 dBc at 75 MHz IF
- SFDR = 85 dBc (BW = 300 MHz) at DC IF
- Selectable 2×, 4×, 8× interpolation filters

Applications
============

- Electronic test and measurement equipment
- General-purpose software radios
- Radar systems
- Ultra wideband satellite receivers
- Signals intelligence (SIGINT)
- Point to point communication systems
- DOCSIS 3.0 CMTS and HFC networks
- Multiple input/multiple output (MIMO) radios
- Automated test equipment
