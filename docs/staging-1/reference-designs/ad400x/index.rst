.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad400x

.. _ad400x:

AD40xx/ADAQ4001/ADAQ4003 User Guide
===================================

Introduction
------------

This document describes the No-OS software used to control the AD4003 part and
includes an example of how to initialize a AD4003 part.

Overview
--------

The :adi:`AD4003`/:adi:`AD4007`/:adi:`AD4011`/:adi:`AD4020` are low noise, low
power, high speed, 18-bit, precision successive approximation register (SAR)
analog-to-digital converters (ADCs). The :adi:`AD4003`, :adi:`AD4007`, and
:adi:`AD4011` offer 2 MSPS, 1 MSPS, and 500 kSPS throughputs, respectively. They
incorporate ease of use features that reduce signal chain power consumption,
reduce signal chain complexity, and enable higher channel density. The high-Z
mode, coupled with a long acquisition phase, eliminates the need for a dedicated
high power, high speed ADC driver, thus broadening the range of low power
precision amplifiers that can drive these ADCs directly while still achieving
optimum performance. The input span compression feature enables the ADC driver
amplifier and the ADC to operate off common supply rails without the need for a
negative supply while preserving the full ADC code range. The low serial
peripheral interface (SPI) clock rate requirement reduces the digital
input/output power consumption, broadens processor options, and simplifies the
task of sending data across digital isolation.

The :adi:`ADAQ4003` is an 18-bit precision data acquisition sub-system SiP
design on a laminate that includes the :adi:`AD4003` ADC with a fully
differential driver the ADA4945, a reference buffer (the ADA4807), a precision
resistor iPassive network on a separate die along with discrete capacitors and
resistors. The device solves many design challenges for a wide range of
applications similar to AD400x, yet it still provides the flexibility. It offers
over 75% area savings compared to discrete design (i.e. Increased channel
density and reduced signal chain BOM) and reduces TTM.

Applications
~~~~~~~~~~~~

- Automatic test equipment
- Machine automation
- Medical equipment
- Battery-powered equipment
- Precision data acquisition systems

Supported Devices
-----------------

- :adi:`AD4003`
- :adi:`AD4007`
- :adi:`AD4011`
- :adi:`AD4020`
- :adi:`ADAQ4003`

Evaluation Boards
-----------------

- :adi:`EVAL-AD400x-FMCZ`

HDL Design Description
----------------------

In the
:dokuwiki:`ADI Reference Designs HDL User Guide </resources/fpga/docs/hdl>` can
be found an in-depth presentation and instructions about the HDL design in
general.

The reference design uses the standard
`SPI Engine Framework <https://wiki.analog.com/resources/fpga/peripherals/spi_engine>`__
with an integrated pulse generator, which will provide the required conversion
rate for the ADC.

In order to build the HDL design the user has to go through the following steps:

#. Confirm that you have the right tools (the reference design requires Vivado
   2017.4.1)
#. Clone the HDL GitHub repository (the project is located at
   :git-hdl:`ad40xx_fmc <projects/ad40xx_fmc+>`)
#. Set up the required sampling rate (see caption **Design Configuration**)
#. Build the project (see https://wiki.analog.com/resources/fpga/docs/build)

Design Configuration
~~~~~~~~~~~~~~~~~~~~

The reference design uses an integrated pulse generator to synchronise the
capture events during continuous conversion. The required sampling rate can be
set in :git-hdl:`system_bd.tcl <projects/ad40xx_fmc/zed/system_bd.tcl+>` file to
the required values:

1) Reference clock frequency for SPI interface clock

::

   set spi_clk_ref_frequency 100

2) Device resolution

::

   set adc_resolution 20

3) The targeted sampling rate:

::

   set adc_sampling_rate 1800000

Software Setup
--------------

In order to perform the software setup the user has to go through the following
steps:

#. Confirm that you have the right tools (the reference design requires XSDK)
#. Clone the No-OS GitHub repository (the project is located at
   :git-no-OS:`ad400x-fmcz <projects/ad400x-fmcz+>` )
#. Follow the instructions provided by
   `software_setup <https://wiki.analog.com/resources/fpga/xilinx/software_setup>`__.

No-OS Driver Description
------------------------

The driver has two modes of operation:

- single conversion mode
- offload mmode

In single conversion mode a single sample is read from the ADC, while in offload
mode a buffer is loaded with a user specified number.

To switch between these two modes this define must be modified:

.. code:: c

   #define SPI_ENGINE_OFFLOAD_EXAMPLE  1

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Function
     - Description
   * - ``int32_t ad400x_init(struct ad400x_dev **device, struct ad400x_init_param init_param)``
     - Initialize the device

.. code:: c

   int32_t ad400x_init(struct ad400x_dev **device, struct ad400x_init_param init_param)

.. list-table::

   * - Initialize the device.



.. code:: c

   int32_t ad400x_remove(struct ad400x_dev *dev)

.. list-table::

   * - Free the resources allocated by ad400x_init().



.. code:: c

   int32_t ad400x_spi_reg_read(struct ad400x_dev *dev, uint8_t*reg_data)

.. list-table::

   * - Read register.



.. code:: c

   int32_t ad400x_spi_reg_write(struct ad400x_dev *dev, uint8_t reg_data)

.. list-table::

   * - Write register.



.. code:: c

   int32_t ad400x_spi_single_conversion(struct ad400x_dev *dev, uint32_t*adc_data)

.. list-table::

   * - Read a single sample.

Types Declarations
~~~~~~~~~~~~~~~~~~

.. code:: c

   enum ad400x_supported_dev_ids{
       ID_AD4003,
       ID_AD4007,
       ID_AD4011,
       ID_AD4020,
   };

   struct ad400x_dev {
       /*SPI*/
       spi_desc            *spi_desc;
       /*Device Settings*/
       enum ad400x_supported_dev_ids dev_id;
   };

   struct ad400x_init_param {
       /*SPI*/
       spi_init_param          spi_init;
       /*Device Settings*/
       enum ad400x_supported_dev_ids dev_id;
           uint8_t num_bits;
       bool turbo_mode;
       bool high_z_mode;
       bool span_compression;
       bool en_status_bits;
   };

**HW Platform(s):**

- `ZedBoard <http://zedboard.org/product/zedboard>`__

HDL Downloads
-------------

.. admonition:: Download

   :git-hdl:`projects/pulsar_adc`

No-OS Downloads
---------------

.. admonition:: Download

   :git-no-OS:`drivers/adc/pulsar_adc`
