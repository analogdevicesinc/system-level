.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ad4116asdz/software

======= Software Guide =======

.. _eval-ad4116asdz software:

Eval+ Software
==============

The AD411x Evaluation+ software is available
:adi:`Here. <media/en/evaluation-boards-kits/evaluation-software/ad411x-eval-installer.zip>`

The quick start guide is available on the landing page here
:dokuwiki:`(Quick Start Guide) </resources/eval/user-guides/eval-ad4116asdz#quick_start_guide>`
or for the step by step install guide see the below

Install Guide
-------------

The EVAL-AD4116ASDZ evaluation kit includes a link to the software that needs to
be installed before using the EVAL-AD4116ASDZ evaluation board. There are two
parts to the installation:

- AD411X Eval+ software installation
- EVAL+ Dependencies installation, including SDP board drivers

.. important::

   : The evaluation software and drivers must be installed before connecting
   both the evaluation board and the SDP-B board to the PC. This ensures that
   the evaluations system is correctly recognized when it is connected to the
   PC.

Installing the AD411x Eval+ Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the **AD411X Eval+** software,

- With the SDP board disconnected from the USB port of the PC, download and
  unzip the AD411X Eval+ software installer file from the EVAL-AD4116ASDZ
  product page.
- Double-click the setup.exe file to begin the evaluation board software
  installation. The software then installs to the following default location:
  C:\\Program Files\\Analog Devices\\AD411X EVAL+ .
- A dialog box appears asking for permission to allow the program to make
  changes to the PC. Click Yes .

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-004.png
   :width: 400px

   Figure 4. Granting Permission for the Program to Make Changes to PC

- Select a location to install the software and then click Next. Figure 5 shows
  the default locations, which are displayed when the dialogue box opens, but
  another location can be selected by clicking Browse .

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-005.png
   :width: 400px

   Figure 5. Selecting the Location for Software Installation

- A license agreement appears. Read the agreement, select I accept the License
  Agreement , and click Next .

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-006.png
   :width: 400px

   Figure 6. Accepting the License Agreement

- A summary of the installation displays. Click Next to continue.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-007.png
   :width: 400px

   Figure 7. Reviewing a Summary of the Installation

- The message in Figure 8 appears when the installation is complete. Click Next
  .

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-008.png
   :width: 400px

   Figure 8. Indicating when the Installation is Complete

Installing the Eval+ Dependencies Drivers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the installation of the evaluation software is complete, a welcome window
appears for the installation of the **Eval+ Dependencies**.

- With the SDP board still disconnected from the USB port of the PC, ensure that
  all other applications are closed, and then click Install .

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-009.png
   :width: 400px

   Figure 9. Beginning the Drivers Installation

- To complete the driver installation, click Close , which closes the
  installation setup wizard.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-010.png
   :width: 400px

   Figure 10. Completing the Drivers Setup Wizard

- Before using the evaluation board, restart the PC.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-011.png
   :width: 400px

   Figure 11. Restarting the PC

Setting Up the System for Data Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing the steps in the Software Installation Procedures section and
the Evaluation Board Hardware section, set up the system for data capture as
follows:

- Allow the Found New Hardware wizard to run after connecting the SDP board to
  the PC. If using Windows XP, it may be necessary to search for the SDP
  drivers. Choose to automatically search for the drivers for the SDP board if
  prompted by the operating system.
- Check that the board is connecting to the PC correctly using the Device
  Manager of the PC. Access the Device Manager as follows:

  #. Right-click **My Computer** and then click **Manage**.
  #. A dialog box appears asking for permission to allow the program to make
     changes to the PC. Click **Yes**.
  #. The **Computer Management** window appears. Click **Device Manager** from
     the **System Tools** list (see Figure 12).
  #. If the SDP board appears under **ADI Development Tools** in the **TEST PC**
     nested list, the driver software has installed and the board is connecting
     to the PC correctly.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-012.png
   :width: 400px

   Figure 12. Checking if the Board is Connected to the PC Correctly

Launching the Software
~~~~~~~~~~~~~~~~~~~~~~

After completing the steps in the Setting Up the System for Data Capture
section, launch the **AD411X Eval+** software as follows:

- From the Start menu, click Programs > Analog Devices > AD411X Eval+ > AD411X
  Eval+ . The dialog box shown in Figure 13 appears. Select AD4116 Evaluation
  Board and the main window of the software shown in Figure 16 appears.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-013.png
   :width: 400px

   Figure 13. AD4116 Evaluation Board Selection

- If the EVAL-AD4116ASDZ evaluation system is not connected to the USB port via
  the SDP when the software is launched, the software displays the dialog box
  shown in Figure 14. Connect the evaluation board to the USB port of the PC,
  wait a few seconds, then click Refresh , and the dialog box shown in Figure 13
  appears.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-014.png
   :width: 400px

   Figure 14. Evaluation Board Selection, No Board Connected

- The dialog box shown in in Figure 15 appears. Quickstart mode provides a
  simplified version of the software that can be used as a starting point for
  evaluating the AD4116. This mode provides a graphical user interface (GUI) for
  setting up inputs, as shown in Figure 16, and allows the user to configure the
  device further by using the blue configuration buttons (Label 7 Figure 16).
- Advanced mode can be used when more configurability of the inputs is required.
  In this mode, the input GUI is not available. However, the user has access to
  the Registers tab, which provides full control of the AD4116 register map.
  When operating in advanced mode, the user must consult the AD4116 data sheet.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-015.png
   :width: 400px

   Figure 15. AD411X Eval+ Startup Mode Selection

Eval+ Software Windows
----------------------

After selecting **AD4116 Evaluation Board**, the main window of the evaluation
software displays, as shown in Figure 16. This tab shows the control buttons and
analysis indicators of the AD411X Eval+ software. The main window of the
**AD411X Eval+** software in **Quickstart** mode contains five tabs:
**Configuration**, **Voltage Waveform**, **Noise Table**, and **Histogram**. In
advanced mode, two additional tabs are available: **Ch Waveform** and
**Registers**.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4116asdz/26267-016.png
   :width: 600px

   Figure 16. Configuration Tab in Quickstart Mode

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4116asdz/26267-017.png
   :width: 600px

   Figure 17. Configuration Tab in Advanced Mode

Configuration Tab
~~~~~~~~~~~~~~~~~

- The Configuration tab shows a block diagram of the AD4116. This tab allows the
  user to select inputs, set up the ADC, reset the ADC, view errors present, and
  configure the device for different demonstration modes. Figure 16 shows the
  Configuration tab in detail, and the following sections discuss the different
  elements on the Configuration tab of the software window.

Inputs Quickstart Mode Only (1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The AD4116 has twelve voltage inputs and five low-level inputs, which can be
  configured as single-ended or fully differential pairs (Label 1 in Figure 16).
- The voltage range can also be set per input to ±10 V, ±5 V, 0 V to 10 V, 0 V
  to 5 V or N/A for low-level inputs. Changing the appropriate voltage range
  provides more realistic values for P - P Resolution and RMS Resolution shown
  in the Noise Analysis area (Label 22 in Figure 18).

Output Data Rate (ODR)/Measurement Time (2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The ODR can be set for all inputs in the Configuration tab (Label 2 in Figure
  16). Set the ODR by entering a value in hertz into the ODR(Hz) box or a
  measurement time in milliseconds into the Time(ms) box. If an ODR is entered,
  the software calculates the measurement time. If a time is entered, the
  software calculates the fastest ODR that can achieve the required measurement
  time.
- The device only supports a certain number of ODRs. Therefore, the software
  rounds up to the closest available value. ODR values depend on if a single or
  multiple channels are enabled. The fastest ODRs are available if only one
  channel is enabled. The values shown are valid for the sinc5 + sinc1 filter,
  which is enabled by default. If the sinc3 filter is enabled instead, refer to
  the AD4116 data sheet for the corresponding values.
- The value in the Time(ms) box represents time taken for one sample for one
  enabled channel.
- The value in the Total Time box represents the total time to take one sample
  for all enabled Inputs .

Demo Modes (3)
^^^^^^^^^^^^^^

- The AD411X Eval+ software contains a number of demonstration modes in the Demo
  Modes area (Label 3 in Figure 16). These demonstration modes configure the
  AD4116 for each of the input types (represented by the All ADCIN or All VIN
  Single-Ended and All Differential ).

ADC Reset (4)
^^^^^^^^^^^^^

- Click Reset to perform a software reset of the AD4116 (Label 4 in Figure 16).
  There is no hardware reset pin on the AD4116.
- To perform a hard reset, remove power from the board. The software reset has
  the same effect as a hard reset.

Tutorial Button (5)
^^^^^^^^^^^^^^^^^^^

- Click the tutorial button (Label 5 in Figure 16) to open a tutorial on using
  the software and additional information on using the AD411X Eval+ software.
  Click the blue information buttons for further information on different
  elements of the Configuration tab.

Functional Block Diagram (6)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The functional block diagram of the AD4116 (Label 6 in Figure 16) shows each
  of the functional blocks within the AD4116. Clicking a configuration button on
  the block diagram opens the configuration window for that block.

Configuration Popup Button (7)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Each configuration button (Label 7 in Figure 16) opens a different window to
  configure the relevant functional block.

External Parameters (8,9,10)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- There are three external parameters that are set by the EVAL-AD4116ASDZ board
  but must be entered into the software: the external reference (Label 8 in
  Figure 16), AVDD (Label 9 in Figure 16), and AVSS (Label 10 in Figure 16). The
  external reference on the EVAL-AD4116ASDZ board is set to 2.5 V by using an
  ADR4525. If bypassing the ADR4525 on board, change the external reference
  voltage value in the software to ensure correct calculation of results in the
  Waveform and Histogram tabs.

Configuration Summary (11)
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Clicking Summary (Label 11 in Figure 16) shows the input configuration,
  channel configuration, and information on each of the individual setups as
  well as information on any error present. These tabs can be used to quickly
  check how the ADC inputs and channels are configured, as well as any errors
  that are present.

Status Bar (12)
^^^^^^^^^^^^^^^

- The status bar (Label 12 in Figure 16) displays status updates such as
  Analysis Completed , Reset Completed , and Writing to Registers during
  software use, as well as the Busy indicator.

Waveform Tab
~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-018.png
   :width: 600px

   Figure 18. Voltage Waveform Tab

The AD411X Eval+ software has two different waveform tabs: **Voltage Waveform**
and **Ch Waveform** (in advanced mode only). The waveform tabs graph the
conversions gathered and processes the data, calculating the peak-to-peak noise,
rms noise, and resolution (see Figure 18). The **Voltage Waveform** tab graphs
the data at the voltage input in QuickStart mode. The **Ch Waveform** tab shows
the data converted per channel in Advanced mode.

Waveform Graph and Controls (13,14)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The data waveform graph (Label 13 in Figure 18) shows each successive sample
  of the ADC output. Zoom in on the data in the graph using the control buttons
  (Label 14 in Figure 18). Change the scales on the graph by typing values into
  the x-axis and y-axis.

Samples (15,16)
^^^^^^^^^^^^^^^

- The Samples box (Label 15 in Figure 18) and Sampling Mode (Label 16 in Figure
  18) set the number of samples gathered per batch. If Sampling Mode is set to
  Single Capture , the ADC returns the number of samples specified in the
  Samples box. If Sampling Mode is set to Continuous , the ADC continuously
  returns samples until stopped by the user. Samples specifies the amount of
  samples to be shown on the data graph. Samples is unrelated to the ADC mode.

Sample (17)
^^^^^^^^^^^

- Click Sample (Label 17 in Figure 18) to start gathering ADC results. Results
  appear in the waveform graph.

Plot Selection (18)
^^^^^^^^^^^^^^^^^^^

- The plot selection control area (Label 18 in Figure 18) allows the user to
  select which inputs display on the data waveform and shows the name of the
  input.
- These controls only affect the waveform graphs and have no effect on the
  channel settings in the ADC register map.

Display Units and Axis Controls (19)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Click the Units box in the Graph Configuration area (Label 19 in Figure 18) to
  select whether the data graph displays in units of voltage in amps or codes.
  This control is independent for each graph. The Y-scale and X scale boxes can
  be set to autoscale or fixed scaling. When Autoscale is selected, the axis
  automatically adjusts to show the entire range of the ADC results after each
  batch of samples. When Fixed is selected, the axis range can be set by the
  user. These ranges do not automatically adjust after each batch of samples.

Device Error (20)
^^^^^^^^^^^^^^^^^

- The Device Error indicator (Label 20 in Figure 18) illuminates in the Waveform
  tab when a cyclic redundancy check (CRC) error or an error in the ADC is
  detected. More specific information on the error can be by clicking Summary in
  the Configuration tab (Label 11 in Figure 16).

Analysis Input (21)
^^^^^^^^^^^^^^^^^^^

- The Noise Analysis box shows the analysis of the input selected via the
  analysis control (Label 21 in Figure 18).

Noise Analysis (22)
^^^^^^^^^^^^^^^^^^^

- The Noise Analysis area (Label 22 in Figure 18) displays the results of the
  noise analysis for the selected analysis input, including both noise and
  resolution measurements.

Input Range (23)
^^^^^^^^^^^^^^^^

- The Range box (Label 23 in Figure 18) is an indicator in QuickStart mode. The
  value is selected in the inputs area on the Configuration tab (Label 1 in
  Figure 16). In advanced mode, Range is a control that allows the user to
  select an input range for the input chosen for noise analysis.

Histogram Tab
~~~~~~~~~~~~~

The **Histogram** tab generates a histogram using the gathered samples and
processes the data, calculating the peak-to-peak noise, rms noise, and
resolution (see Figure 19).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-019.png
   :width: 600px

   Figure 19. Histogram Tab of the AD411X Eval+ Software

Histogram Graph and Controls (24,25)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The data histogram graph (Label 24 in Figure 19) shows the number of times
  each sample of the ADC output occurs. Zoom in on the data using the control
  buttons (Label 25 in Figure 19) in the graph. Change the scales on the graph
  by typing values into the x-axis and y-axis.

Noise Analysis (26)
^^^^^^^^^^^^^^^^^^^

- The Noise Analysis area (Label 26 in Figure 19) displays the results of the
  noise analysis for the selected analysis input, including both noise and
  resolution measurements.

Analysis Input (27)
^^^^^^^^^^^^^^^^^^^

- The data used to generate the histogram and values in the Noise Analysis area
  (Label 26 in Figure 19) is set by the Noise Analysis box (Label 27 in Figure
  19). All enabled inputs appear here in the Noise Analysis box.

Display Units and Axis Controls (28)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Click the Units box in the Graph Configuration area (Label 28 in Figure 19) to
  select whether the data graph displays in units of voltages/amps or codes.
  This control is independent for each graph.

The **Y-scale** and **X scale** boxes can be set to autoscale or fixed scaling.
When **Autoscale** is selected, the axis automatically adjusts to show the
entire range of the ADC results after each batch of samples. When **Fixed** is
selected, the user can set the axis range. These ranges do not automatically
adjust after each batch of samples.

Device Error (29)
^^^^^^^^^^^^^^^^^

- The Device Error indicator (Label 29 in Figure 19) illuminates in the
  Histogram tab when a CRC error or an error in the ADC is detected. More
  specific information on the error can be by clicking Summary in the
  Configuration tab (Label 11 in Figure 16).

Register Map Tab
~~~~~~~~~~~~~~~~

Use the Register Map tab to access the registers of the AD7124-8. This tab
changes register settings and shows additional information about each bit in
each individual register.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval_ad4116/26267-020.png
   :width: 600px

   Figure 20. Register Tab

Register Map (30)
^^^^^^^^^^^^^^^^^

- Clicking the register maps nested list (Label 30 in Figure 20) shows each
  register. Clicking the expand button next to each register shows all the bit
  fields contained within that register.

Search (31)
^^^^^^^^^^^

- The search box (Label 31 in Figure 20) allows the user to search the register
  maps list for any register or bit field. Entering a value into this control
  filters the register list.

Register and Bit Field Control (32-35)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The register control area (Label 32 in Figure 20) allows the user to change
  the individual bit of the register selected in the register by clicking the
  bits or by programming the register value directly into the value control box
  (Label 33 in Figure 20). The register and bit controls also show all bit
  fields for the selected register. Change the values by using the dropdown
  boxes (Label 34 in Figure 20) or by selecting or clearing a check box (Label
  35 in Figure 20).

Documentation (36,37)
^^^^^^^^^^^^^^^^^^^^^

- The Documentation area (Label 37 in Figure 20) contains the documentation for
  the register or the bit field selected. This field can be updated by selecting
  a register or bit field in the register list or hovering over the register or
  bit field in the register list or register control. The documentation area can
  also be displayed in a separate window by clicking Expand (Label 36 in Figure
  20).

Save and Load (38)
^^^^^^^^^^^^^^^^^^

- Save and Load (Label 38 in Figure 20) allow the user to save the current
  register map setting to a file and to load the setting from the same file,
  respectively.

:dokuwiki:`Return to Hardware Guide </resources/eval/user-guides/eval-ad4116asdz/hardware_guide>`
:dokuwiki:`Return to Homepage </resources/eval/user-guides/eval-ad4116asdz>`
