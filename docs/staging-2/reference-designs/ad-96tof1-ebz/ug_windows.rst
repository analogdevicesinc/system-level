.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-96tof1-ebz/ug_windows

.. _ad-96tof1-ebz ug_windows:

Windows User Guide
==================

.. todo:: .. include: ./ug_host_system_setup.rst

Enable the USB connection to the host PC
----------------------------------------

- After the DragonBoard boots up press the S3 button on the camera board. This
  will start on the DragonBoard the application that manages the USB host
  interface
- Once the USB connection is active the DS4 LED will light up on the camera
  board and the USB camera driver will be loaded on the PC enabling the
  communication between the host PC and the camera system. The ADI TOF DEPTH
  SENSOR may also show up under Cameras instead of Imaging devices.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/windows_db410c_usb.jpg
   :width: 300px

Troubleshooting
~~~~~~~~~~~~~~~

- The PC does not load the USB driver after pressing the S3 button on the camera
  board
- Press S3 so that DS4 turns off, reconnect the USB cable to the PC into a
  different USB port, press S3 again so that DS4 turns on
- Restart the DragonBoard410c while the USB cable is still connected to the host
  PC

--------------

Ethernet connection
~~~~~~~~~~~~~~~~~~~

- The IP address of the target is needed in order to use the ethernet
  connection. To find the IP address, connect a keyboard, a mouse and a monitor
  to the camera. After booting open a terminal and type either sudo ifconfig or
  ip addr command.
- There are two examples that show how to use the ethernet connection:
  aditof-demo and first-frame-ethernet .
- For first-frame-ethernet example, if the IP address of the target is
  *192.168.1.110* the run command should be:
  ::

     first-frame-ethernet.exe "192.168.1.110"

- In the aditof-demo example, choose to connect via ethernet from the UI. After
  the *Ethernet* checkbox is selected input the IP and press the button
  *Connect*.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/aditof-demo_ethernet.png
   :width: 300px

--------------

Running the evaluation application
----------------------------------

You can either build the evaluation application from source or install it using
the
`aditof-demo installer <https://github.com/analogdevicesinc/aditof_sdk/releases/latest>`__

Navigate to the location where you chose to install the evaluation application
and run aditof-demo.exe. Alternatively, run the shortcut Aditof-Demo from
desktop if you enabled the installer to create one.

.. todo:: .. include: ./ug_aditof_demo.rst
