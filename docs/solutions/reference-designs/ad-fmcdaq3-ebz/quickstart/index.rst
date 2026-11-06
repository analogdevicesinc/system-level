.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart

.. _ad_fmcdaq3_ebz quickstart:

Quickstart
==========

The Quick start guides provide simple step by step instructions on how to do an
initial system setup for the :adi:`AD-FMCDAQ3-EBZ` boards on various FPGA
development boards. In these guides, we will discuss how to program the
bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::
   :maxdepth: 1

   On KCU105 <kcu105>
   On VCU118 <vcu118>
   On ZC706 <zc706>
   On ZCU102 <zcu102>

.. _ad_fmcdaq3_ebz carriers:

Supported carriers
------------------

The :adi:`AD-FMCDAQ3-EBZ` is an FMC (FPGA Mezzanine Card), meaning it requires a
compatible carrier board. The officially supported carriers are listed below, as
documented in the ADI Quick Start Guides.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - EVAL-AD-FMCDAQ3-EBZ
   * - :xilinx:`KCU105`
     - FMC HPC
   * - :xilinx:`VCU118`
     - FMC+
   * - :xilinx:`ZC706`
     - FMC HPC
   * - :xilinx:`ZCU102`
     - FMC HPC0

Supported environments
----------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - :xilinx:`KCU105`
     - Yes
     - Yes
     - ---
   * - :xilinx:`VCU118`
     - Yes
     - Yes
     - ---
   * - :xilinx:`ZC706`
     - Yes
     - Yes
     - Yes
   * - :xilinx:`ZCU102`
     - Yes
     - Yes
     - Yes

Hardware setup
--------------

On most carriers, the :adi:`AD-FMCDAQ3-EBZ` board connects to the HPC connector
(unless otherwise noted). The carrier setup requires power, UART (115200),
ethernet (for Linux), HDMI (if available) and/or JTAG (for no‑OS). A few typical
setups are shown below.

KCU105 + AD-FMCDAQ3-EBZ
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./../images/kcu105_daq3.jpg
   :width: 900

VCU118 + AD-FMCDAQ3-EBZ
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./../images/vcu118_daq3.jpg
   :width: 900

ZC706 + AD-FMCDAQ3-EBZ
~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/ad-fmcdaq3-ebz_zc706.png
   :width: 900

ZCU102 + AD-FMCDAQ3-EBZ
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./../images/zcu102_fmcdaq3.jpg
   :width: 900
