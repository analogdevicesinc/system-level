.. imported from: https://wiki.analog.com/resources/eval/user-guides/adin1300-and-adin1200/adin1200-ieee-compliance-test-mode-access

.. _adin1300-and-adin1200 adin1200-ieee-compliance-test-mode-access:

Configuring the ADIN1200 for Ethernet PHY Compliance Test Modes
===============================================================

Overview
--------

The purpose of this application note is to describe the configuration of the
ADIN1200 for the various Ethernet PHY compliance test modes as set out by
IEEE802.3.

The ADIN1200 supports test modes for 100BASE-TX and 10BASE-T that are useful for
compliance testing. Details of the registers, sequences of writes are captured
in this document. Use this application note in conjunction with the product
datasheet.

Testing Equipment and Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When performing this testing, user will need Ethernet compliance test fixture
and associated Ethernet physical layer compliance software. There are a number
of vendors provide Ethernet Compliance test equipment. For ADI in-house
validation, we used Tektronix TDSET3 compliance software in addition to having
UNH (University of New Hampshire perform compliance testing).

Once equipment is in place and hardware powered and connected to the test
fixture, configure the PHY through the MDIO interface to set the required test
mode and use the compliance software to record and report the results.

Reset Between Tests
~~~~~~~~~~~~~~~~~~~

To ensure the device is in a known state, either start from a power cycle or
alternatively, issue the following writes to reset the device with fresh read of
the hardware configuration.

- GE_SFT_RST_CFG_EN.Write(0b1) - Register 0xFF0D to ensure the hardware
  configuration is refreshed.
- GE_SFT_RST. Write(0b1) - Register 0xFF0C subsystem reset

Extended Register Addressing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADIN1200 supports a range of extended management interface registers which
can be accessed using Clause 45 access or alternatively using Clause 22 access
through the EXT_REG_PTR (address 0x0010) and EXT_REG_DATA (address 0x0011),
these registers provide user ability to read/write to the extended register
space (any register greater than 0x001F) indirectly.

If using Clause 22 access, write the 16-bit register address into the
EXT_REG_PTR register and then read or write the EXT_REG_DATA register.

--------------

100BASE-TX
----------

For 100BASE-TX operation there are a variety of tests. There are two main test
modes main register involved here is the B_100_TX_TST_MODE register at address
0xB413 (available via Clause 45 access)

100BASE-TX Transmit Test Mode Register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Address: 0xB413, Reset: 0x0000, Name: B_100_TX_TST_MODE This register provides
the ability to transmit a 100BASE-TX test signal.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/2_-_b100tx_tst_mode_register.png

To configure the device for 100BASE-TX VOD measurements, issue the following
writes over MDIO

- MII_CONTROL.Write(0x2900) - Register 0x0000 to place the device into Software
  PD, configure 100BASE-TX full duplex, autoneg disabled
- PHY_CTRL_1.AUTO_MDI_EN.Write(0b) - Register 0x0012, bit 10: Disable Auto
  MDI/MDIX
- PHY_CTRL_1.MAN_MDIX.Write(0b0) - Register 0x0012, bit 9: Operate in MDI
  configuration
- B_100_TX_TST_MODE.Write(1/2/3/4) - Register 0xB413 bits 2:0: Configure
  required test mode on Dim 0 or 1
- PHY_CTRL_3. LINK_EN.Write(0b1) - Register 0x0017, bit 13: Enable linking
- MII_CONTROL.SFT_PD.Write(0b0) - Register 0x0000 bit 11: Bring PHY out of
  Software Power Down

--------------

10BASE-TE/10BASE-T TRANSMIT TEST SIGNAL
---------------------------------------

When operating in 10 Mbps speeds, the PHY is configured for 10BASE-Te transmit
levels by default. 10BASE-T provides larger transmit levels and can be
configured by clearing the B_10_E_EN register. The 10BASE-Te/T compliance tests
are:

- Link Pulse Testing
- Medium Attachment Unit (MAU)
- TP_IDL
- Jitter
- Differential Voltage
- Harmonics
- Transmitter Return Loss
- Receiver Return Loss
- Common-Mode Voltage

The B_10_TX_TST_MODE register is used to select transmit test signals useful for
10BASE-T compliance testing.

10BASE-T Transmit Test Mode Register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Address: 0xB412, Reset: 0x0000, Name: B_10_TX_TST_MODE This register provides
the ability to transmit a 10BASE-T test signal.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/3_-_b10tx_tst_mode_register.png

To configure the device for 10BASE-T transmit test mode, consisting of 5MHz
square wave on desired dimension, issue the following writes over MDIO

- GE_SFT_RST_CFG_EN.Write(0b1) - Register 0xFF0D to ensure the hardware
  configuration is refreshed.
- GE_SFT_RST. Write(0b1) - Register 0xFF0C subsystem reset
- MII_CONTROL.SFT_RST. Write(0b1) - Register 0x0000 Issue a software reset, this
  bit is self clearing
- MII_CONTROL.Write(0x0900) - Register 0x0000 Enter Software Power Down and
  configure 10M FD, disable AutoNegotiation
- B_10_TX_TST_MODE.Write(0b100) - Register 0xB412 Choice of 100: Enable Transmit
  5MHz square wave on Dim 1; 011: 5MHz on Dim0; 010 10MHz on Dim1; 001: 10MHz on
  Dim0.
- MII_CONTROL.SFT_PD.Write(0b0) - Register 0x0000 Bring PHY out of Software PD

An alternative configuration, where the device is configured in 10BASE-T forced
mode in loopback with Tx suppression disabled, with transmission of frames with
random payloads using the frame generator as follows:

- GE_SFT_RST_CFG_EN.Write(0b1) - Register 0xFF0D to ensure the hardware
  configuration is refreshed.
- GE_SFT_RST. Write(0b1) - Register 0xFF0C subsystem reset
- MII_CONTROL.SFT_RST. Write(0b1) - Register 0x0000 bit 15, Issue a software
  reset, this bit is self clearing
- MII_CONTROL.SFT_PD.Write(0b0) - Register 0x0000 bit 11, Bring PHY out of
  Software PD
- PHY_CTRL_1.DIAG_CLK_EN.Write(0b1) - Register 0x0012 bit 2, Enable the
  Diagnostic Clock
- MII_CONTROL.LOOPBACK.Write(0b1) - Register 0x0000 bit 14, Enable Loopback
- PHY_CTRL_1.MAN_MDIX.Write(0b0) - Register 0x0012 bit 9, Operate in MDI
  configuration
- PHY_CTRL_STATUS_1.LB_TX_SUP.Write(0b0) - Register 0x0013 bit 6, Stop
  suppressing the transmit signal at the MDI pins in all digital loopback
- PHY_CTRL_STATUS_1.LB_ALL_DIG_SEL.Write(0b1) - Register 0x0013 bit12 Enable all
  digital loopback
- PHY_CTRL_3. LINK_EN.Write(0b1) - Register 0x0017 bit 13, Enable linking
- MII_CONTROL.SFT_PD.Write(0b0) - Register 0x0000 bit 11, Bring PHY out of
  Software PD
- Wait for Link up
- FG_CONT_MODE_EN.Write(0b1) - Register 0x9417 Enable the frame generator into
  continuous mode
- FG_CNTRL_RSTRT.FG_CNTRL.Write(1) - Register 0x9416, bits 2:0: Enable random
  number in the MAC client data frame field, options of decrementing,
  alternative 0x55, all ones, all zeroes, random number
- FG_EN.FG_EN.Write(1) - Enable Frame Generator

Setup for 10BASE-T forced mode in loopback with Tx suppression disabled, with
transmission of frames with random payloads using the frame generator, configure
as follows in sequence above

- FG_CNTRL_RSTRT.FG_CNTRL.Write(0b011) - 0xFF repeating payloads
- FG_CNTRL_RSTRT.FG_CNTRL.Write(0b010) - 0x00 repeating payloads
- FG_CNTRL_RSTRT.FG_CNTRL.Write(0b100) - alternative 0x55 payloads
- FG_CNTRL_RSTRT.FG_CNTRL.Write(0b101) - data field decrementing from 255 to
  0(decimal)

10BASE-T is configured by writing the following register – include it in the
sequence above if 10BASE-T operation is required.

- B_10_E_EN.Write(0x0) - 10BASE-Te is enabled by default, write 0 to configure
  10BASE-T.

--------------

Testing Using ADI Evaluation GUI
--------------------------------

The ADI evaluation board uses small MDIO dongle board for USB to MDIO
communications and the accompanying GUI provides access to the various Test
modes from the ``Test Mode`` tab. Select the relevant test mode to configure and
``Execute Test``. In the ``Activity log`` the register writes can be observed.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/4_-_adin1200_gui_screenshot.png
