.. _fmcomms8 quickstart a10soc:

Arria10 SoC Quick start
===============================================================================

.. image:: ../../images/a10soc_marked.png
   :width: 800

This guide provides quick instructions on how to setup the
:adi:`EVAL-AD-FMCOMMS8-EBZ` on:

- :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
  (Rev. C or later) on FMCA

.. esd-warning::

Using Linux as software
-------------------------------------------------------------------------------

Necessary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   For Intel SoC-FPGA boards, one boot file must be written to the third SD
   card partition, which is not accessible from Windows. You will need either
   a native Linux system or WSL to properly configure the SD card. For detailed
   file placement instructions, refer to
   :external+hdl:ref:`Using Kuiper Linux pre-built images <build_intel_boot_image>`.
   On the Kuiper image, the **zImage** file and the **extlinux.conf** file can
   be found in the carrier-specific folder, which is common to all projects that
   use this carrier. All remaining boot files are located in the project-specific
   folder. The **extlinux** directory is not provided and must be created by the user.

The following files are needed for the system to boot:

- HDL boot image: ``fit_spl_fpga.itb``
- Linux Kernel image: ``zImage``
- Linux device tree: ``socfpga_arria10_socdk_sdmmc.dtb``
- U-Boot image: ``u-boot.img``
- ``extlinux.conf`` in the **extlinux** folder from SD Card
- Write ``u-boot-splx4.sfp`` on **third** SD Card partition:

Instructions on how to manually build the boot files from source can be found
here:

- :external+hdl:ref:`Building the Intel SoC-FPGA kernel and devicetrees from source <build_intel_boot_image>`
- :external+hdl:ref:`fmcomms8` build documentation.
  More HDL build details at :external+hdl:ref:`build_hdl`.

Required software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- SD Card 16GB imaged using the instructions here:
  :external+kuiper:doc:`Kuiper Linux <index>`
- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)

Required hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
  (Rev. C or later) FPGA board and its power supply
- :adi:`EVAL-AD-FMCOMMS8-EBZ` FMC evaluation board
- MicroSD card with at least 16GB of memory
- Mini-USB cable (UART)
- LAN cable (Ethernet)
- 4x UFL cables
- (Optional) USB keyboard & mouse and a HDMI compatible monitor

More details as to why you need these, can be found at
:ref:`fmcomms8 prerequisites`.

.. _fmcomms8 soc-changes:

A10SoC required hardware changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

   The following rework is required on the A10SoC FPGA:

   To avoid using an external clock source and fully rely on the
   :adi:`HMC7044` clock chip, rotate the C6D/C4D caps in C5D/C3D position.
   (Please note: In the latest version of the board, this is now the default
   configuration, so this configuration step might not be needed anymore).

   If LEDS V1P0_LED and VINT_LED are not on please depopulate R22M and
   populate R2M.

In the default configuration of the
:intel:`Arria10 SoC Development Kit <content/www/us/en/products/details/fpga/arria/10.html>`,
some of the FMC header pins are connected to a dedicated clock chip.
To be compatible with the :adi:`EVAL-AD-FMCOMMS8-EBZ`, these pins need to be connected
directly to the FPGA.

The connection of those pins can be changed by moving the position
of six zero Ohm resistors:

- R575 to R574
- R576 to R577
- R612 to R610
- R613 to R611
- R621 to R620
- R633 to R632

These resistors can be found on the backside of the Arria10 SoC
Development Kit underneath the FMC A connector (J29). The following
picture shows the required configuration to be compatible with the
:adi:`EVAL-AD-FMCOMMS8-EBZ`.

.. image:: ../images/a10soc_fmc_rework_6r.jpg
   :align: center
   :width: 400

Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Creating the setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../images/fmcomms8_a10soc.jpeg
   :width: 900

.. esd-warning::

.. warning::

   Before executing the steps below, **VADJ for FMCA must be set to 1.8V**.
   Short pins 9 and 10 on J32 (default position).

Follow the steps in this order, to avoid damaging the components:

#. Connect the :adi:`EVAL-AD-FMCOMMS8-EBZ` FMC board to the FMCA carrier socket
   (G14).
#. Connect USB UART (Mini-USB) to your host PC (J10).
#. Insert MicroSD card into socket.
#. Configure the Arria 10 SoC Development Kit for SD card booting (set the
   jumpers and switches accordingly).
#. Connect the power supply for the FPGA.
#. Turn on the power switch on the FPGA board.
#. Observe kernel and serial console messages on your terminal.

.. seealso::
    For more detailed information on a10soc jumper configuration, check the
    *A10SoC Hardware User Guide* (chapter "Default Switch and Jumper Settings")
    `here <https://www.intel.com/content/www/us/en/content-details/641216/arria-10-soc-development-kit-user-guide.html>`__.

Boot messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is what is printed in the serial console, after you have
connected to the proper ttyUSB or COM port.

Configuring the FPGA will take a few seconds. Once the FPGA has been configured
the green D18 LED will turn on and the boot process will continue.

.. collapsible:: Complete boot log

   ::

      U-Boot 2014.10-00334-gf7a7e26-dirty (Jun 30 2021 - 18:17:34), Build: jenkins-master-hdl_jobs_for_linux-projects-fmcomms8.a10soc-125

      CPU   : Altera SOCFPGA Arria 10 Platform
      BOARD : Altera SOCFPGA Arria 10 Dev Kit
      I2C:   ready
      DRAM:  WARNING: Caches not enabled
      SOCFPGA DWMMC: 0
      FPGA: writing socfpga_arria10_socdk.rbf ...
      Full Configuration Succeeded.
      DDRCAL: Success
      INFO  : Skip relocation as SDRAM is non secure memory
      Reserving 2048 Bytes for IRQ stack at: ffe386e8
      DRAM  : 1 GiB
      WARNING: Caches not enabled
      MMC:   ** Warning - bad CRC, using default environment

      In:    serial
      Out:   serial
      Err:   serial
      Model: SOCFPGA Arria10 Dev Kit
      Net:   dwmac.ff800000
      Hit any key to stop autoboot:  0
      FPGA must be in Early Release mode to program core.
      fpga - loadable FPGA image support

         Unable to read file u-boot.scr
      7662488 bytes read in 381 ms (19.2 MiB/s)
      47522 bytes read in 17 ms (2.7 MiB/s)
      FPGA BRIDGES: enable
      Kernel image @ 0x010000 [ 0x000000 - 0x74eb98 ]
      ## Flattened Device Tree blob at 00000100
         Booting using the fdt blob at 0x000100
         Loading Device Tree to 01ff1000, end 01fff9a1 ... OK

      Starting kernel ...

      [    0.000000] Booting Linux on physical CPU 0x0
      [    0.000000] Linux version 5.4.0-00475-gc588ee4 (jenkins@romlxbuild1.adlk.analog.com) (gcc version 9.2.0 (GCC)) #1847 SMP Fri Jul 2 09:07:42 IST 2021
      [    0.000000] CPU: ARMv7 Processor [414fc091] revision 1 (ARMv7), cr=10c5387d
      [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
      [    0.000000] OF: fdt: Machine model: Altera SOCFPGA Arria 10
      [    0.000000] Memory policy: Data cache writealloc
      [    0.000000] cma: Reserved 128 MiB at 0x38000000
      [    0.000000] percpu: Embedded 19 pages/cpu s45196 r8192 d24436 u77824
      [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 260608
      [    0.000000] Kernel command line: console=ttyS0,115200 root=/dev/mmcblk0p2 rw rootwait
      [    0.000000] Dentry cache hash table entries: 131072 (order: 7, 524288 bytes, linear)
      [    0.000000] Inode-cache hash table entries: 65536 (order: 6, 262144 bytes, linear)
      [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
      [    0.000000] Memory: 885384K/1048576K available (12288K kernel code, 1132K rwdata, 7240K rodata, 1024K init, 173K bss, 32120K reserved, 131072K cma-reserved, 131072K highmem)
      [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
      [    0.000000] ftrace: allocating 39905 entries in 78 pages
      [    0.000000] rcu: Hierarchical RCU implementation.
      [    0.000000] rcu:     RCU event tracing is enabled.
      [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
      [    0.000000] NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
      [    0.000000] L2C-310 erratum 769419 enabled
      [    0.000000] L2C-310 enabling early BRESP for Cortex-A9
      [    0.000000] L2C-310: enabling full line of zeros but not enabled in Cortex-A9
      [    0.000000] L2C-310 ID prefetch enabled, offset 1 lines
      [    0.000000] L2C-310 dynamic clock gating enabled, standby mode enabled
      [    0.000000] L2C-310 cache controller enabled, 8 ways, 512 kB
      [    0.000000] L2C-310: CACHE_ID 0x410030c9, AUX_CTRL 0x76460001
      [    0.000000] random: get_random_bytes called from start_kernel+0x328/0x4dc with crng_init=0
      [    0.000000] clocksource: timer1: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
      [    0.000005] sched_clock: 32 bits at 100MHz, resolution 10ns, wraps every 21474836475ns
      [    0.000013] Switching to timer-based delay loop, resolution 10ns
      [    0.000211] Console: colour dummy device 80x30
      [    0.000241] Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=1000000)
      [    0.000250] pid_max: default: 32768 minimum: 301
      [    0.000308] Mount-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.000316] Mountpoint-cache hash table entries: 2048 (order: 1, 8192 bytes, linear)
      [    0.000780] CPU: Testing write buffer coherency: ok
      [    0.000818] CPU0: Spectre v2: using BPIALL workaround
      [    0.001027] CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
      [    0.001686] Setting up static identity map for 0x100000 - 0x100060
      [    0.001786] rcu: Hierarchical SRCU implementation.
      [    0.002272] smp: Bringing up secondary CPUs ...
      [    0.002781] CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
      [    0.002790] CPU1: Spectre v2: using BPIALL workaround
      [    0.002847] smp: Brought up 1 node, 2 CPUs
      [    0.002854] SMP: Total of 2 processors activated (400.00 BogoMIPS).
      [    0.002859] CPU: All CPU(s) started in SVC mode.
      [    0.003401] devtmpfs: initialized
      [    0.013025] VFP support v0.3: implementor 41 architecture 4 part 30 variant 9 rev 0
      [    0.013264] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
      [    0.013275] futex hash table entries: 512 (order: 3, 32768 bytes, linear)
      [    0.016095] pinctrl core: initialized pinctrl subsystem
      [    0.016977] NET: Registered PF_NETLINK/PF_ROUTE protocol family
      [    0.019427] DMA: preallocated 256 KiB pool for atomic coherent allocations
      [    0.023476] hw-breakpoint: found 5 (+1 reserved) breakpoint and 1 watchpoint registers.
      [    0.023483] hw-breakpoint: maximum watchpoint size is 8 bytes.
      [    0.037693] SCSI subsystem initialized
      [    0.037985] usbcore: registered new interface driver usbfs
      [    0.038028] usbcore: registered new interface driver hub
      [    0.038068] usbcore: registered new device driver usb
      [    0.038248] media: Linux media interface: v0.10
      [    0.038278] videodev: Linux video capture interface: v2.00
      [    0.038352] pps_core: LinuxPPS API ver. 1 registered
      [    0.038358] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
      [    0.038372] PTP clock support registered
      [    0.038706] FPGA manager framework
      [    0.039137] Advanced Linux Sound Architecture Driver Initialized.
      [    0.039797] clocksource: Switched to clocksource timer1
      [    0.060014] NET: Registered PF_INET protocol family
      [    0.060296] IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
      [    0.061219] tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes, linear)
      [    0.061255] TCP established hash table entries: 8192 (order: 3, 32768 bytes, linear)
      [    0.061331] TCP bind hash table entries: 8192 (order: 4, 65536 bytes, linear)
      [    0.061469] TCP: Hash tables configured (established 8192 bind 8192)
      [    0.061567] UDP hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.061604] UDP-Lite hash table entries: 512 (order: 2, 16384 bytes, linear)
      [    0.061780] NET: Registered PF_UNIX/PF_LOCAL protocol family
      [    0.062345] RPC: Registered named UNIX socket transport module.
      [    0.062353] RPC: Registered udp transport module.
      [    0.062357] RPC: Registered tcp transport module.
      [    0.062361] RPC: Registered tcp NFSv4.1 backchannel transport module.
      [    0.063397] workingset: timestamp_bits=30 max_order=18 bucket_order=0
      [    0.072037] NFS: Registering the id_resolver key type
      [    0.072060] Key type id_resolver registered
      [    0.072064] Key type id_legacy registered
      [    0.072115] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
      [    0.072972] io scheduler mq-deadline registered
      [    0.072983] io scheduler kyber registered
      [    0.079197] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
      [    0.080035] ffc02000.serial0: ttyS0 at MMIO 0xffc02000 (irq = 30, base_baud = 6250000) is a 16550A
      [    0.080151] printk: console [ttyS0] enabled
      [    0.085625] loop: module loaded
      [    0.086121] Registered mathworks_ip class
      [    0.086312] spi-nor spi0.0: unrecognized JEDEC id bytes: ff ff ff ff ff ff
      [    0.087375] MACsec IEEE 802.1AE
      [    0.090319] libphy: Fixed MDIO Bus: probed
      [    0.091282] stmmac - user ID: 0x10, Synopsys ID: 0x37
      [    0.091289] stmmaceth ffc02000.ethernet: couldn't get WOL irq -22
      [    0.091340] stmmac - user ID: 0x10, Synopsys ID: 0x37
      [    0.091341]  Ring mode enabled
      [    0.091344]  DMA HW capability register supported
      [    0.091347]  Normal descriptors
      [    0.091349]  RX Checksum Offload Engine supported
      [    0.091351]  COE Type 2
      [    0.091353]  TX Checksum insertion supported
      [    0.091357]  Enhanced/Alarm Timestamps supported
      [    0.091454] libphy: stmmac: probed
      [    0.099556] dwc2 ffb00000.usb: supply vusb_d not found, using dummy regulator
      [    0.099638] dwc2 ffb00000.usb: supply vusb_a not found, using dummy regulator
      [    0.104010] dwc2 ffb00000.usb: DWC OTG Controller
      [    0.104029] dwc2 ffb00000.usb: new USB bus registered, assigned bus number 1
      [    0.104046] dwc2 ffb00000.usb: irq 33, io mem 0xffb00000
      [    0.104313] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
      [    0.104320] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    0.104325] usb usb1: Product: DWC OTG Controller
      [    0.104329] usb usb1: Manufacturer: Linux 5.4.0-00475-gc588ee4 dwc2_hsotg
      [    0.104333] usb usb1: SerialNumber: ffb00000.usb
      [    0.104653] hub 1-0:1.0: USB hub found
      [    0.104677] hub 1-0:1.0: 1 port detected
      [    0.105375] dwc2 ffb40000.usb: supply vusb_d not found, using dummy regulator
      [    0.105430] dwc2 ffb40000.usb: supply vusb_a not found, using dummy regulator
      [    0.109813] dwc2 ffb40000.usb: DWC OTG Controller
      [    0.109826] dwc2 ffb40000.usb: new USB bus registered, assigned bus number 2
      [    0.109841] dwc2 ffb40000.usb: irq 34, io mem 0xffb40000
      [    0.110098] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
      [    0.110105] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
      [    0.110110] usb usb2: Product: DWC OTG Controller
      [    0.110114] usb usb2: Manufacturer: Linux 5.4.0-00475-gc588ee4 dwc2_hsotg
      [    0.110118] usb usb2: SerialNumber: ffb40000.usb
      [    0.110401] hub 2-0:1.0: USB hub found
      [    0.110420] hub 2-0:1.0: 1 port detected
      [    0.110930] usbcore: registered new interface driver usbserial_generic
      [    0.110952] usbserial: USB Serial support registered for generic
      [    0.111013] usbcore: registered new interface driver ftdi_sio
      [    0.111042] usbserial: USB Serial support registered for FTDI USB Serial Device
      [    0.111267] jesd204: found 1 devices and 1 topologies
      [    0.111328] usbcore: registered new interface driver usb-storage
      [    0.111500] usbcore: registered new interface driver usbhid
      [    0.111503] usbhid: USB HID core driver
      [    0.116627] mmc0: SDHCI controller on ff808000.dwmmc0 [ff808000.dwmmc0] using ADMA 64-bit
      [    0.117284] sdhci-pltfm: SDHCI platform and OF driver helper
      [    0.117545] fpga_manager fpga0: Altera SOCFPGA FPGA Manager registered
      [    0.117632] altera_hps2fpga_bridge ff400000.fpga_bridge: fpga bridge [lwhps2fpga] registered
      [    0.117667] altera_hps2fpga_bridge ff500000.fpga_bridge: fpga bridge [hps2fpga] registered
      [    0.117735] of-fpga-region soc:base_fpga_region: FPGA Region probed
      [    0.118010] EDAC MC: ECC not enabled
      [    0.118090] EDAC DEVICE0: Giving out device to module on_chip_ecc controller socfpga_ocram_ecc: DEV socfpga-ocram-ecc (INTERRUPT)
      [    0.118437] NET: Registered PF_INET6 protocol family
      [    0.118900] Segment Routing with IPv6
      [    0.118971] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
      [    0.119342] NET: Registered PF_PACKET protocol family
      [    0.119461] Key type dns_resolver registered
      [    0.119710] Registering SWP/SWPB emulation handler
      [    0.130118] mmc0: new high speed SDHC card at address e624
      [    0.130604] mmcblk0: mmc0:e624 SU16G 14.8 GiB
      [    0.132780]  mmcblk0: p1 p2 p3
      [    0.140499] hid: raw HID events driver (C) Jiri Kosina
      [    0.141193] usbcore: registered new interface driver usbhid
      [    0.141199] usbhid: USB HID core driver
      [    0.148587] axi_sysid 18000000.axi-sysid-0: AXI System ID core version (1.01.a) found
      [    0.148596] axi_sysid 18000000.axi-sysid-0: [fmcomms8_a10soc] on [a10soc] git branch <hdl_2019_r2> git <05a34dfbb> clean [2021-04-19 07:34:24] UTC
      [    0.150367] hmc7044 spi2.2: hmc7044_probe : enter
      [    0.183389] adrv9009 spi2.0: adrv9009_probe : enter
      [    0.193449] adrv9009 spi2.1: adrv9009_probe : enter
      [    0.205011] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition uninitialized -> initialized
      [    0.205036] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition uninitialized -> initialized
      [    0.205042] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition uninitialized -> initialized
      [    0.205048] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition initialized -> probed
      [    0.205055] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition initialized -> probed
      [    0.205060] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition initialized -> probed
      [    0.205066] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition probed -> idle
      [    0.205072] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition probed -> idle
      [    0.205078] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition probed -> idle
      [    0.205083] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition idle -> device_init
      [    0.205089] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition idle -> device_init
      [    0.205094] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition idle -> device_init
      [    0.205100] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition device_init -> link_init
      [    0.205106] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition device_init -> link_init
      [    0.205112] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition device_init -> link_init
      [    0.205117] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition link_init -> link_supported
      [    0.205123] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition link_init -> link_supported
      [    0.205129] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition link_init -> link_supported
      [    0.205134] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition link_supported -> link_pre_setup
      [    0.205140] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition link_supported -> link_pre_setup
      [    0.205145] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition link_supported -> link_pre_setup
      [    0.205151] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition link_pre_setup -> clk_sync_stage1
      [    0.205156] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition link_pre_setup -> clk_sync_stage1
      [    0.205162] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition link_pre_setup -> clk_sync_stage1
      [    0.205167] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition clk_sync_stage1 -> clk_sync_stage2
      [    0.205173] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition clk_sync_stage1 -> clk_sync_stage2
      [    0.205178] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition clk_sync_stage1 -> clk_sync_stage2
      [    0.205184] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition clk_sync_stage2 -> clk_sync_stage3
      [    0.205190] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition clk_sync_stage2 -> clk_sync_stage3
      [    0.205196] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition clk_sync_stage2 -> clk_sync_stage3
      [    0.257259] adrv9009 spi2.0: ADIHAL_resetHw
      [    0.581068] adrv9009 spi2.1: ADIHAL_resetHw
      [    0.935979] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition clk_sync_stage3 -> link_setup
      [    0.935992] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition clk_sync_stage3 -> link_setup
      [    0.936000] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition clk_sync_stage3 -> link_setup
      [    0.936009] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition link_setup -> opt_setup_stage1
      [    0.936015] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition link_setup -> opt_setup_stage1
      [    0.936020] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition link_setup -> opt_setup_stage1
      [    4.367768] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition opt_setup_stage1 -> opt_setup_stage2
      [    4.367783] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition opt_setup_stage1 -> opt_setup_stage2
      [    4.367790] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition opt_setup_stage1 -> opt_setup_stage2
      [    4.367799] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition opt_setup_stage2 -> opt_setup_stage3
      [    4.367805] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition opt_setup_stage2 -> opt_setup_stage3
      [    4.367811] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition opt_setup_stage2 -> opt_setup_stage3
      [    4.367819] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition opt_setup_stage3 -> opt_setup_stage4
      [    4.367824] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition opt_setup_stage3 -> opt_setup_stage4
      [    4.367830] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition opt_setup_stage3 -> opt_setup_stage4
      [    9.372505] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition opt_setup_stage4 -> opt_setup_stage5
      [    9.372520] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition opt_setup_stage4 -> opt_setup_stage5
      [    9.372526] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition opt_setup_stage4 -> opt_setup_stage5
      [    9.374432] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition opt_setup_stage5 -> clocks_enable
      [    9.374443] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition opt_setup_stage5 -> clocks_enable
      [    9.374449] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition opt_setup_stage5 -> clocks_enable
      [    9.375505] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition clocks_enable -> link_enable
      [    9.375516] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition clocks_enable -> link_enable
      [    9.375522] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition clocks_enable -> link_enable
      [    9.424040] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition link_enable -> link_running
      [    9.424053] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition link_enable -> link_running
      [    9.424059] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition link_enable -> link_running
      [    9.538393] adrv9009 spi2.0: adrv9009_info: adrv9009-x2 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [    9.652721] adrv9009 spi2.1: adrv9009_info: adrv9009 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized via jesd204-fsm
      [    9.652744] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[0] transition link_running -> opt_post_running_stage
      [    9.652750] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[1] transition link_running -> opt_post_running_stage
      [    9.652757] jesd204: /soc/spi@100024000/adrv9009-phy-d@1,jesd204:1,parent=spi2.1: JESD204 link[2] transition link_running -> opt_post_running_stage
      [    9.683996] cf_axi_adc 00020000.axi-adrv9009-rx-hpc: ADI AIM (10.01.b) at 0x00020000 mapped to 0x(ptrval), probed ADC ADRV9009-X2 as MASTER
      [    9.710989] cf_axi_dds 00024000.axi-adrv9009-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x00024000 mapped to 0x(ptrval), probed DDS ADRV9009-X2
      [    9.780741] ALSA device list:
      [    9.783620]   No soundcards found.
      [    9.806424] EXT4-fs (mmcblk0p2): recovery complete
      [    9.811086] EXT4-fs (mmcblk0p2): mounted filesystem with ordered data mode. Opts: (null)
      [    9.819101] VFS: Mounted root (ext4 filesystem) on device 179:2.
      [    9.825180] devtmpfs: mounted
      [    9.828399] Freeing unused kernel memory: 1024K
      [    9.833034] Run /sbin/init as init process
      [   10.533449] random: crng init done
      [   10.991254] systemd[1]: System time before build time, advancing clock.
      [   11.045714] systemd[1]: systemd 241 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -IDN2 +IDN -PCRE2 default-hierarchy=hybrid)
      [   11.067108] systemd[1]: Detected architecture arm.

      Welcome to Raspbian GNU/Linux 10 (buster)!

      [   11.107720] systemd[1]: Set hostname to <analog>.
      [   12.179629] systemd[1]: File /lib/systemd/system/systemd-journald.service:36 configures an IP firewall, but the local system does not support BPF/cgroup firewalling.
      [   12.194498] systemd[1]: Proceeding WITHOUT firewalling in effect! (snip)
      [   12.234555] systemd[1]: Listening on udev Kernel Socket.
      [  OK  ] Listening on udev Kernel Socket.
      [  OK  ] Listening on Journal Socket (/dev/log).
               Starting Remount Root and Kernel File Systems...
               Starting Load Kernel Modules...
               Mounting FUSE Control File System...
               Mounting Kernel Debug File System...
      [  OK  ] Started Forward Password Requests to Wall Directory Watch.
      [  OK  ] Reached target Swap.
               Starting Journal Service...
      [  OK  ] Reached target Slices.
      [  OK  ] Listening on Syslog Socket.
      [  OK  ] Listening on fsck to fsckd communication Socket.
      [  OK  ] Listening on udev Control Socket.
      [  OK  ] Listening on initctl Compatibility Named Pipe.
      [  OK  ] Listening on Journal Socket.
               Starting Create Static Device Nodes in /dev...
      [  OK  ] Mounted FUSE Control File System.
      [  OK  ] Mounted Kernel Debug File System.
      [  OK  ] Finished Load Kernel Modules.
      [  OK  ] Finished Remount Root and Kernel File Systems.
      [  OK  ] Finished Create Static Device Nodes in /dev.
               Starting Apply Kernel Variables...
               Starting Create System Users...
               Starting udev Coldplug all Devices...
               Starting Flush Journal to Persistent Storage...
      [  OK  ] Started Journal Service.
      [  OK  ] Finished Create System Users.
      [  OK  ] Finished Apply Kernel Variables.
               Starting Helper to synchronize boot up for ifupdown...
      [  OK  ] Finished Flush Journal to Persistent Storage.
      [  OK  ] Finished Helper to synchronize boot up for ifupdown.
      [  OK  ] Finished udev Coldplug all Devices.
               Starting udev Wait for Complete Device Initialization...
      [  OK  ] Reached target Local File Systems (Pre).
               Starting Rule-based Manager for Device Events and Files...
      [  OK  ] Started Rule-based Manager for Device Events and Files.
      [  OK  ] Found device /dev/ttyS0.
      [  OK  ] Finished udev Wait for Complete Device Initialization.
      [  OK  ] Reached target Local File Systems.
               Starting Set console font and keymap...
               Starting Raise network interfaces...
               Starting Preprocess NFS configuration...
               Starting Create Volatile Files and Directories...
               Starting Show Plymouth Boot Screen...
               Starting Tell Plymouth To Write Out Runtime Data...
      [  OK  ] Finished Set console font and keymap.
      [  OK  ] Started Show Plymouth Boot Screen.
      [  OK  ] Started Forward Password Requests to Plymouth Directory Watch.
      [  OK  ] Finished Tell Plymouth To Write Out Runtime Data.
      [  OK  ] Reached target Local Encrypted Volumes.
      [  OK  ] Finished Preprocess NFS configuration.
      [  OK  ] Reached target NFS client services.
      [  OK  ] Reached target Remote File Systems (Pre).
      [  OK  ] Reached target Remote File Systems.
      [  OK  ] Finished Create Volatile Files and Directories.
               Starting Network Time Synchronization...
               Starting Update UTMP about System Boot/Shutdown...
      [  OK  ] Finished Update UTMP about System Boot/Shutdown.
      [  OK  ] Finished Raise network interfaces.
      [  OK  ] Started Network Time Synchronization.
      [  OK  ] Reached target System Time Synchronized.
      [  OK  ] Reached target System Initialization.
      [  OK  ] Started Daily apt download activities.
      [  OK  ] Started Daily apt upgrade and clean activities.
      [  OK  ] Started Periodic ext4 Online Data Check for All Filesystems.
      [  OK  ] Started Discard unused blocks once a week.
      [  OK  ] Started Daily rotation of log files.
      [  OK  ] Started Daily man-db regeneration.
      [  OK  ] Started Daily Cleanup of Temporary Directories.
      [  OK  ] Reached target Paths.
      [  OK  ] Reached target Timers.
      [  OK  ] Listening on Avahi mDNS/DNS-SD Stack Activation Socket.
      [  OK  ] Listening on D-Bus System Message Bus Socket.
      [  OK  ] Listening on triggerhappy.socket.
      [  OK  ] Reached target Sockets.
      [  OK  ] Reached target Basic System.
               Starting Analog Devices power up/down sequence...
               Starting Save/Restore Sound Card State...
               Starting Avahi mDNS/DNS-SD Stack...
      [  OK  ] Started Regular background program processing daemon.
      [  OK  ] Started D-Bus System Message Bus.
               Starting dphys-swapfile - set up, mount, and delete a swap file...
               Starting Remove Stale Online ext4 Metadata Check Snapshots...
               Starting dhcpcd on all interfaces...
               Starting Check for Raspberry Pi EEPROM updates...
               Starting LSB: Switch to ondemand cpu governor (unless shift key is pressed)...
               Starting LSB: rng-tools (Debian variant)...
               Starting System Logging Service...
               Starting Login Service...
               Starting triggerhappy global hotkey daemon...
      [  OK  ] Started D-Bus System Message Bus.
               Starting WPA supplicant...
      [FAILED] Failed to start rng-tools.service.
      See 'systemctl status rng-tools.service' for details.
      [  OK  ] Started Login Service.
      [  OK  ] Started triggerhappy global hotkey daemon.
      [  OK  ] Started System Logging Service.
      [  OK  ] Started dhcpcd on all interfaces.
      [  OK  ] Started Check for Raspberry Pi EEPROM updates.
      [  OK  ] Started WPA supplicant.
      [  OK  ] Started Avahi mDNS/DNS-SD Stack.
               Starting Authorization Manager...
      [  OK  ] Started Make remote CUPS printers available locally.
      [  OK  ] Reached target Network.
               Starting /etc/rc.local Compatibility...
               Starting HTTP based time synchronization tool...
               Starting OpenBSD Secure Shell server...
      [  OK  ] Started IIO Daemon.
               Starting Permit User Sessions...
      [  OK  ] Started LSB: Switch to ond…(unless shift key is pressed).
      [  OK  ] Started dphys-swapfile - s…mount, and delete a swap file.
      [  OK  ] Started /etc/rc.local Compatibility.
      [  OK  ] Started HTTP based time synchronization tool.
      [  OK  ] Started Permit User Sessions.
               Starting Hold until boot process finishes up...
               Starting Light Display Manager...
      [  OK  ] Started Authorization Manager.
      [  OK  ] Started OpenBSD Secure Shell server.

      Raspbian GNU/Linux 10 analog ttyS0

      analog login: root (automatic login)

      Last login: Fri Jul  2 14:47:07 BST 2021 on ttyS0
      Linux analog 5.4.0-00475-gc588ee4 #1847 SMP Fri Jul 2 09:07:42 IST 2021 armv7l

      The programs included with the Debian GNU/Linux system are free software;
      the exact distribution terms for each program are described in the
      individual files in /usr/share/doc/*/copyright.

      Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
      permitted by applicable law.
      root@analog:~#

Useful commands for the serial terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The below commands are to be run in the serial terminal connected to the FPGA.

To find out the IP of the FPGA board, run the following command and take the
IP specified at "eth0 inet":

.. shell::

   $ifconfig

If the A10Soc is connected to a network with a DHCP server, the IP address
assigned to the board appears on the LCD.
To manually assign an IP address, run `ifconfig eth0 IP_ADDR`.

To see the IIO devices detected, run:

.. shell::

   $iio_info | grep iio:device
   iio:device0: hmc7044-fmc
   iio:device1: 0-0014
   iio:device2: 0-0016
   iio:device3: adrv9009-phy-c
   iio:device4: adrv9009-phy-d
   iio:device5: axi-adrv9009-rx-obs-hpc (buffer capable)
   iio:device6: axi-adrv9009-tx-hpc (buffer capable)
   iio:device7: axi-adrv9009-rx-hpc (buffer capable)

To use the :doc:`JESD204 status utility </software/jesd/jesd_status>`,
run:

.. shell::

   $jesd_status

Additionally, if running ``stty rows 30`` before running ``jesd_status``, you
can expand the visible area of it and see more than 4 lanes.

To power off the system, run the following command, and wait for the final
message to be printed, then power off the FPGA board from the switch as well.

.. shell::

   $poweroff

To reboot the system, run:

.. shell::

   $reboot

.. important::

   Even though this is Linux, this is a persistent file system. Care should
   be taken not to corrupt the file system -- please shut down things, don't
   just turn off the power switch. Depending on your monitor, the standard
   power off could be hiding. You can do this from the terminal as well with
   :code:`sudo shutdown -h now` or the above-mentioned command for powering off.
