.. imported from: https://wiki.analog.com/resources/eval/user-guides/mykonos

.. _mykonos:

AD9371 & AD9375 Prototyping Platform User Guide
===============================================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9371-bc_196-adi_m.png
   :width: 300px

The :adi:`ADRV9371-W/PRBZ <EVAL-ADRV9371>`,
:adi:`ADRV9371-N/PCBZ <EVAL-ADRV9371>` and :adi:`ADRV9375-N/PCBZ <ADRV9375>` are
FMC radio cards for the :adi:`AD9371` respectively :adi:`AD9375`, a highly
integrated RF Transceiver™. While the complete chip level design package can be
found on the the
:adi:`the ADI web site <en/license/licensing-agreement/ad9371.html>`,
information on the card and how to use it, the design package that surrounds it,
and the software which can make it work can be found here.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9371-n_pcbz_side.jpg
   :width: 600px

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:dokuwiki:`ask <ad-fmcomms2-ebz/help_and_support>`.

#. Use the board to better understand the AD9371/AD9375

   #. :dokuwiki:`What you need to get started <mykonos/prerequisites>`
   #. :dokuwiki:`Quick Start Guides <mykonos/quickstart>`

      #. :dokuwiki:`Linux on ZC706 <mykonos/quickstart/zynq>`
      #. :dokuwiki:`Linux on Arria 10 SOC <adrv9371/quickstart/a10soc>`
      #. :ref:`kuiper`
      #. :ref:`kuiper`

   #. Linux Applications

      #. :dokuwiki:`IIO Scope <resources/tools-software/linux-software/iio_oscilloscope>`

         #. :dokuwiki:`AD9371/AD9375 IIO Scope View <resources/tools-software/linux-software/ad9371_osc_main>`
         #. :dokuwiki:`AD9371/AD9375 Control IIO Scope Plugin <resources/tools-software/linux-software/ad9371_plugin>`
         #. :dokuwiki:`Advanced AD9371/AD9375 Control IIO Scope Plugin <resources/tools-software/linux-software/ad9371_advanced_plugin>`

      #. :dokuwiki:`FRU EEPROM Utility </resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`

   #. Push custom data into/out of the AD9371/AD9375

      #. :dokuwiki:`Basic Data files and formats <mykonos/software/basic_iq_datafiles>`
      #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/transceiver-toolbox>`
      #. :dokuwiki:`Python Interfaces </resources/tools-software/linux-software/pyadi-iio>`

#. Design with the AD9371/AD9375

   #. :dokuwiki:`Understanding the AD9371/AD9375 <mykonos/ad9371>`

      #. :adi:`AD9371 Product page <AD9371>`
      #. :adi:`AD9375 Product page <AD9375>`
      #. :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
      #. :dokuwiki:`MATLAB Filter Wizard / Profile Generator for AD9371 <mykonos/software/filters>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. :dokuwiki:`GNU Radio </resources/tools-software/linux-software/gnuradio>`
      #. :dokuwiki:`Transceiver Toolbox </resources/tools-software/transceiver-toolbox>`

   #. Design a custom AD9371/AD9375 based platform

      #. Linux software

         #. :dokuwiki:`AD9371/AD9375 Linux Device Driver </resources/tools-software/linux-drivers/iio-transceiver/ad9371>`

            #.  :dokuwiki:`Customizing the devicetree on the target <ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

         #. :dokuwiki:`AD9528 Low Jitter Clock Generator Linux Driver </resources/tools-software/linux-drivers/iio-pll/ad9528>`
         #. :dokuwiki:`AD7291 IIO ADC Linux Driver </resources/tools-software/linux-drivers/iio-adc/ad7291>`
         #. :dokuwiki:`JESD204B Transmit Linux Driver </resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

            #. :dokuwiki:`JESD204B Status Utility </resources/tools-software/linux-software/jesd_status>`

         #. :dokuwiki:`JESD204B Receive Linux Driver </resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

            #. :dokuwiki:`JESD204B Status Utility </resources/tools-software/linux-software/jesd_status>`

         #. :dokuwiki:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

            #. :dokuwiki:`JESD204 Eye Scan </resources/tools-software/linux-software/jesd_eye_scan>`

         #. :dokuwiki:`AXI ADC HDL Linux Driver </resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         #. :dokuwiki:`AXI DAC HDL Linux Driver </resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

      #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile </resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
      #. :dokuwiki:`AD9371/AD9375 No-OS System Level Design Setup </resources/eval/user-guides/mykonos/no-os-setup>`
      #. :dokuwiki:`HDL Reference Design <mykonos/reference_hdl>` which you must
         use in your FPGA.
      #. :dokuwiki:`Transceiver Toolbox: HDL Targeting with MATLAB and Simulink </resources/tools-software/transceiver-toolbox>`

#. :dokuwiki:`Additional Documentation about SDR Signal Chains - The math behind the RF <ad-fmcomms1-ebz/math>`
#. :dokuwiki:`Help and Support <ad-fmcomms2-ebz/help_and_support>`

Videos
------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
~~~~~~~~~~~~

- Four Quick Steps to Production: Using Model-Based Design for Software-Defined
  Radio
- :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
- :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
- :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
- :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~

- :mw:`Modelling and Simulating Analog Devices" RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
- :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Warning
-------

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning
