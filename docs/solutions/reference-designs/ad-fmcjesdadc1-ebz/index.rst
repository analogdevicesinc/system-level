.. _ad_fmcjesdadc1_ebz eval:

AD-FMCJESDADC1-EBZ (Obsolete)
===============================================================================

14-Bit, 4-Channel, 245.76 MSPS, JESD204B, RF Data Acquisition FMC Board.

.. warning::

   The :adi:`AD-FMCJESDADC1-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

.. note::

   Support was discontinued starting with the **2022_R2** Kuiper Linux release.
   The last release with pre-built files is **2022_r2** - see all releases at
   :git-kuiper:`releases+`.
   HDL source code is available on the
   :git-hdl:`hdl_2022_r2 <hdl_2022_r2:projects/fmcjesdadc1>` branch.

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCJESDADC1-EBZ` is a high speed 4-channel data acquisition
board featuring two :adi:`AD9250` dual 14-bit ADCs at 245.76 MSPS, in an FMC
form factor which supports the JESD204B high speed serial interface. This board
meets all the FMC specifications in terms of mechanical size and mounting hole
locations.

Although this board does meet the FMC specifications, it is not meant as a
commercial off the shelf (COTS) board. If you want a commercial, ready to
integrate product, please refer to one of the many FMC manufacturers.

This board is targeted to use the ADI reference designs and work with both
Altera and Xilinx development systems. ADI provides complete source (HDL and
software) to re-create those projects, but may not provide enough information
to port this to a custom platform.

The analog I/O on this board uses the micro-miniature coaxial (MMCX) connector.
To connect to SMA-based test equipment, you will need an adapter such as Molex
89761-6810.

The card contains:

- :adi:`AD9250` two 14-bit ADC with sampling speeds of up to 250 MSPS, with a
  :adi:`JESD204B <JESD204>` digital interface. (x2, for 4 channels total)
- :adi:`AD9517-1` multi-output clock distribution device with subpicosecond
  jitter performance, on-chip PLL and VCO.
- :adi:`AD7291` 12-bit, low power, 8-channel SAR ADC with temperature sensor.
- :adi:`ADP151` ultralow noise LDO, 2.2 V to 5.5 V, up to 200 mA.
- :adi:`ADP1753` low dropout linear regulator, 1.6 V to 3.6 V, up to 800 mA.
- :adi:`ADP2301` compact, constant-frequency, current-mode step-down DC-to-DC
  regulator with integrated power MOSFET.
- :adi:`ADG3304` bidirectional 4-channel logic level translator.

.. figure:: images/ad-fmcjesdadc1-ebz_top.png
   :alt: AD-FMCJESDADC1-EBZ evaluation board (top view)
   :align: center
   :width: 500

   AD-FMCJESDADC1-EBZ Evaluation Board (top view)

.. figure:: images/ad-fmcjesdadc1-ebz_bottom.png
   :alt: AD-FMCJESDADC1-EBZ evaluation board (bottom view)
   :align: center
   :width: 500

   AD-FMCJESDADC1-EBZ Evaluation Board (bottom view)

Features:

- 4 channels at 245.76 MSPS using JESD204B high speed serial interface
- On-board clock generation from 30.72 MHz crystal via :adi:`AD9517-1`
  (generates 2.45760 GHz, 245.760 MHz, 30.72 MHz)
- Passive differential transformer front end (Minicircuits TC4-1W,
  optimized for first Nyquist zone, 10–100 MHz)
- Meets full FMC mechanical specification (size and mounting holes)

Applications:

- Instrumentation and measurement
- Radar
- Healthcare
- Energy
- Industrial automation

.. toctree::
   :hidden:

   prerequisites
   user-guide
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete as
it should be. If you have any questions, feel free to ask on our
:ez:`/`, but before that, please make sure you read our documentation
thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <ad_fmcjesdadc1_ebz prerequisites>`
   #. :ref:`Quick start guides <ad_fmcjesdadc1_ebz quickstart>`

      #. :ref:`Supported carriers <ad_fmcjesdadc1_ebz carriers>`
      #. :ref:`Hardware setup <ad_fmcjesdadc1_ebz hardware-setup>`
      #. :ref:`MicroBlaze quick start <ad_fmcjesdadc1_ebz microblaze_quickstart>`


   #. :ref:`User guide <ad_fmcjesdadc1_ebz user-guide>`

      #. :ref:`Hardware guide <ad_fmcjesdadc1_ebz hardware-guide>`
      #. :ref:`Software guide <ad_fmcjesdadc1_ebz software-guide>`

#. Design with the AD9250

   - :adi:`AD9250` product page

   - Resources for designing a custom AD9250-based platform:

     #. For Linux software:

        - :external+linux:ref:`AD9250 AXI Linux driver <axi-adc-hdl>`
        - :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
        - :external+linux:ref:`JESD204B/C AXI_ADXCVR Linux driver <axi_adxcvr>`

#. :ref:`Help and Support <help-and-support>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
