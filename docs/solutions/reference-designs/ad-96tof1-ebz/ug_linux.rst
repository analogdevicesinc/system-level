Linux User Guide
================

.. include:: ug_host_system_setup.rst

Enable the USB connection to the host PC
----------------------------------------

-  After the DragonBoard boots up press the S3 button on the camera board. This will start on the DragonBoard the application that manages the USB host interface
-  Once the USB connection is active the DS4 LED will light up on the camera board and the USB camera driver will be loaded on the PC enabling the communication between the host PC and the camera system
-  To check if the camera has been recognized by the host PC, open up a terminal and run the *dmesg* command. The ADI TOF DEPTH SENSOR name should come up in the list displayed by *dmesg*.

.. image:: images/linux_db410c_usb.png
   :alt: Linux driver
   :align: center
   :width: 800

Troubleshooting
---------------

-  The PC does not load the USB driver after pressing the S3 button on the
   camera board

   -  Press S3 so that DS4 turns off, reconnect the USB cable to the PC into a different USB port, press S3 again so that DS4 turns on
   -  Restart the DragonBoard410c while the USB cable is still connected to the
      host PC

--------------

Ethernet connection
-------------------

-  The IP address of the target is needed in order to use the ethernet connection. To find the IP address, connect a keyboard, a mouse and a monitor to the camera. After booting open a terminal and type either sudo ifconfig or ip addr command.
-  There are two examples that show how to use the ethernet connection: **aditof-demo** and **first-frame-ethernet**.
-  For **first-frame-ethernet** example, if the IP address of the target is *192.168.1.110* the run command should be: ``./first-frame-ethernet "192.168.1.110"``
-  In the **aditof-demo** example, choose to connect via ethernet from the UI. After the *Ethernet* checkbox is selected input the IP and press the button *Connect*.

.. image:: images/aditof-demo_ethernet.png
   :alt: aditof-demo connect through ethernet
   :align: center
   :width: 300

--------------

Running the evaluation application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can build the evaluation application from source as part of the SDK build
process described on github.

.. include:: ug_aditof_demo.rst
