.. _ad-paarray3552r-sl software-guide:

Software User Guide
===================

Downloads
---------

The AD-PAARRAY3552R-SL Embedded and Application Software
files are available here:

.. admonition:: Download

   :dokuwiki:`AD-PAARRAY3552R-SL Software Files <_media/resources/eval/user-guides/ad-paarray3552r-sl/ad-paarray3552r-sl-rel1.0.1.exe.zip>`

   The installer contains the following:

     * Embedded Software: **AD-PARRAY3552R-SLv1.0.1.hex**
     * Application Software: PA Array Biasing Software v1.0.0.exe
     * Evaluation License Agreement (ELA) for both firmware and GUI.
     * Wiki User Guide Link

Embedded Software
-----------------

The :adi:`AD-PAARRAY3552R-SL` is accompanied by an open-source software stack
and associated collateral, enabling a complete experience from
evaluation and prototyping all the way to production firmware and applications
development.

The system‘s firmware is based on Analog Devices’ open-source
:git-no-OS:`ADI's no-OS framework </>`, which includes most of the tools required
for embedded code development and debugging as well as libraries enabling host-side
connectivity for system configuration and data transfer over UART.

Updating the Firmware
~~~~~~~~~~~~~~~~~~~~~~

The most common way of programming the system is by dragging and dropping
the provided .hex file to the DAPLINK drive. Using the drag-and-drop method,
the software is going to be a version that Analog Devices creates for
testing and evaluation purposes. This is the easiest way to get started
with the reference design.

Setting up the MAX32625PICO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To update the board’s firmware, a new bootloader has to be flashed
on the MAX32625PICO. Follow below procedure:

#. Download the firmware image:

   :dokuwiki:`MAX32625PICO Firmware <_media/resources/eval/user-guides/pa_array/max32625_max32666fthr_if_crc_swd_v1.0.5.bin.zip>`

#. Do not connect the MAX32625PICO from the PC and the AD-PAARRAY3552R-SL
   board.
#. Plug the micro-USB cable only in the MAX32625PICO.
#. Press the button on the MAX32625PICO and then plug the other end of the
   micro-USB cable into the PC. **(Do not release the button until the
   MAINTENANCE drive is mounted)**.

   .. figure:: max32625pico_maxdap.png
      :width: 200px

#. Release the button once the MAINTENANCE drive is mounted.
#. Drag and drop (to the MAINTENANCE drive) the firmware image.
#. After a few seconds, the MAINTENANCE drive will disappear and be replaced by
   a drive named DAPLINK. This indicates that the process is complete, and the
   MAX32625PICO can now be used to flash the firmware of the AD-PAARRAY3552R-SL
   board.

Programming the AD-PAARRAY3552R-SL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect the MAX32625PICO to the AD-PAARRAY3552R-SL board using the 10-pin
   ribbon cable.
#. Connect the 48 V power supply to the AD-PAARRAY3552R-SL. Make sure the board
   is powered up for the next steps.
#. A DAPLINK drive should appear as mounted on the PC.
#. Drag and drop the **AD-PAARRAY3552R-SLv1.0.0.hex** into the DAPLINK drive.
   After a few seconds, the drive will be remounted.
#. Check the DAPLINK directory and make sure there is no **FAIL.TXT** file. In
   case there is, repeat the drag and drop step. Otherwise, the MAX32625PICO can
   now be disconnected from the AD-PAARRAY3552R-SL, since the firmware update is
   complete.

Application Software
--------------------

The system also integrates a graphical user interface (GUI) that
continuously monitors crucial parameters. This interface facilitates complete
system control, enabling faster prototyping and development.

.. figure:: gui_dashboard.png

   Graphical User Interface (GUI)

The application software requires additional dependencies that need to be
installed on PC for the GUI to function properly. To acquire these
dependencies, click the link below.

.. admonition:: Download

   Visit this page to download the required dependencies:

   `.NET Framework 4.6.2 Runtime <https://dotnet.microsoft.com/en-us/download/dotnet-framework/thank-you/net462-web-installer>`__

System Requirements
~~~~~~~~~~~~~~~~~~~

- Windows 10 OS or later
- Microsoft .Net Framework 4.6.2
  `Download <https://dotnet.microsoft.com/en-us/download/dotnet-framework/thank-you/net462-web-installer>`__
- 1920 by 1080 or greater screen resolution, recommended
- Keyboard and mouse
- Optional internet connectivity to access online resources

Installation Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Extract the contents of the zip file.
#. Open the **AD-PAARRAY3552R-SL-Rel1.0.0** executable file.
#. Install the program to the computer.
#. Once the installation is complete, navigate to the default directory
   **(C:\\Analog Devices\\AD-PAARRAY3552R-SL-Rel1.0.0\\)**.

Graphical User Interface Walkthrough
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section provides a description and functionality details
of the PA Array GUI. Access the Windows application by opening the
**PA Array Biasing Software v1.0.0.exe** in the directory where the files
have been installed.

Home Page
^^^^^^^^^^

.. figure:: gui_home.png

   PA Array GUI Home Page

The **Home Page** provides an overview of the AD-PAARRAY3552R-SL, showcasing the
description of the actual hardware and relevant links to help users to get started.

Dashboard
~~~~~~~~~

.. figure:: gui_dashboard.png

   PA Array GUI Dashboard

The **Dashboard** is where the user interacts with the hardware.
It displays distinct groups with distinct functions.

Historical Graph
~~~~~~~~~~~~~~~~

.. figure:: gui_historical_graph.png

   PA Array GUI Historical Graph

The **Historical Graph** pane shows the real-time temperature monitoring.

Device Group
~~~~~~~~~~~~

.. figure:: gui_device_group.png

   PA Array GUI Device Group

The **Device Connection** displays a list of connected devices to
connect and configure.

Control Group
~~~~~~~~~~~~~

.. figure:: gui_control_group.png

   PA Array GUI Control Group

.. figure:: gui_control_group_main.png

   PA Array GUI Control Group Main Tab

The **Control Group** presents the control options and live values. This is
where users can configure and monitor board functions.

Logs Group
~~~~~~~~~~

.. figure:: gui_logs_groups.png

   PA Array GUI Logs Group

The **Logs** pane displays the run-time logs that occur during
board monitoring/configuration.

Further Help
------------

For questions and more information about this product, connect with us through
the :ez:`Analog Devices Engineer Zone<reference-designs>`.
