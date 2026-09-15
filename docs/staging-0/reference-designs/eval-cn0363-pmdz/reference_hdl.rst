.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-cn0363-pmdz/reference_hdl

.. _eval-cn0363-pmdz reference_hdl:

EVAL-CN0363-PMDZ HDL Reference Design
=====================================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page
   is outdated and the new one can be found at
   https://analogdevicesinc.github.io/hdl/projects/cn0363/index.html

Functional Overview
-------------------

The EVAL-CN0363-PMDZ HDL reference design is based on the Analog Devices base
reference design for the ZED board. In addition to the base reference design
:adi:`EVAL-CN0363-PMDZ` HDL reference design implements function blocks to
communicate over a SPI bus with the :adi:`AD7175-2 SigmaDelta ADC <AD7175-2>` to
configure it and receive the raw ADC data as well a configure the
:adi:`AD5201 digital potentiometer <AD5201>`. The data received from the ADC is
passed to a processing pipeline which performs a digital synchronous detector
and finally write the data to system memory using a DMA. The HDL reference
design is also responsible for generating the LED excitation signal. A
simplified functional block diagram of the system is given below.

.. figure:: https://wiki.analog.com/_media/resources/tools-software/linux-software/colorimeter_block_diagram.png

Supported Devices
-----------------

- :adi:`CN0363`

Supported Carriers
------------------

- `Zed Board <http://zedboard.org/product/zedboard>`__

Files
-----

.. list-table::
   :header-rows: 1

   * - Name
     - Description
     -
   * - :git-hdl?master/projects/cn0363/zed/system_project.tcl:`/`
     - Vivado IP integrator project script
     -
   * - :git-hdl?master/projects/cn0363/zed/system_bd.tcl:`/`
     - Vivado IP integrator board definition script
     -
   * - :git-hdl?master/projects/cn0363/zed/system_constr.xdc:`/`
     - System constraints file
     -
   * - :git-hdl?master/projects/cn0363/zed/system_top.v:`/`
     - Top-level project HDL module
     -
   * - :git-hdl?master/projects/cn0363/zed/filters/hpf.mat:`/`
     - High-pass filter
     -
   * - :git-hdl?master/projects/cn0363/zed/filters/lpf.mat:`/`
     - Low-pass filter
     -

FPGA Reference Designs on GitHub :

.. admonition:: Download

   **Vivado Downloads**

   - Main repository with latest changes (always synced with the latest release)

     - :git-hdl

   - Releases (the used tool version can be found in README.md)

     - https::`/github.com/analogdevicesinc/hdl/tree/hdl_2015_r1+`

Base reference design
---------------------

The EVAL-CN0363-PMDZ HDL reference design is built on-top the standard Analog
Devices base HDL reference design for the ZED board. The base reference design
implements basic input and output connectivity to the ZED board, like USB,
HDMI-out and audio support. It also instantiated the Xilinx PS7 processing
system which contains a dual core ARM A9 applications processor which is used
for running software corresponding to the reference design.

SPI communication
-----------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cn0363-pmdz/cn0363_hdl_spi.png

To implement the SPI communication logic for the EVAL-CN0363-PMDZ HDL reference
design the
:dokuwiki:`SPI Engine framework </resources/fpga/peripherals/spi_engine/>` is
used. This allows the flexibility to access all configuration registers for both
connected SPI devices dynamically from software as well as allowing low-latency
and high-throughput automated access to the SPI bus when capturing sample data
from the ADC.

The :dokuwiki:`SPI-Engine AXI </resources/fpga/peripherals/spi_engine/axi>` core
in the design is mapped into the system"s peripheral memory bus via a AXI-Lite
bus and be accessed by the CPU. It"s interrupt signal is also connected to the
processing system. The SPI-Engine AXI core controls the renaming part of the
SPI-Engine cores used in the design and it has primarily two functions. One is
to give direct access to the SPI bus which is used to configure the
configuration registers of the SPI devices. The other is to configure and
control the SPI-Engine offload core.

The
:dokuwiki:`SPI-Engine interconnect </resources/fpga/peripherals/spi_engine/interconnect>`
core is used to give both the SPI-Engine AXI and SPI-Engine offload core access
to the SPI-Engine execution core. The SPI-Engine offload core is connected to
the first interconnect slave port, which means it has priority over the
SPI-Engine AXI core. This is done because reading the ADC result data is timing
critical while changing the configuration registers is typically not.

The :external+hdl:ref:`spi_engine offload` core is used to read the ADC result
data and feeds the received data into the processing pipeline. Software is
responsible for setting up the core with the correct SPI message to read the ADC
result register as well as enable the core when the ADC converter is active.
Once the core has been set up and enabled the stored SPI message will be
executed when the data ready (RDY) signal from the ADC is detected.

The :external+hdl:ref:`spi_engine offload` core is responsible for handling the
low level SPI bus access. It accepts the SPI-Engine commands from the SPI-Engine
AXI and SPI-Engine offload core and handles them accordingly.

The
:dokuwiki:`SigmaDelta SPI </resources/fpga/peripherals/util_sigma_delta_spi>`
core is responsible for monitoring the low-level SPI bus and extracting the data
ready from the bus which is multiplexed over the same physical wire as the SPI
MISO signal. The data ready signal is connected to the SPI-Engine offload core
which starts to read the ADC conversion result when the signal is asserted. It
is also connected to the processing pipeline which takes a snapshot of the
current phase of the excitation signal when the data ready signal is asserted.
This allows precise time-stamping of the excitation signal phase in relation to
the time when the ADC conversion was performed.

Synchronous detector processing pipeline
----------------------------------------

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-cn0363-pmdz/cn0363_hdl_processing.png

The first block in the EVAL-CN0363-PMDZ processing pipeline is the
:dokuwiki:`cn0363_phase_data_sync </resources/fpga/peripherals/cn0363/phase_data_sync>`
core. It takes a snapshot of the phase counter when a rising edge is detected on
conversion done signal. It will then wait for the corresponding data sample to
be read from the ADC by the SPI block. Once both data and phase are ready they
will be given to the next step in the processing pipeline. The core also
converts the ADC data from offset binary to two"s complement signed format.

As the next step the ADC data is sent through a high-pass filter which is
configured to remove noise below 50 Hz and any DC components.

After that the output data from the high-pass filter and the phase corresponding
phase data is send through a
`CORDIC de-modulator <https://en.wikipedia.org/wiki/CORDIC>`__. The CORDIC
de-modulator will calculate the result of the data multiplied by both the cosine
and sine of the phase. The output is the demodulated in-phase (I) and quadrature
(Q) components data corresponding to the original input signal.

The I and Q components are send into a low-pass filter with a small pass band
which is used to remove frequency components which are different from the
excitation frequency.

The final block in the processing pipeline is a
:dokuwiki:`sequencer block </resources/fpga/peripherals/cn0363/sequencer>` which
cycles through the initial input data, the intermediate results and the final
processing result and sends them to the DMA controller which will copy them to
system memory. Each of sequencer channels can be independently enabled or
disabled. If a channel is discarded and not send to the DMA. During normal
operation typically all but the final processing results are discarded.

The various broadcasting blocks in the processing pipeline are used to forward
the data to the next processing element of the pipeline as well as to the
sequencer which sends them to the DMA. The later allows to inspect the
intermediate results of the processing pipeline.

Both filters are configured in a time-division-multiplexing configuration. This
means for each channel (2 for the high-pass filter and 4 for the low-pass
filter) there is a storage for saving the filter inputs, but the logic for
calculating the filter output as well as the coefficients are shared between
each channel. This is possible since the ADC is running at a output data rate of
50 kHz while the FPGA pipeline is running at 100 MHz. Which gives about 2000
clock cycles to process each high-pass filter result and 1000 clock cycles for
each low-pass filter result.

Building the Design
-------------------

For building the EVAL-CN0363-PMDZ HDL reference design follow the
:dokuwiki:`default instruction for building Analog Devices' HDL reference designs </resources/fpga/docs/hdl#building_hdl>`.

More Information
----------------

- EVAL-CN0363-PMDZ User Guide
