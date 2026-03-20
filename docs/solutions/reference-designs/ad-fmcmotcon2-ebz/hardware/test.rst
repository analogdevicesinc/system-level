AD-FMCMOTCON2-EBZ test procedure
================================

Required hardware
-----------------

-  ZedBoard with mouse and keyboard
-  SD card with ADI Linux image
-  HDMI monitor
-  AD-FMCMOTCON2-EBZ
-  AD-DYNO2-EBZ

Prepare the SD card
-------------------

.. note::

   Following instructions are valid if a Windows host is used. Instructions regarding other Operating Systems can be found in the :external+kuiper:doc:`Kuiper Linux documentation <index>`.

-  Download the SD card image: `motcon2_2015_05_06.zip <../resources/motcon2_2015_05_06.zip>`_
-  Extract motcon2.img from motcon2_2015_05_06.zip archive.
-  Download and install Win32DiskImager: http://sourceforge.net/projects/win32diskimager/files/latest/download?source=navbar
-  Open Win32DiskImager, select the extracted image file (motcon2.img), select
   the SD card device ([K:\\] in our example) and press the "Write" button to
   write the image to the device:

.. image:: ../images/win32diskimager.png
   :width: 300

-  Use Windows "safely remove" to eject the disk.

Program the FRU EEPROM
----------------------

-  Connect the controller board to the ZED board
-  Ensure that the SD card is up to date (run ADI Update Tools)
-  To program the FRU EEPROM, start ADI IIO Oscilloscope, select Settings ->
   Connect; if the EEPROM memory was not already programmed, a window should
   pop-up:

.. image:: ../images/fru_memory.png
   :width: 300

-  Select the AD-FMCMOTCON2-EBZ-FRU.bin master file, type the board's Serial
   Number (which is written on the sticker on the controller board bottom) and
   the Date and click OK to program the EEPROM.

Test ETHERCAT EEPROM
--------------------

-  Open a Terminal Emulator and test the EEPROM memory running "sudo ./verify_eeprom"
-  If everything works OK, the following messages should appear: "Write OK."
   "Read OK."

.. image:: ../images/test_ee2_eeprom.png
   :width: 300

Test AD2S1210
-------------

-  Ensure that the SD card is up to date (run ADI Update Tools and "sudo adi_update_boot.sh 10.50.1.128")
-  Connect a jumper on P6.2 - P6.3
-  From the Resolver tab set the Excitation Frequency to 2000 Hz and 20000 Hz.
   The Sine frequency can be measured on P9.5 using an oscilloscope. Make sure
   that the oscilloscope ground is connected to the DGND_ISO testpoint.

.. image:: ../images/dgnd_iso.jpg
   :width: 300

|image1| |image2|

|image3| |image4|

Test Procedure
--------------

-  Insert three jumpers on the controller board as in the picture below

.. image:: ../images/eth_jumpers.jpg
   :alt: Eth Jumpers
   :width: 600

-  Connect the hardware as shown in the picture below

.. image:: ../images/connections.jpg
   :alt: connections
   :width: 600

-  Insert the Dyno sensor wire in P3 connector on the controller board with the black wire towards the FPGA
-  Insert the Dyno motor wire in the P2 connector on the Drive Board
-  Connect 24V power supplies on P1 and P3 connectors
-  Make sure the **Emergency Stop** switch is pressed
-  Power on the Zedboard
-  Make sure the following LEDs are on:

   -  DS1, DS2, DS3 and DS4 on the Controller Board
   -  DS1 and DS2 on the Drive Board

-  In the Linux ADI IIO Oscilloscope go to the **Motor Control** tab and select
   the following configuration:

   -  **Motor 1**

      -  **Run**: ON
      -  **Delta**: OFF
      -  **Direction**: Counterclockwise
      -  **PWM**: 74.99%

   -  **Motor 2**

      -  **Run**: ON
      -  **Delta**: OFF
      -  **Direction**: Counterclockwise
      -  **PWM**: 74.99%

.. image:: ../images/scr_1.png
   :alt: Motor Control Tab
   :width: 400

-  In the Linux ADI IIO Oscilloscope-Capture1 go to the **Plot Channels** pane
   and select the following configuration:

   -  **ad-mc-adc**

      -  **voltage0**: ON
      -  **voltage1**: ON
      -  **voltage2**: ON
      -  **voltage3**: ON

   -  **ad-mc-adc-m2**

      -  **voltage0**: ON
      -  **voltage1**: ON
      -  **voltage2**: ON
      -  **voltage3**: ON

.. image:: ../images/scr_2.png
   :alt: Motor Control Tab
   :width: 400

ADC
~~~

-  Release the **Emergency Stop** switch and press the **Reset** switch -- the motor should start spinning
-  Make sure that there are no vibrations in the DYNO system.
-  In the Linux ADI IIO Oscilloscope-Capture1 press the following buttons **Capture**, **AutoZoom** and **Stop**
-  Press the **Emergency Stop** switch -- the motor should stop spinning
-  Make sure there are two phase-shifted sinusoidal waveforms on the screen with the amplitude varying between 27000 to 37000
-  Make sure there is a DC signal between around 21500

.. image:: ../images/scr_mot1.png
   :alt: Motor Control Tab
   :width: 600

-  Insert the Dyno sensor wire in P2 connector on the controller board with the black wire towards the FPGA
-  Insert the Dyno motor wire in the P4 connector on the Drive Board
-  Release the **Emergency Stop** switch and press the **Reset** switch -- the motor should start spinning
-  Make sure that there are no vibrations in the DYNO system.
-  In the Linux ADI IIO Oscilloscope-Capture1 press the following buttons **Capture**, **AutoZoom** and **Stop**
-  Press the **Emergency Stop** switch -- the motor should stop spinning
-  Make sure there are two phase-shifted sinusoidal waveforms on the screen with the amplitude varying between 27000 to 37000
-  Make sure there is a DC signal between around 21500

.. image:: ../images/scr_mot2.png
   :alt: Motor Control Tab
   :width: 600

Ethernet
~~~~~~~~

-  Insert an ethernet cable in the P13 connector on the controller board
-  Install `Iperf <https://iperf.fr/download/iperf_2.0.5/iperf-2.0.5-3-win32.zip>`_ on a Windows machine
-  Find the IP address of the Zedboard by typing the following command in the terminal ``ifconfig``
-  Run Iperf server on the Zedboard by typing the following command in the terminal ``iperf -s``
-  Run Iperf client on the Windows PC by typing the following command in the command promt. Replace x with the Zedboard IP
-  ``iperf -c x.x.x.x``
-  After a few seconds a similar message to the one below should appear in the
   windows console. Please make sure that for a Gigabit Ethernet connection, the
   speed is greater than 150 Mbits/sec

.. image:: ../images/iperf_pc.jpg
   :alt: Iperf PC
   :width: 500

-  Insert the ethernet cable in the P11 connector on the controller board and
   repeat the steps above

Dyno
~~~~

-  Release the **Emergency Stop** switch and press the **Reset** switch -- the motor should start spinning
-  Make sure that there are no vibrations in the DYNO system.
-  On the DYNO board open the *Measurements* menu
-  Check the speed & current displayed under *Measurements* on the DYNO LCD to see if it reads 6300rpm +/- 250rpm for speed and 0.03A for current

.. image:: ../images/scr_dyno1.png
   :alt: Motor Control Tab
   :width: 200

-  Set the load to 100%
-  Check the speed & current displayed under *Measurements* on the DYNO LCD to see if it reads 2100rpm +/- 250rpm for speed and 2.4A +/- 0.1A for current

.. image:: ../images/scr_dyno2.png
   :alt: Motor Control Tab
   :width: 200

-  Press the **Emergency Stop** switch -- the motor should stop spinning

.. |image1| image:: ../images/2khz_iio_scope.png
   :width: 300
.. |image2| image:: ../images/2khz_scope.png
   :width: 300
.. |image3| image:: ../images/20khz_iio_scope.png
   :width: 300
.. |image4| image:: ../images/20khz_scope.png
   :width: 300
