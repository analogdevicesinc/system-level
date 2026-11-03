.. collection:: EVAL-AD4050/AD4052-ARDZ
   :subtitle: Evaluating the AD4050/AD4052 Compact, Low Power, 12-Bit/16-Bit, 2 MSPS Easy Drive SAR ADCs
   :image: eval-angle.png
   :label: eval user-guide

   system-level:
     - User guide <.>

   hdl:
     - HDL Project (ad4052_ardz) <projects/ad4052_ardz/index>

   no-OS:
     - no-OS driver (ad405x) <drivers/adc/ad405x>

.. _eval-ad4052-ardz:

EVAL-AD4050/AD4052-ARDZ
=======================

Compact, Low Power, 12-Bit/16-Bit, 2 MSPS Easy Drive SAR ADCs.

.. figure:: eval-angle.png
   :align: right
   :width: 400

The :adi:`EVAL-AD4050-ARDZ` and :adi:`EVAL-AD4052-ARDZ` evaluation boards enable
quick and easy evaluation of the performance and features of the
:adi:`AD4050` or the :adi:`AD4052`, respectively.
The AD4050 and AD4052 are compact, low power, 12-bit or 16-bit (respectively)
Easy Drive successive approximation register (SAR)
analog-to-digital converters (ADCs).

The evaluations board are designed to conform to the Arduino Uno Shield mechanical
and electrical standard.

Overview
--------

This section provides a general overview on the evaluation board, all supported
carriers, firmware and software.

The following carriers are supported, followed by the target firmware:

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
   * - SDP-K1 [#]_
     - ✓
     -

.. [#] The SDP-K1 uses the :external+precision-converters-firmware:doc:`index` or
       the :adi:`closed-source <media/en/technical-documentation/user-guides/eval-ad4050-ad4052-ug-2222.pdf#unique_6>`
       project instead of a no-OS project.

Features
~~~~~~~~

* Full featured evaluation boards for the :adi:`AD4050` and :adi:`AD4052` with
  a USB power solution.
* Single differential channel and common-mode input available through SMA
  connectors.
* PC software (ACE plugin/:ref:`iio-oscilloscope`) for control and data analysis
  of the time and frequency domains.
* Compatible with other Arduino form factor controller boards.

Evaluation board kit contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* EVAL-AD4050-ARDZ/EVAL-AD4052-ARDZ evaluation board.

Equipment needed
~~~~~~~~~~~~~~~~~

* Host PC.
* One of the supported carriers.
* Precision signal source with SMA cable.

Hardware
~~~~~~~~

The evaluation board is connected to the Arduino Uno compatible headers of the
carrier.

When powering from the carrier, ensure the JP2 jumper is to the +5V position and
power on the carrier board.

When powering from an external power supply, ensure the JP2 jumper is set to the
VIN position, power on the carrier board, and provide power to VIN
(according to the carrier board user guide).

For more information about hardware specifications, see the
:adi:`EVAL-AD4050-ARDZ`/:adi:`EVAL-AD4052-ARDZ`
evaluation board pages, in particular, the user guide
and design support files.

User Guides
-----------

This chapter is aimed to everyone using the evaluation board.
It provides instructions on bringing-up the evaluation board with pre-built
binaries for supported carries, and how to interact with it.

.. toctree::
   :titlesonly:
   :glob:

   *

Developers
----------

This chapter summarizes all source code and related documentation of the
evaluation board.

To work with the source code, you should have prior knowledge on software
development and HDL design (for the FPGA).
We provide pointers to introductory guides, although their scope is limited to
topics that particularly relate to our codebase and do not replace the full
documentation of the tools used.

Drivers
~~~~~~~

The drivers source code are available at:

.. list-table::

   * - Firmware
     - Source code
     - Documentation
   * - no-OS
     - :git-no-OS:`drivers/adc/ad405x`
     - :external+no-OS:doc:`doc <drivers/adc/ad405x>`
   * - Linux
     - :git-linux:`staging/xlnx/main/ad4052:drivers/iio/adc/ad4052.c`
     - -

The no-OS driver is divided into a core driver and a tinyIIO layer to be used
with :ref:`libiio`.
The Linux driver is always exposed via the :ref:`iio`.

To get started with no-OS drivers, checkout :external+no-OS:doc:`drivers_guide`,
and for Linux drivers the :ref:`linux-kernel` page.

Projects
~~~~~~~~

The source code for baremetal projects can be found at:

.. list-table::

   * - Carrier
     - Firmware
     - Project
     - Documentation
   * - NUCLEO-H503RB
     - no-OS
     - :git-no-OS:`projects/ad405x`
     - :external+no-OS:doc:`docs <projects/adc/ad405x>`
   * - NUCLEO-H563ZI
     - no-OS
     - :git-no-OS:`projects/ad405x`
     - :external+no-OS:doc:`docs <projects/adc/ad405x>`
   * - SDP-K1
     - precision-converters-firmware
     - :git-precision-converters-firmware:`projects/ad405x_iio`
     - :external+precision-converters-firmware:doc:`docs <source/projects/ad405x_iio/ad405x_iio>`
   * - CoraZ7S
     - Linux
     - \-
     - \-
   * - DE10-Nano
     - Linux
     - \-
     - \-

For the no-OS project, the basic examples use only the core driver, while the
iio example uses the tinyIIO layer to expose the device to :ref:`libiio`.

The precision-converters-firmware project also expose the device to :ref:`libiio`,
differentiating only on the target carrier.

Since the Linux driver exposes the device via the :ref:`iio`, no project is
required to leverage the device on Linux targets
(CoraZ7S and DE10-Nano).

Follow :dokuwiki:`no-OS projects <resources/no-os/build>` and
:external+precision-converters-firmware:doc:`precision-converters-firmware projects <source/build/project_build>`
to comprehend the project structure for each.

Linux devicetrees
~~~~~~~~~~~~~~~~~

For the carriers targeting Linux, the devicetrees are available at:

.. list-table::

   * - Carrier
     - Devicetree
   * - Cora Z7S
     - :git-linux:`zynq-coraz7s-ad4052.dts <staging/xlnx/main/ad4052:arch/arm/boot/dts/xilinx/zynq-coraz7s-ad4052.dts>`
   * - DE10-Nano
     - \-

HDL reference design
~~~~~~~~~~~~~~~~~~~~

The DE10-Nano and Cora Z7s use the FPGA to instantiate the controllers to
interface the evaluation board.

The source code is available at
:git-hdl:`projects/ad4052_ardz`
and documented at
:external+hdl:ref:`ad4052_ardz`.

Get start with the HDL reference design reading the :external+hdl:ref:`user_guide`.

Software & Bindings
~~~~~~~~~~~~~~~~~~~

Using any IIO or TinyIIO driver layer, the device can be interacted through
:ref:`libiio`, language bindings on top of libiio and the :ref:`iio-oscilloscope`
GUI.

For the Python language a class abstraction of the device is available at
:git-pyadi-iio:`adi/ad405x.py`
(:external+pyadi-iio:doc:`class doc <devices/adi.ad405x>`),
with an example at
:git-pyadi-iio:`examples/ad4052_example.py`

Help and Support
----------------

For questions and more information, please visit the
:ez:`EngineerZone Support Community <reference-designs>`.

.. esd-warning::
