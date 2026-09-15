.. imported from: https://wiki.analog.com/resources/eval/user-guides/arradio/quickstart/alterasockit

.. _arradio quickstart alterasockit:

ARRADIO Terasic C5 SoCkit Quick Start Guide
===========================================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/arradio/quickstart/terasic_c5_sockit_arradio.jpg
   :width: 550px

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the ARRADIO board on
`Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`__

Prerequisites
-------------

Required Hardware
~~~~~~~~~~~~~~~~~

- `Terasic C5 SoCkit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`__
- `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`__
  board
- An 8GB Micro-SD Card
- USB keyboard and mouse
- OTG Cable (for the USB keyboard and mouse)
- A VGA compatible monitor
- Ethernet cable
- 1 x Micro-USB cable

Required Software
~~~~~~~~~~~~~~~~~

- You need a Host PC (Linux)
- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
- `IIO Oscilloscope <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__

Creating the Micro-SD Card
--------------------------

.. tip::

   :ref:`kuiper`

Required files
~~~~~~~~~~~~~~

The root of "BOOT" should contain the following files:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``socfpga.dtb``
- ``zImage``
- ``u-boot.scr``
- ``soc_system.rbf``

The root of preloader partition should contain the following file:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``preloader_bootloader.img``

Configuring the Micro-SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   analog@analog:~ $ lsblk

   NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sdb           8:16   1 29.7G  0 disk
   ├─sdb1        8:17   1    1G  0 part /media/analog/BOOT
   ├─sdb2        8:18   1  9.8G  0 part /media/analog/rootfs
   └─sdb3        8:19   1    4M  0 part

   analog@analog:~ $ cd /media/analog/BOOT/socfpga_cyclone5_sockit_arradio
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ ls -l

   total 10248
   -rwxr-xr-x 1 root root  500432 Jul 27 15:06 preloader_bootloader.img
   -rwxr-xr-x 1 root root   25291 Jul 27 15:06 socfpga.dtb
   -rwxr-xr-x 1 root root 2685848 Jul 27 15:06 soc_system.rbf
   -rwxr-xr-x 1 root root     200 Jul 27 15:06 u-boot.scr
   -rwxr-xr-x 1 root root 7269944 Jul 27 15:06 zImage

   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp socfpga.dtb /media/analog/BOOT/socfpga.dtb
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp zImage /media/analog/BOOT/zImage
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp u-boot.scr /media/analog/BOOT/u-boot.scr
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo cp soc_system.rbf /media/analog/BOOT/soc_system.rbf
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sudo dd if=preloader_bootloader.img of=/dev/sdb3

   977+1 records in
   977+1 records out
   500432 bytes (500 kB, 489 KiB) copied, 0.138791 s, 3.6 MB/s

   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ sync
   analog@analog:/media/analog/BOOT/socfpga_cyclone5_sockit_arradio $ cd ../../
   analog@analog:/media/analog $ sudo umount /dev/sdb1
   analog@analog:/media/analog $ sudo umount /dev/sdb2
   analog@analog:/media/analog $ lsblk

   NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sdb           8:16   1 29.7G  0 disk
   ├─sdb1        8:17   1    1G  0 part
   ├─sdb2        8:18   1  9.8G  0 part
   └─sdb3        8:19   1    4M  0 part

--------------

Setting up the hardware (Terasic C5 SoCkit)
-------------------------------------------

You will need to:

::

   -Get the [[https://www.arrow.com/en/products/sockit/arrow-development-tools | Terasic C5 SoCkit]]

::

   {{  resources:eval:user-guides:arradio:quickstart:terasic_c5_sockit.jpg?600
   }}

::

   -Insert the Micro-SD Card into the Micro-SD Card  Connector
   -Connect the ARRADIO board to the FPGA carrier HSMC connector
   -Plug your monitor device into the VGA Video Connector
   -Plug your USB mouse/keyboard into the USB 2.0 OTG Port
   -Plug the Power Supply into 12V Power Supply connector (DO NOT turn the device on)
   -Set the jumpers according to the following table:

.. list-table::
   :header-rows: 1

   * -
     - CLOCKSEL0
     - CLOCKSEL1
     - BOOTSEL0
     - BOOTSEL1
     - BOOTSEL2
   * - **POS**
     - 2-3
     - 2-3
     - 2-3
     - 2-3
     - 1-2

.. list-table::
   :header-rows: 1

   * - JP2
   * - 2.5V or 1.8V

.. list-table::
   :header-rows: 1

   * - SW6
     - MSEL0
     - MSEL1
     - MSEL2
     - MSEL3
     - MSEL4
     - CODEC_SEL
   * - **POS**
     - 0
     - 1
     - 0
     - 1
     - 0
     - 0

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

Booting the Micro-SD Card
-------------------------

Local IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~

::

   -Ignore your PC, and now interact on the USB mouse/keyboard on the Terasic C5 SoCkit device
   -You should see two screens:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/arradio/quickstart/print_iio_linux_arradio_c5soc.png
   :width: 700px

Remote IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~

::

   -Connect USB UART (Micro USB) to your host PC.
   -Plug your ethernet cable into the RJ45 ethernet connector
   -Run the ifconfig command on your UART terminal and get your board IP

::

   root@analog:~# ifconfig

   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet your_board_ip  netmask 255.255.255.0  broadcast
           inet6 fe80::e6e7:b2c:f962:dc57  prefixlen 64  scopeid 0x20<link>
           ether 1c:76:ca:01:23:45  txqueuelen 1000  (Ethernet)
           RX packets 25208  bytes 4726181 (4.5 MiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 5987  bytes 2260634 (2.1 MiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
           device interrupt 29  base 0x2000

::

   -Open IIO Scope application and type ip:board_ip in the URI tab.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/arradio/quickstart/iio_remote_c5soc_arradio.png
   :width: 600px

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be
   taken not to corrupt the file system – please shut down things, don"t just
   turn off the power switch. Depending on your monitor, the standard power off
   could be hiding. You can do this from the terminal as well with ""sudo
   shutdown -h now""

   .. figure:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
      :width: 300px

More Information
----------------

- :dokuwiki:`ARRADIO User Guide </resources/eval/user-guides/arradio>`

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/common.rst

   :start-after: .. start-#support
   :end-before: .. end-#support
