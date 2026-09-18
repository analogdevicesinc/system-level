Pre-release SD Card Creation
============================

.. note::

   This page is archived. The content below refers to the 2019_r1 and
   2018_r2 releases. For current SD card setup instructions, refer to
   the :ref:`Quickstart guide <adrv9009-zu11eg quickstart>`.

Writing the SD Card
-------------------

Details on how to write the SD card can be found at
:dokuwiki:`Zynq Images <resources/tools-software/linux-software/zynq_images>`.

ADRV9009-ZU11EG Specific Boot Files
-----------------------------------

After writing the image, on the boot partition root, the ADRV9009-ZU11EG
specific files can be added from any folder matching
\**zynqmp-adrv9009-zu11eg-revb-adrv2crr-fmc-revb\*** from boot partition.
More information can be found in boot partition ReadMe.txt.

Video Configuration
-------------------

The default configuration for most of the projects is to use the HDMI output,
but for this project the DisplayPort is used. In order for it to work, you should
follow the steps described here:
:ref:`DisplayPort - no picture? <linux-kernel zynqmp>`
After following the steps, the board should be rebooted.
