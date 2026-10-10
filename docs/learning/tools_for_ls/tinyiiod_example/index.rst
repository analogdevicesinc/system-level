.. _datax-iio-for-migrating:

IIO as a Tool for Migrating to an Embedded Implementation
---------------------------------------------------------

Let's load up the pre-built ADALM-LSMSPG tinyiiod server.
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