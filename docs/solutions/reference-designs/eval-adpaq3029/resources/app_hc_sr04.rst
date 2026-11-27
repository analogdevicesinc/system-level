.. _eval-adpaq3029 resources app_hc_sr04:

EVAL-ADPAQ3029 - HC-SR04 demo
=============================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   :download:`HC-SR04 Firmware <hc-sr04.zip>`

   :download:`Tile GUI application <moduware.tile.example-hcsr04.zip>`

-  Follow the same steps as given :ref:`here <eval-adpaq3029 first_app>`
-  In this project, an Ultrasonic Sensor – HC-SR04 has been used.

.. image:: ../images/app5.png
   :align: center
   :width: 300

-  The connections between the Ultrasonic Sensor and ADPAQ module are made as
   described in the table below.

.. image:: ../images/app6.png
   :align: center
   :width: 400

.. container:: round box

   ============ ============== =================
   HC-SR04 Pins GPIO port used ADPAQ Header Pins
   ============ ============== =================
   Vcc          3.3V           P1-3.3V
   Trig         P0_0           P2-5
   Echo         P2_1           P3-1
   Gnd          GND            P1-GND_POWER
   ============ ============== =================

-  Build and run the project
-  The Ultrasonic Sensor measurement is displayed on tile in “cm”.

.. image:: ../images/tile10.png
   :align: center
   :width: 400
