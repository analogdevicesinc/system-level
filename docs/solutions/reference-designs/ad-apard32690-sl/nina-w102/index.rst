NINA-W102 Networking Support
============================

The following document describes how to build and flash firmware for boards with the NINA-W102 WiFi module. As an example, it will use the :adi:`MAX32690 Arduino Form-Factor Board <AD-APARD32690-SL>`.
It will also describe how to build and  flash the Zephyr Wifi sample to work with this board once the NINA-W102 has been flashed.

Some familiarity with Zephyr and building / flashing Zephyr applications is assumed. If you are new to Zephyr, please start with the Getting Started Guide:
https://docs.zephyrproject.org/latest/develop/getting_started/index.html

WiFi
----
The wifi chip on the AD-APARD32690 is a uBlox NINA-W102 "Open CPU" Wifi/Bluetooth module.  The modules is based on an ESP32 chip, with "Open CPU" meaning it does NOT come preloaded with firmware from uBlox, but rather is intended for customers to develop their own firmware to run on it.

Details of the chip: https://www.u-blox.com/en/product/nina-w10-series-open-cpu

Software must be developed using the ESP32 SDK: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html

Core ESP32 Device:  ESP32-D0WDQ6-V3


Pre-Built Firmware for ESP NINA-W102
------------------------------------
ESP provides pre-built firmware for integrating Wifi and BLE through AT commands.  This can be found here: https://www.espressif.com/en/products/sdks/esp-at/overview. There is also a Zephyr driver for this firmware to make it look like generic Wifi here: https://github.com/zephyrproject-rtos/zephyr/tree/main/drivers/wifi/esp_at and a block talking about using the AT Firmware with Zephyr for a specific ESP32 module: https://blog.golioth.io/esp32-esp-at-enables-connectivity-on-any-zephyr-project/.

However, the pre-built firmware is for ESP32 development boards which have a different pin out than the NINA-W102.  Instructions are provided (https://docs.espressif.com/projects/esp-at/en/latest/esp32/Compile_and_Develop/How_to_set_AT_port_pin.html) describing how to change the port pins for the firmware image.


Building NINA-W102 Firmware
---------------------------

Before proceeding, ensure that P50 and P55 on the APARD32690 board are in position 1-2 if you are trying to get the NINA-W102 UART data through the SWD connector. Be sure to switch this back later for testing the Zephyr application.

The following instructions mostly come from this document:
https://docs.espressif.com/projects/esp-at/en/latest/esp32/Compile_and_Develop/How_to_clone_project_and_compile_it.html

Install the ESP SDK: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html

Open the ESP-IDF Command Prompt and run the following steps:

1. Get the project:

   .. code-block:: bash

      git clone --recursive https://github.com/espressif/esp-at.git

2. Run the builder:  python build.py install
    * Select PLATFORM_ESP32
    * Select module ESP32-D2WD as it has the same flash size as the NINA-W102, making it easier to configure
    * When asked about silent mode, select Y.  Otherwise, if silent mode is not enable, you'll need to set the compiler options later to Optimize for Size to get it to fit
3. Edit the components/customized_partitions/raw_data/factory_param_data.csv file so the D2WD line reads the following:
    ::

       PLATFORM_ESP32,ESP32-D2WD,"2MB flash, No OTA",4,78,0,1,13,CN,115200,1,3,-1,-1,0

4. Build the project by running python build.py build
5. The complete firmware image is located in build\factory\factory_ESP32-<device>.bin and can be archived for later loading of devices.


Programming the NINA-W102 on AD-APARD32690
------------------------------------------
A USB-UART adapter will be needed. A good one can be found here if needed:
https://ftdichip.com/products/ttl-232r-3v3/

1. Connect a USB-UART adapter to the NINA-W102 through P38-2 and P56-2, and a ground on P2 or P5
2. Prior to powering up the board, pull the ESP32 SYS_BOOT pin low, but connecting P47 to ground
3. Power up the board.  You can verify the bootloader started correctly by observing the USB-UART adapter in a terminal.  There should be text similar to the following:

   .. code-block:: text

     rst:0x1 (POWERON_RESET),boot:0x23 (DOWNLOAD_BOOT(UART0/UART1/SDIO_REI_REO_V2))
     waiting for download

4. From the ESP command line, run :code:`python build.py -p <COMPORT> flash`. The flash operation should be performed
Depending on the integrity of the cables (bad jumper wires, etc), you may be have to add the -b 115200 forced slower baud rate for data integrity.


Standalone Programming
----------------------
The NINA-W102 device may be flashed using the stand alone ESP Flash download tool without needing to install the full SDK.

Follow the instructions in the previous section up through step 3, then consult the ESP-AT Downloading guide for using the Flash Download Tool on Windows. Selecting the combined factory firmware image, as described above.
https://docs.espressif.com/projects/esp-at/en/latest/esp32/Get_Started/Downloading_guide.html#flash-at-firmware-into-your-device

AT Command Verification
-----------------------
The AT command set can be found here: https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Command_Set/index.html.  Some basic AT commands can be done to verify the part is programmed correctly:

.. code-block::

   AT

   OK
   AT+GMR
   AT version:4.1.0.0-dev(eb730f6 - ESP32 - Jan  3 2024 08:18:49)
   SDK version:v5.0.4-dirty
   compile time(899230b2):Jan 14 2024 17:16:03
   Bin version:v3.2.0.0(ESP32-D2WD)

   OK
   AT+CWINIT=1

   OK
   AT+CWMODE=1

   OK
   AT+CWLAP
   +CWLAP:(3,"MySSID",-74,"94:a6:7e:e3:b8:38",10,-1,-1,4,4,7,1)
   OK

Finished code block

Integrating Into Zephyr
-----------------------

Create files in your Zephyr workspace called `apard_wifi.conf` and `apard_wifi.overlay`.

Next, place the text below in these files:

apard_wifi.overlay
++++++++++++++++++
.. code-block:: dts
   :name: apard_wifi.overlay


   &uart2a_tx_p1_10 {
        power-source = <1>;
   };

   &uart2a_rx_p1_9 {
        power-source = <1>;
   };

   &uart2 {
       pinctrl-0 = <&uart2a_tx_p1_10 &uart2a_rx_p1_9>;
       pinctrl-names = "default";
       current-speed = <115200>;
       status = "okay";

       esp_wifi: esp-wifi {
           compatible = "espressif,esp-at";
           status = "okay";
       };
   };

   / {
       aliases {
           wifi0 = &esp_wifi;
       };
   };

apard_wifi.conf
+++++++++++++++

.. code-block::
   :name: apard_wifi.conf

   # Enable WiFi via ESP-AT
   CONFIG_WIFI=y
   CONFIG_WIFI_ESP_AT=y
   CONFIG_WIFI_ESP_AT_MDM_RX_BUF_COUNT=40

   # Disable NET_L2_ETHERNET to avoid T1L PHY errors
   # when not using T1L, but enabling net-if
   CONFIG_NET_L2_ETHERNET=n

   # Increment max IPV4 count if using multiple net-if interfaces
   CONFIG_NET_IF_MAX_IPV4_COUNT=2

Build your application as below:

.. shell::
   :no-path:

   $west build -p auto -b apard32690//m4 zephyr/samples/net/wifi/shell -- \
   $    -DDTC_OVERLAY_FILE=$PWD/apard_wifi.overlay -DEXTRA_CONF_FILE=$PWD/apard_wifi.conf

Flash the application using a Segger JLink as below:

.. shell::
   :no-path:

   $west flash -r jlink

At this point, make sure that P55 and P50 on the APARD32690 board are in positions 2-3 to get UART data from the MAX32690.

Testing
-------

At this point, make sure that P55 and P50 on the APARD32690 board are in positions 2-3 to get UART data from the MAX32690. Connect to a terminal application with 115200 baud, 8-N-1 UART settings. Make sure that P56 and P38 are also connected.
The Zephyr Wifi sample application comes with a Wifi shell for doing basic Wifi interactions.  After launching the scan, and connect commands were used to successfully connect to an AP via the Zephyr network subsystem.

Verify the devices installed with `device list`:

.. shell::

     *** Booting Zephyr OS build zephyr-v3.5.0-4086-g0a8d03b95f84 ***
    $device list
     devices:
     - rcc@40021000 (READY)
     - reset-controller (READY)
     - interrupt-controller@40010400 (READY)
     - gpio@48001800 (READY)
     - gpio@48001400 (READY)
     - gpio@48001000 (READY)
     - gpio@48000c00 (READY)
     - gpio@48000800 (READY)
     - gpio@48000400 (READY)
     - gpio@48000000 (READY)
     - rng@50060800 (READY)
     - serial@40008000 (READY)
     - serial@40013800 (READY)
     - esp-wifi (READY)

Request a wifi scan with wifi scan:

.. shell::

    $wifi scan
     Scan requested

     Num  | SSID         (len) | Chan (Band)   | RSSI | Security  | BSSID | MFP
     1    | MySSID       9     | 10   (2.4GHz) | -70  | WPA2-PSK  |       | Disable
     Scan request done

Connect to a Wifi Access Point with `wifi connect`.  Note PSK was omitted in the following terminal log:

.. shell::

    $wifi connect "MySSID" 1 ****PSK HERE****
     Connection requested
     Connected

Get status information with `wifi status`:

.. shell::

    $wifi status
     Status: successful
     ==================
     State: COMPLETED
     Interface Mode: STATION
     Link Mode: UNKNOWN
     SSID: MySSID
     BSSID: <__:__:__:__:__:__>
     Band: 2.4GHz
     Channel: 10
     Security: UNKNOWN
     MFP: UNKNOWN
     RSSI: -69
     Beacon Interval: 0
     DTIM: 0
     TWT: Not supported

