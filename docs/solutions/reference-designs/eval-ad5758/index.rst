.. _eval_ad5758:

EVAL-AD5758SDZ
===============================================================================

16-Channel, 14-Bit, Programmable Current-Output DAC.

.. image:: images/AD5758-chip-illustration.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD5758SDZ` is a full-featured evaluation board for the
:adi:`AD5758`, a single-channel, 16-bit, voltage and current output
digital-to-analog converter (DAC) with on-chip dynamic power control (DPC)
and HART connectivity. The board connects to an FPGA carrier's FMC LPC
connector through the EVAL-SDP-CK1Z (FMC-I-SDP) interposer, enabling precise
voltage and current sourcing for industrial and automation applications.

The evaluation board features:

- On-board 2.5 V ADR4525 precision reference
- On-board ADP1031-1 isolated power management unit with SPI signal isolation
- FMC LPC connection to the FPGA carrier via the EVAL-SDP-CK1Z interposer
- SPI-compatible serial interface

Features:

- Single-channel, 16-bit voltage and current output DAC
- Programmable voltage ranges (0 V to 5 V, 0 V to 10 V, ±5 V, ±10 V) and
  current ranges (0-20 mA, 0-24 mA, 4-24 mA, ±20 mA, ±24 mA)
- On-chip dynamic power control (DPC) buck converter
- Integrated diagnostics and HART signal coupling

Applications:

- Industrial process control
- Precision current sourcing/sinking
- Automated test equipment (ATE)
- Data acquisition systems

.. figure:: images/EVAL-AD5758SDZANGLE-web2.png
   :align: center
   :width: 500

   EVAL-AD5758SDZ

.. figure:: images/demo-ad5758-ao87angle-web.gif
   :align: center
   :width: 500

   DEMO-AD5758-AO8Z

Two evaluation boards are available for the AD5758 device: the
:adi:`EVAL-AD5758SDZ` and the
:adi:`DEMO-AD5758-AO8Z <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/demo-ad5758-ao8z.html#eb-overview>`.
Each board is covered in
its own dedicated section.

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index
   spi
   demonstration-platform/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD5758`, we recommend using the
:adi:`EVAL-AD5758SDZ` evaluation board with a ZedBoard FPGA carrier.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`eval_ad5758 user-guide` - what you need to know about the evaluation
      board
   #. :ref:`Prerequisites <eval_ad5758 prerequisites>` - what you need to get
      started
   #. :ref:`Quick start guides <eval_ad5758 quickstart>`:

      #. Using the :ref:`ZedBoard <eval_ad5758 quickstart zed>` (FPGA)

#. Using the :ref:`DEMO-AD5758-AO8Z demonstration platform <demo_ad5758_ao8z>` -
   a compact, eight-channel, isolated analog output module built with the
   AD5758 and ADP1031

#. Design with the AD5758

   - :ref:`eval_ad5758 block-diagrams`

     - :adi:`AD5758 product page <AD5758>`

   - Resources for designing a custom AD5758-based platform

     #. For no-OS software:

        - :git-no-OS:`AD5758 No-OS Driver <drivers/dac/ad5758>` and :git-no-OS:`AD5758 Project <projects/ad5758-sdz>`
        - `AD5758 No-OS Project API Reference (ad5758_sdz.c) <https://analogdevicesinc.github.io/no-OS/doxygen/ad5758__sdz_8c.html>`_

     #. For Linux software:

        #. Linux support:

           - :git-linux:`AD5758 Linux Driver <drivers/iio/dac/ad5758>`
           - :external+linux:doc:`AD5758 Linux IIO DAC driver Documentation
             <drivers/iio-dac/ad5758>`

     #. :git-hdl:`AD5758 HDL Reference Design <projects/ad5758_sdz>` and :external+hdl:ref:`AD5758 HDL Project Documentation <ad5758_sdz>` which you must
        use in your FPGA.

#. :ref:`Help and Support <help-and-support>`

.. _eval_ad5758 block-diagrams:

Block diagrams
-------------------------------------------------------------------------------

.. figure:: images/ad5758-fbl.png
   :align: center
   :width: 800

   AD5758 Block Diagram

Warning
-------------------------------------------------------------------------------

.. esd-warning::

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`AD5758 Product Page <AD5758>`
- :adi:`EVAL-AD5758 Evaluation Board Page <EVAL-AD5758>`
