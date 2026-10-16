.. _pluto devs embedded_code:

Building Apps For PlutoSDR Standalone
=======================================

PlutoSDR includes a single-core ARM® Cortex™-A9 MPCore™ running at 666.66 MHz
for which ADI provides a :git-buildroot:`BuildRoot <pluto:README>` based Linux
distribution. This is part of the firmware provided with PlutoSDR. Many users
of PlutoSDR run applications on a local PC and stream data to and from
PlutoSDR in frameworks like GNU Radio or MATLAB. However, since PlutoSDR is
running Linux users can also write C or C++ applications, among others, that
can be cross-compiled on a host, and then run on PlutoSDR itself like any
other Linux system. This page will discuss an example application, including
the necessary tools, to build applications on a host machine and run them
directly on the PlutoSDR.

Prerequisites:

- A host machine to run a compiler on. This can be either Windows (x86) or
  Linux (x86 or ARM) (yes, you can build PlutoSDR Applications on Raspberry
  Pi). (it's possible on macOS, but just more difficult, since you will need
  to build a toolchain from scratch, beyond the scope of what we're willing to
  write - check google, you are on your own).
- A compiler with the same version used to compile the PlutoSDR firmware. See
  the Pluto SDR mass storage device file ``index.html``, or check the
  `PlutoSDR firmware releases page <https://github.com/analogdevicesinc/plutosdr-fw/releases>`__
  for the relevant information.

  - :xilinx:`Xilinx SDK <products/design-tools/embedded-software/sdk.html>`
  - `Linaro toolchain <http://releases.linaro.org/components/toolchain/binaries/>`__

- System Root of the firmware used on PlutoSDR itself (this will be downloaded
  in the example). This includes the libraries (binaries, so you can
  statically link to things if you want), and headers for those libraries.
  It's important that the compiler be told where things are, so it can find
  the headers and libraries for the Pluto. This can either be done on the
  command line, or by replacing the default sysroot that the compiler comes
  with. If you are only compiling things for Pluto - this is a convenient
  solution, but will eventually will cause problems when you forget, and try
  to compile something else with this same toolchain.

Once you have the necessary tools we can start to build an application. This
example will be done using Linux since it is by far the simplest to set up. We
will use v0.30 of the firmware, which is assumed running on the PlutoSDR. If
you change the firmware you will likely have to recompile your applications
since the compiler or libraries running on the Pluto can change over time.

Set up your Linux Host
-----------------------

#. Make sure to use either the Xilinx or the Linaro toolchain (you only need
   one)

   #. Assuming you have the Xilinx SDK installed in ``/opt/Xilinx``, add the
      necessary tools to your path:

      .. code:: console

         tcollins@winston: source /opt/Xilinx/Vivado/2018.2/settings64.sh

   #. Grab the Linaro toolchain, unpack it, and add it to the path:

      .. code:: console

         tcollins@winston: cd /usr/local/bin
         tcollins@winston: sudo wget http://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-linux-gnueabihf/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabihf.tar.xz
         tcollins@winston: sudo tar -xf gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabihf.tar.xz
         tcollins@winston: export PATH=$PATH:/usr/local/bin/gcc-linaro-7.2.1-2017.11-i686_arm-linux-gnueabihf/bin

#. Make sure the compiler is in your path:

   .. code:: console

      tcollins@winston: arm-linux-gnueabihf-gcc --version
      arm-linux-gnueabihf-gcc (Linaro GCC 7.2-2017.11-rc1) 7.2.1 20171011
      Copyright (C) 2017 Free Software Foundation, Inc.
      This is free software; see the source for copying conditions.  There is NO
      warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#. Download the sysroot for your release of firmware, unpack it, and place it
   somewhere you will find it.

   .. code:: console

      tcollins@winston: wget https://github.com/analogdevicesinc/plutosdr-fw/releases/download/v0.30/sysroot-v0.30.tar.gz
      tcollins@winston: tar zxvf sysroot-v0.30.tar.gz
      tcollins@winston: mv staging $HOME/pluto-0.30.sysroot

#. First create a new directory for this project and move to it.

   .. code:: console

      tcollins@winston: mkdir /tmp/plutoapp
      tcollins@winston: cd /tmp/plutoapp

#. Grab the example code here:

   .. code:: console

      tcollins@winston: wget https://raw.githubusercontent.com/analogdevicesinc/libiio/libiio-v0/examples/ad9361-iiostream.c

#. Cross-compile the example by calling the compiler:

   .. code:: console

      tcollins@winston: arm-linux-gnueabihf-gcc -mfloat-abi=hard --sysroot=$HOME/pluto-0.30.sysroot -std=gnu99 -g -o pluto_stream ad9361-iiostream.c -lpthread -liio -lm -Wall -Wextra

Using the Linaro Toolchain on ARM hosts
-----------------------------------------

This is a little easier, since the compiler is already for ARM. You can follow
the instructions for the i686 devices, but do not install a different
compiler. And when compiling, just call gcc:

.. code:: console

   tcollins@rasberian: gcc -mfloat-abi=hard --sysroot=$HOME/pluto-0.30.sysroot -std=gnu99 -g -o pluto_stream ad9361-iiostream.c -lpthread -liio -lm -Wall -Wextra

Running on Pluto
-----------------

Copy the executable to PlutoSDR:

.. code:: console

   tcollins@winston: scp pluto_stream root@192.168.2.1:/tmp/

Run the app:

.. code:: console

   tcollins@winston:/tmp/plutoapp$ ssh -t root@192.168.2.1 /tmp/pluto_stream
   root@192.168.2.1's password: analog
   * Acquiring IIO context
   * Acquiring AD9361 streaming devices
   * Configuring AD9361 for streaming
   * Acquiring AD9361 phy channel 0
   * Acquiring AD9361 RX lo channel
   * Acquiring AD9361 phy channel 0
   * Acquiring AD9361 TX lo channel
   * Initializing AD9361 IIO streaming channels
   * Enabling IIO streaming channels
   * Creating non-cyclic IIO buffers with 1 MiS
   * Starting IO streaming (press CTRL+C to cancel)
   	RX     1.05 MSmp, TX     1.05 MSmp
   	RX     2.10 MSmp, TX     2.10 MSmp
   	RX     3.15 MSmp, TX     3.15 MSmp
   	RX     4.19 MSmp, TX     4.19 MSmp
   	RX     5.24 MSmp, TX     5.24 MSmp
   	RX     6.29 MSmp, TX     6.29 MSmp
   	RX     7.34 MSmp, TX     7.34 MSmp
   	RX     8.39 MSmp, TX     8.39 MSmp
   	RX     9.44 MSmp, TX     9.44 MSmp

Other standard applications
-----------------------------

Depending on the project you are doing - you may need to include something
like this in a Makefile project (with the appropriate path changes):

.. code:: makefile

   SYSROOT = /home/rgetz/github/pluto/staging/
   PKG_CONFIG_PATH=${SYSROOT}/usr/lib/pkgconfig
   CC=arm-linux-gnueabihf-gcc
   CFLAGS += --sysroot=${SYSROOT}
   LIBS += --sysroot=${SYSROOT}
