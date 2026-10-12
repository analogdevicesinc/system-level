Raspberry Pi User Guide
=======================

Setting up the system
---------------------

Required hardware
~~~~~~~~~~~~~~~~~

-  :adi:`AD-96TOF1-EBZ development kit <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`
-  `Raspberry Pi <https://www.raspberrypi.org/products/>`_ The system was tested on Raspberry Pi3 Model B V1.2 and Raspberry Pi 4. It can work on other models that have a CSI camera interface input.
-  Raspberry Pi 5V power supply
-  To run the system in standalone mode, besides the accessories that are provided in the AD-96TOF1-EBZ box you'll need an additional HDMI cable to connect to a monitor and a USB keyboard and mouse
-  `RPi camera cable <https://www.adafruit.com/product/2087>`_ for connection between RPi and AD-96TOF1-EBZ

Modifying the AD-96TOF1-EBZ to work with the RPi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the **AD-96TOF1-EBZ rev.B** to work with the RPi the following changes must be made on the camera board:

-  short pins 2 and 3 on JP1. JP1 is located underneath the laser board so the laser board must be first detached from the camera board to have access to this solder jumper
-  short R98 and R109
-  move the S1 switch to position 1 - to the dot on the switch

For the **AD-96TOF1-EBZ rev.C** to work with the RPi the following changes must be made on the camera board:

-  move the S1 switch to position 1 - to the dot on the switch
-  set the S5 switch 1 to OFF and all the other S5 switches to ON

Power on sequence
~~~~~~~~~~~~~~~~~

-  Plug the SD card into the Raspberry Pi SD card slot. To benefit from the most recent software updates it is highly recommended to update the SD card with the `latest SD card image <https://github.com/analogdevicesinc/aditof_sdk>`_
-  Connect the HDMI cable from the monitor to the Raspberry Pi HDMI connector
-  Connect the RPi camera cable between the RPi and the P1 connector of the ToF board
-  Connect a USB mouse and keyboard to the Raspberry Pi. It's possible to use
   either a mouse & keyboard combo or a separate mouse and keyboard

AD-96TOF1-EBZ rev.B
^^^^^^^^^^^^^^^^^^^

-  connect the I2C1 of the Raspberry Pi to AD-96TOF1-EBZ development kit. Please
   use jumper wires and the table below.

============================= =============================
Raspberry Pi GPIO Header (J8) AD-96TOF1-EBZ pin header (P4)
============================= =============================
Pin 3 (SDA)                   Pin 17
\                             Pin 21
Pin 5 (SCL)                   Pin 15
\                             Pin 19
============================= =============================

-  take care that the jumper wire connected to RPi header Pin 3 must be split in
   two and routed to both Pin 17 and Pin 21 on camera PCB. The same for SCL wire

.. image:: images/rpi_standalone.jpg
   :alt: RPi connections rev. B
   :align: center
   :width: 400

AD-96TOF1-EBZ rev.C
^^^^^^^^^^^^^^^^^^^

.. image:: images/rpi_standalone_revc.png
   :alt: RPi connections rev. C
   :align: center
   :width: 400

-  connect the 5V power supply to the camera board and set the camera power switch S2 to on. Once the camera board is powered up the DS1 LED will turn on
-  connect the 5V power supply to the Raspberry Pi. Once power is connected to
   the Raspberry Pi the system will boot the Linux OS from the SD card.

Power off sequence
~~~~~~~~~~~~~~~~~~

-  Open a terminal and type **sudo poweroff**. This will safely power off the Raspberry Pi and ensure that the SD card is properly unmounted
-  remove the 5V supply from the Raspberry Pi
-  Set the camera board power switch to off

Troubleshooting
~~~~~~~~~~~~~~~

-  Linux does not boot

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
