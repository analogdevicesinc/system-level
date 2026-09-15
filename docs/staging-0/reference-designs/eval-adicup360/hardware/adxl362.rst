.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-adicup360/hardware/adxl362

.. _eval-adicup360 hardware adxl362:

EVAL-ADXL362-ARDZ Shield
========================

The :adi:`EVAL-ADXL362-ARDZ` shield illustrates the functionality of the
:adi:`ADXL362` - an ultralow power, 3-axis MEMS accelerometer.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/eval-adxl362-ardz.jpg
   :width: 400px

The :adi:`ADXL362` is capable of measuring dynamic acceleration (resulting from
motion or shock) as well as static acceleration (gravity). It provides 12-bit
output resolution and has three operating ranges, ±2 g, ±4 g, and ±8 g.
Additional useful features include an on-chip, 12-bit temperature sensor
accurate to ±0.5°, motion triggered wake-up functionality, and and several
activity detection modes which makes is ideal for portable low-power
instruments.

The :adi:`EVAL-ADXL362-ARDZ` Shield is designed in Arduino Uno R3 format which
makes it suitable to be used with both Arduino Due (e.g. :adi:`EVAL-ADICUP360`
based board) and Arduino Uno R3 base boards.

.. tip::

   The :adi:`EVAL-ADXL362-ARDZ` board has a large capacitor (C18) on the board
   which holds charge for the LCD screen. When power cycling the system, you
   must wait approximately 5 seconds to allow enough time for the capacitors on
   the :adi:`EVAL-ADXL362-ARDZ` board to fully discharge. This is a power
   requirement for the :adi:`ADXL362`, which notes in the datasheet that the
   power rail must come all the way back down to 0V before powering back up.

Getting Started Video
---------------------

.. todo:: .. figure: analogTV>4807248650001

Connectors and Jumper configuration
-----------------------------------

The :adi:`EVAL-ADXL362-ARDZ` Shield has four jumpers to increase flexibility
when stacking systems together. Each jumper and it"s purpose is described below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/eval-adxl362-ardz_silkscreen_w-jumper.png
   :width: 500px

ADXL_CS_SEL
~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Configuration
     - Function
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/horizontal_jumper_12.png
          :width: 125px

     - Routes ADXL362 CS pin to P0.3/IRQ0/CS1
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/horizontal_jumper_23.png
          :width: 125px

     - Routes ADXL362 CS pin to P0.4/RTS/IRQ1

LCD_CS_SEL
~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Configuration
     - Function
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/horizontal_jumper_12.png
          :width: 125px

     - Connects LCD CS pin to P2.2/BM
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/horizontal_jumper_23.png
          :width: 125px

     - Connects LCD CS pin to P1.4/PWM2/MISO0.

ADXL_INT_SEL
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Configuration
     - Function
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/vertical_jumper_12.png
          :width: 65px

     - Connects ADXL362 Interrupt pin 1 (INT1) to P1.0/IRQ3
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/vertical_jumper_23.png
          :width: 65px

     - Connects ADXL362 Interrupt pin 2 (INT2) to P1.0/IRQ3.

LDC_RST_SEL
~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Configuration
     - Function
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/horizontal_jumper_12.png
          :width: 125px

     - Connects LCD Reset to IOREF
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/hardware/horizontal_jumper_23.png
          :width: 125px

     - Connects LCD Reset to pin P1.1/IRQ4

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download

   :adi:`EVAL-ADXL362-ARDZ Design & Integration Files <media/en/reference-design-documentation/design-integration-files/eval-adxl362-ardz-designsupport.zip>`

   - Schematics
   - PCB Layout and Mounting Diagram
   - Bill of Materials
   - Allegro Project

Software examples
-----------------

- :dokuwiki:`ADICUP360 + ADXL362 Demo </resources/eval/user-guides/eval-adicup360/reference_designs/demo_adxl362>`
- :dokuwiki:`ADICUP3029 + ADXL362 Wi-Fi Demo </resources/eval/user-guides/eval-adicup3029/reference_designs/demo_adxl362>`
- :dokuwiki:`Arduino Uno + ADXL362 Demo </resources/eval/user-guides/arduino-uno/reference_designs/demo_adxl362>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you register your hardware.
   :reg:`Register <EVAL-ADXL362-ARDZ?&v=RevD>` to receive all these great
   benefits and more!


