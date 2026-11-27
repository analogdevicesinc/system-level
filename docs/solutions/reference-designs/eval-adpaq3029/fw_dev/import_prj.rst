.. _eval-adpaq3029 fw_dev import_prj:

EVAL-ADPAQ3029 - Importing CCES project
=======================================

Please see the :ref:`resources <eval-adpaq3029 resources>` section to download source code.

-  Launch the CCES IDE on your host & create a new workspace.
-  Click on ``File`` -> ``Import..`` or click ``Import an existing CCES project`` from homepage as shown below.
-  Then select ``General``-> ``Existing Projects into Workspace``.
-  Then choose the source code directory to import one or more projects from the
   selected directory

.. image:: ../images/sw10.png
   :align: center
   :width: 600

The module application runs on the bootloader and the MDK provides APIs required
for communication with the gateway. The bootloader and the MDK projects have to
be added to the workspace. They can be downloaded from the resource page along
with application source code. To add them to the workspace, follow the procedure
described as above.

.. image:: ../images/sw11.png
   :align: center
   :width: 400

Setup path variables
--------------------

-  Open CCES, right click on the desired project and select ``Properties``.
-  In the properties tab, go to ``C/C++ Build`` -> ``Settings`` -> ``Cross Core GCC ARM Embedded C Linker``-> ``Libraries``.
-  Click on ``add`` (at the top right section inside settings tab) and then ``File system``. Then search for the required files from the workspace and add them.

.. image:: ../images/sw12.png
   :align: center
   :width: 600

-  Below image shows the paths to be added. Make sure that you add the path from the workspace. In the figure shown below, ``C:\Users\psirivan\Desktop`` is the path to the workspace, ``6Feb6`` is the name of the workspace.
-  Semihosting support should be ``nosys.specs``, as shown in the figure below.

.. important::

   Make sure that the libraries and objects are not enclosed within inverted
   commas.

.. image:: ../images/sw13.png
   :align: center
   :width: 600
