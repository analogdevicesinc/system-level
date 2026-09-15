.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli

.. _eval-adsd3100-nxz-gui datacollect_cli:

Data Collect, Eval Kit 6.0.0 or later
=====================================

Description
-----------

The Data Collect CLI can collect raw data from the depth module in .bin format.
This be run through the
:dokuwiki:`Depth Compute CLI </resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`
to convert to Depth, IR/AB(Active brightness), and XYZ frames

Use *data_collect –help* to show functionality.

One important change is the removal of ini files. Instead default values are
used by the system. To change the values the following process can be used:

- Save the parameters, for example, *data_collect –ip 10.43.0.1 –scf my_params*
- Edit the *my_params.json* by finding the mode you want to change.
- Use the save parameters, for example, *data_collect –ip 10.43.0.1 –lcf
  my_params*

Note, you can also use *my_params.json* in the GUI via *Tools->Load
Configuration*.

Here is an example of mode of in *my_params.json* file. <blockquote>

::

   "0":    {
       "depth-compute":    {
           "abThreshMin":  3,
           "bitsInAB": 16,
           "bitsInConf":   0,
           "bitsInPhaseOrDepth":   12,
           "confThresh":   25,
           "depthComputeIspEnable":    1,
           "inputFormat":  "mipiRaw12_8",
           "interleavingEnable":   0,
           "jblfABThreshold":  10,
           "jblfApplyFlag":    1,
           "jblfExponentialTerm":  5,
           "jblfGaussianSigma":    10,
           "jblfMaxEdge":  12,
           "jblfWindowSize":   7,
           "partialDepthEnable":   1,
           "phaseInvalid": 0,
           "radialThreshMax":  4200,
           "radialThreshMin":  30
       },
       "configuration-parameters": {
           "fps":  10,
           "headerSize":   128,
           "xyzEnable":    1
       }
   },

</blockquote>

Data Collect, Eval Kit 5.0.0
----------------------------

.. important::

   Camera IP is **10.43.0.1** if you are using SDK **v5.0.0** or later.

.. important::

   In eval kit **v5.0.0** –ft option is removed. The output of data collect is a
   **.bin** file which contain Active brightness, depth, confidence and point
   cloud. These frames can be visualized using **ADIToFGUI.**

Description
-----------

The Data Collect CLI can collect raw data from the depth module in .bin format.
This be run through the
:dokuwiki:`Depth Compute CLI </resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`
to convert to Depth, IR/AB(Active brightness), and XYZ frames

Flag descriptions:

- –f : output data folder
- –n : number of frames captured
- –m : mode ( Check correct mode numbers for your kit here :
  :dokuwiki:`mode_table </resources/eval/user-guides/eval-adtf3175d-nxz/mode_table>`)
- –wt : warmup time (seconds)
- –ccb : stores ccb (Calibration parameters) file stored on NVM of imager
  module. Required for Depth Compute
- –ip: Camera IP
- –fw: Adsd3500 fw file
- –split: Save each frame into a separate file (DEBUG only)
- –netlinktest: Used to test network performance (DEBUG only)
- –h : Call help string for all options

More information can be found in readme

EVAL-ADTF3175D-NXZ Example
~~~~~~~~~~~~~~~~~~~~~~~~~~

Since the ADTF3175D eval kit works via ethernet over usb, the user must specify
the static ip of the camera module

- Open Command Prompt from start menu and move to bin folder in GUI install
  location.
- Please check the serial number of your kit to run the correct command
- Run the following command if your serial number is similar to this
  026am53200mb0ncca4 : (lr-native, 1 frame capture, get ccb) with latest GUI
  release:

  - data_collect.exe –f ``data_output`` –m 1 –n 1 –ip 10.43.0.1
    config_adsd3500_adsd3100.json

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-data_collect.png
   :width: 800px

--------------

Data Collect, Eval Kit 4.3.0 or earlier
---------------------------------------

Description
-----------

The Data Collect CLI can collect raw data from the depth module in .bin format.
This be run through the
:dokuwiki:`Depth Compute CLI </resources/eval/user-guides/eval-adsd3100-nxz/depthcompute_cli>`
to convert to Depth, IR/AB(Active brightness), and XYZ frames

Flag descriptions:

- –f : output data folder
- –n : number of frames captured
- –m : mode ( Check correct mode numbers for your kit here :
  :dokuwiki:`mode_table </resources/eval/user-guides/eval-adtf3175d-nxz/mode_table>`)
- –wt : warmup time (seconds)
- –ccb : stores ccb (Calibration parameters) file stored on NVM of imager
  module. Required for Depth Compute
- –ip: Camera IP
- –fw: Adsd3500 fw file
- –ft: FrameType of saved image (raw/depth/ir/conf) [default: depth]
- –h : Call help string for all options

More information can be found in readme

EVAL-ADTF3175D-NXZ Example
~~~~~~~~~~~~~~~~~~~~~~~~~~

Since the ADTF3175D eval kit works via ethernet over usb, the user must specify
the static ip of the camera module

- Open Command Prompt from start menu and move to bin folder in GUI install
  location.
- Please check the serial number of your kit to run the correct command
- Run the following command if your serial number starts with DV11 or CR :
  (lr-native (mp), 1 frame capture, get ccb):

  - data_collect.exe –f ``data_output`` –m 10 –n 1 –ccb ../crXXX.ccb –ip
    10.42.0.1 tof-viewer_config.json

- Run the following command if your serial number is similar to this
  026am53200mb0ncca4 : (lr-native, 1 frame capture, get ccb) with latest GUI
  release:

  - data_collect.exe –f ``data_output`` –m 1 –n 1 –ccb ../crXXX.ccb –ip
    10.42.0.1 –ft raw config_adsd3500_adsd3100.json

.. important::

   Version: for 4.3.0, data collect"s default output is depth image. To get
   **raw frame** use **–ft** command line argument with **"RAW"** option. Refer
   data_collect –h for mode command line options.

   The get ccb flag is only required for the first capture. Once the ccb of your
   module is stored, it can be reused while running tofi_depth_compute.exe

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adsd3100-nxz-gui/data_collect_ip.png
