CrossCore Embedded Studio Quickstart User Guide
===============================================

This page describes how to use the ADuCM36x Device Family Pack (DFP) with
CrossCore Embedded Studio (CCES) to create, import, build and debug applications
for the ADuCM360 processor. The ADuCM360 processor integrates an ARM Cortex-M3
microcontroller with dual 24-bit sigma delta analog to digital converters along
with various other on-chip analog and digital blocks within a single package.

This page describes how to install and work with the Analog Devices ADuCM36x DFP
to start developing applications for the EVAL-ADICUP360. This page also
highlights common problems and how to avoid them.

Additional help documentation can be found by opening CCES and selecting "Help
Contents" from the CCES Help menu.

This page covers:

-  How to install or upgrade the ADuCM36x Device Family Pack (DFP) an ARM CMSIS Pack for CCES
-  How to create a new project for the ADuCM360
-  How to add startup code and core components to a new project for the ADuCM360
-  How to import existing projects into your workspace
-  How to build projects for programming the ADuCM360
-  How to configure the Tools Settings used by an ADuCM360 project
-  How to configure the debug session for an ADuCM360 application
-  How to start and stop debugging an ADuCM360 application
-  How to create a Binary (.bin) or Intel Hex (.hex) file from an ADuCM360 application
-  How to debug an programs using an ADuCM362 and ADuCM363 Evaluation Board

.. note::

   We have a playlist of YOU TUBE VIDEOS that can help you understand different aspects of CrossCore Embedded Studio. The videos talk about the ADICUP360, but the tools information is relevant for the ADICUP360 as well. `CrossCore Embedded Studio Videos <https://www.youtube.com/playlist?list=PLiwaj4qabLWycR06TNf8eqSwX7qkDbSu_>`_

Workspace and Projects
----------------------

A CCES workspace is a folder (e.g. c:\\Users\\anon\\cces\\2.7.0) that contains
project resources and metadata. When projects are created or imported, details
about that project are stored in the workspace. The workspace metadata also
includes preferences set through the CCES Preferences dialog box and IDE window
layouts. By default, CCES creates new projects within your workspace folder.

Each time you start CCES, you will be prompted for a workspace location. You can
opt to default to a workspace directory by choosing to use a workspace directory
as your default. You will not be prompted the next time you open CCES.

.. image:: ../images/360_workspace.jpg
   :align: center
   :width: 600

How to install or upgrade the ADuCM36x Device Family Pack (DFP) or ARM CMSIS Pack for CCES
------------------------------------------------------------------------------------------

CCES 2.7.0 does not comes with the ADuCM36x Device Family Pack (DFP) or the ARM
CMSIS Pack file pre-installed.

Installing the ADuCM36x DFP
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Switch to the CMSIS Pack Manager perspective by selecting *Window \| Perspective \| Open Perspective \| Other... \| CMSIS Pack Manager*.
-  Once opened, select *Check for Updates on Web ( blue arrows on the toolbar )*. This may take a minute or two.
-  Choose *Analog Devices* and *ADuCM360 Series* in the Devices View.
-  Select the *ADuCM36x CMSIS Pack* version (choose version 1.0.2 or higher) from the Packs View.
-  Click the *Install* Action.

.. important::

   The "Check for Updates on Web" option does not work to obtain the ADICUP360 / ADuCM36X pack. Instead, refer to the "Installing Locally Saved ADuCM36x Pack" section (below) after `downloading the ADuCM36x DFP <https://www.keil.arm.com/packs/aducm36x_dfp-analogdevices/boards/>`_.

Installing the ARM CMSIS Pack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Switch to the CMSIS Pack Manager perspective by selecting *Window \| Perspective \| Open Perspective \| Other... \| CMSIS Pack Manager*.
-  Once opened, select *Check for Updates on Web ( blue arrows on the toolbar )*, if you have not already done so.
-  Choose *ARM* in the Devices View.
-  Select the *Generic* and *ARM.CMSIS* from the Packs View, and select the current version (e.g. 5.1.0)
-  Click the *Install* Action.

.. image:: ../images/360_arm_cmsis.gif
   :align: center

Installing Locally Saved ADuCM36x Pack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, the ADuCM36x Device Family Pack (DFP) files can be installed
using a local downloaded copy.

After downloading the .pack files from the Keil website (https://www.keil.com/dd2/pack/), select the Import Packs button in the CMSIS Pack Manager's Packs View, choose the .pack file as shown in the screenshot below, and click Open.

You will be prompted to accept a license agreement and, after agreeing to it,
the CMSIS-Pack file will be installed into CrossCore Embedded Studio's
CMSIS-Pack installation directory (e.g. C:\\Analog Devices\\CrossCore Embedded
Studio 2.7.0\\ARM\\packs\\AnalogDevices).

.. image:: ../images/360_import_pack.gif
   :align: right

How to create a new project for the ADuCM360
--------------------------------------------

A project for ADuCM360 can be created using the New CrossCore Project Wizard.
This wizard will guide you through the steps to create a new project.

-  To create a new project, go to the menu bar and find *File -> New -> CrossCore Project*.
-  Name the project, and then hit the Next button.
-  Choose Processor family **ARM** and select Processor type **ADuCM360**.

   -  There is no Silicon Revision Option for the ADuCM360, so it defaults to
      "none"

-  Project configuration allows you to add additional Add-ins to your project, such as Pin Multiplexing and changing the template language for a generated main function etc. Typically no configuration or add-ons are necessary.
-  Finally, press *Finish* and the project will be created and you can begin writing your program.

.. image:: ../images/360_new_project.gif
   :align: center

How to add startup code and core components to a new project for the ADuCM360
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A new or empty ADuCM360 project does not have startup code or a linker description file that maps code and data. It is necessary to add these components using the **Run-time Environment (RTE) Configuration Editor**.

CrossCore Projects created for Analog Devices' Cortex-M based processors, such
as ADuCM360 include a system.rteconfig file. Opening this file within the IDE
will open the RTE Configuration Editor. Components from the CMSIS-Pack, such as
drivers and services, can be added to a project by selecting them in the editor
and clicking Save.

At minimum, a new ADuCM360 project **requires** the *Device::Startup*, *CMSIS::Core* and *Device::Global* Configuration components to be added to the project.

-  Double-click on the system.rteconfig to open the RTE Configuration Editor.
-  Select Device::Startup, CMSIS::Core and Device::Global Configuration.
-  Click Save (Ctrl+S)
-  *You can also choose Device::Startup and click the Resolve button to add dependant components*

.. image:: ../images/360_project_structure.gif
   :align: right

How to import existing projects into your workspace
---------------------------------------------------

There are three(3) methods for importing existing projects:

-  Examples that you have saved to a local drive on your PC.
-  Examples that come with the ADuCM36x Device Family Pack (DFP).
-  Examples which are in the ADICUP360 GIT repository (most up to date content).

How to Import Existing Projects Saved to a Local Drive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Select *File \| Import...* from the CCES menu.
-  A dialog will pop-up with several importing options, choose the *General \| Existing Projects into Workspace* option, and click Next
-  Select *Browse* in the dialog window and search for the saved project which is on your local drive.
-  (Optional) If the *Copy projects into workspace* option is checked, the project will be copied to your workspace folder and the newly copied project will be opened and used. This preserves the original version of the project.
-  Click *Finish*

.. image:: ../images/360_import_project.gif
   :align: right

How to Import Examples that come with the ADuCM36x Device Family Pack (DFP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Opening CCES Examples using the CMSIS Pack Manager Perspective
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Open CMSIS Pack Manager perspective by clicking "Open Perspective" icon on tool bar and selecting "CMSIS Pack Manager" in the Open Perspective window (or choose CMSIS Pack Manager perspective if already open).
-  From the Examples View, select the example that you would like to open.
-  Click the *Copy* Action button.
-  A dialog will pop-up showing the location where the example will be copied to. Click *Copy* to copy and open the example project.

.. image:: ../images/360_open_example.gif
   :align: right

Opening Examples using the CCES Example Browser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Launch the CCES Example Broswer by clicking on *Help --> Browse Examples*.
-  Select ADuCM36x_DFP[x.y.z] in Product drop-down list, select the example and
   click Open example. Then the example will be copied to your workspace.

.. image:: ../images/360_example_browser.gif
   :align: right

How to Import Existing Projects from the GIT Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open the GIT perspective by clicking "Open Perspective" icon on tool bar and selecting "Git" in the Open Perspective window (or choose the GIT perspective if already open).
-  Clone the Git repository which contains all the latest code and projects
   associated with the ADuCM360. Populate the URI field with the following
   address.

   -   **URI:** - `EVAL-ADICUP360 <https://github.com/analogdevicesinc/EVAL-ADICUP360>`_
   -  Click *Next*, *Next* and then *Finish*. There may be a pause while the branches are fetched.

-  In the Git Repositories window, *Right Click* on the *Projects* folder and select *Import Projects...*
-  Select *Import existing Eclipse projects*
-  Click *Next* and then *Finish*

.. image:: ../images/360_git.gif
   :align: right

How to configure the Tools Settings used by an ADuCM360 project
---------------------------------------------------------------

-  Select the project in the Project Explorer View.
-  Select the *Cog* icon from the View's toolbar.

   -  Or right-click on the project, select *Properties* and choose *C/C++ Build \| Settings*.

-  After configuring your project, click Apply and/or OK.

.. image:: ../images/360_tool_settings.gif
   :align: right

Disabling/Enabling Semihosting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  To enable/disable semi-hosting in your program, visit your project *Tools Settings*.
-  Change the *semi-hosting support* option under *Linker \| Libraries*:

   -  Enable semi-hosting by selecting the **rdimon.specs** option.

      -  Use this option if using the debugger for things like printf() or other
         similar tools.

   -  Disable semi-hosting by selecting the **nosys.specs** or **None** options.

      -  Use this option for standalone embedded operation.

-  After configuring your project, click Apply and/or OK.
-  Right click on the project and select the *Build Project*.

   -  Or click the *Hammer* icon from the toolbar.

.. image:: ../images/360_no_sys.gif
   :align: right

How to build projects for programming the ADuCM360
--------------------------------------------------

-  Open the C perspective by clicking "Open Perspective" icon on tool bar and selecting C in the Open Perspective window (or choose the C perspective if already open).
-  Right click on the project and select the *Build Project*.

   -  Or click the *Hammer* icon from the toolbar.

.. image:: ../images/360_build_project.gif
   :align: right

How to configure the debug session for an ADuCM360 application
--------------------------------------------------------------

You will need to create a launch configuration to debug your ADuCM360 program.

-  If you have already built a project, select that project in the Project Explorer View.
-  Right-click on the project and choose *Debug As* and *Application with GDB and OpenOCD (Emulator)*
-  In the *Target* tab, choose *Target (processor)* and in the drop-down select **Analog Devices ADuCM360**
-  In the *Target* tab, choose *Interface* and in the drop-down select **ARM CMSIS-DAP compliant adapter**
-  In the *Main* tab, ensure that your project is selected in the *Project* entry box.

   -  If the correct project is not populated, click the *Browse...* button and choose the project. Note that this is optional and you only need to choose a project if you want the IDE to search a project for the built binaries (programs), otherwise you can leave this entry blank.

-  In the *Main* tab, ensure your binary (program) is selected in the *Application* entry box.

   -  If the correct binary (program) is not populated, click on *Search Project...* and choose the binary (program) from those available in the chosen project.
   -  If your binary (program) is not populated and it was not built from a project in your workspace (i.e. you have a pre-built binary), then click the *Browse...* button and search for your pre-built binary (program). Click *Open* when you have found and selected the pre-built binary (program).

-  In the *Common* tab, you can add the debug configuration to your menu bar shortcuts, for both *Debug mode* or // Run mode// by simply ticking the checkboxes.

.. image:: ../images/360_debug_launch.gif
   :align: right

How to start and stop debugging an ADuCM360 application
-------------------------------------------------------

-  Ensure that you have connected your EVAL-ADICUP360 board to your computer via the **DEBUG** USB port (**P14** - the micro USB connected closest to the DC barrel jack).
-  If you are already in the Debug Configurations dialog, then click *Debug*.
-  If you are in the C Perspective, then you can launch the last Debug session by clicking the *Beetle* Debug button on the toolbar.
-  You will be prompted to switch perspective to the Debug perspective. Click *Yes*. You can opt to not show this dialog again.
-  If your binary (program) was built with semi-hosting enabled, then CCES will
   warn you that you need to re-build the program when you want to run the
   program without a debugger attached.

.. image:: ../images/eval-aducm3029-debug-semi-hosting.png
   :align: center

-  If everything goes fine, in the Console window, you will see a report without
   errors.

   -  As a reference, the full text should be similar to:``Open On-Chip Debugger (OpenOCD) 0.9.0
      Licensed under GNU GPL v2
      Report bugs to <openocd-devel@lists.sourceforge.net>
      0
      Info : select transport "swd"
      adapter speed: 1000 kHz
      cortex_m reset_config sysresetreq
      Info : CMSIS-DAP: SWD  Supported
      Info : CMSIS-DAP: Interface Initialised (SWD)
      Info : CMSIS-DAP: FW Version = 1.0
      Info : SWCLK/TCK = 0 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1
      Info : CMSIS-DAP: Interface ready
      Info : clock speed 1000 kHz
      Info : SWD IDCODE 0x2ba01477
      Info : aducm360.cpu: hardware has 2 breakpoints, 1 watchpoints
      Info : CHIPID 0x0284
      memory bus access delay set to 6 tck
      adapter speed: 1000 kHz
      Info : accepting 'gdb' connection on tcp/3333``

-  Your program's execution is stopped automatically at the first breakpoint which is at the beginning of main() loop. You can use the debug functions and features of the CCES environment. (Such as stepping through, breakpoints, register reads, variable values, etc.)
-  To terminate a debug session, click on the red *Stop* button on the toolbar.

.. image:: ../images/360_debug.gif
   :align: center

Windows Firewall Access
~~~~~~~~~~~~~~~~~~~~~~~

-  If this is the first time you have launched OpenOCD, the Windows Firewall may pop-up a window asking for access. Click on "*Allow Access*".

.. image:: ../images/eval-aducm3029-openocd-firewall.png
   :align: center

Linux USB Access
~~~~~~~~~~~~~~~~

-  When installing CCES for the first time, you'll be prompted to set up you system, so that you can access USB without root access. If you need to set up access to your USB after installation, perhaps because you answered no during the installation, then you can run the script in *opt/analog/cces/2.7.0/Setup/setup_openocd_permissions.sh* with sudo access.

How to create a Binary (.bin) or Intel Hex (.hex) file for an ADuCM360 application
----------------------------------------------------------------------------------

Starting with CrossCore Embedded Studio (CCES) 2.8.0, the Artifact of your
project build can now be a Binary or Intel Hex file.

-  Ensure that your program is built with semi-hosting disabled by visiting *Tools Settings \| Linker \| Libraries* and change *Semihosting support* to *nosys.specs* or *None*, depending on your application set-up.
-  Rebuild your application.

.. image:: ../images/360_no_sys.gif

-  Convert your application into Binary (.bin) or Intel Hex (.hex) format by visiting Tools Settings once more.
-  Select the Build Artifact tab.
-  Select Binary (or Intel Hex) as the Artifact Type.
-  Apply and Close
-  Rebuild your application.

.. image:: ../images/360_bin.gif

How to debug programs using ADuCM362 and ADuCM363 Evaluation Boards
-------------------------------------------------------------------

The :adi:`ADuCM362/ADuCM363 evaluation board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-aducm362-aducm363.html>` comes with an Segger J-Link OB emulator which is not supported out of the box by CrossCore Embedded Studio (CCES). However, using Segger's JLinkGDBServer, we can still create and debug our ADuCM362/3 projects using CCES. The following are instructions on how to set up your Debug configuration.

-  Download and install `Segger J-Link Software and Documentation Pack <https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack>`_:

   -  Click for downloads and select the install for your platform.
   -  `Or click here to download the latest Windows version <https://www.segger.com/downloads/jlink/JLink_Windows.exe>`_

-  Run JLinkGDBServer:

   -  Open ``C:\Program Files (x86)\SEGGER\JLink_V512f\JLinkGDBServer.exe`` on Windows.
   -  Run ``LD_LIBRARY_PATH=/opt/SEGGER/JLink /opt/SEGGER/JLinkGDBServerExe`` on Linux.

-  In the JLinkGDBServer application, choose your Target device. For example, ``ADuCM362``.
-  Click OK to run the JLinkGDBServer.
-  Next create a CCES Debug configuration for your ADuCM362 project/program:
-  In the Target tab:

   -  Change the command from ``openocd`` to the path to PackChk (e.g. ``C:\analog\cces\2.8.1\ARM\packs\ARM\CMSIS\5.3.0\CMSIS\Utilities\Win32\PackChk.exe``) or another executable that will run.

      -  We specify a different executable because running OpenOCD will fail and it will cause the launch configuration to terminate.
      -  It is not necessary to set your target to be ``Analog Devices ADuCM36x`` or your interface to ``Segger J-Link`` but it may help you when identifying your Debug configuration later on.

-  In the Main tab:

   -  Ensure that your project and/or program has been added.

-   In the Debugger tab:

   -  Ensure that ``Use remote target`` is checked.
   -  And that your port number is set to ``2331``.

-  In the Startup tab:

   -  Add the following to Initialization commands:``monitor flash device = ADuCM362
      monitor flash download=1
      monitor flash breakpoints = 1
      monitor clrbp
      monitor endian little
      monitor reset
      monitor halt
      monitor sleep 10
      monitor speed auto``

-  Add the following to Run commands:``monitor reg r13 = (0x00000000)
   monitor reg pc = (0x00000004)
   break main
   continue``
-  Click Debug to start loading and running your program.

.. image:: ../images/362_eval.gif

