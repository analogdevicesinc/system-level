.. _hmcad15xx zed:

ZedBoard Quick start
===============================================================================

.. image:: ../images/hmcad1520_zed_setup.jpg
   :width: 500

This guide provides some quick instructions on how to setup and test the
:adi:`HMCAD1511-EBZ/HMCAD1520-EBZ <HMCAD1520-EBZ>` on:

- `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_ 
  FMC (J1) port

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following files are needed for the system to boot:

- HDL boot image: ``BOOT.BIN``
- Linux Kernel image: ``uImage``
- Linux device tree: ``devicetree.dtb``

Instructions on how to manually build the boot files from source can be found
here:

- :ref:`linux-kernel zynq`
- :external+hdl:ref:`hmcad1520` build documentation. More HDL build details at
  :external+hdl:ref:`build_hdl`.

Required Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+scopy:doc:`Scopy <index>` v2.2 or later (must contain the ADC Plugin)
- An UART terminal (Putty/Tera Term, etc.) with baud rate 115200 (8N1)

Required Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- AMD Xilinx `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board/>`_
- 12V 1A barrel jack supply for ZedBoard
- HMCAD1520-EBZ/HMCAD1511-EBZ FMC board
- Micro-USB cable
- LAN Cable (Ethernet)
- Signal Generator
- SMA male to BNC male cable
- External 1GHz clock source if working with the :adi:`HMCAD1520-EBZ` + extra 
  SMA male to SMA male cable, because it does not include an on-board crystal 
  like the :adi:`HMCAD1511`.
- An SD card with at least 16GB of memory.
- (Optional) USB keyboard & mouse and a HDMI compatible monitor

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/hmcad1520_zed_setup_full.jpg

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. esd-warning::

Follow the steps in this order, to avoid damaging the components:

#. Connect the :adi:`HMCAD1520-EBZ/HMCAD1511-EBZ <HMCAD1520-EBZ>` FMC board to
   the FPGA carrier FMC socket
#. Connect USB UART J14 (Micro-USB) to your host PC
#. Insert SD card with ADI Kuiper image into socket J12
#. Set VADJ Select Jumper J18 to 1V8. 
#. Configure Jumpers for SD Card boot mode (JP7-JP11 and MIO0)

   .. image:: ../../images/zed_sw.png
      :width: 600

#. Connect an Ethernet cable to Ethernet port J11
#. Setup the signal generator. In this guide we used a sinusoidal signal with 
   an amplitude of 1V and a frequency of 200kHz.
#. Connect the signal generator output to the IP4 port on the evaluation board
   (J7)
#. If you work with the :adi:`HMCAD1520-EBZ` you will need to connect it to an 
   external clock source since it doesn't include an on-board crystal. Connect 
   the external clock source to the J1 SMA port on the evaluation board.
   Optionally you can bypass the need of an external clock by soldering a 1GHz
   crystal at Y1 and moving the resistance from R12 to R13.
#. Make sure the clock source is set to 1 GHz and 10 dBm and start it
#. Connect via UART with the terminal of your choice
   - For Putty :

      .. image:: ../../images/putty_connect.png
         :width: 400

      - Select Serial
      - Insert baud rate of 115200
      - Insert the COM port the ZedBoard is connected to
         - In order to find the COM port: Device Manager -> Ports(COM & LPT)
         
         .. image:: ../../images/com_ports.png
          :width: 400



#. Turn on the power switch on the FPGA board

.. collapsible:: Complete boot log

   ::

      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 6.12.0-27064-g13b7bb744468-dirty (serban@HYB-dxRedMxsORC) (arm-amd-linux-gnueabi-gcc.real (GCC) 13.3.0, GNU ld (GNU Binutils) 2.42.0.20240723) #7 SMP PREEMPT Wed Feb 18 14:34:56 EET 2026
      [    0.000000] CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
      [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      [    0.000000] OF: fdt: Machine model: Xilinx Zynq ZED
      [    0.000000] OF: fdt: earlycon: stdout-path /amba@0/uart@E0001000 not found
      [    0.000000] Memory policy: Data cache writealloc
      [    0.000000] cma: Reserved 128 MiB at 0x16800000 on node -1
      [    0.000000] Zone ranges:
      [    0.000000]   Normal   [mem 0x0000000000000000-0x000000001fffffff]
      [    0.000000]   HighMem  empty
      [    0.000000] Movable zone start for each node
      [    0.000000] Early memory node ranges
      [    0.000000]   node   0: [mem 0x0000000000000000-0x000000001fffffff]
      [    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000001fffffff]
      [    0.000000] percpu: Embedded 12 pages/cpu s17356 r8192 d23604 u49152
      [    0.000000] pcpu-alloc: s17356 r8192 d23604 u49152 alloc=12*4096
      [    0.000000] pcpu-alloc: [0] 0 [0] 1
      [    0.000000] Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1
      [    0.000000] Dentry cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 32768 (order: 5, 131072 bytes, linear)
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 131072
      [    0.000000] mem auto-init: stack:all(zero), heap alloc:off, heap free:off
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] rcu: Preemptible hierarchical RCU implementation.
      [    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
      [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
      [    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=2
      [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
      [    0.000000] efuse mapped to (ptrval)
      [    0.000000] slcr mapped to (ptrval)
      [    0.000000] L2C: platform modifies aux control register: 0x72360000 -> 0x72760000
      [    0.000000] L2C: DT/platform modifies aux control register: 0x72360000 -> 0x72760000
      [    0.000000] L2C-310 erratum 769419 enabled
      [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
      [    0.000000] L2C-310 full line of zeros enabled for Cortex-A9
      [    0.000000] L2C-310 ID prefetch enabled, offset 1 lines
      [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
      [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
      [    0.000000] L2C-310: CACHE_ID 0x410000c8, AUX_CTRL 0x76760001
      [    0.000000] rcu: srcu_init: Setting srcu_struct sizes based on contention.
      [    0.000000] zynq_clock_init: clkc starts at (ptrval)
      [    0.000000] Zynq clock init
      [    0.000003] sched_clock: 64 bits at 167MHz, resolution 6ns, wraps every 4398046511103ns
      [    0.000024] clocksource: arm_global_timer: mask: 0xffffffffffffffff max_cycles: 0x26703d7dd8, max_idle_ns: 440795208065 ns
      [    0.000055] Switching to timer-based delay loop, resolution 6ns
      [    0.000457] Console: colour dummy device 80x30
      [    0.000492] Calibrating delay loop (skipped), value calculated using timer frequency.. 333.33 BogoMIPS (lpj=1666666)
      [    0.000509] CPU: Testing write buffer coherency: ok
      [    0.000544] CPU0: Spectre v2: using BPIALL workaround
      [    0.000553] pid_max: default: 32768 minimum: 301
      [    0.000730] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
      [    0.000746] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
      [    0.001522] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.070220] Setting up static identity map for 0x100000 - 0x100060
      [    0.080219] rcu: Hierarchical SRCU implementation.
      [    0.080226] rcu:     Max phase no-delay instances is 1000.
      [    0.100230] smp: Bringing up secondary CPUs ...
      [    0.140559] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.140579] CPU1: Spectre v2: using BPIALL workaround
      [    0.140745] smp: Brought up 1 node, 2 CPUs
      [    0.140758] SMP: Total of 2 processors activated (666.66 BogoMIPS).
      [    0.140768] CPU: All CPU(s) started in SVC mode.
      [    0.140911] Memory: 358772K/524288K available (13312K kernel code, 907K rwdata, 10980K rodata, 1024K init, 495K bss, 33484K reserved, 131072K cma-reserved, 0K highmem)
      [    0.141444] devtmpfs: initialized
      [    0.146366] VFP support v0.3: implementor 41 architecture 3 part 30 variant 9 rev 4
      [    0.146608] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.146631] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.152947] pinctrl core: initialized pinctrl subsystem
      [    0.154255] NET: Registered PF_NETLINK/PF_ROUTE protocol family
      [    0.156430] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.157523] thermal_sys: Registered thermal governor 'step_wise'
      [    0.161894] platform axi: Fixed dependency cycle(s) with /axi/interrupt-controller@f8f01000
      [    0.165535] platform replicator: Fixed dependency cycle(s) with /axi/etb@f8801000
      [    0.165646] amba f8801000.etb: Fixed dependency cycle(s) with /replicator
      [    0.165905] platform replicator: Fixed dependency cycle(s) with /axi/tpiu@f8803000
      [    0.166001] amba f8803000.tpiu: Fixed dependency cycle(s) with /replicator
      [    0.166255] platform replicator: Fixed dependency cycle(s) with /axi/funnel@f8804000
      [    0.166356] amba f8804000.funnel: Fixed dependency cycle(s) with /axi/ptm@f889d000
      [    0.166379] amba f8804000.funnel: Fixed dependency cycle(s) with /axi/ptm@f889c000
      [    0.166398] amba f8804000.funnel: Fixed dependency cycle(s) with /replicator
      [    0.166643] amba f8804000.funnel: Fixed dependency cycle(s) with /axi/ptm@f889c000
      [    0.166745] amba f889c000.ptm: Fixed dependency cycle(s) with /axi/funnel@f8804000
      [    0.166983] amba f8804000.funnel: Fixed dependency cycle(s) with /axi/ptm@f889d000
      [    0.167075] amba f889d000.ptm: Fixed dependency cycle(s) with /axi/funnel@f8804000
      [    0.169140] platform 70e00000.lcd-controller: Fixed dependency cycle(s) with /fpga-axi@0/i2c@41600000/hdmi@39
      [    0.171615] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.171629] hw-breakpoint: maximum watchpoint size is 4 bytes.
      [    0.172608] e0001000.serial: ttyPS0 at MMIO 0xe0001000 (irq = 26, base_baud = 3125000) is a xuartps
      [    0.172693] printk: legacy console [ttyPS0] enabled
      [    0.637369] SCSI subsystem initialized
      [    0.640086] usbcore: registered new interface driver usbfs
      [    0.644363] usbcore: registered new interface driver hub
      [    0.648408] usbcore: registered new device driver usb
      [    0.652582] mc: Linux media interface: v0.10
      [    0.655603] videodev: Linux video capture interface: v2.00
      [    0.659860] pps_core: LinuxPPS API ver. 1 registered
      [    0.663539] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.671393] PTP clock support registered
      [    0.674323] jesd204: found 0 devices and 0 topologies
      [    0.678149] FPGA manager framework
      [    0.680506] Advanced Linux Sound Architecture Driver Initialized.
      [    0.687007] clocksource: Switched to clocksource arm_global_timer
      [    0.703878] NET: Registered PF_INET protocol family
      [    0.707719] IP idents hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.714946] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes, linear)
      [    0.722080] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.728584] TCP established hash table entries: 4096 (order: 2, 16384 bytes, linear)
      [    0.735084] TCP bind hash table entries: 4096 (order: 4, 65536 bytes, linear)
      [    0.740988] TCP: Hash tables configured (established 4096 bind 4096)
      [    0.746114] UDP hash table entries: 256 (order: 1, 8192 bytes, linear)
      [    0.751375] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes, linear)
      [    0.757194] NET: Registered PF_UNIX/PF_LOCAL protocol family
      [    0.762081] RPC: Registered named UNIX socket transport module.
      [    0.766701] RPC: Registered udp transport module.
      [    0.770094] RPC: Registered tcp transport module.
      [    0.773537] RPC: Registered tcp-with-tls transport module.
      [    0.777716] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.784014] workingset: timestamp_bits=30 max_order=17 bucket_order=0
      [    0.789882] NFS: Registering the id_resolver key type
      [    0.793712] Key type id_resolver registered
      [    0.796587] Key type id_legacy registered
      [    0.799313] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      [    0.804726] nfs4flexfilelayout_init: NFSv4 Flexfile Layout Driver Registering...
      [    0.810852] fuse: init (API version 7.41)
      [    0.813970] io scheduler mq-deadline registered
      [    0.817195] io scheduler kyber registered
      [    0.819917] io scheduler bfq registered
      [    0.823600] zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
      [    0.830926] ledtrig-cpu: registered to indicate activity on CPUs
      [    0.839795] dma-pl330 f8003000.dma-controller: Loaded driver for PL330 DMAC-241330
      [    0.846154] dma-pl330 f8003000.dma-controller:       DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Events-16
      [    0.865200] brd: module loaded
      [    0.873718] loop: module loaded
      [    0.875955] Registered mathworks_ip class
      [    0.882030] spi-nor spi1.0: found s25fl256s1, expected n25q128a11
      [    0.887011] 5 fixed-partitions partitions found on MTD device spi1.0
      [    0.892141] Creating 5 MTD partitions on "spi1.0":
      [    0.895627] 0x000000000000-0x000000500000 : "boot"
      [    0.900764] 0x000000500000-0x000000520000 : "bootenv"
      [    0.906053] 0x000000520000-0x000000540000 : "config"
      [    0.911303] 0x000000540000-0x000000fc0000 : "image"
      [    0.916361] 0x000000fc0000-0x000002000000 : "spare"
      [    0.921837] MACsec IEEE 802.1AE
      [    0.925024] tun: Universal TUN/TAP device driver, 1.6
      [    0.950894] hwmon hwmon0: temp1_input not attached to any thermal zone
      [    1.050763] macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 41 (00:0a:35:00:01:22)
      [    1.059780] usbcore: registered new interface driver asix
      [    1.063939] usbcore: registered new interface driver ax88179_178a
      [    1.068754] usbcore: registered new interface driver cdc_ether
      [    1.073330] usbcore: registered new interface driver net1080
      [    1.077711] usbcore: registered new interface driver cdc_subset
      [    1.082374] usbcore: registered new interface driver zaurus
      [    1.086678] usbcore: registered new interface driver cdc_ncm
      [    1.091088] usbcore: registered new interface driver r8153_ecm
      [    1.097186] usbcore: registered new interface driver uas
      [    1.101257] usbcore: registered new interface driver usb-storage
      [    1.106040] usbcore: registered new interface driver usbserial_generic
      [    1.111304] usbserial: USB Serial support registered for generic
      [    1.116034] usbcore: registered new interface driver ftdi_sio
      [    1.120507] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    1.126561] usbcore: registered new interface driver upd78f0730
      [    1.131213] usbserial: USB Serial support registered for upd78f0730
      [    1.137054] ULPI transceiver vendor/product ID 0x0451/0x1507
      [    1.141470] Found TI TUSB1210 ULPI transceiver.
      [    1.144706] ULPI integrity check: passed.
      [    1.147525] ci_hdrc ci_hdrc.0: EHCI Host Controller
      [    1.151138] ci_hdrc ci_hdrc.0: new USB bus registered, assigned bus number 1
      [    1.170585] ci_hdrc ci_hdrc.0: USB 2.0 started, EHCI 1.00
      [    1.174899] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 6.12
      [    1.181894] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    1.187813] usb usb1: Product: EHCI Host Controller
      [    1.191400] usb usb1: Manufacturer: Linux 6.12.0-27064-g13b7bb744468-dirty ehci_hcd
      [    1.197751] usb usb1: SerialNumber: ci_hdrc.0
      [    1.201585] hub 1-0:1.0: USB hub found
      [    1.204075] hub 1-0:1.0: 1 port detected
      [    1.209349] i2c_dev: i2c /dev entries driver
      [    1.213531] platform 70e00000.lcd-controller: Fixed dependency cycle(s) with /fpga-axi@0/i2c@41600000/hdmi@39
      [    1.222318] i2c 0-0039: Fixed dependency cycle(s) with /fpga-axi@0/lcd-controller@70e00000
      [    1.229531] adv7511 0-0039: supply avdd not found, using dummy regulator
      [    1.235098] adv7511 0-0039: supply dvdd not found, using dummy regulator
      [    1.240575] adv7511 0-0039: supply pvdd not found, using dummy regulator
      [    1.246049] adv7511 0-0039: supply bgvdd not found, using dummy regulator
      [    1.251606] adv7511 0-0039: supply dvdd-3v not found, using dummy regulator
      [    1.266449] at24 1-0050: supply vcc not found, using dummy regulator
      [    1.272383] at24 1-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
      [    1.278792] gspca_main: v2.14.0 registered
      [    1.281686] usbcore: registered new interface driver uvcvideo
      [    1.289298] cdns-wdt f8005000.watchdog: Xilinx Watchdog Timer with timeout 10s
      [    1.295562] Xilinx Zynq CpuIdle Driver started
      [    1.298700] failed to register cpuidle driver
      [    1.302039] sdhci: Secure Digital Host Controller Interface driver
      [    1.306909] sdhci: Copyright(c) Pierre Ossman
      [    1.309956] sdhci-pltfm: SDHCI platform and OF driver helper
      [    1.314930] clocksource: ttc_clocksource: mask: 0xffff max_cycles: 0xffff, max_idle_ns: 537538477 ns
      [    1.323126] timer #0 at (ptrval), irq=47
      [    1.326053] hid: raw HID events driver (C) Jiri Kosina
      [    1.332518] usbcore: registered new interface driver usbhid
      [    1.336806] usbhid: USB HID core driver
      [    1.339987] SPI driver fb_seps525 has no spi_device_id for syncoam,seps525
      [    1.349950] hmcad15xx spi0.0: resolution: 14-bit, channels: 4, pol-mask: 0
      [    1.359370] hmcad15xx spi0.0: Write addr 0x42: value 0x0000
      [    1.362146] mmc0: SDHCI controller on e0100000.mmc [e0100000.mmc] using ADMA
      [    1.369460] hmcad15xx spi0.0: Read addr 0x53: value 0x0000
      [    1.373644] hmcad15xx spi0.0: Write addr 0x53: value 0x0004
      [    1.378040] hmcad15xx spi0.0: Write addr 0x31: value 0x0204
      [    1.382404] hmcad15xx spi0.0: Read addr 0x3a: value 0x0000
      [    1.386585] hmcad15xx spi0.0: Write addr 0x3a: value 0x0010
      [    1.390972] hmcad15xx spi0.0: Read addr 0x3a: value 0x0010
      [    1.395152] hmcad15xx spi0.0: Write addr 0x3a: value 0x1010
      [    1.399531] hmcad15xx spi0.0: Read addr 0x3b: value 0x0000
      [    1.403710] hmcad15xx spi0.0: Write addr 0x3b: value 0x0010
      [    1.406048] mmc0: new high speed SDHC card at address 0001
      [    1.412209] hmcad15xx spi0.0: Read addr 0x3b: value 0x0010
      [    1.416393] hmcad15xx spi0.0: Write addr 0x3b: value 0x1010
      [    1.420780] hmcad15xx spi0.0: Read addr 0x46: value 0x0000
      [    1.422828] mmcblk0: mmc0:0001 00000 29.1 GiB
      [    1.424968] hmcad15xx spi0.0: Write addr 0x46: value 0x0004
      [    1.430341]  mmcblk0: p1 p2 p3
      [    1.446568] armv7-pmu f8891000.pmu: hw perfevents: no interrupt-affinity property, guessing.
      [    1.454117] hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 (8000003f) counters available
      [    1.462352] axi_sysid 45000000.sysid: AXI System ID core version (1.01.a) found
      [    1.468524] axi_sysid 45000000.sysid: [hmcad1520_ebz] on [zed] git branch <dev_hmcad15xx> git <aaf313727e3d99ff68ece4c1d30500ea42e05447> dirty [2026-02-18 12:00:39] UTC
      [    1.483080] fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
      [    1.489029] usbcore: registered new interface driver snd-usb-audio
      [    1.497272] axi-i2s 77600000.i2s: probed, capture enabled, playback enabled
      [    1.503831] NET: Registered PF_INET6 protocol family
      [    1.508946] Segment Routing with IPv6
      [    1.511376] In-situ OAM (IOAM) with IPv6
      [    1.514073] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    1.519437] NET: Registered PF_PACKET protocol family
      [    1.523501] NET: Registered PF_IEEE802154 protocol family
      [    1.527691] Key type dns_resolver registered
      [    1.530920] Registering SWP/SWPB emulation handler
      [    1.560115] of-fpga-region fpga-region: FPGA Region probed
      [    1.565429] [drm] Initialized axi_hdmi_drm 1.0.0 for 70e00000.lcd-controller on minor 0
      [    1.573497] axi-hdmi 70e00000.lcd-controller: [drm] Cannot find any crtc or sizes
      [    1.581428] axi-hdmi 70e00000.lcd-controller: [drm] Cannot find any crtc or sizes
      [    1.606723] hmcad15xx spi0.0: hmcad15xx_post_setup: resolution=1, mode=4, cntrl=0x11
      [    1.613186] hmcad15xx spi0.0: hmcad15xx_post_setup: pol-mask=0
      [    1.618354] cf_axi_adc 44a00000.axi_adc_hmcad15xx: ADI AIM (10.03.\x00) probed ADC hmcad15xx_axi_adc as MASTER
      [    1.630713] debugfs: File 'Capture' in directory 'dapm' already present!
      [    1.659927] input: gpio-keys as /devices/soc0/gpio-keys/input/input0
      [    1.665504] of_cfs_init
      [    1.666681] of_cfs_init: OK
      [    1.668551] clk: Not disabling unused clocks
      [    1.671520] ALSA device list:
      [    1.673179]   #0: HDMI monitor
      [    1.674924]   #1: ZED ADAU1761
      [    1.690181] EXT4-fs (mmcblk0p2): mounted filesystem 675b84e0-16af-4fea-97ce-a01fc7c7f005 r/w with ordered data mode. Quota mode: disabled.
      [    1.701401] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    1.714202] devtmpfs: mounted
      [    1.717543] Freeing unused kernel image (initmem) memory: 1024K
      [    1.722950] Run /sbin/init as init process
      [    1.725739]   with arguments:
      [    1.725746]     /sbin/init
      [    1.725754]   with environment:
      [    1.725761]     HOME=/
      [    1.725769]     TERM=linux
      [    2.272015] systemd[1]: System time before build time, advancing clock.
      [    2.305142] systemd[1]: Failed to look up module alias 'autofs4': Function not implemented
      [    2.350035] systemd[1]: systemd 247.3-7+rpi1+deb11u6 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +ZSTD +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=unified)
      [    2.372788] systemd[1]: Detected architecture arm.
      [    2.408239] systemd[1]: Set hostname to <analog>.
      [    4.344176] systemd[1]: /lib/systemd/system/plymouth-start.service:16: Unit configured to use KillMode=none. This is unsafe, as it disables systemd's process lifecycle management for the service. Please update your service to use a safer KillMode=, such as 'mixed' or 'control-group'. Support for KillMode=none is deprecated and will eventually be removed.
      [    4.688782] systemd[1]: Queued start job for default target Graphical Interface.
      [    6.887040] random: crng init done
      [    6.889563] systemd[1]: system-getty.slice: unit configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [    6.900657] systemd[1]: (This warning is only shown for the first unit using IP firewalling.)
      [    6.909136] systemd[1]: Created slice system-getty.slice.
      [    6.938124] systemd[1]: Created slice system-modprobe.slice.
      [    6.968051] systemd[1]: Created slice system-serial\x2dgetty.slice.
      [    6.998013] systemd[1]: Created slice system-systemd\x2dfsck.slice.
      [    7.027750] systemd[1]: Created slice User and Session Slice.
      [    7.057639] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
      [    7.087624] systemd[1]: Condition check resulted in Arbitrary Executable File Formats File System Automount Point being skipped.
      [    7.099341] systemd[1]: Reached target Slices.
      [    7.117416] systemd[1]: Reached target Swap.
      [    7.145408] systemd[1]: Listening on Syslog Socket.
      [    7.167905] systemd[1]: Listening on fsck to fsckd communication Socket.
      [    7.197625] systemd[1]: Listening on initctl Compatibility Named Pipe.
      [    7.253179] systemd[1]: Condition check resulted in Journal Audit Socket being skipped.
      [    7.260905] systemd[1]: Listening on Journal Socket (/dev/log).
      [    7.288239] systemd[1]: Listening on Journal Socket.
      [    7.339470] systemd[1]: Listening on udev Control Socket.
      [    7.367941] systemd[1]: Listening on udev Kernel Socket.
      [    7.398165] systemd[1]: Condition check resulted in Huge Pages File System being skipped.
      [    7.405675] systemd[1]: Condition check resulted in POSIX Message Queue File System being skipped.
      [    7.457543] systemd[1]: Mounting RPC Pipe File System...
      [    7.480836] systemd[1]: Mounting Kernel Debug File System...
      [    7.507840] systemd[1]: Condition check resulted in Kernel Trace File System being skipped.
      [    7.515466] systemd[1]: Condition check resulted in Kernel Module supporting RPCSEC_GSS being skipped.
      [    7.577962] systemd[1]: Starting Restore / save the current clock...
      [    7.614936] systemd[1]: Starting Set the console keyboard layout...
      [    7.647455] systemd[1]: Condition check resulted in Create list of static device nodes for the current kernel being skipped.
      [    7.664775] systemd[1]: Starting Load Kernel Module configfs...
      [    7.738039] systemd[1]: Starting Load Kernel Module drm...
      [    7.764332] systemd[1]: Starting Load Kernel Module fuse...
      [    7.801064] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
      [    7.809382] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
      [    7.857940] systemd[1]: Starting Journal Service...
      [    7.902424] systemd[1]: Starting Load Kernel Modules...
      [    7.930428] systemd[1]: Starting Remount Root and Kernel File Systems...
      [    7.972469] systemd[1]: Starting Coldplug All udev Devices...
      [    8.035984] systemd[1]: Mounted RPC Pipe File System.
      [    8.098347] systemd[1]: Mounted Kernel Debug File System.
      [    8.119045] systemd[1]: Finished Restore / save the current clock.
      [    8.174678] systemd[1]: modprobe@configfs.service: Succeeded.
      [    8.188452] systemd[1]: Finished Load Kernel Module configfs.
      [    8.229279] systemd[1]: Finished Set the console keyboard layout.
      [    8.260175] systemd[1]: modprobe@drm.service: Succeeded.
      [    8.277748] systemd[1]: Finished Load Kernel Module drm.
      [    8.309775] systemd[1]: modprobe@fuse.service: Succeeded.
      [    8.327338] systemd[1]: Finished Load Kernel Module fuse.
      [    8.358367] systemd[1]: Started Journal Service.
      [    8.950026] EXT4-fs (mmcblk0p2): re-mounted 675b84e0-16af-4fea-97ce-a01fc7c7f005 r/w. Quota mode: disabled.
      [    9.142706] systemd-journald[96]: Received client request to flush runtime journal.
      [    9.158482] systemd-journald[96]: File /var/log/journal/e78604e8422c4dab8f361c14d26f7cb2/system.journal corrupted or uncleanly shut down, renaming and replacing.
      [   17.496517] Adding 102396k swap on /var/swap.  Priority:-2 extents:1 across:102396k SS
      [   17.508561] macb e000b000.ethernet eth0: PHY [e000b000.ethernet-ffffffff:00] driver [Marvell 88E1510] (irq=POLL)
      [   17.508593] macb e000b000.ethernet eth0: configuring for phy/rgmii-id link mode
      [   19.874357] ------------[ cut here ]------------
      [   19.874379] WARNING: CPU: 1 PID: 494 at drivers/gpu/drm/drm_file.c:312 drm_open_helper+0x144/0x148
      [   19.874419] Modules linked in:
      [   19.874437] CPU: 1 UID: 0 PID: 494 Comm: Xorg Not tainted 6.12.0-27064-g13b7bb744468-dirty #7
      [   19.874458] Hardware name: Xilinx Zynq Platform
      [   19.874468] Call trace:
      [   19.874481]  unwind_backtrace from show_stack+0x10/0x14
      [   19.874541]  show_stack from dump_stack_lvl+0x54/0x68
      [   19.874577]  dump_stack_lvl from __warn+0x7c/0xe0
      [   19.874613]  __warn from warn_slowpath_fmt+0x1b4/0x1bc
      [   19.874649]  warn_slowpath_fmt from drm_open_helper+0x144/0x148
      [   19.874685]  drm_open_helper from drm_open+0x8c/0x130
      [   19.874712]  drm_open from drm_stub_open+0xa4/0xc4
      [   19.874753]  drm_stub_open from chrdev_open+0xac/0x1f4
      [   19.874786]  chrdev_open from do_dentry_open+0x1cc/0x4b0
      [   19.874811]  do_dentry_open from vfs_open+0x24/0xe4
      [   19.874836]  vfs_open from path_openat+0xa24/0xf70
      [   19.874859]  path_openat from do_filp_open+0x90/0x12c
      [   19.874878]  do_filp_open from do_sys_openat2+0xb4/0xe8
      [   19.874900]  do_sys_openat2 from sys_openat+0x78/0xc4
      [   19.874927]  sys_openat from ret_fast_syscall+0x0/0x54
      [   19.874951] Exception stack(0xe0bf1fa8 to 0xe0bf1ff0)
      [   19.874969] 1fa0:                   00273158 b6f5f2c0 ffffff9c 00262b38 000a0002 00000000
      [   19.874986] 1fc0: 00273158 b6f5f2c0 00262b18 00000142 00262b38 00000000 0020c000 00273400
      [   19.875000] 1fe0: b6a0c000 bee38ad0 b69f6944 b69f6964
      [   19.875011] ---[ end trace 0000000000000000 ]---
      [   21.723359] macb e000b000.ethernet eth0: Link is Up - 1Gbps/Full - flow control off
      root@analog:~#

Useful commands for the serial terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The below commands are to be run in the serial terminal connected to the FPGA.

To find out the IP of the FPGA board, run:

.. shell::

   $ifconfig

To see the IIO devices detected, run:

.. shell::

      root@analog:~# iio_info | grep iio:device
        iio:device1: xadc
        iio:device2: axi_adc_hmcad15xx (buffer capable)

.. shell::

   $poweroff

To reboot the system, run:

.. shell::

   $reboot

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should
   be taken not to corrupt the file system -- please shut down things, don't
   just turn off the power switch. Depending on your monitor, the standard
   power off could be hiding. You can do this from the terminal as well with
   :code:`sudo shutdown -h now` or the above-mentioned command for powering off.

About the IIO devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Main receivers RX1, RX2, RX3, and RX4 are handled by the axi-adc-hmcad15xx IIO
device.

Channels:

- IIO device channel: ``axi-adc-hmcad15xx``
- Receiver inputs:

  - {``voltage0``}: RX1
  - {``voltage1``}: RX2
  - {``voltage2``}: RX3
  - {``voltage3``}: RX4
