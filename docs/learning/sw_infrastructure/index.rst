.. collection:: ADI DataX Tools for Precision Wideband System Design
   :subtitle: Hardware and software tools for mixed-signal development.
   :label: tutorial

   Explore software frameworks and prototyping tools using the ADALM-MMSC.

   system-level:
     - .
     - learning/tools_for_ls/index
     - learning/tools_for_prec_wb/index

ADI DataX Tools for Precision Wideband System Design
===============================================================================

.. note::

   This is a work in progress.

Introduction
~~~~~~~~~~~~

Analog Devices manufactures a dizzying array of products from simple, 2-terminal shunt voltage references to some of the most complicated communication and instrumentation devices in existence. ADCs, DACs, and sensors comprise a large subset of this space, and devices from the slow, jellybean LM75 temperature sensor to the Apollo MXfE share many of the same frameworks, programming interfaces, design and development tools.

This tutorial will use a part “somewhere in the middle” in terms of complexity, the AD4080 40 Msps Oversampling SAR ADC, as a launchpad for learning about the powerful tools available for supporting such a broad range of devices. This part’s versatility is ideal for illustrating several key software and hardware concepts:

- Microcontroller / FPGA decision factors
- Linux / no-OS / Zephyr support
- Language support
- Hardware and Software Enablement,  System Prototyping
- Signal chain architecture

This tutorial will cover each of these in summary, accompanied by hands-on exercises with hardware. We’ll test drive key software utilities, run example programs, take some basic performance measurements, and prototype a simple seismic application example for strategic and key (S&K) customer Fred in the Shed Instruments. Finally, we’ll show how concepts can be applied to other data converter products – PLLs, DDS, IMUs, and more.

The tutorial can be most easily run on a Raspberry Pi 5, but we’ll leave you with instructions on how to install everything on your ADI laptop, your co-worker’s Mac, and your other co-worker’s Linux box. You will walk away knowing how to bring up this portable, economical setup in customer lobbies, labs, and conference rooms. It also serves as a testing ground for elements that can be used in a future mixed-mode signal chain tutorial.

You may recognize some of the material; this tutorial builds upon two previous ones:

`Tools for Low-Speed Mixed Signal System Design <../tools_for_ls/index.html>`_

where we connected an AD5592r to a Raspberry Pi and built a transistor curve tracer, and

`Tools for Precision Wideband Mixed Signal System Design <../tools_for_prec_wb/index.html>`_

where we used an ADALM2000 as part of a colorimeter proof of concept, then demonstrated how easy it was to replace the ADALM2000 with an AD4630-24 ADC.

Slide Deck
~~~~~~~~~~~~~~~~~~~~

This tutorial is also designed to be presented as a live, hands-on workshop; a slide deck is provided here:

.. ADMONITION:: Download

   :download:`Slide Deck: ADI’s Software Infrastructure for designing with ADCs, DACs, and Sensors <adi_software_infrastructure_for_adcs_dacs_sensors.pptx>`

.. A complete video run-through will also be provided, either as a companion to following the tutorial yourself, or to practice before presenting as a hands-on workshop. This video is a placeholder for the time being, but many of the concepts apply directly to this workshop:

.. .. ADMONITION:: ToDo

..    To Do: Re-shoot video after experiment-specific module released.

..    .. video:: https://www.youtube.com/watch?v=UHX1njMQ7V0

Materials
---------

- Raspberry Pi 5 + power supply + SD card
- :ref:`ADALM-MMSC <adalm-mmsc>` board (contains the AD4080 and a pre-programmed MAX32666FTHR microcontroller running the IIO server)
- :ref:`ADALM2000 <m2k>` board (Multi-function USB instrument)
- Two micro-USB cables (one for the ADALM2000, one for the ADALM-MMSC)
- Jumper wires: the ADALM2000's two GND wires and its W1 and W2 wires connect to header P17 on the ADALM-MMSC (supplied with the ADALM2000)

Hardware setup
~~~~~~~~~~~~~~

The ADALM-MMSC is powered and read over its USB connection, so no firmware programming or additional power supply is needed; the board ships with the IIO server firmware already loaded. (Firmware upgrade instructions are in the :ref:`ADALM-MMSC documentation <adalm-mmsc>`.)

The complete setup is shown in :numref:`fig-hw_setup`. Connect the ADALM2000 and the ADALM-MMSC to two of the Raspberry Pi 5's USB ports using the micro-USB cables, and connect a display to the Raspberry Pi's micro-HDMI port. Connect the ADALM2000 to the ADALM-MMSC with the jumper wires as described below, and power up the Raspberry Pi last, using its USB-C 5 V power supply.

.. _fig-hw_setup:

.. figure:: complete_hw_setup.png
   :width: 40 em
   :align: center

   Complete hardware setup: Raspberry Pi 5, ADALM-MMSC and ADALM2000.

The ADALM2000 is the signal source for the ADALM-MMSC. The jumper wire connections between the two, marked in red in :numref:`fig-hw_setup`, are shown in close-up in :numref:`fig-m2k_mmsc`:

- Connect the ADALM2000's two black GND wires to the lower two posts of P17 (pins 3 and 4)
- Connect the solid yellow W1 wire to P17 pin 1
- Connect the striped yellow W2 wire to P17 pin 2
- Set jumper P10 to the lower position (DIR) and P12 to the upper position (DIR). This bypasses the Sallen-Key filter and applies the inputs directly to the fully differential amplifier.

.. _fig-m2k_mmsc:

.. figure:: ../../tools/adalm-mmsc/adalm-mmsc_hardware_setup.png
   :width: 30 em
   :align: center

   Close-up of the ADALM2000 to ADALM-MMSC connections.

.. note::

   None of the exercises need the AD4080 inputs to be probed. If you want to probe them anyway, for debugging or other purposes, connect the ADALM2000's 1+ and 1- scope inputs to the ADALM-MMSC. On boards from the first production build, the usual P7 pins are too short for the ADALM2000 fly wires. Use P29 and P30 instead: P29 is ADC_IN_N and goes to 1-, and P30 is ADC_IN_P and goes to 1+. See the errata in the :ref:`ADALM-MMSC documentation <adalm-mmsc>`.

Software Setup
~~~~~~~~~~~~~~
.. important::

   The setup installs several software packages, it is recommended to use a dedicated SD card for this exercise to avoid conflicts or overwriting anything important.

Write the ADI Kuiper Linux image onto the SD card. Directions and the image download are available at:

`Analog Devices Kuiper Linux <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_

This tutorial is tested with Kuiper Linux 2 (full image). It already includes libiio 0.26 (``iio_info``, ``libiio-dev``, Python bindings), libm2k 0.9.0 (including the Python bindings), pyadi-iio, and Scopy 2.0, so these do not need to be installed separately.

Boot up the Raspberry Pi and connect to the internet. There are two ways to set up the software for this workshop:

- :ref:`Manual setup <sw_setup_manual>`: you run each step yourself, which is the best choice if you want to understand what is installed and why.
- :ref:`Debian package <sw_setup_deb>`: a single package that installs everything.

.. _sw_setup_manual:

Option 1: Manual setup
----------------------

Run everything as your normal user, not as root. Only the commands that need ``sudo`` have it.

Step 1: Install system packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kuiper Linux 2 already ships the ADI libraries (libiio, libm2k, pyadi-iio, numpy, Scopy). The workshop also needs a Python GUI toolkit and a few tools for creating the virtual environment and building genalyzer.

::

   sudo apt-get update
   sudo apt-get install -y python3-venv python3-tk pkg-config

When ``sudo`` asks for a password, enter ``analog``: it is the default password of the ``analog`` user on Kuiper Linux.

- ``apt-get update`` downloads a fresh list of available packages and versions. Without it, apt may fetch outdated versions or report that a package can't be found.
- ``-y`` answers "yes" to the confirmation prompt.

The other packages the workshop needs are already pre-installed on Kuiper Linux 2.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Package
     - Why we need it
   * - ``python3-venv``
     - Creates an isolated Python environment (``.venv``) in Step 3. The workshop's extra libraries go there, so they don't touch the system Python that Kuiper's own tools rely on.
   * - ``python3-tk``
     - Provides tkinter, Python's GUI toolkit. matplotlib uses it for interactive windows, such as plots with sliders. Without it you get static plots or an import error.
   * - ``pkg-config``
     - Helps CMake find installed libraries and their compiler flags.

Step 2: Get the exercises
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This workshop is still in progress. To be sure the exercises work, get them from the `ftc24-ws <https://github.com/cristina-suteu/ftc24-ws>`_ repository instead of the folder described below, and skip the rest of this step:

   ::

      git clone https://github.com/cristina-suteu/ftc24-ws.git ~/Desktop/tools-for-pw

The exercises are not a separate repository. They are the ``examples/adalm-mmsc`` folder on the ``adalm-mmsc`` branch of this pyadi-iio fork:

https://github.com/thorenscientific/pyadi-iio/tree/adalm-mmsc/examples/adalm-mmsc

We only want that one folder, not the whole repository. Git's sparse checkout downloads just the folder we ask for.

Clone the repository without its files:

::

   git clone --depth 1 --branch adalm-mmsc --sparse \
      https://github.com/thorenscientific/pyadi-iio /tmp/pyadi-iio

- ``--branch adalm-mmsc`` selects the branch that contains the exercises. The default branch does not have them.
- ``--depth 1`` downloads only the latest snapshot, not the whole history.
- ``--sparse`` checks out only the files in the top-level folder at first, not the whole tree.
- ``/tmp/pyadi-iio`` is a temporary location. We delete it at the end.

Select the exercise folder:

::

   cd /tmp/pyadi-iio
   git sparse-checkout set examples/adalm-mmsc

This makes git download only the contents of ``examples/adalm-mmsc``.

Copy it into the workshop directory and clean up:

::

   mkdir -p ~/Desktop/tools-for-pw
   cp -r examples/adalm-mmsc/. ~/Desktop/tools-for-pw/
   cd ~/Desktop/tools-for-pw
   rm -rf /tmp/pyadi-iio

- ``~/Desktop/tools-for-pw`` is the workshop directory. The virtual environment and the exercises live there.
- After this, the exercise files are directly in ``~/Desktop/tools-for-pw/``.

The C exercise (Exercise 4) is a single file, ``hello_iio.c``. Create the folder and open a new file in it:

::

   mkdir -p ~/Desktop/tools-for-pw/hello_iio
   nano ~/Desktop/tools-for-pw/hello_iio/hello_iio.c

Paste in the following code, then save and exit (Ctrl+O, Enter, Ctrl+X):

.. code-block:: c

   #include <stdio.h>
   #include <stdlib.h>
   #include <iio.h>

   #define URI "local:"

   int main() {

       struct iio_context *ctx;
       struct iio_device *dev;
       struct iio_channel *chn;
       char value[20];
       double temp_f; 
       double temp_c;

       ctx = iio_create_context_from_uri(URI);
       if(!ctx) {
           printf("No context\n");
           return -1;
       }
       dev = iio_context_find_device(ctx, "cpu_thermal");
       if(!dev) {
           printf("No such device \n");
           return -1;
       }
       chn = iio_device_find_channel(dev, "temp1", false);

       iio_channel_attr_read(chn, "input", value, sizeof(value));

       temp_c = atoi(value)/ 1000.0;
       temp_f = temp_c * 1.8 + 32 ;
       printf("%f Fahrenheit Degrees \n", temp_f);
       printf("%f Celsius Degrees \n", temp_c);

       iio_context_destroy(ctx);

       return 0;

   }

Step 3: Create the Python virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You should already be in the workshop directory. If not:

::

   cd ~/Desktop/tools-for-pw

Create the environment:

::

   python3 -m venv --system-site-packages .venv

- ``python3 -m venv .venv`` creates a private Python environment in the ``.venv`` folder.
- ``--system-site-packages`` lets that environment also see packages installed system-wide. The Kuiper packages (iio, libm2k, adi, numpy) live in the system Python. Without this flag the venv couldn't import them, and we'd have to reinstall them.

Install the extra libraries:

::

   .venv/bin/python3 -m pip install matplotlib obspy

- ``.venv/bin/python3 -m pip`` makes sure the packages go into the venv and not the system Python.
- ``matplotlib`` is used for plotting.
- ``obspy`` is used by the seismograph exercise.

Step 4: Build and install genalyzer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Genalyzer is a C library with Python bindings. It isn't packaged for this image, so we compile version v0.1.7 from source.

Download the source:

::

   git clone --branch v0.1.7 --depth 1 https://github.com/analogdevicesinc/genalyzer /tmp/genalyzer

- ``--branch v0.1.7`` picks the version the workshop was tested with.
- ``--depth 1`` downloads only that snapshot, not the whole history, which is faster.
- ``/tmp/genalyzer`` is a temporary location. We delete it at the end.

Configure the build:

::

   mkdir /tmp/genalyzer/build && cd /tmp/genalyzer/build
   cmake -DCMAKE_BUILD_TYPE=Release ..

- Building in a separate build folder keeps the source tree clean.
- ``cmake`` checks that the compiler and FFTW are available and generates the Makefiles.
- ``-DCMAKE_BUILD_TYPE=Release`` builds the optimized version.

Compile:

::

   make -j$(nproc)

- ``make`` compiles the library.
- ``-j$(nproc)`` uses all CPU cores. On a Pi this takes a few minutes.

Install the library system-wide:

::

   sudo make install
   sudo ldconfig

- ``sudo make install`` copies the compiled library and headers into system folders such as ``/usr/local/lib``, which needs root.
- ``ldconfig`` refreshes the system's list of shared libraries, so programs, including the C exercise, can find the new one.

Install the Python bindings into the venv:

::

   cd ~/Desktop/tools-for-pw
   .venv/bin/python3 -m pip install /tmp/genalyzer/bindings/python

This installs the genalyzer Python module into the venv. It wraps the C library you just installed.

Clean up:

::

   rm -rf /tmp/genalyzer

The source and build files are no longer needed.

Step 5: Install Thonny in the venv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Thonny is the editor for the Python exercises (Exercise 3). We install it inside the virtual environment from Step 3, so that it runs on the venv's Python and can find genalyzer, matplotlib and obspy without any extra configuration.

::

   ~/Desktop/tools-for-pw/.venv/bin/python3 -m pip install thonny

- ``.venv/bin/python3 -m pip`` installs Thonny into the venv, not into the system Python, so no ``sudo`` is needed.
- The venv can still see the system-wide packages (``tkinter``, which Thonny needs, comes from ``python3-tk`` in Step 1).

Thonny now lives at ``~/Desktop/tools-for-pw/.venv/bin/thonny``. So that you can start it by just typing ``thonny``, add an alias to your shell configuration:

::

   echo "alias thonny='$HOME/Desktop/tools-for-pw/.venv/bin/thonny'" >> ~/.bashrc
   source ~/.bashrc

- ``alias thonny=...`` makes the command ``thonny`` run the venv's copy of Thonny.
- ``>> ~/.bashrc`` appends the alias to the file that every new terminal reads, so you only do this once.
- ``source ~/.bashrc`` makes the alias available in the terminal you are using now.

Step 6: Install VS Code
^^^^^^^^^^^^^^^^^^^^^^^

VS Code is the editor for the C exercise (Exercise 4).

Download the ARM64 ``.deb`` package from https://code.visualstudio.com/download in a browser. It is saved in the ``Downloads`` folder. Then install it from there:

::

   cd ~/Downloads
   sudo apt install ./code_*_arm64.deb

- ``cd ~/Downloads`` moves to the folder where the browser saved the package.
- ``./code_*_arm64.deb`` tells apt to install the downloaded file instead of looking for the package in its online list.

.. _sw_setup_deb:

Option 2: Debian package
------------------------

.. todo::

   Describe installing the workshop with a Debian package, once the package is available.

Exercise 1: Command line
~~~~~~~~~~~~~~~~~~~~~~~~

Multiple examples require running Linux commands. For those, open the terminal using ``Ctrl + Alt + T`` key combination.

IIO Info
--------
Communication with the various data converter sources and sinks is done through the Industrial I/O (IIO) framework. This framework is used for communicating with devices that are in some sense an ADC or DAC, and is the backbone of many of the tools we will use in this workshop. An important concept in IIO is the "Context". An IIO context usually refers to a computing device or a device driver that is capable of interfacing with IIO devices. The context is the starting point for all IIO operations, and is used to manage devices, channels, and buffers. The context can be local (on the same device), or remote (on a different device). The IIO context is created by the IIO backend, which is responsible for interfacing with the hardware.

There are three IIO contexts in our setup:
- The Raspberry Pi itself, whose backend is local. It has two IIO devices: an internal temperature sensor and a supply voltage monitor
- The ADALM-MMSC, whose backend is serial (served by its MAX32666FTHR microcontroller). It has one IIO device: the AD4080
- The ADALM2000, whose backend is either USB or network. It has several IIO devices: the XADC housekeeping ADCs on the FPGA, the AD9963 ADC/DAC, and custom peripherals (triggering, waveform generation, DMAs) in the FPGA.

Let's use the ``iio_info`` utility to display information about...

...the ``local:`` context (raspberry pi cpu_thermal):

    ::
        
        iio_info
    
    Expected output: ::

        iio_info version: 0.26 (git tag:a0eca0d2)
        Libiio version: 0.26 (git tag: a0eca0d) backends: local xml ip usb serial
        IIO context created with local backend.
        Backend version: 0.26 (git tag: a0eca0d)
        Backend description string: Linux kuiper-ioan 6.1.54-v7l+ #1 SMP Fri Sep 20 07:21:36 UTC 2024 armv7l
        IIO context has 4 attributes:
                hw_carrier: Raspberry Pi 4 Model B Rev 1.4
                dtoverlay: vc4-kms-v3d
                local,kernel: 6.1.54-v7l+
                uri: local:
        IIO context has 2 devices:
                hwmon0: cpu_thermal
                        1 channels found:
                                temp1:  (input)
                                2 channel-specific attributes found:
                                        attr  0: crit value: 110000
                                        attr  1: input value: 49173
                        No trigger on this device
                hwmon1: rpi_volt
                        1 channels found:
                                in0:  (input)
                                1 channel-specific attributes found:
                                        attr  0: lcrit_alarm value: 0
                        No trigger on this device

...Next, the ``usb:`` context (ADALM2000):

    ::
        
        iio_info -u usb:

    Expected output: ::

        iio_info version: 0.26 (git tag:a0eca0d2)
        Libiio version: 0.26 (git tag: a0eca0d) backends: local xml ip usb serial
        IIO context created with usb backend.
        Backend version: 0.26 (git tag: v0.26)
        Backend description string: Linux (none) 5.15.36-182064-g7aa63204d396 #10 SMP PREEMPT Fri Oct 11 13:17:19 CEST 2024 armv7l
        IIO context has 21 attributes:
                hw_model: Analog Devices M2k Rev.D (Z7010)
                hw_model_variant: 1
                hw_serial: 10447384b904000cebff120015b3dbc2d7
                fw_version: v0.33
        [... snip ...]
        IIO context has 14 devices:
                iio:device0: xadc
                        10 channels found:
                                voltage5: vccoddr (input)
                                3 channel-specific attributes found:
                                        attr  0: label value: vccoddr
                                        attr  1: raw value: 1841
                                        attr  2: scale value: 0.732421875
        [... snip ...]

...the ``serial:/dev/ttyACM0,230400,8n1`` context (ADALM-MMSC):

    ::
        
        iio_info -u serial:/dev/ttyACM0,230400,8n1

The iio_info utility is handy for debugging setups, making sure contexts are available, and checking that devices are recognized. There are other command line utilities for reading and writing individual attributes, reading and writing data to DMA buffers, but they're not very convenient for interactive use.

Exercise 2: Scopy (2.0!)
~~~~~~~~~~~~~~~~~~~~~~~~
Scopy is a GUI application that provides the test instrument interfaces to the ADALM2000, as well as custom instruments for other hardware, such as the `AD-SWIOT1L-SL <https://www.analog.com/AD-SWIOT1L-SL>`__ Software-configurable Analog and Digital I/O with 10BASE-T1L. When  no board-specific control panel is available, a debug interface provides access to all IIO attributes for a given context, generic time and frequency domain plots, and DAC data managers. We will use Scopy to control and capture data from the ADALM-MMSC.

Open a terminal and run:

::

   scopy

Wait for the Scopy window to open; this can take a few seconds. Once opened, it should detect the attached ADALM2000. Click "Connect" as shown in :numref:`fig-open_scopy` and wait for the calibration to complete.

.. _fig-open_scopy:
.. figure:: connect.png
   :width: 50 em
   :align: center

   Connecting to the ADALM2000 in Scopy

Connect to the ADALM-MMSC as shown in :numref:`fig-connect_ad4080`.

.. _fig-connect_ad4080:
.. figure:: ad4080_connect.png
   :width: 50 em
   :align: center

   Connecting to the ADALM-MMSC

Open the Debugger instrument of the ADALM-MMSC, as shown in :numref:`fig-open_debug`.

.. _fig-open_debug:
.. figure:: debug.png
   :width: 50 em
   :align: center

   The ADALM-MMSC Debugger

Explore the context's hierarchy, attributes, and channels. Take a peek at ``filter_type``, ``oversampling_ratio``, ``sampling_frequency``, etc.

Next, open the Signal Generator instrument of the ADALM2000. In the Waveform tab, set up the two channels as follows. The ADALM2000 drives the ADALM-MMSC's differential input with both channels, so enable both:

- **Channel 1:** Sine, amplitude 1 Vpp, offset 0, frequency 500 kHz, phase 0
- **Channel 2:** Rising Ramp Sawtooth, amplitude 1 Vpp, offset 0, frequency 50 kHz, phase 0

Click Run. Then open the ADC - Time instrument of the ADALM-MMSC, set the buffer size to 4096 samples, and click the "Start" button to begin capturing data, as shown in :numref:`fig-open_data`.

.. _fig-open_data:
.. figure:: data_panel.png
   :width: 50 em
   :align: center

   Capturing the signal in ADC - Time

The ADALM-MMSC samples at 40 MSPS, so the 4096 samples span 102.4 µs. In that time you should see about 51 cycles of the 500 kHz sine riding on about 5 periods of the 50 kHz ramp.

**Extra Credit:**

Observe the SINC5+Comp filter's step response. Set the ``filter_type`` attribute to **sinc5+pf1** in the Debugger. In the Signal Generator, set Channel 2 to a Square wave with amplitude 1 Vpp, frequency 1 kHz, 50 % duty cycle and offset 0, and disable Channel 1, so that only the square wave reaches the ADC. Zoom in on a rising edge in ADC - Time. The step response should look like :numref:`fig-sinc5_step`.

.. _fig-sinc5_step:
.. figure:: sinc5.png
   :width: 50 em
   :align: center

   SINC5+Comp Step Response

Exercise 3: Python and the Thonny IDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most examples in this workshop are Python scripts. Thonny is a Python IDE and will allow you to edit and run them easily. In the setup, Thonny was installed in the workshop's Python virtual environment, which has all the required packages. Open a terminal and run:

::

   thonny

Wait for the Thonny window to open. To open each exercise, use *Load* in Thonny's toolbar (or *File > Open...*), browse to the file given in the exercise, and click *Run*.


Simple sine wave from the ADALM2000 to the AD4080
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the "hello world" of the ADALM-MMSC: connect to it, capture some samples, and look at them. Start generating a sine wave using Scopy. In Thonny, load
**Desktop/tools-for-pw-system-design/hello_hw/hello_ad4080.py**
and click Run:

.. image:: hello_ad4080.png

The script connects to the ADALM-MMSC using pyadi-iio, with nothing more than its URI, and reads one buffer of 8192 samples captured at 40 MSPS. It converts the raw ADC codes to volts using the scale reported by the device, then plots the samples in the time domain together with an averaged FFT that keeps updating as new buffers arrive. Change the frequency or amplitude in Scopy and watch the spectrum follow.

This exercise shows how little code it takes to get data out of the ADALM-MMSC. The same attributes you explored in the Scopy debug panel (sampling frequency, scale, buffer size) are available as plain Python properties, and a single ``rx()`` call returns the samples.

.. note::

   The scripts connect to the AD4080 at ``serial:/dev/ttyACM0,230400,8n1`` by default. If the Pi assigned a different serial device number to the ADALM-MMSC, use ``iio_info -s`` to see which contexts are available.

Performance metrics with Genalyzer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the previous exercise the signal came from Scopy, and the result was judged by eye. Here the script generates a known test signal and measures how the ADALM-MMSC reproduces it. Stop the ADALM2000 waveform generator and close Scopy, because this demo will generate
a signal programmatically. In Thonny, load
**~/Desktop/tools-for-pw/m2k_source_ad4080_sink.py**
and Run:

.. image:: m2k_source_ad4080_sink.png

The script uses `Genalyzer <https://github.com/analogdevicesinc/genalyzer>`_ to build a waveform containing a 100 kHz fundamental, its 2nd to 4th harmonics, and four unrelated interfering tones at known levels. It plays the waveform through the ADALM2000, captures 16384 samples with the ADALM-MMSC's digital filter turned off (so the full 40 MSPS bandwidth is visible), and runs a Fourier analysis on the result. The fundamental, harmonics and noise tones are labeled on the FFT, and the amplitudes, SNR and THD are printed in the console.

This exercise shows that the ADALM-MMSC can be used as a measurement instrument, not just a data source: because the input is known, you can compare what you transmitted with what the ADC reports. It also shows one program working with two IIO contexts at the same time, the ADALM2000 over USB and the ADALM-MMSC over its serial connection.

Sinc1 frequency response
~~~~~~~~~~~~~~~~~~~~~~~~

The ADALM-MMSC does not have to deliver all 40 MSPS. Its AD4080 includes a digital filter that decimates the data to a lower rate, and the simplest option is the sinc1 filter. It is cheap and fast, but not a brick-wall filter: signals above the new, lower Nyquist frequency are only attenuated, and what remains folds back (aliases) into the band you are looking at.

In Thonny, load and run
**~/Desktop/tools-for-pw/sinc_folding_interactive.py**:

.. image:: sinc_folding_interactive.png
   :width: 25 em

The ADALM2000 transmits a band of noise, and the ADALM-MMSC captures it with its sinc1 filter set to a decimation (oversampling ratio) of 256 by default. This can be changed with the ``-d`` argument. Drag the slider controlling the frequency of the transmitted noise and interpret the resulting FFT for different frequencies, comparing it with the theoretical sinc1 response, including frequency folding.

This exercise shows that the filter type and output data rate are runtime settings of the ADALM-MMSC (the ``filter_type`` and ``oversampling_ratio`` attributes), and that the measured behavior of the hardware matches the theory. It also shows the trade-off between data rate and aliasing that you will face when choosing a filter for your own application.

ObsPy
~~~~~

A seismic signal is slow, only a few hertz, while the AD4080 samples at 40 MSPS, so the ADALM-MMSC's digital filter does the work of bringing the data rate down to something suitable.

In Thonny, load and run **Desktop/tools-for-pw-system-design/hello_seismograph/seismograph.py**:

.. image:: seismograph.png
   :width: 25 em

The script uses `ObsPy <https://docs.obspy.org/>`_ to read a recorded earthquake and plays 40 seconds of it through the ADALM2000, standing in for a real sensor. So that it fits in a single buffer, the waveform is sped up 100 times. The ADALM-MMSC captures it using the sinc1 filter with an oversampling ratio of 1024, which reduces the 40 MSPS to about 39 kSPS, so that a 16384-sample buffer covers about 419 ms. The script then plots the transmitted waveform and the received one together with its envelope.

This exercise shows that a fast SAR ADC can serve a slow, low-frequency application: the oversampling and filtering happen inside the ADALM-MMSC, with no filter code on the host. It also shows that the same chain (libm2k, pyadi-iio and the Python ecosystem) connects the hardware straight into domain-specific tools, in this case ObsPy.

Exercise 4: Using libiio in C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The libiio has language bindings for C, C#, Python, and MATLAB. This exercise will show how to use libiio in C.

The program reads the Raspberry Pi's CPU temperature through libiio. It is the same sensor you saw as ``cpu_thermal`` in the ``local:`` context in Exercise 1. Every libiio program follows the same four steps, and this one shows each of them:

1. **Create a context** with ``iio_create_context_from_uri``. Here the URI is ``local:``, the Raspberry Pi itself.
2. **Find the device** with ``iio_context_find_device``, by name (``cpu_thermal``).
3. **Find the channel** with ``iio_device_find_channel`` (``temp1``, an input channel).
4. **Read an attribute** of the channel with ``iio_channel_attr_read`` (``input``). The value comes in thousandths of a degree Celsius. The program divides it by 1000, converts it to Fahrenheit, prints both, and releases the context.

These are the same calls you would use for the ADALM-MMSC or the ADALM2000. Only the URI (for example ``serial:/dev/ttyACM0,230400,8n1``) and the device, channel and attribute names change.

To read the source code, open a terminal, go to the exercise folder and open the file in VS Code:

::

    cd ~/Desktop/tools-for-pw
    code hello_iio.c

Run using the command: ::

    gcc hello_iio.c -o hello_iio -liio

Alternatively, you can use the CMake build system: ::

    mkdir build
    cd build
    cmake ..
    make

Both will have compiled an executable called hello_iio, which can be run in the command line: ::

    ./hello_iio

Expected output: ::

    102.979400 Fahrenheit Degrees
    39.433000 Celsius Degrees

Appendix A: IIOD and context forwarding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IIOD (IIO Daemon) is a program that creates libiio network contexts (``ip:...``) that are bound to any kind of context (could be ``local:``, ``usb:``, ``serial:``, etc.), acting like a middleman between the two, forwarding commands and data both ways. It is a great tool in managing connectivity in projects with multiple iio devices, which may potentially be connected to multiple hosts, allowing seamless communication between all of them.

Some **example use cases**:

- Exposing an iio context only visible to a Raspberry Pi's (such as the AD4080 serial context) to other computers on the network
- Connecting to multiple iio contexts through a single internet connection, using different ports for each device (four Phasers example in the slide deck)
- Backend compatibility: some libiio builds (such as the one bundled in MATLAB Toolboxes) don't support the serial backend. IIOD can forward the serial context to a port on the local (or loopback) network, allowing the MATLAB Toolbox to connect to that and access the device

IIOD runs on the computer that has access to the context you want to forward. In the case of this workshop, that is the Raspberry Pi to which the ADALM2000 and AD4080 are connected. To check which backends your build of libiio (which IIOD is part of) supports, run ``iio_info -V``: ::

    iio_info version: 0.26 (git tag:a0eca0d)
    Libiio version: 0.26 (git tag: a0eca0d) backends: local xml ip usb serial

To forward a context, first identify its URI:

- For the ADALM2000, use ``usb:`` or ``ip:192.168.2.1``
- For the AD4080, use ``serial:/dev/ttyACM0,230400,8n1`` (or ACM1, depending on the order in which the Pi assigns serial device numbers)

Then choose a port on which iiod will listen. Kuiper linux already has an instance of iiod running on the default port (30431) forwarding the ``local:`` context. 

Examples:

To forward the ADALM2000 connection to port 50905, run: ::
    
    iiod -u ip:192.168.2.1 -p 50905

To forward the AD4080 connection to port 50907, run: ::
    
    iiod -u serial:/dev/ttyACM0,230400,8n1 -p 50907

.. note::
    Leave them running. Closing these processes (or their terminal window) will stop forwarding the context.

You can now use the context from any libiio application (e.g. the workshop
scripts, Scopy, iio-oscilloscope, iio_info, etc.).

For example, ``iio_info`` can now display the AD4080 context by connecting to the IIOD port (even from another computer on the network), instead of directly to the board: ::
    
    iio_info -u ip:analog.local:50907

.. note::
    In the above command, ``analog`` is the default hostname of a Kuiper Linux system, and ``analog.local`` is the name it is reachable at on the local network. This can be replaced with another hostname or IP address as appropriate, if it was changed.
