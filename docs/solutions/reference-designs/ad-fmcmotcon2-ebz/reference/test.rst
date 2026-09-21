.. _ad_fmcmotcon2_ebz test:

AD-FMCMOTCON2-EBZ Test Procedure
===============================================================================

Required hardware
-------------------------------------------------------------------------------

- ZedBoard with mouse and keyboard
- SD card with ADI Linux image
- HDMI monitor
- AD-FMCMOTCON2-EBZ
- AD-DYNO2-EBZ

Prepare the SD card
-------------------------------------------------------------------------------

.. note::

   Following instructions are valid if a Windows host is used. Instructions
   regarding other operating systems can be found in the
   :external+kuiper:doc:`Kuiper Linux documentation <index>`.

- Flash the Kuiper Linux SD card image following the
  :external+kuiper:doc:`Kuiper Linux documentation <index>`.
- On Windows, use `Win32DiskImager <https://sourceforge.net/projects/win32diskimager/>`_:
  select the image file, select the SD card device, and press **Write**.

.. figure:: ../images/win32diskimager.jpg
   :alt: Win32DiskImager
   :align: center
   :width: 300

   Writing the image with Win32DiskImager

- Use Windows "Safely Remove" to eject the disk.

Program the FRU EEPROM
-------------------------------------------------------------------------------

- Connect the controller board to the ZedBoard
- Ensure that the SD card is up to date (run ADI Update Tools)
- To program the FRU EEPROM, start ADI IIO Oscilloscope, select Settings ->
  Connect; if the EEPROM memory was not already programmed, a window should
  appear:

.. figure:: ../images/fru_memory.jpg
   :alt: FRU EEPROM programming dialog
   :align: center
   :width: 300

   FRU EEPROM programming dialog

- Select the AD-FMCMOTCON2-EBZ-FRU.bin master file, type the board's Serial
  Number (written on the sticker on the controller board bottom), the Date,
  and click OK to program the EEPROM.

Test EtherCAT EEPROM
-------------------------------------------------------------------------------

- Open a Terminal Emulator and test the EEPROM memory by running
  ``sudo ./verify_eeprom``
- If everything works correctly, the following messages should appear:
  "Write OK." "Read OK."

.. figure:: ../images/test_ee2_eeprom.jpg
   :alt: EtherCAT EEPROM test
   :align: center
   :width: 300

   EtherCAT EEPROM test output

Test AD2S1210
-------------------------------------------------------------------------------

- Ensure that the SD card is up to date (run ADI Update Tools and
  ``sudo adi_update_boot.sh 10.50.1.128``)
- Connect a jumper on P6.2–P6.3
- From the Resolver tab set the Excitation Frequency to 2000 Hz and 20000 Hz.
  Measure the Sine frequency on P9.5 using an oscilloscope. Ensure the
  oscilloscope ground is connected to the DGND_ISO testpoint.

.. figure:: ../images/dgnd_iso.jpg
   :alt: DGND_ISO testpoint
   :align: center
   :width: 300

   DGND_ISO testpoint

.. figure:: ../images/2khz_iio_scope.jpg
   :alt: 2 kHz excitation - IIO Scope
   :align: center
   :width: 300

   2 kHz excitation - IIO Scope

.. figure:: ../images/2khz_scope.jpg
   :alt: 2 kHz excitation - oscilloscope
   :align: center
   :width: 300

   2 kHz excitation - oscilloscope

.. figure:: ../images/20khz_iio_scope.jpg
   :alt: 20 kHz excitation - IIO Scope
   :align: center
   :width: 300

   20 kHz excitation - IIO Scope

.. figure:: ../images/20khz_scope.jpg
   :alt: 20 kHz excitation - oscilloscope
   :align: center
   :width: 300

   20 kHz excitation - oscilloscope

Test Procedure
-------------------------------------------------------------------------------

- Insert three jumpers on the controller board as shown below:

.. figure:: ../images/eth_jumpers.jpg
   :alt: Ethernet jumpers on controller board
   :align: center
   :width: 600

   Ethernet jumpers on controller board

- Connect the hardware as shown below:

.. figure:: ../images/connections.jpg
   :alt: Hardware connections
   :align: center
   :width: 600

   Hardware connections

- Insert the Dyno sensor wire in P3 connector on the controller board with
  the black wire towards the FPGA
- Insert the Dyno motor wire in the P2 connector on the Drive Board
- Connect 24 V power supplies on P1 and P3 connectors
- Make sure the **Emergency Stop** switch is pressed
- Power on the ZedBoard
- Make sure the following LEDs are on:

  - DS1, DS2, DS3 and DS4 on the Controller Board
  - DS1 and DS2 on the Drive Board

- In the Linux ADI IIO Oscilloscope go to the **Motor Control** tab and
  select the following configuration:

  - **Motor 1**

    - **Run**: ON
    - **Delta**: OFF
    - **Direction**: Counterclockwise
    - **PWM**: 74.99%

  - **Motor 2**

    - **Run**: ON
    - **Delta**: OFF
    - **Direction**: Counterclockwise
    - **PWM**: 74.99%

.. figure:: ../images/scr_1.jpg
   :alt: Motor Control tab configuration
   :align: center
   :width: 400

   Motor Control tab configuration

- In the Linux ADI IIO Oscilloscope–Capture1 go to the **Plot Channels** pane
  and select the following configuration:

  - **ad-mc-adc**: voltage0–voltage3 ON
  - **ad-mc-adc-m2**: voltage0–voltage3 ON

.. figure:: ../images/scr_2.jpg
   :alt: Plot Channels configuration
   :align: center
   :width: 400

   Plot Channels configuration

ADC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Release the **Emergency Stop** switch and press the **Reset** switch - the
  motor should start spinning
- Make sure that there are no vibrations in the DYNO system
- In the Linux ADI IIO Oscilloscope–Capture1 press **Capture**, **AutoZoom**,
  and **Stop**
- Press the **Emergency Stop** switch - the motor should stop spinning
- Make sure there are two phase-shifted sinusoidal waveforms on screen with
  amplitude between 27000 and 37000
- Make sure there is a DC signal at approximately 21500

.. figure:: ../images/scr_mot1.jpg
   :alt: Motor 1 ADC waveforms
   :align: center
   :width: 600

   Motor 1 ADC waveforms

- Insert the Dyno sensor wire in P2 connector on the controller board with
  the black wire towards the FPGA
- Insert the Dyno motor wire in the P4 connector on the Drive Board
- Release the **Emergency Stop** switch and press the **Reset** switch - the
  motor should start spinning
- Make sure that there are no vibrations in the DYNO system
- In the Linux ADI IIO Oscilloscope–Capture1 press **Capture**, **AutoZoom**,
  and **Stop**
- Press the **Emergency Stop** switch - the motor should stop spinning
- Make sure there are two phase-shifted sinusoidal waveforms on screen with
  amplitude between 27000 and 37000
- Make sure there is a DC signal at approximately 21500

.. figure:: ../images/scr_mot2.jpg
   :alt: Motor 2 ADC waveforms
   :align: center
   :width: 600

   Motor 2 ADC waveforms

Ethernet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Insert an Ethernet cable in the P13 connector on the controller board
- Install `Iperf <https://iperf.fr/>`_ on a Windows machine
- Find the IP address of the ZedBoard by running ``ifconfig`` in a terminal
- Run Iperf server on the ZedBoard: ``iperf -s``
- Run Iperf client on the Windows PC, replacing x.x.x.x with the ZedBoard IP:
  ``iperf -c x.x.x.x``
- After a few seconds a result should appear. For a Gigabit Ethernet
  connection, ensure the speed is greater than 150 Mbit/s.

.. figure:: ../images/iperf_pc.jpg
   :alt: Iperf result on Windows
   :align: center
   :width: 500

   Iperf result on Windows

- Insert the Ethernet cable in the P11 connector on the controller board and
  repeat the steps above.

Dyno
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Release the **Emergency Stop** switch and press the **Reset** switch - the
  motor should start spinning
- Make sure that there are no vibrations in the DYNO system
- On the DYNO board open the *Measurements* menu
- Check the speed and current displayed under *Measurements* on the DYNO LCD:
  6300 rpm ±250 rpm for speed and 0.03 A for current

.. figure:: ../images/scr_dyno1.jpg
   :alt: Dyno measurements - no load
   :align: center
   :width: 200

   Dyno measurements - no load

- Set the load to 100%
- Check the speed and current: 2100 rpm ±250 rpm for speed and
  2.4 A ±0.1 A for current

.. figure:: ../images/scr_dyno2.jpg
   :alt: Dyno measurements - 100% load
   :align: center
   :width: 200

   Dyno measurements - 100% load

- Press the **Emergency Stop** switch - the motor should stop spinning
