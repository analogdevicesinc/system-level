.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0523

.. _eval-cn0523-ebz:

EVAL-CN0523-EBZ
===============

USB-Powered, 5.8 GHz RF Power Amplifier with Overtemperature Management.

Overview
--------

The :adi:`EVAL-CN0523-EBZ <CN0523>` is a USB-powered, RF power amplifier
that is optimized for transmitting signal chains in the 5.8GHz ISM band.
Using two :adi:`HMC407` amplifiers cascaded together, the design
provides a gain of 28dB and return losses of more than 10dB throughout its RF
band of operation.

An overtemperature management feature is implemented on the
:adi:`EVAL-CN0523-EBZ <CN0523>` wherein the amplifiers are
automatically disabled when the board temperature reaches a preset threshold,
and it automatically returns to normal operation once the temperature falls
below the hysteresis point.

Designed to be used with the :adi:`ADALM-PLUTO`, or other
software defined radio platform, the board features a small form factor, with
dimensions of ``25.4mm × 50.8mm x 1.5748mm`` (PCB only). The RF input and
output are designed with a 50Ω impedance, enabling direct connection between
the circuit and standard 50Ω systems.

A micro-USB connector is used for the input power, allowing the evaluation board
to use most 5V wall wart power supplies available in the market.

.. figure:: cn0523_simplified_block_diagram.png

   EVAL-CN0523-EBZ Block Diagram

Reference Design Hardware
-------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: top_temp.jpg

   CN0523 Primary Side

SMA Connectors
^^^^^^^^^^^^^^

The SMA connectors are used for the RF input and output connections:

- **J1** is the **RF Input** SMA male connector that would be connected to a
  radio or piece of RF equipment. The maximum RF input level of the
  :adi:`EVAL-CN0523-EBZ <CN0523>` is **+10dBm**. Do not use a higher input
  level to avoid damaging the circuit.

- **J2** is the **RF Output** SMA FEmale connector that would be connected to
  an antenna. The saturated output power (Psat) of :adi:`EVAL-CN0523-EBZ <CN0523>`
  is **+27dBm**. Ensure that the RF load can handle the amplified RF signal.
  Use an RF attenuator if necessary to avoid damage.

LED Indicators
^^^^^^^^^^^^^^

The reference design uses two LEDs to indicate its current status:

=============================== ======= ================
LED Indications of Board Status
=============================== ======= ================
**DS1**                         **DS2** **Board Status**
Off                             Off     No power
Off                             On      Normal operation
On                              On      Overtemperature
=============================== ======= ================

Secondary Side
~~~~~~~~~~~~~~

.. figure:: bot_temp.jpg

   CN0523 Secondary Side

Power Supply Connector
^^^^^^^^^^^^^^^^^^^^^^

- **P1** is the micro-USB port used to provide 5V power to the board. The total
  typical supply current of the on-board RF amplifiers is 230mA.

Changing the Temperature Switch Trip Point (JP1, JP2, JP3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The trip point of the temperature switch can be set using the solder jumpers
  JP1, JP2, and JP3 as shown in the table below. When the board temperature
  reaches the trip point, the :adi:`ADT6401` will disable the two RF
  amplifiers.

  .. figure:: jmp_settings.jpg

      ADT6401 Jumper Settings

+-------------------+------------------+-----------------+----------------+
| Selecting a Trip  |                  |                 |                |
| Point for the     |                  |                 |                |
| ADT6401           |                  |                 |                |
+===================+==================+=================+================+
| **JP1 Setting**   | **JP2 Setting**  | **JP3 Setting** | **Trip Point** |
+-------------------+------------------+-----------------+----------------+
| 2 & 3             | 2 & 3            | 2 & 3           | +45°C          |
+-------------------+------------------+-----------------+----------------+
| 1 & 2             | 2 & 3            | 2 & 3           | +55°C          |
+-------------------+------------------+-----------------+----------------+
| No solder jumper  | 2 & 3            | 2 & 3           | +65°C          |
+-------------------+------------------+-----------------+----------------+
| 2 & 3             | 1 & 2            | 2 & 3           | +75°C          |
+-------------------+------------------+-----------------+----------------+
| 1 & 2             | 1 & 2            | 2 & 3           | +85°C          |
+-------------------+------------------+-----------------+----------------+
| No solder jumper  | 1 & 2            | 2 & 3           | +95°C          |
+-------------------+------------------+-----------------+----------------+
| 2 & 3             | 2 & 3            | 1 & 2           | +65°C          |
+-------------------+------------------+-----------------+----------------+
| 1 & 2             | 2 & 3            | 1 & 2           | +75°C          |
+-------------------+------------------+-----------------+----------------+
| No solder jumper  | 2 & 3            | 1 & 2           | +85°C          |
+-------------------+------------------+-----------------+----------------+
| 2 & 3             | 1 & 2            | 1 & 2           | +95°C          |
+-------------------+------------------+-----------------+----------------+
| 2 & 3             | No solder jumper | 2 & 3           | +105°C         |
+-------------------+------------------+-----------------+----------------+
| 1 & 2             | No solder jumper | 2 & 3           | +115°C         |
+-------------------+------------------+-----------------+----------------+
| No solder jumper  | No solder jumper | 2 & 3           | +55°C          |
+-------------------+------------------+-----------------+----------------+

.. important::
   Due to the considerable thermal dissipation of the RF amplifiers,
   the last three options should not be used.

Getting Started
---------------

Required Equipment
~~~~~~~~~~~~~~~~~~

**Hardware**

- :adi:`EVAL-CN0523-EBZ <CN0523>`
- :adi:`ADALM-PLUTO`
- Two (2) micro-USB power adaptors or micro-USB to USB cables for powering
  :adi:`ADALM-PLUTO` and :adi:`EVAL-CN0523-EBZ <CN0523>`
- One (1) SMA male-to-male cable
- One (1) SMA 30 dB RF attenuator

**Firmware**

- For step-by-step procedure on how to update the Pluto Firmware, you can
  use this :ref:`user guide link <pluto-m2k firmware>`.
  The latest firmware version for the **ADALM-PLUTO** can be found here:

  .. admonition:: download

     ADALM-PLUTO Firmware:
     :git-plutosdr-fw:`Pluto version latest release <releases/latest+>`

- In order to properly operate the ADALM PLUTO, you need to setup and configure
  it. Follow the procedure through this
  :ref:`link <pluto-m2k firmware>`.

Test Setup
~~~~~~~~~~

#. Connect directly the **TX port** of :adi:`ADALM-PLUTO` to the
   **RF Input (J1)** of the :adi:`EVAL-CN0523-EBZ <CN0523>`.
#. Connect directly the **RX port** of the :adi:`ADALM-PLUTO` to
   a 30dB attenuator.
#. Connect **RF Output (J2)** of the :adi:`EVAL-CN0523-EBZ <CN0523>` to a 30dB
   attenuator using a male-to-male SMA cable.
#. Connect **P1** (micro-USB) connector of the :adi:`EVAL-CN0523-EBZ <CN0523>`
   into a PC USB port or a 5V USB charger.
#. Connect the micro-USB to USB cable to a PC/laptop and the other end to the
   :adi:`ADALM-PLUTO` data port.
#. The DS2 LED of :adi:`EVAL-CN0523-EBZ <CN0523>` will automatically
   turn on, indicating that the board is powered on and is in operation.
#. Refer to the image below for the full hardware setup.

   .. figure:: full_hw_setup.jpg

      EVAL-CN0523-EBZ Test Setup

.. warning::

   Connecting the CN0523 directly to the PlutoSDR input (Rx)
   may result in an exceedance of its absolute maximum ratings
   of +2.5dBm. Such an action may lead to permanent damage to the PlutoSDR. It is
   strongly recommended to use a **30dB or 40dB attenuator** at the RX input of
   the ADALM PLUTO to avoid incurring damage.

More Information and Useful Links
---------------------------------

- :adi:`CN0523 Product Page <CN0523>`
- :adi:`HMC407 Product Page <HMC407>`
- :adi:`ADT6401 Product Page <ADT6401>`
- :adi:`LT8364 Product Page <LT8364>`
- :adi:`ADM7150 Product Page <ADM7150>`
- :adi:`ADM7171 Product Page <ADM7171>`
- :ref:`ADALM-PLUTO Overview <pluto>`
- :dokuwiki:`Amplifiers for RF Transmission </university/tools/pluto/users/amp>`
- :dokuwiki:`RF Amplifier Considerations </university/tools/pluto/users/amp>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   `EVAL-CN0523-EBZ Design & Integration Files <https://www.analog.com/cn0523-DesignSupport>`__

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Gerber Files
   - Allegro Board File

Help and Support
----------------

For questions and more information about this product, connect with us through
the Analog Devices :ez:`/`.
