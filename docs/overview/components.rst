.. _overview_components:

ADI DataX Components
===============================================================================

`ADI DataX™ <https://developer.analog.com/solutions/adi-datax>`__ is the
umbrella name for the stack of components ADI publishes to make its hardware
easy to integrate — spanning FPGA logic, kernel drivers, libraries, language
bindings, applications, and ready-to-use Linux images. **Most projects use
only a subset.** Which pieces apply depends on where the ADI part lives, what
processor (if any) sits next to it, and where the application code runs.

This page is a reference: each section covers one DataX component on its own
terms — what it does, when it's the right tool, and where to find its full
documentation. For end-to-end examples that show several components working
together as a single system, see :ref:`overview_workflows`.

.. contents:: Contents
   :local:
   :depth: 2

Choosing what you need
-------------------------------------------------------------------------------

The components below are layered, but you rarely need every layer. A few common
project shapes and the components each typically pulls in:

.. list-table::
   :header-rows: 1
   :widths: 30 12 18 12 28

   * - Project shape
     - HDL
     - Linux drivers
     - no-OS
     - libiio / pyadi-iio
   * - FPGA + Linux SoC (Zynq, ZynqMP, Versal)
     - ✓
     - ✓
     -
     - ✓
   * - Microcontroller + ADI part (STM32, MAX32, RISC-V)
     -
     -
     - ✓
     - ✓ via TinyIIO
   * - Raspberry Pi + Arduino-shield eval board
     -
     - ✓
     -
     - ✓
   * - Host PC + USB instrument (ADALM2000, PlutoSDR)
     -
     -
     -
     - ✓
   * - Remote target accessed over the network
     - varies
     - ✓ on the target
     -
     - ✓ on the host

Each row picks up a different slice of the stack; the :doc:`workflows` page walks
through a worked example of each.

The remainder of this page is ordered roughly bottom-up through the stack: HDL,
Linux kernel drivers, libiio, no-OS, pyadi-iio, and the user-facing applications
and tools.

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

Role in DataX
~~~~~~~~~~~~~

HDL is the FPGA-side foundation. The same IP cores (JESD204, SPI Engine,
AXI DMAC) are reused across reference designs and feed both the Linux IIO
drivers (via AXI memory-mapped interfaces and devicetree bindings) and
no-OS code (which mirrors the same register maps and initialization
sequences). Browse the
:external+hdl:doc:`IP core library <library/index>` and
:external+hdl:doc:`reference projects <projects/index>` for what's
available.

When to Use HDL Components
~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose HDL-based FPGA designs when you need:

- **High Sample Rates:** >100 MSPS ADCs, RF transceivers (GSPS)
- **Low Latency:** Real-time signal processing, feedback loops
- **Multiple Devices:** Interfacing with several converters simultaneously
- **Custom Signal Processing:** FFTs, filtering, custom algorithms in hardware
- **High Data Rates:** Multi-gigabit JESD204 links
- **Flexible I/O:** Custom digital interfaces, GPIO control

Typical applications: software-defined radio, radar and communications
systems, high-speed data acquisition, medical imaging, test &
measurement.

Documentation
~~~~~~~~~~~~~

- :external+hdl:doc:`HDL user guide <user_guide/index>` — including
  :external+hdl:doc:`build instructions <user_guide/build_hdl>`
- :external+hdl:doc:`IP core library <library/index>`
- :external+hdl:doc:`Reference projects <projects/index>`
- :doc:`FPGA Integration Journey workshop </learning/workshop_a_precision_converter_fpga_integration_journey/index>` —
  hands-on tutorial

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

Role in DataX
~~~~~~~~~~~~~

The Linux drivers are the largest and most mature DataX layer (1500+ ADI
parts in mainline). They expose every supported device through the
standardised IIO interfaces — sysfs attributes for control, character
devices for high-throughput buffered capture — which is what libiio,
pyadi-iio, and applications like Scopy depend on. On a Zynq-class FPGA
platform, the drivers are the bridge between the HDL IP cores below and
libiio above; on a Raspberry Pi, they're the entire kernel-side stack.

When to Use Linux Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose Linux-based systems when you need:

- **Full OS Features:** Networking, filesystem, multi-tasking
- **Rich Ecosystems:** Python, MATLAB, C/C++, web servers
- **Remote Access:** SSH, VNC, web interfaces
- **Complex Applications:** Database logging, cloud connectivity, GUIs
- **Rapid Development:** Leverage Linux tools and libraries

Drivers run on any platform that supports the upstream Linux kernel:
Xilinx Zynq / ZynqMP / Versal, Intel SoC FPGAs, Raspberry Pi,
BeagleBone, i.MX / Rockchip / AllWinner processors, and other ARM /
x86 / RISC-V hosts with the appropriate buses (SPI, I2C, ...).

Documentation
~~~~~~~~~~~~~

- `Complete driver list <https://wiki.analog.com/resources/tools-software/linux-drivers-all>`_
  on the ADI wiki — per-device documentation, devicetree examples, and
  known issues
- :doc:`Kernel build guides </linux/kernel/index>`
- :doc:`Kuiper Linux </linux/kuiper/index>` — pre-configured image for
  Raspberry Pi and similar boards
- `Linux IIO framework reference <https://www.kernel.org/doc/html/latest/driver-api/iio/index.html>`_

libiio (Hardware Abstraction Library)
-------------------------------------------------------------------------------

What It Is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`libiio` is the cornerstone library of the DataX software stack. It
provides a platform-independent API for accessing IIO devices, abstracting
away the differences between local hardware, network-connected devices, USB
gadgets, and serial-connected microcontrollers.

With libiio, the same application code works whether your device is:

- On a local Linux system (sysfs/char device access)
- Connected via USB (ADALM2000, PlutoSDR)
- On a remote system over the network
- Connected to a microcontroller via serial (TinyIIO protocol)

.. svg:: libiio-architecture.svg
   :align: center

   libiio sits between the application and the underlying transport. The
   ``IIOD`` daemon re-exports local devices over the network so a remote client
   can use the same API with only a URI change.

Role in DataX
~~~~~~~~~~~~~

libiio is the unified API every DataX-aware host application talks to. Its
backends — ``local:`` (sysfs / char devices on the same Linux host),
``ip:`` (TCP through the ``iiod`` daemon on a remote target), ``usb:``
(USB-attached instruments like ADALM2000), ``serial:`` (microcontrollers
running TinyIIO), and ``xml:`` (saved contexts) — let the same application
move between local, remote, and embedded targets by changing only the URI
string. Native C, C++, Python, C#, and MATLAB bindings are available, plus
command-line tools (``iio_info``, ``iio_attr``, ``iio_readdev``,
``iio_writedev``) for scripting and debugging.

When to Use libiio
~~~~~~~~~~~~~~~~~~

Reach for libiio directly when you need fine-grained C/C++ control, are
embedding the API in a custom tool, or want the command-line utilities
for scripting and triage. Most Python work goes through
:external+pyadi-iio:doc:`pyadi-iio <index>` instead — it's built on top
of libiio and adds device-specific classes.

Documentation
~~~~~~~~~~~~~

- :ref:`libiio` — build, install, and full API reference
- :git-libiio:`Source repository </>`

no-OS (Bare-Metal Firmware Framework)
-------------------------------------------------------------------------------

What It Is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:external+no-OS:doc:`no-OS <index>` is a platform-agnostic firmware framework
for bare-metal embedded systems. It provides drivers and example applications
for ADI devices running on microcontrollers without a full operating system.

The no-OS framework targets developers building cost-sensitive, low-power, or
real-time systems where the overhead of Linux is unnecessary or undesirable.

Role in DataX
~~~~~~~~~~~~~

no-OS is the bare-metal counterpart to the Linux drivers: a
platform-agnostic HAL plus device drivers that target STM32, MAX32,
RISC-V, and other ARM Cortex-M MCUs. Three things make it integrate with
the rest of DataX:

- **Source-compatible with Linux IIO drivers** where possible — a device
  prototyped under Linux can transition to no-OS without rewriting
  driver code.
- **TinyIIO server** — a small implementation of the IIO protocol over
  serial, USB-CDC, or (with lwIP) network, so libiio clients (Scopy,
  pyadi-iio, etc.) can talk to a microcontroller exactly the way they
  talk to a Zynq board.
- **RTOS-friendly** — runs bare-metal or under FreeRTOS / Zephyr.

When to Use no-OS
~~~~~~~~~~~~~~~~~~

Choose no-OS for low-power, low-cost, real-time, or resource-constrained
deployments — battery-powered instruments, industrial sensors, wearables,
standalone data loggers, precision measurement equipment.

Getting Started
~~~~~~~~~~~~~~~

For a complete walkthrough of running an AD4080 on STM32 Nucleo via
TinyIIO, see :doc:`Software Infrastructure </learning/sw_infrastructure/index>`.

Documentation
~~~~~~~~~~~~~

- :external+no-OS:doc:`no-OS documentation <index>` — prerequisites,
  build, flashing, and TinyIIO reference
- :git-no-OS:`Source repository </>`
- :doc:`Software Infrastructure tutorial </learning/sw_infrastructure/index>` —
  hands-on AD4080 + STM32 Nucleo walkthrough

pyadi-iio (Python Device Interfaces)
-------------------------------------------------------------------------------

What It Is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:external+pyadi-iio:doc:`pyadi-iio <index>` provides device-specific Python
classes for ADI hardware, built on top of libiio. Rather than working with
generic IIO attributes and buffers, you get a high-level, Pythonic API tailored
to each device family.

Role in DataX
~~~~~~~~~~~~~

pyadi-iio sits one layer above libiio: device-specific Python classes
(``adi.ad9361``, ``adi.ad4080``, ``adi.adxl345``, etc.) hide the IIO
register and attribute layout, return data as NumPy arrays ready for
SciPy / Matplotlib / Pandas, and switch between local, network, USB, and
serial backends by changing the ``uri`` parameter alone. Browse the
:external+pyadi-iio:doc:`device class catalog <devices/index>` for
what's supported.

When to Use pyadi-iio
~~~~~~~~~~~~~~~~~~~~~

Use pyadi-iio for rapid prototyping, data analysis, scripted automation,
education, and Jupyter-style exploration. Reach for libiio in C/C++
instead when you need hard real-time, GHz-class streaming, or a deeply
embedded build with no Python runtime.

Documentation
~~~~~~~~~~~~~

- :external+pyadi-iio:doc:`pyadi-iio documentation <index>` — install,
  API reference, supported devices
- :external+pyadi-iio:doc:`Device classes <devices/index>`
- :external+pyadi-iio:doc:`Examples <guides/examples>`
- :git-pyadi-iio:`Source repository </>`

Applications and Tools
-------------------------------------------------------------------------------

These are the user-facing tools that DataX feeds into. They consume libiio
(directly or via pyadi-iio) and so work with any DataX target — local,
remote, or microcontroller-based — out of the box.

**Scopy** (:external+scopy:doc:`docs <index>`) — multi-instrument GUI
(oscilloscope, spectrum analyzer, signal generator, network and logic
analyzer, pattern generator, power-supply control) with first-class
support for the ADALM2000 and ADALM1000 plus generic IIO and TinyIIO
targets. Linux, Windows, macOS.

**IIO Oscilloscope** — a leaner GUI viewer that works with any IIO device
without per-device support: real-time time / frequency plots, full sysfs
attribute access, and data logging. Linux primarily.

**MATLAB Toolboxes** — Transceiver Toolbox (AD9361, AD9371, ADRV9009,
AD9081, ...) and HSX Toolbox (AD9680, AD9144, AD9172, ...) stream data
into MATLAB workspaces and integrate with Communications Toolbox. Windows,
Linux, macOS (MATLAB 2018b or newer).

**Kuiper Linux** (:doc:`docs </linux/kuiper/index>`) — ADI's Debian-based
distribution. Pins a tested combination of every component above (ADI
kernel, libiio, pyadi-iio, Scopy, IIO Oscilloscope, GNU Radio, Jupyter
Lab) plus devicetree overlays for common boards. Targets Raspberry Pi
4/400, BeagleBone, and Xilinx Zynq via SD-card image.

See Also
-------------------------------------------------------------------------------

- :doc:`architecture` — full-stack architecture and data-flow examples
- :doc:`workflows` — concrete end-to-end scenarios
- :doc:`versioning-support` — version compatibility and release tracks
- :doc:`Software Infrastructure tutorial </learning/sw_infrastructure/index>`
- :doc:`Converter Connectivity tutorial </learning/converter_connectivity_tutorial/index>`
