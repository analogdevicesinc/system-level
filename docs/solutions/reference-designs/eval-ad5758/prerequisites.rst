.. _eval_ad5758 prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The AD5758 evaluation board: :adi:`EVAL-AD5758SDZ`
#. FMC Interposer Board: `EVAL-SDP-CK1Z
   <https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-SDP-CK1Z.html>`_
   (FMC-I-SDP)

   - Required to connect the SDP-format EVAL-AD5758SDZ to the ZedBoard's FMC
     connector.

#. An FPGA carrier platform. Our recommended platform can be found
   :ref:`here <eval_ad5758 carriers>`.

   - The ZedBoard is the officially supported platform for this evaluation
     board.
   - The evaluation board connects via the FMC LPC connector using the
     FMC-I-SDP interposer.

#. Some way to interact with the FPGA platform:

   #. For the ZedBoard (ARM/FPGA SoC platform), this normally includes:

      - USB cable for UART communication (required)
      - JTAG connection via USB (required for programming)

   #. A microSD card (16 GB or larger recommended) and an SD card reader to
      prepare the boot image.

#. Power supply for the evaluation board:

   - A bench-top power supply capable of 24 V, with connector cables, for the
     PVIN input of the EVAL-AD5758SDZ.

#. Equipment to measure the DAC output:

   - Digital multimeter (DMM), precision current meter, or oscilloscope
   - Appropriate load resistors or current loop for the output range under test

#. Internet connection to download HDL and no-OS source code and build tools
   (firewalls are OK, proxies may require additional configuration).

Software prerequisites
-------------------------------------------------------------------------------

For basic functionality and data visualization, you will need:

HDL Build Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build the HDL reference design, you need:

#. AMD Xilinx Vivado Design Suite (version specified in the
   `HDL Release Notes <https://github.com/analogdevicesinc/hdl/releases>`_)
#. Make (GNU Make for building the HDL project)
#. Git (for cloning the HDL repository)

See the :external+hdl:doc:`HDL User Guide <index>` for detailed
tool installation and build instructions.

No-OS Build Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example uses the no-OS software. To build it, you need:

#. ARM cross-compiler toolchain (e.g., arm-none-eabi-gcc)
#. Make (GNU Make for building the no-OS project)
#. Git (for cloning the no-OS repository)

See :external+no-OS:doc:`build_guide` for detailed setup instructions.

Optional Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For enhanced evaluation and console access:

#. Serial terminal application (e.g., PuTTY, Tera Term, minicom) for UART
   communication - required for viewing console output and DAC status

.. note::

   :adi:`Analog Devices <>` does not offer FPGA carrier platforms for sale or
   loan; obtaining one yourself is the normal part of development or evaluation.

Recommended Reading
-------------------------------------------------------------------------------

Before starting, it's recommended to review:

#. :adi:`AD5758 Datasheet <AD5758>` - for device specifications and features
#. `EVAL-AD5758 User Guide (UG-1268)
   <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad5758-ug-1268.pdf>`_ -
   for evaluation board details
#. :external+hdl:doc:`ADI Reference Designs HDL User Guide <index>` -
   for understanding the HDL framework
#. :external+no-OS:doc:`no-OS documentation <index>` - for no-OS driver and
   project structure

.. note::

   :adi:`ADI <>` does not offer FPGA carrier boards or :adi:`SDP-K1` boards
   for sale or loan; obtaining the hardware is the normal part of development
   and evaluation.
