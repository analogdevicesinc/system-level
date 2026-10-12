.. _eval_adsd3100_nxz startup:

Startup Guide
===============================================================================

This guide will help you get started with the EVAL-ADSD3100-NXZ evaluation kit.

Kit Contents
-------------------------------------------------------------------------------

The package includes:

- ADSD3100-NXZ Evaluation Module

  - ADSD3100 Imager Module
  - i.MX8 M Plus SOM (SolidRun)
  - Camera Interface Board

- 16GB flashed microSD card (Inserted in module SD card slot)
- Anker USB Hub
- USB-C to USB-C cable (Supports PD 2.0, and USB 3.1)

.. figure:: images/adsd3100-nxz-kit.jpg
   :alt: EVAL-ADSD3100-NXZ Kit Contents
   :align: center
   :width: 400

   EVAL-ADSD3100-NXZ Kit Contents

Software Download
-------------------------------------------------------------------------------

Before starting, download and install the software package. See the
:doc:`Software Installation Guide <software_installation>` for detailed
instructions.

Startup Instructions
-------------------------------------------------------------------------------

Follow these steps to get the camera up and running:

1. Install the software package
2. Remove camera from packaging
3. Mount camera. Orientation shown in image below

.. figure:: images/adsd3100_w_enc.png
   :alt: Camera orientation
   :align: center
   :width: 400

   Camera Orientation

4. Connect USB-C cable to module

.. figure:: images/adsd3100_usbc_sdcard.jpg
   :alt: USB-C and SD card location
   :align: center
   :width: 200

   USB-C Connector and SD Card Location

5. Connect to laptop
6. Wait for green light under the USB-C connector on the module to light up
7. Run the GUI

.. figure:: images/adsd3100_kit_w_hubandlaptop.jpg
   :alt: Full setup with hub and laptop
   :align: center
   :width: 400

   Full Setup with Hub and Laptop

Using the USB Hub
~~~~~~~~~~~~~~~~~

If mp_pcm mode fails, connect the module to USB-C hub 5Gbps port (highlighted
by white box), and connect hub to PC.

.. figure:: images/adsd3100_hub.jpg
   :alt: USB Hub connection
   :align: center
   :width: 600

   USB Hub Connection (use highlighted 5Gbps port)

Troubleshooting
-------------------------------------------------------------------------------

GUI Crash
~~~~~~~~~

- Ensure that mode switching is done after module is stopped
- If crashes persist, there may be power insufficiency, especially with mp_pcm
  mode
- Try using the USB hub connected to external power

Green Light Not Activating
~~~~~~~~~~~~~~~~~~~~~~~~~~

- SD-Card could be corrupted
- See :doc:`Flashing Image Instructions <flashing_image_instructions>` to
  reflash the firmware
