Firmware and Module Upgrade
===========================

This page covers methods for updating firmware and replacing modules.

Firmware Upgrade
----------------

The ADSD3500 chip on the ADTF3175 module boots from its own NVM without host
access, requiring communication through the ADSD3500 to perform upgrades using
the Data Collect CLI.

.. important::

   From Version 5.0.0 the IP address has changed to **10.43.0.1**.
   Pre-5.0.0 releases the IP address is **10.42.0.1**.

The firmware binary file for the latest version is available on the respective
flash image. The binary file can also be obtained from the ADSD3500 installer.
From the installer package, under the directory ADSD3500_Release_Firmware, the
binary file required (for example, for the 4.1.5 firmware release):

-  Fw_Update_4.1.5.bin

Windows Upgrade Process
~~~~~~~~~~~~~~~~~~~~~~~

**Version 6.0.0 or Later:**

1. Copy firmware file from image folder to bin directory
2. Execute::

      data_collect.exe --ip 10.43.0.1 --fw Fw_Update_x.y.z.bin

**Version 5.0.0:**

::

   data_collect.exe --ip 10.43.0.1 --fw Fw_Update_x.y.z.bin config_adsd3500_adsd3100.json

**Pre-5.0.0:**

::

   data_collect.exe --ip 10.42.0.1 --fw firmware_upgrade_xxxx.bin tof-viewer_config.json

Example from the host::

   cd "C:\Analog Devices\ADTF3175D\TOF_Evaluation_ADTF3175D-Rel4.1.1\bin"
   data_collect --fw ..\image\NXP-Img-Rel4.1.1-ADTF3175D-0A8ED2B5\Fw_Update_4.1.5.bin --ip 10.42.0.1 tof-viewer_config.json

Critical Steps
~~~~~~~~~~~~~~

1. Ensure the camera network connection is detected by your PC
2. **Allow 60 seconds** after flash completion before power cycling
3. Verify successful update by checking firmware version in the GUI:
   "Current adsd3500 firmware version is: X.X.X.X"

Module Upgrade
--------------

When Replacement is Needed
~~~~~~~~~~~~~~~~~~~~~~~~~~

Kits with serial numbers starting with 'CR' or 'DV11' require module
replacement, as older ADTF3175 modules are no longer supported in Release
4.3.0+.

Key Improvements in New Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The updated modules feature:

-  Thermal Compensation model added
-  Enhanced integration times
-  Improved laser safety mechanisms

Installation Overview
~~~~~~~~~~~~~~~~~~~~~

**Required tools:**

-  Phillips screwdriver
-  Soldering iron (for some kits)
-  Replacement ADTF3175XMLZ module

**Main steps:**

1. Power down the kit completely
2. Remove the module cover by unscrewing
3. Unscrew the module while tracking spacers and fasteners
4. Disconnect the flex cable connector
5. Connect the new module to the flex cable
6. Reinstall spacers and gradually screw down the module (alternating corners
   for even seating)
7. Replace the cover
8. Update ADSD3500 firmware to version 4.2.0.0 or higher
9. Install Release 4.3.0+ software

Troubleshooting
~~~~~~~~~~~~~~~

If streaming fails after installation, inspect the evaluation kit's back cover
for resistor R57 on the 068977 board. If present, desolder it to restore
functionality.

.. _eval_adtf3175d_mode_table:

Mode Table
----------

The mode number and .ini file counterparts are different based on different
batches of ADTF3175D kits. Please find the right column for your kit below.

Table for serial numbers starting with 'am'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Please note the minimum ADSD3500 version number must be '4.2.1.0'**

+---------------+--------------------------------------+--------------------------------------+-------------------------------+-------------------------------+
| Mode Name     | sr-native                            | lr-native                            | sr-qnative                    | lr-qnative                    |
+===============+======================================+======================================+===============================+===============================+
| Mode Number   | 0                                    | 1                                    | 2                             | 3                             |
+---------------+--------------------------------------+--------------------------------------+-------------------------------+-------------------------------+
| INI file name | RawToDepthAdsd3500_16bitAB_sr-native | RawToDepthAdsd3500_16bitAB_lr-native | RawToDepthAdsd3500_sr-qnative | RawToDepthAdsd3500_lr-qnative |
+---------------+--------------------------------------+--------------------------------------+-------------------------------+-------------------------------+

Table for serial numbers starting with 'DV11'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+-----+-------------------------------+-----+------------------------+
| Mode Name     | N/A | mp                            | N/A | qmp                    |
+===============+=====+===============================+=====+========================+
| Mode Number   | N/A | 10                            | N/A | 7                      |
+---------------+-----+-------------------------------+-----+------------------------+
| INI file name | N/A | RawToDepthAdsd3500_16bitAB_mp | N/A | RawToDepthAdsd3500_qmp |
+---------------+-----+-------------------------------+-----+------------------------+

Table for serial numbers starting with 'CR'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+-----+-------------------------------+-----+------------------------+
| Mode Name     | N/A | mp                            | N/A | qmp                    |
+===============+=====+===============================+=====+========================+
| Mode Number   | N/A | 10                            | N/A | 7                      |
+---------------+-----+-------------------------------+-----+------------------------+
| INI file name | N/A | RawToDepthAdsd3500_16bitAB_mp | N/A | RawToDepthAdsd3500_qmp |
+---------------+-----+-------------------------------+-----+------------------------+
