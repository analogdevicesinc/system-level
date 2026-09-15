.. imported from: https://wiki.analog.com/resources/eval/user-guide/adaq8092-eval-board

.. _adaq8092-eval-board:

ADAQ8092 Evaluation Board User Guide
====================================

General Description
-------------------

The :adi:`EVAL-ADAQ8092-FMCZ <EVAL-ADAQ8092>` evaluates the :adi:`ADAQ8092`, a
14-bit, 105MSPS, high-speed dual-channel data acquisition uModule solution. This
device uses System-in-Package (SiP) technology that integrates three common
signal processing and conditioning blocks. This
:adi:`EVAL-ADAQ8092-FMCZ <EVAL-ADAQ8092>` board does not need an external power
supply to operate and requires a very small jitter in the clock source. We
recommend using the DC1075B to improve the clock signal source. For full details
on the :adi:`ADAQ8092`, see the :adi:`ADAQ8092` data sheet, which must be
consulted in conjunction with this user guide when using the
:adi:`EVAL-ADAQ8092-FMCZ <EVAL-ADAQ8092>`.

Features
--------

- Dual-Channel Simultaneously Sampling ADC
- Integrated differential amplifier/ADC driver
- Single-ended to differential input config circuitry
- LVDS Output capability
- Serial SPI Port for Configuration
- On-board power solution
- FMC-LPC system board connector

Evaluation Board Kit Contents
-----------------------------

- :adi:`EVAL-ADAQ8092-FMCZ <EVAL-ADAQ8092>` evaluation board
- Micro-SD memory card (with adapter) containing system board boot software and
  Linux OS

Equipment Needed
----------------

- PC with Windows 7 or Windows 10 operating system
- EVAL-ADAQ8092-FMCZ
- Digilent ZedBoard with 12 V wall adapter power supply
- Power Supply
- Rohde & Schwarz SMA100A (clock source) - Suggested
- Keysight 336xx series (signal generator) - Suggested
- DC1075B (Clock Divider) - Suggested
- SMA Cables
- Attenuator
- TTE Bandpass Filter - centered on test signal frequency - Suggested
- SD card
- SMA Adapter (Male-Male)

Quick Start Guide
-----------------

.. todo:: section>resources/tools-software/linux-software/adi-kuiper_for_eval_getting_started#Getting Started&showfooter=nofooter

Board Hardware
--------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/eval-adaq8092-fmcz_top-web.png
   :width: 400px

   Figure 1. EVAL-ADAQ8092-FMCZ Board Photo

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/eval-board-block.png
   :width: 800px

   Figure 2. Block Diagram of the EVAL-ADAQ8092-FMCZ

Board Description
~~~~~~~~~~~~~~~~~

**Figure 2** shows the EVAL-ADAQ8092-FMCZ block diagram. The ADAQ8092 µModule
that is soldered to the EVAL-ADAQ8092-FMC does not require external supply to
power-up the board. It uses the +12V supply source from the data capture board
such as Zedboard and activates the LDO"s to provide the 3.3V and 1.8V needed of
the board.

Analog Inputs
~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/analog_input_circuitry.png
   :width: 600px

   Figure 3. Analog Input Circuitry of EVAL-ADAQ8092-FMCZ

The EVAL-ADAQ8092-FMCZ provides the user to either use a single-ended or
differential source. For the single-ended source, user can either use the balun
so that the part will still be driven differentially or bypass it to drive the
part single-endedly. Installation of 0Ω resistor is used to configure the input
of the analog input circuitry.

**Table 1. Factory Default Settings (Single-ended input driven)**

.. list-table::
   :header-rows: 1

   * - Channel
     - Link
     - Location
   * - 1
     - JP1
     - Pin 2 to Pin 3
   * -
     - JP3
     - Pin 2 to Pin 1
   * -
     - JP4
     - Pin 2 to Pin 3
   * - 2
     - JP2
     - Pin 2 to Pin 3
   * -
     - JP5
     - Pin 2 to Pin 1
   * -
     - JP6
     - Pin 2 to Pin 3

.. important::

   *Without changing other resistor values of the board, then this board is
   ready for a single ended source that drives the part single-endedly. But if
   the user uses a differential source, then install 49.9Ω resistors at R1 and
   R3 for Channel 1 and Channel 2, respectively. These should be implemented to
   properly balance the inputs when driven differentially. Refer to* **Figure
   6** *and* **Figure 7** *for the schematic.*

**Table 2. Differentially driven using the balun**

.. list-table::
   :header-rows: 1

   * - Channel
     - Link
     - Location
   * - 1
     - JP1
     - Pin 2 to Pin 1
   * -
     - JP3
     - Pin 2 to Pin 3
   * -
     - JP4
     - Pin 2 to Pin 1
   * - 2
     - JP2
     - Pin 2 to Pin 1
   * -
     - JP5
     - Pin 2 to Pin 3
   * -
     - JP6
     - Pin 2 to Pin 1

.. important::

   *When using this configuration, resistor values should also be changed to
   properly balance the impedance and make the gain approximately equal to 5.
   For channel 1: R8 & R9 = 200 Ω, and, R14 & R16 = 18.2Ω. For channel 2: R10 &
   R11 = 200Ω, and, R15 & R17 = 18.2Ω. Refer to* **Figure 6** *and* **Figure 7**
   *for schematic.*

Encode Circuitry
~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/encode_circuitry.png
   :width: 600px

   Figure 4. Encode Circuitry of EVAL-ADAQ8092-FMCZ

The user can either use a single-ended encode mode or a differential encode
mode. The default configuration of the EVAL-ADAQ8092-FMCZ uses the single-ended
encode mode that requires a CMOS level. Also, the board provides an option to
install an oscillator (Y1) and use it as a built-in clock for a single-ended
encode mode. When using a sinusoidal, PECL or LVDS signal then it is suggested
to use the differential encode mode.

Power Circuitry
~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/power_circuitry.png
   :width: 600px

   Figure 5. Power Circuitry of EVAL-ADAQ8092-FMCZ

The EVAL-ADAQ8092-FMC uses the +12V supply from the data capture board such as
Zed board at C35 of the FMC (FPGA Mezzanine Card) connector pin configuration.
This +12V supply goes to a reverse input protection by the used of LTC4359 (U2)
and then proceed with a step down regulator, LTM8074 (U4). The output of the
LTM8074 which is configured to have 5V output will then supply the LTC1673-1.8
(U3) and LTC1763-3.3 (VR1). The LTC1763-1.8 will be VDD and OVDD supplies, while
the LTC1763-3.3 will be the VCC supply. External supplies can also be used when
some of the built-in power circuitry is failing. Re-work of the board is needed
to achieve this.

Schematic
~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/schematic_1.png
   :width: 800px

   Figure 6. Schematic of EVAL-ADAQ8092-FMCZ (page 1)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/schematic_2.png
   :width: 800px

   Figure 7. Schematic of EVAL-ADAQ8092-FMCZ (page 2)

Evaluating Board Hardware
-------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/complete_setup_final.png
   :width: 900px

   Figure 8. Evaluation setup for EVAL-ADAQ8092-FMCZ

Setting up the board
~~~~~~~~~~~~~~~~~~~~

**Figure 8** illustrates the evaluation system components. To use the system,
here"s the following steps:

#. Connect the evaluation board to the ZedBoard. Ensure that there"s an SD card
   installed on it.
#. Connect the CLK divider (DC1075B) to the evaluation board
#. Connect a micro-USB cable to the USB OTG port
#. Apply power to the ZedBoard and to the DC1075
#. Open the ACE software
#. Apply the desire CLK and input signal
#. Start the evaluation

Controller Board
~~~~~~~~~~~~~~~~

The ZedBoard, which is the system controller board, enables the configuration of
the ADC and capture of data from the evaluation board by the PC via USB (or
Ethernet). The ADAQ8092 support a multi-lane serial port interface (SPI) for
each data converter channel. The SPI interface for each channel is connected to
the ZedBoard via the FMC connector (P1). The ZedBoard™ functions as the
communication link between the PC and connected evaluation board. It buffers
samples captured from the evaluation board in its DDR3 memory. The ZedBoard
board requires power from a 12 volt wall adapter (included with the ZedBoard).
It hosts a Xilinx® ZYNQ® 7020 SoC, which contains two ARM® Cortex-A9 Processors
and a Series-7 FPGA with 85k Programmable Logic cells. A Linux OS runs on the
host processor system. It communicates with the PC through either a USB 2.0 high
speed port or a 10/100/1000 Ethernet port. The default software configuration
uses USB.

FIXME

Software Support
----------------

The ADI ACE application provides a "plug and play" evaluation experience,
enabling users to get up and running quickly with the product evaluation board.
ACE can configure the embedded software on supported controller boards and
provides a quick and easy way to get setup, configure the board and perform data
capture and analysis and/or waveform generation. For ACE installation and
documentation instructions see :adi:`ACE`. Make sure to follow the instructions
to install the necessary evaluation board plug-in support.

- If the machine that ACE is installed on has internet access, you can
  find/install/update plug-ins directly from the ACE application. For
  environments without internet access, you can download these plug-ins from the
  previous link to portable storage and install them into ACE.

.. note::

   Product specific documentation for the evaluation software can be found
   within the ACE plug-in. The controller board supported by ACE with this
   product evaluation board is the ZedBoard™.

FIXME

Software Operation
~~~~~~~~~~~~~~~~~~

To start the ACE evaluation software, here are the following steps:

- 1. Open the ACE software.
- 2. In the Start window, wait until the software recognizes the ``ADAQ8092
  Board`` as an attached hardware, and then double-click on it to go to the
  ``ADAQ8092 Board`` window (refer to Figure 9 ).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/start_window_final.png
   :width: 800px

   Figure 9. Start Window

- 3. In the ADAQ8092 Board window, here you will see the simple block diagram of
  the evaluation board of the ADAQ8092, double-click the ``ADAQ8092`` icon from
  the block diagram to go to the ``ADAQ8092`` chip window (refer to Figure 10 ).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/board_image_final.png
   :width: 800px

   Figure 10. ADAQ8092 Board Window

- 4. In the ADAQ8092 chip window, click ``Proceed to Analysis``, to start the
  evaluation. *Note: Here you change the device attributes before starting the
  evaluation such as: alt_bit_pol_en , data_rand_en, dout_en, pd_gpio, pd_mode,
  sampling_frequency, test_mode, and twos_complement.*

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/chip_image_final2.png
   :width: 800px

   Figure 11. ADAQ8092 (Chip) Window

Analysis
~~~~~~~~

Here in the **ANALYSIS** window, there are three (3) panes, the **CAPTURE**
pane, **ANALYSIS** pane, and **RESULTS** pane.

- In the CAPTURE pane, the user can change the sample count up to 65536 and the
  sample frequency used is shown. At the bottom, the user can capture data once
  by clicking ``Run Once`` or continuously by clicking ``Run Continuously``.
  *Note: Use ``Run Continuously`` when capturing the Average FFT, INL, and DNL.*
- In the ANALYSIS pane, the user can change the ``windowing`` type of the FFT,
  and also the ``average iterations`` when capturing the INL and DNL
  performance. When measuring the INL and DNL, the user should use the ``Run
  Continuously`` function and wait until it reaches the number of ``average
  iterations`` placed.
- In the RESULTS pane, this is where the parametric values will be displayed. At
  the bottom of it, the user can import or export the data.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/waveform.png
   :width: 800px

   Figure 12. Waveform view

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/fft.png
   :width: 800px

   Figure 13. FFT view

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/average_fft_result.png
   :width: 800px

   Figure 14. Average FFT view

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/inl.png
   :width: 800px

   Figure 15. INL view

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq8092/dnl.png
   :width: 800px

   Figure 16. DNL view

Evaluation Board Support
------------------------

Technical support for the evaluation board hardware and software can be
obtained by posting a question to ADI"s
:ez:`EngineerZone <data_converters/precision_adcs>` technical support community
for precision ADCs.

The evaluation board schematic and other board files can be found on the
`EVAL-ADAQ8092-FMCZ <https://wcm.cldnet.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADAQ8092.html>`__
web page.
