.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad7768-ebz/software/baremetal

.. _ad7768-ebz software baremetal:

AD7768-EVB Bare Metal Quick Start Guide
=======================================

Overview
--------

The :adi:`AD7768` is an 8-channel simultaneous sampling sigma-delta (Σ-Δ)
analog-to-digital converter (ADC), respectively, with a Σ-Δ modulator and
digital filter per channel, enabling synchronized sampling of ac and dc signals.

The :adi:`AD7768` achieves 108 dB dynamic range at a maximum input bandwidth of
110.8 kHz, combined with typical performance of ±2 ppm integral nonlinearity
(INL), ±50 μV offset error, and ±30 ppm gain error.

The :adi:`AD7768` user can trade off input bandwidth, output data rate, and
power dissipation, and select one of three power modes to optimize for noise
targets and power consumption. The flexibility of the :adi:`AD7768` allows it to
become a reusable platform for low power dc and high performance ac measurement
module.

The :adi:`AD7768` has three modes: fast mode (256 kSPS maximum, 110.8 kHz input
bandwidth, 51.5 mW per channel), median mode (128 kSPS maximum, 55.4 kHz input
bandwidth, 27.5 mW per channel) and low power mode (32 kSPS maximum, 13.8 kHz
input bandwidth, 9.375 mW per channel).

The :adi:`AD7768` offers extensive digital filtering capabilities, such as a
wideband, low ±0.005 dB pass-band ripple, antialiasing low-pass filter with
sharp roll-off, and 105 dB attenuation at the Nyquist frequency.

Frequency domain measurements can use the wideband linear phase filter. This
filter has a flat pass band (±0.005 dB ripple) from dc to 102.4 kHz at 256 kSPS,
from dc to 51.2 kHz at 128 kSPS, or from dc to 12.8 kHz at 32 kSPS.

The :adi:`AD7768` also offers sinc response via a sinc5 filter, a low latency
path for low bandwidth, and low noise measurements. The wideband and sinc5
filters can be selected and run on a per channel basis.

Within these filter options, the user can improve the dynamic range by selecting
from decimation rates of ×32, ×64, ×128, ×256, ×512, and ×1024. The ability to
vary the decimation filtering optimizes noise performance to the required input
bandwidth.

Embedded analog functionality on each ADC channel makes design easier, such as a
precharge buffer on each analog input that reduces analog input current and a
precharge reference buffer per channel reduces input current and glitches on the
reference input terminals.

The device operates with a 5 V AVDD1A and AVDD1B supply, a 2.25 V to 5.0 V
AVDD2A and AVDD2B supply, and a 2.5 V to 3.3 V or 1.8 V IOVDD supply (see the
1.8 V IOVDD Operation section for specific requirements for operating at 1.8 V
IOVDD).

The device requires an external reference; the absolute input reference voltage
range is 1 V to AVDD1 − AVSS.

The specified operating temperature range is −40°C to +105°C. The device is
housed in a 10 mm × 10 mm 64-lead LQFP package with a 12 mm × 12 mm printed
circuit board (PCB) footprint.

Supported devices
~~~~~~~~~~~~~~~~~

- :adi:`AD7768`

Evaluation boards
~~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD7768`

Supported FPGA carrier
~~~~~~~~~~~~~~~~~~~~~~

- :xilinx:`ZedBoard <products/boards-and-kits/1-8dyf-11.html>`

HDL Design Description
----------------------

In the
:dokuwiki:`ADI Reference Designs HDL User Guide </resources/fpga/docs/hdl>` can
be found an in-depth presentation and instructions about the HDL design in
general.

In order to build the HDL design the user has to go through the following steps:

#. Confirm that you have the right tools (see
   `Release notes <https://github.com/analogdevicesinc/hdl/releases>`__)
#. Clone the HDL GitHub repository (see
   https://wiki.analog.com/resources/fpga/docs/git)
#. Build the project (see https://wiki.analog.com/resources/fpga/docs/build)

The HDL architecture comprises a serial data path that enables all the ADC
channels and a parallel data path, so that the user can enable only the desired
channels.

HDL block diagram
~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7768evb_fmc_hdl.svg
   :width: 800px

HDL Downloads
~~~~~~~~~~~~~

.. admonition:: Download

   - AD7768-EVB HDL Project - :git-hdl:`projects/ad7768evb`

No-OS Downloads
~~~~~~~~~~~~~~~

.. admonition:: Download

   - AD7768-EVB Main Driver -
     :git-no-OS:`no-OS/tree/main/projects/ad7768-evb <tree/main/projects/ad7768-evb+>`
   - Generic Platform Drivers -
     :git-no-OS:`https://github.com/analogdevicesinc/no-OS/tree/main/common_drivers/platform_drivers <tree/main/legacy/common_drivers/platform_drivers+>`
   - AD7768 Driver - :git-no-OS:`drivers/adc/ad7768`
   - ADC Core Driver -
     :git-no-OS:`https://github.com/analogdevicesinc/no-OS/tree/main/common_drivers/adc_core <tree/main/legacy/common_drivers/adc_core+>`
   - no-OS IIO - :dokuwiki:`iio </resources/tools-software/no-os-software/iio>`
