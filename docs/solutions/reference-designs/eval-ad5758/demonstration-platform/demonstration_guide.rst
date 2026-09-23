.. _demonstration-guide:

Using the Demo Board
===============================================================================

.. warning::
   Before proceeding, please ensure you have the DEMO_AD5758-AO8Z Demo
   software installed on your PC or Laptop and that the latest version of
   the firmware has been uploaded to the board. Instructions on how to
   complete these steps can be found earlier in this guide in the :doc:`Software Details <software_details>` section.

.. figure:: ../images/artboard_1.png
   :align: center

   DEMO-AD5758-AO8Z Setup

Connecting the Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Remove Jumpers P4 & P5
2. Connect the power supplies as shown in Figure 1. The field power
   supply should be capable of supplying at least 300 mA @ 24 V. The
   system supply needs to only supply about 20 mA (max) @ 24 V
3. Alternatively, if only one power supply is available, then P4 & P5
   jumpers can be left in place and a single field supply used.

   .. danger::
      If either P4 and/or P5 jumpers are inserted, then there will be no
      isolation between the system domain and the field power domain.

4. Connect a USB cable from your PC or laptop to the USB port on the
   demo board.
5. Start the :adi:`DEMO-AD5758-AO8Z <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/demo-ad5758-ao8z.html#eb-overview>`
   GUI Software and select the correct COM
   port, then click [Connect]

.. figure:: ../images/com-connect.png
   :align: center

6. The GUI display should resemble the following image.

.. figure:: ../images/full-panel-power_up-state.png
   :align: center

DPC ON vs. DPC OFF Demonstration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Quiescent Current should be approximately:

   - IFIELD = 26 mA ± 5 mA
   - ISYSTEM = 3 mA ± 1 mA

2. Connect a 1 Ω resistors to each of eight channel headers (CH0 to
   CH7).

   .. important::
      Resistor values between 0 Ω and 1 kΩ can be used. However, lower
      values provide a more challenging load and demonstrate the DPC mode
      power savings better.

3. Turn on Channel 0 by clicking the DPC OFF radio button. This turns on
   the channel but leaves DPC mode disabled by fixing the output of the
   DPC buck (and thus the power supply to the buffer) to 23.3 V

.. figure:: ../images/dpc_off-0ma.png
   :align: center

4. Set Desired Output to 20 mA and click Apply to all. This will set the
   remaining channels to the same state as channel 0. i.e. 20 mA output,
   DPC OFF.

.. figure:: ../images/apply-to-all-dpc_off-20ma.png
   :align: center

   Observe that VDPC+ is fixed at 23.3 V even though the buffer output is at
   0 V.

5. IFIELD should now be around 207 mA ± 10 mA (~5 W). ISYSTEM should be
   relatively unchanged.

6. Click the Status button of any channel to see a graph of the internal
   die temperature rise of the AD5758. Notice how the temperature rises
   rapidly when DPC is disabled.

.. figure:: ../images/die-temperature_rise_off-to-dpc_off.png
   :align: center

.. important::
   When DPC mode is turned off, the DPC buck is programmed to output a
   fixed voltage of 23.3 V. Because the load resistance is low (1 Ω), there
   is a large voltage drop across the AD5758 output buffer. There is
   23.3V X 20mA = 466mW of power dissipated in the output buffer plus an
   additional 47 mW dissipation in the DPC buck regulator (466 mW X (1-η)).
   Which translates to 513 mW of dissipation per channel in the module.

7. Now select CH0 DPC ON

.. figure:: ../images/13-08-2019_14-17-26.png
   :align: center

8. Click "Apply to all".

.. figure:: ../images/13-08-2019_14-26-28.png
   :align: center

Notice how VDPC+ is now at its minimum value of approximately 4.95 V and
the die temperature begins to drop rapidly as DPC power saving take
effect.

.. figure:: ../images/die-temperature_fall_dpc_off-to-dpc_on-very-long.png
   :align: center

.. important::
   When DPC mode is turned on, a high efficiency (η = 0.9) buck converter
   reduces the supply to the buffer to 2.5 V above the required output
   voltage or 4.95 V - whichever is higher, so there is now a small voltage
   drop of only 4.95 V across the AD5758 output buffer. This translates to
   4.95V X 20mA = 99mW plus 99 mW X (1 - η) = 10 mW of heat dissipation in
   the output buffer of the AD5758. This is a power saving of 404 mW per
   channel.

   If VIOUT > 2.5 V, then the DPC buck tracks the output to maintain a
   fixed 2.5 V headroom.

9. IFIELD should now be around 72 mA ± 5 mA (~ 1.7 W). ISYSTEM should be
   unchanged.

Related Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`AD5758`: Single-Channel, 16-Bit Current and Voltage Output DAC with
  Dynamic Power Control and HART Connectivity
- :adi:`ADP1031`: Three-Channel, Isolated Micropower Management Unit with
  Seven Digital Isolators
- Video: `ADI: Doubling Channel Density of Industrial Output Modules
  <https://www.youtube.com/watch?v=3jvZrx5-yEY>`__
- Video: `Analog Devices: AD5758 DAC for EMC/EMI Robustness
  <https://www.youtube.com/watch?v=QbfdilQjfNY>`__
