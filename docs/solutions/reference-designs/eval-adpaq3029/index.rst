.. _eval_adpaq3029 eval:

EVAL ADPAQ3029
=====================================================================================

.. image:: images/hw1.png
   :align: center
   :width: 400

Overview
-------------------------------------------------------------------------------

The EVAL-ADPAQ3029 is a development and evaluation module based on the
:adi:`ADuCM3029` ultra low power ARM Cortex-M3 microcontroller, designed to
work with the Moduware modular platform. The module plugs into a Moduware
gateway (the Mini-Dev board), which communicates with it over SPI and forwards
the data to a smartphone application over Bluetooth Low Energy (BLE). Sensors,
actuators and transducers can be connected to the module through its three
evaluation headers, and an on-board :adi:`ADT7410` temperature sensor is
available out of the box. The firmware is developed in CrossCore Embedded
Studio on top of the Moduware Module Development Kit (MDK), while the user
interface is built as a web-based tile that runs in the Moduware mobile app.

Features:

- :adi:`ADuCM3029` MCU: ARM Cortex-M3 up to 26 MHz, 256 KB flash with ECC,
  64 KB SRAM and a hardware cryptographic accelerator (AES-128/256, SHA-256)
- Three SPI, I2C, UART and SPORT interfaces, GPIOs, three timers with PWM and
  a 12-bit, 8-channel SAR ADC
- Three evaluation headers (P1, P2, P3), a debug connector and an on-board
  :adi:`ADT7410` temperature sensor
- Smartphone connectivity through the Moduware gateway (SPI to the gateway,
  BLE to the phone)
- Free CrossCore Embedded Studio toolchain, with IAR and Keil also supported
  over CMSIS-DAP
- Ready-to-use example projects: RGB LED, ADC, HC-SR04, SHT20, servo motor and
  UART

Applications:

- IoT sensor and actuator nodes controlled from a smartphone
- Wireless (BLE) monitoring and control
- Rapid prototyping for makers and hobbyists
- Learning embedded firmware and mobile GUI development

.. image:: images/adpaq_platform.png
   :align: center
   :width: 600

.. toctree::
   :hidden:

   first_app
   fw_dev
   fw_dev/import_prj
   hw_setup
   introduction
   resources
   resources/app_adc
   resources/app_hc_sr04
   resources/app_servo
   resources/app_sht20
   resources/app_uart
   sw_tools_setup
   tile_dev

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ez:`/`, but before that, please make sure you read our documentation
thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Getting started with the EVAL-ADPAQ3029:

   #. :ref:`Introduction <eval-adpaq3029 introduction>`
   #. :ref:`Hardware setup <eval-adpaq3029 hw_setup>`
   #. :ref:`Software tools setup <eval-adpaq3029 sw_tools_setup>`
   #. :ref:`Running your first application (RGB LED) <eval-adpaq3029 first_app>`

#. Developing your own application:

   #. :ref:`Firmware development <eval-adpaq3029 fw_dev>`, including
      :ref:`importing the projects into CCES <eval-adpaq3029 fw_dev import_prj>`
   #. :ref:`Tile (mobile app GUI) development <eval-adpaq3029 tile_dev>`
   #. :ref:`Resources and example projects <eval-adpaq3029 resources>`

#. Design with the ADuCM3029:

   - :adi:`ADuCM3029 product page <ADuCM3029>`
   - :adi:`ADT7410 product page <ADT7410>`

#. :ref:`Help and Support <help-and-support>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
