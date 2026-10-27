.. _ad-ethernetapldevice-sl:

AD-ETHERNETAPLDEVICE-SL
=======================

Ethernet-APL Field Platform for Intelligent, Safe, Secure, and Connected Industrial Devices

Introduction
------------

The :adi:`AD-ETHERNETAPLDEVICE-SL` is a complete Ethernet-APL field platform designed
for prototyping intelligent, secure, and connected industrial field devices.

Key Features
~~~~~~~~~~~~~

- Certified for intrinsic safety (Ex ia IIC Ga)
- Pre-certified Ethernet-APL
- Extensive security features: built-in security for hardware root-of-trust,
  data confidentiality and integrity, and secure communications.

   - Designed with IEC 62443 and EUCRA requirements in mind.
     Support available for security certification.

- :adi:`MAX42500` voltage monitor with integrated windowing watchdog
- :adi:`MAX6613` temperature sensor
- :adi:`ADFS7124-4` sigma-delta ADC (SC3 certified)
- Complete FMEDA documentation
- :adi:`MAX32690`  dual-core MCU (ARM Cortex-M4 with FPU + RISC-V co-processor)
- External RAM (512 Mb) and Flash (64 Mb)
- 10BASE-T1L Ethernet via :adi:`ADIN1110`  MAC/PHY
- Supports APL class A, :adi:`ADIN1100D2Z` recommended
- Open-source software stack with drivers and example applications
- Zephyr RTOS support and integration with Code Fusion Studio

.. figure:: comb_top.png
   :width: 450 px
   :align: left
   :alt: AD-EthernetAPLDevice-SL Board

   AD-EthernetAPLDevice-SL Board

.. figure:: ad-ethernetapldevice-sl_hockeypuck_block_diagram.svg
   :width: 450 px
   :align: right
   :alt: Simplified Block Diagram

   AD-EthernetAPLDevice-SL Simplified Block Diagram

.. csv-table:: Specifications
   :file: specifications.csv

Hardware Design Files
~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   The hardware design files are available for download from the product page.
   The design files include schematics, PCB layouts, and bill of materials (BOM)
   for the AD-EthernetAPLDevice-SL.

   :adi:`AD-EthernetAPLDevice-SL Design Files <media/en/reference-design-documentation/design-integration-files/ad-ethernetapldevice-sl-design-files.zip>`

   - :download:`Schematic Power and Comms board <02-083152-01-b.pdf>`
   - :download:`Schematic Digital IS board <02-083153-01-e.pdf>`
   - :download:`Schematic Digital NON-IS board <02-084576-01-c.pdf>`
   - :download:`Layout Power and Comms board <08-083152-01-b.pdf>`
   - :download:`Layout Digital IS board <08-083153-01-d.pdf>`
   - :download:`Layout Digital NON-IS board <08-084576-01-b.pdf>`

Package Contents
----------------

The development kit is delivered with a set of accessories required to put the
system together and get it up and running in no time.

This is what you'll find in the development kit box:

- 1x AD-EthernetAPLDevice-SL intrinsic safety certified kit (Power and Comms +
  Digital IS boards)
- 1x Digital NON-IS board. This board is not IS certified and enables access to
  the RISC-V Jtag for debugging purposes (Digital NON-IS board)
- 1x MAX32650PICO programmer (ARM) + cable
- 1x Olimex programmer (RISC-V)
- 1x Olimex adapter + cable

Application Development
-----------------------

.. figure:: sw_block_diagram.png
   :width: 400 px

   Software Architecture

The :adi:`AD-ETHERNETAPLDEVICE-SL` firmware examples are based on ADI's
open-source no-OS framework. It includes the bare-metal device drivers for all
the components in the system as well as example applications enabling
connectivity via the 10BASE-T1L interface for system configuration and data
transfer.

Additionally, a proprietary PROFINET stack software application is available to
enable easy evaluation and system prototyping
(`MyAnalog account <https://myanalog.com>`_ required).

.. admonition:: Software Request
   :class: tip

   To request for the software package, please accomplish this form:
   https://form.analog.com/form_pages/softwaremodules/SRF.aspx

   Under Target Technology, please select ``Industrial Sensing``
   and check the box for ``Ethernet-APL Device Reference Design/Profinet - FreeRTOS Demo (TMG)``.

   .. figure:: software-request.png

Hardware Components and Connections
-----------------------------------

.. figure:: power-connectors.png
   :width: 600 px

   Power Board Connections

.. figure:: is-connector.png
   :width: 600 px

   Digital IS Board Connections

.. figure:: non-is-connectors.png
   :width: 600 px

   Digital NON-IS Board Connections

.. csv-table:: Pin Description
   :file: pin-descriptions.csv

Hardware Setup
--------------

Required Hardware
~~~~~~~~~~~~~~~~~

- **Development kit**: AD-EthernetAPLDevice-SL
- **Debugging board**: If RISC-V co-processor needs to be debugged, replace the
  IS digital board with the NON-IS Digital board
- **Power supply**: Powered via DEMO-ADIN1100D2Z supplied from external power connector
  (from 9V to 15V), or an Ethernet-APL field switch
- **ARM programmer**: MAX32625PICO or any SWD-compatible programmer
- **RISC-V programmer**: Olimex ARM-USB-OCD
- **Media converter**: 10BASE-T1L to 10BASE-T or similar. DEMO-ADIN1100D2Z
  includes a media converter and can be used for both power and data, or an
  Ethernet-APL field switch

Setup Instructions
~~~~~~~~~~~~~~~~~~

#. Connect the AD-EthernetAPLDevice-SL to the DEMO-ADIN1100D2Z and ensure that
   all connectors are fully seated.

#. Connect a 2- or 4-wire PT100 sensor to the temperature-sensor connector.

#. Connect the MAX32625PICO programmer to the ARM debug header with the
   10-pin ribbon cable.

#. To debug the RISC-V co-processor, install the NON-IS digital board and
   connect a RISC-V debug probe to its RISC-V JTAG header. This header is only
   available on the NON-IS board.

#. Connect the DEMO-ADIN1100D2Z to your PC with an Ethernet cable.

#. Power the DEMO-ADIN1100D2Z from a 9 V to 15 V supply. The
   AD-EthernetAPLDevice-SL is powered over Ethernet.

#. Open a terminal application (PuTTY is recommended) and connect to the
   virtual COM port assigned to the MAX32625PICO programmer. Set the serial
   connection to **115200** baud, 8 data bits, no parity, and 1 stop bit.

#. Press the reset button on the DEMO-ADIN1100D2Z. The terminal displays the
   board's IP address, which you can use to ping the board.

.. figure:: config.png
   :width: 600 px
   :alt: Hardware Setup

   AD-EthernetAPLDevice-SL Hardware Setup

Software Setup
--------------

Programming the AD-EthernetAPLDevice-SL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-EthernetAPLDevice-SL is supported by an open-source software stack based
on Analog Devices' no-OS framework. It includes:

- Baremetal drivers for all on-board components
- Example applications for data acquisition and system configuration via 10BASE-T1L
- Zephyr RTOS board definition
- Integration with Code Fusion Studio

For a complete experience, download latest Code Fusion Studio from :adi:`here <codefusion-studio>`.

The software stack includes:

- no-OS drivers and HAL
- Example applications for ADCs, DACs, sensors
- UART and Ethernet (10BASE-T1L) communication support
- Zephyr RTOS support

Complementary Documentation
---------------------------

  .. toctree::
     :titlesonly:
     :maxdepth: 2
     :glob:

     */index

Help and Support
----------------

For questions and more information, please visit the :ez:`/` community or
contact your local ADI representative.
