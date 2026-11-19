.. _datax-matlab-example:

Language Support: MATLAB
------------------------

.. note::

   This is a work in progress.

While the previous exercises used Python and pyadi-iio to communicate with
the AD5592r, the IIO framework is language-agnostic. Any language that can
call into the libiio C library (or use its command-line tools) can control the
hardware. In this section, we will recreate the NPN curve tracer example
in **MATLAB**, and instead of running on the Raspberry Pi, we will use the
**MAX32666FTHR** Feather board as a tinyiiod IIO server, connected to the
ADALM-LSMSPG over SPI and I2C, and controlled from a PC over USB serial.

.. note::

   This exercise demonstrates two key concepts: using MATLAB as an alternative
   to Python for IIO device control, and using a bare-metal microcontroller
   (MAX32666FTHR) as a portable alternative to the Raspberry Pi Linux host.

Hardware Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

In addition to the ADALM-LSMSPG board, you will need:

- **MAX32666FTHR** Feather development board
- Micro USB cable for the MAX32666FTHR

Software Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

- **MATLAB** installed on your PC (base MATLAB is sufficient, no additional
  toolboxes required)
- **ADI Precision Toolbox** for MATLAB — clone or download from
  `GitHub <https://github.com/analogdevicesinc/PrecisionToolbox>`__ and add
  to the MATLAB path
- **libiio** installed on your PC (provides the ``iio_info`` and ``iio_attr``
  command-line tools, and the shared library used by PrecisionToolbox)

  - Windows: download the installer from the
    `libiio GitHub releases <https://github.com/analogdevicesinc/libiio/releases>`__
  - Linux: ``sudo apt install libiio-utils``

Architecture Overview
^^^^^^^^^^^^^^^^^^^^^

The architecture differs from the Raspberry Pi setup. Instead of running
Python directly on the Linux host that is physically connected to the
AD5592r, we now have a two-part system:

::

   ┌────────────────┐   USB Serial    ┌─────────────────────┐
   │  PC (MATLAB)   │ ◄────────────►  │   MAX32666FTHR      │
   │                │    iio_attr/    │   (tinyiiod server) │
   │ curve_tracer.m │    libiio       │                     │
   │     script     │                 │  AD5592r ◄── SPI    │
   └────────────────┘                 │  AD5593r ◄── I2C    │
                                      │  LM75    ◄── I2C    │
                                      └─────────────────────┘

The MAX32666FTHR runs a **tinyiiod** firmware — a bare-metal IIO daemon that
exposes the AD5592r, AD5593r, and LM75 as standard IIO devices over USB
serial. The MATLAB script on the PC sends IIO commands through the serial
link, exactly as if it were talking to a Linux IIO device over the network.

Step 1: Flash the MAX32666FTHR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure the MAX32625PICO DAPLink and the MAX32666FTHR are flashed with the
correct firmware for the ADALM-LSMSPG tinyiiod example — see the
`ADALM-LSMSPG documentation <https://analogdevicesinc.github.io/documentation/tools/adalm-lsmspg/index.html>`__
for step-by-step instructions.

Step 2: Connect the Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Mount the MAX32666FTHR onto the ADALM-LSMSPG board using the Feather
   headers **P1** (16-pin) and **P28** (12-pin), with the Feather's
   components facing downward.

2. Connect the USB cable to the MAX32666FTHR.

3. The **heartbeat LED** (DS1) on the ADALM-LSMSPG should begin blinking
   with a double-pulse pattern, indicating the tinyiiod server is running
   and waiting for connections.

Step 3: Verify the Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, identify the COM port assigned to the MAX32666FTHR. On Windows, open
**Device Manager** and look under **Ports (COM & LPT)** for the USB serial
device.

Then verify the IIO context from a terminal:

.. code-block:: bash

   iio_info -u serial:COM11,115200,8n1n

Replace ``COM11`` with your actual COM port. You should see output listing
four IIO devices:

- ``lm75`` — temperature sensor
- ``ad5592r`` — 8-channel ADC/DAC over SPI (used for NPN curve tracer)
- ``ad5593r`` — 8-channel ADC/DAC over I2C (used for PNP curve tracer)
- ``one-bit-adc-dac`` — GPIO channels mapped as 1-bit ADC/DAC

Confirm that the ``ad5592r`` device shows channels ``voltage0`` (output),
``voltage1`` (input), ``voltage2`` (input and output), and that the scale
attribute reads approximately ``0.61035156`` mV/LSB.

Step 4a: Curve Tracer with ADI Precision Toolbox (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The recommended approach uses the
`ADI Precision Toolbox <https://github.com/analogdevicesinc/PrecisionToolbox>`__,
which calls libiio directly from MATLAB in-process. This is significantly
faster than spawning subprocesses and mirrors how pyadi-iio works in Python.

The Precision Toolbox provides the ``adi.AD5592r.Rx`` class, which inherits
attribute read/write methods from the ``matlabshared.libiio.base`` class.
The key methods used are:

- ``getAttributeDouble(channel, attribute, isOutput)`` — read a channel
  attribute as a double (e.g., the ``scale`` factor)
- ``getAttributeRAW(channel, attribute, isOutput)`` — read a channel
  attribute as a string (e.g., ADC ``raw`` readings)
- ``setAttributeRAW(channel, attribute, value, isOutput)`` — write a channel
  attribute (e.g., set a DAC ``raw`` output value)

The ``isOutput`` flag selects between input (ADC) and output (DAC) channels,
which is important because channels like ``voltage2`` exist as both.

.. collapsible:: ad5592r_curve_tracer.m — Precision Toolbox version (click to expand)

   .. code-block:: matlab

      %% AD5592r NPN Curve Tracer using PrecisionToolbox
      %% Sweeps base and collector voltages on the ADALM-LSMSPG board
      %% and plots Ic vs Vc family of curves.
      clc
      clear

      % Instantiate the system object and connect
      rx = adi.AD5592r.Rx();
      rx.uri = 'serial:COM11,115200,8n1n';
      rx.EnabledChannels = 2;
      rx.SamplesPerFrame = 1;
      rx();

      % Circuit constants (NPN curve tracer on ADALM-LSMSPG)
      Rsense = 47.0;       % 47 Ohms - collector sense resistor
      Rbase  = 47.0e3;     % 47 kOhms - base resistor
      Vbe    = 0.7;         % Approximate base-emitter voltage

      % Read scale (mV per LSB) - identical for all AD5592r channels
      mV_per_lsb = rx.getAttributeDouble('voltage0', 'scale', true);
      fprintf('Scale: %.6f mV/LSB\n', mV_per_lsb);

      % Initialize DAC outputs to a safe starting point
      rx.setAttributeRAW('voltage0', 'raw', num2str(round(500 / mV_per_lsb)), true);
      rx.setAttributeRAW('voltage2', 'raw', num2str(round(500 / mV_per_lsb)), true);

      % Sweep parameters
      base_mv  = 499:500:2499;
      coll_mv  = 0:50:2450;
      n_base   = length(base_mv);
      n_coll   = length(coll_mv);

      % Preallocate results
      curves_vc = zeros(n_base, n_coll);
      curves_ic = zeros(n_base, n_coll);
      labels    = cell(1, n_base);

      for bi = 1:n_base
          vb_raw = round(base_mv(bi) / mV_per_lsb);
          rx.setAttributeRAW('voltage0', 'raw', num2str(vb_raw), true);

          ib = ((vb_raw * mV_per_lsb / 1000) - Vbe) / Rbase;
          fprintf('Base Drive: %.3f V, %.1f uA\n', vb_raw * mV_per_lsb / 1000, ib * 1e6);
          labels{bi} = sprintf('I_b = %.1f \\muA', ib * 1e6);

          for ci = 1:n_coll
              vc_raw = round(coll_mv(ci) / mV_per_lsb);
              rx.setAttributeRAW('voltage2', 'raw', num2str(vc_raw), true);

              vc_drive_raw = str2double(rx.getAttributeRAW('voltage2', 'raw', false));
              vc_sense_raw = str2double(rx.getAttributeRAW('voltage1', 'raw', false));

              ic = (vc_drive_raw - vc_sense_raw) * mV_per_lsb / Rsense;
              vc = vc_sense_raw * mV_per_lsb / 1000.0;

              curves_vc(bi, ci) = vc;
              curves_ic(bi, ci) = ic;
          end
      end

      % Plot
      figure('Name', 'AD5592r NPN Curve Tracer');
      hold on;
      for bi = 1:n_base
          plot(curves_vc(bi, :), curves_ic(bi, :), 'LineWidth', 1.5);
      end
      hold off;
      title('ADALM-LSMSPG NPN Curve Tracer (MATLAB)');
      xlabel('Collector Voltage (V)');
      ylabel('Collector Current (mA)');
      legend(labels, 'Location', 'northwest');
      grid on;

      % Cleanup
      release(rx);

The script structure mirrors the Python version:

1. **Connect** to the AD5592r by creating an ``adi.AD5592r.Rx`` object with
   the serial URI and calling ``rx()`` to initialize the IIO context.
   ``EnabledChannels = 2`` selects ``voltage1`` (an ADC input channel) for
   context initialization. ``SamplesPerFrame = 1`` since we only need
   single-value attribute access, not buffered streaming.
2. **Read the scale** attribute using ``getAttributeDouble`` to get the
   mV-per-LSB conversion factor (approximately 0.610 mV/LSB for the AD5592r
   with internal reference).
3. **Outer loop** — sweep the base drive voltage (``voltage0``, DAC output)
   through 5 steps from 499 mV to 2499 mV using ``setAttributeRAW``, setting
   a different base current for each curve.
4. **Inner loop** — for each base current, sweep the collector drive voltage
   (``voltage2``, DAC output) from 0 to 2450 mV in 50 mV steps. At each
   step, read back the collector drive (``voltage2``, ADC input) and collector
   sense (``voltage1``, ADC input) using ``getAttributeRAW`` to compute the
   collector current through the 47 Ohm sense resistor.
5. **Plot** the family of I-V curves and release the device.

Step 4b: Curve Tracer with Command-Line Tools (Alternative)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As an alternative to the Precision Toolbox, you can use the ``iio_attr``
command-line tool (provided by libiio) directly from MATLAB via the
``system()`` function. This approach is useful for quick debugging and
learning how IIO attributes work at the lowest level, but is significantly
slower because each read or write spawns a new subprocess.

.. collapsible:: ad5592r_curve_tracer_cli.m — iio_attr version (click to expand)

   .. code-block:: matlab

      function ad5592r_curve_tracer_cli(uri)
          if nargin < 1
              uri = 'serial:COM11,115200,8n1n';
          end

          device = 'ad5592r';
          fprintf('URI: %s\n', uri);

          % Circuit constants (NPN curve tracer on ADALM-LSMSPG)
          Rsense = 47.0;      % 47 Ohms - collector sense resistor
          Rbase  = 47.0e3;    % 47 kOhms - base resistor
          Vbe    = 0.7;        % Approximate base-emitter voltage

          % Read scale (mV per LSB) - identical for all AD5592r channels
          mV_per_lsb = iio_read(uri, device, 'voltage0', true, 'scale');
          fprintf('Scale: %.6f mV/LSB\n', mV_per_lsb);

          % Initialize DAC outputs to a safe starting point
          iio_write(uri, device, 'voltage0', true, 'raw', round(500 / mV_per_lsb));
          iio_write(uri, device, 'voltage2', true, 'raw', round(500 / mV_per_lsb));

          % Sweep parameters (matching the Python example)
          base_mv  = 499:500:2499;
          coll_mv  = 0:50:2450;
          n_base   = length(base_mv);
          n_coll   = length(coll_mv);

          % Preallocate results
          curves_vc = zeros(n_base, n_coll);
          curves_ic = zeros(n_base, n_coll);
          labels    = cell(1, n_base);

          for bi = 1:n_base
              vb_raw = round(base_mv(bi) / mV_per_lsb);
              iio_write(uri, device, 'voltage0', true, 'raw', vb_raw);

              ib = ((vb_raw * mV_per_lsb / 1000) - Vbe) / Rbase;
              fprintf('Base Drive: %.3f V, %.1f uA\n', ...
                      vb_raw * mV_per_lsb / 1000, ib * 1e6);
              labels{bi} = sprintf('I_b = %.1f \\muA', ib * 1e6);

              for ci = 1:n_coll
                  vc_raw = round(coll_mv(ci) / mV_per_lsb);
                  iio_write(uri, device, 'voltage2', true, 'raw', vc_raw);

                  vc_drive_raw = iio_read(uri, device, 'voltage2', false, 'raw');
                  vc_sense_raw = iio_read(uri, device, 'voltage1', false, 'raw');

                  ic = (vc_drive_raw - vc_sense_raw) * mV_per_lsb / Rsense;
                  vc = vc_sense_raw * mV_per_lsb / 1000.0;

                  curves_vc(bi, ci) = vc;
                  curves_ic(bi, ci) = ic;
              end
          end

          % Plot
          figure('Name', 'AD5592r NPN Curve Tracer');
          hold on;
          for bi = 1:n_base
              plot(curves_vc(bi, :), curves_ic(bi, :), 'LineWidth', 1.5);
          end
          hold off;
          title('ADALM-LSMSPG NPN Curve Tracer (MATLAB)');
          xlabel('Collector Voltage (V)');
          ylabel('Collector Current (mA)');
          legend(labels, 'Location', 'northwest');
          grid on;
      end

      %% IIO helper functions using iio_attr command-line tool

      function val = iio_read(uri, device, channel, is_output, attr)
          dir_flag = output_flag(is_output);
          cmd = sprintf('iio_attr -u %s -c %s %s %s %s', ...
                        uri, dir_flag, device, channel, attr);
          [status, result] = system(cmd);
          if status ~= 0
              error('iio_attr read failed: %s', strtrim(result));
          end
          tokens = regexp(result, '''([^'']+)''\s*$', 'tokens');
          if ~isempty(tokens)
              val = str2double(tokens{1}{1});
          else
              val = str2double(strtrim(result));
          end
          if isnan(val)
              error('Could not parse iio_attr output: %s', strtrim(result));
          end
      end

      function iio_write(uri, device, channel, is_output, attr, value)
          dir_flag = output_flag(is_output);
          cmd = sprintf('iio_attr -u %s -c %s %s %s %s %d', ...
                        uri, dir_flag, device, channel, attr, value);
          [status, result] = system(cmd);
          if status ~= 0
              error('iio_attr write failed: %s', strtrim(result));
          end
      end

      function flag = output_flag(is_output)
          if is_output
              flag = '-o';
          else
              flag = '-i';
          end
      end

The helper functions ``iio_read`` and ``iio_write`` wrap calls to the
``iio_attr`` command-line tool. Each call spawns a subprocess that
connects to the tinyiiod server over serial, reads or writes the specified
channel attribute, and returns the result.

.. note::

   This approach is noticeably slower than the Precision Toolbox version
   (Step 4a). The ``system()`` calls spawn a new ``iio_attr`` subprocess for
   every read and write operation. For approximately 250 sweep points with
   4 IIO operations each, that is roughly 1000 subprocess launches. The
   Precision Toolbox avoids this overhead by calling libiio directly
   in-process, similar to how pyadi-iio wraps the libiio C library in Python.

Step 5: Run the Curve Tracer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Using the Precision Toolbox (Step 4a):**

In MATLAB, ensure the PrecisionToolbox is on your path, update the URI in
the script to match your COM port, and run:

.. code-block:: matlab

   ad5592r_curve_tracer

**Using the command-line version (Step 4b):**

.. code-block:: matlab

   ad5592r_curve_tracer_cli('serial:COM11,115200,8n1n')

Replace ``COM11`` with your actual COM port.

Both versions will:

1. Read the scale from the AD5592r.
2. Sweep through 5 base voltage steps, each with 50 collector voltage steps.
3. Print progress to the MATLAB command window.
4. Display a figure with the NPN transistor I-V characteristic curves.

The resulting plot should be comparable to the one produced by the Python
``ad5592r_curve_tracer.py`` script run on the Raspberry Pi.

.. figure:: ad5592r_npn_curve_tracer.png
   :width: 500px

   AD5592r NPN Curve Tracer output from MATLAB.

Comparison: Raspberry Pi vs. MAX32666FTHR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Both platforms produce the same curve tracer results, but the underlying
architecture is different:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * -
     - **Raspberry Pi (Linux)**
     - **MAX32666FTHR (Bare Metal)**
   * - OS
     - ADI Kuiper Linux
     - No-OS (tinyiiod firmware)
   * - IIO Framework
     - Linux kernel IIO drivers
     - no-OS IIO + tinyiiod
   * - Connection to AD5592r
     - SPI via device tree overlay
     - SPI via no-OS SPI driver
   * - Host Communication
     - Network (``ip:analog.local``)
     - USB Serial (``serial:COMx,115200,8n1n``)
   * - Script Runs On
     - Raspberry Pi or remote PC
     - Remote PC only
   * - Power
     - 5V USB-C wall adapter
     - USB bus power from PC