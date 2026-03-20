Dynamometer Drive System
========================

.. image:: ../images/mc2_dyno_single.jpg
   :alt: Dynamometer Drive System
   :width: 400

Features
--------

-  `Two BLDC motors connected in a dyno setup (BLY171S-24V-4000 and BLY171D-24V-4000) <http://www.anaheimautomation.com/products/brushless/brushless-motor-item.php?sID=143&pt=i&tID=96&cID=22>`_
-  Electronically adjustable load – the load value is set using the onboard buttons + LCD
-  Programmable step and ramp load changes
-  Measurement and display of load motor phase currents
-  Measurement and display of load motor speed

+---+
+---+

Block Diagram
-------------

.. image:: ../images/dyno_diagram.png
   :width: 800

+---+
+---+

Key Parts
---------

+------------------------------------------------+---------------------------------------------------------------------------------------------+
| Power                                          |                                                                                             |
+================================================+=============================================================================================+
| :adi:`ADuM5000`                                | isoPower® integrated isolated dc-to-dc converter                                            |
+------------------------------------------------+---------------------------------------------------------------------------------------------+
| :adi:`ADP3335`                                 | HIGH ACCURACY ULTRALOW QUIESCENT CURRENT, 500 mA, ANYCAP® LOW DROPOUT                       |
+------------------------------------------------+---------------------------------------------------------------------------------------------+
| Isolation                                      |                                                                                             |
+------------------------------------------------+---------------------------------------------------------------------------------------------+
| :adi:`ADUM3223`                                | 3 KV RMS ISOLATED PRECISION HALF-BRIDGE DRIVER, 4 A OUTPUT                                  |
+------------------------------------------------+---------------------------------------------------------------------------------------------+
| Control                                        |                                                                                             |
+------------------------------------------------+---------------------------------------------------------------------------------------------+
| :adi:`ADUC7023`                                | Precision Analog Microcontroller, 12-Bit Analog I/O, ARM7TDMI MCU with Enhanced IRQ Handler |
+------------------------------------------------+---------------------------------------------------------------------------------------------+

+---+
+---+

User Guide
----------

The system is equipped with an LCD which displays information about the state of the load such and together with the 3 push buttons placed below it can be used to display and configure different system parameters. The **+/-** buttons are used to navigate through the system's menu and to change different system parameters, while the **Enter** button is used to confirm parameter changes or to enter / exit the menu screens.

+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Menu diagram | Menu description                                                                                                                                                                   |
+==============+====================================================================================================================================================================================+
| |Dyno menu|  | Main menu is displayed at power up.                                                                                                                                                |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | The measurement menu displays RMS phase currents and motor speed. The load can be adjusted by pressing the "+" or "-" buttons. In order to go back to the main menu press "Enter". |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | Waveforms menu. Select ramp or step load.                                                                                                                                          |
|              | In order to go back select "..." and press "Enter"                                                                                                                                 |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | Step load menu. Select "Step" to start toggling the load.                                                                                                                          |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | Press "+" or "-" to toggle between the preset step values.                                                                                                                         |
|              | In order to go back press "Enter"                                                                                                                                                  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | Set maximum duty cycle.                                                                                                                                                            |
|              | In order to go back press "Enter"                                                                                                                                                  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | Set minimum duty cycle.                                                                                                                                                            |
|              | In order to go back press "Enter"                                                                                                                                                  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | Ramp load menu. Press "+" or "-" to change ramp period.                                                                                                                            |
|              | In order to go back press "Enter"                                                                                                                                                  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | Settings menu.                                                                                                                                                                     |
|              | In order to go back select "..." and press "Enter"                                                                                                                                 |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | Change duty cycle step.                                                                                                                                                            |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              | About.                                                                                                                                                                             |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+---+
+---+

External Control
----------------

In order interface the Dyno with an external control system:

-  Slide switch S2 to EXT_CTRL position
-  Connect to the header P1

.. image:: ../images/dyno_ext_control.png
   :alt: Dynamometer Drive System
   :width: 400

The external available signals are:

=========== ===============================
Dyno Signal Description
=========== ===============================
I_A         Phase A motor current (185mv/A)
I_B         Phase B motor current (185mv/A)
PWM1        Phase A PWM (3.3V levels)
PWM2        Phase B PWM (3.3V levels)
PWM3        Phase C PWM (3.3V levels)
=========== ===============================

+---+
+---+

.. warning::

   The system needs a 5V 500mA power supply. The power connector is a 2.1 X
   5.5MM jack with the center pin positive(+)

Downloads
---------

.. admonition:: Download
   :class: download

   **AD-DYNO2-EBZ**


   -  `Schematics <../resources/ad-dyno2-ebz_schematics.pdf>`_
   -  `Bill of Materials <../resources/ad-dyno2-ebz_bom.zip>`_
   -  `Allegro Board File <../resources/ad-dyno2-ebz_layout.zip>`_ (This file is `compressed <http://www.7-zip.org/7z.html>`_). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_ (You need 16.5 or higher).


.. |Dyno menu| image:: ../images/dyno_menu.png
   :width: 500
