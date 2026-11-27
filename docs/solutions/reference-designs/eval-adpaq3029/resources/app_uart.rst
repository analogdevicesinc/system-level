.. _eval-adpaq3029 resources app_uart:

EVAL-ADPAQ3029 - UART(Arduino) demo
===================================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   :download:`UART (Arduino) Firmware <uart.zip>`

   :download:`Tile GUI application <moduware.tile.example-uart.zip>`

   :download:`Arduino code <uart.ino.zip>`

-  Follow the same steps as given :ref:`here <eval-adpaq3029 first_app>`
-  In this project, an Arduino board has been used.

.. image:: ../images/app11.png
   :align: center
   :width: 200

-  Upload the ``Arduino code`` into ``Arduino Uno`` board using Arduino IDE.
-  The connections between the Arduino and ADPAQ Board are made as described
   below.

.. container:: round box

   =================== ============== =================
   Arduino Pins        GPIO port used ADPAQ Header Pins
   =================== ============== =================
   Digital pin 10 (RX) UART0_TX       P2-2
   Digital pin 11 (TX) UART0_RX       P2-3
   GND                 GND            P2-10
   =================== ============== =================

-  Apart from these connections, an led along with a 10k resistor has to be
   connected between the Digital pin 12 of Arduino and Ground.

.. image:: ../images/app12.png
   :width: 400

-  Build and run the project
-  The tile has 2 buttons “On” and “Off” buttons. By clicking on those buttons,
   we can control the led that is connected to the pin 12 of Arduino.

.. image:: ../images/tile15.png
   :align: center
   :width: 400

|image1|

.. |image1| image:: ../images/tile16.png
   :width: 400
