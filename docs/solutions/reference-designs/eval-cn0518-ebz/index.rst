.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0518

.. _eval-cn0518-ebz:

EVAL-CN0518-EBZ
===============

USB-Powered, 915 MHz RF Low Noise Amplifier Receiver with Overpower Protection Circuit.

Overview
--------

The :adi:`EVAL-CN0518-EBZ <CN0518>` is a USB-powered, RF power
amplifier that is optimized for receiving signal chains in the 915 MHz ISM band.
Using two :adi:`HMC376` amplifiers cascaded together, the design
provides a gain of 25dB and return losses of more than 10dB at its center
frequency.

The circuit includes a high speed overpower cutoff that protects sensitive
downstream equipment connected to the receiver system. The receiver system also
automatically returns to normal operation when the RF power level drops within
the acceptable range.

Designed to be used with the :adi:`ADALM-PLUTO`, the
:adi:`EVAL-CN0518-EBZ <CN0518>` features a small form factor with
dimensions of 25.4mm×49.6mmx1.5748mm (PCB only). The RF input and output
are designed with a 50Ω impedance, enabling direct connection between the
circuit and standard 50Ω systems.

A micro-USB connector is used for the input power, allowing the evaluation board
to use most 5V wall wart power supplies available in the market.

.. figure:: eval-cn0518-ebz.jpg
   :width: 500 px

   EVAL-CN0518-EBZ Reference Design Board

The :adi:`EVAL-CN0518-EBZ <CN0518>` features the :adi:`HMC376`,
which is a GaAs, pHEMT, MMIC, low noise amplifier
operating between 700MHz to 1000MHz. This amplifier is ideal for use in GSM
and CDMA cellular base station front end receivers. This low noise amplifier
does not require any external matching circuitry to operate.

.. figure:: block_diagram.png

   EVAL-CN0518-EBZ Simplified Block Diagram

Reference Design Hardware
-------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: primary_side.png

   CN0518 Primary Side

Secondary Side
~~~~~~~~~~~~~~

.. figure:: secondary_side.png

   CN0518 Secondary Side

SMA Connectors
~~~~~~~~~~~~~~

The SMA connectors are used for the RF input and output connections.

+--------------------------+----------------------+--------------------------+
| RF Port                  | Reference Designator | Description              |
+--------------------------+----------------------+--------------------------+
| RF Input (SMA male       | J2                   | Connect to a radio or    |
| connector)               |                      | piece of RF equipment    |
+--------------------------+----------------------+--------------------------+
| RF Output (SMA female    | J1                   | Connect to an antenna    |
| connector)               |                      |                          |
+--------------------------+----------------------+--------------------------+

LED Indicators
~~~~~~~~~~~~~~

The reference design uses two LEDs to indicate its current status:

============= ==================== =============================================
RF Port       Reference Designator Description
============= ==================== =============================================
**Green LED** DS1                  Indicates that power is present on the board
**Red LED**   DS2                  Indicates when an overpower event occurs
============= ==================== =============================================

This table shows the board status when the various LEDs are ON/OFF.

========= ======= ======================================
Green LED Red LED Board Status
========= ======= ======================================
OFF       OFF     No Power
ON        OFF     Normal RF Operation
ON        ON      Overpower Event (RF Output Attenuated)
========= ======= ======================================

Power Supply Connector
~~~~~~~~~~~~~~~~~~~~~~

- **P1** is the micro-USB port used to provide 5V power to the board.

Getting Started
---------------

Required Equipment
~~~~~~~~~~~~~~~~~~

Hardware
^^^^^^^^

- :adi:`EVAL-CN0518-EBZ <CN0518>`
- :adi:`ADALM-PLUTO`
- Two (2) micro-USB power adaptor or micro-USB to USB cable for powering
  :adi:`ADALM-PLUTO` and :adi:`EVAL-CN0518-EBZ <CN0518>`
- One (1) SMA male-to-male cable

Firmware
^^^^^^^^

For the step-by-step procedure on how to update the Pluto Firmware, you can use
this :ref:`user guide link <pluto-m2k firmware>`.

The latest firmware version for the **ADALM-PLUTO** can be found here:

.. admonition:: Download

   ADALM-PLUTO Firmware: `Pluto version latest release <https://github.com/analogdevicesinc/plutosdr-fw/releases/latest>`__

ADALM-PLUTO Preparation
~~~~~~~~~~~~~~~~~~~~~~~

Follow the step-by-step process on how to configure the ADALM-PLUTO for proper
operation by referring to this
:ref:`link <pluto-m2k firmware>`.

Test Setup
~~~~~~~~~~

.. figure:: test_setup.png

   EVAL-CN0518-EBZ Test Setup

#. Connect directly the **Rx port** of :adi:`ADALM-PLUTO` to
   **J1** of the :adi:`EVAL-CN0518-EBZ <CN0518>`.
#. Connect the **Tx port** of the :adi:`ADALM-PLUTO` to **J2** of
   the :adi:`EVAL-CN0518-EBZ <CN0518>` using a male-to-male SMA cable.
#. Connect **P1** (micro-USB) connector of the
   :adi:`EVAL-CN0518-EBZ <CN0518>` into a PC USB port or a 5V USB
   charger.
#. Connect the micro-USB to USB cable to a PC/laptop and the other end to the
   :adi:`ADALM-PLUTO` data port.
#. The DS2 LED of :adi:`CN0518-EBZ <CN0518>` will automatically turn on,
   indicating that the board is powered on and is in operation.

.. important::
   The :adi:`ADALM-PLUTO` can be configured using an IIO Oscilloscope, visit
   the website on :ref:`iio-oscilloscope` to learn more about the tool.

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download or update to the latest version of IIO Oscilloscope
   found on this :git-iio-oscilloscope:`link <releases+>`.

- Once done with the installation or an update of the latest IIO Oscilloscope,
  open the application. The user needs to supply a URI, which will be used in
  the context creation of the IIO Oscilloscope. The instructions can be seen in
  the previous section.
- Press refresh to display available IIO devices. Once the
  :adi:`ADALM-PLUTO` appeared, press connect.

.. figure:: connecting_of_iio_osc.jpg

   IIO Oscilloscope Configuration

- On the AD936x tab, set the required parameters for the
  :adi:`EVAL-CN0518-EBZ <CN0518>` to operate properly.

.. figure:: ad936x.png

   ADALM-PLUTO Settings

- Using the capture window, you can see the RF output of the
  :adi:`EVAL-CN0518-EBZ <CN0518>` in the frequency domain.

.. figure:: capture_window.png

   CN0518 RF Output

More Information and Useful Links
---------------------------------

- :adi:`CN0518 Product Page <CN0518>`
- :adi:`HMC376 Product Page <HMC376>`
- :adi:`ADG901 Product Page <ADG901>`
- :adi:`ADL5904 Product Page <ADL5904>`
- :adi:`LT8335 Product Page <LT8335>`
- :adi:`LT3042 Product Page <LT3042>`
- :adi:`ADM7170 Product Page <ADM7170>`
- :adi:`LTC6991 Product Page <LTC6991>`
- :ref:`ADALM-PLUTO Overview <pluto>`
- :dokuwiki:`Amplifiers for RF Transmission </university/tools/pluto/users/amp>`
- :dokuwiki:`RF Amplifier Considerations </university/tools/pluto/users/amp>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`EVAL-CN0518-EBZ Design & Integration Files <CN0518-DesignSupport>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Registration
------------

.. tip::

   Receive software update notifications and documentation
   updates, view the latest videos, and more when you register your hardware.
   :adi:`Register <EVAL-CN0518-EBZ?&v=Rev F>` to receive all these great benefits
   and more!

Help and Support
-------------------

For questions and more information about this product, connect with us through the Analog Devices :ez:`/` .
