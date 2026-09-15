.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/eval-adisimu1-rpiz

.. _circuits-from-the-lab eval-adisimu1-rpiz:

EVAL-ADISIMU1-RPIZ Hardware User Guide
======================================

OVERVIEW
--------

The :adi:`EVAL-ADISIMU1-RPIZ` allows multiple compatible IMU components (with
the ADIS16IMU1/PCBZ and ADIS16IMU4/PCBZ breakout boards connector) to be
connected to the Raspberry Pi. The following table outlines which IMU components
can be directly mounted with the EVAL-ADISIMU1-RPIZ board

.. list-table::
   :header-rows: 1

   * - IMU Part Number
     - ADISIMU1 Connector
     - Mounting Location
     - Breakout Board Connector
   * - :adi:`ADIS16362`
     - P2
     - Mounting Slot B
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16364`
     - P2
     - Mounting Slot B
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16365`
     - P2
     - Mounting Slot B
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16135`
     - P2
     - Mounting Slot C
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16136`
     - P2
     - Mounting Slot C
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16137`
     - P2
     - Mounting Slot C
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16375`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16480`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16485`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16488A`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16489`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16490`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16495`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16497`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16545`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16547`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16550`
     - P2
     - Mounting Slot F
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16467`
     - P7
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16460`
     - P7
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16465`
     - P7
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16470`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16475`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16477`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16500`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16501`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16505`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16507`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16575`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16576`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ
   * - :adi:`ADIS16577`
     - P3
     - Mounting Slot I
     - ADIS16IMU4/PCBZ

.. list-table::
   :header-rows: 1

   * - IMU Part Number
     - Status
     - ADISIMU1 Connector
     - Mounting Location
     - Breakout Board Connector
   * - :adi:`ADIS16360`
     - Obsolete
     - P2
     - Mounting Slot B
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16400`
     - Obsolete
     - P2
     - Mounting Slot B
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16407`
     - Obsolete
     - P2
     - Mounting Slot B
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16367`
     - Obsolete
     - P2
     - Mounting Slot B
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16405`
     - Obsolete
     - P2
     - Mounting Slot B
     - ADIS16IMU1/PCBZ
   * - :adi:`ADIS16133`
     - Obsolete
     - P2
     - Mounting Slot C
     - ADIS16IMU1/PCBZ

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/top_perspective.png
   :width: 500px

Videos
------

Unboxing and Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following video is a walkthrough for the unboxing experience and a guide for
setting up the hardware to be ready for your own application development.

.. video:: https://www.youtube.com/watch?v=vesoMeTnPW8

.. video:: https://www.youtube.com/watch?v=G-k81W2yJRY

Inertial Measurement Unit(IMU)/Gyroscope Mounting
-------------------------------------------------

There are two ways you can mount components on the EVAL-ADISIMU1-RPIZ.

#. Directly mount the IMU using the proper mounting location
#. Indirect connection using the P3 connector along with the ribbon cable and
   the breakout board

Any IMU can use the indirect method of connecting to the P3 header using the
ribbon cable and it"s corresponding breakout board. So the following sections
are going to describe how to directly mount the compatible IMUs to the
EVAL-ADISIMU1-RPIZ. Please see the pictures for device mounting hole locations.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/mounting.png
   :width: 600px

.. tip::

   There are four(4) mounting holes without any labels. These mounting holes are
   assigned to mount the EVAL-ADISIMU1-RPIZ to the Raspberry Pi host board.
   There are four(4) nylon screws and spacers provided in the kit, and these
   should be used for this purpose. The nominal diameter of the four(4) holes is
   3.175mm.

.. note::

   **MACHINE SCREWS IMPACT LOCAL MAGNETIC FIELDS** The machine screws in the
   EVAL-ADISIMU1-RPIZ kit are made out of stainless steel, which can have some
   moderate impact on magnetic fields, local to the IMU. For those whose
   application demands the best magnetometer performance offered by these IMUs,
   consider using plastic screws that will not impact the magnetic fields around
   the devices.

P2 Connection
-------------

Mounting Slot B
~~~~~~~~~~~~~~~

IMU Components

- ADIS16360
- ADIS16362
- ADIS16364
- ADIS16365
- ADIS16367
- ADIS16400
- ADIS16405
- ADIS16407

Mounting Materials

- (2) M2 x 0.4 x 4mm machine screws

  - For high-vibration environments, consider using more than 2 screws.
    :adi:`Application Note AN-1045 <static/imported-files/application_notes/AN-1045.pdf>`
    offers some ideas on using more than two screws to attach this package style
    to a system frame.

- (2) M2 Hex nuts

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/mounting_b.png
   :width: 600px

The image below shows the proper mounting of IMU"s on Mounting Slot B.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/mounting_b.jpg
   :width: 450px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/20201216_202707.jpg
   :width: 332px

Mounting Slot C
~~~~~~~~~~~~~~~

IMU Components

- ADIS16133
- ADIS16135
- ADIS16136
- ADIS16137

Mounting Materials

- (4) M2 x 0.4 x 16mm machine screws
- (4) M2 Hex nuts

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/mounting_c.png
   :width: 600px

Below is an example of proper mounting of IMU"s on mounting hole C

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/adis_mounting_c.jpg
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/20201216_202543.jpg
   :width: 420px

Mounting Slot F
~~~~~~~~~~~~~~~

IMU Components

- ADIS16375
- ADIS16480
- ADIS16485
- ADIS16488A
- ADIS16489
- ADIS16490
- ADIS16495
- ADIS16497
- ADIS16545
- ADIS16547
- ADIS16550

Mounting Materials

- (4) M2 x 0.4 x 16mm machine screws
- (4) M2 Hex nuts

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/mounting_f.png
   :width: 600px

Below is an image that show proper mounting of IMU"s on mounting slot F.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/mounting_f.jpg
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/hole_f.jpg
   :width: 460px

P7 Connection
-------------

IMU Components:

- ADIS16467
- ADIS16460
- ADIS16465

Mounting Materials

- (3) M2 x 0.4 x 16mm machine screws
- (3) M2 Hex nuts

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/mounting_i.png
   :width: 600px

Below is an image that show proper mounting of IMU"s on mounting slot I. Ensure
that the machine screws are tightened on the bottom side of the board using the
hex nuts as shown below:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/mounting_i.jpg
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/20201211_212825.jpg
   :width: 425px

Raspberry Pi Connector
----------------------

The 40 pin Raspberry Pi connector of the EVAL-ADISIMU1-RPIZ mounts directly on
top of the Raspberry Pi 4, or equivalents, 40 pin male headers.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/dsc09075.png

Headers and Jumpers
-------------------

Real Time Clock
~~~~~~~~~~~~~~~

Placing a shunt on this connector P1 provides power to the Real Time Clock (RTC)
of the IMU"s attached to connector P2

Power
~~~~~

The board has a selectable power between +5V or +3.3V from the RPI. The default power supply is +3.3V unless otherwise stated in the datasheet of the IMU. The power to the IMU can be selected using connector P5. .. note::

   It"s critical to know the power supply required for the IMU you are using before changing this setting. If you power any IMU from 5V that was designed for 3.3V power, you will destroy the IMU and it will no longer function. This is a **VERY EXPENSIVE** mistake.

.. list-table::
   :header-rows: 1

   * - Power
     - Shunt Position
   * - +5.0V
     - Pin 1 and Pin 2
   * - +3.3V
     - Pin 2 and Pin 3 *(Default Position)*

Sync Selector
~~~~~~~~~~~~~

Sync Header
^^^^^^^^^^^

Header P6 allows for selectable sync signal to be used by the IMU"s. It can be
done by moving the shunt to select the source, either via RPI or an external
source.

.. list-table::
   :header-rows: 1

   * - Sync
     - Shunt Position
   * - RPI
     - Pin 1 and Pin 2 *(Default Position)*
   * - Ext
     - Pin 3 and Pin 4

Ext Sync Pads
^^^^^^^^^^^^^

This allows for an external sync signal to be used in the system by installing
an SMA connector on pads of connector J1.

Test Points
~~~~~~~~~~~

+5V
^^^

This test point provides connection to the +5V rail.

+3.3V
^^^^^

This test point provides connection to the +3.3V rail.

GND
^^^

This test point provides connection to the ground.

DAC
^^^

This test point provides connection to the output of the DAC.

ADC
^^^

This test point provides connection to the output of the ADC.

Schematic, PCB Layout Files, Bill of Materials
----------------------------------------------

.. admonition:: Download

   EVAL-ADISIMU1-RPIZ Design & Integration Files

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/02_059367b_top.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/05-059367-01-b.xlsx`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/adismu1/08_059367b.pdf`

*End of Document*
