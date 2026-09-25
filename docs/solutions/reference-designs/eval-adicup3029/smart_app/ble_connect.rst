ADICUP3029 BLE Connection Documentation
=======================================

This is a guide with information regarding the BLE registration, data packet
size, and configuration. This is will enable users to use the IoTNode smart app
in applications leveraging the capabilities of ADICUP3029 board with Bluetooth
connectivity.

General Description/Overview
----------------------------

IoTNode application permits the connection of a single board at a time to
visualize data from it. However multiple sensors may be present on that board
(ex. temperature, CO, acceleration). The information sent to the application is
tied to the sensor id.

The ADI BLE packet description currently has three types of packets:

=================== =====
Packet type         Value
=================== =====
Registration packet 0x00
Name packet         0x01
Data packet         0x02
=================== =====

The packet type is specified using the packet type sensor id field.

The sensorID/packetType byte is composed of:

==== ==== ==== ==== ==== ==== ==== ====
7    6    5    4    3    2    1    0
==== ==== ==== ==== ==== ==== ==== ====
SID5 SID4 SID3 SID2 SID1 SID0 PKT1 PKT0
==== ==== ==== ==== ==== ==== ==== ====

========= ===========
Sensor ID Packet Type
========= ===========
6 bits    2 bits
========= ===========

You could have multiple sensors on a board with different ids the app shows
information from one sensor at a time. It knows what information is related to
which sensor by using the sensor id.

Registration Packet
~~~~~~~~~~~~~~~~~~~

+-----------------+---------------------------------------------------------+------------+
| Data            | Info                                                    | Size(byte) |
+=================+=========================================================+============+
| pktTypeSensorId | registration packet                                     | 1          |
+-----------------+---------------------------------------------------------+------------+
| numFields       | must match No. of field name packets                    | 1          |
+-----------------+---------------------------------------------------------+------------+
| dataType        | every field in the data packet must have this data type | 1          |
+-----------------+---------------------------------------------------------+------------+
| sensorName      | string with the name of the sensor                      | 17         |
+-----------------+---------------------------------------------------------+------------+

============== ========
SensorID value 6 bits
============== ========
0x00           0b000000
to             to
0x3F           0b111111
============== ========

=============== =========== ============
Data type value Description Size (bytes)
=============== =========== ============
1               Byte        1
2               Short       2
3               Int         4
4               Long        8
5               Float       4
6               Double      8
7               Char        2
=============== =========== ============

Field Name Packet
~~~~~~~~~~~~~~~~~

=============== ================================== ==========
Data            Info                               Size(byte)
=============== ================================== ==========
pktTypeSensorId registration packet                1
fieldId         index of field in data packet      1
fieldName       string with the name of the sensor 18
=============== ================================== ==========

Data Packet
~~~~~~~~~~~

=============== ========================================= ==========
Data            Info                                      Size(byte)
=============== ========================================= ==========
pktTypeSensorId registration packet                       1
Sensor_Data1    Represents 4 bytes float data for field 1 4
Sensor_Data2    Represents 4 bytes float data for field 2 4
Sensor_Data3    Represents 4 bytes float data for field 3 4
Sensor_Data4    Represents 4 bytes float data for field 4 4
=============== ========================================= ==========

*End of Document*
