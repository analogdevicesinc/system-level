.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv904x/dpd/adrv904x_dpd_capabilities

.. _adrv904x dpd adrv904x_dpd_capabilities:

NO TITLE
========

This page captures the capabilities of ADRV904x compared with the previous
generation integrated DFE transceiver AD9029.

.. list-table::
   :header-rows: 1

   * - **Specification**
     - **ADRV9029**
     - **ADRV904x**
   * - Maximum Tx Signal IBW supported
     - 200 MHz
     - 400 MHz
   * - Technology node
     - 28 nm
     - 16 nm
   * - Maximum DPD Sample Rate
     - 1 GHz
     - 2 GHz
   * - Actuator Platform
     - GMP 32 LUTs
     - GMP + **DDR** 49 LUTs
   * - No. of DPD Coefficients
     - 95
     - 255 (including DDR)
   * - Adaptation Rate per Tx Channel
     - 1s
     - ~250ms
   * - CFR Support
     - Yes
     - Yes
   * - Post CFR Gain
     - No
     - Yes
   * - Dedicated HW for GaN PA Support
     - No
     - Yes
   * - Typical Applications
     - Small Cell, M-MIMO and Macro-cell 4G and 5G systems
     - Small Cell, M-MIMO and Macro-cell 4G and 5G systems
   * - Processor
     - \*Dedicated ARM M4 Processor for DPD
     - \* Dedicated quad core A55 Processor for DPD with 8MB memory
   * -
     - \*96x96 HW Correlator
     - \* 256x256 HW Correlator + HW Feature Filter
   * -
     -
     - \* Dedicated HW for Charge Trapping Correction on GaN PAs

**NOTE:** DDR Stands for Dynamic Deviation Reduction based Volterra Series that
effectively compensates for memory effects in wide bandwidth PAs
