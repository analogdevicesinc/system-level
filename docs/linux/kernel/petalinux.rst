.. _linux-kernel petalinux:

Build with Petalinux
====================

The ADI Linux kernel can also be compiled using Petalinux to be used on Xilinx
SoC FPGA based platforms (using :git-meta-adi:`ADI Yocto </>` repository).
The following table specifies the supported Petalinux versions and documentation:

.. list-table::
   :header-rows: 1

   - - Petalinux version
     - Meta-adi branch
     - Documentation
   - - 2018.2
     - :git-meta-adi:`2018_R2 <2018_R2:>`
     - :git-meta-adi:`README <2018_R2:meta-adi-xilinx/README.md>`
   - - 2018.3
     - :git-meta-adi:`2019_R1 <2019_R1:>`
     - :git-meta-adi:`README <2019_R1:meta-adi-xilinx/README.md>`
   - - 2019.1
     - :git-meta-adi:`2019_R2 <2019_R2:>`
     - :git-meta-adi:`README <2019_R2:meta-adi-xilinx/README.md>`
   - - 2021.1
     - :git-meta-adi:`2021_R1 <2021_R1:>`
     - :git-meta-adi:`README <2021_R1:meta-adi-xilinx/README.md>`
   - - 2021.2
     - :git-meta-adi:`2021_R2 <2021_R2:>`
     - :git-meta-adi:`README <2021_R2:meta-adi-xilinx/README.md>`
   - - 2022.2
     - :git-meta-adi:`2022_R2 <2022_R2:>`
     - :git-meta-adi:`README <2022_R2:meta-adi-xilinx/README.md>`
   - - 2023.2
     - :git-meta-adi:`2023_R2 <2023_R2:>`
     - :git-meta-adi:`README <2023_R2:meta-adi-xilinx/README.md>`
   - - latest
     - :git-meta-adi:`main <main:>`
     - :git-meta-adi:`README <main:meta-adi-xilinx/README.md>`

Messages
--------

If you are interested in the Linux console messages and command line interface,
connect a USB cable to the USB UART port.
Terminal settings are 115200, 8N1.

The user is:

.. list-table::
   :header-rows: 1

   - - user
     - password
   - - root
     - analog

.. note::

   This specifies any shell prompt running on the target.

.. collapsible:: Full boot log

   ::

      Xilinx Zynq MP First Stage Boot Loader
      Release 2018.3   Apr 16 2019  -  10:56:27
      NOTICE:  ATF running on XCZU9EG/silicon v4/RTL5.1 at 0xfffea000
      NOTICE:  BL31: Secure code at 0x0
      NOTICE:  BL31: Non secure code at 0x8000000
      NOTICE:  BL31: v1.5(release):xilinx-v2018.2-919-g08560c36
      NOTICE:  BL31: Built : 11:27:45, Apr 16 2019
      PMUFW:  v1.1


      U-Boot 2018.01 (Apr 16 2019 - 11:28:18 +0000) Xilinx ZynqMP ZCU102 rev1.0

      I2C:   ready
      DRAM:  4 GiB
      EL Level:       EL2
      Chip ID:        zu9eg
      MMC:   mmc@ff170000: 0 (SD)
      SF: Detected n25q512a with page size 512 Bytes, erase size 128 KiB, total 128 MiB
      * Warning - bad CRC, using default environment

      In:    serial@ff000000
      Out:   serial@ff000000
      Err:   serial@ff000000
      Model: ZynqMP ZCU102 Rev1.0
      Board: Xilinx ZynqMP
      Bootmode: LVL_SHFT_SD_MODE1
      Net:   ZYNQ GEM: ff0e0000, phyaddr c, interface rgmii-id
      eth0: ethernet@ff0e0000
      U-BOOT for zynqmp-zcu102-fmcomms5

      ethernet@ff0e0000 Waiting for PHY auto negotiation to complete………………………………….. TIMEOUT !
      Hit any key to stop autoboot:  0
      reading uEnv.txt
      381 bytes read in 11 ms (33.2 KiB/s)
      Loaded environment from uEnv.txt
      Importing environment from SD …
      Running uenvcmd …
      Copying Linux from SD to RAM…
       No boot file defined **
      Device: mmc@ff170000
      Manufacturer ID: 3
      OEM: 5344
      Name: SU08G
      Tran Speed: 50000000
      Rd Block Len: 512
      SD version 3.0
      High Capacity: Yes
      Capacity: 7.4 GiB
      Bus Width: 4-bit
      Erase Group Size: 512 Bytes
      reading image.ub
      16130812 bytes read in 1071 ms (14.4 MiB/s)
      ## Loading kernel from FIT Image at 10000000 ...
         Using 'conf@system-top.dtb' configuration
         Trying 'kernel@1' kernel subimage
           Description:  Linux kernel
           Type:         Kernel Image
           Compression:  gzip compressed
           Data Start:   0x100000e0
           Data Size:    7578821 Bytes = 7.2 MiB
           Architecture: AArch64
           OS:           Linux
           Load Address: 0x00080000
           Entry Point:  0x00080000
           Hash algo:    sha1
           Hash value:   2906e2018b0136613000500062aae9a5a87345dc
         Verifying Hash Integrity ... sha1+ OK
      ## Loading ramdisk from FIT Image at 10000000 ...
         Using 'conf@system-top.dtb' configuration
         Trying 'ramdisk@1' ramdisk subimage
           Description:  petalinux-user-image
           Type:         RAMDisk Image
           Compression:  gzip compressed
           Data Start:   0x10746fac
           Data Size:    8498623 Bytes = 8.1 MiB
           Architecture: AArch64
           OS:           Linux
           Load Address: unavailable
           Entry Point:  unavailable
           Hash algo:    sha1
           Hash value:   2f2c19999c6cd778aac11517d67b011692990ace
         Verifying Hash Integrity ... sha1+ OK
      ## Loading fdt from FIT Image at 10000000 ...
         Using 'conf@system-top.dtb' configuration
         Trying 'fdt@system-top.dtb' fdt subimage
           Description:  Flattened Device Tree blob
           Type:         Flat Device Tree
           Compression:  uncompressed
           Data Start:   0x1073a6ac
           Data Size:    51257 Bytes = 50.1 KiB
           Architecture: AArch64
           Hash algo:    sha1
           Hash value:   bd214ecff2ac522d2d26afed2b79009a67ee721b
         Verifying Hash Integrity ... sha1+ OK
         Booting using the fdt blob at 0x1073a6ac
         Uncompressing Kernel Image ... OK
         Loading Ramdisk to 077e5000, end 07fffdbf ... OK
         Loading Device Tree to 00000000077d5000, end 00000000077e4838 ... OK

      Starting kernel ...

      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 4.14.0-xilinx-v2018.3 (oe-user@oe-host) (gcc version 7.3.0 (GCC)) #1 SMP Tue Apr 16 11:08:34 UTC 2019
      [    0.000000] Boot CPU: AArch64 Processor [410fd034]
      [    0.000000] Machine model: ZynqMP ZCU102 Rev1.0
      [    0.000000] efi: Getting EFI parameters from FDT:
      [    0.000000] efi: UEFI not found.
      [    0.000000] cma: Reserved 256 MiB at 0x0000000070000000
      [    0.000000] psci: probing for conduit method from DT.
      [    0.000000] psci: PSCIv1.1 detected in firmware.
      [    0.000000] psci: Using standard PSCI v0.2 function IDs
      [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
      [    0.000000] random: fast init done
      [    0.000000] percpu: Embedded 21 pages/cpu @ffffffc87ff5c000 s46488 r8192 d31336 u86016
      [    0.000000] Detected VIPT I-cache on CPU0
      [    0.000000] CPU features: enabling workaround for ARM erratum 845719
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1034240
      [    0.000000] Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlyprintk rootfstype=ext4 rootwait
      [    0.000000] PID hash table entries: 4096 (order: 3, 32768 bytes)
      [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes)
      [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes)
      [    0.000000] software IO TLB [mem 0x6bfff000-0x6ffff000] (64MB) mapped at [ffffffc06bfff000-ffffffc06fffefff]
      [    0.000000] Memory: 3775276K/4194304K available (10428K kernel code, 728K rwdata, 4472K rodata, 512K init, 2164K bss, 156884K reserved, 262144K cma-reserved)
      [    0.000000] Virtual kernel memory layout:
      [    0.000000]     modules : 0xffffff8000000000 - 0xffffff8008000000   (   128 MB)
      [    0.000000]     vmalloc : 0xffffff8008000000 - 0xffffffbebfff0000   (   250 GB)
      [    0.000000]       .text : 0xffffff8008080000 - 0xffffff8008ab0000   ( 10432 KB)
      [    0.000000]     .rodata : 0xffffff8008ab0000 - 0xffffff8008f20000   (  4544 KB)
      [    0.000000]       .init : 0xffffff8008f20000 - 0xffffff8008fa0000   (   512 KB)
      [    0.000000]       .data : 0xffffff8008fa0000 - 0xffffff8009056200   (   729 KB)
      [    0.000000]        .bss : 0xffffff8009056200 - 0xffffff80092735b0   (  2165 KB)
      [    0.000000]     fixed   : 0xffffffbefe7fd000 - 0xffffffbefec00000   (  4108 KB)
      [    0.000000]     PCI I/O : 0xffffffbefee00000 - 0xffffffbeffe00000   (    16 MB)
      [    0.000000]     vmemmap : 0xffffffbf00000000 - 0xffffffc000000000   (     4 GB maximum)
      [    0.000000]               0xffffffbf00000000 - 0xffffffbf1dc00000   (   476 MB actual)
      [    0.000000]     memory  : 0xffffffc000000000 - 0xffffffc880000000   ( 34816 MB)
      [    0.000000] Hierarchical RCU implementation.
      [    0.000000]  RCU event tracing is enabled.
      [    0.000000]  RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
      [    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
      [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
      [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
      [    0.000000] GIC: Using split EOI/Deactivate mode
      [    0.000000] arch_timer: cp15 timer(s) running at 99.99MHz (phys).
      [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x170f8de2d3, max_idle_ns: 440795206112 ns
      [    0.000003] sched_clock: 56 bits at 99MHz, resolution 10ns, wraps every 4398046511101ns
      [    0.000347] Console: colour dummy device 80x25
      [    0.000366] Calibrating delay loop (skipped), value calculated using timer frequency.. 199.98 BogoMIPS (lpj=399960)
      [    0.000373] pid_max: default: 32768 minimum: 301
      [    0.000471] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes)
      [    0.000485] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes)
      [    0.001036] ASID allocator initialised with 65536 entries
      [    0.001081] Hierarchical SRCU implementation.
      [    0.001426] EFI services will not be available.
      [    0.001449] zynqmp_plat_init Platform Management API v1.1
      [    0.001454] zynqmp_plat_init Trustzone version v1.0
      [    0.001546] smp: Bringing up secondary CPUs ...
      [    0.001787] Detected VIPT I-cache on CPU1
      [    0.001815] CPU1: Booted secondary processor [410fd034]
      [    0.002081] Detected VIPT I-cache on CPU2
      [    0.002098] CPU2: Booted secondary processor [410fd034]
      [    0.002351] Detected VIPT I-cache on CPU3
      [    0.002369] CPU3: Booted secondary processor [410fd034]
      [    0.002410] smp: Brought up 1 node, 4 CPUs
      [    0.002424] SMP: Total of 4 processors activated.
      [    0.002429] CPU features: detected feature: 32-bit EL0 Support
      [    0.002436] CPU: All CPU(s) started at EL2
      [    0.002449] alternatives: patching kernel code
      [    0.003172] devtmpfs: initialized
      [    0.008711] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
      [    0.008727] futex hash table entries: 1024 (order: 5, 131072 bytes)
      [    0.014117] xor: measuring software checksum speed
      [    0.052007]    8regs     :  2302.000 MB/sec
      [    0.092036]    8regs_prefetch:  2052.000 MB/sec
      [    0.132067]    32regs    :  2830.000 MB/sec
      [    0.172098]    32regs_prefetch:  2379.000 MB/sec
      [    0.172103] xor: using function: 32regs (2830.000 MB/sec)
      [    0.172166] pinctrl core: initialized pinctrl subsystem
      [    0.172643] NET: Registered protocol family 16
      [    0.173358] cpuidle: using governor menu
      [    0.173925] vdso: 2 pages (1 code @ ffffff8008ab6000, 1 data @ ffffff8008fa4000)
      [    0.173949] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
      [    0.174401] DMA: preallocated 256 KiB pool for atomic allocations
      [    0.195403] reset_zynqmp reset-controller: Xilinx zynqmp reset driver probed
      [    0.196008] ARM CCI_400_r1 PMU driver probed
      [    0.200822] zynqmp-pinctrl ff180000.pinctrl: zynqmp pinctrl initialized
      [    0.209180] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
      [    0.276332] raid6: int64x1  gen()   403 MB/s
      [    0.344306] raid6: int64x1  xor()   446 MB/s
      [    0.412333] raid6: int64x2  gen()   689 MB/s
      [    0.480360] raid6: int64x2  xor()   602 MB/s
      [    0.548440] raid6: int64x4  gen()  1042 MB/s
      [    0.616483] raid6: int64x4  xor()   741 MB/s
      [    0.684509] raid6: int64x8  gen()   979 MB/s
      [    0.752552] raid6: int64x8  xor()   745 MB/s
      [    0.820617] raid6: neonx1   gen()   726 MB/s
      [    0.888653] raid6: neonx1   xor()   852 MB/s
      [    0.956750] raid6: neonx2   gen()  1170 MB/s
      [    1.024775] raid6: neonx2   xor()  1207 MB/s
      [    1.092839] raid6: neonx4   gen()  1505 MB/s
      [    1.160873] raid6: neonx4   xor()  1441 MB/s
      [    1.228916] raid6: neonx8   gen()  1651 MB/s
      [    1.296971] raid6: neonx8   xor()  1532 MB/s
      [    1.296975] raid6: using algorithm neonx8 gen() 1651 MB/s
      [    1.296978] raid6: .... xor() 1532 MB/s, rmw enabled
      [    1.296982] raid6: using neon recovery algorithm
      [    1.298416] SCSI subsystem initialized
      [    1.298560] usbcore: registered new interface driver usbfs
      [    1.298589] usbcore: registered new interface driver hub
      [    1.298620] usbcore: registered new device driver usb
      [    1.298679] media: Linux media interface: v0.10
      [    1.298703] Linux video capture interface: v2.00
      [    1.298740] pps_core: LinuxPPS API ver. 1 registered
      [    1.298744] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    1.298759] PTP clock support registered
      [    1.298956] zynqmp-ipi ff9905c0.mailbox: Probed ZynqMP IPI Mailbox driver.
      [    1.299103] FPGA manager framework
      [    1.299202] fpga-region fpga-full: FPGA Region probed
      [    1.299299] Advanced Linux Sound Architecture Driver Initialized.
      [    1.299539] Bluetooth: Core ver 2.22
      [    1.299562] NET: Registered protocol family 31
      [    1.299565] Bluetooth: HCI device and connection manager initialized
      [    1.299573] Bluetooth: HCI socket layer initialized
      [    1.299578] Bluetooth: L2CAP socket layer initialized
      [    1.299600] Bluetooth: SCO socket layer initialized
      [    1.300138] clocksource: Switched to clocksource arch_sys_counter
      [    1.300202] VFS: Disk quotas dquot_6.6.0
      [    1.300243] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
      [    1.304119] NET: Registered protocol family 2
      [    1.304428] TCP established hash table entries: 32768 (order: 6, 262144 bytes)
      [    1.304633] TCP bind hash table entries: 32768 (order: 7, 524288 bytes)
      [    1.305011] TCP: Hash tables configured (established 32768 bind 32768)
      [    1.305076] UDP hash table entries: 2048 (order: 4, 65536 bytes)
      [    1.305148] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes)
      [    1.305292] NET: Registered protocol family 1
      [    1.305547] RPC: Registered named UNIX socket transport module.
      [    1.305552] RPC: Registered udp transport module.
      [    1.305555] RPC: Registered tcp transport module.
      [    1.305559] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    1.305650] Trying to unpack rootfs image as initramfs...
      [    1.631102] Freeing initrd memory: 8296K
      [    1.631496] hw perfevents: no interrupt-affinity property for /pmu, guessing.
      [    1.631643] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
      [    1.632331] audit: initializing netlink subsys (disabled)
      [    1.632410] audit: type=2000 audit(1.627:1): state=initialized audit_enabled=0 res=1
      [    1.632713] workingset: timestamp_bits=62 max_order=20 bucket_order=0
      [    1.633383] NFS: Registering the id_resolver key type
      [    1.633399] Key type id_resolver registered
      [    1.633403] Key type id_legacy registered
      [    1.633411] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      [    1.633427] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
      [    1.661982] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
      [    1.661993] io scheduler noop registered
      [    1.661997] io scheduler deadline registered
      [    1.662013] io scheduler cfq registered (default)
      [    1.662017] io scheduler mq-deadline registered
      [    1.662021] io scheduler kyber registered
      [    1.662671] nwl-pcie fd0e0000.pcie: Link is DOWN
      [    1.662712] OF: PCI: host bridge /amba/pcie@fd0e0000 ranges:
      [    1.662728] OF: PCI:   MEM 0xe0000000..0xefffffff -> 0xe0000000
      [    1.662735] OF: PCI:   MEM 0x600000000..0x7ffffffff -> 0x600000000
      [    1.662859] nwl-pcie fd0e0000.pcie: PCI host bridge to bus 0000:00
      [    1.662867] pci_bus 0000:00: root bus resource [bus 00-ff]
      [    1.662874] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xefffffff]
      [    1.662880] pci_bus 0000:00: root bus resource [mem 0x600000000-0x7ffffffff pref]
      [    1.663128] pci 0000:00:00.0: PCI bridge to [bus 01-0c]
      [    1.664475] xilinx-dpdma fd4c0000.dma: Xilinx DPDMA engine is probed
      [    1.664724] xilinx-zynqmp-dma fd500000.dma: ZynqMP DMA driver Probe success
      [    1.664873] xilinx-zynqmp-dma fd510000.dma: ZynqMP DMA driver Probe success
      [    1.665024] xilinx-zynqmp-dma fd520000.dma: ZynqMP DMA driver Probe success
      [    1.665176] xilinx-zynqmp-dma fd530000.dma: ZynqMP DMA driver Probe success
      [    1.665324] xilinx-zynqmp-dma fd540000.dma: ZynqMP DMA driver Probe success
      [    1.665473] xilinx-zynqmp-dma fd550000.dma: ZynqMP DMA driver Probe success
      [    1.665624] xilinx-zynqmp-dma fd560000.dma: ZynqMP DMA driver Probe success
      [    1.665775] xilinx-zynqmp-dma fd570000.dma: ZynqMP DMA driver Probe success
      [    1.665976] xilinx-zynqmp-dma ffa80000.dma: ZynqMP DMA driver Probe success
      [    1.666126] xilinx-zynqmp-dma ffa90000.dma: ZynqMP DMA driver Probe success
      [    1.666272] xilinx-zynqmp-dma ffaa0000.dma: ZynqMP DMA driver Probe success
      [    1.666424] xilinx-zynqmp-dma ffab0000.dma: ZynqMP DMA driver Probe success
      [    1.666573] xilinx-zynqmp-dma ffac0000.dma: ZynqMP DMA driver Probe success
      [    1.666724] xilinx-zynqmp-dma ffad0000.dma: ZynqMP DMA driver Probe success
      [    1.666873] xilinx-zynqmp-dma ffae0000.dma: ZynqMP DMA driver Probe success
      [    1.667023] xilinx-zynqmp-dma ffaf0000.dma: ZynqMP DMA driver Probe success
      [    1.691525] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
      [    1.694301] cacheinfo: Unable to detect cache hierarchy for CPU 0
      [    1.698261] brd: module loaded
      [    1.701516] loop: module loaded
      [    1.702305] ahci-ceva fd0c0000.ahci: couldn't get PHY in node ahci: -517
      [    1.702458] mtdoops: mtd device (mtddev=name/number) must be supplied
      [    1.704118] m25p80 spi0.0: SPI-NOR-UniqueID 1044002c39910013f8ff0800169b713d29
      [    1.704124] m25p80 spi0.0: found n25q512a, expected m25p80
      [    1.704336] m25p80 spi0.0: n25q512a (131072 Kbytes)
      [    1.704357] 4 ofpart partitions found on MTD device spi0.0
      [    1.704361] Creating 4 MTD partitions on "spi0.0":
      [    1.704370] 0x000000000000-0x000000100000 : "qspi-fsbl-uboot"
      [    1.704813] 0x000000100000-0x000000600000 : "qspi-linux"
      [    1.705178] 0x000000600000-0x000000620000 : "qspi-device-tree"
      [    1.705604] 0x000000620000-0x000000c00000 : "qspi-rootfs"
      [    1.706833] libphy: Fixed MDIO Bus: probed
      [    1.707769] tun: Universal TUN/TAP device driver, 1.6
      [    1.708955] CAN device driver interface
      [    1.711099] macb ff0e0000.ethernet: Not enabling partial store and forward
      [    1.711471] libphy: MACB_mii_bus: probed
      [    1.714562] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 31 (00:0a:35:00:22:01)
      [    1.714572] TI DP83867 ff0e0000.ethernet-ffffffff:0c: attached PHY driver [TI DP83867] (mii_bus:phy_addr=ff0e0000.ethernet-ffffffff:0c, irq=POLL)
      [    1.715210] usbcore: registered new interface driver asix
      [    1.715257] usbcore: registered new interface driver ax88179_178a
      [    1.715281] usbcore: registered new interface driver cdc_ether
      [    1.715306] usbcore: registered new interface driver net1080
      [    1.715331] usbcore: registered new interface driver cdc_subset
      [    1.715354] usbcore: registered new interface driver zaurus
      [    1.715386] usbcore: registered new interface driver cdc_ncm
      [    1.715693] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
      [    1.717226] usbcore: registered new interface driver uas
      [    1.717258] usbcore: registered new interface driver usb-storage
      [    1.717741] rtc_zynqmp ffa60000.rtc: rtc core: registered ffa60000.rtc as rtc0
      [    1.717791] i2c /dev entries driver
      [    1.718762] IR NEC protocol handler initialized
      [    1.718766] IR RC5(x/sz) protocol handler initialized
      [    1.718770] IR RC6 protocol handler initialized
      [    1.718774] IR JVC protocol handler initialized
      [    1.718777] IR Sony protocol handler initialized
      [    1.718781] IR SANYO protocol handler initialized
      [    1.718784] IR Sharp protocol handler initialized
      [    1.718788] IR MCE Keyboard/mouse protocol handler initialized
      [    1.718791] IR XMP protocol handler initialized
      [    1.719525] usbcore: registered new interface driver uvcvideo
      [    1.719528] USB Video Class driver (1.1.1)
      [    1.719950] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer at ffffff8009315000 with timeout 60s
      [    1.720095] cdns-wdt ff150000.watchdog: Xilinx Watchdog Timer at ffffff800931d000 with timeout 10s
      [    1.720304] Bluetooth: HCI UART driver ver 2.3
      [    1.720311] Bluetooth: HCI UART protocol H4 registered
      [    1.720315] Bluetooth: HCI UART protocol BCSP registered
      [    1.720319] Bluetooth: HCI UART protocol ATH3K registered
      [    1.720322] Bluetooth: HCI UART protocol Three-wire (H5) registered
      [    1.720369] Bluetooth: HCI UART protocol Intel registered
      [    1.720373] Bluetooth: HCI UART protocol QCA registered
      [    1.720406] usbcore: registered new interface driver bcm203x
      [    1.720434] usbcore: registered new interface driver bpa10x
      [    1.720462] usbcore: registered new interface driver bfusb
      [    1.720492] usbcore: registered new interface driver btusb
      [    1.720496] Bluetooth: Generic Bluetooth SDIO driver ver 0.1
      [    1.720540] usbcore: registered new interface driver ath3k
      [    1.720989] cpufreq: cpufreq_online: CPU0: Running at unlisted freq: 1199880 KHz
      [    1.721040] cpufreq: cpufreq_online: CPU0: Unlisted initial frequency changed to: 1199999 KHz
      [    1.721423] sdhci: Secure Digital Host Controller Interface driver
      [    1.721426] sdhci: Copyright(c) Pierre Ossman
      [    1.721430] sdhci-pltfm: SDHCI platform and OF driver helper
      [    1.768310] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
      [    1.774351] ledtrig-cpu: registered to indicate activity on CPUs
      [    1.774485] usbcore: registered new interface driver usbhid
      [    1.774489] usbhid: USB HID core driver
      [    1.775341] ad9361 spi1.0: ad9361_probe : enter (ad9361-2x)
      [    1.776161] ad9361 spi1.1: ad9361_probe : enter (ad9361)
      [    1.780225] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
      [    1.782096] pktgen: Packet Generator for packet performance testing. Version: 2.75
      [    1.784331] Netfilter messages via NETLINK v0.30.
      [    1.784442] ip_tables: (C) 2000-2006 Netfilter Core Team
      [    1.784567] Initializing XFRM netlink socket
      [    1.784623] NET: Registered protocol family 10
      [    1.785037] Segment Routing with IPv6
      [    1.785078] ip6_tables: (C) 2000-2006 Netfilter Core Team
      [    1.785184] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    1.785485] NET: Registered protocol family 17
      [    1.785496] NET: Registered protocol family 15
      [    1.785510] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
      [    1.785515] Ebtables v2.0 registered
      [    1.785601] can: controller area network core (rev 20170425 abi 9)
      [    1.785630] NET: Registered protocol family 29
      [    1.785641] can: raw protocol (rev 20170425)
      [    1.785646] can: broadcast manager protocol (rev 20170425 t)
      [    1.785652] can: netlink gateway (rev 20170425) max_hops=1
      [    1.785853] Bluetooth: RFCOMM TTY layer initialized
      [    1.785861] Bluetooth: RFCOMM socket layer initialized
      [    1.785877] Bluetooth: RFCOMM ver 1.11
      [    1.785884] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
      [    1.785888] Bluetooth: BNEP filters: protocol multicast
      [    1.785894] Bluetooth: BNEP socket layer initialized
      [    1.785898] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
      [    1.785904] Bluetooth: HIDP socket layer initialized
      [    1.786012] 9pnet: Installing 9P2000 support
      [    1.786027] Key type dns_resolver registered
      [    1.786408] registered taskstats version 1
      [    1.786735] Btrfs loaded, crc32c=crc32c-generic
      [    1.791029] ff000000.serial: ttyPS0 at MMIO 0xff000000 (irq = 49, base_baud = 6249375) is a xuartps
      [    1.947009] mmc0: new high speed SDHC card at address e624
      [    1.954657] mmcblk0: mmc0:e624 SU08G 7.40 GiB
      [    1.962249]  mmcblk0: p1 p2 p3
      [    3.421883] console [ttyPS0] enabled
      [    3.425977] ff010000.serial: ttyPS1 at MMIO 0xff010000 (irq = 50, base_baud = 6249375) is a xuartps
      [    3.436499] xilinx-psgtr fd400000.zynqmp_phy: Lane:1 type:8 protocol:4 pll_locked:yes
      [    3.444737] PLL: shutdown
      [    3.449270] zynqmp_clk_divider_set_rate() set divider failed for pl2_ref_div1, ret = -13
      [    3.457812] xilinx-dp-snd-codec fd4a0000.zynqmp-display:zynqmp_dp_snd_codec0: Xilinx DisplayPort Sound Codec probed
      [    3.468465] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
      [    3.476489] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
      [    3.484771] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
      [    3.497205] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: xilinx-dp-snd-codec-dai <-> xilinx-dp-snd-codec-dai mapping ok
      [    3.509891] xilinx-dp-snd-card fd4a0000.zynqmp-display:zynqmp_dp_snd_card: Xilinx DisplayPort Sound Card probed
      [    3.520056] OF: graph: no port node found in /amba/zynqmp-display@fd4a0000
      [    3.527030] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
      [    3.533639] [drm] No driver support for vblank timestamp query.
      [    3.539597] xlnx-drm xlnx-drm.0: bound fd4a0000.zynqmp-display (ops 0xffffff8008b63130)
      [    4.624148] [drm] Cannot find any crtc or sizes
      [    4.628842] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.zynqmp-display on minor 0
      [    4.636943] zynqmp-display fd4a0000.zynqmp-display: ZynqMP DisplayPort Subsystem driver probed
      [    4.645873] xilinx-psgtr fd400000.zynqmp_phy: Lane:3 type:3 protocol:2 pll_locked:yes
      [    4.663811] ahci-ceva fd0c0000.ahci: AHCI 0001.0301 32 slots 2 ports 6 Gbps 0x3 impl platform mode
      [    4.672767] ahci-ceva fd0c0000.ahci: flags: 64bit ncq sntf pm clo only pmp fbs pio slum part ccc sds apst
      [    4.683052] scsi host0: ahci-ceva
      [    4.686540] scsi host1: ahci-ceva
      [    4.689953] ata1: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x100 irq 45
      [    4.697865] ata2: SATA max UDMA/133 mmio [mem 0xfd0c0000-0xfd0c1fff] port 0x180 irq 45
      [    4.707503] xilinx-psgtr fd400000.zynqmp_phy: Lane:2 type:0 protocol:3 pll_locked:yes
      [    4.715487] dwc3 fe200000.dwc3: stop_host(): INFO: Host already stopped
      [    4.722422] dwc3 fe200000.dwc3: stop_peripheral(): INFO: Peripheral already stopped
      [    4.766682] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
      [    4.772175] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 1
      [    4.780041] xhci-hcd xhci-hcd.0.auto: hcc params 0x0238f625 hci version 0x100 quirks 0x22010810
      [    4.788752] xhci-hcd xhci-hcd.0.auto: irq 58, io mem 0xfe200000
      [    4.794780] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
      [    4.801560] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    4.808772] usb usb1: Product: xHCI Host Controller
      [    4.813640] usb usb1: Manufacturer: Linux 4.14.0-xilinx-v2018.3 xhci-hcd
      [    4.820334] usb usb1: SerialNumber: xhci-hcd.0.auto
      [    4.825472] hub 1-0:1.0: USB hub found
      [    4.829236] hub 1-0:1.0: 1 port detected
      [    4.833325] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
      [    4.838823] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 2
      [    4.846588] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003
      [    4.853370] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    4.860588] usb usb2: Product: xHCI Host Controller
      [    4.865457] usb usb2: Manufacturer: Linux 4.14.0-xilinx-v2018.3 xhci-hcd
      [    4.872150] usb usb2: SerialNumber: xhci-hcd.0.auto
      [    4.877242] hub 2-0:1.0: USB hub found
      [    4.881012] hub 2-0:1.0: 1 port detected
      [    4.886074] pca953x 0-0020: 0-0020 supply vcc not found, using dummy regulator
      [    4.896411] GPIO line 496 (sel0) hogged as output/low
      [    4.901804] GPIO line 497 (sel1) hogged as output/high
      [    4.907283] GPIO line 498 (sel2) hogged as output/high
      [    4.912759] GPIO line 499 (sel3) hogged as output/high
      [    4.917991] pca953x 0-0020: interrupt support not compiled in
      [    4.923821] pca953x 0-0021: 0-0021 supply vcc not found, using dummy regulator
      [    4.933865] pca953x 0-0021: interrupt support not compiled in
      [    4.940392] ina2xx 3-0040: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.947156] ina2xx 3-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.953909] ina2xx 3-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.960672] ina2xx 3-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.967434] ina2xx 3-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.974195] ina2xx 3-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.980952] ina2xx 3-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.987721] ina2xx 3-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.994491] ina2xx 3-004a: power monitor ina226 (Rshunt = 5000 uOhm)
      [    4.996145] xhci-hcd xhci-hcd.0.auto: remove, state 4
      [    4.996158] usb usb2: USB disconnect, device number 1
      [    4.996524] xhci-hcd xhci-hcd.0.auto: USB bus 2 deregistered
      [    4.996534] xhci-hcd xhci-hcd.0.auto: remove, state 4
      [    4.996544] usb usb1: USB disconnect, device number 1
      [    4.996932] xhci-hcd xhci-hcd.0.auto: USB bus 1 deregistered
      [    4.996943] dwc3 fe200000.dwc3: stop_peripheral(): INFO: Peripheral already stopped
      [    5.018321] ata2: SATA link down (SStatus 0 SControl 330)
      [    5.018342] ata1: SATA link down (SStatus 0 SControl 330)
      [    5.051096] ina2xx 3-004b: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.057477] i2c i2c-0: Added multiplexed i2c bus 3
      [    5.062852] ina2xx 4-0040: power monitor ina226 (Rshunt = 2000 uOhm)
      [    5.069615] ina2xx 4-0041: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.076375] ina2xx 4-0042: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.083136] ina2xx 4-0043: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.089908] ina2xx 4-0044: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.096673] ina2xx 4-0045: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.103442] ina2xx 4-0046: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.110210] ina2xx 4-0047: power monitor ina226 (Rshunt = 5000 uOhm)
      [    5.116592] i2c i2c-0: Added multiplexed i2c bus 4
      [    5.162178] i2c i2c-0: Added multiplexed i2c bus 5
      [    5.167090] i2c i2c-0: Added multiplexed i2c bus 6
      [    5.171880] pca954x 0-0075: registered 4 multiplexed busses for I2C mux pca9544
      [    5.179208] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 33
      [    5.186748] at24 7-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
      [    5.193480] i2c i2c-1: Added multiplexed i2c bus 7
      [    5.198460] i2c i2c-1: Added multiplexed i2c bus 8
      [    5.205294] si570 9-005d: registered, current frequency 300000000 Hz
      [    5.211677] i2c i2c-1: Added multiplexed i2c bus 9
      [    5.230432] si570 10-005d: registered, current frequency 148500000 Hz
      [    5.236899] i2c i2c-1: Added multiplexed i2c bus 10
      [    5.241972] i2c i2c-1: Added multiplexed i2c bus 11
      [    5.246961] i2c i2c-1: Added multiplexed i2c bus 12
      [    5.251955] i2c i2c-1: Added multiplexed i2c bus 13
      [    5.256942] i2c i2c-1: Added multiplexed i2c bus 14
      [    5.261822] pca954x 1-0074: registered 8 multiplexed busses for I2C switch pca9548
      [    5.270789] at24 15-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      [    5.277515] i2c i2c-1: Added multiplexed i2c bus 15
      [    5.282514] i2c i2c-1: Added multiplexed i2c bus 16
      [    5.287508] i2c i2c-1: Added multiplexed i2c bus 17
      [    5.292506] i2c i2c-1: Added multiplexed i2c bus 18
      [    5.297500] i2c i2c-1: Added multiplexed i2c bus 19
      [    5.302506] i2c i2c-1: Added multiplexed i2c bus 20
      [    5.307499] i2c i2c-1: Added multiplexed i2c bus 21
      [    5.312495] i2c i2c-1: Added multiplexed i2c bus 22
      [    5.317371] pca954x 1-0075: registered 8 multiplexed busses for I2C switch pca9548
      [    5.324963] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 34
      [    5.331576] ad9361 spi1.0: ad9361_probe : enter (ad9361-2x)
      [    5.766498] ad9361 spi1.0: ad9361_probe : AD936x Rev 2 successfully initialized
      [    5.773905] ad9361 spi1.1: ad9361_probe : enter (ad9361)
      [    5.782016] [drm] Cannot find any crtc or sizes
      [    6.003730] ad9361 spi1.1: ad9361_probe : AD936x Rev 2 successfully initialized
      [    6.021782] cf_axi_dds 99024000.cf-ad9361-dds-core-lpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.00.b) at 0x99024000 mapped to 0xffffff80094b5000, probed DDS AD9361
      [    6.046963] cf_axi_dds 99044000.cf-ad9361-dds-core-B: Analog Devices CF_AXI_DDS_DDS SLAVE (9.00.b) at 0x99044000 mapped to 0xffffff80094bd000, probed DDS AD9361
      [    7.078009] cf_axi_adc 99020000.cf-ad9361-A: ADI AIM (10.00.b) at 0x99020000 mapped to 0xffffff800ce20000, probed ADC AD9361-2 as MASTER
      [    7.370437] cf_axi_adc 99040000.cf-ad9361-B: ADI AIM (10.00.b) at 0x99040000 mapped to 0xffffff800ce38000, probed ADC AD9361 as SLAVE
      [    7.383259] input: gpio-keys as /devices/platform/gpio-keys/input/input0
      [    7.390137] rtc_zynqmp ffa60000.rtc: setting system clock to 2019-04-16 12:02:36 UTC (1555416156)
      [    7.399204] PLL: shutdown
      [    7.401820] zynqmp_pll_disable() clock disable failed for dpll_int, ret = -13
      [    7.409839] ALSA device list:
      [    7.412796]   #0: DisplayPort monitor
      [    7.416852] Freeing unused kernel memory: 512K
      INIT: version 2.88 booting
      Starting udev
      [    7.523630] udevd[1990]: starting version 3.2.2
      [    7.532605] udevd[1991]: starting eudev-3.2.2
      [    8.014357] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [    8.026590] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
      Starting internet superserver: inetd.
      Configuring packages on first boot....
       (This may take several minutes. Please do not power off the machine.)
      Running postinst /etc/rpm-postinsts/100-sysvinit-inittab...
      update-rc.d: /etc/init.d/run-postinsts exists during rc.d purge (continuing)
      INIT: Entering runlevel: 5
      Configuring network interfaces... [    8.448344] pps pps0: new PPS source ptp0
      [    8.452360] macb ff0e0000.ethernet: gem-ptp-timer ptp clock registered.
      [    8.459031] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready
      udhcpc: started, v1.27.2
      udhcpc: sending discover
      udhcpc: sending discover
      udhcpc: sending discover
      udhcpc: no lease, forking to background
      done.
      Starting system message bus: dbus.
      Starting Dropbear SSH server: Generating key, this may take a while...
      Public key portion is:
      ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCuF37DxkZR0sjSKHa2/vQlwY+WPoFEclQnxWAgIbwqrElBne+3L/pT8j89OQyd1IRqS2Gc9aB1HaJXTXH13+uDsfU9JjecisogekSK8GlXEn4ihfHNmD+97ipiYcfanTyAXGCPgSrOgvnZ3VZiLmCtMpf75HeXVjFp/lrZ7Q5NdhnqChdsYCCGr5LFfA1L2cf2ux2haQlcQtCFEfyJVd6WXkXeLzOrWkChj2zp/YvEyXyOzAZN0hD6GHydo7QviGNxsVl+CKlqzvNJYKXI9t7Tj1g/tVnoxg4OxBZLapypuYlC+tK5ScOFH76iqy2UPP/eXXbbLZaHHA23uMmNu1vN root@zynqmp-zcu102-fmcomms5
      Fingerprint: md5 09:93:70:b0:28:21:92:90:fe:b0:1d:2a:de:e6:be:34
      dropbear.
      Starting IIO Daemon: iiod
      Starting syslogd/klogd: done
      Starting tcf-agent: OK

      PetaLinux 2018.3 zynqmp-zcu102-fmcomms5 /dev/ttyPS0

      zynqmp-zcu102-fmcomms5 login: root
      Password:

Petalinux, meta-adi and Device Trees
------------------------------------
There are several approaches for modifying and customizing the device trees of
a Petalinux project.

Please see:

.. toctree::
   :titlesonly:

   petalinux-dts/index

