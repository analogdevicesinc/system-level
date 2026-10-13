.. _xud1a:

ADXUD1AEBZ (XUD1A) X to C Band Up/Down Converter Board
===============================================================================

.. figure:: images/eval-adxud1aebz_angle.jpg
   :width: 600

   ADXUD1AEBZ

General Description
-------------------------------------------------------------------------------

The ADXUD1AEBZ evaluation board is a quad channel Up and Down converter designed
for X Band general purpose use. The complete Analog Devices solution chain
consists of amplifiers, LNAs, switches, mixers, integrated pll/VCO, and power
management circuitry all powered by a single +12V power supply. Frequency
conversion can be accomplished using either the integrated pll/VCO or an
external LO. This evaluation board is intended to be used with an external Low
Noise Amplifier and Power Amplifier to set the desired noise figure and output
power of the user's signal chain.

The ADXUD1AEBZ consists of 4 channels capable of up and down conversion over a
RF frequency band from 8 GHz to 12 GHz and IF frequency band from 4.2 GHz to 6.3
GHz. The RF input/outputs on the evaluation board are brought out to SMA coaxial
connectors whereas the IF input/outputs are brought out to SMPM coaxial
connectors specifically designated for transmit or receive. Digital control via
GPIO and SPI lines are established through a PMOD connector with a compatible
interposer board to allow :adi:`System Demonstration Platform (SDP-S) <SDP-S>`
and FMC Mezzanine connector options. Control signals for the board are expected
to be 1.8V logic with on-board level translators converting to the on-board
logic level of 3.3V.

.. figure:: images/eval-adxud1aebz_top-web.gif
   :width: 600

   ADXUD1AEBZ Board: Front

.. figure:: images/eval-adxud1aebz_bottom.jpg
   :width: 600

   ADXUD1AEBZ Board: Back

Requirements
-------------------------------------------------------------------------------

Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`HMC903LP3E Datasheet <media/en/technical-documentation/data-sheets/HMC903.pdf>`
-  :adi:`ADL8111 Datasheet <media/en/technical-documentation/data-sheets/ADL8111.pdf>`
-  :adi:`HMC8411LP2FE Datasheet <media/en/technical-documentation/data-sheets/HMC8411LP2FE.pdf>`
-  :adi:`HMC963LC4 Datasheet <media/en/technical-documentation/data-sheets/HMC963.pdf>`
-  :adi:`HMC383LC4 Datasheet <media/en/technical-documentation/data-sheets/HMC383.pdf>`
-  :adi:`HMC773ALC3B Datasheet <media/en/technical-documentation/data-sheets/HMC773ALC3B.pdf>`
-  :adi:`ADF4371 Datasheet <media/en/technical-documentation/data-sheets/ADF4371.pdf>`
-  :adi:`ADRF5020 Datasheet <media/en/technical-documentation/data-sheets/ADRF5020.pdf>`
-  :adi:`HMC652LP2E Datasheet <media/en/technical-documentation/data-sheets/hmc652lp2-hmc655lp2.pdf>`

-  ADXUD1AEBZ Rev. D Design:

   -  :download:`Schematic <files/02-065073-01-d.pdf>`
   -  :download:`Bill of Materials <files/xud1a_bom.zip>`

-  Interposer Board Rev. A Design:

   -  :download:`Schematic <files/02-067148-01-a.pdf>`
   -  :download:`Bill of Materials <files/interposerbom.zip>`

-  Interposer Board Rev. B Design:

   -  :download:`Schematic <files/02-067148-01-b.pdf>`
   -  :download:`Bill of Materials <files/interposerbom-b.zip>`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ADXUD1AEBZ
-  Interposer Board
-  SMA-SMA cabling to interface with the RF ports
-  SMPM-SMA cabling to interface with the IF ports
-  Digital controller and any associated hardware (:adi:`SDP-S` or PMOD)

.. warning::

   The SDP-S is the only SDP controller which will work with XUD1A.

   | All other SDP controllers (SDP-B, SDP-H1, SDP-K1) are **NOT** compatible.

Suggested Test Equipment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  20GHz RF Signal Generator (2x)
-  20GHz Spectrum Analyzer
-  20GHz Vector Network Analyzer (optional)
-  Oscilloscope (optional)
-  RF Power Meter (optional)

Software/Digital Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PMOD Control

-  Two 14-pin PMOD cables (`Example <https://www.digikey.com/en/products/detail/assmann-wsw-components/H3AKH-1406G/998997>`_)
-  Example PMOD digital controllers:

   -  `Raspberry Pi <https://www.raspberrypi.org/>`_
   -  FPGA demonstration board
   -  `Arduino <https://www.arduino.cc/>`_
   -  `FTDI <https://www.ftdichip.com/>`_

SDP Control

-  `SDP Drivers <http://swdownloads.analog.com/ACE/SDP/SDPDrivers.exe>`_
-  :dokuwiki:`Basic SDP-S Test Program Rev A <_media/resources/eval/user-guides/xud1a/sdp_xud1a.zip>`
-  :dokuwiki:`Basic SDP-S Test Program Rev B <_media/resources/eval/user-guides/xud1a/sdps_xud1a_r1.zip>`

.. note::

   Windows 10 might try to block the example Test Program, you'll have to
   explicitly allow it in your security settings

- :adi:`SDP-S controller board <sdp-s>`

.. _xud1a software:

Software

- :git-pyadi-iio:`PyADI-IIO </>` interface for LibIIO

   -  :git-pyadi-iio:`ADF4371 Wrapper <adi/adf4371.py>`
   -  :external+pyadi-iio:doc:`ADF4371 Documentation <devices/adi.adf4371>`

- :download:`Standalone Python Application using SDP-S Controller <files/xud_ctrl.zip>`

Board Design
-------------------------------------------------------------------------------

The ADXUD1AEBZ evaluation board has 4 SMA RFIO connectors for the RF
Input/Output and 8 SMPM RFIO connectors for the IF Input/Output. The 8 SMPM
connectors have 4 Rx IF channels and 4 Tx IF channels. There is 1 SMA connector
available to supply an external LO signal. The board is configured for an
external LO by default. A capacitor can be rotated to disable the external LO
port and access the internal pll/VCO (ADF4371). The pll/VCO can be programmed
via SPI to allow an on-board LO signal.

One 12V DC barrel jack is provided to apply the required 12V power supply with
on-board power management circuitry to convert to the necessary power rails.

One 14 PIN PMOD connector is provided to apply GPIO/SPI digital control lines.

Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADXUD1AEBZ board must be powered from the included power supply with a
voltage level of 12V. There is an on-board power management tree which generates
the required voltage rails for all of the associated parts.

.. _xud1a block diagram:

RF/IF Signal Chain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADXUD1AEBZ has 4 RF input/output SMA connectors and 4 Tx IF inputs and 4 Rx
IF outputs via SMPM connectors. Each RF channel is bandpass filtered and tied to
two :adi:`ADRF5020` switches with independent :adi:`HMC903 <hmc903lp3e>`
amplifiers for Tx and Rx. Up/down conversion is accomplished using the
:adi:`HMC773A <hmc773alc3b>` with the option to drive the LO either externally
via the J4 SMA connector or internally with the :adi:`adf4371`. The Rx IF
channel is amplified by the :adi:`ADL8111` and :adi:`hmc8411` whereas the Tx IF
channel is internally bypassed by the :adi:`ADL8111`.

.. figure:: images/xud1a_revd_blockdiagram.png
   :width: 800

   ADXUD1AEBZ Block Diagram

LO Signal Chain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The LO signal is amplified by :adi:`HMC963 <hmc963lc4>` and :adi:`HMC383
<hmc383lc4>` amplifiers and divided across all channels to provide a common LO
signal. The user can decide between an internal pll or external LO. The internal
pll is the :adi:`adf4371` with an option for an external reference via J3
connector or an on-board VCXO reference. An external LO source can be injected
via the J4 SMA connector. When using an external LO, the recommended input power
to J4 is +5 dBm.

By default, the board populates C165 for an external LO source with C61 not
installed. The user can remove C165 and re-install on the C61 pad to enable use
of the ADF4371. When using the onboard ADF4371, the default reference is the
onboard VCXO with C372 installed and C373 not installed. The user can remove
C372 and re-install on the C373 pad to enable use of the external reference
port J3.

.. note::

   An external LO source is recommended for performance based measurements. The
   on-board ADF4371 is provided for convenience to allow stand-alone operation
   of the hardware for a wide range of operational frequencies. A bandpass
   filter should be inserted in the ADF4371 pll output path depending on the
   final frequency plan to reject the harmonic content generated by the ADF4371
   internal multipliers.

Digital Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PMOD Pinout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The digital input signals are intended to be 1.8V logic while the
:adi:`ADRF5020`, :adi:`ADL8111`, and :adi:`ADF4371` digital control inputs
require logic levels of 3.3V. Level translators and digital logic circuitry have
been included between the PMOD connector and aforementioned components.

.. figure:: images/xud1a_pmod.png
   :width: 400

   ADXUD1AEBZ PMOD Pinout

Interposer Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Interposer board allows the option to control the ADXUD1AEBZ via
:adi:`System Demonstration Platform (SDP-S) <SDP-S>` and FPGA via FMC Mezzanine
connector. Note the Interposer board PMOD connector is pin compatible with the
ADXUD1AEBZ PMOD connector and can be connected directly to XUD1A.

.. figure:: images/xud1a_sdps.png
   :width: 600

   ADXUD1AEBZ Interposer Pinout with SDP-S Connector

Control Logic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The PMOD inputs are fed to a buffer and logic network for simplified board
control and quick switching time.

.. figure:: images/xud1a_controlblockdiagram.png
   :width: 600

   ADXUD1AEBZ Control Block Diagram

.. list-table:: ADXUD1AEBZ RF Control Logic
   :header-rows: 1

   * - Channel
     - Mode
     - TxRx0
     - TxRx1
     - TxRx2
     - TxRx3
     - Rx Gain Mode
   * - A
     - Tx
     - 1
     - \-
     - \-
     - \-
     - 0
   * -
     - Rx Low Gain
     - 0
     - \-
     - \-
     - \-
     - 0
   * -
     - Rx High Gain
     - 0
     - \-
     - \-
     - \-
     - 1
   * - B
     - Tx
     - \-
     - 1
     - \-
     - \-
     - 0
   * -
     - Rx Low Gain
     - \-
     - 0
     - \-
     - \-
     - 0
   * -
     - Rx High Gain
     - \-
     - 0
     - \-
     - \-
     - 1
   * - C
     - Tx
     - \-
     - \-
     - 1
     - \-
     - 0
   * -
     - Rx Low Gain
     - \-
     - \-
     - 0
     - \-
     - 0
   * -
     - Rx High Gain
     - \-
     - \-
     - 0
     - \-
     - 1
   * - D
     - Tx
     - \-
     - \-
     - \-
     - 1
     - 0
   * -
     - Rx Low Gain
     - \-
     - \-
     - \-
     - 0
     - 0
   * -
     - Rx High Gain
     - \-
     - \-
     - \-
     - 0
     - 1


.. list-table:: ADXUD1AEBZ ADF4371 Control Logic
   :header-rows: 1

   * - ADF4371 Output
     - PLL_OUTPUT_SEL
   * - 8 - 16 GHz
     - 1
   * - 16 - 32 GHz
     - 0

Data Set
-------------------------------------------------------------------------------

Data was collected on a total of four boards. With 4 channels per board, there
are a total of 16 datasets per measurement characterizing the XUD1A boards
across all states (Rx High Gain, Rx Low Gain, and Tx). Units were tested in a
fixed IF configuration (swept LO & swept RF) with an IF Frequency of 4.5 GHz.

Receive High Gain Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/rx_hg_s11.png
   :width: 600

   Rx High Gain Mode S11

.. figure:: images/rx_hg_s21.png
   :width: 600

   Rx High Gain Mode S21

.. figure:: images/rx_hg_s22.png
   :width: 600

   Rx High Gain Mode S22

Noise Figure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/rx_hg_nf.png
   :width: 600

   Rx High Gain Mode Noise Figure

IIP3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/rx_hg_iip3.png
   :width: 600

   Rx High Gain Mode IIP3

Data Tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Rx High Gain Mode Gain (dB)
   :header-rows: 1

   * - Frequency
     - Minimum
     - Average
     - Maximum
   * - 8 GHz
     - 13.36
     - 14.63
     - 15.30
   * - 9 GHz
     - 13.72
     - 14.74
     - 15.81
   * - 10 GHz
     - 12.61
     - 14.32
     - 15.58
   * - 11 GHz
     - 12.78
     - 13.48
     - 14.24
   * - 12 GHz
     - 11.90
     - 13.38
     - 14.55

.. list-table:: Rx High Gain Mode Noise Figure (dB)
   :header-rows: 1

   * - Frequency
     - Minimum
     - Average
     - Maximum
   * - 8 GHz
     - 14.37
     - 14.72
     - 15.53
   * - 9 GHz
     - 14.13
     - 14.93
     - 15.54
   * - 10 GHz
     - 14.07
     - 15.16
     - 16.32
   * - 11 GHz
     - 15.45
     - 16.49
     - 17.09
   * - 12 GHz
     - 15.25
     - 16.17
     - 17.76

.. list-table:: Rx High Gain Mode Input IP3 (dBm)
   :header-rows: 1

   * - Frequency
     - Minimum
     - Average
     - Maximum
   * - 8 GHz
     - 7.06
     - 7.59
     - 8.18
   * - 9 GHz
     - 7.70
     - 8.31
     - 8.81
   * - 10 GHz
     - 7.72
     - 8.75
     - 9.59
   * - 11 GHz
     - 9.17
     - 9.74
     - 10.54
   * - 12 GHz
     - 9.75
     - 10.40
     - 11.26

Receive Low Gain Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/rx_lg_s11.png
   :width: 600

   Rx Low Gain Mode S11

.. figure:: images/rx_lg_s21.png
   :width: 600

   Rx Low Gain Mode S21

.. figure:: images/rx_lg_s22.png
   :width: 600

   Rx Low Gain Mode S22

Noise Figure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/rx_lg_nf.png
   :width: 600

   Rx Low Gain Mode Noise Figure

IIP3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/rx_lg_iip3.png
   :width: 600

   Rx Low Gain Mode IIP

Data Tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Rx Low Gain Mode Gain (dB)
   :header-rows: 1

   * - Frequency
     - Minimum
     - Average
     - Maximum
   * - 8 GHz
     - -1.69
     - -0.32
     - 0.38
   * - 9 GHz
     - -1.29
     - -0.13
     - 0.88
   * - 10 GHz
     - -2.33
     - -0.53
     - 0.96
   * - 11 GHz
     - -2.26
     - -1.36
     - -0.50
   * - 12 GHz
     - -3.02
     - -1.43
     - -0.17

.. list-table:: Rx Low Gain Mode Noise Figure (dB)
   :header-rows: 1

   * - Frequency
     - Minimum
     - Average
     - Maximum
   * - 8 GHz
     - 14.43
     - 17.17
     - 18.35
   * - 9 GHz
     - 14.40
     - 17.30
     - 18.34
   * - 10 GHz
     - 14.31
     - 17.53
     - 19.14
   * - 11 GHz
     - 16.58
     - 18.72
     - 19.57
   * - 12 GHz
     - 15.39
     - 18.55
     - 20.50

.. list-table:: Rx Low Gain Mode Input IP3 (dBm)
   :header-rows: 1

   * - Frequency
     - Minimum
     - Average
     - Maximum
   * - 8 GHz
     - 7.67
     - 8.25
     - 9.14
   * - 9 GHz
     - 8.49
     - 9.16
     - 9.88
   * - 10 GHz
     - 8.58
     - 9.72
     - 10.59
   * - 11 GHz
     - 10.61
     - 11.10
     - 11.8
   * - 12 GHz
     - 10.83
     - 11.53
     - 12.50

Tx Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/tx_s11.png
   :width: 600

   Tx Mode S11

.. figure:: images/tx_s21.png
   :width: 600

   Tx Mode S21

.. figure:: images/tx_s22.png
   :width: 600

   Tx Mode S22

IP3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/tx_oip3.png
   :width: 600

   Tx Mode OIP3

.. figure:: images/tx_iip3.png
   :width: 600

   Tx Mode IIP3

Data Tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Tx Mode Gain (dB)
   :header-rows: 1

   * - Frequency
     - Minimum
     - Average
     - Maximum
   * - 8 GHz
     - -13.86
     - -13.10
     - -12.73
   * - 9 GHz
     - -13.64
     - -12.51
     - -11.59
   * - 10 GHz
     - -13.21
     - -12.12
     - -11.15
   * - 11 GHz
     - -14.72
     - -13.87
     - -12.70
   * - 12 GHz
     - -14.63
     - -13.93
     - -13.25

.. list-table:: Tx Mode Output IP3 (dBm)
   :header-rows: 1

   * - Frequency
     - Minimum
     - Average
     - Maximum
   * - 8 GHz
     - 7.67
     - 8.25
     - 9.14
   * - 9 GHz
     - 8.49
     - 9.16
     - 9.88
   * - 10 GHz
     - 8.58
     - 9.72
     - 10.59
   * - 11 GHz
     - 10.61
     - 11.10
     - 11.8
   * - 12 GHz
     - 10.83
     - 11.53
     - 12.50

Switching Speed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Switching Speed (ns)
   :header-rows: 1

   * - Mode
     - Edge Type
     - Minimum
     - Average
     - Maximum
   * - All Modes
     - Rising
     - 146.4
     - 159.2
     - 178.4
   * -
     - Falling
     - 11.4
     - 13.9
     - 20.8

.. note::

   Switching Speed measurements captured for an RF Frequency of 10 GHz,
   LO Frequency of 14.5 GHz and IF Frequency of 4.5 GHz.

Evaluation
-------------------------------------------------------------------------------

Software Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two methods to control the XUD1A board using the interposer board.
Either over the FMC connector using the ZCU102 FPGA or over the SDP connector
using a SDP-S controller. Limited functionality is available using the SDP-S
controller, but a user has the basic ability to program the state of XUD1A (Tx,
Rx Low Gain, Rx High Gain).

Standalone Python Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the application from the :ref:`Software <xud1a software>` section.
Extract the file contents to your desired PC drive. It is recommended to save
the folder to your root drive for simplicity. Using your preferred command
terminal, change the directory to the desired state folder (e.g.
`>> cd C:/XUD1A_ctrl/TX`). Execute the application through the terminal window.
