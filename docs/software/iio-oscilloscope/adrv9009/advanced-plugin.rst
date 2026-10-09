.. _iio-oscilloscope adrv9009 advanced-plugin:

Advanced plugin
===============

The ADRV9009/ADRV9008 Advanced plugin works with the
:ref:`iio-oscilloscope`.
You always use the latest version if possible. Changing any field will immediately
write changes which have been made to the ADRV9009 settings to the driver,
but not to the HW unless the Save Settings button is pressed.

The ADRV9009 Advanced Plugin allows testing of different device driver
initialization options and values.
In contrast to the controls on the
:doc:`plugin` – the controls here are not part of the main driver API.

In the No-OS driver the values directly correspond to members of the
(taliseInit_t) talInit init structure. For the ADRV9009 Linux Device Driver each
control corresponds to a specific devicetree property. Since the ADRV9009 Linux
driver uses the Analog Devices provided API driver. Ultimately also for the
Linux driver maps any settings back to the taliseInit_t init structure. It's
therefore recommended to consult the **ADRV9009 User Guide** for more
information about the options provided here.

.. image:: taliseinit_t.png

See more details about :external+linux:ref:`adrv9009-customization`.

In order for the settings made on these plugin to take affect, the Save Settings
button must be pressed. It should be noted that the driver then reinitialized
the ADRV9009 from reset, which will rerun all calibrations and this may take
several seconds to complete.

.. tip::

   After you customized the driver for your application needs you can read back
   all values from the Linux debugfs:

   .. shell::

      /sys/bus/iio/devices/iio:device3
      $pwd
       /sys/bus/iio/devices/iio:device3
      $cd /sys/kernel/debug/iio/iio\:device3
      /sys/kernel/debug/iio/iio:device3
      $grep "" * | sed "s/:/ = </g" | awk '{print $0">;"}'
       adi,arm-gpio-config-en-tx-tracking-cals-enable = <0>;
       adi,arm-gpio-config-en-tx-tracking-cals-gpio-pin-sel = <0>;
       adi,arm-gpio-config-en-tx-tracking-cals-polarity = <0>;
       adi,arm-gpio-config-orx1-tx-sel0-pin-enable = <0>;
       adi,arm-gpio-config-orx1-tx-sel0-pin-gpio-pin-sel = <0>;
       adi,arm-gpio-config-orx1-tx-sel0-pin-polarity = <0>;
       adi,arm-gpio-config-orx1-tx-sel1-pin-enable = <0>;
       adi,arm-gpio-config-orx1-tx-sel1-pin-gpio-pin-sel = <0>;
       adi,arm-gpio-config-orx1-tx-sel1-pin-polarity = <0>;
       adi,arm-gpio-config-orx2-tx-sel0-pin-enable = <0>;
       adi,arm-gpio-config-orx2-tx-sel0-pin-gpio-pin-sel = <0>;
       adi,arm-gpio-config-orx2-tx-sel0-pin-polarity = <0>;
       adi,arm-gpio-config-orx2-tx-sel1-pin-enable = <0>;
       adi,arm-gpio-config-orx2-tx-sel1-pin-gpio-pin-sel = <0>;
       adi,arm-gpio-config-orx2-tx-sel1-pin-polarity = <0>;
       adi,aux-dac-enables = <0>;
       adi,aux-dac-resolution0 = <0>;
       adi,aux-dac-resolution1 = <0>;

       [ -- snip -- ]

Simply update the values at
:external+linux:ref:`adrv9009`.

For the No-OS driver the mapping can be found at
:external+linux:ref:`adrv9009-customization`.

Screenshots / Descriptions
--------------------------

Clock Settings
++++++++++++++

.. image:: adrv9009_adv_plugin_1.png

Calibrations
++++++++++++

.. image:: adrv9009_adv_plugin_2.png

TX Settings
+++++++++++

.. image:: adrv9009_adv_plugin_3.png

RX Settings
+++++++++++

.. image:: adrv9009_adv_plugin_4.png

Observation RX Settings
+++++++++++++++++++++++

.. image:: adrv9009_adv_plugin_5.png

Frequency Hopping Mode Setup
++++++++++++++++++++++++++++

.. image:: adrv9009_adv_plugin_6.png

PA Protection Settings
++++++++++++++++++++++

.. image:: adrv9009_adv_plugin_7.png

Gain Settings
+++++++++++++

.. image:: adrv9009_adv_plugin_8.png

AGC Settings
++++++++++++

.. image:: adrv9009_adv_plugin_9.png

ARM GPIO Settings
+++++++++++++++++

.. image:: adrv9009_adv_plugin_10.png

AUX DAC Settings
++++++++++++++++

.. image:: adrv9009_adv_plugin_11.png

JESD204B Settings
+++++++++++++++++

.. image:: adrv9009_adv_plugin_12.png

JESD204B Framer Settings
++++++++++++++++++++++++

.. image:: adrv9009_adv_plugin_13.png

JESD204B Deframer Settings
++++++++++++++++++++++++++

.. image:: adrv9009_adv_plugin_14.png

BIST
++++

.. image:: adrv9009_adv_plugin_15.png

BIST stands for Build-In Self-Test. Selections on this Tab take immediately
effect and therefore don’t require the Save Settings Button. Functionality
exposed here is only meant to inject test patterns/data than can be used to
validate the Digital Interface or functionality of the device.

There are three major facilities.

BIST TX NCO Tone
~~~~~~~~~~~~~~~~

User selectable tone with frequency in kHz, that can be injected into the TX
path.

BIST PRBS
~~~~~~~~~

Patterns and Pseudorandom Binary Sequence (PRBS) that can be injected into the
RX path.
