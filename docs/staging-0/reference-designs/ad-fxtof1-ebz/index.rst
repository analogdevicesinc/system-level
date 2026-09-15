.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fxtof1-ebz

.. _ad-fxtof1-ebz:

AD-FXTOF1-EBZ
=============

.. important::

   This system has reached its end of life and has a last time buy status.

Introduction
------------

The
:adi:`AD-FXTOF1-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-FXTOF1-EBZ.html>`
is a proven hardware platform for depth perception. When paired with a processor
board from the Raspberry Pi or Nvidia family, it can be used for 3D software and
algorithm development. The solution has VGA resolution which means that objects
can be detected to a higher level of granularity than other 3D ToF solutions, an
ability to detect depth in strong ambient light conditions and multiple range
detection modes for increased accuracy. A native and host SDK is provided. The
SDK also provides OpenCV, Python®, MATLAB®, Open3D and RoS wrappers so that
developers can use them to simplify application development.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fxtof1.png
   :width: 200px

.. list-table::
   :header-rows: 1

   * - Development kit contents
   * - ToF module
   * - Interposer board
   * - 25 pins flex cable
   * - 15 pins flex cable
   * - Screws and standoffs to attach the interposer board to the ToF module
   * - USB cable to supply 5V to the system

.. list-table::
   :header-rows: 1

   * - High level specification
     -
     -
   * - **Range**
     - Near: 25cm to 80cm
     -
   * -
     - Medium: 30cm to 300cm
     -
   * - **Accuracy**
     - < 2% for all ranges
     -
   * - **Frame Rate**
     - 30fps (depends on processor board, OS and interface to host computer)
     -
   * - **Resolution**
     - 640 x 480 pixels
     -
   * - **Operating Temperature**
     - -20⁰C to 75⁰C
     -
   * - **Laser optics**
     - 940nm VCSEL with 87⁰ x 67⁰ batwing profile diffuser
     -
   * - **Receive lens**
     - FoV 87⁰ x 67⁰ including 940nm BPF, F=1.2
     -
   * - **Power input**
     - 5V @ 2A
     -
   * - **Interface**
     - 25 pins flex cable
     -
   * - **Block diagram**
     -

      .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/fxtof1_block_diagram.png
         :width: 350px

     -

.. admonition:: Download

   **ToF module resources:**

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-fxtof1-ebz_mechanical_drawing.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/tofcam.zip`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-fxtof1-ebz_high_level_bom.xlsx`

.. admonition:: Download

   **Interposer board resources:**

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/02-066110-01-a.pdf`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/09-066110-01a.zip`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/05-066110-01-a.zip`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/20-066110-01a.zip`

.. note::

   For more information and how to buy the system please visit the
   :adi:`AD-FXTOF1-EBZ Product page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-fxtof1-ebz.html>`

.. note::

   For an example of how to integrate the AD-FXTOF1-EBZ in a camera please visit
   the
   :adi:`AD-3DSMARTCAM1-PRZ Product page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-smartcam1-prz.html>`

--------------

System setup & evaluation
-------------------------

The development kit can be connected to a number of processor boards for system
evaluation and computer vision applications development. The evaluation software
for the supported embedded platforms can be accessed by following the
instructions in the **Application Development** section below

.. note::

   **Getting the system up and running**

   - :dokuwiki:`Raspberry Pi 3 & 4 User Guide </resources/eval/user-guides/ad-fxtof1-ebz/ug_rpi>`
   - :dokuwiki:`Nvidia Jetson Nano User Guide </resources/eval/user-guides/ad-fxtof1-ebz/ug_jetson>`
   - :dokuwiki:`Nvidia Xavier NX User Guide </resources/eval/user-guides/ad-fxtof1-ebz/ug_xavier_nx>`

--------------

Application Development
-----------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/sdk_stack.png
   :width: 300px

The system has options of USB, Ethernet or Wi-Fi to connect to a host computer,
this flexibility enables evaluation across a wide range of use cases and
environments. Sampling rates of up to 30fps are supported. Data is fed from the
depth camera to the processor board over MIPI-CSI interface. This data is read
using V4L2 capture driver and in-turn either feeds it to native SDK or sends it
to the Host SDK over Ethernet, WiFi and USB interfaces. Native/Host SDK provides
this data to user applications for further use. For ease of application, the SDK
also provides OpenCV, Python and MATLAB wrappers such that developers can simply
use these wrappers to develop application.

The Depth Perception Rapid Prototyping Platform supports a wide range of
operating systems and programming languages. An open-source SDK that accompanies
the hardware platform enables you to extract depth data from the camera on the
processor and operating system of your choice. Windows and Linux support are
built into the SDK as well as sample code and wrappers for various languages
including Python, C/C++ and MATLAB. The SDK also integrates with 3rd party
technologies like OpenCV and RoS.

.. admonition:: Download

   `Access the full ADI 3D ToF software suite to get started <https://github.com/analogdevicesinc/aditof_sdk>`__

.. note::

   `Get more information abut the available 3D ToF algorithms from Analog Devices <https://www.arrow.com/tofalgorithms>`__
   `Explore the available 3D vision algorithms demos <https://github.com/robotics-ai/tof_process_public>`__

--------------

Videos
------

.. video:: https://www.youtube.com/watch?v=-CErH6ROli8

.. video:: https://www.youtube.com/watch?v=G-9UfaZXUCk

.. video:: https://www.youtube.com/watch?v=_ew0QKQMUtI

.. video:: https://www.youtube.com/watch?v=uRY2UZ0E5_o

--------------

Laser Safety
------------

.. important::

   This device complies with International Standards IEC 60825-1:2014 & 2007 for
   a Class 1 laser product. This device also complies with 21 CFR 1040.10 and
   1040.11 except for deviations pursuant to Laser Notice No. 50, dated June 24,
   2007. Only use Software and Firmware updates that are specifically provided
   for this solution.

--------------

Help and Support
----------------

For questions and more information please contact us on the Analog Devices
Engineer Zone.

.. note::

   :ez:`EngineerZone 3D ToF Depth Sensing <depth-perception-ranging-technologies/lidar-solutions/3d-tof-depth-sensing/>`
