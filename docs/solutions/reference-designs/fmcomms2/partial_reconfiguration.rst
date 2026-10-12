.. _fmcomms2 partial-reconfiguration:

Partial Reconfiguration with FMCOMMS2
===============================================================================

.. warning::

   This page has not been updated since 2014 and may contain outdated
   information.

Introduction
-------------------------------------------------------------------------------

Partial reconfiguration is a unique feature of Xilinx FPGAs, which offer the
possibility to reprogram a well specified portion of the FPGA on the fly,
without affecting the functionality of the remaining logic.

The purpose of this design is to showcase this feature and to present a
framework of the design flow, without trying to deliver a fully optimized
solution. The design is built upon a version of the :ref:`FMCOMMS2 <fmcomms2>`
reference design.

.. note::

   The following wiki page does not want to replace Xilinx documentations and
   application notes, which contains more detailed descriptions, suggestions and
   recommendations. It is highly recommended to examine all the docs provided by
   Xilinx. During the design process, the following documentations and
   application notes were used:

   - `Design Flows Overview <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2013_4/ug892-vivado-design-flows-overview.pdf>`_
   - `Partial Reconfiguration User Guide <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2013_4/ug909-vivado-partial-reconfiguration.pdf>`_
   - `Partial Reconfiguration Tutorial <https://www.xilinx.com/support/documentation/sw_manuals/xilinx2013_4/ug947-vivado-partial-reconfiguration-tutorial.pdf>`_
   - `Partial Reconfiguration of a Hardware Accelerator <https://www.xilinx.com/support/documentation/application_notes/xapp1159-partial-reconfig-hw-accelerator-zynq-7000.pdf>`_

Supported carriers
-------------------------------------------------------------------------------

- `ZC706 <https://www.xilinx.com/ZC706>`_
- `Mini-ITX <http://www.em.avnet.com/en-us/design/drc/Pages/Xilinx-Zynq-7000-All-Programmable-SoC-Mini-ITX-Development.aspx>`_

.. note::

   **Mini-ITX** board definition file can be found at
   http://zedboard.org/support/documentation/2056 .

Design Flow
-------------------------------------------------------------------------------

.. note::

   The supported design tools are:

   - `Vivado 2014.2 <https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/2014-2.html>`_

The design flow that was used is the Tcl-based non-project flow. All the design
phases are created and executed in the memory, and the user is responsible to
generate reports, log files or save checkpoints, for later investigations.

All the important Tcl processes, which define the necessary design phases can be
found in :git-hdl:`adi_prcfg_project.tcl
<legacy_fmcomms2_pr:projects/scripts/adi_prcfg_project.tcl>`
script. In the picture below can be seen the flow chart of the used design flow.

.. image:: images/pr_design_flow.png
   :width: 300

The design consists of the following base stages:

- Create the workspace
- Create and synthesize the static part of the design, the re-configurable
  part is defined as a black box
- Create and synthesize every re-configurable logic
- Load the static design with one of the re-configurable logic, and
  implement it
- Repeat the previous step with every re-configurable logic
- Verify the compatibility of the bitstreams

After every step, the script makes a checkpoint and generates and saves
additional reports.

To build the HDL project, the user must follow the :dokuwiki:`same instructions
<resources/fpga/docs/build>` as with any other reference designs. The design
does not require any additional library compilations, it should run with the
same cores as the :ref:`FMCOMMS2 <fmcomms2>` reference design.

After the **source ./system_project.tcl** script is executed, the workspace
will contain the following directory tree:

.. code-block::

     ./prcfg_static                      # files related to the static design
      |       |
      |       /checkpoints               # synthesis and route checkpoints
      |       +logs                      # log file after synthesis
      +prcfg_default                     # by-pass logic
      |        |
      |        /bit                      # partial and overall bitstreams (*.bit and *.bin)
      |        +checkpoints              # synthesis and route checkpoints
      |        +logs                     # log files after synthesis, place, route and optimization
      |        +results                  # top_routed checkpoint, timing and utilization reports
      +prcfg_bist                        # BIST logic
      |        |
      |        /bit                      # partial and overall bitstreams (*.bit and *.bin)
      |        +checkpoints              # synthesis and route checkpoints
      |        +logs                     # log files after synthesis, place, route and optimization
      |        +results                  # top_routed checkpoint, timing and utilization reports
      +prcfg_qpsk                        # QPSK modulation/demodulation logic
      |       |
      |       /bit                       # partial and overall bitstreams (*.bit and *.bin)
      |       +checkpoints               # synthesis and route checkpoints
      |       +logs                      # log files after synthesis, place, route and optimization
      |       +results                   # top_routed checkpoint, timing and utilization reports
      +sdk_export                        # contains the hardware specification file for the SDK project
      |
      +verify_design                     # contains the result of the bit stream verification

The script is saving a design checkpoint after every critical step in the design
flow, giving the possibility to revert or jump back, if something goes wrong.
For example, if the user wants to go back and examine the synthesis of the
static design, he/she simply needs to write the following command into the tcl
console:

.. code-block::

   open_checkpoint ./prcfg_static/checkpoints/synth_static.dcp

By default, the script runs all the necessary design flow stages (synthesis,
implementation, logic verification and so on) in order to get a valid bitstream.
There is a possibility to define which stages we want to run, by modifying the
value of the following variables, in the script called
:git-hdl:`/<board_name>/system_project.tcl
<legacy_fmcomms2_pr:projects/fmcomms2/zc706/system_project.tcl>`:

.. code-block:: tcl

   # activate/deactivate different flow stages
   set runInit     1
   set runSynth    1
   set runImpl     1
   set runPrv      1
   set runBit      1

.. note::

   But need to keep in mind, each stage is depending on the prior stages.

Partial Reconfiguration Logic
-------------------------------------------------------------------------------

In the HDL design of the FMCOMMS2, the re-configurable portion is defined in the
RX/TX data path, between the AD9361 IP core and TX/RX DMAs, given the
possibility to implement different types of modulation schemes, and to change
these modulations, while the system is running.

.. image:: images/fmcomms2_hdl_prcfg.png
   :width: 800

Initially, the top of the PR module is instantiated on the top of the design
as a black box. The
:git-hdl:`prcfg_setup.tcl <legacy_fmcomms2_pr:projects/fmcomms2/common/prcfg_bd.tcl>`
script makes sure that the FIFO interfaces between the DMAs and device core
are brought up to the top.
The top of the PR is a generic
:git-hdl:`hdl wrapper <legacy_fmcomms2_pr:library/prcfg/common/prcfg_top.v>`,
where the
:git-hdl:`TX <legacy_fmcomms2_pr:library/prcfg/default/prcfg_dac.v>`
and
:git-hdl:`RX <legacy_fmcomms2_pr:library/prcfg/default/prcfg_adc.v>`
modules are instantiated.

Adding new PR logic to the design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a new PR logic is defined, the user needs to make sure that the top
modules (which should be named
:git-hdl:`prcfg_dac.v <legacy_fmcomms2_pr:library/prcfg/default/prcfg_dac.v#L43-L61>`
and
:git-hdl:`prcfg_adc.v <legacy_fmcomms2_pr:library/prcfg/default/prcfg_adc.v#L43-L60>`)
have the same interface as the already defined modules (**Default**, **Bist**
or **Qpsk**). The new logic should be placed in the
**hdl/library/prcfg/[logic_name]** directory, and should be added into the
flow, by modifying
:git-hdl:`system_project.tcl <legacy_fmcomms2_pr:projects/fmcomms2/mitx045/system_project.tcl>`
script.

.. image:: images/pr_generichdl.png
   :width: 350

More information about the used FIFO interface can be found in the
:dokuwiki:`ADI Reference Design HDL User Guide <resources/fpga/docs/hdl#dac_interface>`.

Predefined PR Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently, the reference project supports three different PR logic, which can be
implemented and loaded into the PR portion:

- **Default logic**, which leaves the data intact, so the design will function
  the same way as a regular FMCOMMS2 design.
- **BIST logic**, which contains several internal tone generators for testing
  purposes. The user can select between three different options by setting a
  register, on the register map.
- **QPSK logic**, which contains a QPSK modulator and demodulator. The
  modulation and demodulation logic were generated using **MatLab HDL Coder
  3.3**.

The user can interact with PR logic, using a control and a status registers. The
table bellow presents the definitions of these two registers, in case of each
logic.

.. list-table:: Control Register [DEVICE_BASEADDR + 0x02E]
   :header-rows: 0
   :widths: 15 35 25 25

   * - **Default**
     - Not Used[31:0]
     -
     -
   * - **Bist**
     - Not Used[31:8]
     - Tone generator[7:4]
     - Channel[3:0]
   * - **QPSK**
     - Not Used[31:8]
     - Data path[7:4]
     - Channel[3:0]

.. list-table:: Status Register [DEVICE_BASEADDR + 0x02F]
   :header-rows: 0
   :widths: 15 25 15 15 30

   * - **Default**
     - Not Used[31:8]
     -
     -
     - PR_ID[7:0] = 0xA0
   * - **Bist**
     - Not Used[31:10]
     - PN_ERR[9:9]
     - PN_OOS[8:8]
     - PR_ID[7:0] = 0xA1
   * - **QPSK**
     - Not Used[31:10]
     - PN_ERR[9:9]
     - PN_OOS[8:8]
     - PR_ID[7:0] = 0xA2

Default Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This logic is loaded by default into the PR portion. It does not modify the data
path; the system works as the original AD-FMCOMMS2 design. The default logic ID
number is **0xA0**.

Bist Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This logic contains several internal tone generators for testing purposes. The
user can select between the generators by setting up the **Tone generator** bits
of the Control register. The BIST logic ID number is **0xA1**.

The available configurations:

- 0x0 -- Default, pass through configuration
- 0x1 -- Internal sine tone generator (with a frequency of fs/8)
- 0x2 -- Internal PRBS generator
- 0x3 -- Internal pattern generator (alternating 0x5555 and 0xAAAA)

In the receiver side, a PRBS monitor checks the received signal, and saves the
values into the PN_ERR and PN_OOS of the Status register. Note that if the PRBS
generator/monitor is used, the device should be in Digital Loopback mode.

QPSK Logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The QPSK modulator and demodulator used in this logic, were generated by the
MatLab HDL coder. The QPSK logic ID number is **0xA2**. The following Simulink
model was used to generate the HDL files. The model source file can be found in
the HDL GitHub repository.

.. image:: images/pqsk_simulink_model.png

In the block diagram below, it can be seen how these modules were integrated
into the QPSK logic. The red blocks represent the Verilog modules, which were
generated by the HDL Coder.

.. image:: images/pr_hdl_qpsk.png
   :width: 600

The available configurations:

- 0x0 -- Default, pass through configuration (bypass the
  modulation/demodulation)
- 0x1 -- Internal PRBS generator, the sequence is modulated and sent to the
  device in the transmitter side, and demodulated on the receive side.
- 0x2 -- Data from the DMA, user can send data from the memory.

In the receiver side, a PRBS monitor checks the received signal, when the actual
configuration is 0x1, and save the values into the PN_ERR and PN_OOS of the
Status register. In PRBS mode Digital Loopback should be used.

Downloads
-------------------------------------------------------------------------------

- **HDL project**
  https://github.com/analogdevicesinc/hdl/tree/legacy_fmcomms2_pr/projects/fmcomms2
- **PR Logic**
  https://github.com/analogdevicesinc/hdl/tree/legacy_fmcomms2_pr/library/prcfg
- **Workflow script**
  https://github.com/analogdevicesinc/hdl/blob/legacy_fmcomms2_pr/projects/scripts/adi_prcfg_project.tcl
- **QPSK simulink model**
  https://github.com/analogdevicesinc/hdl/blob/legacy_fmcomms2_pr/library/prcfg/qpsk/qpsk.slx

Test the design using a Linux image
-------------------------------------------------------------------------------

To create or update an SD card in order to test the reference design, the user
should follow these steps below:

#. Create and SD card from source by following the instructions from :ref:`here
   <linux-kernel zynq>`, or update an existent SD card by following the
   instructions from :external+kuiper:doc:`here <index>`.
#. Make sure that the BOOT partition of the SD card contains the correct
   BOOT.bin, device tree and uImage (to create the BOOT.bin the user should use
   **config_default.bit** bit file)
#. Copy the partial bitstreams to a known location on the file system.
#. Boot up the Linux.
#. If the PR project is supported by the :ref:`IIO oscilloscope
   <iio-oscilloscope>`, the PR plugin will be loaded automatically (wiki page of
   the :dokuwiki:`PR plugin
   <resources/tools-software/linux-software/partial_reconfiguration_plugin>`).
   If not, follow the instruction above to update the SD card and/or make sure
   that the correct bit file was used.

Reconfigure the FPGA from Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user can update the re-configurable portion of the FPGA, by using the
:dokuwiki:`Partial Reconfiguration plugin
<resources/tools-software/linux-software/partial_reconfiguration_plugin>` of the
oscilloscope. The plugin does the following two steps, after the user specifies
the partial bitstream:

#. set the device attribute called **is_partial_bitstream** to 1
#. write the generated partial bin file to the PCAP configuration interface
   (/dev/xdevcfg).

The functions, which do the update of the PR portion can be found
:git-iio-oscilloscope:`here <master:plugins/pr_config.c#L89-L134>`.

.. note::

   A few recommendations for the IIO oscilloscope setup:

   - The transmit side should be on **DAC Buffer Output** mode
   - If PRBS is used, the **Digital Loopback** should be enabled
   - Because the IIO oscilloscope is using data from the memory, the ADC side
     should be on pass through configuration (0x0), in this way the user can
     examine the modulated data
   - Use a higher sample count for the constellation plot

.. image:: images/fmcomms2_setup_pr.png
   :width: 350

.. image:: images/pr_setup.png
   :width: 350

.. image:: images/default_const.png
   :width: 350

.. image:: images/qpsk_const.png
   :width: 350
