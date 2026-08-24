CO Toxic Gas Measurement Demo (with EVAL-CN0357-ARDZ)
=====================================================

The **cn0357_example_noos** is a toxic gas(CO) detector demo project for the EVAL-ADICUP3029 base board with additional :adi:`EVAL-CN0357-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>` shield, created using the CrossCore Embedded Studio environment.

General Description/Overview
----------------------------

This user guide gives a detailed explanation about **cn0357_example_noos** toxic gas (CO) detection project for :doc:`EVAL-ADICUP3029 </solutions/reference-designs/eval-adicup3029/hardware/adicup3029>` base board and :adi:`EVAL-CN0357-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>` gas sensor shield. The gas sensor shield consists of portable gas detector circuit.

.. image:: ../images/picture1.jpg
   :align: center
   :width: 500

The :adi:`EVAL-CN0357-ARDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-CN0357-ARDZ.html>` shield circuit provides a potentiostatic circuit for biasing the electrochemical sensor and 16-bit Sigma-Delta ADC. The small currents passing in the sensor is being converted to a voltage that can be read by the ADC. The 16-bit ADC value is received via SPI interface of the EVAL-ADICUP3029 board, where the gas concentration is computed.

The **cn0357_example_noos** application configures the necessary components, processes ADC output value and make all necessary conversions in order to provide the gas concentration. A UART interface (38400 baud rate and 8-bits data length) is used to send the results to terminal window: CO Concentration in **Parts Per Million(PPM)** are the outputs provided in the terminal window.

At the start of the project, the software computes the necessary parameters and configure the digital rheostat(AD5270) . The required parameters are the sensor sensitivity and feedback resistor range. These can be modified by changing the values of the constants **CN0357_SENSOR_SENSITIVITY** and **CN0357_FEEDBACK_RESISTOR** found in the **adi_cn0357.h** header file of the project.

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0357-ARDZ
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  7V - 12V DC power supply (only if you have Rev B of the CN0357)

-  Software

   -  cn0357_example_noos software

      -  Inside Sensor_Sw Pack (1.0.0 or higher)

   -  CrossCore Embedded Studio (2.6.0 or higher)
   -  ADuCM302x DFP (2.0.0 or higher)
   -  ADICUP3029 BSP (1.0.0 or higher)
   -  Android IoTNode App (optional)

      -  Either Android or iOS version

   -  Serial Terminal Program (Required for running in release mode only)

      -  Such as Putty or Tera Term

Setting up the hardware
-----------------------

-  Make sure that Carbon Monoxide sensor **CO-AX** is properly placed on the **EVAL-CN0357-ARDZ** sensor shield ()
-  Ensure the jumper **AD5720_CS** has a shunt across Pin 3 and Pin 4 of the **EVAL-CN0357-ARDZ**
-  Ensure the jumper **AD7790_CS** has a shunt across Pin 1 and Pin 2 of the **EVAL-CN0357-ARDZ**

.. image:: ../images/jumper_cn0357.png
   :align: center
   :width: 500

-  Place the **(S5)** switch position to read "Wall/USB", and the **(S2)** switch position to read "USB" on the **EVAL-ADICUP3029**.

.. image:: ../images/jumper_ble.png
   :align: center
   :width: 500

-  Mount **EVAL-CN0357-ARDZ** on the **EVAL-ADICUP3029** base board such that **DIGI1** and **DIGI0** of the EVAL-CN0357-ARDZ are connected to the **P6** and **P7** on the EVAL-ADICUP3029 board respectively.
-  Plug in the micro USB cable into the **(P10)** USB port on the **EVAL-ADICUP3029**, and the other end into the PC or laptop.

.. important::

   Extremely important to plug in an acceptable power supply to the barrel jack
   P2 of the EVAL-ADICUP3029 to supply power for the EVAL-CN0357-ARDZ Rev B. The
   boards will not work if you try only to power it from the USB. The external
   power supply is not required for EVAL-CN0357-ARDZ Rev C.

Configuring the Software
------------------------

The CN0357 comes with a carbon monoxide sensor, and those default settings are
programmed into the software. If you decide to use a different type of sensor,
you will need to change the sensor sensitivity and feedback resistor.

In *adi_cn0357.h* header file the user can configure parameters:

-  **CN0357_FEEDBACK_RESISTOR** - CN0357_FEEDBACK_RESISTOR -This is the value that the rheostat needs to be configured to for proper operation (ohms). This value is dervied from equation 2 (located on page 2) on the CN0357 datasheet.

::

       #define CN0357_FEEDBACK_RESISTOR (9230.76)

-  **CN0357_SENSOR_SENSITIVTY** - CN0357_SENSOR_SENSITIVTY - sensitivity (nA/ppm) of the electrochemical sensor being used.

::

       #define CN0357_SENSOR_SENSITIVTY (0.0000000065)

In the *cn0357_app.h* header files you can configure the following parameters:

-  **ADI_APP_DISPATCH_TIMEOUT** - *DISPATCH TIMEOUT* will define how often the data is sent over Bluetooth.
-  **ADI_APP_USE_BLUETOOTH** - *ENABLE BLUETOOTH* parameter - will either use Bluetooth or will have the option to print to console window in debug mode or terminal in release mode.

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0357.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0357** can be found here:

.. admonition:: Download
   :class: download

   Pre-built CN0357 Hex File

   -  `AduCM3029_demo_cn0357.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0357.hex>`_

   Complete CN0357 Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0357 Source Code <projects/ADuCM3029_demo_cn0357>`

Outputting Data
---------------

Once the hardware is setup and software is configured, user needs to select how
they want to view the data coming from the gas sensor(CN0357).

There are **three** different ways to visualize the data:

-  CrossCore Embedded Studio Console Window (through semihosting)
-  Serial Terminal Program (such as Putty or Tera Term)
-  IoTNode Smart Device App

Depending on how you want to operate the board and visualize the data, there are two different options that must be selected from. Below is a table outlining the general operation, and you need to click on which **launch** file you need to program onto the EVAL-ADICUP3029, and hit the **<F5>** key on your keyboard.

|image1|

+---------------------------+-----------------------+---------------------------+
| Data Output Destination   | Connected to Debugger | Configuration File        |
+===========================+=======================+===========================+
| CCES Console Window       | Yes                   | ADICUP3029_Debug.launch   |
+---------------------------+-----------------------+---------------------------+
| PC/Laptop Serial Terminal | No                    | ADICUP3029_Release.launch |
+---------------------------+-----------------------+---------------------------+
| IoTNode Smart App         | Yes                   | ADICUP3029_Debug.launch   |
+---------------------------+-----------------------+---------------------------+
| IoTNode Smart App         | No                    | ADICUP3029_Release.launch |
+---------------------------+-----------------------+---------------------------+

|
| The data for this demo can be viewed in the serial terminal window (via UART) and by connecting to the Analog Devices iOS Smart Device App (for more information and installation directions check out the :doc:`iOS Smart Device App </solutions/reference-designs/eval-adicup3029/smart_app/ios_app>` page) or Android Smart Device App (for more information and installation directions check out the :dokuwiki:`Android Smart Device App <resources/eval/user-guides/eval-adicup3029/smart_app/android_app>` page)

Debug Launch Mode
~~~~~~~~~~~~~~~~~

**Debug launch mode** is used when connected to the debugger. In debug mode, all the outputs are directed to the console window of the CrossCore tools via semihosting. The data is also sent by default to the IoTNode smart app (ADI_APP_USE_BLUETOOTH =1), but can be turned of if desired by setting ADI_APP_USE_BLUETOOTH = 0.

Figure shows when ADI_APP_USE_BLUETOOTH is set to 1, sensor data is sent to the
smart app and printed onto the console.

|image2|

If you have the app installed on your phone, these figure shows the output on
android device.

.. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your
   phone.

   -  Simply open up the IoTNode application on your phone.
   -  "Scan" for nearby demos.
   -  Once you find your demo, click on it to open it up.

-  **Android App display**
-  **iOS App display**

|image3| |image4|

|image5| |image6|

Release Launch Mode
~~~~~~~~~~~~~~~~~~~

**Release launch mode** is used for running without the debugger connected. When in release mode, console output is redirected to UART. Bluetooth is enabled, and sensor data is sent to android application. If disabled, sensor data is directed only to the UART. If you are using the UART to make print to the PC/laptop, here are the settings your TCP client must be set too. Following is the UART configuration.

::

     Select COM Port
     Baud rate: 38400
     Data: 8 bit
     Parity: none
     Stop: 1 bit
     Flow Control: none

Figure shows the UART terminal when ADI_APP_USE_BLUETOOTH is set to 1

.. image:: ../images/disco.png
   :width: 300

**iOS App and Android App display** If you have the app installed on your phone, these figure shows the output on android device.

.. important::

   Do not try to connect directly (or pair) to the EVAL-ADICUP3029 from your
   phone.

   -  Simply open up the IoTNode application on your phone.
   -  "Scan" for nearby demos.
   -  Once you find your demo, click on it to open it up.

-  **Android App display**
-  **iOS App display**

|image7| |image8|

|image9| |image10|

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

A debug configuration must be set up for this project in order to have the possibility to program and to debug the **ADICUP3029_CN0357** project. To do this, follow the instructions from :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

-  Make sure the target board is connected to workstation (via **USB** at P10) and using the tool bar, navigate to the small Debug icon\ |image11| and select the debugging session you created. The application will programmed and the program execution will stop at the beginning of the main() function.

::

     * Use step-by-step execution or directly run the program.

After completion of the steps above the program will be loaded onto the system
FLASH and it will run by default every time the board is powered up.

.. image:: ../images/debug_image.png
   :align: center
   :width: 1000

Project Structure
~~~~~~~~~~~~~~~~~

The **cn0357_example_noos** project use ADuCM302x C/C++ Project structure.

This project contains: system initialization part - disabling watchdog, enabling
clock for peripherals; port configuration for SPI0;SPI2;UART , SPI and UART
initialisation, SPI, UART read/write functions, AD7790 control, AD5270 control
and gas concentration computation, BLE initialization, packet formation and
sending data .

.. image:: ../images/project_struct.png
   :align: left
   :width: 400

The **cn0357_app.cpp** is the application file for the project. The **ADuCM3029** folder consists of pinmux for SPI0, SPI2 and UART0.

The **RTE** folder contains ADuCM3029 Device Family Pack,Board Support Package files and Sensor Config files related to cn0357_example_noos project.

*End of Document*

.. |image1| image:: ../images/adt7420_demo_launch_configurations.png
   :width: 200

.. |image2| image:: ../images/console_image.png
   :width: 600

.. |image3| image:: ../images/appbef.png
   :width: 390

.. |image4| image:: ../images/app.png
   :width: 400

.. |image5| image:: ../images/ipad_connect.png
   :width: 600

.. |image6| image:: ../images/co_val.png
   :width: 600

.. |image7| image:: ../images/appbef.png
   :width: 390

.. |image8| image:: ../images/app.png
   :width: 400

.. |image9| image:: ../images/ipad_connect.png
   :width: 600

.. |image10| image:: ../images/co_val.png
   :width: 600

.. |image11| image:: ../images/bug.png
   :width: 30
