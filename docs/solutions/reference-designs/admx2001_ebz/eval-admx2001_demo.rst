EVAL-ADMX2001 LCR Meter Demo/Evaluation Setup
=============================================

.. note::

   This page applies to hardware revision B and C, and firmware versions 1.3.1,
   1.3.2, and 1.3.3. It may not apply to past or future versions. For firmware
   update instructions, see :ref:`Firmware Updates <eval-admx2001 firmware-updates>`.

The EVAL-ADMX2001 LCR Meter Demo is an evaluation system that is comprised of
both the ADMX2001B and the EVAL-ADMX2001EBZ boards.

The **ADMX2001B** is a high-performance, precision impedance analyzer module.

-  Highly compact, 1.5 inch by 2.5 inch System-on-Module (SOM)
-  Resistance measurements at DC or impedance measurements from 0.2 Hz to 10 MHz
-  18-bit acquisition channels
-  Operates from a single 3.3V supply
-  Flexible UART and SPI interfaces
-  18 display mode formats in SI units

The **EVAL-ADMX2001EBZ** is an easy-to-use evaluation and development breakout
board that enables convenient access to the functionality of the ADMX2001B
Precision Impedance Analyzer Measurement Module.

-  BNC connectors can interface to common LCR meter test probes and fixtures
-  UART interface can be used with USB-to-UART cables to interface to host PC
-  Trigger and clock synchronization signals are available through SMA
   connectors that simplify the connection to standard test equipment
-  Arduino-style headers allow the user to develop embedded code with boards
   like the SDP-K1
-  Power jack accepts various input voltages from ac/dc power adapters that can
   supply +5V to +12V

EVAL-ADMX2001EBZ Evaluation Kit Contents
----------------------------------------

-  **EVAL-ADMX2001EBZ** board
-  UART to USB cable (TTL-232R-RPI)
-  Universal power adapter with 9VDC output
-  LCR meter test clips

Additional Equipment Required
-----------------------------

-  **ADMX2001B** High-Performance Precision Impedance Analyzer Measurement
   Module

.. important::

   It is critical to purchase both the ADMX2001B High-Performance Precision
   Impedance Analyzer Measurement Module and the EVAL-ADMX2001EBZ LCR Meter
   Demonstration Board. These are sold separately.

Optional Equipment
------------------

-  LCR meter accessories. Available from various test and measurement
   manufacturers, for example:

   -  `Keysight's Impedance Measurement Accessories
      <https://www.keysight.com/en/pc-1000002552%3Aepsg%3Apgr/lcr-meter-impedance-measurement-product-accessories>`_
   -  `B+K Precision TL89S1 SMD Test Fixture
      <https://www.digikey.com/en/products/detail/b-k-precision/TL89S1/7915183>`_
   -  `B+K Precision TL89F1 4-Terminal Test Fixture for leaded components
      <https://www.digikey.com/en/products/detail/b-k-precision/TL89F2/6618989>`_

-  Calibration Standards and Accessories

   -  `IET Labs <https://www.ietlabs.com/>`_ (former General Radio products)
   -  `Keysight 42090A Open Termination
      <https://www.keysight.com/en/pd-1000003831%3Aepsg%3Apro-pn-42090A/open-termination-4-terminal-pair>`_
   -  `Keysight 42091A Short Termination
      <https://www.keysight.com/en/pd-1000003830%3Aepsg%3Apro-pn-42091A/short-termination-4-terminal-pair>`_
   -  `Keysight 42030A Four Terminal Pair Standard Resistor Set
      <https://www.keysight.com/en/pd-1000003832%3Aepsg%3Apro-pn-42030A/four-terminal-pair-standard-resistor-set>`_
   -  `Keysight 16380A Standard Air Capacitor Set (1pF to 1000pF)
      <https://www.keysight.com/en/pd-1000003834%3Aepsg%3Apro-pn-16380A/standard-air-capacitor-set-1pf-to-1000pf>`_
   -  `Keysight 16380C Capacitance Standard Set (0.01uF to 10uF)
      <https://www.keysight.com/en/pd-1000003833%3Aepsg%3Apro-pn-16380C/capacitance-standard-set-001uf-to-10uf>`_

-  LCR Meter for verification and calibration transfer

   -  `Keysight E4980A Precision LCR Meter
      <https://www.keysight.com/en/pd-715495-pn-E4980A/precision-lcr-meter-20-hz-to-2-mhz>`_

Quick Start
~~~~~~~~~~~

There are five simple steps to start evaluating the ADMX2001:

-  Driver Installation
-  Terminal Emulator Installation
-  Basic hardware setup
-  Open a session through the terminal emulator (e.g. TeraTerm)
-  Perform basic measurements

These steps are explained in detail in the following sections.

1. Driver Installation
----------------------

.. note::

   The default communication interface to the EVAL-ADMX2001EBZ is via its UART
   port. When using the UART to USB cable included with the evaluation board
   (TTL-232R-RPI), FTDI's Virtual COM Port (VCP) drivers must be downloaded from
   their website located at https://www.ftdichip.com/Drivers/VCP.htm

**Installation steps:**

-  Download the driver **setup executable** for the host OS version from
   https://www.ftdichip.com/Drivers/VCP.htm

   -  Note: for detailed instructions, visit
      https://www.ftdichip.com/Support/Documents/InstallGuides.htm

-  Unzip the file and run the setup executable
-  **Connect the USB to UART cable to the PC**
-  Open the Device Manager
-  In the Device Manager window, verify that the USB Serial Port is displayed
   under “Ports (COM & LPT)” and that a serial port identifier has been assigned
   as shown below:

.. image:: images/dev_mgr_vcp_installed.png
   :align: center
   :width: 600

2. Terminal Emulator Installation
---------------------------------

To communicate with ADMX2001B via its command-line interface and UART, a
terminal emulator like TeraTerm is recommended. Download TeraTerm from the
official Github Releases page:

.. admonition:: Download
   :class: download

   \ https://github.com/TeraTermProject/teraterm/releases\

Download and run the latest stable release. Follow the on-screen instructions.

Alternatives like PuTTY can also be used, but some users have had issues with
PuTTY where the terminal window does not open. Additionally, some terminals do
not support the ANSI Escape Codes which manipulate the cursor position and text
color. If the ANSI Escape Codes are not supported, the terminal will render them
as boxes. TeraTerm supports these characters.

3. Basic Hardware Setup
-----------------------

The following figure shows the basic connections required for evaluating the
EVAL-ADMX2001.

.. figure:: images/eval-admx2001ebz_basic_connections_labeled.png
   :align: center
   :width: 600

-  Insert the ADMX2001B module into the EVAL-ADMX2001EBZ board in the location
   shown above. The connectors are keyed, so they can only be inserted in the
   orientation shown
-  Set the load select switches to OPEN and GND, as shown below. This is
   required for the self-test to pass, indicated by the red/green LED on the
   underside of the ADMX2001B module

.. figure:: images/open_load.png
   :align: center
   :width: 450

-  Connect the power adapter to the power jack and to the AC outlet
-  Verify that the self-test light is green (light is on the bottom of the
   board, but is visible if viewed from the side where the oscillator and FPGA
   are mounted)
-  Connect the UART to USB cable to the UART terminals TX (orange)-->TX, RX
   (yellow)-->RX and GND (black)-->GND:

.. figure:: images/uart_to_usb.jpg
   :align: center
   :width: 450

-  Ensure that the CLK_SEL jumper cap (located under the UART header) is set to
   INT (internal clock)
-  Set the load select switches to DUT and GND, as shown below:

.. figure:: images/bnc_load.png
   :align: center
   :width: 450

-  Use the test leads to connect to the device under test (DUT):

.. figure:: images/photo_setup_labeled.jpg
   :align: center
   :width: 600

The two BNC connectors from the red leads go to the HCUR/HPOT ports, the two BNC
connectors from the black leads go to the LPOT/LCUR ports.

.. important::

   Inspect the BNC connectors on the test clips. The housing can become
   partially unscrewed, allowing the conductor to be pushed back inside and
   preventing it from making good contact. Additionally, when using the clips in
   the "open" configuration, each clip should clamp on its own small wire scrap
   to ensure both sides of the clip are electrically connected.

An example of an unscrewed housing of a test clip:

.. figure:: images/cal_connections_5.jpg
   :align: center
   :width: 600

An example of how to use the wire scrap in each of the test clips, when using
them in the open configuration:

.. figure:: images/open_config_test_clips_2.png
   :align: center
   :width: 600


Self-Test Functionality
~~~~~~~~~~~~~~~~~~~~~~~

When the ADMX2001B powers on, it automatically performs a self-test. The
bi-color LED on the underside of the board will turn green if the board boots
and passes the self-test, or half-green half-red if the self-test fails. It will
turn red if there is a major issue preventing it from booting such as a power
issue, missing encryption key, missing firmware or something else. In order to
pass the analog component of the self-test, the switches S1 and S2 must be set
to OPEN and GND. Alternatively, if S1 and S2 are in the DUT and GND position,
the test leads must be connected in the 'open' configuration to pass the
self-test. The board will still attempt to function without passing the
self-test.

The status of the last self-test can be seen by running the command
``selftest``. Using ``selftest run`` will rerun the self-test. By default, the
self-test only runs on boot.

4. Opening a Session via TeraTerm
---------------------------------

After installing TeraTerm, open the program and choose Serial connection. Select
the COM port identified earlier in Device Manager. Click OK. Then choose the
dropdown labeled Setup, click Serial port, and ensure that the COM port is set,
Speed=115200, Data=8 bits, Parity=none, Stop bits=1 bits, Flow control=none.
Click New setting. Optionally, choose Setup->Save setup. Save the file to the
default directory. Now, when launching TeraTerm, it will automatically try to
connect with the saved settings.

Make sure the hardware is properly installed and that power is available to the
board via the 12V power adapter. TeraTerm should now be connected to the board.
To check:

-  Press ENTER to display the ADMX2001> prompt
-  Type ``*idn`` and press ENTER to display the firmware version
-  Type ``help`` and press ENTER to see a list of commands supported by
   ADMX2001B.

Please note that closing the TeraTerm window does not reset the ADMX2001B
settings from the last session.

5. Performing Basic Measurements
--------------------------------

Upon opening a session with TeraTerm, the ADMX2001B is ready to perform
impedance measurements.

.. important::

   The measurements reported by the module will not be accurate unless it has
   been calibrated. For detailed instructions on how to calibrate the module,
   please refer to the `Calibration Procedure
   <https://wiki.analog.com/eval-admx2001ebz>`_ section in this user guide.

By default, the module is set to perform single-point impedance measurements in
rectangular coordinates with a 1V pk signal (magnitude = 1) at 1kHz, and no DC
offset. To initiate a measurement type the ``z`` command at the prompt and press
ENTER.

Measurement settings are not always in their base SI form. Frequency is in kHz,
delays are in milliseconds. The signal magnitude sets the Vpk value. The
peak-to-peak value is twice the signal magnitude, centered around the offset
voltage. The DC offset is in volts.

The AC magnitude can be configured anywhere between 0.15V pk and 2.25V pk, but
the actual magnitude across the DUT will be be dependent on the DUT impedance,
due to the 100Ω source resistance; see `Selecting a Measurement Range`_ for
details.

.. tip::

   The order in which the settings commands are entered is not important.

Example
~~~~~~~

Perform a capacitance measurement in parallel with an equivalent resistor
(Cp-Rp) at 100kHz with a 1V amplitude (2V pk-pk) sine. Return 5 readings, where
each is an average of 10 samples.

::

   ADMX2001> frequency 100
   frequency = 100.0000kHz
   ADMX2001> display 9
   Measurement model: 9 - Capacitance and equivalent parallel resistance (Cp,Rp)
   ADMX2001> magnitude 1
   magnitude = 1.0000
   ADMX2001> average 10
   average = 10
   ADMX2001> count 5
   sampleCount = 5
   ADMX2001> z
   0,5.677640e-13,8.062763e+07
   1,5.668012e-13,8.305672e+07
   2,5.675237e-13,8.208995e+07
   3,5.673763e-13,8.276912e+07
   4,5.683635e-13,8.463327e+07
   ADMX2001>

.. note::

   By default, auto-range is selected. To disable the auto-ranging function, use
   the ``setgain <ch> <setting>`` command to select a specific measurement range
   for the voltage (ch0) or current (ch1) measurement channels.

Using the Help Functionality in the Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``help`` command will display all the commands available to the user from
the command-line interface (CLI). To get help for any command, simply type

.. figure:: images/help_command_printout_teraterm.png
   :align: center
   :width: 1000

::

   ADMX2001>help <command>

For example, to get help with how to select different measurement display
formats, type

::

   ADMX2001>help display

Which should show a similar screen to the picture shown below

.. figure:: images/help_display_teraterm.png
   :align: center
   :width: 1000

Useful Hints
~~~~~~~~~~~~

Measurement Display Modes
-------------------------

The ADMX2001B returns a result in one of 18 different display modes, shown
below. The result is always reported in the base SI unit. For instance,
``display mode 0`` (Cs, Rs) returns the series capacitance in Farads, and the
series resistance in Ohms.

+---------------------+--------------------------------------------------------+--------+------------------------+
| Display Mode Number | Mode Name                                              | Form   | SI Unit                |
+=====================+========================================================+========+========================+
| 0                   | Equivalent series capacitance and resistance           | Cs, Rs | Farads, Ohms           |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 1                   | Equivalent series capacitance and dissipation factor   | Cs, D  | Farads, Dimensionless  |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 2                   | Equivalent series capacitance and quality factor       | Cs, Q  | Farads, Dimensionless  |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 3                   | Inductance and equivalent series resistance            | Ls, Rs | Henries, Ohms          |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 4                   | Equivalent series inductance and dissipation factor    | Ls, D  | Henries, Dimensionless |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 5                   | Equivalent series inductance and quality factor        | Ls, Q  | Henries, Dimensionless |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 6                   | Impedance in rectangular coordinates (default)         | R, X   | Ohms, Ohms             |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 7                   | Impedance in magnitude and phase in degrees            | Z, deg | Ohms, Degrees          |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 8                   | Impedance in magnitude and phase in radians            | Z, rad | Ohms, Radians          |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 9                   | Capacitance and equivalent parallel resistance         | Cp, Rp | Farads, Ohms           |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 10                  | Equivalent parallel capacitance and dissipation factor | Cp, D  | Farads, Dimensionless  |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 11                  | Equivalent parallel capacitance and quality factor     | Cp, Q  | Farads, Dimensionless  |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 12                  | Inductance and equivalent parallel resistance          | Lp, Rp | Henries, Ohms          |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 13                  | Equivalent parallel inductance and dissipation factor  | Lp, D  | Henries, Dimensionless |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 14                  | Equivalent parallel inductance and quality factor      | Lp, Q  | Henries, Dimensionless |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 15                  | Admittance in rectangular coordinates                  | G, B   | Siemens, Siemens       |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 16                  | Admittance in magnitude and phase in degrees           | Y, deg | Siemens, Degrees       |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 17                  | Admittance in magnitude and phase in radians           | Y, rad | Siemens, Radians       |
+---------------------+--------------------------------------------------------+--------+------------------------+
| 18                  | Off                                                    | None   | None                   |
+---------------------+--------------------------------------------------------+--------+------------------------+

Selecting a Measurement Range
-----------------------------

By default, the ADMX2001B is in auto-ranging mode, which will optimize the
measurement gain of the voltage and current measurement channels, depending on
the frequency and magnitude of the test signal.

.. note::

   The auto-ranging algorithm will only be applied to the conditions of the
   first measurement. When performing frequency sweeps, the impedance of the
   device under test will change and could fall outside of the measurement range
   selected by the initial measurement conditions.


   Additionally, the DC offset control is disabled when using the autorange.
   Manual gain setting must be employed when using the DC offset. The DC offset
   will be automatically set to -0.25V to allow the saturation detection to
   perform as expected when autoranging.

In some cases, the user may want to select a specific measurement range. The
measurement range is mostly affected by the transimpedance of channel 1 and the
test signal magnitude. It is recommended to select the transimpedance value that
is smaller than the expected value of the impedance under test, but larger than
the next transimpedance selection.

For example, if the DUT's expected impedance value is 2kΩ, enter the following
in the command line prompt:

::

   ADMX2001> setgain ch0 0
     voltGain = 0
   ADMX2001> setgain ch1 1
     currGain = 1

The command ``setgain ch1`` modifies the current measurement range of L_CUR
(channel 1). This is done by setting different values for (R\ :sub:`TIA`) in the
feedback loop of the transimpedance amplifier A2. The command ``setgain ch1 1``
sets the transimpedance to 499Ω, appropriate for the 1kΩ-10kΩ range. It is not
recommended to use the 10kΩ-100kΩ range for a 2kΩ load since this could exceed
the current input channel measurement capabilities and return incorrect
readings.

The ADMX2001B uses a balancing bridge architecture. A 100 ohm series resistor Rs
protects the source channel. When calculating the current through a DUT or the
actual AC magnitude across that DUT, this resistor must be factored in. A
transimpedance amplifier is used in measuring the current, and has a 10 ohm
input protection resistor R\ :sub:`IN`. A simplified diagram is shown below. In
the diagram, Z\ :sub:`X` is the DUT (unknown impedance). The transimpedance
amplifier holds the connection point to R\ :sub:`IN` (inverting terminal of the
TIA) at 0V. Since R\ :sub:`S`, Z\ :sub:`X` and R\ :sub:`IN` are in series, the
DUT current is equal to (magnitude setting Vpk)/(\|Z\ :sub:`X`\ \| + 100Ω +
10Ω).

.. figure:: images/source_and_measurement_channels_v3_renumbered.png
   :align: center
   :width: 600

Available current gain settings and the transimpedance values associated with
them are listed below.

======== ================= ==============
Ch1 Gain Max Input Current Transimpedance
======== ================= ==============
0        25mA              49.9Ω
1        2.5mA             499Ω
2        250uA             4.99kΩ
3        25uA              49.9kΩ
======== ================= ==============

Continuing from the previous example, when the DUT is 2kΩ and the magnitude is
set to the maximum setting of 2.25Vpk, the current through the DUT (and into the
TIA) is 2.25Vpk/(2kΩ + 110Ω) = 1.06mA. Then selecting ch1 gain to be 1 makes the
measurement fit well within the max input current range of 2.5mA.

The command ``setgain ch0`` modifies the input voltage range of channel 0
(between terminals H_POT and L_POT). This is less common, but it can be used to
improve measurement sensitivity if the impedance under test is smaller than the
lead impedance or less than 100Ω. It can also be used if the magnitude of the
test signal is small. This can be the case with sensitive loads, or when the
test frequency is high.

Available voltage gain values for channel 0 are listed below.

======== ======================= ===========
Ch0 Gain Max Input Voltage Range Gain Factor
======== ======================= ===========
0        ±2.5V                   1
1        ±1.25V                  2
2        ±625mV                  4
3        ±312.5mV                8
======== ======================= ===========

The DUT voltage is determined by the set magnitude and the two series protection
resistors. The DUT voltage is equal to (magnitude setting Vpk)*(\|Z\ :sub:`X`\
\|)/(\|Z\ :sub:`X`\ \| + 110Ω). For example, to measure a 25Ω DUT with the
magnitude set to the maximum setting of 2.25Vpk, the DUT voltage is
2.25Vpk*(25Ω)/(25Ω + 110Ω) = 416.7mVpk, a little under the 625mVpk limit. To
utilize the full range, set the ch0 gain = 2.

Voltages across and currents through the DUT that exceed these maximum values
for each gain range may result in the ADC saturating, causing the measurement to
fail.

Typing the command ``setgain`` will display the gain of both input channels and
whether or not autoranging is enabled.

::

   ADMX2001> setgain
   Autorange enabled
   voltGain = 1
   currGain = 3
   ADMX2001>

To turn autoranging back on after setting a manual range type ``setgain auto``

Even though 16 gain combinations are possible, most measurements can be
performed with the 7 combinations shown in the table below.

======== ======== ===========================
Ch0 Gain Ch1 Gain Impedance Measurement Range
======== ======== ===========================
3        0        < 10Ω
2        0        < 25Ω
1        0        < 50Ω
0        0        100Ω to 1kΩ
0        1        1kΩ to 10kΩ
0        2        10kΩ to 100kΩ
0        3        > 100kΩ
======== ======== ===========================

These are the same ranges that the autoranging algorithm uses. The previously
mentioned procedures can be used to calculate the DUT current and voltage. The
following section shows how to estimate the impedance value of the DUT to
determine the measurement range. Note that these measurement ranges apply for
``magnitude = 1`` and ``offset = 0``. They may not apply for other settings. To
calculate whether the ADC will saturate, use the balancing bridge diagram above.
Using the sum of the signal magnitude and offset, calculate what the current
through the 110Ω resistors + DUT will be, and choose a gain from the Ch1 gain
table. Then, calculate the voltage across the DUT due to this current through
it, and choose a voltage gain from the Ch0 gain table.

For a 2kΩ DUT where the sum of the magnitude and offset is 1Vpk, using the two
equations we find:

-  DUT current = 1Vpk/(2kΩ + 110Ω) = 0.47mA, select Ch1 Gain = 1.
-  DUT voltage = 1Vpk\*2kΩ/(2kΩ + 110Ω) = 948mV, select Ch0 Gain = 0 or 1.
-  The above selection matches the suggested gain combination (0,1) with a given
   impedance measurement range from 1kΩ to 10kΩ.

Estimating the Impedance and Admittance of Capacitive and Inductive Devices
---------------------------------------------------------------------------

Impedance is defined as the opposition to the flow of alternating current.
Admittance is the reciprocal of impedance, or how easy is for alternating
current to flow. Electrical components such as resistors, capacitors and
inductors have a direct relationship between their value and the expected
impedance (Z):

Z = X = -1/(2πfC) for capacitors Z = X = 2πfL for inductors Z = R for resistors

Where f is the frequency of the signal; C, L, and R are the component values in
Farads, Henries and Ohms respectively. R represents resistance and X reactance.

For admittance (Y):

Y = B = 2πfC for capacitors Y = B = -1/(2πfL) for inductors Y = G = 1/R for
resistors

Where f is the frequency of the signal; C, L, and R are the component values in
Farads, Henries and Ohms respectively. G represents conductivity and B
susceptance.

All components, regardless of their construction, will show a combination of
resistive (conductive) and reactive (susceptive) properties. These properties
can be expressed in the form of ideal electrical components combined either in
series or parallel. At any given frequency, impedance/admittance can be
expressed as a combination of the reactive element (capacitor or inductor) and a
resistive element. The total impedance or admittance magnitude can be obtained
by calculating the square-root of the sum of squares (RSS) of the two components
or

Z = sqrt(R\*R + X\*X)

Y = sqrt(G\*G + B\*B)

| To determine the best measurement range for measurement, it is necessary to
  estimate the impedance or admittance of the device under test at the frequency
  of measurement using the equations above. A simpler method to obtain an
  approximate value based on the expected capacitance or inductance value is
  through the reactance chart shown below.

.. image:: images/reactance_chart_labeled.jpg
   :align: center
   :width: 600

To find the approximate impedance or admittance value for a capacitor or
inductor, find the closest expected value assigned to the diagonal lines and
find its equivalent impedance/admittance value on the vertical axis at the
frequency of interest (on the horizontal axis). For example, the impedance of a
159fF capacitor, which is represented by the red solid diagonal line in the
reactance chart, exhibits \|Z|=1MΩ at 1MHz, indicated by the "1M" tick on the
vertical axis. This matches the estimated value using equation Z = X =
-1/(2πfC). Similarly, for a 15.9nF capacitor, which is shown as blue solid
diagonal line in the chart, \|Z|=10KΩ at 1kHz.

Reducing Measurement Noise
--------------------------

The ``average`` command determines how many samples are averaged for each
reading returned. Averaging reduces noise and is helpful in applications that
require to detect small changes in a value or when the impedance component of
interest is small in comparison to the total impedance magnitude (e.g. ESR of
capacitors). The default is set to 1, which means that no averaging is done.

.. tip::

   Averaging increases the time required to return a reading. Values greater
   than 256 have been observed to have little effect in reducing measurement
   noise and have a significant impact on measurement speed.

Improving Measurement Precision
-------------------------------

To ensure precise and accurate measurements, impedance measurements should be
performed with appropriate test fixtures. Measurement leads can introduce
additional errors due to parasitic impedances that will vary depending on
mechanical configuration.

.. tip::

   The test leads included with the EVAL-ADMX2001EBZ kit can introduce
   fluctuations of a few picofarads depending on their position. This effect
   becomes more noticeable with test frequencies higher than 100kHz.

To ensure repeatable and stable measurements, custom-made fixtures that minimize
impedance fluctuations due to mechanical configuration are recommended. For
example, to test surface-mount components, fixtures like the `B+K Precision
TL89S1
<https://www.digikey.com/en/products/detail/b-k-precision/TL89S1/7915183>`_ or
the `Keysight 16034G
<https://www.keysight.com/en/pd-1000000474%3Aepsg%3Apro-pn-16034G/smd-test-fixture>`_
are recommended. For a full list of recommended accessories, please refer to the
Recommended Accessories Section at the beginning of this user guide.

Performing Parametric Sweeps
----------------------------

The ADMX2001B can automatically perform measurements that sweep different
measurement parameters such as

-  Frequency, common in EIS applications (Electrical Impedance Spectroscopy).
   The frequency increments can be linear or logarithmic.
-  DC bias, common in C-V measurements for semiconductor devices
-  Magnitude

By default, the sweep function is off. To enable parametric sweeps, use the
``sweep_type`` command and specify the sweep type. The command also requires the
user to enter the start and end points of the sweep. The number of points is
determined by the ``count`` command.

Example
~~~~~~~

Perform an 11-point logarithmic frequency sweep from 100kHz to 1MHz.

::

   ADMX2001> count 11
   sampleCount = 11
   ADMX2001> sweep_type frequency 100 1000
   Frequency
   sweepStart = +100.0000KHz
   sweepEnd = +1000.0000KHz
   ADMX2001> sweep_scale log
   Sweep scale is log
   ADMX2001> z
   1.000000e+05,5.683433e-13,8.149236e+07
   1.258925e+05,5.704062e-13,4.727518e+07
   1.584893e+05,5.674423e-13,2.989029e+07
   1.995262e+05,5.652225e-13,1.917354e+07
   2.511886e+05,5.622380e-13,1.233886e+07
   3.162278e+05,5.577508e-13,8.082886e+06
   3.981072e+05,5.490229e-13,5.611289e+06
   5.011872e+05,5.421543e-13,3.547964e+06
   6.309573e+05,5.299540e-13,2.360688e+06
   7.943282e+05,5.136760e-13,1.624230e+06
   1.000000e+06,4.798023e-13,1.411488e+06
   ADMX2001>

.. note::

   When sweeping parameters, the first value printed will be the swept
   parameter, followed by the measurement in the display format selected.

Performing DC Resistance Measurements
-------------------------------------

The DC resistance measurement function can be easily selected by setting the
test frequency to zero. In DC mode, since the AC test signal is disabled, the DC
offset must be used to generate the test signal. Due to the hardware design,
saturation may not be detected if the DC offset is positive; set the DC offset
to a negative value to prevent this. DC resistance mode only works in display
mode 6, so the display mode must be configured as such.

::

   ADMX2001> frequency 0
   DC Resistance mode enabled
   ADMX2001> display 6
   Measurement model: 6 - Impedance in rectangular coordinates (default) (Rs,Xs)
   ADMX2001> offset -1
   Offset = -1.0000
   ADMX2001> z
   0,4.995231e+01
   ADMX2001>

In the DC resistance mode, only the DC resistance value is returned.

Plotting Measurement Data
-------------------------

When acquiring multiple measurements or performing sweeps, it is useful to plot
the results to observe trends or characteristics of the device under test.
TeraTerm allows the user to save a log by going to File->Log, which can then be
copy and pasted into a \*.csv file that can be opened by spreadsheet
applications such as Microsoft Excel®. The log file must be saved BEFORE taking
any measurements.

To plot the acquired data in Microsoft Excel, follow the steps below:

-  In TeraTerm, click File, in the dropdown list select Log, and save the log
   file with any name but make sure to change the default extension from \*.log
   to \*.csv
-  Configure the ADMX2001B and run the ``z`` command to acquire the desired
   measurements
-  In a separate TeraTerm window named "TeraTerm:Log", click close to stop
   logging data
-  Open the file with Excel
-  Select the data to plot and insert a scatter plot to visualize the data

Optimizing Measurement Timing
-----------------------------

This section describes what settings impact the measurement time and how. It
also discusses ways to reduce the measurement time down to ~10-12 ms for single
measurements (firmware version 1.3.2 only). The measurement time is dependent on
a number of factors. Command transmission time, configured delays, source setup
time, ADC acquisition time, count setting, averages, etc. Some factors, like the
ADC acquisition time, are dependent on the frequency since the ADC needs to
capture a minimum of three cycles of the waveform.

Delay Usage and Measurement Sequencing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The commands ``mdelay`` (measurement delay) and ``tdelay`` (trigger delay) can
be used to control the settling time between measurements.

-  The measurement delay or ``mdelay`` is observed before each measurement, but
   not between samples when averaging. The delay is also applied during sweeps
   and between multiple counts. Both the DC offset and AC test signal are
   enabled during the delay, but the ADCs do not capture data for the
   measurement until the delay has elapsed.
-  The ideal measurement delay suitable for different DUTs may vary. When
   measuring a large capacitor, consider the settling time it requires to charge
   the DUT; a longer mdelay is preferred to prevent accuracy loss.
-  Trigger delay is only observed after trigger events controlled by the
   ``tcount`` command. This is useful when using the ADMX2001B with external
   scanning cards or multiplexers, to allow proper debounce and settling time.
   If configured, the DC offset will be enabled during the trigger delay, but
   the AC source will only start for the data capture.

To setup ``mdelay`` and ``tdelay``, simply enter the command followed by a value
in milliseconds.

Below is a demonstration on how each measurement time parameter fits in the
measurement sequence. Note that the sinusoidal excitation is turned on during
periods marked with blocks in light/dark green. If enabled, the DC offset will
turn on during the tdelay blocks. The example measurement uses a 15.8 Ohm
resistor as the DUT.

.. image:: images/command_timing_diagram.png
   :align: center
   :width: 1000

1. Single sample measurement. When measuring one count sample, an ``mdelay`` is
   observed before each measurement where the single sample is captured.

::

   ADMX2001> count 1
   sampleCount = 1
   ADMX2001> average 1
   average = 1
   ADMX2001> z
   0,1.589015e+01,5.979061e-03

2. Multiple samples averaging. When measuring with ``average`` > 1, ``mdelay``
   is observed only before the first sample, but not between samples.

::

   ADMX2001> count 1
   sampleCount = 1
   ADMX2001> average 10
   average = 10
   ADMX2001> z
   0,1.588981e+01,5.922471e-03

3. Multiple counts measurement. When doing multiple counts of single sample
   measurement, ``mdelay`` is observed before each measurement in their
   individual count.

::

   ADMX2001> count 3
   sampleCount = 3
   ADMX2001> average 1
   average = 1
   ADMX2001> z
   0,1.588983e+01,6.072280e-03
   1,1.589017e+01,6.406131e-03
   2,1.588982e+01,6.175226e-03

4. Multiple triggers measurement. When ``tcount`` >1, multiple measurement
   triggers are enabled. Based on single measurement cycle setting (say
   ``count`` = 3, ``average`` = 1), multiple measurement events are triggered.
   The ``tdelay`` defines the delay time between these trigger events.

::

   ADMX2001> count 3
   sampleCount = 3
   ADMX2001> average 1
   average = 1
   ADMX2001> tdelay 10
   triggerDelay = 10.0000msec
   ADMX2001> tcount 3
   triggerCount = 3
   ADMX2001> z
   0,1.588982e+01,6.526160e-03
   1,1.589041e+01,5.718554e-03
   2,1.589056e+01,6.170146e-03
   0,1.588994e+01,6.373706e-03
   1,1.589030e+01,5.733064e-03
   2,1.589026e+01,5.668341e-03
   0,1.589055e+01,5.907189e-03
   1,1.588984e+01,5.669621e-03
   2,1.588993e+01,6.286668e-03

Optimizing Single Point Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In version 1.3.2, many optimizations were added to reduce the measurement time.

-  The ``initiate`` and ``trigger`` mode (trigger mode), previously used only
   for external triggers, is now optimized for faster measurements. See `Trigger
   Input/Output Ports <https://wiki.analog.com/eval-admx2001ebz>`_ for details
   on how to use trigger mode (also referred to as the WAIT_FOR_TRIGGER state).
-  When in trigger mode, most commands are disabled. This is because measurement
   attributes like frequency, gain, magnitude, offset, delays, and others are
   locked. Locking them means that for each measurement, setup and
   initialization tasks for those attributes can be skipped because they will
   always be unchanged. This saves a significant amount of time on each
   measurement, especially reducing the time between a trigger being received
   and the measurement acquisition starting.

   -  Sweeps do not benefit from this optimization, because the sweep attribute
      cannot be updated in trigger mode.
   -  If enabled, the DC offset is always on in trigger mode. The autorange must
      be off to enable the DC offset. Keeping the DC offset enabled constantly
      can be useful when testing with DUTs that need a long DC settling time, as
      that delay does not need to be repeated for every measurement.

-  The measurement is only reported over the active interface (UART commmand
   line interface or SPI). The active interface is set based on the most
   recently sent command. For instance, if the command ``initiate`` is sent over
   UART, and then the command TRIGGER (0x18) is sent over SPI, the result will
   be readable in the SPI FIFO and not accessible on UART. If INITIATE (0x17) is
   sent over SPI, and then ``trigger`` is sent over UART, the result will print
   immediately to UART and not be accessible in the SPI FIFO. See
   :doc:`ADMX2001B SPI Interface
   </solutions/reference-designs/admx2001_ebz/spi-interface>` for
   details on how to operate the SPI interface.

   -  The SPI interface is the fastest and can save multiple milliseconds over
      using the UART (command line) interface.

.. image:: images/trigger_mode.png
   :align: center
   :width: 800

To achieve the fastest single-point measurement time, there are a few points to
consider.

-  Interface: The SPI interface should be used to receive the measurement data.
   Either interface can be used to configure measurement settings, this will not
   impact the speed of each measurement. The active interface is updated every
   time a command is sent, to whichever interface sent that command.
-  Trigger source: In trigger mode, there are three options for the trigger
   source.

   -  The ``trigger`` command can be sent over the UART (CLI). This is the
      slowest method, and since ``trigger`` will be the most recent command, it
      will always report the result over the UART (CLI).
   -  The TRIGGER (0x18) command can be sent over SPI. This is the preferred
      method as it is fast, and easy to set up. It also guarantees that the
      active interface will be set to SPI.
   -  A pulse can be applied to the TRIG_IN pin. For this pulse to be
      registered, external trigger mode must be enabled; see `Trigger
      Input/Output Ports <https://wiki.analog.com/eval-admx2001ebz>`_.
      Measurements initiated with the external trigger can report data over
      either the UART or SPI interfaces, dependent on where the most recent
      command was received. For instance, this could be the ``initiate`` command
      in CLI, or INITIATE (0x17) over SPI.

-  Trigger count: when using trigger mode, the trigger count (tcount) sets a
   condition for automatically exiting trigger mode. It will receive ``tcount``\
   \*triggers before returning to the normal operating mode. To continue
   measuring in trigger mode, the ``initiate`` command is needed to re-enter the
   mode. To exit trigger mode before completing ``tcount``\ \*triggers, the
   ``abort`` command can be used (0x1A) in SPI.

   -  There is also support for an "infinite" trigger mode. Run ``tcount 65536``
      to enter this mode; the only way to exit trigger mode in this case is with
      the ``abort`` command. Normal ``z`` measurements are disabled when
      ``tcount`` is set to 65536.

-  Autorange: The autorange should be disabled for the fastest measurements. The
   autorange tests the ideal gain by taking multiple measurements with different
   gain settings, and checking for ADC saturation. Therefore, it can
   significantly increase the measurement time.

   -  When using the autorange with trigger mode, the autorange test is
      performed when the ``initiate`` command runs. See the flow chart above.
      Leaving and re-entering trigger mode will update the selected gain.

-  Delays: The trigger delay (tdelay) and measurement delay (mdelay) directly
   impact the measurement time. In trigger mode, the tdelay is applied once per
   supplied trigger, and the mdelay is supplied once per count (not tcount).
   Therefore, a typical single measurement will have tdelay+mdelay added on. The
   default tdelay is 4 ms; this can typically be set to 0 ms with no negative
   impacts; this is recommended to optimize the measurement time. The default
   mdelay is 1 ms; at frequencies above 10 kHz, setting this to 0 ms will cause
   the ADC to capture some data before the AC source has fully turned on. This
   typically has no impact on the measurement result, allowing 1 ms to be saved
   per measurement, but it should be tested with each setup.
-  Frequency: the measurement time is highly dependent on the test frequency
   below ~3 kHz. This is because the system tries to capture a minimum of 3
   cycles of the excitation waveform. See the log plot below for the measurement
   time across frequency.
-  Display mode: the measurement time is also dependent on the display mode.
   Rectangular formats like display mode 6 (R, X) and 15 (G, B) are the fastest,
   as they require the least processing. Modes with angle in degrees or radians
   (polar form) can take 2-3 extra milliseconds; see the chart below.

.. image:: images/measurement_time.png
   :align: center
   :width: 1200

\*Typical measurement times above are based on the following settings:

-  Interface = SPI, SPI trigger source
-  Mode = trigger mode
-  mdelay = 0
-  tdelay = 0
-  average = 1
-  calibration = on (can save 1-2 ms turning calibration off)
-  autorange = off

Note that measurements taken over the UART will be slower.

Calibration Procedure
~~~~~~~~~~~~~~~~~~~~~

A few milliseconds after power up, the ADMX2001B is ready to perform
measurements. However, any readings and their units are scaled and assigned
using nominal circuit parameters. Measurement accuracy can only be evaluated
after performing calibration on the module with an external calibration source
with certified traceability. For example, the `Keysight E4980A
<https://www.keysight.com/us/en/product/E4980A/precision-lcr-meter-20-hz-2-mhz.html>`_
can be used.

There are three basic calibration steps involved in calibrating the module: open
calibration, short calibration, and load calibration. The first two correct the
module and test lead parasitics. The latter provides traceability to an external
source. The calibration steps must be performed in the order open->short->load.
Open and load calibration are the most important. Short calibration may need to
be skipped in certain gain ranges where the current ADC would saturate. Open
calibration may need to be skipped in gain ranges that the voltage ADC would
saturate.

.. image:: images/open_short_load_config.png
   :align: center
   :width: 1200

.. image:: images/open_short_load_config_photo.png
   :align: center
   :width: 1200

.. tip::

   When performing load calibration for a given gain setting and frequency, the
   optimal load device (usually a resistor) is one with an impedance magnitude
   close to that of the eventual DUT. The best accuracy at a certain gain and
   frequency will be with DUTs of a similar impedance to the one used in
   calibration.


   Resistors, capacitors or inductors can be used for calibration. High-quality
   resistors (e.g. thin film or metal film), air capacitors, and gas-filled
   capacitors tend to provide the best results. Alternatively, C0G/NP0 type
   ceramic capacitors can be used as well. The true value of these components
   must be determined with traceable measurements from another meter, such as
   the Keysight E4980A.

Each measurement front-end configuration (ch0 and ch1 gain combination) needs to
be calibrated separately. If calibration is performed for only one gain
combination, calibration needs to be carried out again if the front-end
configuration changes. There are a total of 16 possible gain combinations based
on the 4 gain and transimpedance ranges for channel 0 and channel 1
respectively.

The autorange will only choose between the 7 gain combinations that have a zero
in at least one position. These are shown in the impedance measurement range
table within the section `Selecting a Measurement Range`_. If all measurements
will be done with the autorange or with these gains, then the other gain
settings do not need to be calibrated. In versions 1.2.0 and older, if the user
calibrates at a specific gain and frequency, then changes the frequency and
calibrates again, the user will overwrite the result of the first calibration.
In version 1.2.2, support for calibration over frequency was added. See
`Calibration Over Frequency`_ for more details.

.. important::

   Each calibration point is for a specific frequency. Measurements taken at a
   different frequency may be out of tolerance. Always calibrate as near as
   possible to the intended test frequency.

Calibration Steps
-----------------

To calibrate the module in a specific gain combination, follow the steps below:

-  Select the desired measurement configuration (gain, frequency, magnitude and
   offset)

   -  Autorange must be disabled during calibration.

-  Set the averaging to at least 200 samples.
-  Ensure the load select switches are in the DUT and GND positions, described
   in `Basic Hardware Setup <https://wiki.analog.com/eval-admx2001ebz>`_
-  Connect the H_POT and H_CUR terminal together and the L_POT and L_CUR
   terminals together to form two separate connection pairs

   -  If using the test clips, place them so the alligator clips are separated
      by the same distance as they will be when the DUT is connected. Each clip
      should be clipped to a very short scrap of uninsulated wire, which serves
      to improve the connection between each half of the clip
   -  An alternative is to use BNC cables to connect the H_POT/H_CUR pairs and
      the L_POT/L_CUR pairs.
   -  Open calibration at high frequencies and in higher impedance measurement
      ranges is especially susceptible to error, due to the increased
      opportunity for coupling into the current measurement path. The test setup
      is especially important under these conditions
   -  For better results, use `Keysight 42090A Open Termination
      <https://www.keysight.com/en/pd-1000003831%3Aepsg%3Apro-pn-42090A/open-termination-4-terminal-pair>`_

-  Run the ``calibrate open`` command
-  Connect all the measurement terminals together

   -  Short calibration can be performed only when gain channel 1 is set to 0 or
      1. When channel 1 is in gain 1, the magnitude of the source must be less
      than 0.2Vpk.
   -  When measuring extremely tiny impedances (<100mΩ), short calibration
      becomes extremely important. Many fixtures have a low repeatability under
      these conditions. Optimizing the repeatability of the fixture is critical
      to getting a meaningful result, for both calibration and measurement
   -  For better results, use `Keysight 42091A Short Termination
      <https://www.keysight.com/en/pd-1000003830%3Aepsg%3Apro-pn-42091A/short-termination-4-terminal-pair>`_

-  Run the ``calibrate short`` command, if possible
-  Connect a known impedance between the measurement leads
-  Run the ``calibrate rt <value1> xt <value2>`` command where ``<value1>`` is
   the true value of the resistive component (Ohms) of the calibration impedance
   and ``<value 2>`` is the true value of the reactive component (Ohms)

   -  To obtain true values of resistive and reactive components beforehand, use
      an LCR meter and select Rs and X for the display mode.
   -  Scientific notation can be used when entering the rt and xt values
   -  For best results, a standard resistor set like the `Keysight 42030A
      <https://www.keysight.com/en/pd-1000003832%3Aepsg%3Apro-pn-42030A/four-terminal-pair-standard-resistor-set>`_
      can be used

After completing the steps above, calibration coefficients are generated and
stored in RAM. These coefficients will be applied to any subsequent
measurements, but will be lost after a power cycle or reset of the module. To
store the coefficients in non-volatile memory (flash) the command ``calibration
commit <timestamp>`` must be executed. The timestamp parameter is optional. If
supplied, the unix timestamp is the number of seconds elapsed since 01/01/1970.
For example:

::

   ADMX2001>calibrate commit 1689959855

This will store the calibration coefficients in the RAM to the flash, and set
the date and time stamp of the calibration to 07/21/23 at 05:17 UTC.

.. note::

   To help ensure calibration integrity, the calibration coefficients stored in
   flash are password protected. The default password is ``Analog123`` and must
   be entered after running ``calibrate commit`` to save the coefficients. The
   password can be changed with the ``calibrate password`` command. Maximum
   password length is 12 characters.

Calibration Example
-------------------

Calibrate the gain setting (0, 1) at 100kHz with a resistor of value 1k Ohms.
The true resistance Rt from the E4980A at 100kHz was measured as 1000.019 Ohms,
and the true reactance Xt was 0.822 Ohms.

::

   ADMX2001> setgain ch0 0
   voltGain = 0
   ADMX2001> setgain ch1 1
   currGain = 1
   ADMX2001> frequency 100
   frequency = 100.0000kHz
   ADMX2001> magnitude 1         <--- 1 Vpk, 2 Vpp
   magnitude = 1.0000
   ADMX2001> offset 0
   Offset = 0.0000
   ADMX2001> average 200
   average = 200
   ADMX2001> tdelay 200
   triggerDelay = 200.0000msec
                                 <--- Connect open load now
   ADMX2001> calibrate open
   0,-1.117998e-09,1.162904e-06
   Frequency = 100.0000kHz
   Cal Temp: 41.4 deg C
   open:Done
   short:Not Done
   load:Not Done
   ADMX2001> magnitude 0.2       <--- Need to reduce the magnitude to avoid saturating the current ADC when measuring a short
   magnitude = 0.2000
                                 <--- Connect short load now
   ADMX2001> calibrate short
   0,2.075835e-02,1.224807e-02
   Frequency = 100.0000kHz
   Cal Temp: 41.4 deg C
   open:Done
   short:Done
   load:Not Done
   ADMX2001> magnitude 1         <--- Magnitude can be set back to 1 now
   magnitude = 1.0000
                                 <--- Connect calibration load now (in this case, a 1kΩ resistor)
   ADMX2001> calibrate rt 1e+3 xt 0.822
   0,1.010381e+03,-1.254483e+01
   Frequency = 100.0000kHz
   Cal Temp: 41.5 deg C
   open:Done
   short:Done
   load:Done
   ADMX2001> calibrate commit 1689959855   <--- The timestamp can be omitted here
   PASSWORD> ****
   commit : success
   ADMX2001> display 6
   Measurement model: 6 - Impedance in rectangular coordinates (default) (Rs,Xs)
   ADMX2001> z
   0,1.000021e+03,8.220137e-01
   ADMX2001>

Reading and Writing Calibration Coefficients
--------------------------------------------

Calibration coefficients for each gain can be read to the terminal, and written
back to the device. This allows the user to save coefficients for multiple
different test setups, conditions, or frequencies. To read the currently loaded
coefficients for a certain gain setting, run the command ``rdcal <vgain>
<igain>``. This prints the 12 AC and and 2 DC coefficients to the terminal,
where they could be saved by an external device. To write coefficients to the
device, use the command ``storecal <vgain> <igain> <coefficient_name> <value>``,
where ``coefficient_name`` is one of the 12 AC or 2 DC coefficients. For
example, set Ro to 1e+6 for the gain vgain=0, igain=1:

::

   ADMX2001> storecal 0 1 Ro 1e+6
   ADMX2001> rdcal 0 1
   Ro = 1.0000000e+06
   Xo = -8.5991553e+05
   Go = -1.1179984e-09
   Bo = 1.1629038e-06
   Rs = 2.0758350e-02
   Xs = 1.2248066e-02
   Gs = 3.5733319e+01
   Bs = -2.1083758e+01
   Rg = -9.4387458e+03
   Xg = 8.5097009e+05
   Gg = -3.5847357e+01
   Bg = 2.1737716e+01
   No calibration coefficients found for the given arguments. The defaults coefficients are ...
   Rdg = 1.0000000e+00
   Rdo = 0.0000000e+00
   ADMX2001>

This process should be repeated for all coefficients for a given gain to be
valid. If using other gains, the coefficients will need to be stored for them
too. Then, they must be saved using ``calibrate commit``; otherwise, they will
be lost if the system reboots.

Calibration Over Frequency
--------------------------

Starting in firmware version 1.2.2, calibration over frequency support is
implemented. This means that all 16 gain settings can be fully calibrated at
multiple frequency points. The process for calibrating over frequency is the
same as single point calibration, except after running ``calibrate commit`` for
the final gain setting at a given frequency, the user can then change the
frequency and repeat the process.

When calibration is enabled, taking a measurement with ``z`` will automatically
load the calibration coefficients with the nearest frequency from memory. After
taking the measurement, running the command ``calibrate`` with no arguments will
report the frequency of the coefficients that were used. For instance, if
calibration was performed at 1 kHz and at 100 kHz, a measurement at 55 kHz would
use the coefficients saved for 100 kHz.

There are no restrictions on what frequencies the user can calibrate at.
However, there are two hardware revisions of the ADMX2001B module; one has
EEPROM for the nonvolatile memory (older) and the other has flash memory.
Modules with the EEPROM can store 25 calibration sets at different frequency
points before new sets start to overwrite the oldest ones. Modules with the
flash can store up to 450 calibration sets. The command ``selftest run`` will
report whether the module has EEPROM or flash installed.

New commands have been added to facilitate calibration over frequency:
``resetcal`` (unchanged) will erase only the currently loaded calibration set
from RAM. ``calibrate reload`` will load the nearest frequency calibration
coefficients from the nonvolatile memory and store them in the RAM (taking a
measurement implicitly runs ``calibrate reload``). ``calibrate erase`` will
permanently delete all saved calibration sets from memory, restoring to the
default configuration. This requires the password (default is Analog123) and
cannot be undone! ``calibrate list`` will report all frequencies that have any
calibration data saved (at least one gain setting). ``calibrate list <freq>``
will report what gain settings at a given frequency have been calibrated.

The commands for reading and writing calibration coefficients detailed in
`Reading and Writing Calibration Coefficients
<https://wiki.analog.com/eval-admx2001ebz>`_ apply to the currently selected
frequency.

Preloaded Calibration Sets
--------------------------

Version 1.2.2 also adds support for ADMX2001B modules to ship with a set of
calibration coefficients intended to help with evaluating the board. Although
the firmware supports it, boards that are currently shipping will not have
calibration coefficients preloaded. This will be a future development.

Preloaded coefficients may not apply to a given test setup and their accuracy is
not guaranteed. If the board came with them pre-loaded, then the below new
commands apply: ``calibrate switch <evalkit/default>`` choosing evalkit will
apply the preloaded coefficients. Choosing default will apply user generated
coefficients. Generating calibration coefficients will automatically change the
active set to default. ``calibrate`` with no arguments will report the active
set. The evalkit set cannot be modified or erased. Only the default (user) set
should be modified or erased.

Compensation Procedure
----------------------

Compensation is an additional measurement adjustment function designed to
account for changes in the test fixture or leads that were not present during
calibration. This feature is in development; currently, it is recommended to
recalibrate for each fixture, and use the commands detailed in `Reading and
Writing Calibration Coefficients <https://wiki.analog.com/eval-admx2001ebz>`_ to
save and load calibration data from a host device.

.. image:: images/calibration_compensation_boundary_2.png
   :align: center
   :width: 600

EVAL-ADMX2001EBZ Terminal Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/eval-admx2001ebz_diagram_3.png
   :align: center
   :width: 600

+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| Terminal Name         | Description                                                                                                               |
+=======================+===========================================================================================================================+
| H_CUR                 | Signal source terminal. It generates the excitation required for measurement. This terminal can source up to +/-5V @ 50mA |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| H_POT                 | Voltage sense terminal. Connect to H_CUR at the device under test (DUT)                                                   |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| L_POT                 | Voltage sense terminal. Connect to L_CUR at the device under test (DUT)                                                   |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| L_CUR                 | Current sense terminal. Return path for the excitation signal. Connect to the opposite end of the DUT as H_CUR            |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| UART TX               | UART transmitter pin. Connect to TX pin on the UART to USB cable. Uses 3.3V logic                                         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| UART RX               | UART receiver pin. Connect to RX pin on the UART to USB cable. Uses 3.3V logic                                            |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| UART GND              | UART ground. Connect to ground pin on the UART to USB cable                                                               |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| CLK_SEL               | Jumper selection of internal or external clock. Set to internal for default operation                                     |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| TRIG_IN               | Trigger input. Use for hardware-timed acquisition only, otherwise leave disconnected                                      |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| TRIG_OUT              | Measurement complete trigger out                                                                                          |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| CLK_IN                | External clock input. Use a LVCMOS 50MHz clock signal and set CLK_SEL to EXT position                                     |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| CLK_OUT               | Clock output. These two terminals have a buffered replica of the 50MHz main clock                                         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| PMOD                  | Controller and Peripheral PMOD terminals for SPI port                                                                     |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| Header P6 pins [9-10] | Digital output 0-1                                                                                                        |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+
| Header P7 pins [1-6]  | Digital output 2-7                                                                                                        |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------+

|

SPI Interface
-------------

The ADMX2001B supports a SPI interface in addition to the UART CLI interface.
The SPI bus can be accessed on Header P6 and both PMOD headers of
EVAL-ADMX2001EBZ, or pins B14-B17 of the ADMX2001B module. A full command
reference for the SPI interface can be found at :doc:`ADMX2001B SPI Interface.
</solutions/reference-designs/admx2001_ebz/spi-interface>`

Trigger Input / Output Ports
----------------------------

The EVAL-ADMX2001EBZ has SMA terminals for the trigger input and output ports.
These can be used to synchronize multiple modules or control measurement timing
with an external instrument. To use the trigger input, the module must be
configured to external ``trig_mode`` using the command ``trig_mode
<internal/external>``. By default, the board is in internal ``trig_mode``, and
ignores pulses on the TRIG_IN port. Next, set the trigger count with ``tcount
<count>``. This controls how many external triggers the module will respond to
before exiting the WAIT_FOR_TRIGGER state. There is also an "infinite" trigger
setting; if the tcount is set to 65536, then it will respond to unlimited
triggers and never exit the WAIT_FOR_TRIGGER state automatically. Now, type the
command ``initiate``. The module will enter the WAIT_FOR_TRIGGER state. Most
commands are disabled in this state. The module will automatically return to the
IDLE state after receiving ``tcount`` triggers, or immediately if it receives
the ``abort`` command. While in the WAIT_FOR_TRIGGER state, a software trigger
can be provided with the command ``trigger``, in both internal or external
``trig_mode``. If the ``trig_mode`` is external, then a 3.3V 15μs pulse (min) to
the TRIG_IN port will be registered as a trigger.

When a measurement is initiated from the WAIT_FOR_TRIGGER state, either by an
external trigger or software trigger, it will generate a 3.3V 15μs pulse on the
TRIG_OUT port.

Immediately after running ``initiate``, the autorange algorithm will run (if the
autorange is enabled). The gain chosen by this instance of the autorange will be
locked in for subsequent measurements in trigger mode. If the DC offset is
enabled, then the DC offset will be applied as soon as the ``initiate`` command
runs. The DC offset and autorange cannot be used at the same time.

Warning: when the ``initiate`` command is run, the board will reload the
calibration data automatically from the flash. Any coefficients that were not
committed (saved to the flash) will be lost. This process is the same as running
the command ``calibrate reload``. Verify that any calibration data that should
be applied during trigger mode measurements is saved for it to be applied, and
not lost.

PMOD Headers
------------

The EVAL-ADMX2001EBZ features PMOD_IN and PMOD_OUT headers for interfacing with
a host over SPI.

===================== ========== ============================================
Pin Number            Pinout     Note
===================== ========== ============================================
1                     No Connect
2                     SDI
3                     SDO
4                     SCLK       20 MHz max
5                     GND
6                     VCC        3.3V, PMOD_OUT only. VCC current not limited
7                     No Connect
8                     No Connect
9                     CS
10                    No Connect
11                    GND
12                    VCC        3.3V, PMOD_OUT only. VCC current not limited
===================== ========== ============================================

Pins 6 and 12 are No Connect on PMOD_IN (P12). On PMOD_OUT (P11), they connect
to the 3.3V supply, and there is no current limiting on the board.

Digital Output Pins
-------------------

The ADMX2001B features eight general purpose digital output pins, intended for
controlling external MUXes or other peripherals. Support was added in version
1.2.2. The outputs are broken out on EVAL-ADMX2001EBZ, and can be accessed on
pins 9-10 of P6, and pins 1-6 of P7. They can be set with the command
``gpio_ctrl <N>`` where N is a decimal from 0-255, and each of the 8 inputs are
controlled by the respective bit for that position. Digital output 0 corresponds
to the LSB. For instance, configuring ``gpio_ctrl 133`` (1000 0101 in binary)
will set high P6 pin 9, and P7 pins 1 and 6.

=================== ========== =========
Header : Pin Number Bit Number N Setting
=================== ========== =========
P6 : 9              0          1
P6 : 10             1          2
P7 : 1              2          4
P7 : 2              3          8
P7 : 3              4          16
P7 : 4              5          32
P7 : 5              6          64
P7 : 6              7          128
=================== ========== =========

ADMX2001B Pin Configuration and Function Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/admx2001b_pinout_top.png
   :align: center
   :width: 600

+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| Pin Number                                | Mnemonic    | Description                                                                                   |
+===========================================+=============+===============================================================================================+
| Center Pad                                | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A1-4, B1-4                                | VDD         | Power supply terminals. Apply +3.3V nominal                                                   |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A11                                       | VCC         | 5V rail, not current limited. Leave unconnected.                                              |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A18                                       | VEE         | -5V rail, not current limited. Leave unconnected.                                             |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A23                                       | CLKIN       | External clock input. Must connect to 50MHz source or CLKOUT terminal                         |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A25                                       | CLKOUT      | Clock output. If using external clock on CLKIN, leave unconnected. Otherwise connect to CLKIN |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| A22, A24, A26                             | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B5, B7, B9, B11, B13, B18, B21            | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B10                                       | TRIGIN      | Measurement trigger input. If unused, leave unconnected                                       |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B12                                       | TRIGOUT     | Measurement trigger output. If unused, leave unconnected                                      |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B14                                       | SCK         | Serial data clock input                                                                       |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B15                                       | SDI         | Serial data input                                                                             |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B16                                       | SDO         | Serial data output                                                                            |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B17                                       | CS          | Serial interface port chip select input                                                       |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B19                                       | TX          | UART transmit output. Connect to host’s receiver                                              |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B20                                       | RX          | UART receive input. Connect to host’s transmitter                                             |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B22                                       | JTAG_VCC    | JTAG power out.                                                                               |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B23                                       | TCK         | JTAG test clock.                                                                              |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B24                                       | TDO         | JTAG test data out.                                                                           |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B25                                       | TMS         | JTAG test mode select.                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| B26                                       | TDI         | JTAG test data in.                                                                            |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C18-C25                                   | GPIO0-GPIO7 | General-purpose digital output terminals                                                      |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C1, C3, C4, C6, C7, C9, C10, C12-C17, C26 | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| D1, D3, D4, D6, D7, D9, D10, D12          | GND         | Ground                                                                                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C2, D2                                    | HCUR        | Source terminal                                                                               |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C5, D5                                    | HPOT        | Voltage measurement high terminal. Tie to HCUR at the device under test                       |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C8, D8                                    | LPOT        | Voltage measurement low terminal. Tie to LCUR at the device under test                        |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| C11, D11                                  | LCUR        | Current measurement input                                                                     |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+
| All other pins                            | NC          | Do not connect                                                                                |
+-------------------------------------------+-------------+-----------------------------------------------------------------------------------------------+

| | ----

.. _eval-admx2001 firmware-updates:

Firmware Updates
~~~~~~~~~~~~~~~~

The ADMX2001B module firmware is user-updatable. Programming files must be
requested by contacting admx-support@analog.com. Make a myAnalog account on
:adi:`(analog.com) <en/index.html>`, by clicking in the top right. Then, email
admx-support@analog.com, and mention the email associated with the myAnalog
account.

Warning: updating between certain firmware versions can cause saved calibration
coefficients to be lost.

**Equipment List:**

-  EVAL-ADMX2001EBZ board
-  ADMX2001B Impedance Analyzer Measurement Module
-  Intel Altera USB Blaster `(Terasic)
   <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=46>`_
-  Universal power adapter with 9VDC output

**Software Prerequisites:**

-  Python 3.7 or greater
-  Latest Intel Quartus Prime Programmer And Tools

   -  Navigate to the downloads page for the latest Quartus Prime Lite Edition,
      and click the "Additional Software" tab. Alternatively, the full Quartus
      Prime Lite Edition can be used. Both are free, but the programmer is a
      smaller download

-  Drivers installed for the Altera USB Blaster
-  Firmware programming folder containing \*.pof file (downloaded from
   Analog.com, request from admx-support@analog.com)

**Board Programming Setup**

-  Connect the USB Blaster to the computer over USB and verify the driver
   installation
-  Plug the ADMX2001B module into EVAL-ADMX2001EBZ board
-  Connect the USB blaster to the port labeled "P8 JTAG" on the EVAL-ADMX2001EBZ
-  Connect the EVAL-ADMX2001EBZ to a 9V DC supply

Update Using Installation Script
--------------------------------

Versions 1.2.4+ comes bundled with an installation script to simplify the
firmware installation process.

This script is the preferred installation method.

-  Follow the steps under **Board Programming Setup**
-  Ensure that Quartus Prime 18.1 or newer is installed in the following path:
   ``C:\intelFPGA_lite\<version_number>\quartus``
-  Open a command prompt window
-  Navigate to the Tools folder present in the installation directory of
   ``Admx2001Firmware-Relx.y.z``, ``C:\Analog
   Devices\Admx2001Firmware-Relx.y.z\Tools``

   -  Here, x, y, & z represents the release number (1.2.4 for example)

-  Run the following command: ``python admx2001_flash_pof.py --pof "C:\Analog
   Devices\Admx2001Firmware-Relx.y.z\Firmware\admx_lcr_encrypted.pof"``

   -  Ensure that x.y.z is replaced with the appropriate release number (1.2.4
      for example)

-  Wait until the message "Programming POF completed successfully" is displayed
   in the terminal. It may take around 20 to 30 seconds for the process to
   complete.

   -   Do not unplug the board or otherwise interrupt the programming process.

-  When the programming is completed (message displayed and prompt appears)
   close the terminal and unplug the USB blaster. The firmware update is
   complete.

Update Using Manual Programmer
------------------------------

Versions 1.2.2 and older do not come bundled with an installation script. The
Quartus Prime Programmer interface can be used to perform the update. The
installation script is the preferred method, as selecting the wrong settings in
the manual programming tool can cause the board to no longer boot. It will need
to be returned/swapped.

If there are issues preventing the installation script from working to program
the board, the manual programmer method can be used. In this case, contact
admx-support@analog.com for assistance using the manual programmer.

Firmware Release Highlights
---------------------------

Currently available firmare versions and release highlights:

+---------+--------+-------------------------------------------------------------------------------------------------------------+
| Version | Status | Release Highlights                                                                                          |
+=========+========+=============================================================================================================+
| 1.3.2   | Stable | Measurement time optimizations, minor bug fixes                                                             |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.3.1   | Stable | Substantial measurement noise improvements, bug fixes and more                                              |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.2.4   | Stable | Same firmware as 1.2.2. Installation script added to release package                                        |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.2.2   | Stable | Adds calibration over frequency, configurable digital outputs, external trigger support, bug fixes and more |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.2.0   | Stable | Bug fixes, noise and repeatability improvements. Calibration with complex loads now supported               |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.1.1   | Legacy | Same fixes as 1.2.0, but not compatible with boards using the flash memory.                                 |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.1.0   | Legacy | Added SPI interface and built in self test                                                                  |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.0.1   | Legacy |                                                                                                             |
+---------+--------+-------------------------------------------------------------------------------------------------------------+
| 1.0.0   | Legacy |                                                                                                             |
+---------+--------+-------------------------------------------------------------------------------------------------------------+

The full release notes are included with each firmware download.

Python Scripting
~~~~~~~~~~~~~~~~

To facilitate easier measurement optimization on a PC, there is a library of
Python functions which make it easy to operate the command-line interface from a
Python script. Instead of typing commands over TeraTerm, the library accesses
the Serial port directly, and calling the library functions will execute the
same commands that are normally typed into the terminal emulator.

These Python libraries are currently accessible by request. First, make a
myAnalog account on :adi:`(analog.com) <en/index.html>` by clicking in the top
right. Then, email admx-support@analog.com, and mention the email associated
with the myAnalog account.

The Python script download includes an example measurement sweep script, which
shows how to set up the Serial port, configure measurements and begin collecting
data. More example scripts are coming in the future. Nearly all functions found
in the command-line interface have corresponding Python functions in the
library. These functions also perform a certain degree of error checking. This
library is for evaluation purposes only.

Version 1.1.0 includes a graphical user interface.

Python Graphical User Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since Python Evaluation Script version 1.1.0, the download package includes a
Python based graphical user interface (GUI). The GUI does not yet support all
features of the ADMX2001B, but it provides an quicker start and easier
experimentation compared to using the UART command-line interface (CLI). The GUI
communicates with the board over the UART CLI in the background, so any open
terminals connected to the board need to be closed prior to using the GUI.

The GUI requires some 3rd-party Python libraries. The download includes a
README.txt file (in the /GUI/ folder) with instructions on how to download these
libraries and run the GUI.

Currently, the GUI supports:

-  Continuous or singular measurements
-  Plotting of multiple measurements or sweeps
-  Saving of measurement data
-  18 display modes in SI units
-  Automatic and manual gain selection
-  Frequency, offset, magnitude and average settings
-  Calibrated measurements (but not the process of calibrating the board)
-  And more!

.. image:: images/admx2001b_python_gui_example.png
   :align: center
   :width: 400

The Python GUI is bundled with the latest firmware downloads and available by
request. First, make a myAnalog account on :adi:`(analog.com) <en/index.html>`
by clicking in the top right. Then, email admx-support@analog.com, and mention
the email associated with the myAnalog account.

Support
~~~~~~~

For support, general questions, or firmware update help, reach out to
admx-support@analog.com. `External Link <http://example.com>`_
