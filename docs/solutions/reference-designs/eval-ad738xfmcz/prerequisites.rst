.. _eval-ad738xfmcz prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum,
you need to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. An AD738x-based evaluation board:
   :adi:`EVAL-AD7380FMCZ <EVAL-AD738xFMCZ>` / :adi:`EVAL-AD7381FMCZ <EVAL-AD738xFMCZ>` /
   :adi:`EVAL-AD7386FMCZ`
#. An FPGA carrier platform. Our recommended one can be found
   :ref:`here <eval-ad738xfmcz carriers>`.

   - There are a few more boards, which do work, but are currently
     not supported by us. The experience with the fabric-only
     solutions is very close to the ARM/FPGA SoC based solutions,
     but the GUI runs on a host PC (Windows or Linux).

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - Micro-USB cable for UART console
      - LAN cable (Ethernet) for SSH or IIO applications
      - HDMI or DisplayPort monitor (Optional)
      - USB Keyboard (Optional)
      - USB Mouse (Optional)

   #. for the FPGA-only, this includes:

      - LAN cable (Ethernet)
      - Host PC (Windows or Linux)
      - Micro-USB cable for UART
      - Micro-USB cable for JTAG (PROG)

#. Internet connection (without proxies makes things much easier) to
   update the scripts/binaries on the SD card that came with the ADI
   FMC Card (firewalls are OK, proxies make things a pain).
#. Test equipment for generating analog input signals.
#. An SD card with at least 16GB of memory (in case you're using
   Linux). You should have received one when purchasing the
   evaluation board.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding visualizing the data
received from the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain
   the IIO plugin)
#. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
#. UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or
   loan; getting one yourself is the normal part of development or
   evaluation.
