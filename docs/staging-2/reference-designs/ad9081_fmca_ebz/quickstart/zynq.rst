.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynq

.. _ad9081_fmca_ebz quickstart zynq:

AD9081 Zynq-7000 SoC ZC706 Quick Start Guide
============================================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/ad9081-fmca-ebz-zc706.png
   :width: 600px

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the :adi:`AD9081-FMCA-EBZ`/:adi:`AD9082-FMCA-EBZ`
on:

- :xilinx:`ZC706 <ZC706>` The revision that is supported is 1.2 or higher.

Instructions on how to build the Zynq Linux kernel and devicetrees from source
can be found here:

- :dokuwiki:`Building the Zynq Linux kernel and devicetrees from source </resources/tools-software/linux-build/generic/zynq>`
- :dokuwiki:`How to build the Zynq boot image BOOT.BIN </resources/tools-software/linux-software/build-the-zynq-boot-image>`

Required Software
-----------------

- SD Card 16GB imaged using the instructions here: :ref:`kuiper`.
- Starting with our 2020_R1 release this will be included.
- Alternatively if you already have a SD-Card - download the files below.

  -  `AD9081-FMCA-EBZ-ZC706-19032021.zip <http://swdownloads.analog.com/cse/mxfe/AD9081-FMCA-EBZ-ZC706-19032021.zip>`__

- Copy next boot files from ``zynq-zc706-adv7511-ad9081`` directory or the
  download ZIP directly on sdcard ``BOOT`` partition :

  - ``BOOT.bin``
  - ``uImage``
  - ``devicetree.dtb``

- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

Required Hardware
-----------------

- Xilinx :xilinx:`ZC706 <ZC706>` board - Rev 1.2 or higher
- :adi:`AD9081-FMCA-EBZ` or :adi:`AD9082-FMCA-EBZ` FMC card
- Reference clock source (optional)
- Mini-USB cable
- Ethernet cable
- Optionally USB keyboard, mouse and a HDMI compatible monitor

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl.rst

   :start-after: .. start-#board-setup
   :end-before: .. end-#board-setup

Example Device Trees
--------------------

.. list-table::
   :header-rows: 1

   * - Function
     - File
     -
   * - dtsi
     - :git-linux:`adi-ad9081-fmc-ebz.dtsi <master:arch/arm/boot/dts/adi-ad9081-fmc-ebz.dtsi>`
     -
   * - dts
     - :git-linux:`socfpga_arria10_socdk_ad9081.dts <master:arch/arm/boot/dts/socfpga_arria10_socdk_ad9081.dts>`
     -
   * - dts
     - :git-linux:`socfpga_arria10_socdk_ad9081_np12.dts <master:arch/arm/boot/dts/socfpga_arria10_socdk_ad9081_np12.dts>`
     -
   * - dts
     - :git-linux:`zynq-zc706-adv7511-ad9081-np12.dts <master:arch/arm/boot/dts/zynq-zc706-adv7511-ad9081-np12.dts>`
     -
   * - dts
     - :git-linux:`zynq-zc706-adv7511-ad9081.dts <master:arch/arm/boot/dts/zynq-zc706-adv7511-ad9081.dts>`
     -

Testing
-------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

.. figure:: http://www.xilinx.com/images/product-images/zc706-base-board.jpg

- Connect the :adi:`AD9081-FMCA-EBZ` or :adi:`AD9082-FMCA-EBZ` FMC board to the
  FPGA carrier // HPC FMC // socket.
- Connect USB UART (Mini USB) to your host PC.
- Insert SD card into socket.
- Configure ZC706 for SD BOOT (Set the jumpers: The main one is: SW11 - Big Blue
  Switch in the middle, which controls the Boot Mode, it needs to be set: 1:
  Down, 2: Down, 3: Up, 4: Up, 5: Down.
- Turn on the power switch on the FPGA board.
- Observe kernel and serial console messages on your terminal.

Messages
~~~~~~~~

<hidden Complete kernel boot log (Click to expand)> ::

   U-Boot 2014.07-dirty (Nov 20 2014 - 17:07:55)

   Board:  Xilinx Zynq
   I2C:   ready
   DRAM:  ECC disabled 1 GiB
   MMC:   zynq_sdhci: 0
   SF: Detected S25FL128S_64K with page size 512 Bytes, erase size 128 KiB, total 32 MiB
   In:    serial
   Out:   serial
   Err:   serial
   Net:   Gem.e000b000
   Hit any key to stop autoboot:  0
   Device: zynq_sdhci
   Manufacturer ID: 3
   OEM: 5344
   Name: SC32G
   Tran Speed: 50000000
   Rd Block Len: 512
   SD version 3.0
   High Capacity: Yes
   Capacity: 29.7 GiB
   Bus Width: 4-bit
   reading uEnv.txt
   407 bytes read in 27 ms (14.6 KiB/s)
   Loaded environment from uEnv.txt
   Importing environment from SD ...
   Running uenvcmd ...
   Copying Linux from SD to RAM...
   reading uImage
   6506856 bytes read in 580 ms (10.7 MiB/s)
   reading devicetree.dtb
   23071 bytes read in 39 ms (577.1 KiB/s)
   reading uramdisk.image.gz
   **Unable to read file uramdisk.image.gz**
   ## Booting kernel from Legacy Image at 03000000 ...
      Image Name:   Linux-5.4.0-93252-ga4800dc5737b
      Image Type:   ARM Linux Kernel Image (uncompressed)
      Data Size:    6506792 Bytes = 6.2 MiB
      Load Address: 00008000
      Entry Point:  00008000
      Verifying Checksum ... OK
   ## Flattened Device Tree blob at 02a00000
      Booting using the fdt blob at 0x2a00000
      Loading Kernel Image ... OK
      Loading Device Tree to 1fff7000, end 1ffffa1e ... OK

   Starting kernel ...

   Booting Linux on physical CPU 0x0
   Linux version 5.4.0-93252-ga4800dc5737b (michael@mhenneri-D06) (gcc version 8.2.0 (GCC)) #2881 SMP PREEMPT Fri Mar 19 16:22:37 CET 2021
   CPU: ARMv7 Processor [413fc090] revision 0 (ARMv7), cr=18c5387d
   CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   OF: fdt: Machine model: Xilinx Zynq ZC706
   OF: fdt: earlycon: stdout-path /amba@0/uart@E0001000 not found
   Memory policy: Data cache writealloc
   cma: Reserved 128 MiB at 0x38000000
   percpu: Embedded 15 pages/cpu s29516 r8192 d23732 u61440
   Built 1 zonelists, mobility grouping on.  Total pages: 260608
   Kernel command line: console=ttyPS0,115200 root=/dev/mmcblk0p2 rw earlycon rootfstype=ext4 rootwait clk_ignore_unused cpuidle.off=1
   Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
   Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
   mem auto-init: stack:off, heap alloc:off, heap free:off
   Memory: 888452K/1048576K available (9216K kernel code, 743K rwdata, 7044K rodata, 1024K init, 162K bss, 29052K reserved, 131072K cma-reserved, 131072K highmem)
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
   random: get_random_bytes called from start_kernel+0x2cc/0x454 with crng_init=0
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
   Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
   Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
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
   jesd204: created con: id=0, topo=0, link=0, /amba/spi@e0007000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-tx@44b60000
   jesd204: created con: id=1, topo=0, link=2, /amba/spi@e0007000/hmc7044@0 <-> /fpga-axi@0/axi-adxcvr-rx@44a60000
   jesd204: created con: id=2, topo=0, link=0, /fpga-axi@0/axi-adxcvr-tx@44b60000 <-> /fpga-axi@0/axi-jesd204-tx@44b90000
   jesd204: created con: id=3, topo=0, link=2, /fpga-axi@0/axi-adxcvr-rx@44a60000 <-> /fpga-axi@0/axi-jesd204-rx@44a90000
   jesd204: created con: id=4, topo=0, link=0, /fpga-axi@0/axi-jesd204-tx@44b90000 <-> /fpga-axi@0/axi-ad9081-tx-hpc@44b10000
   jesd204: created con: id=5, topo=0, link=2, /fpga-axi@0/axi-jesd204-rx@44a90000 <-> /fpga-axi@0/axi-ad9081-rx-hpc@44a10000
   jesd204: created con: id=6, topo=0, link=2, /fpga-axi@0/axi-ad9081-rx-hpc@44a10000 <-> /amba/spi@e0006000/ad9081@0
   jesd204: created con: id=7, topo=0, link=0, /fpga-axi@0/axi-ad9081-tx-hpc@44b10000 <-> /amba/spi@e0006000/ad9081@0
   jesd204: /amba/spi@e0006000/ad9081@0: JESD204[2] transition uninitialized -> initialized
   jesd204: /amba/spi@e0006000/ad9081@0: JESD204[0] transition uninitialized -> initialized
   jesd204: found 8 devices and 1 topologies
   FPGA manager framework
   Advanced Linux Sound Architecture Driver Initialized.
   clocksource: Switched to clocksource arm_global_timer
   thermal_sys: Registered thermal governor 'step_wise'
   NET: Registered protocol family 2
   tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 6144 bytes, linear)
   TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
   TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
   TCP: Hash tables configured (established 8192 bind 8192)
   UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
   UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
   NET: Registered protocol family 1
   hw perfevents: no interrupt-affinity property for /pmu@f8891000, guessing.
   hw perfevents: enabled with armv7_cortex_a9 PMU driver, 7 counters available
   workingset: timestamp_bits=30 max_order=18 bucket_order=0
   bounce: pool size: 64 pages
   io scheduler mq-deadline registered
   io scheduler kyber registered
   zynq-pinctrl 700.pinctrl: zynq pinctrl initialized
   dma-pl330 f8003000.dmac: Loaded driver for PL330 DMAC-241330
   dma-pl330 f8003000.dmac:        DBUFF-128x8bytes Num_Chans-8 Num_Peri-4 Num_Events-16
   brd: module loaded
   loop: module loaded
   Registered mathworks_ip class
   spi-nor spi2.0: found s25fl128s1, expected n25q128a11
   random: fast init done
   spi-nor spi2.0: s25fl128s1 (32768 Kbytes)
   5 fixed-partitions partitions found on MTD device spi2.0
   Creating 5 MTD partitions on "spi2.0":
   0x000000000000-0x000000500000 : "boot"
   0x000000500000-0x000000520000 : "bootenv"
   0x000000520000-0x000000540000 : "config"
   0x000000540000-0x000000fc0000 : "image"
   0x000000fc0000-0x000002000000 : "spare"
   MACsec IEEE 802.1AE
   libphy: Fixed MDIO Bus: probed
   tun: Universal TUN/TAP device driver, 1.6
   libphy: MACB_mii_bus: probed
   Marvell 88E1116R e000b000.ethernet-ffffffff:07: attached PHY driver [Marvell 88E1116R] (mii_bus:phy_addr=e000b000.ethernet-ffffffff:07, irq=POLL)
   macb e000b000.ethernet eth0: Cadence GEM rev 0x00020118 at 0xe000b000 irq 29 (00:0a:35:00:01:22)
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
   usb usb1: Manufacturer: Linux 5.4.0-93252-ga4800dc5737b ehci_hcd
   usb usb1: SerialNumber: ci_hdrc.0
   hub 1-0:1.0: USB hub found
   hub 1-0:1.0: 1 port detected
   i2c /dev entries driver
   si570 1-005d: registered, current frequency 156250000 Hz
   i2c i2c-0: Added multiplexed i2c bus 1
   adv7511 2-0039: 2-0039 supply avdd not found, using dummy regulator
   adv7511 2-0039: 2-0039 supply dvdd not found, using dummy regulator
   adv7511 2-0039: 2-0039 supply pvdd not found, using dummy regulator
   adv7511 2-0039: 2-0039 supply bgvdd not found, using dummy regulator
   adv7511 2-0039: 2-0039 supply dvdd-3v not found, using dummy regulator
   i2c i2c-0: Added multiplexed i2c bus 2
   at24 3-0054: 1024 byte 24c08 EEPROM, writable, 1 bytes/write
   i2c i2c-0: Added multiplexed i2c bus 3
   pca953x 4-0021: 4-0021 supply vcc not found, using dummy regulator
   i2c i2c-0: Added multiplexed i2c bus 4
   rtc-pcf8563 5-0051: registered as rtc0
   i2c i2c-0: Added multiplexed i2c bus 5
   at24 6-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
   i2c i2c-0: Added multiplexed i2c bus 6
   i2c i2c-0: Added multiplexed i2c bus 7
   i2c i2c-0: Added multiplexed i2c bus 8
   pca954x 0-0074: registered 8 multiplexed busses for I2C switch pca9548
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
   mmc0: new high speed SDHC card at address aaaa
   mmcblk0: mmc0:aaaa SC32G 29.7 GiB
   jesd204: /amba/spi@e0007000/hmc7044@0,jesd204:1,parent=spi1.0: Using as SYSREF provider
    mmcblk0: p1 p2 p3
   axi_adxcvr 44a60000.axi-adxcvr-rx: adxcvr_enforce_settings: Using QPLL without access, assuming desired Lane rate will be configured by a different instance
   axi_adxcvr 44a60000.axi-adxcvr-rx: AXI-ADXCVR-RX (17.01.a) using QPLL on GTX2 at 0x44A60000. Number of lanes: 4.
   axi_adxcvr 44b60000.axi-adxcvr-tx: AXI-ADXCVR-TX (17.01.a) using QPLL on GTX2 at 0x44B60000. Number of lanes: 4.
   axi-jesd204-rx 44a90000.axi-jesd204-rx: AXI-JESD204-RX (1.07.a) at 0x44A90000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
   axi-jesd204-tx 44b90000.axi-jesd204-tx: AXI-JESD204-TX (1.06.a) at 0x44B90000. Encoder 8b10b, width 4/4, lanes 4, jesd204-fsm.
   axi_sysid 45000000.axi-sysid-0: AXI System ID core version (1.01.a) found
   axi_sysid 45000000.axi-sysid-0: [ad9081_fmca_ebz] on [zc706] git branch <master> git <1099badaf4f3621f9db1723a17d0dcd3dc74e26b> clean [2021-03-08 14:35:28] UTC
   fpga_manager fpga0: Xilinx Zynq FPGA Manager registered
   usbcore: registered new interface driver snd-usb-audio
   NET: Registered protocol family 10
   Segment Routing with IPv6
   sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
   NET: Registered protocol family 17
   NET: Registered protocol family 36
   Registering SWP/SWPB emulation handler
   [drm] Cannot find any crtc or sizes
   [drm] Initialized axi_hdmi_drm 1.0.0 20120930 for 70e00000.axi_hdmi on minor 0
   ad9081 spi0.0: AD9081 Rev. 3 Grade 10 (API 1.1.0) probed
   cf_axi_dds 44b10000.axi-ad9081-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x44B10000 mapped to 0x(ptrval), probed DDS AD9081
   asoc-simple-card adv7511_hdmi_snd: spdif-hifi <-> 75c00000.axi-spdif-tx mapping ok
   cf_axi_adc 44a10000.axi-ad9081-rx-hpc: ADI AIM (10.01.b) at 0x44A10000 mapped to 0x(ptrval), probed ADC AD9081 as MASTER
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition initialized -> probed
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition initialized -> probed
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition probed -> idle
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition probed -> idle
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition idle -> device_init
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition idle -> device_init
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition device_init -> link_init
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition device_init -> link_init
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_init -> link_supported
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_init -> link_supported
   hmc7044 spi1.0: hmc7044_jesd204_link_pre_setup: Link2 forcing continuous SYSREF mode
   hmc7044 spi1.0: hmc7044_jesd204_link_pre_setup: Link0 forcing continuous SYSREF mode
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_supported -> link_pre_setup
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_supported -> link_pre_setup
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_pre_setup -> clk_sync_stage1
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_pre_setup -> clk_sync_stage1
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition clk_sync_stage1 -> clk_sync_stage2
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition clk_sync_stage1 -> clk_sync_stage2
   [drm] Cannot find any crtc or sizes
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition clk_sync_stage2 -> clk_sync_stage3
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition clk_sync_stage2 -> clk_sync_stage3
   [drm] Cannot find any crtc or sizes
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition clk_sync_stage3 -> link_setup
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition clk_sync_stage3 -> link_setup
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_setup -> opt_setup_stage1
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_setup -> opt_setup_stage1
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage1 -> opt_setup_stage2
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage1 -> opt_setup_stage2
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage2 -> opt_setup_stage3
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage2 -> opt_setup_stage3
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage3 -> opt_setup_stage4
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage3 -> opt_setup_stage4
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage4 -> opt_setup_stage5
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage4 -> opt_setup_stage5
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition opt_setup_stage5 -> clocks_enable
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition opt_setup_stage5 -> clocks_enable
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition clocks_enable -> link_enable
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition clocks_enable -> link_enable
   ad9081 spi0.0: JESD RX (JTX) Link2 in DATA, SYNC deasserted, PLL locked, PHASE established, MODE valid
   ad9081 spi0.0: JESD TX (JRX) Link0 0xF lanes in DATA
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_enable -> link_running
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_enable -> link_running
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[2] transition link_running -> opt_post_running_stage
   jesd204: /amba/spi@e0006000/ad9081@0,jesd204:0,parent=spi0.0: JESD204[0] transition link_running -> opt_post_running_stage
   input: gpio_keys as /devices/soc0/gpio_keys/input/input0
   rtc-pcf8563 5-0051: setting system clock to 2021-03-19T15:24:20 UTC (1616167460)
   clk: Not disabling unused clocks
   ALSA device list:
     #0: HDMI monitor
   EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
   VFS: Mounted root (ext4 filesystem) on device 179:2.
   devtmpfs: mounted
   Freeing unused kernel memory: 1024K
   Run /sbin/init as init process
   systemd[1]: Failed to lookup module alias 'autofs4': Function not implemented
   systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2)
   systemd[1]: Detected architecture arm.

   Welcome to Kuiper GNU/Linux 10 (buster)!

   systemd[1]: Set hostname to <analog>.
   systemd[1]: File /lib/systemd/system/systemd-journald.service:12 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
   systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
   systemd[1]: /etc/systemd/system/tof-server.service:1: Assignment outside of section. Ignoring.
   systemd[1]: /etc/systemd/system/tof-server.service:2: Assignment outside of section. Ignoring.
   random: systemd: uninitialized urandom read (16 bytes read)
   random: systemd: uninitialized urandom read (16 bytes read)
   systemd[1]: Reached target Swap.
   [  OK  ] Reached target Swap.
   random: systemd: uninitialized urandom read (16 bytes read)
   systemd[1]: Started Forward Password Requests to Wall Directory Watch.
   [  OK  ] Started Forward Password R�…uests to Wall Directory Watch.
   systemd[1]: Listening on Journal Socket (/dev/log).
   [  OK  ] Listening on Journal Socket (/dev/log).
   [  OK  ] Listening on Journal Socket.
            Starting Set the console keyboard layout...
            Starting Load Kernel Modules...
   [  OK  ] Created slice User and Session Slice.
   [  OK  ] Listening on Syslog Socket.
            Mounting RPC Pipe File System...
   [  OK  ] Listening on udev Control Socket.
   [  OK  ] Created slice system-getty.slice.
   [  OK  ] Listening on fsck to fsckd communication Socket.
   [  OK  ] Created slice system-serial\x2dgetty.slice.
   [  OK  ] Created slice system-systemd\x2dfsck.slice.
            Starting Restore / save the current clock...
   [  OK  ] Listening on udev Kernel Socket.
            Starting udev Coldplug all Devices...
            Starting Journal Service...
   [  OK  ] Listening on initctl Compatibility Named Pipe.
   [  OK  ] Reached target Slices.
            Mounting Kernel Debug File System...
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Started Set the console keyboard layout.
   [  OK  ] Started Journal Service.
   [FAILED] Failed to mount RPC Pipe File System.
   See 'systemctl status run-rpc_pipefs.mount' for details.
   [DEPEND] Dependency failed for RPC �…curity service for NFS server.
   [DEPEND] Dependency failed for RPC �…ice for NFS client and server.
   [  OK  ] Started Restore / save the current clock.
   [  OK  ] Mounted Kernel Debug File System.
            Starting Remount Root and Kernel File Systems...
   [  OK  ] Reached target NFS client services.
   [  OK  ] Reached target Remote File Systems (Pre).
   [  OK  ] Reached target Remote File Systems.
            Mounting Kernel Configuration File System..random: crng init done
   random: 7 urandom warning(s) missed due to ratelimiting
   .
            Starting Apply Kernel Variables...
   [  OK  ] Mounted Kernel Configuration File System.
   [  OK  ] Started udev Coldplug all Devices.
   [  OK  ] Started Apply Kernel Variables.
            Starting Helper to synchronize boot up for ifupdown...
   [  OK  ] Started Helper to synchronize boot up for ifupdown.
   [  OK  ] Started Remount Root and Kernel File Systems.
            Starting Create System Users...
            Starting Flush Journal to Persistent Storage...
            Starting Load/Save Random Seed...
   [  OK  ] Started Create System Users.
   [  OK  ] Started Load/Save Random Seed.
            Starting Create Static Device Nodes in /dev...
   [  OK  ] Started Flush Journal to Persistent Storage.
   [  OK  ] Started Create Static Device Nodes in /dev.
            Starting udev Kernel Device Manager...
   [  OK  ] Reached target Local File Systems (Pre).
   [  OK  ] Started udev Kernel Device Manager.
            Starting Show Plymouth Boot Screen...
   [  OK  ] Started Show Plymouth Boot Screen.
   [  OK  ] Reached target Local Encrypted Volumes.
   [  OK  ] Started Forward Password R�…s to Plymouth Directory Watch.
            Starting Load Kernel Modules...
   [  OK  ] Found device /dev/ttyPS0.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Found device /dev/disk/by-partuuid/18f1f9d5-01.
            Starting File System Check�…isk/by-partuuid/18f1f9d5-01...
   [  OK  ] Started File System Check Daemon to report status.
   [  OK  ] Started File System Check �…/disk/by-partuuid/18f1f9d5-01.
            Mounting /boot...
   [  OK  ] Mounted /boot.
   [  OK  ] Reached target Local File Systems.
            Starting Raise network interfaces...
            Starting Tell Plymouth To Write Out Runtime Data...
            Starting Set console font and keymap...
            Starting Create Volatile Files and Directories...
            Starting Preprocess NFS configuration...
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [  OK  ] Started Preprocess NFS configuration.
   [  OK  ] Started Set console font and keymap.
   [  OK  ] Started Create Volatile Files and Directories.
            Starting Update UTMP about System Boot/Shutdown...
            Starting Network Time Synchronization...
   [  OK  ] Started Update UTMP about System Boot/Shutdown.
            Starting Load Kernel Modules...
            Starting Tell Plymouth To Write Out Runtime Data...
   [  OK  ] Started Network Time Synchronization.
   [  OK  ] Started Raise network interfaces.
   [  OK  ] Started Tell Plymouth To Write Out Runtime Data.
   [FAILED] Failed to start Load Kernel Modules.
   See 'systemctl status systemd-modules-load.service' for details.
   [  OK  ] Reached target System Time Synchronized.
   [  OK  ] Reached target System Initialization.
   [  OK  ] Listening on D-Bus System Message Bus Socket.
   [  OK  ] Started Daily rotation of log files.
   [  OK  ] Started Daily apt download activities.
   [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
   [  OK  ] Listening on triggerhappy.socket.
   [  OK  ] Listening on GPS (Global P�…ioning System) Daemon Sockets.
   [  OK  ] Listening on CUPS Scheduler.
   [  OK  ] Reached target Sockets.
   [  OK  ] Started Daily Cleanup of Temporary Directories.
   [  OK  ] Started Daily man-db regeneration.
   [  OK  ] Started Daily apt upgrade and clean activities.
   [  OK  ] Reached target Timers.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Reached target Paths.
   [  OK  ] Reached target Basic System.
   [  OK  ] Started D-Bus System Message Bus.
   [  OK  ] Started tof-server.service.
            Starting Avahi mDNS/DNS-SD Stack...
            Starting rng-tools.service...
            Starting dhcpcd on all interfaces...
            Starting WPA supplicant...
            Starting Login Service...
   [  OK  ] Started Regular background program processing daemon.
   [  OK  ] Started CUPS Scheduler.
   [  OK  ] Started Manage Sound Card State (restore and store).
            Starting LSB: Switch to on�…nless shift key is pressed)...
            Starting System Logging Service...
            Starting Check for Raspberry Pi EEPROM updates...
            Starting Disk Manager...
            Starting Save/Restore Sound Card State...
            Starting dphys-swapfile - �…unt, and delete a swap file...
            Starting triggerhappy global hotkey daemon...
            Starting Modem Manager...
   [  OK  ] Started System Logging Service.
   [  OK  ] Started triggerhappy global hotkey daemon.
   [FAILED] Failed to start rng-tools.service.
   See 'systemctl status rng-tools.service' for details.
   [  OK  ] Started dhcpcd on all interfaces.
   [  OK  ] Started Check for Raspberry Pi EEPROM updates.
   [  OK  ] Started Save/Restore Sound Card State.
   [  OK  ] Reached target Sound Card.
   [  OK  ] Started Login Service.
   [  OK  ] Started Avahi mDNS/DNS-SD Stack.
   [  OK  ] Started WPA supplicant.
            Starting Authorization Manager...
   [  OK  ] Reached target Network.
            Starting OpenBSD Secure Shell server...
            Starting Permit User Sessions...
            Starting HTTP based time synchronization tool...
            Starting /etc/rc.local Compatibility...
   [  OK  ] Started IIO Daemon.
   [  OK  ] Started Make remote CUPS printers available locally.
   [  OK  ] Started LSB: Switch to ond�…(unless shift key is pressed).
   [  OK  ] Started HTTP based time synchronization tool.
   [  OK  ] Started Permit User Sessions.
   [  OK  ] Started /etc/rc.local Compatibility.
   [  OK  ] Started dphys-swapfile - s�…mount, and delete a swap file.
            Starting Light Display Manager...
            Starting Hold until boot process finishes up...
   [  OK  ] Started Authorization Manager.
   [  OK  ] Started OpenBSD Secure Shell server.
   [  OK  ] Started Modem Manager.

   Raspbian GNU/Linux 10 analog ttyPS0

   analog login: root (automatic login)

   Last login: Fri Mar 19 15:23:10 GMT 2021 on ttyPS0
   Linux analog 5.4.0-93252-ga4800dc5737b #2881 SMP PREEMPT Fri Mar 19 16:22:37 CET 2021 armv7l

   The programs included with the Debian GNU/Linux system are free software;
   the exact distribution terms for each program are described in the
   individual files in /usr/share/doc/*/copyright.

   Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
   permitted by applicable law.
   root@analog:~#

</hidden>

Login Information

- user: analog
- password: analog

These devices should be present:

::

   root@analog:~# iio_info | grep iio:device
           iio:device0: xadc
           iio:device1: hmc7044
           iio:device2: axi-ad9081-tx-hpc (buffer capable)
           iio:device3: axi-ad9081-rx-hpc (buffer capable)

All links should be in ``DATA`` without errors:

::

   root@analog:~# jesd_status -s
     (DEVICES) Found 2 JESD204 Link Layer peripherals

     (0): axi-jesd204-rx/44a90000.axi-jesd204-rx  [*]
     (1): axi-jesd204-tx/44b90000.axi-jesd204-tx

     (STATUS)
     Link is                 enabled
     Link Status
     Measured Link Clock     250.003
     Reported Link Clock     250.000
     Lane rate
     Lane rate / 40
     LMFC rate
     SYSREF captured
     SYSREF alignment error
     SYNC~

     (LANE STATUS)
     Lane#                             0      1      2      3
     Errors                            1      0      0      1
     Latency (Multiframes/Octets)      1/33   1/34   1/32   1/32
     CGS State                         DATA   DATA   DATA   DATA
     Initial Frame Sync                Yes    Yes    Yes    Yes
     Initial Lane Alignment Sequence   Yes    Yes    Yes    Yes

    F1axi-jesd204-rx/44a90000.axi-jesd204-rxF2axi-jesd204-tx/44b90000.axi-jesd204-txF9Quit

More info on
:dokuwiki:`JESD204 Status Application </resources/tools-software/linux-software/jesd_status>`
can be found there.

Pyadi-iio Example
~~~~~~~~~~~~~~~~~

Pyadi-iio is a python abstraction module for ADI hardware with IIO drivers to
make them easier to use. For more check
`Pyadi-iio <https://github.com/analogdevicesinc/pyadi-iio>`__. An example of
using AD9081 can be checked :git-pyadi-iio:`here <examples/ad9081_example.py+>`

IIO Oscilloscope Remote
~~~~~~~~~~~~~~~~~~~~~~~

Please see also
here:`Oscilloscope </resources/tools-software/linux-software/iio_oscilloscope>`__

The IIO Oscilloscope application can be used locally on FPGA platforms featuring
a graphical desktop environment such as ZCU102 or ZC706 or remote using a
network connection.

When using the remote option, once you logged in to the Linux terminal you need
to check the IP address of the using the ifconfig command to see if there was
any address assigned by a DHCP server. If not, you need to manually set an
address with ifconfig in the same address space your PC is using.

Once the IIO Osc application is launched goto Settings -> Connect and enter the
IP address of the target in the popup window.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/osc.png

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/ad9081_iio_osc.rst

.. todo:: .. include: /resources/tools-software/linux-software/ad9081_plugin.rst

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

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/common.rst

   :start-after: .. start-#useful-links
   :end-before: .. end-#useful-links

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/common.rst

   :start-after: .. start-#support
   :end-before: .. end-#support
