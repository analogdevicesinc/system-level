.. _quadmxfe prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

Quad-MxFE platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. The :adi:`AD9081`-based evaluation board:
   :adi:`ADQUADMXFE1EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Quad-MxFE.html>`
#. An FPGA carrier platform: :xilinx:`VCU118`. See :ref:`supported carriers
   <quadmxfe quickstart carriers>`.
#. 12V, 9A+ wall supply and power cable (included in the kit)
#. FMC+ Extender (included in the kit)
#. 2x 6" MMCX-to-MMCX cables (included in the kit)
#. 3x Board Standoffs (included in the kit)
#. Fan/heat sinks (included in the kit) — **install prior to first use** per
   :ref:`Fan Installation Directions <quadmxfe boardhardwaredetails>`
#. 500 MHz reference oscillator or waveform generator (~0 dBm)
#. 2x USB Micro cables (UART + JTAG)
#. Ethernet cable

   *NOTE: do not use the Ethernet cable that comes with the VCU118 board. It is
   a crossover cable and will not work with the platform*

#. 50 Ohm SMA cables — as needed
#. (Optional) USB to Ethernet dongle for direct connection

With Calibration Board (ADQUADMXFE-CAL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following are needed only if using the optional
:ref:`16Tx/16Rx Calibration Board <quadmxfe calboard>` (sold separately):

#. :ref:`ADQUADMXFE-CAL Calibration Board <quadmxfe calboard>`

   - Includes 12V power supply, PMOD ribbon cable, male-to-male 0.1" 12 pin
     header, board standoffs, and 2x 3" MMCX-MMCX cables

#. 32x MMCX-MMCX cables to connect between Quad MxFE Board & Calibration Board
   (2 provided with the ADQUADMXFE-CAL kit, 30 additional required)

   -  https://www.samtec.com/products/rf316-03sp1-03sp1-0100

Software prerequisites
-------------------------------------------------------------------------------

#. :xilinx:`Xilinx Vivado/Vitis <support/download.html>` (includes XSCT for
   programming the FPGA)

#. A UART terminal (PuTTY/Tera Term/Minicom, etc.) with baud rate 115200 (8N1)

#. :ref:`IIO Oscilloscope <quadmxfe iio-oscilloscope>`

   - :git-iio-oscilloscope:`Latest IIO Oscilloscope release <releases+>`
   - :git-libiio:`Latest Libiio release <releases+>`

#. (Optional) MATLAB 2019b or 2020a — see
   :ref:`MATLAB Control Overview <quadmxfe quickbringup matlab-control-overview>`

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan; getting
   one yourself is the normal part of development or evaluation.
