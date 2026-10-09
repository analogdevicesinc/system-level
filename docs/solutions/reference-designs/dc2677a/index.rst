.. _dc2677a:

DC2677A
===============================================================================

High Voltage, 18-Bit, 8-Channel Data Acquisition Reference Design.

.. image:: images/dc2677a_chip.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

Demonstration circuit 2677A (:adi:`DC2677A`) is a reference design for robust
industrial data acquisition applications for the :adi:`LTC2358-18`. The device
supports high voltage measurements with a large input common range and
incorporates input protection that allows up to 400V of continuous input
protection.

The design features an :adi:`ADA4522-2` dual zero-drift operational amplifier
and :adi:`LT6658` dual-output, high current reference for sensor excitation. The
digital interface uses an HSMC (high-speed mezzanine connector), compatible with
the Altera Cyclone V SoCkit and other Altera FPGA evaluation boards supporting
3.3V CMOS I/O.

.. list-table::
   :header-rows: 1

   * - Supported Devices
     - Supported Carriers
   * - :adi:`DC2677A`
     - `Cyclone V SoC Development Kit
       <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_
   * - :adi:`LTC2358-18`
     -

Features:

- 18-bit, 8-channel SAR ADC with SoftSpan programmable input ranges
- Up to 400V continuous input overvoltage protection
- Dual zero-drift amplifier (:adi:`ADA4522-2`) for low offset and low drift
- Dual-output high current reference (:adi:`LT6658`) for sensor excitation
- HSMC interface compatible with Altera Cyclone V SoCkit and other Altera FPGA
  boards supporting 3.3V CMOS I/O

Applications:

- High voltage industrial data acquisition
- Process control and monitoring
- Sensor excitation and signal conditioning
- High accuracy measurement systems

.. image:: images/dc2677a.png
   :align: center
   :width: 500

.. toctree::
   :hidden:

   user-guide
   prerequisites
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

To better understand the :adi:`LTC2358-18`, we recommend using the
:adi:`DC2677A` evaluation board.

Table of contents
-------------------------------------------------------------------------------

#. Using the DC2677A full stack reference design that we offer:

   #. :ref:`dc2677a user-guide` - what you need to know about the evaluation
      board
   #. :ref:`dc2677a prerequisites` - what you need to get started with the
      setup
   #. :ref:`dc2677a quickstart`:

      #. Using the :ref:`Cyclone V SoCkit <dc2677a quickstart c5soc>`

#. Use the board to better understand the DC2677A

   #. :external+kuiper:doc:`Configure a SD Card <hardware-configuration>`
   #. :dokuwiki:`Update the SD Card <resources/tools-software/linux-software/kuiper-linux/update>`

   #. Linux Applications

      #. :ref:`libiio`
      #. :dokuwiki:`FRU EEPROM Utility
         <resources/tools-software/linux-software/fru_dump>`

#. Design with the DC2677A

   #. Design a custom DC2677A based platform

      #. HDL software

         #. :git-hdl:`DC2677A HDL Reference Design <projects/dc2677a>`

      #. Linux software

         #. :git-linux:`DC2677A Linux driver source code <main:drivers/iio/adc/>`
         #. :git-linux:`DC2677A Linux device tree <main:arch/arm/boot/dts/>`

      #. More information

         #. :external+hdl:doc:`ADI HDL User Guide <user_guide/index>`
         #. :external+hdl:doc:`AXI_LTC235x <library/axi_ltc235x/index>`

#. :ref:`Help and Support <help-and-support>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
