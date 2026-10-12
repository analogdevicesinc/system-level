.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq3-ebz

.. _ad_fmcdaq3_ebz:

AD-FMCDAQ3-EBZ
==============

Dual 14-bit, 1.25 GSPS JESD204B ADC and dual 16-bit, 2.5 GSPS JESD204B DAC
FMC Board.

.. image:: images/ad9680_chip.png
   :align: left
   :width: 150
   :alt: AD9680 chip

Overview
--------

The :adi:`AD-FMCDAQ3-EBZ` is an FMC board featuring the :adi:`AD9680` dual,
14-bit, 1.25 GSPS, JESD204B ADC, the :adi:`AD9152` dual, 16-bit, 2.5 GSPS,
JESD204B DAC, the :adi:`AD9528` clock, and power management components. It is
clocked by an internally generated carrier platform via the FMC connector,
comprising a completely self-contained data acquisition and signal synthesis
prototyping platform. In an FMC footprint (84 mm × 69 mm), the module's
combination of wideband data conversion, clocking, and power closely
approximates real-world hardware and software for system prototyping and design,
with no compromise in signal chain performance.

Features:

- FMC-compatible form factor, powered from a single FMC connector
- Provides two channels of ADC and two channels of DAC with full synchronization
  capabilities
- Includes schematics, layout, BOM, Gerber files, HDL, Linux® drivers, IIO
  Oscilloscope, VisualANALOG
- AD9680: JESD204B (subclass 1) 4-lane coded serial digital outputs, SFDR: 80
  dBc at 1.0 GHz AIN, 2 GHz usable analog input full power bandwidth
- AD9152: JESD204B (subclass 1), supports complex signal bandwidths up to 800
  MHz, selectable 2×, 4×, 8× interpolation filters

Applications:

- Electronic test and measurement equipment
- General-purpose software radios
- Radar systems
- Ultra wideband satellite receivers
- Signals intelligence (SIGINT)
- Point-to-point communication systems
- Multiple input/multiple output (MIMO) radios
- Automated test equipment

.. image:: images/fmcdaq3_top_new.png
   :width: 500
   :alt: AD-FMCDAQ3-EBZ board top view
   :align: center

.. toctree::
   :hidden:

   prerequisites
   quickstart/index
   introduction
   hardware
   hardware/functional_overview
   software
   software/baremetal
   software/linux
   help_and_support

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our :ref:`EngineerZone
forums <help-and-support>`, but before that, please make sure you read our
documentation thoroughly.

To better understand the :adi:`AD9680` / :adi:`AD9152`, we recommend using the
:adi:`AD-FMCDAQ3-EBZ` evaluation board.

Table of contents
-----------------

#. :doc:`Introduction <introduction>`

#. :doc:`Quick Start Guides <quickstart/index>`:

   #. :doc:`On ZC706 <quickstart/zc706>`
   #. :doc:`On ZCU102 <quickstart/zcu102>`
   #. :doc:`On KCU105 <quickstart/kcu105>`
   #. :doc:`On VCU118 <quickstart/vcu118>`
   #. :doc:`On A10GX <quickstart/a10gx>`

#. :doc:`Hardware <hardware>`

   #. :ref:`Functional Overview & Specifications <fmcomms11 functional-overview>`

#. :external+hdl:doc:`projects/daq3/index`

#. :doc:`Software <software>`

   #. :ref:`no-OS drivers <ad-fmcdaq3-ebz software baremetal>`
   #. :ref:`Linux <ad-fmcdaq3-ebz software linux>`

      #. :ref:`ZC706, and related platforms <ad-fmcdaq3-ebz software linux>`
      #. :ref:`linux-kernel microblaze`
      #. Applications

         #. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`

#. :dokuwiki:`Production Testing Process <resources/eval/user-guides/ad-fmcdaq2-ebz/testing>`

#. :ref:`Help and Support <help-and-support>`

.. _ad_fmcdaq3_ebz block diagram:

Block diagram
-------------

.. image:: images/block_diagram_fmcdaq3.jpg
   :align: center
   :width: 800

ADI articles
------------

About JESD standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <analog-dialogue/articles/jesd204c-primer-part2.html>`

Warning
-------

.. esd-warning::
