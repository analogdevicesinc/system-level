.. _eval-ad9083:

EVAL-AD9083
===============================================================================

16-Channel, 125 MHz Bandwidth, Continuous Time Σ-Δ ADC.

.. image:: images/ad9083_chip.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9083` is an FMC evaluation card for the :adi:`AD9083`, a
16-channel, 125 MHz bandwidth, continuous time Σ-Δ (CTSD) ADC. The device
features an on-chip, programmable, single-pole antialiasing filter and
termination resistor designed for low power, small size, and ease of use.

Each of the 16 ADC cores features a first-order CTSD modulator architecture
with integrated, background nonlinearity correction logic and self-cancelling
dither. Each ADC has a signal processing tile to filter out-of-band shaped
noise and reduce the sample rate, containing a cascaded integrator comb (CIC)
filter and a quadrature digital downconverter (DDC) with multiple finite input
response (FIR) decimation filters.

The serialized output uses a Subclass 1 JESD204B interface configurable in
various lane configurations (up to four lanes). Multiple device synchronization
is supported through the SYSREF±, TRIG±, and SYNCINB± input pins.

Features:

- 16-channel, 125 MHz bandwidth CTSD ADC
- Programmable single-pole antialiasing filter
- Programmable input termination resistor
- Integrated background nonlinearity correction and self-cancelling dither
- Signal processing tile per channel: CIC filter + quadrature DDC + FIR
- JESD204B interface, up to 4 lanes (Subclass 1)
- Multiple device synchronization (SYSREF±, TRIG±, SYNCINB±)
- 1.8 V SPI (3-wire) configuration interface
- Flexible power-down modes
- 100-ball CSP_BGA, −40°C to +85°C

Applications:

- Multi-channel instrumentation and data acquisition
- Phased array radar and electronic warfare
- Test and measurement equipment
- Communications receivers
- Medical imaging

:adi:`EVAL-AD9083` looks like this:

.. image:: images/eval-ad9083.jpg
   :align: center
   :width: 400

.. toctree::
   :hidden:

   prerequisites
   user-guide
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9083`, we recommend using the
:adi:`EVAL-AD9083` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <eval-ad9083 prerequisites>` — what you need to get started
   #. :ref:`Quick start guides <eval-ad9083 quickstart>`:

      #. Using the :ref:`ZCU102/Zynq UltraScale+ MP SoC <eval-ad9083 quickstart zcu102>`

   #. :ref:`User Guide <eval-ad9083 user-guide>`
   #. :ref:`ACE Evaluation Guide <eval-ad9083 quickstart ads8-v3ebz>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD9083

   - :adi:`AD9083 product page <AD9083>`

   - Resources for designing a custom AD9083-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+hdl:ref:`axi_jesd204_rx`
           - :external+hdl:ref:`axi_adxcvr`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+hdl:ref:`axi_dmac`
           - :external+linux:ref:`ad9083`

        #. About the JESD204 utilities:

           - :external+linux:ref:`jesd204-fsm-framework`
           - :doc:`JESD204 status utility </software/jesd/jesd_status>`
           - :external+hdl:ref:`jesd204`

     #. :external+hdl:ref:`HDL reference design <ad9083_evb>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad9083 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/ad9083_block_diagram.png
   :align: center
   :width: 500

ADI articles
-------------------------------------------------------------------------------

About the JESD204 standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
