.. _eval_adtf3175_nxz software_installation:

Software Installation
===============================================================================

This installation guide covers the software packages for EVAL-ADTF3175-NXZ
evaluation kits.

Overview
-------------------------------------------------------------------------------

The evaluation software includes three primary components:

- **ADIToFGUI** - Graphical interface for camera visualization
- **Data Collect** - Command-line interface for data acquisition
- **Depth Compute** - Command-line interface for depth calculations

Download
-------------------------------------------------------------------------------

.. admonition:: Download
   :class: download

   `Download the latest software package from GitHub <https://github.com/analogdevicesinc/ToF/releases>`_

- **EVAL-ADTF3175-NXZ users:** Download v2.1.1 installer
- **EVAL-ADTF3175D-NXZ users:** Download latest 5.x.x version

System Requirements
-------------------------------------------------------------------------------

- Seventh Gen Intel Core i5 Processor @ 2.4GHz (dual-core minimum)
- 8 GB RAM
- Graphics driver supporting OpenCL 2.0+

Installation Steps
-------------------------------------------------------------------------------

The installer guides users through the following steps:

1. **Introduction** - Launch the installer and click Next to begin
2. **License Agreement** - Read and accept the license agreement
3. **Installation Location** - Select the installation location or accept the
   default
4. **Prerequisites** - The installer will automatically detect and install:

   - OpenCL 2.0 Runtime
   - Visual Studio 2015 redistributable

5. **Completion** - After installation completes, the software is ready to use

Image Folder Contents
-------------------------------------------------------------------------------

The installation includes the following folders:

- **microsd-xxxxxxxx:** NXP SOM SD card image with flashing instructions
- **fwUpdate_X.X.X:** ADSD3500 firmware with update procedures
- **depth_compute:** Depth compute binaries and documentation

Next Steps
-------------------------------------------------------------------------------

After installation, you can:

- Run :doc:`ADIToFGUI <aditofgui>` for camera visualization
- Use :doc:`Data Collect CLI <datacollect_cli>` for data acquisition
- Process data with :doc:`Depth Compute CLI <depthcompute>`
