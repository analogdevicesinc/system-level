.. _fmcxmwbr1 prerequisites:

Prerequisites
===============================================================================

Required hardware
-------------------------------------------------------------------------------

For the ADRV9009-ZU11EG example setup:

#. :adi:`AD-FMCXMWBR1-EBZ` kit (FMC bridge board, protoplate interface board,
   ribbon cable, custom power cable)
#. :adi:`ADRV9009-ZU11EG RF-SOM <ADRV9009-ZU11EG>` with heat plate and heat
   sink fitted
#. :adi:`ADRV2CRR-FMC` carrier board
#. `TE150A1251F01
   <https://www.digikey.com/en/products/detail/sl-power-electronics-manufacture-of-condor-ault-brands/TE150A1251F01/9856910>`_
   power supply (or similar)
#. SD card (16GB or larger)
#. Ethernet cable for network connection
#. USB Type C to Type A adapter
#. USB 3.0 Hub
#. Keyboard
#. Display port monitor and cable

For use with other carriers or controllers:

#. :adi:`AD-FMCXMWBR1-EBZ` kit
#. An FPGA carrier platform with FMC connector, or a RaspberryPi-compatible
   controller (such as the
   `X-MW controller
   <https://www.xmicrowave.com/documentation/x-mwcontroller-touch-interface/>`_)
#. `32x32 X-Microwave Prototype plate
   <https://www.xmicrowave.com/product/xm-pp2-3232-01/>`_ (for protoplate
   interface board)

Required software
-------------------------------------------------------------------------------

The setup requires an SD card imaged with ADI Kuiper Linux. Pre-built artifacts
for the :adi:`AD-FMCXMWBR1-EBZ` HDL project are not currently available.
Users must compile the HDL project and Linux kernel components manually.

-  SD card imaged with :external+kuiper:doc:`Kuiper Linux <index>`
-  UART terminal application (115200 baud, 8N1)
-  Vivado for HDL project compilation (see
   `Release notes <https://github.com/analogdevicesinc/hdl/releases>`_ for
   version requirements)

.. important::

   ADI does not offer FPGA carrier platforms for sale or loan. Users must
   source their own evaluation hardware.
