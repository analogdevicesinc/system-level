.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad9213_dual_ebz

.. _eval-ad9213-dual:

EVAL-AD9213-DUAL
===============================================================================

Dual 12-bit, 10 GSPS RF ADC platform with 20 GSPS interleaving via MCS.

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9213-DUAL-EBZ` platform features two
:adi:`AD9213` single-channel, 12-bit, 10 GSPS radio frequency (RF)
analog-to-digital converters (ADCs) with a JESD204B interface. The
two converters are interleaved to achieve 20 GSPS, using their
built-in multi-chip synchronization (MCS) capability.

The :adi:`ADF4377`, a high-performance, ultra-low jitter, dual-output
integer-N phase-locked loop (PLL) with integrated VCO, drives the interleaving.
The :adi:`LTC6955 <en/products/ltc6955.html>` low jitter fanout clock
buffer and the :adi:`LTC6952 <en/products/ltc6952.html>` JESD204B
clock generation and distribution IC together form a clocking
architecture optimized for multi-channel scalability.

The platform supports direct sampling of L, S, and C bands with up
to 8 GHz of instantaneous bandwidth (IBW) per channel.

Features:

- 20 GSPS sample rate through interleaving supporting up to 8 GHz of
  instantaneous BW
- Multi-chip synchronization (MCS) at 10 GSPS using a scalable reference
  distribution architecture
- Input network supporting a wide analog frequency range DC - 9 GHz
- Compact layout scheme that can be quickly adopted into a customer
  application

Applications:

- Electronic Warfare (EW)
- Electronic Countermeasures (ECM) / Electronic Counter-Countermeasures (ECCM)
- Radar
- Instrumentation
- Multi-channel Wideband Receivers

.. figure:: ./images/ad9213_dual_ebz_board.jpeg
   :alt: Photo of the AD9213-DUAL-EBZ evaluation board
   :align: center
   :width: 600

   AD9213-DUAL-EBZ Evaluation Board

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience.
However, like many things, documentation is never as complete as it should
be. If you have any questions, feel free to ask on our :ez:`/`, but before
that, please make sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <eval-ad9213-dual prerequisites>` - what you need
      to get started
   #. :ref:`Quick start guide <eval-ad9213-dual quickstart>`:

      #. Using the
         :ref:`Intel Stratix 10 SX SoC Development Kit
         <eval-ad9213-dual quickstart stratix10>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :adi:`VisualAnalog <en/resources/interactive-design-tools/visualanalog.html>`

#. Design with the AD9213

   - :adi:`AD9213 <en/products/ad9213.html>` product page

   - Resources for designing a custom AD9213-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`AXI ADC HDL Linux driver <axi-adc-hdl>`
           - :external+linux:ref:`AXI-DMAC DMA Controller Linux driver
             <axi-dmac>`
           - :external+linux:ref:`AXI_ADXCVR High-speed transceivers
             Linux driver <axi_adxcvr>`
           - :external+linux:ref:`JESD204B Receive Linux driver
             <axi_jesd204_rx>`

        #. About the JESD204 utilities:

           - :external+linux:ref:`JESD204 (FSM) interface Linux Kernel
             framework <jesd204-fsm-framework>`

#. :ref:`Help and support <eval-ad9213-dual help-and-support>`

.. _eval-ad9213-dual help-and-support:

Help and support
-------------------------------------------------------------------------------

If you have any questions regarding the :adi:`EVAL-AD9213-DUAL-EBZ` or are
experiencing any problems while using it or while following
any of the :ref:`AD9213-DUAL-EBZ user guides <eval-ad9213-dual quickstart>`
feel free to ask us a question. Questions can be asked on our
:ez:`EngineerZone support community </>`.

For questions regarding the AD9213-DUAL-EBZ hardware or the HDL reference
design, please use the
:ez:`FPGA Reference Designs <community/fpga>` sub-community.
For questions regarding the Linux drivers for any of the components on the
AD9213-DUAL-EBZ, please use the
:ez:`Linux Software Drivers
<community/linux-device-drivers/linux-software-drivers>` sub-community.

For questions regarding the
:adi:`AD9213 <en/products/ad9213.html>` ADC, please use the
:ez:`Data Converters <community/data_converters>` sub-community.
For questions regarding the
:adi:`ADF4377 <en/products/adf4377.html>` Clock, please use the
:ez:`Clock and Timing <community/clock_and_timing>` sub-community.

When asking a question, please take the time to give a detailed description
of your problem. Always include on which platform you are currently using
the :adi:`EVAL-AD9213-DUAL-EBZ`. If you are experiencing a problem,
please state the steps you have executed, the result you expected to get,
and the result you actually got. By doing so you enable us to provide you
precise and detailed answers in a timely manner.

Before asking questions, please also take the time to check if somebody else
already asked the same question and already got an answer.

For more information also check:

- `VITA's FMC info <http://www.vita.com/fmc>`_

Warning
-------------------------------------------------------------------------------

.. esd-warning::
