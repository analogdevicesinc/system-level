ADICUP3029 Board Support Package (BSP)
======================================

.. warning::

   This CMSIS pack and its contents are DEPRECATED and no longer supported.
   Please do not use this moving forward

General Description/Overview
----------------------------

The ADICUP3029 software pack provides access to all the necessary on-board peripheral drivers for the :adi:`EVAL-ADICUP3029` development platform. The ADICUP3029 software pack builds on top of what the ADuCm302x software pack provides. The ADICUP3029 software pack makes it easier to use the on-board peripherals so creating your application layer is will be easier. Combined with the ADuCM302x and Sensors software pack, there are many great Internet of Things(IoT) applications and demos that can be replicated using the ADICUP3029 development platform.

The drivers and examples in the BSP are designed to work with CrossCore Embedded
Studio 2.6.0 ® and the ADuCM302x Device Family Pack 2.0.0, Sensor Software
1.1.0, BLE Software 1.0.0, WiFi Software 1.0.0.

Application Examples for the ADICUP3029
---------------------------------------

The following application examples are provided as part of the ADICUP3029 BSP
software pack:

-  :doc:`Temperature Demo (with EVAL-ADT7420-PMDZ) </solutions/reference-designs/eval-adicup3029/reference_designs/demo_adt7420>`
-  :doc:`PMOD Accelerometer Demo (with PmodACL2 from Digilent) </solutions/reference-designs/eval-adicup3029/reference_designs/demo_pmodacl2>`
-  :doc:`CO Toxic Gas Measurement Demo with Bluetooth (with EVAL-CN0357-ARDZ) </solutions/reference-designs/eval-adicup3029/reference_designs/demo_cn0357>`
-  :doc:`Visible Light Detection/Measurement Demo (with EVAL-CN0397-ARDZ) </solutions/reference-designs/eval-adicup3029/reference_designs/demo_cn0397>`

Changing the MAC Address of the EM9304
--------------------------------------

Each of the EVAL-ADICUP3029 boards has the same Bluetooth Low Energy(BLE) MAC
address by default. Although this won't be a problem for most users, some users
might be trying to prototype/create a system using multiple ADICUP3029 boards.
In those circumstances it might be required to change your MAC address to a
different unique value.

We have created five(5) additional BLE MAC addresses which can be quickly programmed using the desired MAC_address.HEX file and the drag and drop method described :doc:`here. </solutions/reference-designs/eval-adicup3029/tools/adicup3029_hw_drivers>`

The current available MAC address configurations are outlined in the table
below.

+--------------------------------+---------------------------------+--------------------+
| ADICUP3029 Board Configuration | ADICUP3029 .HEX File Name       | EM9304 MAC Address |
+================================+=================================+====================+
| Default Release Mode           | pre-programmed (no file needed) | 00-05-F7-01-41-44  |
+--------------------------------+---------------------------------+--------------------+
| ChangeMAC_45                   | change_mac_45.hex               | 00-05-F7-01-41-45  |
+--------------------------------+---------------------------------+--------------------+
| ChangeMAC_46                   | change_mac_46.hex               | 00-05-F7-01-41-46  |
+--------------------------------+---------------------------------+--------------------+
| ChangeMAC_47                   | change_mac_47.hex               | 00-05-F7-01-41-47  |
+--------------------------------+---------------------------------+--------------------+
| ChangeMAC_48                   | change_mac_48.hex               | 00-05-F7-01-41-48  |
+--------------------------------+---------------------------------+--------------------+
| ChangeMAC_49                   | change_mac_49.hex               | 00-05-F7-01-41-49  |
+--------------------------------+---------------------------------+--------------------+

The MAC address .HEX files can be found with the EVAL-ADICUP3029 pack, in the following directory: // **C:\\Analog Devices\\CrossCore Embedded Studio 2.6.0\\ARM\\packs\\AnalogDevices\\EVAL-ADICUP3029_BSP\\1.1.0\\Tools\\ble\\programmer\\EVAL-ADICUP3029**
Documentation
-------------

For detailed information regarding the ADICUP3029 software pack, please see our
complete ADICUP3029 software user guide.

.. hint::

   `ADICUP3029 BSP Release Notes <http://download.analog.com/tools/EZBoards/ADICUP3029/Releases/Release_1.1.0/EVAL-ADICUP3029_1.1.0_Release_Notes.pdf>`_

.. important::

   You MUST have this software package installed on your laptop or PC in order
   to compile, debug, and run the applications for the ADICUP3029 platform.

Downloading the ADICUP3029 Software Pack
----------------------------------------

The software pack can be downloaded in several ways.

-  Downloaded via the tools program

   -  It is **recommended** to download the ADICUP3029 software pack through from the tools program you are using. That way, all the files, directories structure, and project structure for the various applications is properly saved and accessed. For a detailed description on how to download the ADICUP3029 software pack through CrossCore Embedded Studio please see our :doc:`CrossCore Embedded Studio Quickstart User Guide </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>`.

-  Downloaded to local directory

   -  However if you do decide to download the ADICUP3029 software pack to your
      PC/laptop directly, please use the link below, and make sure you save the
      software pack to the correct local directory for your
      applications/projects.

.. admonition:: Download
   :class: download

   `ADICUP3029 BSP 1.1.0 <http://download.analog.com/tools/EZBoards/ADICUP3029/Releases/AnalogDevices.EVAL-ADICUP3029_BSP.1.1.0.pack>`_

*End of Document*
