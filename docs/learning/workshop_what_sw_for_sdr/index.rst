What software do I need for my SDR?
===============================================================================

.. contents:: Contents
   :local:
   :depth: 2

Theoretical Concepts and Practical Foundations
----------------------------------------------

Typical Customer Design Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software-defined radio development follows a progressive, stage-based approach that takes designs from initial research through to production deployment.
The key advantage of ADI's approach is that the **same HDL, software, and infrastructure components are used throughout the entire flow**,
reducing the learning curve and development risk at each stage.

.. figure:: images/theoretical_content/customer_design_flow.png
   :alt: Customer Design Flow
   :align: center
   :width: 40em

   Typical Customer Design Flow

The typical customer design flow consists of 5 progressive stages, each building upon the previous one.

In the **research** phase, engineers validate that the chosen ADI device meets application requirements through simulation and measurement.

Key activities include:

* **Behavioral Simulation**: Model the system before building hardware
* **Device Evaluation**: Test actual hardware performance using evaluation boards
* **Measurements**: Characterize critical performance metrics such as SFDR (Spurious-Free Dynamic Range), SNR (Signal-to-Noise Ratio), EVM (Error Vector Magnitude),
  NF (Noise Figure), and NSD (Noise Spectral Density)

Tools used: Evaluation boards, IIO Oscilloscope, ACE software, bench test equipment.

During the **Algorithm Development** phase, engineers implement signal processing algorithms using high-level languages while streaming real data
from hardware.
Here, the focus is on rapid prototyping and validation of algorithms in realistic conditions via **MATLAB/Python/GRC Reference Implementation**,
**Hardware Streaming**, and **Iterative Development**.

Development environments at this stage include MATLAB, Simulink with ADI toolboxes, Python with PyADI-IIO, GNU Radio Companion with gr-iio blocks.

The **Design Elaboration** phase refines algorithms for embedded deployment through modeling and optimization. This stage include modeling using the same
development tools, validating optimized algorithms with real hardware data, and transitioning from floating-point to fixed-point arithmetic
for efficient hardware implementation.

Critical considerations include fixed-point precision, filter coefficient quantization, timing budgets, and FPGA resource utilization.

While *prototyping*, algorithms are deployed to development hardware for integration and optimization. This stage includes:

* **Deployment to Development Board**: Move algorithms to actual hardware (PlutoSDR, Jupiter, or FMC boards)
* **Design Optimization**: Tune for performance and resource efficiency
* **HDL Integration**: Integrate custom signal processing with ADI reference designs

The final stage, **Production**, includes deployment to custom hardware with complete system validation.

Throughout all stages, the same HDL IP cores, Linux kernel drivers, and application software are reused, dramatically reducing development risk and
time-to-market.


Software in the Design-in Journey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI's software ecosystem provides a cohesive solution across the entire design-in journey, supporting multiple development environments
while maintaining a common underlying infrastructure. The ecosystem enables engineers to work in their preferred tools—whether GUI-based applications,
scripting environments, or modeling platforms—all leveraging the same drivers, libraries, and hardware abstraction layers.

**Common Software Infrastructure:**

All components below are part of the `DataX <https://github.com/analogdevicesinc/datax>`_ ecosystem.

* `libiio <https://github.com/analogdevicesinc/libiio>`_: Cross-platform library providing unified hardware access
* **IIO Kernel Drivers**: Linux drivers for ADI converters and transceivers
* **iiod Server**: Network-transparent access to hardware
* **Language Bindings**: Support for C, C++, Python, MATLAB, and more

**Development Tools and Environments:**

* **IIO Oscilloscope** (`link <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_): Cross-platform GUI for visualizing and controlling IIO devices
* **MATLAB and Simulink**: ADI toolboxes for algorithm development and modeling
* **Python**, **Jupiter**, and `PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_: Python library for rapid prototyping with ADI hardware
* **GNU Radio** with **gr-iio** (`link <https://github.com/analogdevicesinc/gr-iio>`_) blocks for flowgraph-based development
* **ACE Software** (`link <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`_): Plugin-based framework for evaluation board control
* **Scopy** (`link <https://analogdevicesinc.github.io/scopy/>`_): Modern multi-instrument software suite


Evaluation, Test and Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices provides a single cohesive software solution, meeting customers in their ecosystem or at their tools of choice.

   .. figure:: images/theoretical_content/sw_solution.png
      :alt: Software Solution Architecture
      :align: center
      :width: 40em

      Single cohesive software solution supporting multiple user personas and tools

**Product Evaluation** uses hardware and software tools to verify that the transceiver meets application requirements.

Time investment is (very roughly) proportional to complexity and how application specific it needs to be.

**Tools:** IIO Oscilloscope, ACE software, Scopy, GNU Radio, MATLAB, bench test equipment


Algorithmic Development, Modeling and Prototyping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Product Prototyping** provides Plug 'n' Play hardware and software to see the key features and performance of the part.

It can configure, capture signals, or generate waveforms in 10-15 minutes, stream real data from hardware into development
environments (MATLAB, Python, GNU Radio) and develop and validate algorithms with hardware-in-the-loop

**Development Environments:** MATLAB, Simulink, Python, `PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_, GNU Radio Companion

**Tools:** MATLAB, Simulink, Python, `PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_, GNU Radio


Building Blocks for Development and New Revenue Streams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI's modular architecture provides reusable building blocks that accelerate development and create opportunities for new applications and revenue streams.

   .. figure:: images/theoretical_content/building_blocks.png
      :alt: Building Blocks for Development
      :align: center
      :width: 40em

      Modular building blocks

Modular building blocks enable rapid development and platform scalability. Signal processing components including filters, decimators, interpolators,
and other DSP primitives are standard offerings that accelerate algorithm implementation. Protocol implementations such as OFDM, QPSK, and FSK
are pre-implemented for rapid deployment, while pre-validated HDL provides high-performance streaming and buffering for demanding applications.

Efficient clock and power distribution features enable portable and battery-powered applications. Multiple libraries and frameworks provide flexible
hardware access and algorithm development: `PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`_ for rapid Python prototyping with hardware-in-the-loop,
MATLAB and Simulink toolboxes for system-level modeling and deployment, GNU Radio with `gr-iio <https://github.com/analogdevicesinc/gr-iio>`_ blocks
for flowgraph-based signal processing, and standardized Linux drivers that reduce integration effort.

The business benefits are compelling. Faster time-to-market results from pre-validated components that reduce development cycles, while proven building
blocks minimize integration challenges and eliminate redundant design work through IP reuse. Platform scalability allows you to start with ADALM-PLUTO
and scale seamlessly to production platforms.

Revenue opportunities emerge through application-specific solutions for vertical markets, proprietary algorithm development, custom hardware transitions
with unified software stacks, and IP licensing of optimized implementations.

Common Architecture for Easy Platform Transition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The common architecture across ADI's platforms makes it easy to transition between hardware as your project evolves from prototype to production.

   .. figure:: images/theoretical_content/common_architecture.png
      :alt: Common Architecture Makes It Easy to Transition Between Platforms
      :align: center
      :width: 40em

      Common architecture enables seamless transitions between platforms

**Shared Software and HDL Stack:**

* **Same libraries**: libiio, PyADI-IIO, and hardware drivers work across all platforms
* **Common Linux image**: ADI Kuiper Linux brings up the same software stack whether on a laptop or embedded board
* **Unified HDL**: Common FPGA designs across all SDR platforms
* **Consistent drivers**: Same drivers whether accessing hardware locally or via USB

**Platform Progression:**

* Start with :adi:`ADALM-PLUTO <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html>`:
   Provides quick verification, rapid algorithm development, and SIGINT applications at very low cost
* **Scale to production**:
   Same software and HDL seamlessly transfer to higher-performance platforms
* **Use modules for clean design**:
   Leverage ADI's reference designs and IP cores

**Open Source Repositories:**

* Common Linux kernel and drivers: https://github.com/analogdevicesinc/linux
* Common HDL IP cores: https://github.com/analogdevicesinc/hdl

This architecture ensures that code developed on entry-level hardware like ADALM-PLUTO can be reused on production platforms with minimal changes,
dramatically reducing development risk and time-to-market.

Analysis | Control | Evaluation
-------------------------------

Once you have the IIO framework set up, you need tools to analyze, control, and evaluate your hardware. ADI provides several software tools that
work seamlessly with IIO devices, from simple command-line utilities to full-featured graphical applications.

ACE Software and Plugins
~~~~~~~~~~~~~~~~~~~~~~~~

**ACE (Analysis, Control, Evaluation)** is ADI's original software framework for interacting with evaluation boards and development platforms.
It provides a plugin-based architecture where different modules can control specific hardware features.

**ADGenericIIOBoard Plugin** is a key plugin within ACE that enables interaction with any IIO-compatible device.
This generic approach means you can use the same plugin to control different ADI evaluation boards without requiring board-specific software.

**Installation:**

Download ACE from the
`ADI website <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`_.
ACE is available for Windows only.

   .. figure:: images/analysis_control_eval/adgeneric_iio_board_plugin.png
      :alt: ADGenericIIOBoard Plugin Interface
      :align: center
      :width: 40em

      ADGenericIIOBoard Plugin showing IIO device control

IIO Oscilloscope
~~~~~~~~~~~~~~~~

**IIO Oscilloscope (IIO-Scope)** is a powerful cross-platform application for visualizing and controlling IIO devices.
It provides both time-domain and frequency-domain visualization along with device configuration capabilities.

**Key Features:**

* **Multi-platform support**: Runs on Linux, Windows, and macOS
* **Time and frequency domain plots**: View signals in both domains simultaneously
* **Device configuration**: Modify hardware parameters in real-time
* **Plugin architecture**: Extensible with generic and device-specific plugins
* **Remote operation**: Can connect to IIO devices over network using iiod

**Installation:**

.. tab-set::

   .. tab-item:: Linux

      .. code-block:: bash

         # Debian/Ubuntu
         sudo apt install iio-oscilloscope

   .. tab-item:: Windows

      Download the installer from the
      `IIO Oscilloscope releases <https://github.com/analogdevicesinc/iio-oscilloscope/releases>`_.

   .. figure:: images/analysis_control_eval/iio_scope.png
      :alt: IIO Oscilloscope Main Interface
      :align: center
      :width: 40em

      IIO Oscilloscope showing time and frequency domain plots

**Generic Plugins:**

IIO-Scope includes several generic plugins that work with any IIO device:

* **DMM (Digital Multimeter) Plugin**:
   Displays real-time numerical values from device channels, useful for monitoring DC values, temperatures, voltages, and other scalar measurements

   .. figure:: images/analysis_control_eval/dmm_plugin.png
      :alt: DMM Plugin Interface
      :align: center
      :width: 40em

      DMM Plugin showing real-time channel values

* **Debug Tab/Plugin**:
   Provides low-level access to all IIO device attributes, allowing direct read/write operations on any device parameter for advanced debugging and development

   .. figure:: images/analysis_control_eval/debug_tab.png
      :alt: Debug Tab Interface
      :align: center
      :width: 40em

      Debug Tab showing device attributes tree

**Specific Control Plugins:**

For more complex devices, IIO-Scope offers specialized plugins:

* **FPGA Settings Plugin**:
   Controls FPGA-specific parameters such as clock configurations, data path settings, and interface modes
* **High Level Device Control Plugins**:
   Provide intuitive interfaces for complex RF transceivers, DACs, and ADCs with features like frequency tuning, gain control, and filter configuration

   .. figure:: images/analysis_control_eval/fpga_settings.png
      :alt: FPGA Settings Plugin
      :align: center
      :width: 40em

      FPGA Settings Plugin for controlling FPGA-specific parameters

   .. figure:: images/analysis_control_eval/high_level_device_ctrl.png
      :alt: High Level Device Control Plugin
      :align: center
      :width: 40em

      High Level Device Control Plugin providing intuitive interfaces for RF transceivers

IIO Command Line Tools
~~~~~~~~~~~~~~~~~~~~~~~

For automation, scripting, and headless operation, the IIO framework includes command-line utilities:

* **iio_info**: Lists all available IIO devices and their attributes
* **iio_attr**: Reads or writes device/channel attributes
* **iio_readdev**: Captures samples from device channels
* **iio_writedev**: Transmits samples to device channels
* **iio_reg**: Direct register access for low-level debugging

.. note::

   The examples below are not meant to be run as part of this workshop — they are some of
   the most common ``iio`` commands that you may choose to run on your own to explore the
   attributes and capabilities of your IIO devices.

These tools are particularly useful for:

* Automated testing and continuous integration
* Remote device control via SSH
* Scripting complex measurement sequences
* Quick parameter verification without GUI overhead

**Installation:**

.. tab-set::

   .. tab-item:: Linux

      .. code-block:: bash

         # Debian/Ubuntu
         sudo apt install libiio-utils

   .. tab-item:: Windows

      Download libiio from the
      `libiio releases <https://github.com/analogdevicesinc/libiio/releases>`_.
      The command-line tools are included in the installer.

**iio_info**

Displays information about all available IIO devices and their attributes, channels, and triggering capabilities.

.. code-block:: bash

   iio_info
   iio_info -n 192.168.1.100

**iio_attr**

Reads or writes device and channel attributes for configuration and control.

.. code-block:: bash

   iio_attr -d cf-ad9361-lpc
   iio_attr -c voltage0 frequency
   iio_attr -c voltage0 frequency 2400000000

**iio_readdev**

Captures samples from device channels and saves to file for analysis.

.. code-block:: bash

   iio_readdev -d cf-ad9361-lpc -c voltage0 -s 1024 > samples.raw

**iio_writedev**

Transmits samples from file to device channels.

.. code-block:: bash

   iio_writedev -d cf-ad9361-lpc -c voltage0 < samples.raw

**Remote Access via iiod**

Connect to IIO devices over network using the iiod server:

.. code-block:: bash

   iio_info -n 10.48.65.212

Scopy: Next-Generation Analysis Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Scopy <https://analogdevicesinc.github.io/scopy/>`_ is ADI's modern, next-generation instrument software that supersedes IIO-Scope with enhanced
capabilities and a more intuitive interface. It transforms your PC into a complete laboratory instrument suite.

**Scopy provides:**

* **Multiple instrument views**: Oscilloscope, spectrum analyzer, network analyzer, signal generator, logic analyzer, pattern generator, and more
* **Modern UI/UX**: Contemporary interface with improved usability
* **Enhanced visualization**: Advanced plotting with zoom, cursors, measurements, and annotations
* **Cross-platform**: Available for Windows, Linux, and macOS
* **Generic IIO support**: Works with any IIO-compatible device, not just ADI hardware
* **Export capabilities**: Save data, screenshots, and configurations for documentation

**Installation:**

Download Scopy from the `Scopy releases page <https://github.com/analogdevicesinc/scopy/releases>`_.
Installers are available for Windows, Linux (AppImage, Flatpak), and macOS.

   .. figure:: images/analysis_control_eval/scopy_interface.png
      :alt: Scopy Main Interface
      :align: center
      :width: 40em

      Scopy interface showing multiple instrument views

Scopy is the recommended tool for new projects, offering a more complete and modern experience than the older IIO-Scope application.

qIQ Receiver
~~~~~~~~~~~~

qIQ Receiver is a specialized application for analyzing and demodulating various wireless communication standards.
It's particularly useful for RF engineers working with:

* **Digital modulation analysis**: BPSK, QPSK, QAM, and other modulation schemes
* **Constellation diagrams**: Real-time visualization of modulation quality
* **Spectrum analysis**: Detailed frequency domain analysis
* **Recording and playback**: Capture RF signals for offline analysis

**Installation:**

qIQ Receiver is available for Windows. Download from the
`qIQ Receiver page <https://www.qorvo.com/design-hub/design-tools/qiq-receiver>`_.

   .. figure:: images/analysis_control_eval/qiq_receiver.png
      :alt: qIQ Receiver Interface
      :align: center
      :width: 40em

      qIQ Receiver showing constellation diagram and spectrum

qIQ Receiver bridges the gap between generic oscilloscope tools and specialized protocol analyzers, making it easier to develop and debug wireless communication systems with ADI SDR platforms.

GNU Radio
~~~~~~~~~

`GNU Radio <https://www.gnuradio.org/>`_ is a free and open-source software development toolkit that provides
signal processing blocks to implement software-defined radios and signal processing systems.
ADI provides the `gr-iio <https://github.com/analogdevicesinc/gr-iio>`_ block set for seamless integration
with IIO-compatible hardware.

**Key Features:**

* **Visual flowgraph design**: GNU Radio Companion (GRC) provides a graphical interface for building
  signal processing chains by connecting blocks
* **Extensive block library**: Hundreds of pre-built blocks for filtering, modulation, demodulation,
  synchronization, and more
* **Real-time processing**: Stream data directly from SDR hardware for live signal processing
* **Cross-platform**: Available on Linux, Windows (via Radioconda), and macOS
* **Python integration**: Flowgraphs generate Python code, enabling scripting and automation

**ADI Integration (gr-iio):**

The `gr-iio <https://github.com/analogdevicesinc/gr-iio>`_ package provides GNU Radio blocks for:

* **PlutoSDR Source/Sink**: Receive and transmit with ADALM-PLUTO
* **FMCOMMS Source/Sink**: Support for FMComms and other AD936x-based platforms
* **Generic IIO blocks**: Work with any IIO-compatible device

**Installation:**

.. tab-set::

   .. tab-item:: Linux

      .. code-block:: bash

         # Debian/Ubuntu - install Python, pip, and GNU Radio
         sudo apt install python3 python3-pip gnuradio gr-iio

   .. tab-item:: Windows

      #. Install `Python <https://www.python.org/downloads/>`__ (ensure "Add to PATH" is checked)

      #. Use `Radioconda <https://github.com/ryanvolz/radioconda>`_ to install GNU Radio:

         .. code-block:: bash

            conda install gnuradio gnuradio-iio

.. figure:: images/analysis_control_eval/gnuradio_companion.png
   :alt: GNU Radio Companion Interface
   :align: center
   :width: 40em

   GNU Radio Companion flowgraph with PlutoSDR source and sink blocks

GNU Radio is ideal for rapid prototyping of communication systems, educational demonstrations,
and developing custom signal processing applications with ADI SDR hardware.

MATLAB and Simulink Toolboxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI provides official toolboxes for MATLAB and Simulink that enable hardware-in-the-loop development
with ADI SDR platforms. These toolboxes integrate seamlessly with MathWorks' signal processing and
communications workflows.

**Available Toolboxes:**

* `Analog Devices Transceiver Toolbox <https://github.com/analogdevicesinc/TransceiverToolbox>`_:
  MATLAB/Simulink interface for ADI RF transceivers (AD936x, ADRV9009, etc.)
* `Analog Devices High Speed Converter Toolbox <https://github.com/analogdevicesinc/HighSpeedConverterToolbox>`_:
  Support for high-speed ADCs and DACs

**Key Features:**

* **System objects**: MATLAB System objects for streaming data to/from hardware
* **Simulink blocks**: Drag-and-drop blocks for hardware integration in Simulink models
* **Hardware-in-the-loop**: Develop and validate algorithms with real RF signals
* **Code generation**: Generate deployable code from Simulink models
* **Example library**: Pre-built examples for common SDR applications

**Supported Hardware:**

* ADALM-PLUTO (PlutoSDR)
* FMCOMMS2/3/4/5 evaluation boards
* ADRV9361-Z7035, ADRV9364-Z7020
* ADRV9009, ADRV9008
* Jupiter SDR

**Installation:**

#. Install MATLAB (R2021a or later recommended) with the following toolboxes:

   * Signal Processing Toolbox
   * Communications Toolbox
   * DSP System Toolbox (recommended)

#. Install libiio:

   .. tab-set::

      .. tab-item:: Linux

         .. code-block:: bash

            sudo apt install libiio-dev

      .. tab-item:: Windows

         Download and install libiio from the
         `libiio releases <https://github.com/analogdevicesinc/libiio/releases>`_.

#. Clone and install the ADI Transceiver Toolbox:

   .. code-block:: bash

      git clone https://github.com/analogdevicesinc/TransceiverToolbox.git

   Then in MATLAB, navigate to the cloned folder and run:

   .. code-block:: matlab

      cd TransceiverToolbox
      startup_trx

   Alternatively, install via MATLAB Add-Ons by searching for "Analog Devices Transceiver Toolbox".

**Example Usage:**

.. code-block:: matlab

   % Create PlutoSDR receiver object
   rx = adi.AD9361.Rx;
   rx.uri = 'ip:pluto.local';
   rx.CenterFrequency = 2.4e9;
   rx.SamplesPerFrame = 2^14;

   % Receive samples
   data = rx();

   % Plot spectrum
   pspectrum(data, rx.SamplingRate);

.. figure:: images/analysis_control_eval/matlab_transceiver_toolbox.png
   :alt: MATLAB Transceiver Toolbox
   :align: center
   :width: 40em

   MATLAB Transceiver Toolbox streaming data from PlutoSDR

The MATLAB toolboxes are ideal for engineers already working in the MathWorks ecosystem who need
to integrate real hardware into their simulation and algorithm development workflows.


SDR Solutions Provided by ADI
------------------------------

These are a few of our SDR products for hobbyists and professionals alike. The hands-on exercises section below showcases
their capabilities along with several application examples that guide you from both a theoretical and practical point of view.

**Hardware Platforms:**

The following three ADI SDR platforms offer different capabilities to suit various development needs:

* :adi:`ADALM-PLUTO <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html>`:
   Entry-level SDR ideal for learning and prototyping

   - 2x Tx and 2x Rx ports (50 Ohm matched)
   - LO Frequency Range: 70MHz → 6GHz
   - Bandwidth: 56MHz
   - Sample rate: 61.44MSPS; 14 bits
   - Interfaces: USB2, UART

* :adi:`Jupiter (AD-JUPITER-EBZ) <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-jupiter-ebz.html>`:
   Mid-range platform for advanced development

   - 2x Tx and 2x Rx ports (50 Ohm matched)
   - LO Frequency Range: 30MHz → 6GHz
   - Bandwidth: 40MHz
   - Sample rate: 61.44MSPS; 16 bits
   - Interfaces: USB3, 1Gb Ethernet, Display Port, UART

* :adi:`Talise SOM (ADRV9009-ZU11EG) <https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/adrv9009-zu11eg.html>`:
   High-performance platform for production-grade applications

   - 4x Tx and 4x Rx (expandable to 8 TRx)
   - LO Frequency Range: 75MHz → 6GHz
   - RX Bandwidth: 200MHz, TX Bandwidth: 450MHz
   - Interfaces: USB3, 1Gb Ethernet, Display Port, PCIe 3.0, SFP, QSFP, UART

All three platforms share the same software stack and HDL architecture, demonstrating ADI's platform scalability—algorithms
developed on the entry-level Pluto can be seamlessly transferred to production-grade hardware with minimal code changes.


Hands on exercises
------------------

.. toctree::
   :maxdepth: 1

   beginner_sdr_exercises/index
   advanced_sdr_exercises/index


References
----------

**ADI Hardware:**

* `[1] ADALM-PLUTO <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html>`_
* `[2] Jupiter SDR <https://wiki.analog.com/resources/eval/user-guides/jupiter-sdr/hardware-overview>`_
* `[3] Talise SOM (ADRV9009-ZU11EG) <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adrv9009-zu11eg.html>`_

**Books and Learning Resources:**

* `[4] T. F. Collins, R. Getz, Di Pu, A. M. Wyglinski - Software-Defined Radio for Engineers, 2018
  <https://www.analog.com/en/resources/education/education-library/software-defined-radio-for-engineers.html>`_
* `[5] GNU Radio <https://www.gnuradio.org/>`_
* `[6] M. Lichtman, "PySDR" <https://pysdr.org/>`_
* `[7] T. F. Collins - ADI Transceivers: A Deep Dive (GRCon18)
  <https://www.gnuradio.org/grcon/grcon18/presentations/ADI_Transceivers_A_Deep_Dive/>`_
* `[8] J. Gallachio - learnSDR <https://github.com/gallicchio/learnSDR>`_

**SDR Software Platforms:**

* `[9] SDRangel <https://www.sdrangel.org/>`_
* `[12] PyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio/>`_
* `[13] iio_attr documentation <https://wiki.analog.com/resources/tools-software/linux-software/libiio/iio_attr>`_
* `GQRX <https://www.gqrx.dk/>`_

**Academic References:**

* [10] K. Mueller and M. Muller, "Timing recovery in digital synchronous data receivers,"
  IEEE Trans. Commun., vol. C-24, no. 5, pp. 516-531, May 1976.
* [11] J. Costas, "Synchronous Communications," Proceedings of the IEEE, vol. 44, p. 1713-1718, 1956

**ADI Kuiper Linux:**

* `[15] Kuiper 2 source code <https://github.com/analogdevicesinc/adi-kuiper-gen/tree/staging/kuiper2.0>`_
* `[16] Kuiper 2 build workflows <https://github.com/analogdevicesinc/adi-kuiper-gen/actions/workflows/kuiper2_0-build.yml>`_
