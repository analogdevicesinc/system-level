.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad738x

.. _ad738x:

AD738x - No-OS Driver
=====================

Supported Devices
-----------------

- :adi:`AD7380`
- :adi:`AD7381`
- :adi:`AD7383`
- :adi:`AD7384`
- :adi:`AD7386`
- :adi:`AD7387`
- :adi:`AD7388`
- :adi:`AD4680`
- :adi:`AD4681`
- :adi:`AD4682`
- :adi:`AD4683`
- :adi:`AD4684`
- :adi:`AD4685`

Evaluation Boards
-----------------

- :adi:`EVAL-AD7380FMCZ`
- :adi:`EVAL-AD7381FMCZ`
- :adi:`EVAL-AD7386FMCZ`
- :adi:`EVAL-AD7383FMCZ`
- :adi:`EVAL-AD7380-4FMCZ`

Overview
--------

The AD7380 family of generics are dual and quad 16-bit, 14-bit, and 12-bit
pin-compatible family of simultaneous sampling, high speed, low power,
successive approximation analog-to-digital converters (ADC) that operate from a
3.3 V power supply and features throughput rates up to 4 MSPS. The analog input
type is differential for the :adi:`AD7380`, :adi:`AD7381`, :adi:`AD4680`,
:adi:`AD4681`, :adi:`AD7380-4`, :adi:`AD7389-4`, :adi:`AD7381-4` can accept a
wide common mode input voltage, and are sampled and converted on the falling
edge of CS. The :adi:`AD7383`, :adi:`AD7384`, :adi:`AD4682` and :adi:`AD4683`
have the pseudo-differential input while the :adi:`AD7386`, :adi:`AD7387`,
:adi:`AD7388`, :adi:`AD4684` and :adi:`AD4685` have single-ended input. The
AD7380 family has optional integrated on-chip oversampling blocks to improve
dynamic range and reduce noise at lower bandwidths. An internal 2.5 V reference
is included.

Alternatively, an external reference up to 3.3 V can be used. The conversion
process and data acquisition use standard control inputs allowing for easy
interfacing to microprocessors or DSPs. It is compatible with 1.8 V, 2.5 V, and
3.3 V interfaces, using a separate logic supply.

The dual :adi:`AD7380`, :adi:`AD7381`, :adi:`AD4680`, :adi:`AD4681`,
:adi:`AD7383`,\ :adi:`AD7384`, :adi:`AD4682`, :adi:`AD4683`, :adi:`AD7386`,
:adi:`AD7387`, :adi:`AD7388`, :adi:`AD4684` and :adi:`AD4685` family are
available in a 16-lead 3mm x 3mm LFCSP package while the quad generics
:adi:`AD7380-4`, :adi:`AD7389-4`, and :adi:`AD7381-4` are available in 4mmx4mm
LFCSP package. Both the duals and quad generic operate in specified from −40°C
to +125°C temperature range.

Applications
~~~~~~~~~~~~

- Motor control position feedback
- Motor control current sense
- Data acquisition systems
- EDFA applications
- I and Q demodulation
- SONAR
- Power Quality

HDL Design Description
----------------------

In the
:dokuwiki:`ADI Reference Designs HDL User Guide </resources/fpga/docs/hdl>` can
be found an in-depth presentation and instructions about the HDL design in
general.

The reference design uses the standard :external+hdl:ref:`spi_engine` with an
integrated pulse generator, which will provide the required conversion rate for
the ADC.

In order to build the HDL design the user has to go through the following steps:

#. Confirm that you have the right tools (the reference design requires Vivado
   2018.3)
#. Clone the HDL GitHub repository (the project is located at
   :git-hdl:`ad738x_fmc <projects/ad738x_fmc+>`)
#. Build the project (see https://wiki.analog.com/resources/fpga/docs/build)

Software Setup
--------------

In order to perform the software setup the user has to go through the following
steps:

#. Confirm that you have the right tools (the reference design requires XSDK)
#. Clone the No-OS GitHub repository (the project is located at
   :git-no-OS:`ad738x-fmcz <projects/ad738x_fmcz+>` )
#. Follow the instructions provided by
   :dokuwiki:`software_setup </resources/fpga/xilinx/software_setup>`.

No-OS Driver Description
------------------------

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Function
     - Description
   * - See code below
     - See function descriptions in the code section

.. code:: c

   int32_t ad738x_init(ad738x_dev **device, ad738x_init_param init_param)

.. list-table::

   * - Initialize the device.



.. code:: c

   int32_t ad738x_remove(ad738x_dev *dev)

.. list-table::

   * - Free the resources allocated by ad738x_init().



.. code:: c

   int32_t ad738x_reference_sel(ad738x_dev *dev, ad738x_ref_sel ref_sel)

.. list-table::

   * - Enable internal or external reference.



.. code:: c

   int32_t ad738x_power_down_mode(ad738x_dev *dev, ad738x_pwd_mode pmode)

.. list-table::

   * - Device power down.



.. code:: c

   int32_t ad738x_oversampling_config(ad738x_dev *dev, ad738x_os_mode os_mode, ad738x_os_ratio os_ratio, ad738x_resolution res)

.. list-table::

   * - Sets the oversampling mode in the device (os_mode). Sets the oversampling
       ratio (osr). Sets the size of the conversion result data (res)



.. code:: c

   int32_t ad738x_reset(ad738x_dev *dev, ad738x_reset_type reset)

.. list-table::

   * - Device reset over SPI.



.. code:: c

   int32_t ad738x_set_conversion_mode(ad738x_dev *dev, ad738x_conv_mode mode)

.. list-table::

   * - Select if ADC A and ADC B output on both SDOA and SDOB lines (two wire
       mode) or only on on the SDOA line.



.. code:: c

   int32_t ad738x_spi_single_conversion(ad738x_dev *dev, uint16_t*adc_data)

.. list-table::

   * - Read conversion result from device.



.. code:: c

   int32_t ad738x_spi_write_mask(ad738x_dev *dev, uint8_t reg_addr, uint32_t mask, uint16_t data)

.. list-table::

   * - SPI write to device using a mask.



.. code:: c

   int32_t ad738x_spi_reg_write(ad738x_dev *dev, uint8_t reg_addr, uint16_t reg_data)

.. list-table::

   * - Write to device.



.. code:: c

   int32_t ad738x_spi_reg_read(ad738x_dev *dev, uint8_t reg_addr, uint16_t*reg_data)

.. list-table::

   * - Read from device.

Types Declarations
~~~~~~~~~~~~~~~~~~

.. code:: c

   typedef enum {
       TWO_WIRE_MODE,
       ONE_WIRE_MODE
   } ad738x_conv_mode;

   typedef enum {
       NORMAL_OS_MODE,
       ROLLING_OS_MODE
   } ad738x_os_mode;

   typedef enum {
       OSR_DISABLED,
       OSR_X2,
       OSR_X4,
       OSR_X8,
       OSR_X16,
       OSR_X32,
   } ad738x_os_ratio;

   typedef enum {
       RES_16_BIT,
       RES_18_BIT
   } ad738x_resolution;

   typedef enum {
       SOFT_RESET,
       HARD_RESET
   } ad738x_reset_type;

   typedef enum {
       NORMAL_PWDM,
       FULL_PWDM
   } ad738x_pwd_mode;

   typedef enum {
       INT_REF,
       EXT_REF
   } ad738x_ref_sel;

   typedef struct {
           /*SPI*/
           spi_desc            *spi_desc;
           /*Device Settings*/
           ad738x_conv_mode    conv_mode;
       ad738x_resolution   resolution;
   } ad738x_dev;

   typedef struct {
           /*SPI*/
           spi_init_param          spi_init;
           /*Device Settings*/
           ad738x_conv_mode        conv_mode;
           ad738x_ref_sel          ref_sel;
   } ad738x_init_param;


HDL Downloads
-------------

.. admonition:: Download

   :git-hdl:`projects/ad738x_fmc`

No-OS Downloads
---------------

.. admonition:: Download

   :git-no-OS:`ad738x No-OS Project <projects/ad738x_fmcz>`
