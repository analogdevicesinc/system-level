.. _ad9084-multi-chip-sync:

Multi-Chip Synchronization with 2x AD9084+VCU118 and Parent ADF4030
===============================================================================

Overview
-------------------------------------------------------------------------------

Modern multi-channel RF systems—such as phased-array radar, electronic warfare
(EW) receivers, active beamforming platforms, and massive MIMO base
stations—require coherent operation across tens or hundreds of converter
channels. In these systems, all Analog-to-Digital Converters (ADCs) and
Digital-to-Analog Converters (DACs) across independent circuit boards must
operate with **deterministic latency** and **tight channel-to-channel phase
coherence** (typically sub-10 picoseconds).

The :adi:`AD9084` (Apollo MxFE®) integrates four 16-bit 28 GSPS DACs and four
12-bit 20 GSPS ADCs (4T4R) alongside extensive high-speed Digital Signal
Processing (DSP) datapaths and 48-lane JESD204B/C transceivers. Operating
multiple :adi:`EVAL-AD9084` evaluation boards on separate AMD/Xilinx
:xilinx:`VCU118` Virtex UltraScale+ FPGA carriers introduces several system-level
synchronization challenges:

- **Transmission Path Skew**: Length mismatches in external RF cables, FMC+
  connectors, and PCB traces between the master clock source and individual
  converter boards.
- **Clock Divider Ambiguity**: Internal clock dividers in the data converters,
  on-board clock synthesizers, and FPGA JESD204 transceivers can power up in
  random phase states without explicit synchronization.
- **Thermal Drift**: Dynamic temperature variations during prolonged runtime
  induce phase drift across clock distribution networks and board-level
  components.

To solve these challenges, Analog Devices provides a complete multi-tier
synchronization architecture combining:

1. **Parent ADF4030 Synchronizer**: A 10-channel precision synchronizer with
   sub-picosecond Time-to-Digital Converters (TDCs) that measures bidirectional
   Time-of-Flight (ToF) to calibrate out interconnect delays.
2. **On-Board ADF4382 Synthesizers**: Low-noise sampling clock PLLs with
   automatic phase adjustment via bleed current control, steered directly by
   Apollo firmware.
3. **Apollo Internal MCS Engines**: Hardware calibration blocks that align
   internal SYSREF and digital datapath dividers.
4. **AXI ADF4030 HDL Core (`axi_adf4030`)**: An FPGA IP core instantiated on
   each VCU118 carrier that recovers bidirectional BSYNC timing, measures
   periods, and synthesizes phase-aligned trigger pulses across all boards.

This application note provides the complete reference design and setup guide
for achieving repeatable, phase-coherent Multi-Chip Synchronization (MCS) across
two :adi:`EVAL-AD9084` boards paired with two :xilinx:`VCU118` FPGA carriers and
a central parent :adi:`ADF4030` synchronizer.

.. image:: ../images/apollo_block_diagram.png
   :align: center
   :width: 700px
   :alt: Apollo MxFE Functional Block Diagram

Target Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Multi-Chip Synchronization Performance Targets
   :widths: 35 30 35
   :header-rows: 1

   * - Parameter
     - Specification
     - Notes
   * - Inter-Device Channel Alignment
     - < ±10 ps
     - Measured at analog RF inputs/outputs across boards
   * - Power-Cycle Latency Repeatability
     - Deterministic (0 cycle variance)
     - Preserved across link re-initialization and reboots
   * - Thermal Phase Drift Compensation
     - Continuous (Closed-loop)
     - Active background tracking via Apollo firmware & ADF4382
   * - JESD204 Interface Mode
     - Subclass 1 (JESD204B/C)
     - Deterministic latency using SYSREF/BSYNC distribution

Hardware Setup & Interconnect Topology
-------------------------------------------------------------------------------

Required Equipment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **2x AMD/Xilinx VCU118 Evaluation Boards** (:xilinx:`VCU118`): Virtex
   UltraScale+ (`XCVU9P-L2FLGA2104E`) FPGA carriers hosting the MicroBlaze
   Linux subsystem, JESD204 link cores, and `axi_adf4030` trigger IP.
2. **2x EVAL-AD9084 Evaluation Boards** (:adi:`EVAL-AD9084`): Apollo MxFE
   evaluation cards.
3. **4x Samtec FMC+ Extenders**: 2x Vita 57.4 FMC+ extender cards per VCU118
   carrier to ensure proper mechanical seating and signal integrity.
4. **1x Parent EVAL-ADF4030 Board** (:adi:`ADF4030`): 10-channel precision
   synchronizer board serving as the system timing master.
5. **Ultra-Low Noise Reference Clock Generator**: 100 MHz or 125 MHz reference
   source driving the ADF4030 reference input and local synthesizers.
6. **Phase-Matched Coaxial Cable Sets**:
   - SMA-to-SMA length-matched cables for differential BSYNC connections.
   - RF cables for external reference clock distribution.
   - Power splitter and matched RF cables for multi-channel RF loopback testing.
7. **Host Workstation & Networking**: Dual Gigabit Ethernet connection to both
   VCU118 boards and JTAG (Digilent USB) cables for bitstream programming.

System Interconnect Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The figure below illustrates the physical wiring and signal distribution
between the parent ADF4030, the two AD9084 evaluation boards, and the two
VCU118 FPGA carriers.

.. mermaid::

   flowchart TD
       subgraph ClockSource["Reference Clock Source"]
           REF["100/125 MHz Ultra-Low Noise Reference"]
       end

       subgraph ParentSync["Parent Synchronizer (ADF4030)"]
           ADF["ADF4030 10-Channel Synchronizer\n(Integrated TDC)"]
           CH0["CH0: Reference Channel"]
           CH1["CH1: BSYNC Node 0 (AD9084)"]
           CH2["CH2: BSYNC Node 0 (VCU118)"]
           CH3["CH3: BSYNC Node 1 (AD9084)"]
           CH4["CH4: BSYNC Node 1 (VCU118)"]
       end

       subgraph Node0["Node 0: VCU118 + EVAL-AD9084"]
           PLL0["ADF4382-0\n(Clock PLL)"]
           APOLLO0["AD9084-0 (Apollo MxFE)\n4T4R Converters + DSP"]
           FPGA0["VCU118-0 (Virtex UltraScale+)\n- MicroBlaze Linux\n- axi_adf4030 IP\n- JESD204 Core"]
       end

       subgraph Node1["Node 1: VCU118 + EVAL-AD9084"]
           PLL1["ADF4382-1\n(Clock PLL)"]
           APOLLO1["AD9084-1 (Apollo MxFE)\n4T4R Converters + DSP"]
           FPGA1["VCU118-1 (Virtex UltraScale+)\n- MicroBlaze Linux\n- axi_adf4030 IP\n- JESD204 Core"]
       end

       REF -->|Ref Clock| ADF
       REF -->|Ref Clock| PLL0
       REF -->|Ref Clock| PLL1

       CH1 -->|Bidirectional BSYNC| APOLLO0
       CH2 -->|Bidirectional BSYNC| FPGA0
       CH3 -->|Bidirectional BSYNC| APOLLO1
       CH4 -->|Bidirectional BSYNC| FPGA1

       PLL0 -->|12 GHz Sampling Clock| APOLLO0
       APOLLO0 -->|DELADJ / DELSTR GPIO| PLL0
       APOLLO0 <-->|JESD204B/C SerDes| FPGA0

       PLL1 -->|12 GHz Sampling Clock| APOLLO1
       APOLLO1 -->|DELADJ / DELSTR GPIO| PLL1
       APOLLO1 <-->|JESD204B/C SerDes| FPGA1

Signal Descriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **BSYNC (Bidirectional Synchronized Clock)**: A differential timing signal
  generated by the parent ADF4030 that combines SYSREF pulses and phase-marker
  information. The physical line is bidirectional: during initial calibration,
  the signal direction is reversed so the Apollo device drives BSYNC back to the
  ADF4030, allowing the round-trip Time-of-Flight (ToF) to be precisely measured.
- **DELADJ & DELSTR (Delay Adjust & Strobe)**: Dedicated GPIO lines between the
  Apollo device and the on-board ADF4382 clock PLL. Apollo firmware computes
  phase corrections via an internal TDC and pulses DELADJ/DELSTR to tune the
  ADF4382 charge-pump bleed current without processor intervention.
- **JESD204B/C Links**: High-speed serialized data lanes connecting converter
  DSP cores to the FPGA transceiver array, operating in Subclass 1 mode with
  deterministic latency locked to the BSYNC reference.

HDL Architecture: `axi_adf4030` IP Core
-------------------------------------------------------------------------------

To integrate the parent ADF4030 BSYNC signal into the FPGA subsystem, each
VCU118 design instantiates the `axi_adf4030` HDL IP core in the MicroBlaze
block design.

.. mermaid::

   flowchart LR
       subgraph IO["Differential IO"]
           BSYNC_P["bsync_p"]
           BSYNC_N["bsync_n"]
           IOBUF["IOBUFDS_DCIEN\n(SIM_DEVICE=UltraScale+)"]
           BSYNC_P --> IOBUF
           BSYNC_N --> IOBUF
       end

       subgraph Core["axi_adf4030 HDL Core"]
           GEN["bsync_generator.sv\n- 3-Stage Pipeline\n- CALIB FSM\n- ratio_counter\n- Regenerator"]
           STRETCH["trigger_bsync_stretcher.sv\n- Set/Reset Latch\n- BSYNC Edge Align"]
           CH0["trigger_channel[0]\nt_delay = (2*RATIO - 2 - PHASE)*Tclk"]
           CH1["trigger_channel[1]"]
           CH_N["trigger_channel[N-1]"]
           REGMAP["axi_adf4030_regmap.sv\n- AXI4-Lite Slave\n- CDC (sync_bits, sync_data, sync_event)"]
       end

       subgraph System["FPGA Subsystem"]
           AXI["MicroBlaze AXI4-Lite"]
           EXT_TRIG["External Trigger SMA"]
           JESD_SYSREF["JESD204 SYSREF / LMFC"]
           TDD_TRIG["AXI TDD / NCO FFH Trigger"]
           DMA_TRIG["AXI DMAC Capture Start"]
       end

       IOBUF <-->|Bidirectional BSYNC| GEN
       GEN -->|bsync_event| CH0
       GEN -->|bsync_event| CH1
       GEN -->|bsync_event| CH_N
       GEN -->|bsync_event| STRETCH

       EXT_TRIG -->|select_trig=1| STRETCH
       REGMAP -->|manual_trigger (select_trig=0)| STRETCH
       STRETCH -->|stretched_trigger| CH0
       STRETCH -->|stretched_trigger| CH1
       STRETCH -->|stretched_trigger| CH_N

       AXI <-->|s_axi_*| REGMAP
       REGMAP <-->|Registers & CDC| GEN
       REGMAP <-->|TRIG_PHASE[N] & EN| CH0
       REGMAP <-->|TRIG_PHASE[N] & EN| CH1
       REGMAP <-->|TRIG_PHASE[N] & EN| CH_N

       CH0 --> JESD_SYSREF
       CH1 --> TDD_TRIG
       CH_N --> DMA_TRIG

Key submodules inside `library/axi_adf4030/`:

1. **Bidirectional I/O Buffer (`IOBUFDS_DCIEN`)**:
   Utilizes the AMD UltraScale+ specific `IOBUFDS_DCIEN` primitive. The receiver
   path includes programmable on-chip termination and an `IBUFDISABLE` input
   that disables the input buffer when the FPGA drives BSYNC out to eliminate
   internal feedback and bus contention.
2. **BSYNC Receiver & Calibration FSM (`bsync_generator.sv`)**:
   - **IDLE**: Awaits the initial rising edge on the incoming BSYNC line. A
     3-stage pipeline reduces metastability probability.
   - **CALIB**: Measures the half-period of the BSYNC clock by counting
     `device_clk` cycles while BSYNC is asserted high. The measured count is
     stored in `ratio_counter` and exported to the register map as `BSYNC_RATIO`.
   - **BSYNC_GEN**: Regenerates a local, low-jitter copy of the BSYNC clock
     using the calibrated ratio.
   - **BSYNC_ALIGNMENT_ERROR**: Continuously verifies that every subsequent
     BSYNC edge matches the calibrated ratio. Any timing glitch or cycle slip
     latches an alignment error flag requiring software reset.
3. **Per-Channel Trigger Generators (`trigger_channel.sv`)**:
   Up to 8 independent trigger channels generate output pulses phase-delayed
   relative to the BSYNC window. The delay from trigger arrival to the output
   rising edge is governed by:

   .. math::

      t_{\text{delay}} = \left(2 \times \text{BSYNC\_RATIO} - 2 - \text{TRIG\_PHASE}\right) \times T_{\text{device\_clk}}

   Where:
   - :math:`\text{BSYNC\_RATIO}` is the measured half-period count.
   - :math:`\text{TRIG\_PHASE}` is the programmable phase offset register.
   - :math:`T_{\text{device\_clk}}` is the FPGA core device clock period.
4. **Trigger Stretcher (`trigger_bsync_stretcher.sv`)**:
   When narrow, asynchronous trigger pulses are received from external SMA pins
   or software writes, this module uses a set/reset latch to capture and hold
   the trigger asserted until the next rising edge of BSYNC, preventing missed
   triggers.
5. **Clock Domain Crossing (CDC) & Constraints (`axi_adf4030_regmap.sv`)**:
   All control bits and phase values cross between `s_axi_aclk` and `device_clk`
   using ADI synchronization primitives (`sync_bits`, `sync_data`, `sync_event`).
   Explicit `set_false_path` constraints are generated automatically by
   `axi_adf4030_constr.ttcl`.

Register Summary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: AXI ADF4030 Register Map Highlights
   :widths: 20 20 60
   :header-rows: 1

   * - Offset
     - Name
     - Function
   * - `0x00`
     - `VERSION`
     - Core version and peripheral ID
   * - `0x04`
     - `CONTROL`
     - Bit 0: `DIRECTION` (0=Drive, 1=Receive), Bit 1: `SELECT_TRIG`, Bit 2: `SW_RESET`
   * - `0x05`
     - `STATUS`
     - Bit 0: `BSYNC_READY`, Bit 1: `BSYNC_CAPTURED`, Bit 2: `ALIGNMENT_ERROR`
   * - `0x06`
     - `BSYNC_RATIO`
     - Calibrated half-period count in `device_clk` cycles
   * - `0x07`–`0x0E`
     - `TRIG_CHANNEL[0..7]`
     - Bits [15:0]: Channel `TRIG_PHASE`, Bit 31: `CHANNEL_EN`
   * - `0x10`
     - `MANUAL_TRIGGER`
     - Write 1 to pulse software trigger across CDC to `device_clk`

Building the HDL Project with the AXI Trigger Core
-------------------------------------------------------------------------------

To deploy Multi-Chip Synchronization on the VCU118 carrier, the `axi_adf4030`
trigger IP core must be packaged and integrated into the `ad9084_ebz_vcu118` HDL
block design before synthesizing the bitstream.

Prerequisites & Toolchain Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **AMD/Xilinx Vivado ML Enterprise Edition**: Vivado 2025.1 (or the version
   matching your current ADI HDL release).
2. **Toolchain Environment Configuration**:
   Source the Vivado environment setup script to add `vivado` and related tools
   to your path:

   .. shell::
      :show-user:

      $source /opt/Xilinx/Vivado/2025.1/settings64.sh

3. **Clone the ADI HDL Repository**:

   .. shell::
      :show-user:

      $git clone https://github.com/analogdevicesinc/hdl.git
      $cd hdl
      $git checkout main

Packaging the `axi_adf4030` IP Core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analog Devices manages HDL IP cores as reusable modules located under the
`library/` directory. Each IP core contains an `<ip_name>_ip.tcl` packaging
script that generates the IP metadata (`component.xml`) required by Vivado IP
Integrator.

To build and package the `axi_adf4030` core:

.. shell::
   :show-user:

   $cd library/axi_adf4030
   $make

During this step, Vivado runs in batch mode to:

1. Analyze and package the SystemVerilog sources (`axi_adf4030.sv`,
   `bsync_generator.sv`, `trigger_channel.sv`, `trigger_bsync_stretcher.sv`,
   `axi_adf4030_regmap.sv`).
2. Set configuration generics:
   - `FPGA_FAMILY = 0` (selects `IOBUFDS_DCIEN` for UltraScale+ on VCU118).
   - `CHANNEL_COUNT = 4` (configurable from 1 to 8).
   - `TRIGGER_STRETCH = 1` (enables latching stretcher for asynchronous inputs).
3. Generate CDC timing constraints from the template `axi_adf4030_constr.ttcl`.
4. Produce the packaged Vivado IP repository in `library/axi_adf4030/`.

Integrating the Trigger Core into the VCU118 Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Declare Library Dependency**:
   Verify that `axi_adf4030` is listed as a required library dependency in
   `projects/ad9084_ebz/vcu118/Makefile`:

   .. code-block:: makefile

      REQUIRED_LIBRARIES += axi_adf4030

2. **Block Design Instantiation (`system_bd.tcl`)**:
   In the project's block design script, instantiate the `axi_adf4030` core,
   connect its AXI4-Lite control interface, wire clock and reset nets, and map
   the phase-aligned trigger channels to the JESD204 and DMA subsystems:

   .. code-block:: tcl

      # Instantiate the AXI ADF4030 Trigger IP core
      ad_ip_instance axi_adf4030 axi_adf4030_0 [list \
        FPGA_FAMILY 0 \
        CHANNEL_COUNT 4 \
        TRIGGER_STRETCH 1 \
      ]

      # Map AXI4-Lite control interface on MicroBlaze interconnect
      ad_cpu_interconnect 0x44A00000 axi_adf4030_0/s_axi

      # Connect AXI bus clock and high-speed device clock
      ad_connect sys_cpu_clk axi_adf4030_0/s_axi_aclk
      ad_connect sys_cpu_resetn axi_adf4030_0/s_axi_aresetn
      ad_connect device_clk axi_adf4030_0/device_clk
      ad_connect rstn axi_adf4030_0/rstn

      # Connect External Differential BSYNC Ports (IOBUFDS_DCIEN)
      create_bd_port -dir IO bsync_p
      create_bd_port -dir IO bsync_n
      ad_connect bsync_p axi_adf4030_0/bsync_p
      ad_connect bsync_n axi_adf4030_0/bsync_n

      # Route Aligned Trigger Channels to FPGA Subsystems
      # Channel 0 -> JESD204 RX SYSREF / LMFC alignment
      ad_connect axi_adf4030_0/trig_channel_0 axi_jesd204_rx/sysref
      # Channel 1 -> JESD204 TX SYSREF / LMFC alignment
      ad_connect axi_adf4030_0/trig_channel_1 axi_jesd204_tx/sysref
      # Channel 2 -> AXI TDD Engine / Fast Frequency Hopping Phase Reset
      ad_connect axi_adf4030_0/trig_channel_2 axi_tdd_0/sync_in
      # Channel 3 -> AXI DMAC Synchronous Capture Trigger
      ad_connect axi_adf4030_0/trig_channel_3 axi_dmac_0/sync

3. **Physical Constraints (`system_constr.xdc`)**:
   Assign the differential BSYNC pins to dedicated FMC+ or SMA differential I/O
   pins on the VCU118 Virtex UltraScale+ High-Performance (HP) bank with LVDS
   signaling and internal termination:

   .. code-block:: tcl

      # Differential BSYNC IOBUFDS_DCIEN Pin Constraints (Bank 64 HP)
      set_property -dict {PACKAGE_PIN AU22 IOSTANDARD LVDS} [get_ports bsync_p]
      set_property -dict {PACKAGE_PIN AU23 IOSTANDARD LVDS} [get_ports bsync_n]

Building the Complete VCU118 Bitstream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the project is configured, run `make` from the project directory. The ADI
HDL build system will automatically check and build any missing library IP cores
(including `axi_adf4030`, `axi_adxcvr`, `axi_jesd204_rx`, `axi_jesd204_tx`),
generate the block design, run synthesis, place-and-route, and generate the
programming bitstream:

.. shell::
   :show-user:

   $cd projects/ad9084_ebz/vcu118
   $make
     Building axi_adf4030 ... OK
     Building axi_adxcvr ... OK
     Building axi_jesd204_rx ... OK
     Building axi_jesd204_tx ... OK
     Building ad9084_ebz_vcu118 [/home/analog/hdl/projects/ad9084_ebz/vcu118/ad9084_ebz_vcu118_vivado.log] ... OK

Build Artifacts:

- **FPGA Bitstream**:
  `projects/ad9084_ebz/vcu118/ad9084_ebz_vcu118.runs/impl_1/system_top.bit`
- **Hardware Handoff File (XSA)**:
  `projects/ad9084_ebz/vcu118/ad9084_ebz_vcu118.sdk/system_top.xsa`

The resulting `.bit` file is used to program the VCU118 FPGA via JTAG/XSCT, and
the `.xsa` file contains the hardware specification used to build the Linux
device tree with `pyadi-dt` or XSCT.

Multi-Chip Synchronization Theory of Operation
-------------------------------------------------------------------------------

Achieving phase coherence across multiple AD9084 boards is performed in a
four-stage hierarchy:

.. mermaid::

   sequenceDiagram
       autonumber
       participant Master as Parent ADF4030
       participant Apollo0 as AD9084 Node 0
       participant Apollo1 as AD9084 Node 1
       participant FPGA as VCU118 FPGAs

       Note over Master,Apollo1: Stage 1: BSYNC Time-of-Flight (ToF) Path Delay Measurement
       Master->>Apollo0: Delta-T0: BSYNC Fwd Pulse (Record t0_out, t0_in)
       Master->>Apollo1: Delta-T0: BSYNC Fwd Pulse (Record t0_out, t0_in)
       Apollo0->>Master: Delta-T1: Apollo Drives BSYNC Rev Pulse (Record t1_out, t1_in)
       Apollo1->>Master: Delta-T1: Apollo Drives BSYNC Rev Pulse (Record t1_out, t1_in)
       Note over Master,Apollo1: Compute Path Delays & Apply Negative Phase Offsets to ADF4030

       Note over Apollo0,Apollo1: Stage 2: Apollo MCS Initial Calibration
       Apollo0->>Apollo0: Align Internal SYSREF to BSYNC (Validate < 0.4 cycles)
       Apollo1->>Apollo1: Align Internal SYSREF to BSYNC (Validate < 0.4 cycles)

       Note over Apollo0,Apollo1: Stage 3: Sampling Clock Phase Alignment & Tracking Cal
       Apollo0->>Apollo0: Foreground Tracking Cal -> Measure Phase vs Ref
       Apollo1->>Apollo1: Foreground Tracking Cal -> Measure Phase vs Ref
       Apollo0->>Apollo0: Enable Continuous BG Tracking (DELADJ/DELSTR to ADF4382)
       Apollo1->>Apollo1: Enable Continuous BG Tracking (DELADJ/DELSTR to ADF4382)

       Note over FPGA,Apollo1: Stage 4: FPGA Trigger & Datapath Synchronization
       FPGA->>FPGA: Calibrate axi_adf4030 Ratio -> Align Baseband Timers & TDD

Stage 1: BSYNC Time-of-Flight (ToF) Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Physical cable lengths and PCB traces connecting the parent ADF4030 to each
Apollo board inevitably differ in electrical delay. Without compensation,
BSYNC pulses arrive at converter dies at different absolute times.

To calibrate this delay, the ADF4030 and Apollo devices perform a bidirectional
Time-of-Flight (ToF) measurement:

1. **Delta-T0 (Forward Measurement)**:
   - The ADF4030 drives BSYNC out to Apollo.
   - The ADF4030 internal TDC logs transmission time :math:`\Delta t_{0,\text{adf}}`.
   - The Apollo internal TDC logs arrival time :math:`\Delta t_{0,\text{apollo}}`.
2. **Delta-T1 (Reverse Measurement)**:
   - The BSYNC direction is reversed: ADF4030 output buffer is disabled, and
     Apollo drives BSYNC back toward the ADF4030.
   - Apollo logs transmit timestamp :math:`\Delta t_{1,\text{apollo}}`.
   - ADF4030 TDC logs arrival timestamp :math:`\Delta t_{1,\text{adf}}`.
3. **Delay Calculation**:
   The round-trip delay and one-way electrical path delay are calculated as:

   .. math::

      \text{calc\_delay} = (\Delta t_{0,\text{adf}} - \Delta t_{1,\text{adf}}) - (\Delta t_{1,\text{apollo}} - \Delta t_{0,\text{apollo}})

   .. math::

      \text{round\_trip} = (\text{calc\_delay} + T_{\text{bsync\_period}}) \pmod{T_{\text{bsync\_period}}}

   .. math::

      \text{path\_delay} = \frac{\text{round\_trip}}{2}

4. **Phase Compensation**:
   The driver programs a negative phase offset :math:`(-\text{path\_delay})`
   into the ADF4030 channel output attribute. This advances the transmission of
   BSYNC on that specific channel so that BSYNC edges arrive at the internal dies
   of all Apollo chips at the exact same physical instant.

.. warning::

   **Bus Contention Hazard**: BSYNC is a shared differential line. If both
   ADF4030 and Apollo attempt to drive BSYNC simultaneously, signal contention
   and incorrect TDC readings will occur. Direction switching must be strictly
   sequenced using the driver sysfs/debugfs controls.

Stage 2: Apollo MCS Initial Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once BSYNC edges arrive simultaneously at both Apollo devices:

1. Apollo executes `adi_apollo_mcs_cal_init_run()`.
2. The internal SYSREF digital dividers are phase-aligned to the incoming
   compensated BSYNC edge.
3. The driver validates the alignment:
   - Confirms that SYSREF is locked.
   - Verifies that the timing difference between internal dividers and BSYNC is
     strictly within **±0.4 clock cycles**.
   - If validation fails, initialization aborts with a descriptive error.

Stage 3: Clock PLL Phase Alignment & Tracking Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While Stage 2 aligns digital clock dividers, physical RF sampling clocks (12 GHz)
generated by the local ADF4382 PLLs can still drift due to thermal expansion
and voltage fluctuations.

**Single Clock vs. Dual Clock Mode**:
- **Single Clock Mode (Recommended for MCS)**: A single central ADF4382 PLL
  drives both Side A and Side B of the Apollo device. Apollo firmware
  continuously tracks phase error using an internal TDC and modulates the
  ADF4382 charge-pump bleed current via `DELADJ` and `DELSTR` GPIO strobes.
  Full background tracking calibration is supported.
- **Dual Clock Mode**: Separate ADF4382 PLLs drive Side A and Side B. Due to
  hardware constraints, active background tracking is unsupported in dual-clock
  mode, making Single Clock mode mandatory for long-term thermal phase stability.

Tracking Calibration Execution:

1. **Setup**: The driver configures the TDC decimation rate (typically `1023`).
2. **Auto-Align Enable**: The ADF4382 auto-alignment mode is activated
   (`out_altvoltage0_en_auto_align = 1`).
3. **Foreground Calibration**: Runs `adi_apollo_mcs_cal_fg_tracking_run()` to
   determine baseline bleed current settings (polarity, coarse, fine).
4. **Background Tracking**: Initiates continuous background tracking
   (`adi_apollo_mcs_cal_bg_tracking_run()`), ensuring persistent sub-10 ps phase
   alignment despite ambient temperature variations.

Stage 4: FPGA Baseband & Trigger Alignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To align baseband data streams across the two VCU118 FPGAs:

1. Both FPGAs receive BSYNC from dedicated channels of the parent ADF4030.
2. The `axi_adf4030` core on each board locks to BSYNC and counts `BSYNC_RATIO`.
3. Synchronized triggers are routed to:
   - JESD204 link framing and LMFC counters.
   - AXI TDD controllers for synchronized TX burst gating.
   - NCO Fast Frequency Hopping (FFH) phase reset strobes.
   - AXI DMAC capture start signals.

Linux Driver & Device Tree Configuration
-------------------------------------------------------------------------------

Device Tree Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the MicroBlaze Linux kernel device tree (`arch/microblaze/boot/dts/`), both
nodes configure the ADF4030, ADF4382, Apollo AD9088/AD9084, and `axi_adf4030`
trigger cores.

Below is the representative device tree configuration for **Node 0**:

.. code-block:: dts

   /* Parent ADF4030 Synchronizer */
   &spi0 {
       adf4030: adf4030@0 {
           compatible = "adi,adf4030";
           reg = <0>;
           spi-max-frequency = <1000000>;
           #io-channel-cells = <1>;

           adi,vco-frequency-hz = <1000000000>;
           adi,bsync-frequency-hz = <250000000>;
           adi,bsync-autoalign-reference-channel = <0>;

           /* Output Channel 0: Master Reference */
           adi,channel@0 {
               reg = <0>;
               adi,output-enable;
               adi,auto-align-on-sync-en;
           };

           /* Output Channel 1: BSYNC to AD9084 Node 0 */
           adi,channel@1 {
               reg = <1>;
               adi,output-enable;
               adi,auto-align-on-sync-en;
               adi,reference-channel = <0>;
           };

           /* Output Channel 2: BSYNC to VCU118 Node 0 FPGA */
           adi,channel@2 {
               reg = <2>;
               adi,output-enable;
               adi,auto-align-on-sync-en;
               adi,reference-channel = <0>;
           };
       };

       /* On-Board ADF4382 Clock PLL */
       adf4382: adf4382@1 {
           compatible = "adi,adf4382";
           reg = <1>;
           spi-max-frequency = <1000000>;
           #io-channel-cells = <1>;

           clocks = <&ref_clk>;
           clock-names = "ref_clk";
           adi,ref-frequency-hz = <125000000>;
           adi,output-frequency-hz = <12000000000>;
       };

       /* Apollo AD9084 Device */
       trx0_ad9084: ad9088@2 {
           compatible = "adi,ad9088";
           reg = <2>;
           spi-max-frequency = <1000000>;

           /* Consumer IIO Channels for MCS: BSYNC and Clock */
           io-channels = <&adf4030 1>, <&adf4382 0>;
           io-channel-names = "bsync", "clk";

           /* MCS Configuration Properties */
           adi,mcs-track-decimation = /bits/ 16 <1023>;
           adi,trigger-sync-en;

           /* Firmware Profile and Pre-Stored Calibration */
           adi,device-profile-fw-name = "ad9084_profile.bin";
           adi,device-calibration-data-name = "ad9084_cal.bin";
       };
   };

   /* FPGA AXI ADF4030 Trigger IP Core */
   &amba_pl {
       axi_adf4030_0: axi-adf4030@44a00000 {
           compatible = "adi,axi-aion-trig", "adi,axi-adf4030-1.00.a";
           reg = <0x44a00000 0x1000>;
           clocks = <&clk_bus_0>, <&clk_device_0>;
           clock-names = "s_axi_aclk", "device_clk";
           adi,channel-count = <4>;
           adi,trigger-stretch;
       };
   };

.. note::

   For **Node 1**, configure the `io-channels` phandles to reference ADF4030
   channel 3 (for AD9084 Node 1) and channel 4 (for VCU118 Node 1 FPGA).

Automated JESD204 FSM Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When `io-channels` are defined in the device tree, the Linux kernel
:external+linux:ref:`jesd204-fsm-framework` automatically orchestrates MCS
calibration across all devices in the link during system boot:

.. list-table:: JESD204 FSM State Execution
   :widths: 35 65
   :header-rows: 1

   * - FSM Stage
     - Action Performed
   * - `CLK_SYNC_STAGE3`
     - Parent ADF4030 aligns all output channels to reference channel 0.
   * - `OPT_POST_SETUP_STAGE1`
     - BSYNC Delta-T0/Delta-T1 ToF measurement, path delay calculation,
       ADF4030 phase adjustment, and Apollo MCS init calibration.
   * - `OPT_POST_SETUP_STAGE2`
     - Trigger synchronization setup and FPGA BSYNC ToF calibration.
   * - `OPT_POST_SETUP_STAGE3`
     - Aligned trigger pulse generation and verification.
   * - `OPT_POST_RUNNING_STAGE`
     - Foreground tracking calibration run and continuous background tracking
       initiation.

Interactive / Manual Calibration Sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For troubleshooting, laboratory characterization, or custom sequencing, the
full MCS flow can be executed manually via debugfs and sysfs:

.. code-block:: bash

   #!/bin/bash
   # Manual MCS Calibration Script for AD9084 + ADF4030 + ADF4382

   APOLLO="/sys/kernel/debug/iio/iio:device0"
   ADF4030="/sys/bus/iio/devices/iio:device1"
   ADF4382="/sys/bus/iio/devices/iio:device2"

   echo "[1/8] Initializing MCS calibration..."
   echo 1 > "$ADF4030/apollo_sysref_0_output_enable"
   echo 1 > "$APOLLO/mcs_init"

   echo "[2/8] Executing Delta-T0 forward measurement (ADF4030 -> Apollo)..."
   echo 1 > "$APOLLO/mcs_dt0_measurement"
   apollo_t0=$(cat "$APOLLO/mcs_dt0_measurement")
   adf_t0=$(cat "$ADF4030/apollo_sysref_0_phase")

   echo "[3/8] Reversing direction for Delta-T1 measurement (Apollo -> ADF4030)..."
   echo 0 > "$ADF4030/apollo_sysref_0_output_enable"
   echo 1 > "$APOLLO/mcs_dt1_measurement"
   apollo_t1=$(cat "$APOLLO/mcs_dt1_measurement")
   adf_t1=$(cat "$ADF4030/apollo_sysref_0_phase")

   echo "[4/8] Restoring BSYNC line state and calculating path delay..."
   echo 1 > "$APOLLO/mcs_dt_restore"
   echo 1 > "$ADF4030/apollo_sysref_0_output_enable"

   # Calculate path delay in femtoseconds (BSYNC period = 4,000,000 fs @ 250 MHz)
   bsync_period=4000000
   calc_delay=$(( (adf_t0 - adf_t1) - (apollo_t1 - apollo_t0) ))
   round_trip=$(( (calc_delay + bsync_period) % bsync_period ))
   path_delay=$(( round_trip / 2 ))

   echo "      Calculated One-Way Path Delay: ${path_delay} fs"
   echo "-${path_delay}" > "$ADF4030/apollo_sysref_0_phase"

   echo "[5/8] Running Apollo MCS Initial Calibration..."
   echo 1 > "$APOLLO/mcs_cal_run"
   init_status=$(cat "$APOLLO/mcs_cal_run")
   echo "      Init Cal Status: ${init_status}"

   if [ "$init_status" != "Passed" ]; then
       echo "ERROR: MCS Initial Calibration failed! Status detail:"
       cat "$APOLLO/mcs_init_cal_status"
       exit 1
   fi

   echo "[6/8] Enabling ADF4382 Auto-Alignment..."
   echo 1 > "$ADF4382/out_altvoltage0_en_auto_align"

   echo "[7/8] Launching Tracking Calibration..."
   echo 1 > "$APOLLO/mcs_track_cal_setup"
   echo 1 > "$APOLLO/mcs_fg_track_cal_run"
   echo 1 > "$APOLLO/mcs_bg_track_cal_run"

   echo "[8/8] Validating Tracking Synchronization..."
   cat "$APOLLO/mcs_track_cal_validate"

Step-by-Step Bring-Up & Verification Workflow
-------------------------------------------------------------------------------

Step 1: Hardware Assembly & Power Up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Mount each :adi:`EVAL-AD9084` board onto the FMC+ (HPC0) connector of its
   respective :xilinx:`VCU118` carrier using two Samtec Vita 57.4 FMC+ extenders.
2. Ensure VADJ on both VCU118 boards is configured to **1.8V** (via the BEAM
   tool or on-board jumpers).
3. Connect the differential BSYNC SMA cables:
   - ADF4030 Channel 1 to AD9084 Node 0 BSYNC IN.
   - ADF4030 Channel 2 to VCU118 Node 0 FPGA BSYNC SMA pair.
   - ADF4030 Channel 3 to AD9084 Node 1 BSYNC IN.
   - ADF4030 Channel 4 to VCU118 Node 1 FPGA BSYNC SMA pair.
4. Distribute the common 100/125 MHz reference clock to the ADF4030 REFIN and
   both ADF4382 synthesizers using matched 50 Ω coaxial cables.
5. Connect Gigabit Ethernet and micro-USB JTAG cables from both boards to the
   local network / host workstation.
6. Power on the VCU118 boards and parent ADF4030 simultaneously.

Step 2: FPGA Programming & Linux Boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Program both VCU118 boards via the Xilinx Software Command-Line Tool (`xsct`):

.. code-block:: bash

   xsct% connect
   xsct% targets -set -filter {name =~ "xcvu9p*"}
   xsct% fpga -f system_top.bit
   xsct% after 1000
   xsct% dow simpleImage.vcu118_ad9084.strip
   xsct% after 1000
   xsct% con
   xsct% disconnect

Both systems will boot into Linux and output the serial console log at 115200 baud.

Step 3: Verifying JESD204 Link Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On each VCU118 node, check the JESD204 status utility to verify that all lanes
have completed Code Group Synchronization (CGS) and Initial Frame
Synchronization (IFS):

.. code-block:: bash

   # Verify receiver link status
   jesd_status -d axi-jesd204-rx-0

   # Verify transmitter link status
   jesd_status -d axi-jesd204-tx-0

Confirm that the output reports:
- Link state: `DATA`
- Measured link clock and frame clock match configuration.
- Zero lane alignment errors or disparity errors.

Step 4: Validating MCS Tracking Calibration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On each node, inspect the tracking calibration validation attribute:

.. code-block:: bash

   cat /sys/kernel/debug/iio/iio:device0/mcs_track_cal_validate

Expected output:

.. code-block:: text

   MCS Tracking Cal Validation:
     ADF4382 HW:  bleed_pol=0 coarse=5 fine=128
     Apollo FW:   bleed_pol=0 coarse=5 fine=128
     Status:      SYNCHRONIZED

If the status reports `SYNCHRONIZED`, the Apollo firmware TDC and ADF4382
hardware bleed current values match, confirming that closed-loop phase tracking
is actively maintaining synchronization.

Step 5: Multi-Board RF Phase Coherence Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To physically verify sub-10 ps alignment and cross-boot repeatability:

1. **RF Test Setup**:
   Connect a common RF signal generator (e.g. 2.4 GHz CW tone at -10 dBm) to a
   2-way resistive power splitter with length-matched RF cables connected to:
   - Channel RX0 on Node 0 (:adi:`EVAL-AD9084` board 0).
   - Channel RX0 on Node 1 (:adi:`EVAL-AD9084` board 1).

2. **Automated Cross-Board Capture with `pyadi-iio`**:
   Execute the following Python validation script on the host workstation to
   capture synchronized data buffers and calculate the inter-board phase delta:

.. code-block:: python

   import numpy as np
   import adi
   import matplotlib.pyplot as plt

   # Connect to both VCU118 MicroBlaze Linux nodes over Gigabit Ethernet
   ip_node0 = "ip:192.168.1.10"
   ip_node1 = "ip:192.168.1.11"

   sdr0 = adi.ad9084(uri=ip_node0)
   sdr1 = adi.ad9084(uri=ip_node1)

   # Configure identical receive settings
   fs = 4.0e9  # 4 GSPS RX sample rate
   sdr0.rx_sample_rate = fs
   sdr1.rx_sample_rate = fs
   sdr0.rx_enabled_channels = [0]
   sdr1.rx_enabled_channels = [0]
   sdr0.rx_buffer_size = 16384
   sdr1.rx_buffer_size = 16384

   # Trigger synchronous data capture
   data0 = sdr0.rx()[0]
   data1 = sdr1.rx()[0]

   # Compute relative phase angle between Node 0 and Node 1
   cross_corr = np.sum(data0 * np.conj(data1))
   phase_diff_deg = np.angle(cross_corr, deg=True)
   time_delay_ps = (np.angle(cross_corr) / (2 * np.pi * 2.4e9)) * 1e12

   print(f"Inter-Device Phase Difference: {phase_diff_deg:.2f}°")
   print(f"Equivalent Time Skew:          {time_delay_ps:.2f} ps")

   # Plot time-domain overlay
   t = np.arange(100) / fs * 1e9
   plt.figure(figsize=(10, 5))
   plt.plot(t, np.real(data0[:100]), label="Node 0 (AD9084-0)", color="tab:blue")
   plt.plot(t, np.real(data1[:100]), label="Node 1 (AD9084-1)", color="tab:red", linestyle="--")
   plt.title(f"Coherent ADC Tone Capture (Time Skew = {time_delay_ps:.2f} ps)")
   plt.xlabel("Time (ns)")
   plt.ylabel("ADC Amplitude")
   plt.legend()
   plt.grid(True)
   plt.savefig("mcs_phase_coherence.png")
   print("Plot saved to mcs_phase_coherence.png")

3. **Multi-Boot Repeatability Test**:
   Perform 50 consecutive link re-initialization cycles or board reboots.
   Measure the phase delta :math:`\Delta \phi` for each run. A successful MCS
   deployment will show:
   - Standard deviation of phase offset :math:`\sigma_{\Delta \phi} < 10\text{ ps}`.
   - Zero integer clock cycle jumps across reboots.

Troubleshooting & Diagnostics
-------------------------------------------------------------------------------

.. list-table:: Diagnostics and Failure Mode Resolution
   :widths: 25 35 40
   :header-rows: 1

   * - Error / Symptom
     - Root Cause
     - Recommended Action
   * - `MCS Initcal Status: Failed`
     - SYSREF not detected or timing difference > 0.4 clock cycles.
     - Verify differential BSYNC cabling and polarity. Check that ADF4030
       channel outputs are enabled and delivering nominal amplitude.
   * - `calc_delay exceeds 2x BSYNC period`
     - Extreme physical cable delay mismatch or signal reflection on BSYNC.
     - Inspect coaxial cables for damage. Ensure matched cable lengths between
       ADF4030 outputs and converter boards.
   * - `Trigger phase outside safe margin [16, 48]`
     - Trigger pulse arrives dangerously close to BSYNC transition edge.
     - Adjust `TRIG_PHASE` in the `axi_adf4030` register map to place the
       trigger edge within the 25%–75% safe window of the BSYNC cycle.
   * - `mcs_track_cal_validate: MISMATCH`
     - Apollo firmware bleed values do not match ADF4382 hardware state.
     - Verify DELADJ and DELSTR GPIO connections between Apollo and ADF4382.
       Ensure background tracking is enabled (`echo 1 > mcs_bg_track_cal_run`).
   * - `BSYNC Alignment Error latched`
     - Glitch, runt pulse, or phase jump detected on BSYNC clock.
     - Issue software reset to `axi_adf4030` (`echo 1 > sw_reset`). Check
       reference clock phase noise and supply decoupling.
   * - Inconsistent phase across reboots
     - Converter operates in Dual Clock mode without tracking calibration.
     - Switch device tree and hardware clocking to Single Clock mode (center PLL
       driving both Side A and Side B).

Related Documents & References
-------------------------------------------------------------------------------

- :ref:`ad9084` - AD9084-FMCA-EBZ Apollo MxFE System Reference Design
- :ref:`ad9084 quickstart microblaze` - VCU118 Quick Start Guide
- :external+linux:ref:`ad9088` - AD9084/AD9088 Linux Device Driver Documentation
- :external+hdl:ref:`axi_adf4030` - AXI ADF4030 HDL IP Core Specification
- :adi:`UG-2300` - AD9084/AD9088 Software Development User Guide
- :adi:`UG-2326` - EVAL-AD9084 Evaluation Board User Guide
- :adi:`ADF4030` - ADF4030 10-Channel Precision Synchronizer Product Page
- :adi:`ADF4382` - ADF4382 Low-Noise Clock Synthesizer Product Page
