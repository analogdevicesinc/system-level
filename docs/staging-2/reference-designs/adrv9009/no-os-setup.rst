.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9009/no-os-setup

.. _adrv9009 no-os-setup:

ADRV9009/ADRV9008 No-OS System Level Design Setup
=================================================

Supported devices
-----------------

- :adi:`ADRV9008-1`
- :adi:`ADRV9008-2`
- :adi:`ADRV9009`

Supported evaluation boards
---------------------------

- :adi:`EVAL-ADRV9008-9009`
- :adi:`ADRV9009-ZU11EG`
- :adi:`AD-FMCOMMS8-EBZ`

Supported carriers
------------------

- `Intel Arria 10 GX FPGA Development Kit <https://www.intel.com/content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>`__
- :xilinx:`ZC706 <ZC706>`
- :xilinx:`ZCU102 <ZCU102>`
- :adi:`ADRV2CRR-FMC`

Project layout
--------------

The project is located under ``no-OS/projects/adrv9009`` and has the following
layout, with source code under the ``src`` subdirectory and reference profiles
obtained with TES software under ``profiles`` subdirectory.

::

   $ tree
   no-OS/projects/adrv9009
   ├── Makefile
   ├── profiles
   │   ├── tx_bw100_ir122p88_rx_bw100_or122p88_orx_bw100_or122p88_dc122p88
   │   │   ├── talise_config_ad9528.h
   │   │   ├── talise_config.c
   │   │   └── talise_config.h
   │   ├── tx_bw200_ir245p76_rx_bw200_or245p76_orx_bw200_or245p76_dc245p76
   │   │   ├── talise_config_ad9528.h
   │   │   ├── talise_config.c
   │   │   └── talise_config.h
   │   └── tx_bw400_ir491p52_rx_bw200_or245p76_orx_bw400_or491p52_dc245p76
   │       ├── talise_config_ad9528.h
   │       ├── talise_config.c
   │       └── talise_config.h
   ├── src
   │   ├── app
   │   │   ├── app_clocking.c
   │   │   ├── app_clocking.h
   │   │   ├── app_config.h
   │   │   ├── app_jesd.c
   │   │   ├── app_jesd.h
   │   │   ├── app_talise.c
   │   │   ├── app_talise.h
   │   │   ├── app_transceiver.c
   │   │   ├── app_transceiver.h
   │   │   └── headless.c
   │   ├── devices
   │   │   └── adi_hal
   │   │       ├── adi_hal.h
   │   │       ├── common.h
   │   │       ├── LICENSE.txt
   │   │       ├── no_os_hal.c
   │   │       └── parameters.h
   │   └── README
   └── src.mk

The ADRV9009 driver may be found under
``no-OS/drivers/rf-transceiver/talise/api`` and the firmware files under
``no-OS/drivers/rf-transceiver/talise/firmware``.

TES artefacts
-------------

You may use the
:ez:`\|TES software <wide-band-rf-transceivers/tes-gui-software-support-adrv9009-adrv9008-1-adrv9008-2/w/documents/13807/tes-gui-api-software-support-adrv9009->`
to generate profiles and corresponding Stream Binary by graphically selecting
``Tools -> Create Script -> Init .c Files``. This will generate a directory
containing the following files:

::

   ├── headless.c
   ├── headless.h
   ├── talise_config_ad9528.h
   ├── talise_config.c
   ├── talise_config.h
   └── TaliseStream.bin

Profiles
~~~~~~~~

Using the new profile can be achieved by creating a new directory under
``no-OS/adrv9009/profiles`` directory and copying the 3 ``talise_config*`` files
to it and selecting it in the build system.

Let"s say our profile directory is called ""new_profile"", we may select it for
build by making sure the ""PROFILE"" make variable in ``src.mk`` file points to
it:

::

   PROFILE = new_profile

Stream binary
~~~~~~~~~~~~~

After obtaining a ``TaliseStream.bin`` file from the TES GUI, this can be
converted to a header file via this Linux command.

::

   $ xxd -i TaliseStream.bin > talise_stream_binary.h

Should you want to use this generated file, replace
``no-OS/drivers/rf-transceiver/talise/firmware/talise_stream_binary.h`` with it.

Build
-----

.. todo:: .. include: /resources/no-os/build.rst

Build Switches
~~~~~~~~~~~~~~

The project builds by default for ADRV9009-W/PCBZ with whatever carrier is
specified in the hardware files (.hdf or .sopcinfo/.sof).

:adi:`AD-FMCOMMS8-EBZ` support on :xilinx:`ZCU102 <ZCU102>` may be enabled by
adding ``-DFMCOMMS8_ZCU102`` compiler flag or uncommenting the define in
``src/app/app_config.h``.

:adi:`ADRV9009-ZU11EG` support on :adi:`ADRV2CRR-FMC` may be enabled by adding
``-DZU11EG`` compiler flag or uncommenting the define in
``src/app/app_config.h``.

Legacy build instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

We strongly recommend you use the command line build instructions above but if
you would like to perform a manual and graphical project configuration, you may
follow the following legacy build guides for
:dokuwiki:`Intel platforms <resources/fpga/altera/software_setup>` or
:dokuwiki:`Xilinx platforms <resources/fpga/xilinx/software_setup>`.

Demo Applications
-----------------

Make sure to connect your adrv9002 evaluation board to the correct FMC connector
or the carrier you use:

- :dokuwiki:`ADRV9009-W on ZCU102 </resources/eval/user-guides/adrv9009/quickstart/zynqmp>`
- :dokuwiki:`ADRV9009-W on ZC706 </resources/eval/user-guides/adrv9009/quickstart/zc706>`
- :dokuwiki:`ADRV9009ZU11EG on ADRV2CRRFMC </resources/eval/user-guides/adrv9009-zu11eg/quick-start-guide>`
- :dokuwiki:`FMCOMMS8 on ZCU102 </resources/eval/user-guides/ad-fmcomms8-ebz/quick-start-guide>`

.. todo:: .. include: /resources/no-os/dac_dma_example.rst

.. todo:: .. include: /resources/no-os/iiod_demo.rst
