.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad353xr

.. _eval-ad353xr:

EVAL-AD353XR
===============================================================================

16-Bit, 4/8-Channel, Low Power, Voltage Output DAC with On-Chip Reference.

.. figure:: ./images/ad3530R.jpeg
   :alt: EVAL-AD3530R evaluation board
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

The :adi:`EVAL-AD3530R` and :adi:`EVAL-AD3531R` are evaluation boards for the
:adi:`AD3530R` and :adi:`AD3531R`, low power, 16-bit, buffered voltage output
digital-to-analog converters (DACs). The :adi:`AD3530R` provides 8 output
channels, while the :adi:`AD3531R` provides 4. Both devices include
software-programmable gain controls that result in full-scale output spans of
2.5 V or 5 V. Target applications include optical transceivers, test and
measurement, industrial automation, and data acquisition systems.

The :adi:`AD3530R` and :adi:`AD3531R` variants add a 2.5 V, 5 ppm/°C
internal voltage reference (disabled by default); the base :adi:`AD3530` and
:adi:`AD3531` use an external reference only. All variants operate from a
single 2.7 V to 5.5 V supply and include integrated multiplexers for
monitoring output voltages, output currents, and internal die temperature.
The evaluation board also includes an on-board :adi:`ADR4525` precision
voltage reference. The EVAL-AD3530RARDZ interfaces to a PC via an
:adi:`EVAL-SDP-CK1Z` system demonstration platform board and is controlled
using :adi:`ACE` software. A 12-pin SPI PMOD connector (P5) also allows
direct connection to microcontrollers, without requiring the SDP-K1.

The devices guarantee monotonic operation by design, incorporate power-on
reset (POR) circuits, and offer power-down modes that reduce current
consumption to 670 μA typical. The SPI-compatible, 4-wire serial interface
supports clock rates up to 50 MHz and IOVDD levels as low as 1.08 V.

Features:

- 16-bit voltage output DAC: 8-channel (AD3530R) or 4-channel (AD3531R)
- Single 2.7 V to 5.5 V supply range
- Internal 2.5 V references; output voltages of 2.5 V or 5 V
- Ultra-low output headroom for improved system efficiency
- Compact WLCSP package optimized for QSFP-DD and OSFP form factors
- SPI-compatible serial interface
- On-board :adi:`ADR4525` precision voltage reference
- Flexible power input: USB-C connector, terminal block, or SDP-K1
- Configurable link options (JP1–JP5) for supply, reference, and
  level-shifter settings
- PMOD connector for standalone microcontroller use

Applications:

- Optical transcievers
- Industrial automation and control systems
- Data acquisition systems
- Test and measurement equipment

.. figure:: ./images/eval_ad3530R.jpeg
   :alt: EVAL-AD3530R evaluation board top view
   :align: center
   :width: 800

   EVAL-AD3530R evaluation board

.. toctree::
   :hidden:
   
   prerequisites
   quickstart/index
   user-guide

Following the documented flow provides a much better experience. If you have
questions, ask on our :ez:`fpga` community forum, but please read the
documentation thoroughly first.

To evaluate the :adi:`AD3530R`, use the :adi:`EVAL-AD3530R` evaluation board
together with the :adi:`EVAL-SDP-CK1Z` SDP-K1 controller board and the
:adi:`ACE` software. For FPGA-based designs, the HDL reference design
supports the CoraZ7s, DE10-Nano, and ZedBoard carriers.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board and HDL reference design:

   #. :ref:`Prerequisites <eval-ad353xr prerequisites>` - what you need
      to get started
   #. :ref:`Quick start guides <eval-ad353xr quickstart>`:

      #. Using the :ref:`CoraZ7s <eval-ad353xr quickstart coraz7s>`
      #. Using the :ref:`DE10-Nano <eval-ad353xr quickstart de10nano>`
      #. Using the :ref:`ZedBoard <eval-ad353xr quickstart zed>`

#. Design with the AD3530R

   #. About the device driver:

           - :external+linux:ref:`AXI ADC HDL Linux driver <axi-adc-hdl>`
           - :external+linux:ref:`AXI-DMAC DMA Controller Linux driver <axi-dmac>`
           - :external+linux:ref:`AXI_ADXCVR High-speed transceivers Linux driver <axi_adxcvr>`
           - :external+linux:ref:`JESD204B Receive Linux driver <axi_jesd204_rx>`

#. About the JESD204 utilities:

   - :external+linux:ref:`JESD204 (FSM) interface Linux Kernel framework <jesd204-fsm-framework>`

#. :ref:`Help and Support <help-and-support>`

.. _eval-ad353xr block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: ./images/eval_ad3530R_bd.jpeg
   :alt: Block diagram of the AD3530R HDL reference design
   :align: center
   :width: 800

   AD3530R HDL reference design block diagram

.. figure:: ./images/eval_ad3531R_bd.jpeg
   :alt: Block diagram of the AD3531R HDL reference design
   :align: center
   :width: 800

   AD3531R HDL reference design block diagram

Resources
-------------------------------------------------------------------------------

- :adi:`AD3530/AD3530R Datasheet <media/en/technical-documentation/data-sheets/ad3530_ad530r.pdf>`
- :adi:`AD3531/AD3531R Datasheet <media/en/technical-documentation/data-sheets/ad3531-ad3531r.pdf>`
- :adi:`UG-2276: EVAL-AD3530R User Guide <media/en/technical-documentation/user-guides/eval-ad3530r-ug-2276.pdf>`
- :adi:`UG-2320: EVAL-AD3531R User Guide <media/en/technical-documentation/user-guides/eval-ad3531r-ug-2320.pdf>`

Warning
-------------------------------------------------------------------------------

.. esd-warning::
