.. _pluto devs controlling_gpios:

Controlling GPIOs on the ADALM-PLUTO
======================================

Available GPIOs
----------------

Source is the Rev D schematic (see the
:ref:`hardware revisions <pluto hacking hardware revision-d>` page for how to
obtain it).

The user can select the Programmable Logic GPIO operation through the
``phaser_enable`` software-controlled pin.

The ``phaser_enable`` pin defaults to 0, selecting the Pluto functionality. If
set to 1, the GPIOs switch to Phaser functionality.

Programmable Logic (PL)
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Zynq 7010 Pin
     - Zynq Pin Name
     - Schematic Net
     - PCB Test Point
     - Pluto Functionality
     - Phaser Functionality
   * - K13
     - IO_L10P_T1_34
     - PL_GPIO0
     - L10P
     - SPI MOSI
     - TXDATA
   * - M12
     - IO_L12N_T1_MRCC_34
     - PL_GPIO1
     - L12N
     - SPI MISO
     - BURST
   * - R10
     - IO_L24N_T3_34
     - PL_GPIO2
     - L24N
     - SPI CLKO
     - MUXOUT
   * - N14
     - IO_L7N_T1_34
     - PL_GPIO3
     - L7N
     - IIC SDA
     - IIC SDA
   * - M14
     - IO_L9N_T1_DQS_34
     - PL_GPIO4
     - L9N
     - IIC SCL
     - IIC SCL

Processor System (PS)
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Zynq 7010 Pin
     - Zynq Pin Name
     - Schematic Net
     - PCB Test Point
   * - D8
     - PS_MIO0_500
     - PS_GPIO0
     - MIO0
   * - B10
     - PS_MIO11_500
     - PS_GPIO1
     - MIO10
   * - D6
     - PS_MIO10_500
     - PS_GPIO2
     - MIO11
   * - B5
     - PS_MIO9_500
     - PS_GPIO3
     - MIO09
   * - C13
     - PS_MIO53_501
     - PS_GPIO4
     - MIO53
   * - D13
     - PS_MIO49_501
     - PS_GPIO5
     - MIO49
   * - B12
     - PS_MIO48_501
     - PS_GPIO6
     - MIO48
