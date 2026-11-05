.. _adxl355:

ADXL355 3-Axis MEMS Accelerometer Developer Resources
#####################################################

.. attention::

   This page is in development, in a deployed pull request. Feedback welcome in
   the PR comment section.

ADXL355 Overview
================

The :adi:`ADXL355` is a low noise density, low zero-g offset drift, low power,
3-axis MEMS accelerometer with selectable measurement ranges. The ADXL355
supports the ±2g, ±4g, and ±8g ranges, and offers industry leading noise, offset
drift over temperature, and long term stability, enabling precision applications
with minimal calibration and with very low power consumption. Applications
include:

-  Inertial measurement units (IMUs)/altitude and heading reference systems (AHRS)
-  Platform stabilization systems
-  Structural health monitoring
-  Seismic imaging
-  Tilt sensing
-  Robotics
-  Condition monitoring

The ADXL355 accelerometers offer guaranteed temperature stability with null
offset coefficients of 0.15mg/°C (max). The stability minimizes resource and
expense associated with calibration and testing effort, helping to achieve
higher throughput for device OEMs. In addition, the hermetic package helps
ensure that the end product conforms to its repeatability and stability
specifications long after they leave the factory.

With output of ±2g to ±8g full scale range (FSR), selectable digital filtering
from 1 Hz to 1 kHz, and low noise density of 25µ/√Hz at less than 200µA current
consumption, ADXL355 MEMS accelerometer offers performance level comparable to
much more expensive devices with less power consumption and BOM cost.

ADI DataX Enablement
====================

`ADI DataX™ <https://developer.analog.com/solutions/adi-datax>`__ is a highly
adaptable, open technology stack that bridges the gap between signal chains and
applications across a wide range of processing platforms, operating systems, and
software ecosystems to enable physically intelligent systems.

The ADXL355 is supported in several ADI DataX frameworks as shown in :numref:`fig-adxl355_datax_map`

.. _fig-adxl355_datax_map:

.. figure:: adxl355_datax_map.png
   :width: 700px
   :height: 400px
   :align: center

   ADXL355 DataX Enablement

Open-source drivers and ready-to-run examples are provided for ADI ARM
processors running bare-metal (no-OS) or Zephyr, Raspberry Pi running Linux.
Examples include Python, C, MATLAB, and others. Code is written for portability,
and can be easily migrated to your development platform of choice, and into your
product.

Getting Started
===============

There are several combinations of evaluation and development boards and
controller platforms, with different capabilities and associated software and
device driver resources. Review the options and choose the one that best suits
your needs.

Evaluation Boards and Development Platforms
===========================================

EVAL-ADXL35x-SDP
----------------

.. image:: EVAL-ADXL355Z-SDP-KIT_ANGLE.gif
   :width: 350px

The :adi:`EVAL-ADXL35x-SDP` is an easy-to-use Customer Evaluation System that
allows the user a quick start on testing and evaluating the ADXL355 or ADXL357
accelerometer. The system consists of a main board (EVAL-SDP-CB1Z evaluation
platform), an interface board (EVAL-SDP-INTER4-Z), and a satellite board
(EVAL-ADXL355Z or EVAL-ADXL357Z breakout board).

The EVAL-SDP-CB1Z board, also called “SDP-B”, connects directly to a PC via an
USB cable, with the USB connection providing both communications and power to
the board. The SDP-B is connected to the interface board (EVAL-SDP-INTER4-Z),
which provides the signal conditioning and electrical connections to
communicated with the satellite board (EVAL-ADXL355Z or EVAL-ADXL357Z) through a
cable. This cable allows the satellite to be easily manipulated for testing or
separately placed into an environmental chamber for temperature or humidity
testing. Separating the boards mitigates corruption of data due to the
temperature and humidity effects of other components.

.. Note::
   This system is intended for performance evaluation only. Source code for the SDP-B firmware and GUI software is not available.
   
For complete instructions refer to the `EVAL-ADXL35x-SDP User Guide <https://wiki.analog.com/resources/eval/user-guides/inertial-mems/accelerometers/adxl35x/eval-adxl35x-sdp>`__

EVAL-ADXL35X
------------

.. image:: EVAL-ADXL354BZANGLE-web.gif
   :width: 350px

The :adi:`EVAL-ADXL35X-Z` are simple evaluation boards that allow quick
evaluation of the performance of Analog Devices new series of low power, low
noise, low drift 3-axis, MEMS accelerometers. The series consists of both analog
and digital output devices, supporting a variety of Full Scale Ranges (FSR). The
model descriptions are shown in the ordering guide below. These evaluation
boards are ideal for evaluation of the ADXL35x accelerometer series in an
existing system because the stiffness and the small size of the evaluation board
minimize the effect of the board on both the system and acceleration
measurements.

.. Note::
   This board does not directly interface to any standard platforms, and requires a separate cable. This may be desirable for interfacing to an arbitrary platform board, or when the sensor needs to be separated from the platform board by a cable.

For complete instructions refer to the `EVAL-ADXL35X-Z User Guide <https://wiki.analog.com/resources/eval/user-guides/inertial-mems/accelerometers/adxl354_355>`__

EVAL-ADXL355-PMDZ
-----------------

.. image:: EVAL-ADXL335-PMDZANGLE-web.png
   :width: 350px

The :adi:`EVAL-ADXL355-PMDZ` is a compact, low-cost, Pmod-compatible evaluation
board for the ADXL355. It targets several standard microcontroller development
boards that either have a native Pmod interface, or via an adapter. It also
targets the Raspberry Pi via the :adi:`PMD-RPI-INTZ` adapter board. The Pmod
board is small in size with dimensions approximately 2.5 cm in width by 2.5 cm
in length.

SPI PMOD peripheral connectors can also be found on many 3rd party MCU or FPGA
development boards, where the EVAL-ADXL355-PMDZ can be connected directly into
those systems, and you can develop your own code using our reference code below.

Developing with the ADXL355
===========================

The EVAL-ADXL335-PMDZ will be used for the various example systems described
below. These examples are designed to be used as-is for initial development,
then ported to your target hardware.

.. image:: adxl355_pmdz.png
   :width: 350px

Pmod  Processor Connector
-------------------------

The PMOD interface is a series of standardized digital interfaces for various
digital communication protocols such as SPI, I2C, and UART. These interface
types were standardized by Digilent, which is now a division of National
Instruments. Complete details on the Pmod specification can be found on the
`Digilent Pmod landing page <https://digilent.com/reference/pmod/start>`__.

The specific interface used for the EVAL-ADXL355-PMDZ boards is the extended
SPI. In general ADI has adopted the extended SPI connector for all PMOD devices
which have an SPI interface. It provides flexibility to add interrupts, general
purpose I/O, resets, and other digitally controlled functions.

+---------------+---------------------+----------+---------------+----------------+----------+
| P1 Pin Number | Pin Function        | Mnemonic | P1 Pin Number | Pin Function   | Mnemonic |
+===============+=====================+==========+===============+================+==========+
| Pin 1         | Chip Select         | CS       | Pin 7         | Interrupt 1    | INT1     |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 2         | Master Out Slave In | MOSI     | Pin 8         | Not Connected  | NC       |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 3         | Master In Slave Out | MISO     | Pin 9         | Interrupt 2    | INT2     |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 4         | Serial Clock        | SCLK     | Pin 10        | Data Ready     | DRDY     |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 5         | Digital Ground      | DGND     | Pin 11        | Digital Ground | DGND     |
+---------------+---------------------+----------+---------------+----------------+----------+
| Pin 6         | Digital Power       | VDD      | Pin 12        | Digital Power  | VDD      |
+---------------+---------------------+----------+---------------+----------------+----------+

.. image:: adxl355_layout.png
   :width: 300px

ADXL355 Interrupt Pins
----------------------

The EVAL-ADXL355-PMDZ has two interrupt pins and a data ready pin which can be
used as external indicators for the user. The interrupt pins can be programmed
through software to reflect various status flags within the ADXL355, and those
pins are accessible through the SPI PMOD header. For complete details on the
individual status flags, what they mean, and how to program the chip to reflect
those interrupts, please consult the :adi:`ADXL355` data sheet.

Power Supply Considerations and Configuration
---------------------------------------------

When using the ADXL355 PMOD board, the 3.3V power for the PMOD comes directly
from the host board it is connected to. Most Pmod platform boards can supply at
least 100 mA, more than adquate for the EVAL-ADXL355-PMDZ.

Device Driver and Software Support
==================================

There are two device driver and accompanying software solutions provided for
the EVAL-ADXL355-PMDZ:

**ADXL355 no-OS Driver**

   * The :git-no-OS:`ADXL355 no-OS driver <main:drivers/accel/adxl355>` is used
     in bare-metal applications, typically running on low-power, embedded
     microcontrollers.

   * The :git-no-OS:`ADXL355 no-OS example project <main:projects/eval-adxl355-pmdz>`
     uses the ADXL355 no-OS driver and has several configuration options:

      * The tinyiiod configuration emulates the Linux IIO framework through the
        tinyiiod daemon library. The application communicates with the host
        computer via the serial backend, over a USB-UART physical connection.
        This facilitates rapid application development on a host computer,
        independent from embedded code development. This is the configuration
        that will be referenced in the no-OS platform setups below.
      * The "dummy" configuration implements a simple command-line program that
        can be run on a terminal.

.. ADMONITION:: Download

   A zip file containing prebuilt programming files for the no-OS example project,
   targeting platforms below are available at:
   :git-no-OS:`eval-adxl355-pmdz.zip <releases/download/last_commit/eval-adxl355-pmdz.zip+>`.

   More details are provided in the platform-specific sections below.

**ADXL355 Linux Driver**

* The :dokuwiki:`ADXL355 Linux driver <resources/tools-software/linux-drivers/iio-accelerometer/adxl355>` is used in
  applications running the Linux operating system, typically on larger processors
  and SoC devices.
* The ADXL355 Linux driver uses the Industrial Input/Output (IIO) framework,
  greatly simplifying the development of application code via the cross-platform
  Libiio library, which is written in C and includes bindings for Python,
  MATLAB, C#, and other languages. Application code can run directly on the
  platform board, communicating with the device over the local backend, or from
  a remote host over the network or USB backends.


System Setup Using ADICUP3029
=============================

The EVAL-ADXL355-PMDZ can be used with :adi:`ADICUP3029 <eval-adicup3029>`.

Demo Requirements
-----------------

The following is the list of items needed in order to replicate this demo.

-  Hardware

   -  :adi:`EVAL-ADICUP3029`
   -  :adi:`EVAL-ADXL355-PMDZ`
   -  Micro-USB to USB Cable
   -  PC or Laptop with USB Port

-  Software

   - For IIO / libiio: eval-adxl355-pmdz_aducm3029_iio_example.hex from the
     programming file zip
   - For terminal CLI: eval-adxl355-pmdz_aducm3029_dummy_example.hex from the
      programming file zip

.. TIP::

   There are two basic ways to program the ADICUP3029 with the software for the
   ADXL355.

   #. Dragging and Dropping the .Hex to the Daplink drive

   #. Using the drag and drop method, the software is going to be a version
      that Analog Devices creates for testing and evaluation purposes.
      This is the **EASIEST** way to get started with the reference design.


Setting up the Hardware
-----------------------

#. Connect **EVAL-ADXL355-PMDZ** board at connector **P9** of the
   **EVAL-ADICUP3029**.

#. Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029 and
   connect it to a computer. The final setup should look similar to the picture
   below.

   .. figure:: adxl355_adicup3029_connections.jpg
      :width: 900px

      Hardware Setup

#. Make sure the following switches are as shown from the table below.

   .. figure:: switch_config.png
      :width: 900px

      Switch Confuguration

#. From your PC, open My Computer and look for the DAPLINK drive, if you see
   this then the drivers are complete and correct.

   .. figure:: daplink.jpg
      :width: 300px

      DAPLINK Drive

#. Drag and drop the eval-adxl355-pmdz_aducm3029_iio_example.hex file to the
   DAPLINK drive and your ADICUP3029 board will be programmed. The DS2 (red) LED
   will blink rapidly.

#. The DS2 will stop blinking and will stay ON once the programming is done.

#. For demo purposes, place the board horizontally such that the Z-axis reading
   will be approximately 9.8 m/s^2.


System Setup Using MAX32655FTHR or MAX32650FTHR
===============================================

The **EVAL-ADXL355-PMDZ** can be used with the MAX32655FTHR or
MAX32650FTHR.



Demo Requirements
-----------------

The following is the list of items needed in order to replicate this demo.

- **Hardware**

  - :adi:`MAX32655FTHR <MAX32655FTHR>` or :adi:`MAX32650FTHR <MAX32650FTHR>`
    with :adi:`MAX32625PICO <MAX32625PICO>`
  - :adi:`FTHR-PMD-INTZ <FTHR-PMD-INTZ>`
  - :adi:`EVAL-ADXL355-PMDZ <EVAL-ADXL355-PMDZ>`
  - Micro-USB to USB Cable
  - 10-pin ribbon cable
  - PC or Laptop with USB Port

- **Software**

  - For MAX32655FTHR, programming file from zip:

    - For IIO / libiio: eval-adxl355-pmdz_maxim_iio_example_max32655_adxl355.hex
    - For terminal CLI: eval-adxl355-pmdz_maxim_dummy_example_max32655_adxl355.hex

  - For MAX32650FTHR,

    - For IIO / libiio: eval-adxl355-pmdz_maxim_iio_example_max32650_adxl355.hex
    - For terminal CLI: eval-adxl355-pmdz_maxim_dummy_example_max32650_adxl355.hex

MAX32655FTHR
------------

1. Connect **MAX32655FTHR** with the **FTHR-PMOD-INTZ**. Note that MAXIM
feather board should have stacking headers for feather board where the
interposer board will be connected.

2. Connect **EVAL-ADXL355-PMDZ** to the **FTHR-PMOD-INTZ**.

3. Power up the **MAX32655FTHR** by connecting it to your laptop using micro-USB

4. Open the file explorer. Drag-and-drop the pre-built hex file to the DAPLINK.
If the transfer was not completed, update the firmware for the DAPLINK. Follow
the steps here: https://github.com/MaximIntegrated/max32625pico-firmware-images/

5. Open PuTTY or other similar software. Check the Device Manager to set
correct COM for the MAX32655FTHR. Set baud rate according to hex file used:

+------------------------------------------------------------------+-----------+
| Hex file                                                         | Baud rate |
+==================================================================+===========+
| eval-adxl355-pmdz_maxim_dummy_example_max32655_adxl355           | 57600     |
+------------------------------------------------------------------+-----------+
| eval-adxl355-pmdz_maxim_iio_example_max32655_adxl355             | 115200    |
+------------------------------------------------------------------+-----------+
| eval-adxl355-pmdz_maxim_iio_trigger_example_max32655_adxl355.hex | 115200    |
+------------------------------------------------------------------+-----------+

The final setup should look similar to the picture below.

.. image:: adxl355_max32655fthr_connections.jpg
   :width: 450px

MAX32650FTHR
------------

#. Using a 10-pin ribbon cable, connect the **MAX32625PICO** to the
   **MAX32650FTHR**.

   .. image:: max32650fthr_with_pico.png
      :width: 400px

#. Connect **MAX32650FTHR** to the **FTHR-PMOD-INTZ**.

#. Connect **EVAL-ADXL355-PMDZ** to the **FTHR-PMOD-INTZ**.

   ===================== ==================
   MAX31855PMB1          FTHR-PMOD-INTZ SPI
   ===================== ==================
   Pin 1 (Chip Enable)   CS
   Pin 2 (Not connected) MOSI
   Pin 3 (MISO)          MISO
   Pin 4 (SCK)           SCK
   Pin 5 (GND)           GND
   Pin 6 (VCC)           VCC
   ===================== ==================

   The final setup should look similar as shown below.

   .. image:: max32650fthr_adxl355pmod.jpg
      :width: 450px

#. Power up the **MAX32650FTHR** by connecting it to your laptop using
   micro-USB. Connect **MAX32625PICO** to your laptop as well.

#. Open the file explorer. Drag-and-drop the pre-built hex file to the DAPLINK.
   If the transfer was not completed, update the firmware for the DAPLINK. Follow
   the steps here: https://github.com/MaximIntegrated/max32625pico-firmware-images/

#. Open PuTTY or other similar software. Check the Device Manager to set the
   correct COM port for the **MAX32650FTHR**.

#. Set baud rate according to the hex file used available in
   :git-no-OS:`MAX32650FTHR_demo_ADXL355.hex <releases/download/last_commit/eval-adxl355-pmdz.zip+>`:

====================================================== =========
Hex file                                               Baud rate
====================================================== =========
eval-adxl355-pmdz_maxim_dummy_example_max32650_adxl355 57600
eval-adxl355-pmdz_maxim_iio_example_max32650_adxl355   115200
====================================================== =========

The expected output viewed in the PuTTY is shown below.

.. image:: basic_putty_adxl355.png
   :width: 600px

System Setup Using Raspberry Pi
===============================

The EVAL-ADXL355-PMDZ can be used with a Raspberry Pi.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  **Hardware**

   -  :adi:`EVAL-ADXL355-PMDZ <ADXL355>`
   -  :adi:`PMOD to Raspberry Pi Adapter (PMD-RPI-INTZ) <PMD-RPI-INTZ>`
   -  Raspberry PI Zero, Zero W, 3B+, or 4
   -  16GB (or larger) Class 10 (or faster) micro-SD card
   -  5Vdc, 2.5A power supply with micro USB connector (USB-C power supply for Raspberry Pi 4)
   -  User interface setup (choose one):

      -  HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi
      -  Host Windows/Linux/Mac computer on the same network as Raspberry Pi

-  **Software**

   - :dokuwiki:`Kuiper Linux Image <resources/tools-software/linux-software/adi-kuiper_images/release_notes>`


Loading Image on SD Card
------------------------

In order to boot the Raspberry Pi and control the **EVAL-ADXL355-PMDZ**, you
will need to install ADI Kuiper Linux on an SD card. Complete instructions,
including where to download the SD card image, how to write it to the SD card,
and how to configure the system are provided on the :ref:`kuiper`.

Configuring the SD Card
-----------------------

Follow the configuration procedure under **Configuring the SD Card for
Raspberry Pi Projects** at :ref:`kuiper`, substituting the
following lines in **config.txt**:

::

   dtoverlay=rpi-adxl355

Setting up the Hardware
-----------------------

To set up the circuit for evaluation, consider the following steps:

#. Connect the **P9** of the **PMOD to Raspberry Pi Interposer** board at the
   male header GPIO pin connector of the **Raspberry Pi** as shown below.

   .. image:: interposer.png
      :width: 500px

#. Connect the :adi:`EVAL-ADXL355-PMDZ <EVAL-ADXL355-PMDZ>` on the
   PMOD to Raspberry Pi Interposer board either via Port P1 or P2.

   .. |image3| image:: adxl355_rpi_connections.jpg
      :width: 600px

#. Burn the SD card with the proper ADI Kuiper Linux image. Insert the burned
   SD card on the designated slot on the RPi.
#. Connect the system to a monitor using an HDMI cable through the mini HDMI
   connector on the RPi.
#. Connect a USB keyboard and mouse to the RPi through the USB ports.
#. Power on the RPi board by plugging in a 5V power supply with a micro-USB
   connector. The final setup should look similar to the picture below.

   .. image:: eval-adxl355-pmdz_overall_setup.png
      :width: 600px

System Setup Using EVAL-ADICUP360 **(DEPRECATED)**
==================================================

The original software example for the ADXL355 was developed on the ADICUP360
platform, and is a simple, terminal-based command line interface. This type of
example program is being deprecated in favor of tinyiiod-based servers for
embedded platforms, however this example is still available for reference here:
:dokuwiki:`ADXL355 Accelerometer PMOD Demo on ADICUP360<resources/eval/user-guides/eval-adicup360/reference_designs/demo_adxl355>`.

.. IMPORTANT::

   In order to use the **EVAL-ADXL355-PMDZ** with the **ADICUP360**, the user
   **MUST** remove resistor R1. The ADXL355 holds the DATA_RDY pin low during
   powerup, and that holds the EVAL-ADICUP360 in UART boot mode. When this mode is
   active the MCU will stay in standby mode till it receives the proper command,
   effectively making the ADuCM360 not run. So to avoid this, please remove R1 and
   note that you can't use the DATA_RDY pin with the ADICUP360.

.. NOTE::

   Note that the libiio, iio oscilloscope, and pyadi-iio sections below do NOT
   apply to this example.

Application Software (All Platforms)
====================================

The Libiio is a library used for interfacing with IIO devices and is required
to be installed on your computer.

.. ADMONITION:: Download

   Download and install the latest :git-libiio:`Libiio package <releases+>` on
   your machine.


To be able to connect your device, the software must be able to create a
context. The context creation in the software depends on the backend used to
connect to the device as well as the platform where the EVAL-ADXL355-PMDZ is
attached. Two platforms are currently supported for the EVAL-ADXL355-PMDZ:
Raspberry Pi using the ADI Kuiper Linux and the ADICUP3029 running the no-OS
ADXL355 demo project. The user needs to supply a **URI** which will be used in
the context creation.

The :ref:`libiio iio_info` command is a part of the libIIO package that reports
all IIO attributes.

Upon installation, simply enter the command on the terminal command line to
access it.

For RPI Direct Local Access:
----------------------------

.. shell::

   $iio_info

For Windows machine connected to Raspberry Pi:
----------------------------------------------

.. shell::

   $iio_info -u ip:<ip address of your ip>

For example, if your Raspberry Pi has the IP address 192.168.1.7, then enter:

.. shell::

   $iio_info -u ip:192.168.1.7



.. NOTE::

   Do note that the Windows machine and the RPI board should be connected to
   the same network in order for the machine to detect the device.

For Windows machine connected to ADICUP3029:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shell::

   $iio_info -u serial:<serial port>

Examples:

* In a Windows machine, you can check the port of your ADICUP3029 via Device
  Manager in the Ports (COM & LPT) section. If your device is in COM4, enter:

.. shell::

   $iio_info -u serial:COM4

On a Unix-based machine, you will see it under the /dev/ directory in this
format "ttyUSBn", where n is a number depending on how many serial USB devices
attached. If you see that your device is ttyUSB0, enter:

.. shell::

   $iio_info -u serial:/dev/ttyUSB0

IIO Commands
~~~~~~~~~~~~

There are different commands that can be used to manage and control the device
being used. The :ref:`libiio iio_attr` command reads and writes IIO attributes.

.. shell::

   $iio_attr [OPTION]...

To look at the context attributes, enter the following command on the terminal:

.. shell::

   $iio_attr -a -C

The :ref:`libiio iio_reg` command reads or writes SPI or I2C registers in an
IIO device. This is generally not needed for end applications, but can be
useful in debugging drivers. Note that you need to specify a context using the
*-u* qualifier when you are not directly accessing the device via RPI or when
you are using the ADICUP3029 platform.

.. shell::

   $iio_reg -u <context> <device> <register> [<value>]

To read the device ID (register = 0x02) of an ADXL355 interfaced via RPI from a
Windows machine, enter the following code on the terminal:

.. shell::

   $iio_reg -u ip:<ip address> adxl355 0x02


IIO Oscilloscope
~~~~~~~~~~~~~~~~

Download and install the latest version of IIO Oscilloscope from:
:git-iio-oscilloscope:`IIO Oscilloscope Installers <releases+>`.

Once done with the installation or an update of the latest IIO Oscilloscope,
open the application. The user needs to supply a URI which will be used in the
context creation of the IIO Oscilloscope and the instructions can be seen from
the previous section.
Press refresh to display available IIO Devices, once ADXL355 appeared, press
connect.

.. image:: adxl355_iio_osc.png
   :width: 300px

Debug Panel
^^^^^^^^^^^

Below is the Debug panel of ADXL355 wherein you can directly access the
attributes of the device.

.. image:: adxl355_iio_debug.png
   :width: 400px

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the x, y and z axis
acceleration readings and the device temperature.

.. image:: adxl355_iio_dmm_panel.png
   :width: 400px

PyADI-IIO
~~~~~~~~~

:ref:`pyadi-iio` is a python abstraction module for ADI hardware with IIO
drivers to make them easier to use. This module provides device-specific APIs
built on top of the current libIIO python bindings. These interfaces try to
match the driver naming as much as possible without the need to understand the
complexities of libIIO and IIO.

Follow the step-by-step procedure on how to install, configure, and set up
PYADI-IIO and install the necessary packages/modules needed by referring to
this :ref:`link <pyadi-iio>`.

Running the example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PYADI-IIO in your machine, you are now ready
to run python script examples. In our case, run the **adxl355_example.py**
found in the examples folder.

.. NOTE::

   Github link for the python sample script: :git-pyadi-iio:`ADXL355 Python
   Example <examples/adxl355_example.py>`

Running directly on the RPi
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. shell:: ps1

   /d/pyadi-iio/examples
   $python adxl355_example.py

Press enter and you will get these readings.

.. image:: adxl355_python_example_rpi.png
   :width: 600px

For No-OS
^^^^^^^^^

.. shell:: ps1

   /d/pyadi-iio/examples
   $python adxl355_no_os_example.py serial:<serial port>,57600

In a Windows machine, you can check the port of your MAX32655FTHR and
MAX32650FTHR via Device Manager in the Ports (COM & LPT) section. If your
device is in COM8, you have to use:

.. shell::

   $python pyadi-iio/examples/adxl355_no_os_example.py serial:COM8,57600

Press enter and you will get these readings.

.. image:: no_os_adxl355_pyadi.png
   :width: 600px


More information and useful links
---------------------------------

-  :adi:`EVAL-ADXL355-PMDZ Product Page <EVAL-ADXL355-PMDZ>`
-  :adi:`ADXL355 Product Page <ADXL355>`
-  :git-no-OS:`EVAL-ADXL355-PMDZ no-OS projects <eval-adxl355-pmdz>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. ADMONITION:: Download

   :adi:`EVAL-ADXL355-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-adxl355-pmdz-designsupport.zip>`

   * Schematics
   * Bill of Materials
   * Gerber Files
   * Assembly Files
   * Allegro Layout File


Additional Information
----------------------

-  :ref:`pyadi-iio`
-  :ref:`iio-oscilloscope`
-  :ref:`kuiper`

Hardware Registration
---------------------

.. tip::

   Receive software update notifications, documentation updates, view the
   latest videos, and more when you register your hardware.
   `Register <https://my.analog.com/en/app/registration/hardware/EVAL-ADXL355-PMDZ?&v=Rev%20B>`__
   to receive all these great benefits and more!
