.. _eval-ad5529r-ardz prerequisites:

Prerequisites
=============

This section lists the hardware and software prerequisites required to
evaluate the :adi:`AD5529R` using the :adi:`EVAL-AD5529R-ARDZ` evaluation board.

Hardware Prerequisites
----------------------

**Required:**

- :adi:`EVAL-AD5529R-ARDZ` evaluation board
- `Cora Z7-07S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development/>`_
  carrier board
- MicroSD card (8 GB or larger, Class 10 recommended)
- Micro-USB cable for UART console access
- 5V/2A power supply for the Cora Z7 (if not using USB power)

.. TODO:: Verify power supply requirements for eval board

**Optional (for verification and debugging):**

- Oscilloscope for output waveform verification
- Digital multimeter (DMM) for DC voltage measurements
- Logic analyzer for SPI bus debugging

Software Prerequisites
----------------------

- **Option A: Kuiper Linux SD Card Image (Recommended)**

    Download the :external+kuiper:doc:`index` image with AD5529R support

- **Option B: Individual Boot Files**

    If building from source, you need:

    - ``BOOT.BIN`` - First Stage Boot Loader (FSBL) + FPGA bitstream
    - ``uImage`` - Linux kernel image
    - ``devicetree.dtb`` - Device tree blob for AD5529R + Cora Z7

    .. TODO:: Add links to pre-built boot files when available

    Build instructions:

     - :external+hdl:ref:`build_hdl`
     - :ref:`linux-kernel zynq`

Tools Required
--------------

**IIO Oscilloscope (GUI)**

The IIO Oscilloscope provides a graphical interface for controlling the DAC
channels and monitoring device attributes.

- :git-iio-oscilloscope:`IIO Oscilloscope Repository </>`
- :ref:`iio-oscilloscope`

**UART Terminal**

A serial terminal for console access during boot and debugging:

- **Windows**: `PuTTY <https://www.putty.org/>`_ or Tera Term
- **Linux/macOS**: ``minicom``, ``screen``, or ``picocom``

**Serial port settings:**

.. code-block:: text

   Baud rate: 115200
   Data bits: 8
   Stop bits: 1
   Parity: None
   Flow control: None

**PyADI-IIO (Python Scripting)**

Python library for programmatic DAC control:

- :git-pyadi-iio:`PyADI-IIO Repository </>`
- :ref:`PyADI-IIO Documentation <pyadi-iio>`

Installation:

.. code-block:: bash

   pip install pyadi-iio

**IIO Command-Line Tools**

For low-level device interaction:

- ``iio_info`` - List available IIO devices and attributes
- ``iio_attr`` - Read/write device and channel attributes
- ``iio_reg`` - Direct register access

These tools are included in the :git-libiio:`libiio </>` package.
