.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0521

.. _eval-cn0521-ebz:

EVAL-CN0521-EBZ
===============

USB-Powered, 2.4 GHz RF Low Noise Amplifier Receiver with Overpower Protection Circuit.

Overview
--------

The :adi:`EVAL-CN0521-EBZ <CN0521>` is a USB-powered, RF low noise amplifier (LNA)
that is optimized for receiving signal chains in the 2.4GHz ISM band.
Using two :adi:`HMC639` amplifiers cascaded together, the design provides
a gain of 21dB and return losses of more than 10dB throughout its RF
band of operation.

The board includes a high speed overpower cutoff that protects sensitive
downstream equipment connected to the receiver system. The receiver system
also automatically turns back on when the RF power level drops within the
acceptable range.

Designed to be used with the :adi:`ADALM-PLUTO`,
the :adi:`EVAL-CN0521-EBZ <CN0521>` features a small form factor, 
with dimensions of 25.4mm×49.6mm×1.5748mm (PCB only). 
The RF input and output are designed with a 50Ω impedance, enabling direct
connection between the circuit and standard 50Ω systems.

A micro-USB connector is used for the input power, allowing the evaluation
board to use most 5V wall wart power supplies available in the market.

.. figure:: cn0521.png
   :align: center

   EVAL-CN0521-EBZ Reference Design Board

The :adi:`EVAL-CN0521-EBZ <CN0521>` features the :adi:`HMC639`, which is a GaAs,
pHEMT, high linearity, low noise amplifier operating between 0.2GHz to
4GHz for various applications such as fixed-wireless, cellular, and
CATV. This low noise RF amplifier does not require any external matching
circuitry to operate.

.. figure:: block_diagram.png
   :align: center

   EVAL-CN0521-EBZ Simplified Block Diagram

Components
----------

.. figure:: primary_side.png
   :align: center

   CN0521 Primary Side

.. figure:: secondary_side.png
   :align: center

   CN0521 Secondary Side

SMA Connectors
~~~~~~~~~~~~~~

The SMA connectors are used for the RF input and output connections.

================================= ==================== ===================
RF Port                           Reference Designator Description
================================= ==================== ===================
RF Input (SMA male connector)     J1                   Connect to a radio
                                                       or piece of RF
                                                       equipment
RF Output (SMA female connector)  J2                   Connect to an
                                                       antenna
================================= ==================== ===================

LED Indicators
~~~~~~~~~~~~~~

The reference design uses two LEDs to indicate its current status:

============= ==================== ==============================================
RF Port       Reference Designator Description
============= ==================== ==============================================
**Green LED** (DS2)                Indicates that power is present on the board
**Red LED**   (DS1)                Indicates when an overtemperature event
                                   occurs
============= ==================== ==============================================

This table shows the board status when the various LEDs are ON/OFF.

========= ======= ======================================
Green LED Red LED Board Status
========= ======= ======================================
OFF       OFF     No Power
ON        Off     Normal RF Operation
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

- :adi:`EVAL-CN0521-EBZ`
- :adi:`ADALM-PLUTO`
- Two (2) micro-USB power adaptor or micro-USB to USB cable for powering
  :adi:`ADALM-PLUTO` and :adi:`EVAL-CN0521-EBZ <CN0521>`
- One (1) SMA male-to-male cable

Firmware
^^^^^^^^

For the step-by-step procedure on how to update the Pluto Firmware, you
can use this 
:ref:`user guide link <pluto-m2k firmware>`.

The latest firmware version for the **ADALM-PLUTO** can be found here:

.. admonition:: Download

   ADALM-PLUTO Firmware

   :git-plutosdr-fw:`Pluto version latest release <releases/latest+>`

ADALM-PLUTO Preparation
~~~~~~~~~~~~~~~~~~~~~~~

Follow the step-by-step process on how to configure the ADALM-PLUTO for
proper operation by referring to this 
:ref:`link <pluto-m2k firmware>`.

Test Setup
~~~~~~~~~~

Normal Operation
^^^^^^^^^^^^^^^^

.. figure:: test_setup.png
   :align: center

   EVAL-CN0521-EBZ Test Setup


#. Connect directly the **Rx port** of :adi:`ADALM-PLUTO` to J2 of the
   :adi:`EVAL-CN0521-EBZ <CN0521>`.
#. Connect the **Tx port** of the :adi:`ADALM-PLUTO` to J1 of the
   :adi:`EVAL-CN0521-EBZ <CN0521>` using a male-to-male SMA cable.
#. Connect **P1** (micro-USB) connector of the :adi:`EVAL-CN0521-EBZ`
   into a PC USB port or 5 V USB charger.
#. Connect the micro-USB to USB cable to a PC/laptop and the other end
   to the :adi:`ADALM-PLUTO` data port.
#. The DS2 LED of :adi:`EVAL-CN0521-EBZ <CN0521>` will automatically turn on,
   indicating the board is powered on and is in operation.

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO Oscilloscope
   found on this 
   :git-repo:`link <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`.

  - Once done with the installation or an update of the latest IIO
    Oscilloscope, open the application. The user needs to supply a URI,
    which will be used in the context creation of the IIO Oscilloscope.
    The instructions can be seen in the previous section.
  - Press Refresh to display available IIO devices. Once the
    :adi:`ADALM-PLUTO` appeared, press connect.

      .. figure:: connecting_of_iio_osc.jpg
         :align: center

   IIO Oscilloscope Configuration

   - On the AD936x tab, refer to this 
      :dokuwiki:`link <resources/tools-software/linux-software/fmcomms2_plugin>` 
      for proper configuration of the AD936x.

   - Using the capture window, you can see the RF output of the
      :adi:`EVAL-CN0521-EBZ <CN0521>` in the frequency domain.

      .. figure:: capture_window.png
         :align: center

   CN0521 RF Output

More Information and Useful Links
---------------------------------

- :adi:`CN0521 Product Page <CN0521>`
- :adi:`HMC639 Product Page <HMC639>`
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

   :adi:`EVAL-CN0521-EBZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/cn0521-designsupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Help and Support
----------------

For questions and more information, please visit the :ez:`/` community or
contact your local ADI representative.
