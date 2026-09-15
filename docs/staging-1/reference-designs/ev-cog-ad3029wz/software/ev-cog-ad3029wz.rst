.. imported from: https://wiki.analog.com/resources/eval/user-guides/ev-cog-ad3029wz/software/ev-cog-ad3029wz

.. _ev-cog-ad3029wz software ev-cog-ad3029wz:

Analog Devices EV-COG-AD3029LZ Off-Chip Drivers and Examples
============================================================

.. note::

   **There are no seperate toolchain,On-Board Peripheral Drivers & Software for
   EV-COG-AD3029WZ, the toolchain,On-Board Peripheral Drivers & Software for
   EV-COG-AD3029LZ works with EV-COG-AD3029WZ.The user needs to change only the
   pin muxing based on the application.For help regarding pinmapping refer to
   the Hardware Details section.**

General Description/Overview
----------------------------

The EV-COG-AD3029LZ software pack provides access to all the necessary on-board
peripheral drivers for the :adi:`EV-COG-AD3029LZ` development platform. This
software layer is the secondary layer needed when writing applications using
this development platform. The **EV-COG-AD3029LZ** software pack builds on top
of what the ADuCm302x software pack provides. The **EV-COG-AD3029LZ** software
pack makes it easier to use the on-board peripherals so creating your
application layer is will be easier. Combined with the ADuCM302x and Sensors
software pack, there are many great **Internet of Things(IoT)** applications and
demos that can be replicated using the **EV-COG-AD3029LZ** development platform.

The drivers and examples in the BSP are designed to work with CrossCore Embedded
Studio 2.6.0 ® and the ADuCM302x Device Family Pack 2.0.0.

EV-COG-AD3029LZ software pack contains the following components:

- Bluetooth Companion Module
- On-Chip Driver Examples ( GPIO,RTC, SPI, Systick, TMR, UART, WDT)
- Bluetooth Profile Examples

::

   ** FindMe Target
   ** Proximity Reporter
   ** Data Exchange (Hello World)
 * Android IoTNode application software
 * Documentation

For detailed information regarding the EV-COG-AD3029LZ software pack, please see our complete EV-COG-AD3029LZ software user guide. .. note::

   #. `EV-COG-AD3029LZ BSP 3.1.0 Release Notes <http://download.analog.com/tools/EZBoards/COG_AD3029/Releases/Release_3.1.0/EV-COG-AD3029LZ_3.1.0_Release_Notes.pdf>`__
   #. `EV-COG-AD3029LZ BSP 2.0.0 Release Notes <http://download.analog.com/tools/EZBoards/COG_AD3029/Releases/Release_1.0.0/EV-COG-AD3029LZ_1.0.0_Release_Notes.pdf>`__

.. important::

   You **MUST** have this software package installed on your laptop or PC in
   order to compile, debug, and run the applications for the EV-COG-AD3029LZ
   platform.

Downloading the EV-COG-AD3029LZ Software Pack
---------------------------------------------

The software pack can be downloaded in several ways.

#. Downloaded via the tools program

- It is recommended to download the EV-COG-AD3029LZ software pack through from
  the tools program you are using. That way, all the files, directories
  structure, and project structure for the various applications is properly
  saved and accessed. For a detailed description on how to download the
  EV-COG-AD3029LZ software pack through CrossCore Embedded Studio please see our
  :dokuwiki:`CrossCore Embedded Studio Quickstart Userguide </resources/eval/user-guides/ev-cog-ad3029lz/tools/cces_guide>`.

#. Downloaded to local directory

- However if you do decide to download the EV-COG-AD3029LZ software pack to your
  PC/laptop directly, please use the link below, and make sure you save the
  software pack to the correct local directory for your applications/projects.

.. admonition:: Download

   #. `EV-COG-AD3029LZ BSP 3.1.0 (Latest) <http://download.analog.com/tools/EZBoards/COG_AD3029/Releases/AnalogDevices.EV-COG-AD3029LZ_BSP.3.1.0.pack>`__
   #. `EV-COG-AD3029LZ BSP 1.0.0 <http://download.analog.com/tools/EZBoards/COG_AD3029/Releases/AnalogDevices.EV-COG-AD3029LZ_BSP.1.0.0.pack>`__



:dokuwiki:`Back </resources/eval/user-guides/ev-cog-ad3029lz>`
