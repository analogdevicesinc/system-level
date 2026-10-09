.. _dac-fmc-ebz:

DAC-FMC-EBZ
===============================================================================

High-Speed JESD204B Digital-to-Analog Converter Evaluation Boards.

Overview
-------------------------------------------------------------------------------

The DAC-FMC-EBZ family of evaluation boards provides a platform for evaluating
Analog Devices' high-speed, JESD204B-based digital-to-analog converters (DACs).
These boards are designed to work with the :git-hdl:`AD-DAC-FMC-EBZ HDL
reference design <projects/dac_fmc_ebz>`, supporting a range of DAC devices
from the AD9135/AD9136 through the AD9172/AD9176.

The evaluation boards connect to a Data Pattern Generator (DPG3) or an ADS7-V2
controller board via DPG or FMC connectors, enabling quick characterization of
DAC performance including single-tone output, NCO frequency shifting, and
multi-carrier waveform generation.

Supported devices:

- :adi:`AD9135` / :adi:`AD9136` -- Dual, 16-bit, 2.8 GSPS DAC
- :adi:`AD9144` -- Quad, 16-bit, 2.8 GSPS DAC
- :adi:`AD9152` -- Dual, 16-bit, 2.25 GSPS DAC
- :adi:`AD9154` -- Quad, 16-bit, 2.4 GSPS DAC
- :adi:`AD9172` / :adi:`AD9174` / :adi:`AD9176` -- Dual, 16-bit, 12.6 GSPS DAC

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   ad9136/index
   ad9144/index
   ad9152/index
   ad9154/index
   ad917x/index

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board:

   #. :ref:`User Guide <dac-fmc-ebz user-guide>` -- what you need to know about
      the evaluation boards
   #. :ref:`Prerequisites <dac-fmc-ebz prerequisites>` -- what you need to get
      started with the setup
   #. :ref:`Quick Start Guides <dac-fmc-ebz quickstart>`:

      #. Using the :ref:`ZCU102 <dac-fmc-ebz quickstart zcu102>`
      #. Using the :ref:`ZC706 <dac-fmc-ebz quickstart zc706>`

#. :external+hdl:ref:`DAC-FMC-EBZ HDL Reference Design <dac_fmc_ebz>` which you
   must use in your FPGA.

#. Resources for designing a custom AD9081/AD9082-based platform software

   #. For Linux software:

      #. About the device driver:

         - :external+hdl:ref:`axi_jesd204_tx`
         - :external+hdl:ref:`axi_jesd204_rx`
         - :external+hdl:ref:`axi_adxcvr`
         - :external+linux:ref:`axi-dac-dds-hdl`
         - :external+hdl:ref:`axi_dmac`
         - :external+linux:ref:`ad9172`

      #. About the device tree:

         - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

      #. About the JESD204 utilities:

         - :external+linux:ref:`jesd204-fsm-framework`
         - :external+linux:ref:`hmc7044`
         - :doc:`JESD204 status utility </software/jesd/jesd_status>`
         - :doc:`JESD204 Eye Scan </software/jesd/jesd_eye_scan>`
         - :external+hdl:ref:`jesd204`

      #. :ref:`Building Zynq Linux kernel and devicetree <linux-kernel zynq>`
      #. :ref:`Building ZynqMP Linux kernel and devicetree <linux-kernel zynqmp>`

   #. For No-Os software:

      - :external+no-OS:doc:`projects/dac/ad9172` - no-OS project documentation

#. AD9135 / AD9136

   #. :ref:`eval-ad9136` -- overview, schematics, BOM, and design files
   #. :ref:`ace-ad9136-ebz`
   #. :ref:`ad9136-ebz`
   #. :ref:`ad9136-fmc-ebz`

#. AD9144

   #. :ref:`eval-ad9144` -- overview, schematics, BOM, and design files
   #. :ref:`ace-ad9144-ebz`
   #. :ref:`ace-ad9144-fmc-ebz`
   #. :ref:`ad9144-adrf6720-ebz`
   #. :ref:`ad9144-ebz`
   #. :ref:`ad9144-fmc-ebz`

#. AD9152

   #. :ref:`eval-ad9152` -- overview, schematics, BOM, and design files
   #. :ref:`ad9152-adrf6720-ebz`
   #. :ref:`ad9152-ebz`
   #. :ref:`ad9152-fmc-ebz`

#. AD9154

   #. :ref:`eval-ad9154` -- overview, schematics, BOM, and design files
   #. :ref:`ad9154-ace-ebz`
   #. :ref:`ad9154-ace-fmc-ebz`
   #. :ref:`ad9154-adrf6720-ebz`
   #. :ref:`ad9154-ebz`
   #. :ref:`ad9154-fmc-ebz`
   #. :ref:`ad9154-m6720-ebz`

#. AD917x

   #. :ref:`eval-ad917x`

#. :ref:`Help and Support <help-and-support>`

ADI articles
-------------------------------------------------------------------------------

About JESD standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
