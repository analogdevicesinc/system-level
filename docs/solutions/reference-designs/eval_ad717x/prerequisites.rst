.. _prerequisites:

Prerequisites
===============================================================================

What you need depends on which workflow you intend to follow. All workflows
require an AD717x/AD411x-based evaluation board as a starting point.

Common Hardware
-------------------------------------------------------------------------------

An :adi:`AD717x <en/lp/001/ad717x-family.html>`/:adi:`AD411x <en/products/ad4111.html>`-based
evaluation board:

- :adi:`EVAL-AD4111SDZ`
- :adi:`EVAL-AD4112SDZ`
- :adi:`EVAL-AD4113SDZ`
- :adi:`EVAL-AD4114SDZ`
- :adi:`EVAL-AD4115SDZ`
- :adi:`EVAL-AD7172-4SDZ`
- :adi:`EVAL-AD7172-2SDZ`
- :adi:`EVAL-AD7173-8SDZ`
- :adi:`EVAL-AD7173-8ARDZ`
- :adi:`EVAL-AD7175-2SDZ`
- :adi:`EVAL-AD7175-8`
- :adi:`EVAL-AD7175-8ARDZ`
- :adi:`EVAL-AD7177-2SDZ`

ACE Software Evaluation
-------------------------------------------------------------------------------

- :ref:`ace`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`EVAL-AD7173-8ARDZ` evaluation board (or compatible eval board)
- :adi:`SDP-K1 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`
  controller board
- USB Type-A to USB Micro-B cable

Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`ACE (Analysis | Control | Evaluation) software
  <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`

  - Install with **Precision Converter Components** selected
  - Enable the **LibIIO Wrapper** during installation

.. DE10-Nano No-OS Quickstart
.. -------------------------------------------------------------------------------
..
.. Reference: :ref:`eval_ad717x de10nano`

.. Hardware
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..
.. - Any AD717x/AD411x evaluation board (see `Common Hardware`_ above)
.. - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
..   FPGA development board
..
..   - 5 V/2 A wall power supply with barrel jack (included with DE10-Nano)
..   - Mini-USB to USB Type-A cable (included with DE10-Nano)
..
.. - Ethernet cable
.. - UART terminal application (e.g. Tera Term, PuTTY, or Minicom)
..   at 115200 baud (8N1)
..
.. Software
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
..
.. - `Intel Quartus Prime
..   <https://www.intel.com/content/www/us/en/products/details/fpga/development-tools/quartus-prime.html>`_
..   (Lite edition is sufficient)
.. - :external+no-OS:doc:`AD717x No-OS Driver <drivers/adc/ad717x>`

Renesas RL78G13 Microcontroller No-OS Driver
-------------------------------------------------------------------------------

Reference: :ref:`ad7175-mcu-driver`,
:ref:`ad7176-mcu-driver`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `Renesas Demo Kit for RL78G13 (YRDKRL78G13)
  <https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rl78-low-power-8-16-bit-mcus/yrdkrl78g13-yrdkrl78g13-demonstration-kit-rl78g13>`_
- :adi:`EVAL-AD7175-2SDZ` (for the AD7175-2 driver) or
  :adi:`EVAL-AD7176-2SDZ <en/products/ad7176-2.html>` (for the AD7176-2 driver)
- Five jumper wires for the SPI connection (CS, DIN, DOUT, SCLK, GND)

Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `IAR Embedded Workbench for Renesas RL78 Kickstart
  <https://www.iar.com/embedded-development-tools/iar-embedded-workbench/>`_

FMC-SDP Interposer / AMD KC705 Reference Design
-------------------------------------------------------------------------------

Reference: :ref:`interposer`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `AMD KC705 FPGA board
  <https://www.amd.com/en/products/adaptive-socs-and-fpgas/evaluation-boards/ek-k7-kc705-g.html>`_
- FMC-SDP adapter board
- :adi:`EVAL-AD7175-2SDZ` or :adi:`EVAL-AD7176-2SDZ <en/products/ad7176-2.html>` evaluation board

Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Xilinx ISE 14.3

.. note::

   ADI does not offer FPGA carrier platforms for sale or loan; obtaining
   one is a normal part of the development or evaluation process.
