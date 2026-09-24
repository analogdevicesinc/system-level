.. _single-pair-ethernet-hub developer-guide:

#################
 Developer Guide
#################

The Developer Guide provides the information required to develop, extend, and
integrate applications with SPE Hub. This document defines the MQTT-based
communication protocol between the SPE Hub and embedded MQTT clients.

.. _single-pair-ethernet-hub developer-guide mqtt-client:

******************************
 Local MQTT Broker and Client
******************************

The SPE Hub includes both a local MQTT broker and a local MQTT client. The
broker, implemented with Aedes, runs on the host PC and accepts connections from
embedded nodes. The local client then connects to that broker as a standard MQTT
client with the client ID ``host`` and subscribes to host topics.

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  MQTT Client
      -  Topic Subscription
      -  Description

   -  -  Local
      -  ``host/#``
      -  Receives all messages under the host namespace.

**References:**

-  `aedes <https://www.npmjs.com/package/aedes>`__
-  `mqtt <https://www.npmjs.com/package/mqtt>`__


**********************
 Embedded MQTT Client
**********************

An embedded MQTT client is implemented on a microcontroller running an embedded
TCP/IP stack. The client connects to the MQTT broker on the host PC and uses its
assigned static IPv4 address as its MQTT client identifier, allowing the SPE Hub
to identify and manage each node on the network.

The EVAL-ADIN1140D1Z is used throughout this document as a reference example. It
integrates a microcontroller that hosts both the embedded TCP/IP stack and MQTT
client, with the TCP/IP stack configured to the static IPv4 address
192.168.1.100. This address is presented to the SPE Hub as the MQTT client
identifier when the connection is established.

The following sections detail the protocol requirements and implementation
guidelines that embedded MQTT clients must follow to ensure interoperability
with the SPE Hub.

**References:**

-  `yyjson <https://github.com/ibireme/yyjson>`__
-  `paho.mqtt.c <https://github.com/eclipse-paho/paho.mqtt.c>`__
-  `lwip <https://github.com/lwip-tcpip/lwip>`__

Client Connection Mechanism
===========================

The embedded MQTT client shall use its assigned IPv4 address as the MQTT client
ID when establishing a connection to the MQTT broker. The client shall configure
an MQTT keep-alive interval that enables timely detection of connection loss by
the broker. This ensures that the SPE Hub can accurately maintain node
connectivity state and promptly update node status following a communication
failure or unexpected disconnect.

Once the embedded MQTT client successfully connects to the broker, it subscribes
to a hierarchical topic structure that enables messages to be addressed at
multiple levels, including all nodes, individual nodes, specific evaluation
boards, and device families. This provides flexible support for group-based and
individual communication.

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  MQTT Client
      -  Topic Subscription
      -  Description

   -  -  Embedded
      -  ``node/#``
      -  Network-wide namespace used for messages that apply to all nodes.

   -  -  Embedded
      -  ``192.168.1.100/#``
      -  Node-specific namespace used to target individual nodes.

   -  -  Embedded
      -  ``eval-adin1140d1z/#``
      -  Evaluation board namespace used to target EVAL-ADIN1140D1Z boards.

   -  -  Embedded
      -  ``adin1140/#``
      -  Device namespace used to target ADIN1140 devices.

   -  -  Embedded
      -  ``adin1110/#``
      -  Device namespace used to target ADIN1110 devices.


The local client then publishes a message (an empty-payload message where the
topic name conveys the event) indicating that telemetry publishing may begin.

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  MQTT Client
      -  Topic Publish
      -  Description

   -  -  Local
      -  ``192.168.1.100/publish/start``
      -  Enable MQTT publishing.

Data Publications
=================

The SPE Hub maintains an in-memory data store for each node. MQTT messages
published by the embedded client to the topic below are merged into the
corresponding node context and used to drive rendering of the node-specific user
interface.

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  MQTT Client
      -  Topic Publish
      -  Description

   -  -  Embedded
      -  ``host/192.168.1.100/data``
      -  Publish generic telemetry.

The node data store is maintained as a key-value collection. Incoming MQTT data
is merged on a per-key basis, with existing keys updated using the most recently
published value and new keys added as required.

Mandatory Fields
----------------

The SPE Hub requires a defined set of key-value pairs to be published before an
MQTT client can be registered. Nodes that do not publish the required
information shall remain unregistered and shall not be displayed within the user
interface. Once this information has been published it does not need to be
published again even if the node disconnects.

Embedded Topic: ``host/192.168.1.100/data``

.. code:: json

   {
     "ver": "2.0.0",
     "board": {
       "name": "eval-adin1140d1z",
       "rev": "a",
       "devices": ["max32690", "adin1140", "adin1110", "adt7420", "at24c64d"],
       "regmap": ["adin1140"]
     }
   }

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  Field
      -  Type
      -  Description

   -  -  ``ver``
      -  ``string``
      -  Protocol version.

   -  -  ``board.name``
      -  ``string``
      -  Evaluation board name.

   -  -  ``board.rev``
      -  ``string``
      -  Evaluation board revision.

   -  -  ``board.devices``
      -  ``string[]``
      -  Evaluation board devices.

   -  -  ``board.regmap``
      -  ``string[]``
      -  Supported register devices.

**Example: Initial Publication**

The following message is typically published once during node initialization. It
contains the metadata required by the SPE Hub to register the node and establish
its initial node context.

Embedded Topic: ``host/192.168.1.100/data``

.. code:: json

   {
     "ver": "2.0.0",
     "board": {
       "name": "eval-adin1140d1z",
       "rev": "a",
       "devices": ["max32690", "adin1140", "adin1110", "adt7420", "at24c64d"],
       "regmap": ["adin1140"]
     },
     "max32690": {
       "firmware": { "ver": "1.0.0", "desc": "" }
     },
     "adin1140": {
       "status": true,
       "diags": {
         "plca": [],
         "mac": [],
         "ptp": []
       }
     },
     "adin1110": {
       "status": false,
       "config": [],
       "diags": {
         "link": [],
         "mac": []
       }
     },
     "adt7420": {
       "status": true,
       "config": []
     },
     "at24c64d": {
       "status": false,
       "config": []
     }
   }

**Example: Incremental Publications**

Once the node has been registered, the embedded MQTT client may publish
incremental updates at a periodic rate. Incoming data is merged into the
existing node context, with updated values replacing previous values on a
per-key basis.

Embedded Topic: ``host/192.168.1.100/data``

.. code:: json

   {
     "adin1140": {
       "status": true,
       "diags": {
         "plca": [],
         "mac": [],
         "ptp": []
       }
     },
     "adin1110": {
       "status": false,
       "config": [],
       "diags": {
         "link": [],
         "mac": []
       }
     },
     "adt7420": {
       "status": true,
       "config": []
     },
     "at24c64d": {
       "status": false,
       "config": []
     }
   }

Register Control Publications
=============================

The SPE Hub enables register read and write operations to devices defined in the
initial data publication.

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  MQTT Client
      -  Topic Subscription
      -  Description

   -  -  Embedded
      -  ``eval-adin1140d1z/register/adin1140/write``
      -  Evaluation board topic for register write to ADIN1140.

   -  -  Embedded
      -  ``adin1140/register/adin1140/write``
      -  Device topic for register write to ADIN1140.

   -  -  Embedded
      -  ``192.168.1.100/register/adin1140/write``
      -  Node topic for register write to ADIN1140.

   -  -  Embedded
      -  ``eval-adin1140d1z/register/adin1140/read``
      -  Evaluation board topic for register read to ADIN1140.

   -  -  Embedded
      -  ``adin1140/register/adin1140/read``
      -  Device topic for register read to ADIN1140.

   -  -  Embedded
      -  ``192.168.1.100/register/adin1140/read``
      -  Node topic for register read to ADIN1140.

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  MQTT Client
      -  Topic Publish
      -  Description

   -  -  Embedded
      -  ``host/192.168.1.100/register/adin1140/read``
      -  Node topic for register read response from ADIN1140.

   -  -  Embedded
      -  ``host/192.168.1.100/register/adin1140/write``
      -  Node topic for register write response from ADIN1140.

**Example: Register Read Request**

-  Local Topic: ``eval-adin1140d1z/register/adin1140/read``
-  Local Topic: ``adin1140/register/adin1140/read``
-  Local Topic: ``192.168.1.100/register/adin1140/read``

.. code:: json

   {
     "addr": 18
   }

-  Embedded Topic: ``host/192.168.1.100/register/adin1140/read``

.. code:: json

   {
     "addr": 18,
     "data": 4660
   }

**Example: Register Write Request**

-  Local Topic: ``eval-adin1140d1z/register/adin1140/write``
-  Local Topic: ``adin1140/register/adin1140/write``
-  Local Topic: ``192.168.1.100/register/adin1140/write``

.. code:: json

   {
     "addr": 18,
     "data": 4660
   }

-  Embedded Topic: ``host/192.168.1.100/register/adin1140/write``

.. code:: json

   {
     "addr": 18,
     "data": 4660
   }

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  Field
      -  Type
      -  Description

   -  -  ``addr``
      -  ``number``
      -  Register address information.

   -  -  ``data``
      -  ``number``
      -  Register data information.

Sense Publications
==================

The SPE Hub supports a dedicated sense topic for sensor measurements. Clients
publish samples to sense subtopics, and the Hub handles aggregation, storage,
and visualization automatically.

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  MQTT Client
      -  Topic Publish
      -  Description

   -  -  Embedded
      -  ``host/192.168.1.100/sense/temp-rsvd``
      -  Publish node default temperature sample for the Hub.

   -  -  Embedded
      -  ``host/192.168.1.100/sense/voltage``
      -  Publish node voltage sample.

   -  -  Embedded
      -  ``host/192.168.1.100/sense/current``
      -  Publish node current sample.

Temperature (Reserved)
----------------------

The temp-rsvd subtopic is reserved for the SPE Hub's built-in temperature chart.
The chart does not store raw samples; instead, it aggregates incoming data into
time-aligned buckets that keep graph resolution stable while preserving trend
information. Each viewing window uses its own bucket size. Multiple samples
arriving within the same bucket are reduced into summary values (average,
minimum, maximum, and count).

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  Window
      -  Bucket Size
      -  Max Buckets

   -  -  10 min
      -  5 s
      -  120

   -  -  1 hr
      -  15 s
      -  240

   -  -  6 hrs
      -  60 s
      -  360

   -  -  12 hrs
      -  90 s
      -  480

   -  -  24 hrs
      -  120 s
      -  720

Incoming sensor measurements are staged and committed on a 1-second service
tick. If multiple samples arrive within the same second, only the most recent
sample is retained for that tick. This means the minimum publish period of
the reserved temperature measurement is one second.

**Example: Temperature**

Embedded Topic: ``host/192.168.1.100/sense/temp-rsvd``

.. code:: json

   {
     "y": 26.5
   }

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  Field
      -  Type
      -  Description

   -  -  ``y``
      -  ``number``
      -  Temperature sample value in degrees Celsius.

Generic Sense
-------------

Sense subtopics can be visualized using the Sense Chart template component, with
the topic field selecting the measurement to display. This allows a node to
publish multiple measurements, such as voltage and current, each rendered on its
own chart. Up to two generic sensor streams are supported per node. Additional
sense subtopics beyond the first two are ignored. Unlike the reserved
temperature stream, generic sensor streams are displayed as raw samples rather
than being aggregated into time-aligned buckets. Incoming data points are
retained in a rolling buffer and plotted directly within a 60-second sliding
window, providing a real-time view of the most recent measurements.

**Example: Voltage**

Embedded Topic: ``host/192.168.1.100/sense/voltage``

.. code:: json

   {
     "y": 3.3
   }

**Example: Current**

Embedded Topic: ``host/192.168.1.100/sense/current``

.. code:: json

   {
     "y": 0.42
   }

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  Field
      -  Type
      -  Description

   -  -  ``y``
      -  ``number``
      -  Sensor sample value for the subtopic.

LED Control Publications
========================

The SPE Hub enables LED control for evaluation boards.

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  MQTT Client
      -  Topic Subscription
      -  Description

   -  -  Embedded
      -  ``eval-adin1140d1z/led``
      -  Evaluation board topic for LED control.

   -  -  Embedded
      -  ``192.168.1.100/led``
      -  Node topic for LED control.

**Example: LED Control Request**

Local Topic: ``192.168.1.100/led``

.. code:: json

   {
     "type": 0,
     "cmd": 2
   }

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  Field
      -  Type
      -  Description

   -  -  ``type``
      -  ``number``
      -  Selector. 0 = ALL LEDs, 1 = LED1, 2 = LED2, etc.

   -  -  ``cmd``
      -  ``number``
      -  Command. 0 = OFF, 1 = ON, 2 = TOGGLE.

.. _single-pair-ethernet-hub developer-guide templates:

***********
 Templates
***********

Templates control how a node's published data is presented on its device page.
Telemetry structures and available data vary between nodes, so SPE Hub renders
each node using a template selected from its board metadata.

SPE Hub supports two kinds of templates:

-  **Custom templates** are HTML and CSS layouts.
-  **Component templates** are built-in, application-defined widgets.

Structure
=========

Templates are loaded from the ``resources/templates`` directory. Each template
resides in a dedicated folder whose name matches its identifier, resolved from
the node's board metadata: ``board.template`` if present, otherwise
``board.name``.

.. code:: text

   resources/templates/
   ├── resources/                    # Common assets
   │   └── cpu-bold.svg
   └── eval-adin1140d1z/             # Template identifier (board.template or board.name)
       ├── manifest.json             # Entry point for the template
       ├── eval-adin1140d1z.html
       ├── eval-adin1140d1z.css
       ├── adin1140.html
       ├── adin1140.css
       └── resources/                # Template-specific assets
           └── EVAL-ADIN1140D1Z.png

Templates are hot-reloaded: SPE Hub watches ``resources/templates`` and
re-renders the affected node when a ``.html``, ``.css``, or ``.json`` file
changes.

Manifest
========

The ``manifest.json`` file is the entry point for a template and defines the
content rendered on the node's device page. It contains two arrays, ``custom``
and ``components``, which are processed in order and rendered as they appear in
the manifest.

.. code:: json

   {
     "custom": [
       {
         "path": "templates/eval-adin1140d1z/eval-adin1140d1z",
         "data": ["adin1140", "max32690", "adt7420", "adin1110"],
         "card": {
           "title": "EVAL-ADIN1140D1Z",
           "subtitle": "Evaluation Board",
           "accordion": true
         }
       },
       {
         "path": "templates/eval-adin1140d1z/adin1140",
         "data": ["adin1140"],
         "card": {
           "title": "ADIN1140",
           "subtitle": "Device Diagnostics",
           "accordion": true
         }
       }
     ],
     "components": [
       {
         "type": "temp-chart",
         "card": { "title": "Temperature Chart", "accordion": true }
       },
       {
         "type": "sense-chart",
         "config": { "topic": "voltage", "yLabel": "Voltage (V)" },
         "card": { "title": "Voltage Chart", "accordion": true }
       }
     ]
   }

Each ``custom`` and ``component`` entry is rendered within a card on the device
page. The ``card`` object controls the card's title, subtitle, and user
interface behavior.

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 20 60
   :class: bold-header

   -  -  Field
      -  Type
      -  Description

   -  -  ``title``
      -  ``string``
      -  Heading text displayed on the card. Required.

   -  -  ``subtitle``
      -  ``string``
      -  Optional secondary text displayed beneath the title.

   -  -  ``accordion``
      -  ``boolean``
      -  When ``true``, the card can be collapsed and expanded by the user.

Custom Templates
================

Custom templates are HTML and CSS layouts that render board-specific content.
Each entry in the manifest's ``custom`` array is compiled, populated with
published node data, sanitized, and rendered inside its card.

Fields
------

A custom entry is described by three fields.

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 20 60
   :class: bold-header

   -  -  Field
      -  Type
      -  Description

   -  -  ``path``

      -  ``string``

      -  Path to the layout files, relative to the ``resources`` directory and
         specified without a file extension. SPE Hub loads the corresponding
         ``.html`` file and, optionally, a matching ``.css`` file.

   -  -  ``data``
      -  ``string[]``
      -  Published data keys required by the layout. Only the specified keys are
         exposed to the template.

   -  -  ``card``
      -  ``object``
      -  The card header used to frame the rendered layout.

Sanitization
------------

Template content is sanitized before rendering to prevent script injection and
cross-site scripting (XSS) attacks. Only the HTML elements listed below are
permitted; any other markup is stripped from the output. The following HTML
tags are supported within templates:

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: bold-header

   -  -  Category
      -  Supported Tags
   -  -  Container
      -  ``div``, ``span``, ``section``, ``p``
   -  -  List
      -  ``ul``, ``ol``, ``li``
   -  -  Heading
      -  ``h1``, ``h2``, ``h3``, ``h4``, ``h5``, ``h6``
   -  -  Text style
      -  ``strong``, ``em``, ``b``, ``i``, ``small``
   -  -  Media
      -  ``img``
   -  -  Control
      -  ``button``
   -  -  Formatting
      -  ``br``

Component Templates
===================

Component templates are built-in widgets instantiated by SPE Hub at runtime.
Beyond visualization, they can provide interactive functionality such as user
actions, command execution, and device controls, with the logic maintained
inside the application.

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 80
   :class: bold-header

   -  -  Type
      -  Description

   -  -  ``temp-chart``
      -  Real-time temperature chart for the node, sourced from the node's
         temperature telemetry stream.

   -  -  ``sense-chart``
      -  Generic real-time line chart bound to a sensor telemetry stream. The
         ``topic`` selects the telemetry channel to plot, and ``yLabel`` sets
         the y-axis label.

