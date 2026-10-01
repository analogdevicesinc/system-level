.. _stingray:

ADAR1000EVAL1Z (Stingray) X/Ku-Band Analog Beamforming Front-End
===============================================================================

.. figure:: images/adar1000eval1z_angle-evaluation-board.jpg
   :width: 800

   ADAR1000EVAL1Z

General Description
-------------------------------------------------------------------------------

The ADAR1000-EVAL1Z evaluation board is an analog beamforming front-end designed
for testing the performance of the :adi:`adar1000` and :adi:`adtr1107`. The
:adi:`adar1000` is an 8 GHz to 16 GHz, 4-Channel, X Band and Ku Band Beamformer
IC. The :adi:`adtr1107` is a 6 GHz to 18 GHz, Front-End Transmit/Receive module.

The ADAR1000-EVAL1Z board consists of 8 RF cells. Each cell contains a core
:adi:`adar1000` surrounded by four :adi:`ADTR1107s <adtr1107>`. All RF
input/outputs on the evaluation board are brought out to SMPM coaxial
connectors. There is a 12V power input and all required voltage rails for the
board are generated on-board. Digital control of the board as well as the
beamformers is enabled using either an
:adi:`System Demonstration Platform (SDP-S) <SDP-S>` connector or a dual PMOD
interface. Control signals for the board are expected to be 3.3V logic with
on-board level translators converting this to the on-chip logic level of 1.8V.

.. figure:: images/adar1000eval1z_top-web.gif
   :width: 600

   ADAR1000EVAL1Z Front

.. figure:: images/adar1000eval1z_bottom-web.gif
   :width: 600

   ADAR1000EVAL1Z Back

.. figure:: images/adar1000eval1z_top_kit.jpg
   :width: 600

   ADAR1000EVAL1Z with Heatsink

.. figure:: images/adar1000eval1z_bottom_kit-web.jpg
   :width: 600

   ADAR1000EVAL1Z with Antenna Tiles

Main RFICs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ADAR1000: 8 GHz to 16 GHz, 4-Channel, X Band and Ku Band Beamformer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :adi:`ADAR1000 Product page <adar1000>`

ADTR1107: 6 GHz to 18 GHz, Front-End Transmit/Receive Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :adi:`ADTR1107 Product page <adtr1107>`

Peripheral ICs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RF Detector Block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :adi:`HMC948 Log Detector <hmc948>`
-  :adi:`ADA4807-1 180MHz, Rail-to-Rail Input/Output Operational Amplifier <ada4807-1>`
-  :adi:`LTC2314-14 14-Bit, 4.5Msps Serial Sampling ADC <ltc2314-14>`

Power Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :adi:`LT8652S Dual Channel 18V/8.5A, Synchronous Step-Down Silent Switcher <lt8652s>`
-  :adi:`LT8642S 18V/10A Synchronous Step-Down Silent Switcher 2 <lt8642s>`
-  :adi:`LT3093 –20V/200mA, Ultralow Noise, Ultrahigh PSRR Negative Linear Regulator <lt3093>`
-  :adi:`LT3094 −20V/500mA, Ultralow Noise, Ultrahigh PSRR Negative Linear Regulator <lt3094>`
-  :adi:`LT8606 42V/350mA Synchronous Step-Down Regulator <lt8606>`
-  :adi:`ADP150-1.8 1.8V Ultralow Noise, 150 mA CMOS Linear Regulator <adp150>`
-  :adi:`ADP5074 2.4A, DC-to-DC Inverting Regulator <adp5074>`

Control & Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :adi:`ADM1172-1 Hot Swap Controller with Power-Fail Comparator <adm1172>`
-  :adi:`ADM1186-2 Quad Voltage Sequencer and Monitor with Programmable Timing <adm1186>`
-  :adi:`LTC2992 Dual, Wide-Range Power Monitor with GPIO <ltc2992>` **(RevB only)**
-  :adi:`LTC4301 Supply Independent Hot Swappable 2-Wire Bus Buffer <ltc4301>` **(RevB only)**

Requirements
-------------------------------------------------------------------------------

Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`ADAR1000 Datasheet <media/en/technical-documentation/data-sheets/ADAR1000.pdf>`
-  :adi:`ADTR1107 Datasheet <media/en/technical-documentation/data-sheets/ADTR1107.pdf>`
-  :download:`Assembly Drawing <files/stingray_assembly_v2.pdf>`
-  :download:`Board Dimensions <files/stingray_dimensions.zip>`
-  Rev. A design:

   -  :download:`Schematic <files/059522a_modified.pdf>`
   -  :download:`BOM <files/059522a_bom.zip>`

-  Rev. B/C design:

   -  :download:`Schematic <files/02_059522b_top.pdf>`
   -  :download:`BOM <files/059522b_bom.zip>`

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ADAR1000-EVAL1Z Evaluation Board Kit
-  Snap-on Antenna Board (available upon request)
-  SMPM-SMA cabling to interface with the RF ports
-  Digital controller and any associated hardware (:adi:`SDP-S` or PMOD)

.. warning::

   The SDP-S is the only SDP controller which will work with Stingray.

   | All other SDP controllers (SDP-B, SDP-H1, SDP-K1) are **NOT** compatible
     with the Stingray platform.

Suggested Test Equipment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  20GHz RF Signal Generator
-  20GHz Spectrum Analyzer
-  20GHz Vector Network Analyzer
-  Thermal Camera (optional)
-  Oscilloscope (optional)
-  RF Power Meter (optional)

Software/Digital Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PMOD Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Two 12-pin PMOD cables (:mouser:`Example <200-IDSD06D1800R>`)
-  Four 12-pin 0.100" male-male headers (`Example <https://www.digikey.com/en/products/detail/samtec-inc/TSW-106-22-T-D/7867287>`_)
-  Example PMOD digital controllers:

   -  `Raspberry Pi <https://www.raspberrypi.org/>`_
   -  FPGA demonstration board
   -  `Arduino <https://www.arduino.cc/>`_
   -  `FTDI <https://www.ftdichip.com/>`_

SDP Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `SDP Drivers <http://swdownloads.analog.com/ACE/SDP/SDPDrivers.exe>`_
-  :dokuwiki:`Basic SDP Test Program <_media/resources/eval/user-guides/stingray/stingray_test.zip>`
   (Windows 10 might try to block this, you'll have to explicitly allow it in your security settings)
-  :adi:`SDP-S controller board <sdp-s>`

.. note::

   SDP Control is fine for initial characterization. Recommended to use the
   linux drivers for end system control for easier software control and software
   scalability.


Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  :git-linux:`ADAR1000 LibIIO Linux Driver <drivers/iio/beamformer/adar1000.c>`

   - :external+linux:ref:`Driver Documentation <adar1000>`

- :git-pyadi-iio:`PyADI-IIO </>` interface for LibIIO

   -  :git-pyadi-iio:`ADAR1000 wrapper <adi/adar1000.py>`
   -  :external+pyadi-iio:doc:`ADAR1000 Documentation <devices/adi.adar1000>`
   -  :git-pyadi-iio:`Example for single ADAR1000 <examples/adar1000_single_example.py>`
   -  :git-pyadi-iio:`Example for array of ADAR1000s <examples/adar1000_array_example.py>`

Board Design
-------------------------------------------------------------------------------

The ADAR1000-EVAL1Z evaluation board has 8 SMPM RFIO connectors for the 8 cells
on the component side of the board. There are 33 SMPM connectors on the opposite
side of the board. 32 of these correspond to the 32 RF channels while the last
connector goes to the RF detector and ADC combo on the bottom of the board which
is intended to be used for calibration.

Two 6-pin Molex "Mini-Fit Jr." connectors are provided to apply the required 12V
power supply. One is for the power supply input, and the other can be used to
daisy-chain a second board to power both boards using one power supply. Note
that the included power supply can only support two ADAR1000-EVAL1Z boards.

Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADAR1000-EVAL1Z board must be powered from the included power supply with a
voltage level of 12V. There is an on-board power management tree which generates
the required voltage rails for all of the associated parts.

RF Input and Output Signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADAR1000-EVAL1Z board has 41 surface-mounted SMPM connectors which are
described in the table below.

.. list-table:: RF Connectors
   :header-rows: 1

   * - Connector(s)
     - Name(s)
     - Description
   * - J1 - J8
     - RFIOx
     - ADAR1000 RFIO Connectors
   * - J1_1 - J1_8, J2_1 - J2_8, J3_1 - J3_8, J4_1 - J4_8
     - ANT1_1 - ANT1_8, ANT2_1 - ANT2_8, ANT3_1 - ANT3_8, ANT4_1 - ANT4_8
     - Antenna Connectors
   * - J9
     - N/A
     - RF Detector Input Connector

.. figure:: images/component_side_overview.png
   :width: 600

   ADAR1000-EVAL1Z Component Side Overview

.. figure:: images/antenna_side_overview.png
   :width: 600

   ADAR1000-EVAL1Z Antenna Side Overview

Digital Signals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The digital input signals are intended to be 3.3V logic while the
:adi:`adar1000` requires logic levels of 1.8V. To protect the :adi:`adar1000`,
level translators have been included between the digital connectors and the
:adi:`ADAR1000s <adar1000>`. There are test points on the 1.8V side of the level
translators, but these are not meant to be used to inject signals, only to view
the signals reaching the :adi:`ADAR1000s <adar1000>`.

PMOD Pinout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/pmod_pinout.png
   :width: 600

   ADAR1000-EVAL1Z PMOD Pinout

SPI Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ADAR1000-EVAL1Z has five chip-select lines available for use. Four of these
lines (CSB1, CSB2, CSB3, CSB4) are intended to be used for the
:adi:`ADAR1000s <adar1000>` while the last line (CSB5) is dedicated for the RF
detector/ADC combo on the antenna side of the board.

Each :adi:`adar1000` has two ADDRx pins which can be used to control 4 separate
:adi:`ADAR1000s <adar1000>` using only one CSB line. See the
:adi:`ADAR1000 Datasheet <media/en/technical-documentation/data-sheets/ADAR1000.pdf>`
for details on this. As the ADAR1000-EVAL1Z has eight :adi:`ADAR1000s <adar1000>`,
a minimum of two CSB lines are needed to have control over all the
individual ICs. There are two CSB selector switches (S1, S2) which select the
CSB line for the associated side of the board. Looking at the component side of
the board, the left four :adi:`ADAR1000s <adar1000>` use the CSB line selected
by S1 while the right four :adi:`ADAR1000s <adar1000>` use the CSB line selected
by S2.

.. figure:: images/csb_selectors.jpg
   :width: 600

   CSB Selector Switches

The ADAR1000-EVAL1Z alone demonstrates a small beamformer array, but multiple
boards can also be stacked and combined to create larger arrays. In order to
simplify the digital interface, two boards can be controlled using one digital
controller if the two boards use all four of the available CSB lines without
worrying about talking to the wrong IC.

Data Set
-------------------------------------------------------------------------------

Receive Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gain, Return Loss
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/stingray_rx_spars_maxgain.png
   :width: 600

   Gain and Return Loss vs. Frequency, at Maximum Gain, Receive Channel

.. figure:: images/stingray_rx_gain_gain.png
   :width: 600

   Gain vs. Frequency for Gain Settings from 0 to 127, Single Receive Channel

Noise Figure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure:: images/stingray_rx_nf_over_gain.png
   :width: 600

   Noise Figure vs. Frequency over Gain, Receive Channel

Input P1dB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/stingray_rx_ip1db_gain.png
   :width: 600

   Input P1dB vs. Frequency over Gain, Receive Channel

Input IP3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/stingray_rx_iip3_gain.png
   :width: 600

   Input IP3 vs. Frequency over Gain, Receive Channel

Transmit Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gain, Return Loss
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/stingray_tx_spars_maxgain.png
   :width: 600

   Gain and Return Loss vs. Frequency, at Maximum Gain, Transmit Channel

Noise Figure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/stingray_tx_nf_over_gain.png
   :width: 600

   Noise Figure vs. Frequency over Gain, Transmit Channel

Output IP3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/stingray_tx_oip3_maxgain.png
   :width: 600

   Output IP3 vs. Frequency, Transmit Channel

Output P1dB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/stingray_tx_p1db_maxgain.png
   :width: 600

   Output P1dB vs. Frequency, Transmit Channel

Output Power vs Input Power
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/stingray_tx_poutvspin_maxgain.png
   :width: 600

   Output Power vs Input Power, Transmit Channel at 10 GHz

Switching Speed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This measurement was conducted using a single cell (1x ADAR1000, 4x ADTR1107) on
the ADAR1000EVAL1Z board. All tests were conducted at 10 GHz RF Frequency. The
Tx output was combined using a 4:1 combiner and fed into a :adi:`adl6010`
envelope detector. The detector Vout was connected to the high impedance input
of an oscilloscope. The oscilloscope trigger signal was the TR pin of the
ADAR1000.

Pulse characteristics are a 1 kHz pulse repetition frequency with a 50 us pulse
width (5% duty cycle).

.. figure:: images/stingray_pulsemeasurement_1khz_pri_50us_pw_4channels_rxtx_m25dbm_input.png
   :width: 600

   Rx-Tx Switching Time, 4 Coherently Combined Channels, 10 GHz RF, -25 dBm Input Power

.. figure:: images/stingray_pulsemeasurement_1khz_pri_50us_pw_4channels_txrx_m25dbm_input.png
   :width: 600

   Tx-Rx Switching Time, 4 Coherently Combined Channels, 10 GHz RF, -25 dBm Input Power

.. figure:: images/stingray_pulsemeasurement_1khz_pri_50us_pw_4channels_rxtx_m7dbm_input_200nsdiv.png
   :width: 600

   Rx-Tx Switching Time, 4 Coherently Combined Channels, 10 GHz RF, -7 dBm Input Power

.. figure:: images/stingray_pulsemeasurement_1khz_pri_50us_pw_4channels_txrx_m7dbm_input_200nsdiv.png
   :width: 600

   Tx-Rx Switching Time, 4 Coherently Combined Channels, 10 GHz RF, -7 dBm Input Power

Evaluation
-------------------------------------------------------------------------------

Hardware Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mechanical Parts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  1x ADAR1000-EVAL1Z board with heatsink already attached
-  2x Uprights with 16 screws attached (6 per leg for the ADAR1000-EVAL1Z board,
   1 per leg for the feet)
-  2x Feet with angles installed

.. _stingray mechanical assembly:

Mechanical Assembly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Using a **3/32 inch allen key**, connect the feet to the uprights using the
   **2 silver screws** already installed at the bottom of the upright. The
   screws should be snug, but don't need to be cranked down.
-  Using a **5/64 inch allen key**, connect the ADAR1000-EVAL1Z board to the
   uprights, one at a time using the **12 black screws** already installed in
   the uprights. The uprights are attached via the **front (component side)** of
   the ADAR1000-EVAL1Z board. The screws should be snug, but don't need to be
   cranked down.
-  The platform should now be fully assembled. Compare the result to the
   :download:`Assembly Drawing <files/stingray_assembly_v2.pdf>` to ensure
   proper assembly.

Test Setup Assembly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Follow the :ref:`Mechanical Assembly <stingray mechanical assembly>` instructions.
-  Plug the included power supply into an outlet before connecting the power
   supply to P1 in the lower left-hand side of the board. Once finished, a red
   LED (D3) should be lit in the bottom-left corner of the board.
-  Connect your digital controller of choice to the appropriate connector (P3/P4
   for PMOD control, P5 for :adi:`SDP-S` control).
-  Disable any test equipment of interest, and connect it to the ADAR1000-EVAL1Z
   board.

Board Power Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADAR1000-EVAL1Z board's power tree is controlled using two signals,
**PWR_UP_DOWN** and **+5V_CTRL**. Due to the default settings of the
:adi:`adar1000` on powerup, the :adi:`adtr1107` PAs need to be protected so as
not to be destroyed when power is applied. The easiest way to control this is to
power everything on the board except for the :adi:`ADTR1107s' <adtr1107>` +5V
rail, initialize the :adi:`ADAR1000s <adar1000>` to put the :adi:`adtr1107` PAs
into a safe state, and then power up the +5V rail.

Both **PWR_UP_DOWN** and **+5V_CTRL** are controlled with pulses, not logic
levels, as they are inputs to flip-flops rather than enable signals directly.

.. _stingray powerup:

Powerup Procedure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Apply +12V to either P1 or P2. Note the red LED (D3) on the bottom of the
   board. When lit, 12V is applied and the hot swap circuit is active. At this
   point, no RF rails are powered, but some miscellaneous rails are up:

   -  +3.3V_INT (U8, :adi:`lt8606`)
   -  +1.8V_INT (U9, :adi:`adp150`)
   -  -6.0V_INT (U10, :adi:`ADP5074`)

#. Configure the LTC2992 by following the
   :ref:`CONFIGURING THE LTC2992 <stingray ltc2992 config>` section below.

#. Pulse the **PWR_UP_DOWN** signal to sequence the first RF power rails. Once
   the power sequencer is finished, the ADAR1000s are fully powered up and the
   ADTR1107s are partially powered. This is indicated with an orange LED (D6).

   -  +3.3V (U11, :adi:`lt8642s`)
   -  -3.3V (U13, :adi:`lt3093`)
   -  -5.0V (U14, :adi:`lt3094`)

   .. note::

      The :adi:`adm1186` power sequencer's **enable** and **power_good** signals
      can be read using the on-board :adi:`ltc2992`. The **enable** signal is
      connected to GPIO1 and the **power_good** signal is connected to GPIO3.

   .. important::

      **BE SURE TO CONFIGURE THE LTC2992 SUCH THAT ALL GPIO PINS ARE HI-Z! SEE**
      :ref:`CONFIGURING THE LTC2992 <stingray ltc2992 config>`

#. Initialize the ADAR1000s to put the ADAR1000-EVAL1Z into a known safe state
   with the ADTR1107 PAs pinched off. See the :ref:`Recommended ADAR1000
   Initialization Sequences <stingray initialization>` section for
   a recommended set of SPI writes.

#.  Now that the ADTR1107 PAs are pinched off, +5V can safely be applied. This
    is accomplished by pulsing the **+5V_CTRL** signal. Once the +5V rail is up,
    a green LED (D4) is lit showing that the board is fully powered up.

   -  +5.0V (U12, :adi:`lt8652S`)

   .. note::

      The internal **+5V_CTRL** (after U3) and the :adi:`LT8652's <lt8652>`
      **power_good** signals can be read using the on-board :adi:`ltc2992`. The
      **+5V_CTRL** signal is connected to GPIO2 and the **power_good** signal is
      connected to GPIO4.

   .. important::

      **BE SURE TO CONFIGURE THE LTC2992 SUCH THAT ALL GPIO
      PINS ARE HI-Z! SEE** :ref:`CONFIGURING THE LTC2992 <stingray ltc2992 config>`


Powerdown Procedure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#.  Pulse the **+5V_CTRL** signal to bring down the +5V power supply rail. The
    green LED will turn off indicating that the rail is down.
#.  Pulse the **PWR_UP_DOWN** signal to tell the power sequencer to bring down
    the other RF rails in reverse order from powerup.

   .. note::

      It is possible to only pulse **PWR_UP_DOWN** to turn off the board as
      disabling the power sequencer will also bring down the +5V rail. This is
      not recommended as it's safer to intentionally bring down +5V first, and
      will guarantee that any software controlling the board will not lose the
      current state.


Software Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Follow the :ref:`Powerup Procedure <stingray powerup>` to safely turn the
   board on.
-  At this point, the board is fully enabled, but all amplifiers are powered
   down. In order to pass signals, the board needs to be put into either Rx or
   Tx mode and the :adi:`adtr1107` amplifiers properly biased up. See the
   :adi:`ADAR1000 Datasheet <media/en/technical-documentation/data-sheets/ADAR1000.pdf>`
   for information on how to do this.

RF Detector and ADC Combination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is an on-board RF detector/ADC combo which can be used to help calibrate
the ADAR1000-EVAL1Z or measure test signals. The circuit is located on the
antenna side of the board near the bottom.

The RF detector is the :adi:`hmc948` which feeds an :adi:`ada4807-1` unity gain
buffer. The :adi:`ada4807-1` output then goes to the :adi:`LTC2314-14`. See the
:adi:`LTC2314-14 Datasheet <media/en/technical-documentation/data-sheets/231414fa.pdf>`
for information on retrieving data from the ADC.

The :adi:`hmc948` has approximately 54dB of dynamic range at 10GHz centered at
-24dBm.

.. _stingray initialization:

Recommended ADAR1000 Initialization Sequences
-------------------------------------------------------------------------------

.. note::

   The below sequences don't take into account the different hardware addresses
   of the various ADAR1000s. Consult the
   :adi:`ADAR1000 Datasheet <media/en/technical-documentation/data-sheets/ADAR1000.pdf>`
   for more information on the hardware addressing.


.. note::

   The below sequences don't take into account the issues described in the
   Errata Documentation on the :adi:`ADAR1000 Product page <adar1000>`.
   Consult these documents for more information about how to properly
   communicate with all parts on the board.


.. note::

   The below sequences don't account for the fact that the Stingray uses two CSB
   lines to address all of the ADAR1000s on the board. In order to configure all
   chips, the sequences must be run on each required CSB line individually.


Initial Powerup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :caption: adar1000_init.py

   """
   This sequence is suggested to be run after powering the +3.3V, -3.3V, and -5.0V rails on the Stingray board,
   but before powering the +5.0V rail. This will help protect the ADTR1107 PAs. It will put the chips into a
   known safe state on powerup.
       **Format: (Register, Data, Description)**

   INIT_SEQUENCE = [
       # HOUSEKEEPING
       (0x000, 0x81, 'Reset'),
       (0x401, 0x02, 'Allow LDO adjustments from user settings'),
       (0x400, 0x55, 'Adjust LDO Settings'),
       (0x038, 0x60, 'Bypass the beam and bias RAM (enable SPI)'),
       (0x02E, 0x7F, 'Enable all Rx channels, LNA, VGA, Vector Mod'),
       (0x02F, 0x7F, 'Enable all Tx channels, PA, VGA, Vector Mod'),
       (0x034, 0x08, 'Set LNA preamplifier to nominal bias'),
       (0x035, 0x55, 'Set Rx VGA and Vector Mod to nominal bias'),
       (0x036, 0x2D, 'Set Tx VGA and Vector Mod to nominal bias'),
       (0x037, 0x06, 'Set Tx PA preamplifier to nominal bias'),

       # PA BIAS VALUES
       (0x029, 0x85, 'Set PA1_BIAS_ON value (≈ -2.5V)'),
       (0x02A, 0x85, 'Set PA2_BIAS_ON value (≈ -2.5V)'),
       (0x02B, 0x85, 'Set PA3_BIAS_ON value (≈ -2.5V)'),
       (0x02C, 0x85, 'Set PA4_BIAS_ON value (≈ -2.5V)'),
       (0x046, 0x85, 'Set PA1_BIAS_OFF value (≈ -2.5V)'),
       (0x047, 0x85, 'Set PA2_BIAS_OFF value (≈ -2.5V)'),
       (0x048, 0x85, 'Set PA3_BIAS_OFF value (≈ -2.5V)'),
       (0x049, 0x85, 'Set PA4_BIAS_OFF value (≈ -2.5V)'),

       # LNA BIAS VALUES
       (0x02D, 0x68, 'Set LNA_BIAS_ON value (≈ -2.0V)'),
       (0x04A, 0x68, 'Set LNA_BIAS_OFF value (≈ -2.0V)'),

       # TR CONTROL STATE
       (0x031, 0x90, 'Disable Tx/Rx using SPI TR control'),

       # Enable PA/LNA DACs
       (0x030, 0x50, 'Enable the PA and LNA output DACs'),
   ]

Max Gain & 0° Phase
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :caption: adar1000_max_gain_0_phase.py

   """
   Sequence to set all ADAR1000 channels to maximum gain and 0° phase.
       **Format: (Register, Data, Description)**

   CHANNEL_SETUP = [
       # Rx GAIN
       (0x010, 0xFF, 'Set channel 1 Rx to maximum gain'),
       (0x011, 0xFF, 'Set channel 2 Rx to maximum gain'),
       (0x012, 0xFF, 'Set channel 3 Rx to maximum gain'),
       (0x013, 0xFF, 'Set channel 4 Rx to maximum gain'),

       # Rx PHASE
       (0x014, 0x3F, 'Set channel 1 Rx I Vector Modulator to 0°'),
       (0x015, 0x20, 'Set channel 1 Rx Q Vector Modulator to 0°'),
       (0x016, 0x3F, 'Set channel 2 Rx I Vector Modulator to 0°'),
       (0x017, 0x20, 'Set channel 2 Rx Q Vector Modulator to 0°'),
       (0x018, 0x3F, 'Set channel 3 Rx I Vector Modulator to 0°'),
       (0x019, 0x20, 'Set channel 3 Rx Q Vector Modulator to 0°'),
       (0x01A, 0x3F, 'Set channel 4 Rx I Vector Modulator to 0°'),
       (0x01B, 0x20, 'Set channel 4 Rx Q Vector Modulator to 0°'),

       # Tx GAIN
       (0x01C, 0xFF, 'Set channel 1 Tx to maximum gain'),
       (0x01D, 0xFF, 'Set channel 2 Tx to maximum gain'),
       (0x01E, 0xFF, 'Set channel 3 Tx to maximum gain'),
       (0x01F, 0xFF, 'Set channel 4 Tx to maximum gain'),

       # Tx PHASE
       (0x020, 0x3F, 'Set channel 1 Tx I Vector Modulator to 0°'),
       (0x021, 0x20, 'Set channel 1 Tx Q Vector Modulator to 0°'),
       (0x022, 0x3F, 'Set channel 2 Tx I Vector Modulator to 0°'),
       (0x023, 0x20, 'Set channel 2 Tx Q Vector Modulator to 0°'),
       (0x024, 0x3F, 'Set channel 3 Tx I Vector Modulator to 0°'),
       (0x025, 0x20, 'Set channel 3 Tx Q Vector Modulator to 0°'),
       (0x026, 0x3F, 'Set channel 4 Tx I Vector Modulator to 0°'),
       (0x027, 0x20, 'Set channel 4 Tx Q Vector Modulator to 0°')
   ]

Disable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :caption: adar1000_disable.py

   """
   This sequence will disable the ADAR1000 and put the chip into a low power state.
       **Format: (Register, Data, Description)**

   DISABLE = [
       (0x029, 0x85, 'Set CH1 PA_BIAS_ON to minimal power (≈ -2.5V)'),
       (0x02A, 0x85, 'Set CH2 PA_BIAS_ON to minimal power (≈ -2.5V)'),
       (0x02B, 0x85, 'Set CH3 PA_BIAS_ON to minimal power (≈ -2.5V)'),
       (0x02C, 0x85, 'Set CH4 PA_BIAS_ON to minimal power (≈ -2.5V)'),
       (0x02D, 0x68, 'Set LNA_BIAS_ON to minimal power (≈ -2.0V)'),
       (0x030, 0x50, 'Enable the LNA bias DAC output'),
       (0x031, 0x90, 'Put ADAR1000 into SPI-controlled TR state and disable TX_EN/RX_EN bits')
   ]

Rx Enable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :caption: adar1000_rx_enable.py

   """
   This sequence will configure the ADAR1000 for Rx and set the LNAs to full power.
   Be sure you know what you're doing!
       **Format: (Register, Data, Description)**

   RX_SETUP = [
       (0x030, 0x40, 'Disable the LNA bias DAC output to allow the ADTR1107 LNAs to self-bias'),
       (0x031, 0xB0, 'Put ADAR1000 into SPI-controlled Rx mode')
   ]

Tx Enable (Reduced Power)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :caption: adar1000_tx_enable_reduced.py

   """
   This sequence will configure the ADAR1000 for Tx and set the PAs to a reduced power state.
   Be sure you know what you're doing!
       **Format: (Register, Data, Description)**

   TX_SETUP_REDUCED_POWER = [
       (0x029, 0x42, 'Set CH1 PA_BIAS_ON to reduced power (≈ -1.25V)'),
       (0x02A, 0x42, 'Set CH2 PA_BIAS_ON to reduced power (≈ -1.25V)'),
       (0x02B, 0x42, 'Set CH3 PA_BIAS_ON to reduced power (≈ -1.25V)'),
       (0x02C, 0x42, 'Set CH4 PA_BIAS_ON to reduced power (≈ -1.25V)'),
       (0x031, 0xD2, 'Put ADAR1000 into SPI-controlled Tx mode')
   ]

Tx Enable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :caption: adar1000_tx_enable.py

   """
   This sequence will configure the ADAR1000 for Tx and set the PAs to full power.
   Be sure you know what you're doing!
       **Format: (Register, Data, Description)**

   TX_SETUP = [
       (0x029, 0x38, 'Set CH1 PA_BIAS_ON to full power (≈ -1.06V)'),
       (0x02A, 0x38, 'Set CH2 PA_BIAS_ON to full power (≈ -1.06V)'),
       (0x02B, 0x38, 'Set CH3 PA_BIAS_ON to full power (≈ -1.06V)'),
       (0x02C, 0x38, 'Set CH4 PA_BIAS_ON to full power (≈ -1.06V)'),
       (0x031, 0xD2, 'Put ADAR1000 into SPI-controlled Tx mode')
   ]

.. _stingray ltc2992 config:

Configuring the LTC2992
-------------------------------------------------------------------------------

| On powerup, the LTC2992 is configured with GPIO3 held low. To properly power
  the Stingray board, this pin needs to be set to Hi-Z. Complete the below I2C
  writes to ensure that all GPIO pins are set to Hi-Z:

.. note::

   The LTC2992's I2C 7-bit address is 0x6A, its 8-bit address is 0xD4. Looking
   at the schematic for the board, it would seem that the address pins
   are pulled down (resulting in the address being 0x6F according to Table 3
   of the :adi:`LTC2992 datasheet <media/en/technical-documentation/data-sheets/ltc2992.pdf>`),
   but the 100kΩ resistors are too weak to overcome the internal circuitry of
   the LTC2992, so the actual address is 0x6A.


.. note::

   The LTC2992 requires repeated START conditions for readback.


.. code-block:: python
   :caption: ltc2992_configuration.py

   """
   This sequence will set the LTC2992's GPIO pins to Hi-Z.
       **Format: (Register, Data, Description)**

   LTC2992_SETUP = [
       (0x96, 0x00, 'Set GPIO1-GPIO3 pins to Hi-Z'),
       (0x97, 0x00, 'Set GPIO4 pin to Hi-Z')
   ]

Stingray Board Cell & Channel Maps
-------------------------------------------------------------------------------

Cell Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/cell_mapping.png
   :width: 600

   ADAR1000-EVAL1Z Cell Mapping

Channel Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/channel_mapping.png
   :width: 600

   ADAR1000-EVAL1Z Channel Mapping

Channel Map (Back of Board)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/channel_mapping_reverse.png
   :width: 600

   ADAR1000-EVAL1Z Channel Mapping (Back of Board)
