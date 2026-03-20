Linux Drivers
=============

|IIO| The Linux Industrial I/O (IIO) subsystem is intended to provide support for devices that, in some sense, are analog-to-digital or digital-to-analog converters. Devices that fall into this category are:

-  ADCs - can be used on ADCs ranging from a 1MSPS SoC ADC to >250 MSPS industrial ADCs
-  DACs
-  Accelerometers, gyros, IMUs
-  Capacitance-to-Digital converters (CDCs)
-  Pressure, temperature, and light sensors, etc.
-  RF Transceivers (like the AD9361)

The IIO Divers for the motor control solution require the HDL cores to have a
specified register map. A DMA interface is set up for high speed data transfer
using multiple multiplexed data channels. Below is the list of IIO drivers for
the motor control solution.

+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| IIO DriverName     | Channel  | Description                                                                                                                                                                                            |
+====================+==========+========================================================================================================================================================================================================+
| **ad-mc-adc**      | voltage0 | Not used                                                                                                                                                                                               |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | voltage1 | Motor 1 Ia ADC raw data                                                                                                                                                                                |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | voltage2 | Motor 1 Ib ADC raw data                                                                                                                                                                                |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | voltage3 | Motor 1 VBus ADC raw data                                                                                                                                                                              |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **ad-mc-adc-m2**   | voltage0 | Not used                                                                                                                                                                                               |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | voltage1 | Motor 2 Ia ADC raw data                                                                                                                                                                                |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | voltage2 | Motor 2 Ib ADC raw data                                                                                                                                                                                |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                    | voltage3 | Motor 2 VBus ADC raw data                                                                                                                                                                              |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **ad-mc-speed**    | voltage0 | Motor 1 speed. Number of counts in 10ns units between two motor commutations. In order to display the speed in RPM, the data should be processed by checking the 1/x option and multiply by 25.000.000 |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **ad-mc-speed-m2** | voltage0 | Motor 1 speed. Number of counts in 10ns units between two motor commutations. In order to display the speed in RPM, the data should be processed by checking the 1/x option and multiply by 25.000.000 |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **ad-mc-ctrl**     | Not used |                                                                                                                                                                                                        |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **ad-mc-ctrl-m2**  | Not used |                                                                                                                                                                                                        |
+--------------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Each IIO driver has in the device tree and entry related to the actual driver
and an entry corresponding to the allocated DMA. Below is an example of how the
device tree looks for the motor control IIO drivers.

::

   &fpga_axi {
       ad-mc-speed@40410000 {
           compatible = "xlnx,axi-ad-mc-speed-1.00.a";
           reg = <0x40410000 0x10000>;
           dmas = <&ad_mc_speed_dma 0>;
           dma-names = "ad-mc-speed-dma";
       };
       ad_mc_speed_dma: dma@40510000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40510000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 57 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <32>;
               adi,type = <0>;
           };
       };

       ad-mc-adc@40420000 {
           compatible = "xlnx,axi-ad-mc-adc-1.00.a";
           reg = <0x40420000 0x10000>;
           dmas = <&ad_mc_adc_dma 0>;
           dma-names = "ad-mc-adc-dma";
       };
       ad_mc_adc_dma: dma@40520000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40520000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 54 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <64>;
               adi,type = <0>;
           };
       };

       ad-mc-ctrl@40430000 {
           compatible = "xlnx,axi-ad-mc-ctrl-1.00.a";
           reg = <0x40430000 0x10000>;
           dmas = <&ad_mc_ctrl_dma 0>;
           dma-names = "ad-mc-ctrl-dma";
       };
       ad_mc_ctrl_dma: dma@40530000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40530000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 53 0>;
           clocks = <&clkc 15>;
               dma-channel {
               adi,buswidth = <256>;
               adi,type = <0>;
           };
       };

       ad-mc-speed-m2@40440000 {
           compatible = "xlnx,axi-ad-mc-speed-1.00.a";
           reg = <0x40440000 0x10000>;
           dmas = <&ad_mc_speed_dma_m2 0>;
           dma-names = "ad-mc-speed-dma";
       };
       ad_mc_speed_dma_m2: dma@40540000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40540000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 52 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <32>;
               adi,type = <0>;
           };
       };

       ad-mc-adc-m2@40450000 {
           compatible = "xlnx,axi-ad-mc-adc-1.00.a";
           reg = <0x40450000 0x10000>;
           dmas = <&ad_mc_adc_dma_m2 0>;
           dma-names = "ad-mc-adc-dma";
       };
       ad_mc_adc_dma_m2: dma@40550000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40550000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 36 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <64>;
               adi,type = <0>;
           };
       };

       ad-mc-ctrl-m2@40460000 {
           compatible = "xlnx,axi-ad-mc-ctrl-1.00.a";
           reg = <0x40460000 0x10000>;
           dmas = <&ad_mc_ctrl_dma_m2 0>;
           dma-names = "ad-mc-ctrl-dma";
       };
       ad_mc_ctrl_dma_m2: dma@40560000 {
           compatible = "adi,axi-dmac-1.00.a";
           reg = <0x40560000 0x10000>;
           #dma-cells = <1>;
           interrupts = <0 35 0>;
           clocks = <&clkc 15>;
           dma-channel {
               adi,buswidth = <256>;
               adi,type = <0>;
           };
       };
   };

   &spi0 {
       status = "okay";
       ad2s1210@0 {
           compatible = "ad2s1210";
           reg = <0>;
           spi-cpha;
           spi-max-frequency = <1000000>;
           sample-gpios = <&gpio 86 0>;
           adi,entirely-configuration-mode-enable;
       };
   };

.. |IIO| image:: ../images/iio_logo.png
   :width: 200
