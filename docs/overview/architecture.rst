.. _overview_architecture:

Full Stack Architecture
===============================================================================

This page explains the complete architecture of `ADI DataX™
<https://developer.analog.com/solutions/adi-datax>`__, from hardware to
applications. Understanding this layered approach will help you see how the
different components work together and where your design fits in.

.. contents:: Contents
   :local:
   :depth: 2

The Seven-Layer Architecture
-------------------------------------------------------------------------------

The ADI technology stack follows a layered architecture model, where each layer provides
services to the layer above it and consumes services from the layer below. This
separation of concerns makes the system modular, testable, and portable across
different platforms.

.. svg:: architecture-layers.svg
   :align: center

   Seven-layer architecture of ADI DataX, from silicon to user applications

Layer 1: Hardware
~~~~~~~~~~~~~~~~~

ADI's analog and mixed-signal silicon: data converters (SAR / Sigma-Delta /
Pipeline ADCs and DACs), RF transceivers, sensors and IMUs, PLLs and
clocks, power management, and signal-chain components. These devices talk
to the digital world over SPI, I2C, JESD204B/C, LVDS, or parallel buses.
See :doc:`components` for which DataX layers apply to each device family.

Layer 2: Hardware Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The processor, FPGA, or microcontroller that physically connects to the
ADI device. Three broad classes: FPGA SoCs (Zynq / ZynqMP / Versal,
Intel SoC FPGAs), Linux-class application processors (Raspberry Pi,
BeagleBone, i.MX, Rockchip, ...), and bare-metal microcontrollers (STM32,
MAX32, RISC-V, and other ARM Cortex-M parts). The choice drives which
DataX components apply; the workflows page works through the most common
combinations.

Layer 3: HDL and Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This layer provides the HDL (Hardware Description Language) or firmware needed
to interface with ADI devices.

**HDL Components (for FPGAs):**

The :external+hdl:doc:`HDL repository <index>` provides:

- **Reference Designs:** Complete FPGA projects for evaluation boards
- **IP Cores:** Reusable building blocks

  - :external+hdl:doc:`JESD204 <library/jesd204/index>` framework for high-speed serial links
  - :external+hdl:doc:`SPI Engine <library/spi_engine/index>` for efficient SPI communication
  - :external+hdl:doc:`DMA controllers <library/axi_dmac/index>` for high-throughput data movement
  - Device-specific interface cores

- **Common Infrastructure:** Clock management, resets, interrupts, AXI interconnects

**Firmware (for Microcontrollers):**

The :external+no-OS:doc:`no-OS repository <index>` provides:

- **Platform-agnostic drivers:** Works across STM32, MAX32, RISC-V, etc.
- **TinyIIO server:** Lightweight IIO protocol implementation for MCUs
- **Build system:** CMake-based builds for multiple platforms
- **RTOS support:** FreeRTOS, Zephyr integration
- **Example projects:** Complete applications for evaluation boards

Layer 4: Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Device drivers provide the software interface to hardware, hiding low-level
register access behind standard APIs.

**Linux IIO Drivers:**

The `IIO (Industrial I/O) <https://www.kernel.org/doc/html/latest/driver-api/iio/index.html>`_
kernel subsystem provides:

- **Standard Interface:** Uniform API across all ADI devices
- **Sysfs Access:** Read/write device attributes via filesystem
- **Buffer Support:** High-speed DMA data capture
- **Trigger System:** Synchronized multi-device sampling
- **Devicetree Integration:** Hardware description and configuration

ADI maintains drivers for hundreds of devices in the mainline Linux kernel.
See the `Linux drivers page <https://wiki.analog.com/resources/tools-software/linux-drivers-all>`_
for the complete list.

**Zephyr Drivers:**

For RTOS-based systems, ADI provides drivers for the `Zephyr Project <https://www.zephyrproject.org/>`_:

- Sensor subsystem integration
- Standard Zephyr APIs
- Devicetree support

**no-OS Drivers:**

For bare-metal microcontroller systems, no-OS drivers provide:

- Direct hardware control
- Minimal overhead
- Platform-agnostic interfaces

Layer 5: Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hardware abstraction libraries provide higher-level access to devices, hiding
the details of drivers and low-level protocols.

**libiio:**

The :ref:`libiio` is the cornerstone of the DataX software stack:

- **Multiple Backends:**

  - ``local:`` - Direct access to local IIO devices
  - ``usb:`` - USB-connected devices (ADALM2000, PlutoSDR)
  - ``ip:`` - Network-connected devices
  - ``serial:`` - Serial-connected devices (microcontrollers running TinyIIO)
  - ``xml:`` - Saved device descriptions

- **Language Bindings:** C, C++, Python, C#, MATLAB
- **Context Management:** Automatic discovery and connection
- **Buffer Operations:** High-performance data streaming
- **Attribute Access:** Read/write device configuration

With libiio, the same code can access a device whether it's on a local Linux
system, across a network, or connected via USB/serial.

**libm2k:**

For ADALM2000 (M2k) devices, libm2k provides:

- High-level instrument APIs (oscilloscope, signal generator, power supply)
- Calibration management
- Streaming data capture
- Python and C++ bindings

Layer 6: Language Bindings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Language bindings provide device-specific, high-level interfaces in various
programming languages.

**pyadi-iio (Python):**

The :external+pyadi-iio:doc:`pyadi-iio library <index>` provides Python classes
for ADI devices:

- **Device-Specific Classes:** ``ad9361``, ``ad4080``, ``ad9081``, etc.
- **NumPy Integration:** Direct access to data as NumPy arrays
- **Property-Based API:** Pythonic attribute access
- **Rapid Prototyping:** Perfect for Jupyter notebooks and scripts

**MATLAB Toolboxes:**

- **Transceiver Toolbox:** Control and data capture for RF transceivers
- **HSX Toolbox:** High-speed ADC/DAC support
- **Simulink Integration:** Hardware-in-the-loop simulation

**C/C++ APIs:**

Direct use of libiio, libm2k, or no-OS libraries for compiled applications.

Layer 7: Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Complete GUI applications provide turn-key solutions for common tasks.

**Scopy:**

:external+scopy:doc:`Scopy <index>` is a multi-function GUI application providing:

- Oscilloscope interface
- Spectrum analyzer
- Signal generator
- Logic analyzer
- Network analyzer
- Custom device control panels

**IIO Oscilloscope:**

A generic viewer for any IIO device:

- Time-domain plots
- FFT analysis
- Attribute configuration
- Data logging

**Kuiper Linux:**

:doc:`Kuiper Linux </linux/kuiper/index>` is a Debian-based distribution with:

- Pre-installed ADI tools (Scopy, IIO Oscilloscope, pyadi-iio)
- Kernel with ADI drivers
- Configuration for ADI evaluation boards
- Development tools pre-configured

Data Flow Example: AD4080 Precision ADC
-------------------------------------------------------------------------------

Let's trace data flow through all seven layers using the AD4080 40 MSPS ADC as
an example, based on the :doc:`Software Infrastructure tutorial </learning/sw_infrastructure/index>`.
This follows the **no-OS path** (Workflow 2): the AD4080 is driven by bare-metal
firmware on an STM32, which exposes it to a host PC via the TinyIIO serial
protocol. The Linux IIO driver path (Layers 3–4) is bypassed in this scenario.

Scenario: Capturing ADC data in Python on a host PC, with the AD4080
connected to an STM32 microcontroller via SPI and the STM32 connected to the
host via USB serial.

.. svg:: dataflow-ad4080.svg
   :align: center

   Data flow for AD4080 ADC with STM32 microcontroller

**Layer 1 - Hardware:**
The AD4080 ADC samples analog signals and provides digital data over SPI.

**Layer 2 - Hardware Interface:**
The STM32 microcontroller (ST Nucleo-H563ZI) interfaces with the AD4080's SPI bus,
handles chip selects, and manages data acquisition timing.

**Layer 3 - Firmware:**
The no-OS firmware running on the STM32:

- Initializes the AD4080 (sampling rate, filter configuration)
- Reads samples via SPI
- Packages data in IIO buffer format
- Runs a TinyIIO server on UART

**Layer 4 - Drivers:**
Not needed in this scenario, as the microcontroller talks directly to libiio
via the serial backend.

**Layer 5 - Libraries:**
libiio on the Raspberry Pi:

- Connects to the STM32 via serial backend (``serial:/dev/ttyACM0,230400,8n1``)
- Discovers the AD4080 IIO device
- Provides buffer interface for data streaming

**Layer 6 - Language Bindings:**
pyadi-iio's ``adi.ad4080`` class wraps the IIO context — the application
code that targets ``serial:`` here is identical to the code that would
target ``local:`` on a Zynq board or ``ip:`` on a remote target; only
the URI changes.

**Layer 7 - Applications:**
Scopy or a custom Python script displays and analyzes the data.

This same architecture works for FPGA-based systems, just with HDL at Layer 3
and Linux IIO drivers at Layer 4 instead of firmware and TinyIIO.

Component Interdependencies
-------------------------------------------------------------------------------

Understanding Component Relationships
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A key strength of ADI DataX is how components share code and design patterns
across different platforms. The HDL repository serves as a common foundation
for both FPGA-based (Linux) and microcontroller-based (no-OS) implementations,
while host tools work uniformly across both paths through libiio.

.. svg:: ecosystem-interdependencies.svg
   :align: center

   How the DataX components depend on each other, with HDL as a common foundation

**Key Relationships:**

**HDL as Common Foundation:**

The HDL repository (analogdevicesinc/hdl) provides:

- **For FPGA/Linux:** IP cores are synthesized into FPGA fabric, generating
  AXI memory maps and devicetree bindings that Linux IIO drivers use
- **For Microcontrollers/no-OS:** Register maps, timing specifications, and
  initialization sequences are referenced by bare-metal drivers

**Host PC Tools - Platform Independent:**

All host-side tools (Python, MATLAB, Scopy, etc.) work identically whether
the device is:

- On a Zynq FPGA running Linux (``local:`` or ``ip:`` backend)
- On a microcontroller running no-OS firmware (``serial:`` backend)
- Connected via USB (``usb:`` backend)

This is achieved through **libiio's abstraction layer**, which presents a
uniform IIO interface regardless of underlying hardware.

How HDL Supports Both Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HDL repository contains more than just FPGA designs - it's the reference
implementation for device behavior.

.. svg:: hdl-shared-usage.svg
   :align: center

   How HDL IP cores and specifications support both FPGA and MCU paths

**Shared Between FPGA and MCU:**

1. **Device Register Maps:**

   - Defined in HDL documentation and IP cores
   - Linux drivers (``axi-ad9081.c``) and no-OS drivers (``ad9081.c``) use
     identical register addresses and bit fields
   - Ensures consistent device configuration

2. **Initialization Sequences:**

   - Complex devices require specific power-up sequences
   - HDL projects document the correct sequence
   - Both Linux and no-OS drivers follow the same initialization

3. **Timing Specifications:**

   - SPI clock rates, setup/hold times defined in HDL
   - FPGA SPI Engine implements these in hardware
   - no-OS software SPI follows the same timing constraints

4. **Interface Patterns:**

   - JESD204 lane configurations
   - DMA transfer sizes and alignment
   - Interrupt handling sequences

**Platform-Specific Implementations:**

- **FPGA:** HDL IP cores synthesized into programmable logic, high-speed
  parallel processing
- **MCU:** Software drivers on ARM Cortex-M, sequential execution, lower speed
  but lower power

**Result:** The same ADI device (e.g., AD9081) works correctly whether connected
to a Zynq FPGA or an STM32 microcontroller, with host applications seeing the
same IIO interface.

Example: AD9081 Across Platforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider the AD9081 MxFE (Mixed-Signal Front End):

**On FPGA (Zynq + Linux):**

1. HDL project (``projects/ad9081_fmca_ebz/zcu102``) synthesizes:

   - JESD204 IP core for multi-gigabit serial links
   - DMA controllers for data streaming
   - AXI interfaces with specific register addresses

2. Linux driver (``axi-ad9081.c``) accesses device via:

   - Memory-mapped AXI registers (programmed by HDL)
   - SPI controller for device configuration
   - DMA buffers for high-throughput data capture

3. Host application uses: ``adi.ad9081(uri="local:")``

**On Microcontroller (STM32 + no-OS):**

1. no-OS firmware references HDL for:

   - Same register map as FPGA implementation
   - Same initialization sequence
   - Same JESD204 configuration (adapted for software)

2. no-OS driver (``ad9081.c``) accesses device via:

   - GPIO bit-banging or hardware SPI peripheral
   - TinyIIO server on USB CDC (serial)
   - Circular buffers for data capture

3. Host application uses: ``adi.ad9081(uri="serial:/dev/ttyACM0,230400,8n1")``

**Identical from the host's perspective:** the same pyadi-iio calls
(``mxfe.rx_sample_rate = ...``, ``mxfe.rx()``) run against either target;
libiio hides the backend difference.

Design Philosophy
-------------------------------------------------------------------------------

Key Principles
~~~~~~~~~~~~~~

DataX layers integrate with existing ecosystems rather than reinventing
them — the Linux IIO subsystem, the Python scientific stack, MATLAB,
and the standard FPGA toolchains all sit at the boundary. The interfaces
between layers (IIO sysfs attributes, IIO buffers, JESD204 framing, the
TinyIIO protocol on the wire) are stable enough that the same higher-
level code runs across local, network, USB, and serial backends and
across Linux, Windows, and macOS hosts. Most of the stack —
HDL, Linux drivers, libiio, pyadi-iio, no-OS — is open source and
maintained on GitHub.

Why the IIO Framework?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Industrial I/O (IIO) <https://www.kernel.org/doc/html/latest/driver-api/iio/index.html>`_
subsystem is central to the ADI architecture. It is not the only kernel subsystem that ADI uses or authors drivers within, but it is the most widely applicable for many ADI products to date. IIO is used for a number of reasons:

**Standard Interface:**
All ADI devices present a uniform interface, whether they're ADCs, DACs, IMUs,
or sensors. Learn it once, use it everywhere.

**Kernel Integration:**
IIO is part of the mainline Linux kernel, maintained by the kernel community.
Drivers go through rigorous review and testing.

**High Performance:**
IIO's buffer interface supports:

- DMA for zero-copy data movement
- Triggered sampling for synchronization
- Watermark-based interrupts for efficient CPU usage

**Extensibility:**
IIO's attribute system allows device-specific features without breaking the
standard interface.

**Cross-Platform:**
TinyIIO brings the IIO protocol to microcontrollers, so the same software stack
works on Linux and bare-metal systems.

Platform Considerations
-------------------------------------------------------------------------------

Choosing the Right Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15 25 30 30

   * - Platform
     - Best For
     - Advantages
     - Considerations
   * - **FPGA (Zynq, ZynqMP, Cyclone, Stratix)**
     - High-speed data converters, custom signal processing, multiple devices
     - Parallel processing, low latency, flexible I/O, Linux + FPGA fabric
     - Higher cost, power, complexity; requires HDL knowledge
   * - **Microcontroller (STM32, MAX32)**
     - Precision measurement, low power, standalone operation, embedded
     - Low cost, low power, real-time, simple deployment
     - Limited processing, slower interfaces, bare-metal or RTOS
   * - **Raspberry Pi / SBC**
     - Prototyping, learning, demos, multi-device setups
     - Low cost, easy to use, full Linux, Python, MATLAB support
     - Limited I/O, no hard real-time, USB/Ethernet connectivity

**Decision Factors:**

- **Sample Rate:** >100 MSPS typically needs FPGA
- **Signal Processing:** FFTs, filtering, custom algorithms favor FPGA
- **Power Budget:** Microcontrollers for battery operation
- **Ease of Development:** Raspberry Pi for rapid prototyping
- **Cost:** Microcontrollers < Raspberry Pi < FPGAs
- **I/O Requirements:** Multiple devices, custom protocols need FPGAs

See :doc:`workflows` for detailed examples of each platform type.

Migration Paths
~~~~~~~~~~~~~~~

The layered architecture is what makes platform migration cheap. Prototype
on a Raspberry Pi with pyadi-iio, validate the algorithm in Python, then
move to no-OS on an MCU for cost / power reduction or to a Zynq board for
performance scaling — at layers 5-7 the code is unchanged; only the
``uri`` passed to ``adi.<device>(uri=...)`` differs (``local:`` vs.
``serial:`` vs. ``ip:``). The :doc:`workflows` page walks through each
combination.

See Also
-------------------------------------------------------------------------------

- :doc:`components` — per-component documentation
- :doc:`workflows` — concrete end-to-end scenarios
- :doc:`versioning-support` — version compatibility and release tracks
- :doc:`Software Infrastructure tutorial </learning/sw_infrastructure/index>` —
  complete AD4080 walk-through
- :doc:`FPGA Integration Journey </learning/workshop_a_precision_converter_fpga_integration_journey/index>` —
  HDL deep dive
- :doc:`Converter Connectivity tutorial </learning/converter_connectivity_tutorial/index>` —
  IIO framework basics
