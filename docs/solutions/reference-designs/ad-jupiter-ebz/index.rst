.. imported from: https://wiki.analog.com/resources/eval/user-guides/jupiter-sdr

.. _ad-jupiter-ebz:

AD-JUPITER-EBZ
===============

Software-Defined Radio Module.

Overview
--------

:adi:`AD-JUPITER-EBZ` is a versatile software-defined platform based on Analog
Devices :adi:`ADRV9002` and
:xilinx:`AMD Xilinx Zynq UltraScale+ MPSoC. <products/adaptive-socs-and-fpgas/soc/zynq-ultrascale-plus-mpsoc.html>`
:adi:`ADRV9002` is a new generation RF transceiver that has dual-channel
transmitters, dual-channel receivers covering 30 MHz to 6 GHz frequency range
with very good RF linearity performance and a set of advanced features like fast
profiles switching, flexible power vs performance configuration, fast frequency
hopping, multi-chip synchronization and DPD for narrow and wide band waveform.
The evaluation platform includes XCZU3EG processing device that has a wide range
of interfaces making the system capable of local processing or streaming to a
remote host. It comes integrated in a self-contained ruggedised aluminum case
which gives flexibility in evaluating and prototyping across different
environments.

.. figure:: images/jupitersdr_back1.png
   :align: center

.. figure:: images/jupitersdr_front1.png
   :align: center

The platform comes with open-source software that includes:

- Linux and no-OS
- HDL reference design
- IIO
- MATLAB
- GNU Radio
- Python

Key Features
------------

- RF/SDR
     - ADRV9002 transceiver
         - 2 x RX, 2 x TX
         - LO Frequency range 30 MHz to 6 GHz
         - 12 KHz to 40 MHz frequency bandwidth
         - Sampling rate 12 KS/s to 61.44 MS/s
     - External device clock input
     - External MCS input
     - RF Front-end
- Processing system
     - AMD Xilinx Zynq UltraScale+ MPSoC XCZU3EG
         - ARM CORTEX-A53 1.5GHz
         - ARM CORTEX-R5 500 MHz
         - Mali-400 MP2 graphic processor
         - Programmable logic 154k
     - DDR4 – 2 GB (x32)
     - Boot source
         - SD CARD 3.0
         - FLASH memory 128MB
- User Interfaces
     - USB 3.1 Gen 1 – Type C
         - Upstream Facing Port (UFP)
         - Downstream Facing Port (DFP)
         - USB 2.0 compatible
     - Ethernet 1000BASE-T RGMII
     - Display Port v1.2 (2 lanes 5.4Gb/s)
     - SATA 3
     - USB (micro) debug interface
     - 16 GPIOs (3V3 LVCMOS)
- Power Sources
     - USB Type-C (power only)
         - Power Sink 5V, 9V/3A
     - USB Type-C (data)
         - Power Sink 5V/3A
         - Power Source 5V/0.9A
     - 802.3at POE compliant, 25.5W Type2 (POE+)

Applications
------------

- Software-defined radio (SDR)
- Electronic warfare
- Radar
- Communications
- Spectrum monitoring
- Test and measurement

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the
:ref:`Help and Support <ad-jupiter-ebz help-and-support>` section at the bottom
of the page.

To better understand the :adi:`ADRV9002`, we recommend to use
the :adi:`AD-JUPITER-EBZ` evaluation board.

Table of contents
-----------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Quick start guide <ad-jupiter-ebz quickstart>`
   #. Configure an SD Card with :external+kuiper:ref:`use-kuiper-image`
   #. Linux Applications

      #. :ref:`iio-oscilloscope`

         #. :dokuwiki:`ADRV9001/2 IIO Scope View <resources/tools-software/linux-software/adrv9002_osc_main>`
         #. :ref:`ADRV9001/2 Control IIO Scope Plugin <adrv9002-plugin>`
         #. :dokuwiki:`ADRV9001/2 Profile Generator Plugin <resources/tools-software/linux-software/adrv9002_profile_generator_plugin>`

      #. :external+scopy:ref:`adrv9002`
      #. :ref:`pyadi-iio`
      #. :ref:`libiio cli`

#. Design with the ADRV9002

   - :ref:`Block diagram <ad-jupiter-ebz block-diagram>`

     - :adi:`ADRV9002 Product page <ADRV9002>`
     - :adi:`Full Datasheet and chip design package <design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`

   - Hardware in the Loop / How to design your own custom baseband

     - :ref:`GNU Radio <software gnuradio>`
     - :ref:`matlab transceiver-toolbox`

   - Resources for designing a custom ADRV9002-based platform software

     #. For Linux software:

        #. About the device driver:

           - :external+linux:ref:`adrv9002`
           - :external+linux:ref:`adrv9002-customization`
           - :external+linux:ref:`axi-adc-hdl`
           - :external+linux:ref:`axi-dmac`

        #. About the device tree:

           - :ref:`linux-kernel zynqmp`

     #. For no-OS software:

        #. :external+no-OS:doc:`projects/rf-transceiver/adrv9001`

     #. :external+hdl:ref:`Jupiter SDR HDL Reference Design <jupiter_sdr>` which you must use in your FPGA.

        - :external+hdl:ref:`user_guide`
        - :external+hdl:ref:`ADRV9001 HDL reference design <adrv9001>`

   - Jupiter SDR Hardware Overview (see :ref:`ad-jupiter-ebz hardware-overview`)

   - Multi-chip synchronization support (see :ref:`ad-jupiter-ebz mcs-setup`)

   - :ref:`Additional Documentation about SDR Signal Chains - The math behind the RF <fmcomms2 common fmcomms-math>`

#. :ref:`Help and Support <ad-jupiter-ebz help-and-support>`

.. toctree::
   :hidden:

   quickstart/index
   hardware-overview
   mcs-setup
   known-issues
   production_testing/production-testing

Reference Material
------------------

- :adi:`ADRV9002: Narrow to Wide Band Integrated RF Transceiver <education/education-library/videos/6170462863001.html>`

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
~~~~~~~~~~~~

- Four Quick Steps to Production: Using Model-Based Design for Software-Defined
  Radio

  - :adi:`Part 1 - the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
  - :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
  - :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
  - :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~

- :mw:`Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
- :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

.. _ad-jupiter-ebz help-and-support:

Help and support
----------------

- Known issues (see :ref:`ad-jupiter-ebz known-issues`)
- For Hardware technical support go to:

  - :ez:`Design Support Community ADRV9001-ADRV9007 <wide-band-rf-transceivers/design-support-adrv9001-adrv9007>`

- For questions regarding the HDL reference design please use the

  - :ez:`FPGA Reference Designs <fpga>` sub-community.

- For questions regarding the ADI Linux distribution, the Linux drivers, or the
  device trees for the ADRV9001/2 based platforms, please use the

  - :ez:`Linux Software Drivers <linux-software-drivers>` sub-community.

- For questions regarding the no-OS drivers for ADRV9001/2, please use the

  - :ez:`Microcontroller and No-OS Driver <microcontroller-no-os-drivers>` sub-community.

.. esd-warning::
