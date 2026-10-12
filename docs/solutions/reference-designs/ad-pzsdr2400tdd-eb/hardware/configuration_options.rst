Configuration Options
=====================

Several GPO and GPIO pins are brought to the RF card through connector J2,
found on the bottom of the PCB. These pins allow configuration of the PA, LNA
and SPDT switch found on the PCB. These devices are summarized in the table
below.

.. list-table::
   :header-rows: 1
   :widths: 15 12 35 10 28

   * - Control Name
     - Location
     - Device Controlled
     - Value
     - Action
   * - RF_GPIO0
     - P2 - 31
     - PA Channel #1 (:adi:`HMC921`)
     - 0/1
     - Disabled/Enabled
   * - RF_GPIO0
     - P2 - 31
     - PA Channel #2 (:adi:`HMC921`)
     - 0/1
     - Disabled/Enabled
   * - AD9361_GPO0
     - P2 - 09
     - LNA Channel #1 (:adi:`HMC669`)
     - 0/1
     - Bypassed/Enabled
   * - AD9361_GPO1
     - P2 - 11
     - LNA Channel #2 (:adi:`HMC669`)
     - 0/1
     - Bypassed/Enabled
   * - AD9361_GPO3
     - P2 - 15
     - SPDT Switch (:adi:`HMC546`)
     - 0/1
     - RFC to TX/RFC to RX
