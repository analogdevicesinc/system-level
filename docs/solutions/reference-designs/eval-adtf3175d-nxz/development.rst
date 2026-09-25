SDK Development Guide
=====================

Overview
--------

The SDK serves as a reference design for controlling the ADSD3500 camera. It is
available under MIT license and works on Windows, Linux, and embedded Linux
systems.

**Key Resources:**

-  GitHub Repository:
   `ToF <https://github.com/analogdevicesinc/ToF>`_ SDK source code
-  Documentation: Doxygen API reference via GitHub
-  Namespace: ``aditof``

Architecture
------------

Two primary deployment scenarios:

EVAL-ADTF3175D Platform
   Embedded Linux device runs ucv-app with SDK. Host connects via USB 3.0 UVC
   using Protobuf for commands.

Embedded Linux SoC
   User application links directly with SDK on device hardware.

Core Classes
------------

Essential SDK components include:

System
   Discovers and manages cameras

Camera
   Controls device operations

Frame
   Manages captured image data

DepthSensorInterface
   Sensor-level control

C++ Development (9 Steps)
-------------------------

1. **Camera Discovery**: Use System class to retrieve available cameras
2. **Configuration**: Apply JSON settings file via
   ``setControl("initialization_config", ...)``
3. **Initialization**: Call ``camera->initialize()``
4. **Version Details**: Access SDK/platform version information
5. **Frame Types**: Query available capture modes (sr-native, lr-native, etc.)
6. **Mode Selection**: Set frame type (e.g., "lr-qnative")
7. **Start Camera**: Initialize data capture
8. **Request Frame**: Retrieve frame object
9. **Extract Data**: Access specific frame types (depth, IR, raw, confidence)

Python Development
------------------

The Python binding demonstrates network camera control::

   IP_addr = ['10.42.0.1']  # Camera IP addresses
   fsync_toggle = 1         # Frame sync mode (0=manual, 1=auto, 2=disabled)

Key operations mirror C++ workflow but use network discovery via
``getCameraListAtIp()``.

Available Frame Types
---------------------

The ADSD3500 supports multiple modes:

-  Short-range/long-range native modes
-  Quarter-resolution variants
-  Mixed modes for hybrid processing
-  Sizes range from 512×512 to 1024×4096 pixels

Return Codes
------------

SDK uses ``Status`` enum for operation results, documented in Doxygen
reference.
