.. _eval_adsd3100_nxz software_installation:

Software Installation
===============================================================================

This installation guide covers the software packages for EVAL-ADSD3100-NXZ and
EVAL-ADTF3175-NXZ evaluation kits.

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

- **EVAL-ADSD3100-NXZ or EVAL-ADTF3175-NXZ users:** Download v2.1.1 installer
- **EVAL-ADTF3175D-NXZ users:** Download latest 5.x.x version

System Requirements
-------------------------------------------------------------------------------

- Seventh Gen Intel Core i5 Processor @ 2.4GHz (dual-core minimum)
- 8 GB RAM
- Graphics driver supporting OpenCL 2.0+

Installation Steps
-------------------------------------------------------------------------------

The installer guides users through the following steps:

Step 1: Introduction
~~~~~~~~~~~~~~~~~~~~

Launch the installer and click Next to begin.

.. figure:: images/s1.png
   :alt: Installation Introduction
   :align: center
   :width: 600

   Installation Introduction Screen

Step 2: License Agreement
~~~~~~~~~~~~~~~~~~~~~~~~~

Read and accept the license agreement to continue.

.. figure:: images/s2.png
   :alt: License Agreement
   :align: center
   :width: 600

   License Agreement Screen

Step 3: Installation Location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the installation location or accept the default.

.. figure:: images/s3.png
   :alt: Installation Location
   :align: center
   :width: 600

   Installation Location Selection

Step 4: Installation Progress
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The installer will automatically detect and install prerequisites:

- OpenCL 2.0 Runtime
- Visual Studio 2015 redistributable

Step 5: Completion
~~~~~~~~~~~~~~~~~~

After installation completes, the software is ready to use.

.. figure:: images/s5.png
   :alt: Installation Complete
   :align: center
   :width: 600

   Installation Complete

Image Folder Contents
-------------------------------------------------------------------------------

The installation includes the following folders:

.. figure:: images/image_folder.png
   :alt: Image Folder Contents
   :align: center
   :width: 400

   Image Folder Contents

- **microsd-xxxxxxxx:** NXP SOM SD card image with flashing instructions
- **fwUpdate_X.X.X:** ADSD3500 firmware with update procedures
- **depth_compute:** Depth compute binaries and documentation

Next Steps
-------------------------------------------------------------------------------

After installation, you can:

- Run :doc:`ADIToFGUI <aditofgui>` for camera visualization
- Use :doc:`Data Collect CLI <datacollect_cli>` for data acquisition
- Process data with :doc:`Depth Compute CLI <depthcompute_cli>`
