.. _ad9084 quickstart:

Quickstart
===============================================================================

The Quick Start Guides provide a simple step by step instruction on how to do an
initial system setup for the :adi:`EVAL-AD9084 <AD9084-FMCA-EBZ>` evaluation
board on various FPGA development boards. They will discuss how to program the
bitstream, run a no-OS program or boot a Linux distribution.

.. toctree::
   :maxdepth: 2

   Virtex UltraScale+ VCU118/VCU128 <microblaze>
   Versal ACAP VCK190/VPK180 <versal>
   Intel Agilex 7 I-Series <agilex>
   new_usecase

.. _ad9084 carriers:

Supported carriers
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9084 <AD9084-FMCA-EBZ>` is, by definition a "FPGA mezzanine card" (FMC),
that means it needs a carrier to plug into.
The carriers we support are:

.. list-table::
  :header-rows: 1

  - - Board
    - AD9084-FMCA-EBZ
    - Side A lanes
    - Side B lanes
    - FMC+ risers required
  - - :xilinx:`KC705`
    - No
    -
    -
    -
  - - :xilinx:`KCU105`
    - No
    -
    -
    -
  - - :xilinx:`VC707`
    - No
    -
    -
    -
  - - :xilinx:`VCU118`
    - Yes
    - 12
    - 12
    - 2
  - - :xilinx:`VCU128`
    - Yes
    - 12
    - 12
    - 2
  - - :xilinx:`VCK190`
    - Yes
    - 4
    - 4
    - 2
  - - :xilinx:`VPK180`
    - Yes
    - 4
    - 4
    - 0
  - - :xilinx:`ZCU102`
    - No
    -
    -
    -
  - - :xilinx:`ZC706`
    - No
    -
    -
    -
  - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
    - No
    -
    -
    -
  - - :intel:`Stratix 10 SoC <content/www/us/en/products/details/fpga/stratix/10.html>`
    - No
    -
    -
    -
  - - :intel:`Agilex 7 SoC I-Series <content/www/us/en/products/details/fpga/agilex/7.html>`
    - Yes
    - 8
    - 8
    - 1

Supported Environments
-------------------------------------------------------------------------------

The supported environments are:

.. list-table::
  :header-rows: 1

  - - Board
    - HDL
    - Linux Software
    - No-OS Software
  - - :xilinx:`KC705`
    -
    -
    -
  - - :xilinx:`KCU105`
    -
    -
    -
  - - :xilinx:`VC707`
    -
    -
    -
  - - :xilinx:`VCU118`
    - Yes
    - Yes
    - WIP
  - - :xilinx:`VCU128`
    - Yes
    - Yes
    - WIP
  - - :xilinx:`VCK190`
    - Yes
    - Yes
    - WIP
  - - :xilinx:`VPK180`
    - Yes
    - Yes
    - WIP
  - - :xilinx:`ZCU102`
    -
    -
    -
  - - :xilinx:`ZC706`
    -
    -
    -
  - - :intel:`Arria 10 SoC <content/www/us/en/products/details/fpga/arria/10.html>`
    -
    -
    -
  - - :intel:`Stratix 10 SoC <content/www/us/en/products/details/fpga/stratix/10.html>`
    -
    -
    -
  - - :intel:`Agilex 7 SoC I-Series <content/www/us/en/products/details/fpga/agilex/7.html>`
    - Yes
    - Yes
    - No
