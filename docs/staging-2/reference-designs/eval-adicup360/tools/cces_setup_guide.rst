.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/tools/cces_setup_guide

.. _eval-adicup360 tools cces_setup_guide:

EVAL-ADICUP360 Tool Chain
=========================

This page provides all the necessary steps to get CrossCore Embedded Studio
(CCES)
:adi:`CrossCore Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>`
software environment up and running on Windows or Linux.

The CCES software development environment for EVAL-ADICUP360 is based on open
source tools, and is maintained by Analog Devices. CCES includes support for DSP
(digital signal processing) and ARM Cortex M- and A- devices, and includes the
following features and many more:

- Eclipse based IDE
- GNU ARM Embedded Toolchain for Cortex-M core based parts (6-2017-q2-update
  release)
- OpenOCD with support for Cortex-M microcontroller (open source SWD)
- CMSIS Pack files
- Mbed CMSIS-DAP
- J-Link Lite

.. important::

   **CrossCore Embedded Studio** is based on **Eclipse**, but because the MBED
   platform provides a CMSIS-DAP interface to connect to the board, the
   EVAL-ADICUP360 can be used without problems with **IAR Embedded Workbench
   IDE** or **Keil µVision IDE** as well.

Pre-Requisites and Requirements List
------------------------------------

There are a few things that you will need for the tools and software to work
properly.

- PC or laptop computer
- EVAL-ADICUP360 hardware
- Micro USB to USB cables

.. important::

   USB cable needs to have ALL data lines connected, can"t use a charging only
   micro USB cable.

- Terminal Program to interface your PC with the EVAL-ADICUP360
- `Putty <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`__
- `Tera Term <https://en.osdn.jp/projects/ttssh2/releases/>`__
- Or other favorite Terminal program

CrossCore Embedded Studio Download Packages
-------------------------------------------

.. admonition:: Download

   The EVAL-ADICUP360 **requires** the use of Crosscore Embedded Studios version
   **2.7.0 or higher**.

   :adi:`CrossCore Embedded Studio <en/design-center/evaluation-hardware-and-software/software/adswt-cces.html>`

The following features are available and supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Compilation using the GNU ARM Embedded toolchain for the ADuCM360 ARM
  Cortex-M3 core.
- Debugging ADuCM360 via the IDE with GDB/OpenOCD.
- Development and debugging of bare-metal applications on the ADuCM360 Cortex-M3
  core.

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
  ADI_CrossCoreEmbeddedStudio-Rel2.8.0.exe
- The CrossCore Embedded Studio installer will install the mBed windows serial
  driver.
- It is available separately, if required

  - https://developer.mbed.org/handbook/Windows-serial-configuration

The executable installs all necessary components to the Analog Devices local
directory structure which can be found below.

- CrossCore Embedded Studio installs to C:\\Analog Devices\\CrossCore Embedded
  Studio 2.8.0
- Eclipse IDE installs to C:\\Analog Devices\\CrossCore Embedded Studio
  2.8.0\\Eclipse
- GNU ARM Embedded Toolchain for Cortex-M installs to C:\\Analog
  Devices\\CrossCore Embedded Studio 2.8.0\\ARM\\gcc-arm-embedded
- OpenOCD installs to C:\\Analog Devices\\CrossCore Embedded Studio
  2.8.0\\ARM\\openocd\\bin
- CMSIS Pack files are installed to C:\\Analog Devices\\CrossCore Embedded
  Studio 2.8.0\\ARM\\packs

Installing CrossCore Embedded Studio on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CrossCore Embedded Studio can be installed and used on Ubuntu 14.04+ 32-bit and
64-bit.

- If you are installing on a 64-bit distribution, then you will also need to
  install 32-bit support and compatibility libraries:

  - sudo dpkg –add-architecture i386 && apt-get update
  - sudo apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386
    libgtk2.0-0:i386 libxtst6:i386 gtk2-engines-murrine:i386
    libcanberra-gtk-module:i386 gtk2-engines:i386 libpng-dev:i386
    libssl-dev:i386

- To install CrossCore Embedded Studio, run the command:

  - sudo dpkg -i adi-CrossCoreEmbeddedStudio-linux-x86-2.8.0.deb

The Ubuntu Linux Installer(Debian) installs all necessary components to the
Analog Devices local directory structure which can be found below.

- CrossCore Embedded Studio installs to /opt/analog/cces/2.8.0
- Eclipse IDE installs to /opt/analog/cces/2.8.0/Eclipse
- GNU ARM Embedded Toolchain for Cortex-M installs to
  /opt/analog/cces/2.8.0/ARM/gcc-arm-embedded
- OpenOCD installs to /opt/analog/cces/2.8.0/ARM/openocd/bin
- CMSIS Pack files are installed to /opt/analog/cces/2.8.0/ARM/packs

Activating CrossCore Embedded Studio
------------------------------------

The first time you launch CrossCore Embedded Studio, you will be prompted to
input a serial number, name, and email address. The serial number for **ALL**
EVAL-ADICUP360 boards is:

.. important::

   **EVAL-ADICUP360 CrossCore Serial Number**

   EZK-CCES-5JNP-FQH2-IAZZ-IJY4-E4HG-YIY6-JE01

The New License Wizard will guide you through the process.

- Select Yes to install a license at this time.
- Choose ``I have a serial number that I would like to activate`` and click
  Next.
- Enter the serial number above ( EZK-CCES-5JNP-FQH2-IAZZ-IJY4-E4HG-YIY6-JE01 )
  and click Next.
- Choose ``Install and activate a license on-line all in one step`` and click
  Next.
- Complete your name and address and click Finish.
- On success, you will be prompted with a dialog that tells you that ``Your
  license has been successfully activated``. Click OK.

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
