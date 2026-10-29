.. imported from: https://wiki.analog.com/resources/eval/dpg/eval-ad9783

.. _eval-ad9783 user-guide:

User guide
===============================================================================

The complete documentation of the evaluation board can be found at:

- :adi:`AD978x data sheet <media/en/technical-documentation/data-sheets/AD9780_9781_9783.pdf>`
- IBIS models: available for download from the :adi:`AD9783` product page

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9783` connects to the controller board (SDP-H1/ADS7-V2) or to
the FPGA carrier through the :adi:`AD-DAC-FMC` adapter board.

The main connectors and controls of the evaluation board are:

.. list-table::
   :header-rows: 1

   * - Reference
     - Description
   * - J1
     - Clock input (SMA)
   * - J5 (IOUT1P), J9 (IOUT2P)
     - DAC outputs (SMA)
   * - J2 (LO IN)
     - Local oscillator input of the ADL5375 modulator (SMA)
   * - J6 (RF OUT)
     - ADL5375 modulator output (SMA)
   * - P5, P6
     - 5 V power supply input
   * - S2
     - AD9783 chip reset
   * - XD1
     - USB status LED

.. _eval-ad9783 user-guide adl5375:

Using the ADL5375 modulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, solder jumpers JP4, JP5, JP6, and JP7 are configured to route the
DAC outputs to SMA J5 (IOUT1P) and to J9 (IOUT2P). This jumper setting is shown
on the left of :numref:`eval-ad9783 fig-jumper-config`. To connect the DAC
output to the filter that feeds into the :adi:`ADL5375`, the solder jumpers
should be reconfigured as shown on the right of
:numref:`eval-ad9783 fig-jumper-config`. Source the desired LO of the modulator
(i.e. 900 or 1800 MHz, 3 dBm) on SMA J2 (LO IN). The ADL5375 modulator output
can be observed on SMA J6 (RF OUT).

.. _eval-ad9783 fig-jumper-config:

.. figure:: images/ad9783-jumper-config.jpg
   :align: center
   :width: 800

   DAC output configuration (left) and modulator output configuration (right)

Using the ZCU102 carrier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use the SPI communication through a cable directly into the ZCU102 PMOD0, the
solder jumpers XJP1, XJP3, XJP4 and XJP5 must be desoldered from the evaluation
board, and the SPI signals are connected from XP3 of the evaluation board to
PMOD0 of the ZCU102. The steps and the pinout are described in
:ref:`eval-ad9783 quickstart zcu102`.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board is supplied with a **5 Vdc 1 A** power supply connected to
P5 and P6. The controller board (SDP-H1/ADS7-V2) is supplied separately with a
12 Vdc power supply.

The supply voltages of the evaluation board can be checked at:

- P5 and P6: 5 V
- TP3, TP5 and TP7: 3.3 V
- TP9 and TP11: 1.8 V

When using the ZCU102, the **Vadj** of the :adi:`AD-DAC-FMC` adapter board must
be set to **1.8 V** by writing its EEPROM, see
:ref:`eval-ad9783 quickstart zcu102`.

Schematic, PCB layout, bill of materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The design files (schematics, PCB layout, and BOM) for the AD9783-DPG2-EBZ RevB
and the AD9783-DUAL-EBZ RevB can be downloaded as an
:adi:`archive <media/en/technical-documentation/evaluation-documentation/eval-ad9783-design-files.zip>`
from the :adi:`EVAL-AD9783` evaluation board page. It contains:

-  Schematics: AD9783-DPG2-EBZ RevB, AD9783-DUAL-EBZ RevB
-  Bill of Materials: AD9783-DPG2-EBZ RevB, AD9783-DUAL-EBZ RevB
-  PCB Gerber files: AD9783-DPG2-EBZ RevB
-  PCB BRD file: AD9783-DPG2-EBZ RevB, AD9783-DUAL-EBZ RevB
-  PCB Layout PDF: AD9783-DPG2-EBZ RevB

The quick start guide for users of the DPG2 and DPG3 controller boards is
available as a
:adi:`PDF <media/en/technical-documentation/evaluation-documentation/eval-ad9783-81-80-evaluation-board-quick-start-guide.pdf>`.

Software guide
-------------------------------------------------------------------------------

The evaluation board is controlled from the PC through :adi:`ACE <ace>` and the
:dokuwiki:`DPG Lite <resources/tools-software/ace/dpg-lite>` application, using
an SDP-H1 or ADS7-V2 controller board. For a step-by-step walkthrough, see the
:ref:`eval-ad9783 quickstart sdp-h1-ace` guide.

Troubleshooting
-------------------------------------------------------------------------------

This section lists items to check and practices to use when debugging any
unexpected performance of a board. If unexpected results occur:

-  Check the voltage rails of the evaluation board. P5 and P6 should be 5 V;
   TP3, TP5, and TP7 should be 3.3 V; TP9 and TP11 should be 1.8 V.
-  Check if all (3) blue LEDs on the AD-DAC-FMC-ADP board are lit up. Reconnect
   the board to the FMC connector of the controller board (SDP-H1/ADS7-V2) if
   not lit up.
-  Check if the controller board (SDP-H1/ADS7-V2) is being supplied properly by
   the 12 Vdc adapter. Some LEDs on the controller board should be lit up.
-  Perform a chip reset by pressing S2 on the AD9783 evaluation board.
-  Power cycle both the controller board (SDP-H1/ADS7-V2) and the AD9783
   evaluation board.
-  Probe C18 and C19 to make sure a clock signal is being sent into the DAC.
-  Check if XD1 is lit up on the evaluation board. Reconnect/replace the USB
   cable connection to the evaluation board if it is not lit up.
-  Disconnect and reconnect the controller board (SDP-H1/ADS7-V2) and the AD9783
   evaluation board. Reopen the ACE and DPG Lite software.
