.. _fmcomms8:

AD-FMCOMMS8-EBZ
===============================================================================

Quad Wideband RF Transceiver FMC Module.

.. image:: images/adrv9009-bc.jpg
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD-FMCOMMS8-EBZ` is an integrated RF design containing two Analog
Devices :adi:`ADRV9009` wideband transceivers. By connecting to a compatible
FPGA development board that supports FMC HPC mechanical connector and JESD204B
bus interface it can be used for evaluation and prototyping with up to 4
Transmit and Receive channels that can be synchronised in phase and frequency.
Additionally it can be used with the ADRV9009-ZU11EG RF-SOM system, giving a
path to evaluating and prototyping with up to 8 phase and frequency synchronised
Transmit and Receive channels for complex multi-stream applications ensuring
end-to-end deterministic latency.

The ADRV9009 Transceivers include integrated LO and phase synchronization.
Overall system frequency and phase synchronization is maintained with a clock
tree structure using ADI high performance low jitter :adi:`HMC7044` device,
making it ideal for applications requiring RF phase alignment with a large
number of channels.

Features:

- Two :adi:`ADRV9009` devices providing quad transmitters, quad
  receivers, and quad input observation receivers for DPD
- Max Rx BW: 200 MHz
- Max Tunable Tx synthesis BW: 450 MHz
- Max Observation Rx BW: 450 MHz
- Fully integrated fractional-N RF synthesizers
- Multi-chip phase synchronization for all RF LO and baseband clocks
- Tuning range: 75 MHz to 6000 MHz
- FMC HPC compatible interface
- VITA 57.1 mechanical dimensions (84 mm x 69 mm)

Applications:

- Multi-channel RF systems
- Digital pre-distortion (DPD)
- Phased array and beamforming
- Software-defined radio (SDR)
- MIMO communications

.. figure:: images/ad-fmcomms8-ebz-evalboard.png
   :align: center
   :width: 500

   EVAL-AD-FMCOMMS8-EBZ

.. toctree::
   :hidden:

   prerequisites
   user-guide
   quickstart/index
   testing

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the :ref:`Help and Support <fmcomms8
help_and_support>` section at the bottom of the page.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <fmcomms8 prerequisites>` - what you need to get started
   #. :ref:`Quick start guides <fmcomms8 quickstart>`:

      #. Using the :dokuwiki:`ADRV9009-ZU11EG <resources/eval/user-guides/ad-fmcomms8-ebz/quick-start-guide>`
      #. Using the :ref:`ZCU102 <fmcomms8 quickstart zcu102>`
      #. Using the :ref:`Arria10 SoC <fmcomms8 quickstart a10soc>`

   #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`

#. Design with the ADRV9009

   #. :ref:`fmcomms8 block-diagram`
   #. :adi:`ADRV9009 product page <ADRV9009>`
   #. :adi:`Full datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
   #. :download:`MATLAB Filter Wizard / Profile Generator for ADRV9009 <https://www.analog.com/media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`
   #. Hardware in the Loop / How to design your own custom BaseBand

      - :ref:`GNU Radio <software gnuradio>`
      - :ref:`Transceiver Toolbox <matlab transceiver-toolbox>`

   #. Resources for designing a custom ADRV9009-based platform

      #. For Linux software:

         #. :external+linux:ref:`ADRV9009 Linux device driver <adrv9009>`
            - :external+linux:ref:`ADRV9009 Device Driver Customization <adrv9009-customization>`
            - :ref:`Customizing the devicetree on the target <linux-kernel zynq>`

         #. :external+linux:doc:`JESD204 (FSM) Interface Linux Kernel framework <drivers/jesd204/jesd204-fsm-framework>`
         #. :external+linux:doc:`HMC7044 Clock Linux driver <drivers/iio-pll/hmc7044>`
         #. :external+linux:doc:`JESD204B Transmit Linux driver <drivers/jesd204/axi_jesd204_tx>`

            - :external+hdl:ref:`axi_jesd204_tx`
            - :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

         #. :external+linux:doc:`JESD204B Receive Linux driver <drivers/jesd204/axi_jesd204_rx>`

            - :external+hdl:ref:`axi_jesd204_rx`
            - :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

         #. :external+linux:doc:`AXI_ADXCVR Highspeed Transceivers Linux driver <drivers/jesd204/axi_adxcvr>`

            - :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`

         #. :external+linux:doc:`AXI ADC HDL Linux driver <drivers/iio-adc/axi-adc-hdl>`
         #. :external+linux:doc:`AXI DAC HDL Linux driver <drivers/iio-dds/axi-dac-dds-hdl>`
         #. :external+linux:doc:`AXI-DMAC DMA Controller Linux driver <drivers/dma/axi-dmac>`
         #. :external+hdl:ref:`axi_dmac`

      #. :external+no-OS:doc:`ADRV9009 No-OS System Level Design Setup <drivers/rf-transceiver/talise>`

      #. :external+hdl:doc:`HDL reference design <projects/fmcomms8/index>`

#. :ref:`Production testing <fmcomms8 testing>`

#. :ref:`Help and Support <fmcomms8 help_and_support>`

.. _fmcomms8 block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. image:: images/adrv9009_bd_diag.png
   :align: center
   :width: 800

Warning
-------------------------------------------------------------------------------

.. esd-warning::

.. _fmcomms8 help_and_support:

Help and support
-------------------------------------------------------------------------------

For questions and more information, please visit the :ez:`/` technical support
community.
