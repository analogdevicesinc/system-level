.. _adrv9009-zu11eg carrier-board:

ADRV2CRR-FMC Carrier Board Hardware Overview
=============================================

.. image:: images/adrv2crr-fmc_desc.png

The ADRV2CRR-FMC is the carrier board to allow users evaluate the functionality
of the ADRV9009-ZU11EG RF-SOM. It contains common high speed I/O ports to give
flexibility in what connectivity option the user needs. It comes with a power
supply that powers up the full system, heatsink that the user fits to the RFSOM
heat spreader plate and necessary cables and adapters to get up and running.

Information on getting started and links to access the system software
provided is contained on the main :ref:`RF-SOM page <adrv9009-zu11eg>`.

Power Input
-----------

The ADRV2CRR-FMC has a single 12V supply input, distributed to the
internal power supplies and interface connectors. Included in the package
is a 12V, 145W power supply, which powers the complete prototyping platform
built out of :adi:`ADRV9009-ZU11EG`, :adi:`ADRV2CRR-FMC` and
:adi:`AD-FMCOMMS8-EBZ`. There are four LEDs that show the status of the
power supplies: PG_ALL, PG_SOM, PWR_FAULT1 and PWR_FAULT2. A detailed
description of these signals is available in the
:ref:`ADRV9009-ZU11EG RF-SOM Hardware Overview <adrv9009-zu11eg hardware>`
page.

ZU11EG Ultrascale+ Configuration
---------------------------------

Boot Mode Pins
~~~~~~~~~~~~~~

Slide switches (S13 - S16) select the boot source of the Xilinx ZU11EG
Ultrascale+.

-  Mode Pins [3:0] 0000 JTAG
-  Mode Pins [3:0] 0010 Quad-SPI (32b)
-  Mode Pins [3:0] 1110 SD1 (3.0)

.. image:: images/btn_boot.png
   :align: center
   :width: 200

SD Card
~~~~~~~

-  SD card selection S9 switches between carrier and SOM SD card connector

.. image:: images/adrv9009-zu11g-sd-card-select.png
   :align: center
   :width: 200

JTAG
~~~~

The JTAG connector P7 is a 2x14 pin header intended to fit the Xilinx Platform
Cable.

RF-SOM Interface Connectors
---------------------------

The interface to the ADRV9009-ZU11EG consists of two SAMTEC SEARAY™
400-pin connectors (P12 and P14). For a detailed description of the signal
interface visit the
:ref:`ADRV9009-ZU11EG RF-SOM Hardware Overview <adrv9009-zu11eg hardware>`
page.

FMC Connector
-------------

The ADRV2CRR-FMC includes a standard ANSI/VITA 57.1 FMC high-pin count connector
P1, which is partially populated. Following signals are present:

-  10 serial transceiver lanes FMC_HPC_DPx, 2x serial transceiver
   reference clock FMC_HPC_GBTCLKx
-  34 differential IO pairs FMC_HPC_LAx, 2 differential clocks
   FMC_HPC_CLK0/1_M2C
-  JTAG, I2C interfaces

FMC HA and HB differential signals are not populated with user-defined digital
IOs as specified in the FMC HPC standard. Instead, RF reference clock signals,
synchronization signal, and ADRV9009 IOs are connected to these positions to
enhance the capability of the P1 connector by providing the possibility:

-  to add extra ADRV9009 transceivers to the system, and synchronize
   these with the RF-SOM. This is accomplished with the
   :adi:`AD-FMCOMMS8-EBZ`
-  to design custom RF boards that make use of the analog and digital ADRV9009
   IOs.

.. important::

   All the previous mentioned ADRV9009 IOs, and reference clocks are connected
   to P1 through 0 Ohm jumpers (JP8-JP91). If an FMC mezzanine card is
   connected, which conflicts with these signals remove the 0 Ohm jumpers. For
   the synchronization signal SYNC_OUT2 remove R21

IO Expansion Connector
----------------------

IO expansion connector P25 is a 2.54mm pitch 2x10mm female connector that gives
access to 12 single-ended (6 differential pairs) general purpose IOs, connected
to high-performance ZU11EG PL bank 65. The expansion IOs are referenced to 1.8V.
If other levels are needed voltage level translators need to be used.

PMOD Connector
--------------

PMOD connector P10, is a 2x6 pin, low-speed host interface, referenced to 3.3V.

.. important::

   Fairchild FXLA108 bidirectional voltage level translator is used on the PMOD
   signals, to connect these to the 1.8V referenced ZU11EG PL banks. The FXLA108
   has auto direction sensing, and might not work properly with some signals,
   like bidirectional SPI data lines, or open-drain signals.

Interfaces
----------

The following table outlines levels of functionality provided in software for
the I/O interfaces on the carrier board.

.. image:: images/carrier_io.png

.. admonition:: Download
   :class: download

   The Footprint is located here:

   .. -  `Compressed 3D Model .DXF file <resources/talisecarrier.zip>`_
   .. -  `Compressed 3D Model .STP file <resources/adrv2crr_3d.zip>`_
   .. -  `Compressed 3D Model Rev C .STP file <resources/08_048950c.zip>`_

Revision Options
----------------

These are X-GRADE options.

.. admonition:: Download
   :class: download

   .. -  `Rev C.1 Schematics <resources/02-048950-01-c2_1_.pdf>`_
   .. -  `Rev C.1 BOM <resources/rev_c.1_bom.zip>`_
   .. -  `Rev C to Rev C.1 Errata <resources/revc_to_revc.1_errata.xlsx>`_
   .. -  `Letter of Volatility <resources/letter_of_volatility_adrv2crr-fmc_carrier_board.pdf>`_

.. admonition:: Download
   :class: download

   .. -  `Rev C Schematics <resources/02-048950-01-c.pdf>`_
   .. -  `Rev C BOM <resources/05-048950-01-c.zip>`_
   .. -  `Rev B/C BRD File <resources/08_048950c_BRD.zip>`_
   .. -  `Rev C Board Design Files <resources/20_048950c_archive.zip>`_

.. admonition:: Download
   :class: download

   .. -  `Rev B Schematics <resources/carrier_board_02_048950b_top.pdf>`_
   .. -  `Rev B BOM <resources/05-048950-b_BOM.zip>`_
   .. -  `Rev B/C BRD File <resources/08_048950c_BRD.zip>`_

.. admonition:: Download
   :class: download

   .. -  `Rev A Schematics <resources/carrier_board_02_048950a_top.pdf>`_

Switches/Jumpers
----------------

-  USB PHY configuration (the only supported configuration)

.. image:: images/jmp_usb.png
   :align: center
   :width: 200

-  Power good jumpers (P18, P20) (the only working configuration)

.. image:: images/jmp_pgood.png
   :align: center
   :width: 200
