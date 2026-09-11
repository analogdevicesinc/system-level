ADIToFGUI
=========

ADIToFGUI is the graphical interface for visualizing and capturing ToF data.

Eval Kit 5.0.0 or Later
-----------------------

Key Features
~~~~~~~~~~~~

-  Adjust configuration parameters during use through the Ini Parameter window
   (accessible via the Tools menu)
-  Real-time modification of device settings without restarting the application

Connection Process
~~~~~~~~~~~~~~~~~~

1. Launch ADIToFGUI from the bin folder
2. Select the appropriate configuration file (typically
   ``config_adsd3500_adsd3100.json``)
3. Choose a desired mode
4. Initiate playback to begin streaming frames

GPU Optimization for Point Cloud Rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When point cloud rendering performs slowly, ensure GPU acceleration is active.
For NVIDIA systems:

1. Navigate to the NVIDIA Control Panel
2. Add ``ADIToFGUI.exe`` as a program
3. Select "High-performance NVIDIA processor" in the settings

Eval Kit 4.3.0 or Earlier
-------------------------

Display Options
~~~~~~~~~~~~~~~

Two primary visualization modes are available:

Active Brightness and Depth
   Shows intensity in one window and depth measurements in millimeters in
   another. Real-time depth data is available via cursor hovering.

Point Cloud and Depth
   Generates 3D point cloud visualization alongside depth imagery.

Point Cloud Controls
~~~~~~~~~~~~~~~~~~~~

-  **Mouse wheel**: Zoom in/out
-  **Right-click drag**: Pan
-  **Left-click drag**: Rotate
-  **Slider**: Adjust point size visibility
