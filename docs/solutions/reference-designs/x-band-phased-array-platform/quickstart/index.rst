.. _xbdp quickstart:

Quick start
===============================================================================

The Quick start guides provide simple step by step instructions on how to do
an initial system setup for the :adi:`X-Band Phased Array Platform <resources/evaluation-hardware-and-software/evaluation-boards-kits/x-band-development-platform>`
on various FPGA development boards. In these guides, we will discuss how
to boot a Linux distribution.

.. toctree::

   On ZCU102 <zcu102>

.. _xbdp carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`X-Band Phased Array Platform <resources/evaluation-hardware-and-software/evaluation-boards-kits/x-band-development-platform>`
includes the :adi:`EVAL-AD9081` evaluation board, as well as an interposer,
which are, by definition, "FPGA mezzanine cards" (FMC); that means it needs a
carrier to plug into.

The carriers we support are listed below, as well as the FMC port where to
connect the evaluation board and the interposer:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - AD9081-FMCA-EBZ
     - Interposer
   * - :xilinx:`ZCU102`
     - FMC HPC0
     - FMC HPC1

Supported Environments
-------------------------------------------------------------------------------

The supported OS are:

.. list-table::
   :header-rows: 1

   * - FPGA board
     - HDL
     - Linux software
     - No-OS software
   * - :xilinx:`ZCU102`
     - Yes
     - Yes
     - ---

Hardware Setup
-------------------------------------------------------------------------------

The :adi:`X-Band Phased Array Platform <resources/evaluation-hardware-and-software/evaluation-boards-kits/x-band-development-platform>`
contains one :adi:`AD9081-FMCA-EBZ (MxFE) <eval-ad9081>` Evaluation Board,
one :ref:`xud1a`, and one :ref:`stingray`. On most carriers, the
:adi:`EVAL-AD9081` board connects to the HPC0 connector (unless otherwise
noted). The carrier setup requires power, UART (115200), Ethernet (Linux), HDMI
(if available). A few typical setups are shown below.

ZCU102 + EVAL-AD9081 (MxFE) + X/C Band Up/Down Converter (XUD1A) + X/Ku Phased Array Prototyping Board (Stingray)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/beamformerkit.jpg
   :width: 800
