EVALUATING THE AD9780/AD9781/AD9783 DIGITAL-TO-ANALOG CONVERTERS
================================================================

Preface
-------

This user guide describes both the hardware and software setup needed to acquire data capture from :adi:`AD9783-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9783.html#eb-relatedhardware>` evaluation board to characterize :adi:`AD9780`/:adi:`AD9781`/:adi:`AD9783` 12-/14-/16- bit 500MSPS high-speed digital-to-analog converter

This guide shows how AD9783-DPG2-EBZ works with ADS7-V2/SDP-H1 controller boards
developed by Analog Devices. Link to the old user guide document is provided for
customers who still have DPG2 and DPG3 controller boards.

Typical Setup
-------------

.. container:: centeralign

   \ |image1| *Figure 1a. EVAL-AD978x with SDP-H1*\

.. container:: centeralign

   |image2| *Figure 1b. EVAL-AD978x with ADS7-V2*\

.. tip::

   Tip: Click on any picture in this guide to open an enlarged version.

Helpful Files
-------------

-  `Quick Start Guide <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dpg2_evaluation_board_quick_start_guide.pdf>`_ for DPG2/DPG3 users
-  Data Sheet: :adi:`AD978x <static/imported-files/data_sheets/AD9780_9781_9783.pdf>`
-  IBIS Models: :adi:`AD9783 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9783.ibs>`, :adi:`AD9781 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9781.ibs>`, :adi:`AD9780 <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=ad9780.ibs>`
-  Schematics: `AD9783-DPG2-EBZ RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dpg2-ebz_revb_schematic.pdf>`_ `AD9783-DUAL-EBZ RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dual-ebz_revb_schematic.pdf>`_
-  Bill of Materials `AD9783-DPG2-EBZ RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dpg2-ebz_revb_bom.xls>`_ `AD9783-DUAL-EBZ RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dual-ebz_revb_bom.zip>`_
-  PCB Gerber files: `AD9783-DPG2-EBZ RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dpg2-ebz_revb_gerber_files.zip>`_
-  PCB BRD file: `AD9783-DPG2-EBZ RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dpg2-ebz_revb.zip>`_ `AD9783-DUAL-EBZ RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dual-ebz_revb.zip>`_
-  PCB Layout PDF: `AD9783-DPG2-EBZ RevB <https://wiki.analog.com/_media/resources/eval/dpg/ad9783-dpg2-ebz_revb_layout.pdf>`_

Software Needed:
----------------

-  `Analysis \| Control \| Evaluation (ACE) Software <https://wiki.analog.com/resources/tools-software/ace>`_
-  `DPG Lite <https://wiki.analog.com/resources/tools-software/ace/dpg-lite>`_ (Recommended; Installed with ACE) or `DPG Downloader <https://wiki.analog.com/resources/eval/dpg/dpgdownloader>`_

.. important::

   \ Known Issue: ACE may fail to detect HS-DAC boards, details `here <https://wiki.analog.com/resources/tools-software/ace/knownissues>`_.

Hardware Needed:
----------------

-  :adi:`AD9783-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9783.html#eb-relatedhardware>` Evaluation Board
-  `SDP-H1 <https://wiki.analog.com/resources/eval/dpg/hsdac-sdp-h1>`_ (EVAL-SDP-CH1Z) Board / `ADS7-V2 <https://wiki.analog.com/resources/eval/ads7-v2>`_ (ADS7-V2EBZ) Board
-  5Vdc 1A Power supply for the evaluation board
-  :adi:`AD-DAC-FMC`-ADP High-Speed DAC Evaluation Board to FMC Adapter Board
-  PC with ACE and DPG Lite Software Applications
-  High-Frequency Continuous Wave Generator (Clock Source)
-  Signal/Spectrum Analyzer
-  (2) SMA Cables
-  (2) Banana Plug Cables
-  The following are to be included if using SDP-H1 Evaluation Kit:

   -  12Vdc 1A Wall Adapter
   -  (2) USB-A to USB-Mini Cable

-  The following are to be included if using ADS7-V2 Evaluation Kit:

   -  12Vdc Power Supply
   -  Power Cord
   -  USB-A to USB-B Cable

Quick Start Guide
-----------------

-  Attach :adi:`AD9783-DPG2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD9783.html#eb-relatedhardware>` to controller board's (SDP-H1/ADS7-V2) FMC connector using the AD-DAC-FMC-ADP adapter board.
-  Connect the controller board (SDP-H1/ADS7-V2) to PC via USB and to a **12V power supply**.
-  Connect the evaluation board to PC via USB and to a **5Vdc 1A power supply** on **P5** and **P6**. Refer to Figures 1a and 1b.
-  Connect continuous wave generator for clock input to **SMA J1** and DAC output from **SMA J5 (IOUT1P)** or **SMA J9 (IOUT2P)** to a signal/spectrum analyzer.
-  Set clock input to **200MHz**, **3dBm**.
-  Open ACE. The board will be automatically recognized by the software. Click the plugin. Otherwise, install the :adi:`ACE plugin <plugins/ace/Board.AD9783.1.2019.43200.acezip>` for AD9783.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/ace_board_detect.png
   :align: center
   :width: 400

.. container:: centeralign

   *Figure 2. AD9783 Plugin*

-  On the ACE Board View, double click the AD9783 block to access the Chip View.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/ace_gui.jpg
   :align: center
   :width: 800

.. container:: centeralign

   *Figure 3. AD9783 Chip View*

-  The default values for the register is displayed and set. The values can be changed on the Chip View GUI, or on the **Memory Map** for registers not available in the GUI. For more info on the memory map, refer to :adi:`AD978x <static/imported-files/data_sheets/AD9780_9781_9783.pdf>` datasheet. Once the desired values are set, Click **Apply Changes** and then **Read All** on the upper right window.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/ace_apply.png
   :align: center
   :width: 400

.. container:: centeralign

   *Figure 4. Apply Changes and Read All button*

-  Start DPG Downloader Lite. The controller board (SDP-H1/ADS7-V2), the device
   part number and clock frequency should be displayed. Refer to Figures 5a and
   5b.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9783_dpg_window_sdp-h1.png
   :align: center
   :width: 600

.. container:: centeralign

   *Figure 5a. DPG Lite Session for EVAL-AD9783 with SDP-H1*

   |image3|

.. container:: centeralign

   *Figure 5b. DPG Lite Session for EVAL-AD9783 with ADS7-V2*

-  In DPG Downloader Lite, from the "Add Generator Waveforms" pulldown menu select **Single Tone** and apply the settings as shown in Figures 5a and 5b. Set the **Data Rate** to 200MHz and **Desired Frequency** to 16MHz. Set **DAC Resolution** to 16 for AD9783, 14 for AD9781, and 12 for AD9780. Uncheck the "Unsigned Data" box and Check the **Generate Complex Data (I & Q)**.
-  Select the I/Q tone from the **I/Q Data Vector** pulldown menu.
-  Press the download arrow and then the play button. The spectrum similar to
   Figure 6 should appear in the signal/spectrum analyzer.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/c_ad9783_16mhz.png
   :align: center
   :width: 600

.. container:: centeralign

   *Figure 6. Spectrum Output for AD9783; Fdac = 200MSPS, Fout = 16MHz*\

Using the ADL5375 Modulator
~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, solder jumpers JP4, JP5, JP6, and JP7 are configured to route the
DAC outputs to SMA J5 (IOUT1P) and to J9 (IOUT2P). This jumper setting is shown
on Figure 7a. To connect the DAC output to the filter that feeds into the
ADL5375, the solder jumpers should be reconfigured as shown in Figure 7b. Source
the desired LO of the modulator (i.e. 900 or 1800MHz, 3dBm) on SMA J2 (LO IN).
The ADL5375 Modulator output can be observed on SMA J6 (RF OUT).

|image4|

.. container:: centeralign

   *Figure 7a (left). DAC Output Configuration; Figure 7b (right) Modulator Output Configuration*\

Troubleshooting
---------------

This section lists items to check and practices to use when debugging any
unexpected performance of a board. If unexpected results occur:

-  Check the voltage rails of the evaluation board. P5 and P6 should be 5V; TP3, TP5, and TP7 should be 3.3V; TP9 and TP11 should be 1.8V.
-  Check if all (3) blue LEDs on the AD-DAC-FMC-ADP board is lit up. Reconnect the board to the FMC connector of the controller board (SDP-H1/ADS7-V2) if not lit up.
-  Check if controller board (SDP-H1/ADS7-V2) is being supplied properly by 12Vdc adapter. Some LEDs on the controller board should lit up.
-  Perform a chip reset by pressing S2 on the AD9783 evaluation board.
-  Power cycle both the controller board (SDP-H1/ADS7-V2) and the AD9783 evaluation board.
-  Probe C18 and C19 to make sure a clock signal is being sent into the DAC.
-  Check if XD1 is lit up on the evaluation board. Reconnect/replace the USB cable connection to the evaluation board if it's not lit up.
-  Disconnect and reconnect the controller board (SDP-H1/ADS7-V2) and AD9783
   evaluation board. Reopen ACE and DPG Lite software.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9783_with_sdp-h1.png
   :width: 600
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9783_with_ads7.png
   :width: 600
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/dpg/ad9783_dpg_window_ads7v2.png
   :width: 600
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/dpg/jumper_config.jpg
   :width: 800
