.. imported from: https://wiki.analog.com/resources/eval/dpg/eval-ad9783

.. _eval-ad9783 quickstart sdp-h1-ace:

EVALUATING THE AD9780/AD9781/AD9783 DIGITAL-TO-ANALOG CONVERTERS
================================================================

Preface
-------

This guide describes both the hardware and software setup needed to download
data to the :adi:`AD9783-DPG2-EBZ <EVAL-AD9783>` evaluation board to
characterize the :adi:`AD9780`/:adi:`AD9781`/:adi:`AD9783` 12-/14-/16-bit 500
MSPS high-speed digital-to-analog converters.

This guide shows how the AD9783-DPG2-EBZ works with the ADS7-V2/SDP-H1
controller boards developed by Analog Devices. The user guide document for
customers who still have DPG2 and DPG3 controller boards is listed in the
:ref:`eval-ad9783 user-guide` page.

Typical setup
-------------

.. grid::
   :widths: 50% 50%

   .. _eval-ad9783 fig-setup-sdp-h1:

   .. figure:: ../images/ad9783-with-sdp-h1.png

      EVAL-AD978x with SDP-H1

   .. _eval-ad9783 fig-setup-ads7-v2:

   .. figure:: ../images/ad9783-with-ads7-v2.png

      EVAL-AD978x with ADS7-V2

.. tip::

   Click on any picture in this guide to open an enlarged version.

Software needed
---------------

-  :adi:`Analysis | Control | Evaluation (ACE) Software <ace>`
-  :dokuwiki:`DPG Lite <resources/tools-software/ace/dpg-lite>` (recommended;
   installed with ACE) or
   :dokuwiki:`DPG Downloader <resources/eval/dpg/dpgdownloader>`

.. important::

   Known issue: ACE may fail to detect HS-DAC boards, details
   :dokuwiki:`here <resources/tools-software/ace/knownissues>`.

Hardware needed
---------------

-  :adi:`AD9783-DPG2-EBZ <EVAL-AD9783>` evaluation board
-  :dokuwiki:`SDP-H1 <resources/eval/dpg/hsdac-sdp-h1>` (EVAL-SDP-CH1Z) board /
   :ref:`ADS7-V2 <ads7-v2>` (ADS7-V2EBZ) board
-  5 Vdc 1 A power supply for the evaluation board
-  :adi:`AD-DAC-FMC`-ADP high-speed DAC evaluation board to FMC adapter board
-  PC with ACE and DPG Lite software applications
-  High-frequency continuous wave generator (clock source)
-  Signal/spectrum analyzer
-  (2) SMA cables
-  (2) Banana plug cables
-  The following are to be included if using the SDP-H1 evaluation kit:

   -  12 Vdc 1 A wall adapter
   -  (2) USB-A to USB-Mini cable

-  The following are to be included if using the ADS7-V2 evaluation kit:

   -  12 Vdc power supply
   -  Power cord
   -  USB-A to USB-B cable

Quick start guide
-----------------

-  Attach the :adi:`AD9783-DPG2-EBZ <EVAL-AD9783>` to the controller board's
   (SDP-H1/ADS7-V2) FMC connector using the AD-DAC-FMC-ADP adapter board.
-  Connect the controller board (SDP-H1/ADS7-V2) to the PC via USB and to a
   **12 V power supply**.
-  Connect the evaluation board to the PC via USB and to a
   **5 Vdc 1 A power supply** on **P5** and **P6**. Refer to
   :numref:`eval-ad9783 fig-setup-sdp-h1` and
   :numref:`eval-ad9783 fig-setup-ads7-v2`.
-  Connect a continuous wave generator for the clock input to **SMA J1** and the
   DAC output from **SMA J5 (IOUT1P)** or **SMA J9 (IOUT2P)** to a
   signal/spectrum analyzer.
-  Set the clock input to **200 MHz**, **3 dBm**.
-  Open ACE. The board is automatically recognized by the software. Click the
   plugin. Otherwise, install the
   :adi:`ACE plugin <plugins/ace/Board.AD9783.1.2019.43200.acezip>` for the
   AD9783.

   .. _eval-ad9783 fig-ace-plugin:

   .. figure:: ../images/ad9783-ace-plugin.png
      :align: center
      :width: 400

      AD9783 plugin

-  On the ACE Board View, double click the AD9783 block to access the Chip View.

   .. _eval-ad9783 fig-ace-chip-view:

   .. figure:: ../images/ad9783-ace-chip-view.jpg
      :align: center
      :width: 800

      AD9783 Chip View

-  The default values for the registers are displayed and set. The values can be
   changed on the Chip View GUI, or on the **Memory Map** for registers not
   available in the GUI. For more info on the memory map, refer to the
   :adi:`AD978x <media/en/technical-documentation/data-sheets/AD9780_9781_9783.pdf>`
   datasheet. Once the desired values are set, click **Apply Changes** and then
   **Read All** on the upper right window.

   .. _eval-ad9783 fig-ace-apply:

   .. figure:: ../images/ad9783-ace-apply-changes.png
      :align: center
      :width: 400

      Apply Changes and Read All buttons

-  Start DPG Downloader Lite. The controller board (SDP-H1/ADS7-V2), the device
   part number and the clock frequency should be displayed. Refer to
   :numref:`eval-ad9783 fig-dpg-sdp-h1` and
   :numref:`eval-ad9783 fig-dpg-ads7-v2`.

   .. _eval-ad9783 fig-dpg-sdp-h1:

   .. figure:: ../images/ad9783-dpg-lite-sdp-h1.png
      :align: center
      :width: 600

      DPG Lite session for the EVAL-AD9783 with SDP-H1

   .. _eval-ad9783 fig-dpg-ads7-v2:

   .. figure:: ../images/ad9783-dpg-lite-ads7-v2.png
      :align: center
      :width: 600

      DPG Lite session for the EVAL-AD9783 with ADS7-V2

-  In DPG Downloader Lite, from the "Add Generator Waveforms" pulldown menu
   select **Single Tone** and apply the settings as shown in
   :numref:`eval-ad9783 fig-dpg-sdp-h1` and
   :numref:`eval-ad9783 fig-dpg-ads7-v2`. Set the **Data Rate** to 200 MHz and
   **Desired Frequency** to 16 MHz. Set **DAC Resolution** to 16 for the AD9783,
   14 for the AD9781, and 12 for the AD9780. Uncheck the "Unsigned Data" box and
   check **Generate Complex Data (I & Q)**.
-  Select the I/Q tone from the **I/Q Data Vector** pulldown menu.
-  Press the download arrow and then the play button. A spectrum similar to
   :numref:`eval-ad9783 fig-spectrum` should appear in the signal/spectrum
   analyzer.

   .. _eval-ad9783 fig-spectrum:

   .. figure:: ../images/ad9783-spectrum-16mhz.png
      :align: center
      :width: 600

      Spectrum output for the AD9783; Fdac = 200 MSPS, Fout = 16 MHz

For the jumper settings used to connect the DAC output to the ADL5375 modulator,
the board design files and the troubleshooting checklist, refer to the
:ref:`eval-ad9783 user-guide`.
