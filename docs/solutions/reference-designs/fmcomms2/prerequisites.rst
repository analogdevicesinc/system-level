.. _fmcomms2 prerequisites:

Prerequisites for AD9361/AD9364 based boards
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD9361/AD9364-based evaluation boards: :adi:`EVAL-AD-FMCOMMS2` /
   :adi:`EVAL-AD-FMCOMMS3` / :adi:`EVAL-AD-FMCOMMS4`

   To determine which one is best for you, check out the
   :ref:`introduction <fmcomms2 common introduction>` section.

#. A FPGA carrier platform. Our recommended one can be found
   :ref:`here <fmcomms2/3/4 carriers>`.

   - There are a few more boards, which do work, but are currently not
     supported by us. The experience with the fabric-only solutions is very
     close to the ARM/FPGA SoC based solutions, but the GUI runs on a host PC
     (Windows or Linux).

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - Micro‑USB cable for UART console
      - LAN cable (Ethernet) for SSH or IIO applications
      - HDMI monitor (1080p is best) or VGA monitor (Optional)
      - USB Keyboard (Optional)
      - USB Mouse (Optional)

   #. for the FPGA-only solutions, this includes:

      - LAN cable (Ethernet)
      - Host PC (Windows or Linux)
      - Micro‑USB cable for UART
      - Micro‑USB cable for JTAG (PROG)

#. Internet connection (without proxies makes things much easier) to update
   the scripts/binaries on the SD card that came with the ADI FMC Card
   (firewalls are OK, proxies make things a pain).
#. RF test equipment for generating signals within the operating frequency
   range.
#. An SD card with at least 16GB of memory (in case you're using Linux). You
   should have received one when purchasing the evaluation board.

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding visualizing the data received
from the FPGA, we use the following:

#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must contain the IIO
   plugin)
#. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
#. UART terminal application (PuTTY/TeraTerm/Minicom), 115200 8N1

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
