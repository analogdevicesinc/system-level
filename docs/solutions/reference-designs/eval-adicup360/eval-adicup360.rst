EVAL-ADICUP360 User Guide
=========================

The :adi:`EVAL-ADICUP360` is an Arduino-like platform based on the :adi:`ADuCM360` fully integrated, 3.9 kSPS, 24-bit data acquisition system that incorporates dual high performance, multichannel sigma-delta (Σ-Δ) analog-to-digital converters (ADCs), a 32-bit ARM Cortex™-M3 processor, and Flash/EE memory on a single chip. The platform has an Arduino-Due compatible form factor and has two additional PMOD connectors. It is accompanied by an Eclipse based development environment.

.. image:: images/ecosystem_collage.png
   :align: right
   :width: 500

-  :doc:`Introduction </solutions/reference-designs/eval-adicup360/introduction>`
-  :doc:`Tools and Driver Details </solutions/reference-designs/eval-adicup360/tools>`

   -  :doc:`CrossCore Download & Installation Guide </solutions/reference-designs/eval-adicup360/tools/cces_setup_guide>`
   -  :doc:`CrossCore Quickstart User Guide </solutions/reference-designs/eval-adicup360/tools/cces_user_guide>`
   -  :doc:`Hardware Drivers and USB Storage Drives </solutions/reference-designs/eval-adicup360/tools/adicup360_hw_drivers>`
   -  :doc:`Using EVAL-ADICUP360 with IAR and Keil IDEs </solutions/reference-designs/eval-adicup360/tools/keil_iar_support>`
   -  :doc:`Unbricking the ADICUP360 </solutions/reference-designs/eval-adicup360/tools/ccsfp_unlock_adicup360>`

-  :doc:`Hardware Details </solutions/reference-designs/eval-adicup360/hardware>`

   -  :doc:`EVAL-ADICUP360 Base Board </solutions/reference-designs/eval-adicup360/hardware/base_board>`
   -  :doc:`EVAL-ADT7420-PMDZ PMOD </solutions/reference-designs/eval-adicup360/hardware/adt7420>`
   -  :doc:`EVAL-ADXL355-PMDZ PMOD </solutions/reference-designs/eval-adicup360/hardware/adxl355>`
   -  :doc:`EVAL-ADXL362-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/adxl362>`
   -  :doc:`EVAL-CN0216-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0216>`
   -  :doc:`EVAL-CN0326-PMDZ PMOD </solutions/reference-designs/eval-adicup360/hardware/cn0326>`
   -  :doc:`EVAL-CN0336-PMDZ PMOD </solutions/reference-designs/eval-adicup360/hardware/cn0336>`
   -  :doc:`EVAL-CN0337-PMDZ PMOD </solutions/reference-designs/eval-adicup360/hardware/cn0337>`
   -  :doc:`EVAL-CN0338-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0338>`
   -  :doc:`EVAL-CN0357-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0357>`
   -  :doc:`EVAL-CN0391-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0391>`
   -  :doc:`EVAL-CN0394-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0394>`
   -  :doc:`EVAL-CN0395-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0395>`
   -  :doc:`EVAL-CN0396-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0396>`
   -  :doc:`EVAL-CN0397-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0397>`
   -  :doc:`EVAL-CN0398-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0398>`
   -  `EVAL-CN0409-ARDZ Shield <https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0409>`_
   -  :doc:`EVAL-CN0411-ARDZ Shield </solutions/reference-designs/eval-adicup360/hardware/cn0411>`

-  :doc:`Example Projects with Setup Instructions </solutions/reference-designs/eval-adicup360/reference_designs>`

   -  :doc:`Blinking LEDs Demo </solutions/reference-designs/eval-adicup360/reference_designs/demo_blink>`
   -  :doc:`Command Line Interpreter Demo </solutions/reference-designs/eval-adicup360/reference_designs/demo_cli>`
   -  :doc:`High Accuracy Temperature Demo (with EVAL-ADT7420-PMDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_adt7420>`
   -  :doc:`High Resolution Accelerometer Demo (with EVAL-ADXL355-PMDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_adxl355>`
   -  :doc:`Low Power Accelerometer Demo (with EVAL-ADXL362-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_adxl362>`
   -  :doc:`PMOD Accelerometer Demo (with PmodACL2 from Digilent) </solutions/reference-designs/eval-adicup360/reference_designs/demo_pmodacl2>`
   -  :doc:`Weigh Scale Demo (with EVAL-CN0216-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0216>`
   -  :doc:`pH Monitor with Temperature Compensation Demo (with EVAL-CN0326-PMDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0326>`
   -  :doc:`Data Acquisition for Input Current Demo (with EVAL-CN0336-PMDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0336>`
   -  :doc:`RTD Temperature Measurement Demo (with EVAL-CN0337-PMDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0337>`
   -  :doc:`CO2 Gas Measurement Demo (with EVAL-CN0338-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0338>`
   -  :doc:`CO Toxic Gas Measurement Demo (with EVAL-CN0357-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0357>`
   -  :doc:`Universal Multichannel Thermocouple Measurement(Digital Output) Demo (with EVAL-CN0391-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0391>`
   -  :doc:`Universal Multichannel Thermocouple Measurement(Analog Output) Demo (with EVAL-CN0394-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0394>`
   -  :doc:`Volatile Organic Compound (VOC) Gas Detection Demo (with EVAL-CN0395-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0395>`
   -  :doc:`Dual Toxic Gas Measurement Demo (with EVAL-CN0396-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0396>`
   -  :doc:`Visible Light Detection/Measurement Demo (with EVAL-CN0397-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0397>`
   -  :doc:`Soil Moisture and pH Measurement Demo (with EVAL-CN0398-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0398>`
   -  :doc:`Turbidity Measurement Demo (with EVAL-CN0409-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0409>`
   -  :doc:`Total Dissolved Solids Measurement Demo (with EVAL-CN0411-ARDZ) </solutions/reference-designs/eval-adicup360/reference_designs/demo_cn0411>`

-  :doc:`Application Demos with Setup Instructions </solutions/reference-designs/eval-adicup360/application_demos>`

   -  :doc:`Smart Greenhouse Demonstration (Soil moisture, soil pH, temperature, and visible light spectrum/intensity, LED control </solutions/reference-designs/eval-adicup360/application_demos/smart_greenhouse>`)

-  :doc:`Cases, Enclosures, and 3D Printer Files </solutions/reference-designs/eval-adicup360/mechanical>`
-  :doc:`Help and Support </solutions/reference-designs/eval-adicup360/help_and_support>`
-  :doc:`Compliance Testing and Results </solutions/reference-designs/eval-adicup360/compliance_testing_and_results>`
