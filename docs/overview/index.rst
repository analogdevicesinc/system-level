.. _overview:

ADI DataX Overview
===============================================================================

Welcome to the overview of `ADI DataX™
<https://developer.analog.com/solutions/adi-datax>`__, Analog Devices' open,
multi-platform technology stack that connects ADI signal chains to your
application across processing platforms, operating systems, and software
ecosystems. This section is a high-level introduction to how the pieces fit
together so you can bring your designs from concept to reality.

.. contents:: Contents
   :local:
   :depth: 2

Introduction
-------------------------------------------------------------------------------

ADI DataX is an umbrella for the HDL reference designs, drivers (Linux,
Zephyr, no-OS), the libiio library and its companion daemon (``iiod`` /
``tinyiiod``), language bindings such as pyadi-iio, and distributions like
Kuiper Linux that ADI publishes to make its hardware easy to integrate.
Whether you're building a high-speed FPGA-based data acquisition system, a
precision embedded measurement device, or a prototyping platform on a
Raspberry Pi, ADI DataX provides the building blocks you need.

The diagram below — from the
`ADI DataX landing page <https://developer.analog.com/solutions/adi-datax>`__ —
summarises what DataX covers. The three blue layers in the middle are what
DataX provides; everything above and below them is your application and the
physical signal chain you connect it to:

.. svg:: datax-stack.svg
   :align: center

   ADI DataX layers the software stack between your signal chain and your
   application.

Reading the diagram from the bottom up:

- **Physical World** — the analog signal chain plus any edge compute platform
  (FPGA, MCU/SoC, APU) running the DataX stack.
- **Hardware Abstraction Layer** — a thin layer that normalises access to the
  hardware: FPGA IP, the Linux IIO subsystem, Zephyr's device APIs, and the
  no-OS Common API. This is what lets the same higher-level driver code run
  on very different platforms.
- **ADI Device Drivers** — drivers for the actual ADI parts. Linux ships with
  more than 1,500 ADI drivers (running on application processors); Zephyr and
  no-OS together cover 600+ parts on microcontrollers and SoCs.
- **Application API** — a single, platform-independent C API in libiio with
  bindings throughout the broader ecosystem: pyadi-iio (Python), MATLAB, ROS 2,
  Nvidia toolsets, GNU Radio, and more.
- **Application** — your code. Because the API is the same regardless of where
  the device lives or what runs the drivers, the same script that talks to a
  USB instrument on a laptop can talk to an FPGA-attached transceiver on a
  Zynq board.

The Integrated System Approach
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the heart of ADI DataX is an **integrated system philosophy**: ADI surrounds
your processor, FPGA, or microcontroller with best-in-class ADI analog and
mixed-signal components, plus the software and HDL support needed to make them
work together. DataX integrates with the ecosystems engineers already use —
the Linux kernel, the IIO subsystem, Python and MATLAB, GitHub, and the
standard FPGA toolchains — rather than asking you to adopt proprietary
infrastructure.

What ADI DataX Provides
-------------------------------------------------------------------------------

ADI DataX spans seven layers, from hardware to high-level applications:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Layer
     - Description
   * - **Hardware**
     - ADI devices (ADCs, DACs, transceivers, sensors, IMUs, PLLs, DDS, etc.)
   * - **Interface**
     - FPGA, processor, or microcontroller platforms (Zynq, ZynqMP, Versal,
       Raspberry Pi, STM32, MAX32, etc.)
   * - **HDL/Firmware**
     - FPGA reference designs with IP cores (JESD204, SPI Engine, DMA controllers)
       and bare-metal firmware for microcontrollers
   * - **Drivers**
     - Linux IIO kernel drivers, Zephyr drivers, devicetree support
   * - **Libraries**
     - Hardware abstraction libraries (libiio, libm2k)
   * - **Language Bindings**
     - Python (pyadi-iio), MATLAB toolboxes, C/C++ APIs
   * - **Applications**
     - GUI tools (Scopy, IIO Oscilloscope), Linux distributions (Kuiper Linux)

Each layer builds on the one below it, creating a complete path from silicon to
software application.

In This Section
-------------------------------------------------------------------------------

.. toctree::
   :hidden:
   :maxdepth: 1

   architecture
   components
   layer-interactions
   workflows
   versioning-support

- :doc:`architecture` — the seven-layer model and how data flows through it,
  with a focus on how HDL, drivers, libiio, and language bindings depend on
  each other.
- :doc:`components` — what each DataX component is, when to use it, and where
  to find its full documentation.
- :doc:`workflows` — five end-to-end scenarios (FPGA + high-speed converter,
  MCU + precision ADC, Raspberry Pi, remote multi-device via IIOD,
  hardware-in-the-loop) showing how the components combine.
- :doc:`versioning-support` — release tracks, which component versions work
  together, and where to get help.

Pick a workflow first if you already know your hardware shape; otherwise read
:doc:`architecture` for the full picture, then drill into :doc:`components`.

See Also
-------------------------------------------------------------------------------

- :doc:`Reference Designs </solutions/reference-designs/index>` — board-level
  starting points
- :doc:`Kuiper Linux </linux/kuiper/index>` — pre-configured Linux
  distribution that bundles a tested DataX combination
- :doc:`Learning </learning/index>` — hands-on tutorials and workshops
- `EngineerZone <https://ez.analog.com/>`_ — community support forums
