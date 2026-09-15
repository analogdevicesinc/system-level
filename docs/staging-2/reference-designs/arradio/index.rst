.. imported from: https://wiki.analog.com/resources/eval/user-guides/arradio

.. _arradio:

ARRADIO
=======

The `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`__
board is an `HSMC <http://www.altera.com/literature/ds/hsmc_spec.pdf>`__ board
by `Arrow <https://www.arrow.com/en/manufacturers/analog-devices>`__ &
`Terasic <http://arradio.terasic.com/>`__ for the :adi:`AD9361`, a highly
integrated RF Agile Transceiver™. While the complete chip level design package
can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information
on the card, and how to use it, the design package that surrounds it, and the
software which can make it work, can be found on this page.

The ARRADIO board is not a product of Analog Devices, and questions about
purchase, or returns should go to Arrow. You can purchase the board from
`Arrow's web site <https://www.arrow.com/en/products/arradio/terasic-technologies>`__.

The purpose of the ARRADIO board is to provide an RF platform to which shows
maximum performance of the AD9361. It"s expected that the RF performance of this
platform can meet the datasheet specifications without issues at 2.4 GHz, and
not much anywhere else. This is due to the external Johanson Technology"s
`2450BL15B050E <https://www.johansontechnology.com/datasheets/baluns/JTI_Balun-2450BL15B050_12-03.pdf>`__
2.45 GHz Balun that is on the board. This balun is rated for a operating
frequency of 2400~2500 MHz.

This platform is primarily for hardware / RF investigation and bring up of
various waveforms from a RF team before their custom hardware is complete, where
they want to see waveforms at their frequency of interest, and are not afraid of
changing out the balun if necessary. (Have a look in the
:dokuwiki:`Configuration <ad-fmcomms2-ebz/hardware/configuration_options>`
sections).

The ARRADIO board is very similar to the
:dokuwiki:`AD-FMComms2-EBZ </resources/eval/user-guides/AD-FMComms2-EBZ>`,
except it utilizes the HSMC connector which connects to the
`Arrow SoCKit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`__.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/rfc_top_01.jpg
   :width: 420px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcadc2-ebz/rfc_bot_01.jpg
   :width: 420px

Table of Contents
-----------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to
:dokuwiki:`ask <ad-fmcomms2-ebz/help_and_support>`.

#. :dokuwiki:`Introduction <ad-fmcomms2-ebz/introduction>`
#. Hardware (Schematics) see
   `ARRADIO <https://www.arrow.com/en/products/arradio/terasic-technologies>`__

   #. :dokuwiki:`Functional Overview & Specifications <ad-fmcomms2-ebz/hardware/functional_overview>`
   #. :dokuwiki:`Configuration options <ad-fmcomms2-ebz/hardware/configuration_options>`
   #. :dokuwiki:`Tuning the system <ad-fmcomms2-ebz/hardware/tuning>`

#. Use the board to better understand the AD9361

   #. :dokuwiki:`What you need to get started <ad-fmcomms2-ebz/prerequisites>`
   #. :dokuwiki:`Quick Start Guides <ad-fmcomms2-ebz/quickstart>`

      #. :dokuwiki:`Linux on Altera SoCKit <arradio/quickstart/alterasockit>`
      #. :dokuwiki:`Configure a pre-existing SD-Card </resources/tools-software/linux-software/zynq_images#preparing_the_image>`
      #. :dokuwiki:`Update the old card you received with your hardware </resources/tools-software/linux-software/zynq_images#staying_up_to_date>`

   #. Linux Applications

      #. :dokuwiki:`IIO Scope <resources/tools-software/linux-software/iio_oscilloscope>`
      #. :dokuwiki:`AD9361 Control in the IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_plugin>`
      #. :dokuwiki:`Advanced AD9361 Control IIO Scope Plugin <resources/tools-software/linux-software/fmcomms2_advanced_plugin>`
      #. :dokuwiki:`Command Line/Shell scripts <ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`

   #. Push custom data into/out of the AD9361

      #. :dokuwiki:`Basic Data files and formats <ad-fmcomms2-ebz/software/basic_iq_datafiles>`
      #. :dokuwiki:`Create and analyze data files in MATLAB <ad-fmcomms2-ebz/software/datafiles>`
      #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
      #. :dokuwiki:`AD9361 libiio streaming example </resources/tools-software/linux-software/libiio#libiio_-_ad9361_iio_streaming_example>`

#. Design with the AD9361

   #. :dokuwiki:`Understanding the AD9361 <ad-fmcomms2-ebz/ad9361>`

      #. :adi:`AD9361 Product page <AD9361>`
      #. :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      #. :dokuwiki:`MATLAB Filter Design Wizard for AD9361 <ad-fmcomms2-ebz/software/filters>`

   #. Simulation

      #. :dokuwiki:`MathWorks SimRF Models of the AD9361 <ad-fmcomms2-ebz/software/simrf>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. MATLAB/Simulink Examples

         #. :dokuwiki:`Stream data into/out of MATLAB </resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`
         #. :dokuwiki:`Beacon Frame Receiver Example </resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink#beacon_frame_receiver_example>`
         #. :dokuwiki:`QPSK Transmit and Receive Example </resources/tools-software/linux-software/libiio/clients/qpsk_example>`
         #. :dokuwiki:`LTE Transmit and Receive Example </resources/tools-software/linux-software/libiio/clients/lte_example>`

      #. :dokuwiki:`GNU Radio </resources/tools-software/linux-software/gnuradio>`
      #. :dokuwiki:`FM Radio/Tuner </resources/tools-software/fm-radio>` (listen
         to FM signals on the HDMI monitor)
      #. :dokuwiki:`C example </resources/tools-software/linux-software/libiio#libiio_-_ad9361_iio_streaming_example>`

   #. Design a custom AD9361 based platform

      #. :dokuwiki:`Linux software <ad-fmcomms2-ebz/software/linux>`

         #. :dokuwiki:`Linux Device Driver </resources/tools-software/linux-drivers/iio-transceiver/ad9361>`
         #. :dokuwiki:`Build the demo on Altera SoCKit from source <ad-fmcomms2-ebz/software/linux/zynq>`
         #. :dokuwiki:`Build the 2014_R2 Release Linux kernel from source <ad-fmcomms2-ebz/software/linux/zynq_2014r2>`
         #. :dokuwiki:`Customizing the devicetree on the target <ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

      #. :dokuwiki:`No-OS Driver <ad-fmcomms2-ebz/software/baremetal>`

         #. :dokuwiki:`Build the HDL & No-OS from source <ad-fmcomms2-ebz/software/baremetal/arradio_noos>`

      #. :dokuwiki:`HDL Reference Design <ad-fmcomms2-ebz/reference_hdl>` which
         you must use in your FPGA.

         #. :dokuwiki:`Digital Interface Timing Validation <ad-fmcomms2-ebz/interface_timing_validation>`

#. Additional Documentation about SDR Signal Chains

   #. :dokuwiki:`The math behind the RF <ad-fmcomms1-ebz/math>`

#. :dokuwiki:`Help and Support <ad-fmcomms2-ebz/help_and_support>`

Videos
------

.. video:: https://www.youtube.com/watch?v=rdwdi8eIxRQ
