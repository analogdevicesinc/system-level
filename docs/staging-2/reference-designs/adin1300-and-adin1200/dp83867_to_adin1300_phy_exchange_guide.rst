.. imported from: https://wiki.analog.com/resources/eval/user-guides/adin1300-and-adin1200/dp83867_to_adin1300_phy_exchange_guide

.. _adin1300-and-adin1200 dp83867_to_adin1300_phy_exchange_guide:

PHY Exchange Guide, DP83867 to ADIN1300 Gb
==========================================

Overview
--------

This PHY exchange guide captures pertinent information to support migration
from the TI DP83867IR/CR/CS/E/IS to the Analog Devices ADIN1300 Ethernet PHY.
The ADIN1300 has compelling reasons for adoption versus this competitor PHY,
such as reduced power consumption, lower latency, and smaller footprint due
to the small package size.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/figure1_motivators_to_migrate_dp83867.png

The ADIN1300 Ethernet PHY supports all the standard functions and pins of an
Ethernet PHY and it is very straight forward to migrate an existing design to
the ADIN1300. The following sections detail the modifications at the
schematic level required to migrate from a DP83867 device to the ADIN1300
device. Including a description of differences corresponding to each
functional group of pins and differences in the hardware pin configuration of
the device. A side-by-side pinout and package comparison and a feature
comparison table are included for easy reference. The ADIN1300 datasheet
provides a detailed description of all functions of the device and should
also be consulted for reference.

Hardware Changes By Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power Supplies Overview
^^^^^^^^^^^^^^^^^^^^^^^

Both devices require a minimum of 2 power supply rails, where the VDDIO is
connected to the same power supply voltage as the MAC or as the PHY analog
supply AVDD_3P3 (VDDA2P5). The VDDIO supply rail powers the MAC interface and
MDIO blocks, this can operate from 1.8V, 2.5V or 3.3V. Both devices have an
on-chip voltage regulator to generate the internal core supply rail. The
supply requirements are listed in Table 1.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table1_overview_of_power_supply_rails_dp83867.png

The ADIN1300 is robust to power supply sequencing and the power can be
applied in any order. Decoupling requirements for each device differ as
described in Table 2

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table2_decoupling_requirements_for_each_phy_dp83867.png

RESET Operation
^^^^^^^^^^^^^^^

Both devices have a RESET_N pin which initializes the device and latches the
hardware pin configuration. To reset the device the RESET_N pin should be
held low for >10 μs. Deglitch circuitry is included on this pin to reject
pulses shorter than ~1 μs. This pin requires a 1 kΩ pull-up resistor to
AVDD_3P3. The ADIN1300 includes power monitoring circuitry to monitor all of
the supplies. At power-up, the ADIN1300 is held in hardware reset until each
of the supplies has crossed its minimum rising threshold value.

The hardware strapping pins are read and updated at the de-assertion of reset
for both devices. For the ADIN1300, the RESET_N pin resides in the AVDD_3P3
voltage domain. In applications where the MAC interface is powered from VDDIO
of 1.8V, level shifting of the RESET_N signal applied to the ADIN1300 may be
required to ensure the voltage level on the RESET_N pin is in excess of the
minimum input high threshold level. The DP83867 requires external control
over the RESET_N pin during power up and a much longer time to when the
management registers are accessible. If the RESET_N pin is connected to a
host controller, then the PHY must be held in reset for a minimum of 200 ms
after the last supply powers up. If the host controller cannot be connected
to RESET_N, then a 100-Ω resistor and 47-uF capacitor are required to be
connected in series between the RESET_N pin and ground.

Clocking
^^^^^^^^

A 25 MHz crystal or external clock source is used to provide the reference
clock for both devices. A crystal can be connected to pins XTAL_I/XTAL_O
(XI/XO), with both devices using the same external circuit. Or a 25 MHz
refence clock can be provided on the input clock pin CLK_IN (XI). In RMII
mode, the ADIN1300 expects an external 50 MHz REF_CLK provided to the
XTAL_I/REF_CLK pin.

Bias Resistor
^^^^^^^^^^^^^

An external resistor is required to bias internal reference circuitry for
both DP83867 and ADIN1300. The ADIN1300 requires a 3.01 kΩ resistor (1%
tolerance, 100 ppm/°C temperature coefficient) connected to pin 10. The
DP83687 uses an 11 kΩ (1%) on pin 12 in QFN package or pin 15 in QFP package.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table3_bias_resistor_values_dp83867.png

Media Dependent Interface (MDI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ADIN1300 has voltage mode line drivers with on-chip terminations so no
external termination resistors are required. Both devices use voltage mode
line drive for connection from the MDI_0:3_P/N (TD_P/M_A:D) pins to the
magnetics and RJ-45 line using the same external circuit. The recommended
external circuit for the interface to the magnetics and RJ-45 is shown in
Figure 2.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/figure2_isolating_using_discrete_magnetics_dp83867.png

MDIO/Management Interface
^^^^^^^^^^^^^^^^^^^^^^^^^

Both devices support the IEEE management interface using the MDIO/MDC pins
and require a pullup resistor on the MDIO pin (Management Data Open Drain
Input/Output). The recommended value for ADIN1300 is a 1.5kΩ resistor
connected to pin 24. The DP83867 recommends 2.2kΩ connected to pin 17 (QFN)
or pin 21 (QFP). Both devices provide an interrupt pin, INT_N (¯INT). This
pin requires a 1.5 kΩ pull-up resistor to VDDIO. The DP83867 recommends 2.2kΩ
pull-up resistors for their interrupt pin.

LED Function
^^^^^^^^^^^^

The ADIN1300 support two LED pins on LED_0 and LINK_ST. The LED_0 has
programmability of LED functions, with different blinking operation possible
through MDIO configuration, the default mode is ON when Link is Up, blink if
activity. The LINK_ST provides static information about Link up or down
status. The DP83867 supports 3 LEDs pins 45, 46, 47 (QFN) or pins 61, 62, 63
(QFP) in addition to one GPIO pin that can be configured to operate as LED_3.
Both devices use these pins for strapping purposes.

LED Circuit
'''''''''''

The ADIN1300 LED_0 operates from the AVDD_3P3 voltage domain, therefore can
support driving LEDs even when the MAC interface is running at the lower
voltage of 1.8V. The default LED operation is on if the Link is up and blinks
when there is activity, this operation can be reprogrammed through MDIO
write. For the LED_0 of the ADIN1300, it can be configured with 4-level
strapping. The strapping configuration will have an impact on how the LED
function operates and needs to be considered if the LED pins are used to
directly drive an LED. If the strap pin is pulled high by the strapping
resistors, (MODE_3/MODE_4) the output will be configured as an active low
driver and conversely if the strapping input is pulled low (MODE_0/MODE_1),
the output will be configured as active high. This LED circuit should be
configured accordingly.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/figure3_led0_hardware_config_dp83867.png

Link Status, LINK_ST
''''''''''''''''''''

The ADIN1300 has a dedicated LINK_ST pin to provide information to the MAC on
the status of the Link. By default, the LINK_ST pin goes high indicating the
link is up and low to indicate the link is down. The LINK_ST polarity is
programmable by setting the bit high GE_LNK_STAT_INV_EN. The LINK_ST could be
used to drive an LED, however it resides in the VDDIO voltage domain,
therefore, when driving an LED in an integrated RJ45 jack where the PHY VDDIO
is 1.8V, level shifting will be required. This can be done using a FET.

--------------

MAC Interface
^^^^^^^^^^^^^

The ADIN1300 supports RGMII, MII and RMII MAC interface modes. The following
sections describe the RGMII, MII and RMII interfaces for both devices.

RGMII Interface
'''''''''''''''

The RGMII interface is the communication path between the PHY and MAC
devices. The RGMII interface has a low pin count interface supports 10M, 100M
and Gigabit operation, with a total of 12 pins for data transmission,
reception and to signal errors or collision. It is the most common interface
for Gigabit applications and has the lowest latency. Table 5 shows a pin
overview of both devices for the RGMII MAC interface mode. Both devices
support the internal delay on the clocks. By default, the ADIN1300 is
configured in RGMII mode with a 2 ns delay on RXC and TXC.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table4_rgmii_mac_interface_pin_mode_comparison_dp83867.png

MII Interface
'''''''''''''

The MII interface is the communication path between the PHY and MAC devices.
The MII interface has a high pin count, with a total of 15 pins for data
transmission, reception and to signal errors or collision. It is sometimes
used in 100M applications as it has a lower latency than RGMII and is much
lower than RMII. Table 5 shows a pin overview of both devices for the MII MAC
interface mode. When using the ADIN1300 in MII mode, the multifunction pin
``LED_0/COL/TX_ER`` automatically becomes either COL or TX_ER. If EEE
advertisement is disabled the pin function is COL as full and half-duplex
operation is supported and TX_ER is not required as an input. If EEE
advertisement is enabled the pin function is TX_ER as only full duplex
operation is supported with EEE and the COL pin is not required. Similarly,
the ``INT_N/CRS`` becomes CRS.

The ADIN1300 sub-system registers provide user with ability to reconfigure
which pin the COL and CRS functions are provided on (option of redirecting to
GP_CLK, LINK_ST or INT_N). This requires a register write over MDIO interface
to reconfigure. Note, the DP83867IR only support MII mode with the 64-QFP
12x12 mm package.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table5_mii_mac_interface_pin_mode_comparison_dp83867.png
RMII Interface
''''''''''''''
The DP83867 does not support the RMII interface. RMII is a reduced MII
interface using fewer pins as shown in Table 6. The pin count for this
interface is 8 pins.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table6_rmii_mac_interface_pin_mode_comparison_dp83867.png
In RMII mode, the ADIN1300 requires an external 50MHz clock applied to
XTAL_I. This clock could come from the MAC.

Output Clocks
^^^^^^^^^^^^^
The ADIN1300 provides a 25 MHz output reference clock on the REF_CLK pin.
This can be used a 25 MHz input reference clock for another PHY device. The
ADIN1300 can optionally provide a number of clock signals on the GP_CLK pin.
This is configured via MDIO writes and the clocks available are a 125 MHz
free running clock, 25 MHz clock and 25 MHz/125 MHz recovered clock.
Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~
Both devices have a number of strapping options to enable managed or
unmanaged configurations of the PHY function such as PHY address, mode of
operation, Auto-Negotiation and MAC Interface. After power on, the strapping
pin voltages get sensed and latched upon existing from a reset and the sensed
voltages are used to set the personality of the PHY. When configuring any
strapping configurations, ensure to review the default state of the MAC side,
whether the pins are being driven when coming out of reset or if there are
internal pulls. Understanding the behavior on the MAC side is key to ensuring
there are no conflicts with the hardware strapping implemented, or to adjust
the strapping resistor values if required. The DP83867 uses 4-level strapping
options throughout, while the ADIN1300 uses a mix of 2-level and 4-level. In
general, strapping pins are multi-functional and have different operation
after the device is brought out of reset. The ADIN1300 has internal pull
downs on many of its strapping pins (not all), therefore it would be possible
to minimize external strapping resistors.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/figure4_adin1300_hardware_strapping_2and4_level_dp83867.png
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table7_4level_strapping_resistor_ratios_adin_1300_dp83867.png
Strapping configurations are very specific to the device, consult the
respective datasheets to determine the exact configuration for required use
case. The DP83867 has internal 9 kΩ pulldown resistors on all pins used for
strapping functions.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table8_4level_strapping_resistor_ratios_dp83867.png
Hardware Configuration of Speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For the ADIN1300, speed configuration is done using two pins, PHY_CFG0 and
PHY_CFG1. These pins do not have any internal pull resistors, therefore
external strapping is required. Both pins support 4-level strapping,
providing much flexibility in terms of the possible combinations, such as
Auto-neg speeds shown in Table 9 or Forced modes shown in Table 10. Review
the datasheet hardware configuration pin section for full detail on the
possible settings using these pins.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table9_autoneg_speeds_1300_dp83867.png
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table10_forced_neg_speeds_1300_dp83867.png
Hardware Configuration of Auto-MDIX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Selection of Auto-MDIX for the ADIN1300 is done using one pin, (MDIX_MODE)
with 4-level strapping.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table11_auto_mdix_modes_1300_dp83867.png
MAC Interface Selection
^^^^^^^^^^^^^^^^^^^^^^^
The ADIN1300 uses two hardware pins, MACIF_SEL0 and MACIF_SEL1 to provide
user ability to select different MAC interfaces. These two pins have internal
weak pull downs, therefore the default operation would be RGMII with delays
as shown in Table 12. To configure any other MAC interface mode, use 10kΩ
pull up or pull down resistors to select accordingly.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table12_mac_interface_selection_1300_dp83867.png
Hardware Configuration of PHY Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Both devices have a default strapping providing a PHY address of 0x0000. The
ADIN1300 uses two-level strapping for the four PHY address pins, either pull
high or low to configure the PHY address, with an option of 16 unique
addresses possible. Two level strapping provides a very robust PHY addressing
scheme. The DP83867 provides four level strapping for the PHY address pins,
capable of 16 unique address when using the QFN device or 32 when using the
QFP. When configuring any strapping configurations, assess the default state
of the MAC side, in case it conflicts with the hardware strapping
implemented.

.. important::

   Strapping configurations are very specific to the device, consult the
   respective datasheets to determine the exact configuration for required use
   case.

Package
~~~~~~~
The ADIN1300 is available in a 40 lead LFCSP (6 mm x 6 mm footprint). The
DP83867 is available in two package options, 48 lead QFN (7 mm x 7 mm) and 64
pin QFP (12 mm x 12 mm). Due to the smaller package footprint and differing
pinout, the ADIN1300 is not a drop-in replacement for the DP83867 product. It
will require a re-spin of schematic and board layout to achieve this
exchange.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table13_package_comparrison_dp83867.png
The DP83867 requires the 64-QFP (12 mm x 12 mm) option to support MII or RMII
interface.
.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table14_package_comparrison_dp83867.png
The underside of the LFCSP package for the ADIN1300 includes an exposed
paddle which should be soldered directly to the board with an array of vias
for thermal purposes. There are also two exposed stripes adjacent to the
exposed paddle. These do not need to be soldered to the board, they should be
treated as a keep out area as they are connected to supply rails in the
device, therefore should not be tied to ground and there should be no routing
or traces on the PCB layer directly underneath them.
Other Pinout Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Integrated MDI Termination
^^^^^^^^^^^^^^^^^^^^^^^^^^
Both devices include integrated termination resistors on the MDI paths. These
are voltage mode PHYs, no external resistors are required for biasing and no
supply voltage is required at the center tap of the transformer.
RGMII Drive/Termination resistors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ADIN1300 provides user with ability to adjust the RGMII drive current
through the GE_RGMII_IO_CNTRL register.
MII
^^^
The ADIN1300 also supports MII MAC interface mode in the standard 40-QFN (6
mm x 6mm) package for 10/100M operation. The DP83867 must use the 64-QFP (12
mm x 12 mm) package.
RMII
^^^^
The ADIN1300 also supports RMII MAC interface mode for 10/100M operation. The
DP83867 does not support the RMII interface.
SGMII
^^^^^
The DP83867 supports SGMII interface in the CS/E/IS variants. The ADIN1300
does not support SGMII interface.
GMII
^^^^
The DP83867 supports GMII interface in the 64-lead QFP (12 mm x 12 mm)
package option. The ADIN1300 does not support GMII interface.
Software Considerations
~~~~~~~~~~~~~~~~~~~~~~~
Both devices can be hardware strapped to be used in an unmanaged
configuration. Alternatively, they can provide SMI/MII access over the MDIO
interface. - The DP83869 supports Clause 22 register access, while the
ADIN1300 supports both Clause 22 and Clause 45 register access using both the
802.3 Clause 22 and Clause 45 management frame structures. Registers 0x0 to
0xF are common across all PHYs.
Linux Driver
^^^^^^^^^^^^
The ADIN1300 has a Linux Driver available in the Linux mainline kernel. The
ADIN1300 linux driver detail is captured here:
https://wiki.analog.com/resources/tools-software/linux-drivers/net-phy/adin
Non Operating System Driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ADIN1300 has a Non Operating System Driver available from the devices
product page here: :adi:`en/products/adin1300.html#product-requirement`

.. tip::

   The ADIN1300 has a Linux Driver available in the Linux mainline kernel.

Side by Side Package/Pinout Comparison
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following is a side-by-side comparison of the package and pinouts, showing
the position of the corresponding functional pins on each device

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/figure5_pinout_comparison_dp83867.png

Feature Comparison Table
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/table15_feature_comparrison_table_dp83867.png

Example Configuration for RGMII
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following example captures how to configure the ADIN1300 for an unmanaged
configuration with RGMII Interface, operating in Auto Negotiation mode
advertising all speeds. The PHY will power up in this state, ready to establish
a link with a link partner. The MAC interface configuration pins (MACIF_SEL0/1)
are pulled to ground, setting the PHY to RGMII mode with 2ns Delay on RXC & TXC.
GP_CLK is pulled to VDDIO to configure an automatic MDIX operation. In addition,
the PHY_CFG0 and PHY_CFG1 pins are configured for MODE_4 and MODE_1
respectively. The PHY_CFG0 pin is also shared with the LED_0 pin, it"s
configuration with MODE_4 means an active low LED can be used on LED_0.
The following list summarizes an RGMII auto negotiate, 10 Mbps, 100 Mbps, or
1000 Mbps with full duplex or half duplex, with the software power-down enabled
after reset:

- MAC Interface = RGMII with 2ns delay on RXC/TXC

  - MACIF_SEL0 = MODE_1 = 10 kΩ pull-down resistor
  - MACIF_SEL1 = MODE_1 = 10 kΩ pull-down resistor

- MDIX_MODE = automatic MDIX, preferred MDI

  - MDIX_MODE = MODE_4

- PHY address = 0b0001
- Speed selection = 10 Mbps, 100 Mbps, or 1000 Mbps with full duplex or half
  duplex, automatic negotiate enabled

  - PHY_CFG0 = MODE_4 = 10 kΩ pull-up resistor
  - PHY_CFG1 = MODE_1 = 10 kΩ pull-down resistor

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/figure6_rmii_auto_neg_allspeeds_half_or_full_duplex_dp83867.png
