.. _ad-paarray3552r-sl hardware-guide:

Hardware User Guide
====================

Introduction
-------------

The :adi:`AD-PAARRAY3552R-SL` is designed in a small form
factor to manage the power sequencing of an RF transmitter signal chain, and is
engineered to facilitate power sequencing for a two-stage Doherty amplifier
(LDMOS + GaN) along with a one-stage Doherty amplifier (GaN only). However,
users have the freedom to employ any GaN amplifiers of their choice.

The design incorporates the :adi:`AD3552R` dual-channel, 16-bit DAC
which allows an ultrafast sub-µs Voltage settling time of GaN gates from
pinch-off to the normal operating Voltage.

This also includes a high-side NMOS static switch driver,
:adi:`LTC7000`, which adeptly handles key fault events such as
overvoltage, overcurrent, and overtemperature.

The on-board :adi:`MAX32666` ultralow power Arm Cortex®-M4
microcontroller exposes all the necessary debug and programming features to
enable a complete software development experience with the system. The system’s
firmware is based on ADI’s open-source no-OS framework and a user-friendly
graphical user interface (GUI) for evaluation and further development.

The system can be powered from an external +38V to +55V supply, making it
suitable for applications requiring high current capabilities.

Board Specifications
--------------------

**Dimension:**

- Length: 4 inch (101.6 mm)
- Width: 2.7 inch (68.58 mm)
- Thickness: 0.062 inch (1.62 mm)

- PCB Material: FR4 ISOLA 370HR
- No. of layers: 6

  - Top Layer (Component, Signal Layer, 90 Ω differential)
  - Ground Plane
  - Signal Layer
  - Power Plane
  - Ground Plane
  - Bottom Layer (Component, Signal Layer)

Components and Connections
--------------------------

Primary Side
~~~~~~~~~~~~~

.. figure:: ad-paarray3552r-sl_front_view.png

   AD-PAARRAY3552R-SL Top

Power Supply Connectors
^^^^^^^^^^^^^^^^^^^^^^^^

These connectors are used to supply +48V to the entire circuitry.
The :adi:`AD-PAARRAY3552R-SL` provides an option for the
user to use either a barrel jack connector or a two-wire terminal.

- **P1** - Barrel connector jack. Use this port if a 5.5 mm x 2.5 mm barrel jack
  adapter is preferred.
- **P2** - Two-port terminal connector. Port for supply power through
  non-terminated wires. Ensure proper connection to the positive and negative
  terminals of the power supply.

.. important::
   **Supply power to either P1 or P2 only and not at the same time**
   Supplying power to both terminals may cause permanent damage to the device.

LED Indicators
^^^^^^^^^^^^^^

Three indicator LEDs to display the board’s current status:

- **DS1** - Indicates that a fault event (overvoltage or overcurrent).
- **DS2** - Indicates that a fault event (overtemperature).
- **DS3** - Indicates normal operation and good power regulation.

Peripheral Connectors
^^^^^^^^^^^^^^^^^^^^^

These connectors are used for debugging, programming, and communication
between the software and hardware.

- **P5** - USB-to-UART Serial Communication through micro-USB to USB cable
- **P6** - Programming and debugging using 10-pin SWD cable

Switches
^^^^^^^^

Hardware switches used to reset specific devices:

- **S3** - MAX32666 Microcontroller Reset

Test Points
^^^^^^^^^^^

The reference design board is comprised of several test points. The table
below describes  some of the most significant test points and
their descriptions.

.. figure:: ad-paarray3552r-sl_test_points.png

   AD-PAARRAY3552R-SL Test Points

=========== ========================== ===========
**TP Name** **Description**            **Voltage**
=========== ========================== ===========
TP6         U2 LTC7000 Output          +48V
TP8         U3 ADM7172 LDO Output      +5V
TP9         U4 LT3042 LDO Output       +5V
TP10        U5 LT3042 LDO Output       +5V
TP11        U6 MAX17643 Output         +5.6V
TP12        U7 ADM7170 LDO Output      +3.3V
TP13        U8 ADM7170 LDO Output      +1.8V
TP14        U9 ADM7150 LDO Output      +5V
TP15        U10 LT3471 Positive Output +12V
TP16        U10 LT3471 Negative Output -12V
=========== ========================== ===========

Pin Turrets and Hooks
^^^^^^^^^^^^^^^^^^^^^^

The :adi:`AD-PAARRAY3552R-SL` is designed for specific power amplifiers
and is used on the RF signal chain, as shown below.

.. figure:: ad-paarray3552r-sl_03.png

   RF Signal Chain

The bias lines of these amplifiers must be connected to the designated pinout
on the reference design board. Refer to the table below for the correct pin
assignments.

=============== =============================== ============
Pin Assignments
=============== =============================== ============
**Pin Name**    **Description**                 **Pin Type**
5V0_SW          RF Switch +5V Pin               Hook
EN_SW           RF Switch Enable Pin            Hook
5V0_PDA         Pre-driver Amplifier +5V Pin    Hook
5V0_DA          Driver Amplifier +5V Pin        Hook
EN_DA           Driver Amplifier Enable Pin     Hook
VDC1            Doherty LDMOS Carrier Drain Pin Hook
VDP1            Doherty LDMOS Peaking Drain Pin Hook
VGC1            Doherty LDMOS Carrier Gate Pin  Hook
VGP1            Doherty LDMOS Peaking Gate Pin  Hook
VDC2            Doherty GaN Carrier Drain Pin   Turret
VDP2            Doherty GaN Peaking Drain Pin   Turret
VGC2            Doherty GaN Carrier Gate Pin    Hook
VGP2            Doherty GaN Peaking Gate Pin    Hook
VD1             GaN Main Drain Pin              Turret
VD2             GaN Peak Drain Pin              Turret
VG1             GaN Main Gate Pin               Hook
VG2             GaN Peak Gate Pin               Hook
=============== =============================== ============

Secondary Side
~~~~~~~~~~~~~~~

.. figure:: ad-paarray3552r-sl_bottom.png

   AD-PAARRAY3552R-SL Bottom Side

SMD Packaging Provision
^^^^^^^^^^^^^^^^^^^^^^^^

- For easy evaluation, the board incorporates unpopulated SMD chip pads for
  1210, 1206, 0805, and 0603 packaging. This allows the user to easily install a
  capacitive load of their choice.

Hardware Evaluation
~~~~~~~~~~~~~~~~~~~~

Equipment Needed
^^^^^^^^^^^^^^^^

- :adi:`AD-PAARRAY3552R-SL`
- One (1) :adi:`MAX32625PICO` rapid development platform with
  10-pin SWD cable and with updated firmware: :ref:`see firmware update
  instructions <ad-paarray3552r-sl software-guide>`
- One (1) :adi:`HMC8500` GaN Power Amplifier Evaluation Board
- One (1) :adi:`HMC849A` RF Switch Evaluation Board
- One (1) :adi:`ADL5611` Gain Block AmplifierEvaluation Board
- One (1) +5V to +60V programmable power supply
- Two (2) micro-USB to USB cable
- One (1) Signal Generator
- One (1) Spectrum Analyzer
- Two (2) SMA to SMA male cables
- Host Windows PC:
   -  with 2 free USB-A ports
   -  with installed control GUI:
      :ref:`see installation guide <ad-paarray3552r-sl software-guide>`

Board Modification
^^^^^^^^^^^^^^^^^^^

The AD-PAARRAY3552R-SL requires some hardware modifications, which will depend
on the amplifier you plan to use. Here are the parameters that need modification
before using the board:

- Fault Settings
- Inrush Current Limiter

Fault Settings
^^^^^^^^^^^^^^

The hardware is capable of detecting fault events such as overvoltage,
overcurrent, and overtemperature. Below are the default settings for
these fault events. You will need to adjust these settings based on the
power amplifier you are using.

- Overvoltage: +55V
- Undervoltage: +38V
- Overcurrent: 3.5A
- Overtemperature: +75°C

**Overvoltage Settings**

The LTC7000s OVLO pin manages the overvoltage event. If the voltage on this pin
exceeds 1.21V, an overvoltage fault will be flagged. Below are the default
resistor values for a +55V and +60V overvoltage. Adjust the following resistor
values to set your desired overvoltage. Refer to :adi:`LTC7000` datasheet for
more information.

- +55V overvoltage
  - R3, R114 = 1Meg
  - R4, R115 = 22.6K

- +60V overvoltage
  - R24 = 1Meg
  - R25 = 21K

**Undervoltage Settings**

The LTC7000s RUN pin manages the undervoltage event. If the voltage on this pin
falls below 1.11V, an undervoltage fault will be flagged. Below are the default
resistor values for a +38V and +6V undervoltage. Adjust the following resistor
values to set your desired undervoltage. (Please note that the LTC7000 does not
support a fault flag on its FAULT pin when an undervoltage event occurs, so we
are unable to detect this kind of fault. However, the device will automatically
shut off in such a case). Refer to :adi:`LTC7000` datasheet for more
information.

- +38V undervoltage
  - R156, R177 = 1Meg
  - R172, R160 = 29.4K

- +6V undervoltage
  - R26 = 1Meg
  - R23 = 221K

**Overcurrent Settings**

The LTC7000's SNS and ISET pin are responsible for the
overvoltage event. Below are the default resistor values for a 3.5A
overcurrent. Adjust the following resistor values to set your desired
overcurrent. Refer to :adi:`LTC7000` datasheet for more information.

- R9, R31, R120 = 0.015 (R_SENSE)
- R12, R34, R123 = 105K (R_ISET)

**Overtemperature Settings**

The MAX6516 is manages the overvoltage event. You can adjust the hysteresis to
your desired value.

==================== ============================ ============================
Hysteresis Settings
==================== ============================ ============================
**Hysteresis Point** **R144**                     **R146**
2°C                  Populate with 0-ohm resistor DNI/NC
10°C                 DNI/NC                       Populate with 0-ohm resistor
==================== ============================ ============================

For this demo, we will be using the HMC8500 GaN Power Amplifier with an
operating drain voltage of +28V (absolute max = +35V). It will have the
following fault settings and its corresponding resistor values.

+----------------+-------------------+---------------------+-------------+
| Fault          | Set Value         | Resistor Value      | Remarks     |
+================+===================+=====================+=============+
| Overvoltage    | + 35V             | R3, R114 = 1 Meg;   | U1, U25     |
|                |                   | R4, R115 = 37.4K    |             |
+----------------+-------------------+---------------------+-------------+
| Overvoltage    | + 60V             | R24 = 1 Meg; R25 =  | U2          |
|                |                   | 21K                 |             |
+----------------+-------------------+---------------------+-------------+
| Undervoltage   | + 20V             | R156, R177 = 1 Meg; | U1, U25     |
|                |                   | R160, R172 = 57.6K  |             |
+----------------+-------------------+---------------------+-------------+
| Undervoltage   | + 6V              | R26 = 1 Meg; R23 =  | U2          |
|                |                   | 221K                |             |
+----------------+-------------------+---------------------+-------------+
| Overcurrent    | + 3.5A            | R9, R31, R120 =     | U1, U2, U25 |
|                |                   | 0.015; R12, R34,    |             |
|                |                   | R123 = 105K         |             |
+----------------+-------------------+---------------------+-------------+
| Overvoltage    | + 10°C Hysteresis | R144 = DNI/NC; R146 | U24         |
|                |                   | = 0                 |             |
+----------------+-------------------+---------------------+-------------+

Inrush Current Limiter
~~~~~~~~~~~~~~~~~~~~~~

Driving large capacitive loads such as complex electrical systems with large
bypass capacitors should be powered using the circuit shown in the figure
below.

.. figure:: inrush_current_limiter.png

   Inrush Current Limiter Circuit

The pull-up gate drive to the power MOSFET from TGUP is passed through an RC
delay network, RG and CG, which greatly reduces the turn-on ramp rate of the
MOSFET. This dramatically reduces the inrush current from the source supply and
reduces the transient ramp rate of the load allowing for slower activation of
sensitive electrical loads such as power amplifiers.

The turn-off of the MOSFET is not affected by the RC delay network as the
pull-down for the MOSFET gate is directly from the TGDN pin. Note that the
voltage rating on capacitor CG needs to be the same or higher than the external
MOSFET and CLOAD.

The values for RG and CG to limit the inrush current can be calculated from the
below equation:

.. figure:: formula.png

On this application, we will use a <100mA inrush current.

     * Inrush current = 100mA
     * CLOAD = 20uF (HMC8500 Drain Bypass Capacitor)
     * CG = 10nF (assumed)

Using the formula above, RG = 200K.

=============================== ============== ==================
Inrush Current Limiter Settings
=============================== ============== ==================
**Parameters**                  ``Refdes``     **ResistorValue**
RG                              R11, R33, R122 200K
GC                              C10,C21,C164   10nF
RS                              R14,R36,R125   10 ohms
=============================== ============== ==================

.. Note::
   The default inrush current circuitry (RG, RS, CG) on the board is not
   populated. The user will need to modify the board and install the appropriate
   values before using it.

General Setup
-------------

#. Connect the 10-pin SWD cable to port P6 of the
   :adi:`AD-PAARRAY3552R-SL`.
#. Connect the other end of the SWD cable to the
   :adi:`MAX32625PICO`.
#. Use the micro-USB to USB cable to connect the MAX32625PICO to PC or laptop.
   This connection allows the user to upload firmware to the board.
#. Then, connect the other micro-USB to USB cable to port P5. This connection
   enables USB-to-UART communication.

   .. figure:: uart_connection.png

      UART Connection

#. Connect the positive terminal of the bench power supply to port P2.1.
#. Connect the negative terminal of the bench power supply to port P2.2.
#. Set the power supply voltage to +28V before turning it on. Note: The default
   undervoltage settings were set to +38V. The user needs to modify the hardware
   by changing the resistor values to perform the +28V drain voltage. Refer to
   the “Board Modification Section” above.
#. Turn on the bench power supply. You will notice that DS3 (Green LED) will
   lights on.

   .. figure:: psu_connection.png

      Power Supply Connection

#. Perform the software setup indicate on the software user guide.
#. The system is designed to provide bias on a complete transmitter signal chain
   shown in Figure 3.
#. But for this demo, we will provide bias on the following Tx signal
   chain:

   .. figure:: demo_signal_chain.png

      RF Signal Chain for Demo

#. For safety measures, turn off the bench power supply.
#. Set the signal generator with the following settings:

   - Frequency: 2.4 GHz
   - Power level: -30 dBm

      .. figure:: sig_gen_setup.png

         Signal Generator Setup

#. Set the spectrum analyzer with the following settings:

   - Center frequency: 2.4 GHz
   - Frequency Span: 500 MHz
   - Resolution: Adjust depending on your choice.
   - Amplitude: +20 dBm
   - Marker is at 2.4 GHz

      .. figure:: sig_analyzer_setup.png

         Signal Analyzer Setup

#. Don’t turn on the signal generator yet.
#. Cascade the RF devices by the following chain:
   **HMC849A** -> **ADL5611** -> **HMC8500**

   .. figure:: cascaded_devices.png

      Cascaded Devices

#. Connect the RF input/output of the signal chain to the signal generator and
   spectrum analyzer, respectively.
#. Connect the GND pin of the two HMC8500 to the GND pin of the
   AD-PAARRAY3552R-SL board.
#. Connect the gate pins (VGG) of the HMC8500 to the VG1 and VG2 pins of the
   AD-PAARRAY3552R-SL board, respectively.
#. Connect the drain pins (VDD) of the HMC8500 to the VD1 and VD2 pins of the
   AD-PAARRAY3552R-SL board, respectively.
#. Connect the ADL5611VCC to 5V_PDA pin of the AD-PAARRAY3552R-SL.
#. Connect the HMC849AVDD to 5V_SW and the HMC849AVCTL to EN_SW of the
   AD-PAARRAY3552R-SL. Connect the EN of the HMC849A to the GND.
#. Turn on the +28V bench power supply once again. You will notice that DS3
   (Green LED) lights up, indicating proper
   power-up.

   .. figure:: overall_setup.png

      Overall Hardware Setup

#. Open the GUI Application. In the GUI Homepage, click the ``Go`` button under
   “Device Monitoring and Control”.

   .. figure:: gui_home.png

      GUI Homepage

#. It will show the GUI dashboard. On the device connection, choose the correct
   Serial Port. Then, press the ``Connect`` button.
#. Wait until the HW-SW connection is successful.
#. In the software setup section, you will find the complete details about the
   GUI.
#. The user can perform either a manual power-up/down sequence or an automatic
   power-up/down sequence.
#. For the manual power sequence, the user needs to manually adjust the knobs,
   sliders, and buttons under the “Control Group” section in the GUI according
   to the amplifier’s drain and gate voltage
   requirements.

   .. figure:: gui_control_group_main.png

      GUI Control Group

#. For the automatic power sequence, the user only needs to press the “Start”
   button of the power-up under the “Device Group” section in the GUI. It will
   automatically perform the power-up sequencing requirement of the HMC8500.
   Please note that the automatic power sequencing has default gate voltage
   levels designed for the HMC8500 GaN Power Amplifier.

   .. figure:: gui_device_group.png

      GUI Device Group

#. To change the default voltages in the automatic power sequencing, the user
   needs to modify the source code according to their power amplifier
   requirement.
#. Once properly powered up, turn on the RF signal generator. On the signal
   analyzer, you should see an amplifier RF output signal of around +12 dBm at
   2.4 GHz, indicating a successful power-up.

   .. figure:: rf_output.png

      RF Output

#. To power down, press the “Start” button of the power-down sequence and it
   automatically performs the power-down sequence requirement of the HMC8500.

System Performance
------------------

Power Sequencing
~~~~~~~~~~~~~~~~

The system exhibits an automated bias sequencing required by a power amplifier
which minimizes human intervention and possible device damage. The default bias
sequence implemented follows the common GaN power amplifier
sequencing as shown below.

.. figure:: bias_sequencing_gan.png

   GaN Power Sequence

.. figure:: ldmos.png.jpg

   LDMOS Power Sequence

AD3552R DAC Settling Time
~~~~~~~~~~~~~~~~~~~~~~~~~

The system enables an ultrafast sub-µs voltage settling time
for GaN gates from pinch-off to the normal operating voltage
by utilizing the AD3553R dual-channel, ultrafast, 16-bit DAC.
This rapid voltage transition allows the board to meet the TDD
switching requirements for biasing a GaN amplifier in RF front-end
applications, such as 5G base station radio units.

The typical voltage transition time from GaN pinch-off to its normal
operating voltage is shown in the figure below.

.. figure:: pinch_off_to_normal.png

   Settling Time from Pinch-off to Normal

.. figure:: normal_to_pinch_off.png

   Settling Time from Normal to Pinch-off

Fault Event
~~~~~~~~~~~

The system can protect itself against undesirable fault incidents,
such as overvoltage, overcurrent, and overtemperature events.
The on-board :adi:`LTC7000` handles overvoltage (OV) and overcurrent (OC)
fault detection, while the :adi:`MAX6516` is responsible for temperature
monitoring and detection.

The table below shows the preset threshold for each parameter.

=============== =====================
Safety Features
=============== =====================
Fault Event     Fault Threshold Limit
Overvoltage     +55V
Overcurrent     3.5 A
Overtemperature +75°C
=============== =====================

.. tip::
   Users can define the fault threshold limits based on their application
   by adjusting resistor values. Consult the schematic for the resistor values.

Fault Time Response
~~~~~~~~~~~~~~~~~~~

The system also exhibits fast fault detection and flagging.

**Figure 21** shows the time elapsed from when the LTC7000 detects a fault to
when it sends a signal to the microcontroller. Under normal conditions, the
FAULT pin of the LTC7000 remains HIGH. When a fault event occurs, the FAULT pin
is pulled to GND. The system took almost 1 µs to register the fault flag time.

.. figure:: flag_time.png

   Fault Detected Time

**Figure 22** shows the time it takes for the microcontroller to process the
fault signal coming from the LTC7000 and perform the required power-down
sequencing. The system took almost 5 µs to register the fault flag time.

.. figure:: mcu_time.png

   Fault Flag Time

Thermal Performance
~~~~~~~~~~~~~~~~~~~

**Figure 23** shows the temperature of the AD-PAARRAY3552R-SL board in normal operating
conditions. This is the situation when all of the bias pins are sourcing their
specified loads under normal operations.

.. figure:: thermal.png

   Thermal Performance

Resources
---------

- :adi:`AD-PAARRAY3552R-SL Product Page <AD-PAARRAY3552R-SL>`
- :adi:`MAX32666 Product Page <MAX32666>`
- :adi:`AD3552R Product Page <AD3552R>`
- :adi:`LTC7000 Product Page <LTC7000>`

Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

  :adi:`AD-PAARRAY3552R-SL Design & Integration Files <media/en/reference-design-documentation/design-integration-files/ad-paarray3552r-sl-design-support.zip>`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Further Help
-------------

For questions and more information about this product, connect with us through
the Analog Devices Engineer Zone.

:ez:`EngineerZone Support Community <reference-designs>`
