.. _eval-adar3000:

ADAR3000/3001-EVALZ
================================================================================

17.7 GHz to 21.2 GHz, 4-Beam, 4-Element Ka Band Beamformer.

Overview
-------------------------------------------------------------------------------

The ADAR3000/3001-EVALZ evaluation board evaluates the :adi:`ADAR3000` and
:adi:`ADAR3001`, 17.7 GHz to 21.2 GHz transmit or receive, 4-beam and 4-element
Ka band beamforming core chips for phased arrays. Each of the 16 RF channels
provides a 31.5 dB gain range in 0.5 dB steps and up to 54.5 ps of time delay
in 0.865 ps steps, through variable amplitude and phase (VAP) blocks.

The device stores 256 beam positions in RAM, as 64 beamstates for each of its
4 beams, plus a FIFO of 16 beamstates per beam. A programmable sequencer steps
through the stored beamstates, and update, reset and mute commands are applied
per beam, over SPI or through dedicated pins. All registers are controlled
through a 4-wire SPI, and four address pins allow up to 16 devices to share
the same serial lines.

This reference design controls the evaluation board from an AMD Xilinx
:xilinx:`ZCU102`, through an SDP-I-FMC interposer, running either Linux or
no-OS. Under Linux the device is an IIO device. Under no-OS a basic example
exercises and checks every driver feature, and an IIO example serves the
device to libiio clients over the UART.

Features:

- 16 RF channels, as 4 beams of 4 elements
- 31.5 dB gain range in 0.5 dB steps per channel
- Up to 54.5 ps of true time delay in 0.865 ps steps per channel
- 256 beam positions stored in RAM, and a 64 beam position FIFO
- Programmable beamstate sequencer
- Beamwise update, reset and mute commands, over SPI or pins
- Programmable amplifier bias modes
- On-chip 8-bit ADC with a temperature sensor
- 4-wire SPI, up to 16 devices on the same serial lines

Applications:

- Geosynchronous high-throughput satellite (GEO HTS)
- Low earth orbit (LEO) constellations
- Mobile satellite terminals (land, air, and sea)
- Terrestrial, airborne and satellite phased arrays

.. figure:: images/eval-adar3000.jpg
   :alt: Angled view of the ADAR3000/3001-EVALZ evaluation board
   :align: center
   :width: 600

   ADAR3000/3001-EVALZ evaluation board

.. figure:: images/eval-adar3000-top.jpg
   :alt: Top view of the ADAR3000/3001-EVALZ evaluation board
   :align: center
   :width: 300

   ADAR3000/3001-EVALZ top

.. figure:: images/eval-adar3000-bottom.jpg
   :alt: Bottom view of the ADAR3000/3001-EVALZ evaluation board
   :align: center
   :width: 300

   ADAR3000/3001-EVALZ bottom

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the
:ref:`Help and Support <eval-adar3000 help-and-support>` section at the bottom
of the page.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board:

   #. :ref:`Prerequisites <eval-adar3000 prerequisites>`: what you need to get
      started
   #. :ref:`Quick start guides <eval-adar3000 quickstart>`:

      #. Using the :ref:`ZCU102 <eval-adar3000 quickstart zcu102>` with Linux
         or no-OS

   #. :ref:`User guide <eval-adar3000 user-guide>`: hardware setup and board
      details

#. Design with the ADAR3000:

   #. :adi:`ADAR3000 product page <ADAR3000>`
   #. :external+hdl:ref:`HDL reference design <adar3000>` which you must use
      in your FPGA
   #. :git-linux:`Linux driver <main:drivers/iio/beamformer/adar300x.c>`,
      its :git-linux:`device tree binding <main:Documentation/devicetree/bindings/iio/beamformer/adi,adar300x.yaml>`
      and the
      :git-linux:`ZCU102 device tree <main:arch/arm64/boot/dts/xilinx/adi-adar3000-evb.dts>`
   #. :external+no-OS:doc:`no-OS driver <drivers/beamformer/adar300x>`,
      including its IIO interface
   #. :external+no-OS:doc:`no-OS project <projects/beamformer/adar300x>`,
      with the basic and IIO examples and the full IIO test procedure

#. :ref:`Help and Support <eval-adar3000 help-and-support>`

Helpful documents
-------------------------------------------------------------------------------

- :adi:`ADAR3000` data sheet
- :adi:`ADAR3001` data sheet

Block diagram
-------------------------------------------------------------------------------

.. figure:: images/adar3000_block_diagram.png
   :alt: Functional block diagram of the ADAR3000
   :align: center
   :width: 600

   ADAR3000 functional block diagram

Warning
-------------------------------------------------------------------------------

.. esd-warning::

.. _eval-adar3000 help-and-support:

Help and support
-------------------------------------------------------------------------------

For questions and more information, please visit the :ez:`/` technical support
community.
