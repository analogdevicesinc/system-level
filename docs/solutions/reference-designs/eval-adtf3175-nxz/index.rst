.. _eval_adtf3175_nxz:

EVAL-ADTF3175-NXZ
===============================================================================

3D Time of Flight Camera Evaluation Kit featuring the ADTF3175 Module.

.. admonition:: Download
   :class: download

   `Download the latest software package <https://github.com/analogdevicesinc/ToF/releases>`_

Overview
-------------------------------------------------------------------------------

Analog Devices 3D time of flight (ToF) camera products capture depth
information, enabling advanced machine vision applications and allowing people
and devices to sense, capture and interact with their spatial environments.

The EVAL-ADTF3175-NXZ time of flight (ToF) evaluation kit showcases the
ADTF3175 module. The kit supports USB connectivity to a PC for real-time
visualization, capture and post processing of depth data. The kit includes host
PC software (Windows/Linux) and an open source multi-platform SDK for custom
application development.

For more information see: :adi:`Time of Flight Camera - System Overview <en/analog-dialogue/articles/time-of-flight-system-design-part-1-system-overview.html>`

.. figure:: images/crosby2.jpg
   :alt: EVAL-ADTF3175-NXZ Evaluation Kit
   :align: center
   :width: 400

   EVAL-ADTF3175-NXZ Evaluation Kit

Key Features
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Specification
   * - Resolution
     - 1024x1024 TOF sensor
   * - Illumination
     - FOI 81° x 81° - 940nm VCSEL
   * - Field of View
     - FOV 75° x 75°
   * - Operating Range
     - 0.4 to 4m @ 15% reflectance (native)
   * - Depth Noise
     - <15mm
   * - Accuracy
     - +/- 3mm depth error

Modes of Operation
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 30 20 15 15

   * - Mode Index
     - Mode
     - Resolution
     - Range
     - FPS*
   * - 10
     - Megapixel (mp)
     - 1024x1024
     - 4m
     - ~10
   * - 7
     - Quarter-Megapixel (qmp)
     - 512x512
     - 4m
     - ~15

.. note::
   
   FPS is currently limited by CPU processing speed

Kit Contents
-------------------------------------------------------------------------------

- ADTF3175 Evaluation Module

  - ADSD3175 Module
  - i.MX8 M Plus SOM (SolidRun)
  - Camera Interface Board

- 16GB flashed microSD card (Inserted in module SD card slot)
- USB-C to USB-C cable (Supports PD 2.0, and USB 3.1)
- Tripod

.. toctree::
   :hidden:

   startup
   software_installation
   aditofgui
   datacollect_cli
   depthcompute
   tof_auxtools_cli
   development
   hardware_access
   nvm

System Information
-------------------------------------------------------------------------------

USB and Power
~~~~~~~~~~~~~

**Minimum Requirements:**

- USB 3.0 (5Gbps)
- USB Type-C cable
- 2.0A

**Recommended Requirements:**

- USB 3.1 Gen2
- USB Type-C cable
- 3.0A

.. warning::

   Do not use USB Type-C to USB Type-A adapters.

**Dimensions:** 66mm x 58.6mm x 67.9mm

**Laser Safety:** Class 1

Index of Pages
-------------------------------------------------------------------------------

#. :doc:`Startup Guide <startup>`
#. :doc:`Software Installation <software_installation>`
#. :doc:`ADIToFGUI Tool <aditofgui>`
#. :doc:`Data Collect CLI Tool <datacollect_cli>`
#. :doc:`Depth Compute <depthcompute>`
#. :doc:`Auxiliary Tools <tof_auxtools_cli>`
#. :doc:`SDK Development <development>`
#. :doc:`Hardware Access <hardware_access>`
#. :doc:`NVM Contents <nvm>`

Terms
-------------------------------------------------------------------------------

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

   NVM
      Non-Volatile Memory

   CCB
      Camera Calibration Block

Troubleshooting
-------------------------------------------------------------------------------

Common Issues
~~~~~~~~~~~~~

**Green LED illuminates but camera remains undetected:**

- Reconnect the USB cable 3-5 times
- Try different USB ports

**GUI crashes after successfully requesting frames:**

- Restart the GUI without reconnecting the camera
- Ensure mode switching is done after the module is stopped

**Power Delivery negotiation failures:**

- Some Dell Precision laptops have known PD issues
- Try using a powered USB hub

**Slow frame rates (<3-5fps):**

- Adjust laptop power settings
- Connect external power
- Use USB 3.0 cables
- Monitor MTU settings (10,000 bytes preferred)
- Use iPerf3 for bandwidth testing (target: >1Gbps)

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and Support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
