.. _eval-ad5529r-ardz:

EVAL-AD5529R-ARDZ
===============================================================================

16-Channel, 16-Bit Voltage Output DAC Evaluation Board

.. TODO:: Add product photo (eval-ad5529r-ardz-angle.png)


.. code-block:: rst

   .. figure:: images/eval-ad5529r-ardz-angle.png
      :align: center

      EVAL-AD5529R-ARDZ Evaluation Board

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD5529R-ARDZ <EVAL-AD5529R-ARDZ>` is an evaluation board for the
:adi:`AD5529R`, a 16-channel, 16-bit voltage output digital-to-analog converter
(DAC) with industry-leading specifications.

The evaluation board connects to a Cora Z7-07S FPGA development board via
Arduino-compatible headers. Kuiper Linux runs on the Zynq-7000 SoC and exposes
the DAC channels through the IIO subsystem, enabling control with standard
IIO tools.

Features:

- 16 independent voltage output channels
- 16-bit resolution
- ±1 LSB INL (integral nonlinearity)
- ±25 mA output current capability
- SPI interface (up to 35 MHz SCLK)
- Hardware toggle pins (TG0-TG3) for synchronized updates
- LDAC for simultaneous channel updates

Applications:

- Industrial automation and process control
- Automated test equipment (ATE)
- Arbitrary waveform generation
- Precision voltage source
- Multi-channel control systems

.. toctree::
   :glob:
   :hidden:

   prerequisites
   user-guide
   */index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete
as it should be. If you have any questions, feel free to ask on our
:ez:`EngineerZone </>`, but before that, please make sure you read our
documentation thoroughly.

To better understand the AD5529R, we recommend using the
:adi:`EVAL-AD5529R-ARDZ` evaluation board together with the
`Cora Z7-07S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development/>`_
FPGA development board.

Table of Contents
-------------------------------------------------------------------------------

#. Using the evaluation board / full stack reference design:

   #. :ref:`Prerequisites <eval-ad5529r-ardz prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guide <eval-ad5529r-ardz quickstart>`:

      #. Using the :ref:`Cora Z7-07S <eval-ad5529r-ardz quickstart cora-z7>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD5529R

   #. :ref:`eval-ad5529r-ardz block-diagram`

      #. :adi:`AD5529R Product Page <AD5529R>`
      #. :adi:`AD5529R Datasheet <media/en/technical-documentation/data-sheets/AD5529R.pdf>`

   #. Resources for designing a custom AD5529R-based platform:

      #. Linux software:

         #. :git-linux:`AD5529R Linux Driver <main:drivers/iio/dac/ad5529r.c>`
         #. :external+linux:ref:`axi-dmac`

      #. :external+hdl:ref:`HDL reference design <ad5529r_ardz>` which
         you must use in your FPGA.

      #. No-OS driver (planned):

         #. :git-no-OS:`AD5529R no-OS driver <drivers/dac/ad552xr>`

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad5529r-ardz block-diagram:

Block Diagram
-------------------------------------------------------------------------------

.. figure:: images/ad5529_bd.png
   :align: center

   AD5529R Block Diagram

The AD5529R integrates 16 DAC channels with individual output buffers, a
precision internal voltage reference, and a flexible SPI interface supporting
both single and daisy-chain configurations.

.. _eval-ad5529r-ardz hdl-architecture:

HDL Architecture
-------------------------------------------------------------------------------

.. figure:: images/ad5529_coraz7s_hdl.lfs.svg
   :align: center

   AD5529R HDL Reference Design Block Diagram

The HDL reference design uses the ADI SPI Engine framework for high-throughput
DAC streaming:

- **SPI Engine**: 16-bit data width, offload with streaming enabled
- **AXI DMA**: Memory-to-stream for continuous waveform playback
- **PWM Generators**: Trigger (SPI transactions) + Toggle pins (TG0-TG3)
- **Clock Generator**: 140 MHz reference for 35 MHz SCLK

Warning
-------------------------------------------------------------------------------

.. esd-warning::
