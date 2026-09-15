.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad9083/ad9083_evb_reference_hdl

.. _ad9083 ad9083_evb_reference_hdl:

AD9083 FMC Card HDL Reference Design
====================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page
   is outdated and the new one can be found at
   https://analogdevicesinc.github.io/hdl/projects/ad9083_evb/index.html

Overview
--------

The AD9083 is a 16-bit, 16 channel with 125 MHz bandwidth per channel (2 GSPS
total) analog-to-digital converter (ADC) featuring an on-chip programmable,
single-pole antialiasing filter and termination resistor that is designed for
low power, small size, and ease of use.

The dual ADC cores feature a multistage, differential pipelined architecture
with integrated output error correction logic. Each ADC features wide bandwidth
inputs supporting a variety of user-selectable input ranges.

The AD9083_EVB reference design is a processor based (e.g. Microblaze) embedded
system. The design consists of a receive chain.

The receive chain transports the captured samples from ADC to the system memory
(DDR). Before transferring the data to DDR the samples are stored in a 33Mbit
buffer implemented on block rams from the FPGA fabric (util_adc_fifo) or 65k
samples per channel.

All cores from the receive chain are programmable through an AXI-Lite interface.

Supported Devices
-----------------

- :adi:`AD9083`

https://wiki.analog.com/resources/eval/ad9083

Supported Carriers
------------------

- :xilinx:`ZCU102 <ZCU102>` - HPC0 Slot
-
  `A10SOC <https://www.intel.com/content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>`__
  - FMC A (J29)

Required Hardware
-----------------

- :adi:`AD9083`
- :xilinx:`ZCU102 <ZCU102>` /
  `A10SOC <https://www.intel.com/content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>`__
- FMC extender (for A10SOC setup)

Block Diagram
~~~~~~~~~~~~~

For both platforms, the link is set for full bandwidth mode and operate with the
following parameters:

Deframer paramaters: L=4, M=16, F=8, S=1, N"=16

GTREFCLK – 500MHz LINKCLK(Lane Rate/40) – 250MHz DEVICECLK - 125 MHz ADCCLK –
2000MHz JESD204B Lane Rate – 10Gbps

Beacause of the F=8 parameter the JESD Link IP will have different input and
output frequencies and bus widths. Data will enter the IP on 4 32bit wide
channels (128b) at 250MHz (link clock) and will exit on a 256bit interface
clocked at 125MHz (device clock). The transport layer component presents on its
output 256 bits at once on every clock cycle, representing 1 sample per
converter. The receive chain is then transferred to the DDR using a DMA.

The data path and clock domains are depicted on the below diagram:

Xilinx
^^^^^^

.. figure:: https://wiki.analog.com/_media/resources/fpga/docs/AD9083_evb_2.svg
   :width: 800px

The design has one JESD receive chain with 4 lanes at rate of 10Gbps. The JESD
receive chain consists of a physical layer represented by an XCVR module, a link
layer represented by an RX JESD LINK module and transport layer represented by a
RX JESD TPL module. The links operate in Subclass 0 since it is not using the
SYSREF signal.

Intel
^^^^^

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9083_evb_a10soc.svg
   :width: 800px

The design has one JESD receive chain with 4 lanes at rate of 10Gbps. The JESD
receive chain consists of a physical and link layer represented by
AD9083_JESD204 module, and transport layer represented by a AXI_AD9083 module.
The links operate in Subclass 0 since it is not using the SYSREF signal.

Building the HDL project
~~~~~~~~~~~~~~~~~~~~~~~~

ADI does not distribute the bit/elf files of these projects so they must be
built from the sources available
`here <https://github.com/analogdevicesinc/hdl>`__. To get the source you must
`clone <https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>`__
the HDL repository. Then go to the /projects/ad9083_evb/zcu102 location and run
the make command by typing in your command prompt:

**Linux/Cygwin**

::

   user@analog:~$ cd hdl/projects/ad9083_evb/zcu102
   user@analog:~/hdl/projects/ad9083_evb/zcu102$ make

A more comprehensive build guide can be found in the
:dokuwiki:`HDL User Guide </resources/fpga/docs/hdl>`.

HDL Downloads
-------------

.. admonition:: Download

   :git-hdl:`projects/ad9083_evb`

Software sources
----------------

.. admonition:: Download

   :git-linux:`/`
   :git-no-OS:`projects/ad9083`

More Information
~~~~~~~~~~~~~~~~

- :dokuwiki:`Evaluating Using the ADS8-V3EBZ FPGA-Based Capture Board </resources/eval/ad9083>`
- :dokuwiki:`AD9083 Linux Driver </resources/tools-software/linux-drivers/iio-adc/ad9083>`
- :dokuwiki:`ADI Reference Designs HDL User Guide </resources/fpga/docs/hdl>`
- :dokuwiki:`Generic JESD204B block designs </resources/fpga/docs/hdl/generic_jesd_bds>`
- :external+hdl:ref:`jesd204`

Support
-------

Analog Devices will provide limited online support for anyone using the
reference design with Analog Devices components via the
:ez:`EngineerZone <community/fpga>`.
