.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ltpa-comprb

.. _eval-ltpa-comprb:

EVAL-LTPA-COMPRB User Guide
===========================

.. note::

   We are in the process of migrating our documentation to GitHub Pages.

Overview
--------

The :adi:`EVAL-LTPA-COMPRB` is an optional companion board to the
:adi:`LTpowerAnalyzer® <eval-ltpa-kit>`, and is designed to support the
optimization of loop compensation in power supply designs. The board functions
as a programmable substitute for the series R-C network in a Type 2 compensator,
and allows users to easily evaluate Bode plots and transient responses with
different combinations of resistances and capacitances.

Features
--------

- 500 Ω to 100 kΩ programmable resistance range
- 10 pF to 39 nF programmable capacitance range
- USB-C interface for data and power
- Small form-factor (2.82`` x 1.25``) enables portable applications

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-top.png
   :width: 600px

Hardware Interface
------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-hardware-interface.png
   :width: 1200px

Compensation Terminals
~~~~~~~~~~~~~~~~~~~~~~

The EVAL-LTPA-COMPRB has four terminals for interfacing the board with a DUT:

.. list-table::
   :header-rows: 1

   * - Terminal
     - Function
   * - R
     - Resistor Terminal. Connected to one end of the programmable resistor
       array.
   * - COM
     - Common Terminal. Connected to the junction between the resistor and the
       capacitor arrays.
   * - C
     - Capacitor Terminal. Connected to one end of the programmable capacitor
       array and its parasitic series resistance.

Basic Operation
---------------

Setup Requirements
~~~~~~~~~~~~~~~~~~

- EVAL-LTPA-COMPRB (LTpowerAnalyzer Compensation Probe)
- EVAL-LTPA-KIT (LTpowerAnalyzer Kit)
- ADALM2000 Advanced Active Learning Module
- Device Under Test (e.g., LT8642S Demo Board)
- DC Power Supply

Step-by-Step-Procedure
~~~~~~~~~~~~~~~~~~~~~~

1. The EVAL-LTPA-COMPRB can function as either a programmable resistor (R and
   COM terminals), capacitor (C and COM terminals), or series resistor-capacitor
   network (R and C terminals), depending on how it is connected to your DUT.
   Consider whether you need to tune both the compensation resistance and
   capacitance, or only one of them, then solder wires to the appropriate
   terminals.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-equivalent-circuit.png
   :width: 200px

.. note::

   The compensation probe has a PCB capacitance of approximately 8 pF, which
   appears connected in parallel with the DUT.

2. Identify where the compensation resistor and/or capacitor (whichever is being
   tuned using the probe) are on your DUT, and verify that the component(s) are
   not populated. Solder the wires from the probe terminals across this
   location. For most DUTs, such as the LT8642S demo board, these components can
   be found connected to a designated loop compensation pin (i.e., VC, COMP/ITH,
   etc.).

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-location-example.png
   :width: 1200px

.. tip::

   The compensation probe should be placed as close as possible, and any wires
   used must be kept short to minimize the parasitic inductance and capacitance.

3. Setup the LTpowerAnalyzer hardware, ADALM2000, and the DUT for Bode Plot
   measurement. Refer to the
   :dokuwiki:`EVAL-LTPA-KIT User Guide </resources/eval/user-guides/eval-ltpa-kit>`
   for detailed instructions. Remember to connect a DC power supply to the DUT
   input.

4. Connect a USB cable from the host PC to the USB-C port on the
   EVAL-LTPA-COMPRB.

5. Launch the LTpowerAnalyzer software. Upon launching, it will automatically
   check for any compensation probes that are connected to the host PC. If a
   probe is detected, the software will open a separate window containing the
   Compensation Probe interface.

6. Click on the drop-down menus for Resistance and Capacitance and select your
   desired setting for each. Upon selection, the probe"s embedded algorithm will
   automatically calculate and implement the best resistor/capacitor combination
   that will result in the closest value to your chosen setting. Below is an
   explanation of the different values displayed by the control panel:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-control-panel.png
   :width: 1400px

7. In the main LTpowerAnalyzer control interface, make a Bode Plot measurement
   and observe the loop gain with the programmed compensation values. Adjust the
   resistance and capacitance values as needed for your stability requirements
   (e.g., gain margin, phase margin, crossover frequency, etc.) .

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-bode-plot-example.png
   :width: 1400px

Example Setup Using the LT8642S Demo Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A hardware setup of the compensation probe is shown below for reference. This
example uses the LT8642S demo board included with the EVAL-LTPA-KIT as the
device under test.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-example-application.png
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-example-iso.png
   :width: 400px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-example-top.png
   :width: 300px

.. note::

   Note: These photos were taken using an older version of the EVAL-LTPA-COMPRB
   with a green solder mask.

Accuracy and Limitations
------------------------

If the Compensation Probe is connected properly, the resulting Bode plots should
be very similar to what would be captured had the compensation resistor and
capacitor been soldered directly to the DUT. The following example Bode plots
illustrate this at different compensation resistances for the LT8642S:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-bode-plot-comparison-13k.png
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-bode-plot-comparison-26k.png
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-bode-plot-comparison-52k.png
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-bode-plot-comparison-100k.png
   :width: 600px

The hardware architecture of the Compensation Probe uses digitally-controlled
switches to implement a parallel combination of resistors (or capacitors), with
the total effective value used to emulate a standard E96 resistor (or E24
capacitor).

A limitation of this architecture is that the compensation resistance and
capacitance becomes less accurate at higher and lower settings respectively.
This is inherent to how parallel connections work, as there are simply less
available resistors (or capacitors) that can be combined to produce a valid
result at those settings.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-resistance-error.png
   :width: 600px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ltpa-comprb/eval-ltpa-comprb-capacitance-error.png
   :width: 600px

Useful Links
------------

- :dokuwiki:`EVAL-LTPA-KIT Overview </resources/eval/user-guides/eval-ltpa-kit>`
- :dokuwiki:`EVAL-LTPA-KIT Hardware Setup Guide </resources/eval/user-guides/eval-ltpa-kit/hardware>`
- :dokuwiki:`EVAL-LTPA-KIT Software Setup Guide </resources/eval/user-guides/eval-ltpa-kit/software>`

Support
-------

For questions and more information, please visit the Analog Devices
:ez:`EngineerZone <reference-designs/ltpoweranalyzer>`.
