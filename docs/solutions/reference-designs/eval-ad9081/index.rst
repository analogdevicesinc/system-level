.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad9081_fmca_ebz

.. _ad9081:

AD9081 & AD9082
===============================================================================

MxFE™ Quad, 16-Bit, 12GSPS RFDAC and Quad, 12-Bit, 4/6 GSPS RFADC.

.. figure:: ../images/ad9081.webp
   :align: left
   :width: 150

   AD9081 MxFE

.. figure:: ../images/ad9082.webp
   :align: left
   :width: 120

   AD9082 MxFE

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9081` is an FMC radio card for the :adi:`AD9081`, mixed signal
front end (MxFE®), highly integrated device with four 16-bit, 12 GSPS maximum
sample rate, RF DAC cores, and four 12-bit, 4 GSPS rate, RF ADC cores.
The :adi:`AD9081` model is 4D4AC, supporting 4 DACs and 4 ADCs.

The :adi:`AD9081` / :adi:`AD9082` are well suited for applications requiring both
wideband ADCs and DACs to process signal(s) that have wide instantaneous bandwidth.
The device features 8 transmit and 8 receive lanes that support
24.75 Gbps/lane JESD204C or 15.5 Gbps/lane JESD204B standards. The device
also has an on-chip clock multiplier, and a digital signal processing (DSP)
capability targeted at either wideband or multiband direct to RF applications.

The :adi:`EVAL-AD9082` is an FMC radio card for the :adi:`AD9082`, mixed signal
front-end (MxFE®) is a highly integrated device with a 16-bit, 12 GSPS maximum
sample rate, RF DAC core, and 12-bit, 6 GSPS maximum sample rate, RF ADC cores.
The :adi:`AD9082` model is 4D2AC, supporting 4 DACs and 2 ADCs, and 2D2AC model
supporting 2 DACs and 2 ADCs.

Features:

- Fast frequency hopping
- Direct digital synthesis (DDS)
- Loopback modes
- Digital up/down converters (DUC/DDC)
- Programmable filters and gain control
- JESD204B/C interface (up to 24.75 Gbps)
- Multichip synchronization
- TDD power savings

Applications:

- Wireless communications infrastructure
- Microwave point-to-point, E-band and 5G mmWave
- Broadband communications systems
- DOCSIS 3.1 and 4.0 CMTS
- Phased array radar and electronic warfare
- Electronic test and measurement systems

:adi:`EVAL-AD9081` looks like this, with 4x ADCs and 4x DACs:

.. figure:: ../images/eval_ad9081.png
   :align: center
   :width: 400

   EVAL-AD9081 evaluation board

While :adi:`EVAL-AD9082` looks like this, with 2x ADCs and 4x DACs:

.. figure:: ../images/eval_ad9082.png
   :align: center
   :width: 450

   EVAL-AD9082 evaluation board

.. toctree::
   :hidden:

   2to24ghz-mxfe-rf-front-end
   ad9081
   ad9081_plugin
   ad9081_ace
   prerequisites
   quickstart/index
   user-guide

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9081` / :adi:`AD9082`, we recommend to use
the :adi:`EVAL-AD9081` / :adi:`EVAL-AD9082` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad9081 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`ad9081 prerequisites` - what you need to get started with the setup
   #. :ref:`ad9081 quickstart`:

      #. Using the :ref:`Arria 10 SX SoC <ad9081 quickstart a10soc>`
      #. Using the :ref:`VCK190 & VPK180/Versal <ad9081 quickstart vck190>`
      #. Using the :ref:`VCU118/ Virtex UltraScale+ <ad9081 quickstart vcu118>`
      #. Using the :ref:`ZC706/ Zynq-7000 SoC <ad9081 quickstart zc706>`
      #. Using the :ref:`ZCU102/Zynq UltraScale+ MP SoC <ad9081 quickstart zcu102>`


   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`ad9081 iio-osc-plugin`

#. Design with the AD9081/AD9082

   - :ref:`ad9081 block-diagram`

     - :adi:`AD9081 product page <AD9081>`
     - :adi:`AD9082 product page <AD9082>`

   - Hardware in the Loop / How to design your own custom BaseBand

     - :ref:`GNU Radio <software gnuradio>`
     - :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   - Resources for designing a custom AD9081/AD9082-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`axi_jesd204_tx`
           - :external+linux:ref:`axi_jesd204_rx`
           - :external+linux:ref:`axi_adxcvr`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dac-dds-hdl`
           - :external+linux:ref:`axi-dmac`
           - :external+linux:ref:`ad9081`

        #. About the device tree:

           - :dokuwiki:`Customizing the device tree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

        #. About the JESD204 utilities:

           - :external+linux:ref:`jesd204-fsm-framework`
           - :external+linux:ref:`hmc7044`
           - :dokuwiki:`JESD204 status utility <resources/tools-software/linux-software/jesd_status>`
           - :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`
           - :external+hdl:ref:`jesd204`

     #. :external+hdl:ref:`HDL reference design <ad9081_fmca_ebz>` which you must use in your FPGA
     #. :ref:`ad9081 evaluating-using-ace`

#. :adi:`Evaluating the AD9081/AD9082/AD9986/AD9988 Mixed Signal, Front-End RF Transceiver with ACE software <media/en/technical-documentation/user-guides/eval-ad9081-9082-9986-9988-ug-1829.pdf>`
#. :adi:`UG-1578, Device User Guide <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`
#. :ref:`ad9081 2to24ghz-mxfe-rf-front-end`
#. :dokuwiki:`Additional documentation about SDR Signal Chains - The math behind the RF <resources/eval/user-guides/ad-fmcomms1-ebz/math>`
#. :ref:`Help and Support <help-and-support>`

.. _ad9081 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: ../images/ad9081_block_diagram.png
   :align: center
   :width: 700

   AD9081 block diagram

.. figure:: ../images/ad9082_block_diagram.png
   :align: center
   :width: 700

   AD9082 block diagram

Videos
-------------------------------------------------------------------------------

- :adi:`Fan assembly for the MxFE evaluation board <resources/media-center/videos/6264484847001.html>`
- :adi:`Unboxing & setting up the MxFE evaluation board <resources/media-center/videos/6264485594001.html>`

ADI articles
-------------------------------------------------------------------------------

About JESD standard:

#. :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
#. :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
