.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem

.. _ad-fmcomms2-ebz software matlab_bsp_modem:

QPSK Modem Design Workflow
==========================

.. warning::

   This example has been deprecated and only limited support is provided.
   :mw:`Please look at this example instead <help/comm/ug/hdlqpsktransmitterreceiver.html>`

The purpose of this project set is to demonstrate an example narrowband modem
design from simulation to complete standalone deployment utilizing the ADI
software/hardware infrastructure and the MathWorks toolset. The project includes
MATLAB floating point simulations, Simulink floating point models, and HDL
capable fixed point models of a QPSK modem design. They also include
integrations with SDR devices including PlutoSDR, FMComms2/3/4, and RFSOM for
real-world testing. All designs have been developed to communicate, over the air
if desired, with one another and share a common testing harness for validation.
Together, these designs demonstrate a true development cycle from simulation to
hardware deployment. For deployment, which is completely untethered from MATLAB
or Simulink, a specialized/custom reference design was created through ADI"s BSP
and demonstrates a video link with the PackRF kit.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/workflow.png
   :width: 800px

A detailed workflow that governs this model development is outlined in the
figure above, capturing the necessary steps from ideas to production ready
hardware. This flow has been explored previously in an
:adi:`article series about ADS-B <en/analog-dialogue/articles/using-model-based-design-sdr-1.html>`.

Source Outline
--------------

The modem project is available under the
:git-TransceiverToolbox:`TransceiverToolbox <tree/master/trx_examples/targeting/modem-qpsk+>`
repository
:downgit-TransceiverToolbox:`Zipfile  <trx_examples/targeting/modem-qpsk>`. The
code is structured in the following way:

- ``FixedPoint``: Fixed-point model IP and demos
- ``FloatingPoint``: Floating point mfiles and model IP
- ``test``: Testing harness and interfacing models for float and fixed libraries
- ``utils``: Useful scripts for managing project and environment

The main IP is provided in two libraries ``RxTxFixedPointLibrary.slx``,
``RxFloatingPointLibrary.slx``. These contain receiver and transmitter blocks
which are used in the demo models and testing harness. By using libraries,
blocks can be easily shared and maintained between models. The Fixed-Point
specific libraries models are shown below. These blocks maintain an array of
configuration for the internal designs as well as the necessary interfaces to
the AD9361 transceiver and DMA IP back to the ARM on the SDR itself.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/fixedrxtx.png
   :width: 400px

Theory of Operation
-------------------

The modem was designed as a constantly transmitting frequency division duplexing
(FDD) system with a single transmit channel (uplink) and single receive channel
(downlink), enabling a single point-to-point link between two nodes. The link
itself is a QPSK waveform which continuously transmits data so the target
receive can remain synchronized. When useful data is transmitted it is simply
modulated with some markers and training data known to the receiver. When no
useful data is to be transmitted, the transmitter will connect a LFSR to the
modulator and random data will be sent to the receiver.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/modem_basic.png
   :width: 400px

The system is designed in this way since it produces a relative steady state for
the AD9361"s AGC when the devices are nodes are stationary, and fits nicely with
the controlling IP logic of the AD9361 as well for the transmitter specifically.

The waveform or packet structure is outlined below. The packet contains a known
barker sequence used by correlators to detect a useful payload in the data
stream. Once found a DFE will utilize the following training data for channel
correction or any remaining synchronization. After the training data a 16 bit
header is inserted which is duplicated with all bits flipped for validation.
Currently only the payload length is contained in this header and is limited to
1600 bytes. Finally, the payload data is inserted which can be variable length
but must be a multiple of 8 bytes, which is the DMA word length used in the
final design. During the LFSR state random training data is transmitted.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/packet_structure.png
   :width: 600px

The receiver algorithmically is split into two main areas. The front-end, or
blind section, of the receiver is responsible for timing synchronization and
carrier recovery. These tasks are completed with PLL based algorithms that
continually estimate and correct for drift in the received signal. Connecting
the front-end to the downstream processing is a packet detector, which uses a
set of filters to correlate the known preamble signal with the incoming data.
Once a packet is detected, the second half of the receiver (the downstream
processing) is enabled starting with the DFE. The packet detector also provides
phase ambiguity correction of the QPSK signal through a filter bank.

The DFE initially has a training phase using known PN generated data, then
switches to a decision directed mode once the header appears. The header is
processed so the downstream decoding can be configured including the DMA. The
demodulated bits are then channel decoded, descrambled, and finally CRC checked
before being passed to the DMA. Once the packet has been fully processed the
packet detector will reset and the process for finding another packet will begin
again.

Support Devices and Required Software
-------------------------------------

The developed modem was specifically designed and tuned for the AD9361 using the
axi_ad9361 IP cores. The deployed and streaming models should function with:

- Streaming

  - ADI RF SOM 1x1 and 2x2
  - FMCOMMS 2/3/4 with Zed, ZC706, and ZC702
  - ADALM-PLUTO

- Targetting

  - ADI RF SOM 2x2
  - FMCOMMS 2/3/4 with ZC706

The developed designs implemented to show off different features for debugging
and development in the MATLAB and Simulink environments with ADI transceivers.
Therefore, different examples with require specific toolboxes and hardware
depending on use case.

The main dependencies across all example are :mw:`MATLAB <products/matlab/>`
version *2017b* or later, and your license needs to include the following
components:

- :mw:`Communications Toolbox <products/communications/>`
- :mw:`DSP System Toolbox <products/dsp-system/>`
- :mw:`Signal Processing Toolbox <products/signal/>`
- You can find what toolboxes you have by running the
  :mw:`ver <help/matlab/ref/ver.html>` command

When targeting the FPGA or streaming data, there are two options depending on
the hardware you have. Official MathWorks support is provided through the
:mw:`Communications Toolbox Support Package for Xilinx Zynq-Based Radio <hardware-support/zynq-sdr.html>`.
This Hardware Support Package (HSP) supports the following hardware:

- ADI RF SOM 2x2
- FMCOMMS 2/3/4 with ZC706 or Zedboard

Alternatively, ADI provides support for through the Analog Devices Board Support
Package (BSP) for the following boards:

- ADI RF SOM 1x1 and 2x2
- FMCOMMS 2/3/4 with Zed, ZC706, and ZC702
- PackRF
- FMCOMMS 5 with ZC706 and ZC702

The ADI BSP currently does not support External Mode unlike the MathWorks HSP.
*ADI recommends utilizing the MathWorks officially supported HSP if your board
is shared between both lists.*

.. list-table::
   :header-rows: 1

   * - Demo
     - Purpose
     - Toolboxes Required
     -
     -
     -
     -
     -
     -
     -
   * - EndToEndTest.m
     - Floating-Point MATLAB simulation with optional radio streaming
     - :mw:`Pluto HSP <hardware-support/adalm-pluto-radio.html>` or :mw:`Zynq SDR Support from Communications Toolbox <hardware-support/zynq-sdr.html>`
     -
     -
     -
     -
     -
     -
     -
   * - RadioReceiver.slx
     - Floating-Point Simulink simulation
     - :mw:`Simulink <products/simulink/>`
     -
     -
     -
     -
     -
     -
     -
   * - combinedTxRx_StandardIQ.slx
     - Fixed-Point Simulink deployable model
     - :mw:`Simulink <products/simulink/>`, :mw:`HDL Coder <products/hdl-coder/>`, :mw:`HDL Coder Support Package for Xilinx Zynq-7000 Platform <matlabcentral/fileexchange/40447-hdl-coder-support-package-for-xilinx-zynq-7000-platform>`, :mw:`Communications Toolbox Support Package for Xilinx Zynq-Based Radio <hardware-support/zynq-sdr.html>` or :dokuwiki:`Analog Devices BSP </resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`
     -
     -
     -
     -
     -
     -
     -
   * - combinedTxRx_ExternalMode.slx
     - Fixed-Point Simulink deployable model
     - :mw:`Simulink <products/simulink/>`, :mw:`HDL Coder <products/hdl-coder/>`, :mw:`Embedded Coder <products/embedded-coder/>`,\ :mw:`HDL Coder Support Package for Xilinx Zynq-7000 Platform <matlabcentral/fileexchange/40447-hdl-coder-support-package-for-xilinx-zynq-7000-platform>`, :mw:`Embedded Coder Support Package for Xilinx Zynq-7000 Platform <matlabcentral/fileexchange/40448-embedded-coder-support-package-for-xilinx-zynq-7000-platform>`, :mw:`Communications Toolbox Support Package for Xilinx Zynq-Based Radio <hardware-support/zynq-sdr.html>`
     -
     -
     -
     -
     -
     -
     -
   * - combinedTxRx_ADIDMA.slx
     - Fixed-Point Simulink deployable model
     - :mw:`Simulink <products/simulink/>`, :mw:`HDL Coder <products/hdl-coder/>`, :mw:`HDL Coder Support Package for Xilinx Zynq-7000 Platform <matlabcentral/fileexchange/40447-hdl-coder-support-package-for-xilinx-zynq-7000-platform>`, :dokuwiki:`Analog Devices BSP </resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`
     -
     -
     -
     -
     -
     -
     -
   * - Receiver_FPGACap.slx
     - Fixed-Point Simulink deployable model
     - :mw:`Simulink <products/simulink/>`, :mw:`HDL Coder <products/hdl-coder/>`, :mw:`HDL Coder Support Package for Xilinx Zynq-7000 Platform <matlabcentral/fileexchange/40447-hdl-coder-support-package-for-xilinx-zynq-7000-platform>`, :mw:`HDL Verifier <products/hdl-verifier/>`, :mw:`HDL Verifier Support Package for Xilinx FPGA Boards <matlabcentral/fileexchange/40434-hdl-verifier-support-package-for-xilinx-fpga-boards>`, :mw:`Communications Toolbox Support Package for Xilinx Zynq-Based Radio <hardware-support/zynq-sdr.html>` or :dokuwiki:`Analog Devices BSP </resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp>`
     -
     -
     -
     -
     -
     -
     -

Besides, the following items are required in prototype and production stages:

- :xilinx:`Xilinx Vivado <support/download.html>`

Testing Harness
---------------

MATLAB Unittest Tagging of tests Hardware in the loop

HDL Capable Demos
-----------------

- :git-TransceiverToolbox:`Standard_IQ <trx_examples/targeting/modem-qpsk/FixedPoint/demos/Standard_IQ+>`
- :git-TransceiverToolbox:`ADI_DMA_TT <trx_examples/targeting/modem-qpsk/FixedPoint/demos/ADI_DMA_TT+>`
- :git-TransceiverToolbox:`FPGA_Capture <trx_examples/targeting/modem-qpsk/FixedPoint/demos/FPGA_Capture+>`
- :git-TransceiverToolbox:`External_Mode <trx_examples/targeting/modem-qpsk/FixedPoint/demos/External_Mode+>`

All Demos
~~~~~~~~~

The codebase is designed to reuse code as much as possible. Therefore, the
recommended process for getting started with the modem project is to perform the
following:

Clone the repository: <code> git clone :git-TransceiverToolbox.git\ <:`code>+`

Launch MATLAB and navigate to the
*TransceiverToolbox\\target_models\\modem-qpsk* folder. Now add the necessary
files to your path by running the startup script: <code> startup_adi_qpsk
</code>

If you are generating HDL code you will be to add Vivado to your MATLAB path.
There is a helper function to make this easy as long as Vivado is installed in a
default location: <code> setupHDL </code>

Next, you can proceed to the build and run the desired demo.

Standard IQ
^^^^^^^^^^^

This demo is a simple ``Hello World`` example that demonstrates a simple
loopback test where transmitted packets contain the message ``Hello World N``
where N is a number 0-9. These messages are recovered and passed from the FPGA
directly back into MATLAB for display. This example uses a minimum set of
toolboxes and requires no modification to the HDL reference design. The model is
called Standard IQ since the default interfaces into the IP are 16bit for real
and imaginary, which are reused to send payload information (characters) back to
the host PC. Specifically, the real component contains the payload characters
and the imaginary component contains synchronization information to mark where
the payload starts and stops for correct display.

First, make sure you have gone through the setup process for your given board
documented
:mw:`SDR set up <help/supportpkg/xilinxzynqbasedradio/installation-and-setup.html>`.
The deployed model is applicable for FMComms 2/3/4 and ADI RF SOM SDR devices.

To run this example first navigate to the *FixedPoint\\demos\\Standard_IQ*
folder.

Run the script *hdlworkflow.m* which will build the design for the FPGA: <code>
hdlworkflow </code> Once the build has completed move the generated bit file to
the board as:

::

   dev = sdrdev('ADI RF SOM'); % Replace with your board name if different
   downloadImage(dev,'FPGAImage','hdl_prj/vivado_ip_prj/vivado_prj.runs/impl_1/system_wrapper.bit')

Now the board is ready to go and we can start interfacing with the FPGA through
Simulink and MATLAB. First, open the transmitter interface model: <code> open
Interface_Model_Tx </code> This model is responsible for configurating and
driving the transmitter. Once open run the model, then move back to the MATLAB
command prompt once running.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/siq_tx.png
   :width: 400px

Back at the command prompt run the receiver function which will start printing
received messages:

::

   >> Interface_Rx
   Hello World 7
   Hello World 8
   Hello World 9
   Hello World 0
   Hello World 1
   ....

These messages will appear at a high rate since in this configuration the radio
is running at 384kHz. Now you can modify the design if desired in the model
provided in the folder *combinedTxRx_StandardIQ.slx*. However, By only relying
on the default reference designs, HDL Coder, and the baseline HSP features
information from the FPGA will be limited to the IQ default interfaces from the
generated IP.

External Mode
^^^^^^^^^^^^^

This demo provides builds up the Standard_IQ model but also exposes various
configuration and status information from the deployed design. This example
utilizes Embedded Coder in Simulink to provided interfaces into different
registers of the design and pushes visualization back into Simulink. The 16bit
IQ channels are used to visualized the received constellation at different
points in the received chain. This is configurable since these different routes
are mapped into a mux whose index is controllable through a register. Two
outputs are provides besides the streaming IQ information, which includes a
register that contains the last recovered payload length and a selectable debug
signal. This selectable debug signal also has a connected mux which allows
selection of:

- Timing PLL lock
- Frequency PLL lock
- Peak detections
- Header failure events
- Packet CRC errors
- Packets recovered

First, make sure you have gone through the setup process for your given board
documented
:mw:`SDR set up <help/supportpkg/xilinxzynqbasedradio/installation-and-setup.html>`.
The deployed model is applicable for FMComms 2/3/4 and ADI RF SOM SDR devices.

To run this example first navigate to the *FixedPoint\\demos\\External_Mode*
folder.

Run the script *hdlworkflow.m* which will build the design for the FPGA: <code>
hdlworkflow </code> Once the build has completed move the generated bit file to
the board as:

::

   dev = sdrdev('ADI RF SOM'); % Replace with your board name if different
   downloadImage(dev,'FPGAImage','hdl_prj/vivado_ip_prj/vivado_prj.runs/impl_1/system_wrapper.bit')

Now the board is ready to go and we can start interfacing with the FPGA through
Simulink. First, open the combined interface model: <code> open Interface_Model
</code> This model is responsible for configurating and driving the transmitter,
receiver, and AXI register reads and writes. Once open run the model.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/extmode_interface.png
   :width: 800px

While the model is running the scroll bars and knobs are configurable, which
will change the state or configuration of the deployed modem. At runtime, only a
single Constellation Diagram scope should appear, which will show data from the
point selected in ``Select Scope Index:Value`` radio buttons provided in the
model.

By using the model in External Mode it allows greater configurability of the
running design on hardware. However, External Mode is limited to Simulink,
requires Embedded Coder, and has limited performance.

AXI Memory Mapped Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under the hood Simulink and External are exposing some of the model"s
configuration parameters and status values as AXI-Lite registers provides the
means to configure and monitor the IP at runtime from software. This way the IP
does not have to be regenerated every time a tuning value needs to change and
debugging becomes much more flexible. The External Mode demo is actually using
these interfaces under the hood but it may not be obvious to the users. In the
demos
:git-TransceiverToolbox:`ADI_DMA_TT <targeting_models/modem-qpsk/FixedPoint/demos/ADI_DMA_TT+>`
and
:git-TransceiverToolbox:`AXI_MM <targeting_models/modem-qpsk/FixedPoint/demos/AXI_MM+>`
these control interface are much more obvious, and arguably more flexible.

Register Map
''''''''''''

.. list-table::
   :header-rows: 1

   * - Address Offset
     - Name
     - Purpose
   * - 0x100
     - FRLoopBw
     - Frequency recovery PLL loop bandwidth
   * - 0x104
     - EQmu
     - Equalized stepsize, number is provided as 1/mu
   * - 0x108
     - ScopeSelect
     - Selection of debug IQ data mux index
   * - 0x10C
     - DebugSelect
     - Selection of debug mux index
   * - 0x110
     - payloadLenOutRxAXI
     - (Read) Length of last payload received in bytes
   * - 0x114
     - BypassEQ
     - Bypass equalizer
   * - 0x118
     - EnableRxDecode
     - Enabled modem header processing
   * - 0x11C
     - PDThreshold
     - Threshold of packet detector, value is multiplied by 1/10 internally
   * - 0x120
     - TransmitToggle
     - When toggled internal packet generate will send 1 packet to TX IP
   * - 0x124
     - TransmitAlways
     - When high internal packet generate will send continuous packets to TX IP
   * - 0x12C
     - LoopbackEnable
     - Enable loopback internally with in the IP from TX to RX
   * - 0x130
     - BypassCoding
     - Bypass (disable) channel coding
   * - 0x140
     - debugSelectionAXI
     - (Read) Value of selected debug signal from (0x10C)

FPGA Capture
^^^^^^^^^^^^

In many cases, in order to figure out what is not working right in a design, it
is necessary to be able to look at the internal signals at the design"s internal
clock rate. The most common debugging methodology for deployed signals is to use
the Xilinx Integrated Logic Analyzer (ILA) IP core and the Xilinx Chipscope
Analyzer software. ILA blocks can be dropped into design before synthesis. The
signals to be monitored can be exposed in the design as ``External Port``.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/ila.png
   :width: 500px

Another option is to use the Simulink ``FPGA Capture`` block. This block
connects to the signals in the design that need to be monitored. After
generating the HDL for the model a new model called
``FPGADataCapture_model.slx`` is automatically created allowing to connect to
the deployed design and display the signals in Logic Analyzer, Simulink, or
MATLAB.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/fpga_data_capture.png
   :width: 400px

ADI TunTap
^^^^^^^^^^

The modem IP implements the Data Link layer of the OSI stack but, in a deployed
system, the full stack needs to be implemented. To verify the modem design in a
real-life system it was exposed as an Ethernet connection in Linux by making use
of the
`TUN/TAP virtual network layer device <https://en.wikipedia.org/wiki/TUN/TAP>`__.

TUN and TAP are virtual network kernel drivers. TAP (as in network tap)
simulates an Ethernet device and it operates with layer 2 packets such as
Ethernet frames. TUN (as in network TUNnel) simulates a network layer device and
it operates with layer 3 packets such as IP.

Packets sent by an operating system via a TUN/TAP device are delivered to a
user-space program that attaches itself to the device. A user-space program may
pass packets into a TUN/TAP device. TUN/TAP device delivers (or ``injects``)
these packets to the operating system network stack thus emulating their
reception from an external source.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/tun_tap.png
   :width: 400px

The connection between the TUN/TAP driver and the modem IP is done by a
userspace daemon which is responsible for configuring the modem IP through the
register set that it exposes and for passing data back and forth between the
TUN/TAP driver and the modem"s receive and transmit DMA engines.

- :git-rfsom-box-gui:`Modem daemon source code <tun_tap+>`

Video Streaming for PackRF and Demo Boot Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ADI_DMA_TT design allows for video streaming example which has further
detail in these
articles:`modem setup </resources/eval/user-guides/pzsdr/carriers/packrf/example-use-case>`__
and
:dokuwiki:`PackRF software </resources/eval/user-guides/pzsdr/carriers/packrf/system-software-architecture>`.
This design requires a specific kernel and devicetree, since it was designed for
a specific platform
(:dokuwiki:`PackRF </resources/eval/user-guides/pzsdr/carriers/packrf>`).
Prebuilt files have been provided here (Note that you may have to click on the
\*View raw\* link to directly download the file from the forwarded page on
GitHub):

- :git-TransceiverToolbox:`BOOT.BIN <trx_examples/targeting/modem-qpsk/FixedPoint/demos/ADI_DMA_TT/BOOT.BIN?raw=true+>`
- :git-TransceiverToolbox:`uImage <trx_examples/targeting/modem-qpsk/FixedPoint/demos/ADI_DMA_TT/uImage?raw=true+>`
- :git-TransceiverToolbox:`Device Tree <trx_examples/targeting/modem-qpsk/FixedPoint/demos/ADI_DMA_TT/devicetree.dtb?raw=true+>`

Additional resources
--------------------

-

 .. video:: https://www.youtube.com/watch?v=kL_SyVODxgw
