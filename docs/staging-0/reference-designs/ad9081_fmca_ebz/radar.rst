.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz/radar

.. _ad9081_fmca_ebz radar:

gr-ofdmradar - OFDM Radar on MxFE Platforms using IIO
=====================================================

This page is dedicated to the details of building an OFDM radar on a ZCU102 +
AD9081 with GNURadio and IIO.

This was based on a paper pressented at:

-

 .. video:: https://www.youtube.com/watch?v=hXLwt3q2evs

- `slides <https://events.gnuradio.org/event/8/contributions/130/attachments/54/103/GRCON%202021%20Winter.pdf>`__

If you just want to get the software and hardware running, the following section
covers the setup instructions:

Software / Hardware Quickstart
------------------------------

To get started, in terms of hardware you will need:

- :xilinx:`Zynq UltraScale+ MPSoC ZCU102 Evaluation Kit <products/boards-and-kits/ek-u1-zcu102-g.html>`
- :adi:`AD9081 Evaluation Board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9081.html>`
- TX and RX antennas and cables, optionally additional external RF components
  like receiver LNA(s) or a TX PA
- A computer running linux. Windows may work too, but hasn"t been tested

Required software:

- A development device running x86_64 Linux
- Vivado 2020.2 (Or whatever the current hdl master branch requires), the Vitis
  SDK and a License for MPSoC parts (Included with evaluation kit)
- A recent software build toolchain. (Usually provided by your Linux
  distribution. build-essential on debian stable+, base-devel on ArchLinux,
  etc.)

Preparing the ZCU102 boot files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is usually a good idea to start out by installing a recent image of
:ref:`kuiper` onto the ZCU102"s SD card, so you don"t have to rebuild the
rootfs.

Linux Kernel
^^^^^^^^^^^^

Depending on the age of your release, you may need to build a more recent
kernel:

::

   # First clone the repository
   git clone :git-linux.git
   cd linux

   # First we need to make the Vitis arm64 gcc toolchain available and enable cross compilation
   export PATH=$PATH::`opt/Xilinx/Vitis/2020.2/gnu/aarch64/lin/aarch64-linux/bin/+`
   export ARCH=arm64
   export CROSS_COMPILE=aarch64-linux-gnu-

   # Then we can initialize the .config to something that enables most ADI drivers
   make adi_zynqmp_defconfig

   # And finally build our image
   make -j$(nproc) Image UIMAGE_LOADADDR=0x8000

   # Finally you can copy arch/arm64/boot/Image into the boot directory of the ZCU102 sdcard:
   cp arch/arm64/boot/Image /mnt/boot/

If you"re having trouble building the Linux image, there are more detailed
articles describing the process (WHERE!).

Finally you will have to build the correct device tree blob:

.. warning::

   This step is always necessary if you installed the default Kuiper image, even
   if your Kernel is up to date!

::

   # Build the device tree blob
   make xilinx/zynqmp-zcu102-rev10-ad9081-m8-l4-tdd.dtb

   # Copy to ZCU102 boot directory
   cp arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9081-m8-l4-tdd.dtb /mnt/boot/system.dtb

.. important::

   The device tree blob must be renamed to system.dtb!

Building the HDL
^^^^^^^^^^^^^^^^

::

   # Source your Vivado 2020.2 (or later, depends on the adi/hdl release) settings
   source /opt/Xilinx/Vivado/2020.2/settings64.sh

   # Clone the HDL
   git clone https://github.com/Yamakaja/hdl.git
   git switch data_offload

   # Navigate to the ad9081 / ZCU102 project
   cd projects/ad9081/ad9081_fmca_ebz/zcu102/

   # Build the project with TDD support. Note that enabling TDD support is only possible if you also enable shared device clocks, which means that your IO rates will be symmetrical.
   make TDD_SUPPORT=1 SHARED_DEVCLK=1

The HDL build should take around 15 - 30 mins, and leave you with a
projects/ad9081_fmca_ebz/zcu102/ad9081_fmca_ebz_zcu102.sdk/system_top.xsa when
its done.

This guide describes how you can use the system_top.xsa to build the BOOT.BIN,
which also needs to be copied into the sdcard"s boot partition:
:dokuwiki:`build-the-zynqmp-boot-image </resources/tools-software/linux-software/build-the-zynqmp-boot-image>`

Once you"ve got an updated linux Image, BOOT.BIN and system.dtb installed and
the AD9081 eval board mounted on the ZCU102, you can start to hook up a receive
and transmit antenna / or other RF components.

Building GNU Radio
~~~~~~~~~~~~~~~~~~

To use the gr-iio AD9081 and TDD blocks, you will have to build this GNU Radio
fork/branch, which is fairly close to master:
`Yamakaja/GNURadio <https://github.com/Yamakaja/gnuradio/commits/feature/gr-iio-tdd>`__

::

   # Checkout code
   git clone https://github.com/Yamakaja/gnuradio.git
   git switch feature/gr-iio-tdd

   # Note, you should adjust the cmake build command according to your local environment! This one was created to work with my environment
   mkdir -p build
   cmake -DCMAKE_INSTALL_PREFIX=/usr/local
       -DPYTHON_EXECUTABLE=$(which python3)
       -DPYTHON_INCLUDE_DIR=/usr/include/python3.9
       -DPYTHON_LIBRARY=/usr/lib/libpython3.9.so
       -DGR_PYTHON_DIR=/usr/lib/python3.9/site-packages
       -DENABLE_GRC=ON
       -DENABLE_GR_QTGUI=ON
       -DQWT_LIBRARIES=/usr/lib/libqwt.so
       -DCMAKE_BUILD_TYPE=Debug
       -B build
       -S .

   make -C build -j$(nproc)

   # Install GNU Radio into system directories
   sudo make -C build install

   # Make sure the installation was successful by opening gnuradio-companion
   LD_LIBRARY_PATH=/usr/local/lib /usr/local/bin/gnuradio-companion

Building gr-ofdmradar
~~~~~~~~~~~~~~~~~~~~~

On account of being a GNU Radio module, the process to build gr-ofdmradar is
quite similar:

::

   # Checkout code
   git clone :git-gr-ofdmradar.git
   cd gr-ofdmradar

   # Make sure this build command matches that of your GNU Radio installation!
   mkdir -p build
   cmake -DCMAKE_INSTALL_PREFIX=:`usr/local+`
       -DPYTHON_EXECUTABLE=$(which python3)
       -DPYTHON_INCLUDE_DIR=/usr/include/python3.9
       -DPYTHON_LIBRARY=/usr/lib/libpython3.9.so
       -DGR_PYTHON_DIR=/usr/lib/python3.9/site-packages
       -DCMAKE_BUILD_TYPE=Debug
       -B build
       -S .

   make -C build
   sudo make -C build install

When you now start GNU Radio companion once again, the gr-ofdmradar blocks
should show up in the block-list:

::

   LD_LIBRARY_PATH=/usr/local/lib /usr/local/bin/gnuradio-companion

Testing the OFDM Radar
~~~~~~~~~~~~~~~~~~~~~~

Simulation
^^^^^^^^^^

To validate that the ofdm radar module has been installed properly, you can
launch the ofdmradar_test example in the examples directory of gr-ofdmradar:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/ofdmradar-simulation-flowgraph.png

Running the flowgraph should leave you with a radar screen simulating four
targets:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/ofdmradar-simulation-screen.png

On ZCU102 / AD9081
^^^^^^^^^^^^^^^^^^

To test the OFDM radar with real hardware and signals, open the
ofdmradar_ad9081.grc flowgraph in the gr-ofdmradar example directory.

.. important::

   The ``iio_target`` variable must point to the IP address of your ZCU102
   target!

.. warning::

   The default configuration of the example flowgraph may be in violation of
   your local regulations! Make sure not to transmit on bands which are not
   allocated to you, and keep power limits in mind!

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/ofdmradar-ad9081-flowgraph.png

The following video shows a test where we covered a distance of ~35m:

.. video:: https://www.youtube.com/watch?v=gtTILs929aU

Useful resources
~~~~~~~~~~~~~~~~

For more details in general about the theoretical underpinnings of OFDM radar,
please check out Martin Brauns dissertation:
https://publikationen.bibliothek.kit.edu/1000038892

For more information about gr-ofdmradar system parameters check out the
:git-gr-ofdmradar:`gr-ofdmradar/README.md <README.md+>`

- `gr-ofdmradar <https://github.com/analogdevicesinc/gr-ofdmradar>`__
- `GNU Radio branch with AD9081 blocks <https://github.com/Yamakaja/gnuradio/tree/feature/gr-iio-tdd>`__

--------------

Using the OFDM Radar
--------------------

This section will describe how you can use the OFDM radar to get some actual
returns, how you can tune the system and choose your parameters.

Before going on, please make yourself familiar with the basic operating
principles of an OFDM radar, and the meaning of the system parameters:
:git-gr-ofdmradar#operating-principle

To reinforce your understanding, lets take a look at this example set of
parameters.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_sysparams.png

- The complex system sample rate is ``f_s = 250 MS:`s``,+`
- the FFT Size ``N = 4096``,
- a frame has ``M = 16`` symbols
- and the cyclic prefix length "" N_CP = 256"", \* and ""N_NG = 64"" nyquist
  guard carriers

thus

::

   *the total TX frame length is ''L = (N+N_CP)*M = 69632 samples'',
   * the frame duration is ''T = L / f_s = 279µs'',
   *the (non-oversampled), "theoretical" time domain resolution is ''~c/(2*f_s) = 60 cm'',
   *the (non-oversampled) doppler resolution is ''f_s / ((N+N_CP)*M) = 3590 Hz'' (Pretty bad when you want to estimate speeds, not distance),
   *the true system bandwidth is ''B = (N - 2*N_NG)/N * f_s = 242.2 MHz'',
   *the final processing gain ''G = 10* log10(N * M) ~= 48 dB'',
   *and finally the covered distance spread: ''d = N_CP*c / (4*f_s) = ~77 m''. Other distances may be rendered, but the delay spread should stay below this value to keep the ofdm convolution cyclic.

This leaves us with a couple flowgraph parameters that should be discussed:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_sysparams_annotated.png

- The ``buffer_size`` is used to control how many samples the OFDM radar
  receiver should accept per frame, instead of the frame size itself - the frame
  length ``L`` may not always be a nice value. Note due to obvious reasons this
  value should never be smaller than the actual frame size!
- The ``amplitude`` parameter controls the transmit power by pre-multiplying the
  TX signal. Note that because of the exhibited processing gain, the required
  transmit power may be rather small.
- ``t_0`` is used in the TDD engine and allows you to adjust the offset between
  the start of the transmission and the start of the recording. This value
  should be calibrated according to your system to allow the determination of
  true ranges from the resulting returns.
- The ``display_mult`` parameter is used in the receive path to scale the
  intensity of the return signal for the optimal viewing experience™, but does
  not change the receiver sensitivity . This is simply a post-processing /
  visual operation!

Now lets take a look at the OFDM radar screen as you may see it when opening the
simulation example in gr-ofdmradar:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_screen.png

There are still four parameters left to be explained, that control visualization
parameters (But don"t change anything about the signals themselves):

- The range slider controls range which is shown, and can be thought of as an
  inverted zoom slider: If you want to zoom in the range dimension, move the
  slider to the left.
- The doppler range slider works similarly, but reduces the doppler ranges which
  are shown. This isn"t usually too much of an issue.

To explain the min and max value sliders, we need to take a look at how the
visualization code works:

- The input values to the gui widget have already been fully processed and can
  be thought of as a complex 2D matrix over range and doppler. To visualize this
  matrix we first take the energy of each value, then use a mapping function
  like the following to map those energy values to something between 0 and 1,
  where ``minV`` and ``maxV`` are controlled by the sliders:

::

   def mapv(x):
       x = (x-minV)/(maxV-minV)
       return max(min(x, 1.0), 0.0)

This value is then fed though the turbo color map and shown on screen. For more
information see the fragment shader in which all of this is happening:
:git-gr-ofdmradar:`lib/resources/screen.frag`

To really get an understanding of the max and min sliders you may need to play
around with them in a simulation, but at least now you should have an idea of
what they"re doing.

--------------

System deep dive
----------------

The system deep dive is meant to cover the details of the entire radar system
from top to bottom. Unless you"re trying to recreate a similar system from
scratch or trying to debug an issue, this section may not be too interesting.

Subsystems which will be covered:

- The Transceiver / RF ADC/DAC (AD9081)
- Hardware, HDL
- Linux drivers
- gr-ofdmradar and its blocks

ZCU102 / AD9081
~~~~~~~~~~~~~~~

Some notes on the device that were used:

The :adi:`AD9081 <en/products/ad9081.html>` is a 4-channel RF DAC/ADC in a
single package, with multi-chip synchronization and various other interesting
capabilities. Data is transferred from the DAC to the ADC over up to 8+8 (RX+TX)
SERDES lanes running JESD 204 B/C. Unfortunately the transceivers of the ZU9EG
on the :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` only go
up to ~15 Gbps, as such only JESD 204B operation is available with this hardware
configuration.

Problem statement
~~~~~~~~~~~~~~~~~

Before getting started with the implementation details, we need to establish why
hardware changes are necessary: To be able to implement a **reliable** and
**accurate** radar system, our interfaces must provide certain guarantees. Take
a look at this picture illustrating an ordinary pulse radar:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/pulse_radar.png

In this monostatic setup, the transmitter produces a small pulse, and then
listens for the return signal. To determine the distance to the target, the time
of flight is calculated by taking the time at which the signal returned, and
subtracting that from the transmit time. More information like the doppler
shift, RCS estimation, etc. can be estimated later on in the signal chain, but
these aren"t relevant right now. In this situation only the time of flight is
actually interesting to us, not the absolute time at which the signal was
received. To determine the time of flight, we need to rely on a **known**,
**fixed** timing relationship between the signal was sent out, and our input
samples at the receiver. There exist a number of solutions to this problem, for
example a strongly attenuated version of the TX signal could be looped back to
the receiver. In systems where the full data stream is available, and reliably
so, this may be an adequate solution, but the iio link does not lend itself to
such an approach - mostly because the data rates are much too high:

For the remainder of this page, we will assume that the default ZCU102 / AD9081
JESD configuration has been selected:

- 4 RX + 4 TX channels active @ 250 MS/s, 32-bit complex samples (16 + 16 bit)

::

   *=> ''Rate / direction = 4* 250e6 MS/s * 32 bit/S = 32 Gbps''

While the memory links and the FPGA can deal with these rates, the processing
system and/or the Gigabit ethernet link clearly cannot.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/system_link_rates.png

An issue that result from this bandwidth bottleneck should be fairly obvious: We
cannot transmit or receive a continuous sample stream from GNU Radio. This
problem isn"t unique to the direct RF platform we"re working with here, but also
applies to many other devices like the Pluto SDR, for all sample rates exceeding
the ~3-8 MS/s (?) supported by the USB 2.0 link.

.. tip::

   The following section assumes you have a basic understanding of iio buffers.
   If you"d like a refresher, take a look at the
   :dokuwiki:`IIO internals wiki page </resources/tools-software/linux-software/libiio_internals>`.

So what are the guarantees provided by iio?

- All samples which are part of a single buffer will be played as a continuous
  stream.
- Buffers will not be reordered

By default this will result in a situation like the following, where RX and TX
buffers are sampled completely independently, and the distance between each
buffer is also apparently random:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/iio_buffers_unaligned.png

To summarize, the two issues which we need to address:

- The data rates supported by the link make continuous transmissions impossible,
  we need to work with individual buffers
- When not transmitting continuously, the relationship between RX and TX is
  completely unknown.

The first issue may be addressed fairly easily by increasing buffer sizes. On
one hand this means that our entire transmit and receive waveform need to fit
into memory at once, on the other we are guaranteed that this waveform will be
continuous!

The second problem is much more tricky to solve, and requires modifications to
the HDL. The basic idea is as follows: What if we don"t stream continuously at
the hardware level, but only in small bursts at predetermined times. This means
that we"re effectively using hardware to cut out small windows of the transmit
and receive signals and only allowing those to pass onto the DMA (Or from the
DMA to the signal chain). This results in a greatly reduced data rates (in a
controlled manner), and known relationships between RX and TX. The following
picture illustrates what this system should do (Which is very similar to the
triggering mechanism in an oscilloscope):

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/iio_buffers_aligned.png

The HDL
~~~~~~~

.. tip::

   As of writing this document, not all HDL changes have made it into the
   :git-hdl:`upstream </>` repository yet, thus you may either use my
   development branch, or make sure that the most recent commits from that
   branch have made it into master (Though at that point this paragraph should
   be updated): https://github.com/Yamakaja/hdl/tree/data_offload

On the HDL side we will be using a Timing Division Duplexing (TDD) core, which
was originally developed to control the :adi:`en/products/ad9361.html` family of
transceivers: See the
:dokuwiki:`reference_hdl </resources/eval/user-guides/ad-pzsdr2400tdd-eb/reference_hdl>`
for more information about what the TDD core can do.

Because the TDD engine was previously not available as a standalone IP core, i
created a small wrapper which just references the existing tdd files from the
util and/or common directory:
:git-hdl:`''axi_tdd'' <tree/master/library/axi_tdd+>`.

.. tip::

   While the terminology of the TDD engine registers and signals is derived from
   their use with the AD9361, the different channels function completely
   independently, and may as well just have been numbered in this case.

The data offload engine
^^^^^^^^^^^^^^^^^^^^^^^

Now we should take a look at the ``data offload``, which is responsible for
sampling the stream when triggered by the TDD engine (It"s basically a glorified
FIFO). The data offload is a rather complex block that offers a multitude of
functions and configuration options, for more information see the readme:
`README.md <https://github.com/Yamakaja/hdl/blob/data_offload/library/data_offload/README.md>`__

The interesting part for us are the synchronization modes, which allows the data
offload to remain in a waiting state, until it is triggered either by a write to
a register or externally. The integration into the HDL is as follows:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/ad9081_zcu102_bd_tdd_do.png

.. tip::

   While the data offload engine is triggered by the positive level of the
   ``sync_ext`` signal, the value of that signal is only relevant in the initial
   waiting phase. Once the data offload has been triggered, the external sync
   signal may go LOW immediately. While the exact time that the TDD engine keeps
   that synchronization signal high isn"t too important, keeping it high for too
   long may trigger a second buffer!

As you can tell, the ``tdd_tx_valid`` line is simply connected to the external
synchronization input of the TX data offload. This means that we can precisely
control the start of the sample replay using the TDD engine. Once it has been
triggered, it will fill up its internal buffer (Who"s size \*must\* be an
integer multiple of the iio buffer size. If it"s not, you can use the transfer
length register of the data offload to make sure things line up), and then play
it back to the upack core that takes the packed sample stream and deinterleaves
them into a parallel bus (two \* 16 bit per complex channel, see JESD"s M
parameter) with ""128-bit @ 250 MHz"".

For a more detailed look at the datapath with the M=8, L=4 configuration, take a
look at the following illustration. Now however, that for our purposes the
``UTIL_DACFIFO`` and ``UTIL_ADCFIFO`` have both been replaced by data offloads.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_204b_m8l4.svg

Synchronization on the RX side is a little more involved, to explain why we need
to take a look at the data packing format and the cpack cores. Imagine the
following situation (Which will be quite common ;) ), you"ve got the default
JESD configuration running (Four complex channels), but only one of those
channels is actually in use. It would obviously be a waste to transfer data
which isn"t used, which is why the [cu]pack cores take a parallel stream of
samples (All four channels, no matter which are in use) and turn that into an
interleaved stream of a lower rate. That is if only a single channel out of four
is active, in the above situation the output of the CPACK core will be valid
only once for every four samples, and that one valid sample of 128-bit will
contain all 4 complex samples for that single channel. Because the cpack core is
located before the data offload in the sample stream, this means that we can
store more samples when fewer channels are active.

Now finally the problem i"ve been trying to hint at: The tdd synchronization
signal is not in any way related to the cpacks sample timer. That is depending
on where the cpack core is in its process of collecting four samples compared to
when the sync signal arrives, we may receive an apparently random shift of zero
to three samples. To correct for this phenomenon, currently the cpack core is
just reset with every sync signal. While this certainly isn"t a great solution,
it was the least invasive.

Linux Drivers
~~~~~~~~~~~~~

There are two drivers which may be interesting to take a look at here, the data
offload and TDD driver, though obviously from the system perspective more than
those two are involved.

Data Offload
^^^^^^^^^^^^

The :git-linux:`master:drivers/misc/adi-axi-data-offload.c` is for the most part
just configuring the data offload registers based on the values provided in the
device tree, and also providing a debugfs interface to modify those registers at
runtime. For more information on the device tree options see
:git-linux:`master:Documentation/devicetree/bindings/misc/adi,axi-data-offload.yaml`.

The second part of the driver is the integration into
:git-linux:`master:drivers/iio/frequency/cf_axi_dds.c`, which allows cyclic /
oneshot operation to be handled by the data offload - this feature in particular
is interesting when you"re sending the same radar waveform repeatedly, because
if the data offload is set to cyclic mode and synchronization is enabled, it
will wait for the sync signal before each iteration. Effectively this will allow
you to replay a buffer on the transmit side as often as you"d like, while only
ever loading it once.

TDD
^^^

The :git-linux:`TDD driver <master:drivers/iio/adc/cf_axi_tdd.c>` provides a
couple device tree attributes which can be used for static configuration, but
more importantly it provides an IIO device which can be used to control the tdd
timing registers via the usual iio interface.

<code> iio:device2: axi-core-tdd

::

   4 channels found:
       data1:  (output, WARN:iio_channel_get_type()=UNKNOWN)
       6 channel-specific attributes found:
           attr  0: dp_off_ms value: 0
           attr  1: dp_on_ms value: 0
           attr  2: off_ms value: 0
           attr  3: on_ms value: 0
           attr  4: vco_off_ms value: 0
           attr  5: vco_on_ms value: 0
       data1:  (input, WARN:iio_channel_get_type()=UNKNOWN)
       6 channel-specific attributes found:
           attr  0: dp_off_ms value: 0
           attr  1: dp_on_ms value: 0
           attr  2: off_ms value: 0
           attr  3: on_ms value: 0
           attr  4: vco_off_ms value: 0
           attr  5: vco_on_ms value: 0
       data0:  (output, WARN:iio_channel_get_type()=UNKNOWN)
       6 channel-specific attributes found:
           attr  0: dp_off_ms value: 0
           attr  1: dp_on_ms value: 0
           attr  2: off_ms value: 0
           attr  3: on_ms value: 0
           attr  4: vco_off_ms value: 0
           attr  5: vco_on_ms value: 0
       data0:  (input, WARN:iio_channel_get_type()=UNKNOWN)
       6 channel-specific attributes found:
           attr  0: dp_off_ms value: 0
           attr  1: dp_on_ms value: 0
           attr  2: off_ms value: 0
           attr  3: on_ms value: 0
           attr  4: vco_off_ms value: 0
           attr  5: vco_on_ms value: 0
   10 device-specific attributes found:
           attr  0: burst_count value: 0
           attr  1: counter_int value: 0
           attr  2: dma_gateing_mode value: rx_tx
           attr  3: dma_gateing_mode_available value: rx_tx rx_only tx_only none
           attr  4: en value: 0
           attr  5: en_mode value: rx_tx
           attr  6: en_mode_available value: rx_tx rx_only tx_only
           attr  7: frame_length_ms value: 0
           attr  8: secondary value: 0
           attr  9: sync_terminal_type value: 0
   1 debug attributes found:
           debug attr  0: direct_reg_access value: 0x10061
   No trigger on this device

</code>

GNU Radio Integration
~~~~~~~~~~~~~~~~~~~~~

The GNU Radio integration consists of two parts:

- Hardware control blocks, part of in-tree gr-iio
- Hardware independent signal processing blocks, part of gr-ofdmradar

gnuradio/gr-iio
^^^^^^^^^^^^^^^

These are:

- AD9081 Source / Sink
- TDD Engine Control

AD9081 Source / Sink
''''''''''''''''''''

These work like pretty much any other source and sink blocks, but with a small
twist: We always assume to be working with bursty data, where one burst is the
size of one iio buffer. Burst / buffer boundaries are indicated by a packet
length tag like this:

::

   -> [... x-2, x-1, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, ... ]
                     ^                                       ^
                     | { packet_len: 10 }                    | { packet_len: 10 }

Now because all iio buffers from one source will always have the same size, the
length tags are somewhat redundant, but allow other blocks which cannot make
these assumptions to work with those streams.

.. important::

   If the packet length tag name field is populated in the AD9081 sink block, it
   will enforce that the received stream is tagged correctly. A tagging error
   will not be handled gracefully and abort the flowgraph!

The attributes which are available in GR boil down to the following:

- IIO context uri
- IIO buffer size
- Packet length tag
- NCO attributes

With some additional source/sink specific attributes:

- Sink: Cyclic Mode
- Source: Nyquist Zone (Odd / Even)
- Source: Programmable hardware FIR filter file

**AD9081 Sink Block**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_iio_ad9081_sink_general.png

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_iio_ad9081_sink_channels.png

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_iio_ad9081_sink_coarse_duc.png

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_iio_ad9081_sink_fine_duc.png

**AD9081 Source Block**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_iio_ad9081_source_general.png

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_iio_ad9081_source_coarse_ddc.png

.. tip::

   Note the use of ``gr.nyquist_fold``. This function takes your targeted
   frequency and ADC sample rate, and calculates the required NCO frequencies
   taking aliasing and spectral inversion into account.

TDD Control
'''''''''''

The TDD control block does not have any stream io, and only provides easy access
to the underlying IIO attributes:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_iio_tdd_general.png

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_iio_tdd_primary_timing.png

gr-ofdmradar
^^^^^^^^^^^^

gr-ofdmradar is where all the interesting signal processing is happening.
gr-ofdmradar ships with two categories of blocks: Those implementing OFDM Radar,
and those implementing direction of arrival (DoA) for a linear array.

OFDM Radar Blocks
'''''''''''''''''

Many of the system parameters are shared between the TX, RX and GUI blocks, thus
these are stored in a separate ``OFDM Radar System Parameters`` block:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_params.png

The ``OFDM Radar Transmitter`` block takes just the system parameters and a
length tag key, and outputs a full OFDM radar frame. This frame is length-tagged
using the provided key to allow interoperability with the AD9081 sink:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_tx.png

The ``OFDM Radar Receiver`` is very similar in terms of parameters, but takes an
additional buffer size:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_rx.png

.. tip::

   The ``Buffer Size`` parameter determines how many samples will be expected /
   ofdm frame. While the amount of samples which is actually processed is
   determined by the ofdm system parameters, the block can consume (and discard)
   additional samples to align frame boundaries to the iio buffers for example.
   The amount of discarded samples after each received ofdm frame can be
   determined as ``buffer_size - radar_params.frame_length``.

Finally the ``OFDM Radar GUI`` block takes ofdm radar params and a GUI hint:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_gui.png

**For more information on the parameters and OFDM radar algorithm, take a look
at the**
`gr-ofdmradar/README.md <https://github.com/analogdevicesinc/gr-ofdmradar#operating-principle>`__\
**.**

DoA Blocks
''''''''''

The Doa blocks are less integrated, but also don"t come with many parameters.
The implicit assumption is that we"re working with a linear array and
""lambda/2"" spacing - the main parameter is pretty much how many targets we are
expecting, and how many receiver channels we have.

**DoA Autocorrelator**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_doa_corr.png

**DoA Calibration Block**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_doa_cal.png

**DoA MUSIC Estimator**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_doa_music.png

**DoA ESPRIT Estimator**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9081_fmca_ebz/radar/gr_ofdmradar_doa_esprit.png
