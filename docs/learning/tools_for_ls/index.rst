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

In this tutorial, we will use a transistor curve tracer and temperature sensor
as example applications. The temperature sensor simply involves reading
temperature, doing some math to convert units if necessary, and displaying the
result. The curve tracer involves setting voltages and currents, reading
voltages and currents, doing some basic math, and displaying a result. Each
reading will be treated independently, no correlation to previous or future
readings. We will NOT be measuring AC Signal to Noise Ratio (SNR), Total
Harmonic Distortion (THD), nor measuring steps, wiggles, or any other situation
where precise timing is required. Rest assured, there are lots of very
interesting applications in this category; consider a vector network analyzer
(VNA) - set an excitation frequency, measure forward and reflected power and
phase, do some math, step, repeat, and when done, display the results.

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

- Raspberry Pi 4 or 5; 2GB or greater RAM (for Linux examples). (Model 3B, 3B
   Plus will work, but you will want a 4 or 5 :-) )
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

Background
~~~~~~~~~~

This tutorial builds on the concepts covered in the
:ref:`conv_connect_tutorial`.

It also serves as a preview to the :ref:`precision_adc_tutorial` that starts to
deal with analyzing time series data.

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

A wonderful resource for learning Python is `learnpython.org
<https://learnpython.org/>`__, runs right in your browser without needing to
install anything.

And despite the name, `Python for Kids
<https://nostarch.com/python-kids-2nd-edition>`__ is surprisingly good for
adults, too!

What does “Just Enough Software” look like?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Stack Background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introducing an exciting new product that we'll apply our skills
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Component selection based on software support (vs. pure analog performance)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware Setup
~~~~~~~~~~~~~~~~

Booting the system
~~~~~~~~~~~~~~~~~~~~~~~~

Configuring the System (and rebooting!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Raspberry Pi-based hardware and Linux setup mirrors that of the ADXL345 used
in the :ref:`conv_connect_tutorial`, including bringing up the
pyadi-iio example. Follow the instructions for downloading and installing ADI
Kuiper Linux, and editing config.txt. The only difference is the device tree
overlay to be added to config.txt. For this exercise, add the following lines to
config.txt:

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

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Device Trees: Telling Linux what's connected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pyadi-iio And examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Hands-On!** Working through a simple, but complete case study
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next Steps: Developing on a remote host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Next Steps: Other languages (C++, C#, MATLAB, etc.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

To see this in action, let's load up the pre-built ADALM-LSMSPG tinyiiod server.
Go to :git-no-os:`ADALM-LSMSPG firmware (no-OS releases) <releases/latest+>`,
download the adalm-lsmspg.zip file, and unzip to a convenient location. Shut
down your Raspberry Pi properly, then disconnect the 40-pin ribbon cable from the
ADALM-LSMSPG board. Install a MAX32666FTHR in the FTHR sockets, taking care to
align the pins properly. Connect the supplied MAX PICO board to the MAX32666FTHR
programming header. Connect both the MAX PICO and MAX32666FTHR to the host
computer via USB-A to Micro-B cables. Drag and drop the
adalm-lsmspg_maxim_iio.hex file into the DAPLINK DAPLINK mass storage device
(typically ``D:`` or ``E:`` on Windows systems). The DAPLINK drive will
auto-eject, and the heartbeat LED on the ADALM-LSMSPG will begin blinking.
(Almost done!)

Unlike network and USB backends, the iio serial backend is not discoverable so
we will need to find out what serial port the MAX32666FTHR enumerates as.

.. note::
   Back in "ye oldyn days" serial ports were dedicated D-SUB 9 or 25 pin
   connectors on the host computer, assigned to a particular COM or TTY port.
   Those days are mostly gone; "virtual" USB serial ports are incredibly
   convenient as they allow the use of standard serial port software APIs, the
   drawback is the port numbering can be somewhat arbitrary and inconsistent.

There are various ways to find the serial port - Device Manager on Windows, and
looking for tty* ports in /dev on Linux, but we can also use IIO Oscilloscope or
Scopy from the previous experiments.

Once the serial port is located, run the same curve tracer scripts as before,
but append the COM / tty port URI:

.. code-block:: none

   ad5592r_curve_tracer.py -u serial:COMx
   ad5593r_curve_tracer.py -u serial:COMx

where "x" is the COM port number identified. The output should be identical to
previous runs using the local backend, as shown in :numref:`fig-ct_tinyiiod`

.. _fig-ct_tinyiiod:

.. figure:: curvetraceroutput.png
   :width: 700px
   :height: 400px
   :align: center

   Curve tracer plots, serial backend

At this point you can re-verify your top-level code, but on the actual target
hardware (vs. evaluation boards or crude prototypes). While the devices and
curve tracer application on the ADALM-LSMSPG are not terribly sensitive to
noise, more sensitive applications - precision instrumentation, communications,
sensing, etc. - will absolutely benefit from a quick check before beginning the
potentially long embedded firmware development process.

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
While the ultimate goal of the curve tracer is to have a local display, that's
another layer of both hardware and software development that we can defer a bit
longer with a little bit of creative thinking. Since there is a serial port
available, we can test out the logic by printing values to a terminal, formatted
as comma-separated variable (CSV) data for easy copy/paste into `LibreOffice
<https://www.libreoffice.org/>`__ or other spreadsheet for plotting. And for a
bit of `icing on the cake
<https://www.merriam-webster.com/dictionary/icing%20on%20the%20cake>`__ and
nostalgia, we can also make an ASCII-art plot!

Go back to the zip file from the no-OS release, and drag-and-drop the curve
tracer example HEX file into the DAPLINK drive. Press the RESET button on the
ADALM-LSMSPG and observe the output. The CSV data and ASCII-art plots will be
printed to the terminal as shown in the figures below.

.. code-block::
   :caption: ASCII-art NPN curve trace output

   === AD5592R (SPI) - NPN Curve Tracer (Ic vs Vc) ===
   Y-axis: Ic (0 to 7.16 mA)
   X-axis: Vc (0 to 2.45 V)

   +------------------------------------------------------------+
   |         ****** ***** ***** ***** ***** ***** ** *          |
   |        *                                                   |
   |       *                                                    |
   |      *                                                     |
   |                                                            |
   |      * ** ***** ***** ***** ***** ***** ***** ***** *      |
   |     * *                                                    |
   |      *                                                     |
   |     **                                                     |
   |     *                                                      |
   |    *   *** ***** ***** ***** ***** ***** ***** ***** **    |
   |     ***                                                    |
   |    *                                                       |
   |    **                                                      |
   |    **                                                      |
   |    *  ***** ***** ***** ***** ***** ***** ***** ***** ***  |
   |   *  *                                                     |
   |   ***                                                      |
   |****** **** ***** ***** ***** ***** ***** ***** ***** **** *|
   |                                                            |
   +------------------------------------------------------------+
   0.0       0.49       0.98       1.47       1.96       2.45 V

   ===== AD5592R Curve Trace Complete =====


Similarly, you will see an ASCII-art PNP curve trace similar to the figure below.

.. code-block::
   :caption: ASCII-art PNP curve trace output

   === AD5593R (I2C) - PNP Curve Tracer (Ic vs Vc) ===
   Y-axis: |Ic| (0 to 5.62 mA)
   X-axis: Vc (0 to 2.50 V)

   +------------------------------------------------------------+
   | ***** ****** ***** ****** ***** ****** ***** ****** *******|
   |                                                         *  |
   |                                                        **  |
   |                                                       **   |
   |  ** ****** ***** ****** ****** ***** ****** ***** **** *   |
   |                                                        *   |
   |                                                        *   |
   |                                                       *    |
   |                                                      * *   |
   |                                                            |
   |                                        ***** ******* *     |
   |      ***** ****** ****** ***** ****** *               *    |
   |                                                            |
   |                                                       *    |
   |                                                      *     |
   |                                                            |
   |                                                   ***      |
   |                                   * ** ****** ****         |
   |         ** ****** ****** ****** ** *                       |
   |         *                                                  |
   +------------------------------------------------------------+
   0.0       0.50       1.00       1.50       2.00       2.50 V

   ===== AD5593R Curve Trace Complete =====

At this point all of the math, algorithms, and overall operation of the curve
tracer are running in the embedded target, and we're able to verify everything
is operating properly and with full (analog) performance. The next step can be
to connect a local display, or enable a server for display on a remote screen
such as a tablet or mobile device.


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
