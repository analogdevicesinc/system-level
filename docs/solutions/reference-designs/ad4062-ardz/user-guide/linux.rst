.. _eval-ad4062-ardz linux:

Linux User Guide
================

This user guide uses :external+linux:doc:`index` and supports the carriers
Digilent Cora Z7S and Terasic DE10-Nano. For linux, see
:ref:`eval-ad4062-ardz no-OS`.

Building the firmware
---------------------

Follow the :ref:`Kuiper Linux <kuiper>` documentation to prepare an SD card
with the latest Kuiper image. The AD4062 Linux driver and devicetree are
included in recent Kuiper releases.

Devicetree
----------

Since I3C is a discoverable protocol, the devicetree node is optional,
still, for optional nodes, follow the documentation at
:git-linux:`Documentation/devicetree/bindings/iio/adc/adi%2Cad4062.yaml`.

For the HDL I3C controller, see
:git-linux:`b4/ad4062:Documentation/devicetree/bindings/i3c/adi%2Ci3c-master.yaml`.

Hardware setup
--------------

After flashing the SD Card with Linux, set up the hardware with following steps:

* Disconnect both the evaluation board and the carrier from all power sources.
* Add the SD Card to the carrier.
* Connect the evaluation board to the carrier using the Arduino Uno compatible
  headers (there is only one position where all pins are connected).
* Check jumpers and powering on instructions specific for the carrier.
* When powering the evaluation board from the carrier, follow:

  - Set JP2 jumper on the evaluation board to the +5V position.
    This position connects the evaluation board power management circuitry to
    the +5 V pin on the Arduino Uno power header.
  - Connect the carrier to a PC with a USB cable,
    the evaluation board DS1 LED should turn on, as well as other LEDs on the carrier.

* When powering the evaluation board from an external power supply, follow:

  - Set JP2 jumper on the evaluation board to the VIN position.
    This position connects the evaluation board power management circuitry to
    the VIN pin on the Arduino Uno power header.
  - Power on the carrier via the external power supply option (in general,
    via a DC jack),
    the evaluation board DS1 LED should turn on, as well as other LEDs on the carrier.
  - Connect the carrier to a PC with a USB cable.

I3C Address Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

The AD4060/AD4062 include three digital input pins ADDR0, ADDR1, and ADDR2.
The ADDR[2:0] pins enable the assignment of up to eight unique part instance
values to support up to eight AD4060/AD4062s on one I3C bus.

The evaluation board's jumpers JP11, JP12, and JP10 allow for setting the
ADDR0, ADDR1, and ADDR2 respectively to either VIO or GND.

Flashing the firmware
---------------------

These steps are done before the hardware setup, with the board powered off.

For both CoraZ7S and DE10-Nano, prepare an SD Card with :ref:`Kuiper Linux <kuiper>`.


The AD4062 devicetree and driver are not yet included in Kuiper releases.
Use custom kernel build, see the :ref:`Linux kernel build guide <linux-kernel>`
and :external+hdl:ref:`HDL build guide <build_hdl>`.

The linux driver can be obtained from the
`patch series on linux-iio <https://lore.kernel.org/linux-iio/20251227163506.2fb90815@jic23-huawei/>`__.

Insert the SD Card into the powered-off carrier and follow the hardware setup
steps.

Quick start
-----------

Connect a precision signal source or signal generator to
the analog input Subminiature Version A (SMA) connectors to drive
the AD4060/AD4062 inputs into their specified operating ranges.

.. figure:: signal-bias.png
   :width: 400
   :align: left

   Biasing the EVAL-AD4062-ARDZ Inputs Without Signal Generator Hardware for
   Software Validation

If no signal generator is available, a jumper cable between the
VREF and VCM test points can be used to bias the AD4060/
AD4062 analog inputs to VREF. This is preferred over connecting
the amplifier inputs to GND, because the amplifier VEE rails are
connected to GND by default.

.. clear-content::

Evaluation board hardware
-------------------------

The evaluation board includes the AD4060/AD4062 with companion circuitry
for an out-of-the-box evaluation experience:

* **ADC**: AD4060BCPZ/AD4062BCPZ (14-lead LFCSP)
* **Voltage reference**: :adi:`MAX6070` 2.5V low-noise reference
* **Amplifiers**: Two :adi:`MAX44260` low-power, rail-to-rail op amps
* **Power regulator**: :adi:`ADP7118` 3.3V LDO regulator

Digital Interface
~~~~~~~~~~~~~~~~~

The AD4060/AD4062 digital interface includes:

* **I3C bus**: For reading and writing data (SDA and SCL on Arduino headers)
* **GP0/GP1**: Two programmable GPIOs with multiple functions:

  - Data Ready (RDY) signal
  - Threshold interrupt (GP_INTR)
  - Device enable (DEV_EN) for AFE power cycling
  - Static high/low outputs
  - GPIO controller functionality (Linux only)

* **EEPROM**: On-board I2C EEPROM for board identification

Power Domains
~~~~~~~~~~~~~

The evaluation board operates on the following power domains:

.. list-table::
   :header-rows: 1

   * - Power Rail
     - Source
     - Default Voltage
   * - +5V/VIN
     - Arduino header (from carrier)
     - 5V
   * - VSUPPLY
     - ADP7118 LDO regulator
     - 3.3V
   * - VDD
     - VSUPPLY (via JP8)
     - 3.3V
   * - VIO
     - IOREF from carrier (via JP1)
     - 3.3V
   * - VREF
     - MAX6070 reference
     - 2.5V

For more detailed hardware information, see the
:adi:`EVAL-AD4060/AD4062 User Guide <media/en/technical-documentation/user-guides/eval-ad4060_ad4062.pdf>`.

Interfacing with IIO
--------------------

The Linux IIO driver provides a complete feature set for the AD4060/AD4062,
including threshold events, triggers, and GPIO controller support.

For language bindings and high level GUI tools see :ref:`eval-ad4062-ardz tools`.

Device enumeration
~~~~~~~~~~~~~~~~~~

On the carrier Linux shell:

.. shell::

   $iio_info

Or from a host PC via Ethernet:

.. shell::

   $iio_info -u ip:192.168.2.1

The device appears as ``ad4062`` or ``ad4060`` depending on the part.

Available channels
~~~~~~~~~~~~~~~~~~

The Linux driver exposes a single channel:

* **voltage0**: Differential voltage input channel

Channel attributes
~~~~~~~~~~~~~~~~~~

The channel provides the following standard IIO attributes:

.. list-table::
   :header-rows: 1

   * - Attribute
     - Access
     - Description
   * - ``raw``
     - Read
     - Raw ADC value
   * - ``scale``
     - Read
     - Scale factor to convert raw to mV (based on VREF)
   * - ``calibscale``
     - Read/Write
     - Hardware gain calibration factor
   * - ``oversampling_ratio``
     - Read/Write
     - Burst averaging ratio (1, 2, 4, 8, 16, ...)
   * - ``oversampling_ratio_available``
     - Read
     - List of supported oversampling ratios
   * - ``sampling_frequency``
     - Read/Write
     - Effective sampling frequency in Hz
   * - ``sampling_frequency_available``
     - Read
     - List of available sampling frequencies

Reading voltage
~~~~~~~~~~~~~~~

Read the raw ADC value:

.. shell::

   $iio_attr -c ad4062 voltage0 raw

Read the scale factor:

.. shell::

   $iio_attr -c ad4062 voltage0 scale

Calculate the voltage in mV: ``voltage_mV = raw * scale``

Configuring oversampling
~~~~~~~~~~~~~~~~~~~~~~~~~

View available oversampling ratios:

.. shell::

   $iio_attr -c ad4062 voltage0 oversampling_ratio_available

Set oversampling ratio (value 1 disables oversampling):

.. shell::

   $iio_attr -c ad4062 voltage0 oversampling_ratio 8

.. note::

   When oversampling is enabled (ratio > 1), the device enters burst averaging
   mode, which increases the resolution but reduces the effective sample rate.

Configuring sampling frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

View available sampling frequencies for the current oversampling ratio:

.. shell::

   $iio_attr -c ad4062 voltage0 sampling_frequency_available

Set the sampling frequency:

.. shell::

   $iio_attr -c ad4062 voltage0 sampling_frequency 1000000

.. note::

   The available sampling frequencies depend on the current oversampling ratio.
   Changing the oversampling ratio will update the list of available frequencies.

Hardware gain calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~

The device supports hardware gain calibration to compensate for system gain errors:

.. shell::

   # Read current calibration scale
   $iio_attr -c ad4062 voltage0 calibscale

   # Set calibration scale (normalized value)
   $iio_attr -c ad4062 voltage0 calibscale 1.005

IIO buffered data capture
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Linux driver supports buffered data acquisition using IIO triggers.

Attach the trigger
^^^^^^^^^^^^^^^^^^

The driver automatically registers a trigger named ``ad4062-dev0`` (or similar).
Before enabling the buffer, attach the trigger:

.. shell::

   # Find the trigger name
   $ls /sys/bus/iio/devices/trigger*/name

   # Set the current trigger
   $echo ad4062-dev0 > /sys/bus/iio/devices/iio:device0/trigger/current_trigger

Enable the buffer
^^^^^^^^^^^^^^^^^

.. shell::

   # Enable the channel for buffered capture
   $echo 1 > /sys/bus/iio/devices/iio:device0/scan_elements/in_voltage0_en

   # Set the buffer size
   $echo 256 > /sys/bus/iio/devices/iio:device0/buffer/length

   # Enable the buffer
   $echo 1 > /sys/bus/iio/devices/iio:device0/buffer/enable

Read buffered data
^^^^^^^^^^^^^^^^^^

Using iio_readdev:

.. shell::

   $iio_readdev -s 1024 -b 256 ad4062 voltage0 > data.bin

.. important::

   The trigger **must** be attached before enabling the buffer, otherwise the
   buffer will not capture data.

Threshold event monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD4060/AD4062 support autonomous threshold monitoring. When enabled, the
device continuously samples and compares the result against programmable
thresholds, generating an event when the threshold is crossed.

.. note::

   During threshold monitoring (monitor mode), the device operates autonomously.
   Any register access temporarily exits monitor mode. The Linux driver manages
   this automatically.

Event attributes
^^^^^^^^^^^^^^^^

Threshold events are configured through event attributes under the channel:

.. shell::

   # List event attributes
   $ls /sys/bus/iio/devices/iio:device0/events/

Available event attributes:

.. list-table::
   :header-rows: 1

   * - Attribute
     - Access
     - Description
   * - ``in_voltage0_thresh_either_en``
     - Read/Write
     - Enable threshold monitoring (0=disabled, 1=enabled)
   * - ``in_voltage0_thresh_rising_value``
     - Read/Write
     - Upper threshold value (raw ADC counts)
   * - ``in_voltage0_thresh_rising_hysteresis``
     - Read/Write
     - Hysteresis for upper threshold
   * - ``in_voltage0_thresh_falling_value``
     - Read/Write
     - Lower threshold value (raw ADC counts)
   * - ``in_voltage0_thresh_falling_hysteresis``
     - Read/Write
     - Hysteresis for lower threshold
   * - ``sampling_frequency``
     - Read/Write
     - Sampling frequency during monitor mode
   * - ``sampling_frequency_available``
     - Read
     - List of available monitor mode frequencies

Setting thresholds
^^^^^^^^^^^^^^^^^^

.. shell::

   # Set upper threshold (rising)
   $iio_attr -c ad4062 voltage0 events/thresh_rising_value 30000

   # Set upper threshold hysteresis
   $iio_attr -c ad4062 voltage0 events/thresh_rising_hysteresis 500

   # Set lower threshold (falling)
   $iio_attr -c ad4062 voltage0 events/thresh_falling_value 10000

   # Set lower threshold hysteresis
   $iio_attr -c ad4062 voltage0 events/thresh_falling_hysteresis 500

Configuring monitor mode sampling frequency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shell::

   # View available frequencies
   $iio_attr -c ad4062 voltage0 events/sampling_frequency_available

   # Set monitor mode frequency
   $iio_attr -c ad4062 voltage0 events/sampling_frequency 100000

Enabling threshold monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shell::

   # Enable threshold monitoring
   $iio_attr -c ad4062 voltage0 events/thresh_either_en 1

   # Disable threshold monitoring
   $iio_attr -c ad4062 voltage0 events/thresh_either_en 0

Reading events
^^^^^^^^^^^^^^

Events can be read from the character device:

.. shell::

   # Monitor events (blocking read)
   $cat /dev/iio:device0

Or use ``iio_event_monitor`` if available:

.. shell::

   $iio_event_monitor ad4062

.. important::

   While threshold monitoring is enabled, normal ADC reads are not available.
   Disable monitoring to return to regular sampling mode.

GPIO controller
~~~~~~~~~~~~~~~

When configured in the device tree, the GP0 and GP1 pins can be exposed as
GPIO outputs. The GPIO controller feature allows you to control these pins
as general-purpose outputs.

Device tree configuration
^^^^^^^^^^^^^^^^^^^^^^^^^

To enable GPIO controller support, add the ``gpio-controller`` property to the
device node in the device tree:

::

   &i3c0 {
       adc@0,2ee007c0000 {
           compatible = "adi,ad4062";
           reg = <0x0 0x2ee 0x7c0000>;
           vdd-supply = <&vdd>;
           vio-supply = <&vio>;
           ref-supply = <&ref>;

           gpio-controller;
           #gpio-cells = <2>;
       };
   };

GPIO indexing
^^^^^^^^^^^^^

The GPIO indices match the physical pin numbers:

* GPIO 0 = GP0
* GPIO 1 = GP1

If a GP pin is configured as an interrupt in the ``interrupt-names`` property,
it is **not** available as a GPIO.

Using GPIOs from userspace
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shell::

   # Export GPIO 1 (GP1)
   $echo 1 > /sys/class/gpio/export

   # Set direction to output
   $echo out > /sys/class/gpio/gpio1/direction

   # Set value high
   $echo 1 > /sys/class/gpio/gpio1/value

   # Set value low
   $echo 0 > /sys/class/gpio/gpio1/value

   # Unexport when done
   $echo 1 > /sys/class/gpio/unexport

Low-power mode
~~~~~~~~~~~~~~

The Linux driver automatically manages low-power mode. When the device is idle
(not actively sampling), it enters low-power mode to reduce power consumption.

Threshold event monitoring disables low-power mode, as the device must
continuously sample to detect threshold crossings.

References
----------

* :adi:`AD4060 Product Page <AD4060>`
* :adi:`AD4062 Product Page <AD4062>`
* :adi:`AD4060 Datasheet <media/en/technical-documentation/data-sheets/ad4060.pdf>`
* :adi:`AD4062 Datasheet <media/en/technical-documentation/data-sheets/ad4062.pdf>`
* :adi:`EVAL-AD4060-ARDZ Product Page <EVAL-AD4060-ARDZ>`
* :adi:`EVAL-AD4062-ARDZ Product Page <EVAL-AD4062-ARDZ>`
* :adi:`Evaluation Guide (UG-2318) <media/en/technical-documentation/user-guides/eval-ad4060_ad4062.pdf>`
* :external+hdl:ref:`HDL Project Documentation <ad4062_ardz>`
* :git-linux:`Linux Driver Source <main:drivers/iio/adc/ad4062.c>`
* :git-linux:`Linux Driver Documentation <main:Documentation/iio/ad4062.rst>`
* :git-linux:`Linux Devicetree Bindings <main:Documentation/devicetree/bindings/iio/adc/adi,ad4062.yaml>`
* :external+no-OS:doc:`no-OS Driver Documentation <drivers/adc/ad405x>`
* :external+no-OS:doc:`no-OS Project Documentation <projects/adc/ad405x>`
