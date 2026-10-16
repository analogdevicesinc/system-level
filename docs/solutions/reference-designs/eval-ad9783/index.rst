.. _eval-ad9783:

EVAL-AD9783
==============================================================================

Dual 16-Bit / 14-Bit / 12-Bit LVDS Interface 500 MSPS DACs Evaluation Board.

.. image:: ./images/ad9783-chip_icon.jpeg
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9783` evaluation board allows users to easily set up and test
the 72-lead lead frame chip scale package (LFCSP_VQ) of the :adi:`AD9783` /
:adi:`AD9781` / :adi:`AD9780` devices. Paying careful attention to layout and
circuit design, combined with a prototyping area, allows the user to
effectively evaluate the AD9783, AD9781, AD9780 in applications that require
high resolution and high speed conversion.

Features:

- High dynamic range, dual DAC parts
- Low noise and intermodulation distortion
- Single carrier W-CDMA ACLR = 80 dBc @ 61.44 MHz IF
- Innovative switching output stage permits usable outputs beyond Nyquist frequency
- LVDS inputs with dual-port or optional interleaved single-port operation
- Differential analog current outputs are programmable from 8.6 mA to 31.7 mA full scale
- Auxiliary 10-bit current DACs with source/sink capability for external offset nulling

Applications:

- Wireless infrastructure
- W-CDMA, CDMA2000, TD-SCDMA, WiMAX
- Wideband communications
- LMDS/MMDS, point-to-point
- RF signal generators, arbitrary waveform generators

.. figure:: ./images/ad9783-eval_board.jpeg
   :alt: Photo of the EVAL-AD9783 evaluation board
   :align: center
   :width: 600

   EVAL-AD9783

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

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <eval-ad9783 prerequisites>` - what you
      need to get started
   #. :ref:`Quick start guides <eval-ad9783 quickstart>`:

      #. Using the :ref:`ZCU102 <eval-ad9783 quickstart zcu102>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :external+scopy:doc:`Scopy <index>`

#. Design with the AD9783 / AD9781 / AD9780

   - :ref:`eval-ad9783 block-diagram`

     - :adi:`AD9783` product page
     - :adi:`AD9781` product page
     - :adi:`AD9780` product page

   - Resources for designing a custom AD9783-based platform:

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`AXI-DMAC DMA Controller Linux driver <axi-dmac>`

     #. :external+hdl:ref:`HDL reference design <ad9783_ebz>` which you
        must use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad9783 block-diagram:

Block diagram
-------------------------------------------------------------------------------

The :external+hdl:ref:`AD9783_EBZ` on the ZCU102 uses the
:external+hdl:ref:`AXI AD9783 <axi_ad9783>` IP core to interface the
DAC via a parallel bus. The AXI-DMAC streams sample data from DDR memory
to the IP core, which drives the AD9783 at up to 500 MSPS.

.. figure:: ./images/ad9783-block_diagram.jpeg
   :alt: AD9783 block diagram

   AD9783 block diagram.

ADI articles
-------------------------------------------------------------------------------

#. :adi:`AD9783 Product Page <AD9783>`
#. :adi:`AD9781 Product Page <AD9781>`
#. :adi:`AD9780 Product Page <AD9780>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
