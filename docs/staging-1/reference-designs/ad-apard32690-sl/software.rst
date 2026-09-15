.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-apard32690-sl/software

.. _ad-apard32690-sl software:

AD-APARD32690-SL System User Guide
==================================

| .. important::

   We are in the process of migrating our documentation to GitHub Pages.
   | The latest version of this page can be found at https://analogdevicesinc.github.io/documentation/solutions/reference-designs/ad-apard32690-sl/index.html

Required Hardware
-----------------

Development kits
----------------

- :adi:`AD-APARD32690-SL <design-center/evaluation-hardware-and-software/evaluation-boards-kits/AD-APARD32690-SL.html#eb-overview>`

Power supplies
~~~~~~~~~~~~~~

- 5V to 28V at 2A external power supply or 5V USB-C power supply

Programmers
^^^^^^^^^^^

-
  :adi:`MAX32625PICO <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32625pico.html>`
  or any other similar programmer supporting the SWD interface

--------------

AD-APARD32690-SL Board Description
----------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-apard32690-sl/apard32690_hw_components.png
   :width: 800px

.. list-table::
   :header-rows: 1

   * - LEDs
     -
   * - DS1
     - Power good
   * - DS2
     - User LED

.. list-table::
   :header-rows: 1

   * - Buttons & Switches
     -
   * - S1
     - MAX32690 Reset
   * - S2
     - User Button
   * - S3
     - User switches
   * - S4
     - 1: ADIN1110 SWPD_EN
   * -
     - 2: ADIN1110 SPI_CFG0
   * -
     - 3: ADIN1110 SPI_CFG1

.. list-table::
   :header-rows: 1

   * - Jumper settings
     -
   * - P50
     - Position 1-2: Connect programmer SWD_RX to WiFi UART TX
   * -
     - Position 2-3: Connect programmer SWD_RX to MAX32690
   * - P55
     - Position 1-2: Connect programmer SWD_TX to WiFi UART RX
   * -
     - Position 2-3: Connect programmer SWD_RX to MAX32690
   * - P38
     - Connect WiFi UART TX to MAX32690
   * - P56
     - Connect WiFi UART RX to MAX32690
   * - P51
     - Position 1-2: Set programmer voltage to 3V3 (normal operation mode)
   * -
     - Position 2-3: Set programmer voltage to 1V8 (WiFi chip programming)

.. list-table::
   :header-rows: 1

   * - Connectors
     -
   * - P1
     - 10BASE-T1L
   * - P10
     - USB-C Power & Data
   * - P14
     - External Power 5V-28V
   * - P9
     - SWD Programmer
   * - P11
     - SPOE Shield ISO GND
   * - P16
     - SPOE Shield PI+
   * - P17
     - SPOE Shield PI-
   * - P53
     - SPOE Shield PI+
   * - P54
     - SPOE Shield PI-
   * - P12
     - SPOE Shield Data TRX N
   * - P15
     - SPOE Shield Data TRX P
   * - P8
     - SPI PMOD
   * - P13
     - I2C PMOD
   * - P2
     - Arduino Connector - Power
   * - P3
     - Arduino Connector - Analog
   * - P4
     - Arduino Connector - SPI / I2S
   * - P5
     - Arduino Connector - SPI & I2C
   * - P6
     - Arduino Connector - UART
   * - P7
     - Arduino Connector - GPIO & CAN

System Setup
------------

- Connect the AD-APARD32690-SL to the
  :dokuwiki:`AD-T1LUSB2.0-EBZ </resources/eval/user-guides/ad-t1lusb-ebz>` using
  the single pair Ethernet cable.
- Connect the AD-T1LUSB2.0-EBZ to your PC using an USB cable.
- Connect the MAX32625PICO programmer, or any programmer supporting the SWD
  interface, to the AD-APARD32690-SL.
- Connect the power supply to the AD-APARD32690-SL.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-apard32690-sl/apard32690_system_setup.jpg
   :width: 600px

Updating the AD-APARD32690-SL firmware
--------------------------------------

Setting up the MAX32625PICO
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To update the board"s firmware, a new bootloader has to be flashed on the
MAX32625PICO.

- Download the firmware image:
  `MAX32625PICO firmware <https://github.com/MaximIntegrated/max32625pico-firmware-images/raw/master/bin/max32625_max32650fthr_if_crc_swd_v1.0.6.bin>`__
- Set the MAX32625PICO in MAINTENANCE mode:
- Disconnect the MAX32625PICO from the PC and the AD-SWIOT1L-SL board.
- Plug the micro USB cable only in the MAX32625PICO.
- Keep the button on the MAX32625PICO pressed.
- Plug the micro USB cable into the PC.
- Once you see the MAINTENANCE drive being mounted, you may release the button.

  .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-swiot1l-sl/picture2.jpg

- Drag and drop (to the MAINTENANCE drive) the firmware image you previously
  downloaded.
- After a few seconds, the MAINTENANCE drive will disappear and will be replaced
  by a drive named DAPLINK. Once this is done, the process is complete, and the
  MAX32625PICO may be used to flash the firmware of the AD-SWIOT1L-SL board.

Programming the AD-APARD32690-SL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect the MAX32625PICO to the PC using the micro USB cable.
- Connect the MAX32625PICO to the AD-APARD32690-SL board using the 10-pin ribbon
  cable.
- Connect the power supply to the AD-APARD32690-SL. Make sure the board is
  powered up for the next steps.
- A DAPLINK drive should appear as mounted on your PC.
- Drag and drop the new firmware image into the DAPLINK drive. After a few
  seconds, the drive will be remounted.
- Check the DAPLINK directory and make sure there is no FAIL.TXT file. In case
  there is, repeat the drag and drop step. Otherwise, you may disconnect the
  MAX32625PICO from the AD-APARD32690-SL, since the firmware update is complete.

AD-APARD32690-SL Software Stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system is accompanied by an open-source software stack and associated
collateral, enabling a complete experience from evaluation and prototyping all
the way to production firmware and applications development.

The :git-no-OS:`AD-APARD32690-SL firmware <projects/apard32690>` is based on
Analog Devices" open-source no-OS framework, which includes all the tools
required for embedded code development and debugging as well as libraries
enabling host-side connectivity for system configuration and data transfer over
the UART or the 10BASE-T1L interfaces. The firmware source code and related
documentation can be found on the Analog Devices GitHub at the link above.
