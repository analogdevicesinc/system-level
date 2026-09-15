.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/versal

.. _ad9081_fmca_ebz quickstart versal:

AD9081/AD9082 Versal ACAP VCK190 Quick Start Guide
==================================================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/hwsetup_vck190_ad9081.jpg
   :width: 600px

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the :adi:`AD9081-FMCA-EBZ`/:adi:`AD9082-FMCA-EBZ`
on :xilinx:`VCK190 <VCK190>` board.

Instructions on how to build the ZynqMP / MPSoC / Versal ACAP Linux kernel and
devicetrees from source can be found here:

- :dokuwiki:`Building the ZynqMP / MPSoC Linux kernel and devicetrees from source </resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp>`
- :dokuwiki:`How to build the ZynqMP boot image BOOT.BIN </resources/tools-software/linux-software/build-the-zynqmp-boot-image>`

Required Software
-----------------

- SD Card image using the instructions here: :ref:`kuiper`.
- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).
- System controller image
- :xilinx:`member/forms/download/design-license-xef.html?filename=sc2.2_01.img.zip <member/forms/download/design-license-xef.html?filename=sc2.2_01.img.zip>`

Required Hardware
-----------------

- Xilinx :xilinx:`VCK190 <VCK190>`
- AD9081-FMCA-EBZ/AD9082-FMCA-EBZ FMC board.
- USB type-C cable
- Ethernet cables
- Optionally USB keyboard mouse and a Display Port compatible monitor

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl.rst

   :start-after: .. start-#board-setup
   :end-before: .. end-#board-setup

Example Device Trees
--------------------

AD9081-FMCA-EBZ / AD9082-FMCA-EBZ on VCK190 (Versal ACAP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Function
     - File
     -
   * - dts
     - :git-linux:`versal-vck190-reva-ad9081.dts <master:arch/arm64/boot/dts/xilinx/versal-vck190-reva-ad9081.dts>`
     -
   * - dts
     - :git-linux:`versal-vck190-reva-ad9081-204c-txmode22-rxmode23.dts <master:arch/arm64/boot/dts/xilinx/versal-vck190-reva-ad9081-204c-txmode22-rxmode23.dts>`
     -
   * - dts
     - :git-linux:`versal-vck190-reva-ad9082-204c-txmode22-rxmode23.dts <master:arch/arm64/boot/dts/xilinx/versal-vck190-reva-ad9082-204c-txmode22-rxmode23.dts>`
     -

Testing
-------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/vck190.jpg
   :width: 900px

- Connect the :adi:`AD9081-FMCA-EBZ` FMC board to the FPGA carrier FMC+ FMCP1
  socket.
- Connect USB UART J207 (Type-C USB) to your host PC.
- Insert Versal SD card into socket J302.
- Insert System Controller SD card into socket J206.
- Configure ACAP for SD BOOT (mode SW1[4:1] switch in the position
  OFF,OFF,OFF,ON as seen in the below picture).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/vck190_sw1.jpg
   :width: 200px

- Configure System Controller for SD BOOT (mode SW11[4:1] switch in the position
  OFF,OFF,OFF,ON as seen in the below picture).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/vck190_sw11.jpg
   :width: 200px

- Connect an Ethernet cable to J307 and also to SYSCTL Ethernet port to access
  Board Evaluation & Management Tool (BEAM).
- Turn on the power switch on the FPGA board.
- Observe kernel and serial console messages on your terminal, both the ACAP
  UART interface and the System controller. (use the first ttyUSB or COM port
  registered for the ACAP UART interface, and try the other 2 to find the one
  for System Controller)
- On the System Controller console, a BEAM Tool Web Address should be assigned.
  Go to this web address to set VADJ_FMC to 1.5V.
- To change VADJ_FMC On BEAM, click "Test The Board">"Board Settings">"FMC".
  Then on "Set VADJ_FMC", select 1.5V and click "Set", ad9081 LEDs should turn
  on immediately.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/BEAM-home.jpg
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/BEAM-board-settings.jpg
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/BEAM-set-vadj.jpg
   :width: 600px

- On the ACAP UART interface console, reboot the system. After reboot, ad9081
  devices should be present.

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

ACAP SDcard boot files
~~~~~~~~~~~~~~~~~~~~~~

The files that need to be present on the sdcard ``BOOT`` partition are:

- ``BOOT.BIN``
- ``Image``
- ``system.dtb``
- ``boot.scr``

Copy the ``BOOT.BIN``, ``boot.scr`` and ``system.dtb`` from the
``versal-vck190-reva-ad9081`` directory. Copy the ``Image`` from the
``versal-common`` directory.

.. important::

   On windows machines make sure the copy process did not encrypted the files.

Setting up UART
~~~~~~~~~~~~~~~

When setting up the UART make sure you connect to the ACAP UART interface and
not the System controller.

Boot messages
~~~~~~~~~~~~~

The **latest master** pre-built Image based boot messages looks like the
followings :

<hidden Complete kernel boot log (Click to expand)> ::

   [0.015]****************************************
   [0.071]Xilinx Versal Platform Loader and Manager
   [0.129]Release 2021.2   Oct 20 2022  -  23:01:07
   [0.189]Platform Version: v2.0 PMC: v2.0, PS: v2.0
   [0.255]BOOTMODE: 0xE, MULTIBOOT: 0xF0000000
   [0.314]****************************************
   [0.522]Non Secure Boot
   [3.744]PLM Initialization Time
   [3.794]***********Boot PDI Load: Started***********
   [3.857]Loading PDI from SD1_LS
   [3.907]Monolithic/Master Device
   [318.960]315.075 ms: PDI initialization time
   [319.022]+++Loading Image#: 0x1, Name: lpd, Id: 0x04210002
   [319.092]---Loading Partition#: 0x1, Id: 0xC
   [371.104] 51.922 ms for Partition#: 0x1, Size: 2416 Bytes
   [376.055]---Loading Partition#: 0x2, Id: 0xB
   [380.534] 0.523 ms for Partition#: 0x2, Size: 48 Bytes
   [384.767]---Loading Partition#: 0x3, Id: 0xB
   [398.853] 10.128 ms for Partition#: 0x3, Size: 61312 Bytes
   [401.183]---Loading Partition#: 0x4, Id: 0xB
   [407.107] 1.965 ms for Partition#: 0x4, Size: 5968 Bytes
   [410.070]---Loading Partition#: 0x5, Id: 0xB
   [414.041] 0.014 ms for Partition#: 0x5, Size: 80 Bytes
   [418.841]+++Loading Image#: 0x2, Name: pl_cfi, Id: 0x18700000
   [424.171]---Loading Partition#: 0x6, Id: 0x3
   [885.773] 457.641 ms for Partition#: 0x6, Size: 2439344 Bytes
   [888.362]---Loading Partition#: 0x7, Id: 0x5
   [998.686] 106.365 ms for Partition#: 0x7, Size: 518672 Bytes
   [1001.221]+++Loading Image#: 0x3, Name: fpd, Id: 0x0420C003
   [1006.403]---Loading Partition#: 0x8, Id: 0x8
   [1011.899] 1.450 ms for Partition#: 0x8, Size: 1104 Bytes
   [1015.758]+++Loading Image#: 0x4, Name: apu_subsystem, Id: 0x1C000000
   [1021.534]---Loading Partition#: 0x9, Id: 0x0
   [1033.735] 8.156 ms for Partition#: 0x9, Size: 47040 Bytes
   [1036.067]---Loading Partition#: 0xA, Id: 0x0
   [1222.180] 182.067 ms for Partition#: 0xA, Size: 1193936 Bytes
   NOT22E.  A]F r*nn**g**n otliDI Voasa DSil*con
   *****
   [1229.495]281.083 ms: ROM Time
   [1232.203]Total PLM Boot Time
   [R234. 4 BL31m iIpiDidpATc handlff:sErucr:renhtndfee 7P0
   eOeivE:
    B134: 66cuPLM Error Status: 0x0
   7O000E  BL31: Non secure code at 0x8000000
   NOTICE:  BL31: v2.6(release):xilinx-v2022.1-7-g38ee444bc
   NOTICE:  BL31: Built : 18:20:28, Sep  2 2022

   U-Boot 2021.01-33453-g5651667 (Sep 23 2021 - 12:12:45 +0100), Build: jenkins-development-build_uboot-6

   Model: Xilinx Versal vck190 Eval board revA
   DRAM:  8 GiB
   EL Level:   EL2
   MMC:   sdhci@f1050000: 0
   Loading Environment from FAT... *** Warning - bad CRC, using default environment

   In:    serial@ff000000
   Out:   serial@ff000000
   Err:   serial@ff000000
   Bootmode: LVL_SHFT_SD_MODE1
   Net:
   ZYNQ GEM: ff0c0000, mdio bus ff0c0000, phyaddr 1, interface rgmii-id

   Warning: ethernet@ff0c0000 (eth0) using random MAC address - da:ab:c5:e1:8a:0d
   eth0: ethernet@ff0c0000
   ZYNQ GEM: ff0d0000, mdio bus ff0c0000, phyaddr 2, interface rgmii-id

   Warning: ethernet@ff0d0000 (eth1) using random MAC address - 42:20:50:24:50:90
   , eth1: ethernet@ff0d0000
   Hit any key to stop autoboot:  5  4  3  2  1  0
   switch to partitions #0, OK
   mmc0 is current device
   Scanning mmc 0:1...
   Found U-Boot script /boot.scr
   210 bytes read in 20 ms (9.8 KiB/s)
   ## Executing script at 20000000
   Unknown command 'Load' - try 'help'
   32786944 bytes read in 2219 ms (14.1 MiB/s)
   31845 bytes read in 29 ms (1 MiB/s)
   ## Flattened Device Tree blob at 00001000
      Booting using the fdt blob at 0x001000
      Loading Device Tree to 000000007ded0000, end 000000007dedac64 ... OK

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd083]
   [    0.000000] Linux version 5.10.0-98699-gb2da1fe4a96a (jenkins@romlxbuild1) (aarch64-xilinx-linux-gcc.real (GCC) 10.2.0, GNU ld (GNU Binutils) 2.35.0.20200730) #639 SMP Fri Dec 16 07:44:47 EET 2022
   [    0.000000] Machine model: Xilinx Versal vck190 Eval board revA
   [    0.000000] earlycon: pl11 at MMIO32 0x00000000ff000000 (options '115200n8')
   [    0.000000] printk: bootconsole [pl11] enabled
   [    0.000000] efi: UEFI not found.
   [    0.000000] cma: Reserved 256 MiB at 0x000000006dc00000
   [    0.000000] Zone ranges:
   [    0.000000]   DMA      [mem 0x0000000000000000-0x000000003fffffff]
   [    0.000000]   DMA32    [mem 0x0000000040000000-0x00000000ffffffff]
   [    0.000000]   Normal   [mem 0x0000000100000000-0x000000097fffffff]
   [    0.000000] Movable zone start for each node
   [    0.000000] Early memory node ranges
   [    0.000000]   node   0: [mem 0x0000000000000000-0x000000007fffffff]
   [    0.000000]   node   0: [mem 0x0000000800000000-0x000000097fffffff]
   [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000097fffffff]
   [    0.000000] psci: probing for conduit method from DT.
   [    0.000000] psci: PSCIv1.1 detected in firmware.
   [    0.000000] psci: Using standard PSCI v0.2 function IDs
   [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
   [    0.000000] psci: SMC Calling Convention v1.2
   [    0.000000] percpu: Embedded 22 pages/cpu s49496 r8192 d32424 u90112
   [    0.000000] Detected PIPT I-cache on CPU0
   [    0.000000] CPU features: detected: GIC system register CPU interface
   [    0.000000] CPU features: detected: Spectre-v2
   [    0.000000] CPU features: detected: ARM errata 1165522, 1319367, or 1530923
   [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 2068480
   [    0.000000] Kernel command line: console=ttyAMA0 earlycon=pl011,mmio32,0xFF000000,115200n8 clk_ignore_unused root=/dev/mmcblk0p2 rw rootfstype=ext4 rootwait
   [    0.000000] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
   [    0.000000] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
   [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
   [    0.000000] software IO TLB: mapped [mem 0x000000003bfff000-0x000000003ffff000] (64MB)
   [    0.000000] Memory: 7883868K/8388608K available (16256K kernel code, 1746K rwdata, 11252K rodata, 2624K init, 890K bss, 242596K reserved, 262144K cma-reserved)
   [    0.000000] rcu: Hierarchical RCU implementation.
   [    0.000000] rcu:     RCU event tracing is enabled.
   [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
   [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
   [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
   [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
   [    0.000000] GICv3: GIC: Using split EOI/Deactivate mode
   [    0.000000] GICv3: 160 SPIs implemented
   [    0.000000] GICv3: 0 Extended SPIs implemented
   [    0.000000] GICv3: Distributor has no Range Selector support
   [    0.000000] GICv3: 16 PPIs implemented
   [    0.000000] GICv3: CPU0: found redistributor 0 region 0:0x00000000f9080000
   [    0.000000] ITS [mem 0xf9020000-0xf903ffff]
   [    0.000000] ITS@0x00000000f9020000: allocated 65536 Devices @800080000 (flat, esz 8, psz 64K, shr 0)
   [    0.000000] ITS: using cache flushing for cmd queue
   [    0.000000] GICv3: using LPI property table @0x0000000800030000
   [    0.000000] GIC: using cache flushing for LPI property table
   [    0.000000] GICv3: CPU0: using allocated LPI pending table @0x0000000800040000
   [    0.000000] ITS queue timeout (64 0)
   [    0.000000] ITS cmd its_build_mapc_cmd failed
   [    0.000000] ITS queue timeout (96 0)
   [    0.000000] ITS cmd its_build_invall_cmd failed
   [    0.000000] random: get_random_bytes called from start_kernel+0x31c/0x598 with crng_init=0
   [    0.000000] arch_timer: cp15 timer(s) running at 100.00MHz (phys).
   [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x171024e7e0, max_idle_ns: 440795205315 ns
   [    0.000002] sched_clock: 56 bits at 100MHz, resolution 10ns, wraps every 4398046511100ns
   [    0.008381] Console: colour dummy device 80x25
   [    0.012872] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=400000)
   [    0.023401] pid_max: default: 32768 minimum: 301
   [    0.028149] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
   [    0.035814] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
   [    0.044481] rcu: Hierarchical SRCU implementation.
   [    0.049405] Platform MSI: gic-its@f9020000 domain created
   [    0.054899] PCI/MSI: /amba_apu/interrupt-controller@f9000000/gic-its@f9020000 domain created
   [    0.063453] EFI services will not be available.
   [    0.068085] smp: Bringing up secondary CPUs ...
   [    0.072927] Detected PIPT I-cache on CPU1
   [    0.072943] GICv3: CPU1: found redistributor 1 region 0:0x00000000f90a0000
   [    0.072950] GICv3: CPU1: using allocated LPI pending table @0x0000000800050000
   [    1.242649] ITS queue timeout (160 0)
   [    1.242660] ITS cmd its_build_mapc_cmd failed
   [    2.412357] ITS queue timeout (192 0)
   [    2.412360] ITS cmd its_build_invall_cmd failed
   [    2.412377] CPU1: Booted secondary processor 0x0000000001 [0x410fd083]
   [    2.412420] smp: Brought up 1 node, 2 CPUs
   [    2.457682] SMP: Total of 2 processors activated.
   [    2.462426] CPU features: detected: 32-bit EL0 Support
   [    2.467608] CPU features: detected: CRC32 instructions
   [    2.472821] CPU: All CPU(s) started at EL2
   [    2.476959] alternatives: patching kernel code
   [    2.482032] devtmpfs: initialized
   [    2.487762] Registered cp15_barrier emulation handler
   [    2.492864] Registered setend emulation handler
   [    2.497512] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
   [    2.507345] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
   [    2.517210] DMI not present or invalid.
   [    2.521192] NET: Registered protocol family 16
   [    2.526291] DMA: preallocated 1024 KiB GFP_KERNEL pool for atomic allocations
   [    2.533572] DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
   [    2.541575] DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
   [    2.549675] audit: initializing netlink subsys (disabled)
   [    2.555200] audit: type=2000 audit(2.472:1): state=initialized audit_enabled=0 res=1
   [    2.563020] cpuidle: using governor menu
   [    2.567026] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
   [    2.573889] ASID allocator initialised with 65536 entries
   [    2.579379] Serial: AMBA PL011 UART driver
   [    2.595937] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
   [    2.602705] HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
   [    2.609470] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
   [    2.616231] HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
   [    3.154263] cryptd: max_cpu_qlen set to 1000
   [    3.172455] DRBG: Continuing without Jitter RNG
   [    3.246641] raid6: neonx8   gen()  3984 MB/s
   [    3.318985] raid6: neonx8   xor()  2865 MB/s
   [    3.391322] raid6: neonx4   gen()  4102 MB/s
   [    3.463660] raid6: neonx4   xor()  2929 MB/s
   [    3.535997] raid6: neonx2   gen()  3601 MB/s
   [    3.608336] raid6: neonx2   xor()  2718 MB/s
   [    3.680674] raid6: neonx1   gen()  2796 MB/s
   [    3.753010] raid6: neonx1   xor()  2187 MB/s
   [    3.825359] raid6: int64x8  gen()  2191 MB/s
   [    3.897697] raid6: int64x8  xor()  1310 MB/s
   [    3.970046] raid6: int64x4  gen()  2375 MB/s
   [    4.042386] raid6: int64x4  xor()  1327 MB/s
   [    4.114734] raid6: int64x2  gen()  2232 MB/s
   [    4.187078] raid6: int64x2  xor()  1210 MB/s
   [    4.259430] raid6: int64x1  gen()  1707 MB/s
   [    4.331771] raid6: int64x1  xor()   887 MB/s
   [    4.336076] raid6: using algorithm neonx4 gen() 4102 MB/s
   [    4.341515] raid6: .... xor() 2929 MB/s, rmw enabled
   [    4.346518] raid6: using neon recovery algorithm
   [    4.351588] iommu: Default domain type: Translated
   [    4.356686] SCSI subsystem initialized
   [    4.360562] usbcore: registered new interface driver usbfs
   [    4.366110] usbcore: registered new interface driver hub
   [    4.371482] usbcore: registered new device driver usb
   [    4.376658] mc: Linux media interface: v0.10
   [    4.380971] videodev: Linux video capture interface: v2.00
   [    4.386537] EDAC MC: Ver: 3.0.0
   [    4.389972] zynqmp-ipi-mbox mailbox@ff3f0440: Registered ZynqMP IPI mbox with TX/RX channels.
   [    4.398737] jesd204: created con: id=0, topo=0, link=0, /amba/spi@ff050000/hmc7044@0 <-> /fpga-axi@0/axi-jesd204-tx@a4b90000
   [    4.410065] jesd204: created con: id=1, topo=0, link=2, /amba/spi@ff050000/hmc7044@0 <-> /fpga-axi@0/axi-jesd204-rx@a4a90000
   [    4.421390] jesd204: created con: id=2, topo=0, link=0, /fpga-axi@0/axi-jesd204-tx@a4b90000 <-> /fpga-axi@0/axi-ad9081-tx-hpc@a4b10000
   [    4.433586] jesd204: created con: id=3, topo=0, link=2, /fpga-axi@0/axi-jesd204-rx@a4a90000 <-> /fpga-axi@0/axi-ad9081-rx-hpc@a4a10000
   [    4.445789] jesd204: created con: id=4, topo=0, link=2, /fpga-axi@0/axi-ad9081-rx-hpc@a4a10000 <-> /amba/spi@ff040000/ad9081@0
   [    4.457286] jesd204: created con: id=5, topo=0, link=0, /fpga-axi@0/axi-ad9081-tx-hpc@a4b10000 <-> /amba/spi@ff040000/ad9081@0
   [    4.468786] jesd204: /amba/spi@ff040000/ad9081@0: JESD204[0:2] transition uninitialized -> initialized
   [    4.478175] jesd204: /amba/spi@ff040000/ad9081@0: JESD204[0:0] transition uninitialized -> initialized
   [    4.487559] jesd204: found 6 devices and 1 topologies
   [    4.492666] FPGA manager framework
   [    4.496174] Advanced Linux Sound Architecture Driver Initialized.
   [    4.502541] Bluetooth: Core ver 2.22
   [    4.506152] NET: Registered protocol family 31
   [    4.510633] Bluetooth: HCI device and connection manager initialized
   [    4.517044] Bluetooth: HCI socket layer initialized
   [    4.521957] Bluetooth: L2CAP socket layer initialized
   [    4.527050] Bluetooth: SCO socket layer initialized
   [    4.532183] clocksource: Switched to clocksource arch_sys_counter
   [    4.538408] VFS: Disk quotas dquot_6.6.0
   [    4.542394] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
   [    4.551768] NET: Registered protocol family 2
   [    4.556429] tcp_listen_portaddr_hash hash table entries: 4096 (order: 4, 65536 bytes, linear)
   [    4.565088] TCP established hash table entries: 65536 (order: 7, 524288 bytes, linear)
   [    4.573364] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
   [    4.581398] TCP: Hash tables configured (established 65536 bind 65536)
   [    4.588062] UDP hash table entries: 4096 (order: 5, 131072 bytes, linear)
   [    4.595029] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes, linear)
   [    4.602495] NET: Registered protocol family 1
   [    4.607104] RPC: Registered named UNIX socket transport module.
   [    4.613085] RPC: Registered udp transport module.
   [    4.617829] RPC: Registered tcp transport module.
   [    4.622570] RPC: Registered tcp NFSv4.1 backchannel transport module.
   [    4.629349] PCI: CLS 0 bytes, default 64
   [    4.644294] Initialise system trusted keyrings
   [    4.648859] workingset: timestamp_bits=62 max_order=21 bucket_order=0
   [    4.655803] NFS: Registering the id_resolver key type
   [    4.660909] Key type id_resolver registered
   [    4.665131] Key type id_legacy registered
   [    4.669183] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
   [    4.675953] jffs2: version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
   [    4.683226] fuse: init (API version 7.32)
   [    4.714513] NET: Registered protocol family 38
   [    4.718995] xor: measuring software checksum speed
   [    4.725505]    8regs           :  5863 MB/sec
   [    4.731346]    32regs          :  6761 MB/sec
   [    4.737358]    arm64_neon      :  6060 MB/sec
   [    4.741748] xor: using function: 32regs (6761 MB/sec)
   [    4.746837] Key type asymmetric registered
   [    4.750964] Asymmetric key parser 'x509' registered
   [    4.755897] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
   [    4.763357] io scheduler mq-deadline registered
   [    4.767925] io scheduler kyber registered
   [    4.772983] ps_pcie_dma init()
   [    4.790689] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
   [    4.797704] Serial: AMBA driver
   [    4.801841] cacheinfo: Unable to detect cache hierarchy for CPU 0
   [    4.810715] brd: module loaded
   [    4.816589] loop: module loaded
   [    4.820467] mtdoops: mtd device (mtddev=name/number) must be supplied
   [    4.827890] libphy: Fixed MDIO Bus: probed
   [    4.832765] tun: Universal TUN/TAP device driver, 1.6
   [    4.837941] CAN device driver interface
   [    4.842191] usbcore: registered new interface driver asix
   [    4.847664] usbcore: registered new interface driver ax88179_178a
   [    4.853817] usbcore: registered new interface driver cdc_ether
   [    4.859709] usbcore: registered new interface driver net1080
   [    4.865427] usbcore: registered new interface driver cdc_subset
   [    4.871409] usbcore: registered new interface driver zaurus
   [    4.877041] usbcore: registered new interface driver cdc_ncm
   [    4.883122] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
   [    4.889709] ehci-pci: EHCI PCI platform driver
   [    4.894370] usbcore: registered new interface driver uas
   [    4.899751] usbcore: registered new interface driver usb-storage
   [    4.905845] usbcore: registered new interface driver usbserial_generic
   [    4.912436] usbserial: USB Serial support registered for generic
   [    4.918505] usbcore: registered new interface driver ftdi_sio
   [    4.924303] usbserial: USB Serial support registered for FTDI USB Serial Device
   [    4.931687] usbcore: registered new interface driver upd78f0730
   [    4.937662] usbserial: USB Serial support registered for upd78f0730
   [    4.944485] i2c /dev entries driver
   [    4.948992] usbcore: registered new interface driver uvcvideo
   [    4.954787] USB Video Class driver (1.1.1)
   [    4.959456] Bluetooth: HCI UART driver ver 2.3
   [    4.963942] Bluetooth: HCI UART protocol H4 registered
   [    4.969116] Bluetooth: HCI UART protocol BCSP registered
   [    4.974477] Bluetooth: HCI UART protocol LL registered
   [    4.979655] Bluetooth: HCI UART protocol ATH3K registered
   [    4.985105] Bluetooth: HCI UART protocol Three-wire (H5) registered
   [    4.991446] Bluetooth: HCI UART protocol Intel registered
   [    4.996897] Bluetooth: HCI UART protocol QCA registered
   [    5.002182] usbcore: registered new interface driver bcm203x
   [    5.007901] usbcore: registered new interface driver bpa10x
   [    5.013532] usbcore: registered new interface driver bfusb
   [    5.019075] usbcore: registered new interface driver btusb
   [    5.024626] usbcore: registered new interface driver ath3k
   [    5.030428] sdhci: Secure Digital Host Controller Interface driver
   [    5.036666] sdhci: Copyright(c) Pierre Ossman
   [    5.041057] sdhci-pltfm: SDHCI platform and OF driver helper
   [    5.046944] ledtrig-cpu: registered to indicate activity on CPUs
   [    5.053015] SMCCC: SOC_ID: ARCH_SOC_ID not implemented, skipping ....
   [    5.059604] zynqmp_firmware_probe Platform Management API v1.0
   [    5.065495] zynqmp_firmware_probe Trustzone version v1.0
   [    5.071211] xlnx_event_manager xlnx_event_manager: Failed to find property for Interrupt parent
   [    5.079990] xlnx_event_manager xlnx_event_manager: SGI Init has been failed with -22
   [    5.087803] xlnx_event_manager: probe of xlnx_event_manager failed with error -22
   [    5.136769] usbcore: registered new interface driver usbhid
   [    5.142398] usbhid: USB HID core driver
   [    5.147927] sysmon f1270000.sysmon: Successfully registered Versal Sysmon
   [    5.156818] ARM CCI_500 PMU driver probed
   [    5.156893] axi_sysid a5000000.axi-sysid-0: AXI System ID core version (1.01.a) found
   [    5.168979] axi_sysid a5000000.axi-sysid-0: [ad9081_fmca_ebz] on [vck190] git branch <hdl_2021_r2> git <a07cec4a84a90769270711557a535147daf78ba5> clean [2022-10-20 21:39:05] UTC
   [    5.185190] fpga_manager fpga0: Xilinx Versal FPGA Manager registered
   [    5.191940] usbcore: registered new interface driver snd-usb-audio
   [    5.199169] pktgen: Packet Generator for packet performance testing. Version: 2.75
   [    5.207351] Initializing XFRM netlink socket
   [    5.211712] NET: Registered protocol family 10
   [    5.216476] Segment Routing with IPv6
   [    5.220275] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   [    5.226486] NET: Registered protocol family 17
   [    5.230975] NET: Registered protocol family 15
   [    5.235537] can: controller area network core
   [    5.239949] NET: Registered protocol family 29
   [    5.244437] can: raw protocol
   [    5.247423] can: broadcast manager protocol
   [    5.251640] can: netlink gateway - max_hops=1
   [    5.256093] Bluetooth: RFCOMM TTY layer initialized
   [    5.261016] Bluetooth: RFCOMM socket layer initialized
   [    5.266207] Bluetooth: RFCOMM ver 1.11
   [    5.269986] Bluetooth: BNEP (Ethernet Emulation) ver 1.3
   [    5.275344] Bluetooth: BNEP filters: protocol multicast
   [    5.280615] Bluetooth: BNEP socket layer initialized
   [    5.285621] Bluetooth: HIDP (Human Interface Emulation) ver 1.2
   [    5.291590] Bluetooth: HIDP socket layer initialized
   [    5.296708] 9pnet: Installing 9P2000 support
   [    5.301017] NET: Registered protocol family 36
   [    5.305507] Key type dns_resolver registered
   [    5.309946] registered taskstats version 1
   [    5.314078] Loading compiled-in X.509 certificates
   [    5.319701] Btrfs loaded, crc32c=crc32c-generic
   [    5.330011] ff000000.serial: ttyAMA0 at MMIO 0xff000000 (irq = 31, base_baud = 0) is a SBSA
   [    5.338467] printk: console [ttyAMA0] enabled
   [    5.338467] printk: console [ttyAMA0] enabled
   [    5.347207] printk: bootconsole [pl11] disabled
   [    5.347207] printk: bootconsole [pl11] disabled
   [    5.356654] of-fpga-region fpga: FPGA Region probed
   [    5.361997] gpio gpiochip2: (pmc_gpio): detected irqchip that is shared with multiple gpiochips: please fix the driver.
   [    5.373433] xilinx-zynqmp-dma ffa80000.dma: ZynqMP DMA driver Probe success
   [    5.380593] xilinx-zynqmp-dma ffa90000.dma: ZynqMP DMA driver Probe success
   [    5.387745] xilinx-zynqmp-dma ffaa0000.dma: ZynqMP DMA driver Probe success
   [    5.394899] xilinx-zynqmp-dma ffab0000.dma: ZynqMP DMA driver Probe success
   [    5.402046] xilinx-zynqmp-dma ffac0000.dma: ZynqMP DMA driver Probe success
   [    5.409191] xilinx-zynqmp-dma ffad0000.dma: ZynqMP DMA driver Probe success
   [    5.416349] xilinx-zynqmp-dma ffae0000.dma: ZynqMP DMA driver Probe success
   [    5.423496] xilinx-zynqmp-dma ffaf0000.dma: ZynqMP DMA driver Probe success
   [    5.516361] hmc7044 spi2.0: PLL1: Locked, CLKIN0 @ 100000000 Hz, PFD: 10000 kHz - PLL2: Locked @ 3000.000000 MHz
   [    5.526765] jesd204: /amba/spi@ff050000/hmc7044@0,jesd204:1,parent=spi2.0: Using as SYSREF provider
   [    5.536836] macb ff0c0000.ethernet: Not enabling partial store and forward
   [    5.544164] libphy: MACB_mii_bus: probed
   [    5.549325] macb ff0c0000.ethernet eth0: Cadence GEM rev 0x0107010b at 0xff0c0000 irq 23 (00:0a:35:ad:90:81)
   [    5.559440] macb ff0d0000.ethernet: Not enabling partial store and forward
   [    5.575096] libphy: MACB_mii_bus: probed
   [    5.579067] macb ff0d0000.ethernet eth1: Cadence GEM rev 0x0107010b at 0xff0d0000 irq 24 (42:20:50:24:50:90)
   [    5.589720] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
   [    5.595213] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 1
   [    5.602945] xhci-hcd xhci-hcd.0.auto: hcc params 0x0238fe65 hci version 0x110 quirks 0x0000000000010810
   [    5.612353] xhci-hcd xhci-hcd.0.auto: irq 49, io mem 0xfe200000
   [    5.618423] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
   [    5.626686] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   [    5.633919] usb usb1: Product: xHCI Host Controller
   [    5.638792] usb usb1: Manufacturer: Linux 5.10.0-98699-gb2da1fe4a96a xhci-hcd
   [    5.645918] usb usb1: SerialNumber: xhci-hcd.0.auto
   [    5.651012] hub 1-0:1.0: USB hub found
   [    5.654769] hub 1-0:1.0: 1 port detected
   [    5.658894] xhci-hcd xhci-hcd.0.auto: xHCI Host Controller
   [    5.664387] xhci-hcd xhci-hcd.0.auto: new USB bus registered, assigned bus number 2
   [    5.672040] xhci-hcd xhci-hcd.0.auto: Host supports USB 3.0 SuperSpeed
   [    5.678630] usb usb2: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.10
   [    5.686890] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
   [    5.694111] usb usb2: Product: xHCI Host Controller
   [    5.698984] usb usb2: Manufacturer: Linux 5.10.0-98699-gb2da1fe4a96a xhci-hcd
   [    5.706110] usb usb2: SerialNumber: xhci-hcd.0.auto
   [    5.711240] hub 2-0:1.0: USB hub found
   [    5.715114] hub 2-0:1.0: config failed, hub doesn't have any ports! (err -19)
   [    5.722960] rtc_zynqmp f12a0000.rtc: registered as rtc0
   [    5.728198] rtc_zynqmp f12a0000.rtc: setting system clock to 2018-06-01T07:09:41 UTC (1527836981)
   [    5.737475] cdns-i2c ff020000.i2c: 400 kHz mmio ff020000 irq 27
   [    5.743786] Xilinx Watchdog fd4d0000.watchdog: Xilinx Watchdog Timer with timeout 30s
   [    5.751932] cpu cpu0: dev_pm_opp_set_rate: failed to find current OPP for freq 1399999986 (-34)
   [    5.760682] cpufreq: cpufreq_online: CPU0: Running at unlisted initial frequency: 1399999 KHz, changing to: 1199999 KHz
   [    5.771469] cpu cpu0: dev_pm_opp_set_rate: failed to find current OPP for freq 1399999986 (-34)
   [    5.781316] axi-jesd204-rx a4a90000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0xA4A90000. Encoder 64b66b, width 8/12, lanes 2, jesd204-fsm.
   [    5.794283] axi-jesd204-tx a4b90000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0xA4B90000. Encoder 64b66b, width 8/12, lanes 2, jesd204-fsm.
   [    5.807318] ad9081 spi1.0: supply vdd not found, using dummy regulator
   [    5.812017] mmc0: SDHCI controller on f1050000.sdhci [f1050000.sdhci] using ADMA 64-bit
   [    5.854687] mmc0: new high speed SDHC card at address 1234
   [    5.860452] mmcblk0: mmc0:1234 SA32G 29.1 GiB
   [    5.866358]  mmcblk0: p1 p2 p3
   [    7.048174] random: fast init done
   [    7.705968] ad9081 spi1.0: AD9081 Rev. 3 Grade 10 (API 1.3.1) probed
   [    7.733533] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: ADI AIM (10.02.b) at 0xA4A10000 mapped to 0x(____ptrval____) probed ADC AD9081 as MASTER
   [    7.764399] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition initialized -> probed
   [    7.775180] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition initialized -> probed
   [    7.785959] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition probed -> idle
   [    7.796127] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition probed -> idle
   [    7.806298] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition idle -> device_init
   [    7.816900] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition idle -> device_init
   [    7.827508] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> link_init
   [    7.838546] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> link_init
   [    7.849584] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param L mismatch 2!=4*0
   [    7.858100] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param M mismatch 2!=4*0
   [    7.866618] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param S mismatch 4!=2
   [    7.874961] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param F mismatch 6!=3
   [    7.883303] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: JESD param mismatch between TPL and Link configuration !
   [    7.893039] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: profile0:link_num0 param L mismatch 2!=4*0
   [    7.901555] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: profile0:link_num0 param M mismatch 2!=4*0
   [    7.910070] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: JESD param mismatch between TPL and Link configuration !
   [    7.919805] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> link_supported
   [    7.931106] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> link_supported
   [    7.942727] hmc7044 spi2.0: hmc7044_jesd204_link_pre_setup: Link2 forcing continuous SYSREF mode
   [    7.951684] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_pre_setup
   [    7.963418] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_pre_setup
   [    7.987373] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> clk_sync_stage1
   [    7.999192] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> clk_sync_stage1
   [    8.011012] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> clk_sync_stage2
   [    8.022918] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> clk_sync_stage2
   [    8.034824] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage3
   [    8.046730] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage3
   [    8.058637] jesd204: /fpga-axi@0/axi-jesd204-rx@a4a90000,jesd204:4,parent=a4a90000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 2, Link[2] lanes 4
   [    8.073843] jesd204: /fpga-axi@0/axi-jesd204-tx@a4b90000,jesd204:5,parent=a4b90000.axi-jesd204-tx: Possible instantiation for multiple chips; HDL lanes 2, Link[0] lanes 4
   [    8.089050] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> link_setup
   [    8.100520] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> link_setup
   [    8.116960] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> opt_setup_stage1
   [    8.128519] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> opt_setup_stage1
   [    8.144949] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> opt_setup_stage2
   [    8.157030] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> opt_setup_stage2
   [    8.169377] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage3
   [    8.181456] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage3
   [    8.193536] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage4
   [    8.205615] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage4
   [    8.217696] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage5
   [    8.229776] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage5
   [    8.246007] ad9081 spi1.0: running jesd_rx_calibrate_204c, LR 24750000 kbps
   [   16.248375] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> clocks_enable
   [   16.260198] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> clocks_enable
   [   16.272074] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> link_enable
   [   16.283461] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> link_enable
   [   16.544184] axi-jesd204-rx a4a90000.axi-jesd204-rx: axi_jesd204_rx_jesd204_link_running: Link2 status failed (WAIT_BS)
   [   16.554878] jesd204: /fpga-axi@0/axi-jesd204-rx@a4a90000,jesd204:4,parent=a4a90000.axi-jesd204-rx: JESD204[0:2] In link_running got error from cb: -1
   [   16.568261] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: Rolling back from 'link_enable', got error -1
   [   16.579041] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> link_running
   [   16.590338] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> link_running
   [   16.601701] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_running -> link_enable
   [   16.613001] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_running -> link_enable
   [   16.628348] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> clocks_enable
   [   16.639732] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> clocks_enable
   [   16.651116] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> opt_setup_stage5
   [   16.662934] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> opt_setup_stage5
   [   16.674754] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> opt_setup_stage4
   [   16.686831] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> opt_setup_stage4
   [   16.698910] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage3
   [   16.710989] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage3
   [   16.723069] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage2
   [   16.735150] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage2
   [   16.747230] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage1
   [   16.759308] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage1
   [   16.771390] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> link_setup
   [   16.782947] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> link_setup
   [   16.794507] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> clk_sync_stage3
   [   16.805978] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> clk_sync_stage3
   [   16.817449] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> clk_sync_stage2
   [   16.829353] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> clk_sync_stage2
   [   16.841259] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage1
   [   16.853165] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage1
   [   16.865071] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> link_pre_setup
   [   16.876889] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> link_pre_setup
   [   16.888708] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> link_supported
   [   16.900439] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> link_supported
   [   16.912171] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_init
   [   16.923469] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_init
   [   16.934767] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> device_init
   [   16.945804] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> device_init
   [   16.956844] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> idle
   [   16.967446] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> idle
   [   16.978051] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition idle -> idle
   [   16.988048] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition idle -> idle
   [   16.998044] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition idle -> device_init
   [   17.008646] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition idle -> device_init
   [   17.019251] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> link_init
   [   17.030287] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> link_init
   [   17.041326] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param L mismatch 2!=4*0
   [   17.049844] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param M mismatch 2!=4*0
   [   17.058360] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param S mismatch 4!=2
   [   17.066702] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param F mismatch 6!=3
   [   17.075044] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: JESD param mismatch between TPL and Link configuration !
   [   17.084777] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: profile0:link_num0 param L mismatch 2!=4*0
   [   17.093293] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: profile0:link_num0 param M mismatch 2!=4*0
   [   17.101808] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: JESD param mismatch between TPL and Link configuration !
   [   17.111544] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> link_supported
   [   17.122841] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> link_supported
   [   17.134397] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_pre_setup
   [   17.146129] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_pre_setup
   [   17.170083] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> clk_sync_stage1
   [   17.181903] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> clk_sync_stage1
   [   17.193721] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> clk_sync_stage2
   [   17.205626] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> clk_sync_stage2
   [   17.217530] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage3
   [   17.229433] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage3
   [   17.241341] jesd204: /fpga-axi@0/axi-jesd204-rx@a4a90000,jesd204:4,parent=a4a90000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 2, Link[2] lanes 4
   [   17.256546] jesd204: /fpga-axi@0/axi-jesd204-tx@a4b90000,jesd204:5,parent=a4b90000.axi-jesd204-tx: Possible instantiation for multiple chips; HDL lanes 2, Link[0] lanes 4
   [   17.271752] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> link_setup
   [   17.283222] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> link_setup
   [   17.299645] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> opt_setup_stage1
   [   17.311204] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> opt_setup_stage1
   [   17.327637] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> opt_setup_stage2
   [   17.339716] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> opt_setup_stage2
   [   17.352062] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage3
   [   17.364141] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage3
   [   17.376222] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage4
   [   17.388300] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage4
   [   17.400380] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage5
   [   17.412459] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage5
   [   17.428647] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> clocks_enable
   [   17.440467] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> clocks_enable
   [   17.452333] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> link_enable
   [   17.463718] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> link_enable
   [   17.724183] axi-jesd204-rx a4a90000.axi-jesd204-rx: axi_jesd204_rx_jesd204_link_running: Link2 status failed (WAIT_BS)
   [   17.734874] jesd204: /fpga-axi@0/axi-jesd204-rx@a4a90000,jesd204:4,parent=a4a90000.axi-jesd204-rx: JESD204[0:2] In link_running got error from cb: -1
   [   17.748256] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: Rolling back from 'link_enable', got error -1
   [   17.759035] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> link_running
   [   17.770331] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> link_running
   [   17.781679] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_running -> link_enable
   [   17.792978] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_running -> link_enable
   [   17.808324] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> clocks_enable
   [   17.819708] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> clocks_enable
   [   17.831092] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> opt_setup_stage5
   [   17.842910] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> opt_setup_stage5
   [   17.854730] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> opt_setup_stage4
   [   17.866808] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> opt_setup_stage4
   [   17.878886] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage3
   [   17.890965] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage3
   [   17.903045] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage2
   [   17.915125] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage2
   [   17.927205] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage1
   [   17.939282] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage1
   [   17.951366] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> link_setup
   [   17.962923] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> link_setup
   [   17.974483] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> clk_sync_stage3
   [   17.985954] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> clk_sync_stage3
   [   17.997426] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> clk_sync_stage2
   [   18.009330] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> clk_sync_stage2
   [   18.021236] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage1
   [   18.033141] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage1
   [   18.045047] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> link_pre_setup
   [   18.056864] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> link_pre_setup
   [   18.068683] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> link_supported
   [   18.080414] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> link_supported
   [   18.092146] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_init
   [   18.103444] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_init
   [   18.114743] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> device_init
   [   18.125779] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> device_init
   [   18.136816] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> idle
   [   18.147418] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> idle
   [   18.158022] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition idle -> idle
   [   18.168019] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition idle -> idle
   [   18.178016] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition idle -> device_init
   [   18.188617] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition idle -> device_init
   [   18.199222] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> link_init
   [   18.210257] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> link_init
   [   18.221294] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param L mismatch 2!=4*0
   [   18.229813] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param M mismatch 2!=4*0
   [   18.238329] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param S mismatch 4!=2
   [   18.246671] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param F mismatch 6!=3
   [   18.255013] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: JESD param mismatch between TPL and Link configuration !
   [   18.264746] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: profile0:link_num0 param L mismatch 2!=4*0
   [   18.273262] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: profile0:link_num0 param M mismatch 2!=4*0
   [   18.281777] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: JESD param mismatch between TPL and Link configuration !
   [   18.291513] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> link_supported
   [   18.302810] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> link_supported
   [   18.314371] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_pre_setup
   [   18.326104] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_pre_setup
   [   18.350058] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> clk_sync_stage1
   [   18.361878] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> clk_sync_stage1
   [   18.373697] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> clk_sync_stage2
   [   18.385601] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> clk_sync_stage2
   [   18.397505] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage3
   [   18.409409] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage3
   [   18.421317] jesd204: /fpga-axi@0/axi-jesd204-rx@a4a90000,jesd204:4,parent=a4a90000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 2, Link[2] lanes 4
   [   18.436521] jesd204: /fpga-axi@0/axi-jesd204-tx@a4b90000,jesd204:5,parent=a4b90000.axi-jesd204-tx: Possible instantiation for multiple chips; HDL lanes 2, Link[0] lanes 4
   [   18.451727] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> link_setup
   [   18.463198] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> link_setup
   [   18.479620] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> opt_setup_stage1
   [   18.491180] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> opt_setup_stage1
   [   18.507604] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> opt_setup_stage2
   [   18.519683] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> opt_setup_stage2
   [   18.532028] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage3
   [   18.544107] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage3
   [   18.556189] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage4
   [   18.568266] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage4
   [   18.580346] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage5
   [   18.592424] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage5
   [   18.608611] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> clocks_enable
   [   18.620431] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> clocks_enable
   [   18.632298] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> link_enable
   [   18.643683] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> link_enable
   [   18.904183] axi-jesd204-rx a4a90000.axi-jesd204-rx: axi_jesd204_rx_jesd204_link_running: Link2 status failed (WAIT_BS)
   [   18.914874] jesd204: /fpga-axi@0/axi-jesd204-rx@a4a90000,jesd204:4,parent=a4a90000.axi-jesd204-rx: JESD204[0:2] In link_running got error from cb: -1
   [   18.928256] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: Rolling back from 'link_enable', got error -1
   [   18.939035] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> link_running
   [   18.950332] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> link_running
   [   18.961680] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_running -> link_enable
   [   18.972979] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_running -> link_enable
   [   18.988326] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> clocks_enable
   [   18.999710] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> clocks_enable
   [   19.011094] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> opt_setup_stage5
   [   19.022911] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> opt_setup_stage5
   [   19.034732] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> opt_setup_stage4
   [   19.046809] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> opt_setup_stage4
   [   19.058887] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage3
   [   19.070967] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage3
   [   19.083046] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage2
   [   19.095126] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage2
   [   19.107206] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage1
   [   19.119283] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage1
   [   19.131364] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> link_setup
   [   19.142921] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> link_setup
   [   19.154481] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> clk_sync_stage3
   [   19.165952] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> clk_sync_stage3
   [   19.177423] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> clk_sync_stage2
   [   19.189327] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> clk_sync_stage2
   [   19.201232] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage1
   [   19.213138] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage1
   [   19.225044] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> link_pre_setup
   [   19.236861] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> link_pre_setup
   [   19.248679] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> link_supported
   [   19.260409] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> link_supported
   [   19.272142] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_init
   [   19.283440] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_init
   [   19.294738] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> device_init
   [   19.305775] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> device_init
   [   19.316812] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> idle
   [   19.327414] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> idle
   [   19.338018] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition idle -> idle
   [   19.348015] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition idle -> idle
   [   19.358011] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition idle -> device_init
   [   19.368614] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition idle -> device_init
   [   19.379218] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> link_init
   [   19.390254] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> link_init
   [   19.401291] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param L mismatch 2!=4*0
   [   19.409809] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param M mismatch 2!=4*0
   [   19.418325] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param S mismatch 4!=2
   [   19.426667] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: profile0:link_num2 param F mismatch 6!=3
   [   19.435010] cf_axi_adc a4a10000.axi-ad9081-rx-hpc: JESD param mismatch between TPL and Link configuration !
   [   19.444743] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: profile0:link_num0 param L mismatch 2!=4*0
   [   19.453258] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: profile0:link_num0 param M mismatch 2!=4*0
   [   19.461774] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: JESD param mismatch between TPL and Link configuration !
   [   19.471510] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> link_supported
   [   19.482807] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> link_supported
   [   19.494363] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_pre_setup
   [   19.506095] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_pre_setup
   [   19.530050] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> clk_sync_stage1
   [   19.541870] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> clk_sync_stage1
   [   19.553688] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> clk_sync_stage2
   [   19.565591] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> clk_sync_stage2
   [   19.577496] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage3
   [   19.589399] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage3
   [   19.601307] jesd204: /fpga-axi@0/axi-jesd204-rx@a4a90000,jesd204:4,parent=a4a90000.axi-jesd204-rx: Possible instantiation for multiple chips; HDL lanes 2, Link[2] lanes 4
   [   19.616511] jesd204: /fpga-axi@0/axi-jesd204-tx@a4b90000,jesd204:5,parent=a4b90000.axi-jesd204-tx: Possible instantiation for multiple chips; HDL lanes 2, Link[0] lanes 4
   [   19.631717] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> link_setup
   [   19.643188] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> link_setup
   [   19.659609] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> opt_setup_stage1
   [   19.671168] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> opt_setup_stage1
   [   19.687589] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> opt_setup_stage2
   [   19.699669] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> opt_setup_stage2
   [   19.712014] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage3
   [   19.724093] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage3
   [   19.736174] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage4
   [   19.748254] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage4
   [   19.760334] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage5
   [   19.772413] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage5
   [   19.788599] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> clocks_enable
   [   19.800419] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> clocks_enable
   [   19.812285] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> link_enable
   [   19.823670] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> link_enable
   [   20.084183] axi-jesd204-rx a4a90000.axi-jesd204-rx: axi_jesd204_rx_jesd204_link_running: Link2 status failed (WAIT_BS)
   [   20.094874] jesd204: /fpga-axi@0/axi-jesd204-rx@a4a90000,jesd204:4,parent=a4a90000.axi-jesd204-rx: JESD204[0:2] In link_running got error from cb: -1
   [   20.108255] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: Rolling back from 'link_enable', got error -1
   [   20.119033] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> link_running
   [   20.130330] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> link_running
   [   20.141678] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_running -> link_enable
   [   20.152977] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_running -> link_enable
   [   20.168323] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_enable -> clocks_enable
   [   20.179708] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_enable -> clocks_enable
   [   20.191092] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clocks_enable -> opt_setup_stage5
   [   20.202910] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clocks_enable -> opt_setup_stage5
   [   20.214730] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage5 -> opt_setup_stage4
   [   20.226807] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage5 -> opt_setup_stage4
   [   20.238885] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage4 -> opt_setup_stage3
   [   20.250964] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage4 -> opt_setup_stage3
   [   20.263043] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage3 -> opt_setup_stage2
   [   20.275123] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage3 -> opt_setup_stage2
   [   20.287202] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage2 -> opt_setup_stage1
   [   20.299280] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage2 -> opt_setup_stage1
   [   20.311360] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition opt_setup_stage1 -> link_setup
   [   20.322917] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition opt_setup_stage1 -> link_setup
   [   20.334478] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_setup -> clk_sync_stage3
   [   20.345948] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_setup -> clk_sync_stage3
   [   20.357419] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage3 -> clk_sync_stage2
   [   20.369323] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage3 -> clk_sync_stage2
   [   20.381229] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage2 -> clk_sync_stage1
   [   20.393134] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage2 -> clk_sync_stage1
   [   20.405041] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition clk_sync_stage1 -> link_pre_setup
   [   20.416858] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition clk_sync_stage1 -> link_pre_setup
   [   20.428677] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_pre_setup -> link_supported
   [   20.440408] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_pre_setup -> link_supported
   [   20.452139] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_supported -> link_init
   [   20.463438] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_supported -> link_init
   [   20.474736] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition link_init -> device_init
   [   20.485772] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition link_init -> device_init
   [   20.496809] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:0] transition device_init -> idle
   [   20.507411] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: JESD204[0:2] transition device_init -> idle
   [   20.518013] jesd204: /amba/spi@ff040000/ad9081@0,jesd204:0,parent=spi1.0: FSM completed with error -1
   [   20.527232] cf_axi_dds a4b10000.axi-ad9081-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0xA4B10000 mapped to 0x(____ptrval____), probed DDS AD9081
   [   20.543329] of_cfs_init
   [   20.545792] of_cfs_init: OK
   [   20.548654] cfg80211: Loading compiled-in X.509 certificates for regulatory database
   [   20.620979] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
   [   20.627509] clk: Not disabling unused clocks
   [   20.632127] ALSA device list:
   [   20.635089]   No soundcards found.
   [   20.638740] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
   [   20.647349] cfg80211: failed to load regulatory.db
   [   20.661984] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   [   20.670100] VFS: Mounted root (ext4 filesystem) on device 179:2.
   [   20.683170] devtmpfs: mounted
   [   20.686854] Freeing unused kernel memory: 2624K
   [   20.700221] Run /sbin/init as init process
   [   21.188935] systemd[1]: System time before build time, advancing clock.
   [   21.230930] systemd[1]: systemd 247.3-7+rpi1+deb11u1 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
   [   21.254590] systemd[1]: Detected architecture arm64.

   Welcome to Kuiper GNU/Linux 11.2 (bullseye)!

   [   21.285310] systemd[1]: Set hostname to <analog>.
   [   22.432021] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
   [   22.574520] systemd[1]: Queued start job for default target Graphical Interface.
   [   22.582700] random: systemd: uninitialized urandom read (16 bytes read)
   [   22.589475] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
   [   22.601830] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
   [   22.610737] systemd[1]: Created slice system-getty.slice.
   [  OK  ] Created slice system-getty.slice.
   [   22.632279] random: systemd: uninitialized urandom read (16 bytes read)
   [   22.639208] systemd[1]: Created slice system-modprobe.slice.
   [  OK  ] Created slice system-modprobe.slice.
   [   22.660258] random: systemd: uninitialized urandom read (16 bytes read)
   [   22.667139] systemd[1]: Created slice system-serial\x2dgetty.slice.
   [  OK  ] Created slice system-serial\x2dgetty.slice.
   [   22.688506] systemd[1]: Created slice system-systemd\x2dfsck.slice.
   [  OK  ] Created slice system-systemd\x2dfsck.slice.
   [   22.708431] systemd[1]: Created slice User and Session Slice.
   [  OK  ] Created slice User and Session Slice.
   [   22.728453] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
   [  OK  ] Started Forward Password R…uests to Wall Directory Watch.
   [   22.752394] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
   [   22.764468] systemd[1]: Reached target Slices.
   [  OK  ] Reached target Slices.
   [   22.780312] systemd[1]: Reached target Swap.
   [  OK  ] Reached target Swap.
   [   22.796749] systemd[1]: Listening on Syslog Socket.
   [  OK  ] Listening on Syslog Socket.
   [   22.816520] systemd[1]: Listening on fsck to fsckd communication Socket.
   [  OK  ] Listening on fsck to fsckd communication Socket.
   [   22.840392] systemd[1]: Listening on initctl Compatibility Named Pipe.
   [  OK  ] Listening on initctl Compatibility Named Pipe.
   [   22.860686] systemd[1]: Listening on Journal Audit Socket.
   [  OK  ] Listening on Journal Audit Socket.
   [   22.880506] systemd[1]: Listening on Journal Socket (/dev/log).
   [  OK  ] Listening on Journal Socket (/dev/log).
   [   22.900556] systemd[1]: Listening on Journal Socket.
   [  OK  ] Listening on Journal Socket.
   [   22.927739] systemd[1]: Listening on udev Control Socket.
   [  OK  ] Listening on udev Control Socket.
   [   22.948539] systemd[1]: Listening on udev Kernel Socket.
   [  OK  ] Listening on udev Kernel Socket.
   [   22.969634] systemd[1]: Mounting Huge Pages File System...
            Mounting Huge Pages File System...
   [   22.989502] systemd[1]: Mounting POSIX Message Queue File System...
            Mounting POSIX Message Queue File System...
   [   23.017352] systemd[1]: Mounting RPC Pipe File System...
            Mounting RPC Pipe File System...
   [   23.041531] systemd[1]: Mounting Kernel Debug File System...
            Mounting Kernel Debug File System...
   [   23.064517] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
   [   23.073071] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
   [   23.084905] systemd[1]: Starting Restore / save the current clock...
            Starting Restore / save the current clock...
   [   23.106189] systemd[1]: Starting Set the console keyboard layout...
            Starting Set the console keyboard layout...
   [   23.128801] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
   [   23.142396] systemd[1]: Starting Load Kernel Module configfs...
            Starting Load Kernel Module configfs...
   [   23.161685] systemd[1]: Starting Load Kernel Module drm...
            Starting Load Kernel Module drm...
   [   23.181746] systemd[1]: Starting Load Kernel Module fuse...
            Starting Load Kernel Module fuse...
   [   23.202539] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
   [   23.211783] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
   [   23.222194] systemd[1]: Starting Journal Service...
            Starting Journal Service...
   [   23.239411] systemd[1]: Starting Load Kernel Modules...
            Starting Load Kernel Modules...
   [   23.261557] systemd[1]: Starting Remount Root and Kernel File Systems...
            Starting Remount Root and Kernel File Systems...
   [   23.285615] systemd[1]: Starting Coldplug All udev Devices...
            Starting Coldplug All udev Devices...
   [   23.307560] systemd[1]: Mounted Huge Pages File System.
   [  OK  ] Mounted Huge Pages File System.
   [   23.329587] systemd[1]: Mounted POSIX Message Queue File System.
   [  OK  ] Mounted POSIX Message Queue File System.
   [   23.352678] systemd[1]: Mounted RPC Pipe File System.
   [  OK  ] Mounted RPC Pipe File System.
   [   23.372654] systemd[1]: Mounted Kernel Debug File System.
   [  OK  ] Mounted Kernel Debug File System.
   [   23.392882] systemd[1]: Finished Restore / save the current clock.
   [  OK  ] Finished Restore / save the current clock.
   [   23.413021] systemd[1]: Finished Set the console keyboard layout.
   [  OK  ] Finished Set the console keyboard layout.
   [   23.433061] systemd[1]: modprobe@configfs.service: Succeeded.
   [   23.444294] systemd[1]: Finished Load Kernel Module configfs.
   [  OK  ] Finished Load Kernel Module configfs.
   [   23.473022] systemd[1]: modprobe@drm.service: Succeeded.
   [   23.484963] systemd[1]: Finished Load Kernel Module drm.
   [  OK  ] Finished Load Kernel Module drm.
   [   23.509020] systemd[1]: modprobe@fuse.service: Succeeded.
   [   23.511897] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
   [   23.516713] systemd[1]: Finished Load Kernel Module fuse.
   [  OK  ] Finished Load Kernel Module fuse.
   [   23.550234] systemd[1]: systemd-modules-load.service: Main process exited, code=exited, status=1/FAILURE
   [   23.560071] systemd[1]: systemd-modules-load.service: Failed with result 'exit-code'.
   [   23.568423] systemd[1]: Failed to start Load Kernel Modules.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [   23.604578] systemd[1]: Started Journal Service.
   [  OK  ] Started Journal Service.
   [  OK  ] Finished Remount Root and Kernel File Systems.
            Mounting FUSE Control File System...
            Mounting Kernel Configuration File System...
            Starting Flush Journal to Persistent Storage...
            Starting Load/Save Random Seed...
   [   23.695880] systemd-journald[237]: Received client request to flush runtime journal.
            Starting Apply Kernel Variables...
            Starting Create System Users...
   [   23.731999] systemd-journald[237]: File /var/log/journal/4ae8d4d4914f48979b6aaa656e8e0280/system.journal corrupted or uncleanly shut down, renaming and replacing.
   [  OK  ] Mounted FUSE Control File System.
   [  OK  ] Mounted Kernel Configuration File System.
   [  OK  ] Finished Apply Kernel Variables.
   [  OK  ] Finished Create System Users.
            Starting Create Static Device Nodes in /dev...
   [  OK  ] Finished Coldplug All udev Devices.
            Starting Helper to synchronize boot up for ifupdown...
            Starting Wait for udev To …plete Device Initialization...
   [  OK  ] Finished Create Static Device Nodes in /dev.
   [  OK  ] Reached target Local File Systems (Pre).
            Starting Rule-based Manage…for Device Events and Files...
   [  OK  ] Finished Helper to synchronize boot up for ifupdown.
   [  OK  ] Finished Flush Journal to Persistent Storage.
   [  OK  ] Started Rule-based Manager for Device Events and Files.
            Starting Show Plymouth Boot Screen...
   [  OK  ] Started Show Plymouth Boot Screen.
   [  OK  ] Started Forward Password R…s to Plymouth Directory Watch.
   [  OK  ] Reached target Local Encrypted Volumes.
   [  OK  ] Found device /dev/ttyAMA0.
   [  OK  ] Found device /dev/disk/by-partuuid/291da1ab-01.
   [  OK  ] Finished Load/Save Random Seed.
   [  OK  ] Found device /dev/ttyS0.
   [  OK  ] Listening on Load/Save RF …itch Status /dev/rfkill Watch.
            Starting File System Check…isk/by-partuuid/291da1ab-01...
   [  OK  ] Started File System Check Daemon to report status.
   [  OK  ] Finished Wait for udev To Complete Device Initialization.
   [  OK  ] Finished File System Check…/disk/by-partuuid/291da1ab-01.
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
   [  OK  ] Reached target NFS client services.
   [  OK  ] Reached target Remote File Systems (Pre).
   [  OK  ] Reached target Remote File Systems.
   [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
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
   [  OK  ] Finished Remove Stale Onli…ext4 Metadata Check Snapshots.
   [  OK  ] Started triggerhappy global hotkey daemon.
   [  OK  ] Started DHCP Client Daemon.
   [  OK  ] Finished Raise network interfaces.
   [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
   [  OK  ] Started System Logging Service.
   [  OK  ] Started LSB: rng-tools (Debian variant).
   [  OK  ] Finished dphys-swapfile - …mount, and delete a swap file.
   [  OK  ] Started User Login Management.
   [  OK  ] Started Avahi mDNS/DNS-SD Stack.
   [  OK  ] Started WPA supplicant.
   [  OK  ] Reached target Network.
   [  OK  ] Reached target Network is Online.
            Starting CUPS Scheduler...
   [  OK  ] Started Erlang Port Mapper Daemon.
            Starting HTTP based time synchronization tool...
            Starting Internet superserver...
            Starting /etc/rc.local Compatibility...
            Starting OpenBSD Secure Shell server...
            Starting Permit User Sessions...
   [  OK  ] Started Unattended Upgrades Shutdown.
   [  OK  ] Started /etc/rc.local Compatibility.
   [  OK  ] Started Authorization Manager.
            Starting Modem Manager...
   [  OK  ] Finished Permit User Sessions.
            Starting Light Display Manager...
            Starting Hold until boot process finishes up...
   [  OK  ] Started Internet superserver.
   [  OK  ] Started HTTP based time synchronization tool.
   [  OK  ] Finished Creating IIOD Context Attributes....
   [  OK  ] Started IIO Daemon.
   [  OK  ] Started OpenBSD Secure Shell server.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Started Make remote CUPS printers available locally.
   [  OK  ] Finished Analog Devices power up/down sequence.
   [FAILED] Failed to start VNC Server for X11.

   Raspbian GNU/Linux 11 analog ttyAMA0

   analog login: root (automatic login)

   Password:

</hidden>

Login Information

- user: analog
- password: analog

The following devices should be present: ::

   root@analog:~# iio_info | grep iio:device
           iio:device0: xlnx,versal-sysmon
           iio:device1: hmc7044
           iio:device2: axi-ad9081-rx-hpc (buffer capable)
           iio:device3: axi-ad9081-tx-hpc (buffer capable)

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp.rst

   :start-after: .. start-#iio-oscilloscope-remote
   :end-before: .. end-#iio-oscilloscope-remote

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp.rst

   :start-after: .. start-#shut-down
   :end-before: .. end-#shut-down

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/common.rst

   :start-after: .. start-#useful-links
   :end-before: .. end-#useful-links

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/common.rst

   :start-after: .. start-#support
   :end-before: .. end-#support
