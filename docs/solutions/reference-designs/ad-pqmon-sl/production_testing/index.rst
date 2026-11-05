.. _ad-pqmon-sl production_testing:

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
     - 5 min
   * - Software test
     - 4 min
   * - **Total time**
     - **9 min**

Test Requirements
-----------------

Required Hardware
~~~~~~~~~~~~~~~~~

* Raspberry Pi 4 with power supply
* SD card
* Monitor
* Mini HDMI cable
* Usb keyboard
* DUT - PQM board assembly (main board + front panel)
* New empty SD card for SD test
* T1L cable, not crossed (see image below)
* T1L Usb adapter (:adi:`AD-T1LUSB2.0-EBZ <ad-t1lusb20-ebz>`)
* :adi:`MAX32625PICO` (Daplink programmer) with MAX32650 Daplink firmware
* :adi:`MAX32625PICO` ribbon cable
* 1 x Usb Type-A to Usb Type-C cable (for DUT power)
* 2 x Usb Type-A to Micro-Usb cable (for T1L Usb, Daplink)

.. figure:: images/uncrossed_t1l_spe_cable.png
   :width: 45em

   T1L SPE cable, not crossed

Required Software
~~~~~~~~~~~~~~~~~

The test image is provided on a pre-configured SD card.

Required Setup
~~~~~~~~~~~~~~

.. figure:: images/test_setup.png
   :width: 45em

   Test setup overview

#. Insert the SD card into the Raspberry Pi.

#. Connect the Raspberry Pi to the monitor using the Mini HDMI cable.

#. Connect the Usb keyboard to the Raspberry Pi.

#. Assemble the DUT by inserting plastic standoffs on the main board and
   connecting the front panel to the main board.

   .. figure:: images/required_fasteners.jpg
      :width: 45em

      Required fasteners for test

   .. figure:: images/main_board_fasteners_attached.jpg
      :width: 45em

      Main board with fasteners attached. Two plastic standoffs and hex nuts
      are attached to the shown mounting holes.

   .. figure:: images/complete_board_assembly.png
      :width: 45em

      Complete board assembly. The secondary board does not attach to the 2
      standoffs with screws, it just passively rests on them.

#. Connect Daplink to Raspberry Pi (via Micro-Usb cable) and DUT (via ribbon
   cable).

   .. figure:: images/daplink_connection.png
      :width: 45em

      Daplink connection

#. Connect T1L Usb to Raspberry Pi (via Micro-Usb cable) and DUT (via T1L
   cable).

   .. figure:: images/t1l_connection.png
      :width: 45em

      T1L connection

#. Insert the SD card into the SD slot of the Add-on board.

   .. figure:: images/sd_card_inserted.png
      :width: 45em

      Insert SD card

#. Connect the DUT to the Raspberry Pi (via Usb-C cable).

   .. figure:: images/dut_power_connection.png
      :width: 45em

      Connect DUT power

.. figure:: images/rpi_connections.png
   :width: 45em

   Raspberry Pi connections

Test Process
------------

Wi-Fi Setup
~~~~~~~~~~~

Before starting the testing procedure, make sure the Raspberry Pi is connected
to Wi-Fi.

#. After the Rpi boots, press **CONTROL+C** to exit the test screen.

#. Click on the Wi-Fi network you want to connect to.

   .. figure:: images/wifi_connection.png
      :width: 45em

      Wi-Fi connection

#. Type in the password.

#. After connecting successfully, reboot the Raspberry Pi by following the
   instructions below.

   .. grid::
      :widths: 50% 50%

      .. image:: images/reboot1.png

      .. image:: images/reboot2.png

Running the Test Software
~~~~~~~~~~~~~~~~~~~~~~~~~

After the Raspberry Pi reboots, the test screen will appear on the monitor as
shown below.

.. figure:: images/test_commands.png
   :width: 45em

   Test menu

1) System Test
^^^^^^^^^^^^^^

Type **1** and press **ENTER** to erase DUT flash and begin the system test.

.. figure:: images/test_command_1.png
   :width: 45em

   Starting the system test

.. attention::

   If the test fails early with error message "Error uploading firmware": Try
   disconnecting the Usb-C cable that powers the DUT, reconnecting, and running
   the test again. You should get the message "Firmware upload successful!"

   .. figure:: images/test_command_1_failure.png
      :width: 45em

      Error uploading firmware

**LCD Test**

Wait for test step 3 (LCD Test). Check if the LCD display shows the message
"Press y...".

.. figure:: images/test_command_1_led_prompt.png
   :width: 45em

   LCD test prompt

* If the message appears, press **Y** key.
* If it does not appear, press **N** key.

.. figure:: images/test_command_1_passed_lcd_test.png
   :width: 45em

   LCD test passed

**LED and Button Test**

Wait for test 7 (LED & Button Test). Check if LED DS1 is ON.

.. figure:: images/test_command_1_led_button_test.png
   :width: 45em

   LED DS1 test

* If LED DS1 is ON, press **Y** key.
* If it is OFF, press **N** key.
* Repeat this step for LEDs DS2, DS3.

.. figure:: images/test_command_1_led_button_prompt.png
   :width: 45em

   LED button prompt

Wait for the message "Press button S1! (5 second timeout)". Press button S1
(duration does not matter). Repeat for buttons S2, S3.

.. figure:: images/test_command_1_led_button_passed.png
   :width: 45em

   LED and button test passed

The remaining tests will run automatically. Wait for the final **PASSED** or
**FAILED** message.

.. figure:: images/test_command_1_passed.png
   :width: 45em

   System test passed

After testing a board, disconnect power, T1L, and the ribbon cable, and
continue with the next board.

2) Power Off
^^^^^^^^^^^^

When you are done testing, type **2** and press **ENTER** to power off the test
bench.

.. figure:: images/poweroff.png
   :width: 45em

   Power off
