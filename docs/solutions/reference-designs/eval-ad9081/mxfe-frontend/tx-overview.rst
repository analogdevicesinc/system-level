.. imported from: https://wiki.analog.com/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx-overview

.. _ad9081 mxfe-frontend tx-overview:

Transmitter front end overview & theory of operation
===============================================================================

The 2-24 GHz transmitter block diagram is shown below. The following sections
go into more detail on the theory of operation of the individual, functional
blocks of the signal chain.

.. figure:: ../images/ad9081_2to24_txblockdiagram.png
   :align: center
   :width: 990

   Transmitter block diagram

.. _ad9081 mxfe-frontend tx-overview if-input-stage:

IF input stage
-------------------------------------------------------------------------------

The DAC output first feeds into the IF input section (block diagram below) of
the front end with 4.8 GHz low-pass filtering to reject the DAC image spurious.
The IF input frequency is 4-5 GHz and within the 1st Nyquist of the DAC
sampling at 12 GSPS. After the image LPF comes an :adi:`ADRF5730` digital step
attenuator for fine resolution level control, an LNA, and an additional LPF for
additional suppression of DAC output spurious.

.. figure:: ../images/ad9081_2to24_tx_if_input_section.png
   :align: center
   :width: 600

   Tx IF input section

.. _ad9081 mxfe-frontend tx-overview frequency-conversion:

Frequency conversion stage & frequency plan
-------------------------------------------------------------------------------

The transmit signal chain uses two separate frequency conversion paths to
enable continuous, 2-24 GHz frequency coverage. The two signal paths are
selectable via :adi:`ADRF5020` RF switches. For the 6.5-24 GHz RF output
frequency band, the 4-5 GHz IF input is fed into an :adi:`HMC8191` wideband I/Q
mixer with a tunable LO source, upconverting the entire band to the desired RF
output frequency.

For the 2-7 GHz RF output band, a dual-frequency conversion heterodyne signal
path is used with the IF input first being upconverted to a high, 11-16 GHz IF
through the :adi:`HMC8191` with tunable LO, and then downconverted to the
2-7 GHz RF output through an :adi:`HMC773A` mixer with a fixed 18 GHz LO.
Cascaded low and high-pass filters provide 11-16 GHz IF filtering and an
:adi:`HMC882A` tunable low pass filter mitigates mixer output spurious for the
final 2-7 GHz RF output band. The figure below shows the frequency conversion
section of the signal chain and the frequency operation ranges for each
individual path.

.. figure:: ../images/ad9081_2to24_txfreqconversionsection.png
   :align: center
   :width: 600

   Tx frequency conversion section

The figure below provides an additional frequency plan visualization showing
the individual frequency conversion steps for each frequency band.

.. figure:: ../images/ad9081_2to24_txfreqplan.png
   :align: center
   :width: 500

   Tx frequency plan

The following table summarizes the possible frequency conversion paths:

.. figure:: ../images/ad9081_2to24_tx_frequency_plan.png
   :align: center
   :width: 900

   Tx frequency conversion paths

.. _ad9081 mxfe-frontend tx-overview rf-output-stage:

RF output stage
-------------------------------------------------------------------------------

The RF output stage, shown in the figure below, is comprised of a wideband
:adi:`ADL9006` driver amp, an :adi:`ADMV8818` tunable bandpass filter, and
finally an :adi:`HMC994APM5E` PA. The :adi:`ADMV8818` tunable filter operates
across a 2-18 GHz frequency range for additional filtering of output spurious,
and can be bypassed for operation up to 24 GHz.

.. figure:: ../images/ad9081_2to24_tx_rf_output_section.png
   :align: center
   :width: 600

   Tx RF output section

.. _ad9081 mxfe-frontend tx-overview timing-control:

Timing & control
-------------------------------------------------------------------------------

.. figure:: ../images/ad9081_2to24_tx_switch_and_atten_ctrl.png
   :align: center
   :width: 800

   Tx switch and attenuator control

.. _ad9081 mxfe-frontend tx-overview simulations:

Transmitter performance simulations
-------------------------------------------------------------------------------

Keysight SystemVue/Genesys was used for detailed signal chain modelling and
cascade analysis. Every component in the signal chain was modelled with
frequency-dependent sys-parameter or s-parameter datasets to ensure accurate
simulation results. The Genesys signal chain model shown below takes into
account the following components:

- Manufacturer-provided, frequency-dependent s-parameter or sys-parameter
  datasets for every active and passive RF component
- A standalone model of the :adi:`ADMV8818` tunable bandpass filter configured
  to tune a 1 GHz wide passband to the RF center frequency during frequency
  sweeps. The :adi:`ADMV8818` internal bypass path is engaged above 18 GHz.
- A standalone model of the :adi:`HMC882A` tunable lowpass filter configured
  to tune its 3 dB corner frequency to minimize LO feedthrough and spurious
- Frequency-dependent component interconnect modelling i.e. PCB trace loss
  approximation for DC-50 GHz CPWG traces, 8 mil Rogers 4003 PCB stackup

.. figure:: ../images/ad9081_2to24_tx_genesys_simulation.png
   :align: center
   :width: 900

   Tx Genesys signal chain model

The complete Keysight Genesys/SystemVue simulation workspaces for the Rx and
Tx signal chains are available on request, see
:ref:`ad9081 mxfe-frontend request-files`.

The Genesys workspace already has numerous system analysis and MATLAB-based
frequency sweeps in place, including the following functionality:

- 2-24 GHz CW input sweep with MATLAB equation-based frequency plan automated
  to ensure correct signal chain configuration for any given RF output
  frequency. All LO frequencies, frequency-dependent RF paths, and tunable
  filter passbands automatically tune during sweep.
- Gain levelling implemented using the IF DSAs to normalize cascaded gain to
  the lowest-gain frequency point for optimal flatness (+/- 2 dB).

Transmitter performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gain, OIP3, and OP1dB, 2-24 GHz, rough gain levelling implemented.

As described above, the following plot assumes PCB implementation with low
loss traces. This plot shows the Gain, OIP3, and OP1dB performance of the
transmitter across frequency:

.. figure:: ../images/ad9081_2to24_tx_rf_performance.png
   :align: center
   :width: 950

   Transmitter performance

Transmitter output spectrum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transmitter output spectrum, +12 dBm out at 12.5 GHz.

The following plot shows the spectral output power components of the
transmitter at +12 dBm input power and 12.5 GHz frequency:

.. figure:: ../images/ad9081_2to24_tx_output_spectrum_12ghz.png
   :align: center
   :width: 950

   Transmitter output spectrum, +12 dBm at 12.5 GHz
