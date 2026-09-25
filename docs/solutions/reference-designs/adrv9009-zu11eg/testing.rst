ADRV9009-ZU11EG Production Testing
==================================

Overview
--------

Production tests for ADRV9009-ZU11EG are composed of a series of Bash scripts
that run both on Raspberry Pi and DUT (Device Under Test). The test procedure
requires a Raspberry Pi 4 board (host) connected via Ethernet cable to the DUT.
The Raspberry Pi board requires to have a HDMI monitor and USB keyboard
connected. All test sequences are selected and started from the GUI interface
displayed by Raspberry Pi on the monitor. Please find the required equipment
list below:

Required Hardware
-----------------

-  Raspberry Pi4: Is strictly required to be version 4 or newer. USB 3.0
   connection is required during testing.
-  HDMI monitor: monitor should be connected to Raspberry Pi to display
   the testing sequence and the testing results
-  USB keyboard: keyboard should be connected to Raspberry Pi USB 2.0
   port (black). It is required to interact with the testing SW.
-  USB A-USB type C cable: It is required to be connected between
   Raspberry Pi USB 3.0 port (blue) and USB-C connector of DUT when USB
   device mode of DUT is tested. Will be displayed on test monitor
-  USB A – Micro USB cable: Should be connected between Raspberry Pi USB
   2.0 port and DUT microUSB UART connector (P8). This is required for
   UART over USB interface testing
-  Raspberry Pi microSD card: A minimum 8GB Class 10 microSD card
   prepared for testing sequence as presented bellow should be inserted
   in Raspberry Pi.
-  DUT SD card: A minimum 8GB Class 10 SD card prepared for testing
   sequence as presented bellow should be inserted in ADRV2CRR-FMC P15
   slot.
-  CAT5 ethernet cable: Using ethernet cable communication between
   Raspberry Pi and DUT is performed. On DUT side the ethernet cable
   should be connected on M2 port (Ethernet RGMII)
-  I2C programming cable: This cable is required to be connected between
   Raspberry Pi I2C port (pins 3 - SDA, 2 - SCL and 6 – GND) and
   ADRV2CRR-FMC P19 pin header. Using this connection and item 1 from
   Raspberry Pi menu the ADM1266 sequencer can be programmed
-  USB-C power supply is required for powering up the Raspberry Pi
-  ADRV2CRR-FMC: is the carrier board that can be tested selecting item 3
   on the test menu. It can be considered device under test or should be
   used as requirement when SOM is tested as support carrier for
   ADRV9009-ZU11EG RF-SOM
-  ADRV9009-ZU11EG RF-SOM: can be tested selecting item 4 from test menu.
   It can be tested or used when testing ADRV2CRR-FMC
-  QSFP loopback: should be connected to P3 on ADRV2CRR-FMC (molex 747630020)
-  SFP loopback: should be connected to P4 on ADRV2CRR-FMC
   (amphenol SF-SFPPLOOPBK-003.5)
-  FMC loopback: should be connected to P1 on ADRV2CRR-FMC (Apissys AF101)
-  PCI-Express loopback: should be powered on using an USB A – microUSB
   cable and connected to P17 on ADRV2CRR-FMC (Whizz Systems - PCIe
   Loopback Card)
-  Ethernet loopback: should be connected on M1 port (Ethernet SGMII)
   on ADRV2CRR-FMC
-  Audio loopback: should be connected to P6 and P5 connectors on ADRV2CRR-FMC
-  4 U.FL loopback cables: required for RF testing of ADRV9009-ZU11EG
   RF-SOM (U.FL-2LPHF6-068N1T-A-100)
-  Display Port to HDMI cable: should be connected to P2 video output
   on ADRV2CRR-FMC
-  USB-C OTG cable: should be connected when USB host mode is tested
-  USB 3.0 memory stick: should be FAT formatted and connected through
   USB-C OTG cable to ADRV2CRR-FMC when USB host mode is tested
-  12V power supply: connected to P11 on ADRV2CRR-FMC.

The complete test jig should look like:

.. image:: images/zu11eg-prod-test-setup.jpg
   :align: center
   :width: 600

Required Software
~~~~~~~~~~~~~~~~~

ADRV9009-ZU11EG SD card
^^^^^^^^^^^^^^^^^^^^^^^

The SD card image used for production testing is based on official release of
Zynq images and can be downloaded from :

.. admonition:: Download
   :class: download

   -  **15 December 2022 release**
   -   `Actual file (DUT, 15 Dec 2022) <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/talise_prod_15dec_2022.zip>`_
   -  Checksum ``b056120a53e13b197b5b366742d9f5c7``

.. admonition:: Download
   :class: download

   -  **28 May 2020 release**
   -   `Actual file (DUT, 28 May 2020 FMCOMMS8) <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/adrv9009_fmcomms8_test_card_28_05.img.tar.xz>`_
   -  Checksum ``9d3455a071f4151b9c320282abcb2f04``

.. admonition:: Download
   :class: download

   -  **27 May 2020 release**
   -   `Actual file (DUT, 27 May 2020 SOM) <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/adrv9009_som_test_card_27_05.img.tar.xz>`_
   -  Checksum ``4efbaa39928f2f36b7b462156e6d00f6``

.. note::

   To write it on SD card can follow the instructions for:
   :dokuwiki:`linux hosts <resources/tools-software/linux-software/zynq_images/linux_hosts>` or
   :dokuwiki:`windows hosts <resources/tools-software/linux-software/zynq_images/windows_hosts>`

Raspberry PI SD card
^^^^^^^^^^^^^^^^^^^^

The SD image used is based on Raspbian with desktop. On top of that are
installed the testing scripts. The image can be created starting from vanilla
Raspbian or downloaded from:

.. admonition:: Download
   :class: download

   -  **15 December 2022 release**
   -  `Actual file (RPi, 15 Dec 2022) <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/rpi_talise+prod_15dec.zip>`_
   -  Checksum ``0d8759784c1cebbcd908fe8a01083272``

.. admonition:: Download
   :class: download

   -  **02 Nov 2021 release**
   -  `Actual file (RPi, 02 Nov 2021) <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/adrv9009_pi_test_card_02_11.tar.xz>`_
   -  Checksum ``080fb8771e12195eba7196f9de05ec1c``

.. admonition:: Download
   :class: download

   -  **27 May 2020 release - outdated, do not use!**
   -  `Actual file (RPi, 27 May 2020) <https://swdownloads.analog.com/cse/prod_test_rel/talise_test/adrv9009_pi_test_card_27_05.img.tar.xz>`_
   -  Checksum ``cf5b55f2a874ef43e47f269b4c534c9d``

.. note::

   To write it on SD card can follow the instructions:
   `Installing PI images <https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system>`_

Required setup steps
~~~~~~~~~~~~~~~~~~~~

-  Connect HDMI cable to Raspberry Pi
-  Connect USB keyboard to Raspberry Pi
-  Insert Raspberry Pi microSD card
-  Connect power supply to Raspberry Pi
-  Connect all loopbacks to DUT

.. image:: images/ufl-loopback.png
   :align: center
   :width: 400

-  Connect Ethernet cable between Raspberry Pi and DUT
-  Connect USB cables between Raspberry Pi and DUT
-  Connect I2C pins from Raspberry Pi to P19.

.. image:: images/i2c-rpi-adrv9009-conn.png
   :align: center
   :width: 300

-  Insert SD card in DUT
-  Connect DisplayPort cable to DUT
-  Power on DUT

Test process
~~~~~~~~~~~~

First make sure all the required setup explained above is completed. Once the
test setup is ready, SOM testing should be done using the following steps:

-  Power on both DUT and Raspberry Pi
-  The following screen should be visible after Raspberry Pi booted:

.. image:: images/boot-pi-screen.png
   :align: center
   :width: 800

-  Before starting the test place the labels containing the serial number and
   MAC address on the RF shielding top cover.

.. warning::

   After this step, DO NOT SWAP the RF shielding top cover between boards.

.. important::

   When testing the ADRV9009-ZU11EG run the following tests in this exact order:

   -  Test 1
   -  Test 2
   -  Test 4
   -  Test 5
   -  Test 6

-  Testing sequence can be started by selecting one of the menu items. In order
   to start testing an Ethernet cable should be connected between Raspberry Pi
   and DUT. At the beginning of every test the correct connection with DUT is
   checked. If the connection cannot be established the following error message
   will be printed:

.. image:: images/boot-pi-eth-conn.png
   :align: center
   :width: 800

.. tip::

   Make sure that Ethernet cable is connected, DUT is powered up, DUT SD card is
   inserted and boot mode switches (S13-S16) are configured for SD boot.

-  If connection is OK the test will start. Below is an example of test 1 and 2
   running:

.. image:: images/adrv9009-seq-pll.png
   :align: center
   :width: 700

-  Test 1 - Wait for 30 seconds after PS_DONE LED lights up.

.. image:: images/talise_t1_led_on.jpg
   :align: center
   :width: 300

-  Test 2 - Power cycling needed after PS_DONE LED is OFF.

.. image:: images/talise_t1_led_off.jpg
   :align: center
   :width: 300

-  Test 5 – insert the last 4 digits of the MAC address from the RF
   shielding top cover.

.. image:: images/adrv9009-rf-shielding.png
   :align: center
   :width: 400

-  Test 4 & Test 5 & Test 6 - Follow on-screen instructions to complete
   the tests.
-  Heatsink needs to be installed and **Test 6** should be run again.
-  If test completed successfully the PASSED message will be printed in green
   like in the screen bellow. This means that DUT passed all the assigned tests.

.. image:: images/test_passed_screen.jpg
   :align: center
   :width: 600

-  If one of the tests failed, the FAIL message will be printed like in the
   screen capture bellow:

.. image:: images/test_failed_screen.jpg
   :align: center
   :width: 600

-  In case of a failed test the program will ask if the tester wants to
   repeat that test immediately. The test can be repeated by an undefined
   number of times.
-  If the problem is persistent and the test failing continuously the test
   engineer can decide to not repeat it anymore.

.. tip::

   In this situation it will be asked if user wants to close the test sequence
   and declare the DUT tested failed or can respond NO(n) to question “Do you
   want to close the test?” and in this way mark the test as passed and bypass
   it.

   .. warning::

      This is not recommended!

.. important::

   When testing is finished ADRV and Raspberry PI should always be powered off
   before power is unplugged otherwise the SD cards can be corrupted. First
   should be selected item 9 to power off ADRV. The test engineer should wait
   until LEDs DS6 and DS7 are off. Now the power can be disconnected from ADRV.
   After ADRV is off the Raspberry PI can be turned off by selecting item 8.
