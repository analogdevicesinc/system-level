.. _eval_adtf3175_nxz development:

Development Guide
===============================================================================

This page documents the EVAL-ADTF3175-NXZ development platform, providing
guidance on using the Time-of-Flight (ToF) SDK.

Overview
-------------------------------------------------------------------------------

The SDK operates under MIT license and serves as a reference design for
customers.

**Key Resources:**

- `GitHub Repository <https://github.com/analogdevicesinc/ToF>`_ - ToF SDK source code
- `Doxygen Documentation <https://analogdevicesinc.github.io/ToF/>`_ - API reference
- SDK Namespace: ``aditof``

Architecture
-------------------------------------------------------------------------------

Two deployment scenarios are supported:

EVAL-ADTF3175-NXZ Setup
~~~~~~~~~~~~~~~~~~~~~~~

Device runs embedded Linux with the ADTF3175 module. Connects to host
(Windows/Linux) via USB 3.0 using ethernet-over-USB.

Embedded Linux SoC
~~~~~~~~~~~~~~~~~~

User application links directly with SDK on device.

Core Classes
-------------------------------------------------------------------------------

Essential classes for development:

- **System** - Entry point for camera discovery
- **Camera** - Main camera interface
- **CameraDetails** - Camera information and capabilities
- **DepthSensorInterface** - Low-level sensor access
- **Frame** - Container for captured data
- **FrameDataDetails** - Frame metadata

C++ Development Guide
-------------------------------------------------------------------------------

Step 1: Get List of Available Cameras
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use System class to obtain a vector of Camera objects:

.. code-block:: cpp

   #include <aditof/system.h>

   aditof::System system;
   std::vector<std::shared_ptr<aditof::Camera>> cameras;
   system.getCameraList(cameras);

Step 2: Apply SDK Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply the SDK configuration JSON file:

.. code-block:: cpp

   cameras.front()->setControl("initialization_config", configFile);

Step 3: Initialize Camera
~~~~~~~~~~~~~~~~~~~~~~~~~

Initialize the selected camera:

.. code-block:: cpp

   cameras.front()->initialize();

Step 4: Retrieve Available Frame Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get available modes:

.. code-block:: cpp

   std::vector<std::string> frameTypes;
   cameras.front()->getAvailableFrameTypes(frameTypes);

Step 5: Select Frame Mode
~~~~~~~~~~~~~~~~~~~~~~~~~

Set the desired frame type:

.. code-block:: cpp

   cameras.front()->setFrameType("lr-qnative");

Step 6: Start Camera
~~~~~~~~~~~~~~~~~~~~

Begin camera operation:

.. code-block:: cpp

   cameras.front()->start();

Step 7: Request Frame
~~~~~~~~~~~~~~~~~~~~~

Request a frame from the device:

.. code-block:: cpp

   aditof::Frame frame;
   cameras.front()->requestFrame(&frame);

Step 8: Extract Frame Data
~~~~~~~~~~~~~~~~~~~~~~~~~~

Access frame data and details:

.. code-block:: cpp

   uint16_t *depthData;
   aditof::FrameDataDetails details;
   frame.getData("depth", &depthData);
   frame.getDataDetails("depth", details);

Python Development Guide
-------------------------------------------------------------------------------

Configuration Steps
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import aditof

   # Specify camera IP addresses
   camera_ips = ["10.43.0.1"]

   # Initialize cameras
   system = aditof.System()
   cameras = []
   for ip in camera_ips:
       cameras.extend(system.getCameraListAtIp(ip))

   # Load configuration
   cameras[0].setControl("initialization_config", "config.json")
   cameras[0].initialize()

   # Set frame type and start
   cameras[0].setFrameType("lr-native")
   cameras[0].start()

Frame Capture
~~~~~~~~~~~~~

.. code-block:: python

   # Create Frame object
   frame = aditof.Frame()

   # Request frame from camera
   cameras[0].requestFrame(frame)

   # Access frame details
   frame_details = aditof.FrameDataDetails()
   frame.getDataDetails("depth", frame_details)
   print(f"Width: {frame_details.width}, Height: {frame_details.height}")

   # Stop camera
   cameras[0].stop()

Available Frame Types
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Frame Type
     - Raw Size
     - Output Size
     - Description
   * - sr-native / lr-native
     - 1024x4096
     - 1024x1024
     - Full resolution
   * - sr-qnative / lr-qnative
     - 2560x512
     - 512x512
     - Quarter resolution
   * - sr-mixed / lr-mixed
     - 2560x512
     - 512x512
     - Mixed mode

Frame data includes: raw, depth, infrared (ir), confidence (conf), XYZ
coordinates, and metadata.

API Return Codes
-------------------------------------------------------------------------------

The SDK uses the ``Status`` enum for return code handling. See the
`Doxygen documentation <https://analogdevicesinc.github.io/ToF/>`_ for
complete API reference.
