.. _xbdp additional software:

Additional Software Resources
===============================================================================

ADAR1000EVAL1Z Power Sequence
-------------------------------------------------------------------------------

The proper power on sequencing for the ADAR1000EVAL1Z is embedded within the
firmware of the ZCU102. The embedded script pulses the proper signal nets in the
correct order (POWER_UP_DOWN and 5V_CTRL) automatically upon booting the FPGA.
The power down sequence is not enabled in software. The ADAR1000EVAL1Z board can
be powered down manually by pressing the RESET button on the primary side of the
ADAR1000EVAL1Z board. The following steps need to be completed by the user to
implement the ADAR1000EVAL1Z power up sequencing script.

-  Open a UART terminal and connect to the FPGA as shown in the
   :ref:`Quickstart <xbdp quickstart zcu102 uart>`
-  Download `WinSCP <https://winscp.net/eng/download.php>`_
-  Connect to the ZCU102 via WinSCP

   -  Host: FPGA IP Address

      -  Username: root
      -  Password: analog

-  Navigate to the /etc/ folder
-  Copy the :download:`power sequencing script <files/adar1000eval1z_power_script.zip>`
   to the /etc/ folder
-  Open the rc.local file in the /etc/ directory

   -  Replace contents of rc.local file with the code below

-  Save files, exit WinSCP, and reboot the FPGA

.. code-block:: bash

   #!/bin/sh -e
   #
   # rc.local
   #
   # This script is executed at the end of each multiuser runlevel.
   # Make sure that the script will "exit 0" on success or any other
   # value on error.
   #
   # In order to enable or disable this script just change the execution
   # bits.
   #
   # By default this script does nothing.

   # Print the IP address
   _IP=$(hostname -I) || true
   if [ "$_IP" ]; then
     printf "My IP address is %s\n" "$_IP"
   fi

   python3 /etc/stingray_power.py up

   service iiod restart

   exit 0

.. note::

   Due to the hardware design of the ADAR1000EVAL1Z, the user needs to keep in
   mind the power up and power down execution. If the power sequence is not
   followed in the correct order, then the power sequence state will be
   indeterminate and a hard reset is required to revert to a known power state.

   For example the proper sequence is as follows: Power Up -> Power Down ->
   Power Up -> Power Down

Useful UART Commands
-------------------------------------------------------------------------------

The use of the UART terminal to debug and understand device attribute and
channel attribute settings can be insightful. There are a variety of
:doc:`LibIIO </software/libiio/index>` command sets that can be utilized such as
:ref:`libiio iio_info` and :ref:`libiio iio_attr`. Additional libiio tips and
tricks can be found :doc:`here </software/libiio/tips-tricks>`.

Device Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::
   :user: root
   :group: analog

   root@analog:~# iio_attr -d
   IIO context has 19 devices:
           iio:device0, ltc2314-14: found 1 device attributes
           iio:device1, ams: found 1 device attributes
           iio:device18, adf4371-0: found 2 device attributes
           iio:device19, hmc7044: found 7 device attributes
           iio:device2, adar1000_csb_1_1: found 40 device attributes
           iio:device20, axi-ad9081-rx-hpc: found 13 device attributes
           iio:device21, axi-core-tdd: found 11 device attributes
           iio:device22, one-bit-adc-dac: found 1 device attributes
           iio:device23, one-bit-adc-dac: found 1 device attributes
           iio:device24, one-bit-adc-dac: found 1 device attributes
           iio:device25, axi-ad9081-tx-hpc: found 2 device attributes
           iio:device3, adar1000_csb_1_2: found 40 device attributes
           iio:device4, adar1000_csb_1_3: found 40 device attributes
           iio:device5, adar1000_csb_1_4: found 40 device attributes
           iio:device6, adar1000_csb_2_1: found 40 device attributes
           iio:device7, adar1000_csb_2_2: found 40 device attributes
           iio:device8, adar1000_csb_2_3: found 40 device attributes
           iio:device9, adar1000_csb_2_4: found 40 device attributes
           iio_sysfs_trigger: found 2 device attributes
   root@analog:~#

Channel Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::
   :user: root
   :group: analog

   root@analog:~# iio_attr -c
   IIO context has 19 devices:
           iio:device0, ltc2314-14: found 2 channels
           iio:device1, ams: found 30 channels
           iio:device18, adf4371-0: found 5 channels
           iio:device19, hmc7044: found 8 channels
           iio:device2, adar1000_csb_1_1: found 9 channels
           iio:device20, axi-ad9081-rx-hpc: found 17 channels
           iio:device21, axi-core-tdd: found 4 channels
           iio:device22, one-bit-adc-dac: found 6 channels
           iio:device23, one-bit-adc-dac: found 6 channels
           iio:device24, one-bit-adc-dac: found 5 channels
           iio:device25, axi-ad9081-tx-hpc: found 24 channels
           iio:device3, adar1000_csb_1_2: found 9 channels
           iio:device4, adar1000_csb_1_3: found 9 channels
           iio:device5, adar1000_csb_1_4: found 9 channels
           iio:device6, adar1000_csb_2_1: found 9 channels
           iio:device7, adar1000_csb_2_2: found 9 channels
           iio:device8, adar1000_csb_2_3: found 9 channels
           iio:device9, adar1000_csb_2_4: found 9 channels
           iio_sysfs_trigger: found 0 channels
   root@analog:~#

HMC7044 pll Lock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::
   :user: root
   :group: analog

   root@analog:~# cat /sys/kernel/debug/iio/iio:device19/status
   --- PLL1 ---
   Status: Locked
   Using:  CLKIN1 @ 100000000 Hz
   PFD:    10000 kHz
   --- PLL2 ---
   Status: Locked (Synchronized)
   Frequency:      3000000000 Hz (Autocal cap bank value: 12)
   SYSREF Status:  Valid & Locked
   SYNC Status:    Synchronized
   Lock Status:    PLL1 & PLL2 Locked
   root@analog:~#

.. note::

   The HMC7044 reference clock priority is: [CLKIN1 → CLKIN0 → CLKIN2 → CLKIN3].
   In this example, an external reference clock of 100MHz is applied and is
   selected as the reference clock source. If no external clock is detected,
   then the clock priority will be sequenced and the next available source will
   be chosen. See the :ref:`Hardware Clocking Architecture <xbdp additional hardware clocking>`
   for additional information.

Firmware Identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A unique identifier will be returned for the Image, system.dtb, and BOOT.BIN
files installed on the SD card using the md5 command.

.. shell::
   :user: root
   :group: analog

   root@analog:~# md5sum /boot/Image
   3c1ac2b114bbde82b38fc0463bf03dbd  /boot/Image
   root@analog:~#

.. shell::
   :user: root
   :group: analog

   root@analog:~# md5sum /boot/system.dtb
   bfc14855246807f4e62a2f71ce65deec  /boot/system.dtb
   root@analog:~#

.. shell::
   :user: root
   :group: analog

   root@analog:~# md5sum /boot/BOOT.BIN
   a77ca8194b457c2d020a44d83568cc52  /boot/BOOT.BIN
   root@analog:~#

.. note::

   The returned identifiers in the example may not match the most recent
   firmware file versions. This is an example to show the use of the md5
   command.
