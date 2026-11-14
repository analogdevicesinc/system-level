.. _ad-apardspoe-sl production_testing:

Production Testing
==================

Overview
--------

The purpose of the test procedure is to identify connectivity issues, poor
soldering, and potential manufacturing defects. Some of the issues are directly
identified by explicit part-targeted tests, others are implicit, by running
adjacent tests.

Test Duration
-------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimate Time (minutes)
   * - Test bench setup
     - 3 min
   * - Software test
     - 5 min
   * - **Total time**
     - **8 min**

Test Requirements
-----------------

Required Hardware
~~~~~~~~~~~~~~~~~

* Raspberry Pi 4
* HDMI cable
* Mouse and keyboard
* 1 x :adi:`AD-RPI-T1LPSE-SL` board
* 1 x :adi:`AD-APARDSPOE-SL` (Device Under Test)
* 1 x :adi:`AD-APARD32690-SL` board
* 1 x T1L cable
* 12V power supply USB Type-C
* :adi:`MAX32625PICO` (DAPLink programmer)

Required Software
~~~~~~~~~~~~~~~~~

The test image is provided on a pre-configured SD card.

Required Setup
~~~~~~~~~~~~~~

#. Insert the SD card into the Raspberry Pi.

#. Connect the Raspberry Pi to a monitor, keyboard, and mouse.

#. Insert the AD-RPI-T1LPSE-SL on top of the Raspberry Pi.

#. Connect the AD-APARD32690-SPOE shield on top of the AD-APARD32690-SL board.

#. Connect the T1L cable to AD-RPI-T1LPSE-SL and the AD-APARD32690-SL board.

#. Connect the DAPLink cable to the AD-APARD32690-SL board and plug it into the
   Raspberry Pi.

#. Power the AD-RPI-T1LPSE-SL using a Type-C power supply (12V).

.. figure:: images/rpi_setup.png
   :width: 45em

   Raspberry Pi setup

.. figure:: images/system_setup.png
   :width: 45em

   Complete system setup

Test Process
------------

Wi-Fi Setup
~~~~~~~~~~~

Make sure the Raspberry Pi is connected to Wi-Fi before starting the tests.

#. Power the Raspberry Pi.

#. Press **CONTROL+C** to exit the test screen.

#. Click on the network and type in the password.

   .. figure:: images/test_process_1_wifi_connection.png
      :width: 45em

      Wi-Fi connection

#. After successfully connecting, reboot the Raspberry Pi by following the
   instructions below.

   .. list-table::
      :widths: 50 50
      :header-rows: 0

      * - .. figure:: images/test_process_2_reboot_conn.png

        - .. figure:: images/test_process_3_reboot_conn.png

Running the Tests
~~~~~~~~~~~~~~~~~

After the Raspberry Pi reboots, the test screen will appear on the monitor.

.. figure:: images/terminal_command_1.png
   :width: 45em

   Test menu

1) System Test
^^^^^^^^^^^^^^

Type **1** into the terminal then press **ENTER** to start "1) System Test".
Connect the T1L cable to port 1.

If the test is **PASSED**, the DUT is functional. Continue testing the other
boards.

.. figure:: images/terminal_command_1_passed.png
   :width: 45em

   System test passed
