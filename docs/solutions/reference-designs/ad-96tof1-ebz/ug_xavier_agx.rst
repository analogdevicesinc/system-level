Nvidia Xavier AGX User Guide
============================

Setting up the system
---------------------

Required hardware
~~~~~~~~~~~~~~~~~

-  :adi:`AD-96TOF1-EBZ development kit <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`
-  `Nvidia Xavier AGX <https://developer.nvidia.com/embedded/jetson-agx-xavier-devkit>`_
-  19V power supply for Jetson.
-  To run the system in standalone mode, besides the accessories that are provided in the AD-96TOF1-EBZ box you'll need an additional HDMI cable to connect to a monitor and a USB keyboard and mouse
-  `Camera flex cable <https://www.adafruit.com/product/2087>`_ for connection between Xavier AGX and AD-96TOF1-EBZ

Modifying the AD-96TOF1-EBZ to work with the Nvidia Xavier AGX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All changes required for RPi are applicable to Nvidia Xavier AGX. So please follow the instructions presented here: :doc:`Raspberry Pi User Guide </solutions/reference-designs/ad-96tof1-ebz/ug_rpi>`

Prepare SD card
~~~~~~~~~~~~~~~

-  Download and flash on a SD card the latest image provided from the following link: `aditof_sdk#ad-96tof1-ebz <https://github.com/analogdevicesinc/aditof_sdk>`_
-  Download L4T BSP `L4T BSP <https://developer.nvidia.com/embedded/linux-tegra>`_ package (Tested release R32.3.1)
-  Extract kernel_src from BSP package
-  ADI ToF camera driver and devicetree should be taken from ADI ToF camera driver and devicetree should be taken from :git-aditof_sdk:`aditof_sdk <misc/nvidia>`.
-  Copy paste and replace content of kernel_src folder from L4T BSP with the one downloaded from ADI ToF Repository
-  Build Kernel and devicetree blob following instructions from `Building_the_Kernel_from_Source <https://developer.ridgerun.com/wiki/index.php?title=Xavier/JetPack_4.1/Compiling_Code/Kernel>`_ selecting "CONFIG_VIDEO_ADDI9036" and "CONFIG_EEPROM_AT24" using menuconfig
-  Copy generated kernel Image and devicetree to SD card

Power on sequence
~~~~~~~~~~~~~~~~~

-  Plug the SD card into the Nvidia Xavier AGX SD card slot
-  Connect the HDMI cable from the monitor to the Jetson HDMI connector
-  Connect the camera cable between the camera interposer of Jetson Xavier AGX and the P1 connector of the ToF board
-  Connect a USB mouse and keyboard to the Xavier AGX
-  connect the 5V power supply to the camera board and set the camera power switch S2 to on. Once the camera board is powered up the DS1 LED will turn on
-  connect the 19V power supply to the Xavier AGX. Once power is connected to
   the Xavier AGX the system will boot the Linux OS from the SD card.

.. important::

   Password for "analog" user is "analog". This user has sudo rights

.. image:: images/xavier-agx-ad96tof1.jpg
   :alt: Jetson Xavier AGX connections rev. C
   :align: center
   :width: 400

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo poweroff**. This will safely power off and ensure that the SD card is properly unmounted
-  remove the 5V supply from the Nvidia XAVIER AGX
-  Set the camera board power switch to off

Troubleshooting
~~~~~~~~~~~~~~~

-  Linux does not boot

   -  The SD card is corrupted and this prevents the system from booting.
      Reflash the SD card or check generated devicetree or kernel image

.. admonition:: Download
   :class: download

   **Nvidia Xavier AGX interposer design and manufacturing files**

   
   -  `Design files <resources/08_065345a.zip>`_
   -  `Gerber files <resources/nvidia_agx_xavier_interposer.zip>`_
   

--------------

Running the evaluation application
----------------------------------

:git-aditof_sdk:`This example <examples/aditof-demo>` demonstrates how to capture data from the TOF system on the Nvidia jetson and display it using OpenCV.

Once Linux boots you'll see on the HDMI monitor the Linux desktop and on the top
left corner a shortcut to the evaluation application. Double clicking on the
icon will start the evaluation application. A console window will open to show
the application's status and, after a few seconds, the evaluation application
GUI will be displayed.

.. include:: ug_aditof_demo.rst
