.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9002/quickstart/zynq

.. _adrv9002 quickstart zynq:

ADRV9002 Zynq SoC ZC706 Quick Start Guide
=========================================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/quickstart/adrv9002_zc706_quickstart.png
   :width: 600px

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and
:adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` on:

- :xilinx:`ZC706 <ZC706>` The revision that is supported is 1.2 or higher.

Instructions on how to build the Zynq Linux kernel and devicetrees from source
can be found here:

- :dokuwiki:`Building the Zynq Linux kernel and devicetrees from source </resources/tools-software/linux-build/generic/zynq>`
- :dokuwiki:`How to build the Zynq boot image BOOT.BIN </resources/tools-software/linux-software/build-the-zynq-boot-image>`

LVDS support
------------

According to
`7 Series Select IO guide <https://www.xilinx.com/support/documentation/user_guides/ug471_7Series_SelectIO.pdf>`__
section "LVDS and LVDS_25" and Table 1-43 the LVDS I/O standard (VADJ 1.8V) is
not supported on High Range banks.

Since the evaluation board can operate only with :red:`\ **VADJ set to 1.8V**\ `
and the FMC connector on the carrier (ZC706, Zedborad) is mapped to HR banks the
**:red:`LVDS interface is not supported`**.

Required Software
-----------------

- SD Card 16GB imaged using the instructions here: :ref:`kuiper`. Use 2020_r1 or
  newer release. (Pre-released files, built using Vivado 2020.1 can be
  downloaded from
  `here <https://swdownloads.analog.com/cse/prebuilt/zynq-zc706-adv7511-adrv9002-master-2021_05_13-08_13_21.zip>`__
  )
- Copy next boot files from ``zynq-zc706-adv7511-adrv9002`` directory directly
  on sdcard ``BOOT`` partition :

  - ``BOOT.bin``
  - ``uImage``
  - ``devicetree.dtb``

- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Required Hardware
-----------------

- Xilinx :xilinx:`ZC706 <ZC706>` board - Rev 1.2 or higher
- :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` dautherboard
- Reference clock source
- Mini-USB cable
- Ethernet cable
- // :red:`Specific HW for setting VADJ to 1.8 V` //
- Optionally USB keyboard, mouse and a HDMI compatible monitor

.. todo:: .. include: /resources/eval/user-guides/adrv9002/quickstart.rst

   :start-after: .. start-#identify-your-hardware
   :end-before: .. end-#identify-your-hardware

Testing
-------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

.. figure:: http://www.xilinx.com/images/product-images/zc706-base-board.jpg

.. note::

   **:red:`Before executing below steps, VADJ must be set to 1.8V.`**

   Instruction for reprogramming the VADJ can be found
   `here <https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/960099/configure-zc706-evaluation-board-vadj-for-3-3v>`__
   and `here <https://support.xilinx.com/s/article/56811?language=en_US>`__.

   On an ADRV9002 Card, there is a red LED close to the FMC connector. The role
   of this LED is to indicate if VADJ voltage exceeded 2.0V level. If that was
   the case this LED will be ON. If this LED does not turn off after few seconds
   after boot, then there is an issue and while the board might still operate
   this is exceeding the recommended level for VADJ, decreasing board lifetime
   and can lead to permanent damage of the IC in the worst case.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/quickstart/adrv9002_vadj_led.png
   :width: 200px

- Connect the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` or
  :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` FMC board to the FPGA carrier // LPC
  FMC // socket.
- On the FMC card set switch to select clock source between:

  - an on-board 38.4MHz VCTCXO (default)
  - external (thru J501) 10MHz to 1000MHz / +13dBm

- Connect USB UART (Mini USB) to your host PC.
- Insert SD card into socket.

- Configure ZC706 for SD BOOT (Set the jumpers: The main one is: SW11 - Big Blue
  Switch in the middle, which controls the Boot Mode, it needs to be set: 1:
  Down, 2: Down, 3: Up, 4: Up, 5: Down. Other Jumpers can be checked via looking
  at the picture. (click the picture to make it bigger)).

 .. figure:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/zc706plusfmcjesdadc1.png
    :width: 200px

- Turn on the power switch on the FPGA board.
- Observe kernel and serial console messages on your terminal.
- :red:` There is supported CMOS interface only. `

::

   *

Messages
~~~~~~~~

<hidden Complete kernel boot log (Click to expand)> ::

   U-Boot 2014.07-dirty (Nov 20 2014 - 17:07:55)

   Board:  Xilinx Zynq
   I2C:   ready
   DRAM:  ECC disabled 1 GiB
   MMC:   zynq_sdhci: 0
   SF: Detected S25FL128S_64K with page size 512 Bytes, erase size 128 KiB, total 32 MiB
   *** Warning - bad CRC, using default environment

   In:    serial
   Out:   serial
   Err:   serial
   Net:   Gem.e000b000
   Hit any key to stop autoboot:  0
   Device: zynq_sdhci
   Manufacturer ID: 3
   OEM: 5344
   Name: SL16G
   Tran Speed: 50000000
   Rd Block Len: 512
   SD version 3.0
   High Capacity: Yes
   Capacity: 14.8 GiB
   Bus Width: 4-bit
   reading uEnv.txt
   389 bytes read in 24 ms (15.6 KiB/s)
   Loaded environment from uEnv.txt
   Importing environment from SD ...
   Running uenvcmd ...
   Copying Linux from SD to RAM...
   reading uImage
   6513112 bytes read in 560 ms (11.1 MiB/s)
   reading devicetree.dtb
   18382 bytes read in 28 ms (640.6 KiB/s)
   reading uramdisk.image.gz
   **Unable to read file uramdisk.image.gz**
   ## Booting kernel from Legacy Image at 03000000 ...
      Image Name:   Linux-5.4.0-g2d38bef770bc-dirty
      Image Type:   ARM Linux Kernel Image (uncompressed)
      Data Size:    6513048 Bytes = 6.2 MiB
      Load Address: 00008000
      Entry Point:  00008000
      Verifying Checksum ... OK
   ## Flattened Device Tree blob at 02a00000
      Booting using the fdt blob at 0x2a00000
      Loading Kernel Image ... OK
      Loading Device Tree to 1fff8000, end 1ffff7cd ... OK

   Starting kernel ...

   Booting Linux on physical CPU 0x0
   Linux version 5.4.0-g2d38bef770bc-dirty (dragos@debian) (gcc version 10.2.1 20201103 (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16))) #22 SMP PREEMPT Thu Mar 11 17:55:04 EET 2021
   CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
   CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   OF: fdt: Machine model: Xilinx Zynq ZED
   OF: fdt: earlycon: stdout-path /amba@0/uart@E0001000 not found
   Memory policy: Data cache writealloc
   cma: Reserved 128 MiB at 0x17c00000
   percpu: Embedded 15 pages/cpu s29516 r8192 d23732 u61440
   Built 1 zonelists, mobility grouping on.  Total pages: 130048
   Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait cpuidle.off=1
   Dentry cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
   Inode-cache hash table entries: 32768 (order: 5, 131072 bytes, linear)
   mem auto-init: stack:off, heap alloc:off, heap free:off
   Memory: 368404K/524288K available (9216K kernel code, 744K rwdata, 7000K rodata, 1024K init, 162K bss, 24812K reserved, 131072K cma-reserved, 0K highmem)
   rcu: Preemptible hierarchical RCU implementation.
   rcu:    RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
           Tasks RCU enabled.
   rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
   rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
   NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
   efuse mapped to (ptrval)
   slcr mapped to (ptrval)
   L2C: platform modifies aux control register: 0x72360000 -> 0x72760000
   L2C: DT/platform modifies aux control register: 0x72360000 -> 0x72760000
   L2C-310 erratum 769419 enabled
   L2C-310 enabling early BRESP for Cortex-A9
   L2C-310 full line of zeros enabled for Cortex-A9
   L2C-310 ID prefetch enabled, offset 1 lines
   L2C-310 dynamic clock gating enabled, standby mode enabled
   L2C-310 cache controller enabled, 8 ways, 512 kB
   L2C-310: CACHE_ID 0x410000c8, AUX_CTRL 0x76760001
   random: get_random_bytes called from start_kernel+0x2c8/0x464 with crng_init=0
   zynq_clock_init: clkc starts at (ptrval)
   Zynq clock init
   sched_clock: 64 bits at 333MHz, resolution 3ns, wraps every 4398046511103ns
   clocksource: arm_global_timer: mask: 0xffffffffffffffff max_cycles: 0x4ce07af025, max_idle_ns: 440795209040 ns
   Switching to timer-based delay loop, resolution 3ns
   clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 537538477 ns
   timer #0 at (ptrval), irq=17
   Console: colour dummy device 80x30
   Calibrating delay loop (skipped), value calculated using timer frequency.. 666.66 BogoMIPS (lpj=3333333)
   pid_max: default: 32768 minimum: 301
   Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
   Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
   CPU: Testing write buffer coherency: ok
   CPU0: Spectre v2: using BPIALL workaround
   CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
   Setting up static identity map for 0x100000 - 0x100060
   rcu: Hierarchical SRCU implementation.
   smp: Bringing up secondary CPUs ...
   CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
   CPU1: Spectre v2: using BPIALL workaround
   smp: Brought up 1 node, 2 CPUs
   SMP: Total of 2 processors activated (1333.33 BogoMIPS).
   CPU: All CPU(s) started in SVC mode.
   devtmpfs: initialized
   VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
   clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
   futex hash table entries: 512 (order: 3, 32768 bytes, linear)
   pinctrl core: initialized pinctrl subsystem
   NET: Registered protocol family 16
   DMA: preallocated 256 KiB pool for atomic coherent allocations
   hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
   hw-breakpoint: maximum watchpoint size is 4 bytes.
   zynq-ocm f800c000.ocmc: ZYNQ OCM pool: 256 KiB @ 0x(ptrval)
   e0001000.serial: ttyPS0 at MMIO 0xe0001000 (irq = 25, base_baud = 3125000) is a xuartps
   printk: console [ttyPS0] enabled
   SCSI subsystem initialized
   usbcore: registered new interface driver usbfs
   usbcore: registered new interface driver hub
   usbcore: registered new device driver usb
   mc: Linux media interface: v0.10
   videodev: Linux video capture interface: v2.00
   jesd204: found 0 devices and 0 topologies
   FPGA manager framework
   Advanced Linux Sound Architecture Driver Initialized.
   clocksource: Switched to clocksource arm_global_timer
   thermal_sys: Registered thermal governor 'step_wise'
   NET: Registered protocol family 2
   tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
   TCP established hash table entries: 4096 (order: 2, 16384 bytes, linear)
   TCP bind hash table entries: 4096 (order: 3, 32768 bytes, linear)
   TCP: Hash tables configured (established 4096 bind 4096)
   UDP hash table entries: 256 (order: 1, 8192 bytes, linear)
   UDP-Lite hash table entries: 256 (order: 1, 8192 bytes, linear)
   NET: Registered protocol family 1
   hw perfevents: no interrupt-affinity property for /pmu@f8891000, guessing.
   hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
   workingset: timestamp_bits=30 max_order=17 bucket_order=0
   io scheduler mq-deadline registered
   io scheduler kyber registered
   zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
   dma-pl330 f8003000.dmac: Loaded driver for PL330 DMAC-241330
   dma-pl330 f8003000.dmac:        DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Events-16
   brd: module loaded
   loop: module loaded
   Registered mathworks_ip class
   spi-nor spi1.0: found s25fl128s1, expected n25q128a11
   random: fast init done
   spi-nor spi1.0: s25fl128s1 (16384 Kbytes)
   5 fixed-partitions partitions found on MTD device spi1.0
   Creating 5 MTD partitions on "spi1.0":
   0x000000000000-0x000000500000 : "boot"
   0x000000500000-0x000000520000 : "bootenv"
   0x000000520000-0x000000540000 : "config"
   0x000000540000-0x000000fc0000 : "image"
   0x000000fc0000-0x000001000000 : "spare"
   MACsec IEEE 802.1AE
   libphy: Fixed MDIO Bus: probed
   tun: Universal TUN/TAP device driver, 1.6
   libphy: MACB_mii_bus: probed
   mdio_bus e000b000.ethernet-ffffffff: MDIO device at address 0 is missing.
   usbcore: registered new interface driver asix
   usbcore: registered new interface driver ax88179_178a
   usbcore: registered new interface driver cdc_ether
   usbcore: registered new interface driver net1080
   usbcore: registered new interface driver cdc_subset
   usbcore: registered new interface driver zaurus
   usbcore: registered new interface driver cdc_ncm
   ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
   usbcore: registered new interface driver uas
   usbcore: registered new interface driver usb-storage
   usbcore: registered new interface driver usbserial_generic
   usbserial: USB Serial support registered for generic
   usbcore: registered new interface driver ftdi_sio
   usbserial: USB Serial support registered for FTDI USB Serial Device
   usbcore: registered new interface driver upd78f0730
   usbserial: USB Serial support registered for upd78f0730
   chipidea-usb2 e0002000.usb: e0002000.usb supply vbus not found, using dummy regulator
   ULPI transceiver vendor/product ID 0x0424/0x0007
   Found SMSC USB3320 ULPI transceiver.
   ULPI integrity check: passed.
   ci_hdrc ci_hdrc.0: EHCI Host Controller
   ci_hdrc ci_hdrc.0: new USB bus registered, assigned bus number 1
   ci_hdrc ci_hdrc.0: USB 2.0 started, EHCI 1.00
   usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
   usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   usb usb1: Product: EHCI Host Controller
   usb usb1: Manufacturer: Linux 5.4.0-g2d38bef770bc-dirty ehci_hcd
   usb usb1: SerialNumber: ci_hdrc.0
   hub 1-0:1.0: USB hub found
   hub 1-0:1.0: 1 port detected
   i2c /dev entries driver
   adv7511 0-0039: 0-0039 supply avdd not found, using dummy regulator
   adv7511 0-0039: 0-0039 supply dvdd not found, using dummy regulator
   adv7511 0-0039: 0-0039 supply pvdd not found, using dummy regulator
   adv7511 0-0039: 0-0039 supply bgvdd not found, using dummy regulator
   adv7511 0-0039: 0-0039 supply dvdd-3v not found, using dummy regulator
   adv7511: probe of 0-0039 failed with error -5
   xiic-i2c 41620000.i2c: IRQ index 0 not found
   usbcore: registered new interface driver uvcvideo
   USB Video Class driver (1.1.1)
   gspca_main: v2.14.0 registered
   cdns-wdt f8005000.watchdog: Xilinx Watchdog Timer with timeout 10s
   Xilinx Zynq CpuIdle Driver started
   failed to register cpuidle driver
   sdhci: Secure Digital Host Controller Interface driver
   sdhci: Copyright(c) Pierre Ossman
   sdhci-pltfm: SDHCI platform and OF driver helper
   mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
   ledtrig-cpu: registered to indicate activity on CPUs
   hidraw: raw HID events driver (C) Jiri Kosina
   usbcore: registered new interface driver usbhid
   usbhid: USB HID core driver
   axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
   axi_sysid 45000000.axi-sysid-0: [adrv9001] [CMOS_LVDS_N=1] on [zc706] git branch <dev_adrv9001_a10soc_zc706> git <9331186e2289103cfb641d9991c4ca809fe57476> clean [2021-02-26 08:58:42] UTC
   fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
   usbcore: registered new interface driver snd-usb-audio
   axi-i2s 77600000.axi-i2s: probed, capture enabled, playback enabled
   NET: Registered protocol family 10
   Segment Routing with IPv6
   mmc0: new high speed SDHC card at address aaaa
   sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   mmcblk0: mmc0:aaaa SL16G 14.8 GiB
   NET: Registered protocol family 17
    mmcblk0: p1 p2 p3
   NET: Registered protocol family 36
   Registering SWP/SWPB emulation handler
   random: crng init done
   adrv9002 spi0.0: adrv9002-phy Rev 11.0, Firmware 0.13.6.7,  Stream 0.5.18.0,  API version: 39.0.7 successfully initialized
   cf_axi_adc 44a00000.axi-adrv9002-rx-lpc: ADI AIM (10.01.b) at 0x44A00000 mapped to 0xe9f1d723, probed ADC ADRV9002 as MASTER
   cf_axi_tdd 44a0c800.axi-adrv9002-core-tdd-lpc: Analog Devices CF_AXI_TDD MASTER (1.00.a)
   cf_axi_dds 44a0a000.axi-adrv9002-tx-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x44A0A000 mapped to 0x1b2fbc4a, probed DDS ADRV9002
   asoc-simple-card zed_sound: adau-hifi <-> 77600000.axi-i2s mapping ok
   adau1761 0-003b: Unable to sync registers 0x4002-0x4002. -5
   hctosys: unable to open rtc device (rtc0)
   ALSA device list:
     #0: ZED ADAU1761
   EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   VFS: Mounted root (ext4 filesystem) on device 179:2.
   devtmpfs: mounted
   Freeing unused kernel memory: 1024K
   Run /sbin/init as init process
   systemd[1]: System time before build time, advancing clock.
   systemd[1]: Failed to lookup module alias 'autofs4': Function not implemented
   systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
   systemd[1]: Detected architecture arm.

   Welcome to Kuiper GNU/Linux 10 (buster)!

   systemd[1]: Set hostname to <analog>.
   systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
   systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
   systemd[1]: Listening on Journal Socket (/dev/log).
   [  OK  ] Listening on Journal Socket (/dev/log).
   systemd[1]: Listening on fsck to fsckd communication Socket.
   [  OK  ] Listening on fsck to fsckd communication Socket.
   systemd[1]: Created slice system-serial\x2dgetty.slice.
   [  OK  ] Created slice system-serial\x2dgetty.slice.
   systemd[1]: Listening on Journal Socket.
   [  OK  ] Listening on Journal Socket.
   systemd[1]: Mounting RPC Pipe File System...
            Mounting RPC Pipe File System...
   [  OK  ] Created slice User and Session Slice.
   [  OK  ] Created slice system-systemd\x2dfsck.slice.
   [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
            Starting Load Kernel Modules...
   [  OK  ] Listening on udev Kernel Socket.
   [  OK  ] Listening on Syslog Socket.
   [  OK  ] Listening on udev Control Socket.
            Starting udev Coldplug all Devices...
            Mounting Kernel Debug File System...
            Starting Journal Service...
            Starting Restore / save the current clock...
   [  OK  ] Reached target Slices.
   [  OK  ] Created slice system-getty.slice.
            Starting Set the console keyboard layout...
   [  OK  ] Listening on initctl Compatibility Named Pipe.
   [  OK  ] Reached target Swap.
   [  OK  ] Started Journal Service.
   [FAILED] Failed to mount RPC Pipe File System.
   See 'systemctl status run-rpc_pipefs.mount' for details.
   [DEPEND] Dependency failed for RPC …ice for NFS client and server.
   [DEPEND] Dependency failed for RPC …curity service for NFS server.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Mounted Kernel Debug File System.
   [  OK  ] Started Restore / save the current clock.
            Starting Remount Root and Kernel File Systems...
            Mounting Kernel Configuration File System...
            Starting Apply Kernel Variables...
   [  OK  ] Reached target NFS client services.
   [  OK  ] Reached target Remote File Systems (Pre).
   [  OK  ] Reached target Remote File Systems.
   [  OK  ] Started Set the console keyboard layout.
   [  OK  ] Mounted Kernel Configuration File System.
   [  OK  ] Started Apply Kernel Variables.
   [  OK  ] Started udev Coldplug all Devices.
            Starting Helper to synchronize boot up for ifupdown...
   [  OK  ] Started Helper to synchronize boot up for ifupdown.
   [  OK  ] Started Remount Root and Kernel File Systems.
            Starting Load/Save Random Seed...
            Starting Flush Journal to Persistent Storage...
            Starting Create System Users...
   [  OK  ] Started Load/Save Random Seed.
   [  OK  ] Started Create System Users.
   [  OK  ] Started Flush Journal to Persistent Storage.
            Starting Create Static Device Nodes in /dev...
   [  OK  ] Started Create Static Device Nodes in /dev.
            Starting udev Kernel Device Manager...
   [  OK  ] Reached target Local File Systems (Pre).
   [  OK  ] Started udev Kernel Device Manager.
            Starting Show Plymouth Boot Screen...
   [  OK  ] Started Show Plymouth Boot Screen.
   [  OK  ] Reached target Local Encrypted Volumes.
   [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
   [  OK  ] Found device /dev/ttyPS0.
   [  OK  ] Found device /dev/disk/by-partuuid/0e0f8290-01.
            Starting Load Kernel Modules...
            Starting File System Check…isk/by-partuuid/0e0f8290-01...
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Started File System Check Daemon to report status.
   [  OK  ] Started File System Check …/disk/by-partuuid/0e0f8290-01.
            Mounting /boot...
   [  OK  ] Mounted /boot.
   [  OK  ] Reached target Local File Systems.
            Starting Set console font and keymap...
            Starting Raise network interfaces...
            Starting Create Volatile Files and Directories...
            Starting Preprocess NFS configuration...
            Starting Tell Plymouth To Write Out Runtime Data...
   [  OK  ] Started Set console font and keymap.
   [  OK  ] Started Preprocess NFS configuration.
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [  OK  ] Started Create Volatile Files and Directories.
            Starting Network Time Synchronization...
            Starting Update UTMP about System Boot/Shutdown...
   [  OK  ] Started Update UTMP about System Boot/Shutdown.
   [  OK  ] Started Network Time Synchronization.
   [  OK  ] Reached target System Time Synchronized.
   [  OK  ] Reached target System Initialization.
   [  OK  ] Listening on triggerhappy.socket.
   [  OK  ] Listening on D-Bus System Message Bus Socket.
   [  OK  ] Listening on CUPS Scheduler.
   [  OK  ] Started Daily rotation of log files.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Reached target Paths.
   [  OK  ] Started Daily man-db regeneration.
   [  OK  ] Started Daily Cleanup of Temporary Directories.
   [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
   [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
   [  OK  ] Reached target Sockets.
   [  OK  ] Reached target Basic System.
            Starting Modem Manager...
            Starting System Logging Service...
            Starting triggerhappy global hotkey daemon...
            Starting Login Service...
            Starting Check for Raspberry Pi EEPROM updates...
            Starting rng-tools.service...
   [  OK  ] Started Regular background program processing daemon.
   [  OK  ] Started Manage Sound Card State (restore and store).
            Starting Save/Restore Sound Card State...
   [  OK  ] Started D-Bus System Message Bus.
            Starting WPA supplicant...
            Starting dhcpcd on all interfaces...
            Starting Disk Manager...
            Starting LSB: Switch to on…nless shift key is pressed)...
            Starting Avahi mDNS/DNS-SD Stack...
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Started Daily apt download activities.
   [  OK  ] Started Daily apt upgrade and clean activities.
   [  OK  ] Reached target Timers.
            Starting dphys-swapfile - …unt, and delete a swap file...
   [  OK  ] Started triggerhappy global hotkey daemon.
   [  OK  ] Started System Logging Service.
   [  OK  ] Started Raise network interfaces.
   [  OK  ] Started Check for Raspberry Pi EEPROM updates.
   [FAILED] Failed to start rng-tools.service.
   See 'systemctl status rng-tools.service' for details.
   [  OK  ] Started Login Service.
   [  OK  ] Started Save/Restore Sound Card State.
   [  OK  ] Started dhcpcd on all interfaces.
   [  OK  ] Started Avahi mDNS/DNS-SD Stack.
   [  OK  ] Started WPA supplicant.
            Starting Authorization Manager...
   [  OK  ] Started Make remote CUPS printers available locally.
   [  OK  ] Reached target Network.
            Starting OpenBSD Secure Shell server...
            Starting Permit User Sessions...
            Starting /etc/rc.local Compatibility...
   [  OK  ] Started IIO Daemon.
   [  OK  ] Reached target Sound Card.
   [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
   [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
   [  OK  ] Started /etc/rc.local Compatibility.
   [  OK  ] Started Permit User Sessions.
            Starting Hold until boot process finishes up...
            Starting Light Display Manager...
   [  OK  ] Started OpenBSD Secure Shell server.
   [  OK  ] Started Authorization Manager.

   Raspbian GNU/Linux 10 analog ttyPS0

   analog login:

</hidden>

These devices should be present:

::

   analog@analog:~$ iio_info | grep iio:device
           iio:device0: adrv9002-phy
           iio:device1: xadc
           iio:device2: axi-adrv9002-rx-lpc (buffer capable)
           iio:device3: axi-adrv9002-core-tdd-lpc
           iio:device4: axi-adrv9002-tx-lpc (buffer capable)

For more on device modes, check
:dokuwiki:`device modes. </resources/tools-software/linux-drivers/iio-transceiver/adrv9002#device_modes>`

Pyadi-iio Example
~~~~~~~~~~~~~~~~~

Pyadi-iio is a python abstraction module for ADI hardware with IIO drivers to
make them easier to use. For more check
`Pyadi-iio <https://github.com/analogdevicesinc/pyadi-iio>`__. An example of
using adrv9002 can be checked
:git-pyadi-iio:`here <examples/adrv9002_example.py+>`

IIO Oscilloscope Remote
~~~~~~~~~~~~~~~~~~~~~~~

Please see also
here:`Oscilloscope </resources/tools-software/linux-software/iio_oscilloscope>`__

The IIO Oscilloscope application can be used to connect to another platform that
has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP
address of the target in the popup window.

Shut down
~~~~~~~~~

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be
   taken not to corrupt the file system – please shut down things, don"t just
   turn off the power switch. Depending on your monitor, the standard power off
   could be hiding. You can do this from the terminal as well with ""sudo
   shutdown -h now""

   .. figure:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
      :width: 300px

.. todo:: .. include: /resources/eval/user-guides/adrv9002/common.rst

   :start-after: .. start-#more-information
   :end-before: .. end-#more-information

.. todo:: .. include: /resources/eval/user-guides/adrv9002/common.rst

   :start-after: .. start-#support
   :end-before: .. end-#support
