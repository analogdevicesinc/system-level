.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/evaluation-systems/eval-adis-fx3-developer-resources

.. _inertial-mems evaluation-systems eval-adis-fx3-developer-resources:

EVAL-ADIS-FX3 and FX3Api Developer Resources
============================================

EVAL-ADIS-FX3 Hardware Documentation
------------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/fx3/43893_50034.jpg
   :width: 600px

The EVAL-ADIS-FX3 hardware is completely open-source and MIT licensed. It
includes many improvements learned from the previous generations of evaluation
systems and is designed to be small, flexible, reliable, and low-cost. Some of
the board"s features include:

- A dedicated, onboard 3.3V, 2A linear regulator designed for high-transient
  applications
- A USB-C connector (USB 2.0 compliant only)
- An onboard, field-upgradable EEPROM with USB bootloader fallback
- A software-selectable OFF / 3.3V / 5V IMU supply output with overcurrent and
  short-circuit protection
- A JST-XH-2 external supply connector
- USB and external supply selection jumper
- Onboard status LEDs for indicating the active supply voltage, data
  transmission, and the IMU GPIO state
- An iSensor standard, 16-pin, 2mm connector for compatibility with existing
  iSensor breakout boards and adapters
- An additional 10-pin, 2mm connector for feature expansion.

::

   *

The EVAL-ADIS-FX3 firmware was also redesigned to offer developers the
flexibility to interface with as many external devices as possible. The firmware
includes support for:

- FX3 UART debugging
- Four additional GPIO pins, separate from the four IMU GPIO pins), for external
  test equipment triggering and sensing (such as with a vibration stage or
  motors)
- A separate 3.3V supply that powers the FX3 core and other, external level
  shifters, line drivers, etc.
- An extra, highly-configurable, ``bit-banged`` SPI interface that allows for
  communication with external hardware (ADCs, DACs, protocol interface ICs,
  etc.) and enables ``non-standard`` SPI configurations.
- An I2C port meant for interfacing with I2C-compatible inertial sensors
- Concurrent, multi-board data capture capability. Multiple EVAL-ADIS-FX3 boards
  can be connected to the same PC and can concurrently capture data
  independently of each other
- Very low CPU usage while capturing data, even on older Windows machines
- Windows 7, 8, and 10 compatibility
- 1.5`` x 1.75`` PCB footprint

.. warning::

   The EVAL-ADIS-FX3 does not include any onboard GPIO logic level shifters and
   is designed to only support 3.3V logic! The EVAL-ADIS-FX3 and may be
   permanently damaged if subjected to signals > 3.6V!

The open-source, MIT-licensed design files and resources are located in the
iSensor FX3 API repository on GitHub (:git-iSensor-FX3-API:`link <hardware+>`).
An EVAL-ADIS-FX3 may also be purchased
:adi:`here <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-adis-fx3.html>`.

The image below outlines the various indicators and connectors available on the
EVAL-ADIS-FX3.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/fx3_board_layout.png
   :width: 600px

The EVAL-ADIS-FX3 interface pinouts are also listed below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/fx3_board_pinout.png
   :width: 1100px

The recommended mating connectors are listed in the image shown below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evaluation-systems/fx3_mating_connectors.png
   :width: 600px

Software
--------

The FX3 software stack consists of three parts.

- `FX3 .NET API <https://github.com/analogdevicesinc/iSensor-FX3-API>`__ -
  :git-iSensor-FX3-API:`FX3 Firmware <firmware+>` -
  `FX3 Evaluation GUI <https://github.com/analogdevicesinc/iSensor-FX3-Eval>`__

The `FX3 API <https://github.com/analogdevicesinc/iSensor-FX3-API>`__ manages
all the complex USB transactions and implements all the necessary tools to begin
capturing high-speed, high-performance data in custom applications. This
.NET-compatible API, written in VB.NET and C#, includes data streaming features
tailored to reliably capturing inertial sensor data at the maximum data rate.
The API is also fully
`documented (Sandcastle) <https://analogdevicesinc.github.io/iSensor-FX3-API/>`__,
open-source, and is licensed under the MIT license. The API also includes a
:git-iSensor-FX3-API:`wrapper library <src_wrapper+>`, allowing users to use the
same API in any development environment with support for .NET (MATLAB, LabVIEW,
Python, etc.)

The :git-iSensor-FX3-API:`FX3 Firmware <firmware+>` was designed with
compatibility and flexibility in mind. The firmware attempts to follow the
Cypress program workflow and relies on FX3 system threading, execution priority,
and event flags to execute firmware subroutines and transmit sensor data. Custom
vendor commands trigger subroutines embedded in the firmware that read and write
SPI data, measure external pulses, generate clock signals, and manage board
configuration. Several SPI streaming modes are implemented, which allow
applications to communicate with nearly every device in the iSensor portfolio.
The firmware is fully
`documented (Doxygen) <https://github.com/analogdevicesinc/iSensor-FX3-API>`__
and was developed using the open-source
`development tools <https://www.cypress.com/documentation/software-and-drivers/ez-usb-fx3-software-development-kit>`__
and API offered by Cypress.

The
`FX3 Evaluation GUI <https://github.com/analogdevicesinc/iSensor-FX3-Eval>`__
provides a boilerplate for developing custom test software in a .NET
environment. The evaluation GUI also includes helpful data capture and display
forms to help test and evaluate sensor performance.
