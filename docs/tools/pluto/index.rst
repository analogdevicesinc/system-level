.. _pluto:

ADALM-PLUTO
"""""""""""

.. toctree::
   :hidden:
   :glob:

   */index
   *

.. figure:: pluto_in_hand.png
   :width: 250
   :align: right

The :adi:`ADALM-PLUTO` Active Learning Module (PlutoSDR)
(:adi:`Buy <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html>`)
is an easy to use tool available from Analog Devices
Inc. (ADI) that can be used to introduce fundamentals of
`Software Defined Radio (SDR) <https://en.wikipedia.org/wiki/Software-defined_radio>`__ or
`Radio Frequency (RF) <https://en.wikipedia.org/wiki/Radio_frequency>`__ or
`Communications <https://en.wikipedia.org/wiki/Communication_theory>`__ as
advanced topics in electrical engineering in a self or instructor lead setting.
The PlutoSDR allows students to better understand the real-world RF around them,
and is applicable for all students, at all levels, from all backgrounds. Early
learning in a hands-on manner with the PlutoSDR will ensure a solid foundation
for students to build on, as they pursue science, technology, or engineering
degrees.

The PlutoSDR Active Learning Module is a tool that closes the relationship
between theory and practical radio frequency activities of the user. It provides
a personal portable lab that, when used with a host, can augment the learning
that takes place in the classroom. A variety of software packages such as MATLAB
or Simulink provide an innovative graphical user interface (GUI), allowing
intuitive usage and minimizing the learning curve, enabling students to learn
faster, work smarter, and explore more!

The :adi:`ADALM-PLUTO` Active Learning Module is a learning tool
for everyone.

Based on the :adi:`AD9363`, it offers one receive channel and one
transmit channel which can be operated in full duplex, capable of generating or
measuring RF analog signals from 325 to 3800 MHz, at up to 61.44 Mega Samples
per Second (MSPS) with a 20 MHz bandwidth. The PlutoSDR is completely
self-contained, fits nicely in a shirt pocket or backpack, and is entirely USB
powered with the default firmware. With support for OS X™, Windows™, and Linux™,
it allows exploration and understanding of RF systems no matter where the user
is or when.

Introduction
============

PlutoSDR is a self-contained RF lab in your hand. It's more than the combination
of a few parts, but to understand the capabilities of the module, you must
understand the fundamental operation of each part inside the module. Depending
on who you are, and what you want to do, you may have different needs, different
wants, and will use different software. It's expected that many people will stop
when they solve their immediate problem and don't want to go any deeper into the
stack. Before digging into the documentation, check out the module
:ref:`prerequisites <pluto prerequisites>`, and try to think about how you will
use the ADALM-PLUTO.

.. tip::

   PlutoSDR will populate as a Mass Storage Device when plugged into a
   computer. The presented storage device contains a getting started guide
   (info.html), configuration control for your device (config.txt), and licensing
   information (LICENSE.html).

#. :ref:`Quick Start <pluto users quick_start>`

#. :ref:`Hardware User Guide <pluto hacking hardware>`

#. :ref:`PlutoSDR Users & students <pluto users>`

   - PlutoSDR users normally interact with RF signals with
     :mw:`MATLAB, Simulink <hardware-support/adalm-pluto-radio.html>`,
     :ref:`GNU Radio <software gnuradio>`,
     :git-libiio:`C# <bindings/csharp/examples/ExampleProgram.cs>`,
     or :ref:`Python environment <pyadi-iio>` on a
     host (x86) Windows, Linux or Mac or embedded Linux platform
     (`Raspberry Pi <https://www.raspberrypi.org/>`__,
     `Beaglebone <http://beagleboard.org/>`__,
     `96boards.org <http://www.96boards.org/>`__, insert your favorite embedded
     Linux platform) over USB.
   - If you want to see how to :ref:`generate or capture RF waveforms <iio-oscilloscope>`,
     this is the place.
   - Everyone should read this section, as it describes the device, and
     describes how to get the drivers and host software installed properly.
   - Most users should find all the information they need in this section.

#. :ref:`C/C++ Examples <pluto transceiver_transferring_data>`

   - Controlling the transceiver and transferring data using libiio with C/C++.

#. :ref:`For Developers <pluto devs>`:

   - This material is for those who normally write custom software or HDL (for
     the FPGA) that runs directly on the PlutoSDR. This may put the PlutoSDR in
     different modes, and support different external USB devices (including LAN
     (via USB), or WiFi (via USB)), extending the capabilities of the device.
     This includes all the information to compile HDL projects, compile
     kernels, change to custom USB PID/VID and/or run custom user space
     applications. For example, you could set up:

     - a standalone airplane tracking station which communicates to the
       internet via Wifi or LAN.
     - a mobile terminal to emulate someone else's keyboard.

#. :ref:`Advanced Users <pluto hacking>`

   - This section may be useful for those taking the PCB out of the case and
     making hardware modifications, or connecting GPIO to different devices, or
     attempting to synchronize multiple PlutoSDRs together. Since this is
     pretty wide open, we don't have any examples of this - but we do provide
     the info needed, including all the schematics and layout.

It's expected that most people will work their way down through each section,
reading and skimming most of the content. The content is in a constant state of
improvement, so if you do have a question, please ask at
:ez:`EngineerZone <community/university-program>`,
or check the :ref:`help and support <pluto help_support>` page.

.. esd-warning::
