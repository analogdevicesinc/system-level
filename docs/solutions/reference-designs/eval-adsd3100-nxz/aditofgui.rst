.. _eval_adsd3100_nxz aditofgui:

ADIToFGUI
===============================================================================

ADIToFGUI is the ToF module viewer application for the following modules:

- EVAL-ADSD3100-NXZ
- EVAL-ADTF3175-NXZ
- EVAL-ADTF3175D-NXZ

Eval Kit 5.0.0 or later
-------------------------------------------------------------------------------

With Eval Kit software 5.0.0 there have been some major updates to ADIToFGUI,
starting with the UX.

Usage
~~~~~

Connecting
^^^^^^^^^^

1. Open ADIToFGUI located in the installation "bin" folder.

.. figure:: images/adi-tof-nvidia-aditofgui-1.png
   :alt: ADIToFGUI Launch
   :align: center
   :width: 600

   ADIToFGUI Launch Screen

2. Select "config_adsd3500_adsd3100.json" and click Open.

.. figure:: images/adi-tof-nvidia-aditofgui-2.png
   :alt: Select Configuration
   :align: center
   :width: 600

   Select Configuration File

3. Select the desired mode and click Play.

.. figure:: images/adi-tof-nvidia-aditofgui-3.png
   :alt: Select Mode
   :align: center
   :width: 600

   Select Mode and Play

4. Streaming frames.

.. figure:: images/adi-tof-nvidia-aditofgui-4.png
   :alt: Streaming Frames
   :align: center
   :width: 600

   Streaming Frames

New Features
~~~~~~~~~~~~

Adjusting the Ini Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is now possible to adjust some of the configuration parameters during use.
These parameters are generally stored in ini/JSON files on a per mode basis.
The ADSD3500 and depth compute libraries receive the changed parameter values.

The **Ini Parameter** window can be selected at any point. Select **Ini Params**
in the **Tools** menu.

.. figure:: images/adi-tof-aditofgui-ini-1.png
   :alt: Ini Params Menu
   :align: center
   :width: 300

   Tools Menu - Ini Params

Once opened the **Ini Parameter** window can be used to adjust the parameters.

.. figure:: images/adi-tof-aditofgui-ini-2.png
   :alt: Ini Parameter Window
   :align: center
   :width: 600

   Ini Parameter Window

- **Modify** - Write parameters to the device. The stream is stopped, the
  ADSD3500 and depth compute library updated, then the stream is restarted.
- **Reset** - Set the values back to those from the original ini file.
- **Save** - Save the parameters to a file.

Troubleshooting
~~~~~~~~~~~~~~~

Slow Point Cloud Rendering
^^^^^^^^^^^^^^^^^^^^^^^^^^

If rendering of the point cloud is slow, it may be necessary to ensure the GPU
is rendering and not the CPU. With an NVIDIA GPU you can do the following:

1. Open NVIDIA Control Panel -> Manage 3D Settings -> Program Settings -> Add

.. figure:: images/adi-tof-nvidia-control_panel_1.png
   :alt: NVIDIA Control Panel Step 1
   :align: center
   :width: 600

   NVIDIA Control Panel - Add Program

2. Click Browse

.. figure:: images/adi-tof-nvidia-control_panel_2.png
   :alt: NVIDIA Control Panel Step 2
   :align: center
   :width: 600

   Browse for Application

3. Navigate to the installation bin folder and select ADIToFGUI.exe

.. figure:: images/adi-tof-nvidia-control_panel_3.png
   :alt: NVIDIA Control Panel Step 3
   :align: center
   :width: 600

   Select ADIToFGUI.exe

4. For the selected program "ADIToFGUI" -> Select "High-performance NVIDIA
   processor" -> Apply

.. figure:: images/adi-tof-nvidia-control_panel_4.png
   :alt: NVIDIA Control Panel Step 4
   :align: center
   :width: 600

   Select High-performance NVIDIA processor

Eval Kit 4.3.0 or earlier
-------------------------------------------------------------------------------

Start
~~~~~

Locate ADIToFGUI.exe in the 'viewer' or 'bin' folder at the install location:

- **v2.x.x:** Default location: ``C:\Analog Devices\TOF_Evaluation_BM-RelX.X.X\viewer\``
- **v3.x.x:** Default location: ``C:\Analog Devices\TOF_Evaluation_BM-RelX.X.X\bin\``

For **EVAL-ADTF3175D-NXZ:**

1. Confirm that an unidentified local network has been discovered by the PC
   (IP address = 10.42.0.1)
2. Run the application
3. Hit refresh until a Device is found
4. **Select .json file based on your kit's serial number** (Software Release
   version 4.2.0+):

   - If your serial number starts with 'DV11' or 'CR' select
     **tof-viewer_config.json**
   - If your serial number starts with 'am' select
     **tof_crosby_adsd3500_new_modes_config.json**

For **EVAL-ADTF3175-NXZ** or **EVAL-ADSD3100-NXZ** (only supported with software
release 2.1.1):

1. Start the viewer
2. If a camera is connected it should show up in the 'Device' drop down menu
3. Select your device
4. Select correct config file:

   - EVAL-ADTF3175-NXZ: **tof-viewer-config-adtf3175.json**
   - EVAL-ADSD3100-NXZ: **tof-viewer-config-adsd3100.json**

5. Click 'Open Device'

.. figure:: images/selecting_config.png
   :alt: Selecting Configuration
   :align: center

   Selecting Configuration File

Run Camera
~~~~~~~~~~

Once the device has been initialized the 'ToF Camera Options' menu should be
available. Available modes will depend on the module serial number (see
:ref:`Mode Table <eval_adsd3100_nxz>` in the main page).

Select preferred view option and click play to run camera.

.. figure:: images/gui_initialization_screen.png
   :alt: GUI Initialization
   :align: center

   GUI Initialization Screen

.. important::

   If the user disconnects the camera via USB-C cable while the GUI has
   initialized the camera, the user must restart the GUI.

Active Brightness and Depth
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If this option is selected:

- The first window shows active brightness/intensity
- The second window shows depth (in mm)

The user can hover over the image to see real-time depth data.

.. figure:: images/ab_and_depth.png
   :alt: Active Brightness and Depth
   :align: center

   Active Brightness and Depth View

Mode Switching
~~~~~~~~~~~~~~

To switch modes while the camera is running:

1. Click 'Stop'
2. Select mode in drop down menu
3. Click 'Play'

Point Cloud and Depth
~~~~~~~~~~~~~~~~~~~~~

To switch to Point Cloud view:

1. Click 'Stop'
2. Select 'Point Cloud and Depth'
3. Click 'Play'

The first window shows a point-cloud generated from the depth on the second
window.

.. figure:: images/adtf3175_depth_pc.png
   :alt: Point Cloud and Depth
   :align: center

   Point Cloud and Depth View

**Point Cloud Controls:**

- **Zoom In/Out** - Use the mouse wheel
- **Pan** - Drag the mouse while pressing the right mouse button
- **Rotate** - Drag the mouse while pressing the left mouse button
- **Point Size** - Use the slider at the bottom of the Point Cloud window
- **Reset View** - Press the "Reset View" button

Recording
~~~~~~~~~

.. important::

   Recording via the GUI is deprecated. Please use :doc:`Data Collect CLI
   <datacollect_cli>` for recording data during evaluation.
