.. _eval-cn0506-fmcz prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The :adi:`EVAL-CN0506-FMCZ` FMC evaluation board
#. An FPGA carrier platform. Our supported platforms are:

   - `Arria 10 SoC <https://www.altera.com/products/fpga/arria-10/sx-series>`_
   - :xilinx:`Zynq-7000 (ZC706, Zed Board)`
   - :xilinx:`Zynq UltraScale+ (ZCU102) <products/silicon-devices/soc/zynq-ultrascale-mpsoc.html>`

#. Some way to interact with the FPGA platform:

   #. for the ARM/FPGA SoC platforms, this normally includes:

      - HDMI or DisplayPort monitor
      - USB Keyboard
      - USB Mouse

   #. for all platforms, you will also need:

      - Ethernet cable
      - UART USB cable 
         
         - Mini USB for Intel Arria 10 SoC
         - Micro USB for Xilinx Zynq-7000 and Zynq UltraScale+

#. SD Card with at least 16GB of memory. You should have received one when
   purchasing the evaluation board.
#. Power supply for the carrier board

Software prerequisites
-------------------------------------------------------------------------------

#. MicroSD Card imaged with :external+kuiper:doc:`Kuiper Linux <index>`
#. A UART terminal (Putty/Tera Term/Minicom, etc.) configured for 115200 baud
   rate (8N1)
#. Boot files for your carrier platform (provided on the SD card or built
   manually)

.. note::

   Some carrier boards may require hardware modifications or rework. Please
   consult your specific board's quickstart guide for details before proceeding.

Getting Started
-------------------------------------------------------------------------------

Follow the detailed setup instructions in your carrier board's quickstart guide:

- :ref:`eval-cn0506-fmcz quickstart zc706`
- :ref:`eval-cn0506-fmcz quickstart zcu102`
- :ref:`eval-cn0506-fmcz quickstart zed`
- :ref:`eval-cn0506-fmcz quickstart a10soc`