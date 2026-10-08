DataX Expert Exercises
======================

The following hands-on exercises demonstrate advanced software-defined radio applications
using ADI's SDR platforms.
These exercises build upon the fundamentals covered in the DataX Novice exercises and explore
more sophisticated signal processing techniques, multi-channel systems, and real-world
communication protocols.

.. note::

   These DataX Expert exercises require a solid understanding of SDR fundamentals.
   If you're new to SDR, we recommend starting with the
   :doc:`DataX Novice Exercises <../beginner_sdr_exercises/index>` before attempting
   these DataX Expert topics.


Requirements
~~~~~~~~~~~~

.. important::

   **Manual setups only:** download the exercise files before starting —
   :download:`advanced_exercises.zip <advanced_exercises.zip>` — and extract the archive to
   your Desktop to follow along.

   With the **workshop package** (the recommended Linux setup) you do **not** need this
   download: the ``setup`` script installs the exercises to your Desktop automatically.

These exercises can be run on a **Raspberry Pi 5** running Kuiper Linux with the workshop
package installed (recommended), or from a **PC** (Linux or Windows).

**Hardware:**

* **ADALM-Pluto SDR** (required for all exercises)
* **Micro USB cable** to connect the Pluto to your PC
  (see `Pluto Quick Start <https://wiki.analog.com/university/tools/pluto/users/quick_start>`__
  for details)
* **SMA loopback cable** (for loopback exercises)
* **Antennas**: 2.4 GHz or 915 MHz antennas for over-the-air exercises
* **One SD card** (optional, for Raspberry Pi 5 setup)

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

      After this, the DataX Expert exercises are available under
      ``~/Desktop/datax-workshops/what-sw-for-my-sdr/advanced_exercises``.

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
         :download:`advanced_exercises.zip <advanced_exercises.zip>` and extract them to your Desktop.

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

   Connect your ADALM-Pluto to your PC before starting the exercises. These exercises are
   written for the Pluto, but can be adapted to run on other ADI SDR platforms such as the
   Jupiter or Talise, as shown in the
   :doc:`DataX Novice Exercises <../beginner_sdr_exercises/index>`.

   The following exercises assume the usage of Thonny Python IDE on the Raspberry Pi, but you can use any
   Python IDE or command-line environment on Linux or Windows with the appropriate software installed.

   Generally, the exercises with both a receiver and transmitter counterpart may be run separately (although
   they might yield some warnings) or together with a friend who has the same setup.

.. important::

   **Pluto USB Speed Limitation**: USB 2.0 limits data transfer to 20.4 MiB/s,
   which translates to a maximum sample rate of **5.347 MS/s**.
   Keep this in mind when configuring sample rates for your experiments.

.. tip::

   **Pluto address:** the exercises use ``ip:pluto.local`` (mDNS hostname) and
   ``ip:192.168.2.1`` (default USB-Ethernet IP) interchangeably — both refer to the same
   device. Use whichever resolves on your setup. If ``pluto.local`` does not resolve
   (mDNS/Avahi not available), replace it with ``192.168.2.1``, or vice versa.

.. note::

   If you installed via the workshop package, the exercises live under
   ``~/Desktop/datax-workshops/what-sw-for-my-sdr/advanced_exercises``. Where the steps
   below refer to the **advanced_exercises** folder, that is the location. If you downloaded
   ``advanced_exercises.zip`` instead, use wherever you extracted it — extracting it to your
   Desktop (as instructed above) puts it at ``~/Desktop/advanced_exercises``.

Setting up your SDR
~~~~~~~~~~~~~~~~~~~

These exercises run on the **ADALM-Pluto**. Connect it to your host and prepare it in
software before running any exercise.

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

**What Separates DataX Novices from DataX Expert SDR Users:**

Learning to **test your SDR and find mistakes on your own** is the critical step that
differentiates a DataX Novice from a DataX Expert SDR user.
While DataX Novices focus on running predefined exercises and observing expected results,
DataX Expert users develop the skills to validate system performance, identify impairments,
and troubleshoot issues independently.
The following exercises build these DataX Expert capabilities.

First Steps in SDR Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the theoretical background on sinewave loopback testing, including complex sinusoids,
Zero IF architecture, and key impairments (Image Rejection, LO Leakage, SNR), see the
:ref:`Sinewave Loopback <sinewave-loopback>` section in the DataX Novice Exercises.

Debugging and Tweaking IIO Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This DataX Expert exercise teaches you how to interact with the **Industrial I/O (IIO) subsystem** at a low level, giving you direct control over hardware attributes. Understanding IIO attributes is essential for debugging SDR issues, optimizing performance, and integrating SDR control into custom applications.

**What are IIO Attributes?**

IIO attributes are the low-level parameters that control every aspect of your SDR hardware:

* **Channel attributes**: Per-channel settings like gain, frequency, sample rate
* **Device attributes**: Global settings affecting the entire device
* **Debug attributes**: Low-level register access for DataX Expert debugging

Every high-level API (PyADI-IIO, GNU Radio, MATLAB, Scopy) ultimately reads and writes these IIO attributes through the Linux kernel. By learning to manipulate them directly, you gain:

* **Debugging skills**: Identify whether issues are in your application or the hardware layer
* **Fine-grained control**: Access parameters not exposed by high-level APIs
* **Integration knowledge**: Understand how to integrate SDR control into any application
* **Troubleshooting ability**: Verify attribute values when behavior seems unexpected

**Ways to Access IIO Attributes:**

Today's exercises will use:

#. :adi:`PyADI-IIO <pyadi-iio>`: Python library for SDR control
#. :adi:`libiio <libiio>` utilities: Command-line tools (``iio_attr``, ``iio_info``)
#. :adi:`Scopy <scopy>`: Visual instrument and debugging interface (see the
   `official Scopy documentation <https://wiki.analog.com/university/tools/m2k/scopy>`__
   for a complete guide)

This exercise demonstrates these approaches using the RX gain attribute as an example.

**Using PyADI-IIO to Read/Write Attributes**

**Why This Approach:** Python scripts provide programmatic access to IIO attributes, making it easy to automate configuration, log values, and integrate SDR control into larger applications.

**Steps:**

#. Navigate to the IIO context exercises folder:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ cd ~/Desktop/datax-workshops/what-sw-for-my-sdr/advanced_exercises/1.\ Debugging\ and\ Tweaking\ IIO\ Attributes

#. Open the IIO exploration script in Thonny IDE:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ thonny iio_explore_pyadi.py

   Or right-click ``iio_explore_pyadi.py`` → Open with → **Thonny**

#. Run the script by clicking the **Run** button (green arrow) in Thonny

**What You'll See:**

The script demonstrates how to:

* Create an IIO context (connection to the SDR)
* Access device objects (ad9361-phy for Pluto's RF transceiver)
* Read channel attributes (hardwaregain for RX gain)
* Write channel attributes (set new gain values)
* Verify changes by reading back the value

.. code-block:: python
   :linenos:
   :lineno-start: 1
   :class: code-spaced

   import adi

   # Create IIO context - connects to Pluto SDR
   sdr = adi.Pluto("ip:pluto.local")

   # Access RX channel object
   rx_channel = sdr.rx()

   # Read current RX gain
   current_gain = sdr.rx_hardwaregain_chan0
   print(f"Current RX gain: {current_gain} dB")

   # Set new RX gain value
   sdr.rx_hardwaregain_chan0 = 10  # Set to 10 dB
   print("Set RX gain to 10 dB")

   # Read back to verify
   new_gain = sdr.rx_hardwaregain_chan0
   print(f"New RX gain: {new_gain} dB")

**Expected Output:**

.. code-block:: text

   Current RX gain: 0 dB
   Set RX gain to 10 dB
   New RX gain: 10 dB

**Key Insight:** PyADI-IIO provides a Python-friendly interface to IIO attributes. Under the hood, it's reading and writing the same kernel attributes you'll access with the other tools.

**Using iio_attr Command-Line Utility**

**Why This Approach:** The ``iio_attr`` command-line tool provides immediate access to IIO attributes without writing code. It's ideal for:

* Quick verification of settings
* Shell script automation
* Debugging when GUI tools aren't available
* Understanding the raw IIO interface

**Steps:**

#. Read the current RX gain value:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ iio_attr -u ip:pluto.local -c -i ad9361-phy 'voltage0' hardwaregain

   **What this command does:**

   * ``-u ip:pluto.local``: Connect to Pluto via network (use ``-u usb:`` for USB connection)
   * ``-c``: Access channel-specific attributes
   * ``-i ad9361-phy``: Target the AD9361 RF transceiver device
   * ``'voltage0'``: Select RX1 channel (voltage0 = RX1, voltage1 = RX2)
   * ``hardwaregain``: The attribute name

   **Expected Output:**

   .. code-block:: text

      10

   This shows the value you set in the previous PyADI-IIO exercise (10 dB).

#. Set RX gain to 5 dB:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ iio_attr -u ip:pluto.local -c -i ad9361-phy 'voltage0' hardwaregain 5

   **Expected Output:**

   .. code-block:: text

      5

   The tool automatically reads back and displays the new value after writing it.

#. Experiment with other attributes:

   * List all available devices:

     .. shell::
        :user: analog
        :group: analog
        :show-user:

        $ iio_attr -u ip:pluto.local

   * List all attributes for ad9361-phy device:

     .. shell::
        :user: analog
        :group: analog
        :show-user:

        $ iio_attr -u ip:pluto.local -d ad9361-phy

   * List all channel attributes for voltage0:

     .. shell::
        :user: analog
        :group: analog
        :show-user:

        $ iio_attr -u ip:pluto.local -c -i ad9361-phy 'voltage0'

**Key Insight:** The ``iio_attr`` utility exposes the raw IIO interface. Every attribute you see
here can also be accessed through PyADI-IIO, GNU Radio, MATLAB, or Scopy - they all use the same
underlying IIO layer.

**Using iio_info to Explore the IIO Context**

The ``iio_info`` command provides a quick overview of all devices, channels, and attributes
available in an IIO context. This is useful for discovering what's available on your SDR.

**Steps:**

#. List all devices and their attributes:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ iio_info -u ip:pluto.local

   This command outputs the complete IIO context structure, including:

   * All IIO devices (ad9361-phy, cf-ad9361-lpc, cf-ad9361-dds-core-lpc, etc.)
   * All channels for each device
   * All attributes for each channel and device

#. For a more compact view, you can filter the output:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ iio_info -u ip:pluto.local | grep -E "iio:device|Channel"

**Using Direct Filesystem Access (sysfs)**

IIO attributes are exposed through the Linux sysfs filesystem. You can read and write them
directly using standard shell commands. To do this, you log into the **Linux operating system
running inside the Pluto** itself via SSH — the Pluto runs a minimal embedded Linux that
exposes its hardware through sysfs.

**Steps:**

#. SSH into the Pluto's internal Linux OS:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ ssh root@pluto.local

   Default password: ``analog``

#. Navigate to the IIO devices directory:

   .. shell::
      :user: root
      :group: root
      :show-user:

      $ cd /sys/bus/iio/devices/

#. List available devices:

   .. shell::
      :user: root
      :group: root
      :show-user:

      $ ls -la

   You'll see devices like ``iio:device0``, ``iio:device1``, etc.

#. Read an attribute value directly:

   .. shell::
      :user: root
      :group: root
      :show-user:

      $ cat /sys/bus/iio/devices/iio:device0/in_voltage0_hardwaregain

#. Write an attribute value:

   .. shell::
      :user: root
      :group: root
      :show-user:

      $ echo 10 > /sys/bus/iio/devices/iio:device0/in_voltage0_hardwaregain

#. Verify the change:

   .. shell::
      :user: root
      :group: root
      :show-user:

      $ cat /sys/bus/iio/devices/iio:device0/in_voltage0_hardwaregain

**Key Insight:** Direct filesystem access is useful for embedded applications, shell scripts,
or when you need the lowest-level access to IIO attributes without any library overhead.

Digital QAM Modulation (Pluto)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This DataX Expert exercise explores **16-QAM (Quadrature Amplitude Modulation)**, a higher-order
modulation scheme that encodes 4 bits per symbol by varying both phase and amplitude.
Unlike BPSK (1 bit/symbol) or QPSK (2 bits/symbol), 16QAM uses 16 distinct constellation points,
achieving higher spectral efficiency at the cost of requiring better signal quality.

QPSK is similar to BPSK but has more symbols. PSK with more than 4 symbols includes 8PSK,
16PSK, and beyond.

**GNU Radio Implementation:**

.. important::

   The GNU Radio **Differential Encoder/Decoder blocks do NOT support 16QAM**.
   You must manually rotate the constellation after demodulation to align it with the
   transmitted pattern. Use the slider to find the correct rotation of the constellation.

.. figure:: images/exercises/16qam_with_evm/psk_modulation_gnuradio_schematic.png
   :align: center
   :width: 45em

   16QAM Loopback flowgraph with EVM measurements - Transmitter and Receiver chains

**Understanding the EVM Measurement Block:**

The flowgraph uses the GNU Radio **Measure EVM** block to calculate Error Vector Magnitude.
Here's how the EVM calculation works step by step:

**Step 1: Set of ideal constellation points**

For 16QAM, the ideal constellation points are defined as:

.. math::

   S_{\text{ideal}} = \{s_0, s_1, ..., s_{M-1}\}

where M=16 for 16QAM.

**Step 2: Compute RMS amplitude of the constellation**

.. math::

   A_{\text{RMS}} = \sqrt{\frac{1}{M} \sum_{k=0}^{M-1} |s_k|^2}

For 16QAM with M=16, this gives the reference amplitude for normalization.

**Step 3: Set of noisy symbols received**

.. figure:: images/exercises/16qam_with_evm/psk_modulation_noisy_symbol_set.png
   :align: center
   :width: 45em

   Noisy received symbols compared to ideal constellation points

The received symbols form a set:

.. math::

   R = \{r_0, r_1, ..., r_{N-1}\}

**Step 4: Find the closest ideal symbol**

For each received noisy symbol :math:`r_i`, find the closest ideal symbol :math:`s_{\text{nearest}}`.

**Step 5: Compute error value**

.. math::

   e_i = r_i - s_{\text{nearest},i}

**Step 6: Compute instantaneous EVM for one received symbol**

.. math::

   \text{EVM}_i = \frac{|e_i|}{A_{\text{RMS}}} \times 100\%

The open-source code for this block is available at:
`GNU Radio EVM Implementation <https://github.com/gnuradio/gnuradio/blob/main/gr-digital/lib/meas_evm_cc_impl.cc>`__

**Setup:**

#. Connect the loopback cable between TX1 and RX1:

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 45em

      Pluto SDR with loopback cable connecting TX to RX

#. Open GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. Load the 16QAM flowgraph:

   * Click **File** → **Open**
   * Navigate to: ``~/Desktop/datax-workshops/what-sw-for-my-sdr/advanced_exercises/2. Digital QAM Modulation``
   * Open: ``16QAM_loopback_pluto.grc``

**What You'll See Before Running:**

The flowgraph contains:

* **Transmitter chain**:

  * Random source → 16QAM modulator → Root Raised Cosine (RRC) filter → PlutoSDR Sink

* **Receiver chain**:

  * PlutoSDR Source → RRC filter → 16QAM demodulator → Constellation sink

* **EVM measurement blocks**:

  * Custom Python blocks that calculate Min, Max, and RMS EVM on 100-symbol windows

**Steps:**

#. Run the flowgraph by clicking the **Run** button (green arrow) in the toolbar.

#. Observe the output displays:

   .. figure:: images/exercises/16qam_with_evm/psk_modulation_gnuradio_plot1.png
      :align: center
      :width: 45em

      Same pattern of symbols at TX and demodulated RX. Green shows RX Spectrum after FLL block.

   .. figure:: images/exercises/16qam_with_evm/psk_modulation_gnuradio_plot2.png
      :align: center
      :width: 45em

      Eye diagram after Costas loop of the RX. Use the slider to manually rotate the constellation
      in steps of 90° until it aligns with the transmitted pattern (differential decoding is not
      available for 16QAM).

#. **Observe EVM measurements:**

   .. figure:: images/exercises/16qam_with_evm/psk_modulation_gnuradio_evm_measurement.png
      :align: center
      :width: 45em

      EVM measurements: Instantaneous EVM (%) for each received symbol, Min/Max/RMS EVM over 100 symbols

   The EVM display shows:

   * **Instantaneous EVM (%)**: EVM for each received symbol
   * **Min EVM (%)**: Minimum EVM in 100 symbols
   * **RMS EVM (%)**: Root-mean-square EVM for 100 symbols
   * **Max EVM (%)**: Maximum EVM for 100 symbols
   * **Average EVM (%)**: Running average

#. **Understanding the Python blocks:**

   .. figure:: images/exercises/16qam_with_evm/psk_modulation_python_blocks.png
      :align: center
      :width: 45em

      Python blocks for EVM calculation - EVM RMS is computed over 100-sample windows

   EVM RMS is the RMS value for one window (100 samples) of instantaneous EVM points
   calculated by the EVM Measurement block.

#. Click the **Stop** button (red square) when finished.

Enabling 2nd TX and RX Channels (Pluto)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This exercise demonstrates how to enable and use both TX/RX channel pairs on the AD9361
transceiver in Pluto. Using PyADI-IIO, you can reuse the code and run it on different SDRs
like Pluto, Talise, Jupiter, ADSY1100 (Apollo SoM) and more.

**Prerequisites:**

* **Pluto hack**: `Customizing Pluto <https://wiki.analog.com/university/tools/pluto/users/customizing>`__
* **Pluto firmware update**: `Firmware Update Guide <https://wiki.analog.com/university/tools/pluto/users/firmware>`__

**Hardware Modification:**

To access the 2nd TX and RX channels, you need to add U.FL to SMA cables on Rx2 and Tx2:

.. figure:: images/exercises/mimo/pluto_hardware_mod.png
   :align: center
   :width: 45em

   Hardware modification: Add U.FL to SMA cables on Rx2 and Tx2

**Cable Part Information:**

* **Manufacturer Part Number**: CAB.011 (Taoglas)
* **DigiKey Link**: `CAB.011 on DigiKey <https://www.digikey.com/en/products/detail/taoglas-limited/CAB-011/2332725>`__

**Steps:**

#. Open the Python script in Thonny IDE:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ thonny ~/Desktop/datax-workshops/what-sw-for-my-sdr/advanced_exercises/3.\ Enabling\ 2nd\ TX\ and\ RX\ Channels/python_loopback_sine_pluto_2rx_2tx.py

#. **Examine the code changes** to enable Tx2 and Rx2.

   The key additions/changes to the code are:

   .. code-block:: python
      :linenos:
      :lineno-start: 1
      :class: code-spaced

      import adi
      import numpy as np
      import matplotlib.pyplot as plt

      # Create SDR object
      sdr = adi.Pluto("ip:pluto.local")

      # Configure for 2×2 MIMO operation
      sdr.rx_enabled_channels = [0, 1]  # Enable RX1 and RX2
      sdr.tx_enabled_channels = [0, 1]  # Enable TX1 and TX2

      # Set sample rate (shared by all channels)
      sdr.sample_rate = int(3e6)  # 3 MSPS

      # Set RX buffer size (samples per channel)
      sdr.rx_buffer_size = 2**14  # 16384 samples per channel

      # Set LO frequency (shared by all channels - phase coherent)
      sdr.rx_lo = int(2.4e9)  # 2.4 GHz
      sdr.tx_lo = int(2.4e9)  # 2.4 GHz

      # Set individual channel gains
      sdr.rx_hardwaregain_chan0 = 0  # RX1 gain = 0 dB
      sdr.rx_hardwaregain_chan1 = 0  # RX2 gain = 0 dB
      sdr.tx_hardwaregain_chan0 = -10  # TX1 attenuation = -10 dB
      sdr.tx_hardwaregain_chan1 = -10  # TX2 attenuation = -10 dB

      # Generate different complex sinusoids for each TX channel
      N = 2**14
      fc0 = int(0.02e6)  # TX1: 20 kHz tone
      fc1 = int(0.1e6)   # TX2: 100 kHz tone
      ts = 1 / sdr.sample_rate
      t = np.arange(0, N * ts, ts)

      # TX1 signal: 20 kHz complex sinusoid
      tx1_signal = np.exp(1j * 2 * np.pi * fc0 * t) * 0.9

      # TX2 signal: 100 kHz complex sinusoid
      tx2_signal = np.exp(1j * 2 * np.pi * fc1 * t) * 0.9

      # Interleave TX samples: [tx1[0], tx2[0], tx1[1], tx2[1], ...]
      tx_interleaved = np.empty(N * 2, dtype=np.complex64)
      tx_interleaved[0::2] = tx1_signal  # Even indices = TX1
      tx_interleaved[1::2] = tx2_signal  # Odd indices = TX2

      # Transmit interleaved buffer
      sdr.tx(tx_interleaved)

      # Receive samples (automatically interleaved)
      rx_interleaved = sdr.rx()

      # De-interleave RX samples
      rx1_samples = rx_interleaved[0::2]  # Even indices = RX1
      rx2_samples = rx_interleaved[1::2]  # Odd indices = RX2

      # Plot results
      plt.figure(figsize=(12, 8))

      # RX1 spectrum (should show 20 kHz tone from TX1→RX1 loopback)
      plt.subplot(2, 2, 1)
      plt.psd(rx1_samples, NFFT=1024, Fs=sdr.sample_rate / 1e6)
      plt.title("RX1 Spectrum (TX1→RX1 Loopback)")
      plt.xlabel("Frequency (MHz)")

      # RX2 spectrum (should show 100 kHz tone from TX2→RX2 loopback)
      plt.subplot(2, 2, 2)
      plt.psd(rx2_samples, NFFT=1024, Fs=sdr.sample_rate / 1e6)
      plt.title("RX2 Spectrum (TX2→RX2 Loopback)")
      plt.xlabel("Frequency (MHz)")

      # RX1 time domain
      plt.subplot(2, 2, 3)
      plt.plot(t[:100], rx1_samples.real[:100], label="I (real)")
      plt.plot(t[:100], rx1_samples.imag[:100], label="Q (imag)")
      plt.title("RX1 Time Domain")
      plt.xlabel("Time (s)")
      plt.legend()

      # RX2 time domain
      plt.subplot(2, 2, 4)
      plt.plot(t[:100], rx2_samples.real[:100], label="I (real)")
      plt.plot(t[:100], rx2_samples.imag[:100], label="Q (imag)")
      plt.title("RX2 Time Domain")
      plt.xlabel("Time (s)")
      plt.legend()

      plt.tight_layout()
      plt.show()

   **Key Code Patterns:**

   * **Enable channels**: ``sdr.rx_enabled_channels = [0, 1]``
   * **Individual gain control**: ``sdr.rx_hardwaregain_chan0`` and ``sdr.rx_hardwaregain_chan1``
   * **Sample interleaving**: TX/RX buffers alternate between channels
   * **De-interleaving**: ``rx1 = rx_interleaved[0::2]`` (even), ``rx2 = rx_interleaved[1::2]`` (odd)

#. Run the script by clicking the **Run** button (green arrow) in Thonny.

#. Observe the 2Rx 2Tx loopback results showing independent reception on both channels.

Quadrature Phase Shift Keying (QPSK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These exercises build on the QPSK fundamentals covered in the
:doc:`DataX Novice Exercises <../beginner_sdr_exercises/index>`.
Before starting these DataX Expert QPSK exercises, complete the following DataX Novice exercises:

* **QPSK GNU Radio Loopback Structure** - Understanding the full DSP chain
* **QPSK Console Messaging** - Packet-based transmission
* **QPSK Without Additional DSP** - Raw QPSK loopback
* **QPSK Constellation Modulator** - RRC pulse shaping
* **QPSK Frequency Locked Loop** - Coarse frequency correction

The following exercises isolate and explain the Symbol Sync and Costas Loop blocks
in detail.

Symbol Sync (Pluto)
^^^^^^^^^^^^^^^^^^^

This exercise isolates **Symbol Synchronization** (also called **symbol timing recovery**), a critical DSP block that aligns the receiver's sampling clock with the transmitter's symbol boundaries. Understanding symbol sync is essential for implementing any digital modulation scheme.

**The Synchronization Problem:**

When receiving a digital signal, the receiver faces several challenges:

#. **Frequency offset**: TX and RX local oscillators don't match exactly (handled by FLL)
#. **Phase offset**: Carrier phase is unknown (handled by Costas Loop)
#. **Timing offset**: Don't know WHEN symbols start/end (handled by Symbol Sync)
#. **Sample rate mismatch**: TX and RX clocks drift over time

This exercise focuses on **timing synchronization** - the problem of determining the optimal sampling instant for each symbol.

**Why Symbol Sync Matters:**

* **Without symbol sync**: Sampling at random times within symbol periods → high error rate
* **With symbol sync**: Sampling at optimal decision points → maximum eye opening, minimal ISI

We want to sample where the adjacent symbols cross 0:

.. figure:: images/exercises/qpsk_symbol_sync/cross0.png
   :align: center
   :width: 45em

   Symbol timing recovery: sample where adjacent symbols cross zero

**What Symbol Sync Does:**

The Symbol Sync block:

#. **Estimates symbol timing**: Finds when symbols start and end
#. **Resamples the signal**: Outputs exactly 1 sample per symbol (SPS = 1)
#. **Tracks timing drift**: Adapts to clock frequency differences between TX and RX
#. **Applies matched filtering**: Often includes RRC filter for optimal SNR

**Key Parameters:**

* **Samples per symbol (SPS)**: Input has multiple samples per symbol (e.g., 4 SPS), output has 1 SPS
* **Loop bandwidth**: Controls how quickly timing adjusts (trade-off: fast acquisition vs noise immunity)
* **Damping factor**: Controls oscillation behavior during lock acquisition
* **Timing error detector**: Algorithm that estimates sampling phase error (Mueller-Müller, Gardner, etc.)

**This Exercise's Teaching Approach:**

In DataX Novice QPSK exercises, symbol sync was hidden inside a complete receiver chain. This DataX Expert exercise:

* **Isolates symbol sync**: Shows its effect in isolation
* **Visual comparison**: Constellation with vs without proper symbol timing
* **Interactive tuning**: Adjust loop parameters to see their impact
* **Foundation for custom receivers**: Learn to implement symbol sync in your own DSP chains

**Setup:**

#. Connect loopback cable between TX1 and RX1

   .. figure:: ../images/hw_setup/pluto_loopback_setup.jpg
      :align: center
      :width: 45em

      Pluto SDR with loopback cable connecting TX to RX

#. Open GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. Load the Symbol Sync flowgraph:

   * Click **File** → **Open**
   * Navigate to: ``~/Desktop/datax-workshops/what-sw-for-my-sdr/advanced_exercises/4. Quadrature Phase Shift Keying (QPSK)/Symbol Sync``
   * Open: ``symbol_sync_loopback_pluto.grc``

**Flowgraph Architecture:**

.. figure:: images/exercises/qpsk_symbol_sync/qpsk_symbol_sync_gnuradio_schematic.png
   :align: center
   :width: 45em

   QPSK flowgraph with Symbol Sync block

The flowgraph contains:

* **Transmitter**: Random bits → QPSK modulator → RRC pulse shaping → Pluto TX
* **Receiver path 1** (without Symbol Sync): Pluto RX → Constellation plot
* **Receiver path 2** (with Symbol Sync): Pluto RX → FLL → Symbol Sync → Constellation plot

This side-by-side comparison shows the effect of proper symbol timing.

**Steps:**

#. Run the flowgraph:

   * Click the **Run** button (green arrow)
   * Wait for constellation plots to appear

#. **Observe the constellation WITHOUT Symbol Sync:**

   The first constellation plot shows the received signal with:

   * **FLL applied**: Frequency offset corrected (spectrum centered at DC)
   * **NO symbol sync**: Still sampling at 4 samples per symbol (oversampled)
   * **NO matched filter**: RRC filter not yet applied

   .. figure:: images/exercises/qpsk_symbol_sync/qpsk_symbol_sync_gnuradio_result1.png
      :align: center
      :width: 45em

      All symbols have same amplitude on constellation but I/Q still varying due to remaining frequency/phase offset

   **What you'll see:**

   * **4 samples per symbol**: Each QPSK symbol appears as a cluster of 4 points
   * **Trajectory lines**: Can see the transitions between symbols (not just decision points)
   * **Blurred constellation**: Hard to identify the 4 QPSK decision regions
   * **Variable amplitude**: Symbol magnitudes are inconsistent

   **Why this happens:**

   * Sampling at 4 SPS means you capture intermediate points during symbol transitions
   * Haven't identified the optimal sampling instant within each symbol
   * Matched filter (RRC) hasn't been applied yet

#. **Observe the constellation WITH Symbol Sync:**

   The second constellation plot shows the same signal after Symbol Sync:

   * **1 sample per symbol**: Downsampled to symbol rate
   * **Matched filter applied**: RRC filter provides optimal SNR
   * **Optimal sampling instants**: Only the decision points, not transitions

   .. figure:: images/exercises/qpsk_symbol_sync/qpsk_symbol_sync_gnuradio_result2.png
      :align: center
      :width: 45em

      After symbol sync, constellation points have consistent amplitude

   .. figure:: images/exercises/qpsk_symbol_sync/qpsk_symbol_sync_gnuradio_result_plot1.png
      :align: center
      :width: 45em

      Symbol sync timing stays around 16 = sps setting

   .. figure:: images/exercises/qpsk_symbol_sync/qpsk_symbol_sync_gnuradio_result_plot2.png
      :align: center
      :width: 45em

      Symbol sync error stays around 0

   **What you'll see:**

   * **Tight symbol clusters**: All symbols have the same magnitude
   * **Four clear regions**: QPSK constellation is clearly visible
   * **No transition trails**: Only sampling at optimal decision instants
   * **Remaining rotation**: Phase/frequency offset still present (needs Costas Loop)

   **What changed:**

   * Symbol Sync found the optimal sampling phase within each symbol period
   * Downsampled from 4 SPS to 1 SPS
   * Applied matched filter (RRC) for maximum SNR

#. **Compare the two constellations side-by-side:**

   **Key differences:**

   +---------------------------+----------------------------------+----------------------------------+
   | **Aspect**                | **Without Symbol Sync**          | **With Symbol Sync**             |
   +===========================+==================================+==================================+
   | **Samples per symbol**    | 4 SPS (oversampled)              | 1 SPS (symbol rate)              |
   +---------------------------+----------------------------------+----------------------------------+
   | **Amplitude uniformity**  | Variable (transition samples)    | Constant (decision points only)  |
   +---------------------------+----------------------------------+----------------------------------+
   | **Constellation clarity** | Blurred, trajectory visible      | Clean, distinct symbol clusters  |
   +---------------------------+----------------------------------+----------------------------------+
   | **Matched filter**        | Not applied                      | Applied (optimal SNR)            |
   +---------------------------+----------------------------------+----------------------------------+
   | **ISI (Inter-Symbol       | High (wrong sampling instants)   | Minimal (optimal sampling)       |
   | Interference)**           |                                  |                                  |
   +---------------------------+----------------------------------+----------------------------------+

#. **Observe remaining impairments:**

   Even with Symbol Sync, you'll notice:

   * **Constellation rotation**: The QPSK points may not align with ±1±j
   * **Small residual frequency offset**: FLL doesn't correct perfectly

   These impairments will be addressed by the **Costas Loop** in the next exercise.

#. Stop the flowgraph:

   * Click the **Stop** button
   * Or middle-click on a plot → **Stop**

**Understanding the Symbol Sync Block:**

The GNU Radio **Symbol Sync** block (or **Polyphase Clock Sync**) implements:

#. **Timing error detector**: Estimates whether sampling is early or late

   * **Mueller-Müller algorithm**: Common for PSK modulations
   * **Gardner algorithm**: Non-data-aided, works without knowing symbol values
   * **Early-Late Gate**: Simple but effective for pulse-shaped signals

#. **Loop filter**: Smooths timing error estimates

   * Low-pass filters noisy error signals
   * Determines loop bandwidth and damping

#. **Interpolator**: Resamples signal at optimal timing instants

   * **Polyphase filterbank**: Efficiently resamples with arbitrary fractional delay
   * Includes matched filter (RRC) for optimal SNR

#. **Timing drift tracking**: Continuously adapts to TX/RX clock frequency differences

**Timing Error Detector Intuition:**

The Mueller-Müller algorithm uses this insight:

* **At optimal sampling instant**: Symbol transitions are abrupt
* **Early sampling**: Still in previous symbol (transition not complete)
* **Late sampling**: Already in next symbol (transition overshot)

By analyzing consecutive samples and their differences, the algorithm estimates timing error and adjusts the sampling phase.

**Loop Parameters:**

* **Loop bandwidth**: Typically 0.01 to 0.1 rad/sample

  * **Higher BW**: Faster acquisition, more sensitive to noise
  * **Lower BW**: Slower acquisition, more robust to noise

* **Damping factor**: Typically 0.707 (critically damped)

  * **Higher damping**: Less overshoot, slower settling
  * **Lower damping**: Faster settling, more overshoot

**Next Step:**

The **Costas Loop** exercise (next) will address the remaining phase and frequency offsets, completing the QPSK receiver synchronization chain:

#. **FLL**: Coarse frequency offset correction (covered in DataX Novice exercises)
#. **Symbol Sync**: Timing synchronization + matched filtering (this exercise)
#. **Costas Loop**: Fine frequency and phase offset correction (next exercise)

Together, these three blocks form the complete synchronization subsystem for QPSK demodulation.

**DataX Expert Exploration:**

Try modifying the flowgraph:

#. Remove FLL before Symbol Sync - observe how frequency offset affects timing recovery
#. Change Symbol Sync loop bandwidth (0.01 vs 0.1) - observe acquisition speed vs noise sensitivity
#. Add intentional sampling frequency offset (TX sample rate ≠ RX sample rate) - watch Symbol Sync track the drift

Costas Loop (Pluto)
^^^^^^^^^^^^^^^^^^^

This exercise isolates the **Costas Loop**, a phase-locked loop (PLL) that performs **carrier synchronization** by removing residual frequency and phase offsets. The Costas Loop is the final synchronization stage in a complete QPSK receiver, enabling accurate symbol demodulation.

**The Carrier Synchronization Problem:**

Even after FLL (coarse frequency correction) and Symbol Sync (timing recovery), the received constellation still has:

* **Residual frequency offset**: FLL corrects to within ~100 Hz, but not perfectly
* **Phase offset**: Unknown carrier phase (could be rotated 0°, 90°, 180°, or 270°)
* **Phase drift**: TX and RX oscillators drift slowly over time

Without carrier synchronization:

* Constellation rotates continuously (frequency offset)
* Constellation has fixed but unknown rotation (phase offset)
* Cannot make correct symbol decisions

**What is a Costas Loop?**

The Costas Loop is a **carrier recovery circuit** that:

#. **Estimates phase error**: Computes how much the constellation is rotated
#. **Generates correction**: Produces a phase offset to counteract the rotation
#. **Tracks phase drift**: Continuously adapts to changing carrier phase

It's specifically designed for suppressed-carrier modulations (BPSK, QPSK, 8PSK) where there's no pilot tone to lock onto.

**Why "Costas" Loop?**

Named after John P. Costas (1956), who invented this technique for **carrier recovery without a pilot tone**. Before Costas, receivers needed the transmitter to send a separate carrier reference signal. The Costas Loop extracts carrier phase information from the modulated signal itself.

**Costas Loop Architecture:**

**Key Components:**

#. **Phase error detector**: Computes ``error = I × Q`` (for QPSK)

   * When constellation is correctly aligned: ``I × Q ≈ 0``
   * When rotated: ``I × Q ≠ 0``, sign indicates direction

#. **Loop filter**: Low-pass filters the error signal

   * Smooths noisy error estimates
   * Determines loop bandwidth (trade-off: acquisition speed vs jitter)

#. **NCO (Numerically Controlled Oscillator)**: Generates phase correction

   * Integrates filtered error to produce phase offset
   * Rotates the constellation to cancel carrier offset

#. **Complex multiplier**: Applies phase correction to input signal

**Phase Error Detector for QPSK:**

The classic Costas error function for QPSK is:

.. math::

   \text{error} = \text{sign}(I) \times Q - \text{sign}(Q) \times I

This is a **decision-directed** error detector:

* Uses hard decisions (sign) on in-phase component
* Measures error on quadrature component
* Minimized when constellation aligns with decision boundaries

**This Exercise's Teaching Approach:**

Previous exercises used Costas Loop as part of a complete receiver. This DataX Expert exercise:

* **Isolates Costas Loop effect**: Shows constellation before vs after phase correction
* **Demonstrates phase tracking**: Observe how loop locks and tracks drift
* **Visual understanding**: See phase rotation disappear in real-time
* **Parameter exploration**: Tune loop bandwidth to understand trade-offs

**Setup:**

#. Connect loopback cable between TX1 and RX1

#. Open GNU Radio Companion:

   .. shell::
      :user: analog
      :group: analog
      :show-user:

      $ gnuradio-companion

#. Load the Costas Loop flowgraph:

   * Click **File** → **Open**
   * Navigate to: ``~/Desktop/datax-workshops/what-sw-for-my-sdr/advanced_exercises/4. Quadrature Phase Shift Keying (QPSK)/Costas Loop``
   * Open: ``costas_loop_loopback_pluto.grc``

**Flowgraph Architecture:**

.. figure:: images/exercises/qpsk_costas_loop/qpsk_costas_loop_gnuradio_schematic.png
   :align: center
   :width: 45em

   QPSK flowgraph with Costas Loop for fine frequency and phase correction

The flowgraph contains:

* **Transmitter**: Random bits → QPSK modulator → RRC pulse shaping → Pluto TX
* **Receiver (before Costas)**: Pluto RX → FLL → Symbol Sync → Constellation plot
* **Receiver (after Costas)**: ... → Costas Loop → Constellation plot

This side-by-side comparison shows the Costas Loop's effect on carrier synchronization.

**Steps:**

#. Run the flowgraph:

   * Click the **Run** button (green arrow)
   * Wait for constellation plots to appear

#. **Observe the constellation BEFORE Costas Loop:**

   The first constellation plot shows the received signal after FLL and Symbol Sync but BEFORE Costas Loop:

   * **Frequency mostly corrected**: Spectrum centered near DC (FLL worked)
   * **Timing synchronized**: 1 sample per symbol, clean symbol clusters (Symbol Sync worked)
   * **Residual rotation**: Constellation slowly rotates or has fixed offset
   * **Phase ambiguity**: Might be rotated by 0°, 90°, 180°, or 270°

   .. figure:: images/exercises/qpsk_costas_loop/qpsk_costas_loop_example_result1.png
      :align: center
      :width: 45em

      Symbols are now separated as expected, transitions in eye diagrams are less noisy

   **What you'll see:**

   * **Slow rotation**: Constellation spins slowly (residual frequency offset ~10-100 Hz)
   * **OR fixed rotation**: Constellation locked at wrong angle (phase offset only)
   * **Clear symbol clusters**: Symbol Sync already gave us good sampling instants
   * **Wrong decision regions**: Symbols don't align with ±1±j

   **Why this happens:**

   * FLL corrects coarse frequency offset but leaves small residual
   * No mechanism yet to track fine frequency drift or phase offset
   * Symbol decisions would have high error rate (symbols near decision boundaries)

#. **Observe the constellation AFTER Costas Loop:**

   The second constellation plot shows the same signal after Costas Loop:

   * **No rotation**: Constellation is stationary
   * **Aligned with decision regions**: Symbols at ±1±j (or 90° multiples)
   * **Stable phase**: Tracking and correcting any remaining drift

   .. figure:: images/exercises/qpsk_costas_loop/qpsk_costas_loop_example_result2.png
      :align: center
      :width: 45em

      Clean QPSK constellation after Costas Loop correction

   You can tweak the bandwidth of the Costas Loop and see how it influences the error signal
   and the constellation plot. You can also add a phase shift in radians after Costas Loop.

   .. figure:: images/exercises/qpsk_costas_loop/qpsk_costas_loop_example_result_plot.png
      :align: center
      :width: 45em

      Error signal centered around 0, Phase Correction signal between 0 and 2π

   **What you'll see:**

   * **Stationary constellation**: No rotation, even over long observations
   * **Aligned symbols**: Points cluster tightly around ±1±j (ideal QPSK positions)
   * **Minimal phase jitter**: Small random variations due to noise, but well-controlled
   * **Ready for demodulation**: Symbol decisions can now be made accurately

   **What the Costas Loop did:**

   * Detected the phase error using the ``I × Q`` error function
   * Generated a phase correction signal via the loop filter and NCO
   * Applied correction by rotating the input signal
   * Continuously tracked and corrected residual frequency drift

#. **Compare the two constellations side-by-side:**

   **Key differences:**

   +---------------------------+----------------------------------+----------------------------------+
   | **Aspect**                | **Before Costas Loop**           | **After Costas Loop**            |
   +===========================+==================================+==================================+
   | **Rotation**              | Slowly rotating or fixed offset  | Stationary (locked)              |
   +---------------------------+----------------------------------+----------------------------------+
   | **Phase alignment**       | Random (0°, 90°, 180°, 270°)     | Aligned with decision regions    |
   +---------------------------+----------------------------------+----------------------------------+
   | **Frequency offset**      | Small residual (±100 Hz)         | Fully corrected (<1 Hz)          |
   +---------------------------+----------------------------------+----------------------------------+
   | **Symbol decisions**      | High error rate                  | Low error rate (near optimal)    |
   +---------------------------+----------------------------------+----------------------------------+
   | **Demodulation ready**    | No                               | Yes                              |
   +---------------------------+----------------------------------+----------------------------------+

#. **Observe phase ambiguity resolution:**

   **Important**: The Costas Loop locks to one of **four possible phase states** (0°, 90°, 180°, 270°) because QPSK has 4-fold rotational symmetry.

   * Run the flowgraph multiple times
   * Notice the constellation may lock to different rotations
   * All four rotations are valid Costas Loop lock points

   **Why this happens:**

   * QPSK modulated signal has 90° rotational symmetry
   * Costas Loop error function has the same symmetry
   * Cannot distinguish between the four rotations without additional information

   **How production systems resolve this:**

   * **Differential encoding**: Encode information in phase transitions, not absolute phase
   * **Pilot symbols**: Send known symbols for absolute phase reference
   * **Framing**: Use frame headers with known patterns to detect rotation

   In this flowgraph, differential encoding is used, so the 90° phase ambiguity doesn't affect data recovery.

#. **Experiment with loop bandwidth:**

   Locate the Costas Loop block parameters:

   * **Loop bandwidth**: Default ~0.01 to 0.05 rad/sample

   Try different values:

   * **Higher bandwidth (0.1)**: Faster lock, more phase jitter, less stable
   * **Lower bandwidth (0.001)**: Slower lock, less jitter, more stable

   Observe how acquisition time and noise sensitivity change.

#. Stop the flowgraph:

   * Click the **Stop** button
   * Or middle-click on a plot → **Stop**

**Understanding Costas Loop Parameters:**

The GNU Radio **Costas Loop** block has these key parameters:

* **Loop bandwidth**: Controls how aggressively the loop tracks phase changes

  * **High BW (>0.05)**: Fast acquisition, good for high dynamics, but more sensitive to noise
  * **Low BW (<0.01)**: Slow acquisition, rejects noise well, but can't track fast phase changes

* **Order**: QPSK uses order=4 (4-PSK)

  * Order = number of constellation points with equal magnitude
  * BPSK = 2, QPSK = 4, 8PSK = 8

* **Maximum frequency deviation**: How much frequency offset the loop can track

**Costas Loop vs PLL:**

* **Traditional PLL**: Needs a pilot tone (unmodulated carrier)
* **Costas Loop**: Recovers carrier from modulated signal (no pilot needed)

The Costas Loop is essentially a **data-aided PLL** that uses symbol structure to estimate phase error.

**Phase Error Detector:**

For QPSK, the error function is:

.. code-block:: python

   error = I * sign(Q) - Q * sign(I)

**Intuition:**

* When constellation is aligned (I and Q at ±1): ``error ≈ 0``
* When rotated clockwise: ``error > 0`` → NCO compensates counterclockwise
* When rotated counterclockwise: ``error < 0`` → NCO compensates clockwise

The ``sign()`` function makes it **decision-directed**: it assumes symbols are near decision boundaries and uses that assumption to compute error.

**Complete QPSK Receiver Synchronization Chain:**

You've now studied all three synchronization stages:

#. **FLL (Frequency-Locked Loop)**:

   * **Function**: Coarse frequency offset correction
   * **Accuracy**: ±100 Hz
   * **Speed**: Fast acquisition

#. **Symbol Sync**:

   * **Function**: Timing recovery + matched filtering
   * **Output**: 1 sample per symbol at optimal decision instants
   * **Adapts to**: Sample clock differences between TX and RX

#. **Costas Loop**:

   * **Function**: Fine frequency and phase correction
   * **Accuracy**: <1 Hz frequency error, <5° phase error
   * **Resolves**: Residual offsets and drift

Together, these blocks form a **complete carrier and timing synchronization subsystem** that enables reliable QPSK demodulation under realistic channel conditions.

**DataX Expert Challenge:**

Modify the flowgraph to:

#. Remove the FLL block before Costas Loop
#. Add a large frequency offset (~50 kHz)
#. Observe whether Costas Loop alone can acquire lock (hint: it usually cannot - FLL is essential)
#. Restore FLL and observe two-stage frequency correction: FLL (coarse) → Costas (fine)

**Real-World Applications:**

Costas Loop and its variants are used in:

* **GPS receivers**: Tracking carrier phase for position accuracy
* **Satellite communications**: Maintaining lock on moving spacecraft
* **4G/5G**: Carrier synchronization before OFDM symbol timing
* **Deep space communications**: Extremely weak signals with high frequency uncertainty

Understanding the Costas Loop gives you the foundation to implement robust digital receivers for any PSK modulation scheme.