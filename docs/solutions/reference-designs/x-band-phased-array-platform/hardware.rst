.. _xbdp additional hardware:

Additional Hardware Resources
===============================================================================

Hardware Connections
-------------------------------------------------------------------------------

Please follow the steps presented in the :ref:`Quickstart Guide <xbdp quickstart zcu102>`
to create the hardware setup.

A diagram of the system is shown in the figures below.

.. figure:: images/xbdp-system-block-diagram.png
   :width: 1000

   High Level Block Diagram

.. figure:: images/platformblockdiagram.jpg
   :width: 1000

   Detailed Block Diagram

Inter-Board Connections
-------------------------------------------------------------------------------

The platform is divided into four 8:1 subarrays as detailed in the below figure.
Two ADAR1000s are connected via RF Splitter/Combiner to a single up/down
converter channel on the ADXUD1AEBZ. The IF portion of an individual up/down
converter channel is split to a Tx IF and Rx IF input/output. Each IF output
is directly connected to its respective ADC and DAC.

For more details, review the :ref:`ADAR1000EVAL1Z Primary Side and Secondary Side <stingray>`,
the :ref:`ADXUD1AEBZ Primary Side <xud1a>`, and the
:adi:`AD9081-EVAL <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9081.html#eb-overview>`
board images.

.. figure:: images/xbdp_hardwareconnectiondiagram.png
   :width: 1000

   Inter-Board Connections Diagram

.. _xbdp additional hardware clocking:

Clocking Architecture
-------------------------------------------------------------------------------

Default MxFE Clocking Scheme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default clocking scheme used for the :adi:`AD9081-FMCA-EBZ <eval-ad9081>`
uses the on-chip pll. The :adi:`hmc7044` provides the reference into the chip
derived from the on-board VCXO crystal oscillator. An external reference signal
can be applied to the HMC7044 if the reference signal requires phase lock to
other test equipment used in evaluation. The AD9081 firmware contains a HMC7044
reference clock priority table. No firmware changes are required if the
reference clock is supplied via EXT_HMCREF SMP-F connection.

.. figure:: images/ad9081_default_clk.png
   :width: 800

   AD9081 Clocking Block Diagram

.. note::

   The firmware build HMC7044 reference clock priority is: [CLKIN1 -> CLKIN0 ->
   CLKIN2 -> CLKIN3]. An external reference clock can be applied to the
   EXT_HMCREF SMP-F input without any changes to the firmware or hardware.

Direct MxFE Clocking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MxFE Evaluation Platform has provisions for directly driving the sampling
clock of the MxFE data converter. An SMP-F plug is available for this purpose,
which connects to an AC-coupling capacitor that is not populated by default.
Reference the schematic for more information. The table below lists the
modifications required for direct clocking.

.. figure:: images/ad9081_direct_clk.png
   :width: 800

   AD9081 Direct Clocking Implementation

.. list-table:: Direct Clocking Modifications
   :header-rows: 1

   * - SMP-F Ref Des
     - Modifications
   * - EXT_CLK
     - Depopulate C3D/C5D, Populate C4D/C6D

Default XUD1A LO Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default LO configuration for the XUD1A is for an external LO via SMA-F
connector. The LO is common across all 4 up/down converter channels via splitter
network. Refer to the :ref:`XUD1A Block Diagram <xud1a block diagram>` for more
details.

.. figure:: images/xud1a_lo_pll.png
   :width: 600

   XUD1A LO Block Diagram

On-Board XUD1A LO Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The on-board :adi:`adf4371` pll can be used in lieu of an external LO signal.
The default ADF4371 reference clock is an on-board 100 MHz VCXO crystal
oscillator, but provisions are available to provide an external reference via a
SMP-F connector.


.. figure:: images/xud1a_rework_onboard_pll.png
   :width: 600

   XUD1A On-Board pll Implementation

The table below lists the modifications required for the on-board LO.

.. list-table:: XUD1A On-Board LO Modifications
   :header-rows: 1

   * - Implementation
     - Modifications
   * - ADF4371 Output
     - Depopulate C165, Populate C61
   * - ADF4371 External Reference
     - Depopulate C372, Populate C373
   * - ADF4371 +5V Enable
     - Populate R20 with 0 Ohm 0402 Resistor

Time Division Duplexing
-------------------------------------------------------------------------------

The system platform supports Time Division Duplexing (TDD), which is
controlled using a TDD Engine implemented in firmware. The TDD engine controls
the MxFE Tx and Rx data enable paths, the ADXUD1AEBZ up/down converter circuitry
and ADAR1000EVAL1Z RF circuitry. See the
:ref:`Quickstart MATLAB Support <xbdp quickstart zcu102 matlab>`
section for user-level control.

TDD Nets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Replicated IO for the TDD controller is created in hardware all tied to a common
software control. The replicas of the MxFE datapath enable pins are routed to
signal nets on the ADXUD1AEBZ Interposer board.

.. list-table:: TDD Nets
   :header-rows: 1

   * - Signal
     - ZCU102 FPGA Pin (U1)
     - ZCU102 FMC HPC1 Connector (J4)
     - Interposer Board Net (P3)
     - Pin Number (P3)
   * - MxFE Tx EN
     - AG3
     - D11
     - IMU_GPIO0
     - P3-13
   * - MxFE Rx EN
     - AH3
     - D12
     - IMU_GPIO1
     - P3-14
   * - External Sync
     - AE2
     - D14
     - IMU_GPIO2
     - P3-15
   * - Ground
     -
     -
     - GND
     - P3-7

The control logic for the RF switching is common between the ADAR1000EVAL1Z and
the ADXUD1AEBZ. The **TR_EN** probe point on the secondary side of the
ADAR1000EVAL1Z is recommended to use for connecting a measurement probe.

.. figure:: images/adar1000eval1z_tr_probe.png
   :width: 600

   ADAR1000EVAL1Z TR Probe

Troubleshooting
-------------------------------------------------------------------------------

AD9081 Power On
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADXUD1AEBZ FMC EEPROM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


There are two potential issues that prevent the 1.8V VADJ from powering on the
AD9081-FMCA-EBZ board. Upon boot, the FPGA queries the EEPROM of the different
boards attached. If a non-compliant EEPROM is detected, the VADJ stays low
during boot thus preventing the AD9081 board from powering on.

Currently, the FMC EEPROM of the interposer board used for the ADXUD1AEBZ is not
factory programmed. The user must execute some commands within a UART terminal
to program the FMC EEPROM. The command sets to program the FMC EEPROM of the
ADXUD1AEBZ interposer board are detailed in the
:ref:`Quickstart Guide <xbdp quickstart zcu102>`.
Reboot the FPGA after programming the FMC EEPROM.

AD9081 LTM4616 Enable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The AD9081 :adi:`ltm4616` power module run control pin voltage threshold is
1.7V. Verify the voltage and resistance of the R1M resistor on the
AD9081-FMCA-EBZ exceed the voltage threshold of 1.7V. If not, measure the R1M
resistor and verify the resistance value is 2.2 kΩ. The resistor can be replaced
with a 0402 220 Ω resistor to meet the voltage threshold requirements of the
power module.

.. figure:: images/ad9081_ltm4616_en_resistor_r1m.png
   :width: 600

   AD9081-FMCA-EBZ R1M Location
