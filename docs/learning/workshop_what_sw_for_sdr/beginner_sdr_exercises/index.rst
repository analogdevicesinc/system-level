DataX Novice Exercises
======================

This page contains DataX Novice SDR exercises that demonstrate real-world software-defined radio
applications using ADI's SDR platforms.
These exercises showcase the power of reconfigurable software running on specialized hardware,
allowing you to implement complex signal processing algorithms without custom hardware design.


Requirements
~~~~~~~~~~~~

.. important::

   **Manual setups only:** download the exercise files before starting —
   :download:`beginner_exercises.zip <beginner_exercises.zip>` — and extract the archive to
   your Desktop to follow along.

   With the **workshop package** (the recommended Linux setup) you do **not** need this
   download: the ``setup`` script installs the exercises to your Desktop automatically.

These exercises can be run on a **Raspberry Pi 5** running Kuiper Linux with the workshop
package installed (recommended), or from a **PC** (Linux or Windows).

**Hardware:**

* **ADALM-Pluto SDR** (required for all exercises)
* **Micro USB cable** to connect the Pluto to your PC
  (see `Pluto Quick Start <https://wiki.analog.com/university/tools/pluto/users/quick_start>`__ for details)
* **Jupiter or Talise SDR** (optional, for exercises that use these platforms)
* **SMA loopback cable** (for loopback exercises)
* **Antennas**: 2.4 GHz or 915 MHz antennas for over-the-air exercises (Doppler radar, etc.)
* **Ethernet cable** (for Jupiter SDR connection)
* **Two SD cards** (optional, for Raspberry Pi 5 setup)

**Host setup:**

Prepare the system you will run the exercises from — write and boot a Kuiper SD card, or
install the software stack on a Linux or Windows PC:

.. tab-set::

   .. tab-item:: Linux

      The workshop package works on any Debian-based Linux — Kuiper on a Raspberry Pi, or a
      standard Ubuntu/Debian PC — and pulls in the full SDR software stack for you. This is
      the recommended setup.

      #. **On a Raspberry Pi only:** flash your SD card with the **newest Kuiper Linux
         image** (Debian trixie) built by the official
         `ADI Kuiper repository <https://github.com/analogdevicesinc/adi-kuiper-gen>`__, then
         boot the Raspberry Pi. On an existing Ubuntu/Debian PC, skip straight to the next
         step.

      #. Install the workshop package. It pulls in the SDR software stack (GNU Radio with
         the ``gr-iio`` blocks, ``libiio``, NumPy, Matplotlib, and the Qt GUI) as
         dependencies:

         .. code-block:: bash

            sudo apt update
            sudo apt install datax-workshops-what-sw-for-my-sdr

         .. note::

            If you have a downloaded ``.deb`` rather than an apt source, install it
            with ``apt`` so its dependencies are resolved in one step (the leading
            ``./`` is required so ``apt`` treats it as a file):

            .. code-block:: bash

               sudo apt update
               sudo apt install ./datax-workshops-what-sw-for-my-sdr_*.deb

            Avoid ``dpkg -i`` for this: ``dpkg`` does not install dependencies, so it
            leaves the package unconfigured (and a following ``apt install -f`` may
            remove it instead of completing the install).

      #. Run the packaged ``setup`` script to finish provisioning. Run it as your
         normal user (it uses ``sudo`` internally where needed):

         .. code-block:: bash

            /usr/share/datax-workshops-what-sw-for-my-sdr/setup

         ``setup`` installs PyADI-IIO and copies the exercises to
         ``~/Desktop/datax-workshops/what-sw-for-my-sdr``.

      After this, the DataX Novice exercises are available under
      ``~/Desktop/datax-workshops/what-sw-for-my-sdr/beginner_exercises``.

      .. note::

         **Prefer to set up the stack yourself?** Instead of the package, install the
         dependencies and PyADI-IIO manually:

         .. code-block:: bash

            # Debian/Ubuntu
            sudo apt install python3 python3-pip python3-matplotlib python3-tk gnuradio

            # Install PyADI-IIO (use --break-system-packages on Debian 12+ / Ubuntu 23.04+)
            pip install pyadi-iio

            # Or use a virtual environment (recommended)
            python3 -m venv ~/sdr-venv
            source ~/sdr-venv/bin/activate
            pip install pyadi-iio

         With the manual route, also download the exercise files:
         :download:`beginner_exercises.zip <beginner_exercises.zip>` and extract them to your Desktop.

   .. tab-item:: Windows

      #. Install `Python <https://www.python.org/downloads/>`__ (ensure "Add to PATH" is checked)

      #. Install `libiio <https://github.com/analogdevicesinc/libiio/releases>`__
         (download the latest Windows installer from the releases page).

         .. note::

            These exercises have been tested with libiio v0.26.

      #. Use `Radioconda <https://github.com/ryanvolz/radioconda>`__ to install GNU Radio:

         * Download and install Radioconda from the
           `releases page <https://github.com/ryanvolz/radioconda/releases>`__
         * Open the Radioconda Prompt and install GNU Radio:

           .. code-block:: bash

              conda install gnuradio

      #. Install PyADI-IIO and Matplotlib:

         .. code-block:: bash

            pip install pyadi-iio matplotlib

.. note::

   Connect your SDR hardware (Pluto, Jupiter, or Talise) to your PC before starting
   the exercises.

   The following exercises assume the usage of Thonny Python IDE on the Raspberry Pi, but you can use any
   Python IDE or command-line environment on Linux or Windows with the appropriate software installed.

   Generally, the exercises with both a receiver and transmitter counterpart may be run separately (although
   they might yield some warnings) or together with a friend who has the same setup.

.. note::

   If you installed via the workshop package, the exercises live under
   ``~/Desktop/datax-workshops/what-sw-for-my-sdr/beginner_exercises``. Where the
   steps below refer to the **beginner_exercises** folder, that is the location. If you
   downloaded ``beginner_exercises.zip`` instead, use wherever you extracted it — extracting
   it to your Desktop (as instructed above) puts it at ``~/Desktop/beginner_exercises``.

Setting up your SDR
~~~~~~~~~~~~~~~~~~~

Set up whichever board(s) you plan to use for the exercises — the **ADALM-Pluto**, the
**Jupiter**, or the **Talise**. Each board has to be physically connected to your host and
prepared in software before you run any exercise, so set up only the board(s) you actually
use.

.. figure:: ../images/system_setup.png
   :align: center
   :width: 50em

   Example system setup with the Pluto and Jupiter connected to the host. The Raspberry Pi
   5 shown was used in this version of the workshop, but it is not mandatory — any PC with
   the required software installed works.

Setting up the ADALM-Pluto
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1. Connect the hardware.**

Connect the ADALM-Pluto to your host computer with the **micro USB cable**. Use the port
labeled **USB** (not **PWR**) — this single connection both powers the Pluto and carries
data.

**2. Update the firmware.**

The exercises assume a recent firmware, so update the Pluto to the **newest firmware
release** before anything else, so the exercises run reliably. Follow the official guide:
`PlutoSDR Firmware Updates <https://wiki.analog.com/university/tools/pluto/users/firmware>`__.

**3. Set the USB Ethernet mode for your host OS.**

All exercises reach the Pluto at its default USB-Ethernet address ``192.168.2.1``. The
Pluto exposes this interface over USB, but the USB-Ethernet protocol that actually works
depends on your host operating system. Set the ``usb_ethernet_mode`` that matches the host
you run the exercises from:

.. tab-set::

   .. tab-item:: Linux (Kuiper or Ubuntu)

      On Kuiper the Pluto's default **RNDIS** mode works out of the box. If the Pluto is
      not reachable at ``192.168.2.1``, make sure it is set to RNDIS:

      #. Plug in the Pluto; it mounts as a ``PlutoSDR`` USB mass-storage drive.
      #. Open ``config.txt`` on that drive and, under the ``[SYSTEM]`` section, set:

         .. code-block:: text

            usb_ethernet_mode = rndis

      #. Eject the drive to apply the change (the Pluto reboots).

      **NCM** (CDC-NCM) is also a good option on Linux hosts — if RNDIS gives you
      trouble, set ``usb_ethernet_mode = ncm`` instead. For the full list of modes, see
      `Customizing the Pluto configuration – USB Ethernet Compatibility Mode
      <https://wiki.analog.com/university/tools/pluto/users/customizing#usb_ethernet_compatibility_mode>`__.

   .. tab-item:: Windows

      Windows works with the Pluto's default **RNDIS** mode. If the Pluto is not reachable
      at ``192.168.2.1``, make sure it is set to RNDIS:

      #. Plug in the Pluto; it mounts as a ``PlutoSDR`` USB mass-storage drive.
      #. Open ``config.txt`` on that drive and, under the ``[SYSTEM]`` section, set:

         .. code-block:: text

            usb_ethernet_mode = rndis

      #. Eject the drive to apply the change (the Pluto reboots).

      For the exact procedure, see
      `Customizing the Pluto configuration – USB Ethernet Compatibility Mode
      <https://wiki.analog.com/university/tools/pluto/users/customizing#usb_ethernet_compatibility_mode>`__.

**4. Confirm the connection.**

.. code-block:: bash

   iio_info -s        # the Pluto should be listed
   ping 192.168.2.1

.. _setting-up-jupiter:
.. _booting-jupiter:

Setting up the Jupiter SDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1. Connect the hardware.**

Connect the Jupiter to your host computer with a **micro USB cable** and an **Ethernet
cable**. The exercises reach the Jupiter over the network at ``jupiter.local``.

**2. Prepare the SD card.**

Before booting the Jupiter for the first time, prepare its SD card by building it from the
latest Kuiper release:

#. Flash an SD card with the **newest Kuiper Linux image** (Debian trixie) from the official
   `ADI Kuiper repository <https://github.com/analogdevicesinc/adi-kuiper-gen>`__.

#. Configure the SD card using a **Raspberry Pi** — the Jupiter cannot boot without
   this step, so the commands must be run on a Raspberry Pi first:

   a. Insert the freshly flashed SD card into a Raspberry Pi and boot it.

   b. Run the following configuration commands:

      .. code-block:: bash

         sudo configure-setup.sh jupiter_sdr jupiter_sdr
         sudo hostnamectl set-hostname jupiter

      After the first command, you should see a message similar to:

      .. code-block:: text

         Successfully prepared boot partition for running project jupiter_sdr on jupiter_sdr.

   c. Power off the Raspberry Pi, remove the SD card, and insert it into the Jupiter.

#. Boot the Jupiter with the configured SD card.

**3. Boot and confirm the connection.**

Make sure the back panel **STAT** blue LED is blinking. This indicates the boot stage is
successful. If the LEDs are red, the board is in shut down mode. To start it, press the
push-button once and wait for a blinking pattern.

.. figure:: ../images/jupiter_setup/jupiter_setup_blinking_led.png
   :align: center
   :width: 30em

   Jupiter back panel showing the STAT LED location

Once it is booted, communicate with the Jupiter over SSH:

.. code-block:: bash

   ssh root@jupiter.local
   # Enter "analog" as password when prompted

If you need to reboot the Jupiter (e.g., to close IIO Oscilloscope), you have two methods:

*Method 1: Via SSH*

Open a terminal and run the following commands:

.. code-block:: bash

   ssh root@jupiter.local
   # press Enter and enter "analog" as password
   reboot
   # press Enter

*Method 2: Via Push-Button*

#. Press once the push-button on the back of the Jupiter
#. Wait for the LEDs to turn red
#. Press once more the push-button to boot again
#. Wait for the STAT LED to blink again (blue color)

Setting up the Talise
^^^^^^^^^^^^^^^^^^^^^

The Talise (ADRV9009-ZU11EG) SOM boots from its own SD card and is reached over the network,
like the Jupiter. Preparing it is outside the scope of this workshop — follow the official
documentation:
`ADRV9009-ZU11EG <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adrv9009-zu11eg.html>`__.

Once it is up on the network, connect to it and run the Talise exercises the same way as the
other boards.

.. _sinewave-loopback:

Transmit and receive a complex sinusoid (Sinewave Loopback)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What is the easiest way to validate the basic functionalities of an SDR and analyze performance metrics?
Add a loopback cable between TX and RX channels, transmit a complex sinusoid, and look at the
spectrum on the receive side.

Through this basic test:

* Verify if the up-conversion and down-conversion are accurate
* See how clean the received spectrum is (Image Rejection, LO leakage, Spurs, SNR, SFDR)
* Confirm that the software, HDL, and hardware work properly
* Play with attributes to understand what "knobs" can be tweaked and how
* Validate proper integration of the controls in your application

**What is a Complex Sinusoid?**

A complex sinusoid is a fundamental test signal in SDR systems, consisting of in-phase (I) and
quadrature (Q) components that create a single tone in the frequency domain.
The complex exponential is represented as:

.. math::

   s(t) = A \cdot e^{j2\pi ft} = A \cdot (\cos(2\pi ft) + j\sin(2\pi ft))

where:

* :math:`A` = amplitude
* :math:`f` = frequency
* :math:`t` = time
* **Real part (I)**: :math:`A \cdot \cos(2\pi ft)`
* **Quadrature part (Q)**: :math:`A \cdot \sin(2\pi ft)`

In the constellation diagram, a complex sinusoid appears as a rotating point, tracing a circle
around the origin. Its spectrum shows a single peak at the frequency :math:`f`.

.. figure:: images/intro/complex_sin_plot.png
   :align: center
   :width: 45em

   Real sinusoid vs complex sinusoid in time and frequency domain

.. figure:: images/intro/complex_sin_constellation_plot.png
   :align: center
   :width: 35em

   Complex sinusoid time plot and corresponding constellation plot

**Zero IF Architecture**

Modern SDR platforms like Pluto, Jupiter, and Talise use a **Zero Intermediate Frequency (Zero IF)**
architecture where the signal is directly converted to/from baseband without intermediate frequency stages.

.. figure:: images/intro/complex_sin_constellation_plot2.png
   :align: center
   :width: 45em

   Zero IF architecture block diagram showing transmitter, transmission medium, and receiver

The phase and frequency difference between TX and RX local oscillators affects Phase Modulation
applications, requiring real-time phase and frequency correction algorithms.

**Transmitter Chain:**

#. **Digital Signal Generation**: Create complex I/Q samples in software
#. **DAC (Digital-to-Analog Converter)**: Convert digital samples to analog voltages
#. **Reconstruction Filter**: Remove high-frequency images from the DAC output
#. **I/Q Modulator**: Mix I and Q signals with the Local Oscillator (LO) at 90° phase difference
#. **RF Amplifier**: Amplify the upconverted signal to the desired transmit power
#. **Antenna**: Radiate the RF signal

**Receiver Chain:**

#. **Antenna**: Capture the RF signal
#. **RF Amplifier (LNA)**: Low-noise amplification
#. **I/Q Demodulator**: Mix the RF signal with the LO to downconvert to baseband
#. **Anti-Aliasing Filter**: Remove high-frequency content before sampling
#. **ADC (Analog-to-Digital Converter)**: Sample the analog I/Q signals
#. **Digital Processing**: Process the received samples in software

**Key Impairments to Observe**

When analyzing the received spectrum, several impairments characterize real-world SDR performance:

**1. Image (Mirror Signal):**

Due to I/Q gain and phase imbalances in the mixer, a mirror image of the desired signal appears
on the opposite side of the LO frequency. The **Image Rejection Ratio (IRR)** quantifies how well
the system suppresses this unwanted image:

.. math::

   \text{IRR (dB)} = 10 \log_{10}\left(\frac{P_{\text{wanted}}}{P_{\text{image}}}\right)

Causes of poor image rejection:

* **Gain Imbalance**: I and Q channels have different amplification (should be identical)
* **Phase Imbalance**: I and Q mixer phases deviate from the ideal 90° quadrature relationship

.. figure:: images/intro/image_rejection1.png
   :align: center
   :width: 35em

   Receiver block diagram showing gain and phase impairments that cause image rejection issues

.. figure:: images/intro/image_rejection2.png
   :align: center
   :width: 40em

   Effect of phase and gain imbalance on image rejection ratio

**2. LO Leakage (DC Offset):**

Local Oscillator leakage occurs when the LO signal couples into the mixer output, creating a DC
offset in the baseband I/Q signals. This appears as a spike at the center frequency (DC in baseband).

Causes:

* Imperfect mixer isolation
* DC offsets in the analog signal chain
* LO signal leaking through the RF path

.. figure:: images/intro/lo_leakage.png
   :align: center
   :width: 30em

   Receiver block diagram showing LO leakage and DC offset in the signal chain

**3. Spurs (Spurious Signals):**

Unwanted tones that appear at predictable frequency offsets due to:

* Clock harmonics
* Intermodulation products
* Switching noise from power supplies
* Digital switching transients coupling into analog paths

**4. Signal-to-Noise Ratio (SNR):**

The SNR measures the quality of the received signal relative to the noise floor:

.. math::

   \text{SNR (dB)} = 10 \log_{10}\left(\frac{P_{\text{signal}}}{P_{\text{noise}}}\right)

Higher SNR indicates cleaner signal reception and better ADC/DAC performance.

.. figure:: images/intro/rx_loopback.png
   :align: center
   :width: 45em

   RX spectrum showing SNR measurement between signal peak and noise floor

.. figure:: images/intro/snr_evm.png
   :align: center
   :width: 25em

   Error Vector Magnitude (EVM) measurement showing the difference between measured and ideal signal

The following subsections demonstrate different implementations of this exercise using various tools and platforms.

Using PyADI-IIO (Pluto, Jupiter, Talise)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Pluto**

The Python script performs the following steps:

#. **Configure SDR** - Set up the radio parameters (sample rate, center frequency, gain, etc.)
#. **Create a discrete complex sinusoid** - Generate the I/Q samples mathematically
#. **Call tx() to transmit** - Send the created sinusoid as I and Q data
#. **Call rx() to receive** - Capture the I and Q data from the receiver
#. **Plot the received sinusoid** - Visualize the results

**1. Configure SDR:**

.. code-block:: python
   :linenos:

   import adi
   import numpy as np

   sdr = adi.Pluto("ip:pluto.local")  # Create Radio object

   sample_rate = 3000000  # Sample rate in Hz
   center_freq = 915000000  # Center frequency in Hz
   num_samps = 100000  # Number of samples

   # Configure TX
   sdr.tx_lo = center_freq
   sdr.tx_hardwaregain_chan0 = -10  # TX attenuation in dB
   sdr.tx_cyclic_buffer = True

   # Configure RX
   sdr.rx_lo = center_freq
   sdr.sample_rate = sample_rate
   sdr.rx_rf_bandwidth = sample_rate
   sdr.rx_buffer_size = num_samps
   sdr.gain_control_mode_chan0 = "slow_attack"

**2. Create a discrete complex sinusoid:**

.. code-block:: python
   :linenos:
   :lineno-start: 25

   frequency = 20000  # 20 kHz sinusoid
   fs = int(sdr.sample_rate)
   N = num_samps
   t = np.arange(N) / fs
   samples = 0.5 * np.exp(2.0j * np.pi * frequency * t)

**3. Call tx() to transmit:**

Using PyADI-IIO, only this function needs to be called to start transmitting:

.. code-block:: python
   :linenos:
   :lineno-start: 31

   sdr.tx(samples)

**4. Call rx() to receive:**

Only this function needs to be called to receive:

.. code-block:: python
   :linenos:
   :lineno-start: 33

   rx_samples = sdr.rx()

.. note::

   If you run the example multiple times, the RX capture will have a different phase shift
   compared with TX each time. Even if the LO is the same, there are frequency dividers on
   each channel with random phase shift for each run.

Follow the next steps:

#. Make the loopback setup using Pluto with TX connected to RX via an SMA cable and connect it to your PC.

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 20em

      Pluto SDR with loopback cable connecting TX to RX

#. Open the **beginner_exercises** folder
   (``~/Desktop/datax-workshops/what-sw-for-my-sdr/beginner_exercises``).

#. Go to **1. Sinewave loopback → Python** subfolder.

#. Right click on **python_loopback_sine_pluto.py → Open with Other Application** and
   select **Thonny Python IDE** (or any other Python IDE you have installed) from the
   Recommended Applications list.

   .. figure:: images/exercises/pluto_exercises/sinewave_loopback/python_ide.png
      :alt: Open Python Script with IDE
      :align: center
      :width: 40em

      Open the Python script with Thonny Python IDE

#. To run the script, press the green round button from the top left corner in Thonny IDE as shown below.

   .. figure:: images/exercises/pluto_exercises/sinewave_loopback/run_script.png
      :alt: Run Python Script
      :align: center
      :width: 40em

      Run the Python script in Thonny IDE

#. After running the script, the TX and RX plots appear:

   .. figure:: images/exercises/pluto_exercises/sinewave_loopback/sinewave_loopback_plot.png
      :alt: Sinewave Loopback Plot
      :align: center
      :width: 40em

      TX and RX time domain, FFT, and constellation plots for Pluto sinewave loopback

#. To zoom on a plot, you can use the zoom option as depicted below. Encircle holding left click the area you want to zoom.
   On this example, if you zoom at the figure below on the received signal, you should see a harmonic at 20KHz.

   .. figure:: images/exercises/pluto_exercises/sinewave_loopback/zoom_plot.png
      :alt: Zoom on Plot
      :align: center
      :width: 40em

      Zoom on the plot to see the harmonic at 20KHz

#. To stop running the Python script (if you want to run it again or run another script),
   press **Stop** — the app stops and the plot closes automatically. Thonny stays open, so
   close it too if you are done; or press **Quit** to close both the plot windows and Thonny
   at once.

   .. figure:: images/exercises/pluto_exercises/sinewave_loopback/close_tabs.png
      :alt: Stopping the script
      :align: center
      :width: 40em

      Press Stop to end the script (the plot closes automatically), or Quit to close everything


**Jupiter**

Only the "Configure SDR" section changes compared to Pluto.

Follow these steps:

#. Make the loopback setup using Jupiter with TX1A connected to RX1A via an SMA cable.

   .. figure:: ../images/hw_setup/jupiter_loopback_setup.png
      :align: center
      :width: 30em

      Jupiter SDR with loopback cable connecting TX1A to RX1A

#. Go to **beginner_exercises → 1. Sinewave loopback → Python** and open **python_loopback_sine_jupiter.py**
   using **Thonny Python IDE**.

#. Observe the "Configure SDR" section for Jupiter using ``adi.adrv9002``:

   .. code-block:: python
      :linenos:
      :lineno-start: 1
      :class: code-spaced

      import adi
      import numpy as np

      # Configure SDR
      sdr = adi.adrv9002(uri="ip:jupiter.local")  # Create Radio

      frequency = 15360  # 15.360 KHz sinusoid to be transmitted
      center_freq = 915000000  # Hz
      sample_rate = sdr.rx0_sample_rate
      num_samps = int((sample_rate)/frequency)

      sdr.rx_ensm_mode_chan0 = "rf_enabled"
      sdr.tx_hardwaregain_chan0 = -5
      sdr.rx_hardwaregain_chan0 = 0
      sdr.tx_ensm_mode_chan0 = "rf_enabled"
      sdr.tx_cyclic_buffer = True
      sdr.tx_buffer_size = num_samps
      sdr.rx_buffer_size = num_samps
      sdr.tx0_lo = center_freq
      sdr.rx0_lo = center_freq

#. Run the script by pressing the green button in Thonny.

#. Observe the output plots showing transmitted and received sinusoid.

   .. figure:: images/exercises/jupiter_exercises/sinewave_loopback/sinewave_loopback_python_plot.png
      :align: center
      :width: 40em

      TX and RX time domain, FFT, and constellation plots for Jupiter sinewave loopback

#. Close all plot windows to stop.

#. In this example, a sinusoid at 15.360 KHz is transmitted and received (chosen to have an integer
   number of periods at the sample rate of 15.36 Msps).


**Talise**

.. note::

   The Talise (ADRV9009-ZU11EG) exercise uses the **same PyADI-IIO script** as the Pluto and
   Jupiter versions — you only need to change a few lines (the radio object and its IP
   address). Start from the Pluto or Jupiter script and edit the "Configure SDR" section as
   shown below.

Follow these steps:

#. Go to **beginner_exercises → 1. Sinewave loopback → Python** and open **python_loopback_sine_talise_zu11eg.py**
   using **Thonny Python IDE**.

#. Make the following hardware setup with TX1A_P/N connected to RX1A_P/N via loopback cables.

#. Observe the "Configure SDR" section for Talise:

   .. code-block:: python
      :linenos:
      :lineno-start: 4
      :class: code-spaced

      # Configure properties
      sample_rate = 30720000  # Sample rate
      center_freq = 2000000000  # Center frequency
      num_samps = 100000  # Number of samples per call to rx()
      frequency = 3000000  # Frequency of complex sinusoid
      fc0 = int(center_freq / (sample_rate / 2) * 2**15)  # Digital frequency for TX1

      # Create radio object
      sdr = adi.adrv9009_zu11eg("ip:10.48.65.182")  # IP address of Talise

      # Configure Tx properties
      sdr.tx_hardwaregain_chan0 = -10  # TX attenuation in dB
      sdr.tx_enabled_channels = [0]
      sdr.dds_single_tone(fc0, 0.8, 0)  # Generate tone: freq, scale, channel

      # Configure Rx properties
      sdr.gain_control_mode_chan0 = "slow_attack"
      sdr.rx_enabled_channels = [0]
      sdr.rx_buffer_size = num_samps

#. Run the script by pressing the green button in Thonny. Close all plot windows to stop.

#. Observe the output plots showing transmitted and received signals.


**Scopy**

For Scopy usage with Pluto, see the
`Pluto Quick Start Guide <https://analogdevicesinc.github.io/adi-documentation/tools/pluto/users/quick_start.html>`_.

Using GNU Radio (Pluto, Jupiter)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Pluto**

This exercise implements the sinewave loopback using GNU Radio Companion with interactive sliders
for real-time parameter adjustment.

Follow these steps:

#. Make the loopback setup using Pluto with TX connected to RX via an SMA cable and connect it to your PC.

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 20em

      Pluto SDR with loopback cable connecting TX to RX

#. Open the terminal by pressing **Ctrl + Alt + T** and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **sinewave_loopback_pluto.grc** from
   **beginner_exercises → 1. Sinewave loopback → GNU Radio**.

   .. figure:: images/exercises/pluto_exercises/sinewave_loopback/gnuradio_sinewave_loopback.png
      :align: center
      :width: 45em

      GNU Radio flowgraph for sinewave loopback with Pluto TX and RX blocks

#. To run the flowgraph, click the **Execute** button (green arrow) from the top toolbar.

   .. figure:: images/exercises/pluto_exercises/doppler_radar/run_grc.png
      :align: center
      :width: 45em

      Click the green arrow (Execute) button to run the flowgraph

#. Observe the output plots showing transmitted/received samples, spectrum, and constellation diagram.
   Use the sliders to adjust parameters in real-time:

   * **Frequency slider**: Changes the offset frequency of the transmitted sinusoid
   * **RX Gain slider**: Controls receiver gain
   * **TX Attenuation slider**: Controls transmit power

   .. figure:: images/exercises/pluto_exercises/sinewave_loopback/gnuradio_sinewave_loopback_result.png
      :align: center
      :width: 45em

      Output plots showing transmitted/received samples, spectrum, and constellation with
      interactive sliders for frequency, TX attenuation, and RX gain

#. Click the **Stop** button (red square) or close the window when finished.


**Jupiter**

This exercise implements the same complex sinusoid loopback using GNU Radio Companion's visual flowgraph environment instead of Python code.

Follow these steps:

#. Make the following hardware setup using Jupiter SDR with TX1A connected to RX1A via loopback cable.

   .. figure:: ../images/hw_setup/jupiter_loopback_setup.png
      :alt: Jupiter SDR Hardware Setup
      :align: center
      :width: 40em

      Jupiter SDR setup with TX1A connected to RX1A via loopback cable

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd ~/Desktop/datax-workshops/what-sw-for-my-sdr
      $ gnuradio-companion

#. In GNU Radio Companion, open **beginner_exercises → 1. Sinewave loopback → GNU Radio → sinewave_loopback_jupiter.grc**.

#. Observe the flowgraph structure showing the transmitter and receiver chains:

   .. figure:: images/exercises/jupiter_exercises/sinewave_loopback/sinewave_loopback_gnuradio_schematic.png
      :alt: GNU Radio Flowgraph for Jupiter Sinewave Loopback
      :align: center
      :width: 45em

      GNU Radio flowgraph for sinewave loopback with Jupiter TX and RX blocks

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the output plots showing transmitted/received samples, spectrum, and constellation diagram.

   .. figure:: images/exercises/jupiter_exercises/sinewave_loopback/sinewave_loopback_gnuradio_plot.png
      :alt: GNU Radio Output Plots
      :align: center
      :width: 45em

      Output plots showing transmitted/received samples, spectrum, and constellation diagram

#. Use the sliders to adjust parameters in real-time:

   * **Frequency slider**: Changes the offset frequency of the complex sinusoid
   * **TX Attenuation slider**: Controls transmit power
   * **RX Gain slider**: Controls receiver gain

#. Click the **Stop** button (red square) when finished.


**Jupiter (Double Loopback)**

This exercise demonstrates a double loopback configuration using both TX/RX channel pairs on Jupiter.

Follow these steps:

#. Make the following double loopback hardware setup using Jupiter SDR with TX1A connected to RX1A
   and TX2A connected to RX2A via loopback cables.

   .. figure:: ../images/hw_setup/jupiter_double_loopback_setup.png
      :alt: Jupiter SDR Double Loopback Setup
      :align: center
      :width: 40em

      Jupiter SDR setup with double loopback: TX1A→RX1A and TX2A→RX2A

#. Go to **beginner_exercises → 1. Sinewave loopback → Python** and open **python_loopback_sine_jupiter.py**
   using **Thonny Python IDE**.

#. Observe that the script uses ``adi.adrv9002`` for Jupiter:

   .. code-block:: python
      :linenos:
      :lineno-start: 1
      :class: code-spaced

      import adi
      import numpy as np

      # Configure SDR
      sdr = adi.adrv9002(uri="ip:jupiter.local")  # Create Radio

      frequency = 15360  # 15.360 KHz sinusoid to be transmitted
      amplitude = 0.5
      center_freq = 915000000  # Hz
      sample_rate = sdr.rx0_sample_rate
      num_samps = int((sample_rate)/frequency)

      sdr.rx_ensm_mode_chan0 = "rf_enabled"
      sdr.rx_ensm_mode_chan1 = "rf_enabled"
      sdr.tx_hardwaregain_chan0 = -5
      sdr.tx_hardwaregain_chan1 = -5
      sdr.rx_hardwaregain_chan0 = 0
      sdr.rx_hardwaregain_chan1 = 0
      sdr.tx_ensm_mode_chan0 = "rf_enabled"
      sdr.tx_ensm_mode_chan1 = "rf_enabled"
      sdr.tx_cyclic_buffer = True
      sdr.tx_buffer_size = num_samps
      sdr.rx_buffer_size = num_samps
      sdr.tx0_lo = center_freq
      sdr.tx1_lo = center_freq
      sdr.rx0_lo = center_freq
      sdr.rx1_lo = center_freq

#. Run the script by pressing the green button in Thonny.

#. Observe the output plots showing transmitted and received signals on both channels:

   .. figure:: images/exercises/jupiter_exercises/sinewave_loopback/sinewave_loopback_python_plot.png
      :alt: Python Sinewave Loopback Output
      :align: center
      :width: 45em

      Output plots showing transmitted and received sinusoid on both RX channels

#. Close all plot windows to stop.


Binary Phase Shift Keying (BPSK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Binary Phase Shift Keying is the simplest type of Phase Modulation where the binary data (bits 0 and 1)
are encoded using two distinct phase states of the carrier.

**Encoding:** bits → symbols × carrier_sinusoid

* bit 0 → symbol -1+0j
* bit 1 → symbol +1+0j

For BPSK, Q = 0 (all energy in the In-phase component).

.. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_modulation_concept.png
   :align: center
   :width: 40em

   BPSK modulation concept showing input bits, symbols, and modulated output

.. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_constellation.png
   :align: center
   :width: 40em

   BPSK constellation with two points at -1 and +1 on the real axis

**Where is Phase Modulation used?**

* GSM
* Satellite Television
* Wi-Fi
* Many others

**Ideal World vs Real World**

In an **ideal world** where the LOs of TX and RX are perfectly in sync and where there is no time
delay between RX and TX: **in = out**

.. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_loopback_ideal_world.png
   :align: center
   :width: 40em

   Ideal world: transmitted and received symbols are identical

In a **real world**: **in != out** but the information is still there.

.. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_loopback_real_world.png
   :align: center
   :width: 40em

   Real world: received symbols have phase and frequency offset

**What are the problems when demodulating PSK signals?**

* Phase offset of LO at RX relative to TX
* Frequency offset of LO at RX relative to TX
* Variation of these two in time with distance change and temperature change

Luckily, all these can be solved by software!

**Differential Encoding and Decoding**

Differential encoding solves the phase ambiguity problem:

* To transmit a bit of **"1"**: change state (if previous is "0", change to "1"; if previous is "1", change to "0")
* To transmit a bit of **"0"**: repeat state (if previous is "1", repeat "1"; if previous is "0", repeat "0")

**How the Python Script is Structured**

.. figure:: images/exercises/pluto_exercises/bpsk_loopback/tx_rx_flow_diagram.png
   :align: center
   :width: 45em

   BPSK transmitter and receiver signal processing chain

**Transmitter:**

#. Configure SDR
#. Create array of bits
#. Differential Encoding
#. Interpolate with 16 sps and Remap symbols: bit 0 → -1, bit 1 → 1
#. Shift Spectrum
#. Call tx() function and transmit

**Receiver:**

#. Call rx() function to receive data
#. Adjust the frequency offset (coarse)
#. Select the right samples and decimate (Symbol Sync)
#. Fine frequency and phase adjustment (Costas Loop)
#. Differential Decoding
#. Plot data

**Coarse Frequency Offset Adjustment**

How to adjust the frequency offset:

#. First square the received signal → all symbols (s(t))² will have a constant positive value
#. Take the FFT and measure the peak → the measured peak will be at 2×offset_frequency
#. Apply frequency correction on received samples based on the above measurement

.. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_loopback_init_measurement.png
   :align: center
   :width: 40em

   Initial frequency offset measurement using squared signal FFT

**Symbol Timing Recovery (Mueller and Muller)**

How to select the right samples (Mueller and Muller timing recovery technique):

The variable "mu" represents the timing offset to add to 16sps because we have to select one from
each 16 samples. For example, if mu = 2.43 → we have to shift the input by 2.43 samples.
After a few iterations of the while loop, "mu" stabilizes and only the correct samples are pulled.

We want to sample where the adjacent symbols cross 0 and discard in-between samples.

.. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_loopback_sampling.png
   :align: center
   :width: 40em

   Symbol timing recovery: selecting optimal sample points

**Fine Frequency Synchronization (Costas Loop)**

The Costas Loop functions like a PLL. We multiply the real part of the sample (I) by the imaginary
part (Q), and because Q should be equal to zero for BPSK, the error function is minimized when
there is no phase or frequency offset that causes energy to shift from I to Q.

Q is the error signal - adjust and keep Q = 0.

.. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_constellation_progression.png
   :align: center
   :width: 45em

   Constellation progression: raw → coarse freq → timing recovery → Costas loop

Using PyADI-IIO (Pluto, Jupiter, Talise)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Pluto**

The Python script performs the following steps:

**Transmitter - Create bits and encode:**

.. code-block:: python
   :linenos:

   # Create the array of bits and encode them with Differential Encoding
   num_symbols = 1000
   bits = np.random.randint(0, 2, num_symbols)

   # Differential encoding
   encoded_bits = np.zeros(num_symbols, dtype=int)
   encoded_bits[0] = bits[0]
   for i in range(1, num_symbols):
       encoded_bits[i] = encoded_bits[i-1] ^ bits[i]

**Transmitter - Interpolate and shift spectrum:**

.. code-block:: python
   :linenos:
   :lineno-start: 12

   # Repeat each bit 16 times (interpolate) => 16sps
   sps = 16
   samples = np.repeat(encoded_bits * 2 - 1, sps).astype(np.complex64)

   # For BPSK the data is complex (Q = 0)
   # Shift spectrum to a higher frequency
   f_offset = 100000  # 100 kHz offset
   t = np.arange(len(samples)) / sample_rate
   samples = samples * np.exp(2.0j * np.pi * f_offset * t)

   # Transmit
   sdr.tx(samples)

**Receiver - Coarse frequency adjustment:**

.. code-block:: python
   :linenos:
   :lineno-start: 25

   # Receive samples
   rx_samples = sdr.rx()

   # Square the signal to find frequency offset
   squared = rx_samples ** 2
   fft_squared = np.fft.fftshift(np.fft.fft(squared))
   freqs = np.fft.fftshift(np.fft.fftfreq(len(squared), 1/sample_rate))
   max_freq = freqs[np.argmax(np.abs(fft_squared))]
   offset_freq = max_freq / 2  # Divide by 2 because we squared

   # Apply frequency correction
   t = np.arange(len(rx_samples)) / sample_rate
   rx_corrected = rx_samples * np.exp(-2.0j * np.pi * offset_freq * t)

Follow these steps to run the BPSK transmission and reception experiment:

#. Make the loopback setup using Pluto with TX connected to RX via an SMA cable and connect it to your PC.

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 20em

      Pluto SDR with loopback cable connecting TX to RX

#. Go to **beginner_exercises → 2. Binary Phase Shift Keying (BPSK) → Python** and open **bpsk_loopback_pluto.py**
   using **Thonny Python IDE**.

#. Run the script by pressing the green button in Thonny. Close all plot windows to stop.

#. Twelve plots appear showing the BPSK signal processing stages:

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_bits_transmitted.png
      :alt: BPSK Bits Transmitted
      :align: center
      :width: 40em

      Bits transmitted - original binary data.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_samples_transmitted.png
      :alt: BPSK Samples Transmitted
      :align: center
      :width: 40em

      Samples transmitted - 16 samples per symbol.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_tx_constellation_plot.png
      :alt: BPSK TX Constellation
      :align: center
      :width: 40em

      TX constellation - two points at -1 and +1.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_samples_received_raw.png
      :alt: BPSK Samples Received Raw
      :align: center
      :width: 40em

      Samples received raw - before any correction.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_rx_constellation_plot.png
      :alt: BPSK RX Constellation Raw
      :align: center
      :width: 40em

      RX constellation raw - scattered due to frequency and phase offset.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_coarse_freq_adj_samples.png
      :alt: BPSK Coarse Frequency Adjustment
      :align: center
      :width: 40em

      Samples after coarse frequency adjustment.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_rx_coarse_freq_constellation_plot.png
      :alt: BPSK RX Constellation After Coarse Freq
      :align: center
      :width: 40em

      RX constellation after coarse frequency correction - phase offset remains.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bspk_right_sample_selection.png
      :alt: BPSK Right Sample Selection
      :align: center
      :width: 40em

      Samples after timing recovery - selecting 1 of each 16 samples.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_rx_right_sample_constellation_plot.png
      :alt: BPSK RX Constellation Right Samples
      :align: center
      :width: 40em

      RX constellation after timing recovery - mid-constellation points eliminated.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_costas_loop_freq_vs_time.png
      :alt: BPSK Costas Loop Frequency vs Time
      :align: center
      :width: 40em

      Costas loop frequency error vs time - loop locking onto correct frequency.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bpsk_costas_loop_sample.png
      :alt: BPSK Costas Loop Samples
      :align: center
      :width: 40em

      Samples after Costas loop - fine frequency and phase correction applied.

   .. figure:: images/exercises/pluto_exercises/bpsk_loopback/bspk_rx_costas_loop_constellation_plot.png
      :alt: BPSK RX Constellation After Costas Loop
      :align: center
      :width: 40em

      RX constellation after Costas loop - clean clusters at -1 and +1.


**Jupiter**

This exercise demonstrates BPSK modulation and demodulation using Jupiter SDR with Python.

Follow these steps:

#. Make the hardware setup using Jupiter SDR with TX1A connected to RX1A via loopback cable.

   .. figure:: ../images/hw_setup/jupiter_psk_setup.png
      :alt: Jupiter SDR PSK Setup
      :align: center
      :width: 40em

      Jupiter SDR setup with TX1A connected to RX1A via loopback cable

#. From **beginner_exercises → 2. Binary Phase Shift Keying (BPSK) → Python** subfolder, open **bpsk_loopback_jupiter.py**
   using **Thonny Python IDE**.

#. Observe in the script that the configuration uses ``adi.adrv9002`` for Jupiter:

   .. code-block:: python
      :linenos:
      :lineno-start: 1
      :class: code-spaced

      import adi
      import numpy as np

      # Configure properties
      sdr = adi.adrv9002(uri="ip:jupiter.local")  # Create Radio

      center_freq = 915000000  # Hz
      sample_rate = 30720000  # TX sample rate

      sdr.rx_ensm_mode_chan0 = "rf_enabled"
      sdr.tx_hardwaregain_chan0 = -20
      sdr.rx_hardwaregain_chan0 = 0
      sdr.tx_ensm_mode_chan0 = "rf_enabled"
      sdr.tx_cyclic_buffer = True
      sdr.tx_buffer_size = 1024
      sdr.rx_buffer_size = 32768
      sdr.tx0_lo = center_freq
      sdr.rx0_lo = center_freq

      fs = int(sdr.rx0_sample_rate)

#. Run the script by pressing the green button in Thonny.

#. Observe the output plots showing the BPSK signal processing stages.

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/transmitted_data_encoded.png
      :alt: BPSK Transmitted Data Encoded
      :align: center
      :width: 40em

      Differentially encoded bits ready for transmission

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/tx_samples_wo_freq_shift.png
      :alt: BPSK TX Samples Without Frequency Shift
      :align: center
      :width: 40em

      TX samples before frequency shift - symbols at -1 and +1

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/tx_samples_with_freq_shift.png
      :alt: BPSK TX Samples With Frequency Shift
      :align: center
      :width: 40em

      TX samples after frequency shift - complex sinusoid modulation

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/rx_samples_wo_freq_shift.png
      :alt: BPSK RX Samples Without Frequency Adjustment
      :align: center
      :width: 40em

      RX samples before any correction

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/rx_constellation_with_freq_shift.png
      :alt: BPSK RX Constellation With Frequency Offset
      :align: center
      :width: 40em

      RX constellation showing frequency and phase offset

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/rx_samples_with_freq_adj.png
      :alt: BPSK RX Samples With Frequency Adjustment
      :align: center
      :width: 40em

      RX samples after coarse frequency correction

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/rx_constellation_with_symbol_sync.png
      :alt: BPSK RX Constellation With Symbol Sync
      :align: center
      :width: 40em

      RX constellation after timing recovery - selecting optimal sample points

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/rx_samples_with_costas_loop.png
      :alt: BPSK RX Samples With Costas Loop
      :align: center
      :width: 40em

      RX samples after Costas loop - fine frequency and phase correction

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/rx_constellation_with_costas_loop.png
      :alt: BPSK RX Constellation After Costas Loop
      :align: center
      :width: 40em

      RX constellation after Costas loop - clean clusters at -1 and +1

   .. figure:: images/exercises/jupiter_exercises/bpsk_loopback/rx_tx_samples_decoded.png
      :alt: BPSK TX RX Decoded Samples
      :align: center
      :width: 40em

      Comparison of transmitted and received decoded bits

#. Close all plot windows to stop.


**Talise**

Follow these steps:

#. From **beginner_exercises → 2. Binary Phase Shift Keying (BPSK) → Python** subfolder, open **bpsk_pluto_loopback_talise_zu11eg.py**
   using **Thonny Python IDE**.

#. Observe the "Configure SDR" section for Talise:

   .. code-block:: python
      :linenos:
      :lineno-start: 1
      :class: code-spaced

      # Configure properties
      sdr = adi.adrv9009_zu11eg("ip:10.48.65.182")  # Create Radio
      sdr.rx_enabled_channels = [0]
      sdr.tx_enabled_channels = [0]
      sdr.tx_cyclic_buffer = True
      sdr.tx_cyclic_buffer = True
      sdr.gain_control_mode_chan0 = "slow_attack"
      sdr.gain_control_mode_chan1 = "slow_attack"
      sdr.tx_hardwaregain_chan0 = -20
      sdr.tx_hardwaregain_chan1 = -20
      sdr.tx_hardwaregain_chan1_chip_b = -80
      sdr.tx_hardwaregain_chan1_chip_b = -80
      sdr.gain_control_mode_chan0 = "slow_attack"
      sdr.gain_control_mode_chan1 = "slow_attack"
      sdr.gain_control_mode_chan0_chip_b = "slow_attack"
      sdr.gain_control_mode_chan1_chip_b = "slow_attack"
      sdr.rx_buffer_size = 32768
      sdr.tx_buffer_size = 1024

      fs = int(sdr.rx_sample_rate)

#. Insert the IP address on line 2 to remotely connect to Talise:

   .. code-block:: python
      :linenos:
      :lineno-start: 2
      :class: code-spaced

      sdr = adi.adrv9009_zu11eg("ip:10.48.65.182")  # Create Radio object for Talise

#. Run the script by pressing the green button in Thonny. Close all plot windows to stop.


Raw Loopback in GNU Radio - No Additional DSP (Pluto, Jupiter)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This GNU Radio exercise is the BPSK equivalent of the QPSK raw loopback: it intentionally
omits matched filter, frequency correction, and timing recovery to show what happens without
them. Compare the result with the fully processed BPSK Python loopback above to see why each
DSP stage matters.

**Transmitter:**

* Generate a sequence of bits
* Map bits onto BPSK symbols (-1, +1)
* Offset the spectrum to the right to avoid DC leakage

**Receiver:**

* Shift the spectrum back to DC
* Display time, frequency, and constellation plots — with no additional processing

**Pluto**

Follow these steps:

#. Make the loopback setup using Pluto with TX connected to RX via an SMA cable and connect it to your PC.

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 20em

      Pluto SDR with loopback cable connecting TX to RX

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **BPSK_raw_loopback_pluto.grc** from
   **beginner_exercises → 2. Binary Phase Shift Keying (BPSK) → GNU Radio**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the output displays:

   **Observations:**

   * No frequency offset because the example works on loopback and the LO is the same for RX and TX
   * But has a phase offset between the two paths
   * The constellation shows two clusters that may be rotated away from the real axis
   * Try tweaking the frequency offset slider between TX and RX and see how the data looks — this
     happens when transmitting and receiving between two different devices
   * The spectrum is inefficiently used (spectrum of square wave, no pulse shaping)

#. Click the **Stop** button (red square) when finished.

**Jupiter**

Follow these steps:

#. Make the loopback setup with Jupiter — connect TX to RX and connect the board via Ethernet.

   .. figure:: ../images/hw_setup/jupiter_loopback_setup.png
      :align: center
      :width: 20em

      Jupiter SDR with loopback cable connecting TX to RX

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **BPSK_raw_loopback_jupiter.grc** from
   **beginner_exercises → 2. Binary Phase Shift Keying (BPSK) → GNU Radio**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the same effects as the Pluto version. The frequency offset slider
   demonstrates what happens when TX and RX oscillators are not perfectly synchronized.

#. Click the **Stop** button (red square) when finished.


Quadrature Phase Shift Keying (QPSK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QPSK is similar to BPSK but has more symbols. It encodes 2 bits per symbol using four
constellation points at 45°, 135°, 225°, and 315°. This doubles spectral efficiency compared to BPSK.

.. figure:: images/exercises/pluto_exercises/qpsk_simple/psk_symbols.png
   :align: center
   :width: 40em

   PSK symbol mapping: BPSK (2 symbols), QPSK (4 symbols), 8PSK (8 symbols)

.. figure:: images/exercises/pluto_exercises/qpsk_gnuradio/qpsk_constellation.png
   :align: center
   :width: 40em

   QPSK constellation - 4 points, 2 bits/symbol

PSK with more than 4 symbols increases spectral efficiency but requires better SNR:

.. figure:: images/exercises/pluto_exercises/qpsk_gnuradio/qpsk_ho_modulation.png
   :align: center
   :width: 40em

   Higher-order modulations: 16-QAM, 32-QAM, 64-QAM, 256-QAM

**QPSK GNU Radio Loopback Structure**

The QPSK loopback example in GNU Radio demonstrates the full DSP chain:

.. figure:: images/exercises/pluto_exercises/qpsk_gnuradio/qpsk_loopback_gnuradio_example.png
   :align: center
   :width: 45em

   QPSK loopback GNU Radio flowgraph with TX and RX chains

**Transmitter:**

* Constellation Modulator block: maps bytes into symbols and applies RRC filter

**Receiver:**

* **Frequency Locked Loop (FLL)**: Dynamically adjusts the frequency of the received spectrum
* **Symbol Sync**: Applies RRC filter and selects the right 1 out of 16 symbols
* **Differential Decoder**: Decodes the differentially encoded symbols
* **Constellation Receiver (Costas Loop)**: Fine tunes the remaining frequency and phase error

.. figure:: images/exercises/pluto_exercises/qpsk_simple/qpsk_loopback_gnuradio_run_results.png
   :align: center
   :width: 45em

   QPSK loopback results: same pattern of symbols at TX and demodulated RX

**Key observations:**

* The green trace shows the RX spectrum after FLL block (centered around DC)
* The eye diagram after Costas loop shows clean transitions
* Using the rotation slider, you can rotate the constellation in steps of 90° and observe
  that the symbols received are the same due to Differential Decoding

Raw Loopback - No Additional DSP (Pluto, Jupiter)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Intentionally omits matched filter, frequency correction, and timing recovery to show what happens
without them: wide spectrum, rotating constellation, wrong samples.

.. figure:: images/exercises/pluto_exercises/qpsk_gnuradio/qpsk_gnuradio_flowgraph.png
   :align: center
   :width: 45em

   QPSK flowgraph without additional DSP processing

**Transmitter:**

* Generate sequence of bits
* Map bits onto symbols
* Offset spectrum to the right to not overlap with DC leakage

**Receiver:**

* Shift the spectrum back to DC

**Pluto**

Follow these steps:

#. Make the loopback setup using Pluto with TX connected to RX via an SMA cable and connect it to your PC.

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 20em

      Pluto SDR with loopback cable connecting TX to RX

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **QPSK_raw_loopback_pluto.grc** from
   **beginner_exercises → 3. Quadrature Phase Shift Keying (QPSK)**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the output displays:

   .. figure:: images/exercises/pluto_exercises/qpsk_gnuradio/qpsk_no_processing_result1.png
      :align: center
      :width: 45em

      QPSK without DSP: no frequency offset because loopback uses same LO, but has phase offset

   .. figure:: images/exercises/pluto_exercises/qpsk_gnuradio/qpsk_no_processing_result2.png
      :align: center
      :width: 45em

      The spectrum is inefficiently used (spectrum of square wave)

   **Observations:**

   * No frequency offset because the example works on loopback and the LO is the same for RX and TX
   * But has a phase offset between the two paths
   * Try tweaking the frequency offset between TX and RX and see how the data looks - this happens
     when transmitting and receiving between two different devices
   * The spectrum is inefficiently used (spectrum of square wave)

#. Click the **Stop** button (red square) when finished.

**Jupiter**

Follow these steps:

#. Make the loopback setup with Jupiter — connect TX to RX and connect the board via Ethernet.

   .. figure:: ../images/hw_setup/jupiter_loopback_setup.png
      :align: center
      :width: 20em

      Jupiter SDR with loopback cable connecting TX to RX

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **QPSK_raw_loopback_jupiter.grc** from
   **beginner_exercises → 3. Quadrature Phase Shift Keying (QPSK)**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the same effects as the Pluto version. The frequency offset slider
   demonstrates what happens when TX and RX oscillators are not perfectly synchronized.

#. Click the **Stop** button (red square) when finished.

**Conclusions:**

* The frequency offset and LO drift is required to be corrected at receiver
* The phase offset of the LO at the receiver is required to be corrected
* These are varying with distance and temperature in time → need feedback loop to constantly adjust
* The correct sample from the received signal needs to be extracted (not transitions)
* Even if we do all these, if we rotate the constellation 180°, the symbols received will be out of place


Constellation Modulator (Pluto)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Uses Root-Raised Cosine (RRC) filters for pulse shaping, giving a cleaner spectrum than raw QPSK.

.. figure:: images/exercises/pluto_exercises/qpsk_gnuradio_const_modulator/qpsk_modulator_gnuradio_schematic.png
   :align: center
   :width: 45em

   QPSK flowgraph with Constellation Modulator and RRC filter

**Constellation Modulator block:** Maps bytes into symbols and applies RRC filter.

**RRC filter at RX:** Completes the matched filter pair.

Follow these steps:

#. Make the loopback setup using Pluto with TX connected to RX via an SMA cable and connect it to your PC.

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 20em

      Pluto SDR with loopback cable connecting TX to RX

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **constellation_modulator_loopback_pluto.grc** from
   **beginner_exercises → 3. Quadrature Phase Shift Keying (QPSK) → Constellation Modulator**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the output displays:

   .. figure:: images/exercises/pluto_exercises/qpsk_gnuradio_const_modulator/qpsk_modulator_gnuradio_result_optimized_bw.png
      :align: center
      :width: 45em

      The bandwidth is optimized due to matched filters (one from Const. Modulator at TX and one at RX)

   .. figure:: images/exercises/pluto_exercises/qpsk_gnuradio_const_modulator/qpsk_modulator_gnuradio_result_undecimated_rx.png
      :align: center
      :width: 45em

      The RX signal is not decimated by selecting the right samples

#. Click the **Stop** button (red square) when finished.

**Conclusion:** Using the Constellation Modulator block, the transmitted bits are mapped into IQ
symbols and a RRC filter is applied on the Transmitter path, thus the bandwidth used is optimized.


Frequency Locked Loop - FLL (Pluto)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a Frequency Locked Loop (FLL) to automatically correct for oscillator differences between
TX and RX, keeping the spectrum centered.

.. figure:: images/exercises/pluto_exercises/qpsk_fll/qpsk_fll_gnuradio_schematic.png
   :align: center
   :width: 45em

   QPSK flowgraph with FLL block that dynamically adjusts the frequency of the received spectrum

Follow these steps:

#. Make the loopback setup using Pluto with TX connected to RX via an SMA cable and connect it to your PC.

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 20em

      Pluto SDR with loopback cable connecting TX to RX

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **FLL_loopback_pluto.grc** from
   **beginner_exercises → 3. Quadrature Phase Shift Keying (QPSK) → Frequency Locked Loop (FLL)**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Use the slider to tweak the frequency offset between TX and RX. Observe how the spectrum after FLL
   block stays centered around DC.

   .. figure:: images/exercises/pluto_exercises/qpsk_fll/qpsk_fll_result1.png
      :align: center
      :width: 45em

      Use the slider to tweak the frequency offset - observe spectrum after FLL stays centered around DC

   .. figure:: images/exercises/pluto_exercises/qpsk_fll/qpsk_fll_result2.png
      :align: center
      :width: 40em

      A more precise frequency offset correction still needs to be applied

#. Click the **Stop** button (red square) when finished.


Console Messaging (Pluto, Jupiter)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   **Bonus exercise.** This is an optional bonus exercise — feel free to pick and
   choose which bonus exercises you try.

Packet-based QPSK system where messages are transmitted in bursts and displayed on console.
Each packet contains: access key (preamble), payload length, message data, and CRC32 checksum.

.. figure:: images/exercises/pluto_exercises/qpsk_gnuradio/qpsk_point_to_point_schematic.png
   :alt: QPSK Console Messaging Flowgraph
   :align: center
   :width: 40em

   Transmitter and receiver flowgraph for packet-based QPSK.

This exercise requires **two separate devices** — one running the transmitter flowgraph and
one running the receiver flowgraph. Each device needs its own SDR (Pluto or Jupiter) with
antennas attached. In a workshop setting the instructor typically runs the transmitter; if
you want to run both sides yourself, you need two SDRs and two PCs (or two GNU Radio
Companion instances on the same PC, each connected to a different SDR).

**Pluto**

Follow these steps on the **receiver** device:

#. Attach a receiver antenna to the RX antenna connector and a transmitter antenna to the
   TX antenna connector. Then connect the Pluto to your PC.

   .. figure:: ../images/hw_setup/pluto_qpsk_setup.jpg
      :alt: QPSK Pluto Setup
      :align: center
      :width: 40em

      QPSK Pluto Setup - antennas connected to the RX and TX connectors

#. Open the terminal and navigate to the Desktop directory, then launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd ~/Desktop/datax-workshops/what-sw-for-my-sdr
      $ gnuradio-companion

#. In GNU Radio Companion, open **console_message_receiver_pluto.grc** from
   **beginner_exercises → 3. Quadrature Phase Shift Keying (QPSK) → Console Messaging → Pluto → receiver_pluto**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

On the **transmitter** device (the second Pluto), the same steps apply but open
**console_message_transmitter_pluto.grc** from the ``transmitter_pluto`` subfolder instead.

Once both sides are running:

* The **transmitter** window shows the transmitted samples and spectrum.

  .. figure:: images/exercises/pluto_exercises/qpsk_simple/qpsk_tx_plot.png
     :alt: QPSK Console Message TX Plot
     :align: center
     :width: 40em

     Transmitter output — transmitted samples and spectrum

* The **receiver** window shows the received message, spectrum, and QPSK constellation.

  .. figure:: images/exercises/pluto_exercises/qpsk_simple/qpsk_rx_result.png
     :alt: QPSK Console Message Reception
     :align: center
     :width: 40em

     Receiver output — received message, spectrum, and QPSK constellation

Click the **Stop** button (red square) on each device when finished.


**Jupiter**

Same as Pluto, with minimal code changes for Jupiter.

Follow these steps on the **receiver** device:

#. Attach a receiver antenna to the RX antenna connector and a transmitter antenna to the
   TX antenna connector.

   .. figure:: ../images/hw_setup/jupiter_psk_setup.png
      :alt: Jupiter SDR Hardware Setup for Console Messaging
      :align: center
      :width: 40em

      Jupiter SDR setup - antennas connected to the RX and TX connectors

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd ~/Desktop/datax-workshops/what-sw-for-my-sdr
      $ gnuradio-companion

#. In GNU Radio Companion, open **console_message_receiver_jupiter.grc** from
   **beginner_exercises → 3. Quadrature Phase Shift Keying (QPSK) → Console Messaging → Jupiter → receiver_jupiter**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

On the **transmitter** device, open **console_message_transmitter_jupiter.grc** from the
``transmitter_jupiter`` subfolder instead.

Once both sides are running, observe the received message displayed in the **msg_rx
variable** on the receiver console, along with the constellation diagram showing the QPSK
signal quality.

Click the **Stop** button (red square) on each device when finished.


Text File Messaging (Pluto, Jupiter)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   **Bonus exercise.** This is an optional bonus exercise — feel free to pick and
   choose which bonus exercises you try.

This exercise extends the Console Messaging concept: instead of displaying messages on the console,
the transmitter reads a text file and sends its contents over the air using QPSK, and the receiver
writes the decoded text to a file (``received.txt``). The same packet-based structure is used —
access key, payload length, data, and CRC32 — but the data source and sink are files on disk.

Like Console Messaging, this is a point-to-point exercise: the transmitter flowgraph runs on a
separate device (typically set up by the instructor). The steps below open only the receiver
flowgraph. If you want to run both sides yourself, the transmitter flowgraphs are in the
``transmitter_pluto`` / ``transmitter_jupiter`` subfolders alongside the receiver.

.. figure:: images/exercises/pluto_exercises/qpsk_txtfile_messaging/text_file_msg_gnuradio_schematic.png
   :alt: QPSK Text File Messaging Flowgraph
   :align: center
   :width: 45em

   Transmitter reads from a text file; receiver writes decoded data to ``received.txt``

**Pluto**

Follow these steps:

#. Make the following setup: connect the receiver antenna to the RX antenna connector and the
   transmitter antenna to the TX antenna connector. Then connect the Pluto to your PC.

   .. figure:: ../images/hw_setup/pluto_qpsk_setup.jpg
      :alt: QPSK Pluto Setup
      :align: center
      :width: 40em

      QPSK Pluto Setup - receiver antenna connected to RX connector

#. Open the terminal and navigate to the Desktop directory, then launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd ~/Desktop/datax-workshops/what-sw-for-my-sdr
      $ gnuradio-companion

#. In GNU Radio Companion, open **qpsk_receiver_txtfile_pluto.grc** from
   **beginner_exercises → 3. Quadrature Phase Shift Keying (QPSK) → Text File Messaging → Pluto → receiver_pluto**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the output — the received text is written to ``received.txt`` in the same
   directory as the flowgraph:

   .. figure:: images/exercises/pluto_exercises/qpsk_txtfile_messaging/text_file_msg_gnuradio_output.png
      :alt: QPSK Text File Messaging Output
      :align: center
      :width: 40em

      Received text file contents and signal quality plots

#. Click the **Stop** button (red square) when finished. Open ``received.txt`` to verify the
   decoded message.

**Jupiter**

Follow these steps:

#. Make the following setup: connect the receiver antenna to the RX antenna connector and the
   transmitter antenna to the TX antenna connector.

   .. figure:: ../images/hw_setup/jupiter_psk_setup.png
      :alt: Jupiter SDR Hardware Setup for Text File Messaging
      :align: center
      :width: 40em

      Jupiter SDR setup - receiver antenna connected to RX connector

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd ~/Desktop/datax-workshops/what-sw-for-my-sdr
      $ gnuradio-companion

#. In GNU Radio Companion, open **qpsk_receiver_txtfile_jupiter.grc** from
   **beginner_exercises → 3. Quadrature Phase Shift Keying (QPSK) → Text File Messaging → Jupiter → receiver_jupiter**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the received text written to ``received.txt``, along with the constellation
   diagram showing the QPSK signal quality.

#. Click the **Stop** button (red square) when finished.


Amplitude Shift Keying (ASK) in GNU Radio (Pluto, Jupiter)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ASK encodes data by varying signal amplitude. This exercise uses 4-ASK with symbol levels
between (0, 1/3, 2/3, 1).

.. figure:: images/exercises/pluto_exercises/ask_loopback/ask_gnuradio_example.png
   :align: center
   :width: 45em

   ASK GNU Radio flowgraph showing transmitter and receiver

**Transmitter:**

* Generate four symbols repeatedly
* Repeat each symbol 100 times (100 sps)
* Offset frequency with a complex sinusoid

**Receiver:**

* Decimate (keep only 1 in 100 samples)
* Compute the magnitude of the RX signal

**Conclusion:** ASK combined with PSK forms QAM:

.. figure:: images/exercises/pluto_exercises/ask_loopback/ask_psk_qam.png
   :align: center
   :width: 40em

   ASK + PSK = QAM (used in Wi-Fi, LTE, 5G, cable modems)

**Pluto**

Follow these steps:

#. Make the loopback setup using Pluto with TX connected to RX via an SMA cable and connect it to your PC.

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 20em

      Pluto SDR with loopback cable connecting TX to RX

#. Open the terminal by pressing **Ctrl + Alt + T** and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **ASK_loopback_pluto.grc** from
   **beginner_exercises → 4. Amplitude Shift Keying (ASK)**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the output displays:

   .. figure:: images/exercises/pluto_exercises/ask_loopback/ask_gnuradio_example_result.png
      :align: center
      :width: 45em

      ASK output showing TX symbols, RX constellation with 4 amplitude levels, and magnitude plots

   * **TX symbols**: 100 sps for each symbol between (0, 1/3, 2/3, 1)
   * **RX constellation**: 4 levels of amplitude on the real axis
   * **RX unprocessed signal**: Raw received I/Q samples
   * **Magnitude of RX signal (decimated)**: Only the magnitude, after keeping 1 in 100 samples

#. Use the frequency offset slider to offset the TX signal relative to TX LO frequency
   and observe the changes in the spectrum display.

#. Click the **Stop** button (red square) when finished.


**Jupiter**

Follow these steps:

#. Make the hardware setup using Jupiter SDR with TX1A connected to RX1A via loopback cable.

   .. figure:: ../images/hw_setup/jupiter_loopback_setup.png
      :alt: Jupiter SDR Hardware Setup for ASK
      :align: center
      :width: 40em

      Jupiter SDR setup with TX1A connected to RX1A via loopback cable

#. Open the terminal and launch GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd ~/Desktop/datax-workshops/what-sw-for-my-sdr
      $ gnuradio-companion

#. In GNU Radio Companion, open **ASK_loopback_jupiter.grc** from
   **beginner_exercises → 4. Amplitude Shift Keying (ASK)**.

#. Click the **Execute** button (green arrow) to run the flowgraph.

#. Observe the output displays:

   * **Transmitted Samples**: Shows the repeated symbols with 100 samples per symbol
   * **Received Samples (Unprocessed)**: Raw I/Q signal from the receiver showing amplitude variations
   * **Received Spectrum**: Frequency-domain representation showing the offset carrier
   * **Received Constellation**: Shows **4 distinct amplitude levels** on the real axis (0, 1/3, 2/3, 1)
   * **Magnitude RX**: Time-domain plot showing only the amplitude of the received signal
   * **Decimated RX**: After keeping 1 in 100 samples, showing the recovered symbol sequence

#. You can adjust the frequency offset slider to observe how the received signal changes in the spectrum display.

#. Click the **Stop** button (red square) when finished.


Doppler Radar with GNU Radio (Pluto)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   **Bonus exercise.** This is an optional bonus exercise — feel free to pick and
   choose which bonus exercises you try.

The Doppler effect causes a frequency shift when there is relative motion between radar and target.
This exercise creates a continuous-wave radar using GNU Radio Companion.

The SDR transmits a CW signal at 2.5 GHz. When the signal reflects off your moving hand,
the received frequency shifts - higher pitch when moving toward, lower when moving away.

.. figure:: images/exercises/pluto_exercises/doppler_radar/filter_frequency_diagram.png
   :alt: Band Pass and Reject Filters
   :align: center
   :width: 40em

   Band Reject Filter removes carrier, Band Pass Filter isolates Doppler shift.

**Pluto**

Follow these steps:

#. Make the following setup using Pluto and connect it to your PC:

   .. figure:: ../images/hw_setup/pluto_qpsk_setup.jpg
      :alt: Pluto SDR Doppler Radar Setup
      :align: center
      :width: 20em

      Pluto SDR setup for Doppler radar experiment

#. Open the terminal by simultaneously pressing **Ctrl + Alt + T** on your keyboard.

#. Type the following command in the terminal to open GNU Radio Companion and press Enter:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. In GNU Radio Companion, open **doppler_radar.grc** from
   **beginner_exercises → 5. Doppler Radar**.

   .. figure:: images/exercises/pluto_exercises/doppler_radar/gnu_radio_doppler_schematic.png
      :alt: Doppler Radar GNU Radio Flowgraph
      :align: center
      :width: 40em

      GNU Radio flowgraph for the Doppler radar experiment showing signal processing blocks.

#. To run the flowgraph, press on the green arrow from the top function bar as indicated below.

   .. figure:: images/exercises/pluto_exercises/doppler_radar/run_grc.png
      :alt: Run GNU Radio Flowgraph
      :align: center
      :width: 40em

      Run the GNU Radio flowgraph for Doppler radar experiment

#. Move your hand toward and away from the antennas and observe how the sound and the frequency
   of the received harmonic changes in real time plots.

   The six plots show the received signal at different processing stages: top row displays
   time-domain waveforms, bottom row shows frequency-domain FFT plots where the Doppler shift
   peak moves left (hand moving away) or right (hand moving toward) from the center frequency.

   .. figure:: images/exercises/pluto_exercises/doppler_radar/doppler_plots.png
      :alt: Doppler Radar Principle
      :align: center
      :width: 40em

      Doppler radar principle: the moving hand reflects the transmitted signal back to the
      Rx antenna, shifting the received frequency by ±Δf.


.. note::

   The Doppler radar exercise is only available for the ADALM-Pluto. Jupiter does not
   support this exercise.


