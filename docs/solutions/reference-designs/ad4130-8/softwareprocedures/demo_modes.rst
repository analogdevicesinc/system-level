Demo Modes
==========

Hardware Link for Noise Demo Mode
---------------------------------

+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Link Numbers | Colour | Default Position | Description                                                                                                              | Rough Board Location                  |
+==============+========+==================+==========================================================================================================================+=======================================+
| LK1-3        | White  | Inserted         | Ties AVSS and DGND together                                                                                              | N/A                                   |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK4          | Black  | A                | External Reference voltage select:                                                                                       | Right of J10                          |
|              |        |                  | Pos A: REFIN + is connected to the external +2.5V reference.                                                             |                                       |
|              |        |                  | Pos B: REFIN + is connected to the external +1.8V reference                                                              |                                       |
|              |        |                  | (+1.8V reference not currently available on the board).                                                                  |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK5          | Blue   | Inserted         | Noise Test. Channels AIN0 + AIN1                                                                                         | Right of Thermocouple Connection (A2) |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK6          | White  | Inserted         | REFIN(-) to AVSS                                                                                                         | Left of Switch S3                     |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK7          | Black  | A                | External +2.5V Reference:                                                                                                | Right of J10                          |
|              |        |                  | Pos A: ADR391B                                                                                                           |                                       |
|              |        |                  | Pos B: ADR3625B                                                                                                          |                                       |
|              |        |                  | (The ADR3625B is not currently available on the board)                                                                   |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK8          | Black  | Uninserted       | Connects AIN10 to R95. When used with LK9 you can use the AD4130-8 to measure it's own IOVDD current                     | Left of T_IOVDD                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK9          | Black  | Uninserted       | Connects AIN11 to R95. When used with LK8 you can use the AD4130-8 to measure it's own IOVDD current                     | Left of T_IOVDD                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK10         | Black  | Uninserted       | Connects AIN12 to R96. When used with LK11 you can use the AD4130-8 to measure it's own AVDD current                     | Left of Switch S1                     |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK11         | Black  | Uninserted       | Connects AIN13 to R96. When used with LK10 you can use the AD4130-8 to measure it's own AVDD current                     | Left of Switch S1                     |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK12         | White  | Uninserted       | Connects AVSS to -1.8V. LK1-3 must be removed before this jumper is inserted                                             | Right of Switch S1                    |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK14         | Black  | Uninserted       | Connects REFIN(+) to AVDD                                                                                                | Below 3.5mm Jack Connection (A1)      |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK15         | Black  | A                | ADP150-3.3 Powered up:                                                                                                   | Below Switch S1                       |
|              |        |                  | Pos A: LDO is on                                                                                                         |                                       |
|              |        |                  | Pos B: LDO is off                                                                                                        |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK16         | Black  | A                | ADP150-1.8 Powered up:                                                                                                   | Below Switch S1                       |
|              |        |                  | Pos A: LDO is on                                                                                                         |                                       |
|              |        |                  | Pos B: LDO is off                                                                                                        |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK17         | Black  | A                | Arduino communication:                                                                                                   | Between Arduino Connectors            |
|              |        |                  | Pos A: Standard                                                                                                          |                                       |
|              |        |                  | Pos B: Alternative                                                                                                       |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK18         | Black  | A                | Arduino communication:                                                                                                   | Between Arduino Connectors            |
|              |        |                  | Pos A: Standard                                                                                                          |                                       |
|              |        |                  | Pos B: Alternative                                                                                                       |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK19         | Black  | A                | Arduino communication:                                                                                                   | Between Arduino Connectors            |
|              |        |                  | Pos A: Standard                                                                                                          |                                       |
|              |        |                  | Pos B: Alternative                                                                                                       |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK20         | Black  | A                | Arduino communication:                                                                                                   | Between Arduino Connectors            |
|              |        |                  | Pos A: Standard                                                                                                          |                                       |
|              |        |                  | Pos B: Alternative                                                                                                       |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK21         | Black  | Uninserted       | Connects the CLK pin to the INT pin                                                                                      | Below T_IOVDD                         |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK22         | Red    | Uninserted       | Thermocouple - Cold Junction Resistor Bypass                                                                             | Left of Thermocouple Connection (A2)  |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK23         | Blue   | Uninserted       | Short EXC+/PSW: Pos Inserted = 4 Wire Bridge                                                                             | Left of Switch S3                     |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK24         | Blue   | Uninserted       | Short EXC+/PSW: Pos Inserted = 4 Wire Bridge                                                                             | Left of Switch S3                     |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK25         | Blue   | Uninserted       | Short EXC+/REFIN+: Pos Inserted = 4 Wire Bridge                                                                          | Left of Switch S3                     |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK26         | Blue   | Uninserted       | Allows the user to use an external excitation source                                                                     | Left of Switch S3                     |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK27         | Black  | B                | REFIN(+) to connector:                                                                                                   | Bottom right of J10                   |
|              |        |                  | Pos A: To Connector J10 (BRIDGE)                                                                                         |                                       |
|              |        |                  | Pos B: To Connector J8 (RTD)                                                                                             |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK28         | Black  | B                | REFIN(-) to connector:                                                                                                   | Bottom right of J10                   |
|              |        |                  | Pos A: To Connector J10 (BRIDGE)                                                                                         |                                       |
|              |        |                  | Pos B: To Connector J8 (RTD)                                                                                             |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK29         | White  | Inserted         | Connects CLK pin to GND                                                                                                  | Left of J2                            |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK30         | Black  | Uninserted       | Connects AIN11 to LA_ELECTORDE trace of the A1 connector                                                                 | Below 3.5mm Jack Connection (A1)      |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK31         | Black  | Uninserted       | Connects AIN14 to RA_ELECTORDE trace of the A1 connector                                                                 | Below 3.5mm Jack Connection (A1)      |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK32         | Black  | Uninserted       | Connects AIN15 to DRIVEN_ELECTORDE trace of the A1 connector                                                             | Below 3.5mm Jack Connection (A1)      |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK35         | Red    | Uninserted       | Precision Reference 5.11k ohm Resistor Bypass                                                                            | Right of J8                           |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK36         | Red    | Uninserted       | Headroom Resistor Bypass                                                                                                 | Right J8                              |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK37         | Red    | Uninserted       | Precision Sense 10k ohm Resistor Bypass                                                                                  | Right of J8                           |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| LK45         | Black  | Uninserted       | AVDD/IOVDD short                                                                                                         | Bottom Right of Switch S2             |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| T_AVDD       | Black  | A                | AVDD Supply:                                                                                                             | Below Switch S2                       |
|              |        |                  | Pos A: Directly to supply rail                                                                                           |                                       |
|              |        |                  | Pos B: Through R96 (LK10 and 11 must be inserted) which allows the AD4130-8 to measure it's own AVDD current consumption |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| T_IOVDD      | Black  | A                | IOVDD Supply:                                                                                                            | Below Switch S2                       |
|              |        |                  | Pos A: Directly to supply rail                                                                                           |                                       |
|              |        |                  | Pos B: Through R95 (LK8 and 9 must be inserted) which allows the AD4130-8 to measure it's own IOVDD current consumption  |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| S1           | Switch | +3.3V            | AVDD Voltage connection:                                                                                                 | Top of the Board                      |
|              |        |                  | Pos A: +3.3V from the LDO                                                                                                |                                       |
|              |        |                  | Pos B: +1.8V from the LDO                                                                                                |                                       |
|              |        |                  | Pos C: +1.8V from the LDO                                                                                                |                                       |
|              |        |                  | Pos D: External voltage from J7 terminal block                                                                           |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| S2           | Switch | +3.3V            | IOVDD Voltage connection:                                                                                                | Top of the board                      |
|              |        |                  | Pos A: +3.3V from the LDO                                                                                                |                                       |
|              |        |                  | Pos B: +1.8V from the LDO                                                                                                |                                       |
|              |        |                  | Pos C: +1.8V from the LDO                                                                                                |                                       |
|              |        |                  | Pos D: External voltage from J7 terminal block                                                                           |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+
| S3           | Switch | REF1+/-          | REFIN+/- connection:                                                                                                     | Middle of the board                   |
|              |        |                  | Pos A: REFIN1+/-                                                                                                         |                                       |
|              |        |                  | Pos B: REFIN2+/- (AIN14 and AIN15)                                                                                       |                                       |
|              |        |                  | Pos C: REFOUT and AVSS (Internal Reference needs to be enabled in the ADC Control register)                              |                                       |
+--------------+--------+------------------+--------------------------------------------------------------------------------------------------------------------------+---------------------------------------+

Noise test Demo
---------------

-  **Warning:** The evaluation software and drivers must be installed before connecting the EVAL-AD4130-8WARDZ evaluation board and EVAL-SDP-CK1Z board to the USB port of the PC to ensure the PC correctly recognizes the evaluation system.

If you have not set up the EVAL-AD4130-8WARDZ and controller board previously please go to the :doc:`Quick Start Guide </solutions/reference-designs/ad4130-8/ad4130-8>`

If you have not set up/installed the ACE plugin before please go to :doc:`Install Guide </solutions/reference-designs/ad4130-8/softwareprocedures>`

-  Double click the AD4130-8 Eval Board icon to open the AD4130-8 Eval Board
   view window. The demo wizard will be on the left, either as shown in the
   figure below (Label 1) or already expanded. Expand the wizard by clicking the
   arrow (Label 2).

.. image:: ../images/ad4130_8_ace_noise_test.png
   :align: center
   :width: 600

-  With the wizard expanded, select the noise test button (Label 3).
-  The settings required for the demo are displayed to be viewed prior to writing to the AD4130-8 (Label 4). Click apply (Label 5) to write these settings to the board.
-  The summary is then displayed once the write is complete (Label 1).

.. image:: ../images/ad4130_8_ace_noise_test_summary.png
   :align: center
   :width: 600

-  From here navigate to the chip view by double-clicking the AD4130-8 chip (Label 2).
-  To make further changes to the configuration click on the dark blue block in the chip view (Label 1) or double click the memory map option (Label 2)
-  To begin capturing data double click the Analysis button (Label 3).

.. image:: ../images/ad4130_8_ace_noise_test_chip_view.png
   :align: center
   :width: 600

-  To gather samples, change the Samples Count (Label 1) to the number of
   samples required, then click the Run Once button (Label 2) to acquire the
   samples from the ADC. The image below shows an example of the main window
   after running a noise test.

.. image:: ../images/ad4130_8_ace_noise_test_data.png
   :align: center
   :width: 600

-  For more information on the Waveform window go to the software section :doc:`here </solutions/reference-designs/ad4130-8/softwareprocedures>`

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board is set up to use the external 2.5 V on-board reference
(ADR391). To read samples from the ADC, do the following:

-  The value in the Refin1(+/−) field on the Configuration tab is set to 2.5 V
   by default to use the external 2.5 V on-board reference (ADR391). If a
   different reference is used to the AD4130-8, the Refin1(+/−) field should be
   updated accordingly. (The analysis results are based on the value set in this
   input field.)

   -  Information on the reference choice can be viewed in the :doc:`Reference Options Tab </solutions/reference-designs/ad4130-8/hardwareguide>`

-  When selecting Run Once, a batch of samples is read when clicking the button;
   the batch size is set by the value in the Samples field.

   -  When selecting Run Continuous, the software performs a continuous capture
      from the ADC by clicking the Run Once button. Click the Stop Capture
      button again to stop capturing data.

-  Use the navigation tools within each graph to control the cursor, zooming,
   and panning.

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

--------------

RTD Demo mode
-------------

-  **Warning:** The evaluation software and drivers must be installed before connecting the EVAL-AD4130-8WARDZ evaluation board and EVAL-SDP-CK1Z board to the USB port of the PC to ensure the PC correctly recognizes the evaluation system.

If you have not set up the EVAL-AD4130-8WARDZ and controller board previously please go to the :doc:`Quick Start Guide </solutions/reference-designs/ad4130-8/ad4130-8>`

If you have not set up/installed the ACE plugin before please go to :doc:`Install Guide </solutions/reference-designs/ad4130-8/softwareprocedures>`

.. note::

   The AD4130-8 Ace plugin provides a demo mode for resistance temperature
   detector (RTD) sensors. The RTD demo mode allows the user to get up and
   running with the AD4130-8 and getting data by with just a view clicks of a
   button.

4-wire RTD Demo mode
--------------------

|image1| Links that need to be adjusted for 4-wire RTD demo mode.

+--------------+--------+-------------------------------+---------------------------------------------------+---------------------------------------+
| Link Numbers | Colour | 4-Wire RTD Demo mode Position | Description                                       | Rough Board Location                  |
+==============+========+===============================+===================================================+=======================================+
| LK4          | Black  | Uninserted                    | Disconnects the onboard reference from REFIN1 (+) | Right of J10                          |
+--------------+--------+-------------------------------+---------------------------------------------------+---------------------------------------+
| LK5          | Blue   | Uninserted                    | Disconnects AIN0 from AIN1                        | Right of Thermocouple Connection (A2) |
+--------------+--------+-------------------------------+---------------------------------------------------+---------------------------------------+
| LK6          | White  | Uninserted                    | Disconnects REFIN1 (-) from AVSS                  | Left of Switch S3                     |
+--------------+--------+-------------------------------+---------------------------------------------------+---------------------------------------+
| LK7          | Black  | Uninserted                    | Disconnects the onboard reference from REFIN1 (+) | Right of J10                          |
+--------------+--------+-------------------------------+---------------------------------------------------+---------------------------------------+
| LK35         | Red    | Inserted                      | Precision Reference 5.11k ohm Resistor Bypass     | Right of J8                           |
+--------------+--------+-------------------------------+---------------------------------------------------+---------------------------------------+
| LK36         | Red    | Inserted                      | Headroom Resistor Bypass                          | Right J8                              |
+--------------+--------+-------------------------------+---------------------------------------------------+---------------------------------------+

.. image:: ../images/ad4130_4_wire_rtd.jpg
   :align: center

-  Double click the AD4130-8 Eval Board icon to open the AD4130-8 Eval Board
   view window. The demo wizard will be on the left, either as shown in the
   figure below (Label 1) or already expanded. Expand the wizard by clicking the
   arrow (Label 2).

.. image:: ../images/ad4130_rtd_config_tab.png
   :align: center
   :width: 600

-  With the wizard expanded, select the RTD button (Label 3).
-  In the Configuration Options tab (Label 4), select 4 Wire for Number of Wires, select your RTD type either PT100 or PT1000 and pick which AVDD voltage you have set on the board either 1.8V or 3.3V. This will configure the AD4130-8 registers to the optimum RTD setup.
-  The settings required for the demo are displayed to be viewed prior to writing to the AD4130-8 (Label 5). Click apply (Label 6) to write these settings to the board.
-  The summary is then displayed once the write is complete (Label 1).

.. image:: ../images/ad4130_rtd_config_tab_2.png
   :align: center
   :width: 600

-  From here navigate to the chip view by double-clicking the AD4130-8 chip (Label 2).
-  To make further changes to the configuration click on the dark blue block in the chip view (Label 1) or double click the memory map option (Label 2)
-  To begin capturing data double click the Analysis button (Label 3).

.. image:: ../images/ad4130_8_ace_noise_test_chip_view.png
   :align: center
   :width: 600

-  To gather samples, change the Samples Count (Label 1) to the number of
   samples required, then click the Run Once button (Label 2) to acquire the
   samples from the ADC. The image below shows an example of the main window
   after running a RTD demo mode.

.. image:: ../images/ad4130_rtd_results_tab.png
   :align: center
   :width: 600

-  To display the waveform data in degrees Celsius pick DegC in y-axis units dropdown (Label 3)
-  For more information on the Waveform window go to the software section :doc:`here </solutions/reference-designs/ad4130-8/softwareprocedures>`

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board is set up to use the external 2.044 V in the RTD demo
mode(when AVDD is set to 3.3V in Configuration Options tab or it is 1.022V if
1.8V is selected) on-board reference (From the 5.11k ohm precision resistor). To
read samples from the ADC, do the following:

-  The value in the Refin1(+/−) field on the Configuration tab is set to 2.5 V
   by default to use the external 2.5 V on-board reference (ADR391). If a
   different reference is used to the AD4130-8, the Refin1(+/−) field should be
   updated accordingly (i.e. 2.044 V for AVDD set to 3.3 V and 1.022 V for AVDD
   set to 1.8 V). (The analysis results are based on the value set in this input
   field.)

   -  Information on the reference choice can be viewed in the :doc:`Reference Options Tab </solutions/reference-designs/ad4130-8/hardwareguide>`

-  When selecting Run Once, a batch of samples is read when clicking the button;
   the batch size is set by the value in the Samples field.

   -  When selecting Run Continuous, the software performs a continuous capture
      from the ADC by clicking the Run Once button. Click the Stop Capture
      button again to stop capturing data.

-  Use the navigation tools within each graph to control the cursor, zooming,
   and panning.

Reading Samples from the ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the waveforms resulting from the gathered samples in the Analysis tab. The
waveform graph shows each successive sample of the ADC output (input referred).
The indicators beside this graph show the channels converting. The navigation
tools allow you to control the cursor, zooming, and panning. You can also
display the conversions as temperature (degrees Celsius) or codes. Below the
graph are parameters, such as peak-to-peak noise and rms noise, in the Results
section for the current batch of samples. If there are several enabled analog
input channels, you can select each enabled channel and the conversions through
the analyzed channel using the Results Tab. To save the data into an Excel file,
select the Export button from the Results Tab. A Save dialog box is displayed,
prompting you to save the data to an appropriate folder location.

:doc:`Return to Software Guide </solutions/reference-designs/ad4130-8/softwareprocedures>`

.. |image1| image:: ../images/eval-ad4130-8wardz_block_diagram_with_4_wire_rtd_without_sdp_k1.png
