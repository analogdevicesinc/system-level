.. _eval-adar3000 user-guide:

User guide
===============================================================================

This user guide describes how to set up the ADAR3000/3001-EVALZ evaluation
board for the :adi:`ADAR3000` and :adi:`ADAR3001`, and how it connects to an
FPGA carrier. The :adi:`ADAR3000` and :adi:`ADAR3001` data sheets provide
additional information and should be consulted when using the evaluation
board.

Evaluation board hardware
-------------------------------------------------------------------------------

The ADAR3000/3001-EVALZ carries the beamformer, with its RF inputs RFIN1 to
RFIN4 and RF outputs RFOUT1 to RFOUT4 on 2.92 mm connectors, as single-ended
50 Ω coplanar waveguides. It is controlled through the 120-pin SDP connector
P5. On the bench it is usually driven by an SDP-S controller board and the
ACE software; in this reference design an SDP-I-FMC interposer adapts P5 to
the FMC connector of the FPGA carrier instead.

.. _eval-adar3000 user-guide power-supply:

Power supply
-------------------------------------------------------------------------------

The evaluation board is supplied from two bench supplies, applied to the test
loops on the board:

.. list-table:: Power supplies
   :header-rows: 1
   :widths: 20 30 20 30

   * - Rail
     - Test loops
     - Supply capability
     - Expected draw
   * - 1.2 V analog
     - Red ``1P2V`` to ``AGND``
     - 250 mA
     - 128 mA ± 12 mA (ADAR3000), 110 mA ± 10 mA (ADAR3001)
   * - 1.8 V digital
     - Red ``1P8V`` to ``DGND``
     - 20 mA
     - 7 mA ± 3 mA

The expected draw applies after power up and a soft reset, when the
amplifiers are enabled with their default bias setting of 3. With the
amplifiers disabled, the 1.2 V draw drops to about 1 mA.

The data sheet gives absolute maximum ratings of 1.32 V on V1P2 and 1.98 V on
V1P8, so set the over-voltage protection of the supplies below those values.

.. _eval-adar3000 user-guide hardware-configuration:

Hardware configuration
-------------------------------------------------------------------------------

Set the jumpers as follows for control from an FPGA carrier:

.. list-table:: Jumper settings
   :header-rows: 1
   :widths: 10 20 70

   * - Header
     - Setting
     - Function
   * - P8
     - Pin 1 to pin 2
     - Connects the chip's internal 1.0 V LDO output. Required.
   * - P9
     - Pin 1 to pin 2
     - Connects the chip's internal 1.0 V LDO output. Required.
   * - P4
     - Pin 1 to pin 2
     - Ties ``RESET_N`` (RSTB) to 1.8 V, as shipped. The no-OS project does not
       drive RSTB and resets the device with the soft reset sequence. Pin 2 to
       pin 3 holds the device in reset.
   * - P2
     - Open
     - Fitted, it forces the board SPI mux to bit-banged GPIO SPI.
   * - P12
     - Open
     - Fitted, it disables the SPI level translator U1.
   * - P13
     - Open
     - Fitted, it disables the control pin level translator U3.
   * - P6
     - No jumpers
     - ``ADDR[3:0]`` chip address pins, pulled down to address 0. Fit jumpers
       to give the device another address, matching the ``dev_addr`` the
       software uses.

Other headers expose signals for monitoring:

.. list-table:: Monitoring headers
   :header-rows: 1
   :widths: 10 90

   * - Header
     - Signals
   * - P1
     - SPI and beam command signals at 1.8 V, after the level translators, plus
       the 1.2 V and 1.8 V supplies
   * - P10
     - SPI signals at VIO, before the level translators, plus the supplies
   * - P14
     - SDP connector signals at VIO: SPI and GPIO0 to GPIO7
   * - P3
     - ADC inputs ANLG0 (pin 1) and ANLG1 (pin 3)
   * - P7
     - DAC output (pin 1)
   * - P11
     - Chip GPIO0 to GPIO3

.. _eval-adar3000 user-guide control-interface:

Control interface
-------------------------------------------------------------------------------

All control signals reach the device through the SDP connector P5. The logic
level on the SDP side is VIO, which the controller supplies on P5: 3.3 V from
an SDP-S, and the FMC ``VADJ`` rail through the SDP-I-FMC interposer. Two
level translators shift VIO to the device's 1.8 V:

- U1 carries the SPI: chip select, clock, MOSI and MISO.
- U3 carries the control pins: ``RESET_N`` (RSTB), ``UPDATE``, ``RESET`` and
  ``MUTE``.

Ahead of U1, the 2:1 mux U5 selects the SPI source. With its select input,
SDP GPIO3, low it passes the SDP hardware SPI; with it high it passes
bit-banged SPI on SDP GPIO0 to GPIO2.

On the :xilinx:`ZCU102`, the SPI comes from the ZynqMP PS SPI0 controller
routed through EMIO, and the control pins from EMIO GPIOs:

.. list-table:: ZCU102 control signals
   :header-rows: 1
   :widths: 20 25 55

   * - Signal
     - ZynqMP source
     - Function
   * - SPI0
     - PS SPI0 via EMIO
     - Register access, mode 0, MSB first, up to 1 MHz
   * - ``spi_sel_a``
     - spi0_csn[0]
     - Chip select
   * - GPIO 3
     - EMIO 35
     - SPI mux select, driven low
   * - GPIO 4
     - EMIO 36
     - ``UPDATE``, beamstate update strobe
   * - GPIO 5
     - EMIO 37
     - ``RESET``, beam reset qualifier
   * - GPIO 6
     - EMIO 38
     - ``MUTE``, beam mute qualifier
   * - GPIO 7
     - EMIO 39
     - ``RESET_N`` (RSTB), not driven, see P4 above

The no-OS driver drives the mux select low during initialization. The
complete HDL interface is documented in the
:external+hdl:ref:`ADAR3000 HDL project <adar3000>`.

.. _eval-adar3000 user-guide vadj:

FMC VADJ
-------------------------------------------------------------------------------

Through the interposer, VIO is the carrier's FMC ``VADJ`` rail, which must be
at **1.8 V**. ``VADJ`` also supplies the FPGA I/O banks behind the FMC
connector; at 0 V no pin on that connector can drive, and the SDP side of the
level translators is unpowered.

On the :xilinx:`ZCU102`, ``VADJ`` is not fixed. At power up the board's system
controller reads the IPMI FRU EEPROM of the card in the FMC slot, per the
VITA 57.1 standard, and sets ``VADJ`` from the DC Load record it finds. If no
valid record is present it leaves ``VADJ`` at 0 V. With this setup the card in
the FMC slot is the SDP-I-FMC interposer, and it ships with a blank EEPROM.

The symptom is easy to misread: the FPGA configures, the application runs, SPI
initialization succeeds, and every register read returns ``0xFF`` because MISO
floats. The 1.8 V supply of the evaluation board may also draw far more than
expected, around 47 mA instead of 7 mA, as the control lines drive into the
unpowered FPGA I/O bank. If the no-OS example reports a scratchpad mismatch,
check ``VADJ`` before suspecting the software or the wiring.

To set ``VADJ`` to 1.8 V, either:

- program the interposer's FRU EEPROM with a record requesting 1.8 V, which
  persists across power cycles. See :ref:`software fru-dump`.
- or override ``VADJ`` with the ZCU102 system controller user interface, as
  described in the *ZCU102 Evaluation Board User Guide* (UG1182). The override
  does not persist and has to be repeated after every power cycle.

Schematic, PCB Layout, Bill of Materials
-------------------------------------------------------------------------------

The board is the ADAR3000/3001-EVALZ, schematic 02-059137 revision C. Contact
Analog Devices for its design files.
