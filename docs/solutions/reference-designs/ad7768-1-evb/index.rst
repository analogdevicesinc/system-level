.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad7768-1

.. _ad77681:

EVAL-AD7768-1FMCZ & EVAL-ADAQ7768-1FMC1Z
===============================================================================

Single-Channel, 24-Bit, Simultaneous Sampling Σ-Δ ADC.

.. image:: images/ad77681_chip.png
   :align: left
   :width: 150

.. image:: images/adaq77681_chip.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD7768-1` is a full-featured evaluation board for the
:adi:`AD7768-1`, a 24-bit, 256 kSPS, single-channel, simultaneous sampling
Σ-Δ ADC. It supports PC-based control via the EVAL-SDP-CH1Z board and enables
time and frequency domain analysis (waveforms, histograms, noise). Standalone
operation is also supported.

The :adi:`EVAL-ADAQ7768-1` demonstrates the :adi:`ADAQ7768-1`, a 24-bit,
single-channel precision μModule® DAQ system featuring onboard power
management, gain selection (switch or GPIO), an FMC digital interface to FPGA,
and optional Arduino/PMOD headers.

Both devices target precision data acquisition with flexible digital filters and
three configurable power/performance modes suitable for a wide range of AC and
DC measurements.

Features:

- 24-bit resolution with 108.5 dB dynamic range (FIR, 256 kSPS)
- Three power modes: Fast, Median, and Low Power
- Flexible digital filter options: FIR, sinc5, sinc3 (50 Hz/60 Hz rejection)
- SPI-compatible serial interface with CRC error checking
- FMC LPC connector for FPGA carrier interface

Applications:

- Precision data acquisition and instrumentation
- Industrial monitoring and control
- Vibration and acoustic analysis
- Power quality and grid monitoring

.. figure:: images/eval_ad77681_top_view.jpg
   :align: center
   :width: 500

   EVAL-AD7768-1FMCZ

.. figure:: images/eval_adaq77681_top_view.jpg
   :align: center
   :width: 500

   EVAL-ADAQ7768-1FMC1Z

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

To better understand the :adi:`AD7768-1` / :adi:`ADAQ7768-1`, we recommend to
use the :adi:`EVAL-AD7768-1` / :adi:`EVAL-ADAQ7768-1` evaluation boards.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad77681 user-guide` - what you need to know about the evaluation
      board
   #. :ref:`Prerequisites <ad77681 prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guides <ad77681 quickstart>`:

      #. Using the :ref:`ZedBoard <ad77681 quickstart zed>` (FPGA)
      #. Using the :ref:`AD7768-1 on SDP-K1 <ad77681 quickstart ad77681_sdp_k1>` (SDP)
      #. Using the :ref:`ADAQ7768-1 on SDP-H1 <ad77681 quickstart adaq77681_sdp_h1>` (SDP)

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :external+scopy:doc:`Scopy <index>`

#. Design with the AD7768-1/ADAQ7768-1

   - :ref:`ad77681/adaq77681 block-diagrams`

     - :adi:`AD7768-1 product page <AD7768-1>`
     - :adi:`ADAQ7768-1 product page <ADAQ7768-1>`

   - Resources for designing a custom AD7768-1/ADAQ7768-1-based platform

     #. For Linux software:

        #. About the device driver:

           - :external+linux:doc:`AD7768-1 Linux IIO ADC driver <drivers/iio-adc/ad7768-1>`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dmac`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

     #. For no-OS software:

        - :external+no-OS:doc:`projects/adc/ad7768-1fmcz`

     #. :external+hdl:ref:`HDL reference design <ad77681evb>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _ad77681/adaq77681 block-diagrams:

Block diagrams
-------------------------------------------------------------------------------

EVAL-AD7768-1FMCZ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/ad77681_block_diag.png
   :align: center
   :width: 800

EVAL-ADAQ7768-1FMC1Z
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/adaq77681_block_diag.png
   :align: center
   :width: 800

Videos
-------------------------------------------------------------------------------

- :adi:`ADAQ7768-1 Quick Guide <resources/media-center/videos/6331869818112.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
