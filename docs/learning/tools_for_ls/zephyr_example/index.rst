.. _datax-zephyr-example:

RTOS Support: Zephyr
------------------------

.. note::

   This is a work in progress.

The previous sections ran the curve tracer two ways on the MAX32666FTHR: as a
**tinyiiod server** driven by a script on the PC, and as a **standalone no-OS
application** that does all of the work on the board. In this section we do
both again, this time on `Zephyr <https://zephyrproject.org/>`__, an
open-source real-time operating system that already knows about the
ADALM-LSMSPG and the MAX32666FTHR.

Two variants are covered:

- **Variant A** builds a small Zephyr application that runs the curve tracer
  on the FTHR. You start a sweep by typing ``curvetrace`` in the Zephyr shell,
  and the results are printed as an ASCII-art plot on the serial console.
- **Variant B** builds the Zephyr IIO server, which exposes the AD5592r,
  AD5593r and LM75 as IIO devices over USB serial. The same
  ``ad5592r_curve_tracer.py`` pyadi-iio script used on the Raspberry Pi then
  drives the sweep from the PC.

.. note::

   Nothing in this section needs board-specific code. The ADALM-LSMSPG is an
   official Zephyr shield (``adi_lsmspg``), so the AD5592r, AD5593r and LM75
   drivers, the SPI and I2C buses and the pin assignments all come from the
   Zephyr tree. The applications only refer to the shield's devices by name.

Hardware Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

In addition to the ADALM-LSMSPG board, you will need:

- **MAX32666FTHR** Feather development board
- **MAX32625PICO** DAPLink debug adapter (supplied with the MAX32666FTHR)
- Two Micro USB cables: one for the MAX32666FTHR, one for the MAX32625PICO

Software Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

For both variants:

- A Zephyr development environment: Python 3, ``west`` and the Zephyr SDK.
  Follow the
  `Zephyr Getting Started Guide <https://docs.zephyrproject.org/latest/develop/getting_started/index.html>`__
  up to (but not including) the step that downloads the Zephyr source; the
  workspace is created in Step 1 below.
- A serial terminal, such as **PuTTY** or the serial monitor of VS Code.

For Variant B only:

- **libiio v1** on the PC, from the
  `libiio v1.0.0 release <https://github.com/analogdevicesinc/libiio/releases/tag/v1.0.0>`__
  (on Windows, unzip ``Windows.zip`` and add the folder that contains
  ``libiio1.dll``, ``iio_info.exe`` and ``iio_attr.exe`` to your ``PATH``).

  .. important::

     The Zephyr IIO server speaks the libiio v1 protocol. libiio v0.x tools
     and libraries (for example an older ``iio_info`` installed with IIO
     Oscilloscope) cannot connect to it.

- The **libiio v1 Python bindings**. The ``pylibiio`` package on PyPI is
  still v0.25, so install the bindings from the libiio source instead:

  .. code-block:: bash

     git clone https://github.com/analogdevicesinc/libiio.git
     pip install ./libiio/bindings/python

- **pyadi-iio** and **matplotlib**:

  .. code-block:: bash

     pip install pyadi-iio matplotlib

Architecture Overview
^^^^^^^^^^^^^^^^^^^^^

**Variant A** runs everything on the FTHR. The PC only displays the shell:

::

   ┌────────────────┐  DAPLink serial  ┌───────────────────────────┐
   │  PC (PuTTY)    │ ◄──────────────► │      MAX32666FTHR         │
   │                │    115200 8N1    │        (Zephyr)           │
   │  types         │                  │                           │
   │  "curvetrace"  │                  │  shell ── curve tracer    │
   └────────────────┘                  │              │            │
                                       │      Zephyr DAC / ADC API │
                                       │              │            │
                                       │      SPI ◄───┴──► AD5592r │
                                       └───────────────────────────┘

**Variant B** runs the Zephyr IIO server on the FTHR, and the curve tracer
script on the PC, exactly like the tinyiiod example:

::

   ┌────────────────┐  FTHR USB serial ┌───────────────────────────┐
   │  PC (Python)   │ ◄──────────────► │      MAX32666FTHR         │
   │                │   libiio (v1)    │        (Zephyr)           │
   │  ad5592r_      │                  │                           │
   │  curve_tracer  │                  │   IIO server (iiod)       │
   │  .py           │                  │   AD5592r ◄── SPI         │
   └────────────────┘                  │   AD5593r ◄── I2C         │
                                       │   LM75    ◄── I2C         │
                                       └───────────────────────────┘

The two variants use different serial ports. The **MAX32625PICO** (DAPLink)
programs the FTHR and also bridges the FTHR's console UART to the PC; this is
where the Zephyr shell appears in Variant A. In Variant B, the IIO server uses
a second serial port that the **FTHR's own USB connector** provides.

Step 1: Create the Zephyr Workspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The libiio repository includes a ``west`` manifest that pulls a Zephyr tree
together with the libiio Zephyr module, which provides the IIO server used in
Variant B. Create a workspace from it:

.. code-block:: bash

   mkdir lsmspg-zephyr
   cd lsmspg-zephyr
   west init -m https://github.com/analogdevicesinc/libiio --mr main .
   west update
   pip install -r zephyr/scripts/requirements.txt

The workspace contains ``zephyr/`` (the Zephyr tree, including the
``adi_lsmspg`` shield and the curve tracer sample) and ``libiio/`` (the
libiio Zephyr module and the IIO server sample). Run the ``west build``
commands below from the workspace root.

Step 2: Connect the Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Mount the MAX32666FTHR onto the ADALM-LSMSPG board using the Feather
   headers **P1** (16-pin) and **P28** (12-pin), with the Feather's
   components facing downward.

2. Connect the MAX32625PICO to the FTHR's 10-pin SWD header.

3. Connect both the MAX32625PICO and the MAX32666FTHR to the PC with the
   Micro USB cables. A ``DAPLINK`` drive appears on the PC.

Step 3a: Curve Tracer on the FTHR (Variant A)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The curve tracer is a Zephyr sample in
``zephyr/samples/shields/adi_lsmspg/curve_tracer``. The sample selects the
``adi_lsmspg`` shield in its ``CMakeLists.txt``, so you only pass the board:

.. code-block:: bash

   west build -p always -b max32666fthr/max32666/cpu0 zephyr/samples/shields/adi_lsmspg/curve_tracer

To program the FTHR, drag and drop ``build/zephyr/zephyr.hex`` onto the
``DAPLINK`` drive. The drive ejects itself when programming is done.

The application follows the same steps as the Python and no-OS versions:

1. Sweep the base drive (``CH0``, DAC) from 499 mV to 2499 mV in 500 mV
   steps.
2. For each base voltage, sweep the collector drive (``CH2``, DAC) from 0 to
   2450 mV in 50 mV steps.
3. At each point, read the collector drive (``CH2``, ADC) and collector sense
   (``CH1``, ADC), and compute the collector current from the voltage drop
   across the sense resistor.
4. Print each point, then the ASCII-art plot.

The four channels are described in the sample's ``app.overlay``, and the code
uses the standard Zephyr DAC and ADC APIs, so there is no SPI or register-level
code in the application:

.. code-block:: dts

   / {
   	zephyr,user {
   		io-channels = <&ad5592_dac 0>, <&ad5592_dac 2>,
   			      <&ad5592_adc 1>, <&ad5592_adc 2>;
   		io-channel-names = "vb_drive", "vc_drive",
   				   "vc_sense", "vc_drive_meas";
   	};
   };

.. note::

   The sample uses the resistor values from the ADALM-LSMSPG schematic:
   49.9 Ohm for the collector sense resistor and 49.9 kOhm for the base
   resistor. The no-OS, pyadi-iio and MATLAB examples use 47 Ohm and
   47 kOhm, so their collector currents read about 6% higher for the same
   transistor. Both values can be changed with
   ``CONFIG_CURVE_TRACER_RSENSE_MOHM`` and ``CONFIG_CURVE_TRACER_RBASE_OHM``.

Step 3b: Curve Tracer from Python (Variant B)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Build the IIO server sample from the libiio module. The ``iiod-cdc-acm``
snippet runs the server on the FTHR's USB port, and the second shield,
``iio_adi_lsmspg``, maps the shield's channels to IIO devices:

.. code-block:: bash

   west build -p always -b max32666fthr/max32666/cpu0 libiio/zephyr/samples/iiod -S iiod-cdc-acm -- -DSHIELD="adi_lsmspg;iio_adi_lsmspg" -DCONFIG_SENSOR=y -DCONFIG_ADC=y -DCONFIG_DAC=y

Drag and drop ``build/zephyr/zephyr.hex`` onto the ``DAPLINK`` drive, as in
Step 3a.

.. note::

   ``west flash`` can program the FTHR through the DAPLink as well, but it
   uses OpenOCD with the ``max32665.cfg`` target file, which the Zephyr SDK's
   OpenOCD does not include. Use the OpenOCD from the
   `ADI OpenOCD fork <https://github.com/analogdevicesinc/openocd>`__ if you
   prefer ``west flash`` to drag and drop.

After a reset, the FTHR's USB connector enumerates as a new serial port. On
Windows it is listed in **Device Manager** under **Ports (COM & LPT)** as a
"USB Serial Device". It is a different port from the DAPLink one; its USB
vendor ID is ``2FE3``.

Verify the IIO context, replacing ``COM7`` with your port:

.. code-block:: bash

   iio_info -u serial:COM7,115200,8n1n

You should see three IIO devices:

- ``ad5592r``: 8-channel ADC/DAC over SPI (used for the NPN curve tracer)
- ``ad5593r``: 8-channel ADC/DAC over I2C
- ``lm75``: temperature sensor

The ``ad5592r`` device shows channels ``voltage0`` (input and output),
``voltage1`` (input) and ``voltage2`` (input and output), with a ``scale``
of ``0.610351`` mV/LSB. These are the names that pyadi-iio's ``adi.ad5592r``
class expects, so the Raspberry Pi script runs unchanged.

.. important::

   On Windows, the libiio v1 Python bindings fail on ``import iio`` (and so
   on ``import adi``) with ``TypeError: argument of type 'NoneType' is not
   iterable``, because they look for the C library with
   ``find_library("c")``, which returns ``None`` on Windows. Until this is
   fixed in libiio, add these lines at the top of
   ``ad5592r_curve_tracer.py``, before ``import adi``:

   .. code-block:: python

      import ctypes.util
      _find_library = ctypes.util.find_library
      ctypes.util.find_library = lambda name: (_find_library(name) or "ucrtbase") if name == "c" else _find_library(name)

   Linux and macOS are not affected.

Step 4: Run the Curve Tracer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Variant A (Step 3a):**

Open the DAPLink serial port in your terminal at **115200 8N1**, with no
flow control, and press the **reset** button on the FTHR. Nothing runs at
boot; the application prints a banner and waits at the Zephyr shell prompt.
Type ``curvetrace`` to run one sweep:

.. code-block:: none

   *** Booting Zephyr OS build <version> ***
   ADALM-LSMSPG AD5592R curve tracer on max32666fthr/max32666/cpu0
   Type 'curvetrace' to run a trace

   uart:~$ curvetrace

   ========== AD5592R (SPI) NPN Curve Tracer ==========
   Vref: 2500 mV, Scale: 0.6104 mV/LSB, Rsense: 49.9 ohm, Rbase: 49900 ohm

   Starting sweep...
   Base Drive: 0.4987 V, -4.035 uA
     coll voltage: 0.0012 V  coll current: 0.0000 mA
     coll voltage: 0.0488 V  coll current: 0.0122 mA
     ...

The sweep takes about 3.4 seconds and ends with the ASCII-art plot, as shown in
:numref:`fig-zephyr-curvetrace-console`. Type ``curvetrace`` again to repeat
it.

.. _fig-zephyr-curvetrace-console:

.. figure:: curvetrace_console.png
   :width: 500px
   :align: center

   Curve tracer output on the Zephyr console (Variant A)

**Variant B (Step 3b):**

Run the same script as on the Raspberry Pi, with the FTHR's USB serial port
as the URI:

.. code-block:: bash

   python ad5592r_curve_tracer.py -u serial:COM7,115200,8n1n

The script prints each base drive and collector point, then opens the
matplotlib figure in :numref:`fig-zephyr-pyadi-curve-tracer`. The sweep takes
about 14 seconds, since every DAC write and ADC read is a separate IIO request
over the serial link.

.. _fig-zephyr-pyadi-curve-tracer:

.. figure:: pyadi_curve_tracer.png
   :width: 500px
   :align: center

   Curve tracer plot from pyadi-iio, Zephyr IIO server (Variant B)

Comparison: no-OS vs. Zephyr
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 28 36 36

   * -
     - **no-OS (MAX32666FTHR)**
     - **Zephyr (MAX32666FTHR)**
   * - IIO server
     - tinyiiod firmware from the no-OS release
     - ``libiio/zephyr/samples/iiod``, built for the ``adi_lsmspg`` shield
   * - Standalone curve tracer
     - ``curvetrace_example`` from the no-OS release
     - ``samples/shields/adi_lsmspg/curve_tracer``
   * - How the hardware is described
     - Init parameters in the project's C code
     - Devicetree (the ``adi_lsmspg`` shield and ``app.overlay``)
   * - Device access in the application
     - no-OS AD5592R driver API
     - Standard Zephyr DAC and ADC APIs
   * - Starting a standalone sweep
     - Runs at reset
     - ``curvetrace`` shell command
   * - Host connection for the IIO server
     - USB serial, libiio
     - USB serial, libiio v1

.. note::

   The PC side does not change between the no-OS tinyiiod server and the
   Zephyr IIO server: the same pyadi-iio script talks to both. The firmware
   side moves from a dedicated bare-metal project to an RTOS with a shell,
   a devicetree description of the hardware and drivers that work on any
   Zephyr board with a Feather header.
