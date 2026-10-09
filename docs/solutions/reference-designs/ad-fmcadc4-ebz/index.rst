.. _ad_fmcadc4_ebz eval:

AD-FMCADC4-EBZ (Obsolete)
===============================================================================

14-Bit, 1000 MSPS, Quad-Channel, JESD204B, RF Data Acquisition FMC Board.

.. warning::

   The :adi:`AD-FMCADC4-EBZ` is a **legacy product** that has been retired
   and is no longer available for sale. It has been removed from the HDL and
   software repositories, but is still available in the git history. This
   documentation is provided for reference only.

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCADC4-EBZ` is a high speed four-channel data acquisition board
featuring two :adi:`AD9680` dual channel ADCs at 1000 MSPS and four
:adi:`ADA4961` low distortion, 3.2 GHz, RF Digital Gain Amplifiers driving
each converter. The FMC form factor supports the JESD204B high speed serial
interface. All clocking and channel synchronization is provisioned on-board
using the :adi:`AD9528` clock generator.

Although this board does meet most of the FMC specifications, it is not meant
as a commercial off the shelf (COTS) board. This board is targeted to use the
ADI reference designs that work with Xilinx development systems.

The card contains:

- :adi:`AD9680` 14-bit dual channel ADC with sampling speeds of up to
  1250 MSPS, with a :adi:`JESD204B <JESD204>` digital interface.
- :adi:`ADA4961` Low Distortion, 3.2 GHz, RF Digital Gain Amplifier.
- :adi:`AD9528` JESD204B Clock Generator with 14 LVDS Outputs
- :adi:`ADP2384` 20 V, 4 A, Synchronous, Step-Down DC-to-DC Regulator
- :adi:`ADP7104` 20 V, 500 mA, low noise, CMOS LDO
- :adi:`ADM7154` 600 mA, Ultra Low Noise, High PSRR, RF Linear Regulator
- :adi:`ADM7172` 6.5 V, 2 A, Ultralow Noise, High PSRR, Fast Transient
  Response CMOS LDO
- :adi:`ADP1741` 2 A, low V\ :sub:`IN`\, low dropout, CMOS linear regulator

.. figure:: images/20150331_135648-final.jpg
   :alt: AD-FMCADC4-EBZ evaluation board (top view)
   :align: center
   :width: 600

   AD-FMCADC4-EBZ Evaluation Board (top view)

.. figure:: images/20150402_100228-finalbot.jpg
   :alt: AD-FMCADC4-EBZ evaluation board (bottom view)
   :align: center
   :width: 600

   AD-FMCADC4-EBZ Evaluation Board (bottom view)

Features:

- Four channels of 1.0 GSPS conversion utilizing JESD204B high speed serial
  interface
- Driver amplifier interface with 21 dB voltage gain adjustment
- Optional on-board or external clocking
- Specific design and I/O added for multi-board synchronization

Applications:

- Spectrum analyzers
- Radar
- Jamming / anti-jamming measures
- Data acquisition systems
- Military electronics

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

   #. :ref:`Prerequisites <ad_fmcadc4_ebz prerequisites>`
   #. :ref:`Quick start guides <ad_fmcadc4_ebz quickstart>`

      #. :ref:`Supported carriers <ad_fmcadc4_ebz carriers>`
      #. :ref:`Hardware setup <ad_fmcadc4_ebz hardware-setup>`

   #. :ref:`User guide <ad_fmcadc4_ebz user-guide>`

      #. :ref:`Hardware guide <ad_fmcadc4_ebz hardware-guide>`
      #. :ref:`Software guide <ad_fmcadc4_ebz software-guide>`

#. Design with the AD9680

   - :adi:`AD9680` product page

   - Resources for designing a custom AD9680-based platform:

     #. For Linux software:

        - :external+linux:ref:`AD9680 AXI Linux driver <axi-adc-hdl>`
        - :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
        - :external+linux:ref:`JESD204B/C AXI_ADXCVR Linux driver <axi_adxcvr>`

#. :ref:`Help and Support <help-and-support>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
