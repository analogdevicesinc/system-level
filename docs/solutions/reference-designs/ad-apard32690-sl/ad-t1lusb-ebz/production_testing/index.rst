.. _ad-t1lusb-ebz production_testing:

Production Testing
==================

Overview
--------

The purpose of the test procedure is to identify connectivity issues, poor
soldering, and potential manufacturing defects.

Test Duration
-------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimate Time (minutes)
   * - Test bench setup
     - 5 min
   * - Software test
     - 1 min
   * - **Total time**
     - **6 min**

Test Requirements
-----------------

Required Hardware
~~~~~~~~~~~~~~~~~

* 1 x :adi:`AD-SWIOT1L-SL` board
* 24V power supply for the AD-SWIOT1L-SL board
* Raspberry Pi, power supply, Mini-HDMI cable
* Mouse and keyboard
* T1L-to-Usb cable and :adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>` (media converter) as Device
  Under Test (DUT)
* Usb-A to Type-C cable for the media converter

Required Software
~~~~~~~~~~~~~~~~~

The test image is provided on a pre-configured SD card.

Required Setup
~~~~~~~~~~~~~~

#. Insert the SD card into the Raspberry Pi and power it.

#. Connect the HDMI cable between Rpi and the monitor, insert mouse and
   keyboard dongle into the Rpi's Usb port.

   .. figure:: images/rpi_connections.png
      :width: 45em

      Raspberry Pi connections

#. Connect the T1L-TO-Usb cable into the AD-SWIOT1L-SL and into the
   AD-T1LUSB2.0-EBZ (media converter).

   .. figure:: images/system_connection.png
      :width: 45em

      System connection

#. Connect a Usb Type-C cable to the media converter and plug the other side
   into the Raspberry Pi.

   .. figure:: images/usb_c.png
      :width: 45em

      Usb-C connection

#. Power the AD-SWIOT1L-SL.

Test Process
------------

Wi-Fi Setup
~~~~~~~~~~~

Before starting the testing procedure, make sure the Raspberry Pi is connected
to Wi-Fi.

#. After the Rpi boots the OS, press **CONTROL+C** to exit the test screen.

#. Click on the Wi-Fi network you want to connect to.

   .. figure:: images/wifi_connection.png
      :width: 45em

      Wi-Fi connection

#. Type in the password.

#. After successfully connecting, reboot the Raspberry Pi by following the
   instructions below.

   .. figure:: images/reboot1.png
      :width: 45em

      Reboot instructions

Running the Tests
~~~~~~~~~~~~~~~~~

After the Raspberry Pi reboots, the test screen will appear on the monitor.

.. figure:: images/test_monitor.png
   :width: 45em

   Test menu

1) T1L TO Usb Test
^^^^^^^^^^^^^^^^^^

Type **1** into the terminal then press **ENTER** to start the
"1) T1L TO Usb TEST".

.. figure:: images/test_command_1.png
   :width: 45em

   T1L TO Usb test

In case a failure occurred, a **FAILED** message will be displayed.

After the **PASSED** message is displayed, disconnect the media converter and
T1L cable and test the next pair.

Once you are done testing, press **2** and **ENTER** to power off the
Raspberry Pi.
