.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ltpa-rl2000

.. _eval-ltpa-rl2000:

EVAL-LTPA-RL2000 User Guide
===========================

.. note::

   We are in the process of migrating our documentation to GitHub Pages.

Overview
--------

The :adi:`EVAL-LTPA-RL2000` is a portable, USB efficiency meter based on the
:adi:`LTpowerAnalyzer® <eval-ltpa-kit>` that allows you to plot DC efficiency
and power loss of a DC-DC power supply, across multiple values of load current −
a crucial step in evaluating design performance. This instrument can be used on
its own, and is not dependent on the :adi:`ADALM2000` and the main board for
operation.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/eval-ltpa-rl2000_angle-evaluation-board.jpg
   :width: 400px

The RL2000 has two ±125 V DC voltmeters for measuring the input and output
voltages, a 30 A DC current meter with a programmable 0 V to 5 V voltage drop
for the power supply input, and a 30 A (150 W max.) DC current load for the
power supply output. Internal temperature sensing and a rear-mounted cooling fan
provide thermal protection during high-power applications.

Specifications
--------------

.. list-table::
   :header-rows: 1

   * - Parameter
     - Min
     - Max
     - Units
   * - **Voltmeters**
     -
     -
     -
   * - Input DC Voltage Range
     -
     - ±125
     - V
   * - Resolution
     -
     - 1
     - mV
   * - Input Impedance
     -
     - 2
     - MΩ
   * - Accuracy\*
     -
     - 0.01 + 0.01
     - %
   * - **Current Meter**
     -
     -
     -
   * - Input DC Current Range
     - 10 x 10\ :sup:`-6`
     - 30
     - A
   * - Resolution per Range
     -
     -
     -
   * - • 10 μA
     -
     - 10
     - nA
   * - • 100 μA
     -
     - 10
     - nA
   * - • 1 mA
     -
     - 100
     - nA
   * - • 10 mA
     -
     - 1
     - μA
   * - • 100 mA
     -
     - 10
     - μA
   * - • 1 A
     -
     - 100
     - μA
   * - • 10 A
     -
     - 1
     - mA
   * - • 30 A
     -
     - 1
     - mA
   * - Accuracy\*
     -
     - 0.025 + 0.01
     - %
   * - Servo Voltage
     -
     - 0.01 + 0.01
     - %
   * - Shutdown Temperature
     -
     - 70
     - °C
   * - **Current Load**
     -
     -
     -
   * - DC Load Current Range
     - 10 x 10\ :sup:`-6`
     - 30
     - A
   * - Resolution per Range
     -
     -
     -
   * - • 10 μA
     -
     - 10
     - nA
   * - • 100 μA
     -
     - 10
     - nA
   * - • 1 mA
     -
     - 100
     - nA
   * - • 10 mA
     -
     - 1
     - μA
   * - • 100 mA
     -
     - 10
     - μA
   * - • 1 A
     -
     - 100
     - μA
   * - • 10 A
     -
     - 1
     - mA
   * - • 30 A
     -
     - 1
     - mA
   * - Accuracy\*
     -
     - 0.025 + 0.01
     - %
   * - Load Voltage
     -
     - 75
     - V
   * - Load Power
     -
     - 150
     - W
   * - Shutdown Temperature
     -
     - 70
     - °C

*\*Accuracy specifications are given in: ± (% of reading + % of range).*

About Efficiency Measurements
-----------------------------

Efficiency is calculated as the ratio of its output power to its input power.
Simply put, it is a measure of how much of the input power can converted into a
useful output and supplied to the load. In power supply designs, this is a
critical parameter to evaluate as excessive power loss in the design will
increase energy consumption and produce unwanted heat dissipation. Low
efficiency levels can result in shorter battery life (for battery-powered
systems) and higher board temperatures.

To measure efficiency, you will need to first determine the input power and
output power, which can be derived from measuring their respective voltages and
currents. However, the efficiency also varies depending on the load current –
for example, a converter might achieve ~92% efficiency at a 10 A load but be
significantly less efficiency when operating at light loads. Therefore, it is
essential to plot the efficiency across multiple values of load current to get a
clear picture of its performance.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/32._rl2000.png
   :width: 400px

The diagram below shows a generic test setup for measuring efficiency. In this
example, a programmable current load is used to sweep the output current of the
device under test (DUT), while an ammeter is used to measure the input current.
Two voltmeters monitor the input and output voltages; the input power, output
power, efficiency, and power loss can then be calculated from the measurements.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/31._rl2000.png
   :width: 400px

Hardware Interface
------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/eval-ltpa-rl2000_front-evaluation-board.jpg
   :width: 500px

USB-C Connector
~~~~~~~~~~~~~~~

The USB-C interface is used to connect to the host PC for power and data
communication. The LTpowerAnalyzer® software will automatically detect the
compensation probe and display its control interface window during start-up.

Terminals
~~~~~~~~~

The EVAL-LTPA-RL2000 has four pairs of terminals for interfacing the meter with
a DUT:

.. list-table::
   :header-rows: 1

   * - Terminal Pair
     - Function
   * - Current 1
     - Current Meter (±) Terminals. Used to measure the input supply current of
       the DUT.
   * - Voltage 1
     - Voltmeter 1 (±) Terminals. Used to measure the input supply voltage of
       the DUT.
   * - Voltage 2
     - Voltmeter 2 (±) Terminals. Used to measure the output voltage of the DUT.
   * - Current 2
     - Current Load (±) Terminals. Used to as a programmable load for the DUT.

Hardware Setup
--------------

Setup Requirements
~~~~~~~~~~~~~~~~~~

- EVAL-LTPA-RL2000 (LTpowerAnalyzer® RL2000 Efficiency Meter)
- Device Under Test (e.g., LT8642S Demo Board)
- DC Power Supply

Refer to the diagram below for the typical hardware setup for the RL2000
efficiency meter. It is recommended to use short cables to connect the RL2000 to
the DUT to minimize parasitics.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/33._rl2000.png
   :width: 400px

**Step-by-Step Procedure:**

STEP #1: Connect the Current 1 terminals between the (+) terminal of the input
power source and the (+) input of the DUT. This is used to monitor the input
current of the DUT.

STEP #2: Connect the Voltage 1 terminals across the (+) and (-) input pins of
DUT. This is used to measure the voltage at the input.

STEP #3: Connect the Voltage 2 terminals across the (+) and (-) output pins of
DUT. This is used to measure the voltage at the output.

STEP #4: Connect the Current 2 terminals across the (+) and (-) output pins of
DUT. This will serve as the programmable load for sweeping the output current.

STEP #5: Connect a USB-C cable from the your PC to the USB port on the RL2000 to
complete the setup.

Example Setup Using the LT8642S Demo Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A hardware setup of the RL2000 is shown below for reference. This example uses
the LT8642S demo board included with the EVAL-LTPA-KIT as the device under test.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/37._rl2000.png
   :width: 400px

Typical Applications
--------------------

Example applications of the RL2000 efficiency meter are shown below:

1. Basic Setup.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/25._rl2000.png
   :width: 800px

2. Basic Setup with Servo Voltage. This example demonstrates how the input
   voltage (V1) remains relatively stable when the servo voltage is enabled.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/26._rl2000.png
   :width: 800px

3. Basic Setup with Micro-Power DUT. When dealing with low power DUTs, the
   leakage currents flowing into Voltage 1 and Voltage 2 can skew the current
   measurements considerably. This example shows how the RL2000 can compensate
   for this in the software by calculating the leakage currents and removing
   them from the measured currents, as well as adding settling time to allow the
   load current time to stabilize (refer to RL2000 Control Panel).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/34._rl2000.png
   :width: 800px

4. Basic Setup with Negative Output Voltages. This example shows that the RL2000
   is also capable of measuring negative voltages.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/30._rl2000.png
   :width: 800px

5. Setup for DUTs with Multiple Power Inputs. This example shows how to use two
   RL2000s to measure the efficiency of a DUT with two input supplies. In this
   test case, the output power measurement of the top RL2000 is disabled in the
   software (refer to RL2000 Control Panel).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/28._rl2000.png
   :width: 800px

6. Setup for Higher Load Currents (>30 A). This example setup can be used to
   evaluate the efficiency at load currents up to 60 A by sharing the load
   current between two RL2000s connected in parallel. In this test case, the
   input power measurement of the top RL2000 is disabled in the software (refer
   to RL2000 Control Panel).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/29._rl2000.png
   :width: 800px

7. Setup for Low Output Voltages. At low output voltages, the current load may
   no longer produce an accurate load current, depending on its setting. For
   this test case, an easy way to compensate for this is to use a second supply
   to bias the output with a negative voltage.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/35._rl2000.png
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/36._rl2000.png
   :width: 600px

Making an Efficiency Plot Measurement
-------------------------------------

After setting-up the hardware shown in the Hardware Setup for DC Sweep
Measurement, you may now start making efficiency measurements through the
LTpowerAnalyzer® software.

This section provides a step-by-step guide on how to use the DC Sweep feature of
the LTpowerAnalyzer® software.

**1. Launch the LTpowerAnalyzer® software.**

Check the status bar at the bottom of the main window. It should indicate that
an RL2000 efficiency meter is connected with no errors. Please note that in this
example, we are not using the M2K, the LTpowerAnalyzer main board, or any
current probe since the DC sweep is done entirely by the RL2000.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/14._rl2000.png
   :width: 800px

**2. Run a DC Sweep.**

Step-by-Step Procedure:

STEP #1: Click on the DC Sweep tab.

STEP #2: Select the meter that will be used to sweep the load current. If there
are multiple RL2000s connected, the Blink Led function can be used to identify
which one is currently selected.

STEP #3: Set the start and end values for the sweep.

STEP #4: Select the sweep rate (i.e., either Logarithmic or Linear).

STEP #5: Set the number of data points per decade (for a logarithmic sweep), or
the number of intervals (for a linear sweep).

STEP #6: Click on the Run button the start the load current sweep and efficiency
measurement.

STEP #7: When the load current sweep is complete, select the measurement data
(e.g., efficiency, power loss, etc.) to plot on the Y1 and Y2 axes. Adjust the
graph settings as needed.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/17._rl2000.png
   :width: 1000px

**3. Rename the Measurements.**

Step-by-Step Procedure:

STEP #1: Click on the DATA tab on the right.

STEP #2: Click on the Name value you want to change. After typing the desired
waveform name, press the ENTER or RETURN key.

The legend will automatically be updated to the new name.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/10._rl2000.png
   :width: 800px

**4. Edit The Title.**

Step-by-Step Procedure:

STEP #1: Right-Click on the graph and select Edit Title.

STEP #2: Type in the new title.

STEP #3: Click the OK button.

The plot title will be automatically updated to the new title.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/18._rl2000.png
   :width: 800px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/19._rl2000.png
   :width: 800px

**5. Add a Text Annotation.**

Step-by-Step Procedure:

STEP #1: Right-Click on the graph and select Add Text Annotation.

STEP #2: Type in the text annotations.

STEP #3: Click the OK button.

Next select the new annotation by placing the cursor over it and then left
click. The annotation can then be resized and moved as needed.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/20._rl2000.png
   :width: 800px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/21._rl2000.png
   :width: 800px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/22._rl2000.png
   :width: 800px

**6. Saving Results.**

Step-by-Step Procedure:

STEP #1: Select the Save option in the File tab: File > Save

STEP #2: Enter the file name of the saved data.

STEP #3: Click Save. A Data File type will save the setup and the data

Note that the Setup File type will only save the setup.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/23._rl2000.png
   :width: 800px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/24._rl2000.png
   :width: 800px

Software Interface
------------------

RL2000 Control Panel
~~~~~~~~~~~~~~~~~~~~

The RL2000 control panel automatically appears as a separate window in the
LTpowerAnalyzer® software when an efficiency meter is connected.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/1._rl2000.png
   :width: 400px

.. list-table::
   :header-rows: 1

   * - 1. Power Loss and Efficiency Measurements
     -
   * - Input Power
     - Total input power of the device under test.
   * - Output Power
     - Total output power of the device under test.
   * - Power Loss
     - Total power loss of the device under test.
   * - Efficiency
     - Efficiency of the device under test.

.. list-table::
   :header-rows: 1

   * - 2. Meter Selection
     -
   * - Select Meter
     - Selects the meter being actively controlled by the interface. Meters are
       numbered by order of connection.
   * - Blink Led
     - Blinks the front panel LED. Used to identify the selected meter when
       multiple RL2000s are connected.
   * - Reset
     - Returns all meter settings to their default values.
   * - Info
     - Displays information about the meter (e.g., hardware and firmware
       versions, serial number, serial port, etc.).

.. list-table::
   :header-rows: 1

   * - 3. Meter Readings
     -
   * - Input Voltage
     - DC input voltage of the device under test. Measured across the Voltage 1
       terminals.
   * - Input Current
     - DC input current of the device under test. Measured through the Current 1
       terminals.
   * - Input Power
     - DC input power of the device under test. Calculated using the Voltage 1
       and Current 1 measurements.
   * - Efficiency
     - Input power measurement enable. Adds the input power reading to the total
       used in the power loss and efficiency calculations.
   * - VM Comp
     - Voltmeter current compensation enable. Applies an offset to the input
       current reading to compensate for the leakage current through the Voltage
       1 terminals. Can be used to improve measurement accuracy at low current
       values.

.. list-table::

   * - Output Voltage
     - DC output voltage of the device under test. Measured across the Voltage 2
       terminals.
   * - Output Current
     - DC output current of the device under test. Measured through the Current
       2 terminals.
   * - Output Power
     - DC output power of the device under test. Calculated using the Voltage 2
       and Current 2 measurements.
   * - Efficiency
     - Output power measurement enable. Adds the output power reading to the
       total used in the power loss and efficiency calculations.
   * - VM Comp
     - Voltmeter current compensation enable. Applies an offset to the input
       current reading to compensate for the leakage current through the Voltage
       2 terminals. Can be used to improve measurement accuracy at low current
       values.

.. list-table::
   :header-rows: 1

   * - 4. Meter Settings
     -
   * - Sample Rate
     - Selects the measurement speed of the internal converters. Higher speed
       settings are faster, but result in a noisier measurement.
   * - Settling Time
     - Sets the amount of time to wait for the load current to settle before
       performing a measurement.

.. list-table::

   * - Servo Voltage
     - Sets the amount of voltage drop across the input current meter (Current
       1).
   * - Enable
     - Servo voltage enable. Check this box to activate the servo voltage
       function for the input current meter (Current 1).

.. list-table::

   * - Load Current
     - Sets the amount of output current drawn by the current load (Current 2).
   * - Zero
     - Resets the load current setting to zero amperes.
   * - Enable
     - Current load enable. Check this box to activate the current load (Current
       2).
   * - Share
     - Current share enable. Check this box to automatically divide the load
       current equally among all connected meters.

.. list-table::
   :header-rows: 1

   * - 5. Status Bar
     -
   * - Error
     - Error code of the meter if a problem occurs during operation. Displays No
       Error if the meter is functioning properly.
   * - Temperature
     - Internal temperature of the current meter and load. When either reading
       reaches at least 32°C, the cooling fan will automatically turn on. At
       70°C, the current meter and load will shutdown.

DC Sweep Measurement and Graph Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Measurement Setup is on the left side of the DC Sweep window. Click on the
GRAPH tab on the right to bring up the graph setup.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-rl2000/13._rl2000.png
   :width: 800px

.. list-table::
   :header-rows: 1

   * - DC Sweep Measurement Setup
     -
   * - **RL2000**
     -
   * - Select Meter
     - Selects the meter that will be used to sweep the load current. Meters are
       numbered by order of connection.
   * - Blink Led
     - Blinks the front panel LED. Used to identify the selected meter when
       multiple RL2000s are connected.
   * - Reset
     - Returns all meter settings to their default values.
   * - Info
     - Displays information about the meter (e.g., hardware and firmware
       versions, serial number, serial port, etc.).

.. list-table::

   * - **Sweep**
     -
   * - Start Current
     - Sets the initial load current value in the DC sweep (1 μA to 30 A).
   * - End Current
     - Sets the final load current value in the DC sweep (1 μA to 30 A).
   * - Points Per Decade/Total # Intervals
     - Sets either the number of points per decade for logarithmic sweeps, or
       the number of intervals between the start current and end current for
       linear sweeps (1 to 200).
   * - Log
     - Logarithmic sweep. Select this option to sweep the load current values in
       a logarithmic scale.
   * - Linear
     - Linear sweep. Select this option to sweep the load current values in a
       linear scale.
   * - Run/Stop
     - Triggers the start of the DC sweep. A sweep in progress can be stopped by
       clicking the button again.
   * - Append
     - Append data. Check this box to plot the measurement data of the next
       sweep on top of the existing graph. When left unchecked, all previous
       graphs and data will be erased at the start of the next sweep.

.. list-table::
   :header-rows: 1

   * - DC Sweep Graph Setup
     -
   * - **X Axis**
     -
   * - Minimum
     - 1 μA to 100 A
   * - Maximum
     - 1 μA to 100 A
   * - AutoScale
     - The X Axis data will be automatically scaled.
   * - Log
     - The X Axis data will be plotted using a log-10 scale.
   * - Increments
     - 1 to 20 divisions

.. list-table::

   * - **Y1 Axis**
     -
   * - Data
     - The parameter that will be plotted on the Y1 axis.\*
   * - Minimum
     - -1000 to 990 units
   * - Maximum
     - -990 to 1000 units
   * - AutoScale
     - The Y1 Axis data will be automatically scaled.
   * - Log
     - The Y1 Axis data will be plotted using a log-10 scale.
   * - Increments
     - 1 to 20 divisions

.. list-table::

   * - **Y2 Axis**
     -
   * - Data
     - The parameter that will be plotted on the Y2 axis.\*
   * - Minimum
     - -1000 to 990 units
   * - Maximum
     - -990 to 1000 units
   * - AutoScale
     - The Y2 Axis data will be automatically scaled.
   * - Log
     - The Y2 Axis data will be plotted using a log-10 scale.
   * - Increments
     - 1 to 20 divisions

*\*The parameters that can be plotted on the Y1 and Y2 axes are: Input Voltage
(V1), Input Current (I1), Output Voltage (V2), Output Current (I2), Efficiency,
Input Power (Power1), Output Power (Power2), Power Loss, and Load Current
(Iload).*

Useful Links
------------

- :dokuwiki:`EVAL-LTPA-KIT Overview </resources/eval/user-guides/eval-ltpa-kit>`
- :dokuwiki:`EVAL-LTPA-KIT Hardware Setup Guide </resources/eval/user-guides/eval-ltpa-kit/hardware>`
- :dokuwiki:`EVAL-LTPA-KIT Software Setup Guide </resources/eval/user-guides/eval-ltpa-kit/software>`

Support
-------

For questions and more information, please visit the Analog Devices
:ez:`EngineerZone <reference-designs/ltpoweranalyzer>`.
