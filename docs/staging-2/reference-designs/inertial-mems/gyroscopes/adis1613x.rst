.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/gyroscopes/adis1613x

.. _inertial-mems gyroscopes adis1613x:

ADIS1613x EVALUATION ON THE EVAL-ADIS
=====================================

OVERVIEW
========

The ADIS1613x MEMS gyroscope family the following products:
:adi:`ADIS16133BMLZ <ADIS16133>`, :adi:`ADIS16135 <ADIS16135BMLZ>`,
:adi:`ADIS16136AMLZ <ADIS16136>` and :adi:`ADIS16137BMLZ <ADIS16137>`. All of
these products provide low-profile, high-peformance MEMS gyroscopes that use a
serial peripheral interface for data communications. This interface enables
direct connection with a large variety of embedded processor products. The pin
assignments for the :adi:`ADIS16133` and :adi:`ADIS16135` are identical. The
:adi:`ADIS16136` and :adi:`ADIS16137 <ADIS16136>` provides four configurable I/O
lines, while the other two products only provide one configurable I/O line,
along with a dedidated clock input line (optional). Since these products use a
serial peripheral interface (SPI) for it data communications interface, it
connects directly to many embedded procoesor platforms, such as the
:adi:`Blackfin DSP <blackfin>` series. For a generic example of this type of
connection, click on the following reference:

- :adi:`ADIS16136 Datasheet, Figure 10 <static/imported-files/data_sheets/ADIS16136.pdf#Page=08>`

ADIS16IMU1/PCBZ BREAKOUT BOARD
==============================

The ADIS16IMU1/PCBZ provides a simple method for connecting an existing
processor system to the :adi:`ADIS16133BMLZ <ADIS16133>`,
:adi:`ADIS16135BMLZ <ADIS16135>` :adi:`ADIS16136AMLZ <ADIS16136>` or
:adi:`ADIS16137BMLZ <ADIS16137>`, using 1mm ribbon cables. Click on one of the
following link for more information on this breakout boards.

:dokuwiki:`ADIS16IMU1/PCB Wiki Guide <resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb>`

NOTE: :adi:`ADIS16133BMLZ <ADIS16133>`, :adi:`ADIS16135BMLZ <ADIS16135>`,
:adi:`ADIS16136AMLZ <ADIS16136>` and :adi:`ADIS16137BMLZ <ADIS16137>` are sold
separately.

EVAL-ADIS: PC EVALUATION
========================

For those who would prefer to perform PC-based evaluation of the ADIS1613x
products, before developing their own embedded system, the :adi:`EVAL-ADIS` is
the appropriate system to use. The remainder of this Wiki site will focus on
PC-based evaluation with the :adi:`EVAL-ADIS` system. Here is a list of
equipment required for this:

:adi:`EVAL-ADISZ <EVAL-ADIS>`

:adi:`ADIS16136AMLZ <adis16136>`

NOTE: Substitute :adi:`ADIS16133BMLZ <adis16133>`,
:adi:`ADIS16135BMLZ <adis16135>` or :adi:`ADIS16137BMLZ <ADIS16137>` for the
:adi:`ADIS16136AMLZ <adis16136>`, as needed for specific application
requirements.

SYSTEM REQUIREMENTS
===================

Windows XP, Vista, 7

.NET Framework 3.5

NOTE: Newer versions of the .NET framework do not currently support the IMU
Evaluation software package.

PHYSICAL SETUP
==============

The :adi:`EVAL-ADIS` includes a bag of M2x0.4mm machine screws, which include 4
pieces that are in lengths of 16mm and 20mm. Using the 16mm version will only
allow for 2mm of penetration into the EVAL-ADIS mouting holes, while the 20mm
screws will result in the screws sticking out of the bottom side of the
EVAL-ADIS, when fully-secured.

NOTE: Do not plug the :adi:`EVAL-ADIS` into the USB cable at this stage of the
setup. Wait until the software installation is complete.

NOTE: The following pictures show the ADIS16488, not the ADIS1613x. The
procedure will be the same, but when properly seated in the mating connector,
the ADIS1613x devices will line up with different mounting holes.

Step #1
-------

Place the ADIS1613x device over the :adi:``C`` mounting holes and align its
connector with J4 on the `EVAL-ADIS <EVAL-ADIS>`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-01.jpg
   :width: 400px

Step #2
~~~~~~~

Once the alignment with J4 is correct, gently press the top of the ADIS1613xxMLZ
unit down, so that its connector presses into J4. When the connector is fully
seated, the ADIS1613xxMLZ will rest on the EVAL-ADIS surface. The following
pictures provide a reference of how this setup will look when the ADIS1613xxMLZ
has correct alignment with the mating connector on the :adi:`EVAL-ADIS`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-02.jpg
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-02b.jpg
   :width: 400px

This picture provides an example of the an incorrect connector alignment. Take
care to avoid this type of connection error, because it can cause the the
ADIS1613xxMLZ to experience harmful conditions. Notice the entire row of gold
pins that are outside of the mating connector.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-03.jpg
   :width: 400px

Step #3
~~~~~~~

Select the mounting screws. The :adi:`EVAL-ADIS` includes a bag of M2x0.4mm
machine screws, which include 4 pieces that are in lengths of 16mm and 20mm.
Using the 16mm version will only allow for 2mm of penetration into the EVAL-ADIS
mouting holes, while the 20mm screws will result in the screws sticking out of
the bottom side of the EVAL-ADIS, when fully-secured.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-04.jpg
   :width: 400px

Step #4
~~~~~~~

Use a screwdriver to secure all four screws into the appropriate mouting holes.
Note that difficulty in getting the screws to penetrate the pre-tapped holes can
be an indicator of connector misalignment.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-05.jpg
   :width: 400px

Step #5
~~~~~~~

Set JP1 (:adi:`EVAL-ADIS`) to ``+5V.``

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/13x-eval-adis-jp1.png
   :width: 400px

IMU EVALUATION SOFTWARE OVERVIEW
--------------------------------

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/imu-evaluation-software.rst

   :start-after: .. start-imu-evaluation-software-overview
   :end-before: .. end-imu-evaluation-software-overview

USB Driver Installation
-----------------------

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/imu-evaluation-software.rst

   :start-after: .. start-usb-driver-installation
   :end-before: .. end-usb-driver-installation

IMU EVALUATION SOFTWARE GETTING STARTED
---------------------------------------

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/imu-evaluation-software.rst

   :start-after: .. start-imu-evaluation-software-starting-point
   :end-before: .. end-imu-evaluation-software-starting-point

IMU EVALUATION SOFTWARE REVISION HISTORY
----------------------------------------

.. todo:: .. include: /resources/eval/user-guides/inertial-mems/imu/imu-evaluation-software.rst

   :start-after: .. start-software-revision-history
   :end-before: .. end-software-revision-history

APPLICATION TIP: The **Register Acess** screen writes to user control registers,
inside of the ADIS1613x devices, two bytes at a time. So, when configuring a
register, make sure to include the hexadecimal number for all 16-bits, before
pressing the **Write Register** button. When using an embedded processor to
write to user control registers, inside of the ADIS1613x devices, each command
(16-bits) writes to one byte at a time.
