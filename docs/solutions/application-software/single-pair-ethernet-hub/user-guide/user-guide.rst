.. _single-pair-ethernet-hub user-guide:

############
 User Guide
############

The User Guide is intended for users evaluating Single Pair Ethernet (SPE)
devices with the SPE Hub. It explains how to configure the host PC and network
for device discovery, and how to use the application's features to monitor
telemetry, control devices, and interact with the network in real time.

********************
 Network Topologies
********************

The network topologies section describes a range of supported network
configurations for evaluating SPE Hub with evaluation kits, including multidrop,
daisy-chain, point-to-point, and switched network topologies.

.. toctree::
   :maxdepth: 1

   network-topologies/network-topologies

.. _single-pair-ethernet-hub user-guide configuration:

**********************
 Network Configuration
**********************

Network Connection
==================

The Network Connection page is displayed when SPE Hub is launched. This page
serves as the entry point to the application and is used to select the network
adapter required for device discovery and communication. SPE Hub starts a local
MQTT broker and client bound to the IPv4 address of the selected network
adapter. The broker accepts MQTT connections on the standard unsecured port
(1883).

An IPv4 address uniquely identifies a device on the network. SPE Hub requires
the host PC and all embedded MQTT clients to be configured with unique IPv4
addresses. This allows devices to be uniquely addressed on the network, enabling
reliable routing of MQTT traffic between clients and the broker.

The subnet mask defines which portion of an IPv4 address identifies the network
and which portion identifies an individual device. With a subnet mask of
``255.255.255.0``, addresses sharing the first three octets belong to the same
subnet. For example, ``192.168.1.10``, ``192.168.1.20``, and ``192.168.1.50``
are all members of the ``192.168.1.0/24`` subnet and can communicate directly
with one another.

The default gateway is the IPv4 address of a router used to forward traffic
outside the local subnet. In most SPE Hub deployments, the default gateway field
can be left unconfigured, as the host PC and embedded MQTT clients communicate
within the same subnet and do not require traffic to be routed through a
gateway.

.. figure:: network-connection.png

   *Network Connection*

Network Adapter Configuration
-----------------------------

The network adapter can be assigned a static IPv4 address using the following
method:

#. Open Control Panel > Network and Internet > Network and Sharing Center.

#. Select Change adapter settings, then open Properties for the target Ethernet
   adapter.

#. Open Internet Protocol Version 4 (TCP/IPv4), select Use the following IP
   address, and set:

   -  IP Address: 192.168.1.200
   -  Subnet Mask: 255.255.255.0

#. Click OK to save and close all dialogs.

.. note::

   The IP address and subnet mask shown above are examples. These settings may
   need to be adjusted to match the network configuration.

.. figure:: network-adapter.png

   *Network Adapter Configuration*

Firewall Configuration
----------------------

To accept inbound MQTT connections from embedded clients, Windows Defender
Firewall may need to be configured to allow TCP traffic on port 1883. Port 1883
is the standard port for unsecured MQTT and is used by the SPE Hub local MQTT
broker service to accept connections from devices on the network.

A new inbound rule can be created using the Windows Defender Firewall with
Advanced Security console. The following steps create a rule that permits
inbound TCP traffic on port 1883:

#. Open Windows Defender Firewall with Advanced Security, select Inbound Rules,
   and choose New Rule to start the New Inbound Rule Wizard.

#. Select Port as the rule type, then set the protocol to TCP and specify port
   1883 as the local port to allow.

#. Select Allow the connection, and apply the rule to the network profiles
   (Domain, Private, and Public) that match the deployment environment.

#. Provide a descriptive name for the rule, such as ``SPE Hub MQTT (1883)``, and
   finish the wizard to enable it.

.. figure:: firewall-rule-step1.png

   *Step 1 - Create a new inbound rule*

.. figure:: firewall-rule-step2.png

   *Step 2 - Allow TCP port 1883*

.. figure:: firewall-rule-step3.png

   *Step 3 - Allow the connection*

.. figure:: firewall-rule-step4.png

   *Step 4 - Name and enable the rule*

*************
 Application
*************

The Single Pair Ethernet (SPE) Hub is an MQTT-based evaluation platform for SPE
products, enabling users to design, evaluate, and validate proof-of-concept
applications through real-time device monitoring and control. This section
describes the pages and features available once a network connection has been
established.

Network Overview
================

The Network Overview page serves as the main dashboard of the application.
Connected MQTT clients are automatically discovered and displayed in the
navigation pane when the MQTT service is active. The dashboard provides
visibility into network activity and access to monitoring, control, and
configuration functions.

.. figure:: network-overview.png

   *Network Overview*

Temperature Chart [Built-In]
----------------------------

The Temperature Chart provides a real-time visualization of temperature data
from all connected nodes. Temperature measurements are displayed using a
multi-series line plot, with a dedicated trace for each node. The chart supports
configurable x-axis time-window selection, allowing temperature data to be
viewed over periods of 10 minutes, 1 hour, 6 hours, 12 hours, or 24 hours. The
y-axis can be operated in either Automatic or Manual mode, with manual controls
available for configuring the display range and scale step size. Individual node
traces can be shown or hidden using the legend controls, allowing users to focus
on specific devices or compare behavior across multiple nodes. The chart
provides a real-time view of temperature activity across the network, enabling
users to monitor sensor behavior, identify missing telemetry, detect node
communication issues, and compare measurements between connected devices.

Network Table
-------------

The Network Table provides an operational view of the deployed network, listing
all discovered devices and their current state. Each entry includes a set of
actions that allow users to interact directly with a node. These controls
support both device identification and network administration, enabling users to
activate an onboard LED for physical identification or to kick a client from the
MQTT network.

Register Control
----------------

The Register Control component provides a mechanism for reading from and
writing to device registers across the connected network. The workspace is
divided into three complementary components: Access, Queue and History.
Register Access enables users to perform individual register read and write
transactions on devices associated with a selected node. Register Queue supports
the import and execution of predefined command sequences, simplifying repetitive
register operations and large-scale device configuration. Register History
maintains a chronological record of all register transactions, including request
details, execution status and response data.

The Register Queue component accepts CSV files containing one register
transaction per row. Each row specifies the target, device, action,
address, and optional data value required to perform a register transaction.
Imported commands are processed sequentially in the order they appear within the
queue. Transactions that encounter validation errors are dropped.

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 20 20
   :width: 100%
   :class: bold-header

   -  -  Target
      -  Device
      -  Action
      -  Address
      -  Data

   -  -  192.168.1.101
      -  adin1140
      -  write
      -  0x010037
      -  0x1234

   -  -  192.168.1.101
      -  adin1140
      -  read
      -  0x010037
      -

   -  -  eval-adin1140d1z
      -  adin1140
      -  read
      -  0x010037
      -

   -  -  adin1140
      -  adin1140
      -  read
      -  0x010037
      -

.. note::

   For ADIN1140 and similar devices, the address field is formed by
   concatenating the MMS and register address. For example, ``0x010037``
   corresponds to MMS ``0x01`` and Address ``0x0037``.

.. figure:: register-control.png

   *Register Control*

MQTT Control
============

The MQTT Control component provides a centralized interface for MQTT messaging
within SPE Hub. It supports manual message publication, periodic message
transmission, and monitoring of publish activity through a configurable message
catalog.

The publish component provides generic MQTT message transmission capabilities
within SPE Hub. It allows users to send predefined MQTT messages directly from
the application without requiring an external MQTT client. Messages are loaded
from a selected message catalog, where each entry defines a display name, topic,
and payload. Users can review the message definition and publish it either as a
single transmission or as a recurring transmission.

Interval-based publishing supports configurable transmission periods between
1000 ms and 5000 ms in 500 ms increments. Active interval messages can be
paused, resumed, or removed as required. All transmitted messages are recorded
in the Publish Activity panel, providing a history of message publication.

.. figure:: mqtt-control.png

   *MQTT Control*

Node Navigation
===============

The left sidebar serves as a navigator for all discovered nodes. Devices are
grouped by evaluation board type, support search-based filtering, and provide
status indicators for quick identification of active and inactive nodes.
Selecting a node opens its dedicated device page, which is rendered using a
board-specific template.

Node Template
=============

Templates define how node data is presented within SPE Hub. As telemetry
structures, measurements, and device capabilities vary between evaluation
boards, templates provide a flexible mechanism for displaying board-specific
information and visualizations. Each supported board type is associated with a
dedicated template that maps telemetry and register data to tailored layouts,
controls, and graphics. When a node is selected, SPE Hub automatically loads the
appropriate template, presenting device information in a consistent, intuitive,
and meaningful format across different products.

.. figure:: eval-adin1140d1z-node-overview.png

   *EVAL-ADIN1140D1Z Node Overview*
