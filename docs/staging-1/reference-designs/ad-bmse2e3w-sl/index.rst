.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-bmse2e3w-sl

.. _ad-bmse2e3w-sl:

AD-BMSE2E3W-SL User Guide
=========================

| .. note::

   We are in the process of migrating our documentation to GitHub Pages.
   | This User Guide is now available at https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-bmse2e3w-sl/index.html

.. admonition:: Download

   A concise version of this document is also available in portable document
   format:

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl-ug-2245.pdf`

   Marketing Brochure:

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/high-performance_light_electric_vehicle_bms.pdf`

Overview
--------

The **AD-BMSE2E3W-SL** is a BMS reference design for light electric vehicles
(LEVs). With a voltage range of 72 V to 96 V, this solution is suitable for
electric 2-wheeler and 3-wheeler vehicles with high current capacity ranging up
to 100 A. ​

This single-board system utilizes the best-in-class ADBMS6830 cell monitoring
chip that is capable of monitoring up to 2x 16-channel. This board also features
battery pack monitoring using the ADBMS2950. ​The ADBMS6822 dual isoSPI
transceiver provides a built-in 2-wire reversible isoSPI connection, which
simplifies the communication of BMS parts in a daisy chain configuration before
sending the data to SPI lines in the microcontroller. ​

The on-board MAX32690 MCU, when loaded with the firmware, can perform BMS
measurements such as cell voltage (average and filtered), and pack voltage and
pack current measurement. The board also has a charge, pre-charge, and discharge
mode that can be controlled by the ADBMS2950 pack monitor chip.

The AD-BMSE2E3W-SL is designed to perform either in embedded mode or using a
GUI, where it calculates the battery"s State of Charge (SoC) and State of Health
(SoH) through enhanced coulomb counting technique.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/ad-bmse2e3w-sl_angle.jpg
   :width: 500px

Features
--------

- Variable 72 V to 96 V regulated voltage range, suitable for E2W/E3W
  applications
- ASIL-D compliant and automotive grade BMS chip
- Built-in charge/pre-charge, and discharge circuitry
- 1.8 mV total measurement error for cell voltage monitoring
- High performance cell/pack voltage and current monitoring
- On-board isoSPI communication
- Low Power Cell Monitoring (LPCM) capability
- GPIO Controllable FET Monitoring
- ADBMS6830 GPIO input ready for NTC sensors
- Low Power MAX32690 MCU
- UART and CAN Communication
- SOC and SOH thru Enhanced Coulomb Counting Technique
- E2W/E3W Basic System Behavior Modes
- Embedded Application-ready (via CLI)
- With GUI capable of the following measurements and fault detection:
- Cell Monitoring
- Voltage and Current Pack Monitoring
- Charge Current Monitoring
- Discharge Current Monitoring
- Temperature Monitoring
- Cell OV/UV Detection
- Cell/GPIO Open-wire Detection
- Cell Balancing

Applications
------------

- Electric and hybrid 2-wheeler vehicles
- Electric and hybrid 3-wheeler vehicles
- Light electric vehicles

System Architecture
-------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/updated_block_diagram_72vto96v.png
   :width: 1000px

Specifications
--------------

.. list-table::
   :header-rows: 1

   * - SYSTEM
     -
     -
     -
     -
     -
   * - Parameter
     - Min
     - Typical
     - Max
     - Unit
     - Notes
   * - System Vin+ Supply Voltage from Battery
     - 60
     -
     - 100
     - V
     - Input voltage supply from battery
   * - Battery Emulator System Output Voltage
     - ~66
     -
     - 92
     - V
     - Safe output voltage from Battery Emulator
   * - Current Discharge
     -
     - 50
     - 100
     - A
     - Current rating that the BMS can deliver at discharge mode
   * - Current Charge
     - 0.3
     - 50
     - 100
     - A
     - Current rating that the BMS can deliver at pre-charge/charge mode
   * - Pre-Charge Resistor
     -
     - 3x33
     -
     - Ω
     -
   * - Charge Voltage Input
     -
     -
     - 100
     - V
     -
   * - Discharge Voltage Output
     -
     - 65
     - 92
     - V
     - Regulated voltage range
   * - FET Discharge Rise Time
     -
     -
     - 42
     - mS
     -
   * - FET Driver Discharge Input
     -
     -
     - 5
     - V
     - Coming from GPIO of ADBMS2950
   * - FET Pre-Charge/Charge Rise Time
     -
     -
     - 88
     - mS
     -
   * - FET Driver Pre-Charge/Charge Input
     -
     -
     - 5
     - V
     - Coming from GPIO of ADBMS2950
   * - FET V(gs) range
     - -20
     -
     - 20
     - V
     - Coming from GPIO of ADBMS2950
   * - FET Rds(on) range
     -
     -
     - 4.8
     - mΩ
     - Coming from GPIO of ADBMS2950
   * - ADBMS6830 Cell Monitor
     -
     -
     -
     -
     -
   * - Total Supply Voltage, V+ to V−
     - -0.3
     -
     - 85
     - V
     - 6830 chip"s total supply rating
   * - VREG Supply
     - 4.5
     - 5
     - 5.5
     - V
     -
   * - VREF1, VREF2
     - 3.0
     -
     - 3.3
     -
     - Supply to internal ADCs
   * - VRES/VDD
     - 4.5
     - 5
     - 5.5
     - V
     -
   * - Temp
     - -40
     -
     - 125
     - °C
     -
   * - CPIN Input Range
     - -2.5
     -
     - 5.5
     - V
     -
   * - Cell Count
     - 17
     -
     - 32
     -
     - Min of 17 cells for the system to initiate daisy chain
   * - Drive
     - -0.3
     -
     - 7
     - V
     - Drive voltage range with respect to each cell monitoring V-
   * - ADBMS2950 Pack Monitor
     -
     -
     -
     -
     -
   * - Main Supply Voltage In
     - 14
     -
     -
     - V
     -
   * - VREG Pack Monitor
     - 4.5
     - 5
     - 5.5
     - V
     -
   * - Current Input S1A, I1A, I1B
     - -4
     -
     - 4
     - V
     -
   * - Current Input S1A, I1A, I1B
     - -4
     -
     - 4
     - V
     -
   * - Current Input S2A, I2A, I2B
     - -4
     -
     - 4
     - V
     -
   * - Current Input I3A, I3B
     - -4
     -
     - 4
     - V
     -
   * - MAX32690 Microcontroller
     -
     -
     -
     -
     -
   * - MCU Supply Voltage from BMS
     - 3.3
     -
     - 5.5
     - V
     -
   * - MCU IO Supply for 1.8 V
     - 1.6
     -
     - 3.0
     - V
     -
   * - MCU VDD Supply
     - 3.3
     -
     - 5.5
     - V
     -
   * - MCU Supply at 1.2 V
     - 1.1
     -
     - 1.35
     - V
     -
   * - MCU Supply at 1.0 V
     - 0.9
     -
     - 1.2
     - V
     -

What"s Inside the Box?
----------------------

Upon purchase of the AD-BMSE2E3W-SL kit, the package comes with the following
boards and accessories:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/ad-bmse2e3w-sl_package_contents.png
   :width: 2000px

--------------

Components and Connections
--------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/revised_ad-bmse2e3w-sl_board_with_pin_labels.png
   :width: 3000px

.. list-table::

   * - **Hardware Part Functions**
     -
     -
   * -
     - **Part**
     - **Function**
   * - 1
     - Battery Cell Connector
     - Connector going to battery cells
   * - 2
     - ADBMS6830 (U1)
     - BMS 1 Cell Monitoring Chip with LPCM capability
   * - 3
     - ADBMS6830 (U3)
     - BMS 2 Cell Monitoring Chip with LPCM capability
   * - 4
     - NTC Provision (U1)
     - Connector for Negative Temperature Coefficient (NTC) Thermistor in
       ADBMS6830 (U1)
   * - 5
     - NTC Provision (U3)
     - Connector for Negative Temperature Coefficient (NTC) Thermistor in
       ADBMS6830 (U3)
   * - 6
     - ADBMS2950 (U5)
     - Voltage Pack and Current Pack Monitor Chip
   * - 7
     - ADBMS6822 (U10)
     - Dual isoSPI chip
   * - 8
     - VBAT+ Connector
     - Positive Terminal Connector for total voltage capacity of the battery
       pack
   * - 9
     - Rsense Pack Monitor
     - Resistor Sensing for detecting and monitoring total current in the pack
   * - 10
     - 72V to 96V LINK+_OUT Load Connector
     - Connector going to the load side of the system
   * - 11
     - 72V to 96V LINK+_IN Charger Connector
     - Connector going to the charging side of the system
   * - 12
     - CAN Connector
     - Three terminal connector provision for CAN_H, CAN_L, and GND
       communication
   * - 13
     - Micro USB Supply Provision
     - 5V DC USB supply provision
   * - 14
     - UART/SWDIO Connector
     - Connector for UART/SWDIO communication. Can be used to download program
       and debugging
   * - 15
     - MAX32690 MCU Chip
     - Low power/high power MCU chip used as controller for the system

System Evaluation
=================

Follow the setup shown in the diagram below to get the board up and running.
Ensure that the hardware parts and equipment are complete based on list of
Equipment Needed. The banana plug cables used in this setup only have a maximum
rating of 10A. Cables suitable for higher current rating must be used if the
intended application operates at range higher than 10A. Note that the
AD-BMSE2E3W-SL board can only accommodate up to 100A.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/system_evaluation_set-up.png
   :width: 2000px

Equipment Needed
----------------

- 1x AD-BMSE2E3W-SL Board
- 2x DC2472A Battery Cell Emulator Boards
- 1x MAX32625PICO Programming Adapter with 10-pin SWD cable (loaded with
  firmware image)
- 2x Cell Connector Block (18-cell connector)
- 2x USB Type A to Micro-B cable
- 2x Stackable Banana Plug to Alligator Clip Cable (BU-P1166-12-2, Red)
- 1x Stackable Banana Plug to Alligator Clip Cable (BU-P1166-12-0, Black)
- 7x Top Mount Heatsink *(to be installed for high current applications)*
- 1x Laptop or PC running Windows 10

.. warning::

   This reference design has not undergone compliant testing for EMI/ EMC
   standards for automotive. It is up for the user to do its qualification as
   the requirements vary depending on its end application or use cases.

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning

Hardware Setup
--------------

.. important::

   For high current applications requiring greater than 50 A, it is advisable to
   install a heat sink to protect the pre-charge, charge, and discharge MOSFETs
   from overheating.

   The AD-BMSE2E3W-SL Kit has 7 available **HEATSINK PIN-FIN W/TAPE
   (375424B00034G)** easy-to install, adhesive type, aluminum top mount heat
   sink than can be installed directly on top of the board.

   Peel off the protective film from the bottom of each heat sink and firmly
   press each one on top of the following FETs:

   **(1)** Attach the 5 heat sinks on the top layer of the board **(Q4, Q5, Q6,
   Q7, and Q9)**,

   **(2)** the remaining 2 heat sinks on the bottom layer of the board **(Q3 and
   Q8)**.

The board utilizes the DC2472A battery emulator as input for cell voltage
measurement. The DC2472A allows a cell voltage of 1.4 V (min) to 4.2 V (max).
Follow below steps to set up the board for cell measurement:

1. Screw the two cell connector blocks to the two DC2472A battery emulators.
   Note that the first two terminals and the last terminal of each DC2472A cell
   connector must be left hanging (refer to below figure). Make sure to also set
   the last two terminals" input to low voltage or equivalent range of roughly
   1.4V per cell.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/battery_emulator_pins.png
   :width: 800px

   **Hover mouse on this image and click CTRL twice to magnify**

2. Connect the DC2472A battery emulators to the ADBMSE2E3W-SL board through the
   cell connector blocks. Then, connect a micro-USB Type B cable to each DC2472A
   battery emulator and power the boards by connecting the other end of the
   cables to the Host PC.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/usb_emulator.png

3. Set the DC2472A battery emulators to the lowest voltage by fully turning the
   Cell Voltage Adjustment Potentiometer counterclockwise.

4. Attach the MAX32625PICO programmer to the AD-BMSE2E3W-SL board using the
   10-pin ribbon SWD cable. Power the MAX32625PICO using a micro-USB to USB
   cable connected to the Host PC.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/max32625_power_usb_pc.png

.. note::

   By default (upon purchase), the AD-BMSE2E3W-SL board comes with a
   MAX32625PICO programmer adapter that is loaded with firmware image.

   Otherwise, if you are using a new MAX32625PICO programmer (that is not part
   of the original kit), make sure to flash it first with the
   :git-max32625pico-firmware-images:`correct firmware image <raw/master/bin/max32625_max32690evkit_if_crc_swd_v1.0.7.bin+>`
   before connecting it to the AD-BMSE2E3W-SL board. If you do not know how to
   load the image, follow the instructions below:\**

   .. collapsible:: How to flash the firmware image in the MAX32625PICO

      #. Download the firmware image:
         :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32690 <raw+bin/max32625_max32690evkit_if_crc_swd_v1.0.7.bin>`
      #. Do not connect the MAX32625PICO to the AD-BMSE2E3W-SL Board yet.
      #. Connect the MAX32625PICO to the Host PC using the micro USB to USB cable.

      #. Press the button on the MAX32625PICO. **(Do not release the button until
         the MAINTENANCE drive is mounted)**.

         .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/max32625pico_maxdap.png
            :width: 400px

      #. Release the button once the MAINTENANCE drive is mounted.
      #. Drag and drop (to the MAINTENANCE drive) the firmware image.
      #. After a few seconds, the MAINTENANCE drive will disappear and be replaced
         by a drive named DAPLINK. This indicates that the process is complete, and
         the MAX32625PICO can now be used to flash the firmware of the
         AD-BMSE2E3W-SL Board.

5. Connect the alligator clip cable (red) to the VBATTP Pin or the 3rd of Pin 17
   header of the DC2472A battery emulator. Then insert the other end of the
   cable (banana jack plug) to TP16 (VBAT+ terminal) of the AD-BMSE2E3W-SL
   board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/connector_supply_vbattp.png

6. Connect the alligator clip cable (black) to the GND (VBAT-) supply of the
   DC2472A battery emulator. Then, connect the other end of the cable to the
   Rsense (top side) of the AD-BMSE2E3W-SL.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/gnd_vbat-_to_gnd_sense.png

7. Set the DC2472A battery emulators to HIGH voltage or equivalent to 4.1 V per
   cell by turning the Cell Voltage Adjustment Potentiometer clockwise.

8. Check the supply for the following test points as described in the diagram
   and table below. Make sure that the voltage levels are within the specified
   range.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/quick_test_points.png

.. note::

   .. list-table::

      * - **Hardware Supply Quick Test Point**
        -
        -
        -
      * - **TP Name**
        - **Description**
        - **Function**
        - **Voltage Range**
      * - TP2
        - **U1** ADBMS6830 BMS1_VREG
        - **U1** Input Voltage BMS1_VREG for ADBMS6830
        - Low voltage: 15 V to 20 V
          High voltage: (50 V to 58 V)
      * - TP4
        - **U3** ADBMS6830 BMS2_VREG
        - **U3** Input Voltage BMS2_VREG input for ADBMS6830
        - 0 V to 5 V
      * - TP7
        - **U6** LTC3639 Output
        - **U6** LTC3639 Regulator Voltage Output
        - 4.5 V to 5.5 V
      * - TP8
        - **U9** LT8303 Output
        - **U9** LT8303 Switch Down Regulator Output
        - 3.2 V to 3.5 V
      * - R346
          (Left Pin)
        - **U15** MAX25301A Output
        - **U15** MAX25301A Output 3.3 V going to MCU
        - 3.2 V to 3.5V
      * - TP16
        - VBAT+
        - Total Voltage Supply from battery
        - 72 V to 92 V (regulated)

   8. Once all steps are completed, you are now ready to use this reference
      design and run the accompanying software found in the link below:

   <WRAP tip> The AD-BMSE2E3W-SL comes complete with firmware examples and
   easy-to-use application GUI.

   Access the software resources and see the setup procedure in the <WRAP>
   :dokuwiki:`AD-BMSE2E3W-SL Software User Guide </resources/eval/user-guides/ad-bmse2e3w-sl/software>`.

</WRAP>

--------------

Application
-----------

72V to 96V Light EV Basic System Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below diagram depicts the essential components needed when using this BMS
reference design for basic electric 2-wheeler or 3-wheeler applications. Each
block represents a component. Use the diagram as a guide to understand the
system operation.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/72v-96v_vehicle_system.png
   :width: 1000px

1. \ **Battery Cell/Pack Block**\  - This block is where your battery supply or
   source is located. There are two configurations on how to connect the battery
   cells to the BMS:

.. list-table::

   * - **Single Side Cell Depopulation**

       .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/single_side_cell_depopulation.png
          :width: 500px

     - **Dual Side Cell Depopulation**

       .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/dual_side_cell_depopulation.png
          :width: 500px

       **Hover mouse on this image and click CTRL twice to magnify**

.. note::

   The setup shown in this User Guide uses the single side depopulation method
   only in connecting/aligning the cell to the BMS. The dual side depopulation
   is not yet supported by the software.

2. \ **BMS Block**\  - This block is where the BMS Cell and Pack Monitoring and
   MCU control happens. This block is also responsible for the control of the
   *Charging* (if the battery needs to be charged) and *Discharging* (when the
   battery needs to deliver voltage output going to the load side).

3. \ **User Interface Display**\  - This block is where the measurement,
   diagnosis and status of the BMS are displayed. The Display can have two
   options (or you can use both):

.. list-table::

   * - **UART Communication**

       .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/uart_comm.png
          :width: 500px

     - **CAN-BASIC Communication**

       .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/basic_can_comm.png
          :width: 500px

       **Hover mouse on this image and click CTRL twice to magnify**

.. note::

   For the BASIC CAN setup, we use the PCAN-USB connector
   (https://www.peak-system.com/PCAN-USB.199.0.html?&L=1) as our CAN
   interpreter. This product is *not included* in the AD-BMSE2E3W-SL Kit and
   needs to be purchased separately.

4. \ **Load**\  - This block is where you can place your external load. The
   voltage output at this level can vary from 72V to 96V with 50A to 100A range
   current capacity. The system implements a low side current sensing using
   Rshunt (sense resistor) where the VBAT- of the battery is connected to the
   upper end of the Rshunt bar and Shunt- is connected to the lower end of the
   Rshunt. The Shunt- will then be connected to the end of the load or the
   negative supply of the load.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/load_diagram.png
   :width: 500px

.. tip::

   Combining all components such as the Battery Cell/Pack, BMS, User Interface
   Display, and the Load will create an easy-to-use BMS system for E2W/E3W
   vehicle applications.

   After the set up for vehicle and load connection is done, you can now load
   the sample firmware for vehicle application. Please follow procedure found in
   the
   :dokuwiki:`software installation page </resources/eval/user-guides/ad-bmse2e3w-sl/software>`.

   Open the GUI and input the battery parameters. You should now be able to
   monitor the battery via GUI.

--------------

Resources
---------

- :adi:`ADBMS6830 Product Page <ADBMS6830>`
- :adi:`ADBMS2950 Product Page <ADBMS2950>`
- :adi:`ADBMS6822 Product Page <ADBMS6822>`
- :adi:`MAX32690 Product Page <MAX32690>`
- :adi:`LT8303 Product Page <LT8303>`
- :adi:`ADUM225N Product Page <ADUM225N>`
- :adi:`LTC7001 Product Page <LTC7001>`
- :adi:`LTC3639 Product Page <LTC3639>`

Design & Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-bmse2e3w-sl/ad-bmse2e3w-sl-designsupport.zip`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Help and Support
~~~~~~~~~~~~~~~~

For questions and more information, please visit the Analog Devices Engineer Zone. .. note::

   :ez:`EngineerZone Support Community <reference-designs>`
