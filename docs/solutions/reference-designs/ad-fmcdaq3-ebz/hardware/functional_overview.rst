.. _ad-fmcdaq3-ebz hardware functional_overview:

.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq3-ebz/hardware/functional_overview

.. _ad_fmcdaq3_ebz functional overview:

AD-FMCDAQ3-EBZ (Rev C) Functional Overview
==========================================

The system consists of four functional partitions - transmit path, receive path,
clocking and power supply. A functional block diagram of the system's main
components and signal paths is given below. The power tree and voltage
monitoring are included in the Power section below.

.. image:: ./../images/block_diagram_fmcdaq3.jpg
   :width: 900

Transmit
--------

Key component:

+---------------+-----------------------------------------------------------------------------------------------------------------+
| :adi:`AD9152` | Dual, 16-Bit, 2500 MSPS, TxDAC+® Digital-to-Analog JESD204B Converter with offset, phase and gain compensation. |
+---------------+-----------------------------------------------------------------------------------------------------------------+

The reference design generates the signals for AD9152 either from an internal
DDS or external memory (via VDMA). The internal DDS consists of four independent
signal generators with programmable phase offset and frequency. These four
signal generators are paired to create two tones that are interleaved and driven
to the DAC.

Receive
-------

Key component:

+---------------+---------------------------------------------------------------------+
| :adi:`AD9680` | 14-Bit, 1250 MSPS, Dual Analog-to-Digital JESD204B Converter (ADC). |
+---------------+---------------------------------------------------------------------+

The reference design transfers the received data to DDR via DMA. An optional
off-line FFT core may be used to generate a spectrum plot.

Clocking
--------

Key component:

+---------------+---------------------------------------------------------------+
| :adi:`AD9528` | Low Jitter Clock Generator (1MHz to 1.25GHz) with 14 Outputs. |
+---------------+---------------------------------------------------------------+

The system is clocked through an on board crystal (100MHz). The clock path
mainly consists the :adi:`AD9528` which up converts this signal to ~3.7GHz, and
then divides this back down to any integer divider of this ~3.7GHz output.

The default reference design that ADI provides does the following:

-  Crystal generates a fixed clock frequency of 100MHz.
-  This clock is sent to the AD9528.
-  The AD9528 takes this, and creates:

   -  1233 MHz for the DAC sample rate
   -  1233 MHz for the ADC sample rate
   -  616 MHz for the reference clocks to FPGA

These clocks can be changed, but the key thing to remember is that the AD9528
drives both the ADC and DAC. The AD9528 has various clock banks. The best thing
to do if you are interested in the details of this, is to get the
:adi:`Eval board software <EVAL-AD9528>`, and play with the different
settings (you don't need a demo board connected to run the software).

Power
-----

The system-level power tree .ltp3 file simulated in
:adi:`LTpowerPlanner <ltpowercad>` is given below.
:dokuwiki:`220309_fmcdaq3_power.zip <_media/resources/eval/user-guides/ad-fmcdaq3-ebz/hardware/220309_fmcdaq3_power.zip>`

Key components in the power tree:

+-----------------+---------------------------------+
| :adi:`ADP2384`  | 4A, 20V step-down switcher.     |
+-----------------+---------------------------------+
| :adi:`ADP7104`  | High accuracy, 500mA LDO        |
+-----------------+---------------------------------+
| :adi:`ADP150`   | Ultra low noise, 150/200 mA LDO |
+-----------------+---------------------------------+
| :adi:`ADP1741`  | Low VIN, 2A LDO                 |
+-----------------+---------------------------------+
| :adi:`ADP1755`  | Low VIN, 1.2A LDO               |
+-----------------+---------------------------------+
| :adi:`ADM7154`  | Low VIN, 600mA LDO              |
+-----------------+---------------------------------+

The board receives all the power from the FPGA board through FMC.

The monitoring function of board's DC voltages is accomplished using
:adi:`AD7291` SAR ADC. The block diagram of the ADC and the corresponding
monitored voltages is shown below.

.. image:: ./../images/fmcdaq3_monitoring_adc.jpg
   :width: 900

**VADJ** pin from FMC connector is used for supplying the translators VCCA
voltage. Supported voltage values of this pin are: 1.2V/1.5V/1.8V/2.5V/3.3V.

For differential to single-ended conversion and for minimizing 2nd harmonic
distortion in transmitting and receiving, a double-balun configuration is used
for TX and RX as front-end interface. More topology detail and information about
the front-end design insights are presented in the following articles:

#. :adi:`"Wideband A/D Converter Front-End Design Considerations: When to Use a Double Transformer Configuration" by Rob Reeder and Ramya Ramachandran <analog-dialogue/articles/wideband-a-d-converter-front-end-design-considerations.html>`

#. :adi:`"Ask The Application Engineer—36: Wideband A/D Converter Front-End Design Considerations II: Amplifier-or Transformer Drive for the ADC?" by Rob Reeder and Jim Caserta <analog-dialogue/articles/wideband-adc-design-considerations-2.html>`

#. :adi:`"Transformer-Coupled Front-End for Wideband A/D Converters" by Rob Reeder <analog-dialogue/articles/transformer-coupled-front-end-a-d-converters.html>`

