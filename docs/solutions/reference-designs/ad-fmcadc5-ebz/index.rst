.. _ad_fmcadc5_ebz eval:

AD-FMCADC5-EBZ (Obsolete)
===============================================================================

12-Bit, 5000 MSPS (Interleaved), JESD204B, RF Data Acquisition FMC Board.

.. warning::

   The :adi:`AD-FMCADC5-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

.. note::

   Support was discontinued starting with the **2022_R2** Kuiper Linux release.
   The last release with pre-built files is **2021_r2** - see all releases at
   :git-kuiper:`releases+`.
   HDL source code is available on the
   :git-hdl:`hdl_2021_r2 <hdl_2021_r2:projects/fmcadc5>` branch.

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCADC5-EBZ` is a high speed single channel data acquisition
board featuring two :adi:`AD9625` ADCs. The board is provisioned to sample
the single input at an effective sampling rate of 5 GSPS, with both ADCs
running at 2.5 GHz and sampling at both edges (the clocks are 180 degrees out
of phase to each other). The board is a variant of
`FSF-AD15000A <https://fidus.com/fmcs/>`_ from Fidus Systems Inc.

Although this board does meet most of the FMC specifications, it is not meant
as a commercial off the shelf (COTS) board. If a commercial, ready to integrate
product is required, please refer to one of the many FMC manufacturers.

ADI also provides reference designs (HDL and software) for this board to work
with commonly available Altera and Xilinx development boards.

The AD-FMCADC5-EBZ is a double FMC wide board and requires two fully populated
(transceivers mainly) FMC connectors on the carrier (such as VC707). The
analog signal is connected to J18.

The card contains:

- :adi:`AD9625` 12-bit single channel ADC with sampling speeds of up to
  2500 MSPS, with a :adi:`JESD204B <JESD204>` digital interface. (x2, for
  effective 5 GSPS interleaved operation)

.. figure:: images/ad-fmcadc5-ebz.jpg
   :alt: AD-FMCADC5-EBZ evaluation board
   :align: center
   :width: 600

   AD-FMCADC5-EBZ Evaluation Board

Features:

- 5 GSPS effective sampling rate using two AD9625 devices interleaved at
  2.5 GSPS each, utilizing JESD204B high speed serial interface
- 180-degree phase offset clocking for interleaved operation
- SYSREF-based calibration for interleaving order alignment
- Self-powered and self-clocked when connected to an FMC carrier

Applications:

- Instrumentation and measurement
- Radar
- Healthcare
- Energy
- Industrial automation

Block Diagram
-------------------------------------------------------------------------------

.. figure:: images/adc5_block_diagram.png
   :alt: AD-FMCADC5 Block Diagram
   :align: center
   :width: 800

   AD-FMCADC5-EBZ Block Diagram

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

   #. :ref:`Prerequisites <ad_fmcadc5_ebz prerequisites>`
   #. :ref:`Quick start guides <ad_fmcadc5_ebz quickstart>`

      #. :ref:`Supported carriers <ad_fmcadc5_ebz carriers>`
      #. :ref:`Hardware setup <ad_fmcadc5_ebz hardware-setup>`
      #. :ref:`VC707 quick start <vc707_quickstart>`

   #. :ref:`User guide <ad_fmcadc5_ebz user-guide>`

      #. :ref:`Hardware guide <ad_fmcadc5_ebz hardware-guide>`
      #. :ref:`Software guide <ad_fmcadc5_ebz software-guide>`

#. Design with the AD9625

   - :adi:`AD9625` product page

   - Resources for designing a custom AD9625-based platform:

     #. For Linux software:

        - :external+linux:ref:`AD9625 AXI Linux driver <axi-adc-hdl>`
        - :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
        - :external+linux:ref:`JESD204B/C AXI_ADXCVR Linux driver <axi_adxcvr>`

#. :ref:`Help and Support <help-and-support>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
