.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter

.. _ad-max32sxwise-sl demo smart-watermeter:

Smart Water Meter Application Demo
""""""""""""""""""""""""""""""""""

Overview
========

The **Smart Water Meter Application Demo** addresses the limitations of
mechanical water meters in terms of accuracy, longevity, and monitoring. The
demo is designed to assist utility companies, water providers, and residential
consumers in improving water management, reducing operational costs, and
increasing efficiency.

The :adi:`EV-FLOWMETER-ARDZ`, an advanced and efficient solution for flow
metering, allows the accurate measurement of flow velocity and mass flow rate.
This sensor node is used with the :adi:`MAX32670-SX-ARDZ` Base Board, enabling
continuous monitoring through low-power and long-range proprietary radio
communication. The base board"s custom GUI provides the user with a real-time,
comprehensive summary of their water consumption.

The demo showcases the capability of :adi:`EV-FLOWMETER-ARDZ` as a smart water
meter when combined with the :adi:`MAX32670-SX-ARDZ`, highlighting its
suitability for utility and industrial applications.

To learn more about the reference designs, refer to :adi:`EV-FLOWMETER-ARDZ` and
:adi:`MAX32670-SX-ARDZ`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_overview.png
   :width: 500px

Demo Requirements
=================

Hardware Requirements
---------------------

- Microcontroller/Sensors

  -
    :adi:`EV-FLOWMETER-ARDZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/EV-FLOWMETER-ARDZ.html>`
    (2x)
  -
    :adi:`MAX32670-SX-ARDZ <en/resources/evaluation-hardware-and-software/evaluation-boards-kits/MAX32670-SX-ARDZ.html>`
    (2x)

- Gateway Essentials

  - Raspberry Pi 4
  - Raspberry Pi 4 Power Supply Adapter
  - RAK5146 PiHAT
  - RAK5146 SPI Module
  - Long Range Antenna
  - LAN Cable
  - Micro SD Card
  - Spacer Bolt (4x)
  - Screw (6x)

- Microcontroller/Sensor Setup

  - :adi:`MAX32625PICO` Rapid Development Platform with 10-pin ribbon cable
  - CR123A Battery or any equivalent external DC power supply (+3 V to +4.7 V)
    (2x)
  - Micro USB-to-USB Cable

- Environment Setup

  - :adi:`CN0508` Benchtop Power Supply
  - Flow Transducer with Pipe (2x)
  - Acrylic Water Container
  - Water Pump System
  - Water

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/gateway_essentials.png
   :width: 800px

Software Requirements
---------------------

- Host PC with administrator access

  - Windows 10 OS or later
  - Microsoft .Net Framework 4.6.2
  - 1920 by 1080 or greater screen resolution (recommended)

- Downloaded and installed:

  - :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin+>`

::

   * {{:resources:eval:user-guides:longrangewirelessradio:ad-max32wise-slz_firmware.zip | AD-MAX32WISE-SLZ Firmware (Rel1.0.0)}}

::

   * {{{{
     :resources:eval:user-guides:ad-max32sxwise-sl:demo:wisehub_flowmeterversion.zip | ADI Wireless Sensor Hub Standalone Software for Flowmeter Application}}

::

   * [[http://sourceforge.net/project/showfiles.php?group_id=67297|UART serial monitor]]
     * This demo uses Real Term serial monitor, but other UART serial terminals may also be used.
   * [[https://etcher.balena.io|Balena Etcher]] image writing tool
   * [[https://www.chirpstack.io/docs/chirpstack-gateway-os/install/raspberry-pi.html|ChirpStack Gateway OS]]

Demo Setup
==========

Block Diagram
-------------

.. note::

   The block diagram of the overall setup is shown below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_demo_block_diagram.png

Hardware Setup
--------------

.. note::

   This section describes the
   :dokuwiki:`hardware setup </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#hardware_setup>`
   of the demo divided into three phases: **node board assembly**, **gateway
   assembly**, and **environment assembly**.

   **Sensor board assembly** involves connecting the :adi:`EV-FLOWMETER-ARDZ` to
   the :adi:`MAX32670-SX-ARDZ`. This phase is to be repeated for each sensor
   board. **Gateway assembly** involves setting up the RAK5146 PiHAT and the
   Raspberry Pi 4 as the concentrator hardware, allowing data transmission from
   the sensor boards to the host PC. Lastly, **environment assembly** involves
   building the setup that will simulate water flow across pipes.

Sensor Board Assembly
~~~~~~~~~~~~~~~~~~~~~

.. note::

   For the needed components for this phase, see **Microcontroller/Sensors** and
   **Microcontroller/Sensor Setup** under
   :dokuwiki:`Hardware Requirements </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#hardware_requirements>`.

#. .. note::

      Insert one **CR123A battery (3 V to 4.7 V)** into the battery holder (BT1) of the :adi:`MAX32670-SX-ARDZ` Base Board.

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_battery_attachment.png

      To **check for the battery polarity** in the BT1 connector, refer to the figure above (right). The DS3 LED will light up indicating that you have inserted the battery correctly and that power is provided in the base board.

#. .. note::

      Connect the :adi:`EV-FLOWMETER-ARDZ` Sensor Node to the
      :adi:`MAX32670-SX-ARDZ` Base Board by aligning the corresponding Arduino
      headers on each board.

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_mount_boards.png

#. Connect the :adi:`MAX32625PICO` programming adapter to the :adi:`MAX32670-SX-ARDZ` Base Board through the 10-pin ribbon cable.

   .. note::

      **Make sure that the** :adi:`MAX32625PICO` **programming adapter has been flashed with the correct image before connecting it to the** :adi:`MAX32670-SX-ARDZ` **Base Board.** If you do not know how to load the image, click on the instructions below:

   <hidden **How to flash the firmware image in the MAX32625PICO** >

   #. Download the firmware image: :git-max32625pico-firmware-images:`MAX32625PICO Firmware Image for MAX32670 <raw/master/bin/max32625_max32670evkit_if_crc_swd_v1.0.3.bin+>`
   #. Do not connect the :adi:`MAX32625PICO` to the :adi:`MAX32670-SX-ARDZ` Base Board yet.

   #. Press the button on the :adi:`MAX32625PICO`. **Do not release the button until the MAINTENANCE drive is mounted**.

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-paarray3552r-sl/max32625pico_maxdap.png
         :width: 300px

   #. While holding the button, connect the :adi:`MAX32625PICO` to the Host PC using the micro USB to USB cable.
   #. Release the button once the MAINTENANCE drive is mounted.
   #. Drag and drop (to the MAINTENANCE drive) the firmware image.
   #. After a few seconds, the MAINTENANCE drive will disappear and be replaced by a drive named DAPLINK. This indicates that the process is complete, and the :adi:`MAX32625PICO` can now be used to flash the firmware of the :adi:`MAX32670-SX-ARDZ` Base Board.

   </hidden>

#. .. note::

      Connect the :adi:`MAX32625PICO` programming adapter to the Host PC using the
      micro USB to USB cable.

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_pico_attachment.png

.. note::

   

   To **set up the firmware** of the sensor board, you may proceed to
   :dokuwiki:`Configuring the Sensor Board </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#configuring_the_sensor_board>`
   under
   :dokuwiki:`Software Setup </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#software_setup>`.
   Since **this demo uses two sensor boards**, repeat all steps of
   :dokuwiki:`Sensor Board Assembly </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#sensor_board_assembly>`
   for the second board.

Gateway Assembly
~~~~~~~~~~~~~~~~

.. note::

   For the needed components for this phase, see **Gateway Essentials** under
   :dokuwiki:`Hardware Requirements </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#hardware_requirements>`.

#. Insert the RAK5146 SPI module into the mPCIe slot on the RAK2287 Pi HAT. Make
   sure the card fits snugly into the connector.

#. Gently press the SPI module down and fasten it using the screws provided.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/gateway_1.png
      :width: 400px

#. Connect the RAK5146 PiHAT to the Raspberry Pi using the 40-pin connector.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rpi_4_with_rak5146_hat.png
      :width: 400px

#. Connect the Raspberry Pi to the Host PC using the LAN cable.
#. .. note::

      Power on the Raspberry Pi using the Raspberry Pi 4 Power Supply Adapter.

.. note::

   

   To **configure the gateway**, you may proceed to
   :dokuwiki:`Imaging the SD Card with ChirpStack OS </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#imaging_the_sd_card_with_chirpstack_os>`
   and
   :dokuwiki:`Configuring the Gateway </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#configuring_the_gateway>`
   under
   :dokuwiki:`Software Setup </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#software_setup>`.

Environment Assembly
~~~~~~~~~~~~~~~~~~~~

.. note::

   For the needed components for this phase, see **Environment Setup** under
   :dokuwiki:`Hardware Requirements </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#hardware_requirements>`.

   

   When using the sensor board, a general-purpose ultrasonic flow rate sensor
   probe can be used with it. An example of a probe is the **Flow Transducer
   with Pipe (Model：HS0003)** from Audiowell Sensor Technology.

   For temperature measurement, this board supports up to two 2-wire PT1000/500
   platinum **resistive temperature detectors (RTD)**. 

#. .. note::

      Connect the wires of the **Flow Transducer with Pipe** and the **resistive temperature detector (RTD)** to the sensor board.

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_board_connections.png

      Follow the connections shown above. Repeat this step for the other sensor board and transducer.

   .. important::

      An **RTD** or a **dummy sensor (1.0 kΩ resistor)** is required for each terminal in order for the board to run and capture the flow rate.



#. 

   Set up the **water container** as shown below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_environment_front.png

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_environment_top.png

   

   The :adi:`CN0508` **75 Watt, Single-Output Benchtop Power Supply** is connected to the water pump in order to vary water flow as needed for the demo. 



   

   Once the sensor boards, gateway, and environment are all assembled, proceed
   to
   :dokuwiki:`Software Setup </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#software_setup>`
   to configure the sensor boards, gateway, and the application server. 

Software Setup
--------------

.. important::

   Before proceeding with the steps listed below. **Make sure that all requirements under**
   :dokuwiki:`Software Requirements </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#software_requirements>`
   **are met, with all needed software downloaded and installed**.

This section describes the software setup of the demo divided into five phases:
**configuring the sensor board**, **imaging the SD card with ChirpStack OS**,
**configuring the gateway**, **setting up a self-hosted application server**,
and **connecting a sensor node to the gateway**.

**Configuring the sensor board** involves uploading the appropriate firmware to
the sensor board using the :adi:`MAX32625PICO` programming adapter and obtaining
the board"s DevEUI. To prepare the gateway, **imaging the SD card with
ChirpStack OS** involves flashing the ChirpStack Gateway OS to the Raspberry Pi
4"s micro SD card, while **configuring the gateway** involves creating the
gateway through the ChirpStack Network Server.

To configure the GUI, **setting up a self-hosted application server** involves
configuring the Host PC, installing the GUI, and accessing the gateway. Lastly,
**connecting a sensor node to the gateway** involves creating a device for each
board and accessing the GUI.

.. tip::

   Visit
   :dokuwiki:`ADI Long Range Wireless Radio Software User Guide </resources/eval/user-guides/longrangewirelessradio/software>`
   for a more detailed software setup guide.



Configuring the Sensor Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   Make sure you have completed the steps described in
   :dokuwiki:`Sensor Board Assembly </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#sensor_board_assembly>`
   before proceeding with the steps listed below.

   This phase will require
   `Real Term serial monitor <http://sourceforge.net/project/showfiles.php?group_id=67297>`__
   and **AD-MAX32WISE-SLZ Firmware (Rel1.0.0)** installed.



#. If **AD-MAX32WISE-SLZ Firmware (Rel1.0.0)** is already downloaded, extracted, and installed, go to **C:\\Analog Devices\\AD-MAX32WISE-SLZ-Rel1.0.0\\Software\\ad_max32wise_src\\bin\\flow**.

   The **flow folder** should contain the BIN, ELF, and HEX file.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/bin_files_2.png
      :width: 600px

#. Go to My Computer and search for the **DAPLINK drive**. Drag and drop (or
   copy and paste) the **.bin firmware file** directly into the DAPLINK drive.

   .. tip::

      To check if the flashing is successful, check the DAPLINK directory and
      make sure there is no **FAIL.TXT** file. In case there is, repeat the
      drag and drop step.

#.  Reset the :adi:`MAX32670-SX-ARDZ` Base Board by pressing the **S1 reset button**.

#. Open the
   `Real Term serial monitor <http://sourceforge.net/project/showfiles.php?group_id=67297>`__
   to check if the firmware has been loaded correctly. Make sure to use the
   following settings:

   - Ports : Take note of the COM port used by checking the Device Manager
   - Baud Rates and Ports : set to 921600

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/2.png
      :width: 600px

   - Display formatting : set to ANSI
   - Enable Scrollback : set to 200 .

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/1.png
      :width: 600px

#. Once configured, open the serial monitor by clicking **Open** on the **Port**
   tab.
#. Take note of the **DevEUI (64-bit end-device identifier)**. This will be used later during the gateway setup.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/deveui.png
      :width: 600px

   To **redisplay the DevEUI** on the screen, **reset the** :adi:`MAX32670-SX-ARDZ` **Base Board** by pressing the S1 button.

Imaging the SD Card with ChirpStack OS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This phase will require `Balena Etcher <https://etcher.balena.io>`__
   **image writing tool** installed and
   `ChirpStack Gateway OS <https://www.chirpstack.io/docs/chirpstack-gateway-os/install/raspberry-pi.html>`__
   downloaded. This phase will also use the **micro SD card** listed under
   :dokuwiki:`Gateway Essentials </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#gateway_essentials>`.



#. Run the `Balena Etcher <https://etcher.balena.io>`__ **image writing tool**.
#. Insert the micro SD card into the Host PC.

#. Click **Flash from file** from the options shown in the interface.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/flashing_sd_card.png
      :width: 600px

#. Navigate to the location where the downloaded
   `ChirpStack Gateway OS <https://www.chirpstack.io/docs/chirpstack-gateway-os/install/raspberry-pi.html>`__
   is saved.
#. Select target and choose the targeted micro SD card drive.
#. Click **Flash** to start the burning process of the image in the chosen SD
   card.
#. 

   Wait until it is done.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/flashing_sd_card_2.png
      :width: 600px

    In case the **flashing fails**, consult this guide to resolve the issue: `Balena Etcher FAQs <https://etcher.balena.io/#FAQs>`__. 

.. note::

   After the first boot, the **gateway might reboot
   automatically** to apply some changes. The full image will set up the
   **PostgreSQL database** on its first boot. This could take a couple of
   minutes and during this time the gateway will be less responsive. 

Configuring the Gateway
~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   Make sure you have completed the steps described in
   :dokuwiki:`Gateway Assembly </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#gateway_assembly>`
   before proceeding with the steps listed below. Make sure that the **Raspberry
   Pi (powered on) and Host PC are still connected** through the LAN cable.

**Opening the SSH client**

#. Insert the imaged SD card on the designated slot on the Raspberry Pi.
#. 

   Connect the Host PC to ChirpStack WiFi.

    When prompted to enter password, use **ChirpStackAP** (case-sensitive). 

#. Open command prompt or terminal on the Host PC.

#. 

   On the terminal, enter: <code> ssh admin@192.168.0.1 </code>

#. 

   SSH connection will ask for the password input. Use below credentials:

   - Username: admin
   - Password: admin
   - StaticIP: 192.168.0.1

#. Once connected, check the assigned ChirpStack IP by typing **ifconfig**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/chirpstack_ip.png
      :width: 600px

#. 

   This will show all configs, look for **eth0** and **save the IP address assigned to it**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/eth0_ip.png
      :width: 600px

    In this example, the IP assigned is **169.254.117.207**. This will be used in **Installing the GUI and Accessing the Gateway** under :dokuwiki:`Setting up a Self-Hosted Application Server </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#setting_up_a_self-hosted_application_server>`.



#. Open the Raspberry Pi terminal, then enter:
   :code:`sudo gateway-config`
   This will **open an SSH client** to configure the gateway.

**Navigating the SSH client**

#. In the main menu, choose **Setup concentrator shield**.
#. Choose **RAK5146 (with GNSS)**. Click **OK**.
#. Choose **AU915**. Click **OK**.
#. Choose **Channels 0 to 7 + 64**. Click **OK**.
#. The concentrator restarts and goes back to the main menu.
#.  Quit the main menu.

.. note::

   If you have properly configured the gateway and installed the
   required SD card image, then **you are ready to use the ChirpStack Network
   Server**.

Setting up a Self-Hosted Application Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   Make sure that the **Raspberry Pi (powered on) and Host PC are still
   connected** through the LAN cable.

   This phase will require **ADI Wireless Sensor Hub Standalone Software (Rev
   1.0.3)** downloaded and extracted.

**Configuring the Host PC for the Gateway**



#. 

   Access **Advance Firewall settings** in your computer.

#. 

   Create a new **Inbound Rule**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/inbound_rule_1.png
      :width: 700px

#. 

   **Configure the Inbound Rule** as shown below.

   <hidden **Step-by-step configuration of a new ChirpStack Inbound Rule** >

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/inbound_rule_2.png
      :width: 700px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config.png
      :width: 700px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_2.png
      :width: 700px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_3.png
      :width: 700px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_4.png
      :width: 700px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_5.png
      :width: 700px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/rule_config_6.png
      :width: 700px

   </hidden>

.. note::

   **Installing the GUI and Accessing the Gateway**

#. Run the **ADI Wireless Sensor Hub Standalone Software** with administrator
   privileges. This will start the initialization process and run the process on
   your PC.
#. 

   Check and **save the IP address assigned to the Raspberry Pi gateway**. The server will show all connections available; select the IP of the connector you used.

    In this example, it is the Apple USB Ethernet Adapter.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/ip_address.png

   This information will be used in **Setting up a Local Host URL for the Application Server** under :dokuwiki:`Connecting a Sensor Node to the Gateway </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#connecting_a_sensor_node_to_the_gateway>` to integrate data from the gateway to the GUI. 

#. Use the assigned ChirpStack IP address saved earlier to access its
   configuration interface **by adding the ChirpStack Port (8080)** to the end
   of IP address. Open a page in the browser using **[saved IP address]:8080**
   as the URL.

   In this example, the saved IP address is 169.254.117.207. Hence,
   the URL would be **169.254.117.207:8080**.

   If you haven"t saved the IP address, **revisit steps 3 to 7** in **Opening
   the SSH Client** under
   :dokuwiki:`Configuring the Gateway </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#configuring_the_gateway>`.
   

#. This will open the login page. Enter the same credentials we used to
   establish an SSH connection with the ChirpStack Gateway.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/log_in_page.png
      :width: 600px

Connecting a Sensor Node to the Gateway
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This phase describes how to connect the sensor nodes to ChirpStack and how to
   validate that it can send data. This process is divided into three sections:
   **creating a device profile**, **enrolling device applications**, and
   **setting up a local host URL for the application server**.  At this
   point, it is assumed that you have a **working ChirpStack environment** with
   a connected gateway.

**Creating a Device Profile**



#. Once you are in the ChirpStack landing page, navigate to the **Applications
   tab**.
#. Click **Device profiles** under the **Tenant** category.

#. Click on the **Add device profile** button.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/software/gate_way_setup/add_device_profile.png

#. 

   Answer all required information under the **General** tab, and then click **Submit** once done.

   The following shows the configuration required to add a sensor node:

   

   .. list-table::

      * - **Attribute**
        - **Configuration**
      * - Name
        - Enter desired sensor node name
      * - Region
        - AU915
      * - Region Configuration
        - AU915 (channels 0-7 +64)
      * - MAC Version
        - LoRaWAN 1.0.4
      * - Regional parameters revision
        - A
      * - ADR algorithm
        - Default ADR algorithm (LoRa only)
      * - Expected uplink interval (sec)
        - 10
      * - Device-status request frequency (req/day)
        - 8640



.. note::

   **Enrolling Device Applications**

#. After adding a device, click the **Applications** option under **Tenant**.
#. Click on the **Add application** button.

#. Write the desired **Application Name** on the space provided. Hit **Submit**
   once done.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/submit_application.png
      :width: 600px

#. 

   Open the Application created and **add a device**.

   The following details are also needed:

   - Name: previously defined application name set from the previous steps
   - Device EUI (EUI64): unique serial number of the device
   - Device profile: previously defined device profile set from the previous steps

    In naming the devices, you must include a **specific keyword** (not case-sensitive) to distinguish the sensor nodes shown on the GUI. In this case, the two sensor nodes can be named **flow-1** and **flow-2** respectively.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/device_details.png



#. 

   Once done, click **Submit**. Then, **repeat steps 5 and 6** for the other sensor board.

    For OTAA devices, confirm that when the device tries to OTAA activate, you see a **JoinRequest** message followed by a **JoinAccept** message.

   If you do not see a JoinRequest and JoinAccept, click on the **Flush OTAA devices** button.



#. 

   Enter the **Application key** and hit **Submit** once done.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/app_key.png

    For this demo, the **Application key** is **2b7e151628aed2a6abf7158809cf4f3c**.

   The App Key included in the LoraMAC was used as is for the purpose of evaluation. Users can generate the App Key and add it in the source code on their own. 

.. note::

   **Setting up a Local Host URL for the Application Server**

#. In the Applications tab, select and open **WiSe_Sensors**.
#. 

   Inside the **ADI_SENSOR_NODE** application, navigate to the **Integrations** tab.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/integration.png

#. In the **Integrations** tab, select the **edit** button in the **HTTP
   Configuration** section.
#. 

   Change the **Event Endpoint URL** to the IP of the adapter your gateway is connected.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/http_integration.png

    In this example, it is the IP of the Apple Network Adapter, http://169.254.178.157:5050/api/data/post.

   If you haven"t saved the IP address, **revisit steps 1 to 2** in **Installing the GUI and Accessing the Gateway** under :dokuwiki:`Setting up a Self-Hosted Application Server </resources/eval/user-guides/ad-max32sxwise-sl/demo/smart-watermeter#setting_up_a_self-hosted_application_server>`.



#. After updating the HTTP Integration endpoint URL, submit the changes by
   pressing **Submit**.

#. A pop-up message will appear saying **HTTP Integration updated**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/longrangewirelessradio/http_integration_success.png
      :width: 600px

#. Open your browser and **enter the URL** http://localhost:5050. Now you"ll be
   able to see and monitor your active nodes.

Actual Demo
===========

Working Setup
-------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_actual_setup.png
   :width: 800px

Custom GUI
----------

.. note::

   The custom GUI for this demo highlights the :adi:`EV-FLOWMETER-ARDZ` as a
   **smart water meter** with two main features: **water bill computation** and
   **leakage detection**.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-max32sxwise-sl/demo/smart_water_meter_draft_gui.png

Resources
=========

- :dokuwiki:`MAX32670-SX-ARDZ Base Board </resources/eval/user-guides/max32670-sx-ardz>`

- :dokuwiki:`EV-FLOWMETER-ARDZ Sensor for Flow Rate Metering </resources/eval/user-guides/ev-flowmeter-ardz>`

Design and Integration Files
============================

.. admonition:: Download

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/lora-reference-design/ad-max32sxwise-sl-designsupport.zip`

   - Schematic
   - Bill of Materials
   - Layout
   - Fabrication Files

Help and Support
================

For questions and more information about this product, connect with us through
the Analog Devices Engineer Zone.

.. note::

   :ez:`EngineerZone Support Community <reference-designs>`
