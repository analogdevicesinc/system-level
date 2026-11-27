.. _eval-adpaq3029 resources app_servo:

EVAL-ADPAQ3029 - Servo motor demo
=================================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   :download:`Servo motor Firmware <servo.zip>`

   :download:`Tile GUI application <moduware.tile.example-servo.zip>`

-  Follow the same steps as given :ref:`here <eval-adpaq3029 first_app>`
-  In this project, a Servo motor is used.

.. image:: ../images/app9.png
   :align: center
   :width: 200

-  The connections between the Servo Motor and the ADPAQ module are made as
   shown below.

.. image:: ../images/app10.png
   :width: 300

.. container:: round box

   ================ ============== =================
   Servo motor Pins GPIO port used ADPAQ Header Pins
   ================ ============== =================
   A                5V             P2-1
   B                P0_1           P2-5
   C                GND            P2-10
   ================ ============== =================

-  Build and run the project
-  The tile has a “Freq” button and an input value option. We can set the
   frequency of the servo any value between 0-100 and the servo motor rotates
   accordingly.

.. image:: ../images/tile13.png
   :align: center
   :width: 400

|image1|

.. |image1| image:: ../images/tile14.png
   :width: 400
