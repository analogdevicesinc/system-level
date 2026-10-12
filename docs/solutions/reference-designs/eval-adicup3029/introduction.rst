.. _eval-adicup3029 introduction:

Introduction
============

The :adi:`EVAL-ADICUP3029` is an Arduino-like development platform based on the
:adi:`ADUCM3029` ultra low power microcontroller (MCU) with integrated power
management for processing, control, and connectivity. The MCU system is based on
the ARM Cortex-M3 processor, a collection of digital peripherals, embedded SRAM
and flash memory, and an analog subsystem which provides clocking, reset, and
power management capability in addition to an analog-to-digital converter (ADC)
subsystem. The :adi:`ADUCM3029` has industry leading ultra low power which makes
it ideal for Internet of Things (IoT) applications. The platform has an Arduino
Uno form factor, two PMOD connectors, and an I2C Grove style connector for easy
to connect sensors and signal conditioning add on modules. On board Bluetooth low
energy and Wi-Fi connectivity make this board IoT ready right out of the box,
complete with software and working hardware/software examples. A free programming
and debugging tool is provided by Analog Devices (called CrossCore Embedded
Studios) which is gcc/gdb based. The base platform is accompanied by a set of
Analog Devices hardware add on modules but it can also work with 3rd party
hardware.

This guide is structured as follows:

-  :ref:`Tools and Driver Details <eval-adicup3029 tools>` - Provides all the necessary steps to download/install/use the CCES tools environment, along with a quickstart guide to understanding the tools and how to use the USB mass storage drive
-  :ref:`Hardware Details <eval-adicup3029 hardware>` - Contains hardware-related information about the base board and the various hardware add on modules
-  :ref:`Software and Board Support Packages <eval-adicup3029 software>` - Contains ADuCM3029 drivers for programming the chip, along with various peripheral drivers found on the ADICUP3029 (such as BLE, Wi-Fi, etc). There are also working code examples using sensors and other hardware modules
-  :ref:`Bluetooth Smart Device Apps <eval-adicup3029 smart_app>` - Contains detailed descriptions of downloading and installing either Android or iOS based apps that work with our sensor examples
-  :ref:`Example Projects with Setup Instructions <eval-adicup3029 reference_designs>` - Contains detailed descriptions of the software reference designs available for the base board and add on hardware
-  :ref:`Help and Support <eval-adicup3029 help_and_support>` - Provides info on where to get support on any questions you might have regarding the hardware, software, and tools
-  :ref:`Compliance Testing and Results <eval-adicup3029 compliance_testing_and_results>` - Provides testing results done on the ADICUP3029 for FCC and CE certification.
