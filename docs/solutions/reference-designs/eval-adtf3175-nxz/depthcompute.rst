.. _eval_adtf3175_nxz depthcompute:

Depth Compute
===============================================================================

The Depth Compute CLI processes data from the :doc:`Data Collect CLI <datacollect_cli>`
to generate three types of output frames.

.. important::

   This tool has been removed from the host starting with Eval Kit version 5.0.0.

Output Folders
-------------------------------------------------------------------------------

RadialDepth
~~~~~~~~~~~

Depth images where the depth at each pixel is the distance to the corresponding
point in the scene measured 'radially' from the center of the lens.

AB (Active Brightness)
~~~~~~~~~~~~~~~~~~~~~~

Active Brightness images showing laser return intensity from scene points
(IR frame).

XYZ
~~~

Point cloud data with real-world Cartesian coordinates (X, Y, Z) for each pixel.
The Z image alone functions as a distance measurement from the camera plane.

Usage
-------------------------------------------------------------------------------

EVAL-ADTF3175-NXZ
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   tofi_compute_depth.exe --I=../data_output --CCB=../crXXX.ccb --MODE=10 --O=../proc_data --INI=../config/RawToDepth.ini

Parameters:

- ``--I`` : Input data folder
- ``--CCB`` : Camera calibration file
- ``--MODE`` : Mode index (10 for mp, 7 for qmp)
- ``--O`` : Output folder
- ``--INI`` : INI configuration file

Visualization
-------------------------------------------------------------------------------

Use the provided Python scripts to visualize the output:

Visualize Depth
~~~~~~~~~~~~~~~

.. code-block:: bash

   python tools\depth_compute\visualize_depth.py proc_data\RadialDepth\data_output_0.bin 1024 1024

Visualize Active Brightness
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python tools\depth_compute\visualize_ab.py proc_data\AB\data_output_0.bin 1024 1024

Visualize Point Cloud
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python tools\depth_compute\visualize_pointcloud.py 1024 1024 proc_data\XYZ\data_output_0.bin

Parameters
-------------------------------------------------------------------------------

Users adjust depth compute parameters through an initialization INI file during
SDK runtime. This file also controls ADSD3500 settings when applicable.

Recommended Settings
~~~~~~~~~~~~~~~~~~~~

Example baseline configuration:

.. code-block:: ini

   [depth-compute]
   abThreshMin = 3.0
   confThresh = 25.0
   radialThreshMin = 100
   radialThreshMax = 10000
   jblfApplyFlag = 1
   jblfWindowSize = 7
   jblfGaussianSigma = 10

Parameter Reference
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 15 60

   * - Parameter
     - Unit
     - Description
   * - abThreshMin
     - --
     - Per-frequency brightness invalidation threshold. Ranges across 16-bit
       AB bitwidth.
   * - confThresh
     - degrees
     - Phase unwrapping confidence threshold (0-360 degrees).
   * - radialThreshMin
     - mm
     - Minimum distance-based invalidation boundary.
   * - radialThreshMax
     - mm
     - Maximum distance-based invalidation boundary.
   * - jblfApplyFlag
     - bool
     - Enables (1) or disables (0) noise reduction filtering.
   * - jblfWindowSize
     - pixels
     - Filter kernel dimension. Options: 3, 5, 7.
   * - jblfGaussianSigma
     - --
     - Gaussian sigma value for the joint bilateral filter.
   * - jblfABThreshold
     - --
     - Active brightness threshold for the filter.
   * - jblfExponentialTerm
     - --
     - Exponential term for the filter calculation.
   * - jblfMaxEdge
     - --
     - Maximum edge value for filtering.
   * - partialDepthEnable
     - bool
     - Enable partial depth computation.
   * - phaseInvalid
     - --
     - Phase invalid marker value.
   * - bitsInPhaseOrDepth
     - bits
     - Number of bits allocated for phase or depth data.

ADSD3500 Configuration Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Parameter
     - Description
   * - inputFormat
     - Input data format specification
   * - bitsInAB
     - Bits allocated for active brightness
   * - bitsInConf
     - Bits allocated for confidence data
   * - interleavingEnable
     - Enable interleaving mode
   * - xyzEnable
     - Enable XYZ frame generation

Input Format Options
~~~~~~~~~~~~~~~~~~~~

Eight input format variants are available:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Format
     - Description
   * - mipiRaw12
     - Standard MIPI RAW12 format
   * - mipiRaw12_8
     - MIPI RAW12 with 8-bit packing
   * - raw8
     - Compressed RAW8 format
   * - raw16
     - Standard RAW16 format
   * - raw16_unpacked
     - Unpacked RAW16 for NXP interface
   * - raw16_unpacked_high
     - High bits unpacked RAW16
   * - raw16_unpacked_low
     - Low bits unpacked RAW16
   * - compressed_raw8
     - Compressed 8-bit format

Libraries
-------------------------------------------------------------------------------

The ADTF3175D kits require depth compute binaries to convert raw data to depth
data. These binaries are necessary for the SDK to function properly during the
build process.

The installers are located within an image download package available through
the GitHub installer. See :doc:`Software Installation <software_installation>`
for download instructions.

Windows Binaries
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Version
     - Type
     - Description
   * - X.X.0
     - GPU-accelerated
     - OpenCL version using GPU acceleration
   * - X.X.1
     - CPU-based
     - OpenCL version using CPU (default in GitHub Installer 3.2.0)

Linux Binaries
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Version
     - Type
     - Description
   * - X.X.0
     - GPU-accelerated
     - OpenCL version using GPU acceleration
   * - X.X.1
     - CPU-based
     - OpenCL version using CPU

Selection Guide
~~~~~~~~~~~~~~~

- Use **GPU-accelerated** version (X.X.0) if your system has a compatible GPU
  with OpenCL support for best performance.
- Use **CPU-based** version (X.X.1) if you don't have a compatible GPU or
  experience issues with the GPU version.

.. note::

   The CPU-based version is set as the default in GitHub Installer 3.2.0 and
   later for maximum compatibility.
