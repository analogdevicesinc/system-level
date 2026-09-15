.. imported from: https://wiki.analog.com/resources/eval/user-guide/ev-iso-4224-fmcz

.. _ev-iso-4224-fmcz:

EV-ISO-4224-FMCZ Reference Design Board User Guide
==================================================

General Setup
-------------

The following sections describe the steps for setting up the
:adi:`EV-ISO-4224-FMCZ` Reference Design Board using ZedBoard™.

Reference Design Kit Contents
-----------------------------

- EV-ISO-4224-FMCZ : :adi:`ADAQ4224` Reference Design Board with Digital Signal
  and Power Isolation
- Micro-SD card with adapter containing system board software and Linux OS

Equipment
---------

-
  `Zedboard™ <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__
  Rev 1.0 or later board
- DC/AC signal source (Audio Precision or similar high performance signal
  source)
- SMA cables
- XLR-SMA interposer board
- SD Card (included in the reference design board kit)
- Micro-USB to USB type A cable (optional)
- PC running Windows 7, 8, or 10 with Ethernet port

Software
--------

-  :adi:`Analysis/Control/Evaluation (ACE) Software Installer <en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`
- :adi:`ADAQ4224` ACE Plug-in (see
  :dokuwiki:`quickstart </resources/tools-software/ace/userguide/quickstart>`
  for the plug-in installation guide.)

General Description
-------------------

The :adi:`EV-ISO-4224-FMCZ` is an isolated digital and power reference design
for the :adi:`ADAQ4224`, a 24-bit, 2MSPS μModule Data Acquisition Solution. On
the :adi:`EV-ISO-4224-FMCZ`, the electrically isolated temperature sensor of the
:adi:`ADAQ4224` is connected to the controller side and has a separate ground
potential versus the data acquisition signal path ground. The
:adi:`EV-ISO-4224-FMCZ` has the power management blocks to generate all the
necessary supply rails and reference voltage for the operation of the
:adi:`ADAQ4224` μModule.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/ev-iso-4224-fmcz_and_zedboard_connection.png
   :width: 600px

   Figure 1. EV-ISO-4224-FMCZ Connection with Zedboard

Getting Started
---------------

The following section contains the software installation instructions together
with the hardware configurations necessary to use the :adi:`EV-ISO-4224-FMCZ`.

Software Installation Procedures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the
:adi:`Analysis/Control/Evaluation (ACE) Software <en/resources/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`
installer from the Analog Devices website.

.. warning::

   To ensure that the evaluation system is correctly recognized when it is
   connected to the PC, install the ACE and the :adi:`ADAQ4224` ACE Plug-in
   first before connecting the :adi:`EV-ISO-4224-FMCZ` and ZedBoard™ to the PC.

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The :adi:`EV-ISO-4224-FMCZ` connects to the ZedBoard™. The ZedBoard™ serves as
the communication link between the PC and :adi:`EV-ISO-4224-FMCZ`. Figure 2
shows the connections between the :adi:`EV-ISO-4224-FMCZ`, the ZedBoard™ and the
signal source.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/ev-iso-4224-fmcz_setup.png
   :width: 800px

   Figure 2. Hardware Evaluation Setup

#. Configure the P1 & P2 links on the :adi:`EV-ISO-4224-FMCZ`. Short pin 1 and
   pin 2 for both P1 and P2 jumper links.
#. Configure the VADJ and Boot links on the ZedBoard™ as shown on Figure 3.
#. Connect the :adi:`EV-ISO-4224-FMCZ` securely to the 160-way connector on the
   ZedBoard™. The :adi:`EV-ISO-4224-FMCZ` does not require an external power
   supply adapter.
#. Connect the ZedBoard™ USB_OTG port to the PC, this micro USB to USBA cable is
   included on the ZedBoard™ kit. Power it up with the 12 V wall adapter
   included in the kit.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/zedboard_links.png
   :width: 600px

  Figure 3. Zedboard Link Configuration

Software GUI Setup
------------------

Launching the Software
~~~~~~~~~~~~~~~~~~~~~~

After installing **ACE** (see the Software Installation Procedures section), run
the software with either of the following methods:

- Navigate to the destination folder of the // ACE // installer selected during
  the installation procedure and run the ACE.exe file.
- Search for // ACE // in the Start Menu and run the software.
- Click on the ACE.exe Desktop Shortcut

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/ace_launch.png
   :width: 600px

   Figure 4. Launching ACE.exe from Start Menu

ACE Main Window
~~~~~~~~~~~~~~~

- The EVAL-ADAQ4224-FMCZ icon should be detected in the main window once the
  Zedboard powers-up and LD0 is blinking. Click Refresh Attached Hardware if the
  icon is not seen.
- Click on the EVAL-ADAQ4224-FMCZ icon to open up the Board View.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/ace_main_window.png
   :width: 600px

   Figure 5. ACE Main Window

Board View
~~~~~~~~~~

- The :adi:`ADAQ4224` Communication Mode is selected in the CONFIGURATION Panel
  in the Board View window. The default mode is Single-Lane/24-bit output data
  coding/SPI mode/Single Data Rate
- Click on the either the ADAQ4224 or TEMP SENSE icon to open the Chip view for
  the ADAQ4224 ADC or the ADAQ4224 Temperature Sensor
- Table 1 shows the maximum sampling frequency that can be set for each
  communication mode. *Note that this is a limitation on the Zedboard, not the*
  :adi:`ADAQ4224`\ *.*

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/board_view.png
   :width: 600px

   Figure 6. Board View Window

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/max_sampling_frequency.jpg
   :width: 600px

Table 1. Max Sampling Frequency

ADAQ4224 Chip View Window
~~~~~~~~~~~~~~~~~~~~~~~~~

- The attributes of the :adi:`ADAQ4224` ADC are set on this Chip View Window.
- These attributes include: sampling frequency, calibbias(offset register),
  calibscale(gain register), and scale (Gain of the analog frontend).
- Click on Proceed to Analysis to open Analysis Window.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/adaq4224_chip_view.png
   :width: 600px

   Figure 7. ADAQ4224 Chip View Window

ADAQ4224 Temperature Sensor Chip View Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The attributes of the :adi:`ADAQ4224` Temp Sensor is set on this Chip View
  Window.
- These attributes include: update interval, alarm threshold, hysteresis
  threshold and resolution.
- Click on Proceed to Analysis to open Analysis Window.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/adaq4224_temp_chip_view.png
   :width: 600px

   Figure 8. :adi:`ADAQ4224` Temp Sensor Chip View Window

ADAQ4224 Analysis Window
~~~~~~~~~~~~~~~~~~~~~~~~

- The no. of samples per capture can be set in this window.
- A Coherency calculator can also be used to calculate for a coherent input
  frequency with respect to the set sampling frequency and no. of samples.
- There are different tabs that can be selected to perform a waveform capture,
  an FFT capture and a histogram capture.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/adaq4224_analysis_window.png
   :width: 600px

   Figure 9. :adi:`ADAQ4224` Analysis Window

ADAQ4224 Temp Sensor Analysis Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Click on the Start Button to display the temperature conversions. The plot
  will display the MIN/MAX Alarm thresholds and the actual temperature measured.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/adaq4224_temp_analysis_view_window.png
   :width: 600px

   Figure 10. :adi:`ADAQ4224` Temp Sensor Analysis Window

EV-ISO-4224-FMCZ AC Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- SNR

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/snr_iso_vs_gain.svg
   :width: 700px

   Figure 11. SNR vs. GAIN

- THD

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz/thd_iso_vs_gain.svg
   :width: 700px

   Figure 12. THD vs. GAIN

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :download:`https://wiki.analog.com/_media/resources/eval/user-guide/ev-iso-4224-fmcz_design_support_package.zip`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Gerber and Assembly Files

Additional Information and Useful Links
---------------------------------------

- :adi:`EV-ISO-4224-FMCZ Reference Design Board Page <EV-ISO-4224-FMCZ>`
- :adi:`EV-ISO-4224-FMCZ Design Support Package <EV-ISO-4224-FMCZ-DesignSupport>`
- :adi:`ADAQ4224 Product Page <ADAQ4224>`
- :adi:`LTC6655 Product Page <LTC6655>`
- :adi:`ADR4540 Product Page <ADR4540>`
- :adi:`ADA4807-1 Product Page <ADA4807-1>`
- :adi:`MAX22164 Product Page <MAX22164>`
- :adi:`MAX22165 Product Page <MAX22165>`
- :adi:`ADUM320N Product Page <ADUM320N>`
- :adi:`LT3999 Product Page <LT3999>`
- :adi:`LT3487 Product Page <LT3487>`
- :adi:`ADP7142 Product Page <ADP7142>`
- :adi:`ADP7182 Product Page <ADP7182>`
- :adi:`ADP7118 Product Page <ADP7118>`
- :adi:`LTC1983 Product Page <LTC1983>`
- :adi:`ADP7183 Product Page <ADP7183>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you register your hardware. Register at
   https://form.analog.com/Form_Pages/RFComms/EV-ISO-4224-FMCZ.aspx to receive
   all these great benefits and more!

*End of Document*
