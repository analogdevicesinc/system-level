CrossCore Embedded Studio Quickstart User Guide
===============================================

This page describes how to use the ADuCM302x Device Family Pack (DFP) with
CrossCore Embedded Studio (CCES) to create, import, build and debug applications
for the ADuCM302x processor. The ADuCM302x processor integrates an ARM Cortex-M3
microcontroller with various on-chip peripherals within a single package.

This page describes how to install and work with the Analog Devices ADuCM302x
DFP to start developing applications for the EVAL-ADICUP3029. This page also
highlights common problems and how to avoid them.

Additional help documentation can be found by opening CCES and selecting "Help
Contents" from the CCES Help menu.

This page covers:

-  How to install or upgrade the Analog Devices Packs for CCES

   -  ADuCM302x Device Family Pack (DFP)

-  How to create a new project for the ADuCM3029
-  How to add startup code and core components to a new project for the ADuCM3029
-  How to import existing projects into your workspace
-  How to build projects for programming the ADuCM3029
-  How to configure the Tools Settings used by an ADuCM3029 project
-  How to configure the debug session for an ADuCM3029 application
-  How to start and stop debugging an ADuCM3029 application
-  How to create an Intel Hex (.hex) file from an ADuCM3029 application

.. note::

   We have a playlist of YOUTUBE VIDEOS that can help you understand different functions and features of CrossCore Embedded Studio. `CrossCore Embedded Studio Videos <https://www.youtube.com/playlist?list=PLiwaj4qabLWycR06TNf8eqSwX7qkDbSu_>`_

Workspace and Projects
----------------------

A CCES workspace is a folder (e.g. c:\\Users\\anon\\cces\\2.6.0) that contains
project resources and metadata. When projects are created or imported, details
about that project are stored in the workspace. The workspace metadata also
includes preferences set through the CCES Preferences dialog box and IDE window
layouts. By default, CCES creates new projects within your workspace folder.

Each time you start CCES, you will be prompted for a workspace location. You can
opt to default to a workspace directory by choosing to use a workspace directory
as your default. You will not be prompted the next time you open CCES.

.. image:: ../images/eval-aducm3029-workspace.png
   :align: center
   :width: 500

How to install or upgrade Packs for CCES
----------------------------------------

CCES 2.6.0 does not comes with the Analog Device specific packs or the ARM CMSIS
Pack file pre-installed. The following Packs are required to use the
EVAL-ADICUP3029 along with the hardware examples and wireless connectivity

-  ADuCM302x Device Family Pack (DFP)
-  ARM CMSIS Pack

ADuCM302x Device Family Pack (DFP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  To install the ADuCM302x DFP:
-  Switch to the CMSIS Pack Manager perspective by selecting *Window \| Perspective \| Open Perspective \| Other... \| CMSIS Pack Manager*.
-  Once opened, select *Check for Updates on Web ( blue arrows on the toolbar )*. This may time a minute or two.
-  Choose *Analog Devices* and *ADuCM302x Series* in the Devices View.
-  Select the *ADuCM302x CMSIS Pack* version (choose version 2.0.0 or higher) from the Packs View.
-  Click the *Install* Action.

.. image:: ../images/eval-aducm3029-cmsis-pack-aducm302x-dfp-200.png
   :align: center

Alternatively, the ADuCM3029 Device Family Pack (DFP) files can be installed
using a local download.

After downloading the .pack files from the Keil website (https://www.keil.com/dd2/pack/), select the Import Packs button in the CMSIS Pack Manager's Packs View, choose the .pack file as shown in the screenshot below, and click Open.

You will be prompted to accept a license agreement and, after agreeing to it,
the CMSIS-Pack file will be installed into CrossCore Embedded Studio's
CMSIS-Pack installation directory (e.g. C:\\Analog Devices\\CrossCore Embedded
Studio 2.6.0\\ARM\\packs\\AnalogDevices).

.. image:: ../images/eval-aducm3029-cmsis-pack-import-200.png
   :align: center

ARM CMSIS Pack
~~~~~~~~~~~~~~

-  To install the ARM 4.5.0 CMSIS Pack(or greater):
-  Switch to the CMSIS Pack Manager perspective by selecting *Window \| Perspective \| Open Perspective \| Other... \| CMSIS Pack Manager*.
-  Once opened, select *Check for Updates on Web ( blue arrows on the toolbar )*, if you have not already done so.
-  Choose *ARM* in the Devices View.
-  Select the *Generic* and *ARM.CMSIS* from the Packs View, select version 4.5.0
-  Click the *Install* Action.

.. image:: ../images/eval-aducm3029-cmsis-pack-arm-cmsis-200.png
   :align: center

How to create a new project for the ADuCM3029
---------------------------------------------

A project for ADuCM3029 can be created using the New CrossCore Project Wizard.
This wizard will guide you through the steps to create a new project.

.. image:: ../images/eval-aducm3029-project-new.png
   :align: center

-  To create a new project, go to the menu bar and find *File -> New -> CrossCore Project*.
-  Choose Processor family ARM and select Processor type ADuCM3029.
-  Choose your Silicon revision (default is 1.0).

   -  A *SILICON_REVISION* macro will be set in your project's Tools Settings, allowing you to conditionally check the silicon revision in your source code.

-  Project configuration allows you to add additional Add-ins to your project, such as Pin Multiplexing and changing the template language for a generated main function etc.
-  Finally, press *Finish* and the project will be created and you can begin writing your program.

.. image:: ../images/eval-aducm3029-project-explorer.png
   :align: center

How to add startup code and core components to a new project for the ADuCM3029
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An out-of-the-box ADuCM3029 project does not have startup code or a linker
description file that maps code and data. It is necessary to add these
components using the Run-time Environment (RTE) Configuration Editor.

CrossCore Projects created for Analog Devices' Cortex-M based processors, such
as ADuCM3029 include a system.rteconfig file. Opening this file within the IDE
will open the RTE Configuration Editor. Components from the CMSIS-Pack, such as
drivers and services, can be added to a project by selecting them in the editor
and clicking Save.

At minimum, a new ADuCM3029 project will require the Device::Startup,
CMSIS::Core and Device::Global Configuration components to be added to the
project.

-  Double-click on the system.rteconfig to open the RTE Configuration Editor.
-  Select Device::Startup, CMSIS::Core and Device::Global Configuration.
-  Click Save (Ctrl+S)
-  *You can also choose Device::Startup and click the Resolve button to add dependant components*

.. image:: ../images/eval-aducm3029-project-configure.png
   :align: center

How to import existing projects into your workspace
---------------------------------------------------

There are three(3) methods for importing existing projects:

-  Examples that you have saved to a local drive on your PC.
-  Examples that come with the Analog Devices Pack.
-  Examples which are in the ADICUP3029 GIT repository (most up to date
   content).

How to Import Existing Projects Saved to a Local Drive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Select *File \| Import...* from the CCES menu.
-  A dialog will pop-up with several importing options, choose the *General \| Existing Projects into Workspace* option, and click Next
-  Select *Browse* in the dialog window and search for the saved project which is on your local drive.
-  (Optional) If the *Copy projects into workspace* option is checked, the project will be copied to your workspace folder and the newly copied project will be opened and used. This preserves the original version of the project.
-  Click *Finish*

.. image:: ../images/eval-aducm3029-file-import.png
   :align: center

How to Import Examples that come with the ADuCM3029 Device Family Pack (DFP) or Board Support Packs (BSP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Opening CCES Examples using the CMSIS Pack Manager Perspective
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Open CMSIS Pack Manager perspective by clicking "Open Perspective" icon on tool bar and selecting "CMSIS Pack Manager" in the Open Perspective window (or choose CMSIS Pack Manager perspective if already open).
-  From the Examples View, select the example that you would like to open.
-  Click the *Copy* Action button.
-  A dialog will pop-up showing the location where the example will be copied to. Click *Copy* to copy and open the example project.

.. image:: ../images/eval-aducm3029-cmsis-pack-example-200.png
   :align: center

Opening Examples using the CCES Example Browser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Launch the CCES Example Broswer by clicking on *Help --> Browse Examples*
-  Select ADuCM302x_DFP[x.y.z] in Product drop-down list, select the example and
   click Open example. Then the example will be copied to your workspace.

How to Import Existing Projects from the GIT Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

( Note that at the time of writing, the EVAL-ADICUP3029 GIT repo. is work In
Progress )

-  Open the GIT perspective by clicking "Open Perspective" icon on tool bar and selecting "Git" in the Open Perspective window (or choose the GIT perspective if already open).
-  Clone the Git repository which contains all the latest code and projects
   associated with the ADuCM360. Populate the URI field with the following
   address.

   -   **URI:** - `EVAL-ADICUP3029 <https://github.com/analogdevicesinc/EVAL-ADICUP3029>`_
   -  Click *Next*, *Next* and then *Finish*. There may be a pause while the branches are fetched.

-  In the Git Repositories window, *Right Click* on the *Projects* folder and select *Import Projects...*
-  Select *Import existing Eclipse projects*
-  Click *Next* and then *Finish*

How to configure the Tools Settings used by an ADuCM3029 project
----------------------------------------------------------------

-  Select the project in the Project Explorer View.
-  Select the *Cog* icon from the View's toolbar.

   -  Or right-click on the project, select *Properties* and choose *C/C++ Build \| Settings*.

-  After configuring your project, click Apply and/or OK.

.. image:: ../images/eval-aducm3029-project-tools-settings.png
   :align: center

Enabling/Disabling Semihosting
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

.. image:: ../images/eval-aducm3029-spec.png
   :align: right

How to build projects for programming the ADuCM3029
---------------------------------------------------

-  Open the C perspective by clicking "Open Perspective" icon on tool bar and selecting C in the Open Perspective window (or choose the C perspective if already open).
-  Right click on the project and select the *Build Project*.

   -  Or click the *Hammer* icon from the toolbar.

.. image:: ../images/eval-aducm3029-project-build.png
   :align: center

How to configure the debug session for an ADuCM3029 application
---------------------------------------------------------------

You will need to create a launch configuration to debug your ADuCM3029 program.

-  If you have already built a project, select that project in the Project Explorer View.
-  Right-click on the project and choose *Debug As* and *Application with GDB and OpenOCD (Emulator)*
-  In the *Target* tab, choose *Target (processor)* and in the drop-down select **Analog Devices ADuCM3029**
-  In the *Target* tab, choose *Interface* and in the drop-down select **ARM CMSIS-DAP compliant adapter**
-  In the *Main* tab, ensure that your project is selected in the *Project* entry box.

   -  If the correct project is not populated, click the *Browse...* button and choose the project. Note that this is optional and you only need to choose a project if you want the IDE to search a project for the built binaries (programs), otherwise you can leave this entry blank.

-  In the *Main* tab, ensure your binary (program) is selected in the *Application* entry box.

   -  If the correct binary (program) is not populated, click on *Search Project...* and choose the binary (program) from those available in the chosen project.
   -  If your binary (program) is not populated and it was not built from a project in your workspace (i.e. you have a pre-built binary), then click the *Browse...* button and search for your pre-built binary (program). Click *Open* when you have found and selected the pre-built binary (program).

.. image:: ../images/eval-aducm3029-debug-configuration.png
   :align: center

Hardware breakpoints are limited in your ADuCM3029 application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  When you click Debug or Apply, you will be prompted with a dialog informing your the Hardware Breakpoints are limited. Click *Yes*. You can opt to not show this dialog again.

.. image:: ../images/eval-aducm3029-debug-hw-limited.png
   :align: center

How to start and stop debugging an ADuCM3029 application
--------------------------------------------------------

-  Ensure that you have connected your EVAL-ADICUP3029 board to your computer via the **USB** port (the micro USB connected closest to the DC barrel jack).
-  If you are already in the Debug Configurations dialog, then click *Debug*.
-  If you are in the C Perspective, then you can launch the last Debug session by clicking the *Beetle* Debug button on the toolbar.

.. image:: ../images/eval-aducm3029-debug-toolbar.png
   :align: center

-  You will be prompted to switch perspective to the Debug perspective. Click *Yes*. You can opt to not show this dialog again.

.. image:: ../images/eval-aducm3029-debug-perspective.png
   :align: center

-  If your binary (program) was built with semi-hosting enabled, then CCES will
   warn you that you need to re-build the program when you want to run the
   program without a debugger attached.

.. image:: ../images/eval-aducm3029-debug-semi-hosting.png
   :align: center

-  To change the semihosting settings please see the section on "Enabling/Disabling Semihosting" above.
-  If this is the first time you have launched OpenOCD, the Windows Firewall may pop-up a window asking for access. Click on "*Allow Access*".

.. image:: ../images/eval-aducm3029-openocd-firewall.png
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
      Info : aducm3029.cpu: hardware has 2 breakpoints, 1 watchpoints
      Info : CHIPID 0x0284
      memory bus access delay set to 6 tck
      adapter speed: 1000 kHz
      Info : accepting 'gdb' connection on tcp/3333``

-  Your program's execution is stopped automatically at the first breakpoint
   which is at the beginning of main() loop. You can use the debug functions and
   features of the CCES environment. (Such as stepping through, breakpoints,
   register reads, variable values, etc.)

.. image:: ../images/eval-aducm3029-debugging.png
   :align: center

-  To terminate a debug session, click on the red *Stop* button on the toolbar.

.. image:: ../images/eval-aducm3029-debug-toolbar-stop.png
   :align: center

How to create an Intel Hex (.hex) file or Binary (.bin) file for an ADuCM3029 application
-----------------------------------------------------------------------------------------

-  Ensure that your program is built with semi-hosting disabled by visiting *Tools Settings \| Linker \| Libraries* and change *Semihosting support* to *nosys.specs* or *None*, depending on your application set-up.
-  Rebuild your application.

.. image:: ../images/360_no_sys.gif

-  Convert your application into Intel Hex (.hex) or Binary (.bin) format by visiting Tools Settings once more.
-  Select the Build Steps tab.
-  Add one of the following commands to the *Post-build steps \| Command* entry box, depending on which file type you want.

   -  Intel Hex (.hex) file command:``arm-none-eabi-objcopy -O ihex ${ProjName} ${ProjName}.hex``
   -  Binary (.bin) file command:``arm-none-eabi-objcopy -O binary ${ProjName} ${ProjName}.bin``

-  Rebuild your application.

.. image:: ../images/360_post_bin.gif

*End of Document*
