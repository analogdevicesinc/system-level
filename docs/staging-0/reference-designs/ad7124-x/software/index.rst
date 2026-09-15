.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad7124-x/software

======= Software Guide =======

.. _ad7124-x software:

Eval+ Software
==============

The AD7124 Evaluation+ software is available
:adi:`here. <media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`

The quick start guide is available on the landing page here
:dokuwiki:`(Quick Start Guide) </resources/eval/user-guides/ad7124-x#quick_start_guide>`
or for the step by step install guide see the below

Install Guide
-------------

- Warning : The evaluation software and drivers must be installed before
  connecting both the evaluation board and the SDP-B board to the PC. This
  ensures that the evaluations system is correctly recognized when it is
  connected to the PC.

The software and drivers required for the installation walked through in this
section can be found below:

- :adi:`AD7124 Evaluation Software <media/en/evaluation-boards-kits/evaluation-software/ad7124-eval-plus-installer.zip>`
- `SDP-B system demonstration platform drivers. <http://swdownloads.analog.com/ACE/SDP/SDPDrivers.exe>`__

Installing the AD7124 Eval+ Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Download the Eval+ Software from the link given above.
#. Once the software has been downloaded, extract the downloaded files to a
   convenient location.
#. Navigate to these files and go to the **Volume** directory (AD7124 Eval+
   Installer -> Volume).

#. Run **setup.exe**, as shown below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/install_1.png
      :width: 800px

#. In the "Destination Directory" windows, check that both the "Directory for
   AD7124 Eval+" and "Directory for National Instruments products" are both set
   to the Program Files directory (or a preferred directory of your choosing)
   and click "Next >>".

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/dir_screen.jpg
      :width: 400px

#. You will then be prompted to accept ADI"s license agreement. Read the
   agreement and check the "I accept" box. Hit "Next >>" to continue.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/license_agree.jpg
      :width: 400px

#. Next you will have to read and agree to the National Instruments license
   agreement. Check the "I accept" box. Hit "Next >>" box to continue.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/ni_license_agree.jpg
      :width: 400px

#. In the next pop-up screen you will be asked to disable Windows fast start.
   National Instruments recommends disabling fast start as it can cause hardware
   issues. For more information click the link provided in the pop-up, or
   alternatively
   `here <https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z000000P9ErSAK&l=en-IE>`__.
   In this example, it has been disabled. Hit "Next >>" box to continue.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/fast_start_up.jpg
      :width: 400px

#. The next screen you will see is a summary table of what is going to be
   installed on your machine. Verify that this is indeed the AD7124 Eval
   software and click "Next >>".

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/start.jpg
      :width: 400px

#. The software will then begin installing.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/install.jpg
      :width: 400px

#. Once the installation has completed, the following screen will appear. Click
   "Next >>". The software is now installed.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/install_fin.jpg
      :width: 400px

Once the software is set up an installed the tutorials bellow describe how to
get the AD7124 Evaluation board set up with various sensors.

Eval+ Software Windows
----------------------

Configuration Tab
~~~~~~~~~~~~~~~~~

The Configuration tab (Label 1) shows a block diagram of the AD7124-8. It allows the user to set up the ADC, reset the ADC, read the diagnostics to view errors present, as well as configure the device for different demo modes. The Configuration tab is shown in more detail below, along with explanations of the features on this tab. .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_home_labels.png
   :width: 600px

Board Selection (2)
^^^^^^^^^^^^^^^^^^^

This window displays the current mode of operation of the Eval+ Software.
Clicking SELECT PRODUCT will allow you to change the Eval+ Software to
simulation mode, or alternatively pick another board if there is more then one
connected.

Tutorial Button (3)
^^^^^^^^^^^^^^^^^^^

Clicking on this Question Mark button will open up a tutorial on using the
software, this give additional information on using the AD7124-8 software.

ADC Reset (4)
^^^^^^^^^^^^^

Click ADC RESET to perform a software reset of the AD7124-8. There is no
hardware reset pin on the AD7124-8. To perform a hard reset, remove power from
the board. However, the software reset has the same effect as a hard reset.

Summary (5)
^^^^^^^^^^^

Clicking the SUMMARY button (Label 6) displays the channel configuration
information on each of the individual setups as well as information on any error
present. These tabs can be used to quickly check how the ADC channels are
configured, as well as any errors that are present.

Selecting External Reference (6)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two options to select the external reference on the AD7124-8 front
panel, AVDD and REFIN1(+/-). The REFIN1(+/-). Field sets the external reference
voltage that is connected between REFIN1+ and REFIN1-, and the AVDD field is
used to set the voltage level of the AVDD voltage for the AD7124-4. Using
EVAL-AD7124-8BSDZ eval board the AVDD voltage is 3.3V. Either of these can be
used in calculating the results on the Waveform and Histogram tabs. The
evaluation board has an external 2.5V ADR4525 reference, which can be bypassed;
if bypassing the ADR4525 on board ensure to change the external reference
voltage value in REFIN1(+/-) to ensure correct calculation of results in the
Waveform and Histogram tabs.

Functional Block Diagram (7)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The functional block diagram of the ADC shows each of the functional blocks
within the ADC. Clicking a configuration button on this graph opens the
configuration popup window for that block.

Configuration Popup Button (8)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each configuration popup button opens a different window allowing for
configuration of the relevant functional block.

Demo Modes (9)
^^^^^^^^^^^^^^

The AD7124-8 software supports a number of demo modes, these demo modes
configure the AD7124-8 for each of the modes shown. The is a help file for each
demo mode that is available once the question mark is clicked on.

Device Error (10)
^^^^^^^^^^^^^^^^^

The Device Error LED indicates if an overall error is present in the diagnostics
register. For this indicator to work, the check for the different diagnostic
errors must be enabled in the Error_EN register..

Status Bar (11)
^^^^^^^^^^^^^^^

The status bar displays status updates such as Analysis Completed, Reset
Completed, Configuring Demo Mode etc. during software use, as well as the
software version and busy indicator.

Waveform Tab
~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_waveform_labels.png
   :width: 600px

The Waveform tab graphs the conversions gathered and processes the data,
calculating the peak-to-peak noise, rms noise, and resolution.

Waveform Graph and Controls (1 & 2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data waveform graph shows each successive sample of the ADC output. Zoom in
on the data in the graph using the control toolbar. Change the scales on the
graph by typing values into the x-axis and y-axis.

Analysis Channel (3)
^^^^^^^^^^^^^^^^^^^^

The Noise Analysis section and histogram graph show the analysis of the channel
selected via the Analysis Channel control.

Samples (4 & 5)
^^^^^^^^^^^^^^^

The Samples numeric control and batch control set the number of samples gathered
per batch. Batch control sets whether a single batch or multiple batches of
samples are gathered. This control is unrelated to the ADC mode. You can capture
a defined sample set or continuously gather batches of samples. In both cases,
the number of samples set in the Samples numeric input dictates the number of
samples.

Sample (6)
^^^^^^^^^^

Click the SAMPLE button to start gathering ADC results. Results appear in the
waveform graph (Label 1).

Channel Selection (7)
^^^^^^^^^^^^^^^^^^^^^

The channel selection control selects which channels display on the data
waveform and shows the analog inputs for the channel labeled next to the on and
off controls. These controls only affect the display of the channels and have no
effect on the channel settings in the ADC register map.

Display Units and Axis Controls (8)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click the Display Units drop-down menu to select whether the data graph displays
in units of voltages or codes. This control affects both the waveform graph and
the histogram graph. The axis controls switch between dynamic and fixed. When
dynamic is selected, the axis automatically adjusts to show the entire range of
the ADC results after each batch of samples. When selecting Fixed, the axis
ranges can be programmed; however, these ranges do not automatically adjust
after each batch of samples.

Device Error (9)
^^^^^^^^^^^^^^^^

The Device Error LED indicates if an overall error is present in the diagnostics
register. For this indicator to work, the check for the different diagnostic
errors must be enabled in the Error_EN register.

Noise Analysis (10)
^^^^^^^^^^^^^^^^^^^

The Noise Analysis section displays the results of the noise analysis for the
selected analysis channel, including both noise and resolution measurements.

Histogram Tab
~~~~~~~~~~~~~

The Histogram tab generates a histogram using the gathered samples and processes
the data, calculating the peak-to-peak noise, rms noise, and resolution.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_histogram_labels.png
   :width: 600px

Histogram Graph and Controls (1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data histogram graph shows the number of times each sample of the ADC output
occurs. Zoom in on the data using the control toolbar in the graph (5). Change
the scales on the graph by typing values into the x-axis and y-axis.

Analysis Channel (2)
^^^^^^^^^^^^^^^^^^^^

The Noise Analysis section and histogram graph show the analysis of the channel
selected via the Analysis Channel control.

Noise Analysis (3)
^^^^^^^^^^^^^^^^^^

The Noise Analysis section displays the results of the noise analysis for the
selected analysis channel, including both noise and resolution measurements.

Display Units and Axis Controls (4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click the Display Units drop-down box to select whether the data graph displays
in units of voltages or codes. This control affects both the waveform graph and
the histogram graph. The axis controls can be used to switch between dynamic and
fixed range. When Dynamic is selected, the axis automatically adjusts to show
the entire range of the ADC results after each batch of samples. When selecting
Fixed, the user can program the axis ranges; the axis ranges do not
automatically adjust after each batch of samples.

Modelling Performance Tab
~~~~~~~~~~~~~~~~~~~~~~~~~

The Modelling Performance performance tab uses an ideal model of the AD7124 to
give frequency responses based on the users required specifications. It provides
the user with key information such as the "Filter Profile", "Filter Step
Response" and "Power/Timing Diagrams".

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_model_label.png
   :width: 600px

Model Selection (1)
^^^^^^^^^^^^^^^^^^^

This drop down bar allows the user to select between modelling the filter
profile, the step response or the power/timing diagrams. The main graph window
(3) will update upon selection.

Channel Selection (2)
^^^^^^^^^^^^^^^^^^^^^

Allows the user to select which channel of the AD7124 they want to get modelling
information from.

Waveform Window (3)
^^^^^^^^^^^^^^^^^^^

Shows the results of the requested modelled system. The window can be navigated
using the graphing tools in the top right hand corner (4). The results will
update on the fly as new information is entered.

Filter Rejection (5)
^^^^^^^^^^^^^^^^^^^^

Filter Performance (6)
^^^^^^^^^^^^^^^^^^^^^^

This window shows the Passband frequency at 3dB, along with the settling time
and the notch and ADC frequencies. This values update in real time as the inputs
to the filter rejection window (5) change.

Register Map Tab
~~~~~~~~~~~~~~~~

Use the Register Map tab to access the registers of the AD7124-8. This tab
changes register settings and shows additional information about each bit in
each individual register.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/eval_plus_register_map_labels.png
   :width: 600px

Register Map (1)
^^^^^^^^^^^^^^^^

On the top of the tab are the registers of the AD7124-8. Click any register to
read the register value. Access each register of the AD7124-8 using the register
map.

Search (2)
^^^^^^^^^^

This search bar can be used to search for a particular register or bitfield
within the AD7124-8 register map. To use the search bar, enter the register name
or bitfield that you want to search for, then clock the "plus" icon to the left
of the Register Maps folder to expand out the folder and show the search
results.

Save and Load Buttons (3)
^^^^^^^^^^^^^^^^^^^^^^^^^

The Save and Load buttons on the Register Map tab allow the user to save and
load register settings. Click Save to save all the current register settings to
a file for later use. Click Load to load a previously saved register map.

Export (4)
^^^^^^^^^^

The export button allows the user to save the current register configuration as
a C file. When the export button is clicked, file explorer will be opened and
you will be asked where to save the register configuration code for flashing the
part at a later time.

Register (5)
^^^^^^^^^^^^

The Register section shows the value that is set in the selected register. Check
the value of the register in this window by clicking on the bits. Clicking any
individual bit changes the bit from 1 to 0 or 0 to 1, depending on the initial
state of the bit. The register value can also be changed by writing the
hexadecimal value in the input field to the right of the individual bits.

Documentation (6)
^^^^^^^^^^^^^^^^^

The Documentation section shows information relating to the different bit fields
when selected from the register map section on the left. This information is the
same information in the AD7124-8 data sheet.

AD7124 Eval+ Demo Modes
-----------------------

:dokuwiki:`Visit the demo mode section here </resources/eval/user-guides/ad7124-x/software/demo_modes>`
**Contents of the demo modes section:**

#. :dokuwiki:`Noise Test Demo </resources/eval/user-guides/ad7124-x/software/demo_modes#noise_test_demo>`
#. :dokuwiki:`2 Wire RTD Demo </resources/eval/user-guides/ad7124-x/software/demo_modes#wire_rtd_demo>`
#. :dokuwiki:`3 Wire RTD Demo </resources/eval/user-guides/ad7124-x/software/demo_modes#wire_rtd_demo1>`
#. :dokuwiki:`4 Wire RTD Demo </resources/eval/user-guides/ad7124-x/software/demo_modes#wire_rtd_demo2>`
#. :dokuwiki:`Thermocouple Demo </resources/eval/user-guides/ad7124-x/software/demo_modes#thermocouple_demo>`
#. :dokuwiki:`Thermistor Demo </resources/eval/user-guides/ad7124-x/software/demo_modes#thermistor_demo>`
#. :dokuwiki:`4 Wire Bridge Demo </resources/eval/user-guides/ad7124-x/software/demo_modes#wire_bridge_demo>`
#. :dokuwiki:`6 Wire Bridge Demo </resources/eval/user-guides/ad7124-x/software/demo_modes#wire_bridge_demo1>`

Virtual Eval Guide
------------------

This page provides a step by step guide to launching and using ADI"s new Virtual
Evaluation Tool.

#. Navigate to the Virtual Eval tool by clicking this link:
   http://beta-tools.analog.com/virtualeval/ or alternatively, by going to the
   AD7124 homepage on analog.com and finding the link there.

#. Select the AD7124-8 by going to "Precision ADC < 10MSPS" and finding the part
   there.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/v_eval_start.png
      :width: 500px

#. Now you are ready to start using the tool.

Tutorial
~~~~~~~~

There is an online video walkthrough on using the tool in conjunction with the
AD7124-4, the 8 channel version of the AD7124-. This part works the same way as
the AD7124-8, therefore the tutorial is suitable for both parts. Once logged
into the Virtual Eval Tool and selecting the AD7124-8, navigate to the "Help"
tab. Here you will find the walkthrough video.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/v_eval_vid.png
   :width: 500px

:dokuwiki:`Continue to Hardware Guide </resources/eval/user-guides/ad7124-x/hardware_guide>`
:dokuwiki:`Return to Homepage </resources/eval/user-guides/ad7124-x>`
