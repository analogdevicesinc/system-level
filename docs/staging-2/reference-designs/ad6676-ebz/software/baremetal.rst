.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad6676-ebz/software/baremetal

.. _ad6676-ebz software baremetal:

AD6676-EBZ Bare Metal Quick Start Guide
=======================================

Downloads
---------

.. admonition:: Download

   No-OS:

   - AD6676-EBZ Main Driver -
     :git-no-OS:`no-OS/tree/main/projects/ad6676-ebz <tree/main/projects/ad6676-ebz+>`
   - Xilinx Platform Drivers -
     :git-no-OS:`no-OS/tree/main/legacy/common_drivers/platform_drivers <tree/main/legacy/common_drivers/platform_drivers+>`
   - AD6676 Driver -
     :git-no-OS:`no-OS/tree/main/drivers/adc/ad6676 <tree/main/drivers/adc/ad6676+>`
   - ADC Core Driver -
     :git-no-OS:`no-OS/tree/main/legacy/common_drivers/adc_core <tree/main/legacy/common_drivers/adc_core+>`
   - DMAC Core Driver -
     :git-no-OS:`no-OS/tree/main/legacy/common_drivers/dmac_core <tree/main/legacy/common_drivers/dmac_core+>`
   - JESD204B Core Driver -
     :git-no-OS:`no-OS/tree/main/legacy/common_drivers/jesd_core <tree/main/legacy/common_drivers/jesd_core+>`
   - Transceiver Core Driver -
     :git-no-OS:`no-OS/tree/main/legacy/common_drivers/xcvr_core <tree/main/legacy/common_drivers/xcvr_core+>`
   - Transceiver Modules Drivers -
     :git-no-OS:`no-OS/tree/main/legacy/common_drivers/xcvr_core/xcvr_modules <tree/main/legacy/common_drivers/xcvr_core/xcvr_modules+>`

   HDL project:

   - AD6676EVB HDL project -
     :git-hdl:`hdl/tree/main/projects/ad6676evb <tree/main/projects/ad6676evb+>`
   - AD6676EVB HDL project documentation -
     https://analogdevicesinc.github.io/hdl/projects/ad6676evb/index.html

AD6676 Driver Description
-------------------------

Functions Declarations
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Function
     - Description
   * - ``int32_t ad6676_spi_read(struct ad6676_dev *dev, uint16_t reg_addr, uint8_t*reg_data);``
     - SPI read from device.

\|

.. code:: c

   int32_t ad6676_spi_read(struct ad6676_dev *dev, uint16_t reg_addr, uint8_t*reg_data);

.. list-table::

   * - SPI read from device.

\|

.. code:: c

   int32_t ad6676_spi_write(struct ad6676_dev *dev, uint16_t reg_addr, uint8_t reg_data);

.. list-table::

   * - SPI write to device.

\|

.. code:: c

   static int32_t ad6676_set_splitreg(struct ad6676_dev *dev, uint32_t reg, uint32_t val);

.. list-table::

   * - SPI write a 16 bit register as two consecutive registers, LSB first.

\|

.. code:: c

   static inline int32_t ad6676_get_splitreg(struct ad6676_dev *dev, uint32_t reg, uint32_t*val);

.. list-table::

   * - SPI read from a 16 bit register as two consecutive registers, LSB first.

\|

.. code:: c

   static int32_t ad6676_set_fadc(struct ad6676_dev *dev, uint32_t val);

.. list-table::

   * - Set ADC clock frequency.

\|

.. code:: c

   static inline uint32_t ad6676_get_fadc(struct ad6676_dev *dev);

.. list-table::

   * - Get the ADC clock frequency.

\|

.. code:: c

   int32_t ad6676_set_fif(struct ad6676_dev *dev, struct ad6676_init_param*init_param);

.. list-table::

   * - Set the target IF frequency.

\|

.. code:: c

   uint64_t ad6676_get_fif(struct ad6676_dev *dev, struct ad6676_init_param*init_param);

.. list-table::

   * - Get the target IF frequency.

\|

.. code:: c

   static int32_t ad6676_set_bw(struct ad6676_dev *dev, uint32_t val);

.. list-table::

   * - Set the target BW frequency.

\|

.. code:: c

   static inline uint32_t ad6676_get_bw(struct ad6676_dev *dev);

.. list-table::

   * - Get the target BW frequency.

\|

.. code:: c

   static int32_t ad6676_set_decimation(struct ad6676_dev *dev, struct ad6676_init_param*init_param);

.. list-table::

   * - Set decimation factor in the decimation mode register.

\|

.. code:: c

   static int32_t ad6676_set_clk_synth(struct ad6676_dev *dev, uint32_t refin_Hz, uint32_t freq);

.. list-table::

   * - Set the clock synthesizer to generate a specific frequency using a given
       refrence clock and do VCO and CP calibration.

\|

.. code:: c

   static int32_t ad6676_set_extclk_cntl(struct ad6676_dev *dev, uint32_t freq);

.. list-table::

   * - Enable external clock for the ADC.

\|

.. code:: c

   static int32_t ad6676_jesd_setup(struct ad6676_dev *dev, struct ad6676_init_param*init_param);

.. list-table::

   * - Setup JESD204 link parameters.

\|

.. code:: c

   int32_t ad6676_shuffle_setup(struct ad6676_dev *dev, struct ad6676_init_param*init_param);

.. list-table::

   * - Setup shuffling rate and threshold for the adaptive shuffler.

\|

.. code:: c

   static int32_t ad6676_calibrate(struct ad6676_dev *dev, uint32_t cal);

.. list-table::

   * - Do internal calibration of JESD, ADC or flash.

\|

.. code:: c

   static int32_t ad6676_reset(struct ad6676_dev *dev, uint8_t spi3wire);

.. list-table::

   * - Software reset all SPI registers to default value.

\|

.. code:: c

   static int32_t ad6676_outputmode_set(struct ad6676_dev *dev, uint32_t mode);

.. list-table::

   * - Set output mode as twos complement or straight binary.

\|

.. code:: c

   int32_t ad6676_set_attenuation(struct ad6676_dev *dev, struct ad6676_init_param*init_param);

.. list-table::

   * - Set attenuation in decibels or disable attenuator.

\|

.. code:: c

   int32_t ad6676_setup(struct ad6676_dev **device, struct ad6676_init_param init_param);

.. list-table::

   * - Initialize the device.

\|

.. code:: c

   int32_t ad6676_update(struct ad6676_dev *dev, struct ad6676_init_param*init_param);

.. list-table::

   * - Reconfigure device for other target frequency and bandwidth and
       recalibrate.

\|

.. code:: c

   int32_t ad6676_test(struct ad6676_dev *dev, uint32_t test_mode);

.. list-table::

   * - Perform an interface test.

Make
----

.. todo:: .. include: /resources/fpga/no-os_make/software_setup.rst

GUI
---

.. todo:: .. include: /resources/fpga/xilinx/software_setup.rst
