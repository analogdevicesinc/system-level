.. _eval-ad9694:

EVAL-AD9694
===============================================================================

14-Bit, 500 MSPS, Quad, JESD204B Analog-to-Digital Converter Evaluation Board.

.. image:: images/ad9694-chip-illustration.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`AD9694-500EBZ <EVAL-AD9694>` is a full-featured evaluation board for the
:adi:`AD9694`, a quad, 14-bit, 500 MSPS analog-to-digital converter (ADC) with a
JESD204B serial interface. The device is organized as two dual ADC pairs (Pair
AB and Pair CD).

The board provides all support circuitry required to operate the AD9694 in its
various modes and configurations. It connects to an FPGA carrier board running
ADI Kuiper Linux with IIO-based software tools.

Features:

- JESD204B coded serial digital outputs with support for lane rates up to 15
  Gbps/lane
- Wide full-power bandwidth supports IF sampling of signals up to 1.4 GHz
- Four integrated wideband decimation filters and NCO blocks supporting
  multiband receivers
- Buffered inputs ease filter design and implementation
- Programmable fast overrange detection and signal monitoring
- On-chip temperature diode for system thermal management

Applications:

- Multi-band, multi-mode receivers
- Radar and electronic warfare
- Instrumentation and test equipment
- Software-defined radio (SDR)

.. figure:: images/ad9694-500ebzangle-evaluation-board.jpg
   :align: center
   :width: 500

   AD9694-500EBZ

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   ad9694-500ebz

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our
documentation thoroughly.

To better understand the :adi:`AD9694`, we recommend using the
:adi:`AD9694-500EBZ <EVAL-AD9694>` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad9694 user-guide` --- hardware guide for the evaluation board
   #. :ref:`Prerequisites <ad9694 prerequisites>` --- what you need to get
      started
   #. :ref:`Quick start guides <ad9694 quickstart>`:

      #. Using the :ref:`ZCU102/Zynq UltraScale+ MPSoC <ad9694 quickstart zcu102>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the AD9694

   - :ref:`ad9694 block-diagram`

     - :adi:`AD9694 product page <AD9694>`

   - Resources for designing a custom AD9694-based platform

     #. For Linux software:

        #. About the device driver:

           - :dokuwiki:`AD9694 Linux IIO ADC driver <resources/tools-software/linux-drivers/iio-adc/ad9694>`
           - :external+linux:ref:`axi_jesd204_rx`
           - :external+linux:ref:`axi_adxcvr`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dmac`

        #. About the device tree:

           - :ref:`Customizing the device tree on the target <linux-kernel zynq-tips-tricks>`

        #. About the JESD204 utilities:

           - :external+linux:ref:`jesd204-fsm-framework`
           - :ref:`JESD204 status utility <software jesd-status>`
           - :external+hdl:ref:`jesd204`

     #. :external+hdl:ref:`HDL reference design <ad9694_fmc>` which you must use
        in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _ad9694 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/ad9694-fbl.png
   :align: center
   :width: 500

ADI articles
-------------------------------------------------------------------------------

About the JESD204 standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You---Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You---Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
