ADXL372 Demo using Bluetooth
============================

This demo will use **EVAL-ADXL372-ARDZ** along with **EVAL-ADICUP3029** to create a impact measurement application. The **ADXL372** is an ultralow power, 3-axis, **±200 g** MEMS accelerometer.

General Description/Overview
----------------------------

The ADXL372 demo project uses the **EVAL-ADXL372-ARDZ** shield which has an ADXL372 accelerometer. The ADXL372 is configured to operate in "Instant On" mode which means that the device is powered down, until the sensor records an impact event that triggers a threshold. Once that level is surpassed, the ADXL372 automatically goes into measurement mode to capture the rest of the impact event.

The **EVAL-ADICUP3029** is designed for IOT (Internet of Things) applications in mind, and therefore comes with on board **Bluetooth 5.0** module. The ADuCM3029 is placed in "Plexi" mode, to optimize it's ultra low power consumption and can only be woken up from an external interrupt that comes from the ADXL372 impact sensor. At that point the ADuCM3029 is placed into full power mode to do the other application tasks necessary, before being placed back into "Plexi" mode.

The data is sent via Bluetooth 5.0 link to an iOS smart device, where all the
max impact data can be read.

Both boards and all components are used in their respective low power modes to
optimize the solutions battery life.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-ADXL372-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  iOS Smart Phone/Tablet *(only needed for Bluetooth display)*

-  Software

   -  ADuCM3029_Asset_Health_demo software (on Github)
   -  CrossCore Embedded Studio (2.6.0 or higher)
   -  ADuCM302x DFP (2.0.0 or higher)
   -  ADICUP3029 BSP (1.0.0 or higher)
   -  iOS IoTNode App *(optional)*
   -  Serial Terminal Program, Such as Putty or Tera Term

      -  *(Required for running in release mode only and if you don't want to
         use the smart device app)*

Setting up the Hardware
-----------------------

-  Set switch S2 to USB Arduino function in order to view data over UART also. The UART baud rate is **9600** baud.

.. image:: ../images/img_20170612_144023_hdr.jpg
   :align: center
   :width: 800

-  Place the **EVAL-ADXL372-ARDZ-INT** on top of the **EVAL-ADICUP3029**.
-  Make sure the jumpers **P10, P11, P12** are configured exactly as the picture below.

   -  P10 -> Pin 1-2
   -  P11 -> Pin 1-2
   -  P12 -> Pin 1-2

.. image:: ../images/eval_adxl_ardz_int.jpg
   :align: center
   :width: 800

-  Plug in the micro USB cable into the (P10) USB port on the EVAL-ADICUP3029,
   and the other end into the PC or laptop.

Configuring the Software
------------------------

For this application you will need to install on your :doc:`IOS </solutions/reference-designs/eval-adicup3029/smart_app/ios_app>` or :dokuwiki:`Android <resources/eval/user-guides/eval-adicup3029/smart_app/android_app>` device one of these apps.

Outputting Data
---------------

The data from the accelerometer will be sent over Bluetooth but can also be viewed using a **UART connection**.

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

To establish connection over UART, a micro USB cable connected to the board and a serial console program like `Putty <http://www.putty.org/>`_ are required.

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

.. image:: ../images/capture.png
   :align: center
   :width: 500

Smart Device Output
~~~~~~~~~~~~~~~~~~~

Open up the IoTNode app on your Smart Phone or Tablet.

.. image:: ../images/img_0005.png
   :align: center
   :width: 500

Just press the Scan button on the bottom left corner in order for the app to
start searching for Bluetooth devices.

.. image:: ../images/img_0007.png
   :align: center
   :width: 500

Once the device is visible press connect to access the information provided over **Bluetooth**.

.. image:: ../images/img_0010.png
   :align: center
   :width: 500

After connecting to the device and generating enough G acceleration(**minimum of 10 G** on any axis), information will be displayed on the application. To generate this high value of acceleration you can try and hit the board on your hand ( do not put to much force in order to avoid damages to the device ).

.. tip::

   For more information regarding the mobile application please use the link
   for :doc:`Bluetooth Smart Device Apps </solutions/reference-designs/eval-adicup3029/smart_app>`

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
ADXL372.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_Asset_Health** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt ADXL372 Hex File

   -  `ADuCM3029_Asset_Health.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_Asset_Health.hex>`_

   Complete ADXL372 Source Files

   -  :git-EVAL-ADICUP3029:`ADuCM3029_Asset_Health Source Code <projects/ADuCM3029_Asset_Health>`

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Project Structure
~~~~~~~~~~~~~~~~~

.. image:: ../images/adxl372.png
   :align: center
   :width: 500

The project is structured in 3 layers:

-  Hardware layer - ADXL372
-  Communication layer
-  Application layer - ADuCM3029 and EM9304 BLE

The ADXL372 transmits data to ADuCM3029 controller through the Communication
layer. The data is processed and sent over BLE to a mobile device.

*End of Document*
