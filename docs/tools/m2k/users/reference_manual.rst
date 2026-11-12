.. _m2k reference_manual:

Reference Manual (Understanding the Internals)
==============================================

Overview
--------

The easy to use :adi:`ADALM2000` active learning module (M2K) helps introduce
electrical engineering students and hobbyists to the fundamentals of signals
and systems. Designed for students at all levels and from all backgrounds, the
module can be used for both instructor-led and self-directed learning to help
students develop a foundation in exploring signals and systems into the tens
of MHz that they can build on as they pursue science, technology, or
engineering degrees, without the cost and bulk associated with traditional lab
gear.

With 12-bit ADCs(running at 100MSPS) and DACs(at 150MSPS), the :adi:`ADALM2000`
brings the power of high performance lab equipment to the palm of your hand.
When coupled with Analog Devices' Scopy graphical application software running
on a computer, provides the user with the following high performance
instrumentation:

* Two-channel oscilloscope with differential inputs
* Two-channel arbitrary waveform generator (AWG)
* 16-channel digital logic analyzer (3.3V CMOS and 1.8V or 5V tolerant, 100MS/s)
* 16-channel pattern generator (3.3V CMOS, 100MS/s)
* 16-channel virtual digital I/O
* Two input/output digital trigger signals for linking multiple instruments
  (3.3V CMOS)
* Two-channel voltmeter (AC, DC, ±25V)
* Network analyzer – Bode, Nyquist, Nichols transfer diagrams of a circuit.
  Range: 1Hz to 10MHz
* Spectrum Analyzer – power spectrum and spectral measurements (noise floor,
  SFDR, SNR, THD, etc.)
* Digital Bus Analyzers (SPI, I²C, UART, Parallel)
* Two programmable power supplies (0…+5V , 0…-5V)

Small enough to fit in a shirt pocket, the M2K is completely self-contained and
entirely USB powered with the default firmware. Because M2K is enabled by
libiio drivers, it supports OS X® , Windows®, and Linux®, which allows students
to learn and explore on a variety of host platforms. In addition, the
cross-platform :dokuwiki:`libm2k </university/tools/m2k/libm2k/libm2k>`
interface library allows users to communicate with the M2K their own C, C#, or
Python programs.

.. grid::
   :widths: 50% 50%

   .. figure:: ../images/adalm2000_board1.png
      :width: 400px
      :alt: ADALM2000 board (side 1)

      Figure 1.1 ADALM2000 (side 1)

   .. figure:: ../images/adalm2000_board2.png
      :width: 400px
      :alt: ADALM2000 board (side 2)

      Figure 1.2 ADALM2000 (side 2)

.. figure:: ../images/adalm2000-pin-wires.png
   :width: 700px
   :alt: ADALM2000 pinout

   Figure 2. ADALM2000 Pinout

The :adi:`ADALM2000` board is based on the :xilinx:`Zynq All Programmable SoC (AP SoC) <products/adaptive-socs-and-fpgas/soc/zynq-7000.html>`
to which integrates the software programmability of an ARM-based processor with
the hardware programmability of an FPGA, enabling hardware acceleration while
integrating CPU, DSP, ASSP, and mixed signal functionality into a single device.
The device used in the M2K features a single-core ARM Cortex™-A9 processor
mated with 28nm Artix®-7 based programmable logic, outfitted with commonly used
hardened peripherals (USB, SPI, etc.)

Architecture
------------

The high-level block diagram of :adi:`ADALM2000` is presented in Figure 3. The
Scopy software application will automatically detect the board and communicate
with it via USB 2.0, while the functional blocks of ADALM2000 can be controlled
via :ref:`libm2k` interface, including parameters configuration, acquiring,
storing and transferring data.

Block diagram
~~~~~~~~~~~~~

.. figure:: ../images/block_diagram_m2k.png
   :width: 500px
   :alt: ADALM2000 block diagram

   Figure 3. ADALM2000 block diagram


The block diagram is divided into the following blocks:

* **Analog Inputs**

  * Input Divider and Gain Control — high‑bandwidth input divider. High or Low
    Gain can be selected by the SoC.
  * Buffer — high‑impedance buffer.
  * Driver — provides appropriate signal levels and protection to the ADC.
  * Scope Reference and Offset — generates and buffers reference and offset
    voltages for the scope stages.
  * ADC — Analog‑to‑Digital Converter for each scope channel.

* **Waveform Generator**

  * DAC — Digital‑to‑Analog Converter for each AWG channel.
  * I/V — current‑to‑bipolar‑voltage converters.
  * Output stages

* **Clock and Oscillator** — high‑quality clock signal for the ADC and DAC
* **Digital I/O** — protected access to the FPGA pins assigned for the Pattern
  Generator and Logic Analyzer
* **Power Supplies** — generates all internal supply voltages and user supply
  voltages
* **USB Controller** — host connectivity
* **QSPI Flash** — stores calibration parameters
* **SoC** — FPGA + single‑core ARM processor, high‑speed digital logic, and
  software connectivity.

ADC/DAC AD9963
--------------

The :adi:`AD9963` is a 12-bit, low power Mixed signal Front end converters
that provides two ADC channels with sample rates of 100 MSPS and two DAC
channels with sample rates to 170 MSPS. The :adi:`AD9963` offers high
performance with low power consumption, high integration and a flexible
digital interface. The :adi:`ADALM2000` operates the ADC channels at a
maximum sample rate of 100 MSPS, and the DAC channels at a maximum sample
rate of 150 MSPS.

.. figure:: ../images/ad9963.png
   :width: 400px
   :alt: AD9963 ADC/DAC

   Figure 4. AD9963 ADC/DAC

Analog Inputs
-------------

Input Dividers and Gain Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The gain mode is selected in this stage by the SoC, enabling the corresponding
switch from ADG612 device. ADG612 is a monolithic CMOS device containing four
independently selectable switches with the characteristics:

* Ultralow charge injection (1 pC typically)
* Dual ±2.7 V to ±5.5 V or single +2.7 V to +5.5 V operation
* Automotive temperature range: −40°C to +125°C
* Small, 16-lead TSSOP and SOIC packages

The :adi:`ADALM2000` hardware design includes two gain range settings for the
analog input voltage divider:

* High gain mode: for signals from -2.5 V to +2.5V
* Low gain mode: for signals from -25 V to 25 V

A logic high on EN_SC1_HG turns switch 1 and switch 3 on, selecting high gain mode (gain of HG_1).
A logic high on EN_SC1_LG turns switch 2 and switch 4 on, selecting low gain mode (gain of LG_1).
Where:

.. math::

   HG_1 = \frac{R_{20} + R_{21}}{R_{19} + R_{20} + R_{21}}
         = \frac{200\,\text{K} + 21\,\text{K}}{820\,\text{K} + 200\,\text{K} + 21\,\text{K}}
         = 0.212

.. math::

   LG_1 = \frac{R_{21}}{R_{19} + R_{20} + R_{21}}
         = \frac{21\,\text{K}}{820\,\text{K} + 200\,\text{K} + 21\,\text{K}}
         = 0.020

.. figure:: ../images/inout_div_gainctrl_p.png
   :width: 400px
   :alt: Input divider and gain control stage

   Figure 5. Input divider and gain control stage

Buffers
~~~~~~~

After the input divider stage in the signal chain is the buffer stage. A dual
AD8066 FET input Op Amp is configured as a unity-gain buffer that presents a
high-impedance to the dividers' outputs and drives the following stage. R-C
compensation networks in the figure help to maximize the bandwidth and reduce
peaking (especially at unity gain).

.. figure:: ../images/m2k_sc_buffer.png
   :width: 400px
   :alt: Buffer stage

   Figure 6. Buffer stage

The useful features of the AD8066 are:

* FET input amplifier
* 1 pA input bias current
* Low cost
* High speed: 145 MHz, −3 dB bandwidth (G = +1)
* 180 V/μs slew rate (G = +2)
* Low noise 7 nV/√Hz (f = 10 kHz), 0.6 fA/√Hz (f = 10 kHz)
* Wide supply voltage range: 5 V to 24 V
* Rail-to-rail output
* Maximum offset voltage of 1.5 mV
* Excellent distortion specifications
* SFDR −88 dBc @ 1 MHz
* Low power: 6.4 mA/amplifier typical supply current
* Small packaging: MSOP-8

ADC Drivers
~~~~~~~~~~~

The ADC driver consists of a ADA4940 for each analog input channel. This
fully differential ADC driver is a low noise, low distortion device, with very
low power consumption. Along with the passive components, this stage gives gain
factor equal to 1.3 for the differential signal that comes from the previous
buffer stage and a gain factor equal to 1 for the offset and reference signals.

Another ADA4940 and 2 Schottky diodes are used to provide protection to the ADC
inputs of each channel against voltage levels above the absolute maximum
ratings. In the datasheet of AD9963 the full scale input range of the ADC is
1.56Vpp differential with an absolute maximum rating from -0.3V to 2.1V so the
protection circuit will clamp voltages around these values.

.. figure:: ../images/adc_driver.png
   :width: 400px
   :alt: ADC driver

   Figure 7. ADC driver

References and offset
~~~~~~~~~~~~~~~~~~~~~

Reference and offset voltages are implemented with an AD8567, a dual,
micropower, precision, rail-to-rail input/output amplifier optimized for high
output current capability and large capacitive loads. Other features of this
operational amplifier are:

* low offset voltage (max 350 uV)
* low input bias current (max 20pA)
* GBW : 230 kHz at Av=100
* Unity-gain crossover: 320 kHz
* Single-supply operation: 2.7V to 18V
* Dual-supply operation: ±1.35 V to ±9 V

The reference stage has a 1.2V reference input signal. The reference signal is
amplified with a gain equal to 1.333 before it reaches the ADC driver.

.. figure:: ../images/scope_reference.png
   :width: 400px
   :alt: Scope Amplifier

   Figure 8. Reference Amplifier

In the offset stage, the input signal is generated by AD5625 12-bit nanoDAC.
This signal is amplified with 2.693 before it reaches ADC driver.

.. figure:: ../images/scope_offset.png
   :width: 400px
   :alt: Offset Amplifier

   Figure 9. Offset Amplifier

The reference and offset voltages are derived from an AD5625 nanoDAC, which
uses a 2-wire I2-compatible serial interface.It has single supply operation
(from 2.7V to 5.5V) and is guaranteed monotonic by design.

.. figure:: ../images/ad5625.png
   :width: 400px
   :alt: AD5625

   Figure 10. AD5625

Waveform Generator
------------------

I/V
~~~

The :adi:`AD9963` DACs are a current steering architecture, so it is necessary
to convert the TXIP,TXIN,TXQP,TXQN outputs to a voltage for the AWG frontend.
This operation is performed by an AD8058 dual voltage feedback amplifier. The
output currents from the TXIP and TXIN pins are complementary, meaning that the
sum of the two currents always equals the full-scale current of the DAC. The
digital input code to the DAC determines the effective differential current
delivered to the load. TXIP provides maximum output current when all bits are
high. The output currents vs. DACCODE for the DAC outputs are expressed as

.. math::

   I_{TXIP} = \left( \frac{\text{DACCODE}}{2^N} \right) I_{OUTFS}

where

.. math::

   \text{DACCODE} = 0 \ldots (2^N - 1)

The DAC full-scale output current is regulated by the reference control
amplifier and is determined by the product of a reference current, a
programmable reference resistor, an internal programmable resistor, and a pair
of programmable gain scaling parameters. There are a number of adjustments that
can be made to scale IOUTFS to provide programmability in the output signal
level. There are 2 available ranges for the DAC full scale current: 4 mA full
scale or 1 mA full scale. This current is converted by the AD8058 into voltage
for the last stages of the AWG front end.

.. figure:: ../images/curent_voltage_awg.png
   :width: 400px
   :alt: Current to voltage converter

   Figure 11. Current to voltage converter

The AD8058 has a very low input bias current value (typically 0.5 µA) and is
and is configured as a current to voltage converter such that:

.. math::

   V_+ = V_-

.. math::

   V_- = V_{out} + \left( I_{\text{DAC-AWG1N}} \cdot R_{95} \right)

.. math::

   V_+ = I_{\text{DAC-AWG1P}} \cdot R_{93}

.. math::

   V_{out} = I_{\text{DAC-AWG1P}} \cdot R_{93}
             - I_{\text{DAC-AWG1N}} \cdot R_{95}

The output voltage range of the AD8050  will be different, depending on the DAC
full scale output current:

.. list-table::
   :header-rows: 1
   :widths: 30 40

   * - **Input current (AD8058)**
     - **Output Voltage (AD8058)**
   * - 4 mA FS
     - -0.496 V → 0.496 V
   * - 1 mA FS
     - -0.124 V → 0.125 V

Output stages
~~~~~~~~~~~~~

The AWG reference is generated with the ADR3412 high‑accuracy voltage reference.
The 1.2 V signal is then passed through a buffer implemented with the AD8657.

.. figure:: ../images/awg_reference.png
   :width: 400px
   :align: center
   :alt: AWG reference

   Figure 12. AWG reference

The offset of the signal generator channels is provided by the AD5625 nanoDAC.

.. figure:: ../images/gain_offset_awg.png
   :width: 400px
   :align: center
   :alt: Gain and offset stage of the AWG frontend

   Figure 13. Gain and offset stage of the AWG frontend

Clock and Oscillator
--------------------

The ADF4360-9 is the clock generator used in ADALM2000, with a 20MHz reference
generated by a precision oscillator(Y1). This integrated integer-N synthesizer
and voltage controlled oscillator (VCO) allows a frequency range of between
65 MHz to 400 MHz. The ADF4360-9 is programmed through a 3-wire interface, the
power supply range is 3.0 V to 3.6 V, and a low-power shutdown mode reduces
supply current to 7μA.

.. figure:: ../images/clocking.png
   :width: 500px
   :align: center
   :alt: Oscillator and Clock Generator

   Figure 14. Oscillator and Clock Generator

Digital IO
----------

.. figure:: ../images/digitaliopins.png
   :width: 500px
   :align: center
   :alt: Digital IO Pins

   Figure 15. Digital I/O

Digital IO connections to P1 are shown in the figure above. P1 is the end user
signal connector, with 30 pins corresponding to the input analog channels, the
user power supplies, the signal generator channels, 4 GND pins and digital IO
pins. The Digital IO interface includes 18 pins, 16 of which are the Digital IO
channels and the other two are trigger pins. IO pins are LVCMOS3V3 compatible
and have ESD protection for large currents provided by Schottky Diodes
(D11-D19). Short circuit protection is provided by the PRG18BB221MB1RB PTC
protection devices on the digital lines (RT10-18). These components provide
fault protection at the expense of limiting the bandwidth of the digital pins
slightly when configured as inputs. Similarly, in digital output mode, the 200Ω
resistance and the capacitance of the circuit being driven will limit
bandwidth.

.. note::

   input bandwidth calculation based on 200Ω and 4.4pF + Zynq Cin

.. warning::

   When connecting the digital pins to any external device and the
   :adi:`ADALM2000` is powered off, the ESD protection diodes on the
   :adi:`ADALM2000` will turn on, pulling any signals to ground. Any high logic
   level of the external signal will be reduced to ~ 0.6V.

.. note::

   Would be good to describe a practical series resistance to safely sniff 5V
   logic, considering the unpowered case where the internal 3.3V supply could
   potentially be “dragged” higher than 3.3V

Power Supplies
--------------

User power supplies
~~~~~~~~~~~~~~~~~~~

The user power supplies are implemented with two ADA4805 amplifiers, one in
noninverting configuration for the positive power supply and the other in
inverting configuration for the negative power supply. These amplifiers are
rail-to-rail output, with ultralow pupply current (500µA per amplifier) and
with a typical 0.2 µV/°C offset drift. A shutdown pin allows dynamic management
of the amplifier's supply current. The outputs are guaranteed to source and
sink 58mA, making them suitable for use as an adjustable positive or negative
power supply with a maximum specified load current of 50mA. Compensation
networks allow the amplifier to drive a 1μF output capacitance, providing a
low AC output impedance to the load.

.. figure:: ../images/user_powersupplies.png
   :width: 500px
   :align: center
   :alt: User power supplies

   Figure 16. User power supplies

The ADA4805 shutdown pin is controlled by the SoC through a p-Channel MOSFET.
The device will turn of if the pin is pulled to a voltage with more than 1V
below midsupply.

.. figure:: ../images/enable_supplies.png
   :width: 500px
   :align: center
   :alt: Enable supplies

   Figure 17. Enable supplies

Control signals for the supplies are generated by an AD5627 dual 12 bit
nanoDAC, with an output range of 0-1V corresponding to a range of 0 to 5.02V
for the positive supply and 0 to -5.1V for the negative supply.

.. figure:: ../images/ad5627.png
   :width: 500px
   :align: center
   :alt: AD5627 nanoDAC

   Figure 18. AD5627 nanoDAC

The amplifier used for the positive user power supply has a gain of 5.02:

.. math::

   \text{gain\_pos} = 1 + \frac{R_{161}}{R_{158}}
                    = 1 + \frac{4.02\text{k}}{1\text{k}}
                    = 5.02

For the negative user supply amplifier the gain is -5.1:

.. math::

   \text{gain\_neg} = -\frac{R_{160}}{R_{159}}
                    = -\frac{5.1\text{k}}{1\text{k}}
                    = -5.1

The outputs of the ADA4805s (SUPPLY_POS and SUPPLY_NEG) correspond to the V+
and V- pins on the user connector. Output voltages are also monitored through
scaling circuits with a gains of 1/2 and -1/2 that are then connected to the
AD9963's AUXIO pins. The monitoring function is useful for detecting supply
overcurrent and / or short circuits in the circuit being powered.

.. figure:: ../images/supply_monitor.png
   :width: 500px
   :align: center
   :alt: User supply signals division

   Figure 19. User supply signals division

The positive supply monitoring signal is obtained with a resistive divider with
a gain of 1/2 and the negative supply monitor signal is obtained with an
inverting amplifier with gain -1/2:

.. math::

   G = -\frac{R_{136}}{R_{139}}
     = -\frac{2\text{k}}{4.02\text{k}}
     = -\frac{1}{2}

Internal power supplies
-----------------------

Analog Power supplies
~~~~~~~~~~~~~~~~~~~~~

There are 3 voltage rails in the positive analog section derived from the main
USB connector or auxiliary USB power connector. An ADP2370 synchronous buck
regulator provides the 3.3V voltage rail. This is a high efficiency, low
quiescent current dc-to-dc converter which uses a proprietary high speed
current mode and constant frequency PWM control scheme for excellent stability
and transient response. This rail is used to supply the clock generator, the
ADC drivers and the current-to-voltage converters of the AWG front end.

.. figure:: ../images/3v3_rail.png
   :width: 500px
   :align: center
   :alt: 3.3V positive voltage rail

   Figure 20. 3.3V positive voltage rail

An ADP1614 step-up converter provides the 6V voltage rail. This is a dc-to-dc
switching converter with an integrated power switch capable of providing an
output voltage up to 20V. The device operates in a current-mode pulse-width
modulation with up to 94% efficiency. Due to this architecture is allowed
excellent transient response and easy noise filtering. This rail is used to
supply the user power supply amplifiers, the switches used in the input signal
chain, and the amplifiers of the AWG front end.

.. figure:: ../images/6v_rail.png
   :width: 500px
   :align: center
   :alt: 6V positive voltage rail

   Figure 21. 6V positive voltage rail

An LT1761 LDO Micropower Regulator provides the low-noise 4V rail used to
supply the amplifiers from the buffer stage of the input signal chain. This is
a low dropout regulator with low quiescent and shutdown current and with an
input voltage range of 1.8V to 20V, output current of 100mA, and a dropout
voltage of 300mV.

.. figure:: ../images/4v_rail.png
   :width: 500px
   :align: center
   :alt: 4V positive voltage rail

   Figure 22. 4V positive voltage rail

The negative analog section has 3 voltage rails, -6V, -3.3V and -5V. An ADP5074
inverting regulator provides -6V from the 5V USB input. It has a wide input
voltage range (from 2.85V to 15V) and its integrated main switch enables the
generation of an adjustable negative output down to 39V below the input voltage.
This rail is used to supply the amplifiers of the user power supplies, the
switches used in the input signal chain, and the amplifiers of the AWG front
end.

.. figure:: ../images/m6v_rail.png
   :width: 500px
   :align: center
   :alt: -6V voltage rail

   Figure 23. -6 V voltage rail

An ADP7182 regulates the -6V rail to -3.3V. This device is is a CMOS, low
dropout (LDO) linear regulator that operates from −2.7 V to −28 V and provides
up to −200 mA of output current. This rail is used to supply the ADC drivers
and the current-to-voltage converters of the AWG front end.

.. figure:: ../images/m3v3_rail.png
   :width: 500px
   :align: center
   :alt: -3.3V voltage rail

   Figure 24. -3.3 V voltage rail

An LT1964ES5-5 provides the -5V rail. This device is a low-noise, Low Dropout
Negative micropower Regulator with a fixed output voltage of -5V capable of
supplying 200mA of output current. This rail is used to supply the amplifiers
from the buffer stage of the input signal chain.

.. figure:: ../images/m5v_rail.png
   :width: 500px
   :align: center
   :alt: -5V voltage rail

   Figure 25. -5 V voltage rail

Digital Power supplies
~~~~~~~~~~~~~~~~~~~~~~

There are 4 supply rails for the digital section of the board. These rails are
provided by two ADP2114 Dual Step-Down DC-to-DC Regulators. This device is a
synchronous step-down switching regulator with two independent outputs. It
provides high efficiency(up to 95%) and operates at switching frequencies up to
2MHz. The input voltage range is 2.75V to 5.5V and the output is either fixed
or adjustable.
One of the ADP2114s is used to provide 1.8V for the ADC/DAC and 1.35V for the
DDR3 memory.

.. figure:: ../images/digital_1v8_1v35.png
   :width: 500px
   :align: center
   :alt: 1.8V and 1.35V digital voltage rail

   Figure 26. 1.8V and 1.35 digital voltage rail

The other ADP2114 is used to provide the 1.0V VCCPINT rail, which supplies the
SoC, and the 3.3V rail which supplies the ADC and DACs.

.. figure:: ../images/digital_3v3.png
   :width: 500px
   :align: center
   :alt: 1V and 3.3V digital voltage rail

   Figure 27. 1V and 3.3V digital voltage rail

USB Controller
--------------

A Microchip USB3320 Hi-Speed USB 2.0 transceiver provides a USB PHY and ULPI
connectivity to the SoC. The USB interface provides the following functions:

* USB 2 (480 Mbits/seconds)
* libiio USB device for communicating to the device
* Network device

   * `Remote Network Driver Interface Specification (RNDIS) <https://en.wikipedia.org/wiki/RNDIS>`__
   * This will enumerate with the 192.168.2.1 IP address by default.

* USB serial device

   * provides access to the Linux console on the M2K device via
     `USB Communication Device Class Abstract Control Model (USB CDC ACM) <https://en.wikipedia.org/wiki/USB_communications_device_class>`__
     specification

* Mass Storage Device : this will appear to the host as a disk, where you can
  find links for software uploads, and the serial number of the device.

.. figure:: ../images/usb_phy.png
   :width: 500px
   :align: center
   :alt: USB PHY

   Figure 28. USB PHY

Memory
------

System memory is a Micron `MT41K256M16TW-107 <https://www.micron.com/products/memory/dram-components/ddr3-sdram/part-catalog/part-detail/mt41k256m16tw-107>`__
4Gbyte, 1066 Mbps, DDR3L low voltage SDRAM. This memory is used for temporary
storage of streaming data as well as the operating system.

.. figure:: ../images/ddr3.png
   :width: 500px
   :align: center
   :alt: USB PHY

   Figure 29. DDR3 memory

Firmware is stored in a Micron `MT25QU256ABA8E12-1SIT <https://www.micron.com/products/storage/nor-flash/serial-nor/part-catalog/part-detail/mt25qu256aba8e12-1sit>`__
265Mbyte, 90MBps Serial Flash. This device has an endurance of 100,000 ERASE
cycles minimum (don't update the firmware more times than this).

.. figure:: ../images/flash.png
   :width: 500px
   :align: center
   :alt: USB PHY

   Figure 30. Flash memory

SoC
---

A Xilinx :xilinx:`Zynq` XC7Z010-1CLG225C System on Chip provides processing and
programmable logic functionality with the following specifications:

* FPGA

   * Logic Cells: 28k
   * Block RAM: 2.1Mb
   * DSP Slices 80

* ARM Processing System

   * Single-core ARM® Cortex™-A9 MPCore™
   * 667 MHz

* USB 2.0 (included in the Zynq)

   * streams up to 4MSPS with no dropped samples

Additional information may be found at
`Zynq-7000 All Programmable SoC Overview <https://docs.amd.com/v/u/en-US/ds190-Zynq-7000-Overview>`__
and
`Datasheet <https://docs.amd.com/v/u/en-US/ds187-XC7Z010-XC7Z020-Data-Sheet>`__

Power
-----

The board is completely self powered from USB and has two USB connectors: One
for power and data and one for optional power.

.. figure:: ../images/usb_conn.png
   :width: 500px
   :align: center
   :alt: USB connectors

   Figure 31. USB connectors

Bus power from both USB connectors are pass through an LTC4415 dual monolithic
ideal diodes with adjustable current limit, where the data USB bus current
limit is set to 1A and the power USB bus current limit is set to 2A. The two
ideal diodes are independently enabled and prioritized using inputs EN1 and
/EN2 such that the power USB connector has the higher priority.

.. figure:: ../images/power_selector.png
   :width: 500px
   :align: center
   :alt: Power selector

   Figure 32. Power selector

Features
--------

Analog Inputs

* 2 channels
* differential channel type
* 12-bit resolution
* 100 MS/s sample rate
* Scope scales: 1mV to 10V/div
* ±25V (±50V differential) input range
* 64k samples buffer size/channel
* Trigger: rising/falling edge, high/low, hysteresis
* Sampling modes: average, decimate, min/max
* FFTs, XY plots and histrogram
* Math channels with complex functions
* Cursors with advanced data measurements
* Captured data files can be exported in standard formats (.csv, .txt)

Signal Generator

2 channels
* Single ended channel type
* 12-bit resolution
* Sample rate: 150 MS/s
* AC amplitude (max): ±5 V
* DC Offset (max): ±5 V
* Slew rate (10V step): 400V/µs
* 64k samples buffer size/channel
* Sine, Square, Triangle, Trapezoidal, Rising/Falling Ramp Sawtooth waveforms
* Noise Waveforms (Uniform, Gaussian, Laplacian, Impulse)
* Custom waveforms using standard tools (e.g. Excel)

Pattern Generator

* 16 channels
* Sample rate: 100 MS/s
* Custom pattern buffer/channel: up to 500K samples
* Output logic standard: LVCMOS (3.3V)
* Output type/channel: Push-Pull(PP)/Open-Drain(OD)
* Import patterns using standard file formats (.csv, .txt)
* Customized visualization for signals and buses

Logic Analyzer

* Channels: 16
* Sample rate (real time): 100 MS/s
* 500K samples buffer size/channel
* Input logic: LVCMOS (3.3V, up to 5V)
* Trigger options: auto/normal with multiple trigger logic options
* External trigger available
* Decoders for multiple communication protocols (SPI, I2C, UART, Parallel,
  etc.)
* Export data using standard formats (.csv, .txt)

Digital I/O

* Channels: 16 (shared)
* Input logic: LVCMOS (3.3V, 5V tolerant)
* Output logic standard: LVCMOS (3.3V)
* Virtual I/O devices (switches & displays)
* Individual/Grouped Customized visualization of channels

Power Supplies

* 1 Positive output
* 1 Negative output
* Voltage range: 0.5V…5V and -0.5V…-5V
* Independent/Tracking modes for the 2 power supplies

Network Analyzer

* Shared with following instruments: Oscilloscope, Signal Generator
* Frequency sweep range: 1Hz to 30MHz
* Samples count: 10 → 1000
* Settable input amplitude and offset
* Signal recorded via analog input at each frequency
* Available diagrams: Bode, Nichols, or Nyquist
* Export data using standard formats (.csv, .txt)

Voltmeter

* Channels (shared with scope): 2
* Channel type: differential
* Measurements: DC and AC
* Resolution: 12-bit
* Input range: ±25V (±50V div)
* Peak Hold
* History of recorded values
* Option for Data logging

Spectrum Analyzer

* 2 channels shared with Oscilloscope
* Power spectrum algorithms: FFT
* Frequency range modes: center/span, start/stop
* Frequency scale: linear
* Vertical axis options: voltage-peak, VRMS, dBV, dBu, dBFS
* Window types: flat top, rectangular, triangular, hamming, hann,
  blackman-harris, kaiser
* 5 customizable markers
* Data file export using standard formats (.csv, .txt)

Other Features

* USB power option; all needed cables included.
* External supply option: 5V, 2.5A
* Data transfer via high-speed USB 2.0 interface
* Trigger in allows multiple instruments to be linked
* Individual configuration of instruments
* Export/import instruments configuration

Other Resources
---------------

* :ref:`ADALM2000 for End Users <m2k users>`
* :dokuwiki:`ADALM2000 Based Lab Activity Material, Electronics I and II </university/courses/electronics/labs>`
* Software:

   * :external+scopy:doc:`Scopy <index>`
   * :dokuwiki:`ALICE Active Learning Interface (for) Circuits (and) Electronics for M2K </university/tools/m2k/alice/users-guide-m2k>`
