.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0577

.. _eval-cn0577-fmcz:

EVAL-CN0577-FMCZ
===============================================================================

Analog Front End and Digital Interface for Serial LVDS SAR ADCs.

.. image:: images/ltc2387-18-chip-illustration.png
   :align: left
   :width: 150

Overview
-------------------------------------------------------------------------------

Instrumentation applications such as flow cytometry, optical pulse measurement,
fast control loops, fast digital distortion correction, and image sensor
digitization present unique data acquisition challenges. These applications
often require a combination of high sample rate, high linearity, low drift, low
noise, and low latency.

The :adi:`EVAL-CN0577-FMCZ <CN0577>` is an 18-bit, 15 MSPS, 2 ppm linear data
acquisition system with an easy to drive input impedance of 1.1 kΩ. The analog
input range is 8.096 V peak-to-peak and can be driven in either single-ended or
differential mode, providing flexibility for many different applications.

The circuit is in field programmable gate array (FPGA) mezzanine card (FMC) form
factor, powered with 12 V either from the FMC connector or an external supply.
The digital interface uses serial low voltage differential signaling (LVDS),
minimizing the input/output requirements and enabling easy integration with
other FPGA designs.

A separate data clock eases the timing requirements of the host FPGA. An
on-board 120 MHz clock is forwarded to the FPGA and a CONVERT retiming flip-flop
reduces jitter from the convert signal of the FPGA.

Features:

- 15 MSPS Throughput Rate
- Guaranteed 18-Bit, No Missing Codes
- No Pipeline Delay, No Cycle Latency
- 96 dB SNR (Typical)
- 164.5 dB dynamic range
- 2 ppm INL (Typical)
- Serial LVDS Digital Interface
- Flexible analog input drive (single-ended or differential mode)
- On-board 120 MHz precision voltage-controlled crystal oscillator
  (VCXO)

Applications:

- Flow cytometry
- Optical pulse measurement
- Fast control loops
- Fast digital distortion correction
- Image sensor digitization

.. figure:: images/cn0577_1.jpg
   :align: right
   :width: 600px

   EVAL-CN0577-FMCZ Board

.. toctree::
   :hidden:

   prerequisites
   user-guide
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined have a much better experience with
things. However, like many things, documentation is never as complete as it
should be. If you have any questions, feel free to ask on our :ez:`/`, but
before that, please make sure you read our documentation thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. :ref:`User guide <eval-cn0577-fmcz user-guide>`

   #. :ref:`Hardware guide <eval-cn0577-fmcz hardware-guide>`

      #. :ref:`Hardware configuration <eval-cn0577-fmcz hardware-configuration>`
      #. :ref:`Power supply <eval-cn0577-fmcz power-supply>`
      #. :ref:`Analog inputs <eval-cn0577-fmcz analog-inputs>`
      #. :ref:`Onboard clock reference <eval-cn0577-fmcz clock-reference>`
      #. :ref:`External clock reference option <eval-cn0577-fmcz external-clock>`
      #. :ref:`Schematic, PCB Layout, Bill of Materials <eval-cn0577-fmcz schematic>`

   #. :ref:`Software guide <eval-cn0577-fmcz software-guide>`

      #. :ref:`Connection <eval-cn0577-fmcz connection>`
      #. :ref:`IIO Commands <eval-cn0577-fmcz iio-commands>`
      #. :ref:`IIO Oscilloscope <eval-cn0577-fmcz iio-oscilloscope>`
      #. :ref:`Pyadi-IIO <eval-cn0577-fmcz pyadi-iio>`

#. :ref:`Quick start guides <eval-cn0577-fmcz quickstart>`

   #. :ref:`ZedBoard Quick start <eval-cn0577-fmcz quickstart zed>`

#. :ref:`Help and Support <help-and-support>`

.. _eval-cn0577-fmcz block-diagram:

Block diagram
-------------------------------------------------------------------------------

.. figure:: images/cn0577_block_diag.png

   CN0577 Simplified Block Diagram

.. figure:: images/sys_block_diag.png

   CN0577 System Block Diagram

Reference Demos & Software
-------------------------------------------------------------------------------

- :git-pyadi-iio:`/`
- :ref:`pyadi-iio`
- :ref:`iio-oscilloscope`
- :ref:`kuiper`
- :external+hdl:ref:`cn0577`

More Information and Useful Links
-------------------------------------------------------------------------------

- :adi:`CN0577 Circuit Note Page <CN0577>`
- :adi:`LTC2387-18 Product Page <LTC2387-18>`
- :adi:`ADR4520 Product Page <ADR4520>`
- :adi:`ADA4945-1 Product Page <ADA4945-1>`
- :adi:`ADN4661 Product Page <ADN4661>`
- :adi:`ADG3241 Product Page <ADG3241>`
- :adi:`LT3042 Product Page <LT3042>`
- :adi:`LT3080 Product Page <LT3080>`
- :adi:`LT3094 Product Page <LT3094>`
- :adi:`LT1931 Product Page <LT1931>`

Registration
-------------------------------------------------------------------------------

Receive software update notifications, documentation updates, view
the latest videos, and more when you register your hardware.
`Register <https://my.analog.com/en/app/registration/hardware/EVAL-CN0577-FMCZ?&v=RevB>`__
to receive all these great benefits and more!

HDL Reference design
-------------------------------------------------------------------------------

The HDL Reference Design is documented at
:external+hdl:ref:`cn0577`.

Warning
-------------------------------------------------------------------------------

.. esd-warning::

.. _eval-cn0577-fmcz help-and-support:

Help and support
-------------------------------------------------------------------------------

For questions and more information, please visit the :ez:`/` technical support
community.
