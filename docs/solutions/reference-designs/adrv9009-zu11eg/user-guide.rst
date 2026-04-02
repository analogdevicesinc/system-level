.. _adrv9009-zu11eg user-guide:

User guide
==========

ADRV9009-ZU11EG High-Level Specification
-----------------------------------------

- Two ADRV9009 devices, providing (in total):

   - Quad transmitters
   - Quad receivers
   - Quad input Observation Receiver for DPD
   - Max Rx BW: 200 MHz
   - Max Tunable Tx synthesis BW: 450 MHz
   - Max Observation Rx BW: 450MHz
   - Fully integrated fractional-N RF synthesizers
   - Multi-chip phase synchronization for all RF LO and baseband clocks
   - Tuning range: 75 MHz to 6000 MHz

- Zynq UltraScale+ ZU11EG:

   - Quad-core ARM® Cortex-A53 platform running up to 1.5GHz
   - L1 Cache 32KB I / D per core, L2 Cache 1MB, on-chip Memory 256KB
   - Dual-core Cortex-R5 real-time processors
   - L1 Cache 32KB I / D per core, Tightly Coupled Memory 128KB per core
   - Mali-400 MP2 graphics processing unit up to 667 MHz
   - PCIe® Gen2 x4, 2x USB3.0, SATA 3.1, DisplayPort, 4x Tri-mode Gigabit
     Ethernet
   - 2xUSB 2.0, 2x SD/SDIO, 2x UART, 2x CAN 2.0B, 2x I2C, 2x SPI, 4x 32b GPIO
   - 16nm FinFET+ programmable logic
   - 653k System Logic Cells

- On Board Memory:

   - Processing System (Dedicated for ARM Cores) : 4 GByte DDR4(x64) (with ECC)
   - Programmable Logic (Dedicated for RF Data) : Two independent banks of 2
     GByte DDR4(x32)
   - 1Gbit serial flash for image storage
   - removable SD-Card for secure file storage

- On SOM Peripherals:

   - Ethernet Phy
   - USB 2.0 Phy
   - 12V supply via FMC connectors
   - uSD Card holder

- Storage & Operating Temperature:

   - Storage temperature range supported is -40 °C to +65 °C
   - Operating temperature for prototyping with the heatsink supplied is +25 °C.
     For specific use cases thermal analysis is required to cover varying
     environmental conditions and required performance levels.

Hardware guide
--------------

Hardware Design Details
~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   For Clock Distribution Synchronization, some passive components must be
   replaced on the :ref:`ADRV2CRR-FMC Carrier Board <adrv9009-zu11eg carrier-board>`.

   **Rev C:**

      - Replace C18, C19, C236, C240 with 0 Ohm resistors
      - Replace C289, C290 with 0 Ohm resistors
      - Unload 0 Ohm resistors from location R77, R112 and insert to R110, R111

   **Rev C.1:**

      - Replace C289, C290 with 0 Ohm resistors
      - Unload 0 Ohm resistors from location R77, R112 and insert to R110, R111

Additional hardware documentation:

- :doc:`ADRV9009-ZU11EG </solutions/reference-designs/adrv9009-zu11eg/hardware>`
  (Included are further details on the RF-SOM schematics, BOM, system clocking
  tree, mechanical specs, power tree, electrical interface.)

- :doc:`ADRV2CRR-FMC </solutions/reference-designs/adrv9009-zu11eg/adrv2crr-fmc_carrier_board>`
  (Included are schematics, BOM, mechanical specs, high level system view.)

- :doc:`AD-FMCOMMS8-EBZ Quick Start Guide </solutions/reference-designs/adrv9009-zu11eg/quickstart/fmcomms8-quick-start>`
  (Included are schematics, BOM, mechanical specs, high level system view, Start
  Guide with link to the required software to get up and running.)

Application Development
-----------------------

Multiple :adi:`ADRV9009-ZU11EG`s can be synchronized together enabling a
complete solution for complex multi-stream applications ensuring end-to-end
deterministic latency. The :adi:`ADRV9009` Transceivers include integrated LO
and phase synchronization. Overall system frequency & phase synchronization is
maintained with a clock tree structure using ADI high performance low jitter
:adi:`HMC7044` devices, making it ideal for applications requiring RF phase
alignment with a large number of channels.

The :adi:`ADRV9009-ZU11EG` has extensive I/O capability. Combined with the
:adi:`ADRV2CRR-FMC` evaluation carrier board a variety of high speed I/O can be
evaluated, including USB3, USB2, PCIe 3.0 x8, QSFP+, SFP+, 1Gb Ethernet x2, and
CPRI capability. Please review the I/O functionality reference table provided
in the :ref:`ADRV2CRR-FMC <adrv9009-zu11eg carrier-board>`
homepage for more details on the functionality provided.

An additional High Pin Count FMC Daughter Board (:adi:`AD-FMCOMMS8-EBZ`) can be
plugged into the carrier board with a further two :adi:`ADRV9009` Transceivers
increasing to a total of Eight Tx and Rx channels. A design can easily be
evaluated and then integrated seamlessly into a custom carrier for further
prototyping, or a final product greatly accelerating time to market.

Platform development support includes examples of Linux Industrial I/O (IIO)
Applications, MATLAB®, Simulink®, GNU Radio, and streaming interfaces for
custom C, C++, python, and C# applications. HDL reference designs and drivers
will be provided to help users get up and running faster. Due to varying
implementation options for the various I/O interfaces different levels of
functionality will be provided for each one, further details will be available
in the applications section.

System Setup & Evaluation
-------------------------

The :adi:`ADRV9009-ZU11EG` can be booted from the onboard SD card slot or the
SD card slot on the :adi:`ADRV2CRR-FMC` carrier board. An SD card containing
a bootable image ships in the ADRV2CRR-FMC carrier kit.

Users should check that they have the appropriate Vivado license in place to be
able to use and build the reference HDL code provided for the Ultrascale+ MPSOC
in the system.

Reference Material
------------------

.. image:: ./images/sdr_book.png
   :align: right
   :width: 200

- `Software Defined Radio for Engineers <https://www.analog.com/en/education/education-library/software-defined-radio-for-engineers.html>`__
- :ref:`Additional SDR Maths Documentation <fmcomms2 common fmcomms-math>`

Functional Test
---------------

Details on functional testing for the ADRV9009-ZU11EG:

- :dokuwiki:`ADRV2CRR-FMC Production Test <resources/eval/user-guides/adrv2crr-fmc/testing>`
- :doc:`ADRV9009-ZU11EG Production Test </solutions/reference-designs/adrv9009-zu11eg/testing>`

