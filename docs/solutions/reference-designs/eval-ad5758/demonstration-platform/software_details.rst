.. _eval-ad5758 software:

Software
===============================================================================

Firmware Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The demo board comes with the latest version of the firmware
pre-installed. If you would like to re-install the firmware or update to
the latest version, please follow these steps:

1. Download the latest version of the Demo board firmware. This file is
   called :dokuwiki:`adi5758_20180910.zip <_media/resources/demo/reference-designs/demo-ad5758-ao8z/demo-ad5757-ao8z/firmware/adi5758_20180910.zip>`
2. Unzip this file.
3. Install the latest version of the CrossCore Serial Flash Programmer
   from Analog.com. You can skip this step if you have the latest version
   already installed.
4. Start the CrossCore Serial Flash Programmer.

   1. Set Target to "ADuCM302x".
   2. Select firmware file "adi5758_20180910.hex" in the <File to
      download> field. (This is the file you downloaded and unzipped
      in steps 1 & 2.)
   3. Apply 24 V to the "24 V SYS" connector
   4. Plug the USB cable into the demo board.
   5. Hold down S2 (Boot) button while briefly pressing the S1 (Reset)
      button. Then release S2. This sequence is important.

   .. figure:: ../images/Reset_and_boot_buttons.png
      :align: center

      Reset and Boot buttons

5. On the CrossCore SFP, select the correct COM port. (Be sure to select
   the correct COM port here. It is usually the highest COMnn.)
6. Press [Start] to program device. (If you get the message "Failed to
    open serial device", then repeat step 5 above, taking care to follow
    the exact button press sequence.)
7. Programming the board takes about 10 seconds. When it is complete,
    you will see a message to that effect in the Status Window.

.. figure:: ../images/cross_core.png
   :align: center

   The CrossCore GUI

8. Press the reset button (S1) on the demo board or unplug it from the USB
   cable and reconnect.

The demo board now has the latest version of the firmware.

GUI Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section outlines how to download and install the latest version of
AD5758 Eight Channel Demo Board GUI software. You can skip this step if
you already have the latest version installed which is version 0911.

These instructions are for installation on Windows-10 but should also
work for Windows-7 with minor differences.

**Step-by-step guide**

1. Download the latest version of the :dokuwiki:`ad5758 GUI Software <_media/resources/demo/reference-designs/demo-ad5758-ao8z/gui/demo-ad5758-ao8z_installer.zip>` and save to a
   folder of your choice.
2. Unzip the file "DEMO-AD5758-AO8Z_Installer.zip"
3. Double click the "DEMO-AD5758-AO8Z_Installer.exe" file to run it.
4. Click Next in the pop-up that appears.

.. figure:: ../images/13-11-2019_11-56-36.png
   :align: center

   Welcome to DEMO AD5758 AO8Z 11.12 Setup

5. Read carefully the License Agreement and click "I Agree" if you agree to its
   content.

.. figure:: ../images/image2018-10-18_10-21-47.png
   :align: center

   The License Agreement

6. Click Install to install the software in the default location or Browse… to
   a new location first.

.. figure:: ../images/gui-installation-default_location.png
   :align: center

   Choosing the Install Location

7. Click "Finish" in the final pop-up.
