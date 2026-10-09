.. _ad9467_fmc_250ebz:

EVAL-AD9467-FMC-250EBZ
===============================================================================

16-bit, IF Sampling Analog-to-Digital Converter.

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9467` is an FMC radio card
designed to showcase the :adi:`AD9467`, a 16-bit, monolithic, IF sampling
analog-to-digital converter (ADC) with a conversion rate of up to 250 MSPS.
This reference design includes a data capture interface and an external
DDR-DRAM interface for sample storage. It allows programming the device and
monitoring its internal status registers.

The board provides multiple clock path options for clocking the :adi:`AD9467`,
and configurable analog input conditioning through the :adi:`ADL5565` differential
amplifier.

Features:

- 16-bit, IF sampling ADC
- Conversion rate up to 250 MSPS
- LVDS data interface with buffering and DMA transfer capability
- External DDR-DRAM interface for sample storage
- Multiple clock path options:

  - Default transformer-coupled clock input
  - Crystal oscillator option
  - AD9517-4 clock generator (LVPECL or LVDS)

- SPI interface for device configuration and status monitoring
- Configurable analog input with differential amplifier

Applications:

- IF sampling in communications systems
- Wideband signal capture
- RF measurement and monitoring
- Signals intelligence (SIGINT)

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

.. image:: ./images/ad9467.png
   :width: 400

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9467`, we recommend to use the
:adi:`EVAL-AD9467` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/reference design that we offer:

   #. :ref:`Prerequisites <ad9467_fmc_250ebz prerequisites>` - what you need to
      get started
   #. :ref:`Quick start guides <ad9467_fmc_250ebz quickstart>`:

      #. Using the :ref:`ZedBoard <ad9467_fmc_250ebz quickstart zed>`
      #. Using the :ref:`ZCU102 <ad9467_fmc_250ebz quickstart zcu102>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD9467

   - :adi:`AD9467 product page <AD9467>`
   - :adi:`Full data sheet <media/en/technical-documentation/data-sheets/ad9467.pdf>`

   - Hardware in the Loop / How to design your own custom BaseBand

     - :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
     - :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   - Resources for designing custom AD9467-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+hdl:ref:`AXI_AD9467 IP documentation <axi_ad9467>`
           - :dokuwiki:`AD9467 Linux driver <resources/tools-software/linux-drivers/iio-adc/ad9467>`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`
           - :ref:`Building Zynq Linux kernel and devicetree <linux-kernel zynq>`
           - :ref:`Building ZynqMP Linux kernel and devicetree <linux-kernel zynqmp>`

     #. :external+hdl:ref:`HDL reference design <ad9467_fmc>`
        which you must use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

Additional information
-------------------------------------------------------------------------------

- :adi:`EVAL-AD9467`
- :adi:`UG-200 FMC Interposer User Guide <media/en/technical-documentation/user-guides/UG-200.pdf>`
- :git-hdl:`AD9467_FMC HDL project source code <projects/ad9467_fmc>`
  with ZedBoard and ZCU102 carriers
- :git-linux:`AD9467_FMC/Zed Linux devicetree <arch/arm/boot/dts/xilinx/zynq-zed-adv7511-ad9467-fmc-250ebz.dts>`
- :git-linux:`AD9467_FMC/ZCU102 Linux devicetree <arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-ad9467-fmc-250ebz.dts>`
- :git-linux:`AD9467 Linux driver <drivers/iio/adc/ad9467.c>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
