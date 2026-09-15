.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/imu/adis16375-adisusb

.. _inertial-mems imu adis16375-adisusb:

ADIS16375 EVALUATION ON THE ADISUSB
===================================

OVERVIEW
--------

The :adi:`ADIS16375` iSensor® is a complete inertial system that includes a
triaxis gyroscope and triaxis accelerometer. Each sensor in the :adi:`ADIS16375`
combines industry-leading iMEMS® technology with signal conditioning that
optimizes dynamic performance. The factory calibration characterizes each sensor
for sensitivity, bias, alignment, and linear acceleration (gyro bias). As a
result, each sensor has its own dynamic compensation formulas that provide
accurate sensor measurements over a temperature range of −40°C to +105°C.

The :adi:`ADIS16375` provides a simple, cost-effective method for integrating
accurate, multiaxis, inertial sensing into industrial systems, especially when
compared with the complexity and investment associated with discrete designs.
All necessary motion testing and calibration are part of the production process
at the factory, greatly reducing system integration time. The SPI port typically
connects to a compatible port on an embedded processor, using the connection
diagram below. The four SPI signals facilitate synchronous, serial data
communication. Connect RST to a digital I/O line for remote reset control or
leave it open for normal operation. The factory default configuration provides
users with a data-ready signal on the DIO2 pin, which pulses high when new data
is available in the output data registers.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-spi-conn.png
   :width: 500px

ADIS16375/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16375` to an
embedded controller will provide the most flexibility in developing application
firmware and will more closely reflect the final system design. The
:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`
is the breakout board for the :adi:`ADIS16375` and may provide assistance in the
process of hooking it up to an existing embedded processor system.

ADISUSB: PC EVALUATION
----------------------

For those who would prefer to perform PC-based evaluation of the
:adi:`ADIS16375`, before developing their own embedded system, the
:adi:`ADISUSB` is the appropriate system to use. The remainder of this Wiki site
will focus on PC-based evaluation with the :adi:`ADISUSB` system.

EQUIPMENT LIST
--------------

:adi:`ADISUSB`

:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7 (32-bit systems only)

NOTE: All the required files are contained in the .Cab file and deployed during
software package install.

PHYSICAL SETUP
--------------

The
:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`
includes one interface PCB, 4 M2x.4x18mm machine screws and one
:adi:`ADIS16375AMLZ <ADIS16375>` unit. The :adi:`ADIS16375` is approximately 44
mm × 47 mm × 14 mm and provides a flexible connector interface that enables
multiple mounting orientation options. Set the interface PCB aside, as it is not
used for connecting the :adi:`ADIS16375AMLZ <ADIS16375>` to the :adi:`ADISUSB`.

NOTE: Do not plug the :adi:`ADISUSB` into the USB cable at this stage of the
setup. Wait until the software installation is complete.

Step #1
~~~~~~~

The :adi:`ADIS16375AMLZ <ADIS16375>` installs directly into the J4 connector of
the :adi:`ADISUSB`. The following pictures provide a visual reference for
correct connection. Mounting to the system frame is accomplished by Drilling and
tapping for M2 (drill size #52 1.6mm) or 2-56 (drill size #50 .070) holes in the
:adi:`ADISUSB`, according to the locations in the physical mounting diagram. The
tap is the best way but an M2x0.4 machine screw can be used for tapping the PCB
material. The :adi:`ADIS16375AMLZ <ADIS16375>` is secured using the M2x0.4x18mm
machine screws included with the
:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`.
The mounting location holes are shown in the picture below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-connector-pinout.png
   :width: 300px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-hole-mnt-dimension.png
   :width: 300px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-hole-mnt-location.png
   :width: 500px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-mnounted-adisusb.png
   :width: 500px

WARNING: Make sure that the connector is in proper alignment before pressing it
in. Misalignment can cause pin damage and exposure to harmful conditions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-correct-j4-connection.png
   :width: 600px

Step #2
~~~~~~~

The remote mounting option
:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`
includes one :adi:`ADIS16375AMLZ <ADIS16375>`, one interface printed circuit
board (PCB), and four M2 × 0.4 x 18mm machine screws. The interface PCB provides
larger connectors than the :adi:`ADIS16375AMLZ <ADIS16375>` for simpler
prototyping, four-tapped M2 holes for attachment of the
:adi:`ADIS16375AMLZ <ADIS16375>`, and four holes (machine screw size M2.5 or #4)
for mounting the :adi:`ADIS16375AMLZ <ADIS16375>` to a solid structure. J1 is a
dual-row, 2 mm (pitch) connector that mates to a number of ribbon cable systems,
including 3M Part Number 152212-0100-GB (ribbon crimp connector) and 3M Part
Number 3625/12 (ribbon cable). Note that J1 has 16 pads; however, some legacy
boards use only Pin 1 through Pin 12.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-pcbz-dimensions.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-mounted-on-pcbz-brd.png
   :width: 400px

Step #3
~~~~~~~

Secure the :adi:`ADIS16375AMLZ <ADIS16375>` body, to the
:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`
using (4) M2x0.4x18mm machine screws (included with
:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`).
The suggested torque setting for the attachment hardware is 40 inch-ounces, or
0.2825 N-m.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-adisusb-16375pcbz.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-adisusb-16375pcbz2.png
   :width: 400px

Step #4
~~~~~~~

Connect J1 on the :adi:`ADISUSB` to J1 on the
:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`.
Note that J1 (:adi:`ADISUSB`) has 12 pins and J1
(:adi:`ADIS16375/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16375/products/EVAL-ADIS16375/eb.html>`)
has 16 pins. The four DIO pins are left un-connected using the 12 pin connector
which allows easy access and shown in the pictures below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-adisusb-16375pcbz3.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-adisusb-16375pcbz4.png
   :width: 400px

Step #5
~~~~~~~

The following picture (left side) shows JP1 in the **+3.3V** position
(factory-default). If this is different, change the JP1 jumper setting on the
:adi:`ADISUSB` to the **+3.3V** position and shown in the following picture:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-3.3v-setting.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-5v-markedsetting.png
   :width: 400px

ADIS16375 Evaluation SOFTWARE
-----------------------------

:adi:`Click here to download the ADIS16375 Evaluation Software <static/imported-files/eval_boards/375ES3.zip>`
to a personal computer, which enables PC-based evaluation of the
:adi:`ADIS16375` on an :adi:`ADISUSB` evaluation system. The download file will
contain five separate files: The CAB file (ADIS16375_Rev_3.cab), the setup file
(setup.exe), 375ES(3).zip, support and the setup list. Copy these files to a
convenient folder for running the application from.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-zip-download-file.png
   :width: 600px

Navigate to the folder where the files were saved and double click the setup.exe
file. The following pictures are a guide for the ADIS16375 Evaluation Software
install. The **Welcome** screen will appear click **OK** to continue.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-welcome.png
   :width: 600px

Please choose a directory for the software application or use the default
settings (recommended) and click the computer icon button to go to the next
step.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-install.png
   :width: 600px

Choose a program group or use the default settings (recommended) and click
**Continue**. The last picture confirms completion click **OK** to finish.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-prgrm-group.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-finish.png
   :width: 400px

USB Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~

The ADIS16375_Rev_3.cab file contains USB drivers that are compatible with both
32-bit and 64-bit Windows systems. The drivers are unpacked the same time the
software application is loaded by double clicking the setup.exe file. The first
time the :adi:`ADISUSB` board is plugged into the computer (using the included
USB mini cable) the hardware is recognized and loaded. The computer **Hardware
Wizard** will find and install the drivers by following the steps below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-foundnewhardware.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-install.png
   :width: 400px

The following pictures show the final steps for USB driver install. Click on
**Next** then click on **Finish** completing the installation.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-hardware-wizard.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adisusb-driver-complete-wizard.png
   :width: 400px

.. note::

   For those who are using Windows XP, Service Pack 3, additional steps are
   required for completing the driver installation. Please see page 8, on the
   :adi:`ADISUSB User Guide (UG-363) <static/imported-files/user_guides/UG-363.pdf#Page=08>`
   for additional information on these steps.

Main Window
~~~~~~~~~~~

Once the :adi:`ADIS16375` Evaluation Software starts-up, the Main Window will
appear and look like the following picture. The second picture provides
color-coded boxes to support further discussion of each function in this screen.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-adisusb-main-screen-software.png
   :width: 800px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-adisusb-main-screen-defined.png
   :width: 800px

The orange box identifies the drop-down menus, which provide a number of useful
features.

The **Registers** option provides a listing of user-configurable registers in
the :adi:`ADIS16375` and also provides read/write access to each one of these
registers.

The **Datalog** option provides the core data collection function.

The purple box identifies the output registers, which update, real-time, after
pressing the **Read** button (see the red box for the location of the **Read**
button).

The yellow box identifies the two waveform recorder windows. The top window
contains the three gyroscope outputs. The bottom window contains the three
accelerometer responses. Also, each waveform matches the color of its register
(see register titles in the purple box).

Register Access
~~~~~~~~~~~~~~~

The purpose of the **Register Access** window is to provide both read and write
access to the user registers in the :adi:`ADIS16375`. The following picture
shows the appearance of this window.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-334-reg.png
   :width: 600px

The color coded boxes illustrate the different functions that this window
provides.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/imu_6dof-334-reg-defined.png
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

APPLICATION TIP: The **Register Access** screen writes to user control
registers, inside of the :adi:`ADIS16375`, two bytes at a time. So, when
configuring a register, make sure to include the hexadecimal number for all
16-bits, before pressing the **Write Register** button. When using an embedded
processor to write to user control registers, inside of the :adi:`ADIS16375`,
each command (16-bits) writes to one byte at a time.

Data Capture Menu
~~~~~~~~~~~~~~~~~

The Data Capture function supports synchronous data acquisition, based on the
data-ready signal from the :adi:`ADIS16375`. The following picture represents
the Data Capture window, right after opening it from the **Main Window** and the
second picture provides color-coded boxes, in order to support further
discussion of each function that is associated with this screen.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-adisusb-datalog.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/375-adisusb-datalog-defined.png
   :width: 400px

The red box identifies all of the registers that are eligible for inclusion in
the next acquisition process. Click on each box to include a register in the
next data acquisition sequence. The box will have a check mark when it has been
selected.

The green box identifies the configuration box for the name and location of the
data storage file.

The yellow boxes identify a number of configuration options for the data
acquisition process. The **Samples per File** is a user input for the total
number of samples in a data record. Note that all selected registers will have
this number of samples in the data record file, after the acquisition process
completes. After each update to the **Record Length** box, the software
calculates and displays the total **Capture Time**. The **Numeric Data only..No
File header** option allows the user to add or remove the header in the data
storage file. The **No Scale LSB"s Only** causes the software to convert the
decimal, twos complement number into its representative value. For example, when
enabling **No Scale LSB"s Only,** the gyroscope outputs will be in units of
degrees/second.

EXAMPLE EXERCISES
~~~~~~~~~~~~~~~~~

This section currently has no :adi:`ADIS16375`-specific content, but the
:dokuwiki:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site </resources/eval/user-guides/inertial-mems/imu/adis16448?&#example_evaluation_exercises>`
has some good examples to start with.
