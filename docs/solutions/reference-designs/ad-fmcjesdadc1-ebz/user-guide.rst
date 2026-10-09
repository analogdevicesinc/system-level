.. _ad_fmcjesdadc1_ebz user-guide:

User guide
===============================================================================

.. warning::

   The :adi:`AD-FMCJESDADC1-EBZ` is a **legacy product**
   and is no longer actively supported. This documentation is provided for
   reference only.

.. _ad_fmcjesdadc1_ebz hardware-guide:

Hardware guide
-------------------------------------------------------------------------------

Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-FMCJESDADC1-EBZ board's primary purpose is to easily
understand, validate, and verify the JESD204B interface with various
manufacturers' FPGAs (designs available for Altera and Xilinx).

When fitting into the small FMC form factor, various tradeoffs were made that
limit performance to the first Nyquist zone. These tradeoffs in
size/power/performance are normally the things that Analog Devices advises
customers to avoid in order to achieve maximum performance.

Clocking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD-FMCJESDADC1-EBZ uses the :adi:`AD9517-1`, a small (7.0 mm x 6.75 mm),
low power (~1.4 W) multi-output clock distribution IC with subpicosecond
jitter performance, along with an on-chip PLL and VCO. It is driven by a
single 30.72 MHz crystal and generates the necessary clocks for the system:
2.45760 GHz, 245.760 MHz, and 30.72 MHz.

The ADIsimCLK tool provides the following data about the clocking system on the
245.760 MHz (which drives the AD9250) outputs:

.. image:: images/snr_vs_if.png
   :align: right
   :width: 300

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

This matches up with the datasheet when using the internal VCO. To improve
this number, an external VCXO could have been used (would decrease the jitter
to ~54 fs rms), but this would have increased the size and violated the height
requirements of the FMC specification.

Analog Front End
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD9250 datasheet and the golden evaluation board recommend a Differential
Double Balun Input Configuration (Figure 41 in the datasheet), with this note:

.. important::

   From the AD9250 Datasheet: At input frequencies in the second Nyquist zone
   and above, the noise performance of most amplifiers is not adequate to
   achieve the true SNR performance of the AD9250. For applications where SNR
   is a key parameter, differential double balun coupling is the recommended
   input configuration (see Figure 41).

The AD-FMCJESDADC1-EBZ uses a single differential transformer
(`Minicircuits TC4-1W <http://www.minicircuits.com/pdfs/TC4-1W.pdf>`_) -
as shown in Figure 40 of the datasheet - due to its smaller size. The
specific transformer is specified from 3 to 800 MHz, but is only linear
(±0.5 dB insertion loss/input return loss) from 10 to 100 MHz, limiting
operation to the first Nyquist zone before the converter sees significant
losses on the input side.

This transformer was chosen as a good trade-off of size (3.8 mm x 3.8 mm x
3.8 mm), power (250 mW RF), and secondary/primary impedance ratio (4:1)
suitable for the first Nyquist zone.

.. _ad_fmcjesdadc1_ebz software-guide:

Software guide
-------------------------------------------------------------------------------

Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+linux:ref:`AD9250 AXI Linux driver <axi-adc-hdl>`
- :external+linux:ref:`JESD204B/C Receive Linux driver <axi_jesd204_rx>`
- :external+linux:ref:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux
  driver <axi_adxcvr>`
- :external+kuiper:doc:`Kuiper Linux <index>`

Help & Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. hint::

   - :external+hdl:ref:`build_hdl` contains all the documentation, build
     instructions and register map tables.
   - Browse the HDL GitHub repository:
     :git-hdl:`library components <library>`
     and :git-hdl:`projects <projects>`.
   - Questions? Ask on:

     - :ez:`FPGA/HDL questions <community/fpga>` (or ask on
       `Xilinx Forums <http://forums.xilinx.com/>`_ /
       `Altera Forums <http://www.alteraforums.com/>`_)
     - :ez:`Linux Software Driver questions
       <community/linux-device-drivers/linux-software-drivers>`
     - :ez:`No-OS Driver questions
       <community/linux-device-drivers/microcontroller-no-os-drivers>`
     - :ez:`AD9250 general questions <community/data_converters/high-speed_adcs>`
