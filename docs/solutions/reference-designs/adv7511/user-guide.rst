.. _adv7511 user-guide:

User guide
===============================================================================

The :adi:`ADV7511` is a 225 MHz High-Definition Multimedia Interface (HDMI®)
transmitter integrated on several Xilinx FPGA evaluation boards. This guide
provides information about the hardware configuration and software usage.

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADV7511 is integrated on-board the following Xilinx evaluation platforms:

- :xilinx:`AC701` - Artix-7 FPGA
- :xilinx:`KC705` - Kintex-7 FPGA
- :xilinx:`VC707` - Virtex-7 FPGA
- :xilinx:`ZC702` - Zynq-7000 SoC
- :xilinx:`ZC706` - Zynq-7000 SoC
- `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__ - Zynq-7000 SoC

Video Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The video interface configuration varies by carrier board:

**Most platforms (AC701, KC705, ZC702, ZC706, ZED):**

- 16-bit YCbCr 422 interface (ZC706 is on 24 bit interface)
- Separate synchronization signals
- Pixel clock: up to 148.5 MHz (1080p)

**VC707 platform:**

- 36-bit RGB 444 interface
- Separate synchronization signals
- Pixel clock: up to 148.5 MHz (1080p)

Audio Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All platforms use:

- Single-bit SPDIF interface
- Sample rates: 32 kHz, 44.1 kHz, 48 kHz
- 16-bit or 24-bit audio samples

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADV7511 is powered directly from the evaluation board's on-board power
supply. No external power supply is required for the HDMI transmitter.

Reference documentation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`ADV7511 Programming Guide <media/en/technical-documentation/user-guides/ADV7511_Programming_Guide.pdf>`
- :adi:`ADV7511 Hardware User Guide <media/en/technical-documentation/user-guides/ADV7511_Hardware_Users_Guide.pdf>`
- :adi:`ADV7511 Data Sheet <media/en/technical-documentation/data-sheets/ADV7511.pdf>`

Software guide
-------------------------------------------------------------------------------

The ADV7511 reference design is supported through multiple software options:

no-OS Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The no-OS software uses the **ADV7511 Transmitter Library**, which is a
collection of APIs that provide a consistent interface to the ADV7511. The
library is a software layer that sits between the application and the TX
hardware.

The library provides:

- APIs to configure HDMI TX hardware without low-level register access
- Application portability across different hardware revisions
- Basic services: interrupt service routine, HDCP control, status information

The documentation for the library's API can be accessed here:
:ref:`adv7511 transmitter-api`

The no-OS project can be downloaded here: :git-no-OS:`projects/adv7511`

Linux Software (Zynq platforms only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Zynq platforms (ZC702, ZC706, ZED), the ADV7511 is supported in Linux
through the kernel drivers:

- :external+linux:ref:`AXI HDMI TX Linux driver <hdl-axi-hdmi>`
- :external+linux:ref:`ADV7511 Linux device driver <adv7511>`

The Linux driver provides:

- DRM/KMS framework integration
- HDMI display output
- EDID reading
- Hot-plug detection
- Audio support via ALSA

Functional Description
-------------------------------------------------------------------------------

The reference design consists of two independent IP core modules:

Video Core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The video part consists of an AXI DMAC interface and the ADV7511 video
interface. The ADV7511 interface consists of a 16-bit YCbCr 422 interface
(36-bit RGB 444 for VC707) with separate synchronization signals.

Key features:

- DMA streams frame data to the core
- Small internal buffers (1K) - does NOT buffer full frames
- Configurable video formats through parameter registers
- Pixel clock generated internal to the device
- Programmable color pattern for debug purposes
- Default mode: 1080p

The reference design reads 24-bit RGB data from DDR and performs:

- Color space conversion (RGB to YCbCr)
- Down sampling (444 to 422) for most platforms
- For VC707: passes 36-bit RGB 444 directly

**Video Timing Parameters (1080p example):**

HSYNC parameters:

- **HSYNC count**: 2200 (total horizontal pixel clocks)
- **HSYNC width**: 44 (pulse width in pixel clocks)
- **HSYNC DE Minimum**: 192 (start of active video: 44 + 148)
- **HSYNC DE Maximum**: 2112 (end of active video: 44 + 148 + 1920)

VSYNC parameters:

- **VSYNC count**: 1125 (total vertical lines)
- **VSYNC width**: 5 (pulse width in lines)
- **VSYNC DE Minimum**: 41 (start of active video: 5 + 36)
- **VSYNC DE Maximum**: 1121 (end of active video: 5 + 36 + 1080)

Pixel frequency for 1080p: 148.5 MHz

Audio Core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The audio part consists of an AXI DMAC interface and the ADV7511 SPDIF audio
interface.

Key features:

- Audio clock derived from bus clock
- Programmable division factor
- Audio data: two 16-bit words for left and right channels
- SPDIF frame transmission
- Configurable sample frequency and format
- Default: 48 KHz

For detailed register information, please refer to the regmap.txt file inside
the IP cores.

ASoC Audio
~~~~~~~~~~

The codec driver registers one DAI: **adv7511**.

.. list-table:: Supported DAI Formats
   :header-rows: 1

   * - Format
     - Supported
   * - I2S (SND_SOC_DAIFMT_I2S)
     - Yes
   * - Right Justified (SND_SOC_DAIFMT_RIGHT_J)
     - Yes
   * - Left Justified (SND_SOC_DAIFMT_LEFT_J)
     - Yes
   * - S/PDIF (SND_SOC_DAIFMT_SPDIF)
     - Yes
   * - Normal bit/frameclock (SND_SOC_DAIFMT_NB_NF)
     - Yes
   * - Inverted bitclock, normal frameclock (SND_SOC_DAIFMT_IB_NF)
     - Yes
   * - Codec bit/frameclock slave (SND_SOC_DAIFMT_CBS_CFS)
     - Yes