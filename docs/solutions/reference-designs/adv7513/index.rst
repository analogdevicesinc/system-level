.. _adv7513:

ADV7513
===============================================================================

165 MHz, High-Definition Multimedia Interface (HDMI®) transmitter

Overview
-------------------------------------------------------------------------------

The :adi:`ADV7513` is a 165 MHz, High-Definition Multimedia Interface (HDMI®)
transmitter ideal for DVD players/recorders, digital set-top boxes, A/V
receivers, gaming consoles, and PCs.

The digital video interface contains an HDMI v1.4/DVI v1.0-compatible
transmitter that supports all HDTV formats. The :adi:`ADV7513` supports HDMI
v1.4-specific features including 3D video, x.v.Color™, high bit rate (HBR)
audio, and the programmable auxiliary video information (AVI) InfoFrame
features. With HDCP v1.4, the :adi:`ADV7513` allows secure transmission of
protected content.

The :adi:`ADV7513` supports both S/PDIF and 8-channel I²S audio. Its 8-channel
I²S interface can transmit stereo or 7.1 surround audio up to 768 kHz. The
S/PDIF interface can carry compressed audio including Dolby® Digital, DTS®, and
THX®.

Features:

- Incorporates HDMI v1.4 features, including 3D video support
- 165 MHz supports all video formats up to 1080p and UXGA
- Supports gamut metadata packet transmission
- Integrated CEC buffer/controller
- Compatible with DVI v1.0 and HDCP v1.4
- Video/audio inputs accept logic levels from 1.8 V to 3.3 V
- Programmable, 2-way color space converter
- Supports RGB, YCbCr 4:4:4, YCbCr 4:2:2, and DDR input formats
- Supports ITU-656-based embedded syncs
- Automatic input video format timing detection (CEA-861-E)
- Supports standard S/PDIF for stereo LPCM or compressed audio up to 192 kHz
- High bit rate (HBR) audio
- 8-channel uncompressed LPCM I²S audio up to 192 kHz
- 5 V tolerant I²C and Hot Plug™ Detect (HPD) I/Os, no extra device needed
- No audio master clock needed for supporting S/PDIF and I²S
- On-chip MPU with I²C master performs HDCP operations and EDID reading
- On-chip MPU reports HDMI events through interrupts and registers

Applications:

- Gaming consoles
- PCs
- DVD players and recorders
- Digital set-top boxes
- A/V receivers

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`ADV7513`, we recommend using the evaluation
board with the :adi:`ADV7513` integrated on it.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`adv7513 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`adv7513 prerequisites` - what you need to get started with the
      setup
   #. :ref:`adv7513 quickstart`:

      #. Using the :ref:`DE10-Nano <adv7513 quickstart de10nano>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

#. Design with the :adi:`ADV7513`

   - :ref:`adv7513 block-diagram`

     - :adi:`ADV7513 product page <ADV7513>`

   - Resources for designing a custom ADV7513-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`hdl-axi-hdmi`
           - :external+hdl:ref:`axi_dmac`
           - :external+hdl:ref:`adv7511`
             (supports ADV7511, ADV7511W, ADV7513, ADV7533, ADV7535)

        #. About the device tree:

           - :doc:`Customizing the device tree on the target </linux/kernel/zynq_tips_tricks>`

     #. :external+hdl:ref:`adv7513` which you must use
        in your FPGA.

   - Guides for ADV7513

      - :adi:`ADV7513: 165 MHz, High Performance HDMI Transmitter Data Sheet <media/en/technical-documentation/data-sheets/ADV7513.pdf>`
      - :adi:`ADV7511 Programming Guide, Rev. 1.2 <media/en/technical-documentation/user-guides/ADV7511_Programming_Guide.pdf>`

#. :ref:`Help and Support <help-and-support>`

.. _adv7513 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/adv7513_block_diagram.png
   :align: center
   :width: 600

Warning
-------------------------------------------------------------------------------

.. esd-warning::
