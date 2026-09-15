.. imported from: https://wiki.analog.com/resources/eval/user-guides/pa-array-biasing-reference-design

.. _pa-array-biasing-reference-design:

Power Amplifier (PA) Array Controller User Guide
================================================

Overview
--------

The optimal performance of RF power amplifiers depends on precise biasing
control, which enhances factors like linearity and efficiency. GaN HEMTs have
proven superior in high-frequency and high-power RF applications but require
careful bias voltage timing to prevent device damage. To ensure safe and
reliable operation, proper biasing sequence and protection are essential. This
reference design utilizes ADI"s portfolio for control, protection, and
appropriate bias sequencing of RF power amplifier arrays designed for massive
MIMO and macro base-station applications. The system manages the power-up and
power-down progression of Power Amplifier arrays while continuously monitoring
the system"s crucial parameters.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/block_diagram.jpg
   :width: 600px

   Figure 1. System Architecture

The conventional approach of powering up and powering down of GaN amplifiers
involves using multiple bench power supplies and manually turning them on and
off based on the specific amplifier requirements. However, this method carries a
high risk of damaging the amplifier due to potential human errors and is neither
time-efficient nor cost-effective.

The PA Array Board reference design helps address these challenges, this
innovative reference design eliminates human errors and fully automates the
power-up and power-down procedure, ensuring the safe and reliable operation of
GaN amplifiers.

Features
--------

- Fault Event Protection – undervoltage, overvoltage,overcurrent,
  overtemperature.
- Fast GaN gate voltages settling time ~ <5 microseconds
- Fast fault event to gate pinch-off time ~ <10 microseconds
- Wide range of gate bias voltages +/- 10V
- Precise power-up and down sequence of up to two GaN HEMTs-based amplifier

Applications
------------

- 5G massive MIMOs
- Macro base-stations

Reference Design Hardware
-------------------------

Primary Side
~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/hw_top_label.jpg
   :width: 600px

.. note::

   *Figure 2. Top View*

Power Supply Connectors
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/power_input.jpg
   :width: 200px

- These connectors are used to supply +48V to the entire circuitry. The PA Array
  Controller Board provides an option for the user to use either a barrel jack
  connector or a two-wire terminal.

  - P1 is a power barrel connector jack. The user can use this port if they have
    a +48V barrel jack.
  - P2 is a two-port terminal connector. Any bench power supply can use this
    port. Make sure to properly connect the positive and negative terminals of
    the power supply.

- The user can choose either of the two power supply connectors, P1 or P2. Note
  that using these two connectors at the same time is not recommended and can
  incur damage to the board.

LED Indicators
^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/LED.jpg
   :width: 200px

- The reference design uses four LEDs to indicate its current status:
- DS1 LED indicates that there is a fault event occurring on the first GaN
  amplifier .
- DS2 LED indicates that there is a fault event occurring on the pre-driver and
  driver amplifiers .
- DS3 LED indicates normal operation and good power regulation.
- DS4 LED indicates that there is a fault event occurring on the second GaN
  amplifier .

Peripheral Connectors
^^^^^^^^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/peripherals.jpg
   :width: 200px

- These connectors are used for debugging, programming, and communication
  between the software and hardware.
- P5 -> USB UART-SERIAL Communication
- P6 -> SWD Debugger

Switches
^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/switch.jpg
   :width: 200px

- The main purpose of the switches is to reset a certain device:
- S1 -> LTC7000_1 Reset
- S2 -> LTC7000_2 Reset
- S3 -> MAX32666 Microcontroller Reset
- S4 -> LTC7000_3 Reset

Test Points
^^^^^^^^^^^

- The reference design board is composed of several test points. The table below
  describes some of the most significant test points and their descriptions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/test_points.jpg
   :width: 500px

.. list-table::
   :header-rows: 1

   * - Test Points
     -
     -
   * - **TP Name**
     - **Description**
     - **Voltage**
   * - TP3
     - U1 LTC7000_1 Output
     - +48V
   * - TP6
     - U2 LTC7000_2 Output
     - +48V
   * - TP22
     - U25 LTC7000_3 Output
     - +48V
   * - TP11
     - U6 MAX17643 Output
     - +5.6V
   * - TP15
     - U10 LT3471 Positive Output
     - +12V
   * - TP16
     - U10 LT3471 Negative Output
     - -12V
   * - TP8
     - U3 ADM7172 LDO Output
     - +5V
   * - TP10
     - U5 LT3042 LDO Output
     - +5V
   * - TP9
     - U4 LT3042 LDO Output
     - +5V
   * - TP14
     - U9 ADM7150 LDO Output
     - +5V
   * - TP13
     - U8 ADM7170 LDOOutput
     - +1.8V
   * - TP12
     - U7 ADM7170 LDO Output
     - +3.3V
   * - TP17
     - U11 ADP161 LDO Output
     - +1.1V

Pin Turrets and Hooks
^^^^^^^^^^^^^^^^^^^^^

- The PA Array Controler Board was designed for specific power amplifiers and is
  used on the RF signal chain as shown below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/8t8r_signal_chain.jpg
   :width: 800px

.. note::

   *Figure 3. RF Signal Chain*

::

   *The bias lines of these amplifiers must be connected to their desired pinouts on the reference design board. Refer to the table below for the correct pin assignments.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/pinouts.jpg
   :width: 500px

.. note::

   .. list-table::
      :header-rows: 1

      * - Pin Assignments
        -
        -
      * - **Pin Name**
        - **Description**
        - **Pin Type**
      * - 5V0_802
        - HMC802A VDD Pin
        - Hook
      * - EN_802
        - HMC802A Enable Pin
        - Hook
      * - 5V0_PDA
        - ADL5611 VPOS Pin
        - Hook
      * - 5V0_DA
        - BTS6201U VCC Pin
        - Hook
      * - EN_DA
        - BTS6201U Enable Pin
        - Hook
      * - VDC1
        - A5M36TG140 LDMOS Carrier Drain Pin
        - Hook
      * - VDP1
        - A5M36TG140 LDMOS Peaking Drain Pin
        - Hook
      * - VGC1
        - A5M36TG140 LDMOS Carrier Gate Pin
        - Hook
      * - VGP1
        - A5M36TG140 LDMOS Peaking Gate Pin
        - Hook
      * - VDC2
        - A5M36TG140 GaN Carrier Drain Pin
        - Turret
      * - VDP2
        - A5M36TG140 GaN Peaking Drain Pin
        - Turret
      * - VGC2
        - A5M36TG140 GaN Carrier Gate Pin
        - Hook
      * - VGP2
        - A5M36TG140 GaN Peaking Gate Pin
        - Hook
      * - VD1
        - GTRB384608FC-V1 GaN Main Drain Pin
        - Turret
      * - VD2
        - GTRB384608FC-V1 GaN Peak Drain Pin
        - Turret
      * - VG1
        - GTRB384608FC-V1 GaN Main Gate Pin
        - Hook
      * - VG2
        - GTRB384608FC-V1 GaN Peak Gate Pin
        - Hook

Secondary Side
~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/hw_bottom.png
   :width: 350px

.. note::

   *Figure 4. Bottom View*

--------------

System Setup
------------

Note that this user guide only allows the user to test and measure the time
transition of the following:

- AD3552R DAC settling time

  - From pinch-off to normal operating voltage
  - From normal operating to pinch-off voltage

- Fault detection up to DAC pinch-off voltage

.. note::

   The PA Array Controller Board was not fully characterized so this user guide
   only test and measure the settling time of the three DACs and fault
   detection.

Requirements
~~~~~~~~~~~~

The following is the list of items needed to replicate the timing test.

Hardware
^^^^^^^^

- PA Array Controller Board
- One (1) Programmable Power Supply.

  - It should accommodate a voltage level of +30V to +60V.

- Two (2) micro-USB to USB cable.

  - For UART-Serial communication
  - For SWD Debugger

- One (1)MAX32625-PICO with SWD cable
- One (1) 4-channel oscilloscope
- One (1) Oscilloscope probe
- Six (6) 10nF capacitors - act as a load for all 6 Gate pins

.. important::

   Warning: The PA Array Controller Board was not fully characterized yet. So,
   we **do not** recommend using the actual amplifiers as a load, but instead,
   use a 10 nF capacitor.

Firmware
^^^^^^^^

- To properly load the firmware onto the board, simply drag and drop the
  provided .hex file to the DAPLINK drive. Using the drag-and-drop method, the
  software is going to be a version that Analog Devices creates for testing and
  evaluation purposes. This is the EASIEST way to get started with the reference
  design.

General Test Setup
~~~~~~~~~~~~~~~~~~

This section describes the basic setup and connections in order for the user to
bring up the board.

Hardware Setup
^^^^^^^^^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/hw_setup.jpg
   :width: 700px

   Figure 5. Setting up the hardware

#. First, connect the 10-pin SWD debug cable to port P6 of the PA Array Board.
#. Next is to connect the other end of the SWD debug cable to the MAX32625 Pico.
#. Use the micro-USB to USB cable to connect the MAX32625 Pico to your
   PC/Laptop. This connection allows the user to upload firmware to the board.
#. Then, connect the other micro-USB to USB cable to port P5. This connection
   allows the USB-UART communication that enables the user to access the
   Graphical User Interface (GUI).
#. From your PC, open My Computer and look for the DAPLINK drive, if you see
   this then the drivers are complete and correct.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/daplink.jpg
      :width: 300px

      Figure 6. DAPLINK Drive

#. Connect the positive terminal of the +48V Power Supply to port P2.1.
#. Then, connect the negative terminal to port P2.2. Do not turn-on the power
   supply yet.
#. Lastly, connect the osc probe to the oscilloscope.

Software Setup
^^^^^^^^^^^^^^

#. The board has already been pre-loaded with firmware v0.0.10112023[BETA]P0_21.
#. If the user would like to re-upload the firmware again, simply drag and drop
   the provided ADI PA Array Firmware v0.0.10112023[BETA] (.hex) file onto the
   DAPLINNK drive.
#. To access the graphical user interface (GUI), open the provided PA Array UI
   (.exe) file. For a better understanding of the GUI"s functionality and
   features, please refer to the image provided below, which offers a concise
   description of the graphical user interface.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/gui_dashboard.png
   :width: 600px

   Figure 7. Dashboard

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/gui_home.png
   :width: 600px

   Figure 8. Monitor and Control Panel

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/gui_des1.png
   :width: 600px

   Figure 9. GUI Overview

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/gui_des2.png
   :width: 600px

   Figure 10. GUI Historical Graph

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/gui_des3.png
   :width: 600px

   Figure 11. GUI Device Group

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/gui_des4.png
   :width: 600px

   Figure 12. GUI Control Group

Basic Operation
^^^^^^^^^^^^^^^

#. Now that we are finished setting up the hardware and firmware. We will begin
   to measure the timing response of each AD3552R DAC"s.
#. Let"s start to measure the settling time of the DAC on the GaN gate pins
   (VGC2, VGP2, VG1, VG2).
#. Connect a 10nF capacitive load on each GAN gate pins (VGC2, VGP2, VG1, VG2)
   pin with respect to ground.
#. The positive and negative terminals of all channels of the oscilloscope probe
   must connect in parallel to each of the capacitor pins.
#. Now, set the required configurations of the oscilloscope:

   - -3V on rising edge trigger value.
   - 1us/div and 2V/div.

#. Refer to Figure 5 for the complete hardware setup.
#. Upon board boot-up, the default voltages on the GaN gate pins are the
   pinch-off voltages (-5V).
#. On the GUI, the user has the freedom to choose any voltage they desire from
   -10V to +10V range. For our example, let"s set all the carrier and peak gates
   to their corresponding operating voltages.

   #. VGC2: -2V
   #. VGP2: -2.6V
   #. VG1: -2.75V
   #. VG2: -2.75V

#. There are two ways to set the voltages. The first is by using the spin box
   and the second is by using the slider.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/gan1_gan2_set.jpg
      :width: 400px

      Figure 7. Setting the GaN gate voltages through GUI

#. Once the voltages are entered, press the set button. Do this process on each
   of the GaN gates to replicate the oscilloscope result.
#. You will see the voltage translation from pinch-off to operating voltage. The
   oscilloscope will display the voltage transition and the time response. The
   result should be the same as the images below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgc2_pwr_up_time.png
      :width: 500px

      Figure 7. VGC2 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgp2_pwr_up_time.png
      :width: 500px

      Figure 8. VGP2 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vg1_vg2_pwr_up_time.png
      :width: 500px

      Figure 9. VG1 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vg1_vg2_pwr_up_time.png
      :width: 500px

      Figure 10. VG2 Voltage Time Response

#. Let"s measure this time the DAC voltage transition of the LDMOS gate pins
   (VGC1, VGP1).
#. Connect a 10nF capacitive load on each LDMOS gate pins (VGC1, VGP1) pin with
   respect to ground.
#. The positive and negative terminals of the oscilloscope probe must connect in
   parallel to each of the capacitor pins.
#. Adjust oscilloscope settings:

- Trigger value: +1V on rising edge

#. The default voltages of the LDMOS gate pins are pinch-off voltages (0V). Set
   the gate to its operating voltages.

- VGC1: +3.8V
- VGP1: +1.9V

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/ldmos_set.jpg
      :width: 200px

      Figure 7. Setting the LDMOS gate voltages through GUI

#. Once the voltages are entered, press the set button. You will see the voltage
   translation from pinch-off to operating voltage. The oscilloscope will
   display the voltage transition and the time response. The result should be
   the same as the images below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgc1_pwr_up_time.png
      :width: 500px

      Figure 11. VGC1 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgp1_pwr_up_time.png
      :width: 500px

      Figure 12. VGP1 Voltage Time Response

#. At this point, all the gate pins are in the normal operating voltage state.
   We are now ready to measure the voltage transition from normal operating to
   pinch-off voltage.
#. Connect all 4-channels of the oscilloscope probes in parallel with all the
   capacitor pins.
#. Adjust oscilloscope settings:

- Trigger value: -3V on falling edge

#. Set the gate voltages to their pinch-off voltages.

- VGC2: -5V
- VGP2: -5V
- VGC1: 0V
- VGP1: 0V
- VG1: -5V
- VG2: -5V

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/pinch_off_set.jpg
      :width: 600px

      Figure 7. Setting the GaN gate voltages through GUI

#. Press the set button to reflect the changes. The result should be the same as
   the image below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgc2_pwr_dwn_time.png
      :width: 500px

      Figure 13. VGC2 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgp2_pwr_dwn_time.png
      :width: 500px

      Figure 14. VGP2 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vg1_vg2_pwr_dwn_time.png
      :width: 500px

      Figure 15. VG1 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vg1_vg2_pwr_dwn_time.png
      :width: 500px

      Figure 16. VG2 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgc1_pwr_dwn_time.png
      :width: 500px

      Figure 17. VGC1 Voltage Time Response

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/vgp1_pwr_dwn_time.png
      :width: 500px

      Figure 18. VGP1 Voltage Time Response

   .. note::

      Please note that the capacitor value used in the feedback loop of the
      trans-impedance amplifier is 100 pF. The relationship between speed and
      oscillation ripple is inversely proportional. We can achieve a faster
      settling time but must sacrifice a much cleaner oscillation, and vice versa.

#. We are done capturing the voltage transition from power-up and power-down.
   Now, we will capture the time it takes from when the fault is detected until
   the DAC outputs the gate pinch-off voltage.
#. We have already gathered data from the fault protection circuit, LTC7000.
   When it detects a fault event, it sends a signal from LTC7000 to the MCU in
   approximately 1 microsecond. This value will then be added to the system
   power-down measurement and the time it takes for the MCU to process the fault
   flag up to the DAC command.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/flag_time.png
      :width: 500px

      Figure 19. LTC7000 -> MCU GPIO Fault Flag Time

#. Follow the below steps:
#. Place the positive terminal of the oscilloscope probe into the provided wire
   as shown in the image below. Then connect the negative terminal of the
   oscilloscope probe to the GND of the board.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/fault_setup.jpg
      :width: 500px

      Figure 20. Fault Detection Time Measurement Setup

#. Set the required oscilloscope settings.

- Trigger value: +1V
- 1us/div and 1V/div

#. For this test, we will introduce an overvoltage fault. To do this, increase
   the voltage from the external power supply from +48V to +56V. This will cause
   a fault event since the preset threshold for an overvoltage is +55V.
#. The oscilloscope will display a similar time response as shown below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/mcu_time.png
      :width: 500px

      Figure 21. MCU Processing Time

#. On the GUI, it will notify the user that a fault event occurred and show a
   warning message as in the image below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/fault_detected.jpg
      :width: 500px

      Figure 21. Warning Message

#. Also, the GUI is capable of logging and displaying the fault event time and
   on which device it occurs.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/fault_log.jpg
      :width: 300px

      Figure 21. Fault Logging

#. The overall time from LTC7000 fault detection up to the DAC pinch-off voltage
   is shown on the Fault Event Time Summary below.

--------------

Summary of Results
~~~~~~~~~~~~~~~~~~

System Power Up and System Power Down Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The below table shows the summary of our time response test for each DAC"s. As
  shown below, we achieved the <5us time requirement.

.. list-table::
   :header-rows: 1

   * - Timing Response
     -
     -
     -
     -
     -
   * - **Pin Name**
     - **Description**
     - **Pinch-off voltage (V)**
     - **Operating Voltage (V)**
     - **Power-up time (us)**
     - **Power-down time (us)**
   * - VGC1
     - A5M36TG140 LDMOS Carrier Gate
     - 0
     - +3.8
     - 2.09
     - 2.25
   * - VGP1
     - A5M36TG140 LDMOS Peaking Gate
     - 0
     - +1.9
     - 1.65
     - 2.01
   * - VGC2
     - A5M36TG140 GaN Carrier Gate
     - -5
     - -2
     - 1.95
     - 2.05
   * - VGP2
     - A5M36TG140 GaN Peaking Gate
     - -5
     - -2.6
     - 1.73
     - 1.95
   * - VG1
     - GTRB384608FC-V1 GaN Main Gate
     - -5
     - -2.75
     - 1.81
     - 2.00
   * - VG2
     - GTRB384608FC-V1 GaN Peak Gate
     - -5
     - -2.75
     - 1.81
     - 2.00

.. note::

   *Table 1. Gate Voltages Timing response Summary*

- Power-up time -> from pinch-off voltage to operating voltage.
- Power-down time -> from operating voltage to pinch-off voltage.

Fault Event Time Response Summary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The below table shows the summary of our time response test when a fault
  occurs. As shown below, we achieved the <10us time requirement.
- The total time from fault detection up to the gate pinch-off is given by:
- Total time = Fault flag (us) + MCU Processing time (us) + RF switch time (us)
  + highest power down time between VGC2, VGP2,VG1,VG2 (us) + highest power down
  time between VGC1, VGP1
- Total time = 1.0898 us + 3.7078 us + 0.3 us + 2.05 us + 2.25 us
- Total time = 9.4 us

Fault flag time -> time it takes for the MCU to recognize that there is a fault
signal coming from the LTC7000.

MCU processing time -> total time for MCU to process the fault flag signal up to
commanding the DAC.

RF switch time -> total time for the RF switch to turn-off

Power-down time -> DAC output from operating voltage to pinch-off.

Total time -> time from fault detection to Vgg pinch-off

--------------

Miscellaneous Measurements
~~~~~~~~~~~~~~~~~~~~~~~~~~

As per the customer"s request, we are able to test and measure the DAC settling
time from these specified voltage levels

- Pinch-off voltage: -7V
- Operating voltage: -1.2V

Do note that the firmware loaded on the board doesn"t include these
measurements. We can send a separate firmware if necessary.

-7V to -1.2V DAC Settling Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The DAC output voltage settling time from -7V pinch-off to -1.2V is 2.31us. See the image below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/-7vto-1.2v.png
   :width: 500px

   Figure 22. -7V to -1.2V DAC Settling Time

-1.2V to -7V DAC Settling Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The DAC output voltage settling time from -1.2V pinch-off to -2V is 2.31us. See the image below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/pa_array/-1.2vto-7v.png
   :width: 500px

   Figure 23. -1.2V to -7V DAC Settling Time

*End of Document*
