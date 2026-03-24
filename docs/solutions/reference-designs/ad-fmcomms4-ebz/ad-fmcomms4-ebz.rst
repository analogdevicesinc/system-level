AD-FMCOMMS4-EBZ User Guide
==========================

The AD-FMComms4-EBZ is an FMC board for the :adi:`AD9364`, a highly integrated RF Agile Transceiver™. While the complete chip level design package can be found on the :adi:`the ADI web site <ad9361_design_files>`. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found here.

The purpose of the AD-FMComms4-EBZ is to provide an RF platform to software developers, system architects, etc, who want a single platform which operates over a much wider tuning range (70 MHz – 6 GHz).

The AD-FMComms4-EBZ board is very similar to the `ad-fmcomms2-ebz <https://wiki.analog.com/ad-fmcomms2-ebz>`_ and `ad-fmcomms3-ebz <https://wiki.analog.com/ad-fmcomms3-ebz>`_ boards with only one exception, rather than the :adi:`AD9361` (which is 2 Rx, 2 Tx), it uses the :adi:`AD9364`, a lower cost 1 Rx, 1 Tx device. The AD-FMComms4-EBZ includes both types of external baluns, one targeted for wider tuning range applications (Minicircuits `TCM1-63AX+ <http://www.minicircuits.com/pdfs/TCM1-63AX+.pdf>`_), and ones which provide optimized performance for 2.4 GHz.

Since much of the FMCOMMS2/3/4 share a common device/infrastructure, much of the
documentation is the same.

-  :adi:`Purchase <ad-fmcomms4-ebz#eb-buy>`
-  `Introduction <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/introduction>`_
-  :doc:`FMCOMMS4 Hardware </solutions/reference-designs/ad-fmcomms4-ebz/hardware>`: This provides a brief description of the AD-FMCOMMS4-EBZ board by itself, and is a good reference for those who want to understand a little more about the board. If you just want to use the board, you can skip this section, and come back to it when you want to incorporate the AD9361 into your product.

   -  :doc:`Hardware </solutions/reference-designs/ad-fmcomms4-ebz/hardware>` (including :doc:`schematics </solutions/reference-designs/ad-fmcomms4-ebz/hardware>`)

      -  :doc:`Functional Overview & Specifications </solutions/reference-designs/ad-fmcomms4-ebz/hardware/functional_overview>`
      -  `Characteristics & Performance <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/card_specification>`_
      -  `Configuration options <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/configuration_options>`_
      -  `FCC or CE certification <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/certification>`_
      -  `Tuning the system <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/hardware/tuning>`_

   -   `Production Testing Process <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/testing>`_

-  Use the AD-FMCOMMS4-EBZ Board to better understand the AD9364

   -  `What you need to get started <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/prerequisites>`_
   -  `Quick Start Guides <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart>`_

      -  `Linux on ZC702, ZC706, ZED <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/zynq>`_
      -  `Linux on KC705, VC707 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/quickstart/microblaze>`_
      -  :external+kuiper:doc:`Configure a pre-existing SD-Card <index>`
      -  :external+kuiper:doc:`Update the old card you received with your hardware <index>`

   -  Linux Applications

      -  `IIO Scope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_
      -  `AD936X Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_plugin>`_
      -  `AD936X Advanced Control IIO Scope Plugin <https://wiki.analog.com/resources/tools-software/linux-software/fmcomms2_advanced_plugin>`_
      -  `Command Line/Shell scripts <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/applications/shell_scripts>`_

   -  Push custom data into/out of the AD-FMCOMMS2-EBZ

      -  `Basic Data files and formats <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/basic_iq_datafiles>`_
      -  `Create and analyze data files in MATLAB <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/datafiles>`_
      -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_
      -  `AD9361 libiio streaming example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_
      -  `Python Interfaces <https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio>`_

-  Design with the AD9364

   -  `Understanding the AD9364 <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/ad9361>`_

      -  :adi:`AD9364 Product page <AD9364>`
      -  :adi:`Full Datasheet and chip design package <en/rfif-components/rfif-transceivers/products/AD9361-Integrated-RF-Agile-Transceiver-Design-Res/fca.html>`
      -  `MATLAB Filter Design Wizard <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters>`_

   -  Simulation

      -  `MathWorks SimRF Models <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`_

   -  Hardware in the Loop / How to design your own custom BaseBand

      -  MATLAB/Simulink Examples

         -  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/transceiver-toolbox>`_
         -  `Beacon Frame Receiver Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`_
         -  `QPSK Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/qpsk_example>`_
         -  `LTE Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/lte_example>`_

      -  `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_
      -  `FM Radio/Tuner <https://wiki.analog.com/resources/tools-software/fm-radio>`_ (listen to FM signals on the HDMI monitor)
      -  `C example <https://wiki.analog.com/resources/tools-software/linux-software/libiio>`_

   -  Design a custom AD9361 based platform

      -  `Linux software <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux>`_

         -  `Linux Device Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`_
         -  `Build the demo on ZC702, ZC706, or ZED from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq>`_
         -  `Build the demo on KC705 or VC707 for Microblaze from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/microblaze>`_
         -  `Build the 2015_R2 Release Linux kernel from source <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_2015r2>`_
         -  `Customizing the devicetree on the target <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`_

      -  `No-OS Driver <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`_
      -  `HDL Reference Design <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`_ which you must use in your FPGA.

         -  `Digital Interface Timing Validation <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/interface_timing_validation>`_

-  Additional Documentation about SDR Signal Chains

   -  `The math behind the RF <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms1-ebz/math>`_
   -  :adi:`SDR For Engineers <en/education/education-library/software-defined-radio-for-engineers.html>`

-  `Help and Support <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`_

Warning
-------

.. esd-warning::
