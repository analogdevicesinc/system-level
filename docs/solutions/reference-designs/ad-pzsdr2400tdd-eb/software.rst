Linux Software
==============

Configuring
-----------

When using this card on the
:adi:`PicoZed SDR SOM Development Kit <adrv9361-z7035>`, a slightly different
device tree must be used (zynq-picozed-sdr2-fmc-rfcard-tdd). Please see here
for further details: :external+kuiper:doc:`Preparing the Image <index>`

.. list-table::
   :header-rows: 1

   * - Function
     - File
   * - FMCOMMS2/3 Device Tree
     - :git-linux:`arch/arm/boot/dts/zynq-picozed-sdr2-fmc-rfcard-tdd.dts`
   * - ZYNQ ADRV9361 z7035 FMC RFCARD TDD Device Tree
     - :git-linux:`arch/arm/boot/dts/zynq-adrv9361-z7035-fmc-rfcard-tdd.dts`

This device tree includes the devicetree for the PicoZed SDR SOM Development
Kit but configures the AD9361:

- For TDD mode.
- Sets TX LO frequency to RX LO frequency.
- Enables AD9361 GPO2 and GPO3 to slave the ENSM RX & TX states.
- Enables AD9361 GPO0 and GPO1 to control the external LNAs for RX1 & RX2.
- Configures LNA gain and bypass loss.
