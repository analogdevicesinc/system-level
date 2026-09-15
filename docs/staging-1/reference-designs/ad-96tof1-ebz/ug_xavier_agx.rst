.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-96tof1-ebz/ug_xavier_agx

.. _ad-96tof1-ebz ug_xavier_agx:

Nvidia Xavier AGX User Guide
============================

Setting up the system
---------------------

Required hardware
~~~~~~~~~~~~~~~~~

- :adi:`AD-96TOF1-EBZ development kit <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`
- `Nvidia Xavier AGX <https://developer.nvidia.com/embedded/jetson-agx-xavier-devkit>`__
- 19V power supply for Jetson.
- To run the system in standalone mode, besides the accessories that are
  provided in the AD-96TOF1-EBZ box you"ll need an additional HDMI cable to
  connect to a monitor and a USB keyboard and mouse
- `Camera flex cable <https://www.adafruit.com/product/2087>`__ for connection
  between Xavier AGX and AD-96TOF1-EBZ

Modifying the AD-96TOF1-EBZ to work with the Nvidia Xavier AGX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All changes required for RPi are applicable to Nvidia Xavier AGX. So please
follow the instructions presented here:
:dokuwiki:`Raspberry Pi User Guide </resources/eval/user-guides/ad-96tof1-ebz/ug_rpi>`

Prepare SD card
~~~~~~~~~~~~~~~

- Download and flash on a SD card the latest image provided from the following
  link: :git-aditof_sdk#ad-96tof1-ebz:`aditof_sdk#ad-96tof1-ebz </>`
- Download L4T BSP
  `L4T BSP <https://developer.nvidia.com/embedded/linux-tegra>`__ package
  (Tested release R32.3.1)
- Extract kernel_src from BSP package
- ADI ToF camera driver and devicetree should be taken from ADI ToF camera
  driver and devicetree should be taken from
  :git-aditof_sdk:`aditof_sdk <misc/nvidia+>`.
- Copy paste and replace content of kernel_src folder from L4T BSP with the one
  downloaded from ADI ToF Repository
- Build Kernel and devicetree blob following instructions from
  `Building_the_Kernel_from_Source <https://developer.ridgerun.com/wiki/index.php?title=Xavier/JetPack_4.1/Compiling_Code/Kernel>`__
  selecting ``CONFIG_VIDEO_ADDI9036`` and ``CONFIG_EEPROM_AT24`` using
  menuconfig
- Copy generated kernel Image and devicetree to SD card

Power on sequence
~~~~~~~~~~~~~~~~~

- Plug the SD card into the Nvidia Xavier AGX SD card slot
- Connect the HDMI cable from the monitor to the Jetson HDMI connector
- Connect the camera cable between the camera interposer of Jetson Xavier AGX
  and the P1 connector of the ToF board
- Connect a USB mouse and keyboard to the Xavier AGX
- connect the 5V power supply to the camera board and set the camera power
  switch S2 to on. Once the camera board is powered up the DS1 LED will turn on
- connect the 19V power supply to the Xavier AGX. Once power is connected to the
  Xavier AGX the system will boot the Linux OS from the SD card.

.. important::

   Password for ``analog`` user is ``analog``. This user has sudo rights

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/xavier-agx-ad96tof1.jpg
   :width: 400px

Power off sequence
~~~~~~~~~~~~~~~~~~

- Open a terminal and type *sudo poweroff* . This will safely power off and
  ensure that the SD card is properly unmounted
- remove the 5V supply from the Nvidia XAVIER AGX
- Set the camera board power switch to off

Troubleshooting
~~~~~~~~~~~~~~~

- Linux does not boot
- The SD card is corrupted and this prevents the system from booting. Reflash
  the SD card or check generated devicetree or kernel image

.. admonition:: Download

   **Nvidia Xavier AGX interposer design and manufacturing files**

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/08_065345a.zip`

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/nvidia_agx_xavier_interposer.zip`

--------------

Running the evaluation application
----------------------------------

:git-aditof_sdk:`This example <examples/aditof-demo+>` demonstrates how to
capture data from the TOF system on the Nvidia jetson and display it using
OpenCV.

Once Linux boots you"ll see on the HDMI monitor the Linux desktop and on the top
left corner a shortcut to the evaluation application. Double clicking on the
icon will start the evaluation application. A console window will open to show
the application"s status and, after a few seconds, the evaluation application
GUI will be displayed.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/aditof_demo.png

When starting the application, a terminal window will open to display status
messages (also warning and error messages, in case there are any issues). Shorty
the main window will show up.

The evaluation application allows to do live streaming of depth and IR data as
well as recording the depth and IR data and playing back from a file. The depth
data is displayed as a color map ranging from warm to cold colors as the
distance from the camera increases. A point in the middle of the depth image
shows the distance in mm to the target.

There are 3 operating modes that determine the range of the system:

- Near - 25cm to 80cm
- Medium - 30cm to 4.5m
- Far - 3m to 6m

When in a certain operating mode the system will measure distances outside of
the mode"s range but those will not be accurate.

The evaluation application also displays the temperature in deg C of the camera
(AFE) and laser boards as read from the temperature sensors installed on each
board.

The framerate at which data is acquired from the system is constantly updated on
the GUI. The camera board outputs data at 30 frames per second (fps), but due to
USB connection limitations, the host PC acquires the frames at a lower rate.

Enabling the point cloud display in aditof-demo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The demo application has the capability to display a point cloud image if it
  detects an OpenCV module called viz.

Unfortunately OpenCV does not provide binaries for this module so a manual build
is needed. The steps required to install OpenCV and include it in the project
are presented here:
:git-aditof_sdk:`Enable Point Cloud Aditof-Demo <doc/linux/build_instructions.md#enabling-the-point-cloud-display-in-aditof-demo+>`

- If aditof-demo finds all the OpenCV required modules a button in the interface
  will allow you to display the point cloud. By toggling the button a separate
  window will appear.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/aditof_demo_pointCloud.png
   :width: 800px
