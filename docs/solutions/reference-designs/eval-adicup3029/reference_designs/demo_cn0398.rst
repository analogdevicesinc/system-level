Soil Moisture and pH Measurement Demo using Wi-Fi
=================================================

The **ADuCM3029_demo_cn0398** is a pH and moisture measurements demo project, for the **EVAL-ADICUP3029** base board with additional **EVAL-CN0398-ARDZ** shield, created using CrossCore Embedded Studio and GNU ARM compiler. The demo uses an **ESP8266 WiFi module** to transmit data to the cloud, by publishing to a MQTT broker.

General Description/Overview
----------------------------

The **ADuCM360_demo_cn0398** project uses the :adi:`EVAL-CN0398-ARDZ <en/design-center/reference-designs/hardware-reference-design/circuits-from-the-lab/cn0398.html>` shield which is a single supply, low power, high precision complete solution for soil moisture and pH measurements, including temperature compensation. The circuit is optimized for capacitive soil moisture sensors that are insensitive to water salinity and do not corrode over time. The circuit also measures soil pH so it increases the range of applications where this shield can be used.

The circuit is divided into three independent measurement front ends: pH, soil moisture, and temperature. After signal conditioning, the three channels share an :adi:`AD7124-8 <en/products/analog-to-digital-converters/precision-adc-20msps/ad7124-8.html>`, 24-bit sigma-delta (Σ-Δ) ADC. The **AD7124-8**, is a low power, low noise, completely integrated analog front end for high precision measurement applications. The board offers the possibility to configure **Vin** supply voltage (**P10** connector) in order to use **5V** or **7V-12V**. Considering moisture sensor which is used, the **P8** connector configure **3.3V** or **5V** supply.\ |image1| The user has the possibility to select one of the three GPIOs available for ADC CS pin using **P5** connector (default configuration for **P5** is 1-2 position). For temperature compensation can be used an RTD *PT100* sensor, 2-wire (this is used in the demo), 3-wire or 4-wire connection (see **P1** connector). For this demo was used for the moisture measurement the *VH400* sensor (**P2**) and for pH measurement *Atlas Scientific* sensor (**J1**). The **ADuCM360_demo_cn0398** application processes ADC outputs for all 3 channels (RTD, pH and moisture), calculates pH and moisture values using as input RTD temperature value. This data is sent to cloud using the **UART** module on the base board and the **ESP8266 WiFi module**. The 24-bits **ADC** data are received using **SPI** interface of the **EVAL-ADICUP3029** board.

The **temperature** value is calculated based on the **RTD resistance**:

::

                                                                  CODE - ADC output
                                                                  Rrtd = ((CODE - 2^23)* Rref)/GAIN\*2^23                  Rref - Reference resistor (5kΩ)
                                                                  GAIN - used gain for RTD channel (16)

**1. RTD resistance > 100Ω**

.. image:: ../images/cn0398_demo_1.png
   :width: 800

**2. RTD resistance ≤ 100Ω**

.. image:: ../images/cn0398_demo_2.png
   :width: 800

The **pH** value can be calculated in two ways, so user can configure which one did he want for his application: using *two-point calibration* data or using *Nernst equation*. The pH value will be calculated using calibration measured value:

::

                                                       y1 - measured voltage at calibration point 1 for known pH
                                                       y2 - measured voltage at calibration point 2 for known pH
                                                       pH = [m*(V -y2 + Voffset) + x2]             x1 - known pH at calibration point 1
                                                       x2 - known pH at calibration point 2
                                                       m  = [(x2-x1)/(y2-y1)]                      V - pH channel measured voltage
                                                       Voffset - Offset voltage

A default calibration package can be loaded (in case is not wanted to perform calibration everytime). For this is needed to update **default_calibration_ph** array with known values before the board is program. In case the *two-point calibration* is not wanted, for pH calculation is used *Nernst equation*:

::

         ph  = [PH_ISO -((V - a) / ((2.303 * AVOGADRO * (T + 273.1))]

         PH_ISO - reference hydrogen ion concentration (7)
         V - pH channel measured voltage
         a - zero point tolerance (see *ZERO_POINT_TOLERANCE* parameter)
         AVOGADRO - Avogadro's number (8.314)
         T - RTD temperature

The **moisture** value can be also calculated in two ways. First way is to use *piece-wise formulas* given by manufacturer (check *USE_MANUFACTURER_MOISTURE_EQ* parameter. For **Vegetronix** may use the follow formulas (*m* - moisture value and *Vm* - moisture channel measured voltage):

================= ======================
**Voltage Range** **Equation**
================= ======================
0V - 1.1V         m = 10 \* Vm - 1
1.1V - 1.3V       m = 25 \* Vm - 17.5
1.3V - 1.82V      m = 48.08 \* Vm - 47.5
1.82V - 2.2V      m = 26.32 \* Vm - 7.89
================= ======================

Otherwise the moisture value can be calculated using *transfer function* for the sensor:

::

   m =-1.18467 + 21.5371\*Vm - 110.996\*Vm^2 + 397.025\*Vm^3 - 666.986\*Vm^4 + 569.236\*Vm^5 -246.005\*Vm^6 + 49.4867\*Vm^7 -3.37077\*Vm^8

Demo Requirements
-----------------

The following is a list of items needed in order to replicate this demo.

-  Hardware

   -  EVAL-ADICUP3029
   -  EVAL-CN0398-ARDZ
   -  pH probe with BNC connector
   -  Analog Moisture sensor
   -  PT100 RTD Probe
   -  Mirco USB to USB cable
   -  PC or Laptop with a USB port
   -  ESP8266 WiFi module

-  Software

   -  ADuCM360_demo_cn0398 software
   -  CrossCore Embedded Studio (2.7.0 or higher)
   -  ADuCM302x DFP (1.0.2 or higher)
   -  CMSIS ARM Pack (4.3.0 or higher)
   -  MQTT broker (ex. Mosquitto)

Setting up the Hardware
-----------------------

-  Make sure the **S2** switch on the board is set on position **3**\ (**WiFi**).

.. image:: ../images/adicup3029_switch.png
   :align: center
   :width: 700

-  Plug in the ESP8266 module in the **P1** connector.

.. image:: ../images/adicup3029_esp8266.png
   :align: center
   :width: 700

-  The ESP8266 Enable Pin needs to be tied directly to 3.3V or pulled high to
   the GPIO via a 10K ohm resistor. Because this is not currently on the Rev B
   or Rev C version of the ADICUP3029, you will need to solder a small fly wire
   from the 3.3V pin to the enable pin.
   |image2|\ |image3|
   \* Connect the **EVAL-CN0398-ARDZ** shield to the board.
-  Connect the pH sensor to the **J1** connector of the EVAL-CN0398-ARDZ.
-  Connect the RTD sensor to the **P1** connector of the EVAL-CN0398-ARDZ.\ :dokuwiki:`(see connection details) <resources/eval/user-guides/eval-adicup360/hardware/cn0398>`
-  Connect the moisture sensor to the **P2** connector of the EVAL-CN0398-ARDZ.\ :dokuwiki:`(see connection details) <resources/eval/user-guides/eval-adicup360/hardware/cn0398>`
-  Set the jumpers on the **EVAL-CN0398-ARDZ** to the position shown below.(**P8 SENSOR** to **3.3V**; **VIN SUPPLY** to **5V**; **P5** to **10 on DIG11**)

.. image:: ../images/cn0398_jumper_positions.jpg
   :align: center
   :width: 700

-  Connect the board to the PC via Micro-USB to USB cable.

.. important::

   Extremely important to plug in an acceptable power supply to the barrel jack
   P2 of the EVAL-ADICUP3029 if you are using a moisture sensor that requires
   voltage excitation greater than 5V on the EVAL-CN0398-ARDZ. Only moisture
   sensors using less than 3.3V can run off the USB power option.

Configuring the Software
------------------------

-  **ESP8266.c/h** is the ESP8288 Library which uses AT commands and UART to communicate with the WiFi module. In **ADuCM3029_demo_cn0398.h** you should set your Wi-Fi connection and MQTT information:

::

   /* SSID of the access point. */
   uint8_t aWifiSSID[] = "***";

   /* Password of the access point. */
   uint8_t aWifiPassword[] = "***";

   /* IP address of the broker to publish to. */
   uint8_t aMQTTBrokerIp[] = "***";

-  The ones with a default value can be changed or left as they are:

::

   /* Port of the broker to publish to. */
   uint8_t aMQTTBrokerPort[] = "1883";

   /*! MQTT publisher name. */
   uint8_t aMQTTPublisherName[] = "device_publisher";

   uint8_t aMQTTTopicName[] = "cn0398";

   uint8_t aMQTTTopic[] = "comm_channel";

   /*! MQTT publish packet quality of service. */
   #define ADI_WIFI_MQTT_PUBLISER_QOS (0u)

Using an MQTT Broker
--------------------

The program connects to a WiFi network and to a TCP MQTT broker. After receiving the *SUBACK* confirmation from the server, the program starts by asking the user for calibration details through MQTT publishes on *cn0398* topic(default, can be changed). The messages can be answered by a publish to the *comm_channel* topic(default, can be changed), to which the application is subscribed. After the calibration sequence the program enters an infinite loop in which it waits for 500 ms then outputs instantaneous values of the measured temperature, pH and moisture. This data can also be seen with a subscriber to the *cn0398* topic.

Installing the Mosquitto Broker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example uses the `Eclipse Mosquitto <https://mosquitto.org>`_ which is an open source (EPL/EDL licensed) message broker that implements the MQTT protocol versions 3.1 and 3.1.1. However, the user is free to use his favorite MQTT broker with minimal changes. MQTT provides a lightweight method of carrying out messaging using a publish/subscribe model. This makes it suitable for "Internet of Things" messaging such as with low power sensors or mobile devices such as phones, embedded computers or microcontrollers.

.. hint::

   Alternatively, there is an additional step-by-step procedure written which can be used in combination with the steps outlined below. The combination of both procedures should be enough to get most PC/laptops working.\ `Installing and Configuring Mosquitto <https://sivatechworld.wordpress.com/2015/06/11/step-by-step-installing-and-configuring-mosquitto-with-windows-7/>`_

-  `Download mosquitto <https://mosquitto.org/download/>`_
-  Double click the downloaded .exe file, and install the Mosquitto program
-  During the install, Mosquitto will ask you to make sure you have 2 other programs installed.
-  Click the links within the Windows install wizard **BEFORE** completing the Mosquitto install.

   -  `OpenSSL <http://slproweb.com/products/Win32OpenSSL.html>`_

      -  :dokuwiki:`pthreads <ftp/sources.redhat.com/pub/pthreads-win32/dll-latest/dll/x86>`

-  Make sure these additional programs are installed before you continue
-  Click next and finish the installation.

   -  You may run into an issue that says "VCRUNTIME140.dll is missing. In order
      to proceed you must first have this installed.

.. image:: ../images/reference_design_vcruntime_dll_missing.png
   :align: center
   :width: 600

-  After looking around, I found a great website to download the DLL files from, as well as a great video that shows you have to fix the issue, and it did work for me. *Please note, that this solution is **NOT** affiliated with Analog Devices, and Analog Devices assumes no responsibility for any problems or damages occurred during this process.*
-  `How to fix VCRUNTIME140.DLL Missing Video <https://www.youtube.com/watch?v=-R3LuYNQf98>`_
-  `VCRUNTIME140.DLL Download <http://www.sts-tutorial.com/sites/downloadCenter.php?vcruntime140>`_
-  Re-Run the Mosquitto.exe file, inorder to complete the installation process.

Setting up Mosquitto to Receive MQTT Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  With Mosquitto and other software properly installed, you should be able to run mosquitto. Open a Command Prompt and navigate to the folder where mosquitto is installed. The default location is C:\\Program Files (x86)\\mosquitto. In this case it was installed in C:\\MosquittoMQTT.
-  Type mosquitto.exe -v to start the broker in verbose mode. The code may look
   like this: <code> C:\\MosquittoMQTT>mosquitto.exe -v </code> It should look
   like the following picture

.. image:: ../images/cn0398_open_mqtt_broker.png
   :align: left

.. important::

   Make sure that your computer or laptop is connected to the same network you
   are going to configure in the ADuCM_demo_cn0398.h file. Once you run the
   executable, Mosquitto assumes that you are running on that network.

-  The mosquitto broker is now running locally and has the same IP as your machine and by default runs on port 1883. Open a new Command Prompt and type **ipconfig** to get your local IP address
-  In the **ADuCM_demo_cn0398.h** header file you need to configure the following parameters: ``/* SSID of the access point. */
   uint8_t aWifiSSID[] = "***";
   /* Password of the access point. */
   uint8_t aWifiPassword[] = "***";
   /* IP address of the broker to publish to. */
   uint8_t aMQTTBrokerIp[] = "***";
   /* Port of the broker to publish to. */
   uint8_t aMQTTBrokerPort[] = "1883";``
-  Open a third Command Prompt and navigate to the folder where mosquitto is
   installed and type this command and hit the <ENTER> key:<code>
   C:\\MosquittoMQTT>mosquitto_sub.exe -t cn0398 </code> This command subscribes
   to the topic and will display the cn0398 data. It should look similar to the
   image below.

.. image:: ../images/cn0398_mqtt_subscriber.png
   :align: left

Outputting Data
---------------

-  You are now ready to flash the program on the ADICUP3029 and run it. Before downloading the code, please press the **WIFI_RESET** button (**S4**) on the **ADICUP3029**.
-  If everything works fine you should see the calibration prompt on the **MQTT subscriber** to the *cn0398* topic. Use publisher commands to publish on the *comm_channel* to communicate with the application. To input commands with the publisher use a **Command Prompt** to navigate to **Mosquitto** install folder and input code that looks like this: <code> C:\\MosquittoMQTT>mosquitto_pub.exe -m y -t comm_channel </code>
-  A calibration sequence should look like this:

.. image:: ../images/cn0398_calibration.png
   :align: center

-  After the calibration sequence the program will start to publish data that can be seen with a **MQTT subscriber** to the *cn0398* topic.

|image4|

.. image:: ../images/cn0398_cces_good_console_1.png
   :align: center

Obtaining the Software
----------------------

There are two basic ways to program the ADICUP3029 with the software for the
CN0398.

-  Dragging and Dropping the .Hex to the Daplink drive
-  Building, Compiling, and Debugging using CCES

Using the drag and drop method, the software is going to be a version that
Analog Devices creates for testing and evaluation purposes. This is the EASIEST
way to get started with the reference design

Importing the project into CrossCore is going to allow you to change parameters
and customize the software to fit your needs, but will be a bit more advanced
and will require you to download the CrossCore toolchain.

The software for the **ADuCM3029_demo_cn0398** can be found here:

.. admonition:: Download
   :class: download

   Prebuilt CN0398 Hex File

   -  `AduCM3029_demo_cn0398.Hex <https://github.com/analogdevicesinc/EVAL-ADICUP3029/releases/download/Latest/ADuCM3029_demo_cn0398.hex>`_

   Complete CN0398 Source Files

   -  :git-EVAL-ADICUP3029:`AduCM3029_demo_cn0398 Source Code <projects/ADuCM3029_demo_cn0398>`

How to use the Tools
--------------------

The official tool we promote for use with the EVAL-ADICUP3029 is CrossCore Embedded Studio. For more information on downloading the tools and a quick start guide on how to use the tool basics, please check out the :doc:`Tools Overview page. </solutions/reference-designs/eval-adicup3029/tools>`

Importing
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to import existing projects into your workspace </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

Debugging
~~~~~~~~~

For more detailed instructions on importing this application/demo example into the CrossCore Embedded Studio tools, please view our :doc:`How to configure the debug session </solutions/reference-designs/eval-adicup3029/tools/cces_user_guide>` section.

.. |image1| image:: ../images/cn0398_demo_shield_front_sensors_attached_adicup3029.jpg
   :width: 600

.. |image2| image:: ../images/reference_design_esp8266_hw_mod_back.png
   :width: 400

.. |image3| image:: ../images/reference_design_esp8266_hw_mod_front.png
   :width: 385

.. |image4| image:: ../images/cn0398_data.png
