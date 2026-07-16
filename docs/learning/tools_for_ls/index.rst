.. _datax-tools-for-ls-system-design:

ADI DataX™ Tools for Low Speed Mixed Signal System Design
---------------------------------------------------------

.. note::

   This is a work in progress.

Introduction
~~~~~~~~~~~~

`ADI DataX™ <https://developer.analog.com/solutions/adi-datax>`__ is a highly
adaptable, open technology stack that bridges the gap between signal chains and
applications across a wide range of processing platforms, operating systems, and
software ecosystems to enable physically intelligent systems.

Rather than being a single library or runtime, ADI DataX is a collection of
reusable software building blocks, including device drivers, middleware, FPGA
IP, and reference designs - aligned under a common architecture and enablement
model. This concept is depicted somewhat abstractly in :numref:`fig-datax_diag`

.. _fig-datax_diag:

.. figure:: adi_datax_diag.png
   :width: 700px
   :height: 400px
   :align: center

   ADI DataX Layers

The goal of this tutorial is to bring :numref:`fig-datax_diag` to life in a
tangible way by working through two application examples that map into the
diagram as shown in :numref:`fig-datax_diag_w_apps`

.. _fig-datax_diag_w_apps:

.. figure:: adi_datax_diag_w_apps.png
   :width: 700px
   :height: 400px
   :align: center

   Applications mappped onto ADI DataX layers

What does “Enabled by ADI DataX” mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An Analog Devices product, reference design, or application example is "Enabled
by ADI DataX" if you can follow one or more unbroken paths across
:numref:`fig-datax_diag`, where:

- The compute platform is an easily available standard development board, or a
  bespoke / custom board based on a standard platform
- The OS-specific device drivers are open-source, fully documented
- Language bindings and A simple "Hello, World!" example are written for the
  Ecosystem, and are also open-source
- An application example either exists, or is trivial to derive from the "Hello,
  World!" example.

.. NOTE::

   Not all paths make sense for all products. A good example is the
   :adi:`ADM1266<adm1266>` sequencer -this device is used in large network
   infrastructure and data center boards, which typically have a board
   management controller running OpenBMC, a special-purpose embedded Linux. As
   such, a Raspberry Pi can serve as a proxy for the SoCs typically used in BMC
   applications, only a Linux driver is required, and the ecosystem and
   application layers are Phosphor and Redfish. With a single path, this part is
   "fully ADI DataX enabled". 

But wait, there's more! We also pre-build boot files for as many of these cases
as possible. This means you can bring up examples without having to install and
configure toolchains right away. This can be a huge timesaver when you just want
a quick proof of concept, and don't want the overhead of installing a piece of
software you may not be familiar with (FPGA tools, compilers for processors
you're not going to be using beyond initial development, etc.).

The ADI :ref:`kuiper` Linux distribution is a big part of the "get up and
running quickly" philosophy. Kuiper is a specialized Debian-based Linux
distribution designed specifically for Analog Devices hardware and evaluation
boards. It provides a complete, ready-to-use environment with ADI libraries,
tools, and applications pre-configured for seamless hardware integration.

Rather than manually installing and configuring individual ADI software
components, Kuiper delivers a cohesive development platform that eliminates
setup complexity and gets you running immediately.

The no-OS framework is ADI's bare-metal device drivers, platform drivers, and
example projects, and it too shares the same philosophy. Projects are
automatically built as part of the continuous integration (CI) process, and boot
files for each project, often supporting several platforms, are available in the
releases section of the repository on GitHub.

Developing a Product with ADI DataX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this tutorial, we will help strategic and key customer Fred in the Shed
Instruments, Inc. develop their first products:

- A temperature sensor with options for local display and network connectivity
- A handheld transistor curve tracer for the custom guitar pedal industry

The temperature sensor simply involves reading temperature, doing some math to
convert units if necessary, and displaying the result. The curve tracer involves
setting voltages and currents, reading voltages and currents, doing some basic
math, and displaying a result. Each reading is considered independently, no
correlation to previous or future readings. We will NOT be measuring AC Signal
to Noise Ratio (SNR), Total Harmonic Distortion (THD), nor measuring steps,
wiggles, wavelets, or any other situation where precise timing is required. Rest
assured, there are lots of very interesting applications in this category;
consider a vector network analyzer (VNA) - set an excitation frequency, measure
forward and reflected power and phase, do some math, step, repeat, and when
done, display the results.

We will start with a Linux-based workflow, leveraging Linux device drivers
pre-built in ADI Kuiper Linux, Pyadi-iio. We'll then show how to migrate to
other languages (C, C#, MATLAB), other processing platforms (ARM-based
MAX32xxx, Raspberry Pi Pico), ecosystems (no-OS / bare metal, Zephyr), and
middleware layers (GNURadio, ROS). With ADI DataX, switching between these
layers is cheap - there is little to no barrier to getting a proof of concept up
and running in Linux, then switching to bare metal or Zephyr as development
continues.

Complete written instructions follow, as well as a video guide and a slide deck
that can be used for delivering as a hands-on workshop.

.. NOTE::

   What exactly does “Low Speed” mean? In the context of this tutorial, it means
   that timing is not very critical. Signals are either completely static
   or moving slowly such that it doesn't matter if the instant that an ADC samples
   the signal wiggles around a bit relative to the previous sampling. While clock
   jitter is one source of this uncertainty, software delays (such as the time
   between a timer interrupt and the assertion of a “convert” edge) will likely be
   dominant. Important parameters in low-speed applications are offset, gain error,
   linearity, and temperature drift. “Noise” in a low-speed application is
   typically synonymous with resolution, and can be roughly measured by applying a
   quiet input signal (like a short circuit) and taking a histogram of the output
   readings. AC performance metrics such as signal to noise ratio and total
   harmonic distortion extracted from a Fourier transform of the data will not be
   considered. In contrast - sample jitter is important in a “high speed”
   application. If you are measuring signal to noise ratio, the Signal to Noise
   ratio (SNR) can be no greater than:

   :math:`SNR <= -20 * log(2*\pi*f_{IN}*t_{j})`

   Where:

   :math:`f_{IN}` is the analog input frequency in Hz

   :math:`t_{j}` is the RMS jitter in seconds RMS



Materials
~~~~~~~~~

- Raspberry Pi 4, 400, 5 or 500; 2GB or greater RAM (for Linux examples). (Model 3B, 3B
   Plus will work, but you will want a 4, 400, 5, or 500 :-) )
- 5V USB-C wall adapter for Raspberry Pi (micro USB for model 3)
- 16GB (or larger) Class 10 (or faster) micro-SD card, with :ref:`kuiper` installed
- User interface setup (choose one):
   - HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi
   - Host Windows/Linux/Mac computer on same network as Raspberry Pi
-  :adi:`ADALM2000
   <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm2000.html>`
   (Optional, for observing signals.)
- :adi:`MAX32666FTHR<max32666fthr>` development board (for no-OS examples)
- Either:
   - :adi:`ADALM-LSMSPG<adalm-lsmspg>` Low-Speed Mixed Signal Playground module
- Or:
   - :adi:`EVAL-AD5592R-PMDZ<eval-ad5592r-pmdz>`
   - :adi:`EVAL-AD5593R-PMDZ<eval-ad5593r-pmdz>`
   - :adi:`Raspberry Pi to PMOD/QuikEval™/LTpowerPlay® Adaptor HAT<pmd-rpi-intz>`
   - 2N3904 NPN Transistor
   - 2N3906 PNP Transistor
   - 47Ω resistor
   - 47kΩ resistor
   - Breadboard or prototyping board, hookup wire
- Clone or download zip of the Python code for this tutorial:
  :git-pyadi-iio:`ADALM-LSMSPG Pyadi-IIO examples<examples/adalm-lsmspg>`
- Note that these are included in the pyadi-iio repo, consider cloning the entire thing:

.. shell::

  $git clone https://github.com/analogdevicesinc/pyadi-iio.git

-  AD5592R Device Tree Overlay for alternate configuration with GPIO pins

.. ADMONITION:: Download

   :dokuwiki:`rpi-ad5592r-with_gpios-overlay source and compiled overlay <_media/university/labs/software/tools_for_low_speed_mix-sig_systems/rpi-ad5592r-with_gpios-overlay.zip>`



Slide Deck and Video
~~~~~~~~~~~~~~~~~~~~

Since this tutorial is also designed to be presented as a live, hands-on
workshop, a slide deck is provided here:

.. ADMONITION:: Download

   :download:`Tools for Low-Speed Mixed Signal System Design Slide Deck <tools_for_low_speed_ms_workshop.pptx>`

A complete video run-through is also provided, either as a companion to
following the tutorial yourself, or to practice before presenting as a
hands-on workshop.

.. NOTE:: 

   This video is accurate, but uses the AD5592 Pmod and discretely built
   circuit. It will be re-done to target the ADALM-LSMSPG board.

.. video:: https://www.youtube.com/watch?v=tJtzUrt9_1U


Preparation - a few resources for learning Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While this is not intended to be a Python-centric workshop, it sort of ends up
that way by default because Python is so easy to use and flexible, so we use it
as a tool througout. Even if you are not using Python in your end application,
it often still makes sense as an intermediate tool during development. If you're
not at least somewhat familiar with the language, A wonderful resource for
learning Python is `learnpython.org <https://learnpython.org/>`__, runs right in
your browser without needing to install anything. We're not going to go super
deep into Python arcana and minutia by any means - the "Learn the Basics"
section will leave you more than prepared for what follows.

And despite the name, `Python for Kids
<https://nostarch.com/python-kids-2nd-edition>`__ is surprisingly good for
adults, too!



Software Stack Background, and, To Deliver You from the Preliminary Terrors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A typical Linux-based software stack is shown in :numref:`fig-annotated_stack`.
It's pretty scary, even a relatively simple application exercises most of these
layers, and a full understanding of each and every layer is outside of the
skillset of most engineers - including most software engineers. **And that's
okay**.

.. _fig-annotated_stack:

.. figure:: annotated_stack.png
   :width: 700px
   :align: center

   Annotated Linux software stack

For engineers that are bringing their brainstorms to life for the first time,
building proof of concept, and early prototypes, you don't need to understand
all of the layers. The goal is to operate at a point in the stack where you can
quickly add value - try out a couple of ADCs, DACs, IMUs, or other parts without
having to start from scratch each time. Build basic command line programs that
achieve proof of concept, deferring pretty, focus-group vetted GUIs for later.
The goal of ADI DataX is to expose this operating point as efficiently as
possible so you can get to work.

Introducing the exciting new products to which we'll apply our skills
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The temperature sensor is intended as an "as simple as possible" application.
The temperature sensor IC itself is the ADT75, which has cross-references from
multiple manufacturers (all inferior to Analog Devices, of course!). The Linux
device driver has been in the kernel since at least version 2 (1998), and you
can buy a ten-pack of breakout boards for $15 USD.

Component selection based on software support (vs. pure analog performance)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Talk about the importance of robust, long-term software support. Reference `Free
and Open-Source Software—An Analog Devices Perspective
<https://www.analog.com/en/resources/analog-dialogue/articles/free-and-open-source-software.html>`__

Links out to drivers on kernel.org

**Hands-On!** Working through a simple, but complete case study
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's actually build up a working prototype of these devices. We are going to
start with an entirely Linux-based flow, with all software running on the Linux
machine itself. Does this make sense when our product will ultimately be
targeting a low-cost microcontroller running bare-metal C? You bet! Remember,
With ADI DataX, switching between ecosystem layers is cheap - Use Linux to get
up and running quickly, debug circuitry, verify analog performence. Then there
is little to no barrier to switching to bare metal or Zephyr as development
continues.

Hardware Setup
~~~~~~~~~~~~~~~~

ADALM-LSMSPG overview, block diagram. Reference :ref:`ADALM-LSMSPG User Guide
<adalm-lsmspg>`

Booting the system
~~~~~~~~~~~~~~~~~~~~~~~~

Boot the system, run:

.. code-block:: none

   iio_info

You see the Raspberry Pi's cpu_thermal
sensor, undervoltage warning comparator, but nothing else.

Configuring the System (and rebooting!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<<Point out to Kuiper, maybe refernce the ADALM-LSMSPG user guide>>

Follow the instructions for downloading and installing ADI Kuiper
Linux, and editing config.txt. The only difference is the device tree overlay to
be added to config.txt. For this exercise, Prepare an SD card with ADI Kuiper
Linux following the instructions at :ref:`ADI Kuiper Linux Guide <kuiper>`.

Add the following to the end of ``/boot/config.txt``:

.. code-block:: none

   dtoverlay=rpi-adalm-lsmspg

   # Heartbeat blinky:
   dtparam=act_led_gpio=20
   dtparam=act_led_trigger=heartbeat

   # Short GPIO 21 (pin 40) to ground for shutdown:
   dtoverlay=gpio-shutdown,gpio_pin=21,active_low=1,gpiopull=up

The details of the lsmspg overlay will be covered shortly. The heartbeat blinky
section configures the activity LED to pulse a heartbeat pattern, and assigns it
to GPIO 20 on the Raspberry Pi header. GPIO 21 (pin 40) is configured to trigger
a shutdown when shorted to ground.

Command Line Tools (Hello, AD5592r!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open a terminal and run the following command:

.. code-block:: none

   iio_info

again. If all goes well, you should see a few pages of information about the
AD5592r, AD5593r, LM75, and GPIOs.

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADI IIO Oscilloscope is a cross platform GUI application for basic
interaction with IIO contexts such as evaluation boards running on standard
platforms, standalone modules such as the ADALM-Pluto or AD-JUPITER-EBZ
software-defined radio. The application supports plotting of the captured data
in four different modes (time domain, frequency domain, constellation and
cross-correlation). The application also allows to view and modify IIO
Attributes and settings of the evaluation board’s devices.

IIO Oscilloscope is a legacy application that is being slowly deprecated in
favor of Scopy, so we are only going to cover it briefly.

<<screenshot of IIO Oscilloscope, with one of the blinky GPIOs shown.>>

Scopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scopy is a multi-functional software toolset with full instrument support for
the ADALM2000 including oscilloscope, spectrum analyzer function generator,
network analyzer, and tools for digital debug. From Scopy version 2.0, it now
supports general-purpose interaction with IIO contexts, and largely supersedes
IIO Oscilloscope.

Let's interact with the ADALM-LSMSPG board using Scopy...

<<Walk through blinking LEDs, reading / writing voltages, reading
temperatures.>>


Device Trees: Telling Linux what's connected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Examine device tree overlay, include annotated figure from presentation.

Pyadi-iio And examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open up Thonny, and:

run lm75_example.py

run ad5592r_curve_tracer.py

run ad5592r_curve_tracer.py



Next Steps: Developing on a remote host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As wonderful as Thonny is, it's often advantageious (or essential) to develop on
a much more powerful machine. While the temperature sensor requires little to no
math, and the curve tracer requires a tolerable amount of math, high-bandwidth,
RF, and radar applications will push the Raspberry Pi's limits. And if the
application itself doesn't the development environment - VSCode, MATLAB,
PyCharm, etc. will. Luckily the IIO subsystem supports multiple physical
backends, including Serial, USB, and network. Kuiper Linux is configured to run
a program called "iiod" (IIO daemon) on startup. This process serves up local
IIO devices over a network connection that can be accessed from anywhere on the
network. Open up a terminal again and run:

.. code-block:: none

   iio_info -u ip:localhost

... same information as no argument! We've told iio_info to not look at locally
connected devices, rather, for devices on the network. It just so happens that
the network never left the machine, but it certainly could have. Here is a
screenshot of iio_info running on a Windows 11 machine:

<<Screenshot of iio_info -u ip:analog.local>>

So now we can fire up our favorite bloated (oops - "full featured") Python,
MATLAB, C#, etc. development environment, and communicate with the target
hardware over a network connection.

Language Support: C, C++
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of course we're not limited to Python! The libiio is written natively in C, so
we can write a simple C program that runs natively in Linux, on the Raspberry
Pi. In this section, we'll go through this process.

:doc:`Continue to C, C++ Tutorial <native_c_example/index>`

.. toctree::
   :hidden:

   native_c_example/index

Language Support: MATLAB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The LM75, AD5592r, and AD5593r are supported in ADI's MATLAB precision toolbox.
In this section, we'll work through porting the temperature sensor and curve
tracer to MATLAB.

:doc:`Continue to MATLAB Tutorial <matlab_example/index>`

.. toctree::
   :hidden:

   matlab_example/index


IIO as a Tool for Migrating to an Embedded Implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prototyping in Linux is incredibly convenient - even if we didn't have pre-built
device tree overlays for the ADALM-LSMSPG, it's not terribly difficult to create
our own. And once the driver is bound, we can access the hardware via any of the
libiio supported language bindings. If the end application is based on Linux,
then we can just keep on going to the finish line - write top level code that
runs directly on the target, or on a remote host via USB or Ethernet backends.
But is there any value in starting with Linux if the end application will
ultimately be fully embedded? You bet! The IIO supports the serial backend,
and really doesn't care if it's talking to an actual iiod daemon running on
Linux, or - a "fake" daemon running in a bare-metal application. As long as the
transactions are correct, the libiio doesn't care if it's talking to Linux on a
Raspberry Pi, bare-metal C running on an ARM microcontroller, a BASIC
implementation running on a Parallax BASIC stamp, or a Forth implementation
running on an 8051 CPU. This means that while you're testing out proof of
concept code in Python talking to a Raspberry Pi, your hardware team can be
designing the final board with the target processor. The devices can then be
exposed over the iio network backend using the "tinyiiod server". This allows
you to run the same proof of concept Python (or C or MATLAB or C#) code that
previously talked to the Raspberry Pi, to talk to your actual embedded target.

To see this in action:

:doc:`Continue to tinyiiod Tutorial <tinyiiod_example/index>`

.. toctree::
   :hidden:

   tinyiiod_example/index



Porting to a Fully Embedded System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the hardware is validated using the tinyiiod server, the process of
migrating to a fully embedded system can begin. The :external+no-OS:doc:`index`
is Analog Devices' bare metal framework for embedded systems, supporting Maxim
and Analog Devices processors, as well as STM32, Raspberry Pi pico, AMD Xilinx
and Altera soft processors, freeRTOS, ChibOS, and others. The framework is
designed to be easily portable to other platforms as well.

Let's now migrate the curve tracer logic that until now ran in Python on a
remote host into the embedded target, replacing the tinyiiod server entirely.

:doc:`Continue to tinyiiod Tutorial <standalone_no-os_example/index>`

.. toctree::
   :hidden:

   standalone_no-os_example/index

Ecosystem Support: ROS2 Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While the previous exercises used Python and pyadi-iio, the IIO framework can
also be integrated with **ROS2** (Robot Operating System 2) for robotics and
automation applications. The `adi_iio <https://github.com/analogdevicesinc/adi_ros2>`__
ROS2 package provides a bridge between IIO devices and the ROS2 ecosystem,
exposing device attributes as ROS2 topics and services.

In this section, we will run a servo motor control demo that uses the
ADALM-LSMSPG to generate position commands and read feedback, demonstrating
how IIO devices can be integrated into a ROS2-based control system.

:doc:`Continue to ROS2 Integration Tutorial <ros2_integration/index>`

.. toctree::
   :hidden:

   ros2_integration/index

Next Steps: No-OS development on Linux? You bet!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

...but I'm Confused... No-OS means no Operating System, but we're using Kuiper
Linux, and that's an Operating System. What gives?

Unlike the IIO drivers used in the previous tutorial , which **require** the
Linux kernel and operating system to function, No-OS provides a portable
software stack which can run on any platform that supports a C compiler. This
could be bare metal microcontrollers, truly running without an operating system,
up through full systems like our Kuiper Linux running on a Raspberry Pi. The
No-OS repository includes existing support for the Linux OS, Real-Time Operating
Systems Chibios, and mbed, Raspberry Pico, as well as hardware support for
Maxim/ADI, STM32, AMD Xilinx and Altera. But why? Well, bringing up a toolchain
for a particular embedded processor has its own set of challenges - particularly
if development will begin on a standard development platform, then be ported to
a custom board. Running no-OS code on Linux provides a way to get started on the
embedded code development, before actually embedding. A full treatment of this
flow is beyond the scope of this tutorial, but will be documented in a future
tutorial.

.. todo::

   Port the Fred in the Shed curve tracer to no-OS on Linux.

More “Just Enough Software” examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Drawing parallels to other software flows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wrapup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Additional References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This tutorial builds on the concepts covered in the
:ref:`conv_connect_tutorial`.

It also serves as a preview to the :ref:`precision_adc_tutorial` that starts to
deal with analyzing time series data.