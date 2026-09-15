.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-96tof1-ebz

.. _ad-96tof1-ebz:

AD-96TOF1-EBZ
=============

Introduction
------------

The
:adi:`AD-96TOF1-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-96TOF1-EBZ.html>`
is a proven hardware platform for depth perception. When paired with a processor
board from the 96Boards ecosystem or Raspberry Pi family, it can be used for 3D
software and algorithm development. This modular platform can be used as a
baseline to design a ToF system and will allow customers to start developing
their software and algorithms while the hardware can be modified for their
specific application. The solution has VGA resolution which means that objects
can be detected to a higher level of granularity than other 3D ToF solutions, an
ability to detect depth in strong ambient light conditions and multiple range
detection modes for increased accuracy. A native and host SDK is provided. The
SDK also provides OpenCV, Python®, MATLAB®, Open3D and RoS wrappers so that
developers can use them to simplify application development.

**The full system hardware includes:**

- Laser Transmitter Board
- AFE Receiver Board

**High level specification**

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tofebz/board_revc.jpg
   :width: 400px

::

   *Range
     *Near: 25cm to 80cm
     *Medium: 30cm to 4.5m (Rev.B: 80cm to 3m)
     *Far: 3m to 6m
     *Accuracy: < 2% for all ranges
   *Frame Rate upto 30fps dependent on processor board, OS and interface to host computer
   *Resolution 640 x 480 pixels
   *Operating Temperature -20⁰C to 85⁰C
   * 940nm VCSEL with 110⁰ x 85⁰ batwing profile diffuser
   *Receive lens: FoV 90⁰ x 69.2⁰ including 940nm BPF
   *96Board mezzanine high speed and low speed expansion connector compatibility
   *Raspberry Pi camera connector to connect to any compatible processor board
   *Connectivity support for USB or Network(WiFi, Ethernet)
   *5V DC Input
   *20W max power consumption

**Laser Board**

- The laser board has 4 individual lasers with appropriate precision driver and
  power components for accurate firing of the lasers.
- The board is designed with the lasers positioned so that they fit around the
  AFE board CCD sensor when mated together. This position gives optimum
  performance for a wide range of use cases minimizing any effects of shadowing.
- It receives power and all control I/O through the interface connector.
- :dokuwiki:`Laser Board Design Files and Description </ad-96tof1-ebz/laserboard>`

**AFE Board**

- The AFE board contains a Panasonic CCD Sensor combined with ADDI9036 TOF
  Signal Processor with necessary power and timing signal chains.
- Optics are fitted to the board using industry standard mounting adapters to
  give a wide field of view, but can be changed based on individual use cases.
  There is a threaded adapter for mechanical mounting on an optional tripod
  stand.
- :dokuwiki:`AFE Board Design Files and Description </ad-96tof1-ebz/afeboard>`

.. note::

   For more information and how to buy the system please goto the
   :adi:`Analog Devices AD-96TOF1-EBZ Product page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`

--------------

System setup & evaluation
-------------------------

The development kit is delivered with an SD card containing the evaluation
software for the supported embedded platforms and a set of accessories required
to put the system together and get it up and running in no time.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/96tof_box_contents.jpg
   :width: 400px

Development kit contents:

- Laser Board
- AFE Mezzanine Board
- 5V power supply for the AFE board and power cords
- SD card with the evaluation software
- One page Quick Start Guide

.. note::

   **Getting the system up and running**

   Host computer

   - :dokuwiki:`Windows User Guide </resources/eval/user-guides/ad-96tof1-ebz/ug_windows>`
   - :dokuwiki:`Linux User Guide </resources/eval/user-guides/ad-96tof1-ebz/ug_linux>`

   Embedded platforms

   - :dokuwiki:`DragonBoard 410c User Guide </resources/eval/user-guides/ad-96tof1-ebz/ug_db410c>`
   - :dokuwiki:`Raspberry Pi 3 & 4 User Guide </resources/eval/user-guides/ad-96tof1-ebz/ug_rpi>`
   - :dokuwiki:`Nvidia Jetson Nano User Guide </resources/eval/user-guides/ad-96tof1-ebz/ug_jetson>`

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

Laser Safety
------------

.. important::

   This device complies with International Standards IEC 60825-1:2014 & 2007 for
   a Class 1 laser product. This device also complies with 21 CFR 1040.10 and
   1040.11 except for deviations pursuant to Laser Notice No. 50, dated June 24,
   2007. Only use Software and Firmware updates that are specifically provided
   for this solution.

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tofebz/report_2132_ad-96tof1-ebz_60825_classification.pdf`

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/report_2388_60825_classification.pdf`

--------------

Videos
------

.. video:: https://www.youtube.com/watch?v=t6z9UImtO6g

.. video:: https://www.youtube.com/watch?v=5pfohkFjAuU

.. video:: https://www.youtube.com/watch?v=-CErH6ROli8

.. video:: https://www.youtube.com/watch?v=G-9UfaZXUCk

.. video:: https://www.youtube.com/watch?v=_ew0QKQMUtI

.. video:: https://www.youtube.com/watch?v=uRY2UZ0E5_o

--------------

Help and Support
----------------

For questions and more information please contact us on the Analog Devices
Engineer Zone.

.. note::

   :ez:`EngineerZone 3D ToF Depth Sensing <depth-perception-ranging-technologies/lidar-solutions/3d-tof-depth-sensing/>`
