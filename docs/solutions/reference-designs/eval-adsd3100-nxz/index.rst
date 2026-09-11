.. _eval_adsd3100_nxz:

EVAL-ADSD3100-NXZ
===============================================================================

High-Resolution 1Mpixel 3D Time of Flight Depth Camera Evaluation Kit.

.. admonition:: Download
   :class: download

   `Download the latest software package <https://github.com/analogdevicesinc/ToF/releases>`_

Overview
-------------------------------------------------------------------------------

Analog Devices 3D time of flight (ToF) camera products capture depth
information, enabling advanced machine vision applications and allowing people
and devices to sense, capture and interact with their spatial environments.

The EVAL-ADSD3100-NXZ time of flight (ToF) evaluation kit is a complete
high-resolution (1Mpixel) 3D depth camera system assembled with the NXP i.MX 8M
Plus processor. The camera supports USB connectivity to a PC for real-time
visualization, capture and post processing of depth data. The kit includes host
PC software (Windows/Linux) and an open source multi-platform SDK for custom
application development.

For more information see: :adi:`Time of Flight Camera - System Overview <en/analog-dialogue/articles/time-of-flight-system-design-part-1-system-overview.html>`

.. figure:: images/adsd3100_noenc.png
   :alt: EVAL-ADSD3100-NXZ without enclosure
   :align: center
   :width: 300

   EVAL-ADSD3100-NXZ Module (without enclosure)

.. figure:: images/adsd3100_w_enc.png
   :alt: EVAL-ADSD3100-NXZ with enclosure
   :align: center
   :width: 300

   EVAL-ADSD3100-NXZ Module (with enclosure)

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
     - FOI 60° x 60° - 940nm VCSEL
   * - Field of View
     - FOV 51° x 51°
   * - Operating Range
     - up to 5.2m @ 90% reflectance (native)
   * - Depth Noise
     - 1%
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
     - FPS
   * - 5
     - Megapixel (mp)
     - 1024x1024
     - 5.2m
     - 10
   * - 7
     - Quarter-Megapixel (qmp)
     - 512x512
     - 5.2m
     - 15

Kit Contents
-------------------------------------------------------------------------------

- ADSD3100-NXZ Evaluation Module

  - ADSD3100 Imager Module
  - i.MX8 M Plus SOM (SolidRun)
  - Camera Interface Board

- 16GB flashed microSD card (Inserted in module SD card slot)
- USB-C to USB-C cable (Supports PD 2.0, and USB 3.1)

.. note::

   The stand is *not* included in the kit.

.. toctree::
   :hidden:

   startup
   software_installation
   flashing_image_instructions
   aditofgui
   datacollect_cli
   depthcompute_cli
   tof_auxtools_cli
   development

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

**Dimensions:** 38mm x 72.5mm x 87mm

**Laser Safety:** Class 1

.. admonition:: Download
   :class: download

   `Schematics: eval-adsd3100-nxz_drawing_v1.pdf <resources/eval-adsd3100-nxz_drawing_v1.pdf>`_

Index of Pages
-------------------------------------------------------------------------------

#. :doc:`Startup Guide <startup>`
#. :doc:`Software Installation <software_installation>`
#. :doc:`Flashing Image Instructions <flashing_image_instructions>`
#. :doc:`ADIToFGUI Tool <aditofgui>`
#. :doc:`Data Collect CLI Tool <datacollect_cli>`
#. :doc:`Depth Compute CLI Tool <depthcompute_cli>`
#. :doc:`Auxiliary Tools <tof_auxtools_cli>`
#. :doc:`Development Guide <development>`

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

Mode Table
-------------------------------------------------------------------------------

Mode number and .ini file counterparts are different based on different batches
of kits. Please check the serial number of your kit to determine the correct
mode configuration.

Serial Numbers Starting with 'am'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires ADSD3500 version 4.2.1.0 minimum.

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Mode
     - Mode Name
     - INI File
   * - 0
     - sr-native
     - RawToDepthAdsd3500_sr-native.ini
   * - 1
     - lr-native
     - RawToDepthAdsd3500_lr-native.ini
   * - 2
     - sr-qnative
     - RawToDepthAdsd3500_sr-qnative.ini
   * - 3
     - lr-qnative
     - RawToDepthAdsd3500_lr-qnative.ini

Serial Numbers Starting with 'DV11' or 'CR'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Mode
     - Mode Name
     - INI File
   * - 10
     - mp
     - RawToDepthAdsd3500_mp.ini
   * - 7
     - qmp
     - RawToDepthAdsd3500_qmp.ini

Troubleshooting
-------------------------------------------------------------------------------

EVAL-ADSD3100-NXZ Common Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

**SD-Card could be corrupted:**

- See :doc:`Flashing Image Instructions <flashing_image_instructions>` to
  reflash the SD card

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and Support
-------------------------------------------------------------------------------

Please go to :ref:`Help and Support <help-and-support>` page.
