.. _eval_adxrs290_pmdz eval:

ADXRS290 Gyroscope PMOD Demo
============================

Device Driver Support
---------------------

Two example device driver solutions are provided for controling the
**EVAL-ADXRS290-PMDZ** using the no-OS device driver on the
**EVAL-ADICUP3029** platform and Linux device driver on the
**Raspberry Pi** platform.

1. **EVAL-ADICUP3029**

   The ADICUP3029 example application uses the ADXRS290 no-OS driver, and
   emulates the Linux IIO framework through the tinyiiod daemon library. The
   application communicates with the host computer via the serial backend, over
   a USB-UART physical connection. This facilitates rapid application
   development on a host computer, independent from embedded code development.

2. **Raspberry Pi**

   The Linux driver uses the Industrial Input/Output (IIO) framework, greatly
   simplifying the development of applicaiton code via the cross-platform Libiio
   library, which is written in C and includes bindings for Python, MATLAB, C#,
   and other languages. Application code can run directly on the platform board,
   communicating with the device over the local bakend, or from a remote host
   over the network or USB backends.

Similarly, utility software (iio_info, IIO Oscilloscope, PyADI-IIO, etc.) can be
used for both the EVAL-ADXRS290-PMDZ on Raspberry PI and on ADICUP3029.

----

General Setup Using ADICUP3029
------------------------------

The :adi:`EVAL-ADXRS290-PMDZ` can be used with 
:dokuwiki:`ADICUP3029 </resources/eval/user-guides/eval-adicup3029>`

.. figure:: images/adxrs290_architecture.png
   :align: center
   :width: 400

   Software Architecture

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is a list of items needed in order to replicate this demo.

**Hardware:**

 -  :adi:`EVAL-ADICUP3029`
 -  :adi:`EVAL-ADXRS290-PMDZ`
 -  Micro-USB to USB cable
 -  PC or Laptop with a USB port

**Software:**

There are two basic ways to program the ADICUP3029 with the software for the
ADXRS290.

 -  Dragging and Dropping the HEX file to the DAPLINK drive
 -  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADICUP3029_ADXRS290** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt ADXRS290_IIO HEX File
   
   -  :git-no-OS:`ADXRS290-PMDZ.zip <releases/download/last_commit/adxrs290-pmdz.zip+>`
   
   Complete ADXRS290_IIO Source Files
   
   -  :git-no-OS:`ADXRS290 tinyiiod project source for ADICUP3029 platform <projects/adxrs290-pmdz>`
   

To build the project from source, follow the instructions in the
:git-no-OS:`no-os wiki <wiki+>`.

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

#.  Connect **EVAL-ADXRS290-PMDZ** board at connector **P8** of
    the **EVAL-ADICUP3029**.
#.  Connect a micro-USB cable to the P10 connector of the EVAL-ADICUP3029
    and connect it to a computer. The final setup should look similar
    to the picture below.

.. image:: images/pmodtoadicup_v2.jpg

Flashing the Firmware/Program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/adicup3029_settings.jpg
   :width: 900

#. Make sure the following switches are as shown from the table below:
#. Connect the ADICuP3029 to the PC host via micro-USB cable as shown below.
#. From your PC, open My Computer and look for the DAPLINK drive, if you see
   this then the drivers are complete and correct.

    .. image:: images/daplink_in_mycomputer.jpg
       :width: 600

#. Simply extract the provided zip file. Do note that when you extract the zip
   file, there are two Hex file compressed inside. For this demo use the
   **adxrs290-pmdz_aducm3029_iio_uart.hex**. Then drag and drop this Hex file
   to the DAPLINK drive and your ADICUP3029 board will be programmed. The DS2
   (red) LED will blink rapidly.
#. The DS2 will stop blinking and will stay ON once the programming is done.

.. note::

   An alternative human-readable Command Line Interface (CLI) program is also
   available for the ADXRS290 Pmod on the EVAL-ADXRS290-PMDZ:
   :doc:`ADXRS290 Gyroscope PMOD Command Line Interface Demo </solutions/reference-designs/eval-adicup3029/reference_designs/demo_adxrs290_pmod>`

----

General Setup Using Raspberry Pi
--------------------------------

The :adi:`EVAL-ADXRS290-PMDZ` can be used with a Raspberry Pi.

Demo Requirements
~~~~~~~~~~~~~~~~~

The following is a list of items needed in order to replicate this demo.

-  **Hardware**

   -  :adi:`EVAL-ADXRS290-PMDZ` Circuit Evaluation Board
   -  Raspberry PI Zero, Zero W, 3B+, or 4
   -  16GB (or larger) Class 10 (or faster) micro-SD card
   -  5Vdc, 2.5 A power supply with micro USB connector (USB-C power
      supply for Raspberry Pi 4)
   -  Electrical connection hardware (choose one):

      -  12x 15cm socket-to-socket jumpers such as
         `these from Schmartboard <https://schmartboard.com/wire-jumpers/female-jumpers/5-inch/>`_

         -  `DesignSpark HAT to Pmod Adapter <https://reference.digilentinc.com/reference/add-ons/pmod-hat/start>`_

   -  User interface setup (choose one):

      -  HDMI monitor, keyboard, mouse plugged directly into Raspberry Pi
      -  Host Windows/Linux/Mac computer on same network as Raspberry Pi

-  **Software**

   -  :external+kuiper:doc:`Kuiper Images <index>`

Loading Image on SD Card
~~~~~~~~~~~~~~~~~~~~~~~~

In order to control the **EVAL-ADXRS290-PMDZ** from the Raspberry Pi,
you will need to install ADI Kuiper Linux on an SD card. Complete
instructions, including where to download the SD card image, how to
write it to the SD card, and how to configure the system are provided
at :external+kuiper:doc:`Kuiper Images <index>`.

Write the image and follow the system configuration procedure.

Configuring the SD Card
~~~~~~~~~~~~~~~~~~~~~~~

Follow the Hardware Configuration procedure under
**Preparing the Image: Raspberry Pi** in the
:external+kuiper:doc:`Kuiper Images <index>` page, substituting
the following lines in **config.txt**:

.. code-block::

   dtoverlay=rpi-adxrs290

Setting up the Hardware
~~~~~~~~~~~~~~~~~~~~~~~

To set up the circuit for evaluation, consider the following steps:

.. image:: images/rpi_pmod_con.jpg

.. important::

   Do note that the I/O pins of the Raspberry Pi board are only
   3.3V tolerant. Any peripheral to be attached should be powered
   by a source not exceeding 3.3V.

#.  Connect **EVAL-ADXRS290-PMDZ** board at male header connector
    of the **Raspberry Pi**.
#.  Burn the SD card with the proper ADI Kuiper Linux image. Insert
    the burned SD card on the designated slot on the RPi.
#.  Connect the system to a monitor using an HDMI cable through
    the mini HDMI connector on the RPi.
#.  Connect a USB keyboard and mouse to the RPi through the
    USB ports.
#.  Power on the RPi board by plugging in a 5V power supply
    with a micro-USB connector. The final setup should look
    similar to the picture below.

.. image:: images/system_con.jpg

----

Software (both ADICUP3029 and Raspberry Pi)
-------------------------------------------

Connection
~~~~~~~~~~

To be able to connect your device, the software must be able to create a
context. The context creation in the software depends on the backend used to
connect to the device as well as the platform where the EVAL-ADXRS290-PMDZ is
attached. Two platforms are currently supported for the ADXRS290: Raspberry Pi
using the ADI Kuiper Linux and the ADICUP3029 running the ADXRS290 IIO demo
project. The user needs to supply a URI which will be used in the context
creation.

The Libiio is a library for interfacing with IIO devices.

.. admonition:: Download
   :class: download

   Install the :git-libiio:`Libiio package <releases+>` on your machine.

The :ref:`libiio iio_info` command is a part of the
libIIO package that reports all IIO attributes.

Upon installation, simply enter the command on the terminal command line to
access it.

For RPI Direct Local Access:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   iio_info

For Windows machine connected to Raspberry Pi:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   iio_info -u ip:<ip address of your ip>

Example:

-  If your Raspberry Pi has the IP address 192.168.1.7, you have to
   use *iio_info -u ip::192.168.1.7* as your URI

.. note::

   Do note that the Windows machine and the RPI board should be connected
   to the same network in order for the machine to detect the device.

For Windows machine connected to ADICUP3029:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block::

   iio_info -u serial:<serial port>

Examples:

-  In a Windows machine, you can check the port of your ADICUP3029
   via Device Manager in the Ports (COM & LPT) section. If your
   device is in COM4, you have to use *iio_info -u serial:COM4*
   as your URI.
-  In a Unix-based machine, you will see it under the /dev/ directory
   in this format "ttyUSBn", where n is a number depending on how
   many serial USB devices attached. If you see that your device
   is ttyUSB0, you have to use serial:/dev/ttyUSB0 as your URI.

IIO Commands
^^^^^^^^^^^^

There are different commands that can be used to manage the device being used.
The :ref:`libiio iio_attr` command reads and writes IIO attributes.

.. code-block::

   analog@analog:~$ iio_attr [OPTION]...

Example:

-  To look at the context attributes, enter this code on the terminal:

.. code-block::

   analog@analog:~$ iio_attr -a -C

The :ref:`libiio iio_reg` command reads or writes SPI or I2C
registers in an IIO device. This is generally not needed for end
applications, but can be useful in debugging drivers. Note that you
need to specify a context using the *-u* qualifier when you are not
directly accessing the device via RPI or when you are using the
ADICUP3029 platform.

.. code-block::

   analog@analog:~$ iio_reg -u <context> <device> <register> [<value>]

Example:

-  To to read the device ID (register = 0x02) of an ADXRS90 interfaced
   via RPI from a Windows machine, enter the following code on
   the terminal:

.. code-block::

   iio_reg -u ip:<ip address> adxrs290 0x02

----

IIO Oscilloscope
~~~~~~~~~~~~~~~~

.. important::

   Make sure to download/update to the latest version of IIO-Oscilloscope found on this
   :git-iio-oscilloscope:`link <releases+>`.

-  Once done with the installation or an update of the latest IIO-Oscilloscope, open
   the application. The user needs to supply a URI which will be used in the context
   creation of the IIO Oscilloscope and the instructions can be seen from the
   previous section.
-  Press refresh to display available IIO Devices, once adxrs290 appeared, press
   connect.

.. image:: images/iio_osc_connection.jpg
   :align: center
   :width: 500

Debug Panel
^^^^^^^^^^^

Below is the Debug panel of ADXRS290 wherein you can directly access the
attributes of the device.

.. image:: images/adxrs290_debug.png
   :width: 500

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the X and Y's angular
velocities.

.. image:: images/adxrs290_dmm-2.png
   :width: 500

Waveform Panel
^^^^^^^^^^^^^^

The Waveform panel, also known as the Capture window, displays the real-time
waveform of ADXRS290's response.

.. image:: images/iio_osc_graph.jpg
   :width: 500

.. note::

   The readings from the DMM panel will freeze upon activation of the real-time
   plot in the waveform panel i.e. the two panels are designed to be used
   separately and not simultaneously.

----

PyADI-IIO
~~~~~~~~~

:ref:`PyADI-IIO <pyadi-iio>` is a python abstraction module for ADI hardware
with IIO drivers to make them easier to use. This module provides
device-specific APIs built on top of the current libIIO python bindings.
These interfaces try to match the driver naming as much as possible without
the need to understand the complexities of libIIO and IIO.

Install PyADI-IIO using one of the methods in :ref:`PyADI-IIO <pyadi-iio>`.

The ADXRS290 example requires a number of packages to be installed before
it can be used. To ensure that all required packages are present, we will
be installing them in a virtual environment so that other python projects
will not be affected by this added configuration. Make sure that
`virtualenv <https://pypi.org/project/virtualenv/>`_ has been installed
before proceeding.

Creating a Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Open a command prompt and navigate to the *pyadi-iio* directory.
#. Create a virtual environment by entering the following command:

   .. code-block:: none

      D:\pyadi-iio>python -m venv adxrs290

   Note that the last argument *adxrs290* is just the name of the
   virtual environment to be created. It can be replaced by any
   other name or identifier that you prefer. In case the code
   above does not work, try:

   .. code-block:: none

      D:\pyadi-iio>virtualenv adxrs290

#. Input the following command to activate the virtual environment:

   .. code-block:: none

      D:\pyadi-iio>adxrs290\Scripts\activate

Installing the Packages
^^^^^^^^^^^^^^^^^^^^^^^

Upon activation of the virtual environment, enter the
following commands:

.. code-block::

   (adxrs290) D:\pyadi-iio>pip install -r requirements.txt
   (adxrs290) D:\pyadi-iio>pip install -r examples/requirements_adiplot.txt
   (adxrs290) D:\pyadi-iio>python setup.py install

.. important::

   One of the packages in *requirements_adiplot.txt* is the PyQt5.
   If you already have a pre-installed PyQt5 prior to the installation
   of the packages, we suggest that you uninstall the said package
   in the virtual environment. Duplicate installations may sometimes
   cause errors that inhibit the system from displaying the real-time
   plot. This can easily be done by inputting the command:
   *pip uninstall PyQt5* while the virtual environment is active.

Running the Example
^^^^^^^^^^^^^^^^^^^

#. Connect the ADXRS290 to the device platform you've chosen.
#. If interfaced via RPI, connect your laptop to the same network
   as the ADXRS290 and take note of its IP address. For ADICUP3029,
   take note of the serial port used.
#. On the source code, go to the *examples* folder and open
   *adxrs290.py*. Provide the necessary context in order to detect
   the device. Make sure that only one context source is active
   and the other one is commented out depending on whether you are
   using the RPI board or the ADICUP3029.
#. Run the example by typing this line on the command prompt:

   .. code-block:: none

      D:\pyadi-iio\examples>python adxrs290.py

   .. admonition:: Download
      :class: download

      Below is a copy of the python script:

      :dokuwiki:`adxrs290.py <_media/resources/eval/user-guides/circuits-from-the-lab/eval-adxrs290-pmdz/adxrs290.zip>`

     It will return these lines of data on the terminal:

   .. image:: images/adxrs290_output.png
      :alt: Output on Terminal
      :align: center
      :width: 700

#. You can opt to see a real-time plot of ADXRS290's output.
   To do this, open *adxrs290.py* and set *enable_plot* to
   True.
   
    .. image:: images/adxrs290_enable-plot.png
       :width: 500
   
 
 A plot will pop-up after running the code:

 .. image:: images/adxrs290_plot.png
    :alt: ADXRS290's Real-time Plot
    :align: center
    :width: 500

----

Video Guides
~~~~~~~~~~~~

Unboxing
^^^^^^^^

.. image:: https://img.youtube.com/vi/Z4bt3IdRFEQ/maxresdefault.jpg
    :width: 600px
    :target: https://www.youtube.com/watch?v=Z4bt3IdRFEQ

EVAL-ADICUP3029 Demo
^^^^^^^^^^^^^^^^^^^^

.. image:: https://img.youtube.com/vi/LwD-MHoSlWk/maxresdefault.jpg
    :width: 600px
    :target: https://www.youtube.com/watch?v=LwD-MHoSlWk

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download
   :class: download

   :adi:`EVAL-ADXRS20-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-adxrs290-pmdz-designsupport.zip>`

   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   
Additional Information and Useful Links
---------------------------------------

-  :adi:`ADXRS290 Product Page <ADXRS290>`

Reference Demos & Software
--------------------------

-  :git-no-OS:`ADXRS290 No-OS Build Instruction Guide <wiki+>`
-  :git-no-OS:`ADXRS290 No-OS Drivers <projects/adxrs290-pmdz>`
-  :external+kuiper:doc:`Kuiper Images <index>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos,
   and more when you register your hardware.
   `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-ADXRS290-PMDZ?&v=Rev A>`_
   to receive all these great benefits and more!
