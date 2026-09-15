.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal/arradio_noos

.. _ad-fmcomms2-ebz software baremetal arradio_noos:

NO TITLE
========

.. important::

   This is a legacy page for a product that is no longer supported within the
   no-OS framework.

ARRadio No-OS Quick Start Guide
-------------------------------

This quick start guide shows you how to run the No-OS (baremetal) application on
the ARRadio/C5SoC Kit. This guide may appear very simple, and it is if you have
the right platform which is a Linux machine. This guide does NOT use "armcc" the
ARM compiler nor the ARM-DS5 (paid license). It uses the GNU variant "gcc" to
compile the no-OS application. It builds the bsp image with u-boot and then
programs the fpga and runs the application using u-boot script.

Requirements
~~~~~~~~~~~~

- A host machine with all the tools installed and be available on a command line
  (see note below)
- ARRadio
- Cyclone-V SoC Kit
- SD-card & USB cables

.. note::

   It is absolutely vital that you have an environment that is capable of
   supporting this flow. We exclusively use Linux platforms (Ubuntu and Red Hat
   specifically). Our understanding of operating systems and tools are limited.
   So while it may be possible to run these things on a Windows machine, we do
   not know for sure it will. It is up to you to choose and setup your platform
   to run these tools. If a tool returns an error, try to google that error,
   most likely you will find an answer (may not be a solution) very quickly.

Download/Clone Repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may need to replace "dev" with a known release below.

::

   <nowiki>
   [some-dir]> git clone -b dev :git-hdl
   [some-dir]> git clone -b dev https::`/github.com/analogdevicesinc/no-OS+`

   </nowiki>

You should now have the hdl and no-OS folders in the "some-dir" folder.

Build HDL project
~~~~~~~~~~~~~~~~~

::

   [some-dir]> make -C hdl/projects/arrado/c5soc

If built successfully you should have the "sof" file for the Cyclone-V device.

Build No-OS project
~~~~~~~~~~~~~~~~~~~

::

   [some-dir]> make -C no-OS/arrado/c5soc

If built successfully you should have the "rbf" and "bin" files for SoC kit.

Prepare a Micro SD Card for first time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   The following procedure is one among many methods in achieving its goal. You
   may skip this section, combine multiple sections in a single flow or do
   something entirely different. It is all up to you to decide and follow a
   method. The only and important thing is that you must be comfortable in your
   chosen method. Do not mindlessly copy and execute these commands. If a
   command is missing ``Google It`` first, understand its function and either
   install it or find an alternative in your system.

In this part, you are going to overwrite a drive (if you aren"t careful you will
overwrite your machine"s drive and loose any OS or files on it).

You need to find out your SD card device (here, mine is sdb). Also you may need
to unmount it first.

The card must be partitioned in certain way (need raw and fat). The commands to
do this are below, I have also included my terminal log as a reference.

::

   [some-dir]> sudo sfdisk /dev/sdX < no-OS/arradio/c5soc/format.sfdisk

::

   [~/github/no-OS/arradio/c5soc]> sudo sfdisk /dev/sdb < format.sfdisk
   Checking that no-one is using this disk right now ... OK

   Disk /dev/sdb: 7.5 GiB, 8026849280 bytes, 15677440 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0xa9d78a8b

   Old situation:

   Device     Boot   Start     End Sectors  Size Id Type
   /dev/sdb1          2048 1026048 1024001  500M  b W95 FAT32
   /dev/sdb3       1026049 1028097    2049    1M a2 unknown

   >>> Script header accepted.
   >>> Script header accepted.
   >>> Script header accepted.
   >>> Script header accepted.
   >>> Created a new DOS disklabel with disk identifier 0xa9d78a8b.
   Created a new partition 1 of type 'W95 FAT32' and of size 500 MiB.
   /dev/sdb2: Created a new partition 3 of type 'Unknown' and of size 1 MiB.
   /dev/sdb4:
   New situation:

   Device     Boot   Start     End Sectors  Size Id Type
   /dev/sdb1          2048 1026048 1024001  500M  b W95 FAT32
   /dev/sdb3       1026049 1028097    2049    1M a2 unknown

   The partition table has been altered.
   Calling ioctl() to re-read partition table.
   Syncing disks.

We may need to format the newly created partition.

::

   [some-dir]> sudo mkfs -t vfat /dev/sdX1

::

   [~/github/no-OS/arradio/c5soc]> sudo mkfs -t vfat /dev/sdb1
   mkfs.fat 3.0.28 (2015-05-16)

Unmount and eject the sd-card. It is only formatted now. You don"t need to
format the same SD card again, simply copy the files if you have one already
formatted.

::

   [some-dir]> sudo udisksctl unmount -b /dev/sdX1
   [some-dir]> sudo udisksctl power-off -b /dev/sdX

::

   [~/github/no-OS/arradio/c5soc]> sudo udisksctl unmount -b /dev/sdb1
   Unmounted /dev/sdb1.
   [~/github/no-OS/arradio/c5soc]> sudo udisksctl power-off -b /dev/sdb

Copy system image (U-boot & Initialization) to SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Insert the formatted SD card in your PC. The u-boot binary goes into the raw
partition. These steps needs to be repeated ONLY if you have modified the HPS
core in HDL and/or BSP sources.

::

   [some-dir]> sudo dd if=no-OS/arradio/c5soc/bsp/arradio_c5soc_uboot.bin of=/dev/sdX3
   [some-dir]> sudo sync

::

   [~/github/no-OS/arradio/c5soc]> sudo dd if=bsp/arradio_c5soc_uboot.bin
   of=/dev/sdb3
   977+1 records in
   977+1 records out
   500468 bytes (500 kB, 489 KiB) copied, 0.0619104 s, 8.1 MB/s
   [~/github/no-OS/arradio/c5soc]> sudo sync

Unmount and eject the sd-card.

::

   [some-dir]> sudo udisksctl unmount -b /dev/sdX1
   [some-dir]> sudo udisksctl power-off -b /dev/sdX

::

   [~/github/no-OS/arradio/c5soc]> sudo udisksctl unmount -b /dev/sdb1
   Unmounted /dev/sdb1.
   [~/github/no-OS/arradio/c5soc]> sudo udisksctl power-off -b /dev/sdb

Copy FPGA, Application image, and U-boot script to SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Insert the formatted SD card in your PC. The OS should mount the FAT partition
automatically. The bit, elf, and script files goes to this fat partition. These
steps needs to be repeated ONLY if you have modified the QSYS (or FPAG) design
in HDL and/or the no-OS sources.

::

   [some-dir]> cp no-OS/arradio/c5soc/hw/arradio_c5soc.rbf <sdX1-mount-directory>
   [some-dir]> cp no-OS/arradio/c5soc/sw/arradio_c5soc.bin <sdX1-mount-directory>
   [some-dir]> cp no-OS/arradio/c5soc/u-boot.scr <sdX1-mount-directory>

::

   [~/github/no-OS/arradio/c5soc]> cp hw/arradio_c5soc.rbf
   /media/rkutty/08DA-432B/
   [~/github/no-OS/arradio/c5soc]> cp sw/arradio_c5soc.bin
   /media/rkutty/08DA-432B/
   [~/github/no-OS/arradio/c5soc]> cp u-boot.scr /media/rkutty/08DA-432B/

You may do this using make.

::

   [~/github/no-OS/arradio/c5soc]> make sd-dir=/media/rkutty/08DA-432B/

Unmount and eject the sd-card.

::

   [some-dir]> sudo udisksctl unmount -b /dev/sdX1
   [some-dir]> sudo udisksctl power-off -b /dev/sdX

::

   [~/github/no-OS/arradio/c5soc]> sudo udisksctl unmount -b /dev/sdb1
   Unmounted /dev/sdb1.
   [~/github/no-OS/arradio/c5soc]> sudo udisksctl power-off -b /dev/sdb

Running the no-OS software
~~~~~~~~~~~~~~~~~~~~~~~~~~

Insert the sd-card into the Cyclone V SoC kit and power cycle the board. You
should also connect the UART. The UART log indicates u-boot loading the FPGA bit
files, enabling the HPS-FPGA bridges and running the no-OS application.

::

   U-Boot SPL 2013.01.01 (Sep 05 2017 - 13:23:12)
   BOARD : Altera SOCFPGA Cyclone V Board
   CLOCK: EOSC1 clock 25000 KHz
   CLOCK: EOSC2 clock 25000 KHz
   CLOCK: F2S_SDR_REF clock 0 KHz
   CLOCK: F2S_PER_REF clock 0 KHz
   CLOCK: MPU clock 800 MHz
   CLOCK: DDR clock 400 MHz
   CLOCK: UART clock 100000 KHz
   CLOCK: MMC clock 50000 KHz
   CLOCK: QSPI clock 400000 KHz
   RESET: WARM
   SDRAM: Initializing MMR registers
   SDRAM: Calibrating PHY
   SEQ.C: Preparing to start memory calibration
   SEQ.C: CALIBRATION PASSED
   SDRAM: 1024 MiB
   ALTERA DWMMC: 0

   U-Boot 2013.01.01 (Sep 05 2017 - 13:23:18)

   CPU   : Altera SOCFPGA Platform
   BOARD : Altera SOCFPGA Cyclone V Board
   I2C:   ready
   DRAM:  1 GiB
   MMC:   ALTERA DWMMC: 0
   * Warning - bad CRC, using default environment

   In:    serial
   Out:   serial
   Err:   serial
   Skipped ethaddr assignment due to invalid EMAC address in EEPROM
   Net:   mii0
   Warning: failed to set MAC address

   Hit any key to stop autoboot:  0
   reading u-boot.scr
   229 bytes read in 5 ms (43.9 KiB/s)
   ## Executing script at 02000000
   reading arradio_c5soc.rbf
   7007204 bytes read in 334 ms (20 MiB/s)
   ## Starting application at 0x3FF795A4 ...
   ## Application terminated, rc = 0x0
   reading arradio_c5soc.bin
   197960 bytes read in 16 ms (11.8 MiB/s)
   ## Starting application at 0x00100000 ...
   <-- SEE BELOW -->
   Done.

.. note::

   The design supports both 2R2T mode (AD9361 only) and 1R1T mode (AD9361 and
   AD9364). The rest of the UART log will be different accordingly.

Running the no-OS software (2R2T)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default make builds the software in 2R2T mode. You may make sure such is the
case by looking at these two variables.

::

   -DAD9361_DEVICE=1 -DAD9364_DEVICE=0

Here is the full make command.

::

   [~/github/no-OS/arradio/c5soc]> make
   arm-altera-eabi-gcc -g -O0 -mcpu=cortex-a9 -mfloat-abi=softfp -mfpu=neon 
           -Wall -Werror -std=c99 -o sw/arradio_c5soc.axf -DHPS -Dsoc_cv_av 
           -T/opt/altera/16.1/embedded/host_tools/mentor/gnu/arm/baremetal/arm-altera-eabi/lib/cycloneV-dk-ram.ld 
           -I/opt/altera/16.1/embedded/ip/altera/hps/altera_hps/hwlib/include 
           -I/opt/altera/16.1/embedded/ip/altera/hps/altera_hps/hwlib/include/soc_cv_av 
           -I/opt/altera/16.1/embedded/ip/altera/hps/altera_hps/hwlib/include/soc_cv_av/socal 
           -Isw -Ibsp/generated -DCONFIG_H_ -DAXI_ADC_NOT_LEGACY_DIGITAL_TUNE -DHAVE_VERBOSE_MESSAGES -DHAVE_SPLIT_GAIN_TABLE=1 -DHAVE_TDD_SYNTH_TABLE=1 -DAD9361_DEVICE=1 -DAD9364_DEVICE=0 -DAD9363A_DEVICE=0 -DARRADIO  -I../../../no-OS/ad9361/sw -I../../../no-OS/ad9361/sw/platform_altera ../../../no-OS/arradio/c5soc/alt_retarget_gnu.c  ../../../no-OS/ad9361/sw/ad9361_api.c ../../../no-OS/ad9361/sw/ad9361.c ../../../no-OS/ad9361/sw/ad9361_conv.c ../../../no-OS/ad9361/sw/main.c ../../../no-OS/ad9361/sw/util.c  ../../../no-OS/ad9361/sw/platform_altera/platform.c ../../../no-OS/ad9361/sw/platform_altera/adc_core.c ../../../no-OS/ad9361/sw/platform_altera/dac_core.c
   arm-altera-eabi-objcopy -O binary sw/arradio_c5soc.axf sw/arradio_c5soc.bin

The UART log:

::

   reading u-boot.scr
   229 bytes read in 4 ms (55.7 KiB/s)
   ## Executing script at 02000000
   reading arradio_c5soc.rbf
   7007204 bytes read in 334 ms (20 MiB/s)
   ## Starting application at 0x3FF795A4 ...
   ## Application terminated, rc = 0x0
   reading arradio_c5soc.bin
   194920 bytes read in 16 ms (11.6 MiB/s)
   ## Starting application at 0x00100000 ...
   adc_init: interface clock is (61 MHz).
   ad9361_dig_tune: interface clock is (122 MHz).
   -0f-0f-0f-0f-00-00-00-00-0f-0f-0f-10-0f-00-00-00
   15 --- 5 --- 4 --- 7
   -0f-0f-0f-0f-0f-0f-0f-0f-0f-0f-0f-0a-00-00-00-00
   -0f-05-00-00-00-00-00-0b-0f-0f-0f-0f-0f-0f-0f-0f
   143 --- 4 --- 2 --- 6
   ad9361_init : AD936x Rev 2 successfully initialized
   Done.

Running the no-OS software (1R1T)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build the design in 1R1T mode, invoke make as follows.

::

   make DEFINE=1R1T

You may verify the mode by checking the variables.

::

   -DAD9361_DEVICE=0 -DAD9364_DEVICE=1

Here is the full make command.

::

   [~/github/no-OS/arradio/c5soc]> make DEFINE=1R1T
   arm-altera-eabi-gcc -g -O0 -mcpu=cortex-a9 -mfloat-abi=softfp -mfpu=neon 
           -Wall -Werror -std=c99 -o sw/arradio_c5soc.axf -DHPS -Dsoc_cv_av 
           -T/opt/altera/16.1/embedded/host_tools/mentor/gnu/arm/baremetal/arm-altera-eabi/lib/cycloneV-dk-ram.ld 
           -I/opt/altera/16.1/embedded/ip/altera/hps/altera_hps/hwlib/include 
           -I/opt/altera/16.1/embedded/ip/altera/hps/altera_hps/hwlib/include/soc_cv_av 
           -I/opt/altera/16.1/embedded/ip/altera/hps/altera_hps/hwlib/include/soc_cv_av/socal 
           -Isw -Ibsp/generated -DCONFIG_H_ -DAXI_ADC_NOT_LEGACY_DIGITAL_TUNE -DHAVE_VERBOSE_MESSAGES -DHAVE_SPLIT_GAIN_TABLE=1 -DHAVE_TDD_SYNTH_TABLE=1 -DAD9361_DEVICE=0 -DAD9364_DEVICE=1 -DAD9363A_DEVICE=0 -DARRADIO  -I../../../no-OS/ad9361/sw -I../../../no-OS/ad9361/sw/platform_altera ../../../no-OS/arradio/c5soc/alt_retarget_gnu.c  ../../../no-OS/ad9361/sw/ad9361_api.c ../../../no-OS/ad9361/sw/ad9361.c ../../../no-OS/ad9361/sw/ad9361_conv.c ../../../no-OS/ad9361/sw/main.c ../../../no-OS/ad9361/sw/util.c  ../../../no-OS/ad9361/sw/platform_altera/platform.c ../../../no-OS/ad9361/sw/platform_altera/adc_core.c ../../../no-OS/ad9361/sw/platform_altera/dac_core.c
   arm-altera-eabi-objcopy -O binary sw/arradio_c5soc.axf sw/arradio_c5soc.bin

The UART log:

::

   reading u-boot.scr
   229 bytes read in 4 ms (55.7 KiB/s)
   ## Executing script at 02000000
   reading arradio_c5soc.rbf
   7007204 bytes read in 334 ms (20 MiB/s)
   ## Starting application at 0x3FF795A4 ...
   ## Application terminated, rc = 0x0
   reading arradio_c5soc.bin
   195048 bytes read in 15 ms (12.4 MiB/s)
   ## Starting application at 0x00100000 ...
   adc_init: interface clock is (30 MHz).
   ad9361_dig_tune: interface clock is (61 MHz).
   -00-00-00-00-03-03-03-03-00-00-00-00-00-00-00-00
   15 --- 11 --- 8 --- 15
   -03-03-03-03-03-03-03-03-03-03-03-03-03-03-03-03
   -03-01-00-00-00-00-00-00-00-00-00-00-00-00-00-00
   143 --- 8 --- 2 --- 15
   ad9361_init : AD936x Rev 2 successfully initialized
   Done.

Switching between 2R2T & 1R1T mode(s)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the first run, the build remembers (until you do a clean) your mode of
choice and subsequent builds (in case you modify the sources) assume this mode
as default. As a precaution, always cross check the compiler flags mentioned
above with your desired mode.

::

   [some-dir]> make -C no-OS/arrado/c5soc DEFINE=2R2T /*building in 2R2T mode*/
   [some-dir]> make -C no-OS/arrado/c5soc  /*build assumes 2R2T mode*/
   [some-dir]> make -C no-OS/arrado/c5soc DEFINE=1R1T /*building in 1R1T mode*/
   [some-dir]> make -C no-OS/arrado/c5soc  /*build assumes 1R1T mode*/
