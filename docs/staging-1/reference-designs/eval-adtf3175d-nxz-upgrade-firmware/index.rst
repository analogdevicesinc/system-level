.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adtf3175d-nxz-upgrade-firmware

.. _eval-adtf3175d-nxz-upgrade-firmware:

EVAL-ADTF3175D-NXZ NVM upgrade guide
====================================

.. important::

   From Version 5.0.0 the IP address has change to **10.43.0.1**.

   Pre-5.0.0 releases the IP address is 10.42.0.1.

The ADSD3500 self boots from the NVM on the ADTF3175 module, and the host (IMX8M
Plus) has no access. Therefore the host must communicate through the ADSD3500 to
modify the contents of the NVM, which is typically required for upgrades. The
:dokuwiki:`DataCollect CLI </resources/eval/user-guides/eval-adsd3100-nxz-gui/datacollect_cli>`
allows the user to achieve this.

Datacollect Windows (Recommended)
---------------------------------

- Download upgrade binary zipfile, and unzip binary file
- Move upgrade_binary_xxxx.bin file to bin folder of software install location
  C:\\Analog Devices\\TOF_Evaluation_BM-Rel3.0.0\\bin
- Open command prompt and go to bin folder as shown below

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-firmware-update-1.png

- Connect camera - ensure camera network is detected by the PC
- Run the following command, using the appropriate firmware filename:
- Pre-5.0.0 ``data_collect.exe –ip 10.42.0.1 –fw firmware_upgrade_xxxx.bin
  tof-viewer_config.json``
- 5.0.0 ``data_collect.exe –ip 10.43.0.1 –fw Fw_Update_x.y.z.bin
  config_adsd3500_adsd3100.json``
- 6.0.0 and later, in the ``bin`` folder:

  - ``copy ..\image\NXP-Img-Rela.b.c-ADTF3175D-xxxxxxxx\Fw_Update_x.y.z.bin .``
  - ""data_collect.exe –ip 10.43.0.1 –fw Fw_Update_x.y.z.bin ""

For example, with release 6.0.1 on Windows:

::

   cd C:\Analog Devices\TOF_Evaluation_ADTF3175D-Rel6.0.1\bin>data_collect.exe --ip 10.43.0.1 --fw ..\image\NXP-Img-Rel6.0.1-ADTF3175D-6E34B7B1\Fw_Update_5.2.5.bin

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-firmware-update-2.png

- If the flash sequence finishes, wait 60s
- power cycle the module
- Run the GUI and check if the the ADSD3500 FW version has updated - "Current
  adsd3500 firmware version is: X.X.X.X"

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adtf3175d-nxz/adi-tof-firmware-update-3.png

- If the version number has not updated please check the NXP based option to
  update the firmware. There is a possibility that your PC"s network security

- Wait 60 seconds
- Power cycle camera
- Run GUI and check if the ADSD3500 version number has updated
