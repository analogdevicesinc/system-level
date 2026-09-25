ADRV9361/ADRV9364 u-boot Environment Fix
========================================

Due to an incident during production, on some boards the partition of the flash
containing the u-boot environment variables, has not been written properly with
the u-boot default environment variables, and therefore it does not contain the
necessary information to boot. This is causing the device to remain in u-boot.

Note that this does not impact device hardware quality in any way, and that the
flash memory that contains the u-boot variables has been functionally tested.

How to check if your board has this issue
-----------------------------------------

To check if your device is affected all you need is a MicroUSB cable. Connect
the cable to the UART port of your carrier open the serial port terminal of
choice, power on the board and see if the following text is being displayed:

::

   Model: Zynq Zed Development Board
   Board: Xilinx Zynq
   Silicon: v3.1
   DRAM:  ECC disabled 512 MiB
   MMC:   sdhci@e0100000: 0 (SD)
   SF: Detected n25q256a with page size 256 Bytes, erase size 4 KiB, total 32 MiB
   In:    serial@e0001000
   Out:   serial@e0001000
   Err:   serial@e0001000
   Net:   ZYNQ GEM: e000b000, phyaddr 0, interface rgmii-id
   eth0: ethernet@e000b000
   Zynq>

Instructions for resetting the environment
------------------------------------------

Please perform the following steps to eliminate the issue:

.. important::

   The board has a sticker with the MAC address, as presented in the picture below. The mac address should have ‘:’ after each two numbers, for example “00:05:f7:80:26:ef” |image1|\

From your serial port terminal run the following commands:

::

   Zynq> env default -a
   Zynq> setenv ethaddr "<MAC_ADDR_FROM_STICKER>"
   Zynq> saveenv
   Zynq> reset

If you get an error after **saveenv**, then your flash partition had also been locked. To unlock it and then write the proper environment variables, please follow these steps:

::

   Zynq> env default -a
   Zynq> run sdboot

The board will now boot in Linux. Once done, run the following commands:

::

   root@analog:~# flash_unlock /dev/mtd1
   root@analog:~# flash_erase /dev/mtd1 0 0
   root@analog:~# reboot

When hitting reboot, please pay attention to the prompt **"Hit any key to stop autoboot: 3...2...1"**. When that appears, please press any button to re-enter uboot. Then, all is left to do is to write the default environment variables and save:

::

   Zynq> env default -a
   Zynq> setenv ethaddr "<MAC_ADDR_FROM_STICKER>"
   Zynq> saveenv
   Zynq> reset

Other support
~~~~~~~~~~~~~

The board will then reset, boot normally and be ready to use for your applications. If you have a different issue or these steps have not worked out for you, we offer support at :ez:`Engineer Zone <community/linux-device-drivers/linux-software-drivers>`.

.. |image1| image:: images/adrv936x_mac_addr_sticker.jpg
   :width: 400
