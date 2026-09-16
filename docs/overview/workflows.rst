.. _overview_workflows:

Common Development Workflows
===============================================================================

This page shows concrete examples of how `ADI DataX™
<https://developer.analog.com/solutions/adi-datax>`__ components work
together in real-world development scenarios. Each workflow demonstrates a
complete path from hardware to application, illustrating which components
are used and how they integrate.

.. contents:: Contents
   :local:
   :depth: 2

Introduction
-------------------------------------------------------------------------------

ADI DataX supports five development workflows, each optimized for different
use cases:

1. **FPGA + High-Speed Data Converter** - For high-performance applications
   requiring GSPS sample rates, custom signal processing, or multiple devices

2. **Microcontroller + Precision ADC** - For cost-effective, low-power
   standalone measurement systems

3. **Raspberry Pi + Evaluation Board** - For rapid prototyping, education,
   and demonstration systems

4. **Remote Multi-Device Setup** - For centralized control of multiple
   networked boards from a host PC via IIOD

5. **Hardware-in-the-Loop Testing** - For automated testing, board bring-up,
   and design verification using ADALM2000 and libm2k

Understanding these workflows will help you choose the right approach for your
project and see how the :doc:`technology stack components <components>` fit together.

Technology Stack Deviations: Linux vs. no-OS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many ADI devices support both a Linux IIO driver and a no-OS bare-metal driver.
The same hardware — for example an AD9081 MxFE connected to a Zynq FPGA — can
be driven by either stack. The right choice depends on where you are in the
development cycle, not just on the final deployment target.

.. svg:: workflow-linux-noos.svg
   :align: center

   Linux vs. no-OS development paths: same hardware, different software stacks

Why Start with Linux
^^^^^^^^^^^^^^^^^^^^

For any device that has both a Linux IIO driver and a no-OS bare-metal
driver, prototype on Linux first. Linux drivers validate register writes
and surface errors through ``dmesg``; the libiio command-line utilities,
Scopy, and pyadi-iio all work the moment the driver loads, so you can
confirm the hardware before writing application code; and Linux's
file-write / Python-one-liner iteration loop is dramatically faster than
the rebuild-and-reflash loop a no-OS port requires. The Linux and no-OS
drivers for the same device share register maps and initialisation
sequences, so configuration validated under Linux transfers directly to
the no-OS port.

.. list-table:: Linux vs. no-OS Comparison
   :header-rows: 1
   :widths: 20 40 40

   * - Aspect
     - Linux
     - no-OS (Bare-Metal)
   * - **Best For**
     - Prototyping, validation, algorithm development
     - Production deployment, resource-constrained systems
   * - **Debuggability**
     - | ``dmesg`` for driver errors
       | ``iio_info`` / ``iio_readdev`` / Scopy
       | ``gdb``, ``strace``, ``perf``
       | Remote access via SSH + pyadi-iio
     - | UART / SWD debug console
       | JTAG step-through with IDE
       | Logic analyser on SPI/I2C bus
       | Limited compared to Linux
   * - **Strengths**
     - | - Explicit error messages and return codes
       | - Parameter validation in driver layer
       | - Direct MATLAB/Python/pyadi-iio access
       | - Faster configuration iteration
       | - Large community, extensive documentation
     - | - Minimal footprint, instant boot
       | - Deterministic real-time performance
       | - Lower power consumption
       | - No OS overhead or scheduling jitter
       | - Production-ready, self-contained firmware
   * - **Weaknesses**
     - | - Higher resource usage (RAM, CPU, storage)
       | - Non-deterministic timing due to OS scheduling
       | - Longer boot time
       | - Overkill for simple, standalone deployments
     - | - Steeper learning curve
       | - Limited runtime error checking
       | - Rebuild-and-flash loop for each change
       | - Manual host integration (TinyIIO or custom)

When to Transition to no-OS
^^^^^^^^^^^^^^^^^^^^^^^^^^^

no-OS is the right choice for the **deployed product**, not the
development process. Transition once the device is fully characterised
and configuration is stable; algorithms are validated; boot time, power
budget, or BOM cost make Linux impractical; hard real-time guarantees
are needed; or the system must operate without a network or host PC.

The recommended path: prototype under Linux with ``iio_info`` / Scopy /
pyadi-iio, lock the validated device configuration, port to the
matching no-OS reference project (driver concepts and register maps
mirror the Linux driver), validate equivalence by running the same
stimulus through both stacks, and finally optimise the no-OS firmware
for your deployment targets.


Workflow 1: FPGA + High-Speed Data Converter
-------------------------------------------------------------------------------

This workflow targets high-performance applications using Xilinx Zynq/ZynqMP
SoCs with ADI's high-speed data converters like RF transceivers or multi-GSPS
ADCs/DACs.

Use Case Example: AD9081 MxFE Software-Defined Radio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Hardware:**

- Xilinx ZCU102 (Zynq UltraScale+ MPSoC)
- AD9081-FMCA-EBZ evaluation board (Quad 12 GSPS ADC, Quad 12 GSPS DAC)
- JESD204B/C high-speed serial links (up to 15.5 Gbps per lane)

**Application:** Multi-channel wideband transceiver for communications,
radar, or test equipment.

.. svg:: workflow-fpga.svg
   :align: center

   FPGA workflow: Zynq + AD9081 MxFE via JESD204C

Architecture
~~~~~~~~~~~~

The :external+hdl:doc:`AD9081 HDL project <projects/ad9081_fmca_ebz/index>`
synthesises the JESD204 TPL/Link/PHY, DMA controllers, and clock management
into the Zynq fabric and exposes them to Linux via AXI interfaces. Linux's
``axi-ad9081`` IIO driver initialises the device over SPI, configures the
JESD204 link, programs filters / NCOs / DDCs / DUCs, and presents DMA
buffers as IIO devices. libiio (``local:`` backend) hands those off to
``adi.ad9081`` in pyadi-iio (or to MATLAB / GNU Radio / custom C/C++) for
the application code.

Development Steps
~~~~~~~~~~~~~~~~~

Mount the AD9081-FMCA-EBZ on the ZCU102 FMC connector, build the HDL
project from :external+hdl:doc:`the matching reference design
<projects/ad9081_fmca_ebz/index>`, build a Linux kernel with the
``axi-ad9081`` driver (or use :doc:`Kuiper Linux </linux/kuiper/index>`),
program the bitstream and SD-card image, boot the Zynq, and verify
``iio_info`` lists the AD9081 device. Application code then talks to it
through pyadi-iio, MATLAB, or libiio directly.

When to Use This Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose FPGA-based workflow when you need:

- **High Sample Rates:** >100 MSPS, up to 12+ GSPS
- **Low Latency:** <1 µs signal processing latency
- **Multiple Devices:** Synchronizing several converters
- **Custom Processing:** FFTs, filtering, beamforming in FPGA fabric
- **High Bandwidth:** JESD204 multi-gigabit links
- **Scalability:** Room to grow with additional logic

**Typical Applications:**

- Software-defined radio platforms
- Phased array radar systems
- 5G/6G test equipment
- Satellite communications
- Medical imaging (MRI, ultrasound)
- High-energy physics instrumentation

**Trade-offs:**

- Higher cost ($1K-$10K+ for evaluation boards)
- More complex (requires FPGA knowledge for customization)
- Higher power consumption (5-50W)
- Longer development time
- Requires specialized tools (Vivado, PetaLinux)

Reference Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Project Page:** :external+hdl:doc:`AD9081 FMCA EBZ <projects/ad9081_fmca_ebz/index>`
- **HDL User Guide:** `HDL Documentation <https://analogdevicesinc.github.io/hdl/user_guide/index.html>`_
- **Linux Driver:** `axi-ad9081 driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`_
- **Similar Projects:** :external+hdl:doc:`All HDL Projects <projects/index>`

Workflow 2: Microcontroller + Precision ADC
-------------------------------------------------------------------------------

This workflow targets cost-effective, low-power standalone measurement systems
using bare-metal microcontrollers with precision ADCs.

Use Case Example: AD4080 Precision Data Logger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Hardware:**

- ST Nucleo-H563ZI development board (STM32H563ZI MCU, ARM Cortex-M33, 250 MHz)
- EVAL-AD4080-ARDZ evaluation board (40 MSPS SAR ADC, Arduino form factor)
- SPI interface (up to 80 MHz)
- USB connection to host PC for data streaming

**Application:** Portable seismic sensor, vibration monitor, or precision
measurement instrument.

This example is based on the :doc:`Software Infrastructure Tutorial </learning/sw_infrastructure/index>`.

.. svg:: workflow-mcu.svg
   :align: center

   Microcontroller workflow: STM32 + AD4080 ADC via SPI and TinyIIO

Architecture
~~~~~~~~~~~~

The :external+no-OS:doc:`AD4080 no-OS project <index>` runs on the
STM32H563ZI: it includes the AD4080 device driver, an SPI driver against
the STM32 HAL, DMA-backed circular buffers, and a TinyIIO server speaking
over USB-CDC. There is no Linux kernel driver layer in this stack —
TinyIIO talks the IIO protocol straight over the virtual serial port. On
the host (a laptop or Raspberry Pi), libiio's ``serial:`` backend
connects to ``/dev/ttyACM0``; ``adi.ad4080`` in pyadi-iio (or Scopy /
custom scripts) handles configuration and capture.

Development Steps
~~~~~~~~~~~~~~~~~

Mount the EVAL-AD4080-ARDZ on the ST Nucleo's Arduino headers, build the
no-OS AD4080 firmware for STM32 and flash it via the on-board ST-LINK,
then connect to the device from the host with ``iio_info -u
serial:/dev/ttyACM0,230400,8n1`` and develop with Scopy or pyadi-iio. See
:doc:`Software Infrastructure </learning/sw_infrastructure/index>` for the
full hands-on walk-through.

When to Use This Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose microcontroller-based workflow when you need:

- **Low Cost:** MCU boards $10-$50, total BOM $50-$200
- **Low Power:** <1W typical, battery operation feasible
- **Standalone Operation:** No OS, boots instantly
- **Real-Time Performance:** Deterministic timing
- **Simple Deployment:** Single binary, no updates
- **Portability:** Handheld, wearable applications

**Typical Applications:**

- Portable medical devices (ECG, pulse oximetry)
- Industrial sensors (temperature, pressure, vibration)
- Data loggers (environmental monitoring)
- Precision measurement tools
- Battery-powered instrumentation
- Embedded control systems

**Trade-offs:**

- Lower sample rates (<100 MSPS typically)
- Limited processing (no FFTs, complex algorithms)
- Simpler UI (limited display options)
- Serial/USB bottleneck for data streaming
- Manual firmware updates

Reference Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Tutorial:** :doc:`Software Infrastructure Tutorial </learning/sw_infrastructure/index>`
- **no-OS Framework:** `no-OS Documentation <https://analogdevicesinc.github.io/no-OS/index.html>`_
- **AD4080 Driver:** :external+no-OS:doc:`AD4080 no-OS driver <index>`
- **Similar Designs:** :doc:`Precision ADC Reference Designs </solutions/reference-designs/index>`

Workflow 3: Raspberry Pi + Evaluation Board
-------------------------------------------------------------------------------

This workflow targets rapid prototyping, education, and demonstration using
Raspberry Pi with Arduino-compatible evaluation boards or USB devices.

Use Case Example: Multi-Sensor Data Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Hardware:**

- Raspberry Pi 4 (4 GB RAM)
- SD card with Kuiper Linux
- Multiple Arduino-shield evaluation boards (ARDZ)
- Optional: ADALM2000 USB multi-function instrument

**Application:** Educational lab setup, proof-of-concept prototyping, or
conference demonstration.

.. svg:: workflow-rpi.svg
   :align: center

   Raspberry Pi workflow: RPi + Arduino shields and USB devices

Architecture
~~~~~~~~~~~~

There is no FPGA or MCU firmware layer in this stack — the Pi talks
directly to its shields over SPI / I2C, and the kernel IIO drivers (for
``ad4080``, ``ad4052``, ``ad5592r``, ``adxl345``, the ``m2k`` context for
the ADALM2000, etc.) are already in :doc:`Kuiper Linux </linux/kuiper/index>`,
configured by devicetree overlays. libiio runs three backends side-by-side
on the same host: ``local:`` for the SPI/I2C shields, ``usb:`` for the
ADALM2000, ``ip:`` for any other networked target. pyadi-iio uses the
same device class regardless of backend, with the URI as the only
difference.

Development Steps
~~~~~~~~~~~~~~~~~

Flash :doc:`Kuiper Linux </linux/kuiper/index>` to an SD card, mount the
Arduino shields on the Pi GPIO header (enabling the devicetree overlay
for any custom configurations), and verify with ``iio_info``. From there
develop in Jupyter Lab, Python scripts, MATLAB, or Scopy.

When to Use This Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose Raspberry Pi workflow when you need:

- **Rapid Prototyping:** Get running in minutes
- **Education:** Teach data acquisition and signal processing
- **Demonstrations:** Conference booths, customer visits
- **Multi-Device Systems:** Integrate several evaluation boards
- **Familiar Environment:** Standard Linux, Python, web browsers
- **Low Barrier:** Minimal specialized knowledge required

**Typical Applications:**

- University laboratory setups
- Algorithm development and validation
- Proof-of-concept demonstrations
- Trade show exhibits
- Remote monitoring stations
- Hobbyist projects

**Trade-offs:**

- Medium sample rates (<10 MSPS typical on SPI)
- No hard real-time guarantees
- Limited I/O (shared SPI bus, limited chip selects)
- Networking dependencies for remote access
- SD card reliability concerns

Reference Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Kuiper Linux:** :doc:`Kuiper Linux Guide </linux/kuiper/index>`
- **Raspberry Pi Setup:** :ref:`linux-kernel`
- **Arduino Shields:** :doc:`Evaluation Boards </solutions/reference-designs/index>`
- **Tutorials:** :doc:`Learning Resources </learning/index>`

Workflow 4: Remote Multi-Device Setup
-------------------------------------------------------------------------------

This workflow targets centralized control of multiple embedded boards from a
host PC over a standard Ethernet network, using IIOD (IIO Daemon) as a
network bridge.

Use Case Example: Multi-Board Lab Automation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Hardware:**

- Host workstation (Linux, macOS, or Windows) with libiio installed
- Target 1: Zynq board running Kuiper Linux with AD9081 (high-speed SDR)
- Target 2: Raspberry Pi running Kuiper Linux with precision ADC shields
- Gigabit Ethernet switch

**Application:** Centralized control of physically remote or rack-mounted
instrumentation, multi-channel data collection, or distributed sensor networks.

.. svg:: workflow-remote.svg
   :align: center

   Workflow 4: Host PC accessing multiple embedded targets via IIOD over Ethernet

Architecture
~~~~~~~~~~~~

Each embedded target is a self-contained Workflow 1 or Workflow 3
deployment running ``iiod`` (the IIO daemon, listening on TCP port
30431). The host PC needs no local IIO hardware: libiio's ``ip:`` backend
connects to each remote daemon, and pyadi-iio device classes are
identical to the local case — the URI is the only thing that changes.
Scopy on the host can also point at remote targets via the same ``ip:``
URI in its connection dialog.

Development Steps
~~~~~~~~~~~~~~~~~

Stand up each embedded target as you would for the corresponding
single-target workflow. ``iiod`` is included and enabled automatically in
:doc:`Kuiper Linux </linux/kuiper/index>` (``systemctl status iiod`` to
verify). From the host, ``iio_info -u ip:<target>`` confirms the link;
develop with pyadi-iio's ``ip:`` URIs, or connect Scopy remotely.

When to Use This Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose the remote workflow when you need:

- **Multi-Board Control:** Coordinate data from several embedded platforms
- **Physical Separation:** Boards are rack-mounted, in an anechoic chamber,
  or otherwise inaccessible during operation
- **Workstation Development:** Develop on a powerful host PC while the embedded
  target runs headlessly
- **Centralized Logging:** Aggregate data streams from multiple geographically
  distributed nodes

**Typical Applications:**

- Multi-channel phased array demonstrations
- Distributed environmental or structural monitoring
- Automated test equipment (ATE) control
- Lab automation with multiple instruments
- Production-line test rigs

**Trade-offs:**

- Network latency (not suitable for tight real-time feedback loops)
- Requires IP address management and network configuration
- Firewall rules may need updating to allow TCP port 30431
- Host PC is a single point of failure for the entire setup

Reference Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **IIOD basics:** Appendix A of :doc:`Software Infrastructure Tutorial </learning/sw_infrastructure/index>`
- **libiio ip: backend:** `libiio Documentation <https://analogdevicesinc.github.io/libiio/v0.26/index.html>`_
- **Kuiper Linux (IIOD pre-installed):** :doc:`Kuiper Linux Guide </linux/kuiper/index>`
- **Workflow 1 (FPGA target setup):** See Workflow 1 above
- **Workflow 3 (RPi target setup):** See Workflow 3 above

Workflow 5: Hardware-in-the-Loop Testing
-------------------------------------------------------------------------------

This workflow uses the ADALM2000 multi-function USB instrument with the libm2k
library for automated hardware testing, board bring-up, and design verification.
Unlike the other workflows where ADALM2000 is one of many connected devices,
here it acts as the primary **test instrument** driving and measuring a
device under test (DUT).

Use Case Example: Automated Board Bring-Up with ADALM2000
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Hardware:**

- ADALM2000 (USB multi-function instrument):

  - 2-channel oscilloscope (±25V, 100 MSPS)
  - 2-channel arbitrary waveform generator (±5V, 150 MSPS)
  - Adjustable power supplies (±5V)
  - Logic analyzer (16 channels, 100 MSPS)
  - Voltmeter

- Device Under Test (DUT): ADI evaluation board or custom circuit
- Host PC (Linux, macOS, or Windows) with libm2k installed

**Application:** Scripted board bring-up verification, production test
automation, analog circuit characterization, or educational lab experiments.

.. svg:: workflow-hil.svg
   :align: center

   Workflow 5: ADALM2000 as test instrument in a hardware-in-the-loop setup

Architecture
~~~~~~~~~~~~

The ADALM2000 plugs into the host PC over USB and exposes an IIO context
through libiio's ``usb:`` backend. **libm2k** wraps that context with
instrument-level abstractions — ``AnalogIn``, ``AnalogOut``,
``PowerSupply``, ``LogicAnalyzer``, ``Voltmeter`` — so test code drives
stimulus and reads measurements through the same library. Bindings are
available for Python, C++, C#, LabVIEW, and MATLAB; ``pytest`` /
``unittest`` are the usual harness for assembling pass / fail criteria,
reports, and CI integration.

Development Steps
~~~~~~~~~~~~~~~~~

Install libm2k (``pip install libm2k`` or build from source), wire the
ADALM2000 to the DUT, verify with ``iio_info -u usb:``, and write a
script that combines stimulus and measurement. Examples and a full
quick-start are in the :doc:`libm2k documentation </software/libm2k/index>`.

When to Use This Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose hardware-in-the-loop testing when you need:

- **Automated Bring-Up:** Scripted power-on verification without manual probing
- **Stimulus + Measurement:** Generate known signals and measure DUT response
  in the same script
- **Regression Testing:** Catch analog regressions in CI before hardware ships
- **Production Testing:** Repeatable pass/fail tests on every board

**Typical Applications:**

- Board bring-up and factory acceptance tests
- Frequency response and distortion measurements
- Power supply sequencing validation
- Educational labs requiring signal injection
- Design verification for ADI evaluation boards

**Trade-offs:**

- ADALM2000 bandwidth limited to 25 MHz (not suitable for RF; use ADALM-PLUTO instead)
- USB bandwidth constrains continuous streaming rates
- libm2k API differs from libiio/pyadi-iio (separate programming model)
- Requires host PC — not a standalone embedded solution

Reference Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **libm2k:** :doc:`libm2k Documentation </software/libm2k/index>`
- **ADALM2000:** `ADALM2000 Wiki <https://wiki.analog.com/university/tools/m2k>`_
- **libm2k GitHub:** `github.com/analogdevicesinc/libm2k <https://github.com/analogdevicesinc/libm2k>`_
- **Scopy (GUI for ADALM2000):** :external+scopy:doc:`Scopy Documentation <index>`

Choosing the Right Workflow
-------------------------------------------------------------------------------

Quick Decision Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The table below compares the three **platform workflows** (1–3). Workflows 4
(Remote) and 5 (HIL Testing) are complementary to any of these — see the note
after the table.

.. list-table::
   :header-rows: 1
   :widths: 30 25 25 20

   * - Your Requirement
     - Workflow 1 (FPGA)
     - Workflow 2 (MCU)
     - Workflow 3 (RPi)
   * - Sample Rate > 100 MSPS
     - ✅ Yes
     - ❌ No
     - ❌ No
   * - Custom Signal Processing
     - ✅ FPGA fabric
     - ⚠️ Limited
     - ⚠️ Software only
   * - Low Power (<1W)
     - ❌ No
     - ✅ Yes
     - ⚠️ ~5W
   * - Low Cost (<$100)
     - ❌ No ($1K+)
     - ✅ Yes
     - ✅ Yes
   * - Rapid Prototyping
     - ❌ Weeks
     - ⚠️ Days
     - ✅ Hours
   * - Standalone Operation
     - ⚠️ Possible
     - ✅ Yes
     - ❌ Needs OS
   * - Python/MATLAB Support
     - ✅ Yes
     - ✅ Yes (via serial)
     - ✅ Yes (native)
   * - GUI Applications
     - ✅ Via network
     - ✅ Via serial
     - ✅ Native
   * - Learning Curve
     - ⚠️ Steep
     - ⚠️ Moderate
     - ✅ Easy

Workflows 4 and 5 are complementary to the three platform workflows above.
**Workflow 4** (Remote) can be layered on top of Workflows 1–3: once a board
is running Linux with IIOD, any libiio ``ip:`` client can talk to it.
**Workflow 5** (HIL Testing) is independent — use it when you need automated
stimulus and measurement, regardless of which primary workflow your DUT uses.

Migration Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The layered architecture enables smooth migration between workflows:

**Prototype → Production:**

1. Start with **Workflow 3** (Raspberry Pi) for proof of concept
2. Validate algorithms and user requirements
3. Move to **Workflow 2** (MCU) for cost reduction and standalone operation
4. Or move to **Workflow 1** (FPGA) for performance scaling

**The application code (Layers 5-7) remains largely unchanged**, just switch the
libiio URI.

**Development → Deployment:**

- Develop on desktop with ``ip:`` backend (remote Zynq/RPi via Workflow 4)
- Deploy same code on embedded Zynq with ``local:`` backend
- No code changes needed beyond URI configuration

See Also
-------------------------------------------------------------------------------

**Next Steps:**

- :doc:`components` - Detailed component documentation
- :doc:`versioning-support` - Version compatibility for your chosen workflow
- :doc:`architecture` - Understanding the layered architecture

**Learning Resources:**

- :doc:`Software Infrastructure Tutorial </learning/sw_infrastructure/index>` - Workflow 2 hands-on
- :doc:`FPGA Integration Journey </learning/workshop_a_precision_converter_fpga_integration_journey/index>` - Workflow 1 deep dive
- :doc:`Kuiper Linux Guide </linux/kuiper/index>` - Workflow 3 setup

**Reference Designs:**

- :external+hdl:doc:`HDL Projects <projects/index>` - FPGA designs (Workflow 1)
- :external+no-OS:doc:`no-OS Projects <index>` - MCU firmware (Workflow 2)
- :doc:`Evaluation Boards </solutions/reference-designs/index>` - Arduino shields (Workflow 3)
