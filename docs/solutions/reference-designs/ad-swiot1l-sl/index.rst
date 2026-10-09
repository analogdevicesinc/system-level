.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-swiot1l-sl

AD-SWIOT1L-SL
=============

Software-configurable Analog and Digital I/O with 10BASE-T1L Evaluation and Development Platform.


Introduction
------------

The :adi:`AD-SWIOT1L-SL` is a complete hardware and software platform for
prototyping intelligent, secure, network-capable field devices, with
applications in factory automation, process control, and intelligent buildings.
Some of the main features and benefits include:

- Ultimate flexibility in I/O interface configurability through software
- Embedded processing for implementing self-capable edge devices
- Built-in security for root-of-trust, mutual authentication, data
  confidentiality and integrity, secure boot, and secure communications
- Long-range single-pair 10BASE-T1L Ethernet interface
- Power delivery via the 10BASE-T1L interface or from a field supply enabling
  both low and high power applications
- Fully isolated design for safe operation
- Industry standard form factor compatible with DIN rail mounts

.. figure:: ad-swiot1l-sl_angle-web.jpg
   :width: 400 px

   :adi:`AD-SWIOT1L-SL` Development Platform

.. figure:: swiot1l_block_diagram.png
   :width: 800 px

   :adi:`AD-SWIOT1L-SL` Simplifed Block Diagram


Specifications
--------------

.. csv-table::
   :file: specifications.csv


Package Contents
----------------

The development kit is delivered with a set of accessories required to put the
system together and get it up and running in no time.

This is what you’ll find in the development kit box:

- 1 x :adi:`AD-SWIOT1L-SL` board with enclosure
- 1 x :adi:`AD-T1LUSB-EBZ` 10BASE-T1L to usb adapter board.
- 1 x Profibus (1x2x18AWG) cable for Single Pair Ethernet (SPE) connectivity
- 1 x usb 2.0 cable 
- 1 x cable connector for the external 24 V power supply
- 1 x cable connector for channels connectivity

The AD-SWIOT1L-SL comes with pre-programmed firmware enabling the system to
interface with a PC application for system configuration, control, and data
acquisition over the 10BASE-T1L interface.

.. figure:: swiot1l_kit_v1.jpg
   :width: 600 px

   :adi:`AD-SWIOT1L-SL` Package Contents


Application Development
-----------------------

The AD-SWIOT1L-SL firmware is based on ADI’s open-source no-OS framework. It
includes the bare-metal device drivers for all the components in the system, as
well as example applications enabling connectivity via the 10BASE-T1L interface
for system configuration and data transfer.

.. figure:: sw_block_diagram.png
   :width: 300 px

   :adi:`AD-SWIOT1L-SL` Software Block Diagram


Getting Started with AD-SWIOT1L-SL
----------------------------------

Depending on your specific use case for the AD-SWIOT1L-SL platform, these guickstart guides may serve as valuable resources to assist you in navigating your project:

#. :external+scopy:doc:`Interact with AD-SWIOT1L-SL using Scopy
   <plugins/swiot1l/index>`
#. :ref:`Program and debug AD-SWIOT1L-SL application code
   <ad-swiot1l-sl software-guide>`

   - A step-by-step guide to properly setup and configure your AD-SWIOT1L-SL
     system

#. :git-no-OS:`Program and debug AD-SWIOT1L-SL firmware
   <projects/swiot1l>`

   - Detailed information about programming and debugging the system


User guides
-----------

.. toctree::
   :titlesonly:

   hardware-guide/index
   firmware-guide/index
   software-guide/index
   production-testing/index
   sample_application/index


Help and Support
----------------

For questions and more information, please visit the :ez:`/`.
