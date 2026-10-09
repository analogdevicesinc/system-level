.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad9213_evb

.. _ad9213 evb:

EVAL-AD9213
===============================================================================

12-Bit, 6 GSPS/10.25 GSPS, JESD204B, RF Analog-to-Digital Converter.

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9213` is the evaluation board for the
:adi:`AD9213`, a single, 12-bit, 6 GSPS/10.25 GSPS radio frequency (RF)
analog-to-digital converter (ADC). The :adi:`AD9213` supports high
dynamic range frequency and time domain applications requiring wide
instantaneous bandwidth and low conversion error rates. It features a
16-lane JESD204B interface to support maximum bandwidth capability.

Its integrated input buffer supports up to 6.5 GHz of input bandwidth and
on-chip calibration and dithering preserve linearity and spurious-free
performance across a wide range of signal conditions. A built-in digital
downconverter (DDC) lets you tune to a specific frequency band and reduce
the output data rate when full instantaneous bandwidth is not needed.

The evaluation board interfaces with an FPGA carrier via an FMC+ connector,
using the AMD Xilinx :xilinx:`VCU118` as the main supported platform, while
the :adi:`ADS8-V1EBZ` capture board is also supported (limited).

Features:

- High instantaneous dynamic range with low noise
- Low power dissipation: <4.6 W typical at 10 GSPS
- Wide 6.5 GHz input bandwidth with integrated input buffer
- Overvoltage-protected analog input
- 16-lane JESD204B output interface (up to 16 Gbps line rate)
- Multichip synchronization with 1 sample accuracy,
  including DDC NCO synchronization
- Integrated digital downconverter (DDC) with selectable decimation
- Fast frequency hopping via 48-bit NCO with 16 profile settings
- Fast overrange detection for efficient AGC
- On-chip temperature sensor and negative voltage generators
- Low conversion error rate (CER)
- Compact 12 mm × 12 mm, 192-ball BGA-ED package

Applications:

- Wideband radar and electronic warfare (EW)
- Test and measurement instrumentation
- Wideband communications receivers
- Direct RF sampling systems

.. figure:: ./images/eval_ad9213.jpeg
   :alt: Photo of the EVAL-AD9213 evaluation board
   :align: center
   :width: 800

   EVAL-AD9213 Evaluation Board

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
:ez:`/`, but before that, please
make sure you read our documentation thoroughly.

To better understand the :adi:`AD9213`, we recommend using the
:adi:`EVAL-AD9213` evaluation board together with the
AMD Xilinx :xilinx:`VCU118` FPGA development kit or the
:adi:`ADS8-V1EBZ` FPGA-based capture board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <ad9213 evb prerequisites>` - what you need to
      get started
   #. :ref:`Quick start guides <ad9213 evb quickstart>`:

      #. Using the :ref:`AMD Xilinx VCU118/UltraScale+ <ad9213 evb quickstart vcu118>`
      #. Using the :ref:`ADS8-V1EBZ with the EVAL-AD9213 or EVAL-AD9217 <ad9213 evb quickstart ads8-v1ebz_ad9213_ad9217>`
      #. Using the :ref:`ADS8-V1EBZ with the AD9213-10GEBZ-B <ad9213 evb quickstart ads8-v1ebz_ad9213-10gebz-b>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD9213

   - :ref:`ad9213 evb block-diagram`

     - :adi:`AD9213` product page

   - Resources for designing a custom AD9213-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`AXI ADC HDL Linux driver <axi-adc-hdl>`
           - :external+linux:ref:`AXI-DMAC DMA Controller Linux driver <axi-dmac>`
           - :external+linux:ref:`axi_adxcvr`
           - :external+linux:ref:`axi_jesd204_rx`

        #. About the JESD204 utilities:

           - :external+linux:ref:`jesd204-fsm-framework`

     #. :external+hdl:ref:`HDL reference design <ad9213_evb>` which you
        must use in your FPGA.

        - :external+hdl:ref:`jesd204`

#. :ref:`Help and Support <help-and-support>`

.. _ad9213 evb block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: ./images/ad9213_block_diagram.jpeg
   :alt: Block diagram showing the AD9213 signal chain from RF input to FPGA
   :align: center
   :width: 800

   AD9213 Block Diagram

ADI articles
-------------------------------------------------------------------------------

About the JESD204 standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
