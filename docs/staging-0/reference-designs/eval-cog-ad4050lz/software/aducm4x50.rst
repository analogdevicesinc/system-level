.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-cog-ad4050lz/software/aducm4x50

.. _eval-cog-ad4050lz software aducm4x50:

ADuCM4x50 On-Chip Peripherals Drivers & Software
================================================

General Description/Overview
----------------------------

The ADuCM4x50 Device Family Pack (DFP) provides access to all the necessary
on-chip peripheral drivers for :adi:`ADuCM4050` devices. This software layer is
the foundation layer needed when writing applications using this microprocessor
family. When combined with the **EV-COG-AD4050LZ** software pack as well as the
Sensors software pack, there are many great **Internet of Things(IoT)**
applications and demos that can be replicated using the **EV-COG-AD4050LZ**
development platform.

The following on-chip drivers are provided as part of the ADuCM4x50 Device
Family Pack:

- spi

 .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cog-ad4050lz/software/aducm4050-fbl.png
    :width: 600px

- i2c
- uart
- sport
- beep
- wdt
- gpio
- rtc
- dma
- crypto
- adc
- tmr

For detailed information regarding the ADuCM4x50 DFP, please see our complete ADuCM4x50 software user guide. .. note::

   `ADuCM4050 DFP 1.0.0 Release Notes <http://download.analog.com/tools/EZBoards/ADuCM4050/Releases/DeviceFamilyPack/Release_1.0.0/ADuCM4x50_DFP_1.0.0_Release_Notes.pdf>`__

.. important::

   You **MUST** have this software package installed on your laptop or PC in
   order to compile, debug, and run the applications for the **EV-COG-AD4050LZ**
   platform.

Downloading the ADuCM4x50 Software Pack
---------------------------------------

The software pack can be installed directly by the tool chain"s CMSIS pack
manager. Optionally, you may download and then use the CMSIS pack manager"s
manual installation to install the pack.

#. Downloaded via the tool chain"s CMSIS pack manager

- It is recommended to download the ADuCM4x50 software pack through from the
  tool chain"s CMSIS pack manager. That way, all the files, directories
  structure, and project structure for the various applications is properly
  saved and accessed. For a detailed description on how to download the
  ADuCM4x50 software pack through CrossCore Embedded Studio please see our
  :dokuwiki:`Cross Core Embedded Studio Quickstart User Guide </resources/eval/user-guides/eval-cog-ad4050lz/tools/cces_guide>`.

#. Downloaded to local directory

- However if you do decide to download the ADuCM4x50 software pack to your
  PC/laptop directly, please use the link below to download the pack file from
  Keil"s website. You will then need to ``import`` the pack file using your tool
  chain"s CMSIS pack manager"s import feature. Note that all software packs can
  be downloaded from Keil"s website.

.. admonition:: Download

   `ADuCM4050_DFP Pack 1.0.0 <http://download.analog.com/tools/EZBoards/ADuCM4050/Releases/DeviceFamilyPack/Release_1.0.0/ADuCM4x50_Device_Family_Pack-Rel1.0.0.zip>`__


