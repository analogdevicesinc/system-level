.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-gmsl2eth-sl

.. _ad-gmsl2eth-sl:

AD-GMSL2ETH-SL User Guide
=========================

Introduction
------------

The **AD-GMSL2ETH-SL** is an edge compute platform enabling low latency data
transfer from eight
:adi:`Gigabit Multimedia Serial Link™ (GMSL) <en/product-category/gigabit-multimedia-serial-link.html>`
interfaces on to a 10 Gb Ethernet link. The target applications include
autonomous robots and vehicles where machine vision and real-time sensor fusion
is critical. Some of the main features and benefits include:

- 8 x GMSL2 camera interfaces with up to 6 Gbps/channel
- 10 Gbps SFP+ Ethernet interface
- Precision Time Protocol for synchronization with host systems and other edge
  devices
- Embedded processing capabilities using the on-board
  `AMD Kria K26 System-on-Module Industrial <https://www.amd.com/en/products/system-on-modules/kria/k26/k26i-industrial.html>`__
- ROS2 compliant
- Open-source embedded Linux software and FPGA design
- Advanced camera triggering functions and control features ​

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmsl2eth-sl.jpg
   :width: 350px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-gmsl2eth-sl-block-diagram.png
   :width: 480px

--------------

Specifications
--------------

.. list-table::
   :header-rows: 1

   * - Interfaces
     -
   * - SFP+
     - Supports 10 Gb Ethernet with IEEE 1588 hardware timestamping
   * - RS232
     - Serial interface for connecting UART peripherals, e.g., GNSS devices
   * - I/O
     - 16 general purpose I/O pins with software configurable functionality, 3.3
       V voltage level
   * - GMSL
     - 2 x Quad Fakra connectors supporting 8 x GMSL camera interfaces
   * - Processing
     -
   * - AMD K26
     - Industrial grade AMD K26 SoM
   * - Power & Thermal
     -
   * - Power supply
     - Input voltage: 9 V to 48 V DC at 24 W max
   * - Operating temperature
     - -40°C to 60°C
   * - Software
     -
   * - Operating system
     - Linux OS
   * - Network data protocol
     - RTP over UDP with software implementation and option for licensable FPGA
       accelerated RTP & UDP stack

System setup & evaluation
-------------------------

.. note::

   Follow the
   :dokuwiki:`AD-GMSL2ETH-SL System Setup & Evaluation </resources/eval/user-guides/ad-gmsl2eth-sl-guide>`
   guide to get the system up and running.

--------------

Help and Support
----------------

For questions and more information, please contact us on the Analog Devices
Engineer Zone.

.. note::

   :ez:`EngineerZone Support Community <reference-designs>`
