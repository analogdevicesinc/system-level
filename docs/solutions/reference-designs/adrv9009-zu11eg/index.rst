.. _adrv9009-zu11eg:

ADRV9009-ZU11EG RF System-on-Module
===================================

RF System on Module using the ADRV9009 Wideband Transceiver

.. image:: ./images/adrv9009.png
   :align: left
   :width: 150

Overview
--------

The :adi:`ADRV9009-ZU11EG` :adi:`Export Info <ADRV9009-ZU11EG>` is a highly
integrated RF System-On-Module (RF-SOM) based on the Analog Devices
:adi:`ADRV9009` and Xilinx
`Zynq UltraScale+ MPSoC <https://www.xilinx.com/products/silicon-devices/soc/zynq-ultrascale-mpsoc.html>`__.
The RF-SOM is a platform for evaluation and prototyping. To use the RF-SOM a
carrier board is required. The Analog Devices ADRV2CRR-FMC Carrier board is
designed for this purpose. An additional RF Transceiver board can also be
fitted to the carrier to further expand the system up to 8 Tx and Rx radio
channels.

**The RF-SOM box includes:**

- ADRV9009-ZU11EG RF-SOM
- Heat spreader plate (fitted to the RF-SOM during manufacturing)

**The Carrier box includes:**

- ADRV2CRR-FMC carrier board, SD-Card, Fan Heatsink and other accessories
- Full details found in the Carrier section

Features:

- Quad transmitters
- Quad receivers
- Quad input Observation Receiver for DPD
- Max Rx BW: 200 MHz
- Max Tunable Tx synthesis BW: 450 MHz
- Max Observation Rx BW: 450MHz
- Fully integrated fractional-N RF synthesizers
- Multi-chip phase synchronization for all RF LO and baseband clocks
- Tuning range: 75 MHz to 6000 MHz

Applications:

- 3G, 4G, and 5G TDD macrocell base stations
- TDD active antenna systems
- Massive multiple input, multiple output (MIMO)
- Phased array radar
- Electronic warfare
- Military communications
- Portable test equipment

.. image:: ./images/adrv9009-zu11eg.png
   :align: center
   :width: 600

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of Contents
-----------------

#. Getting started with the ADRV9009-ZU11EG

   #. :ref:`ADRV9009-ZU11EG User Guide <adrv9009-zu11eg user-guide>`
   #. :ref:`What you need to get started <adrv9009-zu11eg prerequisites>`
   #. :ref:`ADRV9009-ZU11EG Quick Start Guide <adrv9009-zu11eg quickstart>`

      #. :external+kuiper:ref:`Configure a pre-existing SD-Card <use-kuiper-image>`
      #. :external+kuiper:ref:`Update the old card you received with your hardware <use-kuiper-image>`

   #. :ref:`Performance Characteristics <adrv9009-zu11eg performance>`
   #. Linux Applications

      #. :ref:`iio-oscilloscope`

         #. :ref:`ADRV9009/ADRV9008 IIO Scope View <iio-oscilloscope adrv9009>`
         #. :ref:`ADRV9009/ADRV9008 Control IIO Scope Plugin <iio-oscilloscope adrv9009 plugin>`
         #. :ref:`Advanced ADRV9009/ADRV9008 Control IIO Scope Plugin <iio-oscilloscope adrv9009 advanced-plugin>`

   #. :ref:`FRU EEPROM Utility <software fru-dump>`
   #. Push custom data into/out of the ADRV9009

      #. :ref:`Basic Data files and formats <adrv9009 basic-iq-datafiles>`
      #. :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`

   #. Design with the ADRV9009

      #. Understanding the ADRV9009

         #. :adi:`ADRV9009` Product page
         #. `Full Datasheet and chip design package <https://www.analog.com/en/lp/001/integrated-rf-agile-transceiver-design-resources.html>`__
         #. `MATLAB Filter Wizard / Profile Generator for ADRV9009 <https://www.analog.com/media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`__

      #. Hardware in the Loop / How to design your own custom BaseBand

         #. :ref:`GNU Radio <software gnuradio>`
         #. :ref:`Board Support Package for MathWorks Tools <matlab transceiver-toolbox>`

      #. Design with the ADRV9009-ZU11EG based platform

         #. Linux software

            #. :ref:`ADRV9009/ADRV9008 Linux Device Driver <iio-transceiver adrv9009>`

               #. :ref:`ADRV9009/ADRV9008 Device Driver Customization <iio-transceiver adrv9009 customization>`
               #. :ref:`Customizing the devicetree on the target <linux-kernel zynq-tips-tricks>`

            #. :dokuwiki:`JESD204 (FSM) Interface Linux Kernel Framework <resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
            #. :dokuwiki:`HMC7044 Clock Jitter Attenuator with JESD204B Linux Driver <resources/tools-software/linux-drivers/iio-pll/hmc7044>`
            #. :dokuwiki:`AXI-DMAC DMA Controller Linux Driver <resources/tools-software/linux-drivers/axi-dmac>`
            #. :dokuwiki:`JESD204B Transmit Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

               #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

            #. :dokuwiki:`JESD204B Receive Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

               #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

            #. :dokuwiki:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

               #. :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`

            #. :dokuwiki:`AXI ADC HDL Linux Driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
            #. :dokuwiki:`AXI DAC HDL Linux Driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

         #. :dokuwiki:`ADRV9009/ADRV9008 No-OS System Level Design Setup <resources/eval/user-guides/adrv9009/no-os-setup>`
         #. :external+hdl:ref:`HDL Reference Design <adrv9009zu11eg>`
         #. :ref:`ADRV9009 and ADRV9009-ZU11EG JESD Parametrization <adrv9009-zu11eg adrv9009-config>`
         #. :doc:`ADRV9009-ZU11EG Multi-SOM Synchronization </solutions/reference-designs/adrv9009-zu11eg/syncronization>`
         #. :ref:`ADRV9009-ZU11EG Phase Synchronization <adrv9009-zu11eg phase-sync>`

Reference Material
------------------

.. image:: images/sdr_book.png
   :width: 200
   :align: left

:adi:`Software Defined Radio for Engineers <en/education/education-library/software-defined-radio-for-engineers.html>`

:ref:`Additional Documentation about SDR Signal Chains - The math behind the RF <fmcomms2 common fmcomms-math>`

Functional Test
---------------

Details on how the ADRV9009-ZU11EG is functionally tested can be found here.

-  :doc:`ADRV9009-ZU11EG Production Test </solutions/reference-designs/adrv9009-zu11eg/testing>`

Pre-requisites and quickstart
-------------------------------------------------------------------------------

.. toctree::
   :caption: Getting Started
   :titlesonly:
   :maxdepth: 1

   user-guide
   prerequisites
   quickstart/index

.. _adrv9009-zu11eg block-diagram:

Functional Block Diagram
-------------------------------------------------------------------------------

.. image:: ./images/adrv9009_blockdiagram.png
   :width: 600

Help and Support
----------------

For questions and more information please contact us on the Analog Devices
Engineer Zone.

.. hint::

   :ez:`fpga`

.. esd-warning::

.. toctree::
   :hidden:

   adrv2crr-fmc_carrier_board
   hardware
   adrv9009-config
   performance
   phase-sync
   pre-release
   syncronization
   testing
