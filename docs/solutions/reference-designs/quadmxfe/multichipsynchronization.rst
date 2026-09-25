.. _quadmxfe multichipsynchronization:

Multi-Chip Synchronization with the Quad-MxFE + Calibration Board
=================================================================

The Quad-MxFE Platform, in conjunction with the
:ref:`16 Tx / 16 Rx Calibration Board <quadmxfe calboard>`, has demonstrated
multi-chip synchronization (MCS) of the four :adi:`AD9081`\ s on the system. MCS
provides the user with a known, **deterministic phase** after each power cycle
for a given operating frequency. The platform provides MATLAB scripts which can
be tweaked for a particular customer application to showcase MCS on their own
system.

.. image:: images/calibrationboardconnected.jpg
   :width: 800

It is helpful to define a few terms prior to a MCS discussion.

-  **Phase Alignment**: The input RF phases to each ADC channel are identical
   and the output RF phases from each DAC channel are identical such that full
   dynamic range and phase noise system-level benefits can be realized
-  **Phase Determinism**:The phase relationship with respect to Rx0 of each
   channel is known, but not necessarily identical, after full power cycle. This
   allows for factory calibration look-up tables (LUTs) to be populated for
   setting boot-up NCO phase offsets for all channels
-  **Phase Coherency**:The phase relationship of each channel is maintained with
   respect to Rx0 after changing NCO frequency from a calibrated frequency X,
   then changed to frequency Y, and then changed back to frequency X. This
   allows for factory calibration to be maintained over multiple frequencies
-  **Multi-Chip Synchronization (for AD9081/AD9082)**: A process which
   simplifies a required system level calibration algorithm, and which uses both
   NCO Master-Slave Sync and One-Shot Sync to provide Tx and Rx phase
   determinism when using multiple MxFEs in a system

The :adi:`AD9081` contains digital signal processing (DSP) blocks on-silicon to
allow for channel-to-channel digital phase and/or amplitude calibration
techniques to be implemented as part, or the entirety, of the system level
calibration. Some of these phase adjustment knobs occur at the
numerically-controlled oscillators (NCOs) residing in the 4x Coarse (Main)
Digital Up/Down Converters (DUC/DDCs) and 8x Fine (Channelizer) DUC/DDCs.
Additionally, on the Rx side, on-silicon programmable finite impulse response
(pFIR) blocks allow for equalization of both phase and amplitude for all Rx
channels in the system. Each of these DSP blocks must be synchronized when
dealing with multiple MxFE® chips in a system.

.. image:: images/quadmxfe_mxfephaseadjustknobs.png
   :width: 800

Multi-chip synchronization using the AD9081/AD9082 is achieved with the help of
two distinct features within the chipset:

-  **One-Shot Sync**: Helps to align baseband data and some internal clocks
-  **NCO Master-Slave Sync**: Helps to align the multiple NCOs spanning across
   all the chips on the platform

There are multiple signals on the platform which are used to achieve MCS. SYSREF
signals are used to help achieve One-Shot Sync. GPIO signals are used to
implement NCO Master-Slave Sync. Additionally, to achieve MCS while the system
undergoes a change in thermal gradients requires use of the PLL phases sent into
the device clock pins of each MxFE®.

.. image:: images/quadmxfe_mcs_board.png
   :width: 800

.. image:: images/quadmxfe_mcsgoals.png
   :width: 1200

One-Shot Sync
=============

The one-shot sync feature first requires that the user defines the JESD link
parameters (such as M, N’, L, etc.) and then configures the synchronization
logic for any desired SYSREF averaging (if using continuous SYSREF pulses).
Additionally, desired LEMC delays can be used to force the LEMC to be generated
at a certain delay after the SYSREF edge. After this is completed, the user then
enables the one-shot sync bit within each digitizer IC and then requests that
SYSREF pulses be sent to each IC within the same clock cycle, as shown in the
figure above. For the Quad-MxFE Platform, analog fine delays have been
introduced within the :adi:`HMC7043` clock buffer IC to allow synchronous
SYSREFs to all digitizer ICs. A subsequent check can be executed to verify the
one-shot sync process performed successfully by querying registers within each
IC which provide information about the phase relationship between the SYSREF
signal and the LEMC boundary of each IC’s link. Once a stable phase is measured
(ie. once the SYSREF-LEMC phase register reads ‘0’), the user then knows that
the LEMCs of all the digitizer ICs are aligned and the user can then proceed to
the NCO master-slave sync process. The subtasks described for the one-shot sync
are contained within an application programming interface (API) provided for the
:adi:`AD9081`.

NCO Master-Slave Sync
=====================

The NCO master-slave sync feature first assigns one of the :adi:`AD9081` within
the subarray to act as a ‘master’ chip, as shown in the above figure. All other
digitizers are then deemed ‘slave’ ICs. The master IC is setup such that the
GPIO0 pin of this device is configured as an output and routed to the GPIO0 nets
of the three slave digitizer ICs. The slave GPIO0 nets are configured as inputs.
The user can then choose to trigger on either the SYSREF pulse, the LEMC rising
edge, or the LEMC falling edge. The LEMC rising edge is used as the NCO
master-slave sync trigger source as default for the base control code provided
with the platform, and the GPIO nets are routed through the HDL instead of
locally on the subarray. Next, the DDC synchronization bits are toggled low and
then high to arm the ADC-side NCO synchronization algorithm. Likewise, the
microprocessor align bit is toggled low and then high to arm the DAC-side NCO
synchronization algorithm. When this trigger is requested, at the next LEMC
rising edge the master digitizer IC asserts high a ‘master out’ signal through
its GPIO0 net. This signal propagates to the GPIO0 inputs of each of the slave
devices. At the next LEMC edge, all digitizer ICs experience a NCO reset
algorithm. After this any LEMC pulses are ignored with regards to the NCO
master-slave sync algorithm. As with the one-shot sync, these NCO master-slave
sync subtasks are contained within API functions for user ease-of-use.

PLL Synthesizer Phase Adjustments
=================================

The :adi:`ADF4371` PLL synthesizers allow for relative sample clock phase
adjustments injected into each digitizer IC. Thermal drift, and the resulting
PLL phase drift between the sample clock and the SYSREF of each IC, is
compensated by creating a feedback mechanism which ensures that the first
transmit channel of each :adi:`AD9081` is phase-aligned to the first
:adi:`AD9081` IC’s first transmit channel, as shown in the figure below. To
achieve this feedback loop, the first transmit channel of each MxFE® outputs a
signal which differentiates itself from the other transmit channels. These four
signals are combined and sent into a common receiver, which for this system is
labeled Rx0.

.. image:: images/quadmxfe_pllphaseadjustwithcalibrationboard.png
   :width: 800

A receiver data capture is obtained which then allows the user to apply
cross-correlation techniques to determine the complex phase offsets between
these four transmit channels, :math:`\phi_{TxOffset}`. The :adi:`ADF4371` PLL
synthesizer ICs contain within them a voltage-controlled oscillator (VCO) which
are operating at a frequency :math:`f_{VCO\_PLL}`. The measured phase offsets
:math:`\phi_{TxOffset}` are then related to the required PLL phase adjustment
:math:`\phi_{PLL\_Adj}` and the RF frequency :math:`f_{carrier}` such that:

:math:`\phi_{PLLAdj}=[f_{VCOPLL}/f_{carrier}]\phi_{TxOffset}`

Using this formula, the :adi:`ADF4371` PLL synthesizer phases can be adjusted by
a new known amount to establish a common Tx baseline between all digitizer ICs
for all power cycles, as shown in the figure below. The open circles for each
channel shown in the figure correspond to the first power cycle, whereas all the
other solid dots correspond to subsequent power cycles. As can be seen from this
figure, the calibrated Tx phase offsets for the first (and second) channelizers
of all :adi:`AD9081`\ s are phase aligned. The second channelizer of each
digitizer IC is aligned in this instance as well because two channelizers are
used for each DAC in the system.

.. image:: images/quadmxfe_txalignment.png
   :width: 800

Publications
============

:adi:`Power-Up Phase Determinism Using Multichip Synchronization Features in
Integrated Wideband DACs and ADCs
<en/technical-articles/power-up-phase-determinism-using-multichip-synchronization.html>`
