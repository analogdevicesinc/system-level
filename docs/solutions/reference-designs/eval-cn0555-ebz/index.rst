.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0555

.. _eval-cn0555-ebz:

EVAL-CN0555-EBZ
===============

USB-Powered, 433.92 MHz RF Low Noise Amplifier Receiver with Overpower Protection.

Overview
--------

The :adi:`CN0555` is a two-stage, USB-powered, RF low noise amplifier
that is optimized for receiver signal chains in the 433.92 MHz 
industrial, scientific and medical (ISM) band. It provides a gain 
of 40 dB through its RF band of operation using two :adi:`ADL5523`
amplifiers cascaded together, boosting signals for various 
communication protocols such as
`ISM <https://en.wikipedia.org/wiki/ISM_radio_band>`__,
`MC-GSM <https://www.google.com/search?q=mc-gsm>`__,
`W-CDMA <https://www.3gpp.org/technologies/keywords-acronyms/104-w-cdma>`__,
`TD-SCDMA <http://www.telecomabc.com/t/tdcdma.html>`__, and
`LTE <https://en.wikipedia.org/wiki/LTE_%28telecommunication%29>`__ .

It includes a high-speed overpower cutoff that protects sensitive
downstream equipment connected to the receiver system and automatically
turns back on when the RF power level drops within the acceptable range.

Designed to be used with the :adi:`ADALM-PLUTO`, the 
:adi:`EVAL-CN0555-EBZ` features a small form-factor with dimensions 
of 25.4 mm × 50.673 mm x 1.5748 mm (PCB only). The reference design 
uses standard 50 Ω SMA coaxial connectors for its RF signal path — 
for easy integration with any RF systems; a female connector is used
for the RF input and a male connector is used for the RF output. 
Coplanar waveguides are used for the RF traces on the board, which 
have a characteristic impedance of 50 Ω. A micro USB connector is used 
for the input power, allowing the evaluation board to use most +5 V 
wall-wart power supplies available in the market.

.. figure:: cn0555-top.png
   :align: center

   EVAL-CN0555-EBZ Reference Design Board

The :adi:`CN0555` reference design features the :adi:`ADL5523`, 
which is a high performance 
`GaAs pHEMT <https://www.google.com/search?q=gaas-phemt>`__
low noise amplifier. It provides a high gain and low noise figure for
single down-conversion intermediate frequency (IF) sampling receiver
architectures, as well as direct down-conversion receivers. It is easy
to tune and only requires a few external components. The device can
support operation voltages from 3 V to 5 V and the current draw can be
adjusted with external bias resistors for applications requiring very
low power consumption.

The :adi:`ADL5904` is a dual-function RF TruPwr detector that 
operates from dc to 6 GHz. It provides rms power measurement along 
with a programmable envelope threshold detection function. The 
RMS power measurement function has a 45 dB detection range, 
nominally from −30 dBm to +15 dBm. The rms power measurement
function also features low power consumption and an intrinsically
ripple-free error transfer function.

.. figure:: blockdiagram.png
   :align: center

   EVAL-CN0555-EBZ Simplified Block Diagram

Reference Design Hardware
-------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: primary_side.png
   :align: center

   CN0555 Primary Side

SMA Connectors
^^^^^^^^^^^^^^

The SMA connectors are used for the RF input and output connections.

- **J1** is the **RF Input** SMA female connector that would be
  connected to an antenna.
- **J2** is the **RF Output** SMA male connector that would be connected
  to a radio or piece of RF equipment.

LED Indicators
^^^^^^^^^^^^^^

The reference design uses two LEDs to indicate its current status.

- The Red LED **(DS1)** lights up when an overpowering event occurs.
- The Green LED **(DS2)** lights up when the power is present on the
  board.

.. figure:: led.png
   :align: center

   CN0555 LED Indications of Board Status

Secondary Side
~~~~~~~~~~~~~~

.. figure:: secondary_side.png
   :align: center

   CN0555 Secondary Side

Power Supply Connector
^^^^^^^^^^^^^^^^^^^^^^

- **P1** is the micro USB port used to provide 5 V power to the board.

Getting Started
---------------

Required Equipment
~~~~~~~~~~~~~~~~~~

Hardware
^^^^^^^^

- :adi:`EVAL-CN0555-EBZ`
- :adi:`ADALM-PLUTO`
- Two (2) micro USB power adaptor or micro USB to USB cable for powering
  ADALM-PLUTO and EVAL-CN0555-EBZ
- One (1) SMA male-to-male cable
- One (1) SMA 10 dB RF attenuator

Firmware
^^^^^^^^

- :git-plutosdr-fw:`releases/latest+`

ADALM-PLUTO Preparation
~~~~~~~~~~~~~~~~~~~~~~~

Firmware Loading
^^^^^^^^^^^^^^^^

#.  Download :git-plutosdr-fw:`releases/latest+`

#.  Unzip the downloaded file.

#.  Connect Pluto to host PC or laptop using a micro USB cable in the
    terminal with a USB symbol.

#.  Open the Pluto mass storage device.

#.  Open the unzipped firmware file.

#.  Copy the file, *pluto.frm*, to the Pluto mass storage device.

    .. figure:: pluto_firmware_update.jpg
       :align: center

       Copying Pluto Firmware to the Pluto Mass Storage Device

#.  This will cause LED1 to blink rapidly. This means that programming
    is taking place. Do not remove power (or USB) while the device is
    blinking rapidly. It takes approximately four minutes to properly
    program the device.

#.  Once the device finishes programming, it will reappear as a mass
    storage device.

#.  Eject (don’t unplug) the Pluto mass storage device.

    .. figure:: eject_pluto.jpg
       :align: center

       Ejection of Pluto Mass Storage Device

#. Now, the USB cable can be safely disconnected from the PC.

Updating to the AD9364
^^^^^^^^^^^^^^^^^^^^^^

#. Connect again the Pluto to host PC using a micro USB cable.

#. Open any serial terminal application (e.g., TeraTerm, Putty) and set
   the SSH to 192.168.2.1, the username is root and password is
   *analog*.

    .. figure:: tera_term_connection.jpg
       :align: center

    .. figure:: username_and_password.jpg
       :align: center

       Copying Pluto Firmware to the Pluto Mass Storage Device

#. To change parameters to the :adi:`AD9364` configuration, enter the
   following commands line by line:

   .. code-block::

      # fw_setenv attr_name compatible
      # fw_setenv attr_val ad9364
      # reboot

   .. figure:: command_line_to_update_ad9364.jpg
      :align: center

      AD9364 Configuration

#. Eject (don’t unplug) the Pluto mass storage device.

#. Then, the USB cable can be safely disconnected from the PC.

#. Connect Pluto again to PC using a micro USB cable and proceed with
   the hardware test setup following the instruction in the next
   section.

Test Setup
~~~~~~~~~~

Normal Operation
^^^^^^^^^^^^^^^^

.. figure:: test_setup.png
   :align: center

   EVAL-CN0555-EBZ Test Setup

#. Connect directly the RX port of :adi:`ADALM-PLUTO` to J2 of the
   :adi:`EVAL-CN0555-EBZ`.

#. Connect the Tx port of the :adi:`ADALM-PLUTO` to J1 of the
   :adi:`EVAL-CN0555-EBZ` using a male-to-male SMA cable.

#. Connect P1 (micro USB) connector of the :adi:`EVAL-CN0555-EBZ` into 
   a PC USB port or 5 V USB charger.

#. Connect the micro USB to USB cable to a PC/laptop and the other end
   to the :adi:`ADALM-PLUTO` data port.

#. The DS2 LED of :adi:`CN0555` will automatically turn on, indicating 
   the board is powered on and is in operation.

.. important::

   The :adi:`ADALM-PLUTO` can be configured using an IIO Oscilloscope, visit
   :ref:`iio-oscilloscope` to learn more about the tool.

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO Oscilloscope
   found on this :git-iio-oscilloscope:`link <releases+>`

- Once done with the installation or an update of the latest IIO
  Oscilloscope, open the application. The user needs to supply a URI,
  which will be used in the context creation of the IIO Oscilloscope and
  the instructions can be seen in the previous section.

- Press refresh to display available IIO devices, once the
  :adi:`ADALM-PLUTO` appeared, press connect.

    .. figure:: connecting_of_iio_osc.jpg
       :align: center

       IIO Oscilloscope Configuration

- On the AD936x tab, set the required parameters for the
  :adi:`CN0555` to operate properly.

     .. figure:: ad936x.png
       :align: center

       ADALM-PLUTO Settings

- Using the capture window, you can see the RF output of the
  :adi:`CN0555` in the frequency domain.

     .. figure:: capture_window.png
       :align: center

       CN0555 RF Output

More Information and Useful Links
---------------------------------

.. admonition:: Download

    - :adi:`CN0555` Circuit Note Page
    - :adi:`ADL5523` Product Page
    - :adi:`ADG901` Product Page
    - :adi:`ADL5904` Product Page
    - :adi:`ADM7170` Product Page
    - :adi:`LT3042` Product Page
    - :adi:`ADALM-PLUTO` Overview
    - :dokuwiki:`Amplifiers for RF Transmission on Analog Wiki </university/tools/pluto/users/amp>`
    - :dokuwiki:`RF Amplifier Considerations</university/tools/pluto/users/amp>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`EVAL-CN0555-EBZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/cn0555-designsupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Gerber Files
   - Allegro Project

Registration
------------

.. note::

   Receive software update notifications and documentation updates, view
   the latest videos, and more when you register your hardware.
   `Register <https://my.analog.com/en/app/registration/hardware/>`_
   to receive all these great benefits and more!
