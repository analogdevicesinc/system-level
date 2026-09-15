.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-96tof1-ebz/laserboard

.. _ad-96tof1-ebz laserboard:

AD-96TOF1-EBZ Laser Board
=========================

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tofebz/3dtof laser blk dig.png
   :width: 400px

The laser board generates the IR light pulses to illuminate the scene. It
connects directly to the AFE board and is powered and controlled through the
interface connector, with an option of external power if needed for specific use
case with different VCSEL.

**Key parts:**

- *VCSEL:* Finisar I940-G2332-NBC-D1-110B85R
- *MOSFET driver:* :adi:`ADP5202`
- *MOSFET:* EPC2007C
- *Temperature measurement:* :adi:`ADT7410`
- *Power:* :adi:`ADP2504`

.. note::

   The previous board versions (Rev. B and Rev. C) use MOSFET driver:
   :adi:`ADP3624`

--------------

.. admonition:: Download

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tofebz/tof_laser_revb.zip`

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tofebz/tof_laser_revc.zip`

   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-96tofebz/tof_laser_revd.zip`
