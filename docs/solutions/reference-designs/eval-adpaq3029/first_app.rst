.. _eval-adpaq3029 first_app:

EVAL-ADPAQ3029 - First application [RGB LED]
============================================

-  Setup the hardware as shown :ref:`here <eval-adpaq3029 hw_setup>`.
-  Make sure to use Dev module with LED. Here is the schematics for one such board - :download:`Nexpaq_Glue_Micro_Dev_Board <resources/dev_board.pdf>`.
-  Download the following projects from the :ref:`resources <eval-adpaq3029 resources>` section.

   -  Bootloader
   -  MDK source code

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   :download:`RGB led Firmware <resources/ledapp.zip>`

   :download:`Tile GUI application <resources/moduware.tile.example-led-rgb.zip>`

-  The mapping of the RGB LED with the ADPAQ GPIOs is given below

.. container:: round box

   ========= ==============
   LED color GPIO port used
   ========= ==============
   Red       P1_08
   Green     P0_14
   Blue      P1_09
   ========= ==============

-  Launch the CCES IDE and import the first 3 projects into CCES as explained :ref:`here <eval-adpaq3029 fw_dev import_prj>`.
-  Build and flash the firmware binary (\*.bin) as explained :ref:`here <eval-adpaq3029 fw_dev>`
-  Deploy the tile application as explained :ref:`here <eval-adpaq3029 tile_dev>`
-  Launch the ``Moduware`` app and pair to the gateway (Mini Dev board)
-  Now you should be able to see tile with ``DevMod``.

.. image:: images/tile5.png
   :align: center
   :width: 400

-  Long Press on the ``DevMod`` Tile. Select the ``RGB LED`` tile.

.. image:: images/app1.png
   :align: center
   :width: 400

-  The tile of the RGBLED app which was uploaded earlier will appear as shown in
   the image.

.. image:: images/app2.png
   :align: center
   :width: 400

-  Test the application using GUI, by pressing R, G and B color buttons to
   observe change in the LED color in ADPAQ Dev module.
