.. _eval_adsd3100_nxz auxtools:

Auxiliary Tools
===============================================================================

This page documents the Python tools available for the ToF evaluation kits.

Version 5.0.0 or Newer
-------------------------------------------------------------------------------

Python Setup
~~~~~~~~~~~~

**Requirements:** Python 3.10 (64-bit)

Windows Installation
^^^^^^^^^^^^^^^^^^^^

Execute the setup batch file from the TOF evaluation package.

Linux Installation
^^^^^^^^^^^^^^^^^^

Use Python virtual environment with pip package management:

.. code-block:: bash

   python3 -m venv tof_env
   source tof_env/bin/activate
   pip install -r requirements.txt

Examples
~~~~~~~~

first_frame.py
^^^^^^^^^^^^^^

Demonstrates retrieving a single camera frame with network or USB connectivity.

.. code-block:: bash

   python first_frame.py

depth-image-animation-pygame.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Streams and visualizes depth frames using PyGame engine.

.. code-block:: bash

   python depth-image-animation-pygame.py

skeletal_tracking.py
^^^^^^^^^^^^^^^^^^^^

Enables skeletal tracking capabilities using TensorFlow Lite.

.. code-block:: bash

   python skeletal_tracking.py

Available Operational Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 20 20

   * - Mode
     - Resolution
     - Description
   * - lr-native
     - 1024x1024
     - Long range native
   * - lr-qnative
     - 512x512
     - Long range quarter native
   * - lr-mixed
     - 512x512
     - Long range mixed
   * - sr-native
     - 1024x1024
     - Short range native
   * - sr-qnative
     - 512x512
     - Short range quarter native
   * - sr-mixed
     - 512x512
     - Short range mixed
   * - pcm-native
     - 1024x1024
     - PCM native

Tools
~~~~~

rawparser.py
^^^^^^^^^^^^

Parses the raw data of a frame and extracts the depth, AB, confidence and point
cloud data. Outputs are saved as PNG and PLY files.

.. code-block:: bash

   python rawparser.py --input data_output_0.bin --mode lr-native

saveCCBToFile.py
^^^^^^^^^^^^^^^^

Saves camera configuration files locally from connected devices.

.. code-block:: bash

   python saveCCBToFile.py --ip 10.43.0.1 --output camera_config.ccb

Version 4.3.0 or Older
-------------------------------------------------------------------------------

.. important::

   These utilities were removed starting with version 5.0.0.

Dependencies
~~~~~~~~~~~~

Miniconda environment with Python 3.9 virtual setup.

Deprecated Tools
~~~~~~~~~~~~~~~~

Depth Compute
^^^^^^^^^^^^^

Processed raw capture files to generate depth and point cloud outputs.

This functionality is now integrated into the main pipeline.

FSF Extraction
^^^^^^^^^^^^^^

Extracted video stream data from FSF format files supporting AB, depth, and
XYZ information.

This format is no longer used in newer versions.
