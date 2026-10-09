.. _fmcomms8 user-guide:

User Guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD-FMCOMMS8-EBZ` contains two :adi:`ADRV9009` wideband
transceivers providing quad transmit, quad receive, and quad observation
receiver channels. The board connects to a compatible FPGA development board via
the FMC HPC connector and uses the JESD204B bus interface for high-speed data
transfer.

System frequency and phase synchronization across all channels is
maintained using an :adi:`HMC7044` clock jitter attenuator with
JESD204B, which distributes clocks and SYSREF signals to both
ADRV9009 devices.

The board complies with VITA 57.1 mechanical dimensions (84 mm x
69 mm) and is powered through the FMC connector from the carrier
board.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   :adi:`AD-FMCOMMS8-EBZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/ad-fmcomms8-ebz-designsupport.zip>`

   - Schematic
   - PCB Layout
   - Bill of Materials
   - Allegro Project

Software guide
-------------------------------------------------------------------------------

The :adi:`EVAL-AD-FMCOMMS8-EBZ` platform development environment supports Linux
Industrial I/O (IIO) applications, MATLAB, Simulink, GNU Radio, and streaming
interfaces for custom C, C++, Python, and C# applications.

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: true
   has_local_connection: true
   show_linux_connection_image: true
   linux_connection_image: images/fmcomms8_zcu102_iio_connect.png
   show_no_os_connection_image: true
   no_os_connection_image: images/fmcomms8_zcu102_iio_connect_no_os.png
   iio_has_plugin: true
   iio_plugin_ref: iio-oscilloscope adrv9009
   iio_show_data_capture: true
   iio_data_captures:
     - title: Linux
       time_domain_image: images/fmcomms8_zcu102_iio_osc.png
     - time_domain_image: images/fmcomms8_zcu102_iio_osc2.png
     - title: no-OS
       time_domain_image: images/fmcomms8_zcu102_no_os_time.png

IIO Oscilloscope plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`ADRV9009 IIO Scope View <iio-oscilloscope adrv9009>`
- :ref:`ADRV9009 Control IIO Scope Plugin <iio-oscilloscope adrv9009 plugin>`
- :ref:`Advanced ADRV9009 Control IIO Scope Plugin <iio-oscilloscope adrv9009 advanced-plugin>`

Data streaming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`Basic IQ Datafiles <adrv9009 basic-iq-datafiles>`
- :dokuwiki:`Stream data into/out of MATLAB <resources/tools-software/linux-software/libiio/clients/matlab_simulink>`
- :ref:`GNU Radio <software gnuradio>`
- :ref:`Transceiver Toolbox <matlab transceiver-toolbox>`

Other tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :doc:`FRU EEPROM Utility </software/fru_dump>`
- :ref:`JESD204B Status Utility <software jesd-status>`
- :ref:`JESD204 Eye Scan <software jesd-eye-scan>`
- :adi:`MATLAB Filter Wizard / Profile Generator for ADRV9009 <media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`
