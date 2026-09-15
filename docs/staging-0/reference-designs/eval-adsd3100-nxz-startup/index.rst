.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adsd3100-nxz-startup

.. _eval-adsd3100-nxz-startup:

EVAL-ADSD3100-NXZ Startup Guide
===============================

Kit Contents
------------

- ADSD3100-NXZ Evaluation Module

  - ADSD3100 Imager Module
  - i.MX8 M Plus SOM (SolidRun)
  - Camera Interface Board

- 16GB flashed microSD card (Inserted in module sd card slot)
- Anker USB Hub
- USB-C to USB-C cable. Supports PD 2.0, and USB 3.1

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100-nxz-kit.jpg
   :width: 400px

Software Download
~~~~~~~~~~~~~~~~~

- GUI Install Guide:
  :dokuwiki:`link </resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`

Startup
~~~~~~~

- :dokuwiki:`Install Software Package </resources/eval/user-guides/eval-adsd3100-nxz-software-installation>`
- Remove camera from packaging
- Mount camera. Orientation shown in image below

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_w_enc.png
   :width: 400px

- Connect USB-C cable to module

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_usbc_sdcard.jpg
   :width: 200px

- Connect USB-C to laptop
- Wait for green light under the USB-C connector on the module light up
- Run :dokuwiki:`GUI </resources/eval/user-guides/eval-adsd3100-nxz-gui>`

.. important::

   If mp_pcm mode does not work (ie. GUI is stuck/crashes), disconnect USB-C
   Cable from laptop. Connect module to USB-C hub 5Gbps port (highlighted by
   white box), and connect hub to pc. Restart the GUI and try again.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_hub.jpg
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adsd3100_kit_w_hubandlaptop.jpg
   :width: 400px

Troubleshooting
~~~~~~~~~~~~~~~

- GUI Crash

  - Ensure that that mode switching is done after module is stopped
  - If the GUI is always crashing, particularly for mp_pcm, the module is likely
    not getting enough power. If adding the hub did not fix the issue, it is
    likely that the host port does not support the power requirements.

- Green light under USB-C Connector not turning on

  - SD-Card could be corrupted. "Firmware Flashing Link"
