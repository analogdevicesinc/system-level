.. _ad9152-fmc-ebz:

EVALUATING THE AD9152 DIGITAL-TO-ANALOG CONVERTER
=================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9152-FMC-EBZ <EVAL-AD9152>` evaluation board (EVB) to characterize the :adi:`AD9152` 16-bit 2.25GSPS Dual JESD204B signal processing RF Digital-to-Analog Converter.

The AD9152-FMC-EBZ has an FMC mezzanine card and connects to an :adi:`ADS7-V2 <eval-ads7-v2>` or :adi:`ADS8-V1 <eval-ads8-v1ebz>` data pattern generator system. The ADS7-V2/ADS8-V1 automatically formats the data and sends it to the EVB via its JESD204B lanes. +12V, +3.3V, and VADJ power supply rails are provided by the ADS7-V2/ADS8-V1 system via the FMC connector P1. A clock distribution chip (AD9516-1) is included on this EVB as a clock fan-out and frequency divider for the DACCLK, JESD204B SYSREF signals, and a GBTCLK clock used by the ADS7-V2/ADS8-V1.

There is also an FMC standard I2C bus that is used by the ADS7-V2/ADS8-V1 to
identify the board. This I2C interface is implemented in software in the
AD9152-FMC-EBZ PIC processor (XU1). All ADS7-V2/ADS8-V1 to/from the EVB
interface signals are connected via the FMC connector P1.

Typical Setup
-------------

.. figure:: ../images/ad9152-fmc-ebz_setup_with_labels.jpg
   :align: center
   :width: 600

   AD9152-FMC-EBZ Setup with ADS7-V2EBZ

.. figure:: ../images/ad9152-fmc-ebz_setup2_with_labels.jpg
   :align: center
   :width: 600

   AD9152-FMC-EBZ Setup with ADS8-V1EBZ

.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.

Helpful Files/Links
-------------------

-  User Guides for non-FMC card users:

   -  :doc:`AD9152-EBZ <ad9152-ebz>`
   -  :doc:`AD9152-ADRF6720-EBZ <ad9152-adrf6720-ebz>`

-  :dokuwiki:`ADS7-V1/-V2 for High-Speed DAC Evaluation <resources/eval/dpg/ads7>`
-  Datasheet: :adi:`AD9152 <media/en/technical-documentation/data-sheets/AD9152.pdf>`
-  IBIS Model: :adi:`AD9152 <media/en/package-pcb-model-library/ibis-models/ad9152bcpz>`
-  AMI Model: `AD9144/AD9152/AD9154/AD9135/AD9136 <https://form.analog.com/Form_Pages/securedownloads/designFilePackage.aspx?prodID=AD9144-9152-9154-9135-9136>`_
-  Schematic: :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva_schematic.pdf>`
-  Bill of Materials: :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva_bom.xlsx>`
-  PCB Gerber Files: :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva_gerber_files.zip>`
-  PCB BRD File: :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva.zip>`
-  PCB Layout PDF: :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva_layout.pdf>`

Software Needed
---------------

-  :dokuwiki:`Analysis | Control | Evaluation (ACE) Software <resources/tools-software/ace>`
-  :dokuwiki:`DPG Lite <resources/tools-software/ace/dpg-lite>` (Recommended; Installed with ACE) or :dokuwiki:`DPG Downloader <resources/eval/dpg/dpgdownloader>`
-  :adi:`AD9152 ACE Plugin <plugins/ace/board.ad9152.1.2020.4400.acezip>`

.. important::


   -  Do not install ACE on a computer with DAC Software Suite.
   -  Known Issue: ACE may fail to detect HS-DAC boards, details :dokuwiki:`here <resources/tools-software/ace/knownissues>`.


Hardware Needed
---------------

-  :adi:`AD9152-FMC-EBZ <EVAL-AD9152>` Evaluation Board which comes with:

   -  USB-A to USB-Mini Cable

-  :doc:`ADS7-V2EBZ </solutions/reference-designs/eval-ad9694/quickstart/ads7-v2>` or :dokuwiki:`ADS8-V1EBZ <resources/eval/ads8-v1>` Evaluation Kit which includes:

   -  12V 60W AC/DC Power Supply
   -  Power Cord
   -  USB-A to USB-B Cable

-  PC with ACE and DPG Lite Software Applications
-  Low Phase Noise High-Frequency Continuous Wave Generator
-  Signal/Spectrum Analyzer
-  (2) SMA Cables

Quick Start Guide
-----------------

-  Attach AD9152-FMC-EBZ onto the FMC connector of ADS7-V2 or ADS8-V1 controller board. Connect the evaluation board to PC via USB, the continuous waveform generator output to J1, and one of the DAC outputs (J4 or J17) to a signal/spectrum analyzer. Connect ADS7-V2/ADS8-V1 to PC via USB and to a 12V 60W AC/DC power supply, then switch the board ON using S1 beside the connector for 12V supply. Refer to :doc:`Typical Setup <ad9152-fmc-ebz>` section for pictures of actual evaluation setup.
-  Set the frequency of the continuous waveform generator output to **1.5 GHz** and the output level to **+3 dBm**. Enable the output.

.. figure:: ../images/ad9152-fmc-ebz_dpg_board_detect_ads7.png
   :align: center
   :width: 600

   ADS7-V2 and AD9152 detected in DPG Software

-  Start DPG Lite or DPG Downloader. A panel named after the detected controller board should appear at the bottom of the DPG window. The device on the evaluation board and the data interface should also be automatically detected by the software and shown at **Evaluation Board** and **Port Configuration**, respectively. See Figure 2.

.. figure:: ../images/ad9152-fmc-ebz_ace_board_detect_ads7.png
   :align: center
   :width: 600

   AD9152-FMC-EBZ detected in ACE

-  Open ACE. The board will automatically be recognized by the software as shown in Figure 3. Otherwise, install the plugin for AD9152 evaluation board by following the steps in this page: :dokuwiki:`Quickstart - ACE Quickstart and Plug-in Installation <resources/tools-software/ace/userguide/quickstart>`.

.. figure:: ../images/ad9152-fmc-ebz_ace_configuration_wizard_ads7.png
   :align: center
   :width: 600

   ACE Initial Configuration Wizard

.. figure:: ../images/ad9152-fmc-ebz_ace_chipview_ads7.png
   :align: center
   :width: 600

   ACE AD9152 Chip View Tab

-  In ACE, apply the configuration wizard settings enumerated below and shown in
   JESD204B PLL should lock and the indicator should turn green.

   -  **FDAC:** 1.5 GHz
   -  **Interpolation:** 2
   -  **JESD Mode:** 4
   -  **Subclass1:** True
   -  **DigGain:** True
   -  **PLL_Enable:** False
   -  **Input Data Format:** 2's complement

.. figure:: ../images/ad9152-fmc-ebz_dpg_generate_output.png
   :align: center
   :width: 600

   Single Tone and ADS7-V2 Configuration Panels in DPG

-  In DPG Lite or DPG Downloader, configure single tone waveform generation. From the **Add Generator Waveforms** pulldown menu, select **Single Tone**. Apply the following settings:

   -  **Data Rate:** 750 MHz
   -  **Desired Frequency:** 100 MHz
   -  **DAC Resolution:** 16 bits
   -  **Amplitude:** -10 dB
   -  **Unsigned Data:** unchecked
   -  **Generate Complex Data (I & Q):** checked

-  In the ADS7-V2 or ADS8-V1 panel in the DPG window, configure **Data Playback** by selecting tones for the DAC outputs from each dropdown menu. Set **JESD Mode** to Mode 4, **Links** to Single and **Subclass** to 1.

.. figure:: ../images/ad9152-fmc_dac_output.png
   :align: center

   AD9152 DAC Output FFT for Data Rate = 700 MHz, FOUT = 100 MHz

-  Press the download arrow (|9154_down_arrow.png|) then the play button (|9154_right_green_arrow.png|). As in Figure 6, **Serial Line Rate** should appear as 7.5 Gbps and **Sync Status** should have a check mark. The FFT plot of the DAC output is in Figure 7.

.. |9154_down_arrow.png| image:: ../images/9154_down_arrow.png
.. |9154_right_green_arrow.png| image:: ../images/9154_right_green_arrow.png
