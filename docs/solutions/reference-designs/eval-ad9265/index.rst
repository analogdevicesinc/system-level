.. _eval_ad9265:

EVAL-AD9265
===============================================================================

16-Bit, 125 MSPS/105 MSPS/80 MSPS, 1.8 V Analog-to-Digital Converter.

.. image:: images/eval-ad9265.png
   :width: 400

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9265` is a full-featured evaluation board for the
:adi:`AD9265`, a 16-bit, 125 MSPS analog-to-digital converter (ADC).
It connects to an FPGA carrier via the FMC LPC connector, enabling data
capture and analysis using standard ADI software tools.

The :adi:`AD9265` is designed to support communications applications where
high performance combined with low cost, small size, and versatility is
desired. The ADC core features a multistage, differential pipelined
architecture with integrated output error correction logic to provide 16-bit
accuracy at 125 MSPS data rates and guarantees no missing codes over the full
operating temperature range. The AD9265 is available in a Pb-free, 48-lead
LFCSP and is specified over the industrial temperature range of −40°C to
+85°C.

Features:

- SNR = 79.0 dBFS @ 70 MHz and 125 MSPS
- SFDR = 93 dBc @ 70 MHz and 125 MSPS
- Low power: 373 mW @ 125 MSPS
- 1.8 V analog supply operation
- 1.8 V CMOS or LVDS output supply
- Integer 1-to-8 input clock divider
- IF sampling frequencies to 300 MHz
- −154.3 dBm/Hz small signal input noise with 200 Ω input impedance @ 70 MHz and 125 MSPS
- Optional on-chip dither for improved SFDR with low power input signals
- Programmable internal ADC voltage reference
- Integrated ADC sample-and-hold inputs
- Flexible analog input range: 1 V p-p to 2 V p-p
- Differential analog inputs with 650 MHz bandwidth
- ADC clock duty cycle stabilizer
- Serial port control (SPI)
- User-configurable, built-in self-test (BIST) capability
- Energy-saving power-down modes
- Pin-compatible with the AD9255 (14-bit)

Applications:

- Multimode digital receivers (3G): GSM, EDGE, W-CDMA, LTE, CDMA2000, WiMAX, TD-SCDMA
- Smart antenna systems
- General-purpose software radios
- Broadband data applications
- Ultrasound equipment

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9265`, we recommend using the
:adi:`EVAL-AD9265` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`eval_ad9265 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`Prerequisites <eval_ad9265 prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guide <eval_ad9265 quickstart>`:

      #. Using the :ref:`ZC706 <eval_ad9265 quickstart zc706>` (FPGA)
      #. Using the :ref:`ZedBoard <eval_ad9265 quickstart zed>` (FPGA)
      #. Using the :ref:`SDP-H1 <eval_ad9265 sdp-h1-evaluation>` (USB)

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :external+scopy:doc:`Scopy <index>`

#. Design with the AD9265

   - :ref:`eval_ad9265 block-diagram`

     - :adi:`AD9265 product page <AD9265>`

   - Resources for designing a custom AD9265-based platform

     #. For Linux software:

        #. About the device driver:

           - :git-linux:`AD9467 Linux IIO ADC driver (also supports AD9265) <drivers/iio/adc/ad9467.c>`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+hdl:ref:`axi_dmac`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

     #. For no-OS software:

        - :external+no-OS:doc:`projects/adc/ad9265-fmc-125ebz`

     #. :external+hdl:ref:`HDL reference design <ad9265_fmc>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _eval_ad9265 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/ad9265-blockdiag.png
   :align: center
   :width: 800

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
