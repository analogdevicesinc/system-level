.. _software jesd-status:

JESD204B Status Utility
===============================================================================

The ``jesd_status`` utility reads the status information of all JESD204B/C
devices from sysfs, aggregates and processes them and prints it to the terminal
in a continuous fashion.

Unlike the :ref:`JESD204 Eye Scan <software jesd-eye-scan>` tool, it doesn't
support eye scan, but can show all the link and lane status information while
remaining lightweight and not requiring a graphical desktop. It can be used from
serial root consoles or SSH terminals.

The utility interfaces with the JESD204 Interface Framework through the
following driver components:

- :external+linux:ref:`axi_jesd204_tx`
- :external+linux:ref:`axi_jesd204_rx`
- :external+linux:ref:`axi_adxcvr`

Source code is available at :git-jesd-eye-scan-gtk:`GitHub <>`.

Usage
--------------------------------------------------------------------------------

.. code-block::

   Usage: jesd_status [-s] [-p PATH]
       -s     Simple mode no boxes and frames (useful for serial terminals)
       -p     Allows setting a different directory root. Default is /.
              This is useful when running the tool remote

Basic execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. shell::

   $jesd_status

Simple terminal mode (useful for serial consoles):

.. shell::

   $TERM=vt100 jesd_status -s

Alternative command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For systems that do not have ``jesd_status`` installed, the following command
can be used to retrieve the same information:

.. shell::

   $grep "" /sys/bus/platform/drivers/axi-jesd204\*/\*/status /sys/bus/platform/drivers/axi-jesd204\*/\*/lane\* /sys/bus/platform/drivers/axi-jesd204\*/\*/encoder

Status information reference
--------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Description
   * - Link enabled/disabled
     - Indicates link state; disabled means link was never activated or an error
       caused FSM rollback
   * - Link status
     - Values vary by encoding (RESET, WAIT, CGS, ILAS, DATA); DATA indicates
       proper operation
   * - SYNC assertion (8B10B)
     - External SYNC signal state
   * - SYSREF captured (Subclass 1)
     - Indicates captured SYSREF pulse
   * - SYSREF alignment error
     - Detects unaligned SYSREF events relative to LMFC/LEMC periods
   * - Lane rate
     - SERDES lane rate/bit clock frequency
   * - LMFC/LEMC rate
     - Internal multiframe clock frequency
   * - Reported Link Clock
     - Common clock framework reported frequency
   * - Measured Link Clock
     - Frequency counter measurement from Link Layer Peripheral
   * - Desired Device Clock
     - Clock value; differs from Link Clock if Dual Clock Operation is required
   * - Reported Device Clock
     - Framework-reported Device Clock frequency
   * - Measured Device Clock
     - Frequency counter measurement for Device Clock
