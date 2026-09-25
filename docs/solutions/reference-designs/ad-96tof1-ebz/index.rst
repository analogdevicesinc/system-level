.. _ad_96tof1_ebz eval:

AD-96TOF1-EBZ
===============================================================================

Overview
-------------------------------------------------------------------------------

The :adi:`AD-96TOF1-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-96TOF1-EBZ.html>`
is a proven hardware platform for depth perception. When paired with a processor
board from the 96Boards ecosystem or Raspberry Pi family, it can be used for 3D
software and algorithm development. This modular platform can be used as a baseline
to design a ToF system.

Features:

- VGA resolution (640x480) at up to 30fps
- Multiple range modes: Near (25-80cm), Medium (30cm-4.5m), Far (3-6m) with <2% accuracy
- 940nm VCSEL with 110° x 85° diffuser, FoV 90° x 69.2°
- 96Board mezzanine and Raspberry Pi camera connector compatibility
- USB, Ethernet and WiFi connectivity options
- Operating temperature -20°C to 85°C

Applications:

- 3D software and algorithm development
- Depth perception prototyping
- Robotics and autonomous navigation
- Object detection and tracking

.. toctree::
   :hidden:

   calibration
   ug_linux
   ug_windows
   ug_db410c
   ug_rpi
   ug_jetson
   ug_xavier_agx
   ug_xavier_nx

Hardware
-------------------------------------------------------------------------------

**The full system hardware includes:**

-  Laser Transmitter Board
-  AFE Receiver Board

.. image:: images/board_revc.jpg
   :alt: Rev C board
   :align: right
   :width: 400

**High level specification**

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

The laser board generates the IR light pulses to illuminate the scene. It
connects directly to the AFE board and is powered and controlled through the
interface connector, with an option of external power if needed for specific use
case with different VCSEL.

-  The laser board has 4 individual lasers with appropriate precision driver and power components for accurate firing of the lasers.
-  The board is designed with the lasers positioned so that they fit around the AFE board CCD sensor when mated together. This position gives optimum performance for a wide range of use cases minimizing any effects of shadowing.
-  It receives power and all control I/O through the interface connector.

**Key parts:**

-  *VCSEL:* Finisar I940-G2332-NBC-D1-110B85R
-  *MOSFET driver:* :adi:`ADP5202`
-  *MOSFET:* EPC2007C
-  *Temperature measurement:* :adi:`ADT7410`
-  *Power:* :adi:`ADP2504`

.. note::

   The previous board versions (Rev. B and Rev. C) use MOSFET driver: :adi:`ADP3624`

.. admonition:: Download
   :class: download

   `Rev. B Hardware design files (including schematics, BoM and layout) <resources/tof_laser_revb.zip>`_ `Rev. C Hardware design files (including schematics, BoM and layout) <resources/tof_laser_revc.zip>`_ `Rev. D Hardware design files (including schematics, BoM and layout) <resources/tof_laser_revd.zip>`_

--------------

**AFE Board**

The AD-96TOF1-EBZ AFE Board from factor is compliant with the 96Boards mezzanine
specification and can connect to compatible 96Board processor family or to
Raspberry Pi compatible boards via an additional MIPI connector interface on the
PCB. It has an EEPROM to store the ToF AFE firmware and system calibration data.
System temperature measurement is enabled through an embedded temperature
sensor.

-  The AFE board contains a Panasonic CCD Sensor combined with ADDI9036 TOF Signal Processor with necessary power and timing signal chains.
-  Optics are fitted to the board using industry standard mounting adapters to give a wide field of view, but can be changed based on individual use cases. There is a threaded adapter for mechanical mounting on an optional tripod stand.

**Key parts:**

-  *CCD sensor:* Panasonic MN34906BL
-  *Optics*: JCD J6920B lens with 940nm bandpass filter
-  *ToF AFE:* :adi:`ADDI9036` TOF Signal Processor
-  *EEPROM:* AT24CM01-XHM-B
-  *Temperature measurement:* :adi:`ADT7410`
-  *Power:* :adi:`ADP5071`, :adi:`LTC3119`, :adi:`ADP7112`, :adi:`ADP5023`

.. admonition:: Download
   :class: download

   `Rev. B Hardware design files (including schematics, BoM and layout) <resources/tof_afe_revb.zip>`_ `Rev. C Hardware design files (including schematics, BoM and layout) <resources/tof_afe_revc.zip>`_

.. note::

   For more information and how to buy the system please goto the :adi:`Analog Devices AD-96TOF1-EBZ Product page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`

--------------

System setup & evaluation
-------------------------------------------------------------------------------

The development kit is delivered with an SD card containing the evaluation
software for the supported embedded platforms and a set of accessories required
to put the system together and get it up and running in no time.

.. image:: images/96tof_box_contents.jpg
   :alt: Box contents
   :align: right
   :width: 400

Development kit contents:

-  Laser Board
-  AFE Mezzanine Board
-  5V power supply for the AFE board and power cords
-  SD card with the evaluation software
-  One page Quick Start Guide

.. note::

   Getting the system up and running


   Host computer

   -  :doc:`Windows User Guide </solutions/reference-designs/ad-96tof1-ebz/ug_windows>`
   -  :doc:`Linux User Guide </solutions/reference-designs/ad-96tof1-ebz/ug_linux>`

   Embedded platforms

   -  :doc:`DragonBoard 410c User Guide </solutions/reference-designs/ad-96tof1-ebz/ug_db410c>`
   -  :doc:`Raspberry Pi 3 & 4 User Guide </solutions/reference-designs/ad-96tof1-ebz/ug_rpi>`
   -  :doc:`Nvidia Jetson Nano User Guide </solutions/reference-designs/ad-96tof1-ebz/ug_jetson>`


--------------

Application Development
-------------------------------------------------------------------------------

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
   :class: download

   `Access the full ADI 3D ToF software suite to get started <https://github.com/analogdevicesinc/aditof_sdk>`_


--------------

Laser Safety
-------------------------------------------------------------------------------

.. important::

   This device complies with International Standards IEC 60825-1:2014 & 2007 for
   a Class 1 laser product. This device also complies with 21 CFR 1040.10 and
   1040.11 except for deviations pursuant to Laser Notice No. 50, dated June 24,
   2007. Only use Software and Firmware updates that are specifically provided
   for this solution.


   `Laser Certification Report AD-96TOF1-EBZ Rev.B & Rev.C <resources/report_2132_ad-96tof1-ebz_60825_classification.pdf>`_

   `Laser Certification Report AD-96TOF1-EBZ Rev.D <resources/report_2388_60825_classification.pdf>`_

--------------

Videos
-------------------------------------------------------------------------------

.. video:: https://www.youtube.com/watch?v=t6z9UImtO6g

.. video:: https://www.youtube.com/watch?v=5pfohkFjAuU

.. video:: https://www.youtube.com/watch?v=-CErH6ROli8

.. video:: https://www.youtube.com/watch?v=G-9UfaZXUCk

.. video:: https://www.youtube.com/watch?v=_ew0QKQMUtI

.. video:: https://www.youtube.com/watch?v=uRY2UZ0E5_o

--------------

Help and Support
-------------------------------------------------------------------------------

For questions and more information please contact us on the Analog Devices
Engineer Zone.

.. hint::

   :ez:`EngineerZone 3D ToF Depth Sensing <depth-perception-ranging-technologies/lidar-solutions/3d-tof-depth-sensing>`
