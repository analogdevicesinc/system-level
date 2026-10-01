.. _datax-zephyr-example:

RTOS Support: Zephyr
------------------------

.. note::

   This is a work in progress.



The MATLAB example above used the MAX32666FTHR as a **tinyiiod server**, exposing
the ADALM-LSMSPG devices over serial for a host script to drive. In this section
we go a step further: the curve tracer application itself now runs **on the
MAX32666FTHR**, written against `Zephyr <https://zephyrproject.org/>`__ — a
small, portable real-time OS. The PC becomes a passive terminal that only
displays results.

.. note::

   This exercise demonstrates using Zephyr as a fully embedded alternative to
   Linux or bare-metal no-OS. Zephyr provides drivers for the shield's chips,
   a POSIX-like shell over UART for interactive debugging, and a build system
   that treats the ADALM-LSMSPG as a first-class device — no external host,
   no IIO daemon, no Python or MATLAB.

.. note::

   The examples below target the **MAX32666FTHR**. The same steps apply to
   the MAX32655FTHR (and any other Feather-form-factor Zephyr board) — swap
   the ``-b max32666fthr/max32666/cpu0`` build target for the equivalent
   board qualifier of your Feather.

Hardware Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

- **ADALM-LSMSPG** shield
- **MAX32666FTHR** Feather development board
- **MAX32625PICO** DAPLink debug adapter (comes with the FTHR kit)
- Two Micro USB cables — one for the FTHR (power), one for the DAPLink
  (SWD + serial bridge)

Software Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

- **Analog Devices CodeFusion Studio (CFS)** 2.2.0 or later — ships an
  integrated Zephyr 4.3.0 tree, the Zephyr SDK toolchain, and the ADI HAL
  for the MAX32 family. Download from
  `developer.analog.com <https://developer.analog.com/tools/codefusion-studio/>`__.
- A serial terminal — **PuTTY**, `Tera Term <https://ttssh2.osdn.jp/>`__,
  or the built-in serial monitor of VS Code.
- (Optional) The full upstream Zephyr checkout via ``west init`` — for
  users not on CFS.

Architecture Overview
^^^^^^^^^^^^^^^^^^^^^

Unlike the tinyiiod approach, there is no host script and no IIO daemon.
Zephyr, the curve tracer logic, and the AD5592R / LM75 drivers all live in
a single firmware image running on the MAX32666FTHR:

::

   ┌────────────────┐    USB Serial    ┌───────────────────────────┐
   │  PC (PuTTY)    │ ◄──────────────► │      MAX32666FTHR         │
   │                │    115200 8N1    │        (Zephyr)           │
   │  read-only     │                  │                           │
   │  terminal      │                  │  Zephyr shell + main()    │
   └────────────────┘                  │  ┌────────────────────┐   │
                                       │  │  ad5592 curvetrace │   │
                                       │  └──────────┬─────────┘   │
                                       │             │             │
                                       │        Zephyr AD559X MFD  │
                                       │             │             │
                                       │      SPI ◄──┴──►  AD5592R │
                                       │      I2C ◄──────►  AD5593R│
                                       │      I2C ◄──────►  LM75   │
                                       └───────────────────────────┘

The **DAPLink** (MAX32625PICO) plays two roles at once: it programs the
FTHR over SWD, *and* it bridges the FTHR's UART1 to the PC as a USB CDC
serial port. That single COM port is where both flashing feedback and the
Zephyr shell prompt appear.

Step 1: Create the Zephyr Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From within CodeFusion Studio, generate a new project targeting
``max32666fthr / max32666 / cpu0``. Start from the **Blinky** template — it
gives us a working baseline (an LED that toggles) before we add anything.
The generated directory tree looks like:

::

   MAX32666_LSMSPG_Zephyr/
   └── m4-0/
       ├── CMakeLists.txt
       ├── prj.conf
       ├── boards/
       │   └── max32666fthr_max32666_cpu0.overlay
       └── src/
           └── main.c

The Blinky template targets the FTHR's on-board RGB LED via the standard
Zephyr ``led0`` alias — no shield references yet.

Step 2: Configure the Drivers (``prj.conf``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zephyr uses a Kconfig-based build. The board's ``defconfig`` already
enables serial console, GPIO, and ``printk``; the ``adi_lsmspg`` shield
already ``select``\ s the SPI, I²C, and MFD subsystems in its
``Kconfig.shield``. On top of those defaults we only need to opt in to
the interactive shell and the AD559X chip driver:

.. code-block:: none

   # Interactive shell over the console UART
   CONFIG_SHELL=y
   CONFIG_DEVICE_SHELL=y
   CONFIG_I2C_SHELL=y

   # AD5592R / AD5593R chip driver
   CONFIG_MFD_AD559X=y

Step 3: The Curve Tracer Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The curve tracer is exposed as a Zephyr **shell command** — ``ad5592
curvetrace`` — rather than running automatically at boot. This makes the
firmware into an interactive instrument: you can poke the DAC, read the
ADC, and rerun a sweep on demand from PuTTY.

The C code mirrors the Python and MATLAB versions exactly:

1. Sweep ``Vbase`` (CH0 DAC) from 499 mV to 2499 mV in 500 mV steps.
2. For each base voltage, sweep ``Vcollector`` (CH2 DAC) from 0 to 2450 mV
   in 50 mV steps.
3. At each point, read back ``Vcdrive_meas`` (CH2 ADC) and ``Vcsense``
   (CH1 ADC), compute ``Ic = (Vcdrive_meas − Vcsense) / Rsense``, and
   print one CSV-friendly line over UART.

.. collapsible:: main.c — Zephyr curve tracer with shell integration (click to expand)

   .. code-block:: c

      /*
       * AD5592R NPN BJT curve tracer on the ADALM-LSMSPG shield.
       * Runs as a Zephyr shell command over the MAX32666FTHR's DAPLink
       * USB-serial console. Uses the AD559X multi-function driver's
       * raw write/read API to talk to the chip.
       *
       *   ad5592 init          One-time setup: enable ref + DAC pin mode.
       *   ad5592 dac  <ch> <c> Write 12-bit DAC code (0..4095).
       *   ad5592 adc  <ch>     Read one ADC channel.
       *   ad5592 curvetrace    Run the NPN BJT curve trace.
       *
       * SPDX-License-Identifier: Apache-2.0
       */

      #include <zephyr/kernel.h>
      #include <zephyr/device.h>
      #include <zephyr/drivers/gpio.h>
      #include <zephyr/drivers/mfd/ad559x.h>
      #include <zephyr/shell/shell.h>
      #include <zephyr/sys/byteorder.h>
      #include <stdlib.h>

      #define VREF_MV   2500
      #define FS_CODE   4095U

      /* AD5592R 16-bit DAC write: [1 | ch[2:0] | data[11:0]] */
      #define AD559X_DAC_WR_MSB   BIT(15)
      #define AD559X_DAC_CH_SHIFT 12

      /* Curve tracer circuit parameters (ADALM-LSMSPG NPN) */
      #define CT_RSENSE_OHM   47
      #define CT_RBASE_KOHM   47
      #define CT_VBE_MV       700
      #define CT_VB_START_MV  499
      #define CT_VB_STOP_MV   2500
      #define CT_VB_STEP_MV   500
      #define CT_VC_START_MV  0
      #define CT_VC_STOP_MV   2500
      #define CT_VC_STEP_MV   50

      #define LED0_NODE DT_ALIAS(led0)
      static const struct gpio_dt_spec led =
              GPIO_DT_SPEC_GET(LED0_NODE, gpios);

      static const struct device *const mfd =
              DEVICE_DT_GET(DT_PARENT(DT_NODELABEL(ad5592_dac)));

      static uint16_t dac_mask;
      static uint16_t adc_mask;
      static bool chip_initialized;

      static int ad5592_dac_write(uint8_t ch, uint16_t value)
      {
          uint16_t msg = sys_cpu_to_be16(AD559X_DAC_WR_MSB |
                              ((uint16_t)ch << AD559X_DAC_CH_SHIFT) |
                              (value & 0x0FFF));
          return mfd_ad559x_write_raw(mfd,
                                      (uint8_t *)&msg, sizeof(msg));
      }

      static int ad5592_adc_read(uint8_t ch, uint16_t *out)
      {
          uint16_t raw = 0;
          int ret = mfd_ad559x_read_reg(mfd, AD559X_REG_SEQ_ADC,
                                        BIT(ch), &raw);
          if (ret) return ret;
          *out = raw & 0x0FFF;
          return 0;
      }

      static int cmd_init(const struct shell *sh,
                          size_t argc, char **argv)
      {
          int ret;
          ret = mfd_ad559x_write_reg(mfd, AD559X_REG_PD_REF_CTRL,
                                     AD559X_EN_REF);
          if (ret) return ret;
          dac_mask = 0xFF;
          adc_mask = 0;
          ret = mfd_ad559x_write_reg(mfd, AD559X_REG_LDAC_EN,
                                     dac_mask);
          if (ret) return ret;
          chip_initialized = true;
          shell_print(sh, "AD5592R initialized");
          return 0;
      }

      static int cmd_curvetrace(const struct shell *sh,
                                size_t argc, char **argv)
      {
          if (!chip_initialized) {
              shell_error(sh, "run 'ad5592 init' first");
              return -EINVAL;
          }
          adc_mask |= BIT(1) | BIT(2);
          mfd_ad559x_write_reg(mfd, AD559X_REG_ADC_CONFIG, adc_mask);

          shell_print(sh, "");
          shell_print(sh,
              "=== NPN Curve Tracer (Rsense=%dR Rbase=%dk) ===",
              CT_RSENSE_OHM, CT_RBASE_KOHM);

          for (int vb = CT_VB_START_MV; vb < CT_VB_STOP_MV;
               vb += CT_VB_STEP_MV) {
              uint32_t vb_c = ((uint32_t)vb * FS_CODE) / VREF_MV;
              ad5592_dac_write(0, vb_c);
              k_msleep(50);

              int ib_ua = (vb > CT_VBE_MV) ?
                          (vb - CT_VBE_MV) / CT_RBASE_KOHM : 0;
              shell_print(sh,
                  "\n-- Vb=%d mV, Ib~%d uA --", vb, ib_ua);
              shell_print(sh,
                  "Vc_drive, Vc_actual, Ic (mV, mV, uA)");

              for (int vc = CT_VC_START_MV; vc < CT_VC_STOP_MV;
                   vc += CT_VC_STEP_MV) {
                  uint32_t vc_c = ((uint32_t)vc * FS_CODE) / VREF_MV;
                  ad5592_dac_write(2, vc_c);
                  k_msleep(10);

                  uint16_t vc_drive = 0, vc_sense = 0;
                  ad5592_adc_read(2, &vc_drive);
                  ad5592_adc_read(1, &vc_sense);

                  int vc_drv_mv = (vc_drive * VREF_MV) / FS_CODE;
                  int vc_sns_mv = (vc_sense * VREF_MV) / FS_CODE;
                  int ic_ua = ((vc_drv_mv - vc_sns_mv) * 1000) /
                              CT_RSENSE_OHM;

                  shell_print(sh, "%d, %d, %d",
                              vc, vc_sns_mv, ic_ua);
              }
          }
          ad5592_dac_write(0, 0);
          ad5592_dac_write(2, 0);
          shell_print(sh, "\n=== done ===");
          return 0;
      }

      SHELL_STATIC_SUBCMD_SET_CREATE(ad5592_cmds,
          SHELL_CMD_ARG(init,       NULL, "Init AD5592R",
                        cmd_init, 1, 0),
          SHELL_CMD_ARG(curvetrace, NULL, "Run NPN curve trace",
                        cmd_curvetrace, 1, 0),
          SHELL_SUBCMD_SET_END
      );
      SHELL_CMD_REGISTER(ad5592, &ad5592_cmds,
                         "AD5592R shell commands", NULL);

      int main(void)
      {
          gpio_pin_configure_dt(&led, GPIO_OUTPUT_INACTIVE);
          while (1) {
              gpio_pin_toggle_dt(&led);
              k_msleep(500);
          }
      }

A few notes about the code:

- ``main()`` only blinks the LED as a "firmware alive" heartbeat. All
  real work happens in shell commands, which the Zephyr shell subsystem
  runs on its own kernel thread.
- ``SHELL_CMD_REGISTER`` is Zephyr's macro for exposing a function as a
  top-level shell command. ``SHELL_STATIC_SUBCMD_SET_CREATE`` groups
  subcommands under a single command name (``ad5592``).
- The AD559X driver's ``mfd_ad559x_write_raw`` / ``mfd_ad559x_read_reg``
  functions handle SPI framing and chip-select for us. There is no
  direct SPI code in the application.
- Output is CSV-shaped so you can copy the PuTTY buffer straight into
  a spreadsheet for plotting.

Step 4: Attach the Shield to the Build
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zephyr ships an official shield definition for the ADALM-LSMSPG. To pull
its devicetree overlay into the build, pass ``--shield adi_lsmspg`` (as
a CMake variable ``-DSHIELD=adi_lsmspg``) to ``west build``. This binds
the AD5592R to the Feather SPI header and the AD5593R + LM75 to the
Feather I²C header automatically — no manual overlay edits required.

.. note::

   The shield definition lives at
   ``<zephyr>/boards/shields/adi_lsmspg/``. Refer to the
   `upstream Zephyr documentation
   <https://docs.zephyrproject.org/latest/boards/shields/adi_lsmspg/doc/index.html>`__
   for its full description.

Step 5: Build and Flash
^^^^^^^^^^^^^^^^^^^^^^^

From the project directory:

.. code-block:: bash

   west build -p always -b max32666fthr/max32666/cpu0 . -- -DSHIELD=adi_lsmspg
   west flash

``west flash`` uses OpenOCD via the DAPLink to program the FTHR. If your
CFS install prefers drag-and-drop instead, the ``build/zephyr/zephyr.hex``
file can be dragged onto the DAPLink mass-storage drive that appears in
Explorer.

Step 6: Open the Serial Terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Identify the COM port assigned to the DAPLink (Windows: **Device Manager
→ Ports (COM & LPT)** — look for the "USB Serial Device" entry that
appears when the DAPLink is plugged in). Open it in PuTTY at
**115200 8N1** with no flow control.

Press the **reset** button on the FTHR. You should see:

.. code-block:: none

   *** Booting Zephyr OS build v4.3.0 ***

   uart:~$

The ``uart:~$`` prompt is Zephyr's interactive shell. From here you can
type ``help`` for a list of built-in commands, ``device list`` to see
every device the kernel is aware of, or ``i2c scan i2c0@4001d000`` to
confirm the shield's I²C chips are alive.

Step 7: Run the Curve Trace
^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the shell prompt:

.. code-block:: none

   uart:~$ ad5592 init
   AD5592R initialized
   uart:~$ ad5592 curvetrace

   === NPN Curve Tracer (Rsense=47R Rbase=47k) ===

   -- Vb=499 mV, Ib~0 uA --
   Vc_drive, Vc_actual, Ic (mV, mV, uA)
   0, 1, -21
   50, 49, 21
   ...
   -- Vb=999 mV, Ib~6 uA --
   ...
   === done ===

Highlight the CSV block in PuTTY (Ctrl+A then right-click to copy on
most terminals) and paste it into a spreadsheet or the Python plotting
snippet from the Raspberry Pi section to render the I–V family.

Comparison: MATLAB (tinyiiod) vs. Zephyr
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * -
     - **MATLAB + tinyiiod**
     - **Zephyr on FTHR**
   * - OS on the FTHR
     - no-OS (tinyiiod firmware)
     - Zephyr RTOS
   * - Where the sweep runs
     - MATLAB on the PC
     - On the FTHR itself
   * - Host role
     - Active — issues every I/O
     - Passive — displays a shell
   * - Framework used
     - libiio + PrecisionToolbox
     - Zephyr device drivers
   * - Connection to devices
     - IIO over USB serial
     - Direct SPI / I²C on the FTHR
   * - Latency per point
     - ~ms (subprocess or in-proc)
     - ~microseconds (direct SPI)
   * - Extending the app
     - Edit MATLAB, rerun
     - Rebuild + reflash firmware

.. note::

   Zephyr trades the host-side flexibility of tinyiiod for **latency,
   portability, and self-containedness**. A Zephyr firmware works with
   only a serial terminal on the host — no libiio, no MATLAB, no Python.
   That makes it a natural stepping-stone toward a *fully embedded*
   product where the FTHR eventually drives a local display or wireless
   link instead of a PC terminal.
