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
.. Reference: :ref:`eval-ad717x de10nano`

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

