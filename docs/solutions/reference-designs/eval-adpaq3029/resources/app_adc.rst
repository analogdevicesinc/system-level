.. _eval-adpaq3029 resources app_adc:

EVAL-ADPAQ3029 - ADC demo
=========================

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   :download:`ADC Firmware <adc.zip>`

   :download:`Tile GUI application <moduware.tile.example-adc.zip>`

-  Follow the same steps as given :ref:`here <eval-adpaq3029 first_app>`
-  A potentiometer has been used in this project to modify the analog voltage
   values.

.. image:: ../images/app3.png
   :align: center
   :width: 200

-  The potentiometer has to be interfaced with the ADPAQ module. The connections
   between the potentiometer and the ADPAQ module are described in the table
   below.

.. image:: ../images/app4.png
   :align: center
   :width: 300

.. container:: round box

   ================== ============== =================
   Potentiometer Pins GPIO port used ADPAQ Header Pins
   ================== ============== =================
   A                  VCC            P1-3.3V
   B                  ADC0_Vin0      P1-ADC0_Vin0
   C                  GND            P1-GND_POWER
   ================== ============== =================

-  Build and run the project
-  If the knob of the potentiometer is rotated, the ADC value should vary
   between 0-4095 for the corresponding analog voltage variations from 0 to
   3.3V.

.. image:: ../images/tile12.png
   :align: center
   :width: 300
