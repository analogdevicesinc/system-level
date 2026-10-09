.. collection:: EVAL-AD4060/AD4062-ARDZ
   :subtitle: Evaluating the AD4060/AD4062 Compact, Low Power, 12-Bit/16-Bit, 2 MSPS Easy Drive SAR ADCs
   :image: eval-angle.png
   :label: eval user-guide

   system-level:
     - User guide <.>

   hdl:
     - HDL Project (ad4062_ardz) <projects/ad4062_ardz/index>

   no-OS:
     - no-OS driver (ad405x) <drivers/adc/ad405x>

.. .. custom-doc:: doc.yml

.. _eval-ad4062-ardz:

EVAL-AD4060/AD4062-ARDZ
=======================

Compact, Low Power, 12-Bit/16-Bit, 2 MSPS Easy Drive SAR ADCs.

.. figure:: eval-angle.png
   :align: right
   :width: 300

The :adi:`EVAL-AD4060-ARDZ` and :adi:`EVAL-AD4062-ARDZ` evaluation boards enable
quick and easy evaluation of the performance and features of the
:adi:`AD4060` or the :adi:`AD4062`, respectively.

The AD4060 and AD4062 are compact, low power, 12-bit or 16-bit (respectively)
Easy Drive successive approximation register (SAR) analog-to-digital converters
(ADCs) featuring an I3C digital interface. These devices offer exceptional
performance with sample rates up to 2 MSPS while maintaining low power consumption,
making them ideal for battery-powered precision measurement and monitoring applications.

The evaluation boards are designed to conform to the Arduino Uno Shield mechanical
and electrical standard, enabling easy integration with various controller boards
and development platforms.

Overview
--------

This section provides a general overview of the evaluation board, all supported
carriers, firmware options, and software tools.

The evaluation boards support multiple carrier platforms for both bare-metal
(no-OS) and Linux environments:

.. list-table::

   * - Carrier
     - no-OS
     - Linux
   * - NUCLEO-H503RB
     - ✓
     -
   * - NUCLEO-H563ZI
     - ✓
     -
   * - Cora Z7S
     -
     - ✓
   * - DE10-Nano
     -
     - ✓

Features
~~~~~~~~

**Evaluation Board Hardware:**

* Full-featured evaluation board for the :adi:`AD4060` (12-bit) and :adi:`AD4062` (16-bit)
* USB power solution via carrier board
* Single differential analog input with common-mode voltage control
* SMA connectors for precision signal input
* On-board :adi:`MAX6070` 2.5V voltage reference
* :adi:`MAX44260` low-power op amps for signal buffering
* :adi:`ADP7118` 3.3V LDO regulator
* Arduino Uno Shield compatible form factor

**Digital Interface (I3C):**

* I3C digital interface for low-pin-count, high-speed communication
* Support for multiple devices on a single I3C bus (up to 8 AD4060/AD4062s)
* Two programmable GPIOs (GP0, GP1) with multiple functions:

  - Data Ready (RDY) signal
  - Threshold interrupt output
  - Device enable (DEV_EN) for AFE power cycling
  - General-purpose outputs (Linux only)

**Software Features:**

* **no-OS (bare-metal):**

  - TinyIIO support for :ref:`libiio` connectivity
  - Two channel modes: standard ADC and burst averaging
  - Configurable sample rates and averaging
  - Serial UART communication with host PC

* **Linux IIO:**

  - IIO subsystem integration
  - Hardware-triggered buffered data acquisition
  - Autonomous threshold event monitoring
  - GPIO controller support
  - Automatic low-power mode management
  - Burst averaging with up to 2048x oversampling (AD4062)

* **GUI Applications:**

  - :ref:`iio-oscilloscope` for waveform visualization and FFT analysis
  - :external+scopy:doc:`Scopy <index>` for advanced signal analysis
  - Real-time data capture and export

* **Language Bindings:**

  - Python support via :external+pyadi-iio:doc:`pyadi-iio <index>`
  - C/C++ support via :ref:`libiio`

Evaluation board kit contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* EVAL-AD4060-ARDZ or EVAL-AD4062-ARDZ evaluation board

Equipment needed
~~~~~~~~~~~~~~~~~

* Host PC (Windows, Linux, or macOS)
* One of the supported carrier boards:

  - STM32 Nucleo board for no-OS evaluation
  - Cora Z7S or DE10-Nano for Linux evaluation

* Precision signal source with SMA cable
* USB cable for carrier connection

Hardware
~~~~~~~~

The evaluation board connects to the Arduino Uno compatible headers of the
carrier board, providing both power and digital communication.

**Power Configuration:**

When powering from the carrier USB:

* Set JP2 jumper on the evaluation board to the **+5V** position
* Connect carrier to PC via USB
* The DS1 LED on the evaluation board should illuminate

When using an external power supply:

* Set JP2 jumper on the evaluation board to the **VIN** position
* Provide 7-12V DC to the carrier's external power input
* Connect carrier to PC via USB for communication
* The DS1 LED on the evaluation board should illuminate

**I3C Address Configuration:**

The evaluation board includes jumpers JP10, JP11, and JP12 to configure the
I3C device address via ADDR[2:0] pins. Default firmware requires all address
pins set to GND (ADDR[2:0] = 000).

For detailed hardware specifications, schematics, and board layout, see the
:adi:`EVAL-AD4060-ARDZ` and :adi:`EVAL-AD4062-ARDZ` product pages, including
the :adi:`user guide <media/en/technical-documentation/user-guides/eval-ad4060_ad4062.pdf>`
and design support files.

Overview
--------

This section summarizes all source code and related documentation for the
evaluation board.

Working with the source code requires prior knowledge of software development
and HDL design (for FPGA-based carriers). We provide pointers to introductory
guides, though their scope is limited to topics particularly relevant to our
codebase and do not replace the full documentation of the tools used.

Drivers
~~~~~~~

The driver source code is available at:

.. list-table::

   * - Firmware
     - Device Support
     - Source code
     - Documentation
   * - no-OS
     - AD4050/AD4052/AD4056/AD4058/AD4060/AD4062 (SPI & I3C)
     - :git-no-OS:`drivers/adc/ad405x`
     - :external+no-OS:doc:`doc <drivers/adc/ad405x>`
   * - Linux
     - AD4060/4062 (I3C only)
     - :git-linux:`drivers/iio/adc/ad4062.c`
     - :git-linux:`doc <Documentation/iio/ad4062.rst>`

.. note::

   The Linux driver is currently under review for upstream inclusion in the
   mainline kernel. See the `patch series on linux-iio
   <https://lore.kernel.org/linux-iio/20251227163506.2fb90815@jic23-huawei/>`__
   mailing list for the latest status.

**Driver Architecture:**

* **no-OS:** The driver is divided into a core driver (device control) and a
  TinyIIO layer (IIO interface for :ref:`libiio` connectivity over serial).
  The core driver supports both SPI (AD405x) and I3C (AD406x) variants.

* **Linux:** The driver is integrated into the IIO subsystem and always exposes
  the device via :ref:`iio`. It provides full support for IIO triggers, events,
  buffers, and GPIO control.

HDL reference design
~~~~~~~~~~~~~~~~~~~~

The FPGA-based carriers (Cora Z7S, DE10-Nano) use an HDL design to instantiate
the I3C controller and interface with the evaluation board.

**Project source:**

* Source code: :git-hdl:`projects/ad4062_ardz`
* Documentation: :external+hdl:ref:`ad4062_ardz`

**Features:**

* I3C controller with offload support\*
* PWM generator for periodic sampling
* Integration with the :external+hdl:doc:`index` framework
* AXI DMA for high-throughput data capture

Get started with the HDL reference design by reading the :external+hdl:ref:`user_guide`.

\* Offload is not supported by the Linux driver.

Design files
~~~~~~~~~~~~

* :adi:`eval-ad4062-ardz <media/en/evaluation-documentation/evaluation-design-files/eval-ad4062-ardz-design-support-files.zip>`
* :adi:`eval-ad4060-ardz <media/en/evaluation-documentation/evaluation-design-files/eval-ad4060-ardz-design-support-files.zip>`

User Guides
-----------

This section is for everyone using the evaluation board. It provides step-by-step
instructions on hardware setup, firmware building and flashing, and interacting
with the device using various software tools.

.. toctree::
   :caption: The following user guides are available:
   :titlesonly:
   :glob:

   user-guide/*
   tools


Help and Support
----------------

For questions and more information, please visit:

* :ez:`EngineerZone Support Community <reference-designs>`
* :adi:`AD4060 Product Page <AD4060>`
* :adi:`AD4062 Product Page <AD4062>`

.. esd-warning::
