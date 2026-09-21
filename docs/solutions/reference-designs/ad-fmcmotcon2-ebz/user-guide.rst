.. _ad_fmcmotcon2_ebz user-guide:

User guide
===============================================================================

.. _ad_fmcmotcon2_ebz hardware-guide:

Hardware guide
-------------------------------------------------------------------------------

The motor control system consists of three boards that work together.

.. figure:: images/mc2_ctrl_single.jpg
   :alt: AD-FMCMOTCON2-EBZ controller board
   :align: center
   :width: 400

   AD-FMCMOTCON2-EBZ

:ref:`AD-FMCMOTCON2-EBZ <ad_fmcmotcon2_ebz controller-board>` - Controller
board, compatible with all AMD Xilinx FPGA platforms with FMC LPC or HPC
connectors.

- 2x Gbit Ethernet PHYs for high-speed industrial communication (RGMII)
- Hall, Differential Hall, Encoder, and Resolver interfaces
- EnDat and BISS digital sensor interfaces
- Current and voltage measurement using isolated ADCs (:adi:`AD7403`)
- Fully isolated control and feedback signals
- AMD Xilinx XADC interface

.. figure:: images/mc2_lv_single.jpg
   :alt: AD-DRVLV2-EBZ low voltage drive board
   :align: center
   :width: 400

   AD-DRVLV2-EBZ

:ref:`AD-DRVLV2-EBZ <ad_fmcmotcon2_ebz lv-board>` - Low voltage drive board.
Connects to the Controller board with a power stage that drives Brushed DC /
BLDC / PMSM / Stepper motors up to 48 V and 20 A.

- Drives 2 motors simultaneously with independent power supplies
- Integrated over-current and reverse voltage protection
- Current and voltage measurement using isolated ADCs
- BEMF zero-crossing detection for sensorless control

.. figure:: images/mc2_dyno_single.jpg
   :alt: AD-DYNO2-EBZ dynamometer drive system
   :align: center
   :width: 400

   AD-DYNO2-EBZ

:ref:`AD-DYNO2-EBZ <ad_fmcmotcon2_ebz dyno>` - Dynamometer drive system
(optional). An electronically adjustable load for testing real-time motor
control performance.

- Two BLDC motors connected in a dyno setup
- Electronically adjustable load via onboard buttons and LCD
- Programmable step and ramp load changes
- Measurement and display of load motor phase currents and speed
- External control via header P1

Additional hardware documentation:

- :ref:`Signal measurement chain <ad_fmcmotcon2_ebz signal-chain>` - Ia/Ib
  and Vbus measurement chains with :adi:`AD7403` isolated ΣΔ modulators and
  Sallen Key reconstruction filters; includes formulas for converting raw ADC
  codes to physical values.
- :ref:`Test procedure <ad_fmcmotcon2_ebz test>` - Step-by-step procedure
  for FRU EEPROM programming, EtherCAT EEPROM, AD2S1210, and dyno functional
  testing.

.. _ad_fmcmotcon2_ebz software-guide:

Software guide
-------------------------------------------------------------------------------

.. _ad_fmcmotcon2_ebz hdl:

AMD Xilinx HDL Reference Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The reference design targets the
`ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`_
and includes complete Linux infrastructure. The reference design contains HDL
blocks for interfacing with the various components of the motor control
hardware:

- **Current Monitor** - Implements communication with the :adi:`AD7401`
  sigma-delta modulators on the AD-FMCMOTCON2-EBZ, including the SINC3
  filters for demodulating the 1-bit digital stream. Exposes AXI-Lite
  registers and a DMA interface for real-time data streaming to the
  application layer. An ADC PACK IP enables 1, 2, or all channels to stream
  data simultaneously.
- **Controller** - Implements the interface to the IP control blocks in the
  system. A DMA interface allows real-time data streaming. Implements a basic
  six-point drive of the motor. An ADC PACK block enables 1, 2, 4, or all
  channels to stream data.
- **Speed Detector** - Implements the algorithm for converting Hall, BEMF,
  and Encoder signals into speed and position data. Exposes AXI-Lite registers
  and a DMA interface.
- **GMII to RGMII** - Converts the GMII interface from the two Ethernet cores
  in the PS7 block to the RGMII interface on the FMC Controller Board. Allows
  RX pins on different I/O banks.
- **I2C** - Two I2C interfaces connected to the FMC board.

.. figure:: images/motorcontrolrev2.jpg
   :alt: Vivado reference design block diagram
   :align: center
   :width: 800

   Vivado reference design block diagram

To build the project, follow the instructions from the
:external+hdl:ref:`ADI Reference Designs HDL User Guide <user_guide>`.

Linux software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The software suite for Linux consists of:

- :external+kuiper:doc:`Kuiper Linux <index>` - includes IIO subsystem drivers
  for the motor control solution (see driver table below).
- :ref:`iio-oscilloscope` - graphical monitoring and control of the motor
  drive system.

.. _ad_fmcmotcon2_ebz linux-drivers:

IIO drivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Linux Industrial I/O (IIO) subsystem provides support for devices that
in some sense are analog-to-digital or digital-to-analog converters.

The IIO drivers for the motor control solution require the HDL cores to have a
specified register map. A DMA interface is set up for high-speed data transfer
using multiple multiplexed data channels.

.. list-table::
   :header-rows: 1

   * - IIO Driver
     - Channel
     - Description
   * - ``ad-mc-adc``
     - voltage0
     - Not used
   * -
     - voltage1
     - Motor 1 Ia ADC raw data
   * -
     - voltage2
     - Motor 1 Ib ADC raw data
   * -
     - voltage3
     - Motor 1 VBus ADC raw data
   * - ``ad-mc-adc-m2``
     - voltage0
     - Not used
   * -
     - voltage1
     - Motor 2 Ia ADC raw data
   * -
     - voltage2
     - Motor 2 Ib ADC raw data
   * -
     - voltage3
     - Motor 2 VBus ADC raw data
   * - ``ad-mc-speed``
     - voltage0
     - Motor 1 speed. Number of counts in 10 ns units between two motor
       commutations. To display speed in RPM, enable the **1/x** option and
       multiply by 25,000,000.
   * - ``ad-mc-speed-m2``
     - voltage0
     - Motor 2 speed. Same scaling as ad-mc-speed.
   * - ``ad-mc-ctrl``
     - Not used
     -
   * - ``ad-mc-ctrl-m2``
     - Not used
     -

Each IIO driver has a device tree entry for the actual driver and an entry for
the allocated DMA:

.. code-block::

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

.. _ad_fmcmotcon2_ebz iio-scope:

IIO Oscilloscope
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The :ref:`iio-oscilloscope` is used for monitoring and controlling the
AD-FMCMOTCON2-EBZ board when running Linux. It has two main sections:
**Capture** for signal monitoring and **Motor Control** for manual control.

**Signals monitoring (Capture)**

The IIO Oscilloscope allows monitoring of current, voltage, speed, and control
signals from the system.

.. list-table::
   :header-rows: 1

   * - Group
     - Channel
     - Description
   * - ``ad-mc-adc``
     - voltage0
     - Not used
   * -
     - voltage1
     - Motor 1 Ia ADC raw data
   * -
     - voltage2
     - Motor 1 Ib ADC raw data
   * -
     - voltage3
     - Motor 1 VBus ADC raw data
   * - ``ad-mc-adc-m2``
     - voltage0
     - Not used
   * -
     - voltage1
     - Motor 2 Ia ADC raw data
   * -
     - voltage2
     - Motor 2 Ib ADC raw data
   * -
     - voltage3
     - Motor 2 VBus ADC raw data
   * - ``ad-mc-speed``
     - voltage0
     - Motor 1 speed. Enable **1/x** and multiply by 25,000,000 to get RPM.
   * - ``ad-mc-speed-m2``
     - voltage0
     - Motor 2 speed. Same scaling as ad-mc-speed.
   * - ``ad-mc-ctrl``
     - Not used
     -
   * - ``ad-mc-ctrl-m2``
     - Not used
     -

.. figure:: images/mc_iio_signals.jpg
   :alt: IIO Oscilloscope signals monitoring
   :align: center
   :width: 600

   IIO Oscilloscope signals monitoring

**Manual Control (Motor Control tab)**

This dialog allows manual control of the two motors by directly specifying the
fill factor of the PWM signals applied to control the 3-phase inverters. The
motors are driven using a 6-step commutation algorithm.

.. figure:: images/mc_manual_ctrl.jpg
   :alt: Manual control interface
   :align: center
   :width: 400

   Manual control interface

.. list-table::
   :header-rows: 1

   * - Control
     - Description
   * - Run
     - Starts the motor
   * - Delta
     - Selects between Star-like and Delta commutation sequence
   * - Direction
     - Selects between clockwise and counterclockwise rotation
   * - PWM
     - In Manual mode, settable between 50%–100%

.. _ad_fmcmotcon2_ebz qdesys-ip:

QDESYS Motor Control IP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`QDESYS <https://qdesys.com/>`_ provides the following reference designs
for the AD-FMCMOTCON2-EBZ:

- EtherCAT design showing how to perform real-time motor control over the
  network
- A high-performance Field Oriented Controller (FOC) - the FOC algorithm is
  provided as a highly optimized IP that can be integrated into the FPGA
  project

Screenshots from the user application taken while running with the
AD-FMCMOTCON2-EBZ:

.. figure:: images/qdesys_main_panel.jpg
   :alt: QDESYS main panel
   :align: center
   :width: 400

   QDESYS main panel

.. figure:: images/qdesys_pwm_panel.jpg
   :alt: QDESYS PWM control panel
   :align: center
   :width: 400

   QDESYS PWM control panel

.. figure:: images/qdesys_current_settings.jpg
   :alt: QDESYS current settings panel
   :align: center
   :width: 400

   QDESYS current settings panel

.. figure:: images/qdesys_rpfm_panel.jpg
   :alt: QDESYS RPFM control panel
   :align: center
   :width: 400

   QDESYS RPFM control panel

.. figure:: images/qdesys_currents.jpg
   :alt: QDESYS phase currents plot
   :align: center
   :width: 400

   QDESYS phase currents plot

.. figure:: images/qdesys_currents_xy.jpg
   :alt: QDESYS stator currents vs space plot
   :align: center
   :width: 400

   QDESYS stator currents vs space plot

.. toctree::
   :hidden:

   reference/controller_board
   reference/lv_board
   reference/signal_chain
   reference/dyno
   reference/test
