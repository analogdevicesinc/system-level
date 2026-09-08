.. _eval_ad717x:

AD717x/AD411x
===============================================================================

Precision Sigma-Delta ADC family for high-resolution, low-noise measurement.

Overview
-------------------------------------------------------------------------------

.. image:: images/ad4111-chip-illustration.png
   :width: 200
   :align: left

The :adi:`AD717x <en/lp/001/ad717x-family.html>`/:adi:`AD411x <en/products/ad4111.html>`
family comprises integrated Sigma-Delta ADCs designed for precision
measurement applications. These devices support both single-channel
configurations for high-precision, low-noise measurements and multiplexed
setups for higher-speed applications such as factory automation PLC input
modules.

The family offers output data rates from 5 SPS to 250 kSPS with channel
scan rates up to 50 kSPS per channel, and up to 24 noise-free bits of
resolution at lower data rates. True rail-to-rail analog and reference
input buffers, an on-chip 2.5 V reference with ±2 ppm/°C drift, and an
INL of ±1 ppm of FSR make these devices well suited for life science
measurements and any application requiring high precision near DC signals.

Supported Devices:

- :adi:`AD4111`
- :adi:`AD4112`
- :adi:`AD4113`
- :adi:`AD4114`
- :adi:`AD4115`
- :adi:`AD4116`
- :adi:`AD7172-2`
- :adi:`AD7172-4`
- :adi:`AD7173-8`
- :adi:`AD7175-2`
- :adi:`AD7175-8`
- :adi:`AD7176-2`
- :adi:`AD7177-2`

Supported Evaluation Boards:

- :adi:`EVAL-AD4111SDZ`
- :adi:`EVAL-AD4112SDZ`
- :adi:`EVAL-AD4113SDZ`
- :adi:`EVAL-AD4114SDZ`
- :adi:`EVAL-AD4115SDZ`
- :adi:`EVAL-AD7172-4SDZ`
- :adi:`EVAL-AD7172-2SDZ`
- :adi:`EVAL-AD7173-8SDZ`
- :adi:`EVAL-AD7173-8ARDZ`
- :adi:`EVAL-AD7175-2SDZ`
- :adi:`EVAL-AD7175-8`
- :adi:`EVAL-AD7175-8ARDZ`
- :adi:`EVAL-AD7177-2SDZ`

Features:

- Output data rates from 5 SPS to 250 kSPS
- Up to 24 noise-free bits of resolution
- True rail-to-rail analog and reference input buffers
- On-chip 2.5 V reference (±2 ppm/°C)
- INL of ±1 ppm of FSR
- 85 dB rejection of 50/60 Hz interference
- SPI-compatible serial interface

Applications:

- Life science / precision near-DC measurements
- Factory automation PLC input modules
- Data acquisition systems
- Process control

.. toctree::
   :hidden:

   user-guide-ad717x
   user-guide-ad411x
   eval-ad7175-2sdz
   prerequisites
   interposer
   ad7175_mcu_driver
   ad7176_mcu_driver
   ace

.. quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete
as it should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please
make sure you read our documentation thoroughly.

Table of Contents
-------------------------------------------------------------------------------

#. **Getting Started with the Evaluation Board**

   #. :ref:`ad717x-user-guide` - AD717x hardware user guide
   #. :ref:`ad411x-user-guide` - AD411x hardware user guide
   #. :ref:`eval-ad7175-2sdz` - Evaluating the AD7175-2
   #. :ref:`prerequisites` - required hardware and software

#. **Reference Designs**

   #. :ref:`interposer` - FMC-SDP Interposer & Xilinx KC705
   #. :ref:`ad7175-mcu-driver` - AD7175-2 microcontroller
      no-OS driver (Renesas RL78G13)
   #. :ref:`ad7176-mcu-driver` - AD7176-2 microcontroller
      no-OS driver (Renesas RL78G13)
   #. :external+hdl:doc:`AD411x/AD717x HDL Reference Design <projects/ad411x_ad717x/index>`

.. #. **Quickstarts**
..
..    #. :ref:`quickstart` - FPGA quickstarts

#. **Evaluation Software**

   #. :ref:`ace` - ACE software installation and operation

#. **Software Applications**

   #. :external+precision-converters-firmware:doc:`AD717x Console Application <source/projects/ad717x_console/ad717x_console>`
   #. :external+precision-converters-firmware:doc:`AD717x IIO Application <source/projects/ad717x_iio/ad717x_iio>`
   #. :external+no-OS:doc:`AD717x No-OS Driver <drivers/adc/ad717x>`
   #. :external+linux:doc:`AD7173 Linux IIO Driver <drivers/iio-adc/ad7173>`

#. **Product Resources**

   #. :adi:`AD717x Family Page <en/lp/001/ad717x-family.html>`
   #. :adi:`AD4111 Product Page <AD4111>`

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
