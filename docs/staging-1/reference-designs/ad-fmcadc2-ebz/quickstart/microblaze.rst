.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcadc2-ebz/quickstart/microblaze

.. _ad-fmcadc2-ebz quickstart microblaze:

AD-FMCADC2-EBZ Microblaze Quick Start Guide
===========================================

.. warning::

   Support for the ad-fmcadc2-ebz was discontinued starting with 2022_R2 Kuiper
   Linux release and it is not supported in the later releases. Last release in
   which pre-build files can be found is 2021_r2. Check this
   :dokuwiki:`link </resources/tools-software/linux-software/adi-kuiper_images/release_notes>`
   to see all Kuiper releases. The HDL project source code can still be found on
   :git-hdl:`hdl_2021_r2 <tree/hdl_2021_r2/projects/fmcadc2+>` release branch.

This guide provides some quick instructions (still takes awhile to download, and
set things up) on how to setup the AD-FMCADC2-EBZ on:

- :xilinx:`VC707 <VC707>`

Required Software
-----------------

- Bitfile and Linux ELF image.
- Xilinx ISE Microprocessor Debugger (XMD) is sufficient for the demo.
- A UART terminal (Tera Term/Hyperterminal), Baud rate 115200 (8N1).

Required Hardware
-----------------

- Xilinx VC707
- AD-FMCADC2-EBZ FMC Board.
- Micro / Mini-USB Cable

Testing
-------

- Connect the AD-FMCADC2-EBZ FMC board to the FPGA carrier, on the VC707: FMC1
  HPC connector.
- Connect USB JTAG (Micro USB) to your host PC.
- Turn on the power switch on the FPGA board.
- Open XMD console to configure the FPGA and download the elf image.

Loading
~~~~~~~

.. todo:: .. include: /resources/tools-software/linux-drivers/platforms/microblaze_loading.rst

   :start-after: .. start-loading
   :end-before: .. end-loading

Messages
~~~~~~~~

.. todo:: .. include: /resources/tools-software/linux-drivers/platforms/microblaze_loading.rst

   :start-after: .. start-messages
   :end-before: .. end-messages

::

   Early console on uartlite at 0x40600000
   bootconsole [earlyser0] enabled
   Ramdisk addr 0x00000000,
   Compiled-in FDT at 80323fe8
   Linux version 3.17.0-126736-gdf1ca8f-dirty (michael@mhenneri-D04) (gcc version 4.8.3 20140131 (prerelease) (crosstool-NG 1.18.0) ) #1947 Wed Dec 17 11:04:20 CET 2014
   setup_cpuinfo: initialising
   setup_cpuinfo: Using full CPU PVR support
   wt_msr_noirq
   setup_memory: max_mapnr: 0x30000
   setup_memory: min_low_pfn: 0x80000
   setup_memory: max_low_pfn: 0xb0000
   setup_memory: max_pfn: 0xb0000
   Zone ranges:
     DMA      [mem 0x80000000-0xafffffff]
     Normal   empty
   Movable zone start for each node
   Early memory node ranges
     node   0: [mem 0x80000000-0xbfffffff]
   On node 0 totalpages: 196608
   free_area_init_node: node 0, pgdat 8040751c, node_mem_map 81000000
     DMA zone: 1536 pages used for memmap
     DMA zone: 0 pages reserved
     DMA zone: 196608 pages, LIFO batch:31
   early_printk_console remapping from 0x40600000 to 0xffffd000
   pcpu-alloc: s0 r0 d32768 u32768 alloc=1*32768
   pcpu-alloc: [0] 0
   Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 195072
   Kernel command line: console=ttyUL0,115200
   PID hash table entries: 4096 (order: 2, 16384 bytes)
   Dentry cache hash table entries: 131072 (order: 7, 524288 bytes)
   Inode-cache hash table entries: 65536 (order: 6, 262144 bytes)
   Memory: 768436K/786432K available (3215K kernel code, 148K rwdata, 724K rodata, 5988K init, 86K bss, 17996K reserved)
   Kernel virtual memory layout:
     * 0xffffe000..0xfffff000  : fixmap
     * 0xffffd000..0xffffe000  : early ioremap
     * 0xb0000000..0xffffd000  : vmalloc & ioremap
   NR_IRQS:128
   /axi@0/axi-intc@41200000: num_irq=15, edge=0x3810
   /axi@0/axi-timer@41c00000: irq=1
   xilinx_timer_set_mode: shutdown
   xilinx_timer_set_mode: periodic
   sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 42949672950ns
   Calibrating delay loop... 49.35 BogoMIPS (lpj=246784)
   pid_max: default: 32768 minimum: 301
   Mount-cache hash table entries: 2048 (order: 1, 8192 bytes)
   Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes)
   devtmpfs: initialized
   regulator-dummy: no parameters
   NET: Registered protocol family 16
   Switched to clocksource xilinx_clocksource
   xilinx_timer_set_mode: oneshot
   NET: Registered protocol family 2
   TCP established hash table entries: 8192 (order: 3, 32768 bytes)
   TCP bind hash table entries: 8192 (order: 3, 32768 bytes)
   TCP: Hash tables configured (established 8192 bind 8192)
   TCP: reno registered
   UDP hash table entries: 512 (order: 1, 8192 bytes)
   UDP-Lite hash table entries: 512 (order: 1, 8192 bytes)
   NET: Registered protocol family 1
   RPC: Registered named UNIX socket transport module.
   RPC: Registered udp transport module.
   RPC: Registered tcp transport module.
   RPC: Registered tcp NFSv4.1 backchannel transport module.
   XGpio: /axi@0/gpio@40030000: registered, base is 254
   XGpio: /axi@0/gpio@40020000: registered, base is 241
   XGpio: /axi@0/gpio@40020000: dual channel registered, base is 233
   Skipping unavailable RESET gpio -2 (reset)
   futex hash table entries: 256 (order: -1, 3072 bytes)
   jffs2: version 2.2. (NAND) (SUMMARY)  ?© 2001-2006 Red Hat, Inc.
   msgmni has been set to 1500
   Block layer SCSI generic (bsg) driver version 0.4 loaded (major 253)
   io scheduler noop registered
   io scheduler deadline registered
   io scheduler cfq registered (default)
   Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
   40600000.serial: ttyUL0 at MMIO 0x40600000 (irq = 36, base_baud = 0) is a uartlite
   console [ttyUL0] enabled
   console [ttyUL0] enabled
   bootconsole [earlyser0] disabled
   bootconsole [earlyser0] disabled
   of_serial 41400000.serial: Unknown serial port found, ignored
   brd: module loaded
   Xilinx SystemACE device driver, major=254
   xilinx_lcd 40010000.gpio_lcd: Device Tree Probing 'gpio_lcd'
   xilinx_lcd 40010000.gpio_lcd: LCD 0x40010000 mapped to 0xb0160000
   60000000.axi-emc: Found 1 x16 devices at 0x0 in 16-bit bank. Manufacturer ID 0x000089 Chip ID 0x0088b0
   NOR chip too large to fit in mapping. Attempting to cope...
   Intel/Sharp Extended Query Table at 0x010A
   Intel/Sharp Extended Query Table at 0x010A
   Intel/Sharp Extended Query Table at 0x010A
   Intel/Sharp Extended Query Table at 0x010A
   Intel/Sharp Extended Query Table at 0x010A
   Using buffer write method
   Using auto-unlock on power-up/resume
   cfi_cmdset_0001: Erase suspend on write enabled
   erase region 0: offset=0x0,size=0x40000,blocks=512
   60000000.axi-emc: program region size/ctrl_valid/ctrl_inval = 1024/16/16
   60000000.axi-emc: 1 set(s) of 1 interleaved chips --> 8 partitions of 16384 KiB
   Reducing visibility of 131072KiB chip to 32768KiB
   4 ofpart partitions found on MTD device 60000000.axi-emc
   Creating 4 MTD partitions on "60000000.axi-emc":
   0x000000000000-0x000001380000 : "fpga"
   0x000001380000-0x000001400000 : "boot"
   0x000001400000-0x000001440000 : "bootenv"
   0x000001440000-0x000002000000 : "image"
   xilinx_spi 44a70000.axi-quad-spi: at 0x44A70000 mapped to 0xb21a0000, irq=13
   libphy: Fixed MDIO Bus: probed
   xilinx_axienet 40e00000.network: TX_CSUM 2
   xilinx_axienet 40e00000.network: RX_CSUM 2
   libphy: Xilinx Axi Ethernet MDIO: probed
   i2c /dev entries driver
   i2c i2c-0: Added multiplexed i2c bus 1
   at24 2-0050: 256 byte 24c02 EEPROM, writable, 1 bytes/write
   at24 2-0054: 256 byte 24c02 EEPROM, writable, 1 bytes/write
   i2c i2c-0: Added multiplexed i2c bus 2
   i2c i2c-0: Added multiplexed i2c bus 3
   i2c i2c-0: Added multiplexed i2c bus 4
   i2c i2c-0: Added multiplexed i2c bus 5
   i2c i2c-0: Added multiplexed i2c bus 6
   i2c i2c-0: Added multiplexed i2c bus 7
   i2c i2c-0: Added multiplexed i2c bus 8
   pca954x 0-0074: registered 8 multiplexed busses for I2C switch pca9548
   platform 44a10000.axi-ad9625: Driver cf_axi_adc requests probe deferral
   spi spi32766.0: Driver ad9467 requests probe deferral
   platform 44a91000.axi-jesd204b-rx: Driver cf_axi_jesd204b_v51 requests probe deferral
   cf_axi_jesd204b_gt 44a60000.axi-jesd-gt-rx: AXI-JESD204B (6.00.b) at 0x44A60000 mapped to 0xb2260000,
   TCP: cubic registered
   NET: Registered protocol family 17
   platform 44a10000.axi-ad9625: Driver cf_axi_adc requests probe deferral
   spi spi32766.0: Driver ad9467 requests probe deferral
   cf_axi_jesd204b_v51 44a91000.axi-jesd204b-rx: AXI-JESD204B 5.2 Rev 1, at 0x44A91000 mapped to 0xb0032000,
   platform 44a10000.axi-ad9625: Driver cf_axi_adc requests probe deferral
   ad9467 spi32766.0: AD9625 PLL LOCKED
   cf_axi_adc 44a10000.axi-ad9625: ADI AIM (8.00.b) at 0x44A10000 mapped to 0xb22a0000, probed ADC AD9625 as MASTER
   Freeing unused kernel memory: 5988K (80409000 - 809e2000)
   Starting logging: OK
   Starting network...
   Starting network...
   udhcpc (v1.22.1) started
   net eth0: Promiscuous mode disabled.
   net eth0: Promiscuous mode disabled.
   Sending discover...
   xilinx_axienet 40e00000.network eth0: Link is Down
   xilinx_axienet 40e00000.network eth0: Link is Up - 100Mbps/Full - flow control off
   Sending discover...
   Sending select for 10.44.2.131...
   Lease of 10.44.2.131 obtained, lease time 86400
   deleting routers
   adding dns 10.32.51.110
   adding dns 10.64.53.110
   random: ssh-keygen urandom read with 45 bits of entropy available
   Starting sshd: OK
   Starting IIO Server Daemon: OK

   Welcome to Buildroot
   buildroot login: root
   Password:
   ~ #

IIO Oscilloscope Remote
~~~~~~~~~~~~~~~~~~~~~~~

Please see also
here:`Oscilloscope </resources/tools-software/linux-software/iio_oscilloscope>`__

The IIO Oscilloscope application can be used to connect to another platform that
has a connected device in order to configure the device and read data from it.

Build and start osc on a network enabled Linux host.

Once the application is launched goto Settings -> Connect and enter the IP
address of the target in the popup window.
