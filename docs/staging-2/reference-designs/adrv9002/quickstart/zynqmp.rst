.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9002/quickstart/zynqmp

.. _adrv9002 quickstart zynqmp:

ADRV9002 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide
========================================================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9002/adrv9002_zcu102_quickstart.png.png
   :width: 600px

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` and
:adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` on:

- :xilinx:`ZCU102 <ZCU102>` The revision that is supported is 1.0 only. Previous
  versions will not work.

Instructions on how to build the ZynqMP / MPSoC Linux kernel and devicetrees
from source can be found here:

- :dokuwiki:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </resources/tools-software/linux-build/generic/zynqmp>`
- :dokuwiki:`How to build the ZynqMP boot image BOOT.BIN </resources/tools-software/linux-software/build-the-zynqmp-boot-image>`

Required Software
-----------------

- SD Card 16GB imaged using the instructions here:
  :dokuwiki:`Zynq & Altera SoC Quick Start Guide </resources/tools-software/linux-software/zynq_images>`.
  Use the 22 June 2020 release (2019_R1) or later.
- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Required Hardware
-----------------

- Xilinx :xilinx:`ZCU102 <ZCU102>` Rev 1.0 or later board
- :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` FMC board.
- Reference clock source
- Micro-USB cable
- Ethernet cable
- Optionally USB keyboard mouse and a Display Port compatible monitor

.. todo:: .. include: /resources/eval/user-guides/adrv9002/quickstart.rst

   :start-after: .. start-#identify-your-hardware
   :end-before: .. end-#identify-your-hardware

Testing
-------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/quickstart/zcu102.jpg
   :width: 900px

- Connect the :adi:`ADRV9002NP/W1/PCBZ <EVAL-ADRV9002>` or
  :adi:`ADRV9002NP/W2/PCBZ <EVAL-ADRV9002>` FMC board to the FPGA carrier HPC0
  FMC0 socket.
- On the FMC card set switch to select clock source between:

  - an on-board 38.4MHz VCTCXO (default)
  - external (thru J501) 10MHz to 1000MHz / +13dBm

- Connect USB UART J83 (Micro USB) to your host PC.
- Insert SD card into socket.
- Configure ZCU102 for SD BOOT (mode SW6[4:1] switch in the position
  OFF,OFF,OFF,ON as seen in the below picture).
- Turn on the power switch on the FPGA board.
- Observe kernel and serial console messages on your terminal. (use the first
  ttyUSB or COM port registered)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/quickstart/zcu102_1p0_bootmode.jpg
   :width: 400px

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

SDcard boot files
~~~~~~~~~~~~~~~~~

The files that need to be present on the sdcard ``BOOT`` partition are:

- ``BOOT.bin``
- ``Image``
- ``system.dtb``

Copy these from the ``zynqmp-zcu102-rev10-adrv9002`` directory.

Messages
~~~~~~~~

<hidden Complete kernel boot log (Click to expand)> ::

   Xilinx Zynq MP First Stage Boot Loader
   Release 2019.1   Feb 19 2021  -  21:11:12
   NOTICE:  ATF running on XCZU9EG/silicon v4/RTL5.1 at 0xfffea000
   NOTICE:  BL31: Secure code at 0x0
   NOTICE:  BL31: Non secure code at 0x8000000
   NOTICE:  BL31: v2.0(release):xilinx-v2019.2
   NOTICE:  BL31: Built : 10:19:24, Jan 13 2020
   PMUFW:  v1.1

   U-Boot 2018.01-21436-gbba91bc203 (Jan 13 2020 - 10:50:58 +0200) Xilinx ZynqMP ZCU102 rev1.0, Build: jenkins-development-build_uboot-1

   I2C:   ready
   DRAM:  4 GiB
   EL Level:       EL2
   Chip ID:        zu9eg
   MMC:   sdhci@ff170000: 0 (SD)
   *** Warning - bad CRC, using default environment

   In:    serial@ff000000
   Out:   serial@ff000000
   Err:   serial@ff000000
   Bootmode: LVL_SHFT_SD_MODE1
   Net:   ZYNQ GEM: ff0e0000, phyaddr c, interface rgmii-id

   Warning: ethernet@ff0e0000 (eth0) using random MAC address - 0a:b9:b6:be:9e:f0
   eth0: ethernet@ff0e0000
   Hit any key to stop autoboot:  0
   switch to partitions #0, OK
   mmc0 is current device
   Device: sdhci@ff170000
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
   407 bytes read in 16 ms (24.4 KiB/s)
   Loaded environment from uEnv.txt
   Importing environment from SD ...
   Running uenvcmd ...
   Copying Linux from SD to RAM...
   **No boot file defined**
   reading system.dtb
   43253 bytes read in 25 ms (1.6 MiB/s)
   reading Image
   29737472 bytes read in 1978 ms (14.3 MiB/s)
   ## Flattened Device Tree blob at 04000000
      Booting using the fdt blob at 0x4000000
      Loading Device Tree to 000000000fff2000, end 000000000ffff8f4 ... OK

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
   [    0.000000] Linux version 4.19.0-ga6ef26d (jenkins@romlxbuild1.adlk.analog.com) (gcc version 8.2.0 (GCC)) #1105 SMP Fri Feb 19 16:51:27 GMT 2021
   [    0.000000] Machine model: ZynqMP ZCU102 Rev1.0
   [    0.000000] earlycon: cdns0 at MMIO 0x00000000ff000000 (options '115200n8')
   [    0.000000] bootconsole [cdns0] enabled
   [    0.000000] efi: Getting EFI parameters from FDT:
   [    0.000000] efi: UEFI not found.
   [    0.000000] cma: Reserved 256 MiB at 0x0000000070000000
   [    0.000000] psci: probing for conduit method from DT.
   [    0.000000] psci: PSCIv1.1 detected in firmware.
   [    0.000000] psci: Using standard PSCI v0.2 function IDs
   [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
   [    0.000000] psci: SMC Calling Convention v1.1
   [    0.000000] random: get_random_bytes called from start_kernel+0x94/0x3f8 with crng_init=0
   [    0.000000] percpu: Embedded 22 pages/cpu @(____ptrval____) s52504 r8192 d29416 u90112
   [    0.000000] Detected VIPT I-cache on CPU0
   [    0.000000] CPU features: enabling workaround for ARM erratum 845719
   [    0.000000] Speculative Store Bypass Disable mitigation not required
   [    0.000000] CPU features: detected: Kernel page table isolation (KPTI)
   [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1034240
   [    0.000000] Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1 root=/dev/mmcblk0p2 rw rootwait
   [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes)
   [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes)
   [    0.000000] software IO TLB: mapped [mem 0x6bfff000-0x6ffff000] (64MB)
   [    0.000000] Memory: 3772376K/4194304K available (12796K kernel code, 1520K rwdata, 13828K rodata, 832K init, 326K bss, 159784K reserved, 262144K cma-reserved)
   [    0.000000] rcu: Hierarchical RCU implementation.
   [    0.000000] rcu:     RCU event tracing is enabled.
   [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
   [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
   [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
   [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
   [    0.000000] GIC: Using split EOI/Deactivate mode
   [    0.000000] arch_timer: cp15 timer(s) running at 99.99MHz (phys).
   [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x170f8de2d3, max_idle_ns: 440795206112 ns
   [    0.000003] sched_clock: 56 bits at 99MHz, resolution 10ns, wraps every 4398046511101ns
   [    0.008247] Console: colour dummy device 80x25
   [    0.012391] Calibrating delay loop (skipped), value calculated using timer frequency.. 199.98 BogoMIPS (lpj=399960)
   [    0.022757] pid_max: default: 32768 minimum: 301
   [    0.027449] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes)
   [    0.034012] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes)
   [    0.041769] ASID allocator initialised with 32768 entries
   [    0.046510] rcu: Hierarchical SRCU implementation.
   [    0.051540] EFI services will not be available.
   [    0.055826] smp: Bringing up secondary CPUs ...
   [    0.060482] Detected VIPT I-cache on CPU1
   [    0.060511] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
   [    0.060812] Detected VIPT I-cache on CPU2
   [    0.060831] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
   [    0.061113] Detected VIPT I-cache on CPU3
   [    0.061132] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
   [    0.061176] smp: Brought up 1 node, 4 CPUs
   [    0.095681] SMP: Total of 4 processors activated.
   [    0.100355] CPU features: detected: 32-bit EL0 Support
   [    0.106854] CPU: All CPU(s) started at EL2
   [    0.109534] alternatives: patching kernel code
   [    0.114823] devtmpfs: initialized
   [    0.122439] Registered cp15_barrier emulation handler
   [    0.122486] Registered setend emulation handler
   [    0.126850] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
   [    0.136436] futex hash table entries: 1024 (order: 4, 65536 bytes)
   [    0.148024] xor: measuring software checksum speed
   [    0.186637]    8regs     :  2375.000 MB/sec
   [    0.226664]    8regs_prefetch:  2051.000 MB/sec
   [    0.266695]    32regs    :  2724.000 MB/sec
   [    0.306724]    32regs_prefetch:  2308.000 MB/sec
   [    0.306765] xor: using function: 32regs (2724.000 MB/sec)
   [    0.311069] pinctrl core: initialized pinctrl subsystem
   [    0.316826] NET: Registered protocol family 16
   [    0.321061] audit: initializing netlink subsys (disabled)
   [    0.326088] audit: type=2000 audit(0.272:1): state=initialized audit_enabled=0 res=1
   [    0.333729] vdso: 2 pages (1 code @ (____ptrval____), 1 data @ (____ptrval____))
   [    0.333733] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
   [    0.348477] DMA: preallocated 256 KiB pool for atomic allocations
   [    0.367373] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
   [    0.436466] raid6: int64x1  gen()   445 MB/s
   [    0.504466] raid6: int64x1  xor()   451 MB/s
   [    0.572495] raid6: int64x2  gen()   679 MB/s
   [    0.640509] raid6: int64x2  xor()   599 MB/s
   [    0.708566] raid6: int64x4  gen()   980 MB/s
   [    0.776627] raid6: int64x4  xor()   737 MB/s
   [    0.844663] raid6: int64x8  gen()  1162 MB/s
   [    0.912718] raid6: int64x8  xor()   759 MB/s
   [    0.980776] raid6: neonx1   gen()   736 MB/s
   [    1.048778] raid6: neonx1   xor()   880 MB/s
   [    1.116836] raid6: neonx2   gen()  1129 MB/s
   [    1.184875] raid6: neonx2   xor()  1173 MB/s
   [    1.252923] raid6: neonx4   gen()  1478 MB/s
   [    1.320965] raid6: neonx4   xor()  1418 MB/s
   [    1.389010] raid6: neonx8   gen()  1552 MB/s
   [    1.457057] raid6: neonx8   xor()  1459 MB/s
   [    1.457095] raid6: using algorithm neonx8 gen() 1552 MB/s
   [    1.461047] raid6: .... xor() 1459 MB/s, rmw enabled
   [    1.465979] raid6: using neon recovery algorithm
   [    1.471270] SCSI subsystem initialized
   [    1.474446] usbcore: registered new interface driver usbfs
   [    1.479765] usbcore: registered new interface driver hub
   [    1.485041] usbcore: registered new device driver usb
   [    1.490190] media: Linux media interface: v0.10
   [    1.494548] videodev: Linux video capture interface: v2.00
   [    1.500023] pps_core: LinuxPPS API ver. 1 registered
   [    1.504908] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
   [    1.514002] PTP clock support registered
   [    1.517899] EDAC MC: Ver: 3.0.0
   [    1.521390] zynqmp-ipi-mbox mailbox@ff990400: Probed ZynqMP IPI Mailbox driver.
   [    1.528652] jesd204: found 0 devices and 0 topologies
   [    1.533319] FPGA manager framework
   [    1.536823] Advanced Linux Sound Architecture Driver Initialized.
   [    1.542980] Bluetooth: Core ver 2.22
   [    1.546271] NET: Registered protocol family 31
   [    1.550672] Bluetooth: HCI device and connection manager initialized
   [    1.556988] Bluetooth: HCI socket layer initialized
   [    1.561832] Bluetooth: L2CAP socket layer initialized
   [    1.566859] Bluetooth: SCO socket layer initialized
   [    1.572180] clocksource: Switched to clocksource arch_sys_counter
   [    1.577835] VFS: Disk quotas dquot_6.6.0
   [    1.581688] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
   [    1.592648] NET: Registered protocol family 2
   [    1.593126] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes)
   [    1.600629] TCP established hash table entries: 32768 (order: 6, 262144 bytes)
   [    1.607968] TCP bind hash table entries: 32768 (order: 7, 524288 bytes)
   [    1.614718] TCP: Hash tables configured (established 32768 bind 32768)
   [    1.620891] UDP hash table entries: 2048 (order: 4, 65536 bytes)
   [    1.626869] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes)
   [    1.633352] NET: Registered protocol family 1
   [    1.637736] RPC: Registered named UNIX socket transport module.
   [    1.643414] RPC: Registered udp transport module.
   [    1.648081] RPC: Registered tcp transport module.
   [    1.652756] RPC: Registered tcp NFSv4.1 backchannel transport module.
   [    1.659887] hw perfevents: no interrupt-affinity property for /pmu, guessing.
   [    1.666390] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
   [    1.674773] Initialise system trusted keyrings
   [    1.678419] workingset: timestamp_bits=62 max_order=20 bucket_order=0
   [    1.685433] NFS: Registering the id_resolver key type
   [    1.689790] Key type id_resolver registered
   [    1.693930] Key type id_legacy registered
   [    1.697914] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
   [    1.704583] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
   [    2.793728] NET: Registered protocol family 38
   [    2.855264] Key type asymmetric registered
   [    2.855302] Asymmetric key parser 'x509' registered
   [    2.858609] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 246)
   [    2.865926] io scheduler noop registered
   [    2.869820] io scheduler deadline registered
   [    2.874074] io scheduler cfq registered (default)
   [    2.878728] io scheduler mq-deadline registered
   [    2.883225] io scheduler kyber registered
   [    2.914847] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
   [    2.918934] cacheinfo: Unable to detect cache hierarchy for CPU 0
   [    2.925775] brd: module loaded
   [    2.929542] loop: module loaded
   [    2.929756] Registered mathworks_ip class
   [    2.932585] mtdoops: mtd device (mtddev=name/number) must be supplied
   [    2.939497] libphy: Fixed MDIO Bus: probed
   [    2.943351] tun: Universal TUN/TAP device driver, 1.6
   [    2.947341] CAN device driver interface
   [    2.951948] usbcore: registered new interface driver asix
   [    2.956437] usbcore: registered new interface driver ax88179_178a
   [    2.962475] usbcore: registered new interface driver cdc_ether
   [    2.968268] usbcore: registered new interface driver net1080
   [    2.973891] usbcore: registered new interface driver cdc_subset
   [    2.979773] usbcore: registered new interface driver zaurus
   [    2.985318] usbcore: registered new interface driver cdc_ncm
   [    2.991589] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
   [    2.997401] ehci-pci: EHCI PCI platform driver
   [    3.002067] usbcore: registered new interface driver uas
   [    3.007119] usbcore: registered new interface driver usb-storage
   [    3.013118] usbcore: registered new interface driver usbserial_generic
   [    3.019566] usbserial: USB Serial support registered for generic
   [    3.025535] usbcore: registered new interface driver ftdi_sio
   [    3.031241] usbserial: USB Serial support registered for FTDI USB Serial Device
   [    3.038511] usbcore: registered new interface driver upd78f0730
   [    3.044390] usbserial: USB Serial support registered for upd78f0730
   [    3.051944] rtc_zynqmp ffa60000.rtc: rtc core: registered ffa60000.rtc as rtc0
   [    3.057847] i2c /dev entries driver
   [    3.063205] usbcore: registered new interface driver uvcvideo
   [    3.066955] USB Video Class driver (1.1.1)
   [    3.072350] Bluetooth: HCI UART driver ver 2.3
   [    3.075426] Bluetooth: HCI UART protocol H4 registered
   [    3.080539] Bluetooth: HCI UART protocol BCSP registered
   [    3.085831] Bluetooth: HCI UART protocol LL registered
   [    3.090915] Bluetooth: HCI UART protocol ATH3K registered
   [    3.096300] Bluetooth: HCI UART protocol Three-wire (H5) registered
   [    3.102548] Bluetooth: HCI UART protocol Intel registered
   [    3.107888] Bluetooth: HCI UART protocol QCA registered
   [    3.113096] usbcore: registered new interface driver bcm203x
   [    3.118711] usbcore: registered new interface driver bpa10x
   [    3.124249] usbcore: registered new interface driver bfusb
   [    3.129697] usbcore: registered new interface driver btusb
   [    3.135121] Bluetooth: Generic Bluetooth SDIO driver ver 0.1
   [    3.140785] usbcore: registered new interface driver ath3k
   [    3.146319] EDAC MC: ECC not enabled
   [    3.149983] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
   [    3.162178] CPUidle arm: Failed to register cpuidle driver
   [    3.167472] sdhci: Secure Digital Host Controller Interface driver
   [    3.173449] sdhci: Copyright(c) Pierre Ossman
   [    3.177769] sdhci-pltfm: SDHCI platform and OF driver helper
   [    3.183770] ledtrig-cpu: registered to indicate activity on CPUs
   [    3.189405] zynqmp_firmware_probe Platform Management API v1.1
   [    3.195160] zynqmp_firmware_probe Trustzone version v1.0
   [    3.203223] zynqmp-pinctrl firmware:zynqmp-firmware:pinctrl: zynqmp pinctrl initialized
   [    3.230667] zynqmp_clk_mux_get_parent() getparent failed for clock: lpd_wdt, ret = -22
   [    3.233364] alg: No test for xilinx-zynqmp-aes (zynqmp-aes)
   [    3.238490] zynqmp_aes zynqmp_aes: AES Successfully Registered
   [    3.238490]
   [    3.246004] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
   [    3.252133] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
   [    3.257710] usbcore: registered new interface driver usbhid
   [    3.263045] usbhid: USB HID core driver
   [    3.273657] axi_sysid 85000000.axi-sysid-0: [adrv9001] [CMOS_LVDS_N=1] on [zcu102] git <061d024d596ef84c6a819854bf2472e6b43a2d5d> clean [2021-02-19 20:33:16] UTC
   [    3.282751] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
   [    3.289316] usbcore: registered new interface driver snd-usb-audio
   [    3.296741] pktgen: Packet Generator for packet performance testing. Version: 2.75
   [    3.302850] Initializing XFRM netlink socket
   [    3.306795] NET: Registered protocol family 10
   [    3.311502] Segment Routing with IPv6
   [    3.314856] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   [    3.320985] NET: Registered protocol family 17
   [    3.325070] NET: Registered protocol family 15
   [    3.329484] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
   [    3.342754] can: controller area network core (rev 20170425 abi 9)
   [    3.348559] NET: Registered protocol family 29
   [    3.352918] can: raw protocol (rev 20170425)
   [    3.357155] can: broadcast manager protocol (rev 20170425 t)
   [    3.362780] can: netlink gateway (rev 20170425) max_hops=1
   [    3.368292] Bluetooth: RFCOMM TTY layer initialized
   [    3.373080] Bluetooth: RFCOMM socket layer initialized
   [    3.378192] Bluetooth: RFCOMM ver 1.11
   [    3.381899] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
   [    3.387173] Bluetooth: BNEP filters: protocol multicast
   [    3.392365] Bluetooth: BNEP socket layer initialized
   [    3.397294] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
   [    3.403178] Bluetooth: HIDP socket layer initialized
   [    3.408220] 9pnet: Installing 9P2000 support
   [    3.412355] NET: Registered protocol family 36
   [    3.416774] Key type dns_resolver registered
   [    3.421525] registered taskstats version 1
   [    3.425069] Loading compiled-in X.509 certificates
   [    3.430177] Btrfs loaded, crc32c=crc32c-generic
   [    3.440707] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 40, base_baud = 6249999) is a xuartps
   [    3.450153] console [ttyPS0] enabled
   [    3.450153] console [ttyPS0] enabled
   [    3.453753] bootconsole [cdns0] disabled
   [    3.453753] bootconsole [cdns0] disabled
   [    3.461945] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 41, base_baud = 6249999) is a xuartps
   [    3.475319] of-fpga-region fpga-full: FPGA Region probed
   [    3.481150] nwl-pcie fd0e0000.pcie: Link is DOWN
   [    3.485798] nwl-pcie fd0e0000.pcie: host bridge /amba/pcie@fd0e0000 ranges:
   [    3.492768] nwl-pcie fd0e0000.pcie:   MEM 0xe0000000..0xefffffff -> 0xe0000000
   [    3.499990] nwl-pcie fd0e0000.pcie:   MEM 0x600000000..0x7ffffffff -> 0x600000000
   [    3.507574] nwl-pcie fd0e0000.pcie: PCI host bridge to bus 0000:00
   [    3.513756] pci_bus 0000:00: root bus resource [bus 00-ff]
   [    3.519239] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xefffffff]
   [    3.526109] pci_bus 0000:00: root bus resource [mem 0x600000000-0x7ffffffff pref]
   [    3.537882] pci 0000:00:00.0: PCI bridge to [bus 01-0c]
   [    3.544313] xilinx-dpdma fd4c0000.dma: Xilinx DPDMA engine is probed
   [    3.550889] xilinx-zynqmp-dma fd500000.dma: ZynqMP DMA driver Probe success
   [    3.557988] xilinx-zynqmp-dma fd510000.dma: ZynqMP DMA driver Probe success
   [    3.565091] xilinx-zynqmp-dma fd520000.dma: ZynqMP DMA driver Probe success
   [    3.572201] xilinx-zynqmp-dma fd530000.dma: ZynqMP DMA driver Probe success
   [    3.579300] xilinx-zynqmp-dma fd540000.dma: ZynqMP DMA driver Probe success
   [    3.586400] xilinx-zynqmp-dma fd550000.dma: ZynqMP DMA driver Probe success
   [    3.593503] xilinx-zynqmp-dma fd560000.dma: ZynqMP DMA driver Probe success
   [    3.600605] xilinx-zynqmp-dma fd570000.dma: ZynqMP DMA driver Probe success
   [    3.607843] xilinx-psgtr fd400000.zynqmp_phy: Lane:1 type:8 protocol:4 pll_locked:yes
   [    3.619181] zynqmp_clk_divider_set_rate() set divider failed for spi1_ref_div1, ret = -13
   [    3.627856] xilinx-dp-snd-codec fd4a0000.zynqmp-display:zynqmp_dp_snd_codec0: Xilinx DisplayPort Sound Codec probed
   [    3.638630] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
   [    3.646720] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
   [    3.655160] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
   [    3.667600] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
   [    3.680357] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: Xilinx DisplayPort Sound Card probed
   [    3.690540] OF: graph: no port node found in /amba/zynqmp-display@fd4a0000
   [    3.697550] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
   [    3.704160] [drm] No driver support for vblank timestamp query.
   [    3.710141] xlnx-drm xlnx-drm.0: bound fd4a0000.zynqmp-display (ops 0xffffff8008dc2e70)
   [    3.851542] random: fast init done
   [    7.834438] [drm] Cannot find any crtc or sizes
   [    7.839198] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.zynqmp-display on minor 0
   [    7.847310] zynqmp-display fd4a0000.zynqmp-display: ZynqMP DisplayPort Subsystem driver probed
   [    7.856306] xilinx-psgtr fd400000.zynqmp_phy: Lane:3 type:3 protocol:2 pll_locked:yes
   [    7.864189] ahci-ceva fd0c0000.ahci: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl platform mode
   [    7.873148] ahci-ceva fd0c0000.ahci: flags: 64bit ncq sntf pm clo only pmp fbs pio slum part ccc sds apst
   [    7.883629] scsi host0: ahci-ceva
   [    7.887219] scsi host1: ahci-ceva
   [    7.890679] ata1: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x100 irq 37
   [    7.898593] ata2: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x180 irq 37
   [    7.911116] m25p80 spi0.0: SPI-NOR-UniqueID 1044002c3991000a03001c00668a718bd1
   [    7.918347] m25p80 spi0.0: found n25q512a, expected m25p80
   [    7.924030] m25p80 spi0.0: n25q512a (131072 Kbytes)
   [    7.928929] 4 fixed-partitions partitions found on MTD device spi0.0
   [    7.935274] Creating 4 MTD partitions on "spi0.0":
   [    7.940058] 0x000000000000-0x000000100000 : "qspi-fsbl-uboot"
   [    7.946265] 0x000000100000-0x000000600000 : "qspi-linux"
   [    7.951966] 0x000000600000-0x000000620000 : "qspi-device-tree"
   [    7.958204] 0x000000620000-0x000000c00000 : "qspi-rootfs"
   [    7.966043] macb ff0e0000.ethernet: Not enabling partial store and forward
   [    7.973403] libphy: MACB_mii_bus: probed
   [    7.977402] mdio_bus ff0e0000.ethernet-ffffffff: MDIO device at address 21 is missing.
   [    7.987597] TI DP83867 ff0e0000.ethernet-ffffffff:0c: attached PHY driver [TI DP83867] (mii_bus:phy_addr=ff0e0000.ethernet-ffffffff:0c, irq=POLL)
   [    8.000642] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 22 (0a:b9:b6:be:9e:f0)
   [    8.010765] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
   [    8.017306] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
   [    8.023798] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
   [    8.030291] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
   [    8.038204] dwc3 fe200000.dwc3: Failed to get clk 'ref': -2
   [    8.044057] xilinx-psgtr fd400000.zynqmp_phy: Lane:2 type:0 protocol:3 pll_locked:yes
   [    8.052411] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
   [    8.057905] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 1
   [    8.065904] xhci-hcd xhci-hcd.0.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x0000000202010810
   [    8.075316] xhci-hcd xhci-hcd.0.auto: irq 50, io mem 0xfe200000
   [    8.081440] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 4.19
   [    8.089710] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   [    8.096930] usb usb1: Product: xHCI Host Controller
   [    8.101798] usb usb1: Manufacturer: Linux 4.19.0-ga6ef26d xhci-hcd
   [    8.107970] usb usb1: SerialNumber: xhci-hcd.0.auto
   [    8.113126] hub 1-0:1.0: USB hub found
   [    8.116906] hub 1-0:1.0: 1 port detected
   [    8.121025] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
   [    8.126519] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 2
   [    8.134177] xhci-hcd xhci-hcd.0.auto: Host supports USB 3.0  SuperSpeed
   [    8.140907] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 4.19
   [    8.149170] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   [    8.156385] usb usb2: Product: xHCI Host Controller
   [    8.161254] usb usb2: Manufacturer: Linux 4.19.0-ga6ef26d xhci-hcd
   [    8.167425] usb usb2: SerialNumber: xhci-hcd.0.auto
   [    8.172538] hub 2-0:1.0: USB hub found
   [    8.176314] hub 2-0:1.0: 1 port detected
   [    8.181473] pca953x 0-0020: 0-0020 supply vcc not found, using dummy regulator
   [    8.188727] pca953x 0-0020: Linked as a consumer to regulator.0
   [    8.195533] GPIO line 496 (sel0) hogged as output/low
   [    8.200920] GPIO line 497 (sel1) hogged as output/high
   [    8.206393] GPIO line 498 (sel2) hogged as output/high
   [    8.211866] GPIO line 499 (sel3) hogged as output/high
   [    8.217220] pca953x 0-0021: 0-0021 supply vcc not found, using dummy regulator
   [    8.218374] ata2: SATA link down (SStatus 0 SControl 330)
   [    8.224469] pca953x 0-0021: Linked as a consumer to regulator.0
   [    8.229855] ata1: SATA link down (SStatus 0 SControl 330)
   [    8.237269] ina2xx 3-0040: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.247949] ina2xx 3-0041: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.254762] ina2xx 3-0042: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.261576] ina2xx 3-0043: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.268391] ina2xx 3-0044: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.275205] ina2xx 3-0045: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.282017] ina2xx 3-0046: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.288840] ina2xx 3-0047: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.295657] ina2xx 3-004a: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.302472] ina2xx 3-004b: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.308889] i2c i2c-0: Added multiplexed i2c bus 3
   [    8.314358] ina2xx 4-0040: power monitor ina226 (Rshunt = 2000 uOhm)
   [    8.321174] ina2xx 4-0041: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.327987] ina2xx 4-0042: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.334799] ina2xx 4-0043: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.341617] ina2xx 4-0044: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.348429] ina2xx 4-0045: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.355247] ina2xx 4-0046: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.362055] ina2xx 4-0047: power monitor ina226 (Rshunt = 5000 uOhm)
   [    8.368462] i2c i2c-0: Added multiplexed i2c bus 4
   [    8.407815] i2c i2c-0: Added multiplexed i2c bus 5
   [    8.412789] i2c i2c-0: Added multiplexed i2c bus 6
   [    8.417585] pca954x 0-0075: registered 4 multiplexed busses for I2C mux pca9544
   [    8.424933] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 24
   [    8.432731] at24 7-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
   [    8.439481] i2c i2c-1: Added multiplexed i2c bus 7
   [    8.444612] i2c i2c-1: Added multiplexed i2c bus 8
   [    8.451554] si570 9-005d: registered, current frequency 300000000 Hz
   [    8.457963] i2c i2c-1: Added multiplexed i2c bus 9
   [    8.475140] si570 10-005d: registered, current frequency 148500000 Hz
   [    8.481634] i2c i2c-1: Added multiplexed i2c bus 10
   [    8.486746] si5324 11-0069: si5328 probed
   [    8.548260] si5324 11-0069: si5328 probe successful
   [    8.553190] i2c i2c-1: Added multiplexed i2c bus 11
   [    8.558239] i2c i2c-1: Added multiplexed i2c bus 12
   [    8.563288] i2c i2c-1: Added multiplexed i2c bus 13
   [    8.568351] i2c i2c-1: Added multiplexed i2c bus 14
   [    8.573233] pca954x 1-0074: registered 8 multiplexed busses for I2C switch pca9548
   [    8.581184] i2c i2c-1: Added multiplexed i2c bus 15
   [    8.612435] i2c i2c-1: Added multiplexed i2c bus 16
   [    8.617493] i2c i2c-1: Added multiplexed i2c bus 17
   [    8.622552] i2c i2c-1: Added multiplexed i2c bus 18
   [    8.627609] i2c i2c-1: Added multiplexed i2c bus 19
   [    8.632669] i2c i2c-1: Added multiplexed i2c bus 20
   [    8.637732] i2c i2c-1: Added multiplexed i2c bus 21
   [    8.642788] i2c i2c-1: Added multiplexed i2c bus 22
   [    8.647669] pca954x 1-0075: registered 8 multiplexed busses for I2C switch pca9548
   [    8.655275] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 25
   [    8.661651] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
   [    8.696744] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
   [    8.826413] mmc0: new ultra high speed SDR104 SDHC card at address aaaa
   [    8.833526] mmcblk0: mmc0:aaaa SP32G 29.7 GiB
   [    8.841380]  mmcblk0: p1 p2 p3
   [    9.100768] random: crng init done
   [   16.938476] adrv9002 spi1.0: adrv9002-phy Rev 12.0, Firmware 0.14.5.6,  Stream 0.5.18.0,  API version: 39.0.7 successfully initialized
   [   16.951258] cf_axi_adc 84a00000.axi-adrv9002-rx-lpc: ADI AIM (10.01.b) at 0x84A00000 mapped to 0x0000000017c91dcf, probed ADC ADRV9002 as MASTER
   [   16.965199] cf_axi_tdd 84a0c800.axi-adrv9002-core-tdd1-lpc: Analog Devices CF_AXI_TDD MASTER (1.00.a)
   [   16.974840] cf_axi_tdd 84a0cc00.axi-adrv9002-core-tdd2-lpc: Analog Devices CF_AXI_TDD MASTER (1.00.a)
   [   17.004448] cf_axi_dds 84a0a000.axi-adrv9002-tx-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x84A0A000 mapped to 0x00000000640a8a22, probed DDS ADRV9002
   [   17.036426] cf_axi_dds 84a0c000.axi-adrv9002-tx2-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x84A0C000 mapped to 0x000000006564ee6e, probed DDS ADRV9002
   [   17.053492] input: gpio-keys as /devices/platform/gpio-keys/input/input0
   [   17.060492] rtc_zynqmp ffa60000.rtc: setting system clock to 2021-03-09 01:17:41 UTC (1615252661)
   [   17.069375] of_cfs_init
   [   17.071824] of_cfs_init: OK
   [   17.074749] cfg80211: Loading compiled-in X.509 certificates for regulatory database
   [   17.159479] [drm] Cannot find any crtc or sizes
   [   17.213690] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
   [   17.220214] clk: Not disabling unused clocks
   [   17.224481] ALSA device list:
   [   17.227432]   #0: DisplayPort monitor
   [   17.231432] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
   [   17.240042] cfg80211: failed to load regulatory.db
   [   17.401445] EXT4-fs (mmcblk0p2): recovery complete
   [   17.406805] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   [   17.414918] VFS: Mounted root (ext4 filesystem) on device 179:2.
   [   17.425156] devtmpfs: mounted
   [   17.428300] Freeing unused kernel memory: 832K
   [   17.432778] Run /sbin/init as init process
   [   17.639668] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
   [   17.661409] systemd[1]: Detected architecture arm64.

   Welcome to Kuiper GNU/Linux 10 (buster)!

   [   17.682519] systemd[1]: Set hostname to <analog>.
   [   17.817555] systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
   [   17.834616] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
   [   17.950609] systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
   [   17.960300] systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
   [   18.109959] systemd[1]: Created slice system-serial\x2dgetty.slice.
   [  OK  ] Created slice system-serial\x2dgetty.slice.
   [   18.136377] systemd[1]: Listening on udev Control Socket.
   [  OK  ] Listening on udev Control Socket.
   [   18.156427] systemd[1]: Listening on udev Kernel Socket.
   [  OK  ] Listening on udev Kernel Socket.
   [  OK  ] Listening on Journal Socket (/dev/log).
   [  OK  ] Created slice User and Session Slice.
   [  OK  ] Listening on initctl Compatibility Named Pipe.
   [  OK  ] Listening on Journal Audit Socket.
   [  OK  ] Reached target Slices.
   [  OK  ] Created slice system-systemd\x2dfsck.slice.
   [  OK  ] Listening on Syslog Socket.
   [  OK  ] Listening on Journal Socket.
            Mounting Huge Pages File System...
            Starting Restore / save the current clock...
            Mounting RPC Pipe File System...
            Mounting Kernel Debug File System...
            Starting Set the console keyboard layout...
            Starting Journal Service...
            Starting udev Coldplug all Devices...
            Mounting POSIX Message Queue File System...
            Starting Load Kernel Modules...
   [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
   [  OK  ] Reached target Swap.
   [  OK  ] Created slice system-getty.slice.
   [  OK  ] Listening on fsck to fsckd communication Socket.
   [  OK  ] Started Journal Service.
   [  OK  ] Mounted Huge Pages File System.
   [  OK  ] Started Restore / save the current clock.
   [  OK  ] Mounted RPC Pipe File System.
   [  OK  ] Mounted Kernel Debug File System.
   [  OK  ] Mounted POSIX Message Queue File System.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Started Set the console keyboard layout.
            Mounting Kernel Configuration File System...
            Starting Apply Kernel Variables...
            Starting Remount Root and Kernel File Systems...
   [  OK  ] Mounted Kernel Configuration File System.
   [  OK  ] Started Apply Kernel Variables.
   [  OK  ] Started Remount Root and Kernel File Systems.
            Starting Load/Save Random Seed...
            Starting Create System Users...
            Starting Flush Journal to Persistent Storage...
   [  OK  ] Started Load/Save Random Seed.
   [  OK  ] Started udev Coldplug all Devices.
   [  OK  ] Started Create System Users.
            Starting Create Static Device Nodes in /dev...
            Starting Helper to synchronize boot up for ifupdown...
   [  OK  ] Started Flush Journal to Persistent Storage.
   [  OK  ] Started Create Static Device Nodes in /dev.
   [  OK  ] Started Helper to synchronize boot up for ifupdown.
            Starting udev Kernel Device Manager...
   [  OK  ] Reached target Local File Systems (Pre).
   [  OK  ] Started udev Kernel Device Manager.
            Starting Show Plymouth Boot Screen...
   [  OK  ] Started Show Plymouth Boot Screen.
   [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
   [  OK  ] Reached target Local Encrypted Volumes.
            Starting Load Kernel Modules...
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Found device /dev/ttyPS0.
   [  OK  ] Found device /dev/disk/by-partuuid/18f1f9d5-01.
            Starting File System Check…isk/by-partuuid/18f1f9d5-01...
   [  OK  ] Started File System Check Daemon to report status.
   [  OK  ] Found device /dev/ttyS0.
   [  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
   [  OK  ] Started File System Check …/disk/by-partuuid/18f1f9d5-01.
            Mounting /boot...
   [  OK  ] Mounted /boot.
   [  OK  ] Reached target Local File Systems.
            Starting Tell Plymouth To Write Out Runtime Data...
            Starting Raise network interfaces...
            Starting Create Volatile Files and Directories...
            Starting Set console font and keymap...
            Starting Preprocess NFS configuration...
   [  OK  ] Started Preprocess NFS configuration.
   [  OK  ] Reached target NFS client services.
   [  OK  ] Reached target Remote File Systems (Pre).
   [  OK  ] Reached target Remote File Systems.
   [  OK  ] Started Set console font and keymap.
   [  OK  ] Started Create Volatile Files and Directories.
            Starting Update UTMP about System Boot/Shutdown...
            Starting Network Time Synchronization...
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [  OK  ] Started Network Time Synchronization.
   [  OK  ] Reached target System Time Synchronized.
   [  OK  ] Started Update UTMP about System Boot/Shutdown.
   [  OK  ] Reached target System Initialization.
   [  OK  ] Listening on CUPS Scheduler.
   [  OK  ] Listening on triggerhappy.socket.
   [  OK  ] Started Daily apt download activities.
   [  OK  ] Listening on D-Bus System Message Bus Socket.
   [  OK  ] Listening on GPS (Global P…ioning System) Daemon Sockets.
   [  OK  ] Started Daily Cleanup of Temporary Directories.
   [  OK  ] Started Daily man-db regeneration.
   [  OK  ] Started Daily rotation of log files.
   [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
   [  OK  ] Reached target Sockets.
   [  OK  ] Started Daily apt upgrade and clean activities.
   [  OK  ] Reached target Timers.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Reached target Paths.
   [  OK  ] Reached target Basic System.
            Starting dhcpcd on all interfaces...
            Starting Modem Manager...
            Starting triggerhappy global hotkey daemon...
            Starting dphys-swapfile - …unt, and delete a swap file...
            Starting LSB: Switch to on…nless shift key is pressed)...
            Starting Check for Raspberry Pi EEPROM updates...
            Starting rng-tools.service...
   [  OK  ] Started D-Bus System Message Bus.
            Starting WPA supplicant...
            Starting Disk Manager...
   [  OK  ] Started Manage Sound Card State (restore and store).
   [  OK  ] Started tof-server.service.
            Starting Avahi mDNS/DNS-SD Stack...
   [  OK  ] Started Regular background program processing daemon.
            Starting Save/Restore Sound Card State...
            Starting Login Service...
            Starting System Logging Service...
   [  OK  ] Started CUPS Scheduler.
   [FAILED] Failed to start rng-tools.service.
   See 'systemctl status rng-tools.service' for details.
            Starting Rotate log files...
            Starting Daily man-db regeneration...
   [  OK  ] Started triggerhappy global hotkey daemon.
   [  OK  ] Started Save/Restore Sound Card State.
   [  OK  ] Started Rotate log files.
   [FAILED] Failed to start Check for Raspberry Pi EEPROM updates.
   See 'systemctl status rpi-eeprom-update.service' for details.
   [  OK  ] Started System Logging Service.
   [  OK  ] Started dhcpcd on all interfaces.
   [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
   [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
   [  OK  ] Started Raise network interfaces.
   [  OK  ] Started Avahi mDNS/DNS-SD Stack.
   [  OK  ] Started WPA supplicant.
   [  OK  ] Started Login Service.
   [  OK  ] Started Make remote CUPS printers available locally.
            Starting Authorization Manager...
   [  OK  ] Reached target Network.
            Starting Daily apt download activities...
            Starting OpenBSD Secure Shell server...
            Starting Permit User Sessions...
            Starting HTTP based time synchronization tool...
            Starting /etc/rc.local Compatibility...
   [  OK  ] Started IIO Daemon.
   [  OK  ] Reached target Sound Card.
   [  OK  ] Started Permit User Sessions.
            Starting Light Display Manager...
   [  OK  ] Started /etc/rc.local Compatibility.
            Starting Hold until boot process finishes up...
   [  OK  ] Started HTTP based time synchronization tool.
   [  OK  ] Started OpenBSD Secure Shell server.
   [  OK  ] Started Authorization Manager.

   Raspbian GNU/Linux 10 analog ttyPS0

   analog login: root (automatic login)

   Last login: Wed Feb 24 01:09:27 GMT 2021 on ttyPS0
   Linux analog 4.19.0-ga6ef26d #1105 SMP Fri Feb 19 16:51:27 GMT 2021 aarch64

   The programs included with the Debian GNU/Linux system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.

   Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
   permitted by applicable law.
   root@analog:~#

</hidden>

For independent mode, these devices should be present:

::

   root@analog:~# iio_info | grep iio:device
           iio:device0: ams
           iio:device1: adrv9002-phy
           iio:device2: axi-adrv9002-rx-lpc (buffer capable)
           iio:device3: axi-adrv9002-rx2-lpc (buffer capable)
           iio:device4: axi-adrv9002-core-tdd1-lpc
           iio:device5: axi-adrv9002-core-tdd2-lpc
           iio:device6: axi-adrv9002-tx-lpc (buffer capable)
           iio:device7: axi-adrv9002-tx2-lpc (buffer capable)

For MIMO mode, these devices should be present: ::

   root@analog:~# iio_info | grep iio:device
           iio:device0: ams
           iio:device1: adrv9002-phy
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
