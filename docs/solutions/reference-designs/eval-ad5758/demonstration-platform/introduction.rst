.. _introduction:

Introduction
===============================================================================

When designing channel-to-channel isolated analog output modules for
process control applications such as programmable logic controller (PLC)
or distributed control system (DCS) modules, the main trade-off usually
considered is power dissipation vs. channel density. As module sizes
shrink, and channel density increases, the power dissipation budget per
channel must decrease to accommodate the maximum power dissipation budget
for the module. Higher channel density also means that there is less PCB
real estate available for each channel.

.. figure:: ../images/01-08-2019_14-52-59.png
   :align: center

   Block diagram of a single channel

This Board is a demonstration a system level solution where the :adi:`AD5758`
and the :adi:`ADP1031` can be used together to implement a compact, eight
channel, channel-to-channel isolated, precision analog output (AO)
module, while achieving less than 2 W worst case power dissipation over
a wide range of operating conditions.

The :adi:`ADP1031` solves the isolation and size challenges and the
:adi:`AD5758` provides a low power dissipation, precision, configurable current
or voltage output channel.

This board uses the :adi:`ADUCM3029` as the system controller to control each
channel independently.

.. figure:: ../images/block_diagram.png
   :align: center

   Eight Channel Board
