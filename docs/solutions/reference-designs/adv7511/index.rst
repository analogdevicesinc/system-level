.. _adv7511:

ADV7511
===============================================================================

225 MHz High-Definition Multimedia Interface (HDMI®) transmitter

Overview
-------------------------------------------------------------------------------

The :adi:`ADV7511` is a 225 MHz High-Definition Multimedia Interface (HDMI®)
transmitter designed for applications requiring high-performance video and
audio over HDMI. The ADV7511 supports HDMI 1.4 features including 3D video
and xvYCC™ color spaces.

The ADV7511 is integrated into several Xilinx evaluation boards including
Artix-7, Kintex-7, Virtex-7, and Zynq platforms. This reference design
provides the video and audio interface between the FPGA and the on-board
ADV7511.

The video uses a 16-bit 422 YCbCr interface (except VC707 which uses 36-bit
444 RGB interface) and the audio uses a single-bit SPDIF interface.

Features:

- HDMI 1.4 compliant transmitter
- Support for video resolutions up to 1080p
- Integrated HDCP engine with key storage
- Audio support via I2S, S/PDIF, or DSD
- On-chip EDID buffer
- RGB, YCbCr 4:4:4, and YCbCr 4:2:2 color space support
- CEC support
- 225 MHz maximum pixel clock

Applications:

- Video processing and distribution
- Set-top boxes and DVD/Blu-ray players
- Gaming consoles
- Professional AV equipment
- FPGA development and prototyping

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   encoder_adv7511_adv7343
   transmitter_api

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`ADV7511`, we recommend using the evaluation
boards with the ADV7511 integrated on them.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`adv7511 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`adv7511 prerequisites` - what you need to get started with the setup
   #. :ref:`adv7511 quickstart`:

      #. Using the :ref:`AC701 <adv7511 quickstart ac701>`
      #. Using the :ref:`KC705 <adv7511 quickstart kc705>`
      #. Using the :ref:`VC707 <adv7511 quickstart vc707>`
      #. Using the :ref:`ZC702 <adv7511 quickstart zc702>`
      #. Using the :ref:`ZC706 <adv7511 quickstart zc706>`
      #. Using the :ref:`ZedBoard <adv7511 quickstart zed>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

#. Design with the ADV7511

   - :ref:`adv7511 block-diagram`

     - :adi:`ADV7511 product page <ADV7511>`

   - Resources for designing a custom ADV7511-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`AXI HDMI TX Linux driver <hdl-axi-hdmi>`
           - :external+hdl:ref:`AXI-DMAC DMA Controller Linux driver <axi_dmac>`
           - :external+hdl:ref:`ADV7511 Linux device driver <adv7511>`

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

     #. :external+hdl:ref:`HDL reference design <adv7511>` which you must use
        in your FPGA.

   - Guides for ADV7511

      - :ref:`adv7511 transmitter-api` - Comprehensive API documentation
      - :adi:`ADV7511: 225 MHz, High Performance HDMI Transmitter with ARC Data Sheet (Rev.Sp0) <media/en/technical-documentation/data-sheets/ADV7511.pdf>`
      - :adi:`UG-235: User Guide for Advantiv ADV7842/ADV7511 Video Evaluation Board <media/en/technical-documentation/user-guides/UG-235.pdf>`
      - :adi:`ADV7511 Programming Guide, Rev. 1.2 <media/en/technical-documentation/user-guides/ADV7511_Programming_Guide.pdf>`

#. :ref:`adv7511 encoder_adv7511_adv7343`
#. :ref:`Help and Support <help-and-support>`

.. _adv7511 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/adv7511_block_design.png
   :align: center
   :width: 800

Warning
-------------------------------------------------------------------------------

.. esd-warning::
