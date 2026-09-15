.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0584

.. _circuits-from-the-lab cn0584:

CN0584 User Guide
=================

| .. important::

   We are in the process of migrating our documentation to GitHub Pages.
   | The latest version of this document can be found at https://analogdevicesinc.github.io/documentation/solutions/reference-designs/eval-cn0584-ebz/index.html

Overview
--------

CN0584 (Low Latency Development Kit) is a development platform consisting of two
boards the :adi:`EVAL-CN0585-FMCZ <CN0585>` and the
:adi:`EVAL-CN0584-EBZ <CN0584>`. :adi:`EVAL-CN0585-FMCZ <CN0585>` consists of 4
x 16-bit ADC channels and 4 x 16-bit DAC channels that are interfaced with an
FPGA through the FMC Low Pin Count (LPC) Connector. Current revision of
:adi:`EVAL-CN0585-FMCZ <CN0585>` is Rev B. :adi:`EVAL-CN0584-EBZ <CN0584>` is
the application specific analog front end (AFE) board.CN0584 is connected to a
Zedboard to build a development system setup like shown in Figure 7.

The Low Latency Development Kit (LLDK) provides a complete data acquisition and
signal generation platform with on-board power rails, voltage monitoring, logic
level translation, general purpose I/O, I2C, SPI, and a personality interface
connector.

The key performance benefit of the LLDK system is the ability to perform a
complete capture and conversion of precision analog input data in <70ns with the
ADC module and generate a settled full-scale analog output in <200ns from
initial data written to the DAC.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/eval-cn0585-fmcz_kit_angle.jpg
   :width: 600px

   Figure 1. Low Latency Development Kit

Connections and Configurations
------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/hil_cn0584_personalityboard_top-web.jpg
   :width: 600px

   Figure 2. EVAL-CN0584-EBZ Board

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/cn0584.png
   :width: 400px

   Figure 3.Simplified Block Diagram of LLDK

ADC Inputs
~~~~~~~~~~

There are four channels of differential input signals on
:adi:`EVAL-CN0584-EBZ <CN0584>`.

.. list-table::
   :header-rows: 1

   * - Channel
     - Positive Input Signal
     - Negative Input Signal
   * - Channel 0
     - J1
     - J2
   * - Channel 1
     - J3
     - J4
   * - Channel 2
     - J5
     - J6
   * - Channel 3
     - J7
     - J8

*Table 1. ADC Input Signal Connectors*

ADC Input Range Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

LLDK has configurable input voltage ranges of ±10 V(Default), ±5 V, ±4.096 V,
±2.5 V, and ±1.5 V. The input range can be changed by modifying resistor
placements on :adi:`EVAL-CN0584-EBZ <CN0584>` as described in Table 2.

.. list-table::
   :header-rows: 1

   * - Channel
     - Input Voltage Range
     - AFE Board Modification
   * - Channel 0
     - ±10 V (default)
     - Include R19A, R21A, R22A, R24A; DNI R18A, R20A, R23A, R25A
   * -
     - ±5 V
     - Include R18A, R20A, R23A, R25A; DNI R19A, R21A, R22A, R24A
   * -
     - ±4.096 V
     - Include R19A, R21A; DNI R18A, R20A, R22A, R23A, R24A, R25A
   * -
     - ±2.5 V
     - Include R18A, R20A; DNI R19A, R21A, R22A, R23A, R24A, R25A
   * -
     - ±1.5 V
     - Include R18A, R19A, R20A, R21A; DNI R22A, R23A, R24A, R25A
   * - Channel 1
     - ±10 V (default)
     - Include R19B, R21B, R22B, R24B; DNI R18B, R20B, R23B, R25B
   * -
     - ±5 V
     - Include R18B, R20B, R23B, R25B; DNI R19B, R21B, R22B, R24B
   * -
     - ±4.096 V
     - Include R19B, R21B; DNI R18B, R20B, R22B, R23B, R24B, R25B
   * -
     - ±2.5 V
     - Include R18B, R20B; DNI R19B, R21B, R22B, R23B, R24B, R25B
   * -
     - ±1.5 V
     - Include R18B, R19B, R20B, R21B; DNI R22B, R23B, R24B, R25B
   * - Channel 2
     - ±10 V (default)
     - Include R19C, R21C, R22C, R24C; DNI R18C, R20C, R23C, R25C
   * -
     - ±5 V
     - Include R18C, R20C, R23C, R25C; DNI R19C, R21C, R22C, R24C
   * -
     - ±4.096 V
     - Include R19C, R21C; DNI R18C, R20C, R22C, R23C, R24C, R25C
   * -
     - ±2.5 V
     - Include R18C, R20C; DNI R19C, R21C, R22C, R23C, R24C, R25C
   * -
     - ±1.5 V
     - Include R18C, R19C, R20C, R21C; DNI R22C, R23C, R24C, R25C
   * - Channel 3
     - ±10 V (default)
     - Include R19D, R21D, R22D, R24D; DNI R18D, R20D, R23D, R25D
   * -
     - ±5 V
     - Include R18D, R20D, R23D, R25D; DNI R19D, R21D, R22D, R24D
   * -
     - ±4.096 V
     - Include R19D, R21D; DNI R18D, R20D, R22D, R23D, R24D, R25D
   * -
     - ±2.5 V
     - Include R18D, R20D; DNI R19D, R21D, R22D, R23D, R24D, R25D
   * -
     - ±1.5 V
     - Include R18D, R19D, R20D, R21D; DNI R22D, R23D, R24D, R25D

*Table 2. ADC Input Voltage Range Selection by Resistor Connections*

DAC Outputs
~~~~~~~~~~~

LLDK can support multiple output voltage ranges which can be configured, such as
0 to 2.5 V, 0 V to 5 V, −5 V to +5 V, and −10 V to +10 V, and custom
intermediate ranges with full 16-bit resolution. In order to change the output
range, resistor placements on the AFE board must be modified and register
settings must be applied to :adi:`AD3552R` on :adi:`EVAL-CN0585-FMCZ <CN0585>`
as described in Table 4.

.. list-table::
   :header-rows: 1

   * - Channel
     - Output Signal
   * - A
     - J9
   * - B
     - J10
   * - C
     - J11
   * - D
     - J12

*Table 3. DAC Output Signal Connectors*

.. list-table::
   :header-rows: 1

   * - Channel
     - Output Span
     - VZS (V)
     - VFS (V)
     - AFE Board Modification
     - Register Setting
   * - CH0
     - +/- 10V (Default)
     - -10.382
     - 10.380
     - Include R9; DNI R10, R11
     - CH0_CH1_OUTPUT_RANGE = 0x100
   * -
     - +/- 5V
     - -5.165
     - 5.166
     - Include R11; DNI R9, R10
     - CH0_CH1_OUTPUT_RANGE = 0x011
   * -
     - 10V
     - -0.165
     - 10.163
     - Include R11; DNI R9, R10
     - CH0_CH1_OUTPUT_RANGE = 0x010
   * -
     - 5V
     - -0.078
     - 5.077
     - Include R10; DNI R9, R11
     - CH0_CH1_OUTPUT_RANGE = 0x001
   * -
     - 2.5V
     - -0.198
     - 2.701
     - Include R10; DNI R9, R11
     - CH0_CH1_OUTPUT_RANGE = 0x000
   * - CH1
     - +/- 10V (Default)
     - -10.382
     - 10.380
     - Include R12; DNI R13, R14
     - CH0_CH1_OUTPUT_RANGE = 0x100
   * -
     - +/- 5V
     - -5.165
     - 5.166
     - Include R13; DNI R12, R14
     - CH0_CH1_OUTPUT_RANGE = 0x011
   * -
     - 10V
     - -0.165
     - 10.163
     - Include R13; DNI R12, R14
     - CH0_CH1_OUTPUT_RANGE = 0x010
   * -
     - 5V
     - -0.078
     - 5.077
     - Include R14; DNI R12, R13
     - CH0_CH1_OUTPUT_RANGE = 0x001
   * -
     - 2.5V
     - -0.198
     - 2.701
     - Include R14; DNI R12, R13
     - CH0_CH1_OUTPUT_RANGE = 0x000
   * - CH2
     - +/- 10V (Default)
     - -10.382
     - 10.380
     - Include R15; DNI R16, R17
     - CH2_CH3_OUTPUT_RANGE = 0x100
   * -
     - +/- 5V
     - -5.165
     - 5.166
     - Include R16; DNI R15, R17
     - CH2_CH3_OUTPUT_RANGE = 0x011
   * -
     - 10V
     - -0.165
     - 10.163
     - Include R16; DNI R15, R17
     - CH2_CH3_OUTPUT_RANGE = 0x010
   * -
     - 5V
     - -0.078
     - 5.077
     - Include R17; DNI R15, R16
     - CH2_CH3_OUTPUT_RANGE = 0x001
   * -
     - 2.5V
     - -0.198
     - 2.701
     - Include R17; DNI R15, R16
     - CH2_CH3_OUTPUT_RANGE = 0x000
   * - CH3
     - +/- 10V (Default)
     - -10.382
     - 10.380
     - Include R18; DNI R19, R20
     - CH2_CH3_OUTPUT_RANGE = 0x100
   * -
     - +/- 5V
     - -5.165
     - 5.166
     - Include R19; DNI R18, R20
     - CH2_CH3_OUTPUT_RANGE = 0x011
   * -
     - 10V
     - -0.165
     - 10.163
     - Include R19; DNI R18, R20
     - CH2_CH3_OUTPUT_RANGE = 0x010
   * -
     - 5V
     - -0.078
     - 5.077
     - Include R20; DNI R18, R19
     - CH2_CH3_OUTPUT_RANGE = 0x001
   * -
     - 2.5V
     - -0.198
     - 2.701
     - Include R20; DNI R18, R19
     - CH2_CH3_OUTPUT_RANGE = 0x000

*Table 4. DAC Output Voltage Range Selection by Resistor Connections and
Register Settings*

Voltage Reference
~~~~~~~~~~~~~~~~~

The default ADC reference configuration uses the internal 2.048 V, ±0.1%
accurate, 20 ppm/°C max voltage reference. For more stringent use cases where
the accuracy and temperature drift is an issue, an external :adi:`LTC6655` 2.048
V, ±0.025% accurate, 2 ppm/°C max voltage reference can be used.

The default DAC reference configuration uses the internal 2.5 V, ±0.3% accurate,
10 ppm/°C max voltage reference. For more stringent use cases where the accuracy
and temperature drift is an issue, an external :adi:`ADR4525` 2.5 V, ±0.02%
accurate, 2 ppm/°C max voltage reference can be used.

.. list-table::
   :header-rows: 1

   * - VREF
     - Jumper Settings
   * - ADC_VREF
     - Short P5
   * - DAC_VREF
     - Short P4

*Table 5. Voltage Reference Settings*

Power Supply Considerations and Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All power for CN0584 is provided by :adi:`EVAL-CN0585-FMCZ <CN0585>` through the
AFE connector. CN0584 uses the +15 V and -15 V rails to provide the positive and
negative supply voltages for the :adi:`ADG5421F <en/products/adg5421f.html>`
input protection switches. The +12 V and -12 V rails provide the positive and
negative supply voltages for the :adi:`ADA4898-1 <en/products/ada4898-1.html>`
ADC buffer amplifiers. The +3.3 V rail powers the EEPROM circuit. Power tree
information can be found in :adi:`EVAL-CN0585-FMCZ <CN0585>`. Table 6 provides
more details on LLDK power rails:

.. list-table::
   :header-rows: 1

   * - Power Rail
     - Description
   * - +12 V
     - LT3045-1 provides the 12V rail supplying up 280mA
   * - -12 V
     - LT3094 provides the -12V rail supplying up to -280mA
   * - +15 V
     - LTM8049 provides the +15V rail at 80% efficiency
   * - -15 V
     - LTM8049 provides the -15V rail at 80% efficiency
   * - +3.3 V
     - Fed through from the FPGA FMC connector to the AFE connector

*Table 6. Power Rail Descriptions*

System Setup Using a ZedBoard
-----------------------------

CN0584 is fully supported using a ZedBoard.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/eval-cn0585-fmcz_kit_top.jpg

   Figure 4. EVAL-CN0585-FMCZ revB connected to EVAL-CN0584-EBZ

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/eval-cn0585-fmcz_angle-web.jpg
   :width: 400px

   Figure 5. EVAL-CN0585-FMCZ revB

The following is a list of items needed for system setup:

- Hardware

  - :adi:`EVAL-CN0585-FMCZ(Rev B) <CN0585>` (Note: Figure 4 features
    EVAL-CN0585-FMCZ revA board. Current LLDK system has revB board shown in
    Figure 5, same connectors and functionalities, only different in USB-C power
    supply.)
  - :adi:`EVAL-CN0584-EBZ <CN0584>`
  -
    `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__
    Rev D or later board
  - 12Vdc, 3A power supply
  - 16GB (or larger) Class 10 (or faster) micro-SD card (included in the box)
  - USB-C power source (included in the EVAL-CN0585-FMCZ Rev-B box)
  - Micro-USB to Type-A cable
  - Ethernet cable
  - User interface setup (choose one):

    - HDMI monitor, keyboard, and mouse plugged directly into the ZedBoard
    - Host Windows/Linux/Mac computer on the same network as the ZedBoard

- Software

  - Host PC (Windows or Linux)
  - A UART terminal if need to access Linux system on the ZedBoard (Putty/Tera
    Term/Minicom, etc.), Baud rate 115200 (8N1)
  - :ref:`iio-oscilloscope`
  - :ref:`kuiper`

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

The box includes a pre-programmed SD card. You can skip the steps in this
section and go to the
:dokuwiki:`Setting up the Hardware </resources/eval/user-guides/circuits-from-the-lab/cn0584#Setting up the Hardware>`
section if using this provided card.

To boot the ZedBoard and control the :adi:`EVAL-CN0585-FMCZ <CN0585>`, you will
need to install ADI Kuiper Linux on an SD card. Complete instructions, including
where to download the SD card image, how to write it to the SD card, and how to
configure the system are provided on the :ref:`kuiper`.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~

Follow the configuration procedure under **Configuring the SD Card for FPGA
Projects** on the :ref:`kuiper` page. Copy the following files onto the boot
directory to configure the SD card (download link for EVAL-CN0585-FMCZ Rev-B
:download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/sd_card_config_files_revb.zip`
, for EVAL-CN0585-FMCZ Rev-A
:download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/sdcard_config_files.zip`
):

- uImage file for Zynq
- BOOT.BIN specific to your :adi:`EVAL-CN0585-FMCZ <CN0585>` + ZedBoard
- setup_adc.sh file for setting up ADC
- devicetree.dtb devicetree for Zynq specific to your
  :adi:`EVAL-CN0585-FMCZ <CN0585>` + ZedBoard.The device tree describes the
  following devices:

  #. one-bit-adc-dac – controls the MAX7301
  #. axi_pwm_gen – generates the CNV signal for analog-to-digital converters
  #. ref_clk – generates the sample clock for ADAQ23876 devices and the
     reference clock for AD3552R devices
  #. rx_dma – controls the DMA for RX path
  #. Ltc2387 – controls ADAQ23876 devices
  #. qspi0 – controls the SPI devices that are connected to the PL SPI IP
  #. dac0_tx_dma - controls the DMA for the first AD3552R device
  #. dac1_tx_dma - controls the DMA for the second AD3552R device
  #. axi_ad3552r_0 – controls the first AD3552R device
  #. axi_ad3552r_1 – controls the second AD3552R device
  #. I2c – controls devices that are connected to PL I2C IP (eeprom, eeprom2,
     ad7291_1)

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

You will need to:

#. Get the
   `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__.

   .. figure:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/AD777x-ARDZ/zedboard.png
      :width: 600px

#. Insert the SD CARD into the SD Card Interface Connector (J12).
#. Connect the :adi:`EVAL-CN0585-FMCZ <CN0585>` board into the ZedBoard FMC
   connector.
#. Connect the :adi:`EVAL-CN0584-EBZ <CN0584>` board into the
   :adi:`EVAL-CN0585-FMCZ <CN0585>`.
#. Connect micro USB to UART port (J14), and the other end to the host PC.
#. Connect the ethernet cable to RJ45 ethernet connector (J11), and the other
   end to the host PC.
#. Plug the Power Supply into the 12V Power ZedBoard input connector (J20) (DO
   NOT turn the device on).
#. Plug USB-C power supply to :adi:`EVAL-CN0585-FMCZ <CN0585>` (revB only)
#. Set the jumpers as seen in Figure 6

   .. figure:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/adaq8092/zed_jumpers.jpg
      :width: 400px

     Figure 6. ZedBoard Jumper Settings

#. Connect the DAC output connectors to the negative ADC input connectors as
   shown in Figure 7 using coax cables (i.e. DAC0 to ADC0-neg, DAC1 to ADC1-neg,
   etc.). Terminate the positive ADC connectors with 50ohms SMA terminators

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/cn0584_loopback_connection.png
      :width: 600px

     Figure 7. EVAL-CN0584-EBZ Loopback Connection on AFE *- Turn the ZedBoard
     on. - Wait ~30 seconds for the ``DONE`` LED to turn blue. This is near the
     DISP1.The hardware set up is now complete. setup_cn0585_diagram.png* Figure
     8. Example System Setup

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

Application Software (both locally and remotely on the FPGA)
------------------------------------------------------------

The CN0584 can be interfaced with using IIO Oscilloscope, Python, or MATLAB to
enable device configuration, capture of incoming samples from the ADCs, and
generation of waveforms to be transmitted by the DACs.

Hardware Connection
~~~~~~~~~~~~~~~~~~~

Libiio is a library used for interfacing with IIO devices and must be installed
on your computer to interface with the hardware.

.. admonition:: Download

   Download and Install the latest
   `Libiio package <https://github.com/analogdevicesinc/libiio/releases>`__ on
   your machine.

To connect to your device, the IIO Osciloscope software must be able to create a
context. The context creation in the software depends on the backend used to
connect to the device as well as the platform where the
:adi:`EVAL-CN0585-FMCZ <CN0585>` is attached. The ZedBoard running ADI Kuiper
Linux is currently the only platform supported for the CN0585.

The user needs to supply a **URI** (Uniform Resource Identifier) which will be
used in the context creation. To get the URI, use the command iio_info in the
terminal. The
:dokuwiki:`iio_info </resources/tools-software/linux-software/libiio/iio_info>`
command is a part of the libIIO package that reports all IIO attributes.Upon
installation, simply enter the command on the terminal command line to access
it.

For FPGA(ZedBoard) Direct Local Access:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info

For Windows machine connected to an FPGA(ZedBoard):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info -u ip:<ip address of your ip>

Example:

- If your ZedBoard has the IP address 169.254.92.202, you have to use *iio_info
  -u ip::169.254.92.202* as your URI

.. note::

   Do note that the Windows machine and the FPGA board should be connected to
   the same network for the machine to detect the device.

IIO Oscilloscope
~~~~~~~~~~~~~~~~

:ref:`iio-oscilloscope` is a cross platform GUI application which can interface
with different evaluation boards from within a Linux system.

.. important::

   Make sure to download/update to the latest version of IIO-Oscilloscope found
   on this link\ :git-iio-oscilloscope:`releases\+`

Once done with the installation or an update of the latest IIO-Oscilloscope,
open the application. The user needs to supply a URI which will be used in
the context creation of the IIO Oscilloscope. If there"s only one platform is
connected, the IIO Oscilloscope will find URI automatically; If more than one
platforms are connected, the user needs to supply the specific URI. The
instructions to obtain the URI can be found in the previous section. Note:
the ``Serial Context`` connection method is not enabled.

Press refresh to display available IIO Devices and press connect.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/cn0585_remote_login.jpg
   :width: 700px

   Figure 9. IIO Oscilloscope Connection

After the board is connected, select the **one-bit-adc-dac-device**, which is
the controller for the MAX7301ATL+ I/O Expander. Then configure pins values
of output voltages 0 through 9, by setting the **raw value to 1**. Press
**Write** to confirm.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/max7301atl_output_channels_configuration.png
   :width: 400px

   Figure 10. MAX7301ATL Output Channels Configuration

.. list-table::
   :header-rows: 1

   * - **one-bit-adc-dac device channel**
     - **Schematic PIN**
   * - Voltage0
     - GPIO0_VIO
   * - Voltage1
     - GPIO1_VIO
   * - Voltage2
     - GPIO2_VIO
   * - Voltage3
     - GPIO3_VIO
   * - Voltage4
     - GPIO6_VIO
   * - Voltage5
     - GPIO7_VIO
   * - Voltage6
     - PAD_ADC0
   * - Voltage7
     - PAD_ADC1
   * - Voltage8
     - PAD_ADC2
   * - Voltage9
     - PAD_ADC3

*Table 7. Voltage Configuration for GPIO Pins*

Input sources for AD3552R devices axi-ad3552r-0 and axi-ad3552r-1 can be
configured as dma_input, ramp_input or adc_input.

- dma_input: DAC input is driven by signals generated by Matlab stored in DMA.
- ramp_input: DAC input is driven by ramp signal generated by Matlab stored in
  DMA.
- adc_input: For passthrough models, DAC input is driven by ADC output. For
  models with integrated HDL_DUT, DAC input is driven by HDL_DUT outputs.

Select the desired input source for both AD3552R devices axi-ad3552r-0 and axi-ad3552r-1 as dma_input.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/input_source_dac0_cn0585.png
   :width: 700px

   Figure 11. AD3552R Input Source Selection in IIO Oscilloscope

.. important::

   Even if the input source is set to adc_input or ramp_input the steps
   regarding the DAC Data Manager tab have to be followed.

Select the desired output range for both AD3552R devices.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/output_range_cn0585.png
   :width: 700px

   Figure 12. AD3552R Output Range Selection in IIO Oscilloscope

.. warning::

   Make sure you don't try to read/write the output_range attribute when the
   stream_status is in start_stream or start_stream_synced.

.. important::

   After changing the output range, the board should be power cycled to ensure
   the DACs operate properly.

From the DAC Data Manager Window select the output channels of the DAC and
enable the cyclic buffer for each DAC.

Load an example file (.mat, .txt, etc) from the IIO Oscilloscope installation
directory, under **Program Files/IIO Oscilloscope/lib/osc/waveforms** folder.

.. important::

   If the source is set as dma_input and the data from all 4 channels needs to
   be synchronized make sure that you press the load button for the
   axi-ad3552r-1 device first then for axi-ad3552r-0.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/DAC_DATA_MANAGEMENT_cn0585.jpg
   :width: 500px

  Figure 13. DAC Data Manager with Example Waves on 4 Channels

Click on the load button.

.. important::

   If the source is set as dma_input and the data from all 4 channels needs to
   be synchronized make sure that you write the start_stream_synced for the
   axi-ad3552r-1 device first then for axi-ad3552r-0.

From the Debug window, select the stream_status IIO Attribute and start the
stream (start_stream_synced means that all 4 channels are updated at the same
time and the data streaming process waits for both DACs to be started).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/stream_status_iio.jpg

    Figure 14. DAC Stream Status Selection

.. important::

   If the source is set as dma_input and the data from all 4 channels needs to
   be synchronized make sure that you write the start_stream_synced for the
   axi-ad3552r-1 device first then for axi-ad3552r-0.

After the stream_status has been written and 4 channels are enabled, hit play button. Then data capture window can be seen like in Figure 15.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/captured_loopback_signal_cn0585.jpg
   :width: 700px

   Figure 15. Captured Loopback Signal

.. important::

   Note that there is a phase delay between voltage0/voltage2 and
   voltage1/voltage3 because the DAC device channels are updated consecutively
   See the DAC UPDATE MODES section in :adi:`AD3552R`

.. warning::

   If you intend to stop the stream transmission and start it again synchronized
   set the stream_status IIO Attribute to stop_stream for axi-ad3552r-1 device
   first then for the axi-ad3552r-0 device.

PyADI-IIO
~~~~~~~~~

The CN0584 can be interfaced to Python using the
:dokuwiki:`PyADI-IIO </resources/tools-software/linux-software/pyadi-iio>`.
PyADI-IIO is a Python abstraction module to simplify interaction with IIO
drivers on ADI hardware. This module provides device-specific APIs built on top
of the current libIIO Python bindings. These interfaces try to match the driver
naming as much as possible without the need to understand the complexities of
libIIO and IIO.

Follow the step-by-step procedure on how to install, configure, and set up
PyADI-IIO and install the necessary packages/modules needed by referring to
:dokuwiki:`PyADI-IIO </resources/tools-software/linux-software/pyadi-iio>`.

Running the example
^^^^^^^^^^^^^^^^^^^

.. admonition:: Download

   Github link for the Python sample script:
   :git-pyadi-iio:`CN0585 Python Example <examples/cn0585_fmcz_example.py+>`

Download or git clone :git-pyadi-iio:`/` to your local drive.

- If direct downloading ZIP folder, make sure to download from cn0585_v1 branch.
- If cloning the repository using `Git <https://git-scm.com/downloads>`__, type
  ``git checkout cn0585_v1`` to switch to the correct branch.

Install additional Packages.

::

   pip install tk pytest paramiko matplotlib
     * Do above in the command prompt window. In general, use pip install "package name" to install any missing package.

After installing and configuring PYADI-IIO on your machine, you are now ready
to run Python script examples. To follow this example, navigate to pyadi-iio
folder (For example, ``D:\\pyadi-iio`` is where pyadi-iio folder is located).
Then run the **cn0585_fmcz_example.py** found in the examples folder.

::

   D:\pyadi-iio>set PYTHONPATH=D:/pyadi-iio/
   D:\pyadi-iio>python examples/cn0585_fmcz_example.py ip:your_board_ip

Press enter and lines below will be observed:

::

   $ python examples/cn0585_fmcz_example.py
   uri: ip:your_board_ip
   ############# EEPROM INFORMATION ############
   read 256 bytes from /sys/devices/soc0/fpga-axi@0/41620000.i2c/i2c-1/1-0050/eeprom
   Date of Man     : Fri Jan 20 08:11:00 2023
   Manufacturer    : Analog Devices
   Product Name    : LLDK-LTC2387-AD3552R
   Serial Number   : 56864654
   Part Number     : 1234
   FRU File ID     : 12131321
   PCB Rev         : VB
   PCB ID          : HIL
   BOM Rev         : VC
   Uses LVDS       : Y

   #############################################
   GPIO4_VIO state is: 0
   GPIO5_VIO state is: 0
   Voltage monitor values:
   Temperature:  49.25 C
   Channel 0:  2267.45605283  millivolts
   Channel 1:  627.4414057359999  millivolts
   Channel 2:  2061.157224874  millivolts
   Channel 3:  753.1738275079999  millivolts
   Channel 4:  2092.285154536  millivolts
   Channel 5:  2084.960935792  millivolts
   Channel 6:  2253.4179669039998  millivolts
   Channel 7:  1809.69238133  millivolts
   AXI4-Lite 0x108 register value: 0x2
   AXI4-Lite 0x10c register value: 0xB
   Sampling rate is: 15000000
   input_source:dac0: dma_input
   input_source:dac1: dma_input

The DAC outputs should be looped back into the ADCs as shown in figure 7 in the
System Setup Using a ZedBoard section. After running the script with the board
in this configuration, the following window will pop up:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0584/figure15_adc_cap_data_python_plot.png
   :width: 700px

  Figure 16: ADC Captured Data Python Plot

.. important::

   If you plan to transmit multiple cycles of synchronous stream, make sure the
   script starts/stops axi-ad3552r-1 first, then axi-ad3552r-0.

MATLAB and Simulink
~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   Required MATLAB Add-Ons:

   - :mw:`Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio <matlabcentral/fileexchange/61624-communications-toolbox-support-package-for-analog-devices-adalm-pluto-radio>`
   - :mw:`HDL Coder <products/hdl-coder.html>`
   - :mw:`SoC Blockset Support Package for Xilinx devices <matlabcentral/fileexchange/70616-soc-blockset-support-package-for-xilinx-devices?s_tid=srchtitle>`
   - :mw:`SoC Blockset <products/soc.html>`

.. admonition:: Download

   Github link for the Matlab sample script:
   :git-HighSpeedConverterToolbox:`CN0585StreamingTest.m <test/CN0585StreamingTest.m+>`

The steps described in the
:dokuwiki:`Analog Devices Transceiver Toolbox For MATLAB and Simulink </resources/tools-software/transceiver-toolbox>`
page have to be followed to configure the Matlab/Simulink project using the
:mw:`MathWorks HDL Workflow Advisor <help/hdlcoder/examples/getting-started-with-hardware-software-codesign-workflow-for-xilinx-zynq-platform.html>`.

Device Control and Data Streaming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remote data streaming to and from hardware is made available through system
object interfaces, which are unique for each component or platform. The hardware
interfacing system objects provide a class to both configure a given platform
and move data back and forth from the device. To run the
:git-HighSpeedConverterToolbox:`CN0585StreamingTest.m <test/CN0585StreamingTest.m+>`
example, the following steps must be completed first.

Ensure MATLAB package ``Communications Toolbox Support Package for Analog
Devices ADALM-Pluto Radio`` is installed from Matlab Add-Ons.

Execute the following commands on the computer terminal (Cygwin is recommended
for Windows) to set up a local git repository.

::

   git clone :git-HighSpeedConverterToolbox.git
   cd HighSpeedConverterToolbox
   git submodule update --init --recursive
   git checkout cn0585_v1

Open Matlab from the HighSpeedConverterToolbox directory.

Open CN0585StreamingTest.m from the test subdirectory, update the board_ip
variable to match the Zedboard IP address, and finally run the script.

The DAC outputs should be looped back into the ADCs as shown in figure 6 in the
System Setup Using a ZedBoard section. After running the script with the board
in this configuration, the window in Figure 17 will pop up. :

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0585/matlab_plot.jpg
   :width: 800px

   Figure 17. ADC Captured Data Matlab Plot

Note the y-axis is plotted in units of ADC codes, and can be converted to
voltage by referencing the transfer function on the :adi:`ADAQ23876` datasheet.

.. important::

   If you plan to transmit multiple cycles of synchronous stream, make sure to
   start:`stop+` axi-ad3552r-1 first, then axi-ad3552r-0.

Configuring Custom HDL Models Using Simulink
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ZedBoard that drives CN0585 is configured with a HDL reference design which
is an embedded system built around a processor core either ARM, NIOS-II, or
Microblaze.

.. figure:: https://wiki.analog.com/_media/playground/rx.png
   :width: 600px

   Figure 18. HDL Block Design with Simulink HDL_DUT in Rx Configuration

.. figure:: https://wiki.analog.com/_media/playground/tx.png
   :width: 600px

   Figure 19. HDL Block Design with Simulink HDL_DUT in Tx Configuration

.. figure:: https://wiki.analog.com/_media/playground/rxtx.png
   :width: 600px

   Figure 20. HDL Block Design with Simulink HDL_DUT in Rx-Tx Configuration

The device digital interface is handled by specific device cores axi_ad35552r
for the DAC path and axi_ltc2387 for the ADC path. The cores are programmable
through an AXI-lite interface. Details of reference design can be found in
:dokuwiki:`Reference Design </resources/eval/user-guides/circuits-from-the-lab/cn0585/reference_hdl>`.
HighSpeedConverterToolbox repository supports IP Core generation flow from
MathWorks which allows for automated integration of HDL_DUT into HDL reference
designs from Analog Devices. The workflow for generating HDL_DUT codes takes
Simulink subsystems, runs HDL-Coder to generate source Verilog, and then
integrates that into a larger reference design. HDL_DUT can be integrated inside
HDL reference design in three different configurations which are Rx,Tx and
Rx-TX. Figure 19 and Figure 20 demonstrates how HDL_DUT is placed between Tx and
Rx path for these three configuration types. HDL_DUT Code Generation Workflow is
described in
:dokuwiki:`configuring-matlab </resources/eval/user-guides/circuits-from-the-lab/cn0584/configuring-matlab>`

Digital Template
----------------

For an example with a model that utilizes a wider sample of MATLAB Simulink
blocks in the design,
:dokuwiki:`digital-template </resources/eval/user-guides/circuits-from-the-lab/cn0584/digital-template>`
includes a Simulink model and instructions on how to use it.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`EVAL-CN0584-EBZ Design & Integration Files <cn0584-designsupport>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information and Useful Links
---------------------------------------

- :adi:`CN0584 Circuit Note Page <CN0584>`
- :adi:`ADAQ23876 Product Page <ADAQ23876>`
- :adi:`AD3552R Product Page <AD3552R>`
- :adi:`LTC6655 Product Page <LTC6655>`
- :adi:`ADR4525 Product Page <ADR4525>`
- :adi:`AD7291 Product Page <AD7291>`
- :adi:`ADG5421F Product Page <ADG5421F>`

Reference Demos & Software
--------------------------

- :dokuwiki:`High Speed Converter Toolbox for MATLAB and Simulink </resources/tools-software/hsx-toolbox>`
- `pyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`__
- :dokuwiki:`PyADI-IIO Installation Guide </resources/tools-software/linux-software/pyadi-iio>`
- :dokuwiki:`IIO Oscilloscope Installation Guide </resources/tools-software/linux-software/iio_oscilloscope>`
- :ref:`kuiper`
