.. collection:: AD9084-FMCA-EBZ
   :subtitle: Evaluating the Apollo MxFE Quad, 16-Bit, 28GSPS RF DAC and Quad, 12-Bit, 20 GSPS RF ADC
   :image: ../images/ad9084.png
   :label: eval user-guide

   system-level:
     - User guide <.>

   hdl:
     - HDL Project (ad9084_ardz) <projects/ad9084_ebz/index>

   linux:
     - Linux driver (ad9084) <drivers/iio-trx-rf/ad9088>

.. _ad9084:

AD9084-FMCA-EBZ (Apollo)
===============================================================================

Apollo MxFE Quad, 16-Bit, 28GSPS RF DAC and Quad, 12-Bit, 20 GSPS RF ADC.

.. image:: ../images/ad9084.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9084` is an FMC radio card for the :adi:`AD9084`,
mixed signal front end (MxFE®), highly integrated device with a 16-bit,
28 GSPS maximum sample rate, RF digital-to-analog converter (DAC) core,
and 12-bit, 20 GSPS maximum sample rate, RF analog-to-digital converter
(ADC) core. The :adi:`AD9084` supports four transmit channels and four
receive channels.

The :adi:`AD9084` is well suited for applications requiring both wideband ADCs
and DACs to process signal(s) having wide instantaneous bandwidth. The device
features a 48 lane, 32.5 Gbps JESD204C or 20 Gbps JESD204B data transceiver
port, an on-chip clock multiplier, and a digital signal processing (DSP)
capability targeted at either wideband or multiband, direct to RF applications.

The :adi:`AD9084` also features a bypass mode that allows the full bandwidth
capability of the ADC and/or DAC cores to bypass the DSP data-paths. The device
also features low latency loopback and frequency hopping modes targeted at
phased array radar systems and electronic warfare applications.

Features:

- Reconfigurable mixed signal platform design
- 4 16-bit RF DACs and 4 12-bit RF ADCs (4T4R)
- Usable RF analog bandwidth to 18GHz
- Fast detect with low latency for fast AGC control
- Spectrum sniffer and monitor
- Signal monitor for slow AGC control
- Multiple loopback (ADC to DAC)
- Power amplifier downstream protection circuitry
- Maximum DAC/ADC sample rate up to 28GSPS/20GSPS
- Versatile digital features
- Maximum instantaneous bandwidth of 10GHz per channel
  (2T2R)
- Programmable FIR filters at full ADC and DAC sample rates
- Configurable fine and coarse DDCs and DUCs
- Fast frequency hopping with profiles
- Dynamic configuration through SPI, HSCI, GPIO, or external
  trigger (TRIG)
- Programmable fractional data rate resampler from 1× to 2×
- JESD204B and JESD204C: 20Gbps and 28.21Gbps
- On-chip temperature monitoring unit
- Package: 24mm × 26mm, 899-ball BGA with 0.8mm pitch

Applications:

- Radar and phase array systems
- Seeker front end
- Tactical defense radio infrastructure
- Electronic warfare and signal intelligence
- Wireless communications infrastructure
- Wireless communications test (5G mmWave, 5G C band, backhaul)

.. image:: ../images/eval_ad9084.png
   :align: center
   :width: 600px

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`AD9084`, we recommend to use the
:adi:`EVAL-AD9084` evaluation board.


Table of Contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`ad9084 user-guide` - what you need to know about the
      evaluation board
   #. :ref:`ad9084 prerequisites` - what you need to get started with the setup
   #. :ref:`ad9084 quickstart`:

      #. Using the :ref:`Agilex 7/ SoC I-Series <ad9084 quickstart agilex>`
      #. Using the :ref:`VCU118/VCU128/ Virtex UltraScale+ <ad9084 quickstart microblaze>`
      #. Using the :ref:`VCK190/VPK180/ Versal ACAP  <ad9084 quickstart versal>`

#. Use the board to better understand the :adi:`AD9084`

      #. :external+kuiper:doc:`Configure a SD Card <hardware-configuration>`
      #. :external+kuiper:ref:`package-management`
      #. :ref:`AD9084 (Apollo) Profile Generator <ad9084 profile-generator>`
      #. :ref:`Running a new JESD mode on hardware <ad9084 quickstart new_usecase>`

   #. Linux Applications

      #. :ref:`IIO Oscilloscope <ad9084 iio-oscilloscope>` with:

         - :ref:`AD9084 Plugin <ad9084 iio-oscilloscope-plugin>`

      #. :doc:`FRU EEPROM Utility </software/fru_dump>`

#. Design with the AD9084

   #. :ref:`ad9084 block-diagram`

      #. :adi:`AD9084 Product page <AD9084>`
      #. `Full Datasheet and chip design package <TODO>`__

   #. Design a custom AD9084 based platform

      #. Linux software

         .. #. `AD9084 Linux Device Driver <TODO>`__

            .. #. `AD9084 Device Driver Customization <TODO>`__

         #. :external+linux:ref:`jesd204-fsm-framework`
         #. :external+hdl:ref:`axi_dmac`
         #. :external+hdl:ref:`axi_jesd204_tx`

            #. :doc:`JESD204B Status Utility </software/jesd/jesd_status>`

         #. :external+hdl:ref:`axi_jesd204_rx`

            #. :doc:`JESD204B Status Utility </software/jesd/jesd_status>`

         #. :external+hdl:ref:`axi_adxcvr`

            #. :doc:`JESD204 Eye Scan </software/jesd/jesd_eye_scan>`

         #. :external+linux:ref:`axi-adc-hdl`
         #. :external+linux:ref:`axi-dac-dds-hdl`

      .. #. :dokuwiki:`HDL Reference Design <resources/eval/user-guides/ad9084/reference_hdl>` which you must use in your FPGA.

.. #. `Help and Support <TODO>`__

Pre-requisites and quickstart
-------------------------------------------------------------------------------

.. toctree::
   :caption: The prerequisites and quickstart guides are provided at:
   :titlesonly:
   :maxdepth: 1

   user-guide
   prerequisites
   quickstart/index

.. _ad9084 block-diagram:

Functional Block Diagram
-------------------------------------------------------------------------------

.. image:: ../images/apollo_block_diagram.png
   :width: 600px

Warning
-------------------------------------------------------------------------------

.. esd-warning::