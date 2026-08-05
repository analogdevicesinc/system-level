Depth Compute
=============

Depth Compute CLI
-----------------

.. note::

   This tool was removed from the host starting with Eval Kit version 5.0.0.

The Depth Compute CLI processes data from the Data Collect CLI to generate
three types of outputs:

RadialDepth folder
   Depth images measuring distance radially from the lens center

AB folder
   Active Brightness images where the value at each pixel is the intensity of
   the return laser light

XYZ folder
   Point cloud data with real-world Cartesian coordinates for each pixel

Usage Example
~~~~~~~~~~~~~

For EVAL-ADTF3175D-NXZ, use two commands depending on collection mode (MP or
QMP)::

   tofi_compute_depth.exe --I=../data_output --CCB=../crXXX.ccb --MODE=1 --O=../proc_data --INI=../config/RawToDepthAdsd3500.ini

Use the appropriate INI configuration file with ``ISP_Enable=1``.

Visualization Commands
~~~~~~~~~~~~~~~~~~~~~~

The toolkit includes Python scripts for output analysis::

   visualize_depth.py
   visualize_ab.py
   visualize_pointcloud.py

Depth Compute Libraries
-----------------------

The ADTF3175D evaluation kit requires depth compute binaries to convert raw
data to depth data.

The installers are packaged within an image download zipfile accessible through
the GitHub-based installer. Consult the :doc:`getting_started` guide for
detailed download instructions.

**Windows Options:**

-  GPU variant: ``TOF_DepthComputeEngine_Windows-RelX.X.0.exe``
-  CPU variant: ``TOF_DepthComputeEngine_Windows-RelX.X.1.exe``
   (default in GitHub Installer 3.2.0)

**Linux Options:**

-  GPU variant: ``TOF_DepthComputeEngine_Linux-RelX.X.0``
-  CPU variant: ``TOF_DepthComputeEngine_Linux-RelX.X.1``

Both Windows and Linux distributions support OpenCL-based processing through
GPU or CPU implementations.

Depth Compute Parameters
------------------------

.. important::

   This section has been deprecated and replaced by an App note that is available
   from the ADI ToF Team.

The ADSD3100 and ADSD3030 generate raw depth data which is processed using ADI's
proprietary depth compute pipeline. The user is able to modify some of the depth
compute parameters to tune performance to a specific application.

Where can the user modify these parameters?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While running the SDK, one of the inputs for initializing the camera is an ini
file. This file contains control to depth compute parameters as well as ADSD3500
control (only enabled if used).

For example:

**DEPTH COMPUTE PARAMETERS (Recommended Settings)**

-  abThreshMin=3.0
-  abSumThresh=25.0
-  confThresh=25.0
-  radialThreshMin=100.0
-  radialThreshMax=10000.0
-  jblfApplyFlag=1
-  jblfWindowSize=7
-  jblfGaussianSigma=10.0
-  jblfExponentialTerm=5.0
-  jblfMaxEdge=12.0
-  jblfABThreshold=10.0

**ADSD3500 Configuration Parameters (Depends on mode)**

-  headerSize=0
-  deltaCompEnable=0
-  inputFormat=raw8
-  depthComputeIspEnable=1
-  partialDepthEnable=0
-  interleavingEnable=1
-  bitsInPhaseOrDepth=16
-  bitsInConf=8
-  bitsInAB=16
-  phaseInvalid=0
-  xyzEnable=1

Parameter Reference
~~~~~~~~~~~~~~~~~~~

+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Name                                 | Unit    | Function                                                                                                                                                                                                                                                                                                                                                                                                | Range                                                | Notes                                                                                          |
+======================================+=========+=========================================================================================================================================================================================================================================================================================================================================================================================================+======================================================+================================================================================================+
| abThreshMin                          | -       | Per-frequency active brightness invalidation threshold. Any pixel with at least one per-frequency active brightness value below abThreshMin will have an invalid depth value. To turn off per-frequency active brightness invalidation, set abThreshMin=0.                                                                                                                                              | AB output bitwidth (16-bit = 0 – 65,535)             | ADSD3500 Command: SET AB INVALIDATION THRESHOLD                                                |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| abSumThresh (DEPRECATED)             | -       | Any Pixel with an active brightness (IR) value of less than threshold value will be invalidated                                                                                                                                                                                                                                                                                                         | AB output bitwidth (16-bit = 0 – 65,535)             | N/A                                                                                            |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| confThresh                           | degrees | Phase unwrapping confidence invalidation threshold. Any pixel with a phase unwrapping confidence value larger than confThresh will have an invalid depth value. To turn off, set confThresh to 360                                                                                                                                                                                                      | 0 – 360                                              | ADSD3500 Command: SET CONFIDENCE THRESHOLD                                                     |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| radialThreshMin                      | mm      | Minimum distance radial distance invalidation threshold. Any pixel with radial depth less than radialThreshMin is invalidated                                                                                                                                                                                                                                                                           |                                                      | ADSD3500 Command: SET RADIAL THRESHOLD MIN                                                     |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| radialThreshMax                      | mm      | Maximum distance radial distance invalidation threshold. Any pixel with radial depth higher than radialThreshMin is invalidated                                                                                                                                                                                                                                                                         |                                                      | ADSD3500 Command: SET RADIAL THRESHOLD MAX                                                     |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| jblfApplyFlag                        | bool    | Enable or Disable JBLF filter (Noise reduction). jblfApplyFlag=0 disables filter. jblfApplyFlag=1 enables filter.                                                                                                                                                                                                                                                                                       | [0,1]                                                | ADSD3500 Command: ENABLE/DISABLE JBLF FILTER                                                   |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| jblfWindowSize                       | pixel   | Select JBLF filter window size. Size of kernel is set to jblfWindowSize pixels x jblfWindowSize pixels. Increasing the size will further reduce noise at the expense of computation cost (compute power).                                                                                                                                                                                               | [3, 5, 7]                                            | ADSD3500 Command: SET JBLF FILTER SIZE                                                         |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| jblfGaussianSigma                    | pixel   | Noise reduction filter spatial Gaussian kernel width. Defines the width of the Gaussian kernel in the noise reduction filter. Setting a small value (such as 0.1) effectively disables the noise reduction. Setting a value much larger than jblfWindowSize (such as 100) provides the largest amount of noise reduction (increases depth range) at the expense of a blurrier depth image.              |                                                      | N/A to the ADSD3500                                                                            |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| jblfExponentialTerm                  |         | Noise reduction filter edge preservation strength. Defines the amount of depth edge preservation in the noise reduction filter. Set jblfExponentialTerm=0 to disable edge preservation. Set large value to preserve more depth edges.                                                                                                                                                                   |                                                      | N/A to the ADSD3500                                                                            |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| jblfMaxEdge                          |         | Noise reduction filter edge invalidation threshold. Defines the depth "edgeness" above which a pixel depth value is invalid. If a pixel per-frequency active brightness is below jblfABThreshold, jblfMaxEdge is set to infinity for that pixel, which disables edge invalidation for that pixel                                                                                                        |                                                      | N/A to the ADSD3500                                                                            |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| jblfABThreshold                      |         | See jblfMaxEdge.                                                                                                                                                                                                                                                                                                                                                                                        |                                                      | N/A to the ADSD3500                                                                            |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| headerSize                           |         | Embedded header size (RAW8 / bytes). It can be either 0 or 128                                                                                                                                                                                                                                                                                                                                          |                                                      |                                                                                                |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| deltaCompEnable                      |         | Instructs the depth compute library to Delta de-compression the data from the imager. 0 - Data is already decompressed ;1 - decompress the data from the imager.                                                                                                                                                                                                                                        |                                                      | Consumed by depth compute library                                                              |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| inputFormat                          |         | MIPI input data from from the ADSD3500. See                                                                                                                                                                                                                                                                                                                                                             |                                                      | Consumed by depth compute library                                                              |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| depthComputeIspEnable                |         | Instructs depth compute library whether it is ISP use case .1 - depth/phase is computed using ADSD3500; 0 - Depth is computed using depth compute library.                                                                                                                                                                                                                                              |                                                      | Consumed by depth compute library                                                              |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| partialDepthEnable                   |         | Instructs the depth compute library whether is a full depth use case or partial depth use case .1- Phase unwrapping is done using depth compute library (MP resolution);0 - depth is computed using ADSD3500 (QMP resolution). Radial to XYZ is done using depth compute library                                                                                                                        |                                                      | Consumed by depth compute library and ADSD3500 Command: SET IMAGER MODE COMMAND (bits 0 and 3) |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| interleavingEnable                   |         | Instructs the ADSD3500 to generated interleaved data on MIPI or use virtual channels. See                                                                                                                                                                                                                                                                                                               |                                                      | ADSD3500 Command: SET IMAGER MODE COMMAND (bit 1)                                              |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| bitsInPhaseOrDepth                   |         | Instructs the ADSD3500 how many bits to use for the phase or depth frames. See                                                                                                                                                                                                                                                                                                                          |                                                      | ADSD3500 Command: SET IMAGER MODE COMMAND (bits 6:4)                                           |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| bitsInConf                           |         | Instructs the ADSD3500 how many bits to use for Confidence data or to disable Confidence data. See                                                                                                                                                                                                                                                                                                      |                                                      | ADSD3500 Command: SET IMAGER MODE COMMAND (bits 11:10)                                         |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| bitsInAB                             |         | Instructs the ADSD3500 how many bits to use for AB data. See                                                                                                                                                                                                                                                                                                                                            |                                                      | ADSD3500 Command: SET IMAGER MODE COMMAND (bits 9:7)                                           |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| phaseInvalid                         |         | Instructs depth compute library to invalidate the pixel based on this value. It is introduced to make depth compute library in line with ADSD3500                                                                                                                                                                                                                                                       |                                                      | Consumed by depth compute library                                                              |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| xyzEnable                            | bool    | Enables generation of XYZ frames by depth compute library. 0 - disable generation of XYZ frames; 1 - enable generation of XYZ frames                                                                                                                                                                                                                                                                    |                                                      | Consumed by depth compute library                                                              |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+------------------------------------------------------------------------------------------------+

inputFormat
^^^^^^^^^^^

-  mipiRaw12 - Input data is 12-bit packed in mipiraw12format. This is the raw data output of ADSD3030.
-  mipiRaw12_11 -Input Data is 12- bit packed in mipiraw12 format with 12th bit as 0. This is the raw data output of ADSD3100.
-  raw8 - Raw8 compressed input
-  raw16 - Input data is already unpacked.
-  raw16_bits11_shift4 - ADSD3100: When ADSD3100 is interfaced with NXP, input data will be unpacked and shifted by 4 bits.
-  raw16_bits11_shift0 - ADSD3100: When ADSD3100 is interfaced with NXP, input data will be unpacked by NXP.
-  raw16_bits12_shift4 - ADSD3030: When ADSD3030 is interfaced with NXP, input data will be unpacked and shifted by 4 bits.
-  raw16_bits12_shift0 - ADSD3030: When ADSD3030 is interfaced with NXP, input
   data will be unpacked by NXP.

interleavingEnable
^^^^^^^^^^^^^^^^^^

Instructs the ADSD3500 to generated interleaved data on MIPI or use virtual
channels.

-  0 - use virtual channels
-  1 - enable interleaving

bitsInPhaseOrDepth
^^^^^^^^^^^^^^^^^^

Instructs the ADSD3500 how many bits to use for the phase or depth frames.

-  8 - 8-bits depth
-  10 - 10-bits depth
-  12 - 12-bits depth
-  14 - 14-bits depth
-  16 - 16-bits depth

bitsInConf
^^^^^^^^^^

Instructs the ADSD3500 how many bits to use for Confidence data or to disable
Confidence data.

-  0 - Off;
-  4 - 4-bits confidence;
-  8 - 8-bits confidence

bitsInAB
^^^^^^^^

Instructs the ADSD3500 how many bits to use for AB data.

-  8 - 8-bits AB
-  10 - 10-bits AB
-  12 - 12-bits AB
-  14 - 14-bits AB
-  16 - 16-bits AB
