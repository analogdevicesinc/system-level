.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad4130-8/softwareprocedures

.. _ad4130-8 softwareprocedures:

EVAL-AD4130-8WARDZ Software Guide
=================================

Ace Plugin
==========

Ace Plugin Install guide
------------------------

- Warning : The evaluation software and drivers must be installed before
  connecting both the evaluation board and the Controller (SDP) board to the PC.
  This ensures that the evaluations system is correctly recognized when it is
  connected to the PC.

The software and drivers required for the installation walked through in this
section can be found below:

- :adi:`Ace Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf>`
- :adi:`AD4130-8 ACE Plugin <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4130-8.html#eb-relatedsoftware>`
- `SDP controller system demonstration platform drivers <http://swdownloads.analog.com/ACE/SDP/SDPDrivers.exe>`__

Installing the ACE Plugin software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the ACE software from the ACE software page or the
:adi:`AD4130-8 <en/products/ad4130-8.html>` product page. Install ACE on a PC
**before using** the
:adi:`EVAL-AD4130-8WARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD4130-8.html#eb-overview>`.

Installing ACE
~~~~~~~~~~~~~~

#. Download the ACE software to a Windows®-based PC.
#. Double click the ACEInstall.exe file to begin the installation. By default,
   the software is saved to the following location: C:\\Program Files
   (x86)\\Analog Devices\\ACE.
#. A dialog box opens asking for permission to allow the program to make changes
   to the PC. Click Yes to begin the installation process.

#. In the ACE Setup window, click Next > to continue the installation.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_1.png
      :width: 400px

#. Read the software license agreement and click I Agree

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_2.png
      :width: 400px

#. Click Browse … to choose the installation location and then click Next >

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_3.png
      :width: 400px

#. The ACE software components to install are preselected. Click Install.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_4.png
      :width: 400px

#. The Windows Security window opens . Click Install

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_5.png
      :width: 400px

#. The installation in progress in the window below. No action is required.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_6.png
      :width: 400px

#. When the installation is complete, click Next >, and then click Finish to
   complete the installation process

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_7.png
      :width: 400px

AD4130-8 Plugin Install
~~~~~~~~~~~~~~~~~~~~~~~

After the AD4130-8 Plugin is downloaded follow the steps to install the file:

#. Double click on the AD4130-8 Plugin.
#. Connect up your EVAL-AD4130-8WARDZ to your pc through a controller board.

Alternatively, the AD4130-8 Plugin can be installed through the steps bellow:

#. From the Start menu of the PC, select All Programs > Analog Devices > ACE>
   ACE.exe to open the ACE software main window shown below.
#. Click on the Plug-in Manager Tab in the top left panel in Ace.

#. Click on the Settings… button.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_install_page_1.png
      :width: 400px

#. Hit the + button next to the Zipped Plug-in Sources.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_install_page_2.png
      :width: 400px

#. Under the Name write ``AD4130-8``
#. Under Source hit the … button and set the path to where you have stored the
   AD4130-8 Plugin.
#. Press ``Ok``.
#. Press ``Close``.

ACE software Operation
----------------------

Launching the software
~~~~~~~~~~~~~~~~~~~~~~

After the EVAL-AD4130-8WARDZ and controller board are properly connected to the
PC, launch the ACE software by taking the following steps:

#. From the Start menu of the PC, select All Programs > Analog Devices > ACE>
   ACE.exe to open the ACE software main window shown below

#. If the EVAL-AD4130-8WARDZ is not connected to the USB port via the controller
   board when the software launches, the AD4130-8 Eval Board icon does not
   appear in the Attached Hardware section in ACE (see Figure below).To make the
   AD4130-8 Eval Board icon appear, connect the EVAL-AD4130-8WARDZ and the
   controller board to the USB port of the PC, wait a few seconds, and then
   follow the instructions in the dialog box that opens.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130-8/ad4130_8_ace_start_page.png
      :width: 400px

#. Double click the AD4130-8 Eval Board icon to open the AD4130-8 Eval Board
   view window shown below:

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130-8/ad4130_8_ace_board_page.png
      :width: 400px

#. Double click the AD4130-8 chip icon in the AD4130-8 Eval Board view window to
   open the AD4130-8 chip view window shown below:

#. Click Software Defaults and then click Apply Changes to apply the default
   settings to the AD4130-8 (see figure below)

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130-8/ad4130_8_ace_chipview_page.png
      :width: 400px

Chip view window
~~~~~~~~~~~~~~~~

After completing the steps in the
:dokuwiki:`Software Installation Procedures </resources/eval/user-guides/ad4130-8/softwareprocedures#ace_plugin_install_guide>`
section and the
:dokuwiki:`Evaluation Board Set-up Procedures </resources/eval/user-guides/ad4130-8/hardwareguide#set-up_procedures>`
section, set up the system for data capture by taking the following steps:

#. Block icons that are dark blue are programmable blocks. Click a dark blue
   block icon to open a configurable pop-up window to customize the data
   capture.
#. The ``Proceed to Memory Map`` button brings the user to the memory map of the
   AD4130-8. This allows the user to configure the AD4130-8.
#. The ``Proceed to Analysis`` button brings the user to the Analysis tab. This
   allows the user to see the performance results of the AD4130-8 and displays
   the data.

Waveform Window
~~~~~~~~~~~~~~~

The Waveform tab graphs the conversions gathered and processes the data,
calculating the peak-to-peak noise, rms noise, and resolution.

1) Waveform graph and controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data waveform graph shows each successive sample of the ADC output. Zoom in
on the data in the graph using the scroll wheel on your mouse or by selecting
the magnifying glass.

2) Analysis Channel
^^^^^^^^^^^^^^^^^^^

The Result section shows the analysis of the channel selected .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_waveform_page_1.png
   :width: 400px

3) Samples
^^^^^^^^^^

The Samples numeric control set the number of samples gathered per batch. This
control is unrelated to the ADC mode. You can capture a defined sample set or
continuously gather batches of samples. In both cases, the number of samples set
in the Samples numeric input dictates the number of samples. The Noise Analysis
section displays the results of the noise analysis for the selected analysis
channel, including both noise and resolution measurements.

4) Capture
^^^^^^^^^^

Click the Run Once button to start gathering ADC results. Click the Run
Continuously button to start gathering ADC results continuously. Results appear
in the waveform graph (Label 1).

5) Display Units and Axis Controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click the Codes drop-down menu to select whether the data graph displays in
units of voltages or codes. This control affects both the waveform graph and the
histogram graph. The axis controls is fixed. When selecting Fixed, the axis
ranges can be programmed; however, these ranges do not automatically adjust
after each batch of samples.

6) Histogram Plot
^^^^^^^^^^^^^^^^^

Allows to view an Histogram plot of the data collected.

Memory map Window
~~~~~~~~~~~~~~~~~

Use the Memory Map tab to access the registers of the AD4130-8, shown in the
figure below. This tab changes register settings and shows additional
information about each bit in each individual register.

1) Export Buttons
^^^^^^^^^^^^^^^^^

The Export buttons on the Register Map tab allow the user to save and load
register settings. Click Save to save all the current register settings to a
file for later use. Click Load to load a previously saved register map.

2) Register
^^^^^^^^^^^

The Register section shows the value that is set in the selected register. Check
the value of the register in this window by clicking on the bits. Clicking any
individual bit changes the bit from 1 to 0 or 0 to 1, depending on the initial
state of the bit. The register value can also be changed by writing the
hexadecimal value in the input field to the right of the individual bits.

3) Bitfields
^^^^^^^^^^^^

The Bitfields section shows the individual bitfield of the selected register.
The register is broken by name into its bitfields, name of the bitfields, a
description of each bitfield, and access information. Show each individual
bitfield by pressing the show bitfield button (label 4). Apply these changes
using label 5. Search for specific registers using label 6.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_memory_page_1.png
   :width: 600px

AD4130-8 Demo Modes
-------------------

:dokuwiki:`Visit the demo mode section here </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes>`
**Contents of the demo modes section:**

#. :dokuwiki:`Noise Test Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#noise_test_demo>`
#. :dokuwiki:`2 Wire RTD Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#wire_rtd_demo>`
#. :dokuwiki:`3 Wire RTD Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#wire_rtd_demo1>`
#. :dokuwiki:`4 Wire RTD Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#wire_rtd_demo2>`
#. :dokuwiki:`Thermocouple Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#thermocouple_demo>`
#. :dokuwiki:`Thermistor Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#thermistor_demo>`
#. :dokuwiki:`4 Wire Bridge Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#wire_bridge_demo>`
#. :dokuwiki:`6 Wire Bridge Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#wire_bridge_demo1>`
#. :dokuwiki:`AD4130-8 Current Consumption Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#current>`
#. :dokuwiki:`AD4130-8 Power test Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#current1>`
#. :dokuwiki:`AD4130-8 ECG Demo </resources/eval/user-guides/ad4130-8/softwareprocedures/demo_modes#ECG>`

Active Function Model Guide
---------------------------

This page provides a step by step guide to launching and using ADI"s new Active
Function Model Tool. The AFM simulates crucial part performance characteristics
within seconds. Configure operating conditions such as operation modes and
sensor biasing/excitation, as well as device features like gain or FIFO.
Performance characteristics include noise, histogram, resolution, power
consumption, timing diagrams, response plots, and more.

:dokuwiki:`Visit the Active Functional Model (AFM) section here </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM>`
**Contents of the AFM section:**

#. :dokuwiki:`Tools and Analysis Windows </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#tools>`
#. :dokuwiki:`Memory Map </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#memory_map>`
#. :dokuwiki:`Sequencer Timing Diagram </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#sequencer_timing_diagram>`
#. :dokuwiki:`FIFO Timing Diagram </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#fifo_timing_diagram>`
#. :dokuwiki:`Power Calculator </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#power_calculator>`
#. :dokuwiki:`Analysis Window </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#analysis_window>`
#. :dokuwiki:`Noise(Simulation Analysis) Window </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#noise_window>`
#. :dokuwiki:`Frequency Response Window </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#frequency_response_window>`
#. :dokuwiki:`Step Response Window </resources/eval/user-guides/AD4130-8/softwareprocedures/AFM#step_response_window>`

Firmware Install Guide
----------------------

:dokuwiki:`AD4130-8 Firmware </resources/eval/user-guides/ad4130/mbed_iio_app>`

:dokuwiki:`Previous Page: Hardware Guide </resources/eval/user-guides/ad4130-8/hardwareguide>`

:dokuwiki:`Return to Homepage </resources/eval/user-guides/ad4130-8>`
