.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/imu/adis1636x

.. _inertial-mems imu adis1636x:

ADIS1636x/40x EVALUATION ON THE EVAL-ADIS
=========================================

OVERVIEW
--------

The :adi:`ADIS16362` is a high-performance IMU that uses a serial peripheral
interface for data communications. This interface enables direct connection with
a large variety of embedded processor products. This electrical connection
typically only requires 5 I/O lines for synchronous data collection, as shown in
the following figure:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16362-spi-uc2.png
   :width: 400px

This Wiki will cover all members of the ADIS1636x family: :adi:`ADIS16360`
:adi:`ADIS16362`, :adi:`ADIS16364`, :adi:`ADIS16365`, :adi:`ADIS16367`,
:adi:`ADIS16400` :adi:`ADIS16405`, :adi:`ADIS16407`.

ADIS1636x/PCB & ADIS1640x/PCBZ BREAKOUT BOARDS
----------------------------------------------

For those who are on a tight timeline, connecting the ADIS1636xBMLZ or
ADIS1640xBMLZ to an embedded controller will provide the most flexibility in
developing application firmware and will more closely reflect the final system
design. For example, the
:adi:`ADIS16362/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16362/products/EVAL-ADIS16362/eb.html>`
is the breakout board for the :adi:`ADIS16362` and may provide assistance in the
process of hooking it up to an existing embedded processor system. Also see the
following breakout board pages:

:adi:`ADIS16360/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16360/products/EVAL-ADIS16360/eb.html>`

:adi:`ADIS16362/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16362/products/EVAL-ADIS16362/eb.html>`

:adi:`ADIS16364/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16364/products/EVAL-ADIS16364/eb.html>`

:adi:`ADIS16365/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16365/products/EVAL-ADIS16365/eb.html>`

:adi:`ADIS16367/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16367/products/EVAL-ADIS16367/eb.html>`

:adi:`ADIS16400/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16400/products/EVAL-ADIS16400/eb.html>`

:adi:`ADIS16405/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16405/products/EVAL-ADIS16405/eb.html>`

:adi:`ADIS16407/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16407/products/EVAL-ADIS16407/eb.html>`

ADIS16IMU1/PCBZ BREAKOUT BOARD
------------------------------

The interface board that comes with ADIS1636x/PCBZ or ADIS1640x/PCBZ orders has
two 12-pin connectors: J1 contains the power, ground and SPI signals while J2
contains the DIOx pins (including data-ready). The ADIS16IMU1/PCBZ provides
access to all of these functions through one 16-pin connector, which simplifies
cabling requirements. Click on the following link for more information on the
ADIS16IMU1/PCBZ:

:dokuwiki:`ADIS16IMU1/PCB Wiki Guide <resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb>`

In addition to offering the convenience of one 16-pin connector, the
ADIS16IMU1/PCBZ also offers M2x0.4mm tapped holes and machine screws to attach
any ADIS1636xBMLZ or ADIS1640xBMLZ product to it.

NOTE: Order :adi:`ADIS16360BMLZ <ADIS16360>`, :adi:`ADIS16362BMLZ <ADIS16362>`,
:adi:`ADIS16364BMLZ <ADIS16364>`, :adi:`ADIS16365BMLZ <ADIS16365>`,
:adi:`ADIS16367BMLZ <ADIS16367>`, :adi:`ADIS16400BMLZ <ADIS16400>`,
:adi:`ADIS16405BMLZ <ADIS16405>` or :adi:`ADIS16407BMLZ <ADIS16407>` separately,
as they are not included with the ADIS16IMU1/PCBZ.

EVAL-ADIS: PC EVALUATION
------------------------

For those who would prefer to perform PC-based evaluation of the ADIS1636x or
ADIS1640x products, before developing their own embedded system, the
:adi:`EVAL-ADIS` is the appropriate system to use. The remainder of this Wiki
site will focus on PC-based evaluation with the :adi:`EVAL-ADIS` system. Here is
a list of equipment required for this:

:adi:`EVAL-ADISZ <EVAL-ADIS>`

:adi:`ADIS16362BMLZ <adis16362>`

NOTE: Substitute :adi:`ADIS16360BMLZ <adis16360>`,
:adi:`ADIS16364BMLZ <adis16364>`, :adi:`ADIS16365BMLZ <adis16365>`,
:adi:`ADIS16367BMLZ <adis16367>`, :adi:`ADIS16400BMLZ <adis16400>`,
:adi:`ADIS16405BMLZ <adis16405>` or :adi:`ADIS16407BMLZ <adis16407>` for the
:adi:`ADIS16362BMLZ <adis16362>`, as needed for specific application
requirements.

EQUIPMENT LIST
--------------

:adi:`EVAL-ADIS`

:adi:`ADIS16362BMLZ <adis16362>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7

.NET Framework 3.5

NOTE: Newer versions of the .NET framework do not currently support the IMU
Evaluation software package.

PHYSICAL SETUP
--------------

The
:adi:`ADIS16362/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16362/products/EVAL-ADIS16362/eb.html>`
includes one interface PCB, which requires two M2 or 2-56 machine screws to
secure the baseplate to the system printed circuit board. The :adi:`ADIS16362`
product family is approximately 22 mm × 32 mm × 24 mm and provides a flexible
connector interface that enables multiple mounting orientation options. Set the
interface PCB aside, as it is not used for connecting the :adi:`ADIS16362` to
the :adi:`EVAL-ADIS`.

NOTE: The machine screws that come with the :adi:`EVAL-ADIS` can have a moderate
impact on local magnetic fields. For those who need the best performance out of
the magnetometer solution, consider replacing them with machine screws that are
made out of aluminum or other non-ferrous materials.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/36x-part-dimensions.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16364bmlz.png
   :width: 400px

NOTE: Do not plug the :adi:`EVAL-ADIS` into the USB cable at this stage of the
setup. Wait until the software installation is complete.

Step #1
~~~~~~~

The :adi:`ADIS16362` installs directly into the J4 connector of the
:adi:`EVAL-ADIS` The **B-holes** on the :adi:`EVAL-ADIS`, are used for
:adi:`ADIS16362` mounting and marked in the picture below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-36x-mounting-locates.png
   :width: 600px

WARNING: Make sure that the connector is in proper alignment before pressing it
in. Misalignment can cause pin damage and exposure to harmful conditions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-36x-mounted-parts.png
   :width: 400px

Step #2
^^^^^^^

The :adi:`ADIS16362` installation, is a simple two-step process:

1. Secure the baseplate using 2 M2 x 0.4mm x 6mm machine screws and the
   **B-holes** on the :adi:`EVAL-ADIS`.

2. Press the connector into its mate.

For removal, 1. Gently pry the connector from its mate using a small slot

screwdriver. 2. Remove the screws and lift the part up.

**Never** attempt to unplug the connector by pulling on the plastic case or
baseplate. Although the flexible connector is very reliable in normal operation,
it can break when subjected to unreasonable handling. When broken, the flexible
connector cannot be repaired.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-364-all-parts.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/364-mounted-eval-adis.png
   :width: 400px

Step #3
^^^^^^^

The following picture shows JP1 in the **+5V** position required for the
:adi:`ADIS16362` product family sensors. **Note** the JP1 jumper
(factory-default) setting on the :adi:`EVAL-ADIS` is **+3.3V**. The power
management system provides jumper selection for three device under test (DUT)
power options: 5 V (USB), 3.3 V, and an external power option. The 5 V option
provides access to the USB"s 5 V supply voltage for the DUT, and the 3.3 V
option uses a linear regulator, 400 μF of bulk capacitance, and a soft start
circuit to manage transient currents on the USB port.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-voltage-5v.png
   :width: 500px

NOTE: If JP1 is left on **+3.3V**, all outputs may not respond and will appear
to be saturated in one direction or the other. See the following picture for an
example of this behavior.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adis-imu-36x-voltage-error.png
   :width: 800px

IMU EVALUATION SOFTWARE OVERVIEW
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/imu-evaluation-software.rst

   :start-after: .. start-imu-evaluation-software-overview
   :end-before: .. end-imu-evaluation-software-overview

USB Driver Installation
~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/imu-evaluation-software.rst

   :start-after: .. start-usb-driver-installation
   :end-before: .. end-usb-driver-installation

IMU EVALUATION SOFTWARE GETTING STARTED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/imu-evaluation-software.rst

   :start-after: .. start-imu-evaluation-software-starting-point
   :end-before: .. end-imu-evaluation-software-starting-point

IMU EVALUATION SOFTWARE REVISION HISTORY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/imu-evaluation-software.rst

   :start-after: .. start-software-revision-history
   :end-before: .. end-software-revision-history

EXAMPLE EXERCISES
~~~~~~~~~~~~~~~~~

This section currently has no :adi:`ADIS16362`-specific content, but the
:dokuwiki:`ADIS16448 Evaluation on the EVAL-ADIS Wiki Site </resources/eval/user-guides/inertial-mems/imu/adis16448?&#example_evaluation_exercises>`
has some good examples to start with.
