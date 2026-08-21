Turbidity Measurement Demo (with EVAL-CN0409-ARDZ)
==================================================

General description
-------------------

The **EVAL-CN0409-ARDZ** shield is a low to high level water turbidity measurement system in combination with the **EVAL-ADICUP360**. It uses the **ADPD105's** ambient light rejection feature to make it ideal for applications where accurate, robust and non-contact turbidity measurements are critical.

|image1|

Setting up the hardware
-----------------------

-  To program the base board, set the jumpers/switches as shown in the next
   figure. The important jumpers/switches are highlighted in red.

.. image:: ../images/switch_cn0397.jpg
   :align: center
   :width: 600

-  Connect the **EVAL-CN0409-ARDZ** to the Arduino connectors **P2, P5, P6, P7, P8** of the **EVAL-ADICUP360** board.
-  Plug in the USB cable from the PC to the EVAL-ADICUP360 base board via the
   Debug USB.(P14)

Calibration procedure
~~~~~~~~~~~~~~~~~~~~~

When the project is being run for the first time a calibration procedure is
required in order to achieve high accuracy results. The user must follow the
steps described in the UART terminal when the application is started.

The user has the option to modify the solutions that are used for calibrating the device. |image2| Any values can be used for the points that are used for calibration, but a proper distribution along the 0 - 1000 NTU range must be taken into account.

.. note::

   These values can be edited in CN0409.h file inside the include folder within
   the project structure.

After the calibration sequence is done at least once, the calibration
coefficients are saved in the controller flash memory and will be used the next
time when a calibration is not done. The calibration can be repeated as desired.
If the program is run for the first time and a calibration routine is not done,
the program will prompt the user to manually input calibration coefficients.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP360
   -  EVAL-CN0409-ARDZ Evaluation Board
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  Test Vials
   -  Turbidity Calibration Solutions (0.02FTU,100FTU and 800FTU)
   -  Turbidity Solutions (10FTU,15FTU,10FTU,100FTU and 1000FTU)

.. note::

   The turbidity calibration solutions used in the evaluation are the `HI88703-11 <https://hannainst.com/turbidity-calibration-standards-for-hi88703-and-hi83414-hi88703-11.html>`_,\ `Oakton T100 <https://www.coleparmer.com/i/oakton-t100-replacement-turbidity-calibration-kit/3563552>`_ and `Cole Parmer kit <https://www.johnmorrisgroup.com/AU/Product/48740/Cole-Parmer-Turbidity-Standards-Pack>`_\

-  Software

   -  ADuCM360_demo_cn0409 software
   -  CrossCore Embedded Studio (2.7.0 or higher)
   -  ADuCM36x DFP (1.0.2 or higher)
   -  CMSIS ARM Pack (4.3.0 or higher)
   -  Serial Terminal Program

      -  Such as Putty or Tera Term

Setting up the hardware
-----------------------

Test Setup Functional Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/test_setup.jpg

Test Vial Considerations
~~~~~~~~~~~~~~~~~~~~~~~~

To obtain a most accurate results when taking measurements, process below should
take into considerations:

-  Test vials must be meticulously cleaned. Cleaning involves washing the vials with soap and deionized water, soaking the sample vial in Hydrochloric Acid solution, rinsing with ultra-filtered deionized water, and polishing with silicone oil.
-  Test vials must also be indexed. After the cleaning process, the vial is used to measure a very low turbidity solution. The position with the lowest measured turbidity should be indexed and this position should be used for succeeding measurements.
-  Remove bubbles in the solution. This can be done by letting the solution stand for several minutes to allow the bubbles to vacate.
-  If possible, use one properly indexed test vial.

.. note::

   It is recommended to use `LaMotte Test Vial <https://www.coleparmer.com/i/lamotte-0290-6-turbidity-sample-test-tubes-vials-6-pk/0556366>`_ as the size fits into the on board vial holder

Measurement Procedure
---------------------

-  Fill a clean test vial up to 10mL of the solution under test
-  Allow sufficient time for bubbles to escape before placing the cap
-  Wipe the test vial with a lint free cloth before inserting into the on board test vial holder to make sure it is free from fingerprints.
-  Open putty software and hit reset button on EVAL-ADICUP360. Follow on screen
   prompt for the calibration as shown below.

.. image:: ../images/putty1.png

.. note::

   For first time use, it is required to perform calibration by typing y key.
   For the succeeding measurements, just hit n key to skip calibration

-  3-point calibration will perform using 0.02FTU,100 FTU and 800 FTU. Wait for
   the onscreen prompt before placing each solution.

.. image:: ../images/putty2.png

-  After calibration, place the solution required to measure turbidity as
   prompted on the screen.

.. image:: ../images/putty3.png

-  For more details on the software, visit CN0409 Software User Guide.

.. note::

   Make sure you are holding on the test vial cap when placing on the holder

.. image:: ../images/setup.jpg

Obtaining the Source Code
-------------------------

There are two basic ways to program the ADICUP360 with the software for the
CN0409.

-  Dragging and Dropping the .Bin to the MBED drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design.

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM360_demo_cn0409** demo can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0409 Bin File

   
   -  `ADuCM360_demo_cn0409.Bin <https://github.com/analogdevicesinc/EVAL-ADICUP360/releases/download/Release-1.0/ADuCM360_demo_cn0409.bin>`_
   
   Complete CN0409 Source Files
   
   -  :git-EVAL-ADICUP360:`ADuCM360_demo_cn0409 Source Code <projects/ADuCM360_demo_cn0409>`
   

.. note::

   For more information on importing, debugging, or other tools related questions, please see the :doc:`tools user guide. </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>`

Outputting Data
---------------

Serial Terminal Output
~~~~~~~~~~~~~~~~~~~~~~

-  In order to view the data, you must flash the program to the EVAL-ADICUP360.
-  Once complete you will need to switch the USB cable from the DEBUG USB (P14) to the USER USB (P13).
-  Then follow the UART settings below with the serial terminal program.

Following is the UART configuration.

::

     Select COM Port
     Baud rate: 9600
     Data: 8 bit
     Parity: none
     Start: 1 bit
     Stop: 2 bit
     Flow Control: none

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP360 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup360/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studios tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>` section.

Project structure
-----------------

|image3|\ The **ADuCM360_demo_cn0409** is a C++ project that uses ADuCM36x C/C++ Project structure.

This project contains: system initialization part, setting system clock,
enabling clock for peripherals; i2c interface, UART via P0.6/P0.7; UART
read/write functions; Memory read/write functions; turbidity calculations;

In the **src** and **include** folders you will find the source and header files related to CN0409 software application. The *Communication.cpp/h* files contain UART and I2C specific data, meanwhile the *CN0409.cpp/h* files contain the calculation part and *Flash.cpp/h* provide memory management. .

.. |image1| image:: ../images/cn0409.jpg
   :width: 400

.. |image2| image:: ../images/cn0409_default_calibration_values.png
.. |image3| image:: ../images/project.png
   :width: 300
