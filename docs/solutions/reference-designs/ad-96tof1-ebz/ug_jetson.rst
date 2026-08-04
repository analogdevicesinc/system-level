Nvidia Jetson Nano User Guide
=============================

Setting up the system
---------------------

Required hardware
~~~~~~~~~~~~~~~~~

-  :adi:`AD-96TOF1-EBZ development kit <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`
-  `Nvidia Jetson Nano <https://developer.nvidia.com/embedded/jetson-nano-developer-kit>`_
-  5V power supply for Jetson. (Jetson board can be powered up from USB but external 4A 5V supply is recommended)
-  To run the system in standalone mode, besides the accessories that are provided in the AD-96TOF1-EBZ box you'll need an additional HDMI cable to connect to a monitor and a USB keyboard and mouse
-  `Camera flex cable <https://www.adafruit.com/product/2087>`_ for connection between Jetson and AD-96TOF1-EBZ

Modifying the AD-96TOF1-EBZ to work with the Nvidia Jetson Nano
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All changes required for RPi are applicable to Nvidia Jetson. So please follow the instructions presented here: :doc:`Raspberry Pi User Guide </solutions/reference-designs/ad-96tof1-ebz/ug_rpi>`

Prepare SD card
~~~~~~~~~~~~~~~

-  Download and flash on a SD card the latest image provided from the following link: `aditof_sdk#ad-96tof1-ebz <https://github.com/analogdevicesinc/aditof_sdk>`_
-  Download L4T BSP `L4T BSP <https://developer.nvidia.com/embedded/linux-tegra>`_ package (Tested release R32.3.1)
-  Extract kernel_src from BSP package
-  ADI ToF camera driver and devicetree should be taken from :git-aditof_sdk:`aditof_sdk <misc/nvidia/jetson/kernel_src>`
-  Copy paste and replace content of kernel_src folder from L4T BSP with the one downloaded from ADI ToF Repository
-  Build Kernel and devicetree blob following instructions from `Building_the_Kernel_from_Source <https://developer.ridgerun.com/wiki/index.php?title=Jetson_Nano/Development/Building_the_Kernel_from_Source>`_ selecting "CONFIG_VIDEO_ADDI9036" and "CONFIG_EEPROM_AT24" using menuconfig
-  Copy generated kernel Image and devicetree to SD card

Power on sequence
~~~~~~~~~~~~~~~~~

-  Plug the SD card into the Nvidia Jetson SD card slot
-  Connect the HDMI cable from the monitor to the Jetson HDMI connector
-  Connect the camera cable between the Jetson Nano and the P1 connector of the ToF board
-  Connect a USB mouse and keyboard to the Jetson
-  connect the 5V power supply to the camera board and set the camera power switch S2 to on. Once the camera board is powered up the DS1 LED will turn on
-  connect the 5V power supply to the Jetson Nano. Once power is connected to
   the Jetson the system will boot the Linux OS from the SD card.

.. important::

   Password for "analog" user is "analog". This user has sudo rights

.. image:: images/jetson_tof.jpg
   :alt: Jetson Nano connections rev. C
   :align: center
   :width: 400

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo poweroff**. This will safely power off and ensure that the SD card is properly unmounted
-  remove the 5V supply from the Nvidia Jetson
-  Set the camera board power switch to off

Running the evaluation application
----------------------------------

:git-aditof_sdk:`This example <examples/aditof-demo>` demonstrates how to capture data from the TOF system on the Nvidia jetson and display it using OpenCV.

Once Linux boots you'll see on the HDMI monitor the Linux desktop and on the top
left corner a shortcut to the evaluation application. Double clicking on the
icon will start the evaluation application. A console window will open to show
the application's status and, after a few seconds, the evaluation application
GUI will be displayed.

.. include:: ug_aditof_demo.rst
