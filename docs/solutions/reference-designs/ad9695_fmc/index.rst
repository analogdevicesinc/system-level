.. _ad9695-fmc:

EVAL-AD9695
===============================================================================

14-Bit, 1300 MSPS, JESD204B Analog-to-Digital Converter Evaluation Board.

.. image:: images/AD9695_chip.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`AD9695-1300EBZ` is a full-featured evaluation board for the
:adi:`AD9695`, a 14-bit, 1300 MSPS analog-to-digital converter (ADC) with a
JESD204B serial interface. The :adi:`AD9697` ADC can also be evaluated using
this board, with identical performance except for power consumption.

The board provides all support circuitry required to operate the AD9695 in its
various modes and configurations. It connects to an FPGA carrier board running
ADI Kuiper Linux with IIO-based software tools.

Features:

- JESD204B coded serial digital outputs with support for lane rates up to
  16 Gbps/lane
- Wide full-power bandwidth supports IF sampling of signals up to 2 GHz
- Four integrated wide-band decimation filter and NCO blocks supporting
  multi-band receivers
- Flexible SPI interface controls various product features and functions
- Programmable fast over-range detection and signal monitoring

Applications:

- Multi-band, multi-mode receivers
- Electronic warfare receivers
- Phased array radar
- Test and measurement equipment

.. figure:: images/ad9695-2.jpg
   :align: center
   :width: 500

   AD9695-1300EBZ

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   ad9695-1300ebz

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9695` / :adi:`AD9697`, we recommend using the
:adi:`AD9695-1300EBZ` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad9695 user-guide` — hardware guide for the evaluation board
   #. :ref:`Prerequisites <ad9695 prerequisites>` — what you need to get
      started
   #. :ref:`Quick start guides <ad9695 quickstart>`:

      #. Using the :ref:`ZCU102/Zynq UltraScale+ MPSoC <ad9695 quickstart zcu102>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. :ref:`Evaluating the AD9695/AD9697 Analog-to-Digital Converter <ad9695-1300ebz>`

#. Design with the AD9695/AD9697

   - :ref:`ad9695 block-diagram`

     - :adi:`AD9695 product page <AD9695>`
     - :adi:`AD9697 product page <AD9697>`

   - Resources for designing a custom AD9695/AD9697-based platform

     #. For Linux software:

        #. About the device driver:

           - :dokuwiki:`AD9695 Linux IIO ADC driver <resources/tools-software/linux-drivers/iio-adc/ad9695>`
           - :external+hdl:ref:`axi_jesd204_rx`
           - :external+hdl:ref:`axi_adxcvr`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+hdl:ref:`axi_dmac`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

        #. About the JESD204 utilities:

           - :external+linux:ref:`jesd204-fsm-framework`
           - :doc:`JESD204 status utility </software/jesd/jesd_status>`
           - :external+hdl:ref:`jesd204`

     #. :external+hdl:ref:`HDL reference design <ad9695_fmc>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _ad9695 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/ad9695_fmc_block_diagram.png
   :align: center
   :width: 500

ADI articles
-------------------------------------------------------------------------------

About the JESD204 standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
