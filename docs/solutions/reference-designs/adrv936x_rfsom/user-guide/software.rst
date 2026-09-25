ADRV9361-Z7035 User Guide - Software
====================================

The Zynq SoC onboard the ADRV9361-Z7035 SDR 2X2 contains Dual ARM® Cortex™-A9
MPCore™ processors capable of running a variety of operating systems and is
supported by an ecosystem of development tools.

Getting Started
---------------

To quickly explore the reference design, here are some resources:

-  The `SD Card Image <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_ used to boot the reference design.
-  The Analog Devices :doc:`ADRV9361-Z7035 SDR Wiki </solutions/reference-designs/adrv936x_rfsom/adrv936x_rfsom>` provides details about reference designs
-  The `HDL <https://github.com/analogdevicesinc/hdl>`_, `no-OS <https://github.com/analogdevicesinc/no-OS>`_ and `Linux <https://github.com/analogdevicesinc/linux>`_ sources are hosted on GitHub

   -  For HDL, we highly recommend cloning from the latest official tag (released twice per year), not the development branch. https://github.com/analogdevicesinc/hdl/releases

      -  For example, choose branch hdl_2015_r2 to get the second release of 2015. Notice the support Xilinx Vivado tool version.
      -

      |image1|

   -  The TCL scripts to build the Vivado project for this carrier are located in /projects/pzsdr/ccfmc
   -  The `ADI Reference Designs HDL User Guide <https://wiki.analog.com/resources/fpga/docs/hdl>`_ explains how to rebuild the FPGA project.

NOTE: The reference design is based on the HDL code maintained by Analog
Devices. To manage dependencies in the build process for Vivado projects, Analog
Devices provides Linux-based makefiles. We recommend that Windows users build
Vivado projects using ‘make’ under CYGWIN. Instructions to install a minimal
version of CYGWIN that will provide a Linux-like environment under Windows are
available here.

Operating Systems
-----------------

The following operating Systems are supported on the Zynq ARM processors. The most up-to-date and comprehensive list can be found `here <https://www.xilinx.com/products/design-tools/software-zone/embedded-computing.html#os>`_ on the Xilinx web site, however the following section will give you an idea of the popular options. Most software developers will start with the Linux reference design and drivers provided by Analog Devices at the GitHub page listed below. Analog Devices also have a wiki page that provides details of their Linux reference design for ADRV9361-Z7035 SDR :doc:`here </solutions/reference-designs/adrv936x_rfsom/adrv936x_rfsom>`.

**Non-Commercial OS**

-  Linux, uBoot, and more on `Xilinx GIT <https://github.com/xilinx>`_ and `Analog Devices GIT <https://github.com/analogdevicesinc>`_
-  PetaLinux tools `here <https://www.xilinx.com/tools/petalinux-sdk.htm>`_
-  Android

**Commercial OS**

-  `Wind River Linux <http://www.freertos.org/>`_

**RTOS**

-  `eCos <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18842266/eCOS>`_
-  `FreeRTOS <http://www.freertos.org/>`_
-  `Micrium uC/OS-II/III <http://www.micrium.com/>`_
-  `QNX <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/628523012/BlackBerry+QNX>`_
-  `Wind River VxWorks <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/625934388/Wind+River>`_

Prototype and Development Tools
-------------------------------

Xilinx Vivado® Design Suite
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Download a free evaluation from www.xilinx.com/support/download.html.
-  Purchase a license at Avnet Express.

MathWorks Native Support
~~~~~~~~~~~~~~~~~~~~~~~~

Communications System Toolbox™ Support Package for Xilinx® Zynq®-Based Radios enables you to use `MATLAB® <https://www.mathworks.com/products/matlab>`_ and `Simulink® <https://www.mathworks.com/products/simulink>`_ to prototype and verify practical wireless systems. Using this support package with ADRV9361-Z7035, you can transmit and receive RF signals right out-of-the-box. This enables you to quickly test your design under real world conditions.

Some useful links for more information are provided as follows:

-  Zynq SDR Support from Communications System Toolbox

   -  www.mathworks.com/hardware-support/zynq-sdr.html

-  Free Trial Software for Software-Defined Radio Design Using PicoZed SDR

   -  www.mathworks.com/picozedsdr-trial

-  MATLAB Filter Design Wizard for AD9361

   -
      wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/filters

-  SimRF Models of the AD9361 Agile RF Transceiver

   -  www.mathworks.com/hardware-support/analog-devices-rf-transceivers.html

::

     *

MathWorks Support by Analog Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices works closely with MathWorks to develop custom capabilities for
the ADRV9361-Z7035 SDR. For example, MathWorks HDL Workflow Advisor support plus
MATLAB and Simulink data exchange over Ethernet with IIO System Object. Some
useful links for more information are provided as follows:

-  Analog Devices BSP for MathWorks HDL Workflow Advisor

   -
      wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp

-  MATLAB and Simulink data exchange over Ethernet with IIO System Object

   -  `matlab_simulink <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/matlab_simulink>`_ []=system&s[]=object

Drivers, Source Code, and Reference Designs
-------------------------------------------

Analog Devices provides a comprehensive set of drivers, source code, reference designs, and other technical resources for the ADRV9361-Z7035 SDR. More information may be found on their :doc:`ADRV9361-Z7035 SDR </solutions/reference-designs/adrv936x_rfsom/adrv936x_rfsom>` wiki page. A source code support package is hosted on `Github <https://github.com/analogdevicesinc>`_, including the HDL and software code.

Analog Devices AD9361 RF Agile Transceiver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices provides complete drivers for the AD9361 for both bare
metal/No-OS and operating systems (Linux). The AD9361 and AD9364 share the same
API. The AD9361 and AD9364 drivers can be found at:

-  `Linux <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`_ wiki page
-  `No-OS <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/baremetal>`_ wiki page

Support for these drivers can be found at:

-  :ez:`Linux <community/linux-device-drivers/microcontroller-no-os-drivers?doc=AD9361_Reference_Manual_UG-570.pdf>` engineer zone page
-  :ez:`No-OS <community/linux-device-drivers/microcontroller-no-os-drivers?doc=AD9361_Reference_Manual_UG-570.pdf>` engineer zone page

In addition, Analog Devices provides FPGA `HDL source code <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl>`_ for the Xilinx Zynq SoC.

Xilinx Zynq-7000 AP SoC
~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices provides complete drivers for the Zynq SoC ARM peripherals,
including those implemented on the ADRV9361-Z7035 SDR 2X2 module.

-  Ethernet Linux MDIO driver
-  USB Linux driver
-  SDIO Linux driver

These are included in the Linux kernel images provided at the `Zynq Images <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_ wiki page.

MATLAB and Simulink Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These designs demonstrate high bandwidth data transfer between ADRV9361-Z7035
SDR and MATLAB or Simulink running on a host PC. They also provide examples of
designing custom baseband functions in the Zynq SoC.

-  `Stream data into/out of MATLAB <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/fmcomms2_3_simulink>`_
-  `Beacon Frame Receiver Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/beacon_frame_receiver_simulink>`_
-  `QPSK Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/qpsk_example>`_
-  `LTE Transmit and Receive Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/lte_example>`_
-  `ADS-B Airplane Tracking Example <https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/adsb_example>`_

.. |image1| image:: ../images/adigit_hub_hdl_repository.png
   :width: 600
