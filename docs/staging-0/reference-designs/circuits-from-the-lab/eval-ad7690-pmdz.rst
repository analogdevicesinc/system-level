.. imported from: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/eval-ad7690-pmdz

.. _circuits-from-the-lab eval-ad7690-pmdz:

EVAL-AD7690-PMDZ PulSAR ADC PMOD User Guide
===========================================

The EVAL-AD7690-PMDZ offers a very high performance of 18 bits with a throughput
of 400 kSPS in a PMOD form factor. It is designed to demonstrate the performance
of :adi:`AD7690` and to provide an easy digital interface for a variety of
system applications.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/pulsar_pmod.jpg
   :width: 500px

The :adi:`AD7690` is an 18-bit, successive approximation, analog to digital converter (ADC) that operates from a single power supply, VDD. It contains a low-power, high-speed, 18-bit sampling ADC with no missing codes, an internal conversion clock, and a versatile serial interface port. .. note::

   * The throughput of your PulSAR ADC will be limited to the SPI bus speed of your platform.

Hardware Setup
--------------

The PMOD board is small in size with dimensions approximately 1 inch in width by
3 inches in length.

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

Typically, when using a PMOD board the power for the module comes directly from
the host board it is connected to. The power is generally capable of providing
up to 100 mA at 3.3V, and for complete power specifications please
`click here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`__.

In the case of the high precision, successive approximation ADC"s architecture,
it was required to provide low noise external power supplies to obtain datasheet
results. The :adi:`AD7690` ADC is driven by precision amplifiers which are also
optimized for noise and power. In order to enable those amplifiers to provide
zero and full-scale inputs to the ADC, power supplies above and below the ADC
input range were needed.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/pmod_power_supplies.png
   :width: 500px

With all these factors combined, the board was designed using external power
supplies of -2.5V, GND, and 7.5V. These supplies provide the power for the
entire PMOD board, so even though power is coming in through the PMOD connector,
it"s not actually powering the components on the board.

Input Connectors
~~~~~~~~~~~~~~~~

For the input signals coming into the
:adi:`EVAL-AD7690-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7690-pmdz.html>`,
SMB connectors were chosen to help minimize the noise at the input. There are
two (2) SMB connectors per board, and that"s because there are both positive(+)
and negative(-) inputs to each converter. This will provide the user with the
cleanest input signal possible, and fully utilize the resolution and speed of
the converters.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/vin.png
   :width: 500px

Each of the converters also has a combination of single-ended inputs,
differential inputs, or pseudo-differential inputs. So in order to determine the
input style of your converter it is imperative to look at the datasheet of the
device you are using. The datasheet of any device should always be followed
before using it in an application or on a board.

Digital Interface (PMOD)
~~~~~~~~~~~~~~~~~~~~~~~~

The PMOD interface is a series of standardized digital interfaces for various
digital communication protocols such as SPI, I2C, and UART. These interface
types were standardized by Digilent, which is now a division of National
Instruments. Complete details on the PMOD specification can be found
`here <https://www.digilentinc.com/Pmods/Digilent-Pmod_%20Interface_Specification.pdf>`__.

The specific interface used for the PulSAR PMOD boards is the extended SPI. In
general, ADI has adopted the extended SPI connector for all PMOD devices which
have an SPI interface. It provides flexibility to add interrupts, general
purpose I/O, resets, and other important digitally controlled functions.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/pulsar_pmod/pmod_pinout.png
   :width: 700px

Above is the connection of the
:adi:`EVAL-AD7690-PMDZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7690-pmdz.html>`
to the SPI PMOD connector. It is hardware configured in a 3-wire mode with no
busy indicator. This basically means that the only signals that go between the
converter and the processor are the CNV (similar to a chip select in this mode),
SCLK (serial Clock), and MISO (serial data out). There are no registers internal
to the :adi:`AD7690` ADC, so there is no need for a data input line, the data
just streams out using the CNVST pin.

More information and Useful links
---------------------------------

- :adi:`AD7690 Product Page <AD7690>`
- :adi:`EVAL-AD7690-PMDZ Product Page <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/eval-ad7690-pmdz.html>`
- :git-precision-converters-firmware:`EVAL-AD7690-PMDZ No-OS Driver <tree/main/projects/ad7689_iio+>`

Schematics, PCB Layout, Bill of Materials
-----------------------------------------

.. admonition:: Download

   - :adi:`AD7690 Datasheet <media/en/technical-documentation/data-sheets/AD7690.pdf>`
   - :adi:`EVAL-AD7690-PMDZ Design & Integration Files <media/en/evaluation-documentation/evaluation-design-files/eval-ad7690-pmdz-designsupport.zip>`

Additional Information
----------------------

- `pyADI-IIO <https://github.com/analogdevicesinc/pyadi-iio>`__
- :dokuwiki:`PyADI-IIO Installation Guide </resources/tools-software/linux-software/pyadi-iio>`
- :dokuwiki:`IIO Oscilloscope Installation Guide </resources/tools-software/linux-software/iio_oscilloscope>`
- :ref:`kuiper`

Registration
------------

.. tip::

   Receive software update notifications, documentation updates, view the latest
   videos, and more when you register your hardware.
   :reg:`Register <EVAL-AD7690-PMDZ?&v=Rev A>` to receive all these great
   benefits and more!
