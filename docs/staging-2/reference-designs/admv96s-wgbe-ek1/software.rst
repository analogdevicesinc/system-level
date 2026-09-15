.. imported from: https://wiki.analog.com/resources/eval/user-guides/admv96s-wgbe-ek1/software

.. _admv96s-wgbe-ek1 software:

ADMV96S-WGBE-EK1 Software User Guide
====================================

``Wethlink`` GUI is an optional software that can be used to configure the
firmware operation from a PC. The firmware establishes a wireless link
automatically without any input from the Wethlink GUI. For a quick evaluation of
the ADMV96S-WGBE-EK1 you need not use the software at all. But if you want to
better observe or change the behavior of the firmware or want access to the raw
registers of the devices, you may use the software to achieve that, and this
page walks you through the installation process..

Requirements
------------

Windows
~~~~~~~

- `wethlink_installer.exe <https://swdownloads.analog.com/update/wethlink/latest/wethlink_installer.exe>`__

Linux
~~~~~

- git
- libiio
- python3
- pip

--------------

Software Setup
--------------

Installing the Wethlink GUI on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- To install the GUI double click the ``wethlink_installer.exe`` file. When
  prompted press ``Install`` and after the setup is completed press ``Close``.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/admv96s-wgbe-ek1/gui_installation.png
   :width: 400px

- After installation the app is found at the path of the Destination Folder in
  the previous step.
- You can start the app by double clicking the ``wethlink.exe`` file in the
  destination folder or by launching it from the Windows start menu.

Running the Wethlink GUI on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is no installer provided on Linux, you have to clone the repo, install the
dependencies and run the app in python.

::

   $ git clone :git-wethlink.git # TODO: does not exist yet
   $ cd wethlink
   $ pip install PyQt6 pyserial pylibiio
   $ python wethlink.py

--------------

Resources
---------

.. tip::

   -
     :dokuwiki:`ADMV96S-WGBE-EK1 Hardware User Guide <:`resources/eval/user-guides/admv96s-wgbe-ek1/hardware>`+`
   - :dokuwiki:`ADMV96S-WGBE-EK1 Firmware User Guide </resources/eval/user-guides/admv96s-wgbe-ek1/firmware/setup>`
   - :dokuwiki:`ADMV96S-WGBE-EK1 Software User Guide </resources/eval/user-guides/admv96s-wgbe-ek1/software>`
   - :git-no-OS:`ADMV96S-WGBE-EK1 Firmware Project <tree/main/projects/wethlink+>`
   - `Wethlink Installer <https://swdownloads.analog.com/update/wethlink/latest/wethlink_installer.exe>`__
