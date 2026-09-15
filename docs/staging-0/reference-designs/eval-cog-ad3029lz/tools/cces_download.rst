.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-cog-ad3029lz/tools/cces_download

.. _eval-cog-ad3029lz tools cces_download:

CrossCore Embedded Studio Download & Install
============================================

This page provides all the necessary steps to get CrossCore Embedded Studio
(CCES) software environment up and running on Windows or Linux.

The CCES software development environment for EV-COG-AD3029LZ is based on open
source tools, and is maintained by Analog Devices. CCES includes support for DSP
(digital signal processing) and ARM Cortex M- and A- devices, and includes the
following features and many more:

- Eclipse based IDE
- GNU ARM Embedded Toolchain for Cortex-M core based parts (5-2016-q2-update
  release)
- OpenOCD with support for ADuCM302x and ADuCM4x50 microcontroller (open source
  SWD)
- CMSIS Pack files
- Mbed CMSIS-DAP
- J-Link Lite

.. important::

   **CrossCore Embedded Studio** is based on **Eclipse**, but because the MBED
   platform provides a CMSIS-DAP interface to connect to the board, the
   EV-COG-AD3029LZ can be used without problems with **IAR Embedded Workbench
   IDE** or **Keil µVision IDE** as well.

Pre-Requisites and Requirements List
------------------------------------

There are a few things that you will need for the tools and software to work
properly.

- PC or laptop computer
- EV-COG-AD3029LZ hardware
- Micro USB to USB cables

.. important::

   USB cable needs to have ALL data lines connected, can"t use a charging only
   micro USB cable.

- Terminal Program to interface your PC with the EV-COG-AD3029LZ
- `Putty <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`__
- `Tera Term <https://en.osdn.jp/projects/ttssh2/releases/>`__
- Or other favorite Terminal program

CrossCore Embedded Studio Download Packages
-------------------------------------------

.. admonition:: Download

   The EV-COG-AD3029LZ **requires** the use of Crosscore Embedded Studios
   version **2.6.0 or higher**. Do not attempt to use earlier versions of the
   CrossCore tools, due to compatibility issues that will **damage** the
   EV-COG-AD3029LZ.

   :download:`http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.6.0/ADI_CrossCoreEmbeddedStudio-Rel2.6.0.exe`

   :download:`http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.6.0/adi-CrossCoreEmbeddedStudio-linux-x86-2.6.0.deb`

The following features are available and supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Compilation using the GNU ARM Embedded toolchain for the ADuCM302x and
  ADuCM4x50 ARM Cortex-M cores.
- Debugging ADuCM302x and ADuCM4x50 via the IDE with GDB/OpenOCD.
- Development and debugging of bare-metal applications on the ADuCM302x and
  ADuCM4x50 ARM Cortex-M core.

The following features are only supported via the Windows version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Use of CrossCore Embedded Studio Add-Ins other than the Linux Add-In
- Debugging an Application using the CrossCore Debugger (TPSDK)

CrossCore Embedded Studio Installer Instructions
------------------------------------------------

It is best that you save all the files/folders to the default directories
recommended by the CrossCore Embedded Studios installer. This way all the
instructions and support provided will be easier.

Installing CrossCore Embedded Studio on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- To install CrossCore Embedded Studio, double-click
  ADI_CrossCoreEmbeddedStudio-Rel2.6.0.exe
- The CrossCore Embedded Studio installer will install the mBed windows serial
  driver.
- It is available separately, if required

  - https://developer.mbed.org/handbook/Windows-serial-configuration

The executable installs all necessary components to the Analog Devices local
directory structure which can be found below.

- CrossCore Embedded Studio installs to C:\\Analog Devices\\CrossCore Embedded
  Studio 2.6.0
- Eclipse IDE installs to C:\\Analog Devices\\CrossCore Embedded Studio
  2.6.0\\Eclipse
- GNU ARM Embedded Toolchain for Cortex-M installs to C:\\Analog
  Devices\\CrossCore Embedded Studio 2.6.0\\ARM\\gcc-arm-embedded
- OpenOCD installs to C:\\Analog Devices\\CrossCore Embedded Studio
  2.6.0\\ARM\\openocd\\bin
- CMSIS Pack files are installed to C:\\Analog Devices\\CrossCore Embedded
  Studio 2.5.1\\ARM\\packs

Installing CrossCore Embedded Studio on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- To install CrossCore Embedded Studio, run the command:
- sudo dpkg -i adi-CrossCoreEmbeddedStudio-linux-x86-2.6.0.deb

The Ubuntu Linux Installer(Debian) installs all necessary components to the
Analog Devices local directory structure which can be found below.

- CrossCore Embedded Studio installs to /opt/analog/cces/2.6.0
- Eclipse IDE installs to /opt/analog/cces/2.6.0/Eclipse
- GNU ARM Embedded Toolchain for Cortex-M installs to
  /opt/analog/cces/2.6.0/ARM/gcc-arm-embedded
- OpenOCD installs to /opt/analog/cces/2.6.0/ARM/openocd/bin
- CMSIS Pack files are installed to /opt/analog/cces/2.6.0/ARM/packs

Activating CrossCore Embedded Studio
------------------------------------

The first time you launch CrossCore Embedded Studio, you will be prompted to
input a serial number, name, and email address. The serial number for **ALL**
EV-COG-AD3029LZ boards is: EZK-CCES-6XMG-BRRR-7CUS-K3AA-J92U-XK4A-2A01

Once the serial number has been activated, the CrossCore development tools will
allow you full and unlimited access to all the features of the tool when using
the Analog Devices family of ARM Cortex Processor.

CrossCore Embedded Studio Support
---------------------------------

For more details on CrossCore Embedded Studio, updated versions of the tools,
release notes, tools documentation, or other support. Please visit the CrossCore
:adi:`webpage <cces>`, or email the CrossCore support team at
:dokuwiki:`processor.tools.support@analog.com </mailto/processor.tools.support@analog.com>`

*End of Document*

:dokuwiki:`Back </resources/eval/user-guides/ev-cog-ad3029lz>`
