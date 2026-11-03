.. _ad719x_asdz_prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. One of the EVAL-AD719xASDZ evaluation boards:

   - :adi:`EVAL-AD7190ASDZ`
   - :adi:`EVAL-AD7192ASDZ`
   - :adi:`EVAL-AD7193ASDZ`
   - :adi:`EVAL-AD7194ASDZ`
   - :adi:`EVAL-AD7195ASDZ`

#. A controller board. The supported options are:

   - :adi:`EVAL-SDP-CK1Z <SDP-K1>`
     (connects via 120-pin or Arduino connectors) with a USB-C cable
   - :adi:`EVAL-SDP-CB1Z <SDP-B>`
     (connects via 120-pin connector only) with a Micro-USB cable
   - `Cora Z7S <https://digilent.com/shop/cora-z7-zynq-7000-single-core-for-arm-fpga-soc-development>`__
     (connects via Pmod JA or Arduino shield) with a Micro-USB cable
   - :intel:`DE10-Nano <content/www/us/en/developer/topic-technology/edge-5g/hardware/fpga-de10-nano.html>`
     (connects via Arduino shield) with a Micro-USB cable

#. A PC running Windows with a USB 2.0 port.

#. Micro SD card with at least 16 GB (required for FPGA carrier boards)

.. warning::

   The evaluation software and drivers must be installed **before** connecting
   the evaluation board and controller board to the PC's USB port, to ensure
   the system is correctly recognized.

Software prerequisites
-------------------------------------------------------------------------------

If using ACE Software (SDP controller boards)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :adi:`ACE Software <ACE>`

#. The ACE plugin matching your device:

   - :adi:`AD7190 ACE Plugin <EVAL-AD7190ASDZ>`
   - :adi:`AD7192 ACE Plugin <EVAL-AD7192ASDZ>`
   - :adi:`AD7193 ACE Plugin <EVAL-AD7193ASDZ>`
   - :adi:`AD7194 ACE Plugin <EVAL-AD7194ASDZ>`
   - :adi:`AD7195 ACE Plugin <EVAL-AD7195ASDZ>`

#. `SDP controller board drivers <http://swdownloads.analog.com/ACE/SDP/SDPDrivers.exe>`_
   (required if not already installed on the PC)

If using IIO Oscilloscope (FPGA carrier boards)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. SD card imaged with :ref:`Kuiper Linux <kuiper>`

#. :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`

#. A serial terminal (PuTTY, Tera Term, Minicom, etc.) configured
   at 115200 baud (8N1)
