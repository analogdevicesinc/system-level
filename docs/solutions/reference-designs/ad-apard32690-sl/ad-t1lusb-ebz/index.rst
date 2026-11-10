AD-T1LUSB2.0-EBZ
================

USB2.0 to 10BASE-T1L Interface Board
""""""""""""""""""""""""""""""""""""

Overview
--------

.. figure:: ad-t1lusb2.0-ebz_angle-web.png
    :align: left
    :width: 300 px

    AD-T1LUSB2.0-EBZ Interface Board

The :adi:`AD-T1LUSB2.0-EBZ </resources/evaluation-hardware-and-software/evaluation-boards-kits/ad-t1lusb20-ebz.html>` board is an interface between USB 2.0 and a 10BASE-T1L
interface.

The current hardware configuration provides a straightforward architecture with
a USB Ethernet Controller and MAC
(`LAN9500A <HTTP://www.microchip.com/en-us/product/lan9500a>`__) connected
through MII to the :adi:`ADIN1100` PHY.

The design also includes an EEPROM for saving and recalling MAC configurations
and status LEDs to indicate link status (MAC) and user-programmable status flags
from the PHY.

The AD-T1LUSB2.0-EBZ board doesn’t require any configuration to be functional
and ready for use.

Features
--------

- Easy-to-use USB2.0 to 10BASE-T1L interface
- Efficient data communication utilizing LAN9500A USB Ethernet Controller and
  MAC connected via MII to the ADIN1100 PHY
- Onboard EEPROM for saving and recalling MAC configurations
- LEDs indicating MAC link status and user-programmable PHY status flags
- Operates without an external power supply, powered directly from the USB bus

Applications
------------

- Industrial Ethernet Application Development
- Building Automation

System Architecture
-------------------

.. figure:: ad-t1lusb2.0-ebz_block_diagram.png
    :width: 600 px

    AD-T1LUSB2.0-EBZ Simplified Block Diagram

What’s Inside the Box?
----------------------

.. figure:: ad-t1lusb2.0-ebz_package_contents.png
    :width: 600 px

    AD-T1LUSB2.0-EBZ Package Contents

Setup Examples
--------------

The AD-T1LUSB2.0-EBZ board is intended to be ready for use out of the box to
quickly control any system with a 10BASE-T1L interface.

A couple of design examples that have a 10BASE-T1L interface that will work
together with the AD-T1LUSB2.0-EBZ board are:

- :adi:`AD-SWIOT1L-SL` - Software-configurable Analog and
  Digital I/O with 10BASE-T1L Evaluation and Development Platform
- :adi:`AD-APARD32690-SL` - Arduino Form-factor Development
  Platform Based on MAX32690 ARM Cortex-M4 Microcontroller

.. note:: The **AD-T1LUSB2.0-EBZ** will **send or receive data only** over a FROFIBUS/SPE cable, so any design with a 10BASE-T1L interface will need to be powered separately.

AD-SWIOT1L-SL Interfacing
-------------------------

.. figure:: ad-swiot1l-sl_ad-t1lusb20-ebz.png

   AD-T1LUSB2.0-EBZ Setup with AD-SWIOT1L-SL

AD-APARD32690-SL Interfacing
----------------------------

.. figure:: ad-adard32690-sl_ad-t1lusb20-ebz.png

   AD-T1LUSB2.0-EBZ Setup with AD-APARD32690-SL

Network Testing
----------------

When the AD-T1LUSB2.0-EBZ board is connected to a computer via a USB cable, a new network interface should be available.

This can be verified by running on a shell terminal the **``ipconfig`` command
on a Windows system** or **``ifconfig`` on a Linux system**.

The new network configuration which corresponds to the following example:

::

   Ethernet adapter Ethernet 3:

      Connection-specific DNS Suffix  . :
      Link-local IPv6 Address . . . . . : fe80::5079:d4ec:5a1:6387%63
      Autoconfiguration IPv4 Address. . : 169.254.193.171
      Subnet Mask . . . . . . . . . . . : 255.255.0.0
      Default Gateway . . . . . . . . . :

After this we can run the ``ping`` command as ``ping -t 169.254.193.171`` to
obtain the following response if everything works properly:

::

   Pinging 169.254.193.171 with 32 bytes of data:
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128
   Reply from 169.254.193.171: bytes=32 time<1ms TTL=128

In this way, we can confirm that the connection between a computer and the
:adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` board works as expected.

Design and Integration Files
----------------------------

.. admonition:: Download

 :adi:`AD-T1LUSB2.0-EBZ Design Support Package <media/en/evaluation-documentation/evaluation-design-files/ad-t1lusb20-ebz-design-support-package.zip>`

 - Schematic
 - PCB Layout
 - Bill of Materials
 - Allegro Project

Support
-------

Analog Devices will provide **limited** online
support for anyone using the reference design with Analog Devices components via
the :ez:`EngineerZone Reference Designs <reference-designs>` forum.

.. toctree::
   :hidden:

   production_testing/index

