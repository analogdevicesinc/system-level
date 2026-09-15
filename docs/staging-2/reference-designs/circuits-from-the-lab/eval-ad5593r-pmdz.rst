.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/eval-ad5593r-pmdz

.. _circuits-from-the-lab eval-ad5593r-pmdz:

EVAL-AD5593R-PMDZ Overview
==========================

EVAL-AD5593R-PMDZ is a minimalist 8-channel, 12-Bit, Configurable ADC/DAC/GPIO
with on-chip Reference, I2C interface PMOD module. This board serves as a
low-cost alternative to the full-featured product evaluation boards, with
terminal block connections and no extra signal conditioning.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/eval-ad5593r-pmdz-top-web.png
   :width: 400px

This user guide will focus on the hardware aspect of the
:adi:`EVAL-AD5593R-PMDZ` including the connectors, indicators, and different
configurations a user would require in order to use the hardware. There is also
a link to the design files as well as software reference designs that use the
hardware with example embedded firmware for a real demo.

Simplified functional block diagram
-----------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/eval_ad5593r-pmod/ad5593r_block_diagram.png
   :width: 500px

Connectors and Configuration
----------------------------

The following section reviews all the hardware connectors and how to interface
with them. It also reviews configuration options and well as important onboard
indicators.

Analog/Digital I/O Connector (P2 & P3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Connector
     - Pin No.
     - Pin Name
     - Pin Description
   * - P2
     - 1
     - CH3
     - Channel 3 Input/Output
   * -
     - 2
     - CH2
     - Channel 2 Input/Output
   * -
     - 3
     - CH1
     - Channel 1 Input/Output
   * -
     - 4
     - CH0
     - Channel 0 Input/Output
   * -
     - 5
     - GND
     - Ground
   * -
     - 6
     - VDD
     - Power Supply
   * - P3
     - 1
     - VREF
     - Voltage Reference
   * -
     - 2
     - GND
     - Ground
   * -
     - 3
     - CH7
     - Channel 7 Input/Output
   * -
     - 4
     - CH6
     - Channel 6 Input/Output
   * -
     - 5
     - CH5
     - Channel 5 Input/Output
   * -
     - 6
     - CH4
     - Channel 4 Input/Output

I2C PMOD Connector (P1)
~~~~~~~~~~~~~~~~~~~~~~~

The EVAL-AD5593R-PMDZ digital IMOD connector is described in the table below.

.. list-table::
   :header-rows: 1

   * - Pin No.
     - Pin Name
     - Pin Description
   * - 1
     - NC
     - Not Connected
   * - 2
     - RST
     - Reset Pin
   * - 3
     - SCL
     - I2C Serial Clock
   * - 4
     - SDA
     - I2C Serial Data
   * - 5
     - DGND
     - Digital Ground
   * - 6
     - VDD
     - Power Supply

Test Points
~~~~~~~~~~~

Users can also check the I2C signal quality and voltage supply of the board
using test points labeled RST, SCL, SDA, and VLOGIC.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/5593-1.png
   :width: 400px

Voltage Reference Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default connection of the AD5593R **Vref** pin is shorted at pin 1 of the
JP1 solder jumper where you can easily configure your voltage reference input at
pin 1 of terminal block P3, either from an external source or internal 2.5V

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/5593-2.png
   :width: 250px

LED Indicator
~~~~~~~~~~~~~

The DS1 is the power green LED indicator of the board.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/5593-3.png
   :width: 300px

Power Supply Considerations and Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using the AD5593R PMOD board, the 3.3V power for the PMOD comes directly
from the host board it is connected to. The power from the host is generally
capable of providing up to 100 mA at 3.3V, but for complete PMOD power
specifications please click\
`here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`__.

Device Driver Support
---------------------

There are two device driver solutions that are provided for controlling the
**EVAL-AD5593R-PMDZ**:

#. **AD5593R no-OS Driver**

- The
  :dokuwiki:`AD5593R no-OS driver </resources/tools-software/uc-drivers/ad5592r>`
  is used in bare-metal applications, typically running on low-power, embedded
  microcontrollers.

#. **AD5593R Linux Driver**

- The
  :dokuwiki:`AD5593R Linux driver </resources/tools-software/linux-drivers/iio-dac/ad5593r>`
  is used in applications running the Linux operating system, typically on
  larger processors and SoC devices.
- The AD5593R Linux driver uses the Industrial Input/Output (IIO) framework,
  greatly simplifying the development of application code via the cross-platform
  Libiio library, which is written in C and includes bindings for Python,
  MATLAB, C#, and other languages. Application code can run directly on the
  platform board, communicating with the device over the local backend, or from
  a remote host over the network or USB backends.

System Setup Using ADICUP3029
-----------------------------

The **EVAL-AD5593R-PMDZ** can be used with
:dokuwiki:`ADICUP3029 </resources/eval/user-guides/eval-adicup3029>`.

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is the list of items needed in order to replicate this demo.

-  Hardware

  - :adi:`EVAL-ADICUP3029`
  - :adi:`EVAL-AD5593R-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5593r-pmdz.html>`
  - Micro-USB to USB Cable
  - PC or Laptop with USB Port

-  Software

  - PuTTY or other similar software
  - :git-EVAL-ADICUP3029:`ADuCM3029_demo_AD5593R.hex <releases/download/Latest/ADuCM3029_demo_ad5592r_ad5593r.hex+>`

.. note::

   There are two basic ways to program the ADICUP3029 with the software for the
   AD5593R.

   #. Dragging and Dropping the Hex to the Daplink drive

      #. Using the drag and drop method, the software is going to be a version
         that Analog Devices creates for testing and evaluation purposes. This
         is the **EASIEST** way to get started with the reference design.

   #. Building, Compiling, and Debugging using CCES

      #. Importing the project into
         :adi:`CrossCore Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>`
         is going to allow you to change parameters and customize the software
         to your application, but will a bit more advanced and will require you
         to download the CrossCore toolchain.

.. admonition:: Download

   The software for the **ADICUP3029_AD5593R** demo can be found here:

   Prebuilt AD5593R Hex File

   - :git-EVAL-ADICUP3029:`ADuCM3029_demo_AD5593R.hex <releases/download/Latest/ADuCM3029_demo_ad5592r_ad5593r.hex+>`

   Complete AD5593R Source Files

   - :git-EVAL-ADICUP3029:`ADuCM3029_demo_AD5593R Source Code <tree/master/projects/ADuCM3029_demo_ad5592r_ad5593r+>`

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

1. Connect **EVAL-AD5593R-PMDZ** board at connector **P9** of the
   **EVAL-ADICUP3029**.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/img_3001.jpg
   :width: 400px

2. Connect a micro-USB cable to the P9 connector of the EVAL-ADICUP3029 and
   connect it to a computer. The final setup should look similar to the picture
   below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/img_2998.jpg
   :width: 400px

3. Make sure the following switches are as shown in the table below. .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/switch_config.png
   :width: 900px

  .. note::

     4. From your PC, open My Computer and look for the DAPLINK drive, if you see this then the drivers are complete and correct.

     .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/daplink.jpg
        :width: 300px

     3. Simply extract the provided zip file. Once extracted, you will see the pre-built hex file for the AD5593R demo. Then drag and drop this Hex file to the DAPLINK drive and your ADICUP3029 board will be programmed. The DS2 (red) LED will blink rapidly.

     4. The DS2 will stop blinking and will stay ON once the programming is done.

     5. Open PuTTY or other similar software. Check the Device Manager to set the correct COM port for the ADICUP3029. Set the baud rate to 115200.

     .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/ad5593_putty.png
        :width: 300px

     6. The expected output viewed in the PuTTY is shown below.

     .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/ad5593_example_adicup.png
        :width: 600px

System Setup Using Raspberry Pi
--------------------------------

The **EVAL-AD5593R-PMDZ** can be used with a Raspberry Pi.

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is a list of items needed in order to replicate this demo.

- Hardware

  - :adi:`EVAL-AD5593R-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5593r-pmdz.html>`
  - :adi:`PMOD to Raspberry Pi Adapter (PMD-RPI-INTZ) <PMD-RPI-INTZ>`
  - Raspberry PI Zero, Zero W, 3B+, or 4
  - 16GB (or larger) Class 10 (or faster) micro-SD card
  - 5Vdc, 2.5A power supply with micro USB connector (USB-C power supply for Raspberry Pi 4)
  - User interface setup (choose one):

    - HDMI monitor, keyboard, and mouse plugged directly into Raspberry Pi
    - Host Windows/Linux/Mac computer on the same network as Raspberry Pi

- Software

  - :ref:`kuiper`

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~~

In order to boot the Raspberry Pi and control the **EVAL-AD5593R-PMDZ**, you will need to install ADI Kuiper Linux on an SD card. Complete instructions, including where to download the SD card image, how to write it to the SD card, and how to configure the system are provided on the :ref:`kuiper`.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

Follow the configuration procedure under **Configuring the SD Card for Raspberry Pi Projects** on the :ref:`kuiper` page, substituting the following lines in **config.txt**:

     ::

        dtoverlay=rpi-ad5593r

     <WRAP important> The EVAL-AD5593R-PMDZ board has a 100k pullup resistor on the RESET pin, which correspond to Raspberry Pi GPIO13 and GPIO17 on PMD-RPI-INTZ P3 and P4, respectively. The default state of these pins is input, with a weak pulldown, but it is strong enough to pull the RESET line low. Adding the following line to config.txt will switch to pullup:

     ::

        gpio=13,17=pu,ip

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

To set up the circuit for evaluation, consider the following steps:

#. Connect the P9 of the **PMOD to Raspberry Pi Interposer** board at the male
   header GPIO pin connector of the **Raspberry Pi** as shown below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0552/interposer.png
      :width: 400px

#. Connect the
   :adi:`EVAL-AD5593R-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5593r-pmdz.html>`
   on the PMOD to Raspberry Pi Interposer board either via Port P3 or P4.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/5593_rpi.jpg
      :width: 400px

#. Burn the SD card with the proper ADI Kuiper Linux image. Insert the burned SD
   card into the designated slot on the RPi.
#. Connect the system to a monitor using an HDMI cable through the mini HDMI
   connector on the RPi.
#. Connect a USB keyboard and mouse to the RPi through the USB ports.

#. Power on the RPi board by plugging in a 5V power supply with a micro-USB
   connector. The final setup should look similar to the picture below.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/setup_5593.png
      :width: 500px

Application Software (All Platforms)
------------------------------------

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The Libiio is a library used for interfacing with IIO devices and is required to
be installed on your computer.

.. admonition:: Download

   Download and Install the latest
   `Libiio package <https://github.com/analogdevicesinc/libiio/releases>`__ on
   your machine.

To be able to connect your device, the software must be able to create a
context. The context creation in the software depends on the backend used to
connect to the device as well as the platform where the EVAL-AD5593R-PMDZ is
attached. Two platforms are currently supported for the AD5593R: Raspberry Pi
using the ADI Kuiper Linux and the ADICUP3029 running the no-OS AD5593R demo
project. The user needs to supply a **URI** which will be used in the context
creation.

The
:dokuwiki:`iio_info </resources/tools-software/linux-software/libiio/iio_info>`
command is a part of the libIIO package that reports all IIO attributes.

Upon installation, simply enter the command on the terminal command line to
access it.

For RPI Direct Local Access:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info

For Windows machine connected to Raspberry Pi:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   iio_info -u ip:<ip address of your ip>

Example:

- If your Raspberry Pi has the IP address 192.168.1.7, you have to use *iio_info
  -u ip::192.168.1.7* as your URI

.. note::

   Do note that the Windows machine and the RPI board should be connected to the
   same network in order for the machine to detect the device.

IIO Commands
~~~~~~~~~~~~

There are different commands that can be used to manage and control the device
being used. The
:dokuwiki:`iio_attr </resources/tools-software/linux-software/libiio/iio_attr>`
command reads and writes IIO attributes.

::

   analog@analog:~$ iio_attr [OPTION]...

Example:

- To look at the context attributes, enter this code on the terminal:

::

   analog@analog:~$ iio_attr -a -C

The
:dokuwiki:`iio_reg </resources/tools-software/linux-software/libiio/iio_reg>`
command reads or writes SPI or I2C registers in an IIO device. This is generally
not needed for end applications but can be useful in debugging drivers. Note
that you need to specify a context using the *-u* qualifier when you are not
directly accessing the device via RPI or when you are using the ADICUP3029
platform.

::

   analog@analog:~$ iio_reg -u <context> <device> <register> [<value>]

Example:

- To read the device ID (register = 0x02) of an AD5593R interfaced via RPI from
  a Windows machine, enter the following code on the terminal:

::

   iio_reg -u ip:<ip address> ad5593r 0x02

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO-Oscilloscope found
   on this link\ :git-iio-oscilloscope:`releases\+`

#. Once done with the installation or an update of the latest IIO-Oscilloscope,
   open the application. The user needs to supply a URI which will be used in
   the context creation of the IIO Oscilloscope and the instructions can be seen
   in the previous section.
#. Press refresh to display available IIO Devices, once ad5593r appeared, press
   connect.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/5593_iio_connect.jpg
   :width: 300px

Debug Panel
^^^^^^^^^^^

Below is the Debug panel of AD5593R wherein you can directly access the
attributes of the device.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/5593_debug.jpg
   :width: 300px

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the input capacitances
and the device temperature.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/5593_dmm.jpg
   :width: 300px

PyADI-IIO
~~~~~~~~~

:dokuwiki:`PyADI-IIO </resources/tools-software/linux-software/pyadi-iio>` is a
Python abstraction module for ADI hardware with IIO drivers to make them easier
to use. This module provides device-specific APIs built on top of the current
libIIO Python bindings. These interfaces try to match the driver naming as much
as possible without the need to understand the complexities of libIIO and IIO.

Follow the step-by-step procedure on how to install, configure, and set up
PYADI-IIO and install the necessary packages/modules needed by referring to this
:dokuwiki:`link </resources/tools-software/linux-software/pyadi-iio>`.

Running the example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PYADI-IIO in your machine, you are now ready to
run Python script examples. In our case, run the https://ad5592r_example.py/
found in the examples folder.

<code> D:\\pyadi-iio\\examples>python ad5592r_example.py </code>

Press enter and you will get these readings.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/ad5593r-pmod/5593_pyadi.jpg
   :width: 600px

.. admonition:: Download

   Github link for the Python sample script:
   :git-pyadi-iio:`AD5593R Python Example <examples/ad5592r_example.py+>`

More Information and Useful Links
---------------------------------

- :adi:`AD5593R Product Page <AD5593R>`
- :adi:`EVAL-AD5593R-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad5593r-pmdz.html>`
- :dokuwiki:`AD5592/AD5593 PMOD ADICUP3029 Demo </resources/eval/user-guides/eval-adicup3029/reference_designs/demo_ad5592r_ad5593r>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`EVAL-AD5593R-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad5593r-pmdz-designsupport.zip>`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

- `pyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`__
- :dokuwiki:`PyADI-IIO Installation Guide </resources/tools-software/linux-software/pyadi-iio>`
- :dokuwiki:`IIO Oscilloscope Installation Guide </resources/tools-software/linux-software/iio_oscilloscope>`
- :ref:`kuiper`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you register your hardware.
   :reg:`Register <EVAL-AD5593R-PMDZ?&v=RevC>` to receive all these great
   benefits and more!


