.. _adrv9009-zu11eg phase-sync:

ADRV9009-ZU11EG Phase Synchronization
======================================

Phase sync ADRV9009 feature
-----------------------------

A multichip synchronization script is available in the
`linux_image_ADI-scripts <https://github.com/analogdevicesinc/linux_image_ADI-scripts>`__
repository:

-  `adrv9009_multichip_sync.sh <https://github.com/analogdevicesinc/linux_image_ADI-scripts/blob/master/adrv9009_multichip_sync.sh>`__

DMA Gating
----------

Steps:

#. Stop sysref
#. Write to sync bit
#. Check sync bit
#. Configure DMA
#. Generate sysref pulse
#. Pull DMA buffer
