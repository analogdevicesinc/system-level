.. _eval_ad7606x eval:

EVAL-AD7606x
===============================================================================

Overview
-------------------------------------------------------------------------------

.. image:: images/AD7606B-P-TAG-chip-illustration.png
   :align: left
   :width: 200

The :adi:`AD7606` family is an 8-/6-/4-channel simultaneous sampling ADC with
16-bit, bipolar input. Each device includes analog input clamp protection
(±16.5 V tolerance), a second-order antialiasing filter (22 kHz, 3 dB cutoff),
track-and-hold amplifier, 16-bit successive approximation ADC, flexible digital
filter, 2.5 V reference and reference buffer, and high-speed serial/parallel
interfaces. The family operates from a single 2.7 V to 5.25 V supply and
supports ±10 V and ±5 V true bipolar inputs with synchronized sampling at up
to 200 kSPS (300 kSPS for :adi:`AD7605-4`). All devices feature 1 MΩ analog
input impedance regardless of sampling frequency. Single supply operation,
on-chip filtering, and high input impedance eliminate the need for driver
op-amps and external bipolar supplies.

The :adi:`AD7606C` is a direct pin replacement (software and hardware
compatible) for both AD7608 and AD7609, with higher input impedance, extended
temperature range, and additional features including 16/18-bit sample size,
system gain/offset/phase calibration, sensor disconnect detection, lower VDRIVE
operation, diagnostics, additional oversampling ratios, and per-channel analog
input range selection with bipolar differential, bipolar single-ended, and
unipolar single-ended options.

Features:

- Multi-channel simultaneous sampling (8/6/4 channels)
- 16-bit resolution with ±10 V and ±5 V bipolar input ranges
- ±16.5 V input clamp protection and 22 kHz antialiasing filter
- 1 MΩ analog input impedance (independent of sampling rate)
- On-chip 2.5 V reference, flexible digital filter, SPI/parallel interfaces
- Sensor disconnect detection (AD7606B/C) and per-channel range selection
  (AD7606C)

Applications:

- Industrial data acquisition and power monitoring
- Motor control and automotive diagnostics
- Medical instrumentation and laboratory equipment
- Environmental monitoring and FPGA-based systems

.. toctree::
   :hidden:

   Prerequisites <prerequisites>
   ad7606_mbed_iio_application
   quickstart/index
   ad7606c-remotecontrol

.. image:: images/eval-ad7606bfmcz.gif
   :align: center
   :width: 500

Recommendations
-------------------------------------------------------------------------------

To get the most from the :adi:`EVAL-AD7606` evaluation board, we recommend
starting with the :ref:`Prerequisites <eval_ad7606x prerequisites>` to ensure
you have all required hardware and software. Then choose an evaluation approach
that best suits your needs. Each path is independent and provides complete
documentation for that specific workflow.

For questions not covered in the documentation, please visit the 
:ref:`Help and Support <help-and-support>` page or post on the 
:ez:`EngineerZone forums <data_converters/precision_adcs>`.

Table of contents
-------------------------------------------------------------------------------

#. :ref:`Prerequisites <eval_ad7606x prerequisites>` - Required hardware,
   software tools, and evaluation platform options

#. Evaluation approaches

   #. :ref:`IIO Ecosystem Quick Start <ad7606_mbed_iio_application>` - Fast
      evaluation with IIO Oscilloscope and graphical tools (recommended)
   #. :ref:`ZedBoard Quick Start <ad7606x quickstart zed>` - Linux and
      no-OS evaluation on AMD Xilinx ZedBoard (FMC)
   #. No-OS Driver Integration

      - :external+no-OS:doc:`AD7606x No-OS Example <projects/adc/ad7606x-fmc>`
      - :git-no-OS:`AD7606 No-OS Driver <drivers/adc/ad7606>`

   #. :external+linux:doc:`Linux IIO Driver <drivers/iio-adc/ad7606>` -
      Configure and build the Linux IIO driver with DeviceTree support
   #. :ref:`FPGA Prototyping <ad7606_ced1z_fpga>` - Evaluation with the
      CED1Z board and Nios II application
   #. :ref:`Automated Testing <ad7606c_remotecontrol>` - ACE software
      automation for MATLAB/Python scripting

#. HDL reference design

   #. :external+hdl:ref:`AD7606x HDL Project <ad7606x_fmc>` - Complete HDL
      reference design for the EVAL-AD7606x-FMCZ board

#. Device and driver resources

   - :adi:`AD7606 Product Page <en/products/ad7606.html>`
   - :adi:`AD7606B Product Page <en/products/ad7606b.html>`
   - :adi:`AD7606C Product Page <en/products/ad7606b.html>`
   - :adi:`AD7605-4 Product Page <en/products/ad7605-4.html>`
   - :adi:`AD7606-4 Product Page <en/products/ad7606-4.html>`
   - :adi:`AD7606-6 Product Page <en/products/ad7606-6.html>`
   - :git-no-OS:`AD7606 No-OS Driver <drivers/adc/ad7606>`
   - :git-linux:`AD7606 Linux IIO Driver <drivers/iio/adc/ad7606.c>`

#. :ref:`Help and Support <help-and-support>`

Help and support
-------------------------------------------------------------------------------

Please visit the :ref:`Help and Support <help-and-support>` page for
additional resources.
