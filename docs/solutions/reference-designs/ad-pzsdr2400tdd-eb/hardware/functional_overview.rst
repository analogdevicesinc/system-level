Functional Overview
===================

A functional block diagram of the system is given below. The system consists
of two transmit paths, two receive paths and power supply.

.. figure:: ../images/2400tdd_block_diagram.jpg
   :width: 600

   AD-PZSDR2400TDD-EB functional block diagram.

Transmit
--------

Key component:

.. list-table::
   :header-rows: 0

   * - :adi:`ADL5324`
     - The ADL5324 incorporates a dynamically adjustable biasing circuit that
       allows for the customization of OIP3 and P1dB performance from 3.3 V to
       5 V, without the need for an external bias resistor.
   * - :adi:`HMC921`
     - The HMC921LP4E is a high linearity GaAs HBT MMIC 2 watt power amplifier
       operating from 0.4 to 2.7 GHz and is housed in a RoHS compliant 4x4 mm
       QFN leadless package.

Receive
-------

Key component:

.. list-table::
   :header-rows: 0

   * - :adi:`HMC669`
     - The HMC669LP3(E) is a versatile, high dynamic range GaAs MMIC Low Noise
       Amplifier that integrates a low loss LNA bypass mode on the IC. The
       amplifier is ideal for receivers and LNA modules operating between 1.7
       and 2.2 GHz and provides 1.4 dB noise figure, 17 dB of gain and
       +29 dBm IP3 from a single supply of +5V @ 86mA.

Switching
---------

Key component:

.. list-table::
   :header-rows: 0

   * - :adi:`HMC546 <HMC546LP2>`
     - The HMC546LP2(E) is a failsafe SPDT switch in a leadless DFN surface
       mount plastic package for use in transmit-receive, and LNA protection
       applications which require very low distortion and high power handling of
       up to 10 watts. The device can control signals from 200 - 2700 MHz and
       is especially suited for WiMAX and WiBro repeaters, PMR and automotive
       telematic applications.

Power
-----

Key components:

.. list-table::
   :header-rows: 0

   * - :adi:`ADP2384`
     - 4A, 20V step-down switcher.
   * - :adi:`ADP7104`
     - High accuracy, 500mA LDO.
   * - :adi:`ADM7171`
     - Ultra low noise, 1 A LDO.

The board receives all the power from the carrier board through a 40 pin
connector.
