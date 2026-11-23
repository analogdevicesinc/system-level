---
orphan: true
---

(adc x-band-dev-kit)=
# X-Band Phased Array Development Platform

The **{adi}`X-Band Phased Array Development Platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/x-band-development-platform.html>`** is a complete system solution designed for phased array radars, electronic warfare, and ground-based SATCOM applications. It provides a testbed for demonstrating hybrid beamforming phased array radar as well as the implementation of system level calibrations, beamforming algorithms, and other signal processing algorithms.

```{image} xbdev-box.png
:alt: X-Band Development Platform Kit
```

The platform consists of three main components:
- **{ref}`x-band-mxfe`** - AD9081 MxFE Evaluation Board
- **{ref}`x-band-converter`** - X/C Band Up/Down Converter
- **{ref}`x-band-beamforming`** - X/Ku-Band Analog Beamforming Board (Stingray)

The system is designed to mate with a {xilinx}`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` Evaluation Board from Xilinx®, featuring the Zynq® UltraScale+™ ZU9EG FPGA, with provided reference software, HDL code, and MATLAB/Python system-level interfacing.

## Target Applications

The X-Band Development Platform enables quick time-to-market development programs for:

- **ADEF (Phased-Array, RADAR, EW, SATCOM)**
- **Hybrid Beamforming**
- **Electronic Test and Measurement**

## Table of Contents
```{toctree}
:maxdepth: 2

Hardware Introduction <hardware/index>
Unboxing and Initial Setup <setup/index>
pyRadar <pyradar/index>
```

```{toctree}
:maxdepth: 1

Troubleshooting <troubleshooting/index>
Additional Resources <resources/index>
```

## System Overview

The X-Band Development Platform highlights a complete system solution specifically targeting a 32-channel transmit/32 receive hybrid beamforming phased array. It is intended as a testbed for demonstrating phased array system level calibrations, hybrid beam forming (analog/digital) algorithms, and other signal processing algorithms.

```{note}
For questions or help with the X-Band Development Platform, please visit:\
{ez}`adef-system-platforms`
```

