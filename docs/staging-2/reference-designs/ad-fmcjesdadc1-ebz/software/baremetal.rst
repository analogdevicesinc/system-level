.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcjesdadc1-ebz/software/baremetal

.. _ad-fmcjesdadc1-ebz software baremetal:

AD-FMCJESDADC1-EBZ Bare Metal Quick Start Guide
===============================================

Xilinx Platform
---------------

This guide provides some quick instructions on how to setup the
AD-FMCJESDADC1-EBZ on either:

- :xilinx:`KC705 <KC705>`
- :xilinx:`VC707 <VC707>`
- :xilinx:`ZC706 <ZC706>`

Downloads
~~~~~~~~~

.. admonition:: Download

   - AD-FMCJESDADC1-EBZ Main, AD9250, AD9517 Drivers -
     :git-no-OS:`ad-fmcjesdadc1-ebz`
   - Platform Drivers - :git-no-OS:`common_drivers/platform_drivers`
   - ADC Core Driver - :git-no-OS:`common_drivers/adc_core`
   - XCVR Driver - :git-no-OS:`common_drivers/xcvr_core`
   - JESD204B Driver - :git-no-OS:`common_drivers/jesd_core`

Required Software
~~~~~~~~~~~~~~~~~

- We upgrade the Xilinx tools on every release. The supported version number can
  be found in our
  `git repository <https://github.com/analogdevicesinc/hdl/tree/master>`__.
- A :dokuwiki:`UART </resources/fpga/uart_setup>` terminal (Tera
  Term/Hyperterminal), baud rate 115200.

Software Setup
~~~~~~~~~~~~~~

- With every release, we add new features, check the generic build process:
- :dokuwiki:`make </resources/fpga/no-os_make/software_setup>`
- :dokuwiki:`GUI </resources/fpga/xilinx/software_setup>` (manual)
