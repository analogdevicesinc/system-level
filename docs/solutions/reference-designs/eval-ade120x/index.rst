.. imported from: https://wiki.analog.com/resources/eval/user-guides/ade120x

.. _eval-ade120x:

EVAL-ADE120x
===============================================================================

Evaluating the ADE1201/ADE1202 configurable, isolated binary input monitors.

.. figure:: eval-ade1202.png
   :align: center
   :width: 400

   EVAL-ADE1202EBZ

Overview
-------------------------------------------------------------------------------

The ADE120x is an isolated binary input monitor. It performs an isolated
measurement of a binary input voltage and communicates the status of this input
to low voltage processors or logic circuits. The ADE120x application circuit
can accept a wide range of binary input voltages from 10 V to 300 V scaled
using a resistor divider before applying the voltage to the pins.

This content applies to both :adi:`ADE1201` and :adi:`ADE1202`.

Features:

- Configurable, isolated digital input (single channel on the ADE1201, dual
  channel on the ADE1202)
- Programmable trip threshold and on-chip debounce filter
- On-chip data and power isolation
- Programmable wetting current
- ADC samples available for system diagnostics

Applications:

- Energy transmission and distribution
- Multifunction relay protection
- Substation battery monitoring
- Circuit breaker status indication

User guides
-------------------------------------------------------------------------------

.. toctree::
   :caption: The user guides are provided at:

   tools
   hardware/eval-ade1202

The evaluation hardware also requires one of the following controller boards:

- :adi:`EVAL-SDP-CB1Z <SDP-B>`, used by the LabVIEW GUI.
- :adi:`EVAL-SDP-CK1Z <SDP-K1>`, used by the MBED software drivers.

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our
:ref:`EngineerZone forums <help-and-support>`, but before that, please make
sure you read our documentation thoroughly.

Warning
-------------------------------------------------------------------------------

.. esd-warning::

Help and support
-------------------------------------------------------------------------------

.. toctree::

   help_and_support

For other questions, see the :ref:`help-and-support` page.
