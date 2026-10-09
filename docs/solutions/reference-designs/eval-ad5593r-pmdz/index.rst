.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/eval-ad5593r-pmdz

.. _eval-ad5593r-pmdz:

EVAL-AD5593R-PMDZ
=================

8-channel, 12-Bit, Configurable ADC/DAC/GPIO with on-chip Reference, I2C
interface Pmod Module

Overview
--------

:adi:`EVAL-AD5593R-PMDZ` is a minimalist 8-channel, 12-Bit, Configurable
ADC/DAC/GPIO with on-chip Reference, I2C interface Pmod module. This
board serves as a low-cost alternative to the full-featured product
evaluation boards, with terminal block connections and no extra signal
conditioning.

.. figure:: eval-ad5593r-pmdz.png

This user guide will focus on the hardware aspect of the
:adi:`EVAL-AD5593R-PMDZ` including the connectors, indicators, and
different configurations a user would require in order to use the
hardware. There is also a link to the design files as well as
software reference designs that use the hardware with example
embedded firmware for a real demo.

Simplified functional block diagram
-----------------------------------

.. figure:: ad5593r_block_diagram.png

Connectors and Configuration
----------------------------

The following section reviews all the hardware connectors and how to
interface with them. It also reviews configuration options and well as
important onboard indicators.

Analog/Digital I/O Connector (P2 & P3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

========= ======= ======== ======================
Connector Pin No. Pin Name Pin Description
========= ======= ======== ======================
P2        1       CH3      Channel 3 Input/Output
          2       CH2      Channel 2 Input/Output
          3       CH1      Channel 1 Input/Output
          4       CH0      Channel 0 Input/Output
          5       GND      Ground
          6       VDD      Power Supply
P3        1       VREF     Voltage Reference
          2       GND      Ground
          3       CH7      Channel 7 Input/Output
          4       CH6      Channel 6 Input/Output
          5       CH5      Channel 5 Input/Output
          6       CH4      Channel 4 Input/Output
========= ======= ======== ======================

I2C Pmod Connector (P1)
~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD5593R-PMDZ` digital Pmod connector is described
in the table below.

======= ======== ================
Pin No. Pin Name Pin Description
======= ======== ================
1       NC       Not Connected
2       RST      Reset Pin
3       SCL      I2C Serial Clock
4       SDA      I2C Serial Data
5       DGND     Digital Ground
6       VDD      Power Supply
======= ======== ================

Test Points
~~~~~~~~~~~

Users can also check the I2C signal quality and voltage supply of the
board using test points labeled RST, SCL, SDA, and VLOGIC.

.. figure:: 5593-1.png

Voltage Reference Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default connection of the AD5593R **VREF** pin is shorted at pin 1
of the JP1 solder jumper where you can easily configure your voltage
reference input at pin 1 of terminal block P3, either from an external
source or internal 2.5 V

.. figure:: 5593-2.png

LED Indicator
~~~~~~~~~~~~~

The DS1 is the power green LED indicator of the board.

.. figure:: 5593-3.png

Power Supply Considerations and Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using the AD5593R Pmod board, the 3.3V power for the Pmod comes
directly from the host board it is connected to. The power from the host
is generally capable of providing up to 100 mA at 3.3V, but for complete
Pmod power specifications please click
:download:`here <pmod-interface-specification-1_3_1.pdf>`.

Device Driver Support
---------------------

There are two device driver solutions that are provided for controlling
the :adi:`EVAL-AD5593R-PMDZ`:

#. **AD5593R no-OS Driver**

   - The :dokuwiki:`AD5593R no-OS driver <resources/tools-software/uc-drivers/ad5592r>`
     is used in bare-metal applications, typically running on low-power,
     embedded microcontrollers.

#. **AD5593R Linux Driver**

   - The :external+linux:ref:`ad5593r`
     is used in applications running the Linux operating system,
     typically on larger processors and SoC devices.

   - The AD5593R Linux driver uses the Industrial Input/Output (IIO)
     framework, greatly simplifying the development of application code
     via the cross-platform Libiio library, which is written in C and
     includes bindings for Python, MATLAB, C#, and other languages.
     Application code can run directly on the platform board,
     communicating with the device over the local backend, or from a
     remote host over the network or USB backends.

System Setup Using ADICUP3029
-----------------------------

The :adi:`EVAL-AD5593R-PMDZ` can be used with
:dokuwiki:`ADICUP3029 <resources/eval/user-guides/eval-adicup3029>`.

**Demo Requirements**
~~~~~~~~~~~~~~~~~~~~~

The following is the list of items needed in order to replicate this
demo.

- **Hardware**

  - :adi:`EVAL-ADICUP3029`
  - :adi:`EVAL-AD5593R-PMDZ`
  - Micro-USB to USB Cable
  - PC or Laptop with USB Port

- **Software**

  - PuTTY or other similar software
  - :git-eval-adicup3029:`ADuCM3029_demo_AD5593R.hex <main:projects/ADuCM3029_demo_ad5592r_ad5593r>`

.. important::

    There are two basic ways to program the ADICUP3029 with the software for
    the :adi:`AD5593R`.

     #. Dragging and Dropping the Hex to the DAPLink drive

         #. Using the drag and drop method, the software is going to be a
            version that Analog Devices creates for testing and evaluation
            purposes. This is the **EASIEST** way to get started with the
            reference design.

     #. Building, Compiling, and Debugging using CCES

         #. Importing the project into
            :adi:`CrossCore Embedded Studio`
            is going to allow you to change parameters and customize the
            software to your application, but will a bit more advanced and
            will require you to download the CrossCore toolchain.

.. admonition:: Download

   The software for the **ADICUP3029_AD5593R** demo can be found here:

   AD5593R Source Files

     - :git-eval-adicup3029:`ADuCM3029_demo_AD5593R Source Code <main:projects/ADuCM3029_demo_ad5592r_ad5593r>`

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

#. Connect **EVAL-AD5593R-PMDZ** board at connector **P9** of the
   **EVAL-ADICUP3029**.

   .. figure:: img_3001.jpg

#. Connect a micro-USB cable to the P9 connector of the EVAL-ADICUP3029
   and connect it to a computer. The final setup should look similar to the
   picture below.

   .. figure:: img_2998.jpg

#. Make sure the following switches are as shown in the table
   below.

   .. figure:: switch_config.png

#. From your PC, open My Computer and look for the DAPLink drive, if you
   see this then the drivers are complete and correct.

   .. figure:: daplink.jpg
      :width: 600px

#. Simply extract the provided zip file. Once extracted, you will see
   the pre-built hex file for the AD5593R demo. Then drag and drop this Hex
   file to the DAPLink drive and your ADICUP3029 board will be programmed.
   The DS2 (red) LED will blink rapidly.

#. The DS2 will stop blinking and will stay ON once the programming is
   done.

#. Open PuTTY or other similar software. Check the Device Manager to set
   the correct COM port for the ADICUP3029. Set the baud rate to 115200.

   .. figure:: ad5593_putty.png

#. The expected output viewed in the PuTTY is shown below.

   .. figure:: ad5593_example_adicup.png

System Setup Using Raspberry Pi
-------------------------------

The :adi:`EVAL-AD5593R-PMDZ` can be used with a Raspberry Pi.

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is a list of items needed in order to replicate this demo.

- **Hardware**

  - :adi:`EVAL-AD5593R-PMDZ`
  - :adi:`Pmod to Raspberry Pi Adapter (PMD-RPI-INTZ) <PMD-RPI-INTZ>`
  - Raspberry PI Zero, Zero W, 3B+, or 4
  - 16 GB (or larger) Class 10 (or faster) micro-SD card
  - 5 Vdc, 2.5 A power supply with micro USB connector (USB-C power
    supply for Raspberry Pi 4)
  - User interface setup (choose one):

    - HDMI monitor, keyboard, and mouse plugged directly into Raspberry
      Pi
    - Host Windows/Linux/Mac computer on the same network as Raspberry
      Pi

- **Software**

  - :external+kuiper:doc:`index`

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

In order to boot the Raspberry Pi and control the :adi:`EVAL-AD5593R-PMDZ`,
you will need to install ADI Kuiper Linux on an SD card. Complete
instructions, including where to download the SD card image, how to
write it to the SD card, and how to configure the system are provided on
the :external+kuiper:doc:`index`.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~

Follow the configuration procedure under **Configuring the SD Card for
Raspberry Pi Projects** on the :external+kuiper:doc:`index`
page, substituting the following lines in **config.txt**:

.. code-block::

   dtoverlay=rpi-ad5593r

.. warning::

    The EVAL-AD5593R-PMDZ board has a 100k pullup resistor on the
    RESET pin, which correspond to Raspberry Pi GPIO13 and GPIO17 on
    PMD-RPI-INTZ P3 and P4, respectively. The default state of these
    pins is input, with a weak pulldown, but it is strong enough to
    pull the RESET line low.
    Adding the following line to config.txt will switch to pullup:

    .. code-block::

         gpio=13,17=pu,ip

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

To set up the circuit for evaluation, consider the following steps:

#. Connect the P9 of the **Pmod to Raspberry Pi Interposer** board at
   the male header GPIO pin connector of the **Raspberry Pi** as shown
   below.

   .. figure:: interposer.png

#. Connect the :adi:`EVAL-AD5593R-PMDZ`
   on the Pmod to Raspberry Pi Interposer board either via Port P3 or
   P4.

   .. figure:: 5593_rpi.jpg

#. Burn the SD card with the proper ADI Kuiper Linux image. Insert the
   burned SD card into the designated slot on the RPi.

#. Connect the system to a monitor using an HDMI cable through the mini
   HDMI connector on the RPi.

#. Connect a USB keyboard and mouse to the RPi through the USB ports.

#. Power on the RPi board by plugging in a 5V power supply with a
   micro-USB connector. The final setup should look similar to the
   picture below.

   .. figure:: setup_5593.png

Application Software (All Platforms)
------------------------------------

Hardware Connection
~~~~~~~~~~~~~~~~~~~

The Libiio is a library used for interfacing with IIO devices and is
required to be installed on your computer.

.. admonition:: Download

    Download and Install the latest :git-libiio:`Libiio package <releases+>`
    on your machine.

To be able to connect your device, the software must be able to create a
context. The context creation in the software depends on the backend
used to connect to the device as well as the platform where the
EVAL-AD5593R-PMDZ is attached. Two platforms are currently supported for
the AD5593R: Raspberry Pi using the ADI Kuiper Linux and the ADICUP3029
running the no-OS AD5593R demo project. The user needs to supply a
**URI** which will be used in the context creation.

The :ref:`libiio iio_info`
command is a part of the libIIO package that reports all IIO attributes.

Upon installation, simply enter the command on the terminal command line
to access it.

For RPI Direct Local Access:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   iio_info

For Windows machine connected to Raspberry Pi:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   iio_info -u ip:<ip address of your ip>

Example:

 - If your Raspberry Pi has the IP address 192.168.1.7, you have to use
   *iio_info -u ip::192.168.1.7* as your URI

.. note::

    Do note that the Windows machine and the RPI board should be connected
    to the same network in order for the machine to detect the device.

IIO Commands
~~~~~~~~~~~~

There are different commands that can be used to manage and control the
device being used. The :ref:`libiio iio_attr`
command reads and writes IIO attributes.

.. code-block::

   analog@analog:~$ iio_attr [OPTION]...

Example:

 - To look at the context attributes, enter this code on the terminal:

    .. code-block::

        analog@analog:~$ iio_attr -a -C

The :ref:`libiio iio_reg`
command reads or writes SPI or I2C registers in an IIO device. This is
generally not needed for end applications but can be useful in debugging
drivers. Note that you need to specify a context using the *-u*
qualifier when you are not directly accessing the device via RPI or when
you are using the ADICUP3029 platform.

.. code-block::

    analog@analog:~$ iio_reg -u <context> <device> <register> [<value>]

Example:

 - To read the device ID (register = 0x02) of an AD5593R interfaced via
   RPI from a Windows machine, enter the following code on the terminal:

     .. code-block::

        iio_reg -u ip: ad5593r 0x02

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. caution::

    Make sure to download/update to the latest version of IIO-Oscilloscope
    found on this :git-iio-oscilloscope:`link <releases+>`.

#. Once done with the installation or an update of the latest
   IIO-Oscilloscope, open the application. The user needs to supply a
   URI which will be used in the context creation of the IIO
   Oscilloscope and the instructions can be seen in the previous
   section.

#. Press refresh to display available IIO Devices, once ad5593r
   appeared, press connect.

.. figure:: 5593_iio_connect.jpg

Debug Panel
^^^^^^^^^^^

Below is the Debug panel of AD5593R wherein you can directly access the
attributes of the device.

.. figure:: 5593_debug.jpg

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the input
capacitances and the device temperature.

.. figure:: 5593_dmm.jpg

PyADI-IIO
~~~~~~~~~

:ref:`pyadi-iio` is a Python abstraction module for ADI hardware with
IIO drivers to make them easier to use. This module provides
device-specific APIs built on top of the current libIIO Python bindings.
These interfaces try to match the driver naming as much as possible
without the need to understand the complexities of libIIO and IIO.

Follow the step-by-step procedure on how to install, configure, and set
up PYADI-IIO and install the necessary packages/modules needed by
referring to this link: :ref:`pyadi-iio`.

Running the example
^^^^^^^^^^^^^^^^^^^

After installing and configuring PYADI-IIO in your machine, you are now
ready to run Python script examples. In our case, run the
ad5592r_example.py found in the examples folder.

.. shell::

   ~/pyadi-iio/examples
   $ python3 ad5592r_example.py

Press enter and you will get these readings.

.. figure:: 5593_pyadi.jpg
   :align: center

.. admonition:: Download

   Github link for the Python sample script:
   :git-pyadi-iio:`AD5593R Python Example <examples/ad5592r_example.py>`

More Information and Useful Links
---------------------------------

- :adi:`AD5593R`
- :adi:`EVAL-AD5593R-PMDZ`
- :doc:`AD5592/AD5593 Pmod ADICUP3029 Demo </solutions/reference-designs/eval-adicup3029/reference_designs/demo_ad5592r_ad5593r>`

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`EVAL-AD5593R-PMDZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/eval-ad5593r-pmdz-designsupport.zip>`

   - Schematics
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Additional Information
----------------------

 - :git-pyadi-iio:`pyADI-IIO </>`
 - :ref:`pyadi-iio`
 - :ref:`iio-oscilloscope`
 - :external+kuiper:doc:`index`

Registration
------------

Receive software update notifications, documentation updates, view the
latest videos, and more when you register your hardware.
`Register <https://my.analog.com/en/app/registration/hardware/EVAL-AD5593R-PMDZ?&v=RevC>`__
to receive all these great benefits and more!
