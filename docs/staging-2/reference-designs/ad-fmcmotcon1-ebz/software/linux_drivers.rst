.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/linux_drivers

.. _ad-fmcmotcon1-ebz software linux_drivers:

Linux Drivers
=============

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-retired
   :end-before: .. end-retired

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/software/iio_logo.png
   :width: 200px

The Linux Industrial I/O (IIO) subsystem is intended to provide support for
devices that, in some sense, are analog-to-digital or digital-to-analog
converters. Devices that fall into this category are:

- ADCs - can be used on ADCs ranging from a 1MSPS SoC ADC to >250 MSPS
  industrial ADCs
- DACs
- Accelerometers, gyros, IMUs
- Capacitance-to-Digital converters (CDCs)
- Pressure, temperature, and light sensors, etc.
- RF Transceivers (like the AD9361)

The IIO Divers for the motor control solution require the HDL cores to have a
specified register map. A DMA interface is set up for high speed data transfer
using multiple multiplexed data channels. Below is the list of IIO drivers for
the motor control solution.

.. list-table::
   :header-rows: 1

   * - IIO DriverName
     - Description
     - Channels
   * - **ad-mc-adc**
     - Driver for the controller board ADCs
     - CH1 - Ia measurement
       CH2 - Ib measurement
       CH3 - It measurement
       CH4 - Vbus measurement
   * - **ad-mc-adc2**
     - Driver for the low voltage drive board ADCs
     - CH1 - Ia measurement
       CH2 - Ib measurement
       CH3 - It measurement
   * - **ad-mc-speed**
     - Driver for the speed and position processing block
     - CH1 - Speed measurement
   * - **ad-mc-ctrl**
     - Driver for the motor controller block
     - CH1 : CH8 - Controller monitoring signals

Each IIO driver has in the device tree and entry related to the actual driver
and an entry corresponding to the allocated DMA. Below is an example of how the
device tree looks for the motor control IIO drivers.

::

   ad-mc-adc@40500000 {
       compatible = "xlnx,axi-ad-mc-adc-1.00.a";
       reg = <0x40500000 0x10000>;
       dmas = <&axi_dma_0 0>;
       dma-names = "ad-mc-adc-dma";
   };

   axi_dma_1: axidma1@40420000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x40420000 0x10000>;
       #dma-cells = <1>;
       interrupts = <0 54 0>;
       clocks = <&clkc 16>;

       dma-channel {
           adi,buswidth = <32>;
           adi,type = <0>;
       };
   };

   ad-mc-ctrl@40520000 {
       compatible = "xlnx,axi-ad-mc-ctrl-1.00.a";
       reg = <0x40520000 0x10000>;
       dmas = <&axi_dma_1 0>;
       dma-names = "ad-mc-ctrl-dma";
   };

   axi_dma_2: axidma2@40410000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x40410000 0x10000>;
       #dma-cells = <1>;
       interrupts = <0 56 0>;
       clocks = <&clkc 16>;

       dma-channel {
           adi,buswidth = <32>;
           adi,type = <0>;
       };
   };

   ad-mc-speed@40510000 {
       compatible = "xlnx,axi-ad-mc-speed-1.00.a";
       reg = <0x40510000 0x10000>;
       dmas = <&axi_dma_2 0>;
       dma-names = "ad-mc-speed-dma";
   };

   axi_dma_3: axidma3@40430000 {
       compatible = "adi,axi-dmac-1.00.a";
       reg = <0x40430000 0x10000>;
       #dma-cells = <1>;
       interrupts = <0 53 0>;
       clocks = <&clkc 16>;

       dma-channel {
           adi,buswidth = <64>;
           adi,type = <0>;
       };
   };

   ad-mc-adc2@40530000 {
       compatible = "xlnx,axi-ad-mc-adc-1.00.a";
       reg = <0x40530000 0x10000>;
       dmas = <&axi_dma_3 0>;
       dma-names = "ad-mc-adc-dma";
   };
