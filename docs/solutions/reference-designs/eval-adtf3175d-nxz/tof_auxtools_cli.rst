Python Auxiliary Tools
======================

Analog Devices provides Python tools for processing Time-of-Flight (ToF)
camera data.

Eval Kit 5.0.0 or Later
-----------------------

**System Requirements:** Python 3.10 (64-bit)

Setup Process
~~~~~~~~~~~~~

Windows and Linux installations both require creating Python virtual
environments and installing dependencies from provided requirement files.

Key Examples
~~~~~~~~~~~~

first_frame.py
   Captures a single frame from the camera, supporting both USB and network
   connections across multiple operational modes (lr-native, sr-native, etc.).

depth-image-animation-pygame.py
   Streams and visualizes ToF depth frames using the PyGame engine, enabling
   real-time depth data display. See :doc:`PyGame animation example <v4l2_driver>`.

skeletal_tracking.py
   Performs human pose detection using TensorFlow Lite integration with depth
   data.

Primary Tools
~~~~~~~~~~~~~

rawparser.py
   Processes recorded raw frame data to extract depth information, confidence
   metrics, and point cloud geometry. The tool outputs:

   -  PNG images for depth and confidence frames
   -  PLY files for 3D point cloud data
   -  MP4 video combining multiple data streams
   -  Metadata documentation

saveCCBToFile.py
   Exports camera calibration binary files to local storage, useful for
   configuration management across devices.

PyGame Animation
----------------

The PyGame animation script demonstrates how to create animated depth image
visualizations.

**Requirements:**

-  ToF Evaluation Kit release 4.1.1 or later with Python 3.9+
-  Matplotlib (for color mapping)
-  PyGame (for animation)
-  NumPy

**Usage:**

Network connection::

   python depth-image-animation-pygame.py <ip> <config>

Local/USB connection::

   python depth-image-animation-pygame.py <config>

**Example:**

::

   python depth-image-animation-pygame.py 10.42.0.1 tof-viewer_config.json

The script should be placed in the ``TOF_Evaluation_ADTF3175D-Rel4.1.1/bin``
directory. Additional examples are available in the official GitHub
repository's streaming examples folder.

Eval Kit 4.3.0 or Earlier
-------------------------

These older versions utilized Miniconda-based environments with tools like
``tofi_compute_depth`` for raw file processing and FSF extraction utilities
for Microsoft video format handling. These tools were discontinued in later
releases.
