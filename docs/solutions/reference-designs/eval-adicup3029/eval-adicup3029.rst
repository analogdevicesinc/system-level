.. _eval-adicup3029 eval-adicup3029:

EVAL-ADICUP3029 User Guide
==========================

The :adi:`EVAL-ADICUP3029` is an Arduino Uno form factor compatible platform based on the industry leading ultra low power :adi:`ADuCM3029` 32-bit ARM Cortex™-M3 microcontroller. The platform is designed to be a development and prototyping vehicle to get customer ideas from concept to production with a minimal risk and faster time to market. The :adi:`EVAL-ADICUP3029` is designed for IOT (Internet of Things) applications in mind, and therefore comes with on board Wi-Fi and Bluetooth 5.0 capabilities. A free version of CrossCore Embedded Studio (an Eclipse based Analog Devices Interactive Development Environment) is supplied to the customer for debugging and application development. Add-on hardware modules, MCU drivers and software application examples help form a complete ecosystem that customers can leverage into their final product.

.. image:: images/adicup3029_ecosystem_collage.png
   :align: right
   :width: 500

-  :ref:`Introduction <eval-adicup3029 introduction>`
-  :ref:`Tools and Driver Details <eval-adicup3029 tools>`

   -  :ref:`CrossCore Download & Installation Guide <eval-adicup3029 tools cces_setup_guide>`
   -  :ref:`CrossCore Quickstart User Guide <eval-adicup3029 tools cces_user_guide>`
   -  :ref:`Hardware Drivers, Drag and Drop, and USB Storage Modes <eval-adicup3029 tools adicup3029_hw_drivers>`
   -  :ref:`Unlocking a "Bricked" ADICUP3029 <eval-adicup3029 tools ccsfp_unlock_adicup3029>`
   -  :ref:`Using EVAL-ADICUP3029 with IAR and Keil IDEs <eval-adicup3029 tools keil_iar_support>`

-  :ref:`Hardware Details <eval-adicup3029 hardware>`

   -  :ref:`EVAL-ADICUP3029 Base Board <eval-adicup3029 hardware adicup3029>`
   -  :ref:`EVAL-ADXL362-ARDZ Shield <eval-adicup360 hardware adxl362>`
   -  :ref:`EVAL-ADXL372-ARDZ Shield <eval-adicup3029 hardware adxl372>`
   -  :ref:`EVAL-ADT7420-PMDZ PMOD <eval-adicup360 hardware adt7420>`
   -  :dokuwiki:`EVAL-AD5592R-PMDZ PMOD <resources/eval/user-guides/circuits-from-the-lab/eval-ad5592r-pmdz>`
   -  :dokuwiki:`EVAL-AD5593R-PMDZ PMOD <resources/eval/user-guides/circuits-from-the-lab/eval-ad5593r-pmdz>`
   -  :dokuwiki:`EVAL-AD5770R-PMDZ PMOD <resources/eval/user-guides/circuits-from-the-lab/eval-ad5770r-pmdz>`
   -  :dokuwiki:`EVAL-AD7124-8-PMDZ PMOD <resources/eval/user-guides/circuits-from-the-lab/eval-ad7124-8-pmdz>`
   -  :ref:`EVAL-ADXRS290-PMDZ PMOD <eval_adxrs290_pmdz eval>`
   -  :ref:`EVAL-CN0326-PMDZ PMOD <eval-adicup360 hardware cn0326>`
   -  :ref:`EVAL-CN0357-ARDZ Shield <eval-adicup360 hardware cn0357>`
   -  :ref:`EVAL-CN0397-ARDZ Shield <eval-adicup360 hardware cn0397>`
   -  :ref:`EVAL-CN0398-ARDZ Shield <eval-adicup360 hardware cn0398>`
   -  :ref:`EVAL-CN0410-ARDZ Shield <eval-adicup3029 hardware cn0410>`
   -  :ref:`EVAL-CN0414-ARDZ Shield <eval-adicup3029 hardware cn0414>`
   -  :ref:`EVAL-CN0415-ARDZ Shield <eval-adicup3029 hardware cn0415>`
   -  :ref:`EVAL-CN0418-ARDZ Shield <eval-adicup3029 hardware cn0418>`
   -  :dokuwiki:`EVAL-CN0428-EBZ Shield <resources/eval/user-guides/circuits-from-the-lab/cn0428>`
   -  :dokuwiki:`EVAL-CN0429-EBZ Shield <resources/eval/user-guides/circuits-from-the-lab/cn0429>`
   -  :dokuwiki:`EVAL-CN0503-ARDZ Shield <resources/eval/user-guides/circuits-from-the-lab/cn0503>`
   -  :dokuwiki:`EVAL-CN0507-ARDZ Shield <resources/eval/user-guides/circuits-from-the-lab/cn0507>`
   -  :dokuwiki:`EVAL-CN0510-ARDZ Shield <resources/eval/user-guides/circuits-from-the-lab/cn0510>`
   -  :dokuwiki:`EVAL-CN0531-PMDZ PMOD <resources/eval/user-guides/circuits-from-the-lab/cn0531>`
   -  :dokuwiki:`EVAL-CN0536-ARDZ Shield <resources/eval/user-guides/circuits-from-the-lab/cn0536>`
   -  :dokuwiki:`EVAL-CN0548-ARDZ Shield <resources/eval/user-guides/circuits-from-the-lab/cn0548>`
   -  :dokuwiki:`EVAL-CN0552-PMDZ PMOD <resources/eval/user-guides/circuits-from-the-lab/cn0552>`

-  :ref:`Software Packs and Board Support Packages <eval-adicup3029 software>`

   -  :ref:`ADuCM302x On-Chip Peripheral Drivers and Software <eval-adicup3029 software aducm302x>`
   -  **Deprecated -** :ref:`ADICUP3029 On-Board Peripheral Drivers and Software <eval-adicup3029 software adicup3029>`
   -  **Deprecated -** :ref:`Sensor Application Software Driver Pack <eval-adicup3029 software sensors>`
   -  **Deprecated -** :ref:`Bluetooth Low Energy (BLE) Software Pack <eval-adicup3029 software ble_sw>`
   -  **Deprecated -** :ref:`Wi-Fi Software Pack <eval-adicup3029 software wifi_sw>`

-  :ref:`Bluetooth Smart Device Apps <eval-adicup3029 smart_app>`

   -  **Deprecated -** :ref:`iOS Smart Device Application <eval-adicup3029 smart_app ios_app>`
   -  **Deprecated -** :ref:`Interfacing Data with IoTNode <eval-adicup3029 smart_app ble_connect>`

-  :ref:`Example Projects with Setup Instructions <eval-adicup3029 reference_designs>`

   -  :ref:`Blinking LEDs Demo <eval-adicup3029 reference_designs demo_blink>`
   -  :ref:`Command Line Interpreter Demo <eval-adicup3029 reference_designs demo_cli>`
   -  :ref:`Accelerometer Demo using Wi-Fi (with EVAL-ADXL362-ARDZ) <eval-adicup3029 reference_designs demo_adxl362>`
   -  :ref:`High Impact Detection Demo with Bluetooth (using EVAL-ADXL372-ARDZ) <eval-adicup3029 reference_designs demo_adxl372>`
   -  :ref:`Temperature Demo (with EVAL-ADT7420-PMDZ) <eval-adicup3029 reference_designs demo_adt7420>`
   -  :ref:`Configurable 8-Channel ADC/DAC (with EVAL-AD5592R-PMDZ or EVAL-AD5593R-PMDZ) <eval-adicup3029 reference_designs demo_ad5592r_ad5593r>`
   -  :ref:`8-Channel 24-bit Sigma Delta ADC (with EVAL-AD7124-8-PMDZ) <eval-adicup3029 reference_designs demo_ad7124-8>`
   -  :ref:`Gyroscope CLI Demo (with EVAL-ADXRS290-PMDZ) <eval-adicup3029 reference_designs demo_adxrs290_pmod>`
   -  :ref:`PMOD Accelerometer Demo (with PmodACL2 from Digilent) <eval-adicup3029 reference_designs demo_pmodacl2>`
   -  :ref:`pH Monitor with Temperature Compensation Demo (with EVAL-CN0326-PMDZ) <eval-adicup3029 reference_designs demo_cn0326>`
   -  :ref:`CO Toxic Gas Measurement Demo with Bluetooth (with EVAL-CN0357-ARDZ) <eval-adicup3029 reference_designs demo_cn0357>`
   -  :ref:`Visible Light Detection/Measurement Demo (with EVAL-CN0397-ARDZ) <eval-adicup3029 reference_designs demo_cn0397>`
   -  :ref:`Soil Moisture and pH Measurement Demo using Wi-Fi (with EVAL-CN0398-ARDZ) <eval-adicup3029 reference_designs demo_cn0398>`
   -  :ref:`Programmable 3-Channel LED Driver Demo (with EVAL-CN0410-ARDZ and CFTL-LED-BAR) <eval-adicup3029 reference_designs demo_cn0410>`
   -  :ref:`PLC/DSC Analog Input Module w/HART Demo (with EVAL-CN0414-ARDZ) <eval-adicup3029 reference_designs demo_cn0414>`
   -  :ref:`Robust Solenoid Measurement System Demo (with EVAL-CN0415-ARDZ) <eval-adicup3029 reference_designs demo_cn0415>`
   -  :ref:`PLC/DSC Analog Output Module w/HART Demo (with EVAL-CN0418-ARDZ) <eval-adicup3029 reference_designs demo_cn0418>`
   -  :ref:`Smart Greenhouse Demo with Cloud Connectivity using Wi-Fi (CN0420) <eval-adicup3029 reference_designs smart_greenhouse>`
   -  :dokuwiki:`Water Conductivity and pH Measurement Demo (using EVAL-CN0428-EBZ & EVAL-M355-ARDZ-INT) <resources/eval/user-guides/circuits-from-the-lab/cn0428>`
   -  :dokuwiki:`Electrochemical Gas Measurement Demo (using EVAL-CN0429-EBZ & EVAL-M355-ARDZ-INT) <resources/eval/user-guides/circuits-from-the-lab/cn0429>`
   -  :ref:`Analog I/O System with HART and Modbus Connectivity for PLC/DCS Applications (CN0435) <eval-adicup3029 reference_designs demo_plc_modbus>`
   -  :ref:`Optical Liquid Analysis Measurement Demo (using the EVAL-CN0503-ARDZ) <eval-adicup3029 reference_designs demo_cn0503>`
   -  :dokuwiki:`2-Port Network Analyzer Software (using the EVAL-CN0507-ARDZ) <resources/eval/user-guides/circuits-from-the-lab/cn0507>`
   -  :dokuwiki:`Battery Impedance Measurement Demo (using the EVAL-CN0510-ARDZ) <resources/eval/user-guides/circuits-from-the-lab/cn0510>`
   -  :ref:`UL 217 Smoke Detector Demo (using the EVAL-CN0537-ARDZ) <eval-adicup3029 reference_designs demo_cn0537>`
   -  :ref:`+/- 5V 20-Bit DC Control Demo (using the EVAL-CN0531-PMDZ) <eval-adicup3029 reference_designs demo_cn0531>`
   -  :ref:`Radiation Measurement Demo (using the EVAL-CN0536-ARDZ) <eval-adicup3029 reference_designs demo_cn0536>`
   -  :dokuwiki:`High Voltage and Current Sense Measurement Demo (using the EVAL-CN0548-ARDZ) <resources/eval/user-guides/circuits-from-the-lab/cn0548>`
   -  :dokuwiki:`Extended Range Capacitance Measurement Demo (using the EVAL-CN0552-PMDZ) <resources/eval/user-guides/circuits-from-the-lab/cn0552>`

-  :ref:`Cases, Enclosures, and 3D Printer Files <eval-adicup3029 mechanical>`
-  :ref:`Help and Support <eval-adicup3029 help_and_support>`
-  :ref:`Compliance Testing and Results <eval-adicup3029 compliance_testing_and_results>`
