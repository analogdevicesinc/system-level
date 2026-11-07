.. collection:: Introduction to Electronics
   :subtitle: Electronics and electrical engineering fundamentals.
   :label: workshop

   An introductory workshop on electronics and microchips for students.

   system-level:
     - .
     - tools/m2k/index
     - learning/workshops_software_defined_instrumentation/index

Introduction to Electronics
===============================================================================

.. contents:: Contents
   :local:
   :depth: 2

Introduction
------------

This workshop is designed for freshmen and second-year students who are passionate about electronics and electrical engineering. It aims to provide them with a comprehensive overview of the field.

The content and structure are tailored to their current level of knowledge, introducing them to the fascinating world of electronics and microchips.


Slide Deck and Booklet
----------------------

Since this tutorial is also designed to be presented as a live, hands-on workshop, a slide deck is provided here:

.. admonition:: Download

   :download:`Introduction to Electronics Slide Deck <electronicsbasics_nov24.pdf>`

A complete booklet of the hands-on activity is also provided, as a companion to following the tutorial yourself:

.. admonition:: Download

   :download:`Introduction to Electronics Booklet <ebasics booklet.pdf>`

A comma separated values file used for generating the base step voltage needed for the Transistor Characteristic demo is also provided:

.. admonition:: Download

   :download:`Base Voltage Values <basevoltage.csv>`

Theory
------

Why Electronics?
~~~~~~~~~~~~~~~~

Every Electronics or Electrical Engineering student has received at least once the question: *why did you choose electronics?*
How can one answer this question better than: *Why not?*

#. It offers diverse career opportunities:

   * Wireless Communications Engineer
   * Network Engineer
   * Electronics Design Engineer
   * Embedded Systems Engineer
   * Satellite Communications Engineer

#. It brings to table innovation and technological advancement

#. It offers impactful contribution

#. It offers continuous learning

What is an IC?
~~~~~~~~~~~~~~

An integrated circuit (IC) is an assembly of electronic components in which hundreds to millions of transistors, resistors, and capacitors are interconnected and built up on a thin substrate of semiconductor material (usually silicon) to form a small chip or wafer. Integrated circuits are the building blocks for most electronic devices and equipment.

**Applications**

* Consumer Electronics: Smartphones, computers, and home appliances.
* Industrial: Automation systems, robotics.
* Medical: Diagnostic equipment, wearable health devices.
* Automotive: Engine control units, infotainment systems.

**Importance**

* Miniaturization of circuits.
* Increased reliability and performance.
* Cost efficiency.

.. figure:: ic.png
   :align: center
   :width: 30em

   ICs are everywhere

.. figure:: circuit.png
   :align: center
   :width: 30em

   LSI - Large Scale Integration circuits compared to the corresponding prototype circuit 1970-1972

**Transistors - what kind of species is that?**

A transistor is a miniature semiconductor that regulates or controls current or voltage flow in addition amplifying and generating these
electrical signals and acting as a switch/gate for them

* Why do we need them?
* How do they work?
* What are the commonly used types?

**Applications**

* Analog Circuits: Amplifiers, oscillators.
* Digital Circuits: Logic gates, microprocessors.
* Power Electronics: Power supplies, motor controllers.

.. figure:: transistor.png
   :align: center
   :width: 30em

   Transistor - the base of Electronics

**Functionality**

* Cut Off ("off"):  Emitter > Base < Collector
* Saturation ("on"): Emitter < Base > Collector
* Forward Active ("proportional"):  Emitter < Base < Collector
* Reverse Active ("negative proportional"):  Emitter > Base > Collector

.. figure:: vce_ib.png
   :align: center
   :width: 30em

   Output Characteristics - common emitter configuration

**How many transistors are needed to create a logic gate?**

Logic gates built with transistors

.. grid::
   :widths: 50% 50%

   .. image:: and.png
      :width: 30em
      :alt: AND

   .. image:: not.png
      :width: 30em
      :alt: NOT

**ADALM2000**

The ADALM2000 (M2K) Advanced Active Learning Module is an affordable USB-powered data acquisition module, that can be used to introduce fundamentals
of electrical engineering in a self or instructor lead setting.

With 12-bit ADCs and DACs running at 100 MSPS, brings the power of high-performance lab equipment to the palm of your hand, enabling electrical
engineering students and hobbyists to explore signals and systems into the tens of MHz without the cost and bulk associated with traditional lab gear.

When coupled with Analog Devices' Scopy™ graphical application software running on a computer, provides the user with high performance instrumentation.

.. grid::
   :widths: 50% 50%

   .. figure:: m2k.png
      :width: 30em
      :alt: M2K

      M2K Active Learning Module

   .. figure:: scopy.png
      :width: 30em
      :alt: Scopy

      Scopy Software

Hands-on activity
-----------------

By the end of this workshop, you will learn:

* How to use a breadboard
* How to power on an IC
* How to read an IC pinout from datasheet
* How to use a desktop Oscilloscope and Signal generator channels by operating a Network Analyzer
* How to visualize a low pass filter characteristic / transfer function
* How to drive a transistor
* How to create a logic function for performing a specific task

**Activities**

* Low pass filter transfer function
* Digital demo - traffic lights using logic gates
* Back to the analog world - Transistors
* Home made battery

**Materials**

* ADALM2000 Active Learning Module
* Solder-less breadboard, and jumper wire kit
* 2 x 1 KΩ resistors
* 2 x 0.1 uF capacitors (marked 104)

**Pre-requisites**

* :ref:`pluto-m2k firmware`
* :git-plutosdr-m2k-drivers-win:`ADALM2000 drivers installation <releases+>`
* :git-scopy:`Install latest version of Scopy software <releases+>`

Example 1 - Scope and Signal generator channels - Cascaded LP filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First Stage Filter
^^^^^^^^^^^^^^^^^^^

**Hardware setup**

.. figure:: demo1hw.png
   :align: center
   :width: 30em

   Schematic for first stage filter

.. figure:: demo1bb.png
   :align: center
   :width: 30em

   Breadboard connections for first stage filter

**Steps**

#. Open Network Analyzer
#. Set the sweep to logarithmic
#. Set the start frequency to 100Hz and stop to 20kHz
#. Set the magnitude axis between -50dB and 10dB
#. Set the phase axis between -180 and 90 degrees

.. figure:: demo1waves.png
   :align: center
   :width: 30em

   Results for Bode Diagram

Second Stage Filter
^^^^^^^^^^^^^^^^^^^

.. figure:: demo1hw1.png
   :align: center
   :width: 30em

.. figure:: demo1bb1.png
   :align: center
   :width: 30em

   Schematic and Breadboard connections

**Steps**

#. Connect the Scope Channel 2 after the first RC group and do a single sweep
#. Take a signal snapshot to preserve the result as a reference
#. Connect the Scope Channel 2 after the second RC stage and perform another sweep

.. figure:: demo1waves1.png
   :align: center
   :width: 30em

   Results for Bode Diagram

Example 2 - Traffic lights control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This demo will showcase the usage of logic gates to implement a logic function which describes the functionality of a well-known device: a traffic light.

**Materials**

* ADALM2000 Active Learning Module
* Jumper wires
* 1 SN74HC08N part
* 1 SN74HC32N part
* 1 SN74HC04N part
* 1 Yellow LED
* 1 Red LED
* 1 Green LED

**Theory of operation**

Logic sequence of a traffic light is the one below:

.. figure:: rgy.png
   :align: center
   :width: 30em

You will use two logic inputs to control the traffic lights, those inputs are marked A and B, the sequence is the one below:

.. figure:: rgy1.png
   :align: center
   :width: 30em

   Flow diagram

Truth table for the logic function that describes the traffic lights sequence

.. figure:: demo2.png
   :align: center
   :width: 30em

**Hardware Setup**

The circuit functionality is represented in the schematic:

.. figure:: demo2hw.png
   :align: center
   :width: 30em

   Schematic

Components Pinout

.. grid::
   :widths: 33% 33% 33%

   .. figure:: sn74hc04n.png
      :width: 30em
      :alt: SN74HC04N

      SN74HC04N

   .. figure:: sn74hc08n.png
      :width: 30em
      :alt: SN74HC08N

      SN74HC08N

   .. figure:: led.png
      :width: 30em
      :alt: LED

      LED Terminals

**Steps**

#. Place the ICs on the breadboard with each pin row on one side of the breadboard delimitator.
#. Open Scopy application
#. Open the Oscilloscope instrument
#. Open the Power instrument
#. Connect the V+ wire to pins 14 of the both ICs - VCC
#. Connect GND pin of the M2K to pin 7 of both ICs
#. Connect DIO 0 pin to SN74HC04N pin 1
#. Connect DIO 0 pin to SN74HC08N pin 1
#. Connect DIO 1 pin to SN74HC04N pin 3
#. Connect DIO 1 pin to Y LED
#. Connect SN74HC04N pin 2 to R LED
#. Connect SN74HC04N pin 4 to SN74HC08N pin 2
#. Connect SN74HC08N pin 3 to G LED
#. Set the V+ to 3.3V and press the Enable button


**Results**

* Open the Scopy Digital IO and Power instruments:
* Toggle the DIO0 and DIO1 digital pins according to the logical function truth table and verify the outputs match the table results

.. figure:: demo2scopy.png
   :align: center
   :width: 30em

   Scopy setup

**Challenge**

* Implement a logical OR function using SN74HC32N part from the kit
* Pinout:

.. figure:: sn74hc32n.png
   :align: center
   :width: 30em

   Logical OR


Example 3 - NPN transistor characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The demo will describe the output characteristics of a BJT NPN transistor using modern instrumentation tools.

**Materials**

* ADALM2000 Active Learning Module
* Jumper wires
* 1 - 100KΩ Resistor
* 1 - 100Ω Resistor
* 1 - small signal NPN transistor - 2N3904
* 1 - small signal PNP transistor - 2N3906

**Theory of operation**

2N3904 Pinout

.. grid::
   :widths: 50% 50%

   .. image:: npn.png
      :width: 30em
      :alt: pnp

   .. image:: npn1.png
      :width: 30em
      :alt: SN74HC08N

**Hardware setup**

* Place the transistor and resistors on the breadboard.
* Make the connections between ADALM2000 and circuit as shown below.

.. figure:: npn2.png
   :align: center
   :width: 30em

   ADALM2000 connections

**Steps**

#. Open Scopy application
#. Create a CSV file with a column having integer values from 0 to 5(0, 1, 2, 3, 4), save it
#. Open the Waveform generator instrument and select Channel 2, load the previously created csv file and make the setup:

   .. figure:: demo2scopy1.png
      :align: center
      :width: 30em

#. Select Channel 1, make the setup below:

   .. figure:: demo2scopy2.png
      :align: center
      :width: 30em

#. Open the scope and select the XY view
#. Add a math channel with the following function: M1 = t0/100  - it represents the Ic current, given the 100 ohms collector resistor

**Results**

Observe the output characteristics of the NPN transistor Ic = f(Vce)

.. figure:: demo2scopyres.png
   :align: center
   :width: 30em

**Challenge**

* Obtain the characteristics for a PNP transistor provided.
* The curve trace should look like the one in the image:

.. figure:: demo2scopych.png
   :align: center
   :width: 30em

Tips: you need to create another csv file for the base control signal of the transistor.

Example 4 - Home made battery - instructor-led
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This demo is instructor-led and intends to implement a proof of concept for a battery powered LED using unconventional materials.

**Materials**

* ADALM2000 Active Learning Module
* Jumper wires (wires with alligator clips will work best)
* 3 lemons: large, fresh, “juicy” lemons work best.
* Zinc plated screws or nails
* Copper plated coins or copper nails or heavy gauge (14 or 12) copper wire.
* Red LED

**Hardware Setup**

#. Insert a copper penny into a small cut or push a copper nail or heavy gauge wire into one side of the lemon.
#. Push a galvanized (zinc coated) screw or nail into the other side of the lemon. The zinc and copper electrodes must not touch.

**Steps**

#. Repeat the procedure for all 3 lemons
#. Connect the lemon cells in series by linking the copper electrode of one lemon to the zinc electrode of the next
#. Connect the Red LED across the battery (copper of first lemon to LED anode, zinc of last lemon to LED cathode)

.. figure:: demo4.png
   :align: center
   :width: 20em


**Results**

You should be able to observe how the Red LED is lit by the 4 or more lemon-cells battery


Takeaways
---------

Electronics can be both fun and challenging, but it brings many satisfactions

ADALM2000 is a very versatile tool suited to use in various applications:

* Lab setups

* Advanced measurements

* Learning platforms

* Research

Resources
---------

* :ref:`university`
* :dokuwiki:`university/courses/alm1k/intro/real-voltage-sources`
* :dokuwiki:`university/courses/electronics/electronics-lab-4`
* :dokuwiki:`university/courses/engineering_discovery/lab_13`

*Specific hardware resources*

* https://www.britannica.com/technology/integrated-circuit/Photolithography
* https://learn.sparkfun.com/tutorials/transistors/all

*Inspiration*

* https://www.arenasolutions.com/resources/glossary/integrated-circuit/
* https://learn.sparkfun.com/tutorials/transistors/all
* https://www.electrical4u.com/transistor-characteristics/?utm_content=cmp-true
* https://www.101computing.net/creating-logic-gates-using-transistors/

