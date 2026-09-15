.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9009/quickstart/a10gx

.. _adrv9009 quickstart a10gx:

ADRV9009 Arria 10 GX Quick Start Guide
======================================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/quickstart/arria10-fpga_adrv9009.jpg
   :width: 330px

.. warning::

   Support for the A10GX carrier is discontinued and will not be supported in
   future releases. Last pre-build images can be found at
   :dokuwiki:`Nios2 Linux on the Altera FPGA Development Boards </resources/tools-software/linux-drivers/platforms/nios2>`
   page.

This guide provides some quick instructions on how to setup the ADRV9009 on
:intel:`A10GX <en:products:details:fpga:development-kits:arria:10-gx>`

Prerequisites
-------------

Required Hardware
~~~~~~~~~~~~~~~~~

- :intel:`A10GX <en:products:details:fpga:development-kits:arria:10-gx>` board
-
  :adi:`ADRV9009 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV9008-9009.html>`
  FMC board
- Ethernet cable
- Micro-USB cable

Required Software
~~~~~~~~~~~~~~~~~

- You need a Host PC (Windows)
- Intel Quartus 21.2
- Bitfile and Linux ELF image
- IIO Scope
  `Download <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`__

.. tip::

   :dokuwiki:`Pre-build Images for Intel Arria 10 GX. </resources/tools-software/linux-drivers/platforms/nios2>`

Setting up the hardware (A10GX)
-------------------------------

You will need to:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/arria10-fpga-kit.jpg
   :width: 330px

::

   -Get the [[intel>en:products:details:fpga:development-kits:arria:10-gx|A10GX]] board.
   -Connect the ADRV9009 FMC board to the FPGA carrier **FMC1** socket(J1).
   -Connect the USB JTAG J3 (Micro USB) to your Host PC.
   -Connect the Ethernet cable.
   -Plug the Power Supply into 12V Power input connector (DC Input).
   -Turn it on.

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

Programming the FPGA
--------------------

Nios II Command Shell is used to program the FPGA. To run Nios II Command Shell
navigate to C:\\intelFPGA_pro\\21.2\\nios2eds and start Nios II Command
Shell.bat. Windows Subsystem for Linux (WSL) needs to be installed in order to
run Nios II Command Shell.

After starting the Command Shell, navigate to the path where the pre-build
images are saved. For example:

::

   ceshu@LADACE-L02:/mnt/c/intelFPGA_pro/21.2/nios2eds$ cd /mnt/c/Users/ladace/Downloads/adrv9009_a10gx

Programming FPGA bitfiled image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To flash the bitfield pre-build image, **nios2-configure-sof** command is used.
For example:

::

   ceshu@LADACE-L02:/mnt/c/Users/ladace/Downloads/adrv9009_a10gx$ nios2-configure-sof adrv9009_a10gx.sof
   Searching for SOF file:
   in .
     adrv9009_a10gx.sof

   Info: *******************************************************************
   Info: Running Quartus Prime Programmer
   Info: Command: quartus_pgm --no_banner --mode=jtag -o p;./adrv9009_a10gx.sof
   Info (213045): Using programming cable "USB-BlasterII [USB-1]"
   Info (213011): Using programming file ./adrv9009_a10gx.sof with checksum 0x30E72CA2 for device 10AX115S2F45@1
   Info (209060): Started Programmer operation at Thu Dec 16 14:05:48 2021
   Info (209016): Configuring device index 1
   Info (209017): Device 1 contains JTAG ID code 0x02E060DD
   Info (209007): Configuration succeeded -- 1 device(s) configured
   Info (209011): Successfully performed operation(s)
   Info (209061): Ended Programmer operation at Thu Dec 16 14:06:03 2021
   Info: Quartus Prime Programmer was successful. 0 errors, 0 warnings
       Info: Peak virtual memory: 1805 megabytes
       Info: Processing ended: Thu Dec 16 14:06:03 2021
       Info: Elapsed time: 00:00:25
       Info: System process ID: 4216

Programming Linux image
~~~~~~~~~~~~~~~~~~~~~~~

To flash the Linux pre-build image, **nios2-download** command is used. For
example:

::

   ceshu@LADACE-L02:/mnt/c/Users/ladace/Downloads/adrv9009_a10gx$ nios2-download -g zImage
   Using cable "USB-BlasterII [USB-1]", device 1, instance 0x00
   Pausing target processor: OK
   Initializing CPU cache (if present)
   OK
   Downloaded 5471KB in 6.1s (896.8KB/s)
   Verified OK
   Starting processor at address 0xC4000000

Nios II Terminal
~~~~~~~~~~~~~~~~

To start the Nios II Terminal use the following **nios2-terminal.exe** command. Example of console: <hidden Complete kernel boot log (Click to expand)> ::

   ceshu@LADACE-L02:/mnt/c/Users/ladace/Downloads/adrv9009_a10gx$ nios2-terminal.exe
   nios2-terminal: connected to hardware target using JTAG UART on cable
   nios2-terminal: "USB-BlasterII [USB-1]", device 1, instance 0
   nios2-terminal: (Use the IDE stop button or Ctrl-C to terminate)

   Linux version 4.9.0-04235-g4db1e6cb5208 (sandu@saturn) (gcc versiLinux version 4.19.0-g17f4223 (jenkins@romlxbuild1.adlk
   .analog.com) (gcc version 8.3.1 20190416 (Altera 19.3 Build 222)) #1876 Tue Jul 27 14:47:24 IST 2021
   On node 0 totalpages: 65536
     Normal zone: 512 pages used for memmap
     Normal zone: 0 pages reserved
     Normal zone: 65536 pages, LIFO batch:15
   pcpu-alloc: s0 r0 d32768 u32768 alloc=1*32768
   pcpu-alloc: [0] 0
   Built 1 zonelists, mobility grouping on.  Total pages: 65024
   Kernel command line: debug console=ttyJ0,115200
   Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)
   Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)
   Sorting __ex_table...
   Memory: 247876K/262144K available (3795K kernel code, 469K rwdata, 4372K rodata, 3176K init, 106K bss, 14268K reserved,
   0K cma-reserved)
   NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
   clocksource: nios2-clksrc: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604467 ns
   Calibrating delay loop (skipped), value calculated using timer frequency.. 200.00 BogoMIPS (lpj=400000)
   pid_max: default: 32768 minimum: 301
   Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
   Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
   devtmpfs: initialized
   random: get_random_u32 called from bucket_table_alloc.isra.6+0x98/0x1e8 with crng_init=0
   clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
   futex hash table entries: 256 (order: -1, 3072 bytes)
   NET: Registered protocol family 16
   jesd204: found 0 devices and 0 topologies
   clocksource: Switched to clocksource nios2-clksrc
   NET: Registered protocol family 2
   tcp_listen_portaddr_hash hash table entries: 512 (order: 0, 4096 bytes)
   TCP established hash table entries: 2048 (order: 1, 8192 bytes)
   TCP bind hash table entries: 2048 (order: 1, 8192 bytes)
   TCP: Hash tables configured (established 2048 bind 2048)
   UDP hash table entries: 256 (order: 0, 4096 bytes)
   UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
   NET: Registered protocol family 1
   RPC: Registered named UNIX socket transport module.
   RPC: Registered udp transport module.
   RPC: Registered tcp transport module.
   RPC: Registered tcp NFSv4.1 backchannel transport module.
   random: fast init done
   workingset: timestamp_bits=30 max_order=16 bucket_order=0
   jffs2: version 2.2. (NAND) ┬⌐ 2001-2006 Red Hat, Inc.
   Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)
   io scheduler noop registered
   io scheduler deadline registered
   io scheduler cfq registered (default)
   io scheduler mq-deadline registered
   io scheduler kyber registered
   101814f0.serial: ttyJ0 at MMIO 0x101814f0 (irq = 2, base_baud = 0) is a Altera JTAG UART
   console [ttyJ0] enabled
   loop: module loaded
   spi_altera 10181400.spi: base (ptrval), irq 8
   libphy: Fixed MDIO Bus: probed
   libphy: altera_tse: probed
   altera_tse 10181000.ethernet (unnamed net_device) (uninitialized): MDIO bus altera_tse-0: created
   altera_tse 10181000.ethernet: Altera TSE MAC version 19.3 at 0x10181000 irq 1/3
   adrv9009 spi0.1: adrv9009_probe : enter
   altera-a10-fpll 10056000.altera-a10-fpll: FPLL PLL calibration OK (1400 us)
   altera-a10-fpll 10046000.altera-a10-fpll: FPLL PLL calibration OK (1400 us)
   altera-a10-fpll 10026000.altera-a10-fpll: FPLL PLL calibration OK (1400 us)
   altera_adxcvr 10024000.axi-adrv9009-tx-xcvr: ATX PLL calibration OK (20 ms)
   altera_adxcvr 10024000.axi-adrv9009-tx-xcvr: Lane 0 TX termination and VOD calibration OK (400 us)
   altera_adxcvr 10024000.axi-adrv9009-tx-xcvr: Lane 1 TX termination and VOD calibration OK (500 us)
   altera_adxcvr 10024000.axi-adrv9009-tx-xcvr: Lane 2 TX termination and VOD calibration OK (500 us)
   altera_adxcvr 10024000.axi-adrv9009-tx-xcvr: Lane 3 TX termination and VOD calibration OK (500 us)
   altera_adxcvr 10024000.axi-adrv9009-tx-xcvr: Altera ADXCVR (17.01.a) probed
   altera_adxcvr 10044000.axi-adrv9009-rx-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (400 us)
   altera_adxcvr 10044000.axi-adrv9009-rx-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (500 us)
   altera_adxcvr 10044000.axi-adrv9009-rx-xcvr: Altera ADXCVR (17.01.a) probed
   altera_adxcvr 10054000.axi-adrv9009-rx-os-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (400 us)
   altera_adxcvr 10054000.axi-adrv9009-rx-os-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (500 us)
   altera_adxcvr 10054000.axi-adrv9009-rx-os-xcvr: Altera ADXCVR (17.01.a) probed
   NET: Registered protocol family 17
   altera_adxcvr 10024000.axi-adrv9009-tx-xcvr: Setting link rate to 61440000 (lane rate: 2457600)
   altera_adxcvr 10044000.axi-adrv9009-rx-xcvr: Setting link rate to 122880000 (lane rate: 4915200)
   altera_adxcvr 10054000.axi-adrv9009-rx-os-xcvr: Setting link rate to 122880000 (lane rate: 4915200)
   adrv9009 spi0.1: adrv9009_probe : enter
   adrv9009 spi0.1: adrv9009_probe : enter
   altera_adxcvr 10054000.axi-adrv9009-rx-os-xcvr: Lane 0 CDR/CMU PLL & RX offset calibration OK (600 us)
   altera_adxcvr 10054000.axi-adrv9009-rx-os-xcvr: Lane 1 CDR/CMU PLL & RX offset calibration OK (600 us)
   adrv9009 spi0.1: ADIHAL_resetHw
   altera_adxcvr 10054000.axi-adrv9009-rx-os-xcvr: Setting link rate to 61440000 (lane rate: 2457600)
   altera-a10-fpll 10056000.altera-a10-fpll: FPLL PLL calibration OK (1200 us)
   random: crng init done
   adrv9009 spi0.1: adrv9009_info: adrv9009 Rev 192, Firmware 6.0.2 API version: 3.6.0.5 successfully initialized
   cf_axi_dds 10064000.axi-adrv9009-tx-hpc: Analog Devices CF_AXI_DDS_DDS MASTER (9.01.b) at 0x10064000 mapped to 0x13d121e
   5, probed DDS AD9371
   cf_axi_adc 10060000.axi-adrv9009-rx-hpc: ADI AIM (10.01.b) at 0x10060000 mapped to 0x2b21001c, probed ADC ADRV9009 as MA
   STER
   Freeing unused kernel memory: 3176K
   This architecture does not have kernel memory protection.
   Run /init as init process
   Starting logging: OK
   Initializing random number generator... done.
   Starting network: OK
   altera_tse 10181000.ethernet eth0: device MAC address b2:94:3d:6e:11:8f
   altera_tse 10181000.ethernet eth0: TSE revision 1303
   altera_tse 10181000.ethernet eth0: PCS PHY ID: 0x00000000
   altera_tse 10181000.ethernet eth0: SGMII PCS block initialised OK
   altera_tse 10181000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx
   Network cable is plugged
   udhcpc: started, v1.25.0
   udhcpc: sending discover
   udhcpc: sending select for 10.48.65.123
   udhcpc: lease of 10.48.65.123 obtained, lease time 21600
   deleting routers
   adding dns 10.32.51.110
   adding dns 10.64.53.110
             inet addr:10.48.65.123  Bcast:10.48.65.255  Mask:255.255.255.0
   Starting dropbear sshd: OK
   Starting IIO Server Daemon

   Welcome to Buildroot
   buildroot login:

</hidden>

IIO Oscilloscope
----------------

To connect the board to IIO Scope start the IIO Oscilloscope application and go
to **Settings** menu and then press **Connect**. From **Select or Discover
libIIO Context** select **Manual** and enter the URI in the following format
**ip:<your_board_ip>** Press the **Refresh** button and then **Connect**.

To determine the IP of the board, in Nios II Command Shell login using **root**
and password **analog**. Then run the **ifconfig** command. For example:

::

   # ifconfig
   eth0      Link encap:Ethernet  HWaddr B2:94:3D:6E:11:8F
             inet addr:10.48.65.123  Bcast:10.48.65.255  Mask:255.255.255.0
             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
             RX packets:1283 errors:0 dropped:119 overruns:0 frame:0
             TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:249905 (244.0 KiB)  TX bytes:684 (684.0 B)
             Memory:10181000-101813ff

   lo        Link encap:Local Loopback
             inet addr:127.0.0.1  Mask:255.0.0.0
             UP LOOPBACK RUNNING  MTU:65536  Metric:1
             RX packets:0 errors:0 dropped:0 overruns:0 frame:0
             TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/quickstart/iioscope_connect.jpg

To plot the captured waveforms go to **File** menu then click **New Plot**.
Select the channels to plot and then click **Capture / Stop** button.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9009/quickstart/iioscope_newplot.jpg

More Information
----------------

- :dokuwiki:`ADRV9009 User Guide </resources/eval/user-guides/mykonos>`
- :dokuwiki:`ADRV9009 HDL Reference Design </resources/eval/user-guides/adrv9009/reference_hdl>`

.. todo:: .. include: /resources/eval/user-guides/ad9081_fmca_ebz/common.rst

   :start-after: .. start-#support
   :end-before: .. end-#support
