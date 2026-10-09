.. _adrv9364z7020 prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

#. The :adi:`ADRV9364-Z7020 <ADRV9364>` SOM, which integrates a Xilinx
   Zynq®-7020 SoC and the AD9364 RF transceiver.

#. A carrier board for the SOM. The supported carriers are:

   - :adi:`ADRV1CRR-BOB` — Break-Out Board carrier (CMOS or LVDS mode)
   - :doc:`ADRV1CRR-PACKRF </solutions/reference-designs/pzsdr/carriers/packrf>` PackRF carrier, LVDS
     mode (OBSOLETE)

#. Some way to interact with the platform, which normally includes:

   - HDMI monitor
   - USB Keyboard
   - USB Mouse

#. Internet connection (without proxies makes things much easier) to update the
   scripts/binaries on the SD card (firewalls are OK, proxies make things a
   pain).

#. RF test equipment.

#. An SD card with at least 16GB of memory imaged with
   :external+kuiper:doc:`Kuiper Linux <index>`.
