.. _eval_adtf3175_nxz aditofgui:

ADIToFGUI
===============================================================================

ADIToFGUI is the ToF module viewer application for the following modules:

- EVAL-ADTF3175-NXZ
- EVAL-ADTF3175D-NXZ
- EVAL-ADSD3100-NXZ

Eval Kit 5.0.0 or later
-------------------------------------------------------------------------------

With Eval Kit software 5.0.0 there have been some major updates to ADIToFGUI,
starting with the UX.

Usage
~~~~~

Connecting
^^^^^^^^^^

1. Open ADIToFGUI located in the installation "bin" folder.
2. Select the appropriate configuration JSON file and click Open:

   - For EVAL-ADTF3175-NXZ: **tof-viewer-config-adtf3175.json**

3. Select the desired mode and click Play.
4. Begin streaming frames.

New Features
~~~~~~~~~~~~

Adjusting the Ini Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is now possible to adjust some of the configuration parameters during use.
These parameters are generally stored in ini/JSON files on a per mode basis.
The ADSD3500 and depth compute libraries receive the changed parameter values.

The **Ini Parameter** window can be selected at any point. Select **Ini Params**
in the **Tools** menu.

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
2. Click Browse
3. Navigate to the installation bin folder and select ADIToFGUI.exe
4. For the selected program "ADIToFGUI" -> Select "High-performance NVIDIA
   processor" -> Apply

Eval Kit 4.3.0 or earlier
-------------------------------------------------------------------------------

Start
~~~~~

Locate ADIToFGUI.exe in the 'viewer' or 'bin' folder at the install location:

- **v2.x.x:** Default location: ``C:\Analog Devices\TOF_Evaluation_BM-RelX.X.X\viewer\``
- **v3.x.x:** Default location: ``C:\Analog Devices\TOF_Evaluation_BM-RelX.X.X\bin\``

For **EVAL-ADTF3175-NXZ** (only supported with software release 2.1.1):

1. Start the viewer
2. If a camera is connected it should show up in the 'Device' drop down menu
3. Select your device
4. Select config file: **tof-viewer-config-adtf3175.json**
5. Click 'Open Device'

Run Camera
~~~~~~~~~~

Once the device has been initialized the 'ToF Camera Options' menu should be
available. Available modes will depend on the module.

Select preferred view option and click play to run camera.

.. important::

   If the user disconnects the camera via USB-C cable while the GUI has
   initialized the camera, the user must restart the GUI.

Active Brightness and Depth
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If this option is selected:

- The first window shows active brightness/intensity
- The second window shows depth (in mm)

The user can hover over the image to see real-time depth data.

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
