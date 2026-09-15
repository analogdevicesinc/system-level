.. imported from: https://wiki.analog.com/resources/eval/user-guides/adrv9029/dpd_model_optimization

.. _adrv9029 dpd_model_optimization:

ADRV9029 DPD Model
==================

DPD Model is a fundamental building block of ADRV9029 DPD that defines the GMP
polynomial(memory terms and polynomial degree) for modeling a Power Amplifier in
the baseband. Good modeling of the PA is critical for achieving good DPD
performance. An example DPD Model descriptor is shown below

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpdmodel.png

DPD Model Generation
--------------------

ADI provides a library of 140 pre-defined DPD models that are optimized for good
performance on ADRV9029 with various types of Power Amplifiers that can be
downloaded at this
:download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/dpdmodels.zip`

For 190 coefficient model files,
:download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpdmodels_190coeffs.zip`

In order to identify a DPD model for that is optimum for a Power Amplifier, the
following procedure is recommended

#. Setup the ADRV9029 Transceiver Evaluation platform as shown in the
   :dokuwiki:`Pre-Requisites page </resources/eval/user-guides/adrv9029/prerequisites>`
#. Ensure that you are able to bringup DPD on the ADRV9029 evaluation platform
   by following the instructions on
   :dokuwiki:`ADRV9029 DPD Evaluation through TES GUI page </resources/eval/user-guides/adrv9029/evaluating_dpd_through_tes_gui>`
#. After verifying that DPD bringup is successful on the ADRV9029 platform,
   browse to the location **C:\\Program Files\\Analog Devices\\ADRV902x
   Transceiver Evaluation Software_x64_FULL\\Resources\\DpdModels**/ on your PC
   and ensure that DPD model library is available. In case the DPD model library
   is not installed in the above mentioned location, the user can download the
   DPD model library at this
   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/dpdmodels.zip`
   and manually install the DPD library at the location **C:\\Program
   Files\\Analog Devices\\ADRV902x Transceiver Evaluation
   Software_x64_FULL\\Resources\\DpdModels** on your PC.
#. At this stage the user can download the DPD model sweep script provided by
   ADI at
   :download:`https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_dpdmodelsweep_sw6p0.zip`.
   The model sweep script automates the process of picking the most suitable
   model for the PA by iterating through the DPD model library and picking the DPD
   model that produces the least amount of error between pre-DPD actuator Tx and
   post PA observed ORx data.
#. Load the script downloaded in Step 4 into the Iron Python tab of the ADRV9029
   TES GUI by clicking on **File->Load** in the Iron Python tab of the ADRV9029
   GUI as shown in the figure below and browsing to the location where you have
   stored the script on your PC.

   .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/adrv9029/adrv9029_loadingscript.png

#. After loading the script, execute the script by clicking **Build->Run** in
   the Iron Python tab of ADRV9029 TES GUI

#. At the end of execution of this script, the DPD model producing the least
   amount of error will be logged as **C:\\Program Files\\Analog
   Devices\\ADRV9025 Transceiver Evaluation
   Software_x64_FULL\\Resources\\DpdModels\\DpdModelOptimized.txt.**

.. note::

   The DPD model sweep script is configured to run on transmitter Tx1 by
   default. Please ensure that the PA gain line up is connected to Tx1 in the
   ADRV9029 Evaluation System

Once the DpdModelOptimized.txt is obtained from the script, user can continue
DPD evaluation by loading this DPD model as described in
:dokuwiki:`ADRV9029 DPD Evaluation through TES GUI </resources/eval/user-guides/adrv9029/evaluating_dpd_through_tes_gui>`
