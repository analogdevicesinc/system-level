Hardware Setup Guide
====================

.. image:: ../images/mc2_system.jpg
   :width: 600

Supported Carriers
------------------

-  `ZedBoard <http://zedboard.org/product/zedboard>`_

+---+
+---+

Required Hardware
-----------------

-  :doc:`AD-FMCMOTCON2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/controller_board>` - Controller board
-  :doc:`AD-DRVLV2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/lv_board>` - Low voltage drive board
-  :doc:`AD-DYNO2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/dyno>` - Dynamo-meter Drive System (Optional)
-  `ZedBoard <http://zedboard.org/product/zedboard>`_
-  12V - 48V capable DC power supply

+---+
+---+

Getting Started
---------------

-  Connect the hardware as shown in the picture below

.. image:: ../images/connections.jpg
   :alt: connections
   :width: 600

-  Make sure the **Emergency Stop** switch is pressed (more information about drive board buttons in the `LV Board description <https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_board>`_)
-  Insert the DYNO sensor wire in the P3 connector on the controller board with the black wire towards the ZedBoad. In case an encoder is used there is a one to one correspondence of the encoder's pins to the pins of the P3 connector.
-  Insert the DYNO motor wire in the P2 connector on the Drive Board
-  Connect the power supply to the P1 connector and, if a second motor is used also on the P3 connector
-  Make sure the following LEDs are ON:

   -  DS1, DS2, DS3 and DS4 on the Controller Board
   -  DS1 and DS2 on the Drive Board

-  Insert the 5V supply in the left side of the DYNO
-  Power on the ZedBoard
-  After the ZedBoard is programmed, in order to start the motor, the **Emergency Stop** switch must be released and then the **Reset** switch must be pressed for a few seconds.

+---+
+---+
