.. _dac-fmc-ebz prerequisites:

Prerequisites
===============================================================================

Hardware Prerequisites
-------------------------------------------------------------------------------

#. One of the DAC-FMC-EBZ evaluation boards:

   - :adi:`EVAL-AD9135` / :adi:`EVAL-AD9136`
   - :adi:`EVAL-AD9144`
   - :adi:`EVAL-AD9152`
   - :adi:`EVAL-AD9154`
   - :adi:`EVAL-AD9172` (AD917x-FMC-EBZ)

#. One of the following FPGA carrier platforms:

   - `ZCU102 <https://www.xilinx.com/ZCU102>`_
   - `ZC706 <https://www.xilinx.com/ZC706>`_
   - `VCU118 <https://www.xilinx.com/VCU118>`_
   - `Arria 10 SoC Development Kit <https://www.altera.com/products/devkit/po-3006/arria-10-sx-soc-development-kit>`__

   .. note::

      ADI does not sell or loan FPGA carrier platforms. These must be purchased
      separately from the FPGA vendor.

#. Depending on the carrier platform and interaction method:

   - For ARM/FPGA SoC carriers (ZCU102, ZC706, A10SoC): HDMI/DisplayPort
     monitor, USB keyboard, USB mouse
   - For all carriers: LAN cable and host PC

#. RF test equipment:

   - Spectrum analyzer
   - Signal generator (low phase noise clock source)
   - SMA cables

#. SD card with at least 16GB of memory

Software Prerequisites
-------------------------------------------------------------------------------

- :dokuwiki:`Analysis | Control | Evaluation (ACE) Software
  <resources/tools-software/ace>` -- for DPG3/ADS7-based evaluation
- :dokuwiki:`DPG Downloader <resources/eval/dpg/dpgdownloader>` -- for vector
  generation and download
- For Linux-based evaluation: ADI Kuiper Linux SD card image
