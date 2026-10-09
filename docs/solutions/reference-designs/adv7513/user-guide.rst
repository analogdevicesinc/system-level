.. _adv7513 user-guide:

User Guide
===============================================================================

Here is the complete product page for the :adi:`ADV7513`.

Hardware Guide
-------------------------------------------------------------------------------

Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADV7513` HDMI transmitter is integrated on-board the
`DE10-Nano <https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/terasic-de10-nano-kit.html>`__.
The FPGA fabric drives the :adi:`ADV7513` with digital video and audio data,
transmitting it over HDMI.

The :adi:`ADV7513` is configured over I²C. The ARM Cortex-A9 processor in the
Cyclone V SoC acts as the I²C master.

Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADV7513` is powered directly from the evaluation board's on-board
power supply. No external power supply is required for the HDMI transmitter.

Functional Description
-------------------------------------------------------------------------------

Video Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `DE10-Nano <https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/terasic-de10-nano-kit.html>`__
reference design uses:

- 16-bit YCbCr 4:2:2 interface
- Separate synchronization signals (HSYNC, VSYNC, DE)
- Pixel clock: up to 148.5 MHz (1920×1080 @ 60 Hz)

The :adi:`ADV7513` supports pixel clocks up to 165 MHz, covering all
resolutions up to 1080p and UXGA.

Audio Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `DE10-Nano <https://www.analog.com/en/resources/reference-designs/circuits-from-the-lab/terasic-de10-nano-kit.html>`__
reference design uses:

- Single-bit S/PDIF interface
- No audio master clock required (clock recovered from S/PDIF bitstream)
- Sample rates: 32 kHz, 44.1 kHz, 48 kHz
- 16-bit or 24-bit audio samples

Under Linux, the :adi:`ADV7513` audio is exposed as an ALSA audio device
through the ASoC framework. The following DAI formats are supported:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Format
     - Description
   * - ``SND_SOC_DAIFMT_I2S``
     - Standard I²S (up to 8 channels, up to 192 kHz)
   * - ``SND_SOC_DAIFMT_SPDIF``
     - S/PDIF (stereo LPCM or IEC 61937 compressed)

Software Guide
-------------------------------------------------------------------------------

Linux Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under Linux, the :adi:`ADV7513` is supported by the ``adv7511`` DRM bridge
driver (``drivers/gpu/drm/bridge/adv7511/``). The driver uses the
``"adi,adv7513"`` compatible string and is otherwise identical to the ADV7511
driver, with the exception that pixel clocks above 165 MHz are rejected.

The driver implements the DRM bridge interface and exposes:

- HPD (Hot Plug Detect) monitoring
- EDID read from the HDMI sink via DDC (I²C)
- HDCP v1.4 support
- CEC controller (via separate CEC framework driver)

The framebuffer is provided by the AXI HDMI driver
(:external+linux:ref:`hdl-axi-hdmi`), which uses
the AXI-DMAC to stream pixel data from memory to the :adi:`ADV7513`.

Relevant Linux drivers:

- :external+linux:ref:`hdl-axi-hdmi`
- :external+linux:ref:`axi-dmac`
- :external+linux:ref:`adv7511`
  (supports ADV7511, ADV7511W, ADV7513, ADV7533, ADV7535)

Resources
-------------------------------------------------------------------------------

- :adi:`ADV7513: 165 MHz, High Performance HDMI Transmitter Data Sheet <media/en/technical-documentation/data-sheets/ADV7513.pdf>`
- :adi:`ADV7511 Programming Guide, Rev. 1.2 <media/en/technical-documentation/user-guides/ADV7511_Programming_Guide.pdf>`
- :external+hdl:ref:`adv7513`

Support
-------------------------------------------------------------------------------

- :ref:`Help and Support <help-and-support>`
- :ez:`FPGA Reference Designs EngineerZone <community/fpga>`
