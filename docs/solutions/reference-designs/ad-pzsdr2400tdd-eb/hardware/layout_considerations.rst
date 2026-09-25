Layout Considerations
=====================

The :adi:`ADL5324` has several passive components surrounding the IC which
directly influence the tuning frequency of the device. The location of these
capacitors is critical to the accurate determination of the tuning frequency.

.. figure:: ../images/tuning_component_placement.png
   :align: center
   :width: 800

   Tuning component placement.

The component spacing for tuning capacitors C1 and C2 is detailed in the
:adi:`ADL5324` datasheet over a variety of frequencies. A table from the
datasheet, detailing this information, is listed below.

.. figure:: ../images/tuning_component_table.png
   :align: center
   :width: 800

   Tuning component table from datasheet.

Placement of the AC coupling capacitors, power supply bypassing capacitors and
DC bias inductor should follow the recommendation of the datasheet, but are
slightly less critical than the tuning capacitors.
