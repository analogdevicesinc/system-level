.. _ad-acevsecrdset-sl production_testing:

Production Testing
==================

Overview
--------

The purpose of this test procedure is to identify connectivity issues, poor
soldering, and potential manufacturing defects in the :adi:`AD-ACEVSECRDSET-SL <ad-bct2ade9113-sl>`
board. Some issues are directly identified by explicit part-targeted tests,
while others are detected implicitly by running adjacent tests.

Test Duration
-------------

.. list-table::
   :header-rows: 1
   :widths: 70 30

   * - Step Description
     - Estimated Time (minutes)
   * - Test bench setup
     - 5 min
   * - Software test
     - 5 min
   * - **Total time**
     - **10 min**

Test Requirements
-----------------

Required Hardware
~~~~~~~~~~~~~~~~~

* :adi:`MAX32625PICO` (Daplink programmer)
* :adi:`AD-ACEVSECRDSET-SL <ad-bct2ade9113-sl>` board
* Raspberry Pi 4, power cable, HDMI cable
* Mouse and keyboard
* Power cable for AD-ACEVSECRDSET-SL board

Required Software
~~~~~~~~~~~~~~~~~

* SD card with the test image

Required Setup
~~~~~~~~~~~~~~

* Insert the SD card into the Raspberry Pi.

* Connect the Raspberry Pi to a monitor and power it.

  .. figure:: images/rpi_setup.png
     :width: 45em

     Raspberry Pi Setup

* Connect the :adi:`MAX32625PICO` (Daplink programmer) to the Raspberry Pi
  and the DUT.

* Power the DUT.

* Connect the mouse and keyboard to the Raspberry Pi.

  .. figure:: images/dut_setup.png
     :width: 45em

     DUT Setup

Test Process
------------

Wi-Fi Setup
~~~~~~~~~~~

Ensure the Raspberry Pi is connected to Wi-Fi before starting the tests. If
the test screen is already running, you will need to exit it first to configure
the network connection.

* After the Raspberry Pi boots, press **Ctrl+C** to exit the test screen.

* Click on the Wi-Fi icon in the system tray and select the network you want
  to connect to.

  .. figure:: images/wifi_connection.png
     :width: 45em

     Wi-Fi Network Selection

* Type in the password and connect to the network.

* After connecting successfully, reboot the Raspberry Pi by navigating to the
  application menu, selecting **Logout**, then choosing **Reboot** from the
  shutdown options.

  .. figure:: images/reboot1.png
     :width: 45em

     Reboot Options

Running the Tests
~~~~~~~~~~~~~~~~~

* After the Raspberry Pi reboots, the test screen will appear on the monitor.

  .. figure:: images/test_monitor.png
     :width: 45em

     Test Screen

* Type **1** and press **ENTER** to start the **System Test**.

  .. figure:: images/test_command_1_run.png
     :width: 45em

     Starting System Test

* Press the reset button on the board and press **ENTER**.

  .. figure:: images/dut_reset.png
     :width: 45em

     Press Reset Button on DUT

* Visually check if **LED STATUS 1** is on. If all tests pass, you will see
  a confirmation message.

  .. figure:: images/test_command_1_led_check_passed.png
     :width: 45em

     LED Check Passed

* If all tests pass, you can move onto the next D.U.T.

* When you are done testing, press **2** and hit **ENTER** to power off the
  Raspberry Pi.

  .. figure:: images/test_command_2_poweroff.png
     :width: 45em

     Power Off Raspberry Pi
