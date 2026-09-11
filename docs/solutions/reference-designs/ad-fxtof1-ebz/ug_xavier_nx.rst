Nvidia Xavier NX User Guide
===========================

Setting up the system
---------------------

Required hardware
~~~~~~~~~~~~~~~~~

-  :adi:`AD-FXTOF1-EBZ development kit <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-fxtof1-ebz.html>`
-  `Nvidia Xavier NX <https://developer.nvidia.com/embedded/jetson-xavier-nx-devkit>`_
-  9V to 19V power supply for Jetson.
-  5V power supply for the interposer.
-  To run the system in standalone mode, besides the accessories that are provided in the AD-FXTOF1-EBZ box you'll need an additional HDMI cable to connect to a monitor and a USB keyboard and mouse
-  `Camera flex cable <https://www.adafruit.com/product/2087>`_ for connection between Xavier NX and AD-FXTOF1-EBZ

Prepare SD card
~~~~~~~~~~~~~~~

-  Download and flash on a SD card the latest image provided from the following link: `aditof_sdk#ad-fxtof1-ebz <https://github.com/analogdevicesinc/aditof_sdk>`_
-  Download L4T BSP `L4T BSP <https://developer.nvidia.com/embedded/linux-tegra>`_ package (Tested release R32.3.1)
-  Extract kernel_src from BSP package
-  ADI ToF camera driver and devicetree should be taken from :git-aditof_sdk:`aditof_sdk <misc/nvidia>`.
-  Copy paste and replace content of kernel_src folder from L4T BSP with the one downloaded from ADI ToF Repository
-  Build Kernel and devicetree blob following instructions from `Building_the_Kernel_from_Source <https://developer.ridgerun.com/wiki/index.php?title=Jetson_Xavier_NX/Development/Building_the_Kernel_from_Source>`_ selecting "CONFIG_VIDEO_ADDI9036" and "CONFIG_EEPROM_AT24" using menuconfig
-  Copy generated kernel Image and devicetree to SD card

Power on sequence
~~~~~~~~~~~~~~~~~

-  Plug the SD card into the Nvidia Xavier NX SD card slot
-  Connect the HDMI cable from the monitor to the Jetson HDMI connector
-  Connect the 25 pins flex cable between the camera and the interposer
-  Connect the 15 pons camera cable between the J1 connector of Jetson Xavier NX and the P1 connector of the interposer. **Make sure to use the cable with contacts on opposite sides.**

.. important::

   Some of the AD-FXTOF1-EBZ kits are missing the correct 15 pins cable to connect to Raspberry Pi or the Nvidia platforms. If in your box there is only one 15 pins cable having the contacts on the same side, please get a new cable with contacts on opposite sides (e.g. `15 pins cable, contacts on opposite sides <https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/686715152001/4573357>`_)

-  Connect a USB mouse and keyboard to the Xavier NX
-  Connect the power supply to the interposer
-  connect the 9V-19V power supply to the Xavier NX. Once power is connected to
   the Jetson the system will boot the Linux OS from the SD card.

.. important::

   Password for "analog" user is "analog". This user has sudo rights

.. image:: images/ad-fxtof1-ebz-xavier-nx-connection.jpg
   :alt: Jetson Xavier nx connections
   :align: center

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo poweroff**. This will safely power off and ensure that the SD card is properly unmounted
-  remove the 9-19V supply from the Nvidia Jetson
-  remove the 5V supply from the interposer

Troubleshooting
~~~~~~~~~~~~~~~

-  Linux does not boot

   -  The SD card is corrupted and this prevents the system from booting.
      Reflash the SD card or check generated devicetree or kernel image

--------------

Running the evaluation application
----------------------------------

:git-aditof_sdk:`This example <examples/aditof-demo>` demonstrates how to capture data from the TOF system on the Nvidia Xavier NX and display it using OpenCV.

.. image:: images/aditof_demo.png

Enabling the point cloud display in aditof-demo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The demo application has the capability to display a point cloud image if it
   detects an OpenCV module called viz.

Unfortunately OpenCV does not provide binaries for this module so a manual build is needed. The steps required to install OpenCV and include it in the project are presented here: :git-aditof_sdk:`Enable Point Cloud Aditof-Demo <doc/linux/build_instructions.md#enabling-the-point-cloud-display-in-aditof-demo>`

-  If aditof-demo finds all the OpenCV required modules a button in the
   interface will allow you to display the point cloud. By toggling the button a
   separate window will appear.

.. image:: images/aditof_demo_pointcloud.png
   :alt: aditof-demo
   :align: center
   :width: 800
