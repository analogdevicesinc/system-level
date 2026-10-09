.. _adrv904x user-guide:

User guide
===============================================================================

The complete user guide of the evaluation board can be found at
:adi:`ADRV904X Evaluation System User Guide (UG-2229) <media/en/technical-documentation/user-guides/eval-adrv904x-ug-2229.pdf>`.

Hardware guide
-------------------------------------------------------------------------------

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA.

The VADJ values can be checked out in the README.md file of each combination
with an FPGA, at: :git-hdl:`projects/adrv904x`.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files for the EVAL-ADRV904x evaluation board include:

- Schematics
- PCB Layout
- Bill of Materials
- Design package

Please refer to the :adi:`ADRV9040 product page <ADRV9040>` for
downloadable design files.

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported with the Libiio library. This library is
cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
MATLAB, and others. One easy to example that can be used with it is:

- :ref:`iio-oscilloscope`

For details on how to customize the driver for a specific use case, see the
:external+linux:ref:`ADRV904x customization guide <adrv904x-customization>`.

Kernel configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable the ADRV904x driver when building the Linux kernel from source:

.. code-block:: text

   Device Drivers  --->
     Industrial I/O support  --->
       [*] Enable ring buffer support within IIO
       [*] Industrial I/O lock free software ring
       [*] Enable triggered sampling support

       Analog to digital converters  --->
         <*> Analog Devices ADRV904X/ADRV9040 RF Transceiver driver

       Frequency Synthesizers DDS/PLL  --->
         Direct Digital Synthesis  --->
           <*> Analog Devices CoreFPGA AXI DDS driver

       <*> JESD204 High-Speed Serial Interface Support

Required firmware files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADRV904x Linux driver requires the following firmware files to be present
in ``/lib/firmware/`` on the target system:

.. list-table::
   :header-rows: 1

   - - File
     - Device tree property
     - Description
   - - ``ADRV9040_FW.bin``
     - ``adi,arm-firmware-name``
     - ARM processor firmware for calibrations and device configuration
   - - ``ADRV9040_DFE_CALS_FW.bin``
     - ``adi,arm-dfe-firmware-name``
     - ARM Cortex-A55 firmware for DFE features (DPD, CLGC, VSWR)
   - - ``stream_image.bin``
     - ``stream-firmware-name``
     - Stream processor image (user-generated via ADI evaluation software)
   - - ``ADRV9040_RxGainTable.csv``
     - ``adi,rx-gaintable-names``
     - Receiver gain table (default or custom)
   - - ``DeviceProfileTest.bin``
     - ``adi,device-config-name``
     - Device profile (user-generated configuration file)

These files are included in the Kuiper Linux SD card image.

.. note::

   The ``stream_image.bin`` must be regenerated when updating firmware versions,
   as it is version-specific. The ``DeviceProfileTest.bin`` is use-case specific
   and contains filter coefficients, clock rates, and DFE resource settings.

Device variants
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two device tree configurations are provided:

- **Default profile** (``zynqmp-zcu102-rev10-adrv904x.dts``): Standard TX/RX
  configuration without observation receiver path activation.
- **NLS profile** (``zynqmp-zcu102-rev10-adrv904x-nls.dts``): Enables the
  observation receiver (ORx) path for transmitter monitoring and DPD
  calibration.

To select the device tree, copy the corresponding ``system.dtb`` to the SD card
boot partition before powering up the board.

IIO attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``adrv904x-phy`` IIO device exposes sysfs attributes under
``/sys/bus/iio/devices/iio:deviceN/``. For a full attribute reference, see the
:external+linux:ref:`ADRV904x Linux device driver <adrv904x>`
documentation.

Channel naming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   - - IIO prefix
     - Signal
   - - ``in_voltage0`` – ``in_voltage7``
     - Main receivers RX1–RX8
   - - ``in_voltage8``
     - Observation receiver ORx1
   - - ``in_voltage9``
     - Observation receiver ORx2
   - - ``out_voltage0`` – ``out_voltage7``
     - Transmitters TX1–TX8
   - - ``out_altvoltage0``
     - TRX LO1
   - - ``out_altvoltage1``
     - TRX LO2
   - - ``out_altvoltage2``
     - TRX AUX LO

Local oscillator control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The two RF PLLs are tunable from 450 MHz to 7100 MHz. It is recommended to
re-run the initial calibrations when crossing a divide-by-2 boundary.

.. shell::

   $cat /sys/bus/iio/devices/iio:device1/out_altvoltage0_LO1_frequency
    3765000000
   $echo 3764000000 > /sys/bus/iio/devices/iio:device1/out_altvoltage0_LO1_frequency

RX channel attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   - - Attribute
     - Access
     - Description
   - - ``in_voltageN_en``
     - Read/Write
     - Enable (1) or disable (0) receiver channel N
   - - ``in_voltageN_hardwaregain``
     - Read/Write
     - Receiver hardware gain in dB (0 to 32 dB range, 256 gain settings)
   - - ``in_voltageN_rf_bandwidth``
     - Read/Write
     - Receiver RF bandwidth in Hz
   - - ``in_voltageN_quadrature_tracking_en``
     - Read/Write
     - Enable quadrature error correction tracking (0 or 1)
   - - ``in_voltageN_bb_dc_offset_tracking_en``
     - Read/Write
     - Enable baseband DC offset tracking calibration (0 or 1)

.. shell::

   $cat /sys/bus/iio/devices/iio:device1/in_voltage0_en
    1
   $echo 0 > /sys/bus/iio/devices/iio:device1/in_voltage0_en

TX channel attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1

   - - Attribute
     - Access
     - Description
   - - ``out_voltageN_en``
     - Read/Write
     - Enable (1) or disable (0) transmitter channel N
   - - ``out_voltageN_hardwaregain``
     - Read/Write
     - Transmitter attenuation in dB (range 0 to −32 dB, higher resolution
       via digital gain)
   - - ``out_voltageN_rf_bandwidth``
     - Read/Write
     - Transmitter RF bandwidth in Hz (baseband filter tunable 300–840 MHz)
   - - ``out_voltageN_quadrature_tracking_en``
     - Read/Write
     - Enable quadrature error correction tracking (0 or 1)
   - - ``out_voltageN_lo_leakage_tracking_en``
     - Read/Write
     - Enable LO leakage tracking calibration (0 or 1)

.. shell::

   $cat /sys/bus/iio/devices/iio:device1/out_voltage0_hardwaregain
    -6.000000 dB
   $echo -12 > /sys/bus/iio/devices/iio:device1/out_voltage0_hardwaregain
   $cat /sys/bus/iio/devices/iio:device1/out_voltage0_rf_bandwidth
    400000000

Temperature sensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The device internal temperature is available via the ``in_temp0_input``
attribute (value in milli-degrees Celsius):

.. shell::

   $cat /sys/bus/iio/devices/iio:device1/in_temp0_input
    72000

Debug facilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Debug attributes are accessible via debugfs at
``/sys/kernel/debug/iio/iio:deviceN/``.

PRBS injection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``bist_framer_0_prbs`` injects a data source into Framer 0 for JESD204 link
verification. Write the data source index to select it:

.. list-table::
   :header-rows: 1

   - - Value
     - Data source
   - - ``0``
     - ADC data
   - - ``1``
     - Checkerboard
   - - ``2``
     - Toggle 0/1
   - - ``3``
     - PRBS31
   - - ``4``
     - PRBS23
   - - ``5``
     - PRBS15
   - - ``6``
     - PRBS9
   - - ``7``
     - PRBS7
   - - ``8``
     - Ramp
   - - ``14``
     - 16-bit programmed pattern (repeat)
   - - ``15``
     - 16-bit programmed pattern (execute once)

.. shell::

   $echo 8 > /sys/kernel/debug/iio/iio:device1/bist_framer_0_prbs

Digital loopback
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``bist_framer_loopback`` routes the digital framer output directly to the
digital deframer input, bypassing the RF path:

.. list-table::
   :header-rows: 1

   - - Value
     - Mode
   - - ``0``
     - Disable loopback
   - - ``1``
     - Digital framer → digital deframer

.. shell::

   $echo 1 > /sys/kernel/debug/iio/iio:device1/bist_framer_loopback

Tone injection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``bist_tone`` injects a configurable NCO tone into the TX path. Syntax:

.. code-block:: text

   echo <enable> <frequency_Hz> <gain_index> > bist_tone

- **enable**: ``0`` = disable TX NCO, ``1`` = enable on all transmitters
- **frequency_Hz**: tone frequency in Hz
- **gain_index**:

.. list-table::
   :header-rows: 1

   - - Index
     - NCO gain
   - - ``0``
     - 0 dB
   - - ``1``
     - 6 dB
   - - ``2``
     - 12 dB
   - - ``3``
     - 18 dB
   - - ``4``
     - 24 dB
   - - ``5``
     - 30 dB
   - - ``6``
     - 36 dB
   - - ``7``
     - 42 dB
   - - ``8``
     - 48 dB

.. shell::

   $echo 1 30000000 2 > /sys/kernel/debug/iio/iio:device1/bist_tone

Direct register access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``direct_reg_access`` allows reading and writing individual device registers.
To access HDL core registers, set bit 31 of the address.

.. shell::

   $echo 0x7 > /sys/kernel/debug/iio/iio:device1/direct_reg_access
   $cat /sys/kernel/debug/iio/iio:device1/direct_reg_access
    0x40
   $echo 0x7 0x50 > /sys/kernel/debug/iio/iio:device1/direct_reg_access
   $cat /sys/kernel/debug/iio/iio:device1/direct_reg_access
    0x50
   $echo 0x80000000 > /sys/kernel/debug/iio/iio:device1/direct_reg_access
   $cat /sys/kernel/debug/iio/iio:device1/direct_reg_access
    0x80062
