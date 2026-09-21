.. _ad_fmcmotcon2_ebz controller-board:

AD-FMCMOTCON2-EBZ Controller Board
===============================================================================

Features
-------------------------------------------------------------------------------

- Compatible with all AMD Xilinx FPGA platforms with FMC LPC or HPC connectors
- Digital board for interfacing with the low and high voltage drive boards
- FMC signals voltage adaptation interface for seamless operation on all FMC
  voltage levels
- Fully isolated digital control and feedback signals

  - 2 isolated GPOs
  - 2 isolated GPIs
  - 18 isolated drive signals - can drive 2 bridges with 4 legs simultaneously
  - 6 high speed ADC digital interfaces (data + clock)

- Isolated AMD Xilinx XADC interface
- 2x Gbit Ethernet PHYs for high speed industrial communication - RGMII mode
- Single ended Hall + Differential Hall + Encoder + Resolver interfaces

  - 2x single ended HALL, 2x differential HALL, 2x encoder interfaces - allows
    2 motors to be driven simultaneously

- Digital sensors interfaces

  - EnDat
  - BISS Interface

Block Diagram
-------------------------------------------------------------------------------

.. figure:: ../images/controller_block_diagram_simplified.jpg
   :alt: AD-FMCMOTCON2-EBZ simplified block diagram
   :align: center
   :width: 500

   Simplified block diagram

Picture and Main Components
-------------------------------------------------------------------------------

.. figure:: ../images/ad-fmcmotcon2-ebz_top_parts.jpg
   :alt: AD-FMCMOTCON2-EBZ top side
   :align: center
   :width: 600

   AD-FMCMOTCON2-EBZ top side

.. figure:: ../images/ad-fmcmotcon2-ebz_bottom_parts.jpg
   :alt: AD-FMCMOTCON2-EBZ bottom side
   :align: center
   :width: 600

   AD-FMCMOTCON2-EBZ bottom side

Key Parts
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Part
     - Description
   * - **Measurement**
     -
   * - :adi:`AD8137`
     - Differential ADC driver
   * - :adi:`AD8646`
     - 24 MHz rail-to-rail dual op amp
   * - :adi:`AD2S1210`
     - Variable resolution, 10-bit to 16-bit R/D converter with reference
       oscillator
   * - **Power**
     -
   * - :adi:`ADuM5000`
     - isoPower® integrated isolated dc-to-dc converter
   * - :adi:`ADP1614`
     - 1000 mA, 2.5 MHz buck-boost dc-to-dc converter
   * - **Isolation**
     -
   * - :adi:`ADuM7640/ADuM7641 <ADuM7640>`
     - 1 kV RMS six-channel digital isolator
   * - :adi:`ADuM1400/ADuM1402 <ADuM1400>`
     - Quad channel digital isolator
   * - :adi:`ADM2486`
     - Isolated RS485 transceiver
   * - :adi:`ADuM1250`
     - Hot swappable dual I2C isolator
   * - **Voltage Translation**
     -
   * - :adi:`ADG3308`
     - 8-channel bidirectional level translator
   * - **Multiplexers**
     -
   * - :adi:`ADG759`
     - CMOS low voltage, 3 ohms 4-channel multiplexer
   * - **Communication**
     -
   * - :adi:`ADN4662`
     - Single, 3V, CMOS, LVDS differential line receiver
   * - **88E1512**
     - Marvell Integrated 10/100/1000 Mbps Energy Efficient Ethernet
       Transceiver

ADC FPGA Interface
-------------------------------------------------------------------------------

The :adi:`AD7403` Isolated Sigma-Delta Modulators present on the controller
board have a 2-wire signal interface with the FPGA:

- 10 / 20 MHz clock input
- 1-bit digital data stream output

The reconstruction of the data provided by the :adi:`AD7403` modulator can be
done using a SINC3 filter. A filter model and HDL implementation are provided
in the AD7403 datasheet. Typical filter output characteristics:

- Output code: 16 bit
- Sampling rate: 78 kHz

The output code resolution and sampling rate can be controlled by changing the
filter model and decimation. Polyphase interpolation filters are utilized to
increase the sampling rate of the system.