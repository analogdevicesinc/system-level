.. _hmcad15xx-ebz:

HMCAD15XX-EBZ
===============================================================================

High Speed Multi-Mode 8/12/14-Bit 1000/640/105 MSPS A/D Converter

Overview
-------------------------------------------------------------------------------
The :adi:`HMCAD1511-EBZ` / :adi:`HMCAD1520-EBZ` are high-speed analog-to-digital
converter (ADC) evaluation boards designed for multichannel data acquisition
applications. The boards feature a multi-mode ADC that supports 8-bit, 12-bit,
and 14-bit resolution modes with sampling rates between 105-1000 MSPS. They 
provide flexible input configuration options with both single-ended and 
differential analog inputs, enabling direct interfacing with a wide variety of
RF and baseband signal sources. The boards include integrated signal 
conditioning and timing circuitry for seamless operation. Hardware and software
controls enable users to optimize the ADC performance for their specific 
application requirements. Software control is accessible through the Linux 
industrial input/output (IIO) framework.

Features:

- Both chips feature:
    - 8 bit resolution.
    - Single/Dual/Quad channel modes with 1000/500/250 MSPS.
- The HMCAD1520 features:
    - 8/12/14 bit resolutions
    - Dual 8-bit Quad Channel Mode
    - 12-bit resolution Single/Dual/Quad channel modes with 640/320/160 MSPS
    - 14-bit precision resolution Quad channel mode with 105 MSPS

Applications:

- Precision Oscilloscopes
- Satellite Receivers
- Hi-End Ultrasound
- Spectrum Analyzers

.. image:: ./images/HMCAD1520-EBZ.webp
   :align: center
   :width: 500

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our EngineerZone 
forums, but before that, please make sure you read our documentation thoroughly.

To better understand the :adi:`HMCAD1511` / :adi:`HMCAD1520`, we recommend to
use the  :adi:`HMCAD1511-EBZ` / :adi:`HMCAD1520-EBZ` evaluation board.

Table of contents
-------------------------------------------------------------------------------
#. Using the evaluation board/full stack reference design that we offer:
    #. :ref:`User Guide <hmcad15xx user-guide>`
    #. :ref:`Prerequisites <hmcad15xx prerequisites>` - what you need to get
       started
    #. :ref:`Quick start guide <hmcad15xx quickstart>`
        #. Using the :ref:`ZedBoard <hmcad15xx zed>`
    #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`
    #. Linux Applications
        #. :ref:`iio-oscilloscope`
#. Design with the HMCAD1511/HMCAD1520
    - :ref:`Block Diagram <hmcad15xx block_diagram>`
        - :adi:`HMCAD1511 product page <HMCAD1511>`
        - :adi:`HMCAD1520 product page <HMCAD1520>`

.. _hmcad15xx block_diagram:

Block Diagram
-------------------------------------------------------------------------------

.. image:: ./images/hmcad1520_block_diagram.png
   :align: center
   :width: 800

Warning
-------------------------------------------------------------------------------

.. esd-warning::