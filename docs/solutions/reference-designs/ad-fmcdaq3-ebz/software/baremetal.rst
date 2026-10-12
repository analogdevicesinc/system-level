.. _ad-fmcdaq3-ebz software baremetal:

.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq3-ebz/software/baremetal

.. _ad_fmcdaq3_ebz baremetal:

AD-FMCDAQ3-EBZ Baremetal (no-OS) Guide
======================================

This guide provides some quick instructions on how to build and run the
AD-FMCDAQ3-EBZ on most of the supported platforms. As of this writing, the
following carriers are supported. You must always check with the github sources
to get a full list of supported carriers as this document may not reflect any
recent additions.

Altera Platform(s)
------------------

- `Arria 10 GX FPGA Development Kit <https://www.intel.com/content/www/us/en/products/details/fpga/development-kits/arria/10-gx.html>`__

AMD Xilinx Platform(s)
----------------------

-  :xilinx:`ZC706`
-  :xilinx:`KCU105`

Downloads
~~~~~~~~~

.. admonition:: Download
   :class: download

   -  HDL (hdl_2016_r2\* release) -
      https://github.com/analogdevicesinc/hdl/tree/hdl_2016_r2/projects/daq3
   -  no-OS (2016_R2\* release) -
      https://github.com/analogdevicesinc/no-OS/tree/2016_R2/fmcdaq3

   Please check with the github pages for latest and previous releases and
   consult the release notes for more information.

Building HDL
~~~~~~~~~~~~

ADI do not distribute the bit/elf files of these projects. They must be built
from the sources. The HDL user guide provides detailed information and steps to
build the DAQ3 project on your desired carrier. The build flow is developed
around GNU make. You may use a windows or linux OS, but do NOT seek OS- specific
support. The prerequisite to the building process is that you be able to run
'quartus', 'vivado' and 'make' all from a shell (Cygwin or Linux). Now, building
the HDL is as simple as running make on your desired carrier.

.. shell::

   hdl/projects/daq3/a10gx
   $make MMU=0

.. shell::

   hdl/projects/daq3/kcu105
   $make

.. shell::

   hdl/projects/daq3/zc706
   $make

Please note that for Altera devices, it is important to set MMU=0. As Altera HAL
do not support run-time MMU and the default bit files are intended for linux and
uses MMU.

Building no-OS
~~~~~~~~~~~~~~

After you built the HDL, you may build the no-OS elf files using the same make
flow.

.. shell::

   no-OS/fmcdaq3/a10gx
   $make

.. shell::

   no-OS/fmcdaq3/kcu105
   $make

.. shell::

   no-OS/fmcdaq3/zc706
   $make

The default flow assumes you have cloned (or downloaded) the sources under the
same directory. If you have a different directory structure override the
defaults using SOPCINFO-FILE or HDF-FILE variables.

.. shell::

   no-OS/fmcdaq3/a10gx
   $make SOPCINFO-FILE=<your-directory/hdl/projects/daq3/a10gx/system_bd.sopcinfo>

.. shell::

   no-OS/fmcdaq3/kcu105
   $make HDF-FILE=<your-directory/hdl/projects/daq3/kcu105/daq3_kcu105.sdk/system_top.hdf>

.. shell::

   no-OS/fmcdaq3/zc706
   $make HDF-FILE=<your-directory/hdl/projects/daq3/zc706/daq3_zc706.sdk/system_top.hdf>

Running no-OS
~~~~~~~~~~~~~

If your carrier is an AMD Xilinx board, you will need to setup a UART terminal
(115200). Altera carriers uses the nios2-terminal. Make the JTAG/UART
connections as per your carrier instructions and run the software on hardware.

.. shell::

   no-OS/fmcdaq3/a10gx
   $make run

.. shell::

   no-OS/fmcdaq3/kcu105
   $make run

.. shell::

   no-OS/fmcdaq3/zc706
   $make run

Using Eclipse GUI
~~~~~~~~~~~~~~~~~

You may use the Eclipse GUI, but this is all up to you. Set your workspace as
the carrier of your choice and all the application and bsp folders should be
there in the GUI. However, please note, while you should seek support on any
hardware or software related to the DAQ3 board, please do not ask us about tool
specific issues whether it be Quartus, Vivado, Eclipse-SDK and such.

Signal-Tap/ILA Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

The default HDL in most cases do NOT instantiate any monitoring cores. The HDL
design is primary intended for Linux use. You may modify the design to add the
debug cores and re-run the make flow.

Understanding/Modifying things
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The best place to start in the no-OS main function in "fmcdaq3.c". It shows how
individual components of a data path chain are initialized and programmed for
the application. After you have the default setup working, feel free to add your
own customization routines and/or signal processing functions to either HDL or
no-OS. It is okay if you break the design, the best way to learn something is
breaking and making it (of course, this does NOT apply to the actual hardware).
