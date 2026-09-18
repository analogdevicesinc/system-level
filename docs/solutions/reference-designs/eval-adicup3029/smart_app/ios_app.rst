iOS Smart App Overview
======================

**IoTNode** is iOS Smart Device App developed by **Analog Devices Inc.** to showcase example projects using **EVAL-ADICUP3029**.

iOS Device Minimum Requirement
------------------------------

Make sure you have an iOS device with following minimum requirement.

-  iOS Software Version: iOS 9.0 or higher.
-  System Memory: minimum 15MB
-  Bluetooth Version: v4 or higher

How to Download & Install IoTNode App on your iOS Device
--------------------------------------------------------

Follow below instructions to download Analog Devices IoTNode app on iOS Device.

-  Go to App Store on your iOS Device.
-  Search **IoTNode**.
-  Tap "GET" and then "INSTALL".

Wait until installation is successful.

.. admonition:: Download
   :class: download

   Direct link to `App Store <https://appsto.re/ie/jkUekb.i>`_

How to use IoTNode
------------------

Follow below instructions to run the App.

-  Turn on device Bluetooth by navigating to Settings -> Bluetooth -> Turn Slider **ON**.
-  On the iOS homescreen navigate to **IoTNode** and tap to open.

.. image:: ../images/smart_app_logo.png
   :align: center
   :width: 200

-  Once open, the app should automatically find Bluetooth devices within range, so you'll want to find and open the project you are working on.
-  Once connected, the app will provide you an option for which sensor(s) you
   are connected to that Bluetooth device.

   -  It's usually only a single sensor, so make sure it's "Checked on" and hit
      "View Data".

-  You are now connected, and data should start to display on the app.

.. image:: ../images/smart_app_ios_all_screens.png
   :align: center
   :width: 800

Interfacing Data to IoTNode
---------------------------

The **IoTNode** app supports an easy to interface registration, configuration, and data packet system. For complete details on writing embedded code to interface to the IoTNode smart app, please check out the link below.

-  :doc:`Interfacing Data with IoTNode </solutions/reference-designs/eval-adicup3029/smart_app/ble_connect>`
