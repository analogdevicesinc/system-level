.. imported from: https://wiki.analog.com/resources/eval/user-guides/inertial-mems/imu/adis1648x

.. _inertial-mems imu adis1648x:

PC-WINDOWS EVALUATION OF THE ADIS1648x
======================================

OVERVIEW
--------

The ADIS1648x MEMS IMUs use a serial peripheral interface for data
communications. This interface enables direct connection with a large variety of
embedded processor products. The :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>`\ and
:adi:`\|EVAL-ADIS-FX <EVAL-ADIS-FX>` evaluation tools provide a platform for
evaluating these IMUs on PC-Windows computing platforms, through a USB port.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis16480-uc-hook-up.png
   :width: 400px

ADIS16IMU1/PCBZ BREAKOUT BOARD
------------------------------

In the PC-Windows use case, the ADIS16IMU1/PCBZ provides a bridge between the
ADIS1648x and the :adi:`ADIS16IMU1/PCBZ <EVAL-ADIS16IMU1>` evaluation platform,
using a standard IDC ribbon cable.

:dokuwiki:`ADIS16IMU1/PCB Wiki Guide <resources/eval/user-guides/inertial-mems/imu/adis16imu1-pcb>`

NOTE: :adi:`ADIS16480AMLZ <ADIS16480>`, :adi:`ADIS16485BMLZ <ADIS16485>` and
:adi:`ADIS16488AMLZ <ADIS16488>` are sold separately.

NOTE: Order (1)
:adi:`ADIS16480AMLZ <en/mems-sensors/mems-inertial-measurement-units/adis16480/products/product.html#product-samples>`
and (1)
:adi:`ADIS16IMU1/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16480/products/product.html#product-samples>`
to acquire the same materials that used to come in the ADIS16480/PCBZ, which is
no longer available.

NOTE: Order (1)
:adi:`ADIS16485AMLZ <en/mems-sensors/mems-inertial-measurement-units/adis16485/products/product.html#product-samples>`
and (1)
:adi:`ADIS16IMU1/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16485/products/product.html#product-samples>`
to acquire the same materials that used to come in the ADIS16485/PCBZ, which is
no longer available.

NOTE: Order (1)
:adi:`ADIS16488AMLZ <en/mems-sensors/mems-inertial-measurement-units/adis16488/products/product.html#product-samples>`
and (1)
:adi:`ADIS16IMU1/PCBZ <en/mems-sensors/mems-inertial-measurement-units/adis16488/products/product.html#product-samples>`
to acquire the same materials that used to come in the ADIS16488/PCBZ, which is
no longer available.

EVAL-ADIS: PC EVALUATION
------------------------

For those who would prefer to perform PC-based evaluation of the ADIS1648x
products, before developing their own embedded system, the :adi:`EVAL-ADIS` is
the appropriate system to use. The remainder of this Wiki site will focus on
PC-based evaluation with the :adi:`EVAL-ADIS` system. Here is a list of
equipment required for this:

:adi:`EVAL-ADISZ <EVAL-ADIS>`

:adi:`ADIS16488AMLZ <adis16488>`

NOTE: Substitute :adi:`ADIS16480AMLZ <adis16480>` or
:adi:`ADIS16485AMLZ <adis16485>` for the :adi:`ADIS16488AMLZ <adis16488>`, as
needed for specific application requirements.

SYSTEM REQUIREMENTS
-------------------

Windows XP, Vista, 7

.NET Framework 3.5

NOTE: Newer versions of the .NET framework do not currently support the IMU
Evaluation software package.

NOTE: The machine screws that come with the :adi:`EVAL-ADIS` can have a moderate
impact on local magnetic fields. For those who need the best performance out of
the magnetometer solution, consider replacing them with machine screws that are
made out of aluminum or other non-ferrous materials.

NOTE: The following steps represent the most convenient means of attachment, but
do not support the ``best practices`` that are listed in this application note:

:ez:`ADIS1648x Mounting Guidelines <docs/DOC-10634>`.

PHYSICAL SETUP
--------------

The :adi:`EVAL-ADIS` includes a bag of M2x0.4mm machine screws, which include 4
pieces that are in lengths of 16mm and 20mm. Using the 16mm version will only
allow for 2mm of penetration into the EVAL-ADIS mouting holes, while the 20mm
screws will result in the screws sticking out of the bottom side of the
EVAL-ADIS, when fully-secured.

NOTE: Do not plug the :adi:`EVAL-ADIS` into the USB cable at this stage of the
setup. Wait until the software installation is complete.

Step #1
~~~~~~~

Place the ADIS1648x device over the :adi:``F`` mounting holes and align its
connector with J4 on the `EVAL-ADIS <EVAL-ADIS>`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-01.jpg
   :width: 400px

Step #2
^^^^^^^

Once the alignment with J4 is correct, gently press the top of the ADIS1648xxMLZ
unit down, so that its connector presses into J4. When the connector is fully
seated, the ADIS1648xxMLZ will rest on the EVAL-ADIS surface. The following
pictures provide a reference of how this setup will look when the ADIS1648xxMLZ
has correct alignment with the mating connector on the :adi:`EVAL-ADIS`.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-02.jpg
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-02b.jpg
   :width: 400px

This picture provides an example of the an incorrect connector alignment. Take
care to avoid this type of connection error, because it can cause the the
ADIS1648xxMLZ to experience harmful conditions. Notice the entire row of gold
pins that are outside of the mating connector.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-03.jpg
   :width: 400px

Step #3
^^^^^^^

Select the mounting screws. The :adi:`EVAL-ADIS` includes a bag of M2x0.4mm
machine screws, which include 4 pieces that are in lengths of 16mm and 20mm.
Using the 16mm version will only allow for 2mm of penetration into the EVAL-ADIS
mouting holes, while the 20mm screws will result in the screws sticking out of
the bottom side of the EVAL-ADIS, when fully-secured.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-04.jpg
   :width: 400px

Step #4
^^^^^^^

Use a screwdriver to secure all four screws into the appropriate mouting holes.
Note that difficulty in getting the screws to penetrate the pre-tapped holes can
be an indicator of connector misalignment.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-05.jpg
   :width: 400px

Step #5
^^^^^^^

Set JP1 (:adi:`EVAL-ADIS`) to ``+3.3V.``

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/448-eval-adis-step5-01.jpg
   :width: 400px

Step #6
^^^^^^^

Install header to connect the two pins on JP2. Even if the application does not
require use of the RTC function, this connection is necessary to assure reliable
operation in the ADIS1648x"s processor function.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adis1648x_evaladis_install_step01-06.jpg
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

EXAMPLE EXERCISES
-----------------

Gyroscope Demonstration
~~~~~~~~~~~~~~~~~~~~~~~

:dokuwiki:`Click here to see a gyroscope demonstration, from the ADIS16448 Wiki Site </resources/eval/user-guides/inertial-mems/imu/adis16448?&#gyroscope_demonstration>`.

Accelerometer Demonstration, Static
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:dokuwiki:`Click here to see the static (gravity) accelerometer demonstration, from the ADIS16448 Wiki Site </resources/eval/user-guides/inertial-mems/imu/adis16448?&#accelerometer_demonstration_gravity>`.

Accelerometer Demonstration, Dynamic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:dokuwiki:`Click here to see the dynamic accelerometer demonstration, from the ADIS16448 Wiki Site </resources/eval/user-guides/inertial-mems/imu/adis16448?&#accelerometer_demonstration_dynamic>`.

Useful Experiments
~~~~~~~~~~~~~~~~~~

Click on the following links to access several useful experiments in ADI"s
Engineer Zone/MEMS Community.

:ez:`Gyroscope Sensitivity Measurement <docs/DOC-2181>`

:ez:`Gyroscope Noise Density <docs/DOC-2212>`

:ez:`Gyroscope In-Run Bias Stability <docs/DOC-2162>`

:ez:`Gyroscope Angle Random Walk <docs/DOC-2163>`

:ez:`ADIS16480 3-D Demonstration <docs/DOC-2223>`
