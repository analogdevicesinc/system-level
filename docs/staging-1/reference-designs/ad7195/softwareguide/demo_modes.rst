.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad7195/softwareguide/demo_modes

.. _ad7195 softwareguide demo_modes:

Demo Modes
==========

Hardware Link for Noise Demo Mode
---------------------------------

.. list-table::
   :header-rows: 1

   * - Link Numbers
     - Colour
     - Default Position
     - Descirption
   * - JP1
     - Black
     - A
     - Used for stacking of Eval boards. To select Eval board(CS_N):
       Pos A(1-2): selects eval board 1 (CS_ARD_1)
       Pos B(2-3): selects eval board 2 (CS_ARD_2)
   * - JP2
     - Black
     - C
     - AVDD voltage select:
       Pos A: sets AVDD to 3.3v LDO supply
       Pos B: sets AVDD to external source
       Pos C: sets AVDD to 5V LDO Supply
   * - JP3
     - Black
     - A
     - IOVDD voltage select:
       Pos A: sets IOVDD to 3.3v LDO supply
       Pos B: sets IOVDD to external source
   * - JP4
     - Black
     - Uninserted
     - This link shorts AIN1 to AIN2. This is useful to perform noise tests on
       the AD7195
   * - JP5
     - Black
     - A
     - DVDD voltage select:
       Pos A: DVDD is connected to 3.3V
       Pos B: DVDD is connected to AVDD
   * - P15
     - Black
     - Uninserted
     - Used as external AVDD voltage connector for scp boards
   * - P16
     - Black
     - Uninserted
     - Used as external IOVDD voltage connector for scp boards

Noise test Demo
---------------

- Warning: The evaluation software and drivers must be installed before
  connecting the EVAL-AD7195ASDZ evaluation board and EVAL-SDP-CB1Z board to the
  USB port of the PC to ensure the PC correctly recognizes the evaluation
  system.

If you have not set up the EVAL-AD7195ASDZ and controller board previously
please go to the
:dokuwiki:`Quick Start Guide </resources/eval/user-guides/AD7195#quick_start_guide>`

If you have not set up/installed the ACE plugin before please go to
:dokuwiki:`Install Guide </resources/eval/user-guides/AD7195/softwareguide#ace_plugin_install_guide>`

#. Double click the AD7195 Eval Board icon to open the AD7195 Eval Board view
   window. The demo wizard will be on the left, either as shown in the figure
   below (Label 1) or already expanded. Expand the wizard by clicking the arrow
   (Label 2).

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/softwareguide/ad7195noisetest.png
      :width: 600px

#. With the wizard expanded, select the noise test button (Label 3).
#. The settings required for the demo are displayed to be viewed prior to
   writing to the AD7195 (Label 4). Click apply (Label 5) to write these
   settings to the board.

#. The summary is then displayed once the write is complete (Label 1).

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/softwareguide/ad7195noisesummary.png
      :width: 600px

#. From here navigate to the chip view by double-clicking the AD7195 chip (Label
   2).
#. To make further changes to the configuration click on the dark blue block in
   the chip view (Label 1) or double click the memory map option (Label 2)

#. To begin capturing data double click the Analysis button (Label 3).

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/softwareguide/ad7195noisechip.png
      :width: 600px

#. To gather samples, change the Samples Count (Label 1) to the number of
   samples required, then click the Run Once button (Label 2) to acquire the
   samples from the ADC. The image below shows an example of the main window
   after running a noise test.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad7195/softwareguide/ad795noisewaveform.png
      :width: 600px

#. For more information on the Waveform window go to the software section
   :dokuwiki:`here </resources/eval/user-guides/AD7195/softwareguide#waveform_window>`

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board is set up to use the external 2.5 V on-board reference
(ADR4525). To read samples from the ADC, do the following:

#. The value in the Refin1(+/−) field on the Configuration tab is set to 2.5 V
   by default to use the external 2.5 V on-board reference (ADR4525). If a
   different reference is used to the AD7195, the Refin1(+/−) field should be
   updated accordingly. (The analysis results are based on the value set in this
   input field.)

   - Information on the reference choice can be viewed in the
     :dokuwiki:`Reference Options Tab </resources/eval/user-guides/AD7195/hardwareguide#reference_options>`

#. When selecting Run Once, a batch of samples is read when clicking the button;
   the batch size is set by the value in the Samples field.

   - When selecting Run Continuous, the software performs a continuous capture
     from the ADC by clicking the Run Once button. Click the Stop Capture
     button again to stop capturing data.
   - Use the navigation tools within each graph to control the cursor, zooming, and
     panning.

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the waveforms resulting from the gathered samples in the Analysis tab. The
waveform graph shows each successive sample of the ADC output (input referred).
The indicators beside this graph show the channels converting. The navigation
tools allow you to control the cursor, zooming, and panning. You can also
display the conversions as voltages or codes. Below the graph are parameters,
such as peak-to-peak noise and rms noise, in the Results section for the current
batch of samples. If there are several enabled analog input channels, you can
select each enabled channel and the conversions through the analyzed channel
using the Results Tab. To save the data into an Excel file, select the Export
button from the Results Tab. A Save dialog box is displayed, prompting you to
save the data to an appropriate folder location.

:dokuwiki:`Return to Software Guide </resources/eval/user-guides/ad7195/softwareguide>`
