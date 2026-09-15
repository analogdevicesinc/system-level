.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ad7173-8ardz/software

======= Software Guide =======

.. _eval-ad7173-8ardz software:

ACE Software
============

The ACE software is available
:adi:`Here. <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`

The quick start guide is available on the landing page here
:dokuwiki:`(Quick Start Guide) </resources/eval/eval-ad7173-8ardz#quick_start_guide>`
or for the step by step install guide see the below.

Installation Guide
------------------

The EVAL-AD7173-8ARDZ evaluation kit includes a link to the software that needs
to be installed before using the EVAL-AD7173-8ARDZ evaluation board.

.. important::

   : The evaluation software and drivers must be installed before connecting
   both the evaluation board and the SDP-K1 board to the PC. This ensures that
   the evaluations system is correctly recognized when it is connected to the
   PC.

Installing the ACE Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install the **ACE** software,

- With the SDP board disconnected from the USB port of the PC, download the ACE
  evaluation software package to start the ACE evaluation software installation
- Click on Download ACE Installer
- Run the installer and follow the instructions to complete the software
  installation process

During the installation process, be sure to select Precision Converter
Components when prompted and enable the LibIIO Wrapper to ensure that all
necessary software components are installed.

.. tip::

   The LibIIO Wrapper must be installed for ACE to detect the connected
   hardware. If you need to install the LibIIO Wrapper after ACE has been
   installed, click the "Help" button in the main ACE window. In the "ACE Help"
   panel that appears expand the "Application Resources" section, and you will
   find a link to run a local copy of the LibIIO Wrapper Installer.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4111ardz/libiio.png
   :width: 400px

   Figure 3. Select Precision Converter Components during ACE installation

When the following prompt appears, be sure to select **LibIIO** and
**LibIIODrivers** options, then click **Install**.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4111ardz/libiio_drivers.png
   :width: 400px

   Figure 4. Select LibIIO components during ACE installation

Evaluation Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

When the ACE evaluation software installation is complete, take the following
steps to set up the SDP-K1 and evaluation board together.

- Connect the SDP-K1 and evaluation board using the Arduino headers.
- Connect the power supplies configuration.
- Connect the USB cable to the SDP-K1.
- Open the ACE software.

Software Operation
~~~~~~~~~~~~~~~~~~

To start the ACE evaluation software, from the Windows Start menu, click Analog
Devices > ACE. The software window opens (See Figure 5) until the software
recognizes the AD7173-8 evaluation board. When the software recognizes the
board, double-click on the icon in the **Start** view to open the main window
seen in Figure 6. Make sure that you already have the AD717x-8 plugin in the
plugin manager.

By clicking on the part in the main ACE evaluation software window (See Figure
6), the chip view will be opened (Figure 7).

The chip view shows the block diagram of the AD7173-8. This tab allows the user
to select inputs, set up the ADC, reset the ADC, and view errors present, as
well as configure the device for different demonstration modes. Figure 7 shows
the chip view in detail, and the following sections discuss the different
elements on the Chip view of the software window.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7173-8/ace_figure_5.png
   :width: 800px

   Figure 5. ACE Evaluation Select Interface Window

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7173-8/ace_figure_6.png
   :width: 800px

   Figure 6. ACE Evaluation Software Main Window

CONFIGURATION TAB
~~~~~~~~~~~~~~~~~

The **Configuration tab** shows a block diagram of the AD7173-8. This tab allows
the user to select inputs, set up the ADC, reset the ADC, and view errors
present, as well as configure the device.

Functional Block Diagram (1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The functional block diagram of the AD7173-8 (Label 1 in Figure 7) shows each
  of the functional blocks within the AD7173-8. Clicking a functional block on
  this diagram opens the configuration pop-up window for that block.

Configuration Pop-Up Button (2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Each block has a pop-up window (Label 2 in Figure 7) which opens a different
  window to configure the relevant block.

External Parameters (3, 4, 5, 6)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- There are three external parameters that are set by the EVAL-AD7173-8ARDZ but
  must be entered into the software: the AVDD1 and AVDD2 (Label 3 in Figure 7),
  external reference (Label 4 in Figure 7), IOVDD (Label 5 in Figure 7)and AVSS
  (Label 6 in Figure 7). The external reference on the EVAL-AD7173-8ARDZ is set
  to 2.5 V by using an ADR4525. If bypassing the ADR4525 on the board, change
  the external reference voltage value in the software to ensure correct
  calculation of results in the Waveform and Histogram tabs in the Waveform
  Analysis window.

Status Bar (7)
^^^^^^^^^^^^^^

- The status bar (Label 7 in Figure 7) displays status updates.

Memory Map Button (8)
^^^^^^^^^^^^^^^^^^^^^

- Opens the Memory Map tab.

Waveform Analysis Button (9)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Opens the Waveform tab.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7175-8/slide1.jpg
   :width: 900px

   Figure 7. AD7173-8 Functional Block Diagram

WAVEFORM TAB
~~~~~~~~~~~~

The **Waveform tab** can display the different waveforms for voltage input,
current input and select the channel. The waveform tab graph the conversions
gathered and processes the data, calculating the peak-to-peak noise, rms noise,
and resolution.

Waveform Graph and Controls (10, 11)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The data waveform graph (Label 10 in Figure 8) shows each successive sample of
  the ADC output. Zoom in on the data in the graph using the control toolbar
  (Label 11 in Figure 8). Change the scales on the graph by typing values into
  the x-axis and y-axis fields.

Samples (12)
^^^^^^^^^^^^

- The Samples numeric control (Label 12 in Figure 8) set the number of samples
  gathered per batch.

Serial Interface and Internal Reference (13)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Sets the ADC mode, enables DATA_STAT and Internal Reference (Label 13 in
  Figure 8).

Run (14)
^^^^^^^^

- Click *Run Once or Run Continuously* (Label 14 in Figure 8) to start gathering
  ADC results. If *Run Once* is clicked, the ADC returns the number of samples
  specified by the Samples control. If *Run Continuously* , the ADC continuously
  returns samples until stopped by the user. Samples specifies the amounts of
  samples to be shown on the data graph. This control is unrelated to the ADC
  mode. Results appear in the waveform graph (Label 10 in Figure 8).

Channel Selection (15)
^^^^^^^^^^^^^^^^^^^^^^

- The Channel Selection control (Label 15 in Figure 8) selects which channel/s
  is displayed on the data waveform. These controls only affect the waveform
  graphs and have no effect on the channel settings in the ADC register map.

Display Units and Axis Controls (16)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Click the Units dropdown box (Label 16 in Figure 8) to select whether the data
  graph displays in units of voltages/amps or codes. This control is independent
  for each graph.

Results Pane (17)
^^^^^^^^^^^^^^^^^

- The *RESULTS* pane (Label 17 in Figure 8) displays parametric values for the
  selected display format. The bottom of the *RESULTS* pane also has buttons
  that allow the user to import or export sample data.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7175-8/slide2.jpg
   :width: 1000px

   Figure 8. AD7175-8 Waveform Tab

HISTOGRAM TAB
~~~~~~~~~~~~~

The Histogram tab generates a histogram using the gathered samples and processes
the data, calculating the peak-to-peak noise, rms noise, and resolution.

Histogram Graph and Controls (18, 19)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The data histogram graph (Label 18 in Figure 9) shows the number of times each
  sample of the ADC output occurs. Zoom in on the data using the control toolbar
  (Label 19 in Figure 9) in the graph.

Channel Selection (20)
^^^^^^^^^^^^^^^^^^^^^^

- The Channel Selection control (Label 15 in Figure 8) selects which channel/s
  is displayed on the data waveform. These controls only affect the waveform
  graphs and have no effect on the channel settings in the ADC register map.

Display Units and Axis Controls (21)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Click the Units dropdown box (Label 21 in Figure 9) to select whether the data
  graph displays in units of voltages/amps or codes. This control is independent
  for each graph.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7175-8/slide3.jpg
   :width: 1000px

   Figure 9. Histogram Tab

Memory Map
~~~~~~~~~~

Register Tree (22)
^^^^^^^^^^^^^^^^^^

- The register maps nested list (Label 22 in Figure 10) shows the full register
  map in a tree control. Each register is shown. Clicking the expand button next
  to each register shows all the bit fields contained within that register.

Register Tree Search (23)
^^^^^^^^^^^^^^^^^^^^^^^^^

- The register tree search box (Label 23 in Figure 10) allows the user to search
  the tree for any register or bit field. Enter a value into this field to
  filter the register tree.

Register and Bit Field Control (24, 25, 26, 27)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The register and bit field control section (Label 24 in Figure 10) allows the
  user to change the individual bit of the register selected in the register
  tree by clicking the bits or by programming the register value directly into
  the number control field (Label 25 in Figure 10). This control also shows all
  bit fields for the selected register. Change the values by using a dropdown
  box (Label 26 in Figure 10) or by selecting or clearing a checkbox (Label 27
  in Figure 10).

Documentation (28)
^^^^^^^^^^^^^^^^^^

- The Bitfield Documentation (Label 28 in Figure 10) contains the documentation
  for the register or the bit field selected. This field can be updated by
  selecting a register or bit field in the register tree or hovering over the
  register or bit field in the register tree or register control. This
  documentation will be displayed by clicking the

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad4111ardz/ad4111_documentation_button.png
    :width: 20px

   button (Label 28 in Figure 10).

Import and Export (29)
^^^^^^^^^^^^^^^^^^^^^^

- Save and Load (Label 29 in Figure 10) allow the user to save the current
  register map setting to a file and to load the setting from the same file,
  respectively.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7175-8/slide4.jpg
   :width: 1000px

   Figure 10. Memory Map

:dokuwiki:`Return to Hardware Guide </resources/eval/user-guides/eval-ad7173-8ardz/hardware_guide>`
:dokuwiki:`Return to Homepage </resources/eval/eval-ad7173-8ardz>`
