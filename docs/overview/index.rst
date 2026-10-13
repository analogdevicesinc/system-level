.. _overview:

Ecosystem Overview
===============================================================================

Welcome to the ADI System Level Documentation ecosystem overview. This section
provides a high-level introduction to how Analog Devices' prototyping software
and HDL components work together to help you bring your designs from concept to
reality.

.. contents:: Contents
   :local:
   :depth: 2

Introduction
-------------------------------------------------------------------------------

Analog Devices provides a comprehensive ecosystem of hardware, HDL (Hardware
Description Language) reference designs, software drivers, libraries, and
applications to accelerate your development process. Whether you're building a
high-speed FPGA-based data acquisition system, a precision embedded measurement
device, or a prototyping platform on a Raspberry Pi, the ADI ecosystem provides
the building blocks you need.

The Integrated System Approach
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the heart of the ADI approach is an **integrated system philosophy**: we surround
your processor, FPGA, or microcontroller with best-in-class ADI analog and mixed-signal
components, along with all the software and HDL support needed to make them work
seamlessly together.

Rather than reinventing the wheel, we leverage established ecosystems:

- **Linux Kernel** for OS-based systems
- **GitHub** for open-source collaboration
- **Python** and **MATLAB** for rapid prototyping
- **IIO (Industrial I/O)** framework for standardized device interfaces
- **Standard FPGA toolchains** (Vivado, Quartus) for HDL development

This approach means you can focus on your application logic and signal processing
while relying on proven, tested infrastructure for interfacing with ADI devices.

What the Ecosystem Provides
-------------------------------------------------------------------------------

The ADI ecosystem spans seven layers, from hardware to high-level applications:

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

Who Should Read This
-------------------------------------------------------------------------------

This overview is designed for:

- **Engineers new to ADI's ecosystem** who want to understand how the pieces fit together
- **Experienced developers** looking for the right starting point for their project
- **System architects** evaluating ADI solutions for their designs
- **Students and researchers** learning about mixed-signal system development

If you're looking for detailed implementation guides, jump directly to the
specific component documentation linked throughout this overview.

What You'll Learn
-------------------------------------------------------------------------------

This overview covers:

.. toctree::
   :maxdepth: 1

   architecture
   components
   workflows
   versioning-support

**Architecture** explains the full-stack architecture and design philosophy,
showing how data flows from hardware through HDL, drivers, libraries, and
applications. Includes detailed diagrams of ecosystem interdependencies,
demonstrating how HDL serves as a common foundation for both FPGA (Linux)
and microcontroller (no-OS) paths, with host tools working uniformly across
both through libiio.

**Components** provides detailed information about each major ecosystem component:
HDL, Linux kernel drivers, libiio, no-OS, pyadi-iio, and applications.

**Workflows** shows concrete examples of how components work together in
real-world scenarios: FPGA-based high-speed systems, microcontroller precision
measurement, Raspberry Pi prototyping, remote multi-device setups via IIOD,
and hardware-in-the-loop testing with ADALM2000.

**Versioning & Support** explains how versioning works across components, which
versions work together, and where to get help.

Quick Navigation
-------------------------------------------------------------------------------

Already know what you're looking for? Jump directly to:

**By Component:**

- :doc:`HDL Reference Designs </overview/components>` - FPGA IP cores and reference projects
- :doc:`Linux Kernel Support </overview/components>` - IIO drivers and devicetree
- :doc:`libiio Library </overview/components>` - Hardware abstraction and backends
- :doc:`no-OS Firmware </overview/components>` - Bare-metal microcontroller support
- :doc:`Python Interfaces </overview/components>` - pyadi-iio device classes

**By Use Case:**

- :doc:`FPGA + High-Speed Data Converter </overview/workflows>` - Zynq/ZynqMP with transceivers
- :doc:`Microcontroller + Precision ADC </overview/workflows>` - STM32/MAX32 with SAR/Sigma-Delta ADCs
- :doc:`Raspberry Pi Prototyping </overview/workflows>` - Arduino shields and USB devices
- :doc:`Remote Multi-Device Setup </overview/workflows>` - IIOD networking across multiple boards
- :doc:`Hardware-in-the-Loop Testing </overview/workflows>` - ADALM2000 for automated test and bring-up

**By Topic:**

- :doc:`Version Compatibility </overview/versioning-support>` - Which versions work together
- :doc:`Support Channels </overview/versioning-support>` - Where to get help

Next Steps
-------------------------------------------------------------------------------

**New to the ecosystem?**

1. Read :doc:`architecture` to understand the full-stack approach
2. Review :doc:`components` to learn about each building block
3. Choose a :doc:`workflow <workflows>` that matches your project
4. Follow the hands-on tutorials in the :doc:`Learning </learning/index>` section

**Ready to build?**

- Browse :doc:`Reference Designs </solutions/reference-designs/index>` for your hardware
- Check :doc:`version compatibility </overview/versioning-support>` for your platform
- Set up your development environment with :doc:`Kuiper Linux </linux/kuiper/index>`
- Explore :doc:`Software Tools </software/index>` for your preferred language

**Need help?**

- Search the `EngineerZone Forums <https://ez.analog.com/>`_
- Review the `ADI Wiki <https://wiki.analog.com/>`_
- Open issues on `GitHub repositories <https://github.com/analogdevicesinc/>`_
- Check product datasheets and application notes

See Also
-------------------------------------------------------------------------------

**External Documentation:**

- `HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/index.html>`_ - Complete HDL reference
- `Linux Kernel Drivers <https://wiki.analog.com/resources/tools-software/linux-drivers-all>`_ - Driver documentation
- `Linux Getting Started <https://analogdevicesinc.github.io/linux/getting_started.html>`_ - Kernel build guides
- `libiio Documentation <https://analogdevicesinc.github.io/libiio/v0.26/index.html>`_ - Library API reference
- `no-OS Documentation <https://analogdevicesinc.github.io/no-OS/index.html>`_ - Firmware framework

**Internal Learning Resources:**

- :doc:`Software Infrastructure Tutorial </learning/sw_infrastructure/index>` - Hands-on workshop with AD4080
- :doc:`FPGA Integration Journey </learning/workshop_a_precision_converter_fpga_integration_journey/index>` - Complete FPGA workflow
- :doc:`Converter Connectivity Tutorial </learning/converter_connectivity_tutorial/index>` - IIO framework introduction
