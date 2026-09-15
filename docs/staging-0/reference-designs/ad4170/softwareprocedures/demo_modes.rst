.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes

.. _ad4170 softwareprocedures demo_modes:

Demo Modes
==========

Noise test Demo
---------------

- Warning: The evaluation software and drivers must be installed before
  connecting the EV-AD4170-ASD1Z-U1 evaluation board and EVAL-SDP-CB1Z board to
  the USB port of the PC to ensure the PC correctly recognizes the evaluation
  system.

If you have not set up the EV-AD4170-ASD1Z-U1 and controller board previously
please go to the
:dokuwiki:`Quick Start Guide </resources/eval/user-guides/ad4170#quick_start_guide>`

If you have not set up/installed the ACE plugin before please go to
:dokuwiki:`Install Guide </resources/eval/user-guides/ad4170/softwareprocedures#ace_plugin_install_guide>`

#. Double click the AD4170 Eval Board icon to open the AD4170 Eval Board view
   window. The demo wizard will be on the left, either as shown in the figure
   below (Label 1) or already expanded. Expand the wizard by clicking the arrow
   (Label 2).

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_noise_test.png
      :width: 600px

#. With the wizard expanded, select the noise test button (Label 1).

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_noise_test_page_2.png
      :width: 300px

#. The settings required for the demo are displayed to be viewed prior to
   writing to the AD4170 (Label 1). Click apply (Label 2) to write these
   settings to the board.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_noise_test_page_3.png
      :width: 300px

#. The summary is then displayed once the write is complete.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_noise_test_page_4.png
      :width: 200px

#. From here navigate to the chip view by double-clicking the AD417x chip (Label
   1).

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_noise_test_page_5.png
      :width: 600px

#. To make further changes to the configuration double click the memory map
   option (Label 1)

#. To begin capturing data double click the Analysis button (Label 2).

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_noise_test_page_6.png
      :width: 600px

#. To gather samples, change the Samples Count (Label 1) to the number of
   samples required, then click the Run Once button (Label 2) to acquire the
   samples from the ADC. The image below shows an example of the main window
   after running a noise test.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_noise_test_page_7.png
      :width: 600px

#. For more information on the Waveform window go to the software section
   :dokuwiki:`here </resources/eval/user-guides/ad4170/softwareprocedures#waveform_window>`

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board is set up to use the external 2.5 V on-board reference
(ADR4525). To read samples from the ADC, do the following:

- The value in the Refin1(+/−) field on the Configuration tab is set to 2.5 V
  by default to use the external 2.5 V on-board reference (ADR4525). If a
  different reference is used to the AD4170, the Refin1(+/−) field should be
  updated accordingly. (The analysis results are based on the value set in this
  input field.)
- Information on the reference choice can be viewed in the
  :dokuwiki:`Reference Options Tab </resources/eval/user-guides/ad4170/hardwareguide#reference_options>`
- When selecting Run Once, a batch of samples is read when clicking the button;
  the batch size is set by the value in the Samples field.
- When selecting Run Continuous, the software performs a continuous capture from the ADC by clicking the Run Once button. Click the Stop Capture button again to stop capturing data.
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

:dokuwiki:`Return to Software Guide </resources/eval/user-guides/ad4170/softwareprocedures>`
