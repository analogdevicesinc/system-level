AD-TRXBOOST1-EBZ Production Testing
===================================

Overview
--------

The production testing is quite simple, since each board has been completely
characterized and we know the layout is good, we can just look for gross errors.
First the noise floor is checked when no input is supplied to make sure it is
within a certain threshold, then a couple tones are input and the response is
checked to be within certain bounds.

Creating an SD test card
------------------------

First, write the latest available SD card image found at
:external+kuiper:doc:`kuiper-linux <index>` to a spare card and prepare the
card to boot into Linux as detailed on that page for the target FMCOMMS and
carrier boards. In this case copy the BOOT.BIN and devicetree.dtb files from
the zynq-zc706-adv7511-ad9361-fmcomms2-3 folder into the base directory of
the SD card's boot partition).

Then the card needs to be modified to run the tests automatically on boot. Test scripts are provided in `linux_image_ADI-scripts <https://github.com/analogdevicesinc/linux_image_ADI-scripts>`_ that automate initializing osc with the correct profile and environment.

See the following example diff for required changes to the launcher to run the
tests on boot:

.. code:: diff

   --- ./.config/autostart/config_autostart_osc.desktop    2013-12-09 15:55:41.774730469 -0500
   +++ ./.config/autostart/config_autostart_osc.desktop    2012-12-31 19:20:18.000000000 -0500
   @@ -1,11 +1,11 @@

    [Desktop Entry]
    Type=Application
   -Exec=/usr/local/bin/osc
   +Exec=sudo /usr/local/bin/test_trxboost1.sh
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true

Required hardware
-----------------

-  1 ZC706 carrier board and power supply
-  1 keyboard/mouse
-  1 HDMI monitor
-  1 SD test card
-  1 AD-FMCOMMS3-EBZ board
-  1 AD-TRXBOOST1-EBZ board
-  1 3 pin power cable
-  1 SMA loopback cable

Test process
------------

The TRXBOOST1 testing should be done using the following steps:

-  Make sure the ZC706 is plugged in with the testing SD card inserted and the
   HDMI monitor and keyboard/mouse are properly attached to the system and
   powered on.
-  The TRXBOOST1 board should be mounted on the TX2A/RX2A jacks of the
   AD-FMCOMMS3-EBZ board and the power cable connected as seen in the following
   image.

.. image:: images/trxboost1_-_close_crop_-_copy.jpg
   :align: center
   :width: 800

-  Connect the RX_IN and TX_OUT jacks on the TRXBOOST1 board with the SMA
   loopback cable.
-  Power on the ZC706 board.
-  The board should boot into the ADI Linux environment and begin the tests
   automatically.
-  When tests pass, the following window should be shown as seen in the image
   below. If tests fail, a error dialog will be shown instead. In either case,
   hit the confirmation button to halt Linux and after several seconds power off
   the carrier board via the physical switch on the ZC706.

.. image:: images/freqcvt1-tests-passed.png
   :align: center
   :width: 800

-  Remove the TRXBOOST1 card and return to step 1 to continue with the next
   board.
