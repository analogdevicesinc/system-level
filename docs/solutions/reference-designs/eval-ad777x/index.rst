.. _eval-ad777x:

EVAL-AD777X
===============================================================================

8-Channel, 24-Bit Simultaneous Sampling Sigma-Delta ADC Evaluation Board.

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7770-AD7779` is the evaluation board for the
:adi:`AD7770`, :adi:`AD7771`, and :adi:`AD7779` 8-channel, simultaneous
sampling, 24-bit sigma-delta (Σ-Δ) analog-to-digital converters (ADCs).
The evaluation board supports all three device variants through the same
hardware; the active device is selected in firmware.

The AD777X family provides an ultralow input current to allow direct sensor
connection. Each input channel features a programmable gain stage with
gains of 1, 2, 4, and 8, mapping lower-amplitude sensor outputs into the
full-scale ADC input range to maximize dynamic range. The devices accept
differential or single-ended input signals and support both unipolar and
bipolar analog supply configurations.

Each channel contains an ADC modulator and a sinc3, low latency digital
filter. A sample rate converter (SRC) provides fine resolution control
over the output data rate, supporting applications where coherency with
line-frequency changes is required. The SPI interface is used for register
access and SAR ADC control (on the :adi:`AD7779`). A 12-bit on-chip SAR
ADC on the :adi:`AD7779` enables device diagnostics without decommissioning
a Σ-Δ channel.

The evaluation board connects to a ZedBoard FPGA development kit via the
FMC LPC connector. Kuiper Linux runs on the Zynq-7000 SoC and exposes the
ADC channels through the IIO subsystem, enabling data capture with
standard IIO tools.

Features:

- 8-channel, simultaneous sampling, 24-bit Σ-Δ ADC
- Programmable gain per channel: 1, 2, 4, and 8
- Ultralow input current - direct sensor connection
- True differential and single-ended input support
- Unipolar and bipolar analog supply configurations
- Integrated 2.5 V reference (AD7779)
- High resolution and low power operating modes
- SRC for fine output data rate resolution
- 12-bit SAR ADC for diagnostics (AD7779)
- SPI control interface with optional CRC validation

Applications:

- Industrial process control
- General-purpose data acquisition
- Electroencephalography (EEG)
- Circuit breakers and protection

.. figure:: ./images/EVAL-AD7770FMCZ_ANGLE.jpeg
   :alt: Photo of the EVAL-AD7770FMCZ evaluation board
   :align: center
   :width: 800

   EVAL-AD7770FMCZ Evaluation Board

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete
as it should be. If you have any questions, feel free to ask on our
:ez:`/`, but before that, please make sure you read our documentation
thoroughly.

To better understand the AD777x family, we recommend using the
:adi:`EVAL-AD7770-AD7779` evaluation board together with the
`ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_
FPGA development kit.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design:

   #. :ref:`Prerequisites <eval-ad777x prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guide <eval-ad777x quickstart>`:

      #. Using the :ref:`ZedBoard <eval-ad777x quickstart zed>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD777x

   - :ref:`eval-ad777x block-diagram`

     - :adi:`AD7770` product page
     - :adi:`AD7771` product page
     - :adi:`AD7779` product page

   - Resources for designing a custom AD777x-based platform:

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dmac`

     #. :external+hdl:ref:`HDL reference design <ad777x_fmcz>` which
        you must use in your FPGA.

     #. No-OS Drivers (in development):
           - :git-no-OS:`AD7779 No-OS driver <drivers/adc/ad7779>`

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad777x block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: ./images/ad7770-fbl.jpeg
   :alt: Block diagram of the AD777x HDL reference design on ZedBoard
   :align: center
   :width: 800

   AD777x Block Diagram

Warning
-------------------------------------------------------------------------------

.. esd-warning::
