.. imported from: https://wiki.analog.com/resources/eval/user-guides/admv96s-wgbe-ek1

.. _admv96s-wgbe-ek1:

ADMV96S-WGBE-EK1
=================

60 GHz Wireless Connector.

Overview
--------

The :adi:`ADMV96S-WGBE-EK1` is a complete evaluation and
prototyping system for 60 GHz short data links. It consists of a pair of
receiver and transmitter boards with a 1 Gbps Ethernet interface on each side of
the wireless link.

The 60 GHz wireless link is implemented by the :adi:`ADMV9615` and
:adi:`ADMV9625` modules. These are coupled with a SerDes device
which translates the modules’ SGMII interface to RGMII so that it can be
connected to an ADIN1300 industrial low latency and low power 1 Gbps Ethernet
PHY. This enables each side of the wireless link to act as an Ethernet port and
essentially create a seamless wire-like connection between two ends of an
Ethernet cable.

The on-board :adi:`MAX32650` ultralow power ARM® Cortex®-M4
microcontroller controls the system’s operation and implements the algorithms to
configure the wireless link in real time so that optimal link quality is
constantly maintained over temperature and various operating conditions. An
open-source software stack is provided for firmware development as well as
reference applications. The MAX32650 can be programmed and debugged through a
JTAG SWD header which can also be used for connecting the Wethlink GUI
application to the board.

.. figure:: 60ghz_link_side_projection.jpg

   ADMV96S-WGBE-EK1 Evaluation Kit

.. figure:: evaal-admv96s-wgbe-ek1.png

   ADMV96S-WGBE-EK1 Simplified Block Diagram

Features
--------

- Allows evaluation and prototyping of 60 GHz short data links to replace
  traditional mechanical connectors in moving joints
- 1 Gbps / 100 Mbps / 10 Mbps Ethernet interface on both sides of the wireless
  data link
- Fully programmable system allowing ultimate flexibility for custom
  developments
- Open-source software stack for firmware development
- Open-source GUI for system configuration, monitoring, and control

Applications
------------

- Slip rings
- Magnetic resonance imaging systems
- Autonomous Guided Vehicles
- Truck and trailer coupling
- Railway coupling

Specifications
--------------

+--------------------------+--------------------------------------------------+
| User Interfaces          |                                                  |
+==========================+==================================================+
| LEDs                     | Power status, TX and RX gain status, TX and RX   |
|                          | PLL lock status, Ethernet status                 |
+--------------------------+--------------------------------------------------+
| Connectivity             |                                                  |
+--------------------------+--------------------------------------------------+
| 10-pin Cortex SWD header | May be used with MAXDAP (MAX32625PICO) external  |
|                          | adapter for connecting the Wethlink GUI to the   |
|                          | evaluation board and for programming firmware.   |
+--------------------------+--------------------------------------------------+
| Ethernet                 | 1xRJ45 1 Gbps / 100 Mbps / 10 Mbps Ethernet port |
+--------------------------+--------------------------------------------------+
| Power supply             |                                                  |
+--------------------------+--------------------------------------------------+
| External power           | 12 VDC at 2A, 2.10 mm ID (0.083“), 5.50 mm OD    |
|                          | (0.217”) connector                               |
+--------------------------+--------------------------------------------------+
| Mechanical Specs         |                                                  |
+--------------------------+--------------------------------------------------+
| Dimensions               | 3.283 x 2.362                                    |
+--------------------------+--------------------------------------------------+

Package Contents
----------------

- 2x ADMV96x5 reference design boards
- ADMV9615
- ADMV9625
- 2x support PCBs
- 1x rail system
- 2x heatsinks
- 2x MAXDAP programmer
- 2x VEL36US120 power adapter
  *Users may need to purchase different adapter
  plugs to accommodate the various power socket standards in different countries
  or regions*

User Guides
-----------

Getting your system up and running by following the user guides.

.. tip::
   Access hardware setup procedure, design files, and

.. toctree::
   :caption: The following user guides are available:
   :titlesonly:
   :maxdepth: 2
   :glob:

   */index

Application Development
-----------------------

Example 1 – Demonstrate Gigabit Capability by Connecting to the Internet Using LAN with the Contactless 60 GHz Link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: use_case_1.png

   ADMV9615 and ADMV9625 Contactless Ethernet Link Labeled Pair1 and Pair-2

Hardware Connections
^^^^^^^^^^^^^^^^^^^^

.. figure:: use_case_1_hw_connections.png

   Hardware Connections for Example 1

#. Mount the ADMV9615 and ADMV9625 Assemblies onto the guide rails with patch
   antennas facing each other.
#. Connect 12V power supplies.
#. Connect one RJ45 Ethernet connector to your PC.
#. Connect the other RJ45 Ethernet connector to your Local Area Network.
#. Turn off your PC’s Wi-Fi connection.
#. Within a few seconds, your PC should connect to your LAN with a speed of up
   to 1 Gbps (if your network can support it)
#. (Optional) Connect MAXDAP connector using a micro-USB to your PCs if you
   would like to configure the firmware.

Example 2 – Create a Two PC LAN Connected with the Contactless 60GHz Link and Share Large Data Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: use_case_2.png

   ADMV9615 and ADMV9625 Contactless Ethernet Link Labeled Pair-1 and Pair-2

Hardware Connections
^^^^^^^^^^^^^^^^^^^^

.. figure:: use_case_2_hw_connections.png

   Hardware Connections for Example 2

#. Mount the ADMV9615 and ADMV9625 assemblies onto the guide rails with patch
   antennas facing each other.

#. Connect 12V power supply, 2 PL.
#. Connect one RJ45 Ethernet connector to PC1’s Ethernet jack.
#. Connect the other RJ45 Ethernet connector to PC2’s Ethernet jack.

File Sharing Setup
^^^^^^^^^^^^^^^^^^

The following procedure was taken from:
`How to Share Files between Two Computers Using LAN Cable – TechWiser <https://techwiser.com/how-to-connect-pc-to-pc-lan-cable/>`_

- On PC1, go to the Start menu and search “Control Panel”. Once you see it,
  click on it, to open it.

.. figure:: file_sharing_setup.png

   File Sharing Setup

- Choose **Networks and Internet**.
- Next, choose **Network and Sharing Center**.
- Click on **Advanced Sharing Settings**.
- Choose **All Networks**.

.. figure:: network_settings.png

.. figure:: network_settings_2.png

- Choose **Turn on Sharing**.

.. figure:: network_and_sharing.png

- Turn off Password Protection (Once Done with File Sharing Turn Password
  Protection Back On)
- Perform steps 2 through 6 for PC2.

To put both PCs on the same network, manually set up IP settings by opening
**Control Panel**.

- Choose **Network and Sharing**.
- Select **Ethernet** and click **Properties**.
- Select **Internet Protocol Version 4 (TCP/IPv4)**.
- Select **Properties**.

For PC1, choose “Use the following IP address”.

.. figure:: ip_address.png

- IP Address: **192.168.1.1**
- Subnet mask: **255.255.255.0**
- Default Gateway: **192.168.1.2**

Use the following DNS server address:

- Preferred DNS Server: **208.67.222.222**
- Alternate DNS server: **208.67.220.220**

For PC2, choose “Use the following IP address”.

.. figure:: pc2_ip_address.png

- IP Address: **192.168.1.2**.
- Subnet mask: **255.255.255.0**.
- Default Gateway: **192.168.1.1**.

Use the following DNS server addresses:

- Preferred DNS Server: **208.67.222.222**
- Alternate DNS Server: **208.67.220.220**

.. figure:: network_tab.png

- Open Windows Explorer and click on the **Network** tab.
- If everything is set up properly, both computers should appear.
- You still need to share a target folder on the LAN.
- Create a new **folder** on the desktop and place some large files into it.

.. figure:: creating_a_folder.png

- Select the folder you want to share and right-click it.
- Choose **Everyone** and click **Add**.

.. figure:: sharing_settings.png

- Once shared, the next window will show the location of the folder.
- That’s it! Go back to the PC from which you want to access the file, open the
  **Networks** panel, and click on the other computer’s name.
- Here you will see the folder you just shared. Open the folder and
  transfer files and folders as you normally do—copy and paste, etc.
- You can repeat these steps from the other computer as well.

.. figure:: shared_folder.png

Example 3 – Use Iperf to Check Ethernet Link Speed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: use_case_3.png

   ADMV9615 and ADMV9625 Contactless Ethernet Link Labeled Pair1 and Pair2

Hardware Connections
^^^^^^^^^^^^^^^^^^^^

.. figure:: use_case_3_hw_connections.png

   Hardware Connections for Example 3

#. Mount the ADMV9615 and ADMV9625 assemblies onto the guide rails with patch
   antennas facing each other.
#. Connect 12V power supplies.
#. Connect one RJ45 Ethernet connector to PC1’s Ethernet jack.
#. Connect the other RJ45 Ethernet connector to PC2’s Ethernet jack.

Iperf
-----

Follow the Procedure from Example 2 for File Sharing Using a 2 PC LAN:

Iperf is a free tool for network performance and measurement,
`download it here <https://iperf.fr/iperf-download.php>`__

.. figure:: iperf.png

-   Unzip the downloaded archive.

-   On PC1, open a DOS Command window and navigate to the directory where iperf
    is installed:

    .. shell:: ps1

       $cd C:\Users\Public\Documents\iperf-3.1.3-win64

-   Set this computer as the server:

    .. shell:: ps1

       /c/Users/Public/Documents/iperf-3.1.3-win64
       $iperf3.exe -s

-   On PC2, open a DOS Command window and Navigate to the directory where iperf is
    installed:

    .. shell:: ps1

       $cd C:\Users\Public\Documents\iperf-3.1.3-win64

-   Set this computer as the client. Type in

    .. shell:: ps1

       /c/Users/Public/Documents/iperf-3.1.3-win64
       $iperf3.exe -c 192.168.1.1

    .. figure:: iperf_settings.png

-   Iperf tests the link speed about 950 Mbps.

Resources
---------

- :ref:`ADMV96S-WGBE-EK1 Software User Guide <admv96s-wgbe-ek1 software-guide>`
- :git-no-OS:`ADMV96S-WGBE-EK1 Firmware Project <projects/wethlink>`
- `Wethlink Installer <https://swdownloads.analog.com/update/wethlink/latest/wethlink_installer.exe>`__

Help and Support
-----------------

For questions and more information, please visit the Analog Devices
:ez:`EngineerZone Support Community <reference-designs>`.

