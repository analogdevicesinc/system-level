.. _eval-ad9783 prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD39783-based evaluation board: :adi:`EVAL-AD9783`

#. 5 V 1 A Power supply for the evaluation board

#. A supported FPGA carrier platform, currently 
   :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>` on HPC0

#. Or :adi:`SDP-H1 <EVAL-SDP-CH1Z>` Board / :adi:`ADS7-V2 <ADS7-V2EBZ>` Board

#. :adi:`AD-DAC-FMC-ADP` High-Speed DAC Evaluation Board to FMC Adapter Board

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - HDMI or DisplayPort monitor
      - USB Keyboard
      - USB Mouse

   #. for the FPGA only solutions, this includes:

      - LAN cable (Ethernet)
      - Host PC (Windows or Linux)

#. Internet connection (without proxies makes things much easier) to update
   the scripts/binaries on the SD card that came with the ADI FMC Card
   (firewalls are OK, proxies make things a pain).

#. RF Test Equipment:

   - RF spectrum analyzer or signal analyzer (to measure and visualize the
     DAC output spectrum and performance)
   - High-Frequency Continuous Wave Generator (Clock Source)
   - SMA cables

#. An SD card with at least 16GB of memory (in case you're using Linux). You
   should have received one when purchasing the evaluation board.

#. Banana Plug Cables

#. The following are to be included:

   #. if using :adi:`SDP-H1` Evaluation Kit:

      - 12 V 1 A Wall Adapter
      - USB-A to USB-Mini Cable

   #. if using :adi:`ADS7-V2` Evaluation Kit:

      - 12 V power supply
      - Power cord
      - USB-A to USB-B cable

Software prerequisites
-------------------------------------------------------------------------------

The following software is needed on the host PC:

- A UART terminal (e.g. PuTTY, Tera Term, Minicom) configured for
  115200 baud, 8N1
- A microSD card flashed with the ADI Kuiper Linux image; follow
  :external+kuiper:doc:`this guide <index>`

For capturing and visualizing data from the device:

#. :adi:`ACE` and :adi:`DPG Lite` Software Applications
#. :ref:`iio-oscilloscope`, a graphical
   tool for capturing and visualizing IIO device data

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   obtaining one is part of the normal evaluation or development process.
