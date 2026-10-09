.. _eval-ad974x:

EVAL-AD974X
===============================================================================

14-Bit / 12-Bit / 10-Bit / 8-Bit, 210 MSPS TxDAC D/A Converter Evaluation Board.

.. image:: ./images/ad9744_chip_icon.jpeg
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9740` / :adi:`EVAL-AD9742`/ :adi:`EVAL-AD9744` /
:adi:`EVAL-AD9748` evaluation board allows users to easily set up and test the
32-lead lead frame chip scale package (LFCSP) of the :adi:`AD9740` /
:adi:`AD9742` / :adi:`AD9744` / :adi:`AD9748` devices. Paying careful attention
to layout and circuit design, combined with a prototyping area, allows the user
to effectively evaluate the AD9740, AD9742, AD9744, and AD9748 in applications
that require high resolution and high speed conversion.

The evaluation board interfaces with an FPGA carrier via an FMC LPC
connector, using the `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__
Rev D or later (Zynq-7000 SoC) as the supported FPGA platform.

Features:

- High performance member of pin-compatible TxDAC product family
- Excellent SFDR performance
- Twos complement or straight binary data format
- Differential current outputs: 2 mA to 20 mA
- Power dissipation: 135 mW at 3.3 V
- Power-down mode: 15 mW at 3.3 V
- On-chip 1.2 V reference
- CMOS-compatible digital interface
- 32-lead LFCSP package
- Edge triggered latches

Applications:

- Direct IFs
- Base stations
- Wireless local loops
- Digital radio links
- Direct digital synthesis (DDS)
- Instrumentation

.. figure:: ./images/ad9744_eval_board.jpeg
   :alt: Photo of the EVAL-AD974x evaluation board
   :align: center
   :width: 600

   EVAL-AD974x

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience
with things. However, like many things, documentation is never as complete
as it should be. If you have any questions, feel free to ask on our
:ez:`/`, but before that, please make sure you read our documentation
thoroughly.

To better understand the :adi:`AD9740` / :adi:`AD9742` / :adi:`AD9744` /
:adi:`AD9748`, we recommend using the :adi:`EVAL-AD9740` / :adi:`EVAL-AD9742` /
:adi:`EVAL-AD9744` / :adi:`EVAL-AD9748` evaluation board together with the
`ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__ 
FPGA development kit.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <eval-ad974x prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guides <eval-ad974x quickstart>`:

      #. Using the :ref:`ZedBoard <eval-ad974x quickstart zed>`
      #. Using the :ref:`SDP-H1 <eval-ad974x quickstart sdp-h1-ace>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :external+scopy:doc:`Scopy <index>`

#. Design with the AD9740 / AD9742 / AD9744 / AD9748

   - :ref:`eval-ad974x block-diagram`

     - :adi:`AD9740` product page
     - :adi:`AD9742` product page
     - :adi:`AD9744` product page
     - :adi:`AD9748` product page

   - Resources for designing a custom AD974x-based platform:

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`AXI-DMAC DMA Controller Linux driver <axi-dmac>`

     #. :external+hdl:ref:`HDL reference design <ad9740_fmc>` which you
        must use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad974x block-diagram:

Block diagram
-------------------------------------------------------------------------------

The :adi:`AD9740` HDL reference design on the Zedboard uses the
:external+hdl:ref:`AXI AD9740 <axi_ad9740>` IP core to interface the
DAC via a parallel bus. The AXI-DMAC streams sample data from DDR memory
to the IP core, which drives the AD974x at up to 210 MSPS.

.. figure:: ./images/ad9744_block_diagram.jpeg
   :alt: AD974x block diagram

   AD974x block diagram.

ADI articles
-------------------------------------------------------------------------------

#. :adi:`AD9740 Product Page <AD9740>`
#. :adi:`AD9742 Product Page <AD9742>`
#. :adi:`AD9744 Product Page <AD9744>`
#. :adi:`AD9748 Product Page <AD9748>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
