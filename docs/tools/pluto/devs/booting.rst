.. _pluto devs booting:

PlutoSDR/M2k boot magic explained
====================================

There are few different use cases, and methods to locally (USB/Serial), or
remotely (USB/Network) to reboot a Pluto/M2k.

Pluto/M2k was designed never to have to be rebooted - but software bugs
happen. Before you reboot things - try to ask yourself "why", what went wrong,
how do I reproduce, and how can I file a bug report that will help someone
debug.

Custom u-boot environment variables
--------------------------------------

There are a set of custom u-boot environmental variables used during boot,
which either are set dynamically by custom u-boot commands, or are imported
from an additional protected u-boot environment or are part of the regular
SPI u-boot environment but are used to control the runtime behavior.

Hardware Revision Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PlutoSDR or M2k firmware (FIT image) supports multiple HW revisions. It's
being done reading a voltage divider which is unique for a given HW revision
using the on chip XADC. This voltage is then mapped into 10 possible values
which are then set in the ``fit_config`` environmental variable. Values are in
the form of ``config@%d`` where ``%d`` is in the range from 0..9. This
variable is then being used to load the corresponding FIT config which is
right now only a dedicated device tree, however when necessary can be
extended to also load a different bitfile.

The ``adi_hwref`` command will set ``fit_config`` and for Pluto Rev.A it will
additionally set the ``PlutoRevA`` variable.

.. list-table::
   :header-rows: 1

   * - variable
     - comment
   * - ``fit_config``
     - config@ number
   * - ``PlutoRevA``
     - set only for Rev.A

Device tree patching
~~~~~~~~~~~~~~~~~~~~~~

During factory calibration the onboard TCXO reference frequency is measured
and the actual reference clock frequency is stored in an additional protected
SPI environment which is imported during boot. Later on this value is used to
patch the device tree property ``clock-frequency`` in the
``/clocks/clock@0`` path. This step can be skipped by the user when setting
the ``ad936x_skip_ext_refclk`` variable. This allows for custom reference
clock frequency set in the regular device tree.

.. list-table::
   :header-rows: 1

   * - variable
     - device tree destination
     - Comment
   * - ``ad936x_ext_refclk``
     - ``/clocks/clock@0`` clock-frequency
     - Skip this by setting the ``ad936x_skip_ext_refclk`` variable
   * - ``model``
     - ``/model``
     - Model string
   * - ``attr_name``
     - ``/amba/spi@e0006000/ad9361-phy@0`` ${attr_name} ${attr_val}
     -
   * - ``attr_val``
     - ``/amba/spi@e0006000/ad9361-phy@0`` ${attr_name} ${attr_val}
     -

Set during DFU update
~~~~~~~~~~~~~~~~~~~~~~~

The DFU altsetting of the DFU interface is stored in the ``dfu_alt_num``
variable and the transfers size is stored in the ``filesize`` variable.

.. list-table::
   :header-rows: 1

   * - variable
     - comment
   * - ``dfu_alt_num``
     - altsetting of the DFU interface in progress
   * - ``filesize``
     - filesize of the transferred firmware image

Miscellaneous
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - variable
     - comment
   * - ``uboot-version``
     - u-boot version string set by the ``envversion`` command

Examples
---------

What this means is to change any of these, log into your pluto sdr (over
network or serial), and do this as root:

- If you want to replace the 40 MHz oscillator, and insert a 20 MHz
  (20000000 Hz) clock:

  .. shell::

     # fw_setenv ad936x_ext_refclk "<20000000>"

  The quotes need to be there to escape the ``<>``, which need to be there
  since this goes into device tree.

- If you have a AD9364 inside your PlutoSDR

  .. shell::

     # fw_setenv attr_name compatible
     # fw_setenv attr_val ad9364

- If you have a standard Zynq 7010 (not the special single core version)

  .. shell::

     # fw_setenv maxcpus

- If you want to tweak your default XO correction rather than 40 MHz, you have
  determined at a stable temp it is 39,999,764 Hz:

  .. shell::

     # fw_setenv xo_correction 39999764

All Environmental Settings Table
-----------------------------------

This table applies for firmware releases v0.32 onward.

.. list-table::
   :header-rows: 1

   * - Control
     - Default
     - min FW Version
     - HW Rev
     - ``name``
     - ``value``
     - configuration meaning
   * - Tuning Range
     - Y
     - All
     - B/C
     - ``attr_name`` / ``attr_val``
     - *<blank>* / *blank*
     - tuning range is 325 - 3800 MHz, ``mode`` is ``1r1t`` or ``2r2t``
   * -
     -
     - All
     - B/C
     - ``attr_name`` / ``attr_val``
     - ``compatible`` / ``ad9364``
     - tuning range is 70 - 6000 MHz, ``mode`` is ``1r1t`` only
   * -
     -
     - 0.32
     - C
     - ``attr_name`` / ``attr_val``
     - ``compatible`` / ``ad9361``
     - tuning range is 70 - 6000 MHz, ``mode`` is ``1r1t`` or ``2r2t``
   * - Number of channels
     - Y
     - 0.32
     - B/C
     - ``mode``
     - ``1r1t``
     - 1 Rx, 1 Tx, 61.44 MSPS max data rate
   * -
     -
     - 0.32
     - C
     - ``mode``
     - ``2r2t``
     - 2 Rx, 2 Tx, 30.72 MSPS max data rate (requires ad9363 or AD9361 settings)
   * - Reference Clock in
     - Y
     - 0.32
     - B/C
     - ``refclk_source``
     - ``internal``
     - Internal Reference Clock, ``ad936x_ext_refclk_override`` holds frequency in Hz
   * -
     -
     - 0.32
     - C
     - ``refclk_source``
     - ``external``
     - Reference Clock on u.FL is used, ``ad936x_ext_refclk_override`` holds frequency in Hz
   * - Reference Clock Value
     - Y
     - 0.32
     - B/C
     - ``ad936x_ext_refclk``
     - ``<40000000>``
     - 40 MHz, is the measured value determined at production test and should not be modified
   * -
     -
     - 0.32
     - C
     - ``ad936x_ext_refclk_override``
     - ``<any>``
     - Actual clock setting in Hz, 10 - 80 MHz, resolution is in Hz
   * - SPI Controls
     - Y
     - 0.32
     - C
     - ``cs_gpio``
     - ``<any>``
     - GPIO chip select for use with axi spi
