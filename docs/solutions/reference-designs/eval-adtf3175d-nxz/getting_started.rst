Getting Started
===============

This guide helps you get started with the EVAL-ADTF3175D-NXZ evaluation kit.

Kit Contents
------------

The evaluation module includes:

-  ADTF3175 Imager Module with i.MX8 M Plus SOM
-  Camera Interface Board and ADSD3500 Interposer board
-  16GB flashed microSD card (Inserted in module sd card slot)
-  USB-C to USB-C cable supporting PD 2.0 and USB 3.1
-  Tripod

System Requirements
-------------------

-  Seventh Gen Intel Core i5 Processor @ 2.4GHz, Dual Core (or equivalent)
-  8GB RAM minimum
-  Graphics card supporting OpenCL 2.0 or higher

Software Download and Installation
----------------------------------

Download
~~~~~~~~

The installer is available from the
`ToF/releases <https://github.com/analogdevicesinc/ToF/releases>`_ page.

For EVAL-ADTF3175D-NXZ units, use version 5.x.x or later.

Installation Process
~~~~~~~~~~~~~~~~~~~~

The installer guides you through several steps:

1. **Initial Setup**: Accept the software license agreement
2. **Location Selection**: Choose where to install the package
3. **Prerequisites**: The system automatically detects and installs OpenCL 2.0
   Runtime and Visual Studio 2015 redistributables if needed
4. **Image Download**: Optionally download the NXP image immediately after
   installation. If you skip this option, navigate to the image folder and
   execute the appropriate script:

   -  Windows: ``get_image.cmd``
   -  Linux: ``get_image.sh``

Post-Installation Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Image folder contains three key items:

microSD card image
   Image for the NXP system-on-module (includes flashing instructions).
   Archive named similarly to ``microsd-54c2ce9f.zip``.

Firmware update file (fwUpdate)
   Firmware for the ADSD3500 chip (such as ``fwUpdate_3.2.2.bin``).

Depth compute binaries
   Binaries for processing depth data.

Available Tools
~~~~~~~~~~~~~~~

After installation, three applications are available from the installation
directory:

-  :doc:`aditofgui` - Graphical interface
-  :doc:`datacollect_cli` - Command-line data capture tool
-  :doc:`depthcompute` - Command-line depth processing tool

Initial Setup
-------------

Step 1: Flash SD Card
~~~~~~~~~~~~~~~~~~~~~

Reflash the included micro-SD card using the flashing instructions included
with the microSD card image.

Step 2: Update Firmware
~~~~~~~~~~~~~~~~~~~~~~~

Flash firmware onto the module using the :doc:`firmware_module_upgrade`
instructions.

Step 3: Connect Hardware
~~~~~~~~~~~~~~~~~~~~~~~~

1. Mount the camera on the included tripod
2. Connect the USB-C cable to the module, then to a laptop

Step 4: Verify Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

Three LED indicators confirm proper startup:

-  Green LED beneath the USB-C connector
-  Blinking LED on the NXP SOM
-  Blue LED on the ADSD3500 interposer board

An unidentified network connection should appear on the host computer.

Step 5: Launch GUI
~~~~~~~~~~~~~~~~~~

Run the :doc:`aditofgui` application to begin streaming.

Power Options
-------------

The system supports dual power modes:

**USB Power (Standard)**
   Connect a USB-C to USB-C cable to a laptop. This provides both power and
   data transfer capability.

**Wall Adapter (Alternative)**
   Use an external wall adapter providing at least 5 watts with USB-C
   connectivity. Note that this eliminates direct data transfer capability.
   When using wall power, connect an IX ethernet cable to establish
   communication between the camera and a networked PC, then modify the
   ``camera_ip`` parameter in the ``tof-tools.config`` file with the device's
   IP address.
