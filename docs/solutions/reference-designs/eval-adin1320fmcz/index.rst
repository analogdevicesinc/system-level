.. _eval-adin1320fmcz:

EVAL-ADIN1320FMCZ
=================

ADIN1320 PHY Evaluation Board.

.. figure:: eval-adin1320fmcz.png
   :align: right
   :width: 300

The :adi:`EVAL-ADIN1320FMCZ` evaluation board is designed to simplify the
testing and integration of the :adi:`ADIN1320`, a low power, single port
Gigabit Ethernet physical layer (PHY) optimized for industrial applications.
The platform enables comprehensive evaluation of the ADIN1320 functionality,
including its Ethernet and serializer/deserializer (SerDes) interfaces. By
supporting the ADIN1320 copper and fiber Ethernet capabilities, the platform
allows evaluation of copper Ethernet (10BASE-Te, 10BASE-T, 100BASE-TX,
1000BASE-T) as well as fiber and SerDes protocols (1000BASE-X, 100BASE-FX,
1000BASE-KX).

The evaluation board integrates two ADIN1320 PHYs, each connected to an RJ45
connector with integrated magnetics for copper connectivity. Both PHYs have
their media access control (MAC) I/O pins routed to a field programmable gate
array (FPGA) mezzanine card (FMC) connector, which allows seamless integration
with FMC-compatible FPGA or system on a chip (SoC) platforms.

Overview
--------

The following carriers are supported, followed by the target firmware:

.. list-table::

   * - Carrier
     - Linux
   * - Zedboard (Zynq-7000)
     - ✓

Features
~~~~~~~~

* Dual ADIN1320 PHY with configurable port connectivity
* Port 0 ADIN1320 supports connection to both RJ45 and SFP connectors
* Port 1 ADIN1320 supports connection to RJ45 and SMA connectors for SGMII signal access.
* FMC connector for FPGA/SoC integration.
* MII, RMII, RGMII (with optional internal RX/TX delay) host interfaces
* Selectable copper (RJ45) or fiber (1000BASE-X, 1000BASE-KX, 100BASE-FX) media
* PHY address and operating mode (line and MAC interface selection) configured via on-board hardware strapping

Evaluation board kit contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ADIN1320EBZ-U1 evaluation board
* LPC FMC to GPIO converter

Equipment needed
~~~~~~~~~~~~~~~~~

* Zedboard - Zynq-7000 development board
* Cat5+ Ethernet cable or a 1000BASE-X capable SFP module
* SD card

User Guides
-----------

.. toctree::
   :titlesonly:
   :glob:

   user-guide/*

Developers
-----------

Drivers
~~~~~~~

.. list-table::

   * - Firmware
     - Source code
     - Documentation
   * - Linux
     - :git-linux:`drivers/net/phy/adin.c`
     - :git-linux:`Documentation/devicetree/bindings/net/adi,adin.yaml`

.. note::

   The mainline ``adin`` PHY driver (``CONFIG_ADIN_PHY``), shared with the
   ADIN1200/ADIN1300 family, does not yet support the ADIN1320. Until support
   is merged upstream, use the ``adin`` driver from the ADI Linux kernel
   fork's :git-linux:`release/adin1320 <release/adin1320:/>` branch.

Help and Support
-----------------

For questions and more information, please visit:

* :ez:`EngineerZone Support Community <reference-designs>`
* :adi:`ADIN1320 Product Page <ADIN1320>`

.. esd-warning::
