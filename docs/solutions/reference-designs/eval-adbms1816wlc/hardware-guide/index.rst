.. _eval-adbms1816wlc hardware:

Hardware Guide
==============

Components and Connections
--------------------------

..  figure:: eval-adbms1816wlc-components.png
    :width: 800 px

    EVAL-ADBMS1816WLC Components

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

Hardware Setup
--------------

**Requirements**

    * 1 × :adi:`EVAL-ADBMS1816WLC` Board
    * 1 × :adi:`DC2472A` Battery Emulator
    * 1 × Digital Multimeter (DMM)

Jumper Configuration
~~~~~~~~~~~~~~~~~~~~

Configure the shunt connectors in **P17, P24,
P34, P30, P18, and P35.** Refer to the pin positions in the 
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
    :adi:`DC2472A` battery emulator.

-   Connect the :adi:`DC2472A` battery emulator to the :adi:`EVAL-ADBMS1816WLC`
    daughterboard through the cell connector.

    .. figure:: emulator-to-daughterboard.png
        :width: 600 px

        EVAL-ADBMS1816WLC to Battery Emulator Setup

-   Connect a 5V external power source to the :adi:`DC2472A` battery emulator (J1) 
    using a USB cable. An external power supply is recommended for adequate
    power.

-   Alternatively, power it through a PC using a USB cable.

    |

    **Power Verification**

    After powering up:

        -   On **DC2472A**:

            - Blue LED (LED1) should turn **ON**

            .. figure:: emulator-led-on.png
                :width: 350 px

                DC2472A Emulator Power LED

Cell Voltage Measurement Using DMM
----------------------------------

Using a **Digital Multimeter (DMM)**:

Rotate the knob of the DC2472A clockwise to set it to the lowest
voltage. Record the measurement for each cell voltage (C1 to C16).

    - Set the DMM to voltage mode
    - Place the probes (+) and (–) between adjacent cells to measure voltage
    - The reading should fall within the specified range to be considered
      “good”; otherwise, mark it as “bad”
    - Do not remove the supply during measurement
    - Clockwise → lowest voltage (1.3V to 1.7V)
    - Counterclockwise → highest voltage (4.0V to 4.5V)

    .. figure:: emulator-potentiometer.png
        :width: 1000 px

        DC2472A Battery Emulator Potentiometer

**Expected Reading between Cells for EVAL-ADBMS1816WLC**

+------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+------+------+------+------------+
| RANGE (V)  | C1    | C2    | C3    | C4    | C5    | C6    | C7    | C8    | C9    | C10   | C11   | C12   | C13  | C14  | C15  | C16  | ASSESSMENT |
+============+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+=======+======+======+======+======+============+
| 4.0 to 5.0 | 4     | 4     | 4     | 4     | 4     | 4     | 4     | 4     | 4     | 4     | 4     | 4     | 4    | 4    | 4    | 4    | GOOD       |
+------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+------+------+------+------------+
| 1.3 to 1.7 | 1.431 | 1.431 | 1.431 | 1.431 | 1.431 | 1.431 | 1.431 | 1.431 | 1.431 | 1.431 | 1.431 | 1.431 | 1.43 | 1.43 | 1.43 | 1.43 | GOOD       |
+------------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+------+------+------+------+------------+

----

Full System Integration Setup
-----------------------------

**Requirements**

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


AD-BMSE2E3WLC-48V Baseboard Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the list of required hardware, select the **AD-BMSE2E3WLC-48V Baseboard**.

-   Install the shunt connectors (if not yet installed) and ensure correct
    positions, as highlighted in red in the figure below.

    .. important:: 

        Header P16 must be configured with the shunt installed between
        pin 2 and pin 3. This setting configures the board for 48V operation.

    .. figure:: baseboard-shunt-config.png
        :width: 1500 px

        AD-BMSE2E3WLC-48V Baseboard Shunt Configuration

-   Connect the second :adi:`DC2472A` battery emulator to the :adi:`EVAL-ADBMS1816WLC` Daughter Board 
    through the cell connector.

    .. figure:: baseboard-to-emulator.png
        :width: 600 px

        AD-BMSE2E3WLC-48V to Battery Emulator Setup

Microcontroller Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

-   Attach the :adi:`MAX32666FTHR` microcontroller to the :adi:`AD-BMSE2E3WLC-48V` 
    Baseboard through the Featherwing connector.

    .. figure:: baseboard-to-max32666fthr.png
        :width: 600 px

        MAX32666FTHR Mounted to the AD-BMSE2E3WLC-48V Baseboard

48V Connection
~~~~~~~~~~~~~~

-   Connect the red alligator to banana jack cable between **48V** and
    **TP11** on the :adi:`AD-BMSE2E3WLC-48V` as shown below.

    .. figure:: 48v-connection.png

        48V Connection

Cable and PC Connection
~~~~~~~~~~~~~~~~~~~~~~~

    (A). Plug the micro-USB cable to the first :adi:`DC2472A` battery emulator
         that is connected to :adi:`AD-BMSE2E3WLC-48V`.

    (B). Plug the micro-USB cable to the second :adi:`DC2472A` battery emulator
         that is connected to :adi:`EVAL-ADBMS1816WLC`.

    (C). Plug the micro-USB cable into the :adi:`MAX32666FTHR`.

    (D). Connect the 2-wire isoSPI cable from P10 of :adi:`AD-BMSE2E3WLC-48V`.

    (E). Connect the other end of the 2-wire isoSPI cable to P10 of
         :adi:`EVAL-ADBMS1816WLC`.

    (F). Connect all USB cables to a USB hub (preferred). 

    .. note::
        
        If your PC/laptop USB ports can supply ≥1 A, you may connect devices 
        directly without a USB hub.

    Your setup should look like below:

    .. figure:: full-integration-setup.png
        :width: 600 px

        Full Hardware Evaluation Setup

----

Sample Application Setup
------------------------

Refer to the diagram below for the sample application setup for Charge and Discharge applications.

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

    The :adi:`EVAL-ADBMS1816WLC` can be evaluated through the ACE GUI by running the 
    AD-BMSE2E3WLC software package. Access the software resources 
    and see the setup procedure in the :ref:`Software User Guide <eval-adbms1816wlc software>`.
