.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/user-guide/software

.. _adrv9361z7035 software:

ADRV9361-Z7035 User Guide - Software
====================================

The Zynq SoC onboard the ADRV9361-Z7035 SDR 2X2 contains Dual ARM® Cortex™-A9
MPCore™ processors capable of running a variety of operating systems and is
supported by an ecosystem of development tools.

Getting Started
---------------

To quickly explore the reference design, here are some resources:

- The :ref:`SD card image <kuiper>` used to boot the reference design.
- The :ref:`adrv9361z7035` page provides details about reference designs.
- The :git-hdl:`HDL </>`, :git-no-OS:`no-OS </>` and :git-linux:`Linux <main:/>`
  sources are hosted on GitHub.

  - For HDL, we highly recommend cloning from the
    :git-hdl:`latest official release <releases+>` (released twice per year),
    not the development branch. See :external+hdl:ref:`releases`.

    - For example, choose branch hdl_2015_r2 to get the second release of 2015.
      Notice the supported AMD Xilinx Vivado tool version.

      .. image:: images/adigit_hub_hdl_repository.png
         :alt: Selecting a release branch in the HDL GitHub repository
         :width: 600

  - The Tcl scripts to build the Vivado project for this carrier are located in
    :git-hdl:`projects/adrv9361z7035`.
  - The :external+hdl:ref:`user_guide` explains how to rebuild the FPGA project.

.. note::

   The reference design is based on the HDL code maintained by Analog Devices.
   To manage dependencies in the build process for Vivado projects, Analog
   Devices provides Linux-based makefiles. Windows users can build Vivado
   projects using ``make`` under Cygwin; see
   :external+hdl:ref:`build_hdl cygwin`.

Operating Systems
-----------------

The following operating systems are supported on the Zynq ARM processors. The
most up-to-date and comprehensive list can be found on the
:xilinx:`AMD Xilinx website <products/design-tools/software-zone/embedded-computing.html>`,
however the following section will give you an idea of the popular options.
Most software developers will start with the Linux reference design and drivers
provided by Analog Devices at the GitHub page listed below. Analog Devices also
provides details of the Linux reference design for ADRV9361-Z7035 SDR at
:ref:`adrv9361z7035`.

Non-Commercial OS
~~~~~~~~~~~~~~~~~

- Linux, U-Boot, and more on `AMD Xilinx GitHub <https://github.com/xilinx>`__
  and `Analog Devices GitHub <https://github.com/analogdevicesinc>`__
- :xilinx:`PetaLinux tools <products/design-tools/embedded-software/petalinux-sdk.html>`
- Android

Commercial OS
~~~~~~~~~~~~~

- `Wind River Linux <https://www.windriver.com/products/linux>`__

RTOS
~~~~

- `eCos <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18842266/eCOS>`__
- `FreeRTOS <https://www.freertos.org/>`__
- `Micrium uC/OS-II/III <https://www.micrium.com/>`__
- `QNX <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/628523012/BlackBerry+QNX>`__
- `Wind River VxWorks <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/625934388/Wind+River>`__

Prototype and Development Tools
-------------------------------

AMD Xilinx Vivado® Design Suite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Download a free evaluation from :xilinx:`support/download.html`.
- Purchase a license at Avnet Express.

MathWorks Native Support
~~~~~~~~~~~~~~~~~~~~~~~~

Communications System Toolbox™ Support Package for Xilinx® Zynq®-Based Radios
enables you to use :mw:`MATLAB® <products/matlab>` and
:mw:`Simulink® <products/simulink>` to prototype and verify practical wireless
systems. Using this support package with ADRV9361-Z7035, you can transmit and
receive RF signals right out-of-the-box. This enables you to quickly test your
design under real world conditions.

Some useful links for more information are provided as follows:

- :mw:`Zynq SDR Support from Communications System Toolbox <hardware-support/zynq-sdr.html>`
- :mw:`Free Trial Software for Software-Defined Radio Design Using PicoZed SDR <picozedsdr-trial>`
- :ref:`MATLAB Filter Design Wizard for AD9361 <fmcomms2 software filters>`
- :mw:`SimRF Models of the AD9361 Agile RF Transceiver <hardware-support/analog-devices-rf-transceivers.html>`

MathWorks Support by Analog Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices works closely with MathWorks to develop custom capabilities for
the ADRV9361-Z7035 SDR. For example, MathWorks HDL Workflow Advisor support plus
MATLAB and Simulink data exchange over Ethernet with IIO System Object. Some
useful links for more information are provided as follows:

- :ref:`Analog Devices BSP for MathWorks HDL Workflow Advisor <matlab transceiver-toolbox>`
- :dokuwiki:`MATLAB and Simulink data exchange over Ethernet with IIO System Object <resources/tools-software/linux-software/libiio/clients/matlab_simulink>`

Drivers, Source Code, and Reference Designs
-------------------------------------------

Analog Devices provides a comprehensive set of drivers, source code, reference
designs, and other technical resources for the ADRV9361-Z7035 SDR. More
information may be found on the :ref:`adrv9361z7035` page. A source code
support package is hosted on
`GitHub <https://github.com/analogdevicesinc>`__, including the HDL and
software code.

Analog Devices AD9361 RF Agile Transceiver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices provides complete drivers for the AD9361 for both bare
metal/no-OS and operating systems (Linux). The AD9361 and AD9364 share the same
API. The AD9361 and AD9364 drivers can be found at:

- :external+linux:ref:`Linux <ad9361>`
- :external+no-OS:doc:`no-OS <drivers/rf-transceiver/ad9361>`

Support for these drivers can be found at:

- :ez:`Linux <linux-software-drivers>` EngineerZone page
- :ez:`no-OS <microcontroller-no-os-drivers>` EngineerZone page

In addition, Analog Devices provides FPGA
:external+hdl:ref:`HDL source code <adrv9361z7035>` for the Zynq SoC.

AMD Xilinx Zynq-7000 AP SoC
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices provides complete drivers for the Zynq SoC ARM peripherals,
including those implemented on the ADRV9361-Z7035 SDR 2X2 module.

- Ethernet Linux MDIO driver
- USB Linux driver
- SDIO Linux driver

These are included in the Linux kernel images provided with :ref:`kuiper`.

MATLAB and Simulink Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These designs demonstrate high bandwidth data transfer between ADRV9361-Z7035
SDR and MATLAB or Simulink running on a host PC. They also provide examples of
designing custom baseband functions in the Zynq SoC.

- :ref:`Stream data into/out of MATLAB <matlab transceiver-toolbox>`
- :ref:`fmcomms2 software beacon-frame-receiver`
- :ref:`fmcomms2 software qpsk-example`
- :ref:`fmcomms2 software lte-example`
- :ref:`fmcomms2 software adsb-example`
