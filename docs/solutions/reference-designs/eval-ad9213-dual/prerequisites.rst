.. _eval-ad9213-dual prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need
to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The :adi:`EVAL-AD9213-DUAL-EBZ` evaluation board
#. `Intel Stratix 10 SX SoC Development Kit (1SX280HU2F50E1VGAS) <https://docs.altera.com/r/docs/683303/current/stratix-10-sx-soc-development-kit-user-guide/overview>`__
#. RF Power Splitter for splitting the test tone to apply two equal signals
   to each of the two ADCs
#. Phase matched coaxial cables to connect the power splitter to the ADC
   input board connectors
#. RF Balun for single-ended-to-differential conversion of the 500 MHz
   reference clock signal, if your signal generator does not have a
   differential output
#. Coax cables for the 500 MHz reference clock connections
#. Signal generators:

   - Analog signal source: frequency and power requirements depend on the
     tests to be performed; a bandpass filter is often used for single tone
     tests
   - 500 MHz Reference Clock source: should have very low phase noise and be
     capable of supplying a 5 dBm 500 MHz clock signal

#. PC running Windows with at least 2 USB ports and an Ethernet port, and
   the following cables to connect to it:

   - One mini-USB cable
   - One micro-USB cable
   - One Ethernet cable

Software prerequisites
-------------------------------------------------------------------------------

The following software must be installed on the host PC:

- Intel Quartus Prime Programmer 19.3
- A serial terminal application (e.g. PuTTY, minicom, or screen)
- :ref:`iio-oscilloscope`
- :adi:`VisualAnalog <en/resources/interactive-design-tools/visualanalog.html>`

  - VisualAnalog Canvas for AD9213-DUAL-EBZ (supplied by ADI)
  - libiio (required for using the IIO Client block in the provided
    VisualAnalog Canvas)
  - IIO Plugin for VisualAnalog


.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.
