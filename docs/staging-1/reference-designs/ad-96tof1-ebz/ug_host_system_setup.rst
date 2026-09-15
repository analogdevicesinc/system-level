.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-96tof1-ebz/ug_host_system_setup

.. _ad-96tof1-ebz ug_host_system_setup:

Setting up the system
=====================

Required hardware
-----------------

- :adi:`AD-96TOF1-EBZ development kit <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ad-96tof1-ebz.html>`
- `DragonBoard 410c <https://www.96boards.org/product/dragonboard410c/>`__
- DragonBoard410c 12V power supply (e.g. AK-ND-49)
- Micro-USB to USB Cable

Power on sequence
-----------------

- Plug the SD card that came in the AD-96TOF1-EBZ box into the DragonBoard410c
  SD card slot. To benefit from the most recent software updates it is highly
  recommended to update the SD card with the
  `latest SD card image <https://github.com/analogdevicesinc/aditof_sdk#supported-embedded-platforms>`__
- Make sure that switch S6 on the DragonBoard410C is set to SD BOOT (position 2
  ON, all others OFF)
- Connect USB cable to the host PC
- Connect the 5V power supply to the camera board and set the camera power
  switch S2 to on. Once the camera board is powered up the DS1 LED will turn on
- Connect the 12V power supply to the DragonBoard 410c. Once power is connected
  to the DragonBoard the system will boot the Linux OS from the SD card
- Wait for the board to finish booting. The booting progress can be monitored by
  observing the user leds 1, 2, 3 and 4 on the DragonBoard410c which are placed
  between the two USB type A connectors. During boot the leds (especially led 3
  and 1) will blink very rapidly. When led 1 is the only one left blinking
  (about once a second) the boot has finished.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tof1-ebz/db410c_usb.jpg
   :width: 300px
