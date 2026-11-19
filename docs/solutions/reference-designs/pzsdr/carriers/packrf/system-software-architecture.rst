.. _pzsdr carriers packrf system-software-architecture:

Portable Radio Software
=======================

The software for the ADRV-PACKRF is provided by Analog Devices as an open source
reference design that can be used in various applications. The system source
code consists of several components, which are used together to control onboard
devices and provide connectivity to external tools for development. The
following components are either used to build the ADRV-PACKRF firmware or can be
used remotely from a host PC through a network connection:

-  FPGA HDL Code :git-hdl:`Standard Reference Design <hdl_2023_r2:projects/adrv9361z7035/ccpackrf_lvds>`, :git-TransceiverToolbox:`Modem Enhancements <v21.1.1:CI/projects/adrv9361z7035/ccbox_lvds_modem>`)
-  Linux Kernel/Device Drivers (`Transceiver <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/ad9361>`_, :git-rfsom-box-gui:`Modem Controller <master:tun_tap>`)
-  `U-boot Bootloader <https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18841973/Build+U-Boot>`_
-  `Graphical User Interface (GUI) <https://github.com/analogdevicesinc/rfsom-box-gui>`_
-  `Modem Design Workflow and Generation <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem>`_
-  `IIO Oscilloscope <https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope>`_
-  `3rd Party Simulation and Development Tools <https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/simrf>`_
-  `MATLAB/Simulink <https://wiki.analog.com/resources/eval/user-guides/matlab_bsp>`_, `GNU Radio <https://wiki.analog.com/resources/tools-software/linux-software/gnuradio>`_

The default design used for FPGAs in the PackRF kit contains the standard reference design built from the `ADI HDL repository <https://github.com/analogdevicesinc/hdl>`_. This design is provided by default since it allows a more general interaction with the transceiver, allowing an end-user to move data through the transceiver in a traditional way with standard tools. The modem design, which can be built from the `Transceiver Toolbox <https://github.com/analogdevicesinc/TransceiverToolbox>`_, modifies the data pipelines which can be unintuitive for those starting out with the kit. The streaming interfaces in the modem design, which represent the transmit and receive chains in software still exist or will appear in development tools, but the data provided by them and their control mechanisms are different.

Getting Started
---------------

For those starting out with the PackRF kit, using the standard `ADRV9361 user-guide <https://wiki.analog.com/resources/eval/user-guides/adrv9361-z7035>`_ is the best place to begin to understand how to use the device. As well as getting started with the basic ADI tools and 3rd party software support.

If you need to create an SD card for the radios or update an existing card, follow `this guide <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`_ selecting **zynq-adrv9361-z7035-box** boot files.
