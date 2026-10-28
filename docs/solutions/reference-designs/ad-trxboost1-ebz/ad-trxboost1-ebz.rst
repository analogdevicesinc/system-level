.. _ad-trxboost1-ebz user-guide:

User guide
===============================================================================

The :adi:`AD-TRXBOOST1-EBZ` is an add-on board for the
:ref:`AD-FMCOMMS2/3/4/5 <fmcomms2>` platform. It adds a pre-amp to the TX
output and an LNA to the RX input of the :adi:`AD9361`.

.. figure:: images/trxboost1_-_top.jpg
   :align: center
   :width: 500

Hardware guide
-------------------------------------------------------------------------------

Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADL5610 Gain Block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  30MHz to 6 GHz
-  Fixed gain of 18.4dB
-  Noise figure: 2.2dB at 900MHz
-  OIP3: 38.8dBm at 900MHz
-  P1dB: 20.4dBm at 900MHz
-  Single 5V supply

ADL5521 LNA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  400MHz to 4GHz
-  Fixed gain of 20.8dB at 900MHz
-  Noise figure: 0.8dB at 900MHz
-  OIP3: 37.0dBm at 900MHz
-  P1dB: 21.8dBm at 900MHz
-  Single supply between 3V and 5V

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power supply is brought to the AD-TRXBOOST1-EBZ through a 3 pin cable. The
connection is made at P2 (pin1 = 3.3V, pin2 = GND, pin3 = 12V), which sits
directly between TX_IN and RX_OUT.

The power originates from the FMCOMMS3 board, connector P301. It can also come
from an external power supply.

Pin map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/pin_map_-_nlw_2-9-16_.png
   :align: center
   :width: 800

..
   Schematic, PCB Layout, Bill of Materials
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. admonition:: Download
      :class: download

      -  `Rev B Schematics <files/trxboost1_sch.pdf>`_
      -  `Rev B Allegro Board File <files/08_038228b-layout.zip>`_
      -  `Rev B Bill of materials <files/trxboost1_bom.xls>`_
      -  `Rev B Gerbers <files/038228b-fab.zip>`_
         (This file is `compressed <http://www.7-zip.org/7z.html>`_)
      -  Get the `Allegro FREE Physical Viewer
         <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`_
         (You need 16.5 or higher).
