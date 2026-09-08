ADICUP360 PC/Laptop Drivers
===========================

When connecting up the ADICUP360 to your computer or laptop, all the necessary
drivers are automatically located and loaded up when using Windows operating
systems.

There are two sets of drivers that get installed on your computer depending on
which USB port you have plugged into your laptop or PC.

.. important::

   It EXTREMELY important to ensure that all drivers are installed, before
   trying to use the ADICUP360 with CrossCore Embedded Studios. So when you see
   that the drivers are being installed in the task bar, open it up and wait
   till everything finished before progressing.

|image1|

Mass Storage Drives
-------------------

MBED Drive
~~~~~~~~~~

When the ADICUP360 is connected to your computer via the **DEBUG USB** port (P14), the "MBED" drive is displayed on your computer as a mass storage device.

This mode allows users to drag and drop or copy and paste a .BIN file directly
into the MBED drive, and that file will program the ADuCM360 on the ADICUP360.
This means you don't have to use the tools or the debugger to program your
board, making this very useful in production releases or updating applications
already in the field.

The PC will start searching for and install the following drivers:|image2|

Then go to the **My Computer** view and search for the MBED drive, if you see this then the drivers are complete and correct.\

|image3|

Bootloader Drive
~~~~~~~~~~~~~~~~

When the ADICUP360 is connected to your computer via the **DEBUG USB** port (P14), AND you hold down the "RESET" button (S5), the "BOOTLOADER" drive is displayed on your computer as a mass storage device. This mode allows a user to overwrite the ADICUP360 interface file. This allows for patches and updates to the firmware to the on board emulator/debugger.

The PC will still use the same drivers that were installed initially:|image4|

Then go to the **My Computer** view and search for the Bootloader drive, if you see this then the drivers are complete and correct.

|image5|

.. admonition:: Download
   :class: download

   The current ADICUP360 interface file can be downloaded here:

   
   `ADICUP360 Interface File <../resources/if_k20dx128_target_aducm360.zip>`_
   

Serial Drive
------------

When the ADICUP360 is connected to your computer via the **USER USB** port (P13), the UART port of the ADuCM360 is able on your computer a virtual Serial COM Port.

This allows users to communicate with the ADICUP360 via the UART port through
serial terminal programs such as Putty or Tera Term (there are many other
applications as well) This will allow you to output data to a PC or even send
UART commands to the ADICUP360.

The PC will start searching for and install the following drivers:|image6|

.. |image1| image:: ../images/device_drivers_install_notification.png
   :width: 400

.. |image2| image:: ../images/debug_usb_device_driver_install.png
   :width: 400

.. |image3| image:: ../images/windows_explorer_mbed_drive.png
   :width: 550

.. |image4| image:: ../images/debug_usb_device_driver_install.png
   :width: 400

.. |image5| image:: ../images/computer_win.png
   :width: 550

.. |image6| image:: ../images/user_usb_device_driver_install.png
   :width: 400
