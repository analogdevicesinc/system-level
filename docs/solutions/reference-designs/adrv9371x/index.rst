ADRV9371x
================================================================================

.. image:: images/ad9371-bc_196-adi_m.png
   :width: 250
   :align: left

The :adi:`ADRV9371-W/PRBZ <EVAL-ADRV9371>`,
:adi:`ADRV9371-N/PCBZ <EVAL-ADRV9371>`,
:adi:`ADRV9375-W/PRBZ <EVAL-ADRV9371>`, and
:adi:`ADRV9375-N/PCBZ <ADRV9375>` are FMC radio cards for the :adi:`AD9371` and
:adi:`AD9375`, highly integrated RF Transceivers™. The
:adi:`ADRV9375-N/PCBZ <ADRV9375>` has the same matching network as the
:adi:`ADRV9371-N/PRBZ <EVAL-ADRV9371>`. The :adi:`ADRV9375-W/PCBZ <ADRV9375>`
has the same matching network as the :adi:`ADRV9371-W/PRBZ <EVAL-ADRV9371>`.
While the complete chip level design package can be found on
:adi:`the ADI website <ad9371>`, information on the card and how to use it,
the design package that surrounds it, and the software which can make it work
can be found here.

.. image:: images/adrv9371-n_pcbz_side.jpg
   :width: 600

Recommendations
--------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, check the **Help and Support** section at
the bottom of the page.

To better understand the :adi:`AD9371` / :adi:`AD9375`, we recommend to use
the :adi:`EVAL-ADRV9371` / :adi:`EVAL-ADRV9375 <ADRV9375>` evaluation boards.

Table of Contents
--------------------------------------------------------------------------------

.. toctree::
   :hidden:

   prerequisites
   quickstart/index
   user-guide/index

#. Use the evaluation board to better understand the AD9371/AD9375

   #. :doc:`/solutions/reference-designs/adrv9371x/prerequisites`
   #. :ref:`Quick Start Guides <adrv9371x quickstart>`:

      #. :ref:`On ZCU102 <adrv9371x quickstart zcu102>`
      #. :ref:`On KCU105 <adrv9371x quickstart kcu105>`
      #. :ref:`On ZC706 <adrv9371x quickstart zc706>`
      #. :ref:`On Arria 10 SoC <adrv9371x quickstart a10soc>`
      #. :ref:`On Arria 10 GX <adrv9371x quickstart a10gx>`

   #. :ref:`adrv9371x user-guide`
   #. Linux Applications

      #. :ref:`iio-oscilloscope`

         #. :ref:`adrv9371x iio-oscilloscope`
         #. :ref:`adrv9371x plugin`
         #. :ref:`adrv9371x advanced-plugin`

      #. :doc:`FRU EEPROM Utility </software/fru_dump>`

   #. Push custom data into/out of the AD9371/AD9375

      #. :ref:`adrv9371x iq datafiles`
      #. :ref:`matlab transceiver-toolbox`
      #. :ref:`pyadi-iio`

#. Design with the AD9371/AD9375

   #. :ref:`Understanding the AD9371/AD9375 <adrv9371x block diagram>`

      #. :adi:`AD9371 Product page <AD9371>`
      #. :adi:`AD9375 Product page <AD9375>`
      #. :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
      #. :ref:`MATLAB Filter Wizard / Profile Generator for AD9371 <adrv9371x filters>`

   #. Hardware in the Loop / How to design your own custom Baseband

      #. :ref:`GNU Radio <software gnuradio>`
      #. :ref:`matlab transceiver-toolbox`

   #. Design a custom AD9371/AD9375 based platform

      #. Linux software

         #. About the device driver:

            #. :external+linux:doc:`AD9371/AD9375 Linux Device Driver <drivers/iio-transceiver/ad9371>`
            #. :external+linux:ref:`axi_jesd204_tx`
            #. :external+linux:ref:`JESD204B Receive Linux Driver <axi_jesd204_rx>`
            #. :external+linux:ref:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <axi_adxcvr>`
            #. :external+linux:ref:`AXI ADC HDL Linux Driver <axi-adc-hdl>`
            #. :external+linux:ref:`axi-dac-dds-hdl`

         #. About the device tree:

            #. :doc:`Customizing the devicetree on the target </linux/kernel/zynq_tips_tricks>`

         #. About the JEDS204 utilities:

            #. :external+linux:ref:`jesd204-fsm-framework`
            #. :ref:`JESD204B Status Utility <software jesd-status>`
            #. :ref:`JESD204 Eye Scan <software jesd-eye-scan>`
            #. :external+hdl:ref:`jesd204`

      #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile <resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
      #. :external+hdl:ref:`adrv9371x` which you must use in your FPGA.
      #. :doc:`Additional Documentation about SDR Signal Chains - The math behind the RF </solutions/reference-designs/fmcomms2/common/math>`

.. _adrv9371x block diagram:

Block Diagram
--------------------------------------------------------------------------------

.. image:: images/mykonos_block_diagram_v2.png
   :width: 800


Additional Information
--------------------------------------------------------------------------------

ADI Articles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Four Quick Steps to Production: Using Model-Based Design for Software-Defined
Radio

- :adi:`Part 1—the Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
- :adi:`Part 2—Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
- :adi:`Part 3—Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
- :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

About JESD standard:

- :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
- :adi:`JESD204C Primer: What's New and in It for You—Part 1 <resources/analog-dialogue/articles/jesd204c-primer-part1.html>`
- :adi:`JESD204C Primer: What's New and in It for You—Part 2 <resources/analog-dialogue/articles/jesd204c-primer-part2.html>`

Mathworks Webinars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :mw:`Modelling and Simulating Analog Devices' RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
- :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Videos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software Defined Radio using the Linux IIO Framework

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

Help and Support
--------------------------------------------------------------------------------

For additional questions or support, please visit the
:ez:`Engineering Zone <rf/wide-band-rf-transceivers/design-support-ad9371>`
forum.
