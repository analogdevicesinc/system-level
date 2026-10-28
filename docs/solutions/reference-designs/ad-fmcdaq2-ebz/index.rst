.. _ad-fmcdaq2-ebz:

AD-FMCDAQ2-EBZ
===============================================================================

Dual 14-bit 1 GSPS ADC and quad 16-bit 2.8 GSPS DAC FMC evaluation board.

.. image:: images/ad9144_chip.png
   :width: 150
   :alt: AD9144 chip
   :align: left

.. image:: images/ad9680_chip.png
   :width: 150
   :alt: AD9680 chip
   :align: right

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCDAQ2-EBZ` module is comprised of the :adi:`AD9680` dual, 14-bit,
1.0 GSPS, JESD204B ADC, the :adi:`AD9144` quad, 16-bit, 2.8 GSPS, JESD204B DAC,
the :adi:`AD9523-1` clock, and power management components. It is clocked by an
internally generated carrier platform via the FMC connector, comprising a
completely self-contained data acquisition and signal synthesis prototyping
platform.

Features:

- Includes schematics, layout, BOM, Gerber files, HDL, Linux® drivers,
  IIO Oscilloscope, VisualANALOG
- FMC-compatible form factor
- Powered from single FMC connector
- Two channels of ADC and two channels of DAC with full synchronization

Applications:

- Electronic test and measurement equipment
- General-purpose software radios
- Radar systems and signals intelligence (SIGINT)
- Ultra wideband satellite receivers
- Point to point and MIMO communication systems
- Automated test equipment

.. image:: images/dac2_top.jpg
   :align: center
   :width: 500

.. toctree::
   :hidden:

   prerequisites
   quickstart/index
   introduction
   hardware
   hardware/card_specification
   hardware/functional_overview
   clocking
   testing
   help_and_support

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience.
However, like many things, documentation is never as complete as it should be.
If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9144` / :adi:`AD9680`, we recommend using the
:adi:`AD-FMCDAQ2-EBZ` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the :adi:`AD-FMCDAQ2-EBZ` full stack reference design:

   #. :ref:`Prerequisites <ad_fmcdaq2_ebz prerequisites>` — what you need to
      get started
   #. :ref:`Quick Start Guides <ad_fmcdaq2_ebz quickstart>`:

      #. :ref:`ZC706 <ad_fmcdaq2_ebz quickstart zc706>`
      #. :ref:`ZCU102 <ad_fmcdaq2_ebz quickstart zcu102>`
      #. :ref:`MICROBLAZE <ad_fmcdaq2_ebz quickstart microblaze>`
      #. :ref:`Arria 10 SoC <ad_fmcdaq2_ebz quickstart a10soc>`
      #. :ref:`A10GX (OBSOLETE) <ad_fmcdaq2_ebz quickstart a10gx>`

   #. Configure an SD card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux applications:

      #. :ref:`IIO Oscilloscope <iio-oscilloscope>`

#. Design with the :adi:`AD9144` / :adi:`AD9680`:

   - :ref:`ad-fmcdaq2-ebz block-diagram`

     - :adi:`AD9144 product page <AD9144>`
     - :adi:`AD9680 product page <AD9680>`

   - :external+hdl:ref:`HDL reference design <daq2>`

#. :ref:`Help and Support <help-and-support>`

.. _ad-fmcdaq2-ebz block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/daq2_card_block_diagram.jpg
   :align: center
   :width: 800

ADI articles
-------------------------------------------------------------------------------

About the JESD204B standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You — Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You — Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
