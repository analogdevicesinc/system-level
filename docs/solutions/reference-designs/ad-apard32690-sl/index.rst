.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-apard32690-sl


AD-APARD32690-SL
================

Arduino Form-factor Development Platform Based on MAX32690 ARM Cortex-M4.

Introduction
------------

The :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` is an Arduino Form-factor
Development Platform based on :adi:`MAX32690 <MAX32690>` ARM Cortex-M4
Microcontroller, targeted for prototyping intelligent, secure, and connected
industrial field devices. Some of the main features and benefits include:

- Arduino Mega-compatible form factor
- Two Pmod™-compatible connectors
- ARM Cortex-M4 Ultra Efficient Microcontroller with integrated Bluetooth 5.2 LE
- WiFi connectivity
- Long-range, single-pair 10BASE-T1L Ethernet interface
- Built-in security for root-of-trust, mutual authentication, data
  confidentiality and integrity, secure boot, and secure communications
- Open-source software stack

.. figure:: eval-max32690-ardz_angle.jpg
   :width: 450 px
   :align: left

   AD-APARD32690-SL Microcontroller Board

.. figure:: ad-apard32690-sl-fbl.png
   :width: 450 px
   :align: right

   Simplified Block Diagram

.. csv-table:: Specifications
    :file: specifications.csv

**Hardware design files:**

- :dokuwiki:`Schematics <_media/resources/eval/user-guides/02-073637-01-c.pdf>`
- :dokuwiki:`Layout <_media/resources/eval/user-guides/08_073637c.zip>`
- :dokuwiki:`Bill of Materials <_media/resources/eval/user-guides/05-073637-01-c.zip>`

Package Contents
----------------

The development kit is delivered with a set of accessories required to put the
system together and get it up and running in no time.

This is what you’ll find in the development kit box:

- 1 x AD-APARD32690-SL board
- 1 x :dokuwiki:`AD-T1LUSB2.0-EBZ <resources/eval/user-guides/ad-t1lusb-ebz>`
  10BASE-T1L to USB adapter board
- 1 x PROFIBUS (1x2x18AWG) cable for Single Pair Ethernet (SPE) connectivity
- 1 x USB 2.0 cable

Application Development
-----------------------

.. figure:: sw_block_diagram.png
    :width: 400 px

    Software Architecture

The :adi:`AD-APARD32690-SL <AD-APARD32690-SL>` firmware is based on ADI’s
open-source no-OS framework. It includes the bare-metal device drivers for all
the components in the system as well as example applications enabling
connectivity via the 10BASE-T1L interface for system configuration and data
transfer.

:git-no-OS:`AD-APARD32690-SL Firmware Source Code and User Guide <projects/apard32690>`__

Hardware Components and Connections
-----------------------------------
.. attention:: TO BE REPLACED!
.. figure:: apard32690_hw_components.png

    Hardware Components and Connections

.. csv-table::
    :file: pin-descriptions.csv

Hardware Setup
--------------

Required Hardware
~~~~~~~~~~~~~~~~~

- **Development kit**: :adi:`AD-APARD32690-SL Microcontroller Board <AD-APARD32690-SL>`
- **Power supplies**: 5V to 28V at 2A external power supply or 5V USB-C power
  supply
- **Programmer**: :adi:`MAX32625PICO` or any other similar programmer
  supporting the SWD interface

#. Connect the AD-APARD32690-SL to the :dokuwiki:`AD-T1LUSB2.0-EBZ <resources/eval/user-guides/ad-t1lusb-ebz>`
   using the single pair Ethernet
   cable.
#. Connect the AD-T1LUSB2.0-EBZ to your PC using an USB cable.
#. Connect the MAX32625PICO programmer, or any programmer supporting the SWD
   interface, to the AD-APARD32690-SL.
#. Connect the power supply to the AD-APARD32690-SL.

.. figure:: apard32690_system_setup.jpg
   :width: 600 px

   AD-APARD32690-SL Hardware Setup

Software Setup
--------------

Updating the AD-APARD32690-SL Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To update the board’s firmware, a new bootloader has to be flashed on the
MAX32625PICO.

#. Download the firmware image: `MAX32625PICO firmware <https://github.com/MaximIntegrated/max32625pico-firmware-images/raw/master/bin/max32625_max32650fthr_if_crc_swd_v1.0.6.bin>`__
#. Set the MAX32625PICO in MAINTENANCE mode:

   * Disconnect the MAX32625PICO from the PC and the AD-SWIOT1L-SL board.
   * Plug the micro USB cable only in the MAX32625PICO.
   * Keep the button on the MAX32625PICO pressed.
   * Plug the micro USB cable into the PC.
   * Once you see the MAINTENANCE drive being mounted, you may release the
     button.

     .. figure:: picture2.jpg
        :width: 300 px

        Imaging the MAX32625PICO

#. Drag and drop (to the MAINTENANCE drive) the firmware image you previously
   downloaded.
#. After a few seconds, the MAINTENANCE drive will disappear and will be
   replaced by a drive named DAPLINK. Once this is done, the process is
   complete, and the MAX32625PICO may be used to flash the firmware of the
   AD-SWIOT1L-SL board.

Programming the AD-APARD32690-SL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the MAX32625PICO to the PC using the micro USB cable.
#. Connect the MAX32625PICO to the AD-APARD32690-SL board using the 10-pin
   ribbon cable.
#. Connect the power supply to the AD-APARD32690-SL. Make sure the board is
   powered up for the next steps.
#. A DAPLINK drive should appear as mounted on your PC.
#. Drag and drop the new firmware image into the DAPLINK drive. After a few
   seconds, the drive will be remounted.
#. Check the DAPLINK directory and make sure there is no FAIL.TXT file. In case
   there is, repeat the drag and drop step. Otherwise, you may disconnect the
   MAX32625PICO from the AD-APARD32690-SL, since the firmware update is complete.

AD-APARD32690-SL Software Stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system is accompanied by an open-source software stack and associated
collateral, enabling a complete experience from evaluation and prototyping all
the way to production firmware and applications development.

The :git-no-OS:`AD-APARD32690-SL firmware <projects/apard32690>`
is based on Analog Devices’ open-source no-OS framework, which includes all the
tools required for embedded code development and debugging as well as libraries
enabling host-side connectivity for system configuration and data transfer over
the UART or the 10BASE-T1L interfaces. The firmware source code and related
documentation can be found on the Analog Devices GitHub at the link above.

User Guide
----------

.. toctree::
   :titlesonly:
   :glob:

   */index

Help and Support
----------------

For questions and more information, please visit the :ez:`/`.

