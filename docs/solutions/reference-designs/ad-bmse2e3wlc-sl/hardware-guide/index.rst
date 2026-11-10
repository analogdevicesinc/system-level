.. _ad-bmse2e3wlc-sl hardware:

Hardware Guide
==============

Components and Connections
--------------------------

..  figure:: baseboard-components.png
    :width: 800 px

    AD-BMSE2E3WLC-48V Baseboard Components

+-------+---------------+---------------------------------------------+
| No.   | Component     | Function                                    |
+=======+===============+=============================================+
| 1     | Battery Cell  | Connector going to battery cells            |
|       | Connector     |                                             |
+-------+---------------+---------------------------------------------+
| 2     | ADBMS1816W    | Battery cell monitoring IC                  |
+-------+---------------+---------------------------------------------+
| 3     | LTC7000       | FET Driver IC                               |
+-------+---------------+---------------------------------------------+
| 4     | 12V Supply    | 12V supply access                           |
+-------+---------------+---------------------------------------------+
| 5a    | Rsense_N      | Resistor sensing for detecting and          |
|       |               | monitoring total current on the baseboard   |
|       |               | negative side                               |
+-------+---------------+---------------------------------------------+
| 5b    | Rsense_P      | Resistor sensing for detecting and          |
|       |               | monitoring total current on the baseboard   |
|       |               | positive side                               |
+-------+---------------+---------------------------------------------+
| 6a    | Arduino       | Arduino header connector left side          |
|       | Headers       |                                             |
+-------+---------------+---------------------------------------------+
| 6b    | Arduino       | Arduino header connector right side         |
|       | Headers       |                                             |
+-------+---------------+---------------------------------------------+
| 7     | Featherwing   | Connector for placing Featherwing form-     |
|       | Connector     | factor boards                               |
+-------+---------------+---------------------------------------------+
| 8     | VBAT+         | Positive terminal connector for total       |
|       | Connector     | voltage capacity of the battery pack        |
+-------+---------------+---------------------------------------------+
| 9     | isoSPI        | Duraclik isoSPI connector terminals         |
|       | Connectors    |                                             |
+-------+---------------+---------------------------------------------+
| 10    | ADG701        | 5V switch, USB-enabled                      |
+-------+---------------+---------------------------------------------+
| 11    | LTC7138       | 5V analog and 5V digital LDO regulator      |
+-------+---------------+---------------------------------------------+
| 12    | V+ Output     | Output control connector from V+ going to   |
|       | Control       | Link+ Output                                |
|       | Connector     |                                             |
+-------+---------------+---------------------------------------------+
| 13    | LINK+_OUT     | Access going to load side                   |
+-------+---------------+---------------------------------------------+
| 14    | Common GND    | Access ground going to load side            |
+-------+---------------+---------------------------------------------+

.. figure:: daughterboard-components.png
    :width: 600 px

    AD-BMSE2E3WLC-48V Daughter Board Components

+-----+----------------------+-----------------------------------------+
| No. | Component            | Function                                |
+=====+======================+=========================================+
| 1   | Battery Cell         | Connector for Cell Input                |
|     | Connector            | (for example, DC2472A cell emulator)    |
+-----+----------------------+-----------------------------------------+
| 2   | ADBMS1816W (U3)      | 16-Cell BMS Monitoring Chip             |
+-----+----------------------+-----------------------------------------+
| 3a  | Arduino Headers      | Arduino Header Connector left side      |
+-----+----------------------+-----------------------------------------+
| 3b  | Arduino Headers      | Arduino Header Connector right side     |
+-----+----------------------+-----------------------------------------+
| 4   | isoSPI Connectors    | Duraclik isoSPI Connector terminals     |
+-----+----------------------+-----------------------------------------+

Test Points
-----------

**AD-BMSE2E3WLC-48V Baseboard**

.. figure:: baseboard-testpoints.png
    :width: 600 px

    AD-BMSE2E3WLC-48V Baseboard Test Points

+----------------+------------------+-----------------+---------------+
| Test Point     | Name             | Typical (V)     | Range (V)     |
+================+==================+=================+===============+
| TP6            | PORT             | 4.9             | 4.5  to 5.15  |
+----------------+------------------+-----------------+---------------+
| TP8            | TRANS            | 0               | 0             |
+----------------+------------------+-----------------+---------------+
| TP7            | VREG             | 4.9             | 4.7 to 5.15   |
+----------------+------------------+-----------------+---------------+
| 12V            | 12V SUPPLY       | 11.9            | 11.5 to 12.5  |
+----------------+------------------+-----------------+---------------+
| E1 (PIN2)      | 5V_ANA           | 5               | 4.5 to 5.15   |
+----------------+------------------+-----------------+---------------+
| E2 (PIN2)      | 5V_DIG           | 5               | 4.5 to 5.15   |
+----------------+------------------+-----------------+---------------+

Hardware Setup
--------------

**Required Hardware**

* 1 × :adi:`AD-BMSE2E3WLC-48V` Baseboard
* 1 × :adi:`EVAL-ADBMS1816WLC` Daughter Board
* 2 × :adi:`DC2472A` Battery Emulator
* 1 × :adi:`MAX32666FTHR` Microcontroller
* 1 × :adi:`MAX32625PICO` Programming Board
* 2 × isoSPI twisted-pair cables
* 1 × 10-pin SWD debugger cable
* 3 × Micro-USB to USB cables
* 1 × PC/Laptop
* 2 × Red Alligator-to-Banana Plug Cables (1166-12-0)
* 2 × Black Alligator-to-Banana Plug Cables (1166-12-0)
* 12 × Pin Header Shunts (if not yet installed)
* 1 × Digital Multimeter (DMM)

Jumper Configuration
~~~~~~~~~~~~~~~~~~~~

**AD-BMSE2E3WLC-48V Baseboard**

From the list of required hardware, select the **AD-BMSE2E3WLC-48V Baseboard**.

Install the shunt connectors (if not yet installed) and ensure correct
positions, as highlighted in red in the figure below.

.. important:: 

    Header P16 must be configured with the shunt installed between
    pin 2 and pin 3. This setting configures the board for 48V operation.

.. figure:: baseboard-shunt-configuration.png
    :width: 1500 px

    AD-BMSE2E3WLC-48V Baseboard Shunt Configuration

----

**EVAL-ADBMS1816WLC Daughter Board**

Configure the shunt connectors in **P17,P18, P24,
P30, P34, and P35.** Refer to the pin positions in the 
figure below for proper shunt configuration.

.. figure:: daughterboard-shunt-configuration.png
    :width: 700 px

    EVAL-ADBMS1816WLC Daughter Board Shunt Configuration

Battery Emulator Setup
~~~~~~~~~~~~~~~~~~~~~~

.. note:: 

    The :adi:`DC2472A` Battery Emulator Board is used for cell voltage
    input in this setup.

-   Plug the screw-terminal block into the cell voltage connector of the
    two :adi:`DC2472A` battery emulators.

-   Connect the first DC2472A battery emulator to the AD-BMSE2E3WLC-48V
    Baseboard through the cell connector.

    .. figure:: baseboard-to-emulator.png
        :width: 600 px

        AD-BMSE2E3WLC-48V to Battery Emulator Setup

-   Connect the second :adi:`DC2472A` battery emulator to the :adi:`EVAL-ADBMS1816WLC`
    Daughter Board through the cell connector.

    .. figure:: daughterboard-to-emulator.png
        :width: 600 px

        EVAL-ADBMS1816WLC to Battery Emulator Setup

-   Connect a 5V external power source to the :adi:`DC2472A` (J1) using a USB
    cable. External power supply is recommended for adequate power.

-   Alternatively, power it through a PC using a USB cable.

**Power Verification**

After powering up:

-   On **DC2472A**:

    - Blue LED (LED1) should turn **ON**

        .. figure:: emulator-led-on.png
            :width: 350 px

            DC2472A Emulator Power LED

-   On **AD-BMSE2E3WLC-48V Baseboard**:

    - Red LED (DS3) and Green LED (DS1) should turn **ON**

        .. figure:: baseboard-led-on.png
            :width: 600 px

            AD-BMSE2E3WLC-48V Baseboard Power LED

Microcontroller Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Attach the :adi:`MAX32666FTHR` microcontroller to the :adi:`AD-BMSE2E3WLC-48V` 
    baseboard through the Featherwing connector.

    .. figure:: max32666fthr-connection.png
        :width: 600 px

        MAX32666FTHR MCU to AD-BMSE2E3WLC-48V Baseboard

48V Connection
~~~~~~~~~~~~~~

-   Connect the red alligator to banana jack cable between **48V** and
    **TP11** on the :adi:`AD-BMSE2E3WLC-48V` as shown below.

    .. figure:: 48v-connection.png

        48V Connection

Cable and PC Connection
~~~~~~~~~~~~~~~~~~~~~~~

    (A). Plug the micro-USB cable to the first :adi:`DC2472A` battery emulator
         that is connected to the :adi:`AD-BMSE2E3WLC-48V` baseboard.

    (B). Plug the micro-USB cable to the second :adi:`DC2472A` battery emulator
         that is connected to the :adi:`EVAL-ADBMS1816WLC` daughterboard.

    (C). Plug the micro-USB cable into the :adi:`MAX32666FTHR` microcontroller.

    (D). Connect the 2-wire isoSPI cable from P10 of the :adi:`AD-BMSE2E3WLC-48V` baseboard.

    (E). Connect the other end of the 2-wire isoSPI cable to P10 of
         the :adi:`EVAL-ADBMS1816WLC` daughterboard.

    (F). Connect all USB cables to a USB hub (preferred). 

    .. note::
        
        If your PC/laptop USB ports can supply ≥1A, you may connect devices 
        directly without a USB hub.

    Your setup should look like below:

    .. figure:: full-integration-setup.png
        :width: 600 px

        Full Hardware Evaluation Setup

----

Sample Application Setup
------------------------

Refer to the diagrams below for the sample application setup for Charge and Discharge applications.

Charge Application
~~~~~~~~~~~~~~~~~~

.. figure:: charge-application.png
    :width: 1500 px

    Charge Application Setup

Discharge Application
~~~~~~~~~~~~~~~~~~~~~

.. figure:: discharge-application.png
    :width: 1500 px

    Discharge Application Setup

.. tip::

    The :adi:`AD-BMSE2E3WLC-SL` comes complete with firmware and easy-to-use application GUI. 
    
    Access the software resources and see the setup procedure in the 
    :ref:`AD-BMSE2E3WLC-SL Software User Guide <ad-bmse2e3wlc-sl software>`.
