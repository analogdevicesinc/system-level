.. _eval_adtf3175d_nxz:

EVAL-ADTF3175D-NXZ
==================

.. important::

   Support or Query: tof@analog.com

**2025-09-12**: Release 6.1.0 is available on GitHub; see
`ToF/releases <https://github.com/analogdevicesinc/ToF/releases>`_.

.. important::

   Please reference the release note to see important changes.

   The documentation is now a part of the release and is also in the GitHub repo:
   `External Link <https://github.com/analogdevicesinc/ToF/blob/v6.1.0/doc/user-guide/ADTF3175D-EvalKit-610.md>`_

Overview
--------

Analog Devices 3D time of flight (ToF) camera products capture depth
information, enabling advanced machine vision applications and allowing people
and devices to sense, capture and interact with their spatial environments.

For more information see:
:adi:`Time of Flight Camera – System Overview <en/analog-dialogue/articles/time-of-flight-system-design-part-1-system-overview.html>`

The EVAL-ADTF3175D-NXZ time of flight (ToF) evaluation kit showcases the
ADTF3175 module with ADI's depth ISP, the ADSD3500. The kit supports ethernet
over USB connectivity to a PC for real-time visualization, capture and post
processing of depth data. The kit includes host PC software (Windows) and an
open source multi-platform SDK for custom application development.

.. image:: images/crosby2.jpg
   :alt: EVAL-ADTF3175D-NXZ
   :align: center
   :width: 400

Key Features
~~~~~~~~~~~~

================ ====================================
Resolution       1024x1024 TOF sensor
Illumination     FOI 81°x81° - 940nm Lumentum VCSEL
Field of view    FOV 75°x75°
Operating range  0.4 to 4m @ 15% reflectance (native)
Depth Noise      <15mm
Accuracy         +/- 3mm depth error
================ ====================================

Modes of Operation
~~~~~~~~~~~~~~~~~~

See the :ref:`Mode Table <eval_adtf3175d_mode_table>` section for mode configurations based on serial number.

Kit Contents
~~~~~~~~~~~~

-  ADTF3175D Evaluation Module

   -  ADTF3175 Module
   -  i.MX8 M Plus SOM (SolidRun)
   -  Camera Interface Board
   -  ADSD3500 Interposer board

-  16GB flashed microSD card (Inserted in module sd card slot)
-  USB-C to USB-C cable. Supports PD 2.0, and USB 3.1
-  Tripod

System Overview
---------------

The EVAL-ADTF3175D-NXZ features three primary components:

ADTF3175 ToF Module
   A complete Time-Of-Flight module for high resolution 3D depth sensing.
   Integrates the ADSD3100 sensor, optical components, infrared illumination
   with driver circuitry, flash memory, and voltage regulators.

ADSD3500 Depth ISP
   This depth image signal processor computes raw ToF sensor data into
   processed depth and brightness frames. It greatly lightens the load on
   the host processor by handling depth computation at the edge.

NXP i.MX8M Embedded System
   An NXP SOM with carrier board manages power distribution and I/O
   connectivity. Runs V4L2 camera and USB video drivers, enabling data
   passthrough via ethernet-over-USB.

Quarter-MegaPixel (512x512)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/pulsatrix_qmp.png
   :align: center

MegaPixel (1024x1024)
~~~~~~~~~~~~~~~~~~~~~

.. image:: images/pulsatrix_mp.png
   :align: center

System Information
------------------

USB and Power
~~~~~~~~~~~~~

**Minimum Requirements**

-  USB 3.0 (5Gbps)
-  USB Type-C cable
-  2.0A

**Recommended Requirements**

-  USB 3.1 Gen2
-  USB Type-C cable
-  3.0A

.. note::

   Do not use USB Type-C to USB Type-A adapters.

**Dimensions:** 66mm x 58.6mm x 67.9mm

**Enclosure Drawing:** `Link <resources/eval-adtf3175d-nxz_drawing_v1.pdf>`_

**Laser Safety:** Class 1

.. toctree::
   :hidden:

   getting_started
   aditofgui
   datacollect_cli
   depthcompute
   tof_auxtools_cli
   development
   hardware_access
   v4l2_driver
   firmware_module_upgrade

Support Links
-------------

-  Module and Eval kit questions:
   :ez:`EngineerZone <depth-perception-ranging-technologies/continuous-wave-cmos-time-of-flight-tof>`
-  Software/SDK questions:
   `ToF/issues <https://github.com/analogdevicesinc/ToF/issues>`_
-  Lumentum VCSEL Information:

   -  https://www.lumentum.com/en/products/10-w-940-nm-triple-junction-vcsel-array
   -  https://www.lumentum.com/en/products/multi-junction-vcsel-arrays

Terms
-----

.. glossary::

   FOI
      Field of Illumination

   FOV
      Field of View

   FPS
      Frames per Second

   SOM
      System On Module

   VCSEL
      Vertical-Cavity Surface-Emitting Laser

Recommendations
---------------

People who follow the flow outlined have a much better experience.
However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Warning
-------

.. esd-warning::

Help and Support
----------------

Please go to :ref:`Help and Support <help-and-support>` page.
