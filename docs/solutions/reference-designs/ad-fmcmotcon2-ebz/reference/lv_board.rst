.. _ad_fmcmotcon2_ebz lv-board:

AD-DRVLV2-EBZ Low Voltage Drive Board
===============================================================================

Features
-------------------------------------------------------------------------------

- Connects to the Controller board with a power stage that drives motors up to
  48 V and 20 A
- Drives 2 motors simultaneously
- High frequency drive stage implemented with ADI isolated gate drivers
- Supported motor types

  - BLDC
  - PMSM
  - Brushed DC
  - Stepper (bipolar / unipolar)

- Integrated over current protection
- Reverse voltage protection
- Current and voltage measurement using isolated ADCs

  - Current measurement on 2 phases for 2 motors
  - DC Link Voltage measurement

- BEMF zero cross detection for sensorless control of PMSM or BLDC motors
- Separate voltage supplies for the 2 motors so that the motors do not
  influence each other

Block Diagram
-------------------------------------------------------------------------------

.. figure:: ../images/lv_block_diagram_simplified.jpg
   :alt: AD-DRVLV2-EBZ simplified block diagram
   :align: center
   :width: 500

   Simplified block diagram

Picture and Main Components
-------------------------------------------------------------------------------

.. figure:: ../images/ad-drvlv2-ebz_top_parts.jpg
   :alt: AD-DRVLV2-EBZ top side
   :align: center
   :width: 600

   AD-DRVLV2-EBZ top side

.. figure:: ../images/ad-drvlv2-ebz_bottom_parts.jpg
   :alt: AD-DRVLV2-EBZ bottom side
   :align: center
   :width: 450

   AD-DRVLV2-EBZ bottom side

Key Parts
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Part
     - Description
   * - **Measurement**
     -
   * - :adi:`AD7403`
     - 16-bit isolated 2nd order Sigma-Delta modulator
   * - :adi:`AD8207`
     - Zero drift, high voltage, bidirectional difference amplifier
   * - :adi:`CMP04`
     - Quad low power, precision comparator
   * - **Power**
     -
   * - :adi:`ADuM5000`
     - isoPower® integrated isolated dc-to-dc converter
   * - :adi:`ADP1621`
     - Constant-frequency, current-mode step-up dc/dc controller
   * - :adi:`ADP2301`
     - 1.2 A, 20 V, 1.4 MHz non-synchronous step-down switching regulator
   * - **MOSFET Drivers**
     -
   * - :adi:`ADuM5230`
     - Isolated half-bridge driver with integrated high-side supply
   * - :adi:`ADuM7223`
     - Isolated precision half-bridge driver, 4.0 A output

Switches
-------------------------------------------------------------------------------

.. figure:: ../images/lv_reset.jpg
   :alt: Drive board switches
   :align: center
   :width: 600

   Drive board switches

**Emergency Stop** switch

- S2 is a latching emergency stop switch.
- If triggered, the supply for the power stage is turned off.

**Reset** switch

- S1 is a reset switch for the emergency stop latch.
- Pressing S1 when S2 is not pressed turns the power stage on.