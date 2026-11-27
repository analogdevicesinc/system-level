.. _uartjtag:

ADALM-UARTJTAG
==============

.. image:: adalm-uartjtag.png
   :width: 400px
   :align: right
   :alt: ADLAM-UARTJTAG photo

In a few of the designs we have done, like the
:ref:`pluto` and :ref:`m2k` there hasn't been enough room on the
PCB for serial and JTAG, so we put it on a small breakout board, which
communicates to the main platform with a small 10-pin ribbon cable, which is
known as the :adi:`ADALM-UARTJTAG`.

This includes the Silicon Labs
`CP2103-GM <https://www.silabs.com/Support%20Documents/TechnicalDocs/CP2103.pdf>`__
USB to UART bridge, which you can plug a USB cable into.

This also includes connection to Xilinx JTAG cable as well. You will need a
:xilinx:`Xilinx JTAG Cable <support/documentation/data_sheets/ds593.pdf>` or
`equivalent <https://store.digilentinc.com/jtag-hs3-programming-cable>`__ to use
it.

Hardware
--------

Analog Devices provides a small adapter board
:adi:`ADALM-UARTJTAG` to be used for JTAG and UART, in order
to make that easier for programming and debugging. You are encouraged to use
this on your designs for the same reason we do - the standard JTAG connector is
huge, and there are times where good old fashion console UART is valuable for
doing debug. The 1.8V supply on the connector above is the I/O voltage, and can
be used anywhere between 1.8V and 3.3V.

In the box, you should have received the UARTJTAG board, ribbon cable, and
jumper.

.. image:: adalm-uartjtag.png
   :width: 400px

The PCB includes a jumper, which forces the Zynq to HALT on JTAG. This is great
for halting, and not allowing anything to run, but does pull down a chip select
for SPI flash, and will not allow the SPI flash to be found by the on-chip
bootloader, or by U-Boot. (If you are loading a U-Boot over JTAG).

The pin connector is likely inserted into the ribbon cable:

.. grid::
   :widths: 50 50

   .. image:: uartjtagcablepluspins2.png
      :width: 300px

   .. image:: uartjtagcablepluspins.png
      :width: 200px

but can be removed, and either soldered to the PCB, or left in the ribbon cable,
so you don't lose it.

.. image:: uartjtagcable.png
   :width: 300px

If you do want more, they can be obtained from
`Samtec <https://www.samtec.com/products/ftsh-105-01-l-d>`__,
:digikey:`Digi-Key <SAM10499-ND>` or
`Arrow <https://www.arrow.com/en/products/ftsh-105-01-l-d/samtec>`__.

Anyone is free to use the same pinout on their platform - or copy the schematics
and make it themselves.

Schematic, PCB Layout, Bill of Materials
----------------------------------------

.. admonition:: Download

   :adi:`ADALM-UARTJTAG Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/adalm-uartjtag-designsupport.zip>`

   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project (get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__
      to view)

Device Driver
-------------

.. admonition:: Downlaod

   `CP2103 Drivers <http://www.silabs.com/products/mcu/pages/usbtouartbridgevcpdrivers.aspx>`__

