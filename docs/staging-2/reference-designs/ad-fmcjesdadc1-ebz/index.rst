.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcjesdadc1-ebz

.. _ad-fmcjesdadc1-ebz:

AD-FMCJESDADC1 FMC Board
========================

The :adi:`AD-FMCJESDADC1-EBZ` is a high speed data acquisition (4 channels at
245.76 MSPS), in a FMC form factor which supports the JESD204B high speed serial
interface. This board is one of the few boards that meet all the FMC
specifications in terms of mechanical size, and mounting hole locations. For
that information, please refer to the FMC specification.

Although this board does meet the FMC specifications, it is not meant as a
`commercial off the shelf <https://en.wikipedia.org/wiki/Commercial_off-the-shelf>`__
(COTS) board. If you want a commercial, ready to integrate product, please refer
to one of the many FMC manufactures, like
`Abaco <https://www.abaco.com/products/fmc176-fpga-mezzanine-card>`__.

This board is targeted to use the ADI reference designs, and work with both
Altera and Xilinx development systems. ADI provides complete source (HDL and
software) to re-create those projects (minus the IP provided by the FPGA
vendors, which we use), but may not provide enough info to port this to your
custom platform.

The analog I/O on this board, uses the
`micro-miniature coaxial <https://en.wikipedia.org/wiki/MMCX_connector>`__
connector. To connect to a SMA based test equipment, you will need something
like the :digikey:`Molex 89761-6810 <0897616810>`.

Contains
--------

The card contains:

- :adi:`AD9250` two 14-bit ADC with sampling speeds of up to 250 MSPS, with a
  :adi:`JESD204B <JESD204>` digital interface.
- :adi:`AD9517-1`, a multi-output clock distribution device with subpicosecond
  jitter performance, along with an on-chip PLL and VCO.
- :adi:`ADP151` an ultralow noise, low dropout linear regulator that operates
  from 2.2 V to 5.5 V and provides up to 200 mA of output current.
- :adi:`ADP1753` a low dropout linear regulators that operate from 1.6 V to 3.6
  V and provide up to 800mA of output current.
- :adi:`AD7291` a 12-bit, low power, 8-channel, successive approximation
  analog-to-digital converter (ADC) with an internal temperature sensor.
- :adi:`ADP2301` is a compact, constant-frequency, current-mode, step-down
  dc-to-dc regulators with integrated power MOSFET. A precise, low voltage
  internal reference makes these devices ideal for generating a regulated output
  voltage as low as 0.8 V, with ±2%
- :adi:`ADG3304` is a bidirectional logic level translator that contains four
  bidirectional channels.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcjesdadc1-ebz/ad-fmcjesdadc1-ebz_bottom.png
   :width: 395px

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcjesdadc1-ebz/ad-fmcjesdadc1-ebz_top.png
   :width: 400px

FPGA Code
---------

The :external+hdl:ref:`fmcjesdadc1` can be found on the wiki.

Eye Scan
--------

Eye scan or this board can be found at
:dokuwiki:`/resources/tools-software/linux-software/jesd_eye_scan </resources/tools-software/linux-software/jesd_eye_scan>`.

Linux
-----

- :dokuwiki:`AD9250 Linux driver </resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
-
  :dokuwiki:`JESD204B/C Receive Linux Driver </resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`:
  Linux driver for the JESD204B receive core.
- :dokuwiki:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
- :dokuwiki:`ZC706 Linux image </resources/tools-software/linux-software/zynq_images>`
- :dokuwiki:`Linux on the KC705, VC707 </resources/eval/user-guides/ad-fmcjesdadc1-ebz/quickstart/microblaze>`

Specifications
--------------

The AD-FMCJESDADC1-EBZ board"s primary purpose is to easily
understand/validate/verify the JESD204B interface with various manufactures
FPGA"s (We have designs for Altera and Xilinx).

When putting things into the small FMC form factor, various tradeoffs were made
which limit the performance to the first nyquist. These tradeoffs in
size/power/performance are normally the things that Analog Devices tells its
customers not to do to get maximum performance.

Clocking
--------

The AD-FMCJESDADC1-EBZ uses the :adi:`AD9517-0`. This is a small (7.0mm x
6.75mm), low power (~1.4W) multi-output clock distribution function with
subpicosecond jitter performance, along with an on-chip PLL and VCO. It"s driven
by a single 30.72 MHz crystal, and generates the necessary clocks for the system
(2.45760GHz, 245.760MHz, 30.72MHz).

The ADIsimCLK tool provides the following data about the clocking system on the
245.760MHz (which drive the AD9250) outputs:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcjesdadc1-ebz/snr_vs_if.png
   :width: 300px

::

   Broadband Jitter (>1kHz) = 516fs (rms)
      SNR = 69.79dB ENOB = 11.63bits
      at IF Freq = 100 MHz
   Integrated Phase Noise from 100kHz to 1.25MHz
     Timing Jitter = 304fs rms
     Phase Jitter EVM = 0.05% rms
     Phase Jitter = 0.027 degrees rms
     ACI/ACR = -69.6dBc
   Delay from Ref to OUT2 is 420ps

This matches up with the datasheet when using the internal VCO. To improve this
number, a external VCXO could have been used (would decrease the jitter to ~54
fs rms), but this would have increased the size, and violated the height
requirements of the FMC specification (most VCXO"s which good performance are
tall).

This is the key aspect of any good converter design - the clock source.

Front End
---------

The datasheet for the AD9250 and the golden evaluation board recommend a
Differential Double Balun Input Configuration (figure 41 in the datasheet), with
this note:

.. important::

   **From the AD9250 Datasheet:**

   *At input frequencies in the second Nyquist zone and above, the noise
   performance of most amplifiers is not adequate to achieve the true SNR
   performance of the AD9250. For applications where SNR is a key parameter,
   differential double balun coupling is the recommended input configuration
   (see Figure 41).*

The AD-FMCJESDADC1-EBZ card uses a single differential transformer
(`Minicircuits TC4-1W <http://www.minicircuits.com/pdfs/TC4-1W.pdf>`__) - as
shown in figure 40 of the datasheet - due to its smaller size (reduced
footprint). The specific transformer used is specified from 3 to 800 MHz, but is
only linear (in terms of insertion loss/input return loss) +/- 0.5dB, from 10 to
100MHz (limiting things to the first nyquist, before the converter sees massive
losses on the input side.

This transformer was chosen as a good trade off of size (3.8mm x 3.8mm x 3.8mm),
Power (250mW of RF), with (Secondary/Primary) impedance (4:1) which operates in
the first nyquist.

Schematic/Layout
----------------

Downloads
~~~~~~~~~

.. admonition:: Download

   - :download:`https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcjesdadc1-ebz/ad-fmcjesdadc1_r1.1.pdf`

   - We are not releasing the gerbers of this board - since the :adi:``golden``
     reference design is the AD9250 Evaluation board, which can be found at the
     `AD9250 <ad9250#product-evaluationkits>` page.

Support
-------

If you have any questions regarding the AD-FMCJESDADC1-EBZ board or are
experiencing any problems while using the board or following the user guides
feel free to ask us a question. Questions can be asked on our
`EngineerZone support community <https://ez.analog.com/>`__. Calling on the phone, emailing someone
directly, will only cause things to get answered in much slower manner.

HDL / Hardware Questions
~~~~~~~~~~~~~~~~~~~~~~~~

For questions regarding the AD-FMCJESDADC1-EBZ hardware or the HDL reference
design please state them in the :ez:`FPGA Reference Designs <community/fpga>`
sub-community. If you have questions about the tools, please go ask the tools
vendors:

- `Xilinx Forums <http://forums.xilinx.com/>`__
- `Altera Forums <http://www.alteraforums.com/>`__

Linux Driver or Application Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For questions regarding the the ADI Linux distribution, the Linux drivers, or
the device trees for the AD9250 based platforms, please use the
:ez:`Linux Software Drivers <community/linux-device-drivers/linux-software-drivers>`
sub-community.

If you have generic userspace questions (*how do I use a standard linux tool*),
we should suggest to use your favorite `search tool <http://www.google.com/>`__
to find that tool/utility/application support method (some use email, some use
web). If you think you have found a bug specific to ARM, please
`report this upstream <https://www.linaro.org/support/>`__.

No-OS Questions
^^^^^^^^^^^^^^^

For questions regarding the no-OS drivers for AD9250, please use the
:ez:`Microcontroller and No-OS Driver <community/linux-device-drivers/microcontroller-no-os-drivers>`
sub-community.

General AD9250 Questions
^^^^^^^^^^^^^^^^^^^^^^^^

Questions about the AD9250, please use the
:ez:`AD9250 <community/data_converters/high-speed_adcs>` sub-community.
