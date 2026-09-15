.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms11-ebz/testing

.. _ad-fmcomms11-ebz testing:

Production testing of the AD-FMCOMMS11
======================================

Overview
--------

The production testing is quite simple. Since each board has been completely
characterized, and we know the layout is good, we can just look for gross
errors. There are multiple ways to run the test depending on the hardware setup.

- fmcomms11_test/fmcomms11_prod_test.sh: used to test AD-FMCOMMS11-EBZ locally
  on the carrier with GUI. A desktop shortcut named ``FMCOMMS11 TEST`` is also
  provided.
- fmcomms11_test/fmcomms11_test: used to test AD-FMCOMMS11-EBZ via console. This
  can be used remotely. You have to supply some parameters to use this.

The test parameters limits are stored in a ``csv`` file which can be specified
in the arguments when running the console test binary. The GUI version uses the
test parameters limits stored in the BOOT partition.

Requirement
-----------

- AD-FMCOMMS11-EBZ
- Zynq ZC706
- FMCOMMS SD card (at least 8 gb class 10) loaded with ADI zynq linux image
  installed with the fmcomms11_test program
- SMA RF loopback cable (1x for FMCOMMS11)
- External monitor connected to the carrier via HDMI
- Keyboard and mouse (with USB hub if they aren"t part of a combo device)
- USB OTG adapter

Preparing the SD Card
---------------------

If you have a production test SD-card already, you can skip this section and
proceed to the :dokuwiki:`Hardware Setup <testing#hardware_setup>` section.

Obtain the pre-built SD card Zynq image for ZC706 pre-installed with the
fmcomms11 test program from this :dokuwiki:`link <testing#hardware_setup>`. If
the image file is compressed – that is, not ending with ``.img`` but with file
extensions of xz, zip, and rar, decompress the file using 7zip or similar tool.
Insert the SD card (at least 8gb ) to a computer. Using a disk writer software,
write the downloaded image (img file) to the SD card. Instructions can be found
on
https://wiki.analog.com/resources/tools-software/linux-software/zynq_images/windows_hosts
about how to use the Win32 disk manager. Etcher, on the other hand, is easier to
use than win32 disk manager. Example Disk writer software:

- `Etcher.io (Linux, Windows, Mac) <https://www.balena.io/etcher/>`__
- `Win32 Disk Imager (Windows) <https://sourceforge.net/projects/win32diskimager/>`__

Once the image has been written on the SD card, it is now ready to use. Eject
the SD card from the card reader and proceed to the hardware setup.

Hardware Setup
--------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/system_test_setup.png

- Plug in the external monitor and connect it via HDMI to the carrier board.
- Connect the USB OTG adapter (and USB hub if needed) to the USB port on the
  carrier, then plug in the keyboard and mouse as well.
- Attach the FMCOMMS11 that has a hardware loopback to the Carrier board via the
  FMC HPC connector (J37).
- Attach the power supply cable of the fan to the fan supply cable connected to
  J61. Make sure that the fan is attached to the FMCOMMS11 securely.
- Insert the SD card that contains the Zynq image and confirm that the carrier
  board is set to boot from SD. The SW11 is configured the same as the following
  image to ensure that the carrier will boot from SD card.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/zilynx_switch_settings.png
   :width: 300px

- Plug the power adapter of the Zynq ZC706.
- Switch on the Zynq ZC706 to and wait for the system to boot on to start the
  test.

Software Setup
--------------

If the Zynq image used is the pre-built image pre-installed with the test
program, there is no other software setup needed.

Test process
------------

#. Make sure that Zynq Carrier board is turned-off during each start of the
   test.
#. Attach the RF loopback cable to the card. See the image in the Hardware Setup
   section for correct placement.
#. Attach the card into the carrier board through the FMC HPC J37.
#. Power on the carrier board.

#. A terminal window open and a dialog box will prompt with a message ensuring
   that the loopback cable is connected as instructed in step 2. Click OK if the
   RF loopback cable is already connected. If there is no dialog box,
   double-click the FMCOMMS11 Test icon in the desktop.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/hardware_setup_reminder.png
      :width: 400px

#. When prompted with a window like the following image, enter the serial number
   found on the board. Pressing cancel will just cancel the test.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/board_number_entry.png
      :width: 300px

#. After entering the serial number, the test will start, and progress will be
   shown on the terminal.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/linux_terminal.png

#. When tests pass, the following window should be shown

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/test_results.png
      :width: 200px

#. If tests fail, a window like the following image should be shown below. In
   either case, hit the OK button to end the test program. You may re-run the
   test software from the desktop to re-test.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/test_results_2.png
      :width: 200px

#. In case of Program errors, the message box like the image below will appear:

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms11-ebz/program_error_msg.png
      :width: 300px

   The instructions on what to do with the error will be displayed on the
   message box. In the case above, the error might be solved by stopping all
   programs that are using the libiio. For example, when the IIO-Oscilloscope
   plot is running, this error will appear. So, stopping IIO-Oscilloscope might
   fix it. If the test has been restarted but the same error appears, the board
   under test has failed. If the next boards have the same problem, retest a
   board that was tested before that ``passed`` to check the state of the
   carrier board.
#. If test ended but did not automatically shut down, Click the icon in top
   left, click the log-off icon, then, click the shutdown button. During
   shutdown, the desktop view will exit and turn black. After several seconds
   power off the carrier board via the physical switch. SW1.
#. Once the carrier board is already powered down, remove the FMCOMMS11 that was
   tested and return to step 1 to continue with the next board.
#. In each test except for program errors, two files are generated, and a
   summary file will be updated.

   #. Measurement file (f_measurement-XXXXX.csv where XXXXX is the serial
      number) - Contains all the data from the measurements done in the program
   #. Processed File (f_processed-XXXXX.csv) - contains the mean, standard
      deviation, as well as the PASS or FAIL remarks for the individual test
      set.
   #. Summary File (f_summary.csv) – contains the list of board serial numbers
      that has been tested and the result of most recent test on each board.
      Therefore, running the test again will just update the result and
      overwrite the processed file and measurement file of that board.

::

   .. note::

Re-running the test on the same board serial number will just overwrite the
previous test results for that serial number. These files will be stored in
/boot/test_results/. To backup these files, turn off the carrier board, remove
the SD card, and insert the SD card to the computer. Locate the detected
removable drive named ``BOOT`` and copy the test_results folder to computer. As
alternative, if the carrier board is connected to the network, SSH or SCP can be
used to copy the files from the ZC706 to the computer.
