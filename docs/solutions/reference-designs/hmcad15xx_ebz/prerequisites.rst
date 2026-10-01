.. _hmcad15xx prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The HMCAD1511/HMCAD1520-based evaluation board:
   :adi:`HMCAD1511-EBZ/HMCAD1520-EBZ <HMCAD1520-EBZ>`
#. An FPGA carrier platform. Our recommended ones can be found
   :ref:`here <hmcad15xx carriers>`.
#. Power supply for your carrier.
#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - HDMI or DisplayPort monitor
      - USB Keyboard
      - USB Mouse

   #. for the FPGA only solutions, this includes:

      - LAN cable (Ethernet)
      - Micro-USB (UART)
      - Host PC (Windows or Linux)

#. Internet connection (without proxies makes things much easier) to update the
   scripts/binaries on the SD card that came with the ADI FMC Card (firewalls
   are OK, proxies make things a pain).
#. Signal Generator
#. SMA male to BNC male cable
#. External 1GHz clock source if working with the :adi:`HMCAD1520-EBZ` + extra 
   SMA male to SMA male cable because the :adi:`HMCAD1520-EBZ` does not include
   an onboard crystal clock like the :adi:`HMCAD1511-EBZ`
#. An SD card with at least 16GB of memory.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding visualizing the data received
from the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.2 or later
   (must contain the ADC Plugin)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan; getting
   one yourself is the normal part of development or evaluation.
