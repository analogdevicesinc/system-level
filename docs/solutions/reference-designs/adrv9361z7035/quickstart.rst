.. _adrv9361z7035 quickstart:

Quick Start Guide
=================

.. image:: images/adrv9361-z7035-top-web.png
   :alt: ADRV9361-Z7035 Board
   :align: right
   :width: 250

This Quick start guide is to provide users with a simplified, concise set of
instructions for setting up :adi:`ADRV9361-Z7035` on various SDR Module Carrier
development boards. The :adi:`ADRV9361-Z7035` is a development kit from Analog
Devices that consists of a hardware platform (ZC7035 board) and a software
package (HDL design, Linux BSP, and no-OS drivers) for the ADRV9361-SOM
system-on-module (SOM). See :ref:`Introduction to ADRV9361-Z7035 <adrv9361z7035 introduction>`
for further details.

Carrier Support
---------------

The ADRV9361-Z7035 supports all features on the :adi:`ADRV1CRR-FMC <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-FMC.html>`
carrier board. The ADRV9364-Z7020 supports a subset of features because the Zynq
Z7020 has fewer available user I/Os. For the ADRV9364-Z7020 it is recommended to
use the :adi:`ADRV1CRR-BOB <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADRV1CRR-BOB.html>`
carrier.

+----------------------+----------------------+
| ADRV1CRR-FMC         | ADRV1CRR-BOB         |
+======================+======================+
| |adrv1crr-fmc-image| | |adrv1crr-bob-image| |
+----------------------+----------------------+

Required Software
-----------------

- SD Card 16GB (minimum size) imaged using the instructions here: :ref:`SDCARD for Zynq & Altera SoC Quick Start Guide <kuiper>`.
- Copy next boot files from ``zynq-adrv9361-z7035-fmc`` directory directly on
  sdcard ``BOOT`` partition :

   -  ``BOOT.bin``
   -  ``devicetree.dtb``

- Then copy image from ``zynq-common``:

   -  ``uImage``

- A UART terminal (Putty/Tera Term/Minicom, etc.),

   -  Set Speed/Baud rate to 115200 (8N1).
   -  For USB - UART driver missing issue, visit this link below:

      -  https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads

Required Hardware
-----------------

- :adi:`ADRV9361-Z7035 <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adrv9361-z7035.html>` board
- :adi:`ADRV1CRR-FMC` board
- Micro-USB 2.0 uart cable
- Ethernet cable
- Power supply connector
- Laptop
- OTG cable for USB keyboard, mouse and other peripherals (Optional)
- HDMI compatible monitor (Optional)

Example Device Trees
--------------------

+----------+---------------------------------------------------------------+
| Function | File                                                          |
+==========+===============================================================+
| dtsi     | :git-linux:`arch/arm/boot/dts/xilinx/zynq-adrv9361-z7035.dtsi`|
+----------+---------------------------------------------------------------+
| dtsi     | :git-linux:`arch/arm/boot/dts/adi-fmcomms2.dtsi`              |
+----------+---------------------------------------------------------------+

Testing
=======

.. esd-warning::

.. image:: images/adrv9361-z7035-fmc-setup_quickstart.png
   :alt: adrv9361-z7035-fmc-setup_quickstart.png

- Connect the :adi:`ADRV1CRR-FMC` FMC board to `ADRV9361-Z7035
  <https://www.xilinx.com/ADRV9361-Z7035>`_ board socket.
- Connect USB UART (Micro USB 2.0) to your host PC/laptop.

   -  (Optional) Connect HDMI cable to monitor.
   -  (Optional) Connect OTG for keyboard, mouse and other peripherals.

- Plug the Ethernet cable in *ETHERNET 1* port in the FMC board then connect to
  network.
- Connect power supply connector.
- Insert micro sdcard into `ADRV9361-Z7035 <https://www.xilinx.com/ADRV9361-Z7035>`_ sd slot.
- Turn on the power switch on the fmc board.
- Open Teraterm and select serial port for terminal messages.
- Observe kernel and serial console messages on your terminal.

Messages
--------

.. collapsible:: Complete kernel boot log (Click to expand)

   .. container:: box bggreen

      This specifies any shell prompt running on the target

      ::

         U-Boot 2018.01-21441-ga6ab387 (Aug 31 2022 - 11:43:06 +0100), Build: jenkins-development-build_uboot-2

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
         reading uEnv.txt
         407 bytes read in 19 ms (20.5 KiB/s)
         Importing environment from SD ...
         Hit any key to stop autoboot:  0
         Device: sdhci@e0100000
         Manufacturer ID: 3
         OEM: 5344
         Name: SP32G
         Tran Speed: 50000000
         Rd Block Len: 512
         SD version 3.0
         High Capacity: Yes
         Capacity: 29.7 GiB
         Bus Width: 4-bit
         Erase Group Size: 512 Bytes
         reading uEnv.txt
         407 bytes read in 19 ms (20.5 KiB/s)
         Loaded environment from uEnv.txt
         Importing environment from SD ...
         Running uenvcmd ...
         Copying Linux from SD to RAM...
         reading uImage
         7754888 bytes read in 448 ms (16.5 MiB/s)
         reading devicetree.dtb
         28708 bytes read in 26 ms (1.1 MiB/s)
          Unable to read file uramdisk.image.gz
         ## Booting kernel from Legacy Image at 03000000 ...
            Image Name:   Linux-5.15.0-175730-gcdaccc1f233
            Image Type:   ARM Linux Kernel Image (uncompressed)
            Data Size:    7754824 Bytes = 7.4 MiB
            Load Address: 00008000
            Entry Point:  00008000
            Verifying Checksum ... OK
         ## Flattened Device Tree blob at 02a00000
            Booting using the fdt blob at 0x2a00000
            Loading Kernel Image ... OK
            Loading Device Tree to 1eb10000, end 1eb1a023 ... OK

         Starting kernel ...

         Booting Linux on physical CPU 0x0
         Linux version 5.15.0-175730-gcdaccc1f2334 (jenkins@romlxbuild2) (arm-xilinx-linux-gnueabi-gcc.real (GCC) 11.2.0, GNU ld (GNU Binutils) 2.37.20210721) #3276 SMP PREEMPT Fri Apr 21 06:46:11 IST 2023
         CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
         CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
         OF: fdt: Machine model: Analog Devices ADRV9361-Z7035 (Z7035/AD9361)
         OF: fdt: earlycon: stdout-path /amba@0/uart@E0001000 not found
         Memory policy: Data cache writealloc
         cma: Reserved 128 MiB at 0x16800000
         Zone ranges:
           Normal   [mem 0x0000000000000000-0x000000001fffffff]
           HighMem  empty
         Movable zone start for each node
         Early memory node ranges
           node   0: [mem 0x0000000000000000-0x000000001fffffff]
         Initmem setup node 0 [mem 0x0000000000000000-0x000000001fffffff]
         percpu: Embedded 11 pages/cpu s14156 r8192 d22708 u45056
         Built 1 zonelists, mobility grouping on.  Total pages: 130048
         Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1
         Dentry cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
         Inode-cache hash table entries: 32768 (order: 5, 131072 bytes, linear)
         mem auto-init: stack:off, heap alloc:off, heap free:off
         Memory: 365992K/524288K available (11264K kernel code, 804K rwdata, 7724K rodata, 1024K init, 457K bss, 27224K reserved, 131072K cma-reserved, 0K highmem)
         rcu: Preemptible hierarchical RCU implementation.
         rcu:    RCU event tracing is enabled.
         rcu:    RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
                 Trampoline variant of Tasks RCU enabled.
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
         random: get_random_bytes called from start_kernel+0x480/0x630 with crng_init=0
         zynq_clock_init: clkc starts at (ptrval)
         Zynq clock init
         sched_clock: 64 bits at 166MHz, resolution 6ns, wraps every 4398046511103ns
         clocksource: arm_global_timer: mask: 0xffffffffffffffff max_cycles: 0x26703d7dd8, max_idle_ns: 440795208065 ns
         Switching to timer-based delay loop, resolution 6ns
         clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 537538477 ns
         timer #0 at (ptrval), irq=25
         Console: colour dummy device 80x30
         Calibrating delay loop (skipped), value calculated using timer frequency.. 333.33 BogoMIPS (lpj=1666666)
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
         SMP: Total of 2 processors activated (666.66 BogoMIPS).
         CPU: All CPU(s) started in SVC mode.
         devtmpfs: initialized
         VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
         clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
         futex hash table entries: 512 (order: 3, 32768 bytes, linear)
         pinctrl core: initialized pinctrl subsystem
         NET: Registered PF_NETLINK/PF_ROUTE protocol family
         DMA: preallocated 256 KiB pool for atomic coherent allocations
         thermal_sys: Registered thermal governor 'step_wise'
         amba f8801000.etb: Fixing up cyclic dependency with replicator
         amba f8803000.tpiu: Fixing up cyclic dependency with replicator
         amba f8804000.funnel: Fixing up cyclic dependency with replicator
         amba f889c000.ptm: Fixing up cyclic dependency with f8804000.funnel
         amba f889d000.ptm: Fixing up cyclic dependency with f8804000.funnel
         hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
         hw-breakpoint: maximum watchpoint size is 4 bytes.
         e0001000.serial: ttyPS0 at MMIO 0xe0001000 (irq = 32, base_baud = 6249999) is a xuartps
         printk: console [ttyPS0] enabled
         SCSI subsystem initialized
         usbcore: registered new interface driver usbfs
         usbcore: registered new interface driver hub
         usbcore: registered new device driver usb
         mc: Linux media interface: v0.10
         videodev: Linux video capture interface: v2.00
         pps_core: LinuxPPS API ver. 1 registered
         pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
         PTP clock support registered
         jesd204: found 0 devices and 0 topologies
         FPGA manager framework
         Advanced Linux Sound Architecture Driver Initialized.
         clocksource: Switched to clocksource arm_global_timer
         NET: Registered PF_INET protocol family
         IP idents hash table entries: 8192 (order: 4, 65536 bytes, linear)
         tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
         TCP established hash table entries: 4096 (order: 2, 16384 bytes, linear)
         TCP bind hash table entries: 4096 (order: 3, 32768 bytes, linear)
         TCP: Hash tables configured (established 4096 bind 4096)
         UDP hash table entries: 256 (order: 1, 8192 bytes, linear)
         UDP-Lite hash table entries: 256 (order: 1, 8192 bytes, linear)
         NET: Registered PF_UNIX/PF_LOCAL protocol family
         RPC: Registered named UNIX socket transport module.
         RPC: Registered udp transport module.
         RPC: Registered tcp transport module.
         RPC: Registered tcp NFSv4.1 backchannel transport module.
         armv7-pmu f8891000.pmu: hw perfevents: no interrupt-affinity property, guessing.
         hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
         workingset: timestamp_bits=30 max_order=17 bucket_order=0
         NFS: Registering the id_resolver key type
         Key type id_resolver registered
         Key type id_legacy registered
         nfs4filelayout_init: NFSv4 File Layout Driver Registering...
         nfs4flexfilelayout_init: NFSv4 Flexfile Layout Driver Registering...
         fuse: init (API version 7.34)
         io scheduler mq-deadline registered
         io scheduler kyber registered
         zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
         dma-pl330 f8003000.dmac: Loaded driver for PL330 DMAC-241330
         dma-pl330 f8003000.dmac:        DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Events-16
         brd: module loaded
         loop: module loaded
         Registered mathworks_ip class
         mwipcore 43c00000.mwipcore: IRQ index 0 not found
         mwipcore 43c00000.mwipcore: Dev memory resource found at (ptrval) 0000FFFF.
         mwipcore 43c00000.mwipcore: 'mwipcore' device not found, creating
         mwipcore 43c00000.mwipcore: Char dev region registered: major num:245
         mwipcore 43c00000.mwipcore: 'mwipcore' device created
         spi-nor spi1.0: SPI-NOR-UniqueID 104473e269910004f3ff360019048cc554
         spi-nor spi1.0: found n25q256ax1, expected n25q256a
         spi-nor spi1.0: n25q256ax1 (32768 Kbytes)
         6 fixed-partitions partitions found on MTD device spi1.0
         Creating 6 MTD partitions on "spi1.0":
         0x000000000000-0x0000000e0000 : "qspi-fsbl-uboot"
         0x0000000e0000-0x000000100000 : "qspi-uboot-env"
         0x000000100000-0x000000600000 : "qspi-linux"
         0x000000600000-0x000000620000 : "qspi-device-tree"
         0x000000620000-0x000001300000 : "qspi-rootfs"
         0x000001300000-0x000002000000 : "qspi-bitstream"
         MACsec IEEE 802.1AE
         libphy: Fixed MDIO Bus: probed
         tun: Universal TUN/TAP device driver, 1.6
         libphy: MACB_mii_bus: probed
         macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 35 (00:0a:35:02:ca:02)
         macb e000c000.ethernet: invalid hw address, using random
         libphy: MACB_mii_bus: probed
         macb e000c000.ethernet eth1: Cadence GEM rev 0x00020118 at 0xe000c000 irq 36 (0e:b8:8c:67:a4:a7)
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
         ULPI transceiver vendor/product ID 0x0424/0x0007
         Found SMSC USB3320 ULPI transceiver.
         ULPI integrity check: passed.
         ci_hdrc ci_hdrc.0: EHCI Host Controller
         ci_hdrc ci_hdrc.0: new USB bus registered, assigned bus number 1
         ci_hdrc ci_hdrc.0: USB 2.0 started, EHCI 1.00
         usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.15
         usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
         usb usb1: Product: EHCI Host Controller
         usb usb1: Manufacturer: Linux 5.15.0-175730-gcdaccc1f2334 ehci_hcd
         usb usb1: SerialNumber: ci_hdrc.0
         hub 1-0:1.0: USB hub found
         hub 1-0:1.0: 1 port detected
         i2c_dev: i2c /dev entries driver
         i2c i2c-0: Added multiplexed i2c bus 1
         i2c i2c-0: Added multiplexed i2c bus 2
         i2c 3-0039: Fixing up cyclic dependency with 70e00000.axi_hdmi
         adv7511 3-0039: supply avdd not found, using dummy regulator
         adv7511 3-0039: supply dvdd not found, using dummy regulator
         adv7511 3-0039: supply pvdd not found, using dummy regulator
         adv7511 3-0039: supply bgvdd not found, using dummy regulator
         adv7511 3-0039: supply dvdd-3v not found, using dummy regulator
         i2c i2c-0: Added multiplexed i2c bus 3
         i2c i2c-0: Added multiplexed i2c bus 4
         i2c i2c-0: Added multiplexed i2c bus 5
         at24 6-0050: supply vcc not found, using dummy regulator
         at24 6-0050: 4096 byte 24c32 EEPROM, writable, 1 bytes/write
         i2c i2c-0: Added multiplexed i2c bus 6
         i2c i2c-0: Added multiplexed i2c bus 7
         i2c i2c-0: Added multiplexed i2c bus 8
         pca954x 0-0070: registered 8 multiplexed busses for I2C switch pca9548
         usbcore: registered new interface driver uvcvideo
         gspca_main: v2.14.0 registered
         cdns-wdt f8005000.watchdog: Xilinx Watchdog Timer with timeout 10s
         Xilinx Zynq CpuIdle Driver started
         failed to register cpuidle driver
         sdhci: Secure Digital Host Controller Interface driver
         sdhci: Copyright(c) Pierre Ossman
         sdhci-pltfm: SDHCI platform and OF driver helper
         ledtrig-cpu: registered to indicate activity on CPUs
         hid: raw HID events driver (C) Jiri Kosina
         usbcore: registered new interface driver usbhid
         usbhid: USB HID core driver
         ad9361 spi0.0: ad9361_probe : enter (ad9361)
         mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
         ad9361 spi0.0: No GPIOs defined for ext band ctrl
         random: fast init done
         mmc0: new high speed SDHC card at address aaaa
         mmcblk0: mmc0:aaaa SP32G 29.7 GiB
          mmcblk0: p1 p2 p3
         ad9361 spi0.0: ad9361_probe : AD936x Rev 0 successfully initialized
         ad9517 spi0.1: AD9517 successfully initialized
         cf_axi_dds 79024000.cf-ad9361-dds-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x79024000 mapped to 0x(ptrval), probed DDS AD9361
         axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
         axi_sysid 45000000.axi-sysid-0: [adrv9361z7035_ccfmc] on [lvds] git branch <master> git <d152ad1e9d6ab2f97167b76f9b9837748f385cdf> clean [2023-04-20 22:57:03] UTC
         fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
         usbcore: registered new interface driver snd-usb-audio
         axi-i2s 77600000.axi-i2s: probed, capture enabled, playback enabled
         NET: Registered PF_INET6 protocol family
         Segment Routing with IPv6
         In-situ OAM (IOAM) with IPv6
         sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
         NET: Registered PF_PACKET protocol family
         NET: Registered PF_IEEE802154 protocol family
         Key type dns_resolver registered
         zynq_pm_remap_ocm: OCM pool is not available
         zynq_pm_suspend_init: Unable to map OCM.
         Registering SWP/SWPB emulation handler
         of-fpga-region fpga-full: FPGA Region probed
         [drm] Initialized axi_hdmi_drm 1.0.0 20120930 for 70e00000.axi_hdmi on minor 0
         axi-hdmi 70e00000.axi_hdmi: [drm] Cannot find any crtc or sizes
         cf_axi_adc 79020000.cf-ad9361-lpc: ADI AIM (10.03.) at 0x79020000 mapped to 0x(ptrval) probed ADC AD9361 as MASTER
         debugfs: File 'Capture' in directory 'dapm' already present!
         input: gpio_keys as /devices/soc0/gpio_keys/input/input0
         of_cfs_init
         of_cfs_init: OK
         clk: Not disabling unused clocks
         ALSA device list:
           #0: HDMI monitor
           #1: ZED ADAU1761
         EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null). Quota mode: disabled.
         VFS: Mounted root (ext4 filesystem) on device 179:2.
         devtmpfs: mounted
         Freeing unused kernel image (initmem) memory: 1024K
         Run /sbin/init as init process
         systemd[1]: System time before build time, advancing clock.
         systemd[1]: systemd 247.3-7+rpi1+deb11u1 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
         systemd[1]: Detected architecture arm.

         Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

         systemd[1]: Set hostname to <analog>.
         systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
         systemd[1]: Queued start job for default target Graphical Interface.
         random: systemd: uninitialized urandom read (16 bytes read)
         systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
         systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
         systemd[1]: Created slice system-getty.slice.
         [  OK  ] Created slice system-getty.slice.
         random: systemd: uninitialized urandom read (16 bytes read)
         systemd[1]: Created slice system-modprobe.slice.
         [  OK  ] Created slice system-modprobe.slice.
         random: systemd: uninitialized urandom read (16 bytes read)
         systemd[1]: Created slice system-serial\x2dgetty.slice.
         [  OK  ] Created slice system-serial\x2dgetty.slice.
         systemd[1]: Created slice system-systemd\x2dfsck.slice.
         [  OK  ] Created slice system-systemd\x2dfsck.slice.
         systemd[1]: Created slice User and Session Slice.
         [  OK  ] Created slice User and Session Slice.
         systemd[1]: Started Forward Password Requests to Wall Directory Watch.
         [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
         systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
         systemd[1]: Reached target Slices.
         [  OK  ] Reached target Slices.
         systemd[1]: Reached target Swap.
         [  OK  ] Reached target Swap.
         systemd[1]: Listening on Syslog Socket.
         [  OK  ] Listening on Syslog Socket.
         systemd[1]: Listening on fsck to fsckd communication Socket.
         [  OK  ] Listening on fsck to fsckd communication Socket.
         systemd[1]: Listening on initctl Compatibility Named Pipe.
         [  OK  ] Listening on initctl Compatibility Named Pipe.
         systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
         systemd[1]: Listening on Journal Socket (/dev/log).
         [  OK  ] Listening on Journal Socket (/dev/log).
         systemd[1]: Listening on Journal Socket.
         [  OK  ] Listening on Journal Socket.
         systemd[1]: Listening on udev Control Socket.
         [  OK  ] Listening on udev Control Socket.
         systemd[1]: Listening on udev Kernel Socket.
         [  OK  ] Listening on udev Kernel Socket.
         systemd[1]: Condition check resulted in Huge Pages File System being skipped.
         systemd[1]: Condition check resulted in POSIX Message Queue File System being skipped.
         systemd[1]: Mounting RPC Pipe File System...
                  Mounting RPC Pipe File System...
         systemd[1]: Mounting Kernel Debug File System...
                  Mounting Kernel Debug File System...
         systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
         systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
         systemd[1]: Starting Restore / save the current clock...
                  Starting Restore / save the current clock...
         systemd[1]: Starting Set the console keyboard layout...
                  Starting Set the console keyboard layout...
         systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
         systemd[1]: Starting Load Kernel Module configfs...
                  Starting Load Kernel Module configfs...
         systemd[1]: Starting Load Kernel Module drm...
                  Starting Load Kernel Module drm...
         systemd[1]: Starting Load Kernel Module fuse...
                  Starting Load Kernel Module fuse...
         systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
         systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
         systemd[1]: Starting Journal Service...
                  Starting Journal Service...
         systemd[1]: Starting Load Kernel Modules...
                  Starting Load Kernel Modules...
         systemd[1]: Starting Remount Root and Kernel File Systems...
                  Starting Remount Root and Kernel File Systems...
         systemd[1]: Starting Coldplug All udev Devices...
                  Starting Coldplug All udev Devices...
         systemd[1]: Mounted RPC Pipe File System.
         [  OK  ] Mounted RPC Pipe File System.
         systemd[1]: Mounted Kernel Debug File System.
         [  OK  ] Mounted Kernel Debug File System.
         systemd[1]: Finished Restore / save the current clock.
         [  OK  ] Finished Restore / save the current clock.
         systemd[1]: modprobe@configfs.service: Succeeded.
         systemd[1]: Finished Load Kernel Module configfs.
         [  OK  ] Finished Load Kernel Module configfs.
         systemd[1]: modprobe@drm.service: Succeeded.
         systemd[1]: Finished Load Kernel Module drm.
         [  OK  ] Finished Load Kernel Module drm.
         random: crng init done
         random: 7 urandom warning(s) missed due to ratelimiting
         systemd[1]: modprobe@fuse.service: Succeeded.
         systemd[1]: Finished Load Kernel Module fuse.
         [  OK  ] Finished Load Kernel Module fuse.
         systemd[1]: systemd-modules-load.service: Main process exited, code=exited, status=1/FAILURE
         systemd[1]: systemd-modules-load.service: Failed with result 'exit-code'.
         systemd[1]: Failed to start Load Kernel Modules.
         [FAILED] Failed to start Load Kernel Modules.
         See 'systemctl status systemd-modules-load.service' for details.
         systemd[1]: Started Journal Service.
         [  OK  ] Started Journal Service.
                  Mounting FUSE Control File System...
                  Mounting Kernel Configuration File System...
                  Starting Apply Kernel Variables...
         [  OK  ] Mounted FUSE Control File System.
         [  OK  ] Mounted Kernel Configuration File System.
         EXT4-fs (mmcblk0p2): re-mounted. Opts: (null). Quota mode: disabled.
         [  OK  ] Finished Remount Root and Kernel File Systems.
         [  OK  ] Finished Set the console keyboard layout.
         [  OK  ] Finished Apply Kernel Variables.
                  Starting Flush Journal to Persistent Storage...
                  Starting Load/Save Random Seed...
                  Starting Create System Users...
         [  OK  ] Finished Load/Save Random Seed.
         [  OK  ] Finished Create System Users.
                  Starting Create Static Device Nodes in /dev...
         [  OK  ] Finished Coldplug All udev Devices.
                  Starting Helper to synchronize boot up for ifupdown...
                  Starting Wait for udev To …plete Device Initialization...
         [  OK  ] Finished Helper to synchronize boot up for ifupdown.
         [  OK  ] Finished Create Static Device Nodes in /dev.
         [  OK  ] Reached target Local File Systems (Pre).
                  Starting Rule-based Manage…for Device Events and Files...
         [  OK  ] Finished Flush Journal to Persistent Storage.
         [  OK  ] Started Rule-based Manager for Device Events and Files.
                  Starting Show Plymouth Boot Screen...
         [  OK  ] Started Show Plymouth Boot Screen.
         [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
         [  OK  ] Reached target Local Encrypted Volumes.
         [  OK  ] Found device /dev/ttyPS0.
         [  OK  ] Found device /dev/disk/by-partuuid/9785213e-01.
         [  OK  ] Finished Wait for udev To Complete Device Initialization.
                  Starting File System Check…isk/by-partuuid/9785213e-01...
                  Starting Load Kernel Modules...
         [  OK  ] Started File System Check Daemon to report status.
         [FAILED] Failed to start Load Kernel Modules.
         See 'systemctl status systemd-modules-load.service' for details.
         [  OK  ] Finished File System Check…/disk/by-partuuid/9785213e-01.
                  Mounting /boot...
         [  OK  ] Mounted /boot.
         [  OK  ] Reached target Local File Systems.
                  Starting Set console font and keymap...
                  Starting Raise network interfaces...
                  Starting Preprocess NFS configuration...
                  Starting Tell Plymouth To Write Out Runtime Data...
                  Starting Create Volatile Files and Directories...
         [  OK  ] Finished Set console font and keymap.
         [  OK  ] Finished Preprocess NFS configuration.
         [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
         [  OK  ] Reached target NFS client services.
         [  OK  ] Reached target Remote File Systems (Pre).
         [  OK  ] Reached target Remote File Systems.
         [  OK  ] Finished Create Volatile Files and Directories.
                  Starting Update UTMP about System Boot/Shutdown...
         [  OK  ] Finished Update UTMP about System Boot/Shutdown.
         [  OK  ] Reached target System Initialization.
         [  OK  ] Started CUPS Scheduler.
         [  OK  ] Started Daily apt download activities.
         [  OK  ] Started Daily apt upgrade and clean activities.
         [  OK  ] Started Periodic ext4 Onli…ata Check for All Filesystems.
         [  OK  ] Started Discard unused blocks once a week.
         [  OK  ] Started Daily rotation of log files.
         [  OK  ] Started Daily man-db regeneration.
         [  OK  ] Started Daily Cleanup of Temporary Directories.
         [  OK  ] Reached target Paths.
         [  OK  ] Reached target Timers.
         [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
         [  OK  ] Listening on CUPS Scheduler.
         [  OK  ] Listening on D-Bus System Message Bus Socket.
         [  OK  ] Listening on Erlang Port Mapper Daemon Activation Socket.
         [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
         [  OK  ] Listening on triggerhappy.socket.
         [  OK  ] Reached target Sockets.
         [  OK  ] Reached target Basic System.
                  Starting Analog Devices power up/down sequence...
                  Starting Save/Restore Sound Card State...
                  Starting Avahi mDNS/DNS-SD Stack...
         [  OK  ] Started Regular background program processing daemon.
         [  OK  ] Started D-Bus System Message Bus.
                  Starting dphys-swapfile - …unt, and delete a swap file...
                  Starting Remove Stale Onli…t4 Metadata Check Snapshots...
                  Starting Creating IIOD Context Attributes......
                  Starting Authorization Manager...
                  Starting DHCP Client Daemon...
                  Starting LSB: Switch to on…nless shift key is pressed)...
                  Starting LSB: rng-tools (Debian variant)...
                  Starting System Logging Service...
                  Starting User Login Management...
                  Starting triggerhappy global hotkey daemon...
                  Starting Disk Manager...
                  Starting WPA supplicant...
         [  OK  ] Finished Save/Restore Sound Card State.
         [  OK  ] Started triggerhappy global hotkey daemon.
         [  OK  ] Started System Logging Service.
         [  OK  ] Finished Raise network interfaces.
         [  OK  ] Started Avahi mDNS/DNS-SD Stack.
         [  OK  ] Started LSB: rng-tools (Debian variant).
         [  OK  ] Started DHCP Client Daemon.
         [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
         [  OK  ] Started Authorization Manager.
         [  OK  ] Started WPA supplicant.
         [  OK  ] Reached target Sound Card.
                  Starting Modem Manager...
         [  OK  ] Reached target Network.
         [  OK  ] Reached target Network is Online.
                  Starting CUPS Scheduler...
         [  OK  ] Started Erlang Port Mapper Daemon.
                  Starting HTTP based time synchronization tool...
                  Starting Internet superserver...
                  Starting /etc/rc.local Compatibility...
                  Starting OpenBSD Secure Shell server...
                  Starting Permit User Sessions...
         [  OK  ] Started /etc/rc.local Compatibility.
         [  OK  ] Started Internet superserver.
         [  OK  ] Started User Login Management.
         [  OK  ] Started Unattended Upgrades Shutdown.
         [  OK  ] Finished Permit User Sessions.
                  Starting Light Display Manager...
                  Starting Hold until boot process finishes up...
         [  OK  ] Started HTTP based time synchronization tool.
         [  OK  ] Started CUPS Scheduler.
         [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
         [  OK  ] Started Make remote CUPS printers available locally.
         [  OK  ] Started Modem Manager.
         [FAILED] Failed to start VNC Server for X11.

         Raspbian GNU/Linux 11 analog ttyPS0

         analog login: root (automatic login)

         Linux analog 5.15.0-175730-gcdaccc1f2334 #3276 SMP PREEMPT Fri Apr 21 06:46:11 IST 2023 armv7l

         The programs included with the Debian GNU/Linux system are free software;
         the exact distribution terms for each program are described in the
         individual files in /usr/share/doc/*/copyright.

         Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
         permitted by applicable law.
         Last login: Mon Apr 24 04:41:06 BST 2023 on ttyPS0
         root@analog:~#

Login Information

- user: analog
- password: analog

Show hardware sysid:

.. container:: box bggreen

   This specifies any shell prompt running on the target

   ::

      root@analog:~# dmesg | grep sysid
      [    1.595804] axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
      [    1.602488] axi_sysid 45000000.axi-sysid-0: [adrv9361z7035_ccfmc] on [lvds] git branch <master> git <d152ad1e9d6ab2f97167b76f9b9837748f385cdf> clean [2023-04-20 22:57:03] UTC

This command display or list all the errors from logs:

.. container:: box bggreen

   This specifies any shell prompt running on the target

   ::

      root@analog:~# dmesg -l err

These devices should be present:

.. container:: box bggreen

   This specifies any shell prompt running on the target

   ::

      root@analog:~# iio_info | grep iio:device
              iio:device0: ad7291
              iio:device1: ad9361-phy
              iio:device2: xadc
              iio:device3: ad9517-3
              iio:device4: cf-ad9361-dds-core-lpc (buffer capable)
              iio:device5: cf-ad9361-lpc (buffer capable)

IIO Oscilloscope Remote
-----------------------

Please see also here: :ref:`Oscilloscope <iio-oscilloscope>`

The IIO Oscilloscope application can be used locally on Transceiver/Radio
Boards. It has a feature of a graphical desktop environment remote using a
network connection.

When using the remote option, once you logged in to the Linux terminal you need
to check the IP address of the using the **ifconfig** command to see if there
was any address assigned by a DHCP server. If not, you need to manually set an
address with ifconfig in the same address space your PC is using.

Getting of IP address:

.. container:: box bggreen

   This specifies any shell prompt running on the target

   ::

      root@analog:~# ifconfig
      eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
              inet 192.168.10.110  netmask 255.255.255.0  broadcast 192.168.10.255
              inet6 fe80::20a:35ff:fe02:ca02  prefixlen 64  scopeid 0x20<link>
              ether 00:0a:35:02:ca:02  txqueuelen 1000  (Ethernet)
              RX packets 20758  bytes 1355088 (1.2 MiB)
              RX errors 0  dropped 0  overruns 0  frame 0
              TX packets 22518  bytes 16552750 (15.7 MiB)
              TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
              device interrupt 35  base 0xb000

      eth1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
              ether 4e:84:60:5e:ad:d4  txqueuelen 1000  (Ethernet)
              RX packets 0  bytes 0 (0.0 B)
              RX errors 0  dropped 0  overruns 0  frame 0
              TX packets 0  bytes 0 (0.0 B)
              TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
              device interrupt 36  base 0xc000

      lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
              inet 127.0.0.1  netmask 255.0.0.0
              inet6 ::1  prefixlen 128  scopeid 0x10<host>
              loop  txqueuelen 1000  (Local Loopback)
              RX packets 75156  bytes 49190154 (46.9 MiB)
              RX errors 0  dropped 0  overruns 0  frame 0
              TX packets 75156  bytes 49190154 (46.9 MiB)

Once the IIO Osc application is launched goto Settings -> Connect and enter the
IP address of the target in the popup window.

|osc_config.png|

IIO OSC ADRV9361-Z7035-FMC Capture Window
=========================================

The AD9361 is a high performance, highly integrated RF Agile Transceiver™. Its
programmability and wideband capability make it ideal for a broad range of
transceiver applications. The device combines an RF front end with a flexible
mixed-signal baseband section and integrated frequency synthesizers, simplifying
design-in by providing a configurable digital interface to a processor.

SDR module or board that contains the necessary RF (Radio Frequency) components
and signal processing circuitry. FMC carrier is a hardware platform that can
host an FMC card and provide access to its I/O interfaces and resources.

Screenshots
-----------

Time Domain View
~~~~~~~~~~~~~~~~

.. image:: images/osc_timedomain.png
   :alt: osc_timedomain.png
   :width: 500

Frequency Domain View
~~~~~~~~~~~~~~~~~~~~~

.. image:: images/osc_frequencydomain.png
   :alt: osc_frequencydomain.png
   :width: 500

Plugins
-------

These plugins enhance the capabilities of the IIO Oscilloscope tool and enable
users to visualize and analyze the data from the ADRV9361 module in different
ways. These provide a convenient and easy-to-use interface for configuring and
controlling the module and performing various signal processing functions.
ADRV9361 plugins:(formerly known as the FMComms2/3/4 Plugin):

- :ref:`ADRV936X Plugins <fmcomms2 software ad9361-plugin>`
- :ref:`ADRV936X Advanced Plugins <fmcomms2 software ad9361-advanced-plugin>`

Shut down
---------

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be
   taken not to corrupt the file system -- please shut down things, don't just
   turn off the power switch. Depending on your monitor, the standard power off
   could be hiding. You can do this from the terminal as well with ``sudo
   shutdown -h now``

   |image1|

.. |adrv1crr-fmc-image| image:: images/adrv1crr-fmc-angle-web.png
   :width: 250

.. |adrv1crr-bob-image| image:: images/adrv1crr-bob-top-web.png
   :width: 250

.. |osc_config.png| image:: images/osc_config.png
   :width: 600

.. |image1| image:: images/shutdown.png
   :width: 300
