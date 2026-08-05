Data Collect CLI
================

The Data Collect CLI captures raw data from depth modules in ``.bin`` format,
which can be processed through the Depth Compute CLI to generate depth,
IR/active brightness, and XYZ frames.

Common Flags
------------

========= =============================================
Flag      Purpose
========= =============================================
``--f``   Output data folder
``--n``   Number of frames to capture
``--m``   Operation mode
``--wt``  Warmup time in seconds
``--ccb`` Calibration parameters file from device NVM
``--ip``  Camera IP address
``--fw``  ADSD3500 firmware file
``--h``   Display help information
========= =============================================

Eval Kit 6.0.0 or Later
-----------------------

Key change: Eliminates ``.ini`` files in favor of JSON-based parameter
management.

**Workflow:**

Save parameters::

   data_collect --ip 10.43.0.1 --scf my_params

Edit the resulting ``my_params.json`` file, then load parameters::

   data_collect --ip 10.43.0.1 --lcf my_params

Parameters can also be loaded in the GUI via Tools → Load Configuration.

Eval Kit 5.0.0
--------------

**Important Notes:**

-  Camera IP address is **10.43.0.1** (changed from earlier versions)
-  The ``--ft`` option was removed
-  Output is always ``.bin`` format containing active brightness, depth,
   confidence, and point cloud data

Eval Kit 4.3.0 or Earlier
-------------------------

-  Camera IP address: **10.42.0.1**
-  Supports the ``--ft`` flag for specifying frame type (raw/depth/ir/conf)
-  Depth is the default output

Hardware Example (EVAL-ADTF3175D-NXZ)
-------------------------------------

For kits with serial numbers like ``026am53200mb0ncca4``::

   data_collect.exe --f "data_output" --m 1 --n 1 --ip 10.43.0.1 config_adsd3500_adsd3100.json

The CCB file is only required for initial captures and can be reused for
subsequent depth compute operations.
