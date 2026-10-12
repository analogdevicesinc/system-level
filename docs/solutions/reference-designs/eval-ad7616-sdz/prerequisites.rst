.. _eval-ad7616-sdz prerequisites:

Prerequisites
===============================================================================

What you need depends on which carrier platform you are targeting. As a
minimum, you need to start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The :adi:`EVAL-AD7616SDZ` evaluation board
#. A carrier platform — see the table below for supported options

   .. list-table::
      :header-rows: 1

      * - Carrier
        - Interface to EVAL-AD7616
        - Additional hardware required
      * - :xilinx:`ZedBoard`
        - FMC
        - :adi:`SDP-I-FMC` adapter board
      * - :xilinx:`ZC706`
        - FMC
        - :adi:`SDP-I-FMC` adapter board
      * - :adi:`SDP-K1`
        - Fly-wire (SPI)
        - STLINK-V3 programmer

#. Power supplies:

   - Both the :adi:`EVAL-AD7616SDZ` and the carrier must be powered via their
     respective connectors.

Software prerequisites
-------------------------------------------------------------------------------

#. **Xilinx Vivado and Vitis** — the supported version can be found on the
   `HDL releases page <https://github.com/analogdevicesinc/hdl/releases>`__.
   Required when targeting ZedBoard or ZC706 (FPGA-based flow).

#. **A UART terminal** (e.g. Tera Term or PuTTY):

   - ZedBoard / ZC706: baud rate **115200** (PS UART console)
   - SDP-K1: baud rate **230400** (IIO serial interface)

#. **STLINK-V3 drivers** — required when using the SDP-K1 carrier to flash the
   firmware.

#. **IIO Oscilloscope** (optional) — can be used to visualize the captured data
   when running the No-OS IIO project on the SDP-K1.

