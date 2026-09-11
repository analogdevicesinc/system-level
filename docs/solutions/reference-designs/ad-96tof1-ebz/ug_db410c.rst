DragonBoard410C User Guide
==========================

Setting up the system
---------------------

Required hardware
~~~~~~~~~~~~~~~~~

-  :adi:`AD-96TOF1-EBZ development kit <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`
-  `DragonBoard410c <https://www.96boards.org/product/dragonboard410c/>`_
-  DragonBoard410c 12V power supply (e.g. AK-ND-49)
-  To run the system in standalone mode, besides the accessories that are
   provided in the AD-96TOF1-EBZ box you'll need an additional HDMI cable to
   connect to a monitor and a USB keyboard and mouse

Power on sequence
~~~~~~~~~~~~~~~~~

-  Plug the SD card that came in the AD-96TOF1-EBZ box into the DragonBoard410c SD card slot. To benefit from the most recent software updates it is highly recommended to update the SD card with the `latest SD card image <https://github.com/analogdevicesinc/aditof_sdk>`_
-  Make sure that switch S6 on the DragonBoard410C is set to SD BOOT (position 2 ON, all others OFF)
-  connect the HDMI cable from the monitor to the DragonBoard410c HDMI connector
-  connect a USB mouse and keyboard to the DragonBoard410c. It's possible to use either a mouse & keyboard combo or a separate mouse and keyboard
-  connect the 5V power supply to the camera board and set the camera power switch S2 to on. Once the camera board is powered up the DS1 LED will turn on
-  connect the 12V power supply to the DragonBoard 410c. Once power is connected
   to the DragonBoard the system will boot the Linux OS from the SD card.

.. image:: images/db410c_standalone.jpg
   :alt: DB410C connections
   :align: center
   :width: 400

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo halt**. This will safely turn off the OS on DragonBoard410c and ensure that the SD card is properly unmounted
-  Remove the 12V supply from the DragonBoard410c
-  Set the camera board power switch to off

Troubleshooting
~~~~~~~~~~~~~~~

-  Linux does not boot

   -  Sometimes the SD card is not read correctly and this prevents the system to boot. Reset the system by removing and reapplying power to the DragonBoard410c
   -  The SD card is corrupted and this prevents the system from booting.
      Reflash the SD card with the SD card image.

--------------

Running the evaluation application
----------------------------------

Once Linux boots you'll see on the HDMI monitor the Linux desktop and on the top
left corner a shortcut to the evaluation application. Double clicking on the
icon will start the evaluation application. A console window will open to show
the application's status and, after a few seconds, the evaluation application
GUI will be displayed.

.. include:: ug_aditof_demo.rst
