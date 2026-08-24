EVAL-ADXL372-ARDZ Shield
========================

The :adi:`ADXL372` is an ultralow power, 3-axis, ±200 g MEMS accelerometer that consumes 22 μA at a 3200 Hz output data rate (ODR). The ADXL372 is designed to be used in internet of things(IoT) applications such as:

-  Impact and shock detection
-  Asset health assessment
-  Portable Internet of Things (IoT) edge nodes
-  Concussion and head trauma detection

In addition to its ultralow power consumption, the ADXL372 has many features to
enable impact detection while providing system level power reduction. The device
includes a deep multimode output first in, first out (FIFO), several activity
detection modes, and a method for capturing only the peak acceleration of over
threshold events.

.. image:: ../images/top_adxl_int_together.png
   :align: center
   :width: 400

Two additional lower power modes with interrupt driven, wake-up features are
available for monitoring motion during periods of inactivity. In wake-up mode,
acceleration data can be averaged to obtain a low enough output noise to trigger
on low g thresholds. In instant on mode, the ADXL372 consumes 1.4 μA while
continuously monitoring the environment for impacts. When an impact event that
exceeds the internally set threshold is detected, the device switches to normal
operating mode fast enough to record the event.

The :adi:`EVAL-ADXL372-ARDZ` Shield is designed to be compatible with the Arduino Uno R3 form factor.

Connectors and Jumper Configuration
-----------------------------------

The :adi:`EVAL-ADXL372-ARDZ` Shield has four jumpers to increase flexibility when stacking systems together. Each jumper and it's purpose is described below.

.. image:: ../images/eval-adxl-ardz-int_jumper_select.png
   :align: center
   :width: 400

ADXL_CS_SELECT(P10)
~~~~~~~~~~~~~~~~~~~

============= =============================
Configuration Function
============= =============================
|image1|      Routes ADXL372 CS pin to CS_1
|image2|      Routes ADXL372 CS pin to CS_2
============= =============================

ADXL_INT1_SELECT(P11)
~~~~~~~~~~~~~~~~~~~~~
============= ===================================
Configuration Function
============= ===================================
|image3|      Connects ADXL372 INT1 pin to INT1_A
|image4|      Connects ADXL372 INT1 pin to INT1_B
============= ===================================

ADXL_INT2_SELECT(P12)
~~~~~~~~~~~~~~~~~~~~~
============= ===================================
Configuration Function
============= ===================================
|image5|      Connects ADXL372 INT2 pin to INT2_A
|image6|      Connects ADXL372 INT2 pin to INT2_B
============= ===================================

VOLTAGE TRANSLATOR VDDIO SELECT(P13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
============= ============================================
Configuration Function
============= ============================================
|image7|      Connects ADXL VDDIO to the 3.3V Arduino pin
|image8|      Connects ADXL VDDIO to the IOREF Arduino pin
============= ============================================

Connecting/Mounting ADXL372
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Direct Mounting (P5 and P2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connectors P5 and P2 are designed to be directly interfaced with the
EVAL-ADXL372Z-PIN. This creates a mechanically strong connection and allows for
the Arduino shield to directly include the ADXL372 sensor. Be careful when
connecting the EVAL-ADXL372Z-PIN with the EVAL-ADXL-ARDZ-INT to make sure that
all the signals go to the correct pin of connectors P5 and P2.

.. image:: ../images/eval-adxl-ardz-int_direct_connection.png
   :align: center
   :width: 400

========== ============== ==============
Pin Number P5 Signal Name P2 Signal Name
========== ============== ==============
PIN 1      DGND           +3.3V
PIN 2      SCLK           IOREF
PIN 3      MOSI           DGND
PIN 4      MISO           INT2
PIN 5      CS             INT1
========== ============== ==============

.. image:: ../images/top_adxl_int_separate.png
   :align: center
   :width: 450

.. image:: ../images/top_adxl_int_together.png
   :align: center
   :width: 300

Ribbon Cable Connection (P7 and P1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connectors P7 and P1 are designed to interface with the EVAL-ADXL372Z-PIN via a
ribbon cable. This allows for remotely mounting the sensor when you can't have
the rest of the electronics on the unit being sensed. Because this is a cabled
over option you could also use other Digital output accelerometer devices with
the EVAL-ADXL-ARDZ-INT such as the ADXL346/46 or the ADXL355/57. Be careful when
connecting the EVAL-ADXL372Z-PIN with the EVAL-ADXL-ARDZ-INT to make sure that
all the signals go to the correct pin of connectors P7 and P1.

.. image:: ../images/eval-adxl-ardz-int_cable_connection.png
   :align: center
   :width: 400

========== ============== ==============
Pin Number P7 Signal Name P1 Signal Name
========== ============== ==============
PIN 1      SCLK           +3.3V
PIN 2      MOSI           IOREF
PIN 3      MISO           DGND
PIN 4      CS             DATA_RDY
PIN 5      SDA            INT1
PIN 6      SCL            INT2
========== ============== ==============

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download
   :class: download

   :adi:`EVAL-ADXL372-ARDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-adxl372-ardz-designsupport.zip>`

   -  Schematic
   -  PCB Layout
   -  Bill of Materials
   -  Allegro Project

Software Examples
-----------------

-  :doc:`ADICUP3029 + ADXL372 Bluetooth Demo </solutions/reference-designs/eval-adicup3029/reference_designs/demo_adxl372>`
-  :dokuwiki:`Arduino Uno + ADXL372 Demo <resources/eval/user-guides/arduino-uno/reference_designs/demo_adxl372>`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest videos, and more when you register your hardware. `Register <https://form.analog.com/Form_Pages/FeedBack/EVAL-ADXL372-ARDZ?&v=RevC>`_ to receive all these great benefits and more!

*End of Document*

.. |image1| image:: ../images/horizontal_jumper_12.png
   :width: 125

.. |image2| image:: ../images/horizontal_jumper_23.png
   :width: 125

.. |image3| image:: ../images/horizontal_jumper_12.png
   :width: 125

.. |image4| image:: ../images/horizontal_jumper_23.png
   :width: 125

.. |image5| image:: ../images/horizontal_jumper_12.png
   :width: 125

.. |image6| image:: ../images/horizontal_jumper_23.png
   :width: 125

.. |image7| image:: ../images/horizontal_jumper_12.png
   :width: 125

.. |image8| image:: ../images/horizontal_jumper_23.png
   :width: 125
