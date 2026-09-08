ADXL355 Low Noise, Programmable ±2g, ±4g, and ±8g Accelerometer PMOD
====================================================================

The :adi:`ADXL355` is a low noise density, low 0 g offset drift, low power, 3-axis MEMS accelerometers with selectable measurement ranges. The ADXL355 supports the ±2g, ±4g, and ±8g ranges, and offers industry leading noise, offset drift over temperature, and long term stability, enabling precision applications with minimal calibration and with very low power consumption.

The ADXL355 accelerometers offer guaranteed temperature stability with null
offset coefficients of 0.15mg/C (max). The stability minimizes resource and
expense associated with calibration and testing effort, helping to achieve
higher throughput for device OEMs. In addition, the hermetic package helps
ensure that the end product conforms to its repeatability and stability
specifications long after they leave the factory.

With output of ±2g to ±8g full scale range (FSR), selectable digital filtering from 1 Hz to 1 kHz, and low noise density of 25µ/√Hz at less than 200µA current consumption, ADXL355 MEMS accelerometer offers performance level comparable to much more expensive devices with less power consumption and BOM cost. For general board details and to buy a board, please visit the :adi:`EVAL-ADXL355-PMDZ` product page.

.. image:: ../images/adxl355_pmdz.png
   :align: center
   :width: 350

Hardware Setup
--------------

The PMOD board is small in size with dimensions approximately 1 inch in width by
1 inch in length. There are a few sections on the hardware I'd like to point out
for you, in order to use the board.

.. important::

   In order to use the EVAL-ADXL355-PMDZ with the ADICUP360, the user MUST
   remove resistor R1. The ADXL355 holds the DATA_RDY pin low during powerup,
   and that holds the EVAL-ADICUP360 in UART boot mode. When this mode is active
   the MCU will stay in standby mode till it receives the proper command,
   effectively making the ADuCM360 not run. So to avoid this, please remove R1
   and note that you can't use the DATA_RDY pin with the ADICUP360

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

When using the ADXL355 PMOD board, the 3.3V power for the PMOD comes directly from the host board it is connected to. The power from the host is generally capable of providing up to 100 mA at 3.3V, but for complete PMOD power specifications please click\ `here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`_.

Digital Interface (PMOD)
~~~~~~~~~~~~~~~~~~~~~~~~

The PMOD interface is a series of standardized digital interfaces for various digital communication protocols such as SPI, I2C, and UART. These interface types were standardized by Digilent, which is now a division of National Instruments. Complete details on the PMOD specification can be found `here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`_.

The specific interface used for the EVAL-ADXL355-PMDZ boards is the extended
SPI. In general ADI has adopted the extended SPI connector for all PMOD devices
which have an SPI interface. It provides flexibility to add interrupts, general
purpose I/O, resets, and other important digitally controlled functions.

============= =================== ========
P1 Pin Number Pin Function        Mnemonic
============= =================== ========
Pin 1         Chip Select         CS
Pin 2         Master Out Slave In MOSI
Pin 3         Master In Slave Out MISO
Pin 4         Serial Clock        SCLK
Pin 5         Digital Ground      DGND
Pin 6         Digital Power       VDD
Pin 7         Interrupt 1         INT1
Pin 8         Not Connected       NC
Pin 9         Interrupt 2         INT2
Pin 10        Data Ready          DRDY
Pin 11        Digital Ground      DGND
Pin 12        Digital Power       VDD
============= =================== ========

|image1|

ADXL355 Interrupt Pins
~~~~~~~~~~~~~~~~~~~~~~

The EVAL-ADXL355-PMDZ has two interrupt pins and a data ready pin which can be used as external indicators for the user. The interrupt pins can be programmed through software to reflect various status flags within the ADXL355, and those pins are accesible through the SPI PMOD header. For complete details on the individual status flags, what they mean, and how to program the chip to reflect those interrupts, please consult the datasheet at :adi:`ADXL355`.

Software examples
-----------------

-  :doc:`ADXL355 Accelerometer PMOD Demo </solutions/reference-designs/eval-adicup360/reference_designs/demo_adxl355>`

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   :adi:`EVAL-ADXL355-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-adxl355-pmdz-designsupport.zip>`

   
   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project
   

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-ADXL355-PMDZ?&v=Rev B>`_ to receive all these great benefits and more!

.. |image1| image:: ../images/adxl355_layout.png
   :width: 300
