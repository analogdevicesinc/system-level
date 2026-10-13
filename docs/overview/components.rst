.. _overview_components:

Ecosystem Components
===============================================================================

This page provides detailed information about each major component in the ADI
prototyping ecosystem. Each section explains what the component does, its key
features, when to use it, and where to find detailed documentation.

.. contents:: Contents
   :local:
   :depth: 2

HDL (Hardware Description Language)
-------------------------------------------------------------------------------

What It Is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :external+hdl:doc:`HDL repository <index>` provides FPGA reference designs
and reusable IP (Intellectual Property) cores for interfacing with ADI devices.
These are complete, tested designs that you can use as-is or customize for your
specific application.

The HDL components are written in Verilog and target both Xilinx and Intel (Altera)
FPGAs. They handle the low-level details of interfacing with high-speed serial
links (JESD204), SPI buses, parallel interfaces, and more.

Key Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Reference Designs:**

Complete FPGA projects for ADI evaluation boards, including:

- Top-level HDL integrating all IP blocks
- Constraints files (pinout, timing)
- Block designs for Zynq/ZynqMP (ARM + FPGA)
- Build scripts and documentation

Browse available designs at :external+hdl:doc:`projects/index`.

**IP Core Library:**

Reusable, parameterizable IP blocks:

- **JESD204B/C Framework** (:external+hdl:doc:`library/jesd204/index`): Complete
  implementation of the JESD204 high-speed serial interface standard used by
  RF transceivers and high-speed ADCs/DACs

- **SPI Engine** (:external+hdl:doc:`library/spi_engine/index`): High-performance
  SPI controller optimized for ADI devices, supporting speeds up to 100 MHz

- **AXI DMAC** (:external+hdl:doc:`library/axi_dmac/index`): High-throughput DMA
  controller for moving data between FPGA fabric and processor memory

- **ADI Device Interfaces**: Parallel, LVDS, and other device-specific cores

**Common Infrastructure:**

- Clock management and distribution
- Reset generation and synchronization
- AXI interconnects and bridges
- Interrupt controllers
- Utility functions (data width converters, clock domain crossings)

**Build System:**

- Automated project generation for Vivado and Quartus
- Library dependency management
- Multi-platform support (Zynq, ZynqMP, Versal, Intel SoCs)

When to Use HDL Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose HDL-based FPGA designs when you need:

- **High Sample Rates:** >100 MSPS ADCs, RF transceivers (GSPS)
- **Low Latency:** Real-time signal processing, feedback loops
- **Multiple Devices:** Interfacing with several converters simultaneously
- **Custom Signal Processing:** FFTs, filtering, custom algorithms in hardware
- **High Data Rates:** Multi-gigabit JESD204 links
- **Flexible I/O:** Custom digital interfaces, GPIO control

**Example Applications:**

- Software-defined radio (SDR) platforms
- Radar and communications systems
- High-speed data acquisition
- Medical imaging
- Test and measurement equipment

Getting Started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Choose a reference design for your evaluation board from :external+hdl:doc:`projects/index`
2. Follow the :external+hdl:doc:`user_guide/build_hdl` guide to build the project
3. Program the FPGA and boot Linux
4. Use the Linux IIO drivers (pre-configured in reference designs)
5. Access devices via libiio and pyadi-iio

**Required Skills:**

- Basic FPGA concepts (recommended but not required to use reference designs)
- Vivado or Quartus tools familiarity
- Linux kernel basics for driver integration

**Learning Resources:**

- :doc:`FPGA Integration Journey </learning/workshop_a_precision_converter_fpga_integration_journey/index>` workshop
- :external+hdl:doc:`user_guide/index` - Complete HDL documentation

Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Main Documentation:** `HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/index.html>`_
- **GitHub Repository:** `analogdevicesinc/hdl <https://github.com/analogdevicesinc/hdl>`_
- **Reference Projects:** :external+hdl:doc:`projects/index`
- **IP Core Library:** :external+hdl:doc:`library/index`

Linux Kernel Drivers
-------------------------------------------------------------------------------

What It Is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADI maintains Linux kernel drivers for hundreds of devices as part of the mainline
Linux kernel. These drivers implement the `IIO (Industrial I/O) <https://www.kernel.org/doc/html/latest/driver-api/iio/index.html>`_
framework, providing a standard interface for data converters, sensors, and
signal chain components.

The drivers run in kernel space and expose devices through:

- **sysfs attributes:** Read/write device configuration
- **Character devices:** High-speed data streaming via buffers
- **Devicetree bindings:** Hardware description and platform configuration

Key Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Comprehensive Device Support:**

ADI drivers cover:

- ADCs and DACs (SAR, Sigma-Delta, Pipeline, RF Sampling)
- RF Transceivers and Direct-Sampling Converters
- Amplifiers and References
- IMUs, Accelerometers, Gyroscopes
- Temperature Sensors
- PLLs and Clock Generators
- DDS (Direct Digital Synthesis)
- Digital Potentiometers and Switches

See the complete list at the `Linux Drivers Page <https://wiki.analog.com/resources/tools-software/linux-drivers-all>`_.

**IIO Framework Benefits:**

- **Standard Interface:** Same API for all device types
- **High Performance:** DMA-based buffer interface for zero-copy data transfer
- **Triggering:** Synchronized multi-device sampling
- **Event System:** Threshold detection, alarms
- **Debug Interface:** Complete attribute access via sysfs

**Devicetree Integration:**

Hardware configuration via devicetree:

- Pin connections and chip selects
- Clock frequencies
- Reference voltages
- Device-specific parameters

Example devicetree snippet:

::

   &spi0 {
       adc@0 {
           compatible = "adi,ad4080";
           reg = <0>;
           spi-max-frequency = <80000000>;
           refin-supply = <&adc_vref>;
       };
   };

When to Use Linux Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose Linux-based systems when you need:

- **Full OS Features:** Networking, filesystem, multi-tasking
- **Rich Ecosystems:** Python, MATLAB, C/C++, web servers
- **Remote Access:** SSH, VNC, web interfaces
- **Complex Applications:** Database logging, cloud connectivity, GUIs
- **Rapid Development:** Leverage Linux tools and libraries

**Supported Platforms:**

- Xilinx Zynq/ZynqMP/Versal (ARM + FPGA)
- Intel SoC FPGAs
- Raspberry Pi
- BeagleBone
- i.MX, Rockchip, AllWinner processors
- Any ARM/x86/RISC-V platform with appropriate buses (SPI, I2C, etc.)

Getting Started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**For Xilinx Zynq Platforms:**

1. Use ADI's pre-built HDL reference design (includes devicetree)
2. Build Linux kernel with :ref:`linux-kernel`, :ref:`linux-kernel petalinux`
   is also supported.
3. Boot Linux on target
4. Drivers load automatically based on devicetree
5. Access via libiio

**For Raspberry Pi / Other Platforms:**

1. Use :doc:`Kuiper Linux </linux/kuiper/index>` (Debian with ADI integration)
2. Connect ADI device via SPI/I2C (e.g., Arduino shields)
3. Configure devicetree overlay
4. Driver loads automatically
5. Access via libiio

**Required Skills:**

- Linux basics (command line, package management)
- Devicetree concepts (for custom hardware)
- Optional: Kernel compilation for custom platforms

Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Driver Documentation:** `Linux Drivers Page <https://wiki.analog.com/resources/tools-software/linux-drivers-all>`_
- **Getting Started:** `Linux Kernel Getting Started <https://analogdevicesinc.github.io/linux/getting_started.html>`_
- **Kernel Builds:** :doc:`Build Guides </linux/kernel/index>`
- **IIO Framework:** `Kernel IIO Documentation <https://www.kernel.org/doc/html/latest/driver-api/iio/index.html>`_

libiio (Hardware Abstraction Library)
-------------------------------------------------------------------------------

What It Is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`libiio` is the cornerstone library of the ADI
software ecosystem. It provides a platform-independent API for accessing IIO
devices, abstracting away the differences between local hardware, network-connected
devices, USB gadgets, and serial-connected microcontrollers.

With libiio, the same application code works whether your device is:

- On a local Linux system (sysfs/char device access)
- Connected via USB (ADALM2000, PlutoSDR)
- On a remote system over the network
- Connected to a microcontroller via serial (TinyIIO protocol)

Key Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Multiple Backends:**

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Backend
     - Description
     - URI Format
   * - ``local:``
     - Direct access to local IIO devices via sysfs and char devices
     - ``local:``
   * - ``ip:``
     - Network access via iiod (IIO daemon)
     - ``ip:192.168.1.100`` or ``ip:hostname.local``
   * - ``usb:``
     - USB-connected devices (ADALM2000, PlutoSDR, etc.)
     - ``usb:`` (auto-discover) or ``usb:1.2.5`` (specific device)
   * - ``serial:``
     - Serial-connected microcontrollers running TinyIIO
     - ``serial:/dev/ttyACM0,230400,8n1``
   * - ``xml:``
     - Load saved device context from XML file
     - ``xml:context.xml``

**Language Bindings:**

libiio has native bindings for:

- C/C++ (native API)
- Python
- C# (.NET)
- MATLAB (via mex files)

**Command-Line Utilities:**

Useful for debugging and scripting:

- ``iio_info`` - List devices and attributes
- ``iio_attr`` - Read/write attributes
- ``iio_readdev`` - Capture data to file
- ``iio_writedev`` - Replay data from file

**Performance:**

- Zero-copy data paths where possible
- DMA buffer support for high throughput
- Asynchronous I/O operations

When to Use libiio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use libiio directly when:

- You need fine-grained control over IIO device access
- You're working in C/C++ and want low-level access
- You're building custom applications or tools
- You need the command-line utilities for scripting

**Note:** Most Python developers will use :external+pyadi-iio:doc:`pyadi-iio <index>`
(built on libiio) rather than libiio directly, as it provides device-specific
high-level interfaces.

Getting Started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Installation:**

On Debian/Ubuntu (including Kuiper Linux):

.. code-block:: bash

   sudo apt install libiio-utils libiio-dev python3-libiio

**Build from Source:**

See :ref:`libiio build` for complete instructions.

**Example C Code:**

.. code-block:: c

   #include <iio.h>

   struct iio_context *ctx;
   struct iio_device *dev;

   // Create context (local, network, USB, or serial)
   ctx = iio_create_context_from_uri("local:");

   // Find device
   dev = iio_context_find_device(ctx, "ad4080");

   // Read attribute
   char buf[1024];
   iio_device_attr_read(dev, "sampling_frequency", buf, sizeof(buf));
   printf("Sample rate: %s\n", buf);

   // Cleanup
   iio_context_destroy(ctx);

**Example Python Code:**

.. code-block:: python

   import iio

   # Create context
   ctx = iio.Context("serial:/dev/ttyACM0,230400,8n1")

   # Find device
   dev = ctx.find_device("ad4080")

   # Read attribute
   rate = dev.attrs["sampling_frequency"].value
   print(f"Sample rate: {rate}")

Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Main Documentation:** `libiio Documentation <https://analogdevicesinc.github.io/libiio/v0.26/index.html>`__
- **GitHub Repository:** :git-libiio:`/`
- **Build Instructions and API reference:** :ref:`libiio`

no-OS (Bare-Metal Firmware Framework)
-------------------------------------------------------------------------------

What It Is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:external+no-OS:doc:`no-OS <index>` is a platform-agnostic firmware framework
for bare-metal embedded systems. It provides drivers and example applications
for ADI devices running on microcontrollers without a full operating system.

The no-OS framework targets developers building cost-sensitive, low-power, or
real-time systems where the overhead of Linux is unnecessary or undesirable.

Key Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Platform Abstraction:**

Write once, compile for multiple MCU platforms:

- STM32 (STMicroelectronics)
- MAX32 (Analog Devices)
- RISC-V (SiFive, GigaDevice)
- Other ARM Cortex-M platforms

The Hardware Abstraction Layer (HAL) isolates device drivers from platform-specific
code.

**Device Drivers:**

Hundreds of drivers for:

- Data converters (ADCs, DACs)
- RF transceivers
- Sensors and IMUs
- PLLs and clock generators
- Power management ICs

Drivers are source-compatible with Linux IIO drivers where possible, easing
migration between platforms. See :ref:`overview_workflows` for the recommended
approach of prototyping with Linux first and transitioning to no-OS once the
use case is proven.

**TinyIIO Server:**

A lightweight implementation of the IIO protocol for microcontrollers:

- Exposes devices via serial, USB CDC, or network (with lwIP)
- Compatible with libiio client applications
- Allows using Scopy, IIO Oscilloscope, and pyadi-iio with MCUs
- Minimal RAM/flash footprint

**RTOS Support:**

Integration with real-time operating systems:

- FreeRTOS
- Zephyr RTOS
- Bare-metal (no RTOS)

**Build System:**

CMake-based build system supporting:

- Multiple toolchains (GCC, Keil, IAR)
- Out-of-tree projects
- Library dependencies

When to Use no-OS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose no-OS for:

- **Low Power:** Battery-operated devices, energy harvesting
- **Low Cost:** Inexpensive MCUs ($1-$10)
- **Real-Time:** Deterministic timing, hard deadlines
- **Standalone Operation:** No need for networking or complex UI
- **Simple Deployment:** Single binary, no OS updates
- **Resource Constrained:** Limited RAM/flash

**Example Applications:**

- Portable medical devices
- Industrial sensors
- Wearable devices
- Standalone data loggers
- Battery-powered instrumentation
- Precision measurement equipment

Getting Started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Prerequisites:**

- Evaluation board (e.g., EVAL-AD4080-ARDZ)
- Microcontroller board (e.g., ST Nucleo)
- ARM GCC toolchain or vendor IDE (STM32CubeIDE, Keil, etc.)
- Serial connection to host PC

**Workflow:**

1. Clone the :external+no-OS:doc:`no-OS repository <index>`
2. Choose a project or create a new one
3. Configure for your platform and device
4. Build with CMake or vendor IDE
5. Flash to microcontroller
6. Connect via serial and use libiio to access device

**Example from Tutorial:**

The :doc:`Software Infrastructure tutorial </learning/sw_infrastructure/index>`
walks through a complete example with the AD4080 ADC and STM32 Nucleo.

Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Main Documentation:** `no-OS Documentation <https://analogdevicesinc.github.io/no-OS/index.html>`_
- **GitHub Repository:** `analogdevicesinc/no-OS <https://github.com/analogdevicesinc/no-OS>`_
- **Build Guide:** :external+no-OS:doc:`index`
- **TinyIIO:** :external+no-OS:doc:`tinyiiod documentation <index>`

pyadi-iio (Python Device Interfaces)
-------------------------------------------------------------------------------

What It Is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:external+pyadi-iio:doc:`pyadi-iio <index>` provides device-specific Python
classes for ADI hardware, built on top of libiio. Rather than working with
generic IIO attributes and buffers, you get a high-level, Pythonic API tailored
to each device family.

Key Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Device-Specific Classes:**

Pre-built classes for major device families:

- **AD9361 / AD9364:** Wideband transceivers
- **AD9081 / AD9082:** MxFE (Mixed-Signal Front End)
- **ADRV9009:** Wideband transceiver
- **AD4080 / AD4630 / AD4020 / AD7124 / AD7606:** ADCs
- **AD9144 / AD9172:** DACs
- **ADXL345 / ADIS16505:** IMUs and sensors
- And many more...

**Pythonic API:**

.. code-block:: python

   import adi

   # Create device
   sdr = adi.ad9361(uri="ip:pluto.local")

   # Configure (properties, not method calls)
   sdr.sample_rate = 2000000
   sdr.rx_rf_bandwidth = 200000
   sdr.rx_lo = 915000000
   sdr.gain_control_mode_chan0 = "slow_attack"

   # Receive data (returns NumPy array)
   data = sdr.rx()

**NumPy Integration:**

- Data returned as NumPy arrays (real or complex)
- Direct integration with SciPy, Matplotlib, Pandas
- Easy data processing and visualization

**Quick Context Switching:**

Change ``uri`` parameter to move between backends:

.. code-block:: python

   # Local device
   adc = adi.ad4080(uri="local:")

   # Network device
   adc = adi.ad4080(uri="ip:192.168.1.100")

   # Serial device
   adc = adi.ad4080(uri="serial:/dev/ttyACM0,230400,8n1")

   # Code remains identical regardless of backend

**Jupyter Notebook Friendly:**

Perfect for interactive exploration, data analysis, and educational use.

When to Use pyadi-iio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use pyadi-iio for:

- **Rapid Prototyping:** Test device functionality quickly
- **Data Analysis:** Capture data and analyze with SciPy/Pandas
- **Automation:** Scripted testing and characterization
- **Education:** Learn about devices interactively
- **Application Development:** Build Python applications with ADI hardware
- **Algorithm Development:** Test DSP algorithms with real hardware

**Not Suitable For:**

- Hard real-time applications (use C/C++ or no-OS)
- Extremely high-throughput streaming (GHz sample rates)
- Deeply embedded systems (no Python runtime)

Getting Started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Installation:**

.. code-block:: bash

   pip install pyadi-iio

Or for latest development version:

.. code-block:: bash

   pip install git+https://github.com/analogdevicesinc/pyadi-iio.git

**Quick Example:**

.. code-block:: python

   import adi
   import matplotlib.pyplot as plt

   # Create AD4080 ADC object
   adc = adi.ad4080(uri="serial:/dev/ttyACM0,230400,8n1")

   # Configure
   adc.rx_buffer_size = 4096
   adc.sampling_frequency = 1000000

   # Capture data
   data = adc.rx()

   # Plot
   plt.plot(data)
   plt.title("AD4080 ADC Capture")
   plt.xlabel("Sample")
   plt.ylabel("Code")
   plt.show()

Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Main Documentation:** :external+pyadi-iio:doc:`index`
- **GitHub Repository:** :git-pyadi-iio:`/`
- **Examples:** :external+pyadi-iio:doc:`guides/examples`
- **Device Classes:** :external+pyadi-iio:doc:`devices/index`

Applications and Tools
-------------------------------------------------------------------------------

Scopy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:external+scopy:doc:`Scopy <index>` is a multi-function GUI application providing
test instrument interfaces:

- **Oscilloscope:** Time-domain waveform capture and display
- **Spectrum Analyzer:** FFT and frequency-domain analysis
- **Signal Generator:** Arbitrary waveforms, sine, square, triangle
- **Network Analyzer:** Bode plots, gain/phase measurements
- **Logic Analyzer:** Digital signal capture
- **Pattern Generator:** Digital pattern generation
- **Power Supply Control:** For ADALM2000 and supported devices
- **Device Panels:** Custom controls for specific devices

**Supported Hardware:**

- ADALM2000 (M2k) - primary platform
- ADALM1000 (M1k)
- Generic IIO devices (via debug panels)
- Devices running TinyIIO (microcontrollers)

**Platforms:** Linux, Windows, macOS

IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A generic viewer for any IIO device:

- **Time Domain:** Real-time waveform plots
- **Frequency Domain:** FFT analysis
- **Attributes:** Configure all device settings via GUI
- **Data Logging:** Record to files
- **Debug Interface:** Access any IIO attribute

Less polished than Scopy, but works with any IIO device without custom support.

**Platforms:** Linux, Windows (older versions)

MATLAB Toolboxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Transceiver Toolbox:**

Control and data capture for RF transceivers:

- AD9361, AD9371, ADRV9009, AD9081, and more
- Streaming data to MATLAB workspace
- Integration with Communications Toolbox
- Filter design and configuration

**HSX Toolbox:**

Support for high-speed ADCs and DACs:

- AD9680, AD9144, AD9172, and similar
- Waveform generation and capture
- JESD204 configuration

**Platforms:** Windows, Linux, macOS (MATLAB 2018b or newer)

Kuiper Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Kuiper Linux </linux/kuiper/index>` is a Debian-based Linux distribution
optimized for ADI development:

**Pre-Installed Software:**

- Scopy and IIO Oscilloscope
- pyadi-iio and libiio
- Development tools (GCC, Python, git)
- Jupyter Lab for interactive Python
- GNU Radio for SDR applications

**Pre-Configured:**

- Kernel with ADI drivers
- Devicetree overlays for common boards
- Network configuration for ADI devices

**Supported Platforms:**

- Raspberry Pi 4/400
- BeagleBone
- Xilinx Zynq (via SD card image)

See Also
-------------------------------------------------------------------------------

**Next Steps:**

- :doc:`workflows` - See how these components work together in real applications
- :doc:`versioning-support` - Understand version compatibility
- :doc:`architecture` - Review the full-stack architecture

**Learning Resources:**

- :doc:`Software Infrastructure Tutorial </learning/sw_infrastructure/index>`
- :doc:`Converter Connectivity Tutorial </learning/converter_connectivity_tutorial/index>`

**External Documentation:**

- `HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/index.html>`_
- `Linux Drivers <https://wiki.analog.com/resources/tools-software/linux-drivers-all>`_
- `libiio Documentation <https://analogdevicesinc.github.io/libiio/v0.26/index.html>`_
- `no-OS Documentation <https://analogdevicesinc.github.io/no-OS/index.html>`_
