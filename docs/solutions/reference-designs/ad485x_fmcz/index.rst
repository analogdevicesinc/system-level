.. _ad485x_fmcz:

AD485X-FMCZ
===============================================================================

Buffered, 8-Channel Simultaneous Sampling, 20-Bit 1 MSPS DAS

.. flex::

   .. image:: ./images/ad485x-chip-illustration.png
      :width: 250
      :align: left

   .. image:: ./images/ad4858-chip-illustration.png
      :width: 250
      :align: left

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD4858` board contains the :adi:`AD4858` chip, which is a
20-bit, low noise 8-channel simultaneous sampling successive approximation
register (SAR) ADC, with buffered differential, wide common range picoamp
inputs.

More about simultaneous sampling A/D converters :adi:`here <en/products/analog-to-digital-converters/precision-ad-converters.html>`.

The :adi:`EVAL-AD4858` supports pin-selectable SPI CMOS and LVDS serial
interfaces. In CMOS mode, applications may employ between 1-8 lanes of serial
output data, allowing the user to optimize bus width and data throughput. In
LVDS mode, pins SDO+/-, SCKI+/- and SCKO+/- function as differential serial
data input, clock output and clock input pins respectively (from the FPGA's
point of view).

Features:

- Full featured evaluation board for the :adi:`AD4858`
- Eight input channels available through SMA connectors
- On-board reference circuit and power supplies
- Standalone capability through FMC connector and/or test points
- PC software for control and data analysis of the time and frequency domain
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__-compatible
- Compatible with other FMC controller boards

Applications:

- Automatic test equipment
- Avionics and aerospace
- Instrumentation and control systems
- Semiconductor manufacturing
- Test and measurement

.. grid::
   :widths: 33% 33% 33%

   .. figure:: ./images/eval-ad4858fmcz_angle-evaluation-board.jpg
      :width: 300px

      Angle view

   .. figure:: ./images/eval-ad4858fmcz_top-evaluation-board.jpg
      :width: 300px

      Top view

   .. figure:: ./images/eval-ad4858fmcz_bottom-evaluation-board.jpg
      :width: 300px

      Bottom view

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:ref:`ask <help-and-support>`.

Table of Contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <ad485x_fmcz prerequisites>` - what you need to get started
   #. :ref:`Quick start guides <ad485x_fmcz quickstart>`:

      #. Using the :ref:`ZedBoard <ad485x_fmcz quickstart zed>` (FPGA)

   #. Use the board to better understand the :adi:`EVAL-AD4858`

      #. :external+kuiper:ref:`Configure a SD Card <use-kuiper-image>`
      #. :external+kuiper:ref:`package-management`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`
      #. :external+scopy:doc:`Scopy <index>`

   #. :ref:`FRU EEPROM Utility <software fru-dump>`

#. Design with the EVAL-AD485X-FMCZ

   #. :ref:`ad485x_fmcz block-diagram`

      #. :adi:`AD4858` Product page
      #. `EVAL-AD485X-FMCZ User Guide <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad4858-ug-2142.pdf>`__

   #. Design a custom EVAL-AD485X-FMCZ-based platform

      #. HDL software

         #. :git-hdl:`AD485x-FMC HDL Reference Design <projects/ad485x_fmcz>`

      #. Linux software

         #. :git-linux:`AD485x Linux driver source code <staging/ad4858_rebased:drivers/iio/adc/ad4858.c>`
         #. :git-linux:`EVAL-AD4858FMCZ Linux device tree <staging/ad4858_rebased:arch/arm/boot/dts/zynq-zed-adv7511-ad4858.dts>`

      #. More information

         #. :ref:`GNU Radio <software gnuradio>`
         #. :external+linux:ref:`AXI ADC HDL Linux Driver <axi-adc-hdl>`

#. :ref:`Help and Support <help-and-support>`

Pre-requisites and quickstart
-------------------------------------------------------------------------------

.. toctree::
   :caption: The prerequisites and quickstart guides are provided at:
   :titlesonly:
   :maxdepth: 1

   prerequisites
   quickstart/index

.. _ad485x_fmcz block-diagram:

Functional Block Diagram
-------------------------------------------------------------------------------

.. image:: ./images/ad4858-fbl.png
   :width: 600

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`AD4858 Product Page <AD4858>`
- `EVAL-AD485X-FMCZ User Guide <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad4858-ug-2142.pdf>`__

Software Projects and Platforms
-------------------------------------------------------------------------------

- :ref:`EVAL-AD4858 + ZedBoard <ad485x_fmcz quickstart zed>`
- :git-hdl:`AD485x-FMC HDL project <projects/ad485x_fmcz>`
- :git-no-OS:`AD485x No-OS driver <drivers/adc/ad4858>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and Support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
