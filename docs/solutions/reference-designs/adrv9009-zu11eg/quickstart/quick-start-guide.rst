.. _adrv9009-zu11eg quick-start:

ADRV9009-ZU11EG Quick Start Guide
==================================

.. image:: ../images/adrv9009-zu11g-quick-setup.png
   :align: center
   :width: 600

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the ADRV9009-ZU11EG on:

-  :adi:`ADRV2CRR-FMC`

If you want to use it with FMCOMMS8, please refer to :ref:`adrv9009-zu11eg fmcomms8-quick-start`

Instructions on how to build the ZynqMP / MPSoC Linux kernel and devicetrees
from source can be found here:

-  `Building the ZynqMP / MPSoC Linux kernel and devicetrees from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`_
-  `How to build the ZynqMP boot image BOOT.BIN <https://wiki.analog.com/resources/tools-software/linux-software/build-the-zynqmp-boot-image>`_

Required Software
-----------------

-  SD Card 16GB image using the instructions here: `Zynq & Altera SoC Quick Start Guide <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Please use the `Please use the Image 28 July 2021 release candidate (2019_R2) or later <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

.. collapsible:: Older Bootfiles (Click to expand)

   -  `ADRV9009-ZU11EG-14-06-2019.zip HW Rev.A <http://swdownloads.analog.com/cse/share/ADRV9009-ZU11EG-14-06-2019.zip>`_
   -  `ADRV9009-ZU11EG-RevB-10-09-2019.zip HW Rev.B <http://swdownloads.analog.com/cse/share/ADRV9009-ZU11EG-RevB-10-09-2019.zip>`_
   -  `ADRV9009-ZU11EG-RevB-07-08-2020.zip HW Rev.B <http://swdownloads.analog.com/cse/share/ADRV9009-ZU11EG-RevB-07-08-2020.zip>`_

Required Hardware
-----------------

-  ADRV9009-ZU11EG SoM board
-  ADRV2CRR-FMC carrier board
-  Micro-USB cable
-  Ethernet cable
-  Power Supply

Optional Hardware
-----------------

-  Reference clock source
-  USB Type-C multiport HUB
-  USB keyboard and mouse
-  DisplayPort compatible monitor

Testing
=======

.. esd-warning::

-  Connect the ``ADRV9009-ZU11EG`` System on Module to the
   ``ADRV2CRR-FMC`` carrier board.
-  Connect the 12V Power Supply to ``P11``
-  Connect USB UART ``P8`` (Micro USB) to your host PC.
-  Connect fan to ``P9``
-  Insert SD card into socket ``P15``.
-  Configure ADRV2CRR-FMC for SD BOOT using ``S13``, ``S14``, ``S15``,
   ``S16``. See picture below.

.. image:: ../images/adrv2crr_rev_a_and_b_sw_jmp_settings.jpg
   :align: center
   :width: 800

-  Configure ``ADRV2CRR-FMC`` for SD BOOT from carrier using ``S9``.
   See picture below.

.. image:: ../images/adrv9009-zu11g-sd-card-select.png
   :align: center
   :width: 400

-  Turn on the power switch on the carrier board using ``S12``.
-  Optionally connect test and measurement equipment to U.FL RF ports.
-  Observe kernel and serial console messages on your terminal. (use the first
   ttyUSB or COM port registered, Baud rate 115200 (8N1))

Messages
--------

.. container:: box bggreen

   This specifies any shell prompt running on the target

   .. collapsible:: Boot log (click to expand)

         ::

            Xilinx Zynq MP First Stage Boot Loader
            Release 2021.1   Aug  3 2022  -  11:00:01

            U-Boot 2018.01-21439-gd244ce5 (Mar 28 2021 - 13:30:43 +0100) Analog Devices Inc. ADR9009-ZU11EG, Build: jenkins-development-build_uboot-3

            I2C:   ready
            DRAM:  4 GiB
            EL Level:       EL2
            Chip ID:        zu11eg
            MMC:   sdhci@ff170000: 0 (SD)
            ** Warning - bad CRC, using default environment

            In:    serial@ff010000
            Out:   serial@ff010000
            Err:   serial@ff010000
            Bootmode: LVL_SHFT_SD_MODE1
            Net:   ZYNQ GEM: ff0b0000, phyaddr 1, interface sgmii
            i2c_mux_set: could not set mux: id: 5 chip: 74 channel: 0
            I2C EEPROM MAC address read failed

            Warning: ethernet@ff0b0000 (eth1) using random MAC address - c6:bd:2a:d9:e2:01
            eth1: ethernet@ff0b0000ZYNQ GEM: ff0e0000, phyaddr 0, interface rgmii-id
            I2C EEPROM MAC address read failed

            Warning: ethernet@ff0e0000 (eth0) using random MAC address - aa:cd:e8:38:80:de
            , eth0: ethernet@ff0e0000
            Hit any key to stop autoboot:  0
            switch to partitions #0, OK
            mmc0 is current device
            Device: sdhci@ff170000
            Manufacturer ID: 41
            OEM: 3432
            Name: SD16G
            Tran Speed: 50000000
            Rd Block Len: 512
            SD version 3.0
            High Capacity: Yes
            Capacity: 14.6 GiB
            Bus Width: 4-bit
            Erase Group Size: 512 Bytes
            reading uEnv.txt
            407 bytes read in 21 ms (18.6 KiB/s)
            Loaded environment from uEnv.txt
            Importing environment from SD ...
            Running uenvcmd ...
            Copying Linux from SD to RAM...
             No boot file defined 
            SF: Detected n25q512a with page size 512 Bytes, erase size 128 KiB, total 128 MiB
            device 0 offset 0x2000000, size 0x20000
            SF: 131072 bytes @ 0x2000000 Read: OK
            reading system.dtb
            79158 bytes read in 32 ms (2.4 MiB/s)
            reading Image
            32514560 bytes read in 2084 ms (14.9 MiB/s)
            ## Flattened Device Tree blob at 04000000
               Booting using the fdt blob at 0x4000000
               Loading Device Tree to 000000000ffe9000, end 000000000ffff535 ... OK

            Starting kernel ...

            [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd034]
            [    0.000000] Linux version 5.10.0-98248-g1bbe32fa5182 (jenkins@romlxbuild1.adlk.analog.com) (aarch64-xilinx-linux-gcc.real (GCC) 10.2.0, 2
            [    0.000000] Machine model: Analog Devices ADRV9009-ZU11EG Rev.B
            [    0.000000] earlycon: cdns0 at MMIO 0x00000000ff010000 (options '115200n8')
            [    0.000000] printk: bootconsole [cdns0] enabled
            [    0.000000] efi: UEFI not found.
            [    0.000000] cma: Reserved 256 MiB at 0x0000000070000000
            [    0.000000] Zone ranges:
            [    0.000000]   DMA      [mem 0x0000000000000000-0x000000003fffffff]
            [    0.000000]   DMA32    [mem 0x0000000040000000-0x00000000ffffffff]
            [    0.000000]   Normal   [mem 0x0000000100000000-0x000000087fffffff]
            [    0.000000] Movable zone start for each node
            [    0.000000] Early memory node ranges
            [    0.000000]   node   0: [mem 0x0000000000000000-0x000000007fffffff]
            [    0.000000]   node   0: [mem 0x0000000800000000-0x000000087fffffff]
            [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000087fffffff]
            [    0.000000] psci: probing for conduit method from DT.
            [    0.000000] psci: PSCIv1.1 detected in firmware.
            [    0.000000] psci: Using standard PSCI v0.2 function IDs
            [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
            [    0.000000] psci: SMC Calling Convention v1.2
            [    0.000000] percpu: Embedded 22 pages/cpu s49496 r8192 d32424 u90112
            [    0.000000] Detected VIPT I-cache on CPU0
            [    0.000000] CPU features: detected: ARM erratum 845719
            [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 1034240
            [    0.000000] Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidl1
            [    0.000000] Dentry cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
            [    0.000000] Inode-cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
            [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
            [    0.000000] software IO TLB: mapped [mem 0x000000003bfff000-0x000000003ffff000] (64MB)
            [    0.000000] Memory: 3761492K/4194304K available (15488K kernel code, 1672K rwdata, 11952K rodata, 2496K init, 507K bss, 170668K reserved)
            [    0.000000] rcu: Hierarchical RCU implementation.
            [    0.000000] rcu:     RCU event tracing is enabled.
            [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=8 to nr_cpu_ids=4.
            [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
            [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
            [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
            [    0.000000] GIC: Adjusting CPU interface base to 0x00000000f902f000
            [    0.000000] GIC: Using split EOI/Deactivate mode
            [    0.000000] random: get_random_bytes called from start_kernel+0x31c/0x550 with crng_init=0
            [    0.000000] arch_timer: cp15 timer(s) running at 33.33MHz (phys).
            [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x7b00c47c0, max_idle_ns: 440795202120 ns
            [    0.000003] sched_clock: 56 bits at 33MHz, resolution 30ns, wraps every 2199023255541ns
            [    0.008361] Console: colour dummy device 80x25
            [    0.012394] Calibrating delay loop (skipped), value calculated using timer frequency.. 66.66 BogoMIPS (lpj=133333)
            [    0.022667] pid_max: default: 32768 minimum: 301
            [    0.027374] Mount-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
            [    0.034613] Mountpoint-cache hash table entries: 8192 (order: 4, 65536 bytes, linear)
            [    0.043179] rcu: Hierarchical SRCU implementation.
            [    0.047369] EFI services will not be available.
            [    0.051756] smp: Bringing up secondary CPUs ...
            [    0.056463] Detected VIPT I-cache on CPU1
            [    0.056501] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
            [    0.056844] Detected VIPT I-cache on CPU2
            [    0.056866] CPU2: Booted secondary processor 0x0000000002 [0x410fd034]
            [    0.057182] Detected VIPT I-cache on CPU3
            [    0.057203] CPU3: Booted secondary processor 0x0000000003 [0x410fd034]
            [    0.057245] smp: Brought up 1 node, 4 CPUs
            [    0.091606] SMP: Total of 4 processors activated.
            [    0.096278] CPU features: detected: 32-bit EL0 Support
            [    0.101382] CPU features: detected: CRC32 instructions
            [    0.106518] CPU: All CPU(s) started at EL2
            [    0.110562] alternatives: patching kernel code
            [    0.115944] devtmpfs: initialized
            [    0.125323] Registered cp15_barrier emulation handler
            [    0.125372] Registered setend emulation handler
            [    0.129346] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
            [    0.138935] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
            [    0.151744] pinctrl core: initialized pinctrl subsystem
            [    0.152337] NET: Registered protocol family 16
            [    0.156729] DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations
            [    0.162816] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
            [    0.170539] DMA: preallocated 512 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
            [    0.178353] audit: initializing netlink subsys (disabled)
            [    0.183803] audit: type=2000 audit(0.116:1): state=initialized audit_enabled=0 res=1
            [    0.184104] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
            [    0.198177] ASID allocator initialised with 65536 entries
            [    0.222829] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
            [    0.223888] HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
            [    0.230544] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
            [    0.237205] HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
            [    1.208657] DRBG: Continuing without Jitter RNG
            [    1.284514] raid6: neonx8   gen()  2356 MB/s
            [    1.352561] raid6: neonx8   xor()  1757 MB/s
            [    1.420621] raid6: neonx4   gen()  2400 MB/s
            [    1.488662] raid6: neonx4   xor()  1717 MB/s
            [    1.556727] raid6: neonx2   gen()  2274 MB/s
            [    1.624764] raid6: neonx2   xor()  1578 MB/s
            [    1.692829] raid6: neonx1   gen()  1948 MB/s
            [    1.760876] raid6: neonx1   xor()  1339 MB/s
            [    1.828924] raid6: int64x8  gen()  1578 MB/s
            [    1.896976] raid6: int64x8  xor()   846 MB/s
            [    1.965032] raid6: int64x4  gen()  1754 MB/s
            [    2.033084] raid6: int64x4  xor()   897 MB/s
            [    2.101150] raid6: int64x2  gen()  1535 MB/s
            [    2.169190] raid6: int64x2  xor()   823 MB/s
            [    2.237260] raid6: int64x1  gen()  1131 MB/s
            [    2.305308] raid6: int64x1  xor()   567 MB/s
            [    2.305344] raid6: using algorithm neonx4 gen() 2400 MB/s
            [    2.309298] raid6: .... xor() 1717 MB/s, rmw enabled
            [    2.314233] raid6: using neon recovery algorithm
            [    2.319145] iommu: Default domain type: Translated
            [    2.323858] SCSI subsystem initialized
            [    2.327513] usbcore: registered new interface driver usbfs
            [    2.332854] usbcore: registered new interface driver hub
            [    2.338129] usbcore: registered new device driver usb
            [    2.343240] mc: Linux media interface: v0.10
            [    2.347380] videodev: Linux video capture interface: v2.00
            [    2.352865] EDAC MC: Ver: 3.0.0
            [    2.356269] zynqmp-ipi-mbox mailbox@ff990400: Registered ZynqMP IPI mbox with TX/RX channels.
            [    2.364886] jesd204: created con: id=0, topo=0, link=0, /fpga-axi@0/axi-jesd204-tx@84a30000 <-> /fpga-axi@0/axi-adrv9009-tx-hpc@84a04000
            [    2.376610] jesd204: created con: id=1, topo=0, link=0, /fpga-axi@0/axi-adxcvr-tx@84a20000 <-> /fpga-axi@0/axi-jesd204-tx@84a30000
            [    2.388288] jesd204: created con: id=2, topo=0, link=0, /axi/spi@ff040000/hmc7044@2 <-> /fpga-axi@0/axi-adxcvr-tx@84a20000
            [    2.399271] jesd204: created con: id=3, topo=0, link=2, /fpga-axi@0/axi-adxcvr-rx-os@84a60000 <-> /fpga-axi@0/axi-jesd204-rx@84a70000
            [    2.411213] jesd204: created con: id=4, topo=0, link=2, /axi/spi@ff040000/hmc7044@2 <-> /fpga-axi@0/axi-adxcvr-rx-os@84a60000
            [    2.422455] jesd204: created con: id=5, topo=0, link=1, /fpga-axi@0/axi-adxcvr-rx@84a40000 <-> /fpga-axi@0/axi-jesd204-rx@84a50000
            [    2.434132] jesd204: created con: id=6, topo=0, link=1, /axi/spi@ff040000/hmc7044@2 <-> /fpga-axi@0/axi-adxcvr-rx@84a40000
            [    2.445122] jesd204: created con: id=7, topo=0, link=1, /axi/spi@ff040000/hmc7044-car@3 <-> /axi/spi@ff040000/hmc7044@2
            [    2.455843] jesd204: created con: id=8, topo=0, link=2, /axi/spi@ff040000/hmc7044-car@3 <-> /axi/spi@ff040000/hmc7044@2
            [    2.466570] jesd204: created con: id=9, topo=0, link=0, /axi/spi@ff040000/hmc7044-car@3 <-> /axi/spi@ff040000/hmc7044@2
            [    2.477328] jesd204: created con: id=10, topo=0, link=1, /fpga-axi@0/axi-jesd204-rx@84a50000 <-> /axi/spi@ff040000/adrv9009-phy-b@1
            [    2.489065] jesd204: created con: id=11, topo=0, link=2, /fpga-axi@0/axi-jesd204-rx@84a70000 <-> /axi/spi@ff040000/adrv9009-phy-b@1
            [    2.500830] jesd204: created con: id=12, topo=0, link=0, /fpga-axi@0/axi-adrv9009-tx-hpc@84a04000 <-> /axi/spi@ff040000/adrv9009-phy-b@1
            [    2.513070] jesd204: created con: id=13, topo=0, link=1, /axi/spi@ff040000/adrv9009-phy-b@1 <-> /axi/spi@ff040000/adrv9009-phy@0
            [    2.524546] jesd204: created con: id=14, topo=0, link=2, /axi/spi@ff040000/adrv9009-phy-b@1 <-> /axi/spi@ff040000/adrv9009-phy@0
            [    2.536062] jesd204: created con: id=15, topo=0, link=0, /axi/spi@ff040000/adrv9009-phy-b@1 <-> /axi/spi@ff040000/adrv9009-phy@0
            [    2.547543] jesd204: /axi/spi@ff040000/adrv9009-phy@0: JESD204[0:0] transition uninitialized -> initialized
            [    2.557215] jesd204: /axi/spi@ff040000/adrv9009-phy@0: JESD204[0:1] transition uninitialized -> initialized
            [    2.566903] jesd204: /axi/spi@ff040000/adrv9009-phy@0: JESD204[0:2] transition uninitialized -> initialized
            [    2.576587] jesd204: found 11 devices and 1 topologies
            [    2.581715] FPGA manager framework
            [    2.585176] Advanced Linux Sound Architecture Driver Initialized.
            [    2.591475] Bluetooth: Core ver 2.22
            [    2.594675] NET: Registered protocol family 31
            [    2.599078] Bluetooth: HCI device and connection manager initialized
            [    2.605395] Bluetooth: HCI socket layer initialized
            [    2.610237] Bluetooth: L2CAP socket layer initialized
            [    2.615260] Bluetooth: SCO socket layer initialized
            [    2.620423] clocksource: Switched to clocksource arch_sys_counter
            [    2.626256] VFS: Disk quotas dquot_6.6.0
            [    2.630089] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
            [    2.640491] NET: Registered protocol family 2
            [    2.641518] tcp_listen_portaddr_hash hash table entries: 2048 (order: 3, 32768 bytes, linear)
            [    2.649721] TCP established hash table entries: 32768 (order: 6, 262144 bytes, linear)
            [    2.657734] TCP bind hash table entries: 32768 (order: 7, 524288 bytes, linear)
            [    2.665174] TCP: Hash tables configured (established 32768 bind 32768)
            [    2.671367] UDP hash table entries: 2048 (order: 4, 65536 bytes, linear)
            [    2.678032] UDP-Lite hash table entries: 2048 (order: 4, 65536 bytes, linear)
            [    2.685189] NET: Registered protocol family 1
            [    2.689645] RPC: Registered named UNIX socket transport module.
            [    2.695275] RPC: Registered udp transport module.
            [    2.699940] RPC: Registered tcp transport module.
            [    2.704608] RPC: Registered tcp NFSv4.1 backchannel transport module.
            [    2.711551] PCI: CLS 0 bytes, default 64
            [    2.715267] hw perfevents: no interrupt-affinity property for /pmu, guessing.
            [    2.722149] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
            [    2.730382] Initialise system trusted keyrings
            [    2.734184] workingset: timestamp_bits=62 max_order=20 bucket_order=0
            [    2.741039] NFS: Registering the id_resolver key type
            [    2.745535] Key type id_resolver registered
            [    2.749675] Key type id_legacy registered
            [    2.753666] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
            [    2.760329] jffs2: version 2.2. (NAND) (SUMMARY)  �© 2001-2006 Red Hat, Inc.
            [    2.767476] fuse: init (API version 7.32)
            [    2.804010] NET: Registered protocol family 38
            [    2.804051] xor: measuring software checksum speed
            [    2.811368]    8regs           :  2593 MB/sec
            [    2.815095]    32regs          :  3071 MB/sec
            [    2.819983]    arm64_neon      :  2612 MB/sec
            [    2.820543] xor: using function: 32regs (3071 MB/sec)
            [    2.825565] Key type asymmetric registered
            [    2.829626] Asymmetric key parser 'x509' registered
            [    2.834485] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 248)
            [    2.841823] io scheduler mq-deadline registered
            [    2.846320] io scheduler kyber registered
            [    2.873248] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
            [    2.877054] cacheinfo: Unable to detect cache hierarchy for CPU 0
            [    2.883828] brd: module loaded
            [    2.887717] loop: module loaded
            [    2.887956] Registered mathworks_ip class
            [    2.891876] libphy: Fixed MDIO Bus: probed
            [    2.895120] tun: Universal TUN/TAP device driver, 1.6
            [    2.899287] CAN device driver interface
            [    2.903665] usbcore: registered new interface driver asix
            [    2.908433] usbcore: registered new interface driver ax88179_178a
            [    2.914465] usbcore: registered new interface driver cdc_ether
            [    2.920252] usbcore: registered new interface driver net1080
            [    2.925874] usbcore: registered new interface driver cdc_subset
            [    2.931757] usbcore: registered new interface driver zaurus
            [    2.937304] usbcore: registered new interface driver cdc_ncm
            [    2.943539] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
            [    2.949387] ehci-pci: EHCI PCI platform driver
            [    2.954123] usbcore: registered new interface driver uas
            [    2.959105] usbcore: registered new interface driver usb-storage
            [    2.965091] usbcore: registered new interface driver usbserial_generic
            [    2.971542] usbserial: USB Serial support registered for generic
            [    2.977514] usbcore: registered new interface driver ftdi_sio
            [    2.983218] usbserial: USB Serial support registered for FTDI USB Serial Device
            [    2.990492] usbcore: registered new interface driver upd78f0730
            [    2.996366] usbserial: USB Serial support registered for upd78f0730
            [    3.003433] i2c /dev entries driver
            [    3.007452] usbcore: registered new interface driver uvcvideo
            [    3.011755] USB Video Class driver (1.1.1)
            [    3.016188] axi_fan_control_driver 80000000.axi-fan-control: clk_get failed with -517
            [    3.024182] Bluetooth: HCI UART driver ver 2.3
            [    3.028020] Bluetooth: HCI UART protocol H4 registered
            [    3.033118] Bluetooth: HCI UART protocol BCSP registered
            [    3.038407] Bluetooth: HCI UART protocol LL registered
            [    3.043498] Bluetooth: HCI UART protocol ATH3K registered
            [    3.048872] Bluetooth: HCI UART protocol Three-wire (H5) registered
            [    3.055118] Bluetooth: HCI UART protocol Intel registered
            [    3.060465] Bluetooth: HCI UART protocol QCA registered
            [    3.065665] usbcore: registered new interface driver bcm203x
            [    3.071286] usbcore: registered new interface driver bpa10x
            [    3.076822] usbcore: registered new interface driver bfusb
            [    3.082274] usbcore: registered new interface driver btusb
            [    3.087733] usbcore: registered new interface driver ath3k
            [    3.093257] EDAC MC0: 36 UE DDR ECC error type :UE Row 0 Bank 0 BankGroup Number 0 Block Number 0 on mc#0csrow#0channel#0 (csrow:0 chann)
            [    3.108288] EDAC MC0: Giving out device to module 1 controller synps_ddr_controller: DEV synps_edac (INTERRUPT)
            [    3.118380] EDAC DEVICE0: Giving out device to module zynqmp-ocm-edac controller zynqmp_ocm: DEV ff960000.memory-controller (INTERRUPT)
            [    3.130636] sdhci: Secure Digital Host Controller Interface driver
            [    3.136490] sdhci: Copyright(c) Pierre Ossman
            [    3.140811] sdhci-pltfm: SDHCI platform and OF driver helper
            [    3.146774] ledtrig-cpu: registered to indicate activity on CPUs
            [    3.152419] SMCCC: SOC_ID: ARCH_SOC_ID not implemented, skipping ....
            [    3.158839] zynqmp_firmware_probe Platform Management API v1.1
            [    3.164601] zynqmp_firmware_probe Trustzone version v1.0
            [    3.210464] zynqmp-pinctrl firmware:zynqmp-firmware:pinctrl: zynqmp pinctrl initialized
            [    3.261518] zynqmp-aes firmware:zynqmp-firmware:zynqmp-aes: will run requests pump with realtime priority
            [    3.276577] alg: No test for xilinx-keccak-384 (zynqmp-keccak-384)
            [    3.277249] alg: No test for xilinx-zynqmp-rsa (zynqmp-rsa)
            [    3.282776] usbcore: registered new interface driver usbhid
            [    3.288183] usbhid: USB HID core driver
            [    3.298771] axi_sysid 85000000.axi-sysid-0: AXI System ID core version (1.01.a) found
            [    3.301131] axi_sysid 85000000.axi-sysid-0: [(null)] on [adrv9009zu11eg] git branch <hdl_2021_r1> git <6a6c5acc8ec422c068c7787cdeb5b0ee4C
            [    3.317071] fpga_manager fpga0: Xilinx ZynqMP FPGA Manager registered
            [    3.323424] usbcore: registered new interface driver snd-usb-audio
            [    3.330825] pktgen: Packet Generator for packet performance testing. Version: 2.75
            [    3.337115] Initializing XFRM netlink socket
            [    3.340999] NET: Registered protocol family 10
            [    3.345682] Segment Routing with IPv6
            [    3.349090] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
            [    3.355144] NET: Registered protocol family 17
            [    3.359259] NET: Registered protocol family 15
            [    3.363753] can: controller area network core
            [    3.368008] NET: Registered protocol family 29
            [    3.372404] can: raw protocol
            [    3.375339] can: broadcast manager protocol
            [    3.379496] can: netlink gateway - max_hops=1
            [    3.383882] Bluetooth: RFCOMM TTY layer initialized
            [    3.388667] Bluetooth: RFCOMM socket layer initialized
            [    3.393776] Bluetooth: RFCOMM ver 1.11
            [    3.397485] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
            [    3.402758] Bluetooth: BNEP filters: protocol multicast
            [    3.407950] Bluetooth: BNEP socket layer initialized
            [    3.412878] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
            [    3.418763] Bluetooth: HIDP socket layer initialized
            [    3.423797] 9pnet: Installing 9P2000 support
            [    3.427940] NET: Registered protocol family 36
            [    3.432354] Key type dns_resolver registered
            [    3.436762] registered taskstats version 1
            [    3.440652] Loading compiled-in X.509 certificates
            [    3.445743] Btrfs loaded, crc32c=crc32c-generic
            [    3.457843] ff010000.serial: ttyPS0 at MMIO 0xff010000 (irq = 31, base_baud = 6249999) is a xuartps
            [    3.466866] printk: console [ttyPS0] enabled
            [    3.466866] printk: console [ttyPS0] enabled
            [    3.471160] printk: bootconsole [cdns0] disabled
            [    3.471160] printk: bootconsole [cdns0] disabled
            [    3.480447] of-fpga-region fpga-full: FPGA Region probed
            [    3.490483] gpio-13 (ulpi-phy-reset): hogged as output/high
            [    3.497715] xilinx-zynqmp-dpdma fd4c0000.dma-controller: Xilinx DPDMA engine is probed
            [    3.506449] zynqmp-display fd4a0000.display: vtc bridge property not present
            [    3.515394] xilinx-dp-snd-codec fd4a0000.display:zynqmp_dp_snd_codec0: Failed to get required clock freq
            [    3.524898] xilinx-dp-snd-codec: probe of fd4a0000.display:zynqmp_dp_snd_codec0 failed with error -22
            [    3.535124] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm0: Xilinx DisplayPort Sound PCM probed
            [    3.543954] xilinx-dp-snd-pcm zynqmp_dp_snd_pcm1: Xilinx DisplayPort Sound PCM probed
            [    3.552860] OF: graph: no port node found in /axi/display@fd4a0000
            [    3.559244] xlnx-drm xlnx-drm.0: bound fd4a0000.display (ops 0xffffffc010ffd810)
            [    4.644438] zynqmp-display fd4a0000.display: [drm] Cannot find any crtc or sizes
            [    4.652071] [drm] Initialized xlnx 1.0.0 20130509 for fd4a0000.display on minor 0
            [    4.659562] zynqmp-display fd4a0000.display: ZynqMP DisplayPort Subsystem driver probed
            [    4.668777] adrv9009 spi1.0: adrv9009_probe : enter
            [    4.674594] adrv9009 spi1.1: adrv9009_probe : enter
            [    4.760470] hmc7044 spi1.3: PLL1: Locked, CLKIN3 @ 38400000 Hz, PFD: 7680 kHz - PLL2: Locked @ 2949.120000 MHz
            [    4.770830] jesd204: /axi/spi@ff040000/hmc7044-car@3,jesd204:3,parent=spi1.3: Using as SYSREF provider
            [    4.780817] hmc7044 spi1.4: Read/Write check failed (0xFF)
            [    4.833539] hmc7044 spi1.4: Probed, SPI read support failed
            [    4.840132] spi-nor spi0.0: SPI-NOR-UniqueID 104000a87704000209002100f73e717c69
            [    4.847824] random: fast init done
            [    4.851386] spi-nor spi0.0: trying to lock already unlocked area
            [    4.857388] spi-nor spi0.0: n25q512a (131072 Kbytes)
            [    4.862362] 4 fixed-partitions partitions found on MTD device spi0.0
            [    4.868706] Creating 4 MTD partitions on "spi0.0":
            [    4.873488] 0x000000000000-0x000002000000 : "qspi-fsbl-uboot"
            [    4.879931] 0x000002000000-0x000002020000 : "qspi-uboot-env"
            [    4.886199] 0x000002020000-0x000002100000 : "qspi-nvmfs"
            [    4.892115] 0x000002100000-0x000007f00000 : "qspi-linux"
            [    4.899871] macb ff0e0000.ethernet: Not enabling partial store and forward
            [    4.907400] libphy: MACB_mii_bus: probed
            [    4.913221] macb ff0e0000.ethernet eth0: Cadence GEM rev 0x50070106 at 0xff0e0000 irq 21 (00:e0:22:fe:0b:d6)
            [    4.923467] xilinx-axipmon ffa00000.perf-monitor: Probed Xilinx APM
            [    4.930029] xilinx-axipmon fd0b0000.perf-monitor: Probed Xilinx APM
            [    4.936559] xilinx-axipmon fd490000.perf-monitor: Probed Xilinx APM
            [    4.943067] xilinx-axipmon ffa10000.perf-monitor: Probed Xilinx APM
            [    4.951512] OF: graph: no port node found in /axi/phy@fd400000
            [    5.053782] at24 0-002c: supply vcc not found, using dummy regulator
            [    5.060764] at24 0-002c: 2048 byte 24c16 EEPROM, writable, 1 bytes/write
            [    5.067510] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 23
            [    5.075102] i2c i2c-1: Added multiplexed i2c bus 3
            [    5.569318] i2c i2c-1: Added multiplexed i2c bus 4
            [    5.574255] i2c i2c-1: Added multiplexed i2c bus 5
            [    5.579276] at24 6-0050: supply vcc not found, using dummy regulator
            [    5.615141] i2c i2c-1: Added multiplexed i2c bus 6
            [    5.620155] at24 7-0050: supply vcc not found, using dummy regulator
            [    5.654316] i2c i2c-1: Added multiplexed i2c bus 7
            [    5.659324] at24 8-0050: supply vcc not found, using dummy regulator
            [    5.695115] i2c i2c-1: Added multiplexed i2c bus 8
            [    5.700043] i2c i2c-1: Added multiplexed i2c bus 9
            [    5.704968] i2c i2c-1: Added multiplexed i2c bus 10
            [    5.709847] pca954x 1-0070: registered 8 multiplexed busses for I2C switch pca9548
            [    5.717454] cdns-i2c ff030000.i2c: 400 kHz mmio ff030000 irq 24
            [    5.724248] cdns-wdt fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 60s
            [    5.731852] cpu cpu0: dev_pm_opp_set_rate: failed to find current OPP for freq 1316666653 (-34)
            [    5.740593] cpufreq: cpufreq_online: CPU0: Running at unlisted initial frequency: 1316666 KHz, changing to: 1199999 KHz
            [    5.751385] cpu cpu0: dev_pm_opp_set_rate: failed to find current OPP for freq 1316666653 (-34)
            [    5.761590] zynqmp-display fd4a0000.display: [drm] Cannot find any crtc or sizes
            [    5.771554] axi-i2s 82000000.axi-i2s-adi: probed, capture enabled, playback enabled
            [    5.779704] adrv9009 spi1.0: adrv9009_probe : enter
            [    5.785338] adrv9009 spi1.1: adrv9009_probe : enter
            [    5.794144] mmc0: SDHCI controller on ff170000.mmc [ff170000.mmc] using ADMA 64-bit
            [    5.838432] hmc7044 spi1.2: PLL1: Locked, CLKIN1 @ 30720000 Hz, PFD: 30720 kHz - PLL2: Locked @ 2949.120000 MHz
            [    5.849324] macb ff0b0000.ethernet: Not enabling partial store and forward
            [    5.859757] mmc0: new high speed SDHC card at address 0001
            [    5.865588] mmcblk0: mmc0:0001 SD16G 14.6 GiB
            [    5.871588] libphy: MACB_mii_bus: probed
            [    5.875571] macb ff0b0000.ethernet eth1: Cadence GEM rev 0x50070106 at 0xff0b0000 irq 20 (c6:bd:2a:d9:e2:01)
            [    5.887653]  mmcblk0: p1 p2 p3
            [    5.891736] axi_adxcvr 84a40000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.05.a) using CPLL on GTH4 at 0x84A40000. Number of lanes: 4.
            [    5.905263] axi_adxcvr 84a60000.axi-adxcvr-rx-os: AXI-ADXCVR-RX (17.05.a) using CPLL on GTH4 at 0x84A60000. Number of lanes: 4.
            [    5.917738] axi_adxcvr 84a20000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.05.a) using QPLL on GTH4 at 0x84A20000. Number of lanes: 8.
            [    5.929482] axi-jesd204-rx 84a50000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0x84A50000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fs.
            [    5.942407] axi-jesd204-rx 84a70000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0x84A70000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fs.
            [    5.955219] axi-jesd204-tx 84a30000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0x84A30000. Encoder 8b10b, width 4/4, lanes 8, jesd204-fs.
            [    5.972920] adrv9009 spi1.0: adrv9009_probe : enter
            [    5.983087] adrv9009 spi1.1: adrv9009_probe : enter
            [    6.014044] cf_axi_adc 84a00000.axi-adrv9009-rx-hpc: ADI AIM (10.01.b) at 0x84A00000 mapped to 0x(____ptrval____), probed ADC ADRV9009-XR
            [    6.045146] cf_axi_dds 84a04000.axi-adrv9009-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x84A04000 mapped to 0x(____ptrval2
            [    6.059953] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition initialized -> probed
            [    6.071171] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition initialized -> probed
            [    6.082381] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition initialized -> probed
            [    6.093608] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition probed -> idle
            [    6.104214] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition probed -> idle
            [    6.114829] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition probed -> idle
            [    6.125442] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition idle -> device_init
            [    6.136484] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition idle -> device_init
            [    6.147523] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition idle -> device_init
            [    6.158566] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> link_init
            [    6.170044] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition device_init -> link_init
            [    6.181515] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> link_init
            [    6.193005] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> link_supported
            [    6.204735] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition link_init -> link_supported
            [    6.216469] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> link_supported
            [    6.228926] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_pre_setup
            [    6.241098] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition link_supported -> link_pre_setup
            [    6.253263] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_pre_setup
            [    6.309896] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> clk_sync_stage1
            [    6.322153] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition link_pre_setup -> clk_sync_stage1
            [    6.334408] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> clk_sync_stage1
            [    6.356435] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> clk_sync_stage2
            [    6.368780] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition clk_sync_stage1 -> clk_sync_stage2
            [    6.381121] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> clk_sync_stage2
            [    6.393546] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage3
            [    6.405887] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition clk_sync_stage2 -> clk_sync_stage3
            [    6.418228] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage3
            [    6.430573] jesd204: /fpga-axi@0/axi-jesd204-rx@84a50000,jesd204:5,parent=84a50000.axi-jesd204-rx: Possible instantiation for multiple c2
            [    6.445780] jesd204: /fpga-axi@0/axi-jesd204-rx@84a70000,jesd204:7,parent=84a70000.axi-jesd204-rx: Possible instantiation for multiple c2
            [    6.460988] jesd204: /fpga-axi@0/axi-jesd204-tx@84a30000,jesd204:9,parent=84a30000.axi-jesd204-tx: Possible instantiation for multiple c4
            [    6.478205] adrv9009 spi1.1: ADIHAL_resetHw
            [    6.807922] adrv9009 spi1.0: ADIHAL_resetHw
            [    7.137699] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> link_setup
            [    7.149606] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition clk_sync_stage3 -> link_setup
            [    7.161513] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> link_setup
            [    7.173585] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> opt_setup_stage1
            [    7.185576] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition link_setup -> opt_setup_stage1
            [    7.197571] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> opt_setup_stage1
            [    7.302940] random: crng init done
            [   11.155203] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> opt_setup_sta2
            [   11.167722] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition opt_setup_stage1 -> opt_setup_sta2
            [   11.180234] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> opt_setup_sta2
            [   11.192954] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_sta3
            [   11.205468] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition opt_setup_stage2 -> opt_setup_sta3
            [   11.217981] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_sta3
            [   11.230697] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_sta4
            [   11.243215] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition opt_setup_stage3 -> opt_setup_sta4
            [   11.255731] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_sta4
            [   16.470043] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_sta5
            [   16.482562] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition opt_setup_stage4 -> opt_setup_sta5
            [   16.495075] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_sta5
            [   16.508137] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> clocks_enable
            [   16.520399] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition opt_setup_stage5 -> clocks_enable
            [   16.532650] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> clocks_enable
            [   16.550135] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> link_enable
            [   16.561954] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition clocks_enable -> link_enable
            [   16.573775] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> link_enable
            [   16.620711] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> link_running
            [   16.632446] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition link_enable -> link_running
            [   16.644179] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> link_running
            [   16.757453] adrv9009 spi1.1: adrv9009_info: adrv9009 Rev 192, Firmware 6.2.1 API version: 3.6.2.1 successfully initialized via jesd204-fm
            [   16.871422] adrv9009 spi1.0: adrv9009_info: adrv9009-x2 Rev 192, Firmware 6.2.1 API version: 3.6.2.1 successfully initialized via jesd20m
            [   16.884116] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_running -> opt_post_running_e
            [   16.896803] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:1] transition link_running -> opt_post_running_e
            [   16.909492] jesd204: /axi/spi@ff040000/adrv9009-phy@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_running -> opt_post_running_e
            [   16.925576] input: gpio_keys as /devices/platform/gpio_keys/input/input0
            [   16.932512] of_cfs_init
            [   16.934968] of_cfs_init: OK
            [   16.937966] cfg80211: Loading compiled-in X.509 certificates for regulatory database
            [   17.061586] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
            [   17.068114] clk: Not disabling unused clocks
            [   17.072633] ALSA device list:
            [   17.075591]   #0: ADRV9009 ZU11EG ADAU1761
            [   17.079945] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
            [   17.088553] cfg80211: failed to load regulatory.db
            [   17.944935] EXT4-fs (mmcblk0p2): recovery complete
            [   17.953394] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
            [   17.961514] VFS: Mounted root (ext4 filesystem) on device 179:2.
            [   17.975849] devtmpfs: mounted
            [   17.979570] Freeing unused kernel memory: 2496K
            [   17.984188] Run /sbin/init as init process
            [   18.494456] systemd[1]: System time before build time, advancing clock.
            [   18.533602] systemd[1]: systemd 247.3-7+rpi1 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRY)
            [   18.556807] systemd[1]: Detected architecture arm64.

            Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

            [   18.581954] systemd[1]: Set hostname to <analog>.
            [   19.969929] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disab.
            [   20.190835] systemd[1]: Queued start job for default target Graphical Interface.
            [   20.199479] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
            [   20.211857] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
            [   20.220887] systemd[1]: Created slice system-getty.slice.
            [  OK  ] Created slice system-getty.slice.
            [   20.240857] systemd[1]: Created slice system-modprobe.slice.
            [  OK  ] Created slice system-modprobe.slice.
            [   20.260796] systemd[1]: Created slice system-serial\x2dgetty.slice.
            [  OK  ] Created slice system-serial\x2dgetty.slice.
            [   20.284787] systemd[1]: Created slice system-systemd\x2dfsck.slice.
            [  OK  ] Created slice system-systemd\x2dfsck.slice.
            [   20.308673] systemd[1]: Created slice User and Session Slice.
            [  OK  ] Created slice User and Session Slice.
            [   20.328694] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
            [  OK  ] Started Forward Password R�…uests to Wall Directory Watch.
            [   20.352710] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
            [   20.365061] systemd[1]: Reached target Slices.
            [  OK  ] Reached target Slices.
            [   20.380579] systemd[1]: Reached target Swap.
            [  OK  ] Reached target Swap.
            [   20.397194] systemd[1]: Listening on Syslog Socket.
            [  OK  ] Listening on Syslog Socket.
            [   20.412791] systemd[1]: Listening on fsck to fsckd communication Socket.
            [  OK  ] Listening on fsck to fsckd communication Socket.
            [   20.436648] systemd[1]: Listening on initctl Compatibility Named Pipe.
            [  OK  ] Listening on initctl Compatibility Named Pipe.
            [   20.461108] systemd[1]: Listening on Journal Audit Socket.
            [  OK  ] Listening on Journal Audit Socket.
            [   20.480793] systemd[1]: Listening on Journal Socket (/dev/log).
            [  OK  ] Listening on Journal Socket (/dev/log).
            [   20.504852] systemd[1]: Listening on Journal Socket.
            [  OK  ] Listening on Journal Socket.
            [   20.522281] systemd[1]: Listening on udev Control Socket.
            [  OK  ] Listening on udev Control Socket.
            [   20.544788] systemd[1]: Listening on udev Kernel Socket.
            [  OK  ] Listening on udev Kernel Socket.
            [   20.566278] systemd[1]: Mounting Huge Pages File System...
                     Mounting Huge Pages File System...
            [   20.582131] systemd[1]: Mounting POSIX Message Queue File System...
                     Mounting POSIX Message Queue File System...
            [   20.605935] systemd[1]: Mounting RPC Pipe File System...
                     Mounting RPC Pipe File System...
            [   20.622162] systemd[1]: Mounting Kernel Debug File System...
                     Mounting Kernel Debug File System...
            [   20.636917] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
            [   20.645539] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
            [   20.658448] systemd[1]: Starting Restore / save the current clock...
                     Starting Restore / save the current clock...
            [   20.687824] systemd[1]: Starting Set the console keyboard layout...
                     Starting Set the console keyboard layout...
            [   20.710146] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
            [   20.723451] systemd[1]: Starting Load Kernel Module configfs...
                     Starting Load Kernel Module configfs...
            [   20.742522] systemd[1]: Starting Load Kernel Module drm...
                     Starting Load Kernel Module drm...
            [   20.762848] systemd[1]: Starting Load Kernel Module fuse...
                     Starting Load Kernel Module fuse...
            [   20.788151] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
            [   20.797422] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
            [   20.808264] systemd[1]: Starting Journal Service...
                     Starting Journal Service...
            [   20.829135] systemd[1]: Starting Load Kernel Modules...
                     Starting Load Kernel Modules...
            [   20.846420] systemd[1]: Starting Remount Root and Kernel File Systems...
                     Starting Remount Root and Kernel File Systems...
            [   20.870354] systemd[1]: Starting Coldplug All udev Devices...
                     Starting Coldplug All udev Devices...
            [   20.893271] systemd[1]: Mounted Huge Pages File System.
            [  OK  ] Mounted Huge Pages File System.
            [   20.918303] systemd[1]: Mounted POSIX Message Queue File System.
            [  OK  ] Mounted POSIX Message Queue File System.
            [   20.940989] systemd[1]: Mounted RPC Pipe File System.
            [  OK  ] Mounted RPC Pipe File System.
            [   20.956993] systemd[1]: Mounted Kernel Debug File System.
            [  OK  ] Mounted Kernel Debug File System.
            [   20.977388] systemd[1]: Finished Restore / save the current clock.
            [  OK  ] Finished Restore / save the current clock.
            [   21.001586] systemd[1]: Finished Set the console keyboard layout.
            [  OK  ] Finished Set the console keyboard layout.
            [   21.027051] systemd[1]: Started Journal Service.
            [  OK  ] Started Journal Service.
            [  OK  ] Finished Load Kernel Module configfs.
            [  OK  ] Finished Load Kernel Module drm.
            [  OK  ] Finished Load Kernel Module fuse.
            [FAILED] Failed to start Load Kernel Modules.
            See 'systemctl status systemd-modules-load.service' for details.
                     Mounting FUSE Control File System...
                     Mounting Kernel Configuration File System...
                     Starting Apply Kernel Variables...
            [  OK  ] Mounted FUSE Control File System.
            [  OK  ] Mounted Kernel Configuration File System.
            [  OK  ] Finished Apply Kernel Variables.
            [  OK  ] Finished Coldplug All udev Devices.
                     Starting Helper to synchronize boot up for ifupdown...
                     Starting Wait for udev To �…plete Device Initialization...
            [  OK  ] Finished Helper to synchronize boot up for ifupdown.
            [  OK  ] Finished Remount Root and Kernel File Systems.
                     Starting Flush Journal to Persistent Storage...
                     Starting Load/Save Random Seed...
                     Starting Create System Users...
            [  OK  ] Finished Create System Users.
            [  OK  ] Finished Load/Save Random Seed.
                     Starting Create Static Device Nodes in /dev...
            [  OK  ] Finished Create Static Device Nodes in /dev.
            [  OK  ] Reached target Local File Systems (Pre).
                     Starting Rule-based Manage�…for Device Events and Files...
            [  OK  ] Finished Flush Journal to Persistent Storage.
            [  OK  ] Started Rule-based Manager for Device Events and Files.
                     Starting Show Plymouth Boot Screen...
            [  OK  ] Started Show Plymouth Boot Screen.
            [  OK  ] Started Forward Password R�…s to Plymouth Directory Watch.
            [  OK  ] Reached target Local Encrypted Volumes.
            [  OK  ] Found device /dev/ttyPS0.
            [  OK  ] Found device /dev/disk/by-partuuid/ce8c84ab-01.
            [  OK  ] Found device /dev/ttyS0.
            [  OK  ] Reached target Hardware activated USB gadget.
            [  OK  ] Listening on Load/Save RF �…itch Status /dev/rfkill Watch.
                     Starting File System Check�…isk/by-partuuid/ce8c84ab-01...
                     Starting Load Kernel Modules...
            [FAILED] Failed to start Load Kernel Modules.
            See 'systemctl status systemd-modules-load.service' for details.
            [  OK  ] Finished Wait for udev To Complete Device Initialization.
            [  OK  ] Finished File System Check�…/disk/by-partuuid/ce8c84ab-01.
                     Mounting /boot...
            [  OK  ] Started File System Check Daemon to report status.
                     Starting Load Kernel Modules...
            [  OK  ] Mounted /boot.
            [  OK  ] Reached target Local File Systems.
                     Starting Set console font and keymap...
                     Starting Preprocess NFS configuration...
                     Starting Tell Plymouth To Write Out Runtime Data...
                     Starting Create Volatile Files and Directories...
            [  OK  ] Finished Set console font and keymap.
            [  OK  ] Finished Preprocess NFS configuration.
            [FAILED] Failed to start Load Kernel Modules.
            See 'systemctl status systemd-modules-load.service' for details.
            [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
                     Starting Raise network interfaces...
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
            [  OK  ] Started Periodic ext4 Onli�…ata Check for All Filesystems.
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
            [  OK  ] Listening on GPS (Global P�…ioning System) Daemon Sockets.
            [  OK  ] Listening on triggerhappy.socket.
            [  OK  ] Reached target Sockets.
            [  OK  ] Reached target Basic System.
                     Starting Save/Restore Sound Card State...
                     Starting Avahi mDNS/DNS-SD Stack...
            [  OK  ] Started Regular background program processing daemon.
            [  OK  ] Started D-Bus System Message Bus.
                     Starting dphys-swapfile - �…unt, and delete a swap file...
                     Starting Remove Stale Onli�…t4 Metadata Check Snapshots...
                     Starting Creating IIOD Context Attributes......
                     Starting Authorization Manager...
                     Starting DHCP Client Daemon...
                     Starting LSB: Switch to on�…nless shift key is pressed)...
                     Starting LSB: rng-tools (Debian variant)...
                     Starting System Logging Service...
                     Starting User Login Management...
                     Starting triggerhappy global hotkey daemon...
                     Starting Disk Manager...
                     Starting WPA supplicant...
            [  OK  ] Finished Save/Restore Sound Card State.
            [  OK  ] Reached target Sound Card.
            [  OK  ] Finished Remove Stale Onli�…ext4 Metadata Check Snapshots.
            [  OK  ] Started triggerhappy global hotkey daemon.
            [  OK  ] Started DHCP Client Daemon.
            [  OK  ] Finished Raise network interfaces.
            [  OK  ] Finished dphys-swapfile - �…mount, and delete a swap file.
            [  OK  ] Started LSB: rng-tools (Debian variant).
            [  OK  ] Started System Logging Service.
            [  OK  ] Started User Login Management.
            [  OK  ] Started Avahi mDNS/DNS-SD Stack.
            [  OK  ] Started WPA supplicant.
            [  OK  ] Reached target Network.
            [  OK  ] Reached target Network is Online.
                     Starting CUPS Scheduler...
            [  OK  ] Started Erlang Port Mapper Daemon.
                     Starting Load USB gadget scheme...
                     Starting HTTP based time synchronization tool...
                     Starting Internet superserver...
                     Starting /etc/rc.local Compatibility...
                     Starting OpenBSD Secure Shell server...
                     Starting Permit User Sessions...
            [  OK  ] Started Unattended Upgrades Shutdown.
            [  OK  ] Started /etc/rc.local Compatibility.
            [  OK  ] Finished Permit User Sessions.
                     Starting Light Display Manager...
                     Starting Hold until boot process finishes up...
            [  OK  ] Started Authorization Manager.
                     Starting Modem Manager...
            [  OK  ] Started HTTP based time synchronization tool.
            [  OK  ] Started Internet superserver.
            [  OK  ] Finished Load USB gadget scheme.
                     Mounting Mount FunctionFS instance...
            [  OK  ] Found device /dev/ttyGS0.
            [  OK  ] Mounted Mount FunctionFS instance.
            [  OK  ] Finished Creating IIOD Context Attributes....
            [  OK  ] Started IIO Daemon.
                     Starting IIO Daemon with USB FFS support...
                     Stopping IIO Daemon...
            [  OK  ] Stopped IIO Daemon.
            [  OK  ] Started IIO Daemon with USB FFS support.
                     Starting Start USB gadget scheme...
            [  OK  ] Started OpenBSD Secure Shell server.
            [  OK  ] Started LSB: Switch to ond�…(unless shift key is pressed).

            Raspbian GNU/Linux 11 analog ttyPS0

            analog login: root (automatic login)

            Linux analog 5.10.0-98248-g1bbe32fa5182 #1143 SMP Wed Aug 3 18:38:55 IST 2022 aarch64

            The programs included with the Debian GNU/Linux system are free software;
            the exact distribution terms for each program are described in the
            individual files in /usr/share/doc/*/copyright.

            Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
            permitted by applicable law.
            Last login: Wed Aug 17 12:17:14 BST 2022 on ttyPS0
            root@analog:~#

Make sure all devices are present
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: box bggreen

   This specifies any shell prompt running on the target

   ::

      root@analog:~# iio_info | grep iio:device
              iio:device0: ams
              iio:device1: hmc7044-car
              iio:device2: adm1177
              iio:device3: hmc7044
              iio:device4: adrv9009-phy
              iio:device5: adrv9009-phy-b
              iio:device6: axi-adrv9009-rx-obs-hpc (buffer capable)
              iio:device7: axi-adrv9009-tx-hpc (buffer capable)
              iio:device8: axi-adrv9009-rx-hpc (buffer capable)

Check clock chip lock status (SoM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `iio_attr <https://wiki.analog.com/resources/tools-software/linux-software/libiio/iio_attr>`_
-  `HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/hmc7044>`_

.. container:: box bggreen

   This specifies any shell prompt running on the target

   ::

      root@analog:~# iio_attr -q -D hmc7044 status
      --- PLL1 ---
      Status: Locked
      Using:  CLKIN1 @ 122880000 Hz
      PFD:    7680 kHz
      --- PLL2 ---
      Status: Locked (Unsynchronized)
      Frequency:      2949120000 Hz
      SYSREF Status:  Valid & Locked
      SYNC Status:    Unsynchronized
      Lock Status:    PLL1 & PLL2 Locked
      root@analog:~#

Check clock chip lock status (Carrier)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `iio_attr <https://wiki.analog.com/resources/tools-software/linux-software/libiio/iio_attr>`_
-  `HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/hmc7044>`_

.. container:: box bggreen

   This specifies any shell prompt running on the target

   ::

      root@analog:~# iio_attr -q -D hmc7044-car status
      --- PLL1 ---
      Status: Locked
      Using:  CLKIN3 @ 19200000 Hz
      PFD:    3840 kHz
      --- PLL2 ---
      Status: Locked (Unsynchronized)
      Frequency:      2949120000 Hz
      SYSREF Status:  Invalid
      SYNC Status:    Unsynchronized
      Lock Status:    PLL1 & PLL2 Locked
      root@analog:~#

Check JESD204B Link Status
~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the `JESD204B Status Utility <https://wiki.analog.com/resources/tools-software/linux-software/jesd_status>`_

.. container:: box bggreen

   This specifies any shell prompt running on the target

   ::

      root@analog:~# TERM=vt100 jesd_status -s

        (DEVICES) Found 3 JESD204 Link Layer peripherals

        (0): 84a30000.axi-jesd204-tx
        (1): 84a50000.axi-jesd204-rx
        (2): 84a70000.axi-jesd204-rx

        (STATUS)               (0)          (1)        (2)
        Link is                 enabled      enabled    enabled
        Link Status             DATA         DATA       DATA
        Measured Link Clock     122.881      245.761    122.881
        Reported Link Clock     122.880      245.760    122.880
        Lane rate               4915.200     9830.400   4915.200
        Lane rate / 40          122.880      245.760    122.880
        LMFC rate               7.680        7.680      3.840
        SYSREF captured         Yes          Yes        Yes
        SYSREF alignment error  No           No         No
        SYNC~                   deasserted

        (LANE STATUS)                   (1)                          (2)
        Lane#                             0      1      2      3       0      1      2      3
        Errors                            0      0      0      0       0      0      0      0
        Latency (Multiframes/Octets)      2/80   2/77   2/78   2/80    2/50   2/50   2/49   2/51
        CGS State                         DATA   DATA   DATA   DATA    DATA   DATA   DATA   DATA
        Initial Frame Sync                Yes    Yes    Yes    Yes     Yes    Yes    Yes    Yes
        Initial Lane Alignment Sequence   Yes    Yes    Yes    Yes     Yes    Yes    Yes    Yes

Video Configuration
-------------------

The default configuration for most of the projects is to use the HDMI output, but for this project the DisplayPort is used. In order for it to work, you should follow the steps described here: `DisplayPort No Picture <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`_ After following the steps, the board should be rebooted.

IIO Oscilloscope Remote
-----------------------

Please see also here:`Oscilloscope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_

The IIO Oscilloscope application can be used to connect to another platform that
has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP
address of the target in the popup window.

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``

   |image1|

.. |image1| image:: ../images/shutdown.png
   :width: 300
