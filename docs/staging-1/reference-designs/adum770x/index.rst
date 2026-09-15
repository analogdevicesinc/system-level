.. imported from: https://wiki.analog.com/resources/eval/user-guides/adum770x

.. _adum770x:

ADuM7701 - Reference Design
===========================

Supported Devices
-----------------

- :adi:`ADuM7701`
- :adi:`AD7405`
- :adi:`AD7403`

Supported Carrier Board
~~~~~~~~~~~~~~~~~~~~~~~

- `Zedboard <http://zedboard.org/product/zedboard>`__

Overview
--------

The :adi:`ADuM7701` is a high performance, second-order, Σ-Δ modulator that
converts an analog input signal into a high speed, single-bit data stream, with
on-chip digital isolation based on Analog Devices, Inc., iCoupler® technology.
The device operates from a 4.5 V to 5.5 V power supply range (VDD1) and accepts
a pseudo differential input signal of ±250 mV (±320 mV full-scale). The pseudo
differential input is ideally suited to shunt voltage monitoring in high voltage
applications where galvanic isolation is required.

The analog input is continuously sampled by a high performance analog modulator
and converted to a ones density digital output stream with a data rate of up to
21 MHz. The original information can be reconstructed with an appropriate sinc3
digital filter to achieve an 86 dB signal-to-noise ratio (SNR) at 78.1 kSPS with
a 256 decimation rate and a 20 MHz master clock. The serial input and output
operates from a 5 V or a 3 V supply (VDD2).

The serial interface is digitally isolated. High speed complementary metal-oxide
semiconductor (CMOS) technology, combined with monolithic transformer
technology, results in the on-chip isolation providing outstanding performance
characteristics, superior to alternatives such as optocoupler devices. The
:adi:`ADuM7701` device is available in both a 16-lead and an 8-lead wide-body
SOIC and has an operating temperature range of −40°C to +125°C.

Applications
~~~~~~~~~~~~

- Shunt current monitoring
- AC motor controls
- Power and solar inverters
- Wind turbine inverters
- Analog-to-digital and optoisolator replacements

HDL Reference Design
--------------------

The provided HDL reference design support"s both the ADuM7701 and AD7405
devices. One of the main difference between thees two devices is the type of the
digital data lines. In case of ADuM7701 it is a single ended lines, and in case
of the AD7405 is differential.

User can configure the corresponding interface type, by setting the
**adc_port_type** Tcl variable in the system_project.tcl file. Note that this
variable should be set before generating any bit file.

The output of the device is a continuous digital bit stream, to reconstruct the original input signal information, this output bit stream needs to be digitally filtered and decimated. A simple .. figure:: :git-hdl:`library/common/util_dec256sinc24b.v`

   is recommended to reconstruct the original input signal information received
   from the ADuM7701. The following equation describes the transfer function of
   the sinc filter:

<m>H(z) = (1/DR (1-Z^-DR)/(1 - Z^-1))^N</m>

where **DR** is the decimation rate and **N** is the sinc filter order. The
implemented filter is a 3rd order sinc filter.

The output of the filter is connected to a DMA, which will handle the data
transfer into the system memory. See the data path in block diagram bellow:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7405_data_path_1.png

The external clock rate (MCLKIN) can be set in the system_bd.tcl file, by
changing the value of the **ext_clk_rate** variable.

Create the project with SDK
---------------------------

.. todo:: .. include: /resources/fpga/xilinx/software_setup.rst

Driver Description
------------------

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Function
     - Description
   * - ``int32_t adum7701_init(adum7701_dev **dev, adum7701_init_param init_param)``
     - Initialize the device

.. code:: c

   int32_t adum7701_init(adum7701_dev **dev, adum7701_init_param init_param);

.. list-table::

   * - Initialize the device.



.. code:: c

   int32_t adum7701_remove(adum7701_dev *dev);

.. list-table::

   * - Free the resources allocated by adum7701_init().

Types Declarations
~~~~~~~~~~~~~~~~~~



.. code:: c

   typedef struct {
           /*GPIO*/
           gpio_desc *dec_ratio;
           gpio_desc *filter_reset;
   } adum7701_dev;

   typedef struct {
           /*GPIO*/
           gpio_init_param dec_ratio;
           gpio_init_param filter_reset;
   } adum7701_init_param;



Downloads
---------

.. admonition:: Download

   | :git-no-OS:`adum7701_fmc/adum7701.c`
   | :git-no-OS:`adum7701_fmc/adum7701.h`
   | :git-no-OS:`adum7701_fmc`
   | :git-hdl:`adum7701:/`
