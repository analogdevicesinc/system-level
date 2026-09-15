.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9029/evaluating_dpd_through_tes_gui

.. _adrv9029 evaluating_dpd_through_tes_gui:

EVALUATING ADRV9029 DPD
=======================

CONFIGURING THE ADRV9029 TRANSCEIVER
------------------------------------

- Review the
  `ADRV902X Unboxing Video <https://www.youtube.com/watch?v=Oq_9bl5f8fM>`__ and
  ensure that the ADRV9029 evaluation platform is functional and you are able to
  interact with the ADRV9029 transceiver through the
  :adi:`ADRV9029 TES GUI <en/license/licensing-agreement/adrv9029-software-license-agreement.html>`.

- Connect various hardware components of the evaluation system as shown in the
  :dokuwiki:`Pre-Requisites page </resources/eval/user-guides/adrv9029/prerequisites>`.

- In the ``Overview`` window of the ADRV9029 TES GUI, select the profile
  ``51_nonLinkSharing`` as shown in the figure below. The profile defines the
  data rates of the transceiver.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_profileselection.png
   :width: 600px

- In the ``Tx`` window of the ADRV9029 TES GUI, you will notice that both the
  DPD Half Band filters are enabled in the Tx signal chain for the profile
  51_nonLinkSharing. Each half band provides an interpolation of 2x. The
  cascaded interpolation rate is 4x for this profile.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/uc51_txpath.png
   :width: 600px

- In the ``Initialization`` window of the ADRV9029 TES GUI, configure the LO
  frequency to match the frequency of operation of the Power Amplifier under
  test. Also ensure the ORx LO is connected to the same LO as Tx and the Tx to
  ORx mapping matches the physical Tx to ORx connection.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_initializationwindow.png
   :width: 600px

- Set the Tx and ORx attenuation to a reasonably high value in the
  ``Initialization`` window, so that the PA is not over-driven and ORx ADC does
  not saturate.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_inittxattenandorxgain.png
   :width: 600px

- :red:` Please turn off the PA before programming the device so that the PA is not damaged by high amplitude tones transmitted by the ADRV9029 during initial calibration .`

PROGRAMMING THE ADRV9029 TRANSCEIVER
------------------------------------

After configuring the ADRV9029 transceiver settings as shown in the previous
section, click the ``Program`` button in the ADRV9029 TES GUI to program the
ADRV9029 transceiver

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_program.png
   :width: 600px

On successful completion of ADRV9029 transceiver programming, the TES GUI will
display a **Programmed Successfully** message on the bottom right hand
corner of the ADRV9029 TES GUI as shown below.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_programmingsuccessful.png
   :width: 600px

EVALUATING DPD ON THE ADRV9029 TRANSCEIVER
------------------------------------------

- Load an OFDM signal such as LTE20 / NR100 in a tab-separated IQ format through
  the ``Transmitter`` tab of the ADRV9029 TES GUI. Click on the ``Tones`` button
  and check the ``Load File`` option on all 4 transmitters. Now, browse to the
  location where the file is stored through the ``File to Load`` window. Load
  the same Tx waveforms to all 4 transmitters.

  Adjust the digital scaling if required and hit the ``Submit`` button to load the
  waveform to the eval platform. Finally, click on the play button next to
  ``Tones`` to start transmitting the waveform on the ADRV9029 Transceiver.

  .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_loadingtxwaveform.png
     :width: 600px

- Turn on the PA and bring the PA to it"s rated power by adjusting the Tx Front
  End attenuation on the ADRV9029 Transceiver through the ``Tx Attenuation``
  setting under the Transmitter tab of ADRV9029 TES GUI.

  .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_txattenadjust.png
     :width: 400px

- Adjust the ORx gain under the ``Obs Rx`` tab of the ADRV9029 GUI to ensure
  that the observation channel is not saturating.

  .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_orx_setup.png
     :width: 400px

- Browse to the DFE Tab in the ADRV9029 TES GUI. Load a DPD model by clicking
  the ``Load Model from file`` button in the ``DPD Model Setup`` User Interface.
  The DPD model is a polynomial function that models the PA through memory
  terms(i,j) and polynomial degree "k". ADI provides a set of pre-calculated DPD
  models that can be accessed in the ``Resources`` folder of the ADRV9029 TES
  GUI Installation directory. After loading the DPD model, set the linear term
  coefficient corresponding to (i=1,j=1,k=0) to 1 + j0 as shown in the figure
  below. For evaluation purposes, any model can be chosen. To optimize the DPD
  model for a particular PA, follow the instructions on the DPD Model
  Optimization page.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpd_modelload.png

- Configure "DPD Tracking Config" parameters (default values provide a good
  starting point).

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpdtrackingconfig.png

- In the "DPD functions" window under the DFE Tab of ADRV9029 TES GUI, select
  desired Tx channel to apply settings(In this example Tx1 is selected).
- Apply DPD model on the M and C tables using "Apply Model on Device from M
  Table" and "Apply Model on Device from C Table" buttons. The C-Table is a low
  power model only applicable in DPD Mode 2.
- Apply DPD tracking configuration by clicking on "Apply Tracking Config"
  button.
- Run Path Delay initial calibration using "Run Path Delay Init Cal" button.
- Click "Enable DPD on selected channels (only)" to enable DPD Tracking.

  .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpdtrackingcal_enable.png

- Now the DPD tracking must be enabled and running. The DPD status can be
  monitored by selecting the Tx channel and clicking the ``Get DPD Status and
  Statistics`` button. Ensure that the error status returns ``No Error`` and the
  ``Iteration Count`` and ``Update Count`` fields are incrementing

  .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpdstatus.png
     :width: 300px
