.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175-nxz

.. _eval-adtf3175-nxz:

EVAL-ADTF3175-NXZ
-----------------

.. admonition:: Download

   :git-ToF:`Download the latest software package from here <releases/+>`

Analog Devices 3D time of flight (ToF) camera products capture depth
information, enabling advanced machine vision applications and allowing people
and devices to sense, capture and interact with their spatial environments.

For more information see:
:adi:`Time of Flight Camera – System Overview <en/analog-dialogue/articles/time-of-flight-system-design-part-1-system-overview.html>`

Introduction
------------

The EVAL-ADTF3175-NXZ time of flight (ToF) evaluation kit is showcasing the
ADTF3175 module. The kit supports USB connectivity to a PC for real-time
visualization, capture and post processing of depth data. The kit includes host
PC software (Windows/Linux) and an open source multi-platform SDK for custom
application development.

Key Features
~~~~~~~~~~~~

.. note::

   .. list-table::

      * - Resolution:
        -
        - 1024x1024 TOF sensor
      * - Illumination:
        -
        - FOI 81°x81° - 940nm VCSEL
      * - Field of view:
        -
        - FOV 75°x75°
      * - Operating range:
        -
        - 0.4 to 4m @ 15% reflectance (native)
      * - Depth Noise:
        -
        - <15mm
      * - Accuracy:
        -
        - +/- 3mm depth error

Modes of Operation
^^^^^^^^^^^^^^^^^^

.. note::

   .. list-table::

      * - Mode Index
        -
        - Mode
        -
        - Resolution
        -
        - FPS\*
      * - 10
        -
        - Megapixel (mp)
        -
        - 1024x1024
        -
        - ~10
      * - 7
        -
        - Quarter-Megapixel (qmp)
        -
        - 512x512
        -
        - ~15

   FPS is currently limited by CPU processing speed

What is included in the kit?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ADTF3175 Evaluation Module

  - ADSD3175 Module
  - i.MX8 M Plus SOM (SolidRun)
  - Camera Interface Board

- 16GB flashed microSD card (Inserted in module sd card slot)
- USB-C to USB-C cable. Supports PD 2.0, and USB 3.1
- Tripod

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/crosby2.jpg
   :width: 300px

--------------

System Overview
~~~~~~~~~~~~~~~

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175-nxz/crosbyonly.png

:dokuwiki:`Click here for more information on each block </resources/eval/user-guides/eval-adtf3175-nxz/adtf3175-bc>`

Quick Start
~~~~~~~~~~~

:dokuwiki:`Start Up Guide </eval-adtf3175-nxz-startup>`

--------------

System Information
~~~~~~~~~~~~~~~~~~

::

   ; USB and Power :

**Minimum Requirements**

- USB 3.0 (5Gbps)
- USB Type-C cable
- 2.0A

**Recommended Requirements**

- USB 3.1 Gen2
- USB Type-C cable
- 3.0A

Note: Do not use USB Type-C to USB Type-A adapters.

::

   ; Dimensions : 66mm x 58.6mm x 67.9mm
   ; Enclosure Drawing : //TO BE COMPLETED//
   ; Laser Safety : Class 1
   ; Operating Environment : //TO BE COMPLETED//

--------------

Index of Pages
--------------

.. note::

   * :dokuwiki:`Start Up Guide </eval-adtf3175-nxz-startup>`

   * :dokuwiki:`Installation </resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`

   * :dokuwiki:`ADIToFGUI Tool </resources/eval/user-guides/eval-adsd3100-nxz-gui>`

   * :dokuwiki:`Data Collect CLI Tool </resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>`

   * :dokuwiki:`Depth Compute CLI Tool </resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`

   * :dokuwiki:`Auxillary Tools </resources/eval/user-guides/eval-adsd3100-nxz/tof_auxtools_cli>`

   * :dokuwiki:`SDK development </resources/eval/user-guides/eval-adsd3100-nxz-development>`

   * :dokuwiki:`Accessing the ADTF-3175x </resources/eval/user-guides/eval-adtf3175x-access>`

   * :dokuwiki:`Troubleshooting Guide </resources/eval/user-guides/aditofgui_ts>`

   * :dokuwiki:`Depth Compute Parameters </resources/eval/user-guides/depthcompute/params>`

--------------

Terms
-----

::

   ; **FOI** : Field of Illumination
   ; **FOV** : Field of View
   ; **FPS** : Frames per Second
   ; **SOM** : System On Module
   ; **VCSEL** : Vertical-Cavity Surface-Emitting Laser
