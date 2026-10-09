.. _arradio:

ARRADIO
=======

The `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`__
board is an `HSMC <http://www.altera.com/literature/ds/hsmc_spec.pdf>`_ board by
`Arrow <https://www.arrow.com/en/manufacturers/analog-devices>`_ & `Terasic <http://arradio.terasic.com/>`_
for the :adi:`AD9361`, a highly integrated RF Agile Transceiver™. While the
complete chip level design package can be found on the :adi:`the ADI web site <ad9361_design_files>`.
Information on the card, and how to use it, the design package that surrounds
it, and the software which can make it work, can be found on this page.

The ARRADIO board is not a product of Analog Devices, and questions about
purchase, or returns should go to Arrow. You can purchase the board from
`Arrow's web site <https://www.arrow.com/en/products/arradio/terasic-technologies>`_.

The purpose of the ARRADIO board is to provide an RF platform to which shows
maximum performance of the AD9361. It's expected that the RF performance of this
platform can meet the datasheet specifications without issues at 2.4 GHz, and
not much anywhere else. This is due to the external Johanson Technology's
`2450BL15B050E <https://www.johansontechnology.com/datasheets/baluns/JTI_Balun-2450BL15B050_12-03.pdf>`_
2.45 GHz balun that is on the board. This balun is rated for a operating
frequency of 2400~2500 MHz.

This platform is primarily for hardware / RF investigation and bring up of
various waveforms from a RF team before their custom hardware is complete, where
they want to see waveforms at their frequency of interest, and are not afraid of
changing out the balun if necessary. (Have a look in the
:dokuwiki:`Configuration <resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>`
sections).

The ARRADIO board is very similar to the :external+hdl:ref:`AD-FMCOMMS2-EBZ <fmcomms2>`
except it utilizes the HSMC connector which connects to the `Arrow SoCKit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_.

.. image:: images/rfc_top_01.jpg
   :align: center
   :width: 420

.. image:: images/rfc_bot_01.jpg
   :align: center
   :width: 420

.. toctree::
   :hidden:

   prerequisites
   quickstart/alterasockit

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Table of Contents
-----------------

- :dokuwiki:`Introduction <resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`
- :doc:`Prerequisites </solutions/reference-designs/arradio/prerequisites>`
- Hardware (Schematics) see `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`__

   - :external+hdl:ref:`Functional Overview & Specifications <fmcomms2>`
   - :dokuwiki:`Configuration options <resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>`
   - :dokuwiki:`Tuning the system <resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`

- Use the board to better understand the AD9361

   - :doc:`What you need to get started </solutions/reference-designs/arradio/prerequisites>`
   - :ref:`arradio quick-start`

      - :ref:`Linux on Altera SoCKit <arradio quick-start>`
      - :ref:`kuiper`
      - :ref:`kuiper`

   - Linux Applications

      - :ref:`iio-oscilloscope`
      - :dokuwiki:`AD9361 Control in the IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_plugin>`
      - :dokuwiki:`Advanced AD9361 Control IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      - :dokuwiki:`Command Line/Shell scripts <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   - Push custom data into/out of the AD9361

      - :doc:`Basic Data files and formats </solutions/reference-designs/fmcomms2/common/basic_iq_datafiles>`
      - :dokuwiki:`Create and analyze data files in MATLAB <resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`
      - :dokuwiki:`Stream data into/out of MATLAB <resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      - :dokuwiki:`AD9361 libiio streaming example <resources/tools-software/linux-software/libiio>`

-  Design with the AD9361

   - :dokuwiki:`Understanding the AD9361 <resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`

      - :adi:`AD9361 Product page <AD9361>`
      - :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      - :dokuwiki:`MATLAB Filter Design Wizard for AD9361 <resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`

   - Simulation

      - :dokuwiki:`MathWorks SimRF Models of the AD9361 <resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`

   - Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         - :dokuwiki:`Stream data into/out of MATLAB <resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         - :dokuwiki:`Beacon Frame Receiver Example <resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`
         - :doc:`QPSK Transmit and Receive Example </solutions/reference-designs/fmcomms2/software/qpsk_example>`
         - :doc:`LTE Transmit and Receive Example </solutions/reference-designs/fmcomms2/software/lte_example>`

      - :ref:`GNU Radio <software gnuradio>`
      - :dokuwiki:`FM Radio/Tuner <resources/tools-software/fm-radio>`
        (listen to FM signals on the HDMI monitor)
      - :dokuwiki:`C example <resources/tools-software/linux-software/libiio>`

   - Design a custom AD9361 based platform

      - :dokuwiki:`Linux software <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`

         - :external+linux:ref:`Linux AD9361 Device Driver <ad9361>`
         - :external+linux:ref:`Linux AD9361 Device Driver Customization <ad9361-customization>`
         - :ref:`Building Zynq Linux kernel and devicetree <linux-kernel zynq>`
         - :dokuwiki:`Build the demo on Altera SoCKit from source <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`
         - :doc:`Customizing the devicetree on the target </linux/kernel/zynq_tips_tricks>`

      - :dokuwiki:`No-OS Driver <resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`

         - :dokuwiki:`Build the HDL & No-OS from source <resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal/arradio_noos>`

      - :external+hdl:ref:`HDL Reference Desig <arradio>` which you must use in
        your FPGA.

         - :dokuwiki:`Digital Interface Timing Validation <resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`

- Additional Documentation about SDR Signal Chains

   - :doc:`The math behind the RF </solutions/reference-designs/fmcomms2/common/math>`

- :dokuwiki:`Help and Support <resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`