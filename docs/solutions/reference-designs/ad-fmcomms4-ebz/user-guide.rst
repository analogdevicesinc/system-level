.. _fmcomms4 user-guide:

User guide
===============================================================================

Hardware
-------------------------------------------------------------------------------

For hardware details including schematic, PCB layout, bill of materials, I/O
voltage levels, and board layers, see the :ref:`Hardware <fmcomms4 hardware>`
page.

For hardware configuration options (baluns, RF paths), see
:ref:`fmcomms2 hardware configuration-options`.

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported through the Linux IIO framework and is
compatible with the following software tools:

- :ref:`IIO Oscilloscope <fmcomms2 software using-iio-osc>` -- real-time data
  visualization and device control
- :external+pyadi-iio:doc:`pyadi-iio <index>` -- Python interfaces for data
  acquisition
- :ref:`Analog Devices Transceiver Toolbox for MATLAB <matlab transceiver-toolbox>`
- :external+no-OS:doc:`No-OS AD9361 project <projects/rf-transceiver/ad9361>`
  -- bare-metal driver

For quick start instructions, see the
:ref:`Quick Start Guides <fmcomms4 quickstart>`.

For more details on the AD9364/AD9361, see
:ref:`Understanding the AD9361 <fmcomms2 common ad9361>`.

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: true
   has_local_connection: true
   show_linux_connection_image: true
   linux_connection_image: images/fmcomms4_linux_connect.png
   show_no_os_connection_image: true
   no_os_connection_image: images/fmcomms4_no_os_connect.png
   iio_has_plugin: true
   iio_plugin_ref: fmcomms2 software ad9361-plugin
   iio_show_data_capture: true
   iio_show_time_domain: true
   iio_time_domain_image: images/fmcomms4_linux_time_domain.png
