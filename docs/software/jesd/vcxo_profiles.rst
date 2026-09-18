.. imported from: https://wiki.analog.com/resources/eval/user-guides/rf-trx-vcxo-and-profiles

.. _software vcxo-profiles:

Changing the VCXO Frequency and Updating the RF Transceiver Profile
================================================================================

About
--------------------------------------------------------------------------------

The evaluation boards for :adi:`AD9371`, :adi:`ADRV9009` and :adi:`ADRV9008`
contain an onboard VCXO (Voltage Controlled Crystal Oscillator) and the
:adi:`AD9528` clock generation/distribution chip.

The VCXO and PLL2 in the :adi:`AD9528` generate a VCO clock from which the
device clocks for the RF transceiver, FPGA reference clocks, and SYSREF
are derived. Common device clock frequencies include 122.88 MHz, 153.6 MHz,
184.32 MHz, 245.76 MHz, and 307.2 MHz.

Users may need to change the VCXO when:

- The desired device clock cannot be expressed as a rational fraction of the
  default 122.88 MHz VCXO (e.g. 125 MHz, 133.33 MHz, 250 MHz, 266.66 MHz for
  baseband rates of 50, 100, 200 MSPS)
- Synchronization via AD9528 PLL1 requires a reference clock that is not
  rationally related to 122.88 MHz
- An alternative VCXO with better jitter or stability characteristics is being
  evaluated

Procedure
--------------------------------------------------------------------------------

Physical VCXO replacement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Replace the onboard VCXO component with one of the desired frequency (e.g.
80 MHz).

Alternatively, bypass the VCXO and PLL1 and directly feed an external clock
into the :adi:`AD9528` via the ``REF_CLK_IN`` SMA connector. This requires
resistor and capacitor modifications outlined in the evaluation board
schematics. The device tree configuration for bypass mode:

.. code-block:: dts

   &clk0_ad9528 {
   	adi,pll1-bypass-enable;
   	adi,osc-in-diff-enable;
   };

VCXO frequency in the device tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the new VCXO frequency in the :adi:`AD9528` device tree node. See
:external+linux:ref:`ad9528` for detailed driver documentation.

.. code-block:: dts

   &clk0_ad9528 {
   	adi,vcxo-freq = <80000000>;
   };

Clock distribution planning (PLL2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PLL2 VCO frequency must fall within one of these valid ranges:

- 1150.000 MHz to 1341.666 MHz
- 862.500 MHz to 1006.250 MHz
- 690.000 MHz to 805.000 MHz

**Manual configuration** — specify divider values directly:

.. code-block:: dts

   &clk0_ad9528 {
   	adi,vcxo-freq = <80000000>;
   	adi,pll2-vco-div-m1 = <3>;
   	adi,pll2-n2-div = <15>;
   	adi,pll2-r1-div = <1>;
   };

**Automatic configuration** — specify only the target M1 frequency and let the
driver compute the dividers:

.. code-block:: dts

   &clk0_ad9528 {
   	adi,vcxo-freq = <80000000>;
   	adi,pll2-m1-frequency = <1200000000>;
   };

RF transceiver profile updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new RF transceiver profile must be generated to match the new device clock
frequency. Use the appropriate MATLAB tool:

- :adi:`MATLAB Profile Generator for AD9371 <media/en/evaluation-boards-kits/evaluation-software/AD9371-TES.zip>`
- :adi:`MATLAB Filter Wizard / Profile Generator for ADRV9009 <media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`

When choosing the device clock frequency, ``Lane rate / 40`` is recommended as a
practical starting point. For example, with the following JESD204 configuration:

.. list-table::
   :header-rows: 1

   * - Path
     - IQ Rate (MSPS)
     - M
     - L
     - N'
     - S
     - Lane Rate (Mbit/s)
   * - TX
     - 240
     - 4
     - 4
     - 16
     - 1
     - 4800
   * - RX
     - 120
     - 4
     - 2
     - 16
     - 1
     - 4800
   * - ORX
     - 240
     - 2
     - 2
     - 16
     - 1
     - 4800

The device clock = lane rate / 40 = 120 MHz, which maps cleanly to a 80 MHz
VCXO with PLL2 M1 frequency of 1200 MHz.

Complete device tree example
--------------------------------------------------------------------------------

Example for :adi:`AD9371` with 80 MHz VCXO on :xilinx:`ZC706`:

.. code-block:: dts

   #include "zynq-zc706-adv7511-adrv9371.dts"

   &clk0_ad9528 {
   	adi,vcxo-freq = <80000000>;
   	adi,pll2-m1-frequency = <1200000000>;
   	/delete-property/ adi,pll2-ndiv-a-cnt;
   	/delete-property/ adi,pll2-ndiv-b-cnt;
   	/delete-property/ adi,pll2-vco-div-m1;
   	/delete-property/ adi,pll2-n2-div;
   	/delete-property/ adi,pll2-r1-div;
   	adi,pll1-feedback-div = <8>;
   };

   &trx0_ad9371 {
   	adi,clocks-clk-pll-vco-freq_khz = <9600000>;
   	adi,clocks-device-clock_khz = <120000>;
   	adi,obs-settings-obs-rx-channels-enable = <3>;
   	adi,rx-profile-iq-rate_khz = <120000>;
   	adi,rx-profile-rf-bandwidth_hz = <80000000>;
   	adi,rx-profile-rx-fir-gain_db = <(0)>;
   	adi,rx-profile-rx-fir-num-fir-coefs = <48>;
   	adi,rx-profile-rx-fir-coefs = /bits/ 16
   		<(0)(0)(1)(2)(-3)(-10)(12)(28)(-33)(-71)(81)(154)
   		(-174)(-305)(343)(561)(-635)(-989)(1155)(1750)(-2330)
   		(-4059)(4644)(16559)(16559)(4644)(-4059)(-2330)(1750)
   		(1155)(-989)(-635)(561)(343)(-305)(-174)(154)(81)(-71)
   		(-33)(28)(12)(-10)(-3)(2)(1)(0)(0)>;
   	adi,rx-profile-custom-adc-profile = /bits/ 16
   		<(574)(382)(201)(98)(1280)(342)(1553)(180)(1285)(67)
   		(784)(33)(48)(38)(23)(189)>;

   	adi,obs-profile-iq-rate_khz = <240000>;
   	adi,obs-profile-rf-bandwidth_hz = <160000000>;
   	adi,obs-profile-rx-bbf-3db-corner_khz = <80000>;
   	adi,obs-profile-rx-fir-gain_db = <6>;
   	adi,obs-profile-rx-fir-num-fir-coefs = <24>;
   	adi,obs-profile-rx-fir-coefs = /bits/ 16
   		<(-51)(-107)(90)(-29)(-72)(128)(-11)(-279)(178)(-46)
   		(-2343)(21563)(-2343)(-46)(178)(-279)(-11)(128)(-72)
   		(-29)(90)(-107)(-51)(0)>;
   	adi,obs-profile-custom-adc-profile = /bits/ 16
   		<(499)(386)(201)(98)(1280)(534)(1741)(601)(1423)(456)
   		(857)(27)(48)(38)(25)(205)>;
   	adi,obs-settings-custom-loopback-adc-profile = /bits/ 16
   		<(581)(379)(201)(98)(1280)(304)(1544)(157)(1288)(59)
   		(787)(34)(48)(39)(23)(189)>;

   	adi,tx-profile-dac-div = <1>;
   	adi,tx-profile-iq-rate_khz = <240000>;
   	adi,tx-profile-rf-bandwidth_hz = <160000000>;
   	adi,tx-profile-tx-bbf-3db-corner_khz = <80000>;
   	adi,tx-profile-tx-dac-3db-corner_khz = <160000>;
   	adi,tx-profile-tx-fir-gain_db = <6>;
   	adi,tx-profile-tx-fir-num-fir-coefs = <16>;
   	adi,tx-profile-tx-fir-coefs = /bits/ 16
   		<(-48)(290)(-51)(-251)(577)(167)(-3254)(21872)
   		(-3254)(167)(577)(-251)(-51)(290)(-48)(0)>;
   };

Extracting filter coefficients from profile XML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following script can extract filter and ADC profile coefficients from
the XML profile files generated by the MATLAB tools:

.. code-block:: bash

   #!/bin/bash
   while IFS='' read -r line || [[ -n "$line" ]]; do
   	if [[ $line == *"filter"* ]]; then
   		echo
   		start="1"
   	fi
   	if [[ $line == *"adc-profile"*"num"* ]] || \
   	   [[ $line == *"AdcProfile"*"num"* ]]; then
   		echo
   		start="1"
   	fi
   	if [[ $line == *"</"* ]]; then
   		echo
   		start="0"
   	fi
   	if [ "$start" == "1" ]; then
   		echo -n "($( echo $line | xargs)) "
   	fi
   done < "$1"

Device tree file locations:

- Zynq: ``linux/arch/arm/boot/dts/``
- ZynqMP: ``linux/arch/arm64/boot/dts/xilinx/``

See :ref:`linux-kernel zynq` and :ref:`linux-kernel zynqmp` for build
instructions.

Troubleshooting
--------------------------------------------------------------------------------

Requesting device clock failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   Requesting device clock 120000000 failed got 122880000

Indicates the clock chip is not properly configured for the new frequency.
Verify the AD9528/HMC7044/HMC7043 device tree properties match the new VCXO
and desired output frequencies.

.. note::

   For HMC7044/HMC7043: the VCO supports even dividers (2–4094) and odd
   dividers (1, 3, 5). Some target frequencies may require adjusting the VCO
   frequency. For example, with a 100 MHz VCXO and 3000 MHz VCO, requesting
   200 MHz via odd divider 15 fails — using a 2800 MHz VCO instead solves the
   issue.

Requesting lane rate failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   adrv9009 spi1.1: Request deframer lanerate 4800000 kHz failed (-22)
   adrv9009 spi1.0: Request framer lanerate 8000000 kHz failed (-22)

The FPGA gigabit transceiver (GTX/GTH/GTY) PLL VCO tuning range is
incompatible with the requested lane rate. GTX QPLL has two non-overlapping
VCO bands with a gap between them; GTH/GTY have dual QPLLs with different VCO
limits.

Mitigation strategies:

- Adjust the number of JESD204 lanes used
- Increase the QPLL/CPLL reference frequency from ``lanerate / 40`` to
  ``lanerate / 20``
- Switch QPLL selection (QPLL0 to QPLL1 or vice versa)
- Use CPLL for both links (requires identical lane rates)

ARM mailbox busy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   ARM Mailbox Busy. Command not executed in MYKONOS_sendArmCommand()

Indicates an ARM firmware internal error from an erroneous or incomplete
transceiver profile. Double-check all settings in the device tree.

TX profile IQrate and filter settings error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   Tx Profile IQrate and filter settings are not possible with current CLKPLL
   frequency

This can originate from invalid profile wizard output or device tree typos.
Pay special attention to ``adi,dig-clocks-clk-pll-hs-div`` — the property uses
enum values where ``hs-div = 2.0`` maps to value ``<0>``, not ``<2>``.

.. code-block:: dts

   adi,dig-clocks-clk-pll-hs-div = <0>;

CLKPLL VCO frequency exceeded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   CLKPLL VCO frequency exceeded max (9.216 GHz) in VCO divider /1.5 case

Caused by an invalid filter wizard profile. Regenerate the profile with
corrected parameters.
