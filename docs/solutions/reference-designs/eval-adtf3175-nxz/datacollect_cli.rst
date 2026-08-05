.. _eval_adtf3175_nxz datacollect:

Data Collect CLI
===============================================================================

The Data Collect CLI collects raw data from the depth module in .bin format.
This data can be processed through the :doc:`Depth Compute CLI <depthcompute>`
to convert to Depth, IR/AB (Active brightness), and XYZ frames.

Use ``data_collect --help`` to show functionality.

Eval Kit 6.0.0 or later
-------------------------------------------------------------------------------

One important change is the removal of ini files. Instead, default values are
used by the system. To change the values, use the following process:

1. Save the parameters::

      data_collect --ip 10.43.0.1 --scf my_params

2. Edit the ``my_params.json`` by finding the mode you want to change.

3. Load the saved parameters::

      data_collect --ip 10.43.0.1 --lcf my_params

.. note::

   You can also use ``my_params.json`` in the GUI via **Tools -> Load Configuration**.

Example Configuration
~~~~~~~~~~~~~~~~~~~~~

Here is an example of a mode configuration in ``my_params.json``:

.. code-block:: json

   "0": {
       "depth-compute": {
           "abThreshMin": 3,
           "bitsInAB": 16,
           "bitsInConf": 0,
           "bitsInPhaseOrDepth": 12,
           "confThresh": 25,
           "depthComputeIspEnable": 1,
           "inputFormat": "mipiRaw12_8",
           "jblfApplyFlag": 1,
           "jblfWindowSize": 7,
           "radialThreshMax": 4200,
           "radialThreshMin": 30
       },
       "configuration-parameters": {
           "fps": 10,
           "headerSize": 128,
           "xyzEnable": 1
       }
   }

Eval Kit 5.0.0
-------------------------------------------------------------------------------

.. important::

   Camera IP is **10.43.0.1** if you are using SDK v5.0.0 or later.

.. important::

   In eval kit v5.0.0 the ``--ft`` option is removed. The output of data collect
   is a .bin file which contains Active brightness, depth, confidence and point
   cloud. These frames can be visualized using ADIToFGUI.

Flag Descriptions
~~~~~~~~~~~~~~~~~

- ``--f`` : output data folder
- ``--n`` : number of frames captured
- ``--m`` : mode (10 for mp, 7 for qmp)
- ``--wt`` : warmup time (seconds)
- ``--ccb`` : stores ccb (Calibration parameters) file stored on NVM of imager
  module. Required for Depth Compute
- ``--ip`` : Camera IP
- ``--fw`` : ADSD3500 firmware file
- ``--split`` : Save each frame into a separate file (DEBUG only)
- ``--netlinktest`` : Used to test network performance (DEBUG only)
- ``--h`` : Call help string for all options

Example
~~~~~~~

Since the eval kit works via ethernet over USB, the user must specify the
static IP of the camera module.

1. Open Command Prompt from start menu and move to bin folder in GUI install
   location.
2. Run the following command (mp mode, 1 frame capture)::

      data_collect.exe --f "data_output" --m 10 --n 1 --ip 10.43.0.1 tof-viewer-config-adtf3175.json

Eval Kit 4.3.0 or earlier
-------------------------------------------------------------------------------

Flag Descriptions
~~~~~~~~~~~~~~~~~

- ``--f`` : output data folder
- ``--n`` : number of frames captured
- ``--m`` : mode (10 for mp, 7 for qmp)
- ``--wt`` : warmup time (seconds)
- ``--ccb`` : stores ccb (Calibration parameters) file stored on NVM of imager
  module. Required for Depth Compute
- ``--ip`` : Camera IP
- ``--fw`` : ADSD3500 firmware file
- ``--ft`` : FrameType of saved image (raw/depth/ir/conf) [default: depth]
- ``--h`` : Call help string for all options

Example
~~~~~~~

Run the following command (mp mode, 1 frame capture, raw output)::

   data_collect.exe --f "data_output" --m 10 --n 1 --ccb ../crXXX.ccb --ip 10.42.0.1 --ft raw tof-viewer-config-adtf3175.json

.. important::

   For version 4.3.0, data collect's default output is depth image. To get raw
   frame use ``--ft`` command line argument with 'RAW' option.

   The ``--ccb`` flag is only required for the first capture. Once the ccb of
   your module is stored, it can be reused while running ``tofi_depth_compute.exe``.
