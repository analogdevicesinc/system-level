.. _eval ltc23xx:

EVAL-LTC23XX
===============================================================================

Low noise, high speed SAR ADC family - 16/18/20-bit, up to 2 MSPS.

Overview
-------------------------------------------------------------------------------

The LTC23xx family consists of low noise, low power, high speed successive
approximation register (SAR) ADCs with resolutions of 16-bit, 18-bit, and
20-bit and maximum sampling rates from 250 kSPS to 2 MSPS. Operating from a
2.5V or 5V supply, these ADCs feature either fully differential or
pseudo-differential input configurations with VREF ranging from 2.5V to 5.1V.

The :adi:`LTC2338-18` is a special variant operating from a single 5V supply
with a ±10.24V true bipolar input range, making it ideal for high voltage
applications requiring a wide dynamic range.

All devices in the family feature a high-speed SPI-compatible serial interface
that supports 1.8V, 2.5V, 3.3V, and 5V logic while also featuring a
daisy-chain mode. The fast throughput with no cycle latency makes the LTC23xx
family ideally suited for a wide variety of high-speed applications. An
internal oscillator sets the conversion time, easing external timing
considerations. The devices automatically power down between conversions,
leading to reduced power dissipation that scales with the sampling rate.

Several variants - including the :adi:`LTC2376`, :adi:`LTC2377`,
:adi:`LTC2378`, :adi:`LTC2379`, and :adi:`LTC2380` series - feature a
unique digital gain compression (DGC) function.
When enabled, DGC maps zero-scale code from 0V to 0.1 x VREF and full-scale
code from VREF to 0.9 x VREF, eliminating the driver amplifier's negative
supply while preserving the full ADC resolution.

Features:

- 16-bit, 18-bit, and 20-bit resolution options
- Up to 2 MSPS throughput with no cycle latency
- Low power: 21 mW at 1 MSPS, scales proportionally with sample rate
- 104 dB SNR (typ) at f\ :sub:`IN` = 2 kHz (:adi:`LTC2378-20`)
- -125 dB THD (typ) at f\ :sub:`IN` = 2 kHz (:adi:`LTC2378-20`)
- ±2 ppm INL maximum, guaranteed no missing codes at 20 bits
- Digital gain compression (DGC) on selected variants
- Fully differential or pseudo-differential input configurations
- VREF range: 2.5V to 5.1V
- SPI-compatible serial interface with daisy-chain mode
- 1.8V to 5V I/O voltages
- Internal conversion clock
- 16-lead MSOP and 4 mm x 3 mm DFN packages

Applications:

- Medical imaging
- High-speed data acquisition
- Portable or compact instrumentation
- Industrial process control
- Low power battery-operated instrumentation
- ATE

.. figure:: ./images/ltc2378-20_eval_board.jpeg
   :alt: Photo of the LTC2378-20 FMC evaluation board
   :align: center
   :width: 800

   LTC2378-20 FMC Evaluation Board

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

To better understand the LTC23xx family, we recommend using the evaluation
board with the `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
FPGA development kit for Linux-based evaluation. For no-OS, you can use a
demonstration board.

.. important::

   This guide focuses on :adi:`LTC2378-20` with the `ZedBoard
   <https://digilent.com/reference/programmable-logic/zedboard/start>`__ for
   Linux (the primary and most supported path) and the :adi:`DC2135A` with the
   :adi:`MAX32666FTHR` for no-OS. The setup applies to all other supported
   devices as they share the same FMC connector and pin-compatible interface.

People who follow the flow outlined in this documentation have a much better
experience. If you have any questions, feel free to ask on our :ez:`/`, but
please read the documentation thoroughly first.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full-stack reference design:

   #. :ref:`Prerequisites <eval ltc23xx prerequisites>` - what you need
      to get started
   #. :ref:`Quick start guides <eval ltc23xx quickstart>`:

      #. Using the
         :ref:`ZedBoard with Linux <eval ltc23xx quickstart zed>`
      #. Using the
         :ref:`DC2135A with no-OS <eval ltc23xx quickstart dc2135a>`

   #. Linux applications:

      #. :ref:`iio-oscilloscope`

#. Design with the LTC23xx family:

   - :adi:`LTC2378-20` product page

   - Resources for designing a custom LTC23xx-based platform:

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dmac`

        #. About the SPI Engine framework:

           - :external+hdl:ref:`spi_engine`

     #. :external+hdl:ref:`ltc2378_fmc` for the
        ZedBoard.

#. :ref:`Help and Support <help-and-support>`

Supported devices
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 10 40

   * - Device
     - Resolution
     - Max Rate
     - Supply
     - Notes
   * - :adi:`LTC2380-16`
     - 16-bit
     - 2 MSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2379-18`
     - 18-bit
     - 2 MSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2370-16`
     - 16-bit
     - 2 MSPS
     - 2.5V
     - Pseudo-differential unipolar
   * - :adi:`LTC2378-20`
     - 20-bit
     - 1 MSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2378-18`
     - 18-bit
     - 1 MSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2378-16`
     - 16-bit
     - 1 MSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2338-18`
     - 18-bit
     - 1 MSPS
     - 5V
     - ±10.24V true bipolar input
   * - :adi:`LTC2377-20`
     - 20-bit
     - 500 kSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2377-18`
     - 18-bit
     - 500 kSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2377-16`
     - 16-bit
     - 500 kSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2369-18`
     - 18-bit
     - 500 kSPS
     - 2.5V
     - Pseudo-differential
   * - :adi:`LTC2367-18`
     - 18-bit
     - 500 kSPS
     - 2.5V
     - Pseudo-differential
   * - :adi:`LTC2367-16`
     - 16-bit
     - 500 kSPS
     - 2.5V
     - Pseudo-differential
   * - :adi:`LTC2376-20`
     - 20-bit
     - 250 kSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2376-18`
     - 18-bit
     - 250 kSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2376-16`
     - 16-bit
     - 250 kSPS
     - 2.5V
     - DGC, fully differential
   * - :adi:`LTC2368-18`
     - 18-bit
     - 250 kSPS
     - 2.5V
     - Pseudo-differential
   * - :adi:`LTC2368-16`
     - 16-bit
     - 250 kSPS
     - 2.5V
     - Pseudo-differential
   * - :adi:`LTC2364-18`
     - 18-bit
     - 250 kSPS
     - 2.5V
     - Pseudo-differential
   * - :adi:`LTC2364-16`
     - 16-bit
     - 250 kSPS
     - 2.5V
     - Pseudo-differential

Warning
-------------------------------------------------------------------------------

.. esd-warning::
