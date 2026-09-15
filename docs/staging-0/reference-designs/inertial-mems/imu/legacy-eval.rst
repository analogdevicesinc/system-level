.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/imu/legacy-eval

.. _inertial-mems imu legacy-eval:

Legacy Evaluation Master Page
=============================

This page lists all of the device-specific, legacy evaluation guides. Other
pages pull data from this page.

ADIS1613x Overview
------------------

The :adi:`ADIS1613x <ADIS16136>` iSensor® is a product family of high
performance, digital gyroscope sensing systems that operate autonomously and
requires no user configuration to produce accurate rate sensing data. It
provides performance advantages with low noise density, wide bandwidth, and
excellent in-run bias stability, which are enabling applications such as
platform control, navigation, robotics, and medical instrumentation. All
:adi:`ADIS1613x <ADIS16136>` product sensors use a serial peripheral interface
for data communications. This interface enables direct connection with a large
variety of embedded processor products. This electrical connection typically
only requires 5 I/O lines for synchronous data collection, as shown in the
following figure:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-spi-connection.png
   :width: 400px

ADIS1613x Breakout Board
------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16136` to an
embedded controller will provide the most flexibility in developing application
firmware and will more closely reflect the final system design. The
:adi:`ADIS16IMU1 <EVAL-ADIS16IMU1>` is the breakout board for the
:adi:`ADIS1613x <ADIS16136>` product family and may assist in the process of
hooking it up to an existing embedded processor system.

ADIS1613x Supply Selection
--------------------------

The following picture (left side) shows JP1 in the **+3.3V** position
(factory-default). Change the JP1 jumper setting on the :adi:`ADISUSB` to the
**+5V** position (shown on the right) required for the
:adi:`ADIS1613x <ADIS16136>` product family.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-5v-markedsetting.png
   :width: 400px

.. important::

   If JP1 is left on **+3.3V**, the gyroscope outputs will not respond and will
   appear to be saturated in one direction or the other. See the following
   picture for an example of this behavior.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-adisusb-main-screen-voltage-error.png
      :width: 500px

ADIS1613x Software Download
---------------------------

Click :adi:`here <static/imported-files/eval_boards/135ES4.zip>` to download the
ADIS16133/5/6 Evaluation Software. The download file will contain three separate
files: The CAB file (ADIS16135_Rev_4.cab), the setup file (setup.exe), and the
setup list. Copy these files to a convenient folder for running the application.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-zipfile-download.png
   :width: 600px

ADISUSB: PC Evaluation
----------------------

.. important::

   UPDATE NOTICE: This guide describes the use of an evaluation tool
   (EVAL-ADISZ) that is no longer available for purchase and remains online to
   support those who already have these tools.

For those who would prefer to perform PC-based evaluation before developing
their embedded system, the :adi:`ADISUSB` is the appropriate system to use. The
remainder of this Wiki site will focus on PC-based evaluation with the
:adi:`ADISUSB` system.

ADISUSB: System Requirements
----------------------------

Windows XP, Vista, 7 (32-bit systems only)

.. tip::

   All the required files are included and are deployed during software package
   install.

.. important::

   Do not plug the :adi:`ADISUSB` into the PC at this stage of the setup! Please
   wait until the software installation is complete.

ADISUSB: Physical Connection
----------------------------

The :adi:`ADISUSB` offers two connection methods for interfacing with our legacy
modules, remote mounting via J1, and onboard evaluation via J4.

The remote mounting option uses an :adi:`ADIS16IMU1 <EVAL-ADIS16IMU1>` to
connect the module to the :adi:`ADISUSB` using a ribbon cable. J1 on
:adi:`ADIS16IMU1 <EVAL-ADIS16IMU1>` is a dual-row, 2 mm (pitch) connector that
mates to a number of ribbon cable systems, including 3M Part Number
152212-0100-GB (ribbon crimp connector) and 3M Part Number 3625/12 (ribbon
cable). Connect J1 on the :adi:`ADISUSB` to J1 on the
:adi:`ADIS16IMU1 <EVAL-ADIS16IMU1>`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-pcbz-dimensions.png
   :width: 300px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-pcbz-connection.png
   :width: 500px

The onboard install directly connects to the J4 connector of the :adi:`ADISUSB`.
The following pictures provide a visual reference for the correct connection.
Mounting to the system frame is accomplished by using 4 M2 pre-drilled holes in
the :adi:`ADISUSB`, marked in the picture below.]]

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-mnt-locations.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-part-mounted.png
   :width: 400px

.. important::

   Make sure that the connector is in proper alignment before pressing it in.
   Misalignment can cause pin damage and may damage the module!

ADISUSB: Evaluation Software Guide
----------------------------------

.. tip::

   The instructions shown below reference the ADIS1613x device, but are
   applicable to all legacy iSensor products.

Navigate to the folder where the files were saved and double click the setup.exe
file. The **Welcome** screen will appear. Click **OK** to continue.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-welcome.png
   :width: 500px

Choose a directory for the software application to extract the files or use the
default settings (recommended) and click the computer icon button to go to the
next step.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-install.png
   :width: 500px

Choose a program group or use the default settings (recommended) and click
**Continue**.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-prgrm-group.png
   :width: 400px

USB Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~

The ADIS16135_Rev_4.cab file contains USB drivers that are compatible with both
32-bit and 64-bit Windows systems. The drivers are unpacked the same time the
software application is loaded by double clicking the setup.exe file. The first
time the :adi:`ADISUSB` board is plugged into the computer (using the included
USB mini cable) the hardware will be recognized and loaded. The Windows
**Hardware Wizard** will find and install the drivers by following the steps
below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px

The following pictures show the final steps for the USB driver install. Click on
**Next** then click on **Finish** completing the installation.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px

.. important::

   For those who are using Windows XP, Service Pack 3, additional steps are
   required for completing the driver installation. Please see page 8, on the
   :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>`
   for additional information on these steps.

After the USB driver installation is complete, connect the :adi:`ADISUSB` USB
connector to the PC, using the USB Mini cable, from the :adi:`ADISUSB` kit. D2
will illuminate as soon as this connection is made. This indicates that the
:adi:`ADISUSB` has power and is going through its start-up/initialization
process. During the initialization process, several messages may appear on the
screen. They are related to updating the :adi:`ADISUSB` firmware and
establishing communication between the PC and the :adi:`ADISUSB`. After the
updates are finished double click on the setup.exe file to launch the software
application.

Main Window
~~~~~~~~~~~

Once the Analog Devices ADIS16135 Evaluation Software starts-up, the Main Window
will appear and look like the following picture. The second picture provides
color-coded boxes to support further discussion of each function in this screen.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-main_screen.png
   :width: 800px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-main_screen-defined.png
   :width: 800px

The orange box identifies the drop-down menus, which provide a number of useful
features. The **Devices** option provides a list of products for
:adi:`ADIS1613x <ADIS16136>` Evaluation, click on **Devices** and then select
**ADIS16133/5/6**. The green box shows the current device selection, which in
this case, identifies the :adi:`ADIS16133` as the current selection.

The **Registers** option provides a listing of user-configurable registers in
the :adi:`ADIS1613x <ADIS16136>` and also provides read/write access to each one
of these registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, real-time, after
pressing the **Read** button (see the red box for the location of the **Read**
button).

The yellow box identifies the waveform recorder window. The window contains the
gyroscope output.

Register Access
~~~~~~~~~~~~~~~

The purpose of the **Register Access** window is to provide both read and write
access to the user registers in the :adi:`ADIS1613x <ADIS16136>`. The following
picture shows the appearance of this window.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-registers.png
   :width: 600px

The color-coded boxes illustrate the different functions that this window
provides.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-registers-defined.png
   :width: 600px

The purple box identifies the register category. In addition to the
Control/Status, this drop-down control offers access to **Output** and
**Calibration** registers.

The red box identifies all of the registers that are in the current category.
Click on the register name to select a register for individual read/write
access.

The green box identifies the read/write control options for the current register
selection. Use the hexadecimal format when writing commands to a particular
register.

The yellow box updates all the registers in the current category.

The **Update Flash** command saves writable user register data.

.. tip::

   The **Register Access** screen writes to user control registers, inside of
   the :adi:`ADIS1613x <ADIS16136>`, two bytes at a time. So, when configuring a
   register, make sure to include the hexadecimal number for all 16-bits, before
   pressing the **Write Register** button. When using an embedded processor to
   write to user control registers, inside of the :adi:`ADIS1613x <ADIS16136>`,
   each command (16-bits) writes to one byte at a time.

Data Capture Menu
~~~~~~~~~~~~~~~~~

The Data Capture function supports synchronous data acquisition, based on the
data-ready signal from the :adi:`ADIS1613x <ADIS16136>`. The following picture
represents the Data Capture window, right after opening it from the **Main
Window** and the second picture provides color-coded boxes, in order to support
further discussion of each function that is associated with this screen.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-datalog.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-adisusb-datalog-defined.png
   :width: 400px

The red box identifies all of the registers that are eligible for inclusion in
the next acquisition process. Click on each box to include a register in the
next data acquisition sequence. The box will have a checkmark when it has been
selected.

The green box identifies the configuration box for the name and location of the
data storage file.

The yellow box identifies a number of configuration options for the data
acquisition process. The **Samples per File** is a user input for the total
number of samples in a data record. Note that all selected registers will have
this number of samples in the data record file, after the acquisition process
completes. After each update to the **Record Length** box, the software
calculates then displays the total **Capture Time**. The **Numeric Data Only…No
File Header** option allows the user to add or remove the header in the data
storage file. The **No Scale LSB"s Only** causes the software to convert the
decimal, twos complement number into its representative value. For example, when
enabling **No Scale LSB"s Only,** the gyroscope outputs will be in units of
degrees/second.
