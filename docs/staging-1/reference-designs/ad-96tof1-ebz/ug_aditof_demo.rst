.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-96tof1-ebz/ug_aditof_demo

.. _ad-96tof1-ebz ug_aditof_demo:

NO TITLE
========

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/aditof_demo.png
   :width: 800px

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
- Medium - 30cm to 4.5m (Rev.B: 80cm to 3m)
- Far - 300cm to 600cm

When in a certain operating mode the system will measure distances outside of
the mode"s range but those will not be accurate.

The system is factory calibrated to achieve high accuracy in all the operating
modes for indoor environments. It is possible to recalibrate the system for your
specific operating conditions by using the calibration procedure and tools
provided
:dokuwiki:`here </resources/eval/user-guides/ad-96tof1-ebz/calibration>`.

The evaluation application also displays the temperature in deg C of the camera
(AFE) and laser boards as read from the temperature sensors installed on each
board.

The framerate at which data is acquired from the system is constantly updated on
the GUI. The camera board outputs data at 30 frames per second (fps), but due to
USB connection limitations, the host PC acquires the frames at a lower rate.

Enabling the point cloud display in aditof-demo
-----------------------------------------------

- The demo application has the capability to display a point cloud image if it
  detects an OpenCV module called viz.

Unfortunately OpenCV does not provide binaries for this module so a manual build
is needed. The steps required to install OpenCV and include it in the project
are presented here:
:git-aditof_sdk:`Windows <doc/windows/build_instructions.md#enabling-the-point-cloud-display-in-aditof-demo+>`
:git-aditof_sdk:`Linux <doc/linux/build_instructions.md#enabling-the-point-cloud-display-in-aditof-demo+>`

- If aditof-demo finds all the OpenCV required modules a button in the interface
  will allow you to display the point cloud. By toggling the button a separate
  window will appear.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/aditof_demo_pointCloud.png
   :width: 800px

.. important::

   Due to the limited computation speed of DragonBoard410c it is recomended to
   enable the point cloud only in the desktop sdk

Troubleshooting
~~~~~~~~~~~~~~~

- The demo application hangs after closing the main window
- Due to some limitations the application always hangs if it is closed using the
  regular X button from the window top bar (title bar). To avoid this unpleasant
  hang, we"ve made available a second X button in the top right corner right
  above the title bar that can be used to safely close the demo application. We
  hope this to be a temporary workaround.
