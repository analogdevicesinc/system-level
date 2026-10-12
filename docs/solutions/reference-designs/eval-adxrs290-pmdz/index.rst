.. _eval_adxrs290_pmdz:

EVAL-ADXRS290-PMDZ
==================

Ultralow Noise, Dual-Axis MEMS Gyroscope for Stabilization Applications

.. image:: images/eval-adxrs290-pmdz.png
   :align: center
   :width: 200

Overview
--------

The :adi:`EVAL-ADXRS290-PMDZ` is a simple Pmod form factor evaluation board for
the :adi:`ADXRS290`, a high-performance MEMS pitch-and-roll (dual-axis in-plane)
angular rate sensor (gyroscope) designed for use in stabilization applications.

The solution senses and digitizes the **X-axis** and **Y-axis** (also called
**roll** and **pitch**) angular rates, producing a positive reading for
clockwise rotation about the X-axis and Y-axis.

.. image:: images/roll_and_pitch.png
   :align: center
   :width: 200

The :adi:`ADXRS290` provides an output full-scale range of ±100°/s with 
a sensitivity of 200 LSB/°/s. Its resonating disk sensor structure enables 
angular rate measurement about the axes normal to the sides of the package 
around an  in-plane axis. Angular rate data is formatted 
as a 16-bit two's complement and is accessible through an SPI digital interface. 
The ADXRS290 exhibits a low noise floor of 0.004°/s/√Hz and features programmable 
high-pass and lowpass filters.

The ADXRS290 communicates via 4-wire SPI and operates as a peripheral 
(subordinate) device, with a maximum clock frequency of 12 MHz.

.. image:: images/spi_comm.png
   :align: center
   :width: 300

The digital communication on the :adi:`EVAL-ADXRS290-PMDZ` is
accomplished using a standard expanded SPI PMOD port.

+------------------+------------+
| Connector P1     |            |
+==================+============+
| **Description**  | **Pin(s)** |
+------------------+------------+
| SS               | 1          |
+------------------+------------+
| MOSI             | 2          |
+------------------+------------+
| MISO             | 3          |
+------------------+------------+
| SCLK             | 4          |
+------------------+------------+
| GND              | 5, 11      |
+------------------+------------+
| IOVDD            | 6, 12      |
+------------------+------------+
| SYNC             | 7          |        
+------------------+------------+

Features
--------

-  Pitch and roll rate gyroscope
-  Ultralow noise: 0.004°/s/√Hz
-  High vibration rejection over a wide frequency range
-  Power saving standby mode
-  80 µA current consumption in standby mode
-  Fast startup time from standby mode: <100 ms
-  Low delay of <0.5 ms for a 30 Hz input at the widest bandwidth setting
-  Serial peripheral interface (SPI) digital output
-  Programmable high-pass and low-pass filters
-  2000 g powered acceleration survivability
-  2.7V to 5.0V operation
-  −25°C to +85°C operation
-  PMOD form factor

Applications
------------

- Optical image stabilization
- Platform stabilization
- Wearable products

.. admonition:: Getting Started

   The :adi:`EVAL-ADXRS290-PMDZ` can be used for a wide range of applications, 
   and the following demos are meant to show examples of the flexibility of the board. 
   To get started with setup, configuration, and example use cases, 
   please proceed to the PMOD Guide and follow the provided serial terminal setup.

   - :ref:`PMOD Guide <eval_adxrs290_pmdz eval>`
   - :ref:`Serial Terminal Setup <eval_adxrs290_pmdz uart_serial_terminal>`

Recommendations
---------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ez:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Warning
-------

.. esd-warning::

Help and Support
----------------

Please go to :ez:`Help and Support <help-and-support>` page.

.. toctree::
   :hidden:

   eval-adxrs290-pmdz
   uart_serial_terminal
