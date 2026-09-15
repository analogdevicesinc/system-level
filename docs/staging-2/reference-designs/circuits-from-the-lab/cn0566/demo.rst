.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0566/demo

.. _circuits-from-the-lab cn0566 demo:

Monopulse Tracking using Phased Array Beamforming​
==================================================

Overview
--------

Monopulse tracking, introduced by Robert Page in 1943 during World War II,
significantly advanced radar tracking capabilities. This technology uses a
phased array to accurately track an object"s path by arranging the array
elements in a line parallel to the horizon, enabling precise tracking of
horizontal motion.

The term ``monopulse`` combines the Greek word ``mono,`` meaning single, and
``pulse,`` referring to a single burst of electromagnetic transmission received
by the antenna. This method tracks a target"s location in terms of azimuth
(horizontal angle) and elevation (vertical angle).

The tracking capability relies on 4×8 antenna lobes, divided into right and left
lobes.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/antenna_lobe.png
   :width: 600px

Signals received by these lobes are processed to create a Sum signal (total
power received) and Difference or Delta signals (difference between signals from
the left and right lobes). The Sum and Delta signals help estimate the target"s
angle:

- If the target is at the center of the radar beam, the delta signal is zero.
- If the target is off-center, the delta signal indicates the direction and
  distance of deviation.

By comparing the Sum and Delta signals, the system can determine the exact angle
of the target in both azimuth and elevation.

Today, monopulse tracking is used in various applications, including military,
air traffic control, space and satellite tracking, aerospace, weather radars,
surveillance, reconnaissance, and telecommunications.

--------------

Demo Objective
--------------

This demo explores the capability of the :adi:`CN0566` to accurately determine
the direction of a target by comparing signals received in multiple, closed
spaced beams.

Demo Setup
----------

Requirements
~~~~~~~~~~~~

- :adi:`EVAL-CN0566-RPIZ <CN0566>` kit
- HB100 microwave source (included in the CN0566 kit)
- HB100 Casing (to be printed; see instructions in the
  :dokuwiki:`#Hardware Setup <#Hardware Setup>` section below)
- 5V, 3A, USB-C wall adapter
- 5V Benchtop Power Supply or Power Bank
- Micro HDMI to HDMI cable (or suitable adapters)
- 16 GB or larger SD card
- Tripod
- Ethernet cable

- Software
- :ref:`kuiper`

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/demo_req.jpg

Hardware Setup
--------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/system_setup.jpg

**CN0566 Phaser Array**

The CN0566 board comes fully assembled and does not require any additional
hardware setup for the demo. For more details about the hardware, you can check
out the
:dokuwiki:`Phaser Hardware Overview page </resources/eval/user-guides/circuits-from-the-lab/cn0566/overview_setup>`.

**HB100 Microwave Sensor**

To set up the HB100 Microwave Sensor:

**Casing**: Download and 3D print the HB100 casing
:download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/hb100_holder.zip`
. This casing includes a 1/4-20 thread, which is standard for camera mounts or
tripods.

**Mounting**: Attach the HB100 to the casing and then mount the casing onto a
tripod or mount. Ensure the center of the HB100 is at the same height as the
center of the CN0566.

**Connecting Power Supply and Other Peripherals**

#. Connect the Raspberry Pi HDMI output closest to the power connector to the
   monitor via an HDMI cable.
#. Connect the USB keyboard and mouse to the Raspberry Pi USB ports.
#. Plug the USB-C wall adapter into the USB-C power jack on the
   EVAL-CN0566-RPIZ. Do NOT plug into the Raspberry Pi USB-C port.
#. Carefully thread the tripod into the tripod mount.
#. Power up the HB100 microwave source with 5V power bank using a micro USB to
   USB cable. Aim this at the array.

Software Setup
--------------

CN0566 Phaser Setup
~~~~~~~~~~~~~~~~~~~

.. note::

   **SD Card Image**

   Install ADI Kuiper Linux on an SD card. Detailed instructions, including
   downloading the SD card image, writing it to the SD card, and configuring the
   system, are available at :ref:`kuiper`.

   Pay close attention to localization settings, keyboard settings, etc.,
   especially when running examples directly on the Raspberry Pi.

   **SD Card Configuration**

   After burning the image, log into the Raspberry Pi and open the configuration
   utility. Set the hostname to **``phaser``** and configure the locale,
   keyboard, and Wi-Fi country (if using Wi-Fi).

   Run the necessary commands to complete the setup. Review the setup script for
   any updates, as newer versions of Kuiper Linux may have changes.

   ::

      wget https://github.com/thorenscientific/rpi_setup_stuff/raw/main/phaser/phaser_sdcard_setup.sh
      sudo chmod +x phaser_sdcard_setup.sh
      ./phaser_sdcard_setup.sh

Python Installation
^^^^^^^^^^^^^^^^^^^

This part assumes a fresh installation of all required software.

#. Download the latest version of Python. Choose the latest available version
   depending on the operating system.
#. Run installer as Administrator.

- During installation, check ``Add Python version to PATH`` before clicking
  ``Install Now``

#. To check if the download is successful, go to command prompt and type the
   command line below: <code> Python –version </code>

Libiio Installation
^^^^^^^^^^^^^^^^^^^

.. note::

   **Libiio** is a library that has been developed by Analog Devices to ease the
   development of software interfacing Linux Industrial I/O (IIO) devices. To
   learn more about Libiio, you can visit the following links:

   - `Libiio User Guide <https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq2-ebz/software/linux/applications/libiio>`__
   - `Libiio Internals <https://wiki.analog.com/resources/tools-software/linux-software/libiio_internals>`__

::

   -Download and install the latest release of libIIO that can be found in this link: :git-libiio:`releases+` .. note::

   Note: There are different installers that can be found in the link, choose the installer that is fit to your host PC. \\ \\ Example: **libiio-0.25-gb6028fd-windows.zip for PC running Windows OS**

::

   -Install the libIIO bindings through pip <code> Pip install pylibiio </code>

Pyadi-iio Installation
^^^^^^^^^^^^^^^^^^^^^^

.. note::

   **Pyadi-iio** is a python abstraction module for ADI hardware with IIO
   drivers to make them easier to use, to learn more about the pyadi-iio you can
   visit this link:
   https://wiki.analog.com/resources/tools-software/linux-software/pyadi-iio

::

   -In windows terminal, clone the pyad-iio repository using the following command: <code>Git clone :git-pyadi-iio.git<:`code>+`
   -Go to the repository where the pyadi-iio is cloned <code>Cd <folder address>/pyadi-iio</code>
   -Install the pre-requisite packages using the requirement text files. <code>Pip install -r requirements.txt</code>
   -Install the PyADI-IIO bindings through pip. <code>Pip install pyadi-iio</code>

Running the System
------------------

To run the GUI for the EVAL-CN0566-RPIZ, you need to run the following in the command line terminal:

.. code::

   cd <pyadi-iio directory>
   cd examples/phaser
   python phaser_gui.py

#. After running the Phaser GUI, select **``Tracking``** in mode selection and
   select ``Lab 8. Monopulse Tracking`` on the middle lower part of the GUI.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/gui.png

#. Click the check boxes for ``Show Delta`` and ``Show Error`` in the
   ``Digital`` tab. Turning the phaser would result to a response to the sum and
   delta plot, tracking the direction of the HB100.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/monopulse.png

#. Select ``Tracking`` from the ``Mode Selection`` in the ``Config`` tab, this
   will create a new window named ``Signal Tracking``.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/steering_angle.png

Help and Support
----------------

For questions and more information, please visit the Analog Devices Engineer Zone. .. note::

   For internal support, you can raise a question or submit a ticket through our Jira Service Desk using the following link: `BU Applications Technical Support <https://jira.analog.com/servicedesk/customer/portal/131>`__.

   For external users, please post your questions under the :ez:`Reference Designs <reference-designs/>` forum in EngineerZone to get assistance from the community and experts.

Related Documents
~~~~~~~~~~~~~~~~~

* :dokuwiki:`EVAL-CN0566-RPIZ User Guide </resources/eval/user-guides/circuits-from-the-lab/cn0566>`
* :dokuwiki:`EVAL-CN0566-RPIZ Hardware User Guide </resources/eval/user-guides/circuits-from-the-lab/cn0566/overview_setup>`
* :dokuwiki:`EVAL-CN0566-RPIZ Software User Guide </resources/eval/user-guides/circuits-from-the-lab/cn0566/software>`
