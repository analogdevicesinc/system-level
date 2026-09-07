.. _eval_adtf3175_nxz hardware_access:

Hardware Access
===============================================================================

This guide explains how to access the ADTF-3175x evaluation module for
advanced configuration and development.

SD Card Configuration
-------------------------------------------------------------------------------

The device ships with read-only Linux partitions. You can modify the micro-SD
card to enable write access by editing the ``extlinux.conf`` file.

Enabling Write Access
~~~~~~~~~~~~~~~~~~~~~

Replace instances of "ro" with "rw" in the configuration file:

**Case 1:** Direct modification on computers without encryption

1. Remove the microSD card from the module
2. Insert into your computer's SD card reader
3. Navigate to the boot partition
4. Edit ``extlinux.conf`` and change "ro" to "rw"
5. Save and safely eject the card

**Case 2:** Network sharing approach for encrypted systems

If your system encrypts removable media, share the SD card over the network
to another machine for editing.

USB-Serial Connection
-------------------------------------------------------------------------------

The ADTF-3175x connects via USB-Serial through a micro-USB cable.

Connection Steps
~~~~~~~~~~~~~~~~

1. Connect the micro-USB cable to the module's serial port
2. Identify the COM port in Windows Device Manager
3. Use PuTTY or similar terminal software
4. Configure serial connection:

   - **Baud rate:** 115200
   - **Data bits:** 8
   - **Stop bits:** 1
   - **Parity:** None
   - **Flow control:** None

Default Credentials
~~~~~~~~~~~~~~~~~~~

- **Username:** analog
- **Password:** analog

Network Connectivity
-------------------------------------------------------------------------------

WiFi Setup
~~~~~~~~~~

Two approaches are available:

**Manual command:**

.. code-block:: bash

   wpa_passphrase <SSID> <Password> | sudo tee /etc/wpa_supplicant/wpa_supplicant-wlan0.conf

**Automated script:**

.. code-block:: bash

   ./adi-enable-wifi.sh <SSID> <Password>

Ethernet
~~~~~~~~

Ethernet connectivity requires a special Harting connector cable
(model 33480147826005).

Safety Warnings
-------------------------------------------------------------------------------

.. warning::

   Improper Linux commands can disable the device. The stock image can be
   re-flashed if problems occur.

.. warning::

   Always properly shut down Linux before power cycling:

   .. code-block:: bash

      sudo systemctl poweroff

   Failure to do so may corrupt the filesystem.
