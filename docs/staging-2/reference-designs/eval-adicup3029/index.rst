.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup3029

.. _eval-adicup3029:

EVAL-ADICUP3029 User Guide
==========================

The :adi:`EVAL-ADICUP3029` is an Arduino Uno form factor compatible platform
based on the industry leading ultra low power :adi:`ADuCM3029` 32-bit ARM
Cortex™-M3 microcontroller. The platform is designed to be a development and
prototyping vehicle to get customer ideas from concept to production with a
minimal risk and faster time to market. The :adi:`EVAL-ADICUP3029` is designed
for IOT (Internet of Things) applications in mind, and therefore comes with on
board Wi-Fi and Bluetooth 5.0 capabilities. A free version of CrossCore Embedded
Studios (an Eclipse based Analog Devices Interactive Development Environment) is
supplied to the customer for debugging and application development. Add-on
hardware modules, MCU drivers and software application examples help form a
complete ecosystem that customers can leverage into their final product.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup3029/adicup3029_ecosystem_collage.png
   :width: 500px

#. :dokuwiki:`Introduction <eval-adicup3029/introduction>`
#. :dokuwiki:`Tools and Driver Details <eval-adicup3029/tools>`

   #. :dokuwiki:`CrossCore Download & Installation Guide <eval-adicup3029/tools/cces_setup_guide>`
   #. :dokuwiki:`CrossCore Quickstart User Guide <eval-adicup3029/tools/cces_user_guide>`
   #. :dokuwiki:`Hardware Drivers, Drag and Drop, and USB Storage Modes <eval-adicup3029/tools/adicup3029_hw_drivers>`
   #. :dokuwiki:`Unlocking a "Bricked" ADICUP3029 <eval-adicup3029/tools/ccsfp_unlock_adicup3029>`
   #. :dokuwiki:`Using EVAL-ADICUP3029 with IAR and Keil IDEs <eval-adicup3029/tools/keil_iar_support>`

#. :dokuwiki:`Hardware Details <eval-adicup3029/hardware>`

   #. :dokuwiki:`EVAL-ADICUP3029 Base Board <eval-adicup3029/hardware/adicup3029>`
   #. :dokuwiki:`EVAL-ADXL362-ARDZ Shield <eval-adicup360/hardware/adxl362>`
   #. :dokuwiki:`EVAL-ADXL372-ARDZ Shield <eval-adicup3029/hardware/adxl372>`
   #. :dokuwiki:`EVAL-ADT7420-PMDZ PMOD <eval-adicup360/hardware/adt7420>`
   #. :dokuwiki:`EVAL-AD5592R-PMDZ PMOD <circuits-from-the-lab/eval-ad5592r-pmdz>`
   #. :dokuwiki:`EVAL-AD5593R-PMDZ PMOD <circuits-from-the-lab/eval-ad5593r-pmdz>`
   #. :dokuwiki:`EVAL-AD5770R-PMDZ PMOD <circuits-from-the-lab/eval-ad5770r-pmdz>`
   #. :dokuwiki:`EVAL-AD7124-8-PMDZ PMOD <circuits-from-the-lab/eval-ad7124-8-pmdz>`
   #. :dokuwiki:`EVAL-ADXRS290-PMDZ PMOD <circuits-from-the-lab/eval-adxrs290-pmdz>`
   #. :dokuwiki:`EVAL-CN0326-PMDZ PMOD <eval-adicup360/hardware/cn0326>`
   #. :dokuwiki:`EVAL-CN0357-ARDZ Shield <eval-adicup360/hardware/cn0357>`
   #. :dokuwiki:`EVAL-CN0397-ARDZ Shield <eval-adicup360/hardware/cn0397>`
   #. :dokuwiki:`EVAL-CN0398-ARDZ Shield <eval-adicup360/hardware/cn0398>`
   #. :dokuwiki:`EVAL-CN0410-ARDZ Shield <eval-adicup3029/hardware/cn0410>`
   #. :dokuwiki:`EVAL-CN0414-ARDZ Shield <eval-adicup3029/hardware/cn0414>`
   #. :dokuwiki:`EVAL-CN0415-ARDZ Shield <eval-adicup3029/hardware/cn0415>`
   #. :dokuwiki:`EVAL-CN0418-ARDZ Shield <eval-adicup3029/hardware/cn0418>`
   #. :dokuwiki:`EVAL-CN0428-EBZ Shield <circuits-from-the-lab/cn0428>`
   #. :dokuwiki:`EVAL-CN0429-EBZ Shield <circuits-from-the-lab/cn0429>`
   #. :dokuwiki:`EVAL-CN0503-ARDZ Shield <circuits-from-the-lab/cn0503>`
   #. :dokuwiki:`EVAL-CN0507-ARDZ Shield <circuits-from-the-lab/cn0507>`
   #. :dokuwiki:`EVAL-CN0510-ARDZ Shield <circuits-from-the-lab/cn0510>`
   #. :dokuwiki:`EVAL-CN0531-PMDZ PMOD <circuits-from-the-lab/cn0531>`
   #. :dokuwiki:`EVAL-CN0536-ARDZ Shield <circuits-from-the-lab/cn0536>`
   #. :dokuwiki:`EVAL-CN0548-ARDZ Shield <circuits-from-the-lab/cn0548>`
   #. :dokuwiki:`EVAL-CN0552-PMDZ PMOD <circuits-from-the-lab/cn0552>`

#. :dokuwiki:`Software Packs and Board Support Packages <eval-adicup3029/software>`

   #. :dokuwiki:`ADuCM302x On-Chip Peripheral Drivers and Software <eval-adicup3029/software/aducm302x>`
   #. **Deprecated -**
      :dokuwiki:`ADICUP3029 On-Board Peripheral Drivers and Software <eval-adicup3029/software/adicup3029>`
   #. **Deprecated -**
      :dokuwiki:`Sensor Application Software Driver Pack <eval-adicup3029/software/sensors>`
   #. **Deprecated -**
      :dokuwiki:`Bluetooth Low Energy (BLE) Software Pack <eval-adicup3029/software/ble_sw>`
   #. **Deprecated -**
      :dokuwiki:`Wi-Fi Software Pack <eval-adicup3029/software/wifi_sw>`

#. :dokuwiki:`Bluetooth Smart Device Apps <eval-adicup3029/smart_app>`

   #. **Deprecated -**
      :dokuwiki:`iOS Smart Device Application <eval-adicup3029/smart_app/ios_app>`
   #. **Deprecated -**
      :dokuwiki:`Interfacing Data with IoTNode <eval-adicup3029/smart_app/ble_connect>`

#. :dokuwiki:`Example Projects with Setup Instructions <eval-adicup3029/reference_designs>`

   #. :dokuwiki:`Blinking LEDs Demo <eval-adicup3029/reference_designs/demo_blink>`
   #. :dokuwiki:`Command Line Interpreter Demo <eval-adicup3029/reference_designs/demo_cli>`
   #. :dokuwiki:`Accelerometer Demo using Wi-Fi (with EVAL-ADXL362-ARDZ) <eval-adicup3029/reference_designs/demo_adxl362>`
   #. :dokuwiki:`High Impact Detection Demo with Bluetooth (using EVAL-ADXL372-ARDZ) <eval-adicup3029/reference_designs/demo_adxl372>`
   #. :dokuwiki:`Temperature Demo (with EVAL-ADT7420-PMDZ) <eval-adicup3029/reference_designs/demo_adt7420>`
   #. :dokuwiki:`Configurable 8-Channel ADC/DAC (with EVAL-AD5592R-PMDZ or EVAL-AD5593R-PMDZ) <eval-adicup3029/reference_designs/demo_ad5592r_ad5593r>`
   #. :dokuwiki:`8-Channel 24-bit Sigma Delta ADC (with EVAL-AD7124-8-PMDZ) <eval-adicup3029/reference_designs/demo_ad7124-8>`
   #. :dokuwiki:`Gyroscope CLI Demo (with EVAL-ADXRS290-PMDZ) <eval-adicup3029/reference_designs/demo_adxrs290_pmod>`
   #. :dokuwiki:`PMOD Accelerometer Demo (with PmodACL2 from Digilent) <eval-adicup3029/reference_designs/demo_pmodacl2>`
   #. :dokuwiki:`pH Monitor with Temperature Compensation Demo (with EVAL-CN0326-PMDZ) <eval-adicup3029/reference_designs/demo_cn0326>`
   #. :dokuwiki:`CO Toxic Gas Measurement Demo with Bluetooth (with EVAL-CN0357-ARDZ) <eval-adicup3029/reference_designs/demo_cn0357>`
   #. :dokuwiki:`Visible Light Detection/Measurement Demo (with EVAL-CN0397-ARDZ) <eval-adicup3029/reference_designs/demo_cn0397>`
   #. :dokuwiki:`Soil Moisture and pH Measurement Demo using Wi-Fi (with EVAL-CN0398-ARDZ) <eval-adicup3029/reference_designs/demo_cn0398>`
   #. :dokuwiki:`Programmable 3-Channel LED Driver Demo (with EVAL-CN0410-ARDZ and CFTL-LED-BAR) <eval-adicup3029/reference_designs/demo_cn0410>`
   #. :dokuwiki:`PLC/DSC Analog Input Module w/HART Demo (with EVAL-CN0414-ARDZ) <eval-adicup3029/reference_designs/demo_cn0414>`
   #. :dokuwiki:`Robust Solenoid Measurement System Demo (with EVAL-CN0415-ARDZ) <eval-adicup3029/reference_designs/demo_cn0415>`
   #. :dokuwiki:`PLC/DSC Analog Output Module w/HART Demo (with EVAL-CN0418-ARDZ) <eval-adicup3029/reference_designs/demo_cn0418>`
   #. :dokuwiki:`Smart Greenhouse Demo with Cloud Connectivity using Wi-Fi (CN0420) <eval-adicup3029/reference_designs/smart_greenhouse>`
   #. :dokuwiki:`Water Conductivity and pH Measurement Demo (using EVAL-CN0428-EBZ & EVAL-M355-ARDZ-INT) <circuits-from-the-lab/cn0428>`
   #. :dokuwiki:`Electrochemical Gas Measurement Demo (using EVAL-CN0429-EBZ & EVAL-M355-ARDZ-INT) <circuits-from-the-lab/cn0429>`
   #. :dokuwiki:`Analog I/O System with HART and Modbus Connectivity for PLC/DCS Applications (CN0435) <eval-adicup3029/reference_designs/demo_plc_modbus>`
   #. :dokuwiki:`Optical Liquid Analysis Measurement Demo (using the EVAL-CN0503-ARDZ) <eval-adicup3029/reference_designs/demo_cn0503>`
   #. :dokuwiki:`2-Port Network Analyzer Software (using the EVAL-CN0507-ARDZ) <circuits-from-the-lab/cn0507>`
   #. :dokuwiki:`Battery Impedance Measurement Demo (using the EVAL-CN0510-ARDZ) <circuits-from-the-lab/cn0510>`
   #. :dokuwiki:`UL 217 Smoke Detector Demo (using the EVAL-CN0537-ARDZ) <eval-adicup3029/reference_designs/demo_cn0537>`
   #. :dokuwiki:`+/- 5V 20-Bit DC Control Demo (using the EVAL-CN0531-PMDZ) <eval-adicup3029/reference_designs/demo_cn0531>`
   #. :dokuwiki:`Radiation Measurement Demo (using the EVAL-CN0536-ARDZ) <eval-adicup3029/reference_designs/demo_cn0536>`
   #. :dokuwiki:`High Voltage and Current Sense Measurement Demo (using the EVAL-CN0548-ARDZ) <circuits-from-the-lab/cn0548>`
   #. :dokuwiki:`Extended Range Capacitance Measurement Demo (using the EVAL-CN0552-PMDZ) <circuits-from-the-lab/cn0552>`

#. :dokuwiki:`Cases, Enclosures, and 3D Printer Files <eval-adicup3029/mechanical>`
#. :dokuwiki:`Help and Support <eval-adicup3029/help_and_support>`
#. :dokuwiki:`Compliance Testing and Results <eval-adicup3029/compliance_testing_and_results>`
