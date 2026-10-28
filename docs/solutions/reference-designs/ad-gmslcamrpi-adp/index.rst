.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-gmslcamrpi-adp

.. _ad-gmslcamrpi-adp:

AD-GMSLCAMRPI-ADP#
==================

GMSL EV Kit Adapter Board.

Seamlessly insert GMSL into the signal chain and create a full GMSL Camera
System with off-the-shelf parts.

.. figure:: signal_chain.png
   :width: 600 px

   GMSL Signal Chain

Overview
--------

The `AD-GMSLCAMRPI-ADP# <design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-GMSLCAMRPI-ADP.html>`__
enables connecting GMSL serializer and deserialier Evaluation Kits (EVK) to a
wide range of cameras and processing platforms supporting industry standard
ribbon cable connectors. The adapter consists of three sections that can be
broken apart from each other, with the following functionalities:

- A **Ribbon Cable Adapter** having two pairs of 15-pin and 22-pin connectors
  routed to each other. The 15-pin connectors support 2 MIPI lanes, while the
  22-pin connectors support 4 MIPI lanes.
- A **GMSL Serializer EVK Adapter** with two 22-pin ribbon cable connectors, for
  connecting cameras to the GMSL serializers. A USB Type-A connector is
  available to supply 5V at 4A to another system.
- A **GMSL Deserializer EVK Adapter** with two 22-pin ribbon cable connectors,
  for connecting to Raspberry Pi, Nvidia or Xilinx development platforms, or
  any other processing platform supporting the 15-pin or 22-pin ribbon cable
  connectors.

.. figure:: block_diagram.png
   :width: 600 px

   AD-GMSLCAMRPI-ADP# Simplified Block Diagram

.. figure:: wikigmsladptop.png
   :width: 600 px

   AD-GMSLCAMRPI-ADP# GMSL Boards

Specifications
--------------

.. csv-table::
   :file: specifications.csv

.. Warning:: Do not use the 15-pin ribbon cable included with the Raspberry Pi camera since that is an opposite sided cable.

**Hardware Design Files**

- :dokuwiki:`Schematics <_media/resources/eval/user-guides/02_075922a_top.pdf>`
- :dokuwiki:`Layout <_media/resources/eval/user-guides/08_075922a.zip>`
- :dokuwiki:`High level BOM <_media/resources/eval/user-guides/05-075922-01-a.zip>`

GMSL EV Kit Compatibility
-------------------------

The MIPI-CSI2 signals, I2C communication, and power pins align on the EV kits
but the MFP connections can vary.

Refer to the :dokuwiki:`Serializer and Deserializer EV Kit Compatibility Guide <resources/eval/user-guides/ad-gmslcamrpi-adp/comp_guide>` to see the connections across EV kits.

Camera Connections
------------------

Connect RPi 15-pin cameras to GMSL Serializer EV Kit’s with the 15-pin to 22-pin
adapter. Or use a 15-pin to 22-Pin Adapter Cable.

.. figure:: wikigmslcamadpser.png
   :width: 500 px

   Connecting RPi Camera directly via Adapter


.. figure:: wikigmsl15adp22ser.png
   :width: 500 px

   Connecting RPi Camera using Adapter Cables

SoC Connections
---------------

The same configuration is used for the SoC side where the 22-pin adapter can be
directly connect to a Jetson Orin Development kit or use the 22-15 pin adapter
to connect to an Raspberry Pi.

.. figure:: wikigmsladpdesjeto.png
   :width: 500 px

   SoC Connection to Jetson Orin Development Kit

.. figure:: wikigmsladpdesrpi4.png
   :width: 500 px

   SoC Connection to Raspberry Pi

Example Configurations
----------------------

The adapter can be used to connect the GMSL Deserializer EV kits to a number of
processing platforms for GMSL evaluation and application development. The user
guides below provide instructions on how to get the systems up and running by
configuring the hardware and running the associated software.

- :dokuwiki:`Nvidia Jetson Orin Nano User Guide <resources/eval/user-guides/ad-gmslcamrpi-adp/ug_nvidia_jetson_orin_nano>`
- :dokuwiki:`Raspberry Pi User Guide <resources/eval/user-guides/ad-gmslcamrpi-adp/ug_rpi>`
- :dokuwiki:`AMD Kria User Guide <resources/eval/user-guides/ad-gmslcamrpi-adp/ug_amd_kria>`

Software Development
--------------------

The GMSL Linux kernel drivers, the complete Linux distributions for the
supported processing platforms, and software user guides can be found on the
:git-gmsl:`/`.

User Guides
-----------

.. toctree::
   :titlesonly:
   :maxdepth: 2
   :glob:

   */index

Support
-------

For questions and more information, please contact us on the **Analog Devices
Engineer Zone**.

- :ez:`EngineerZone Linux Software Drivers <linux-software-drivers>`
- :ez:`EngineerZone FPGA Reference Designs <fpga>`

