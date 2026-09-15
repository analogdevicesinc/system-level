.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/no-os-setup

.. _ad-fmcomms2-ebz software no-os-setup:

AD9361 No-OS Setup
==================

Generic Platform
----------------

The AD9361 No-OS Software together with the Generic Platform Driver can be used
as a base for any microprocessor platform.

The Platform Driver implements the communication with the device and hides the
actual details of the communication protocol to the AD9361 driver. When the
desired type of processor is chosen, the specific communication functions have
to be implemented.

Code Size Information
~~~~~~~~~~~~~~~~~~~~~

The following information was obtained compiling the AD9361 project (with the
Generic Platform Driver integrated) using the gcc v4.7.2 and the *Optimize for
size (-Os)* option enabled.

::

   text    data     bss     dec     hex filename
  45159    1624      24   46807    b6d7 ad9361_generic

Note: The source code from the GitHub SHA
13c1ba56164f4b63844f63e5dd596286b6faf8b3 was used for calculating the code size
information
(https://github.com/analogdevicesinc/no-OS/tree/13c1ba56164f4b63844f63e5dd596286b6faf8b3/ad9361/sw).

Xilinx Platform
---------------

This guide provides some quick instructions on how to setup the AD-FMCOMMS2-EBZ
on either:

- :xilinx:`AC701 <AC701>`
- :xilinx:`KC705 <KC705>`
- :xilinx:`VC707 <VC707>`
- :xilinx:`ZC702 <ZC702>`
- :xilinx:`ZC706 <ZC706>`
- `Digilent ZED Board <http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,400,1028&Prod=ZEDBOARD>`__

.. important::

   The ML605 XPS project remain on this website only for legacy purposes. The
   support for XPS projects has been discontinued.

Required Software
~~~~~~~~~~~~~~~~~

- We"re upgrade the Xilinx tools on every release. The supported version number
  can be found in our
  `git repository <https://github.com/analogdevicesinc/hdl/tree/master>`__.

.. todo:: .. include: ./../../../../../resources/fpga/xilinx/software_setup.rst

Console Commands Driver
~~~~~~~~~~~~~~~~~~~~~~~

The Console Commands Driver is optional for the project. It was created in
addition to the AD9361 driver to control the part using some console commands.

AD9361 Reference Project Serial Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following commands were implemented for controlling the AD9361:

.. list-table::
   :header-rows: 1

   * - Command
     - Description
   * - help?
     - Displays all available commands.
   * - register?
     - Gets the specified register value.
   * - tx_lo_freq?
     - Gets current TX LO frequency [MHz].
   * - tx_lo_freq=
     - Sets the TX LO frequency [MHz].
   * - tx_samp_freq?
     - Gets current TX sampling frequency [Hz].
   * - tx_samp_freq=
     - Sets the TX sampling frequency [Hz].
   * - tx_rf_bandwidth?
     - Gets current TX RF bandwidth [Hz].
   * - tx_rf_bandwidth=
     - Sets the TX RF bandwidth [Hz].
   * - tx1_attenuation?
     - Gets current TX1 attenuation [mdB].
   * - tx1_attenuation=
     - Sets the TX1 attenuation [mdB].
   * - tx2_attenuation?
     - Gets current TX2 attenuation [mdB].
   * - tx2_attenuation=
     - Sets the TX2 attenuation [mdB].
   * - tx_fir_en?
     - Gets current TX FIR state.
   * - tx_fir_en=
     - Sets the TX FIR state.
   * - rx_lo_freq?
     - Gets current RX LO frequency [MHz].
   * - rx_lo_freq=
     - Sets the RX LO frequency [MHz].
   * - rx_samp_freq?
     - Gets current RX sampling frequency [Hz].
   * - rx_samp_freq=
     - Sets the RX sampling frequency [Hz].
   * - rx_rf_bandwidth?
     - Gets current RX RF bandwidth [Hz].
   * - rx_rf_bandwidth=
     - Sets the RX RF bandwidth [Hz].
   * - rx1_gc_mode?
     - Gets current RX1 GC mode.
   * - rx1_gc_mode=
     - Sets the RX1 GC mode.
   * - rx2_gc_mode?
     - Gets current RX2 GC mode.
   * - rx2_gc_mode=
     - Sets the RX2 GC mode.
   * - rx1_rf_gain?
     - Gets current RX1 RF gain.
   * - rx1_rf_gain=
     - Sets the RX1 RF gain.
   * - rx2_rf_gain?
     - Gets current RX2 RF gain.
   * - rx2_rf_gain=
     - Sets the RX2 RF gain.
   * - rx_fir_en?
     - Gets current RX FIR state.
   * - rx_fir_en=
     - Sets the RX FIR state.
   * - dds_tx1_f1_freq?
     - Gets current DDS TX1 F1 frequency [MHz].
   * - dds_tx1_f1_freq=
     - Sets the DDS TX1 F1 frequency [MHz].
   * - dds_tx1_f2_freq?
     - Gets current DDS TX1 F2 frequency [MHz].
   * - dds_tx1_f2_freq=
     - Sets the DDS TX1 F2 frequency [MHz].
   * - dds_tx1_f1_phase?
     - Gets current DDS TX1 F1 phase [degrees].
   * - dds_tx1_f1_phase=
     - Sets the DDS TX1 F1 phase [degrees].
   * - dds_tx1_f2_phase?
     - Gets current DDS TX1 F2 phase [degrees].
   * - dds_tx1_f2_phase=
     - Sets the DDS TX1 F2 phase [degrees].
   * - dds_tx1_f1_scale?
     - Gets current DDS TX1 F1 scale.
   * - dds_tx1_f1_scale=
     - Sets the DDS TX1 F1 scale.
   * - dds_tx1_f2_scale?
     - Gets current DDS TX1 F2 scale.
   * - dds_tx1_f2_scale=
     - Sets the DDS TX1 F2 scale.
   * - dds_tx2_f1_freq?
     - Gets current DDS TX2 F1 frequency [MHz].
   * - dds_tx2_f1_freq=
     - Sets the DDS TX2 F1 frequency [MHz].
   * - dds_tx2_f2_freq?
     - Gets current DDS TX2 F2 frequency [MHz].
   * - dds_tx2_f2_freq=
     - Sets the DDS TX2 F2 frequency [MHz].
   * - dds_tx2_f1_phase?
     - Gets current DDS TX2 F1 phase [degrees].
   * - dds_tx2_f1_phase=
     - Sets the DDS TX2 F1 phase [degrees].
   * - dds_tx2_f2_phase?
     - Gets current DDS TX2 F2 phase [degrees].
   * - dds_tx2_f2_phase=
     - Sets the DDS TX2 F2 phase [degrees].
   * - dds_tx2_f1_scale?
     - Gets current DDS TX2 F1 scale.
   * - dds_tx2_f1_scale=
     - Sets the DDS TX2 F1 scale.
   * - dds_tx2_f2_scale?
     - Gets current DDS TX2 F2 scale.
   * - dds_tx2_f2_scale=
     - Sets the DDS TX2 F2 scale.

Executing a Command Example
'''''''''''''''''''''''''''

Commands can be executed using a serial terminal connected to the UART
peripheral of the development board.

The following image shows an example of how the TX LO frequency can be set to
2.4 GHz using the corresponding command.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/software/fmcomms2_uart.png
   :width: 400px

.. todo:: .. include: /resources/eval/user-guides/ad-fmcomms2-ebz/downloads.rst

   :start-after: .. start-download-no-os
   :end-before: .. end-download-no-os

More Information
----------------

.. note::

   - :ez:`Ask questions about the FPGA reference design <community/fpga>`
