.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-isomax

.. _eval-isomax-DUPLICATED:

EVAL-ISOMAX User Guide
======================

| .. note::

   We are in the process of migrating our documentation to GitHub Pages.
   | This user guide is now available at https://analogdevicesinc.github.io/documentation/solutions/reference-designs/eval-isomax/index.html

Overview
--------

The :adi:`EVAL-ISOMAX` is an integrated dual isoSPI adapter and microcontroller
board featuring the :adi:`MAX32670` high-reliability, ultra-low-power
microcontroller and the :adi:`ADBMS6822` dual isoSPI transceiver. This board
allows multiple ADBMS68xx battery monitors to be connected through daisy-chain
configuration. The EVAL-ISOMAX also features reversible isoSPI, which enables a
redundant path to the peripheral units. The PCB components and DuraClik
connectors are optimized for low electromagnetic interference (EMI)
susceptibility and emissions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-isomax/eval-isomax_angle.jpg
   :width: 500px

Features
~~~~~~~~

- Low-cost integrated monitoring for BMS with on-board MCU and dual isoSPI chip
- Demonstrates SPI to isoSPI 2-wire datalinks
- Includes two isoSPi ports for reversible isoSPI support
- Configurable powering options for LPCM support isoSPI connections through
  simple DuraClik connectors
- Stackable and allows daisy chain of up to eight (8) ADBMS6830BMSW boards
- With PC-based software for control and data analysis using Broad Market
  Browser BMS GUI

Applications
~~~~~~~~~~~~

- IOT Battery Management
- Industrial Machine Vision
- Power Tools
- Mobile Robotics Battery Management
- Industrial Equipment Battery Monitoring
- Adaptive Battery Type System Monitoring
- Portable Energy Storage Systems
- Electric 2-Wheelers (E2Ws) such as E-scooter, E-bikes
- Light Electric Vehicles (LEV)

What"s Inside the Box?
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-isomax/eval-isomax_package_contents.png
   :width: 600px

System Architecture
~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-isomax/eval-isomax_block_diagram.png
   :width: 600px

--------------

Components and Connections
--------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-isomax/primary_side.png
   :width: 800px

.. note::

   **EVAL-ISOMAX Hardware Components**

--------------

Use Cases
---------

The EVAL-ISOMAX has an on-board ultralow-power Arm-Cortex M4-based MCU that is
suitable for broad market applications such as for IoT and industrial battery
management systems. The EVAL-ISOMAX board is recommended to be used with other
ADI broad market BMS boards such as the :adi:`EVAL-ADBMS6830BMSW` battery stack
monitor and the :adi:`EVAL-ADBMS2950-BASIC` pack monitor.

Users may also opt to use other microcontrollers for other applications
requiring more stringent timing, higher memory, or faster computing speed. Other
possible microcontrollers to be paired are the :adi:`SDP-K1` and
:adi:`AD-APARD32690-SL`.

Option 1: Using the EVAL-ISOMAX as Standalone MCU with other ADI Broad Market BMS Boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-isomax/using_isomax_with_other_adi_bm_boards.png
   :width: 800px

.. note::

   **Sample Battery Monitoring Setup with the EVAL-ADBMS6830BMSW**

Option 2: Using the EVAL-ISOMAX as a Secondary Device to other MCU Boards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   See below configuration using different MCUs:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-isomax/eval-isomax_with_ad-apard32690-sl.png
   :width: 800px

.. note::

   **Sample Cell Monitoring Setup using the AD-APARD32690-SL as Main
   Microcontroller Board and EVAL-ISOMAX as isoSPI Adapter**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-isomax/adbms2950_with_isomax_and_sdp-k1.png
   :width: 700px

.. note::

   **Sample Pack Monitoring Setup using the SDP-K1 as Main Microcontroller Board
   and EVAL-ISOMAX as isoSPI Adapter**

--------------

Getting Started
---------------

.. tip::

   Please refer to the following pages for detailed instructions on how to set
   up the EVAL-ISOMAX for evaluation.

   - :dokuwiki:`EVAL-ISOMAX Hardware User Guide </resources/eval/user-guides/eval-isomax/hardware>`
   - :dokuwiki:`EVAL-ISOMAX Software User Guide </resources/eval/user-guides/eval-isomax/software>`

--------------

Resources
---------

- :adi:`ADBMS6822 Product Page <ADBMS6822>`
- :adi:`MAX32670 Product Page <MAX32670>`
- :adi:`MAX77675 Product Page <MAX77675>`
- :adi:`MAX3207E Product Page <MAX3207E>`
- :dokuwiki:`EVAL-ADBMS6830BMSW User Guide </resources/eval/user-guides/eval-adbms6830bmsw>`
- :dokuwiki:`EVAL-ADBMS2950-BASIC User Guide </resources/eval/user-guides/eval-adbms2950-basic>`

Design and Integration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/eval-isomax/eval-isomax_design_support_package.zip`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Help and Support
^^^^^^^^^^^^^^^^

For questions and more information about this product, connect with us through
the Analog Devices Engineer Zone.

.. note::

   :ez:`EngineerZone Support Community <reference-designs>`
