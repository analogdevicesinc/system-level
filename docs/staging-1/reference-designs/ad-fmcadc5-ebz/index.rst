.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcadc5-ebz

.. _ad-fmcadc5-ebz:

AD-FMCADC5-EBZ FMC Board
========================

.. warning::

   Support for the ad-fmcadc5-ebz is discontinued starting with 2022_R2 Kuiper
   Linux release and it will not be supported in future releases. Last release
   in which pre-build files can be found is 2021_r2. Check this
   :dokuwiki:`link </resources/tools-software/linux-software/adi-kuiper_images/release_notes>`
   to see all Kuiper releases.

.. important::

   The HDL project documentation can be found at
   https://analogdevicesinc.github.io/hdl/projects/fmcadc5/index.html

Introduction
------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc5-ebz/ad-fmcadc5-ebz.jpg
   :width: 400px

  The :adi:`AD-FMCADC5-EBZ` is a high speed single channel data acquisition
  board featuring two :adi:`AD9625` ADCs. The board is provisioned to sample the
  single input at an effective sampling rate of 5GSPS, with both the ADCs
  running at 2.5GHz and sampling at both edges (the clocks are 180 out of phase
  to each other). The board is a variant of
  `FSF-AD15000A <https:fidus.com/fmcs/>`__ from Fidus Systems Inc.

Although this board does meet most of the FMC specifications, it is not meant as
a
`commercial off the shelf <https://en.wikipedia.org/wiki/Commercial_off-the-shelf>`__
(COTS) board. If a commercial, ready to go integrate product is required, please
refer to one of the many FMC manufacturers.

ADI also provides reference designs (HDL and software) for this board to work
with commonly available Altera and Xilinx development boards.

Hardware
--------

The AD-FMCADC5-EBZ is a double FMC wide board and requires two fully populated
(transceivers mainly) FMC connectors on the carrier (such as VC707). The board"s
primary purpose is to demonstrate the capabilities of the devices on board
quickly and easily by providing a seamless interface to an FMC carrier platform
and running the reference design on the carrier FPGA. The board is designed to
self power and self clock when connected to the FMC carrier. The analog signal
is connected to J18.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc5-ebz/adc5_block_diagram.png
   :width: 600px

Devices
~~~~~~~

The FMC board includes the following products by Analog Devices:

- :adi:`AD9625` 12-bit single channel ADC with sampling speeds of up to 2500
  MSPS, with a :adi:`JESD204B <JESD204>` digital interface.

Clocking
~~~~~~~~

The AD-FMCADC5-EBZ uses a 2.5GHz crystal. The two AD9625 devices are clocked
from the same clock source, but 180 degrees out of phase.

Running No-OS Application & Achieving Interleaving at 5GSPS
-----------------------------------------------------------

Building & Running the No-OS Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HDL reference design is built around a processor as in an embedded system.
You may use either Linux or No-OS software to demonstrate the design (details in
the downloads section). In order to run the HDL with the No-OS application, one
needs to build the HDL bit file and software elf file.

The :dokuwiki:`HDL user guide </resources/fpga/docs/hdl>` contains the
instructions to build the bit file. **Please make sure you use the latest
release branch (checkout right after cloning).**

Once the bit file is ready, follow these instructions to build the elf file.
This assumes you are following our directory structures. If you are not, just
get the idea from here and port it to your environment. However, you have to
figure out things on your own.

#. Clone `No-OS <https://github.com/analogdevicesinc/no-OS>`__ repository
#. **Checkout the latest release branch (git checkout 2018_R1)**
#. Change the directory to ``ad-fmcadc5-ebz/vc707``.
#. Make the elf file by running ``make
   HDF-FILE=<HDL-REPO>/projects/fmcadc5/vc707/fmcadc5_vc707.sdk/system_top.hdf``

The make will build the default "hello-world", but we only need the bsp and I am
no fan of eclipse, therefore this method. If you are more comfortable with the
GUI, import all the files (or folders) that the make uses.

A typical run looks like this:

::

   [~/github/noos/ad-fmcadc5-ebz/vc707]> make HDF-FILE=~/github/hdl/projects/fmcadc5/vc707/fmcadc5_vc707.sdk/system_top.hdf
   xsct -s ../../scripts/xilinx_xsct.tcl ~/github/hdl/projects/fmcadc5/vc707/fmcadc5_vc707.sdk/system_top.hdf >> xilinx_xsct.log 2>&1

   mb-gcc -Wall -mlittle-endian -mxl-soft-mul -mcpu=v9.2 -mxl-soft-mul -DXILINX -Ibsp/sys_mb/include -I.. -I../../common_drivers/xilinx_platform_drivers -I../../common_drivers/jesd204b_gt -I../../common_drivers/jesd204b_v51 -I../../common_drivers/adc_core -I../../drivers/ad9625 -Os -ffunction-sections -fdata-sections -o vc707.elf sw/src/platform.c ../ad_fmcadc5_ebz.c ../../common_drivers/xilinx_platform_drivers/platform_drivers.c ../../common_drivers/jesd204b_gt/jesd204b_gt.c ../../common_drivers/jesd204b_v51/jesd204b_v51.c ../../common_drivers/adc_core/adc_core.c ../../drivers/ad9625/ad9625.c -Lbsp/sys_mb/lib/ -Tsw/src/lscript.ld -Wl,--start-group,-lxil,-lgcc,-lc,--end-group

Start an UART terminal.

::

   [USB0]
   port    = /dev/ttyUSB0
   speed   = 115200
   bits    = 8
   stopbits    = 1
   parity  = none
   crlfauto    = True ## if not set, expect non-aligned text

   [~/github/noos/ad-fmcadc5-ebz/vc707]> gtkterm -c USB0 &

The folder contains a vc707.tcl file that you can launch with xmd. You can also
run it using Vivado or SDK - up to you.

::

   [~/github/noos/ad-fmcadc5-ebz/vc707]> xmd -tcl vc707.tcl
   rlwrap: warning: your $TERM is 'xterm' but rlwrap couldn't find it in the terminfo database. Expect some problems.

    Xilinx Microprocessor Debugger (XMD) Engine
    XMD v2015.2 (64-bit)
      SW Build 1266856 on Fri Jun 26 16:35:25 MDT 2015
        Copyright 1986-2015 Xilinx, Inc. All Rights Reserved.

   Executing user script : vc707.tcl
   Configuring Device 1 (xc7vx485t) with Bitstream -- hw/system_top.bit
   ..............................10..............................20..............................30......................................................10..............................20..............................30......................................................10..............................20..............................30......................................................10..............................20..............................30......................................................10..............................20..............................30..............................40..............................50..............................60..............................70..............................................10..............................20..............................30..............................40..............................50..............................60..............................70..............................................10..............................20..............................30..............................40..............................50..............................60..............................70..............................80..............................90..............................Done
   Successfully downloaded bit file.

   JTAG chain configuration
   --------------------------------------------------
   Device   ID Code        IR Length    Part Name
    1       23687093           6        xc7vx485t

   JTAG chain configuration
   --------------------------------------------------
   Device   ID Code        IR Length    Part Name
    1       23687093           6        xc7vx485t

   MicroBlaze Processor Configuration :
   -------------------------------------
   Version............................9.5
   Optimization.......................Performance
   Interconnect.......................AXI-LE
   MMU Type...........................Full_MMU
   No of PC Breakpoints...............1
   No of Read Addr/Data Watchpoints...0
   No of Write Addr/Data Watchpoints..0
   Instruction Cache Support..........on
   Instruction Cache Base Address.....0x80000000
   Instruction Cache High Address.....0xbfffffff
   Data Cache Support.................on
   Data Cache Base Address............0x80000000
   Data Cache High Address............0xbfffffff
   Exceptions  Support................on
   FPU  Support.......................off
   Hard Divider Support...............on
   Hard Multiplier Support............on - (Mul64)
   Barrel Shifter Support.............on
   MSR clr/set Instruction Support....on
   Compare Instruction Support........on
   PVR Supported......................on
   PVR Configuration Type.............Full
   Data Cache Write-back Support......off
   Fault Tolerance Support............off
   Stack Protection Support...........off

   Connected to "mb" target. id = 0
   Starting GDB server for "mb" target (id = 0) at TCP port no 1234
   Processor stopped

   System Reset .... DONE
   Downloading Program -- vc707.elf
           section, .vectors.reset: 0x00000000-0x00000007
           section, .vectors.sw_exception: 0x00000008-0x0000000f
           section, .vectors.interrupt: 0x00000010-0x00000017
           section, .vectors.hw_exception: 0x00000020-0x00000027
           section, .text: 0x80000000-0x800069fb
           section, .init: 0x800069fc-0x80006a2f
           section, .fini: 0x80006a30-0x80006a4b
           section, .ctors: 0x80006a4c-0x80006a53
           section, .dtors: 0x80006a54-0x80006a5b
           section, .rodata: 0x80006a5c-0x8000723f
           section, .data: 0x80007240-0x8000746f
           section, .eh_frame: 0x80007470-0x800074fb
           section, .jcr: 0x800074fc-0x800074ff
           section, .bss: 0x80007500-0x8000762b
           section, .heap: 0x8000762c-0x80007a2f
           section, .stack: 0x80007a30-0x80007e2f
   Download Progress..10.20.30.40.50.60.70.80.90.Done
   Setting PC with Program Start Address 0x00000000
   Processor started. Type "stop" to stop processor

   RUNNING> Disconnected from Target 0

   [~/github/noos/ad-fmcadc5-ebz/vc707]>

The following messages should appear on the terminal.

::

   AD9625 successfully initialized.
   AD9625 successfully initialized.
   JESD204B successfully initialized.
   JESD204B successfully initialized.
   SYSREF Calibration Successful[4]
   ADC Core Initialized (157 MHz).
   ADC Core Initialized (157 MHz).
   Initialization done.
   Capture done.

And should be seeing this on the ILA.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_1_1.png
   :width: 800px

Let"s dissect all this.

Interleaving (HDL)
~~~~~~~~~~~~~~~~~~

A brief introduction to interleaving, everyone knows this but we will start with
it anyway. We have two AD9625 devices running at 2.5Gbps, but the clocks to the
devices are 180 degrees out of phase. In other words, the input signal is
sampled by the first ADC at the rising edges of the 2.5GHz clock. The same
signal is sampled by the second ADC at the falling edges of the ``conceptually
same`` clock. That is an effective sampling rate of 5GSPS. All the user needs to
do is interleave these two samples. That sounds easy, but there are some
challenges.

A word of caution (or disclaimer), this interleaving inherently has some
performance factors outside of what we are discussing here. There are two major
factors, first the jitter on the sampling clocks. Second, the gain and phase
variations at the input. The devices itself may also have encoding skew. Some of
these may be filtered or compensated by post processing the samples. I can not
go into the details here, just keep in mind that we are not talking about these
things. Here our focus is on understanding the FPGA design and how to achieve
interleaving - not the performance effects.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_intlv_hdl.png
   :width: 800px

If we look at the data path of the devices independently (see block diagram
above), we can see that alignment and deskew happens at various stages. The
transceivers perform deskew and alignment of bits (comma character alignment and
10B to 8B conversion), the JESD-IP then aligns individual lanes and outputs data
with a fixed latency using SYSREF. The SYSREF resets the LMFC, thus the receiver
knows from the time it receives the SYSREF pulse to the first received ILA data
the latency of the system. After this the samples hit the AD9625 core.

The cores receive two samples from each of the devices. Now it needs to know
which samples goes first (in time) and which one follows it. That is, the
samples are to be interleaved in the same order they were sampled in absolute
time. Ideally being a JESD204B subclass-1 devices using SYSREF should have been
sufficient to do this. The SYSREF is the :adi:``absolute`` reference for all the
concerned transmit and receive devices. However, for practical reasons, SYSREF
is seldom used as a clock but as data and is sampled by the concerned parties at
their own clock. A robust method is to identify, at the receiving device, the
exact sample at which (or immediately after) the device sampled SYSREF. So the
AD9625 supports a mode in which a time stamp is attached to the samples. The
details of which are in the
`data sheet <media/en/technical-documentation/data-sheets/AD9625.pdf>`. The FPGA
design simply uses this time stamp and knows the exact sample at which the
devices sampled SYSREF. The design implements this by aligning samples across
the 16-sample data per device per clock. After which, data is written to a small
FIFO with the write pointer reset by the SYSREF time stamp. A common read
pointer is then used to read the samples. The FIFO supports deskewing of up to 8
samples. The ADC pack simply interleaves these samples assuming device-0 is
first in order. The software needs to make sure that device-0 always samples
SYSREF half a clock ahead of device-1. This is done with a calibration routine.

*The AD9625 supports time stamp insertion at the LSB of the sample (and is the
ONLY option in certain lane configurations). This changes the devices to 11-bit
converters. The HDL design does NOT support this. It supports time stamp
insertion in the CS bits ONLY. The converter resolution remains as 12-bit. If
you would prefer the LSB option, you need to change both HDL and software.*

Interleaving (SW)
~~~~~~~~~~~~~~~~~

The software programs both the devices and the GPIO, transceivers and IP cores
in FPGA. The default transceiver setup only supports single-chip, single-link
configuration. It also does not take into account that a single SYSREF controls
both the devices and transceivers. The default routine is therefore modified to
leave the transceivers up and running but the data path is held under reset.
This is required because the AD9625 does NOT always wait for SYSREF to start the
ILA phase after CGS. The second SYSREF may reset the LMFC, but in its absence,
ILA phase is initiated.

This is the section of the code where the initial setup is done. The setup and
calibration of interleaving follow this.

::

   if (adc5_gpio_ctl(GPIO_DEVICE_ID))
     return -1;

   ad9625_setup(XPAR_SPI_0_DEVICE_ID, 0);
   ad9625_setup(XPAR_SPI_0_DEVICE_ID, 1);

   jesd204b_gt_initialize(XPAR_AXI_FMCADC5_0_GT_BASEADDR, 8);
   jesd204b_setup(XPAR_AXI_AD9625_0_JESD_BASEADDR, jesd204b_st);
   jesd204b_gt_setup_modified(jesd204b_gt_link);

   jesd204b_gt_initialize(XPAR_AXI_FMCADC5_1_GT_BASEADDR, 8);
   jesd204b_setup(XPAR_AXI_AD9625_1_JESD_BASEADDR, jesd204b_st);
   jesd204b_gt_setup_modified(jesd204b_gt_link);

The devices need to be re-programmed to support interleaving. The sequence below
enables the SYSREF time stamping in the CS bits it also programs the monitoring
of SYSREF signals for setup/hold violations at the 2.5GHz clock. This is
required to ensure that the sampling order is correct. This is only the
programming sequence, nothing happened in the hardware yet.

::

   ad9625_spi_write(0, 0x072, 0x8b);
   ad9625_spi_write(0, 0x03a, 0x02);
   ad9625_spi_write(0, 0x0ff, 0x01);
   ad9625_spi_write(1, 0x072, 0x8b);
   ad9625_spi_write(1, 0x03a, 0x02);
   ad9625_spi_write(1, 0x0ff, 0x01);

If starting from reset, the devices are in CGS at this time. The AD9625 may
initiate a ILA as soon as it sees SYNC deasserted regardless of SYSREF. So we
need to make sure that the link is down and the data path is in reset before
synchronization. This does NOT mean a complete shut down. The clocks are still
running and PLLs remain locked. The routines below may be used to bring the data
path down and up again. They also monitor the status of the transceiver lanes so
that they remain active.

The following routine resets the data path and keeps SYNC asserted. The SYSREF
is NOT active.

::

   gtlink_control(0);
   if (gtlink_sysref(0, 0xffff) != 0) {
     xil_printf("[%05d]: Interleaving Synchronization Failed, Exiting!!\n", __LINE__);
     return(-1);
   }

The following routine brings the data path out of reset and deasserts SYNC. The
SYSREF is set and status is checked for all data lanes to be active and in SYNC.

::

   gtlink_control(1);
   if (gtlink_sysref(1, 0x1ffff) != 0) {
     xil_printf("[%05d]: Interleaving Synchronization Failed, Exiting!!\n", __LINE__);
     return(-1);
   }

The software calibration essentially moves in and out of these two routines each
time making sure that SYSREF is sampled by the devices in order. The device-0
samples SYSREF at its rising edge (the rising edge of the ``conceptual clock``),
device-1 samples SYSREF at its rising edge after that (the falling edge of the
``conceptual clock``). The software moves the SYSREF until it sees a violation
on the signal by device-0 but NOT device-1. The setup window is set such that
this still does NOT cause an actual violation so that device-0 samples the
signal correctly. The routine only needs to look at setup violations. There may
be hold violations, but this can be ignored. The SYSREF is generated at
156.25MHz clock and is sampled at 2.5GHz, which means a SYSREF pulse remains
asserted for 16 cycles of its sampling clock. In other words, setup and hold can
NOT be violated in the same sampling edge.

::

   ad9625_sysref_sw_calibrate();

After calibration, the software brings the cores out of reset. As a measure of
the link status, it monitors the PRBS sequences and makes sure that they were
synchronized between the devices and the cores.

::

   adc_setup(ad9625_0, 1);
   adc_setup(ad9625_1, 1);

   ad9625_spi_write(0, AD9625_REG_TEST_CNTRL, 0x5);
   ad9625_spi_write(0, AD9625_REG_OUTPUT_MODE, 0x0);
   ad9625_spi_write(0, AD9625_REG_TRANSFER, 0x1);

   ad9625_spi_write(1, AD9625_REG_TEST_CNTRL, 0x5);
   ad9625_spi_write(1, AD9625_REG_OUTPUT_MODE, 0x0);
   ad9625_spi_write(1, AD9625_REG_TRANSFER, 0x1);

   if (adc_pn_mon(ad9625_0, 1, ADC_PN23A) != 0) return(-1);
   if (adc_pn_mon(ad9625_1, 1, ADC_PN23A) != 0) return(-1);

The devices are set to disable the test patterns and data format is set to 2"s
complement with sign extension. The ILA core is 16bits samples and the format
must be signed decimal to display analog signal correctly.

::

   ad9625_spi_write(0, AD9625_REG_TEST_CNTRL, 0x0);
   ad9625_spi_write(0, AD9625_REG_OUTPUT_MODE, 0x1);
   ad9625_spi_write(0, AD9625_REG_TRANSFER, 0x1);
   adc_write(ad9625_0, ADC_REG_CHAN_CNTRL(0), 0x51);

   ad9625_spi_write(1, AD9625_REG_TEST_CNTRL, 0x0);
   ad9625_spi_write(1, AD9625_REG_OUTPUT_MODE, 0x1);
   ad9625_spi_write(1, AD9625_REG_TRANSFER, 0x1);
   adc_write(ad9625_1, ADC_REG_CHAN_CNTRL(0), 0x51);

Making & Breaking
~~~~~~~~~~~~~~~~~

The design instantiates an ILA core that rolls out the interleaved 512 samples
per clock to just 1 sample per clock. This helps us to understand the
interleaving order issues, if any.

The plots below are when things work as expected.

1. The ILA waveform as it is.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_1_1.png
   :width: 800px

2. The sine wave zoomed in between -1 to 1.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_1_2.png
   :width: 800px

3. The same above with values zoomed in, notice that all the samples are in
   increasing order.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_1_3.png
   :width: 800px

4. At the zero crossing with values zoomed in, again samples are in increasing
   order.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_1_4.png
   :width: 800px

In order to better understand the interleaving order issues, we could break the
system. The calibrate function may be replaced or immediately followed by the
following routine to cause a violation.

::

   while (1) {
      gtlink_control(0);
      if (gtlink_sysref(0, 0xffff) != 0) {
        xil_printf("[%05d]: Interleaving Synchronization Failed, Exiting!!\n", __LINE__);
        return(-1);
      }

      gtlink_control(1);
      if (gtlink_sysref(1, 0x1ffff) != 0) {
        xil_printf("[%05d]: Interleaving Synchronization Failed, Exiting!!\n", __LINE__);
        return(-1);
      }

      if (ad9625_sysref_status() != 0) break;
   }

If it failed, the plots will show samples out of order.

1. The ILA waveform as it is.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_2_1.png
   :width: 800px

2. The sine wave zoomed in between -1 to 1, notice the ``saw-tooth`` created by
   out of order samples.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_2_4.png
   :width: 800px

3. The same above with values zoomed in, notice that the alternative samples are
   swapped, but within themselves, they maintain the increasing order.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_2_2.png
   :width: 800px

4. At the zero crossing with values zoomed in, again alternative samples are out
   of order.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_2_3.png
   :width: 800px

And higher frequencies-

1. Around 900+ MHz.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_4_1.png
   :width: 800px

2. Around 66+ MHz.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_3_1.png
   :width: 800px

If interleaving is in the correct order, it may still appear to be out of order.
This is due to the differences in the offset and gain parameters. It should be
less visible when the input gradient is high but at the peaks must be clearly
visible. Here is the plot with interleaving in-order.

1. Interleaved signal

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_5_1.png
   :width: 800px

2. Zoom in the window below-

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_5_2.png
   :width: 800px

3. The samples are in order.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_5_4.png
   :width: 800px

4. Zoom in the window at the peak below-

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_5_3.png
   :width: 800px

5. The samples are in order, but appear to be out of order.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fmcadc5_ila_5_5.png
   :width: 800px

Modifications
~~~~~~~~~~~~~

An alternative to software calibration is to use a calibration signal (connector
J15) and let the HDL make the decision. This is in the works and I will update
this section shortly.

Downloads (HDL)
---------------

.. todo:: .. include: /resources/fpga/docs/hdl/downloads_insert.rst

   :start-after: .. start-fmcadc5
   :end-before: .. end-fmcadc5

.. todo:: .. include: /resources/fpga/docs/hdl/downloads_insert.rst

   :start-after: .. start-help-support
   :end-before: .. end-help-support

No-OS Software Source
---------------------

.. admonition:: Download

   - AD-FMCADC5-EBZ No-OS - :git-no-OS:`fmcadc5`
