.. imported from: https://wiki.analog.com/resources/eval/user-guides/ev-cog-ad4050w/quickstart_guide/cces

.. _ev-cog-ad4050w quickstart_guide cces:

EV-COG-AD4050WZ with CrossCore Embedded Studio
==============================================

.. note::

   There are no seperate toolchain,On-Board Peripheral Drivers & Software for
   EV-COG-AD4050WZ, the toolchain,On-Board Peripheral Drivers & Software for
   EV-COG-AD4050LZ works with EV-COG-AD4050WZ.The user needs to change only the
   pin muxing based on the application.For help regarding pinmapping refer to
   the Hardware Details section.

IDE Setup
---------

#. Install Cross Core Embedded Studio

- `CrossCore Embedded Studio 2.7.0 for Windows <http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.7.0/ADI_CrossCoreEmbeddedStudio-Rel2.7.0.exe>`__
- `CrossCore Embedded Studio 2..0 for Ubuntu Linux 14.04 x86 <http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.7.0/adi-CrossCoreEmbeddedStudio-linux-x86-2.7.0.deb>`__

#. License Installation

   #. Start CCES and navigate to Help -> Manage Licenses.
   #. Click New and enter the license key provided with the EV-COG-AD4050LZ box.
   #. Follow the on-screen instructions to register and activate the license.

Software Packs and Driver Setup
-------------------------------

#. Download the following packs for EV-COG-AD4050LZ

- `ARM CMSIS Pack <https://keilpack.azureedge.net/pack/ARM.CMSIS.5.1.1.pack>`__
- `Analog Devices ADuCM4x50 Device Support 3.1.0 (Latest) <http://download.analog.com/tools/EZBoards/ADuCM4050/Releases/AnalogDevices.ADuCM4x50_DFP.3.1.0.pack>`__
- `Analog Devices EV-COG-AD4050 Off-Chip Drivers and Examples 3.1.0 (Latest) <http://download.analog.com/tools/EZBoards/COG_4050/Releases/AnalogDevices.EV-COG-AD4050LZ_BSP.3.1.0.pack>`__

#. Start CrossCore Embedded Studio.
#. Go to CMSIS Pack Manager by navigating to Windows ->Perspective ->Open
   Perspective ->Others -> CMSIS Pack Manager.
#. Click Import Existing Packs icon

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/import_existing_packs_icon.jpg

   :dokuwiki:`Refer for more details </resources/ev/user-guides/ev-cog-ad4050lz/tools/cces_guide?&#how_to_install_packs_for_cces>`.

#. Select all the packs and import. This will install the packs. Ignore the
   warnings seen on the console window. In order to remove these warnings,
   additional packs needs to be installed which are available in the last
   section of this page.
#. Please refer to this
   `link <https://os.mbed.com/handbook/Windows-serial-configuration>`__ to
   download and install mbed serial driver on PC.

Running an Example Project
--------------------------

#. Power the MCU Cog using a USB (micro-B) Cable. You should see a red LED and a
   yellow LED turn on by default.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/img_20171030_180904.jpg
      :width: 200px

#. In CCES IDE, click CMSIS Pack Manager icon

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/pack_manager.jpg

#. Select EV-COG-AD4050LZ from the Boards tab on the Left panel. (see below
   image)

#. Copy button_press example from the Examples tab on the Right panel.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/tools/cmsis_pack_manager.jpg

#. Click C/C++ perspective icon

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/c_persp.jpg

#. Under Project Explorer select button_press example, click build icon

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/build_icon.jpg

#. Click on Debug icon

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/debug_icon.jpg

      once build is complete. Below are the Debug Configuration settings.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/debug.jpg
      :width: 700px

#. Click ``ok`` on Perspective Switch and Semihosting Enabled window.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/semihosting.jpg
      :width: 500px

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad4050lz/perspective_switch.jpg
      :width: 500px

#. Click run

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/run_icon.jpg

      on the Debug perspective.

#. Now press BTN1 or BTN2 on EV-COG-AD4050LZ and inspect corresponding LED.

You are all set!

:dokuwiki:`Back </resources/eval/user-guides/ev-cog-ad4050w/quickstart>`

End Document
