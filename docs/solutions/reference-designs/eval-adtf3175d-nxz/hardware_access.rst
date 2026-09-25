Hardware Access
===============

SD Card Configuration
---------------------

The micro-SD card ships with a read-only Linux partition. To enable read-write
access:

For Unencrypted Systems
~~~~~~~~~~~~~~~~~~~~~~~

1. Access the FAT partition via Windows
2. Edit ``extlinux.conf`` in the extlinux folder
3. Replace all ``ro`` with ``rw``

For Encrypted Systems
~~~~~~~~~~~~~~~~~~~~~

1. Use a personal computer to bypass encryption, or
2. Map the partition as a network drive through advanced sharing options
3. Then modify the ``extlinux.conf`` file as described above

.. warning::

   Issue the following command in the CLI to power down the system before
   disconnecting power to prevent file system corruption::

      sudo systemctl poweroff

USB-Serial Connection
---------------------

1. Plug USB-C cable to power the device
2. Open Windows Device Manager
3. Connect the micro-USB cable and note the new COM port
4. Configure PuTTY with:

   -  Connection type: Serial
   -  Speed: 115200
   -  Serial line: [noted COM port]

Default Credentials
-------------------

-  **Username:** analog
-  **Password:** analog

WiFi Setup
----------

Manual Approach
~~~~~~~~~~~~~~~

::

   wpa_passphrase <SSID> <Password> | sudo tee /etc/wpa_supplicant/wpa_supplicant-wlan0.conf
   sudo systemctl enable wpa_supplicant@wlan0
   sudo reboot

Scripted Approach
~~~~~~~~~~~~~~~~~

::

   cd ~/Workspace/Tools
   ./adi-enable-wifi.sh <SSID> <Password>

Ethernet
--------

Requires a special Harting connector cable (specific model referenced in
documentation).
