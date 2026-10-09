.. _software fru-dump:

FMC EEPROM Programming
===============================================================================

As part of the `FMC specification <https://www.vita.com/fmc>`_, EEPROMs exist
on the FMC cards which can provide configuration for different voltages on for
the cards themselves. EEPROM images for different ADI cards are available
online and can be manipulated using the
:doc:`fru-dump tool </software/fru_dump>`.
This page will provide steps for updating specific FMC cards. The steps are very
generic and should apply to all ADI FMC cards which have available master image
files.

FMCOMMS2 + ZCU102 Example
-------------------------------------------------------------------------------

To update the EEPROM image with the masterfiles follow this procedure on the
FPGA development kit itself, such as the ZCU102, ZC706, or similar.

1. Open a terminal or SSH to the target board

2. Locate the EEPROM block devices:

::

   root@analog:~# find /sys/bus/i2c/devices/*/ -name eeprom
   /sys/bus/i2c/devices/14-0050/eeprom
   /sys/bus/i2c/devices/6-0054/eeprom
   /sys/bus/i2c/devices/i2c-1/i2c-6/6-0054/eeprom
   /sys/bus/i2c/devices/i2c-1/i2c-14/14-0050/eeprom
   /sys/bus/i2c/devices/i2c-14/14-0050/eeprom
   /sys/bus/i2c/devices/i2c-6/6-0054/eeprom

**/sys/bus/i2c/devices/14-0050/eeprom** is the desired EEPROM for ZCU102. The
actual path on your system might be different depending on FPGA carrier, kernel
version, and devicetree. **/sys/bus/i2c/devices/6-0054/eeprom** is for the
EEPROM on the FPGA system. The remaining entries are simply references to these
EEPROMs. If you don't know which is which, remove the FMC card and run the
**find** command again. Only the FPGA EEPROM will be listed.

3. Check existing EEPROM.

If empty, it will have the following output:

::

   root@analog:~# fru-dump -b /sys/bus/i2c/devices/14-0050/eeprom
   read 256 bytes from /sys/bus/i2c/devices/14-0050/eeprom
   fru_dump 0.8.1.7, built 04Aug2022
   FRU Version number mismatch 0xff should be 0x01

If programmed, it will have the following output:

::

   root@analog:~# fru-dump -b /sys/bus/i2c/devices/14-0050/eeprom
   read 256 bytes from /sys/bus/i2c/devices/14-0050/eeprom
   Date of Man     : Mon Jul 22 20:23:00 2013
   Manufacturer    : Analog Devices
   Product Name    : AD9361 RF Hardware Development Kit
   Serial Number   : 00045
   Part Number     : AD-FMCOMMS2-EBZ
   FRU File ID     : Empty Field
   PCB Rev         : C
   PCB ID          : 9361FMC01A
   BOM Rev         : 1
   Uses LVDS       : Y

4. To update the EEPROM you will need the master file for that particular board.
   For Kuiper Linux, the master files are located within the
   **/usr/local/src/fru_tools/masterfiles/** folder. If this does not exist or
   you are not using Kuiper Linux, you can download the files from
   :git-fru_tools:`GitHub <masterfiles>`.

Once you have located the master file for you board, update the EEPROM with it.
Below is for FMCOMMS2:

::

   root@analog:~# cat /usr/local/src/fru_tools/masterfiles/AD-FMCOMMS2-EBZ-FRU.bin > /sys/bus/i2c/devices/14-0050/eeprom

Once written it can be checked using fru-dump:

::

   root@analog:~# fru-dump -b /sys/bus/i2c/devices/14-0050/eeprom
   read 256 bytes from /sys/bus/i2c/devices/14-0050/eeprom
   Date of Man     : Mon Jul 22 20:23:00 2013
   Manufacturer    : Analog Devices
   Product Name    : AD9361 RF Hardware Development Kit
   Serial Number   : 00045
   Part Number     : AD-FMCOMMS2-EBZ
   FRU File ID     : Empty Field
   PCB Rev         : C
   PCB ID          : 9361FMC01A
   BOM Rev         : 1
   Uses LVDS       : Y

5. Once the EEPROM is updated it will be read at boot and the card should be
   correctly initialized. So at this point reboot the system

::

   root@analog:~# reboot
