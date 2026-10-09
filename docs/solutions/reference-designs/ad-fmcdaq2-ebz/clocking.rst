.. _ad-fmcdaq2-ebz clocking:

AD-FMCDAQ2-EBZ Clocking
===========================================

Overview
--------

The :adi:`AD9523-1` is responsible for generating and distributing all clock
signals used on the AD-FMCDAQ2-EBZ platform.

The AD-FMCDAQ2-EBZ platform only uses the second PLL of the AD9523-1 with the
reference for the PLL being sourced from a external 125 MHz crystal. The PLL2
VCO has a locking range of 2940 MHz to 3100 MHz, with the external reference
being 125 MHz the nominal output frequency of the VCO is 3000 MHz.

The output of the PLL VCO is down divided to the target frequencies in two
steps. First it is divided by either 3, 4 or 5, which gives a frequency of 1000
MHz, 750 MHz or 600 MHz respectively. This is the master clock frequency for the
data converter system and shared between the DAC and ADC data path, all
generated clocks are based of this master clock.

The master clock is distributed to each clock output and further down divided by
an integer divider in the range of 1-1024. On the AD-FMCDAQ2-EBZ platform 8
different clocks are generated this way, 4 each for the DAC and ADC datapath.

============ ==========================
Clock Output Function
============ ==========================
OUT1         DAC converter clock
OUT4         ADC FPGA reference clock
OUT5         ADC converter SYSREF clock
OUT6         ADC FPGA SYSREF clock
OUT7         DAC FPGA SYSREF clock
OUT8         DAC converter SYSREF clock
OUT9         DAC FPGA reference clock
OUT13        ADC converter clock
Other        Unused
============ ==========================

The ADC and DAC converter clocks are the reference clock for the ADC and DAC
respectively and determine the sampling rate of the converter. If a
deterministic latency relationship between the DAC and ADC datapath is required
the DAC and ADC clock need to be in a (sub-)harmonic relationship to each other,
otherwise their relationship can be chosen freely.

The DAC has built-in interpolation filters that allow interpolation by a factor
of 2, 4 or 8. The interpolation factor and the DAC converter sample-rate decide
the DAC data-input-rate. The data-input-rate is equal to the sample-rate divided
by the interpolation factor.

The ADC has built-in decimation filters that allow interpolation by a factor of
2, 4, 8 or 16. The decimation factor and the ADC converter sample-rate decide
the ADC data-output-rate. The data-output-rate is equal to the sample-rate
divided by the decimation factor.

The JESD204 lane rates depend on the data-output/input-rates. On the
AD-FMCDAQ2-EBZ both for the ADC and the DAC the lane-rate is equal to 10 times
the data-rate.

The ADC FPGA reference clock is the reference clock for the JESD204
clock-data-recovery (CDR) circuit as well the ADC data path inside the FPGA.
Similarly the DAC FPGA reference clock is the reference clock for the JESD204
transmit PLL and the DAC data path inside the FPGA. These clocks should be set
to the JESD204 lane-rate divided by 20.

The SYSREF clocks are used for synchronization and to establish deterministic
latency between the different components. The SYSREF clock must be a integer
multiple of the local-multi-frame-clock (LMFC). The LMFC is a clock that is
generated internally in the converters and FPGA and on the AD-FMCDAQ2-EBZ
platform its rate is 1/32 of the converter data-input/output-rate. This means
the SYSREF clock frequency must be integer down divided of the converter
data-rate / 32 (I.e. data-rate / {32, 64, 96, 128, ...}).

The SYSREF clocks going to the converter and the FPGA must be configured for the
same frequency. If a deterministic latency relationship between the DAC and ADC
datapath is required the DAC and ADC SYSREF signals must be configured for the
same frequency, otherwise the DAC and ADC datapath SYSREF clocks can be
configured with different frequencies.

+-----------------------+-------------------------------------------------------+--------------------------------------+
| Clock                 | Frequency range                                       | Comments                             |
+=======================+=======================================================+======================================+
| PLL2 VCO              | 3000 MHz                                              | Tuning range of 2940 MHz to 3100 MHz |
+-----------------------+-------------------------------------------------------+--------------------------------------+
| Master clock          | 1000 MHz, 750 MHz, 600 MHz                            | PLL2 VCO divided by 3, 4 or 5        |
+-----------------------+-------------------------------------------------------+--------------------------------------+
| ADC converter clock   | ≥ 312.5 MHz, ≤ 1000 MHz, Master clock / N\ :sub:`ADC` |                                      |
+-----------------------+-------------------------------------------------------+--------------------------------------+
| ADC SYSREF clock      | ADC converter clock / (N\ :sub:`ADC_SYSREF` \* 32)    |                                      |
+-----------------------+-------------------------------------------------------+--------------------------------------+
| DAC converter clock   | ≥ 200 MHz, ≤ 1000 MHz, Master clock / N\ :sub:`DAC`   |                                      |
+-----------------------+-------------------------------------------------------+--------------------------------------+
| DAC SYSREF clock      | DAC converter clock / (N\ :sub:`DAC_SYSREF` \* 32)    |                                      |
+-----------------------+-------------------------------------------------------+--------------------------------------+
| ADC JESD204 lane rate | ADC converter clock / ADC decimation factor \* 10     |                                      |
+-----------------------+-------------------------------------------------------+--------------------------------------+
| DAC JESD204 lane rate | DAC converter clock / DAC interpolation factor \* 10  |                                      |
+-----------------------+-------------------------------------------------------+--------------------------------------+

Examples
--------

fDAC = 1000 MSPS, fADC = 1000 MSPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the default AD-FMCDAQ2-EBZ configuration with both converters running at
the maximum supported samplerate of 1 GSPS.

======================== ========== ===============
Clock                    Frequency  Divider setting
======================== ========== ===============
Master clock             1000 MHz   3
ADC converter clock      1000 MHz   1
ADC FPGA reference clock 500 MHz    2
ADC SYSREF clock         7.8125 MHz 128
ADC FPGA SYSREF clock    7.8125 MHz 128
ADC JESD204 lane rate    10 Gbps
DAC converter clock      1000 MHz   1
DAC FPGA reference clock 500 MHz    2
DAC SYSREF clock         7.8125 MHz 128
DAC FPGA SYSREF clock    7.8125 MHz 128
DAC JESD204 lane rate    10 Gbps
======================== ========== ===============

fDAC = 250 MSPS, fADC = 375 MSPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Non-harmonic DAC and ADC sampling rate (No deterministic latency between DAC and
ADC datapath).

======================== ============= ===============
Clock                    Frequency     Divider setting
======================== ============= ===============
Master clock             750 MHz       4
ADC converter clock      375 MHz       2
ADC FPGA reference clock 187.5 MHz     4
ADC SYSREF clock         2.9296875 MHz 256
ADC FPGA SYSREF clock    2.9296875 MHz 256
ADC JESD204 lane rate    3.75 Gbps
DAC converter clock      250 MHz       3
DAC FPGA reference clock 125 MHz       6
DAC SYSREF clock         1.953125 MHz  384
DAC FPGA SYSREF clock    1.953125 MHz  384
DAC JESD204 lane rate    2.5 Gbps
======================== ============= ===============

Replacing the Crystal Oscillator
--------------------------------

On the AD-FMCDAQ2-EBZ platform the reference clock signal for the AD9523-1 PLL2
is provided by a crystal oscillator (XO). The default populated crystal
oscillator has a output frequency of 125 MHz, this results in a nominal AD9523-1
VCO frequency of 3 GHz, all other clock signals are integer down-divided
versions of the signal.

Other VCO frequencies are possible by replacing the XO with a suitable
replacement producing a different frequency. Replacing the XO might require
changing the VCO feedback divider settings to produce a valid VCO frequency. The
VCO frequency must be in the range of 2940 MHz to 3100 MHz, otherwise the PLL2
will not lock.

.. image:: images/ad9523_pll2.png
   :align: right

The reference frequency can optionally be divided by the R2 (1-32) reference
divider or multiplied by 2 using the frequency doubler. The result of this is
the phase-frequency-detector (PFD) input frequency. The maximum PFD input
frequency is 259 MHz. If the reference frequency exceeds this value the
reference divider must be used to bring it into a valid range.

``fPFD`` = ``fReference`` / ``R2`` \* ``frequency_doubler``

The VCO frequency is the PFD input frequency multiplied by the VCO feedback
divider (N2).

``fVCO`` = ``fPFD`` \* ``N2``

The feedback divider is the combination of two counters, the A and B counter.
These are the settings that are programmed to the AD9523-1 configuration
registers.

``N2`` = ``4`` \* ``B`` + ``A``

Rearranging these formulas it is possible to compute the A and B counter
settings from a known reference and a desired VCO frequency.

``N2`` = ``fVCO`` / ``fPFD``

``A`` = ``N2`` % ``4``

``B`` = ``N2`` / ``4``

Example: fXO = 122.88 MHz, fVCO = 2949.12 MHz
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example the frequency doubler is bypassed and the reference divider is
set to 1. That means the PFD input frequency is equal to the reference
frequency.

``N2`` = ``fVCO`` / ``fPFD`` => ``N2`` = ``2949.12`` / ``122.88`` = ``24``

``A`` = ``N2`` % ``4`` => ``A`` = ``24`` % ``4`` = ``0``

``B`` = ``N2`` / ``4`` => ``B`` = ``24`` / ``4`` = ``6``

================================ ========
Configuration Parameter          Setting
================================ ========
PLL2 reference divider (R2)      1
PLL2 reference frequency doubler Disabled
PLL2 feedback A divider          0
PLL2 feedback B divider          6
================================ ========

Modifying the Clock Configuration
---------------------------------

Linux
~~~~~

On Linux the default clock configuration is supplied through the `devicetree
<https://www.devicetree.org/>`_.

The devicetree file that is used for the AD-FMCDAQ2-EBZ and contains the clock
configuration is called :git-linux:`arch/arm/boot/dts/adi-daq2.dtsi`. This file
contains nodes for the :git-linux:`AD9523-1 <arch/arm/boot/dts/adi-daq2.dtsi#L8>`, the :git-linux:`AD9144 <arch/arm/boot/dts/adi-daq2.dtsi#L105>` and the :git-linux:`AD9680 <arch/arm/boot/dts/adi-daq2.dtsi#L120>`. Each node contains properties that
describe the hardware setup and provide default configuration parameters. For
information on how to edit devicetree please see
:doc:`Tips & Tricks - Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`.

To change the clocking configuration the properties of the AD9523-1 node can be
modified. The following lists the most important properties for the
AD-FMCDAQ2-EBZ and their corresponding hardware setting. The function of each of
these settings and how to choose their value has been discussed above. For more
information refer to the :external+linux:ref:`AD9523-1 driver documentation <ad9523>`.

=============================== ========================
Hardware configuration          Property name
=============================== ========================
Frequency of the external VCXO  ``adi,vcxo-freq``
PLL2 reference divider (R2)     ``adi,pll2-r2-div``
PLL2 feedback divider A counter ``adi,pll2-ndiv-a-cnt``
PLL2 feedback divider B counter ``adi,pll2-ndiv-b-cnt``
PLL2 VCO output divider (M1)    ``adi,pll2-vco-diff-m1``
=============================== ========================

Each clock output of the AD9523-1 has its own subnode in the devicetree. This
subnode is used to select the configuration of the clock output. A clock output
node is identified by its ``reg`` property which corresponds to the clock output
channel number. E.g. the on the AD-FMCDAQ2-EBZ the ADC converter clock is
sourced from output 13, so the node for the ADC converter clock has its ``reg``
property set to 13. For a list of all used clock outputs and their function see
above.

For changing the clocking configuration only two of the properties need to be
changed, all other properties should remain at their default value.

====================== =======================
Hardware configuration Property name
====================== =======================
Output divider         ``adi,channel-divider``
Output phase           ``adi,divider-phase``
====================== =======================

**Example: Change the DAC converter clock divider to 4**

::

       ad9523_0_c1:channel@1 {
           reg = <1>;
           adi,extended-name = "DAC_CLK";
           adi,driver-mode = <3>;
           adi,divider-phase = <1>;
           adi,channel-divider = <4>;
   //      adi,output-dis;
       };

Based on the data output and input rates the converter drivers will
automatically calculate the JESD204 lane rate and propagate the configuration to
the JESD204 receiver and transmitter drivers. These drivers will update the
high-speed transceiver configuration accordingly. This means no additional
manual configuration is necessary to setup the JESD204 link.
