.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/reference_hdl

.. _ad-fmcomms2-ebz reference_hdl:

AD9361 HDL Reference Designs
============================

.. important::

   We are in the process of migrating our documentation to GitHubIO.

   This page is outdated and the new one for FMCOMMS2/3/4 can be found at
   https://analogdevicesinc.github.io/hdl/projects/fmcomms2/index.html and for
   FMCOMMS5 at
   https://analogdevicesinc.github.io/hdl/projects/fmcomms5/index.html

Functional Overview
-------------------

The reference design is a processor based (ARM,
`MicroBlaze <https://en.wikipedia.org/wiki/MicroBlaze>`__, or
`NioS <https://en.wikipedia.org/wiki/Nios_II>`__) embedded system. A functional
block diagram of the system is given below. The device interface is a
self-contained peripheral similar to other such pcores in the system. The core
is programmable through an AXI-lite interface. The data path consists of a VDMA
and DMA interface for the transmit and receive path respectively.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/cf_ad9361_zc706_bd.jpg
   :width: 600px

Digital Interface
-----------------

The digital interface consists of 12bits of DDR data and supports full duplex
operation in all configurations up to 2x2. The transmit and receive data paths
share a single clock. The data is sent or received based on the configuration
(programmable) from separate transmit and to separate receive chains.

Transmit
--------

In the transmit direction, complex I and Q signals are generated for each RF.
The digital source could either be an internal DDS or from the external DDR via
VDMA. The internal DDS phase and frequency are programmable.

Receive
-------

In the receive direction, each component of the delineated data is passed to a
PN monitor. The monitors validates the digital interface signal capture and
timing. The data then optionally DC-filtered, corrected for I/Q offset and phase
mismatches and is written to the external DDR memory via DMA. An optional
off-line FFT core may be used to generate a spectrum plot.

Control and SPI
---------------

The device control and monitor signals are interfaced to a GPIO module. The SPI
signals are controlled by a separate AXI based SPI core.

Multi-Cores Operation (ADFMCOMMS5)
----------------------------------

The core supports multiple instances of the same synchronized to a common clock.
The ADFMCOMMS5 uses two instances of this core synchronized to a common clock.
The data is recovered in each individual clock domain and transfers the data to
a single clock domain. The multiple cores must all be using the same clock.

Supported Devices
-----------------

- :adi:`AD-FMCOMMS2-EBZ`
- :adi:`AD-FMCOMMS3-EBZ`
- :adi:`AD-FMCOMMS4-EBZ`
- :adi:`AD-FMCOMMS5-EBZ`
- :dokuwiki:`ARRADIO </resources/eval/user-guides/arradio>`
- :dokuwiki:`PicoZed SDR </resources/eval/user-guides/picozed_sdr>`

Supported Carriers
------------------

These are the supported carriers for the HDL - not the complete package
(software and HDL). Typically the software lags behind the HDL, so if you don"t
see the these listed on the main project page - it is not yet done.

For the FMCOMMS2, 3, 4 based boards, supported carriers include the Xilinx Zynq
based systems:

- :xilinx:`ZC702 <ZC702>`
- :xilinx:`ZC706 <ZC706>`
- `Zed Board <http://www.zedboard.org>`__

but it also works on the Xilinx fabric only solutions (for experts, who have
used the zynq based systems in the past).

- :xilinx:`KC705 <KC705>`
- :xilinx:`VC707 <VC707>`

For Altera SoC based systems and the ARRADIO board, we support
:dokuwiki:`ARRADIO </resources/eval/user-guides/arradio>` :

- `SoC Kit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`__

Download HDL
------------

.. note::

   Please note that the projects **FMCOMMS2**, **FMCOMMS3** and **FMCOMMS4** are
   using the :git-hdl:`same <projects/fmcomms2+>` hdl design. The **ARRADIO**
   Quartus project uses :git-hdl:`Arradio <projects/arradio/c5soc+>` hdl design.

.. todo:: .. include: /resources/fpga/docs/hdl/downloads_insert.rst

   :start-after: .. start-fmcomms2fmcomms3fmcomms4
   :end-before: .. end-fmcomms2fmcomms3fmcomms4

.. todo:: .. include: /resources/fpga/docs/hdl/downloads_insert.rst

   :start-after: .. start-fmcomms5
   :end-before: .. end-fmcomms5

.. todo:: .. include: /resources/fpga/docs/hdl/downloads_insert.rst

   :start-after: .. start-arradio
   :end-before: .. end-arradio

.. note::

   - Questions?
     :dokuwiki:`Ask Help & Support </resources/eval/user-guides/ad-fmcomms2-ebz/help_and_support>`.

Generating Xilinx netlist files
-------------------------------

The repository will not contain Xilinx netlist files, only Xilinx coregen xco
files are provided with the reference design. You must regenerate the IP core
files using this file. See
:dokuwiki:`generating Xilinx netlist/verilog files from xco files </resources/eval/user-guides/ad-fmcomms1-ebz/reference_hdl>`
for details.
