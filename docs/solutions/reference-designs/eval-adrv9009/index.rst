.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9009

.. _adrv9009:

ADRV9009 & ADRV9008
===============================================================================

Integrated Dual RF Tx, Rx, and Observation Rx.

.. image:: images/adrv9009-bc.jpg
   :align: left
   :width: 150

The :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`, :adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>`
and :adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>` are FMC radio cards for the
:adi:`ADRV9009` and :adi:`ADRV9008`, respectively, a highly integrated RF Transceiver™.
While the complete chip level design package can be found on
:adi:`the ADI web site <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`,
information on the card and how to use it, the design package that surrounds it,
and the software which can make it work can be found here.

.. image:: images/adrv9009-PCB.jpg
   :align: center

.. toctree::
   :hidden:

   basic-iq-datafiles
   prerequisites
   quickstart/index

Table of Contents
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it should be.
If you have any questions, feel free to :ref:`ask <help-and-support>`.

#. Use the board to better understand the ADRV9009/ADRV9008-1/ADRV9008-2

   #. :ref:`What you need to get started <adrv9009 prerequisites>`
   #. :ref:`Quick Start Guides <adrv9009 quickstart>`:

      #. :ref:`On ZCU102 <adrv9009 quickstart zcu102>`
      #. :ref:`On ZC706 <adrv9009 quickstart zc706>`
      #. :ref:`On KCU105 <adrv9009 quickstart kcu105>`
      #. :ref:`On Arria 10 GX <adrv9009 quickstart a10gx>`
      #. :ref:`On Arria 10 SoC <adrv9009 quickstart a10soc>`
      #. Configure an SD Card with :external+kuiper:doc:`Kuiper <index>`

   #. Linux Applications

      #. :ref:`iio-oscilloscope`, with:

         #. :ref:`iio-oscilloscope adrv9009`
            (:ref:`iio-oscilloscope adrv9009 plugin`,
            :ref:`iio-oscilloscope adrv9009 advanced-plugin`)

      #. :ref:`FRU EEPROM Utility <software fru-dump-tool>`

   #. Push custom data into/out of the ADRV9009/ADRV9008

      #. :doc:`Basic Data files and formats <basic-iq-datafiles>`
      #. :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
      #. :ref:`Python Interfaces <pyadi-iio>`

#. Design with the ADRV9009/ADRV9008

   #. :ref:`adrv9009 blockdiagram`

      #. :adi:`ADRV9009 Product page <ADRV9009>`
      #. :adi:`ADRV9008 Product page <ADRV9008>`
      #. :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
      #. :adi:`MATLAB Filter Wizard / Profile Generator for ADRV9009 <media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`

   #. Hardware in the Loop / How to design your own custom baseband

      #. :ref:`GNU Radio <software gnuradio>`
      #. :ref:`Transceiver Toolbox <matlab transceiver-toolbox>`

   #. Design a custom ADRV9009/ADRV9008 based platform

      #. Linux software

         #. :external+linux:ref:`ADRV9009/ADRV9008 Linux Device Driver <adrv9009>`

            #. :external+linux:ref:`ADRV9009/ADRV9008 Device Driver Customization <adrv9009-customization>`
            #. :ref:`Customizing the devicetree on the target <linux-kernel zynq-tips-tricks>`

         #. :external+linux:ref:`jesd204-fsm-framework`
         #. :external+linux:ref:`ad9528`
         #. :external+linux:ref:`ad7291`
         #. :external+linux:ref:`axi-dmac`
         #. :external+linux:ref:`axi_jesd204_tx`

            #. :ref:`JESD204B Status Utility <software jesd-status>`

         #. :external+linux:ref:`axi_jesd204_rx`

            #. :ref:`JESD204B Status Utility <software jesd-status>`

         #. :external+linux:ref:`axi_adxcvr`

            #. :ref:`JESD204 Eye Scan <software jesd-eye-scan>`

         #. :external+linux:ref:`axi-adc-hdl`
         #. :external+linux:ref:`axi-dac-dds-hdl`

      #. :ref:`Changing the VCXO frequency and updating the default RF Transceiver Profile <software vcxo-profiles>`
      #. :external+no-OS:doc:`ADRV9009/ADRV9008 No-OS System Level Design Setup <projects/rf-transceiver/adrv9009>`
      #. :external+hdl:ref:`adrv9009` which you must use in your FPGA.
      #. :ref:`HDL Targeting From MATLAB and Simulink <matlab transceiver-toolbox>`

#. :ref:`Additional Documentation about SDR Signal Chains - The math behind the RF <fmcomms2 common fmcomms-math>`
#. :ref:`Help and Support <help-and-support>`

..
   TODO: Add reference to ADRV9009-ZU11EG JESD parametrization page when ported
   Wiki source: https://wiki.analog.com/resources/eval/user-guides/adrv9009-config

.. _adrv9009 blockdiagram:

Block diagram
-------------

.. image:: images/blockdiagram.png

Videos
-------------------------------------------------------------------------------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio

   #. :adi:`Part 1 - The Analog Devices/AMD Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   #. :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   #. :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   #. :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :mw:`Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
#. :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Unboxing guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ez:`Detailed unboxing guide <cfs-file/__key/communityserver-discussions-components-files/703/AD9371-and-ADRV9009-setup-with-ZCU102-or-ZC706-April2019.pdf>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
