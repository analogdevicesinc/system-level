.. _eval-adpaq3029 resources app_sht20:

EVAL-ADPAQ3029 - SHT20 [I2C] demo
=================================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   :download:`SHT20 Firmware <sht20.zip>`

   :download:`Tile GUI application <moduware.tile.example-i2c.zip>`

-  Follow the same steps as given :ref:`here <eval-adpaq3029 first_app>`
-  In this project, SHT20 (Temperature and Humidity Sensor) is used.

.. image:: ../images/app7.png
   :align: center
   :width: 300

-  The connections between the SHT20 and the ADPAQ module are made as described
   below.

.. image:: ../images/app8.png
   :align: center
   :width: 200

.. container:: round box

   ========== ============== =================
   SHT20 Pins GPIO port used ADPAQ Header Pins
   ========== ============== =================
   Vcc        3.3V           P1-1
   SCL        I2C_SCL        P2-9
   SDA        I2C_SDA        P2-8
   Gnd        GND            P1-10
   ========== ============== =================

-  Build and run the project
-  The Sensor will give the Temperature value in ``degree celsius`` and Humidity in ``%RH``.

.. image:: ../images/tile11.png
   :align: center
   :width: 400

|image1|

.. |image1| image:: ../images/tile12.png
   :width: 400
