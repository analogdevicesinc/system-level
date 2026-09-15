.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/gyroscopes/adis16266-eval-adis

.. _inertial-mems gyroscopes adis16266-eval-adis:

ADIS16266 EVALUATION ON THE EVAL-ADIS
=====================================

OVERVIEW
--------

The :adi:`ADIS16266` iSensor® is a high performance, digital gyroscope sensing
system that operates autonomously and requires no user configuration to produce
accurate rate sensing data. It provides performance advantages with high dynamic
range, wide bandwidth, and solid linear-acceleration rejection, which are
enabling for robotics and industrial instrumentation systems. The
:adi:`ADIS16266` uses a serial peripheral interface for data communications.
This interface enables direct connection with a large variety of embedded
processor products. This electrical connection typically only requires 5 I/O
lines for synchronous data collection, as shown in the following figure:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/figure_9_adis16266.png
   :width: 400px

ADIS16266/PCB BREAKOUT BOARD
----------------------------

For those who are on a tight timeline, connecting the :adi:`ADIS16266` to an
embedded controller will provide the most flexibility in developing application
firmware and will more closely reflect the final system design. The
:adi:`ADIS16266/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16266/products/EVAL-ADIS16266/eb.html>`
is the breakout board for the :adi:`ADIS16266` and may provide assistance in the
process of hooking it up to an existing embedded processor system. For more
information on the
:adi:`ADIS16266/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16266/products/EVAL-ADIS16266/eb.html>`
breakout boards, check out the following
:adi:`datasheet link <static/imported-files/data_sheets/ADIS16266.pdf#Page=21>`.

EVAL-ADIS: PC EVALUATION
------------------------

For those who would prefer to perform PC-based evaluation of the
:adi:`ADIS16266`, before developing their own embedded system, the
:adi:`EVAL-ADIS` is the appropriate system to use. The remainder of this Wiki
site will focus on PC-based evaluation with the :adi:`EVAL-ADIS` system.

EQUIPMENT LIST
--------------

:adi:`EVAL-ADIS`

:adi:`ADIS16266/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16266/products/EVAL-ADIS16266/eb.html>`

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7

.NET 3.5 Framework

PHYSICAL SETUP
--------------

Use the following materials to install the
:adi:`ADIS16266/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16266/products/EVAL-ADIS16266/eb.html>`
onto the :adi:`EVAL-ADIS`. Note that the ribbon cable does not currnently come
with either part number. See the following FAQ on the
:ez:`Engineer Zone <community/mems>`, for information on where to purchase one
of these.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/266-pcb-eval-adis-setup-01.jpg
   :width: 400px

The
:adi:`ADIS16266/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16266/products/EVAL-ADIS16266/eb.html>`
mounting holes will line up with the four holes on the :adi:`EVAL-ADIS`, which
have the ``A`` label on them.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/266-pcb-eval-adis-setup-02.jpg
   :width: 400px

Before starting to install, check out the following pictures, which show
**INCORRECT** examples of connecting the ribbon cable to J1 on the
:adi:`ADIS16266/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16266/products/EVAL-ADIS16266/eb.html>`

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/266-pcb-eval-adis-setup-03.jpg
   :width: 400px

**INCORRECT**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/266-pcb-eval-adis-setup-04.jpg
   :width: 400px

**INCORRECT**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/266-pcb-eval-adis-setup-05.jpg
   :width: 400px

**CORRECT**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/266-pcb-eval-adis-setup-06.jpg
   :width: 400px

You may find that it is easier to install the
:adi:`ADIS16266/PCBZ <en/mems-sensors/mems-inertial-sensors/adis16266/products/EVAL-ADIS16266/eb.html>`
on the :adi:`EVAL-ADIS`, before pressing the ribbon connector on to J1, for both
PCBs.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/266-pcb-eval-adis-setup-07.jpg
   :width: 400px

**PHYSICAL INSTALLATION COMPLETE AND CORRECT**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/gyroscopes/266-pcb-eval-adis-setup-08.jpg
   :width: 400px

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
