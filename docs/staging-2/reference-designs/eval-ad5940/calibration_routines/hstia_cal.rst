.. imported from: https://wiki.analog.com/resources/eval/user-guides/eval-ad5940/calibration_routines/hstia_cal

.. _eval-ad5940 calibration_routines hstia_cal:

High Speed TIA Calibration
==========================

Overview
--------

The high speed TIA gain resistor is configurable from 50, 100, 200, 1k, 5k, 10k,
20k, 40k, 80k and 160kΩ. To calibrate the Rtia a precision RCAL resistor needs
to be connected to RCAL0 and RCAL1 pins. Ideally the RCAL should be close in
value to the Rtia to be calibrated and should have a tolerance <= 0.1%. The
calibration process implements an impedance measurement where the magnitude of
the impedance is the value of Rtia. A sine wave is applied through RCAL and the
Rtia. The voltage drop across each is measured with a DFT calculated on each.
Using ratiometric analysis the actual impedance of the Rtia is calculated by the
following equation: \|Rtia \| = \|Vrcal|/\|Vrtia\|.

It is important to calibrate at the correct frequency. For example, if the
measurement of the sensor requires an excitation signal of 50 kHz, the
calibration routine should be carried out at this frequency. This insures CTIA
is factored into the calculation. If carrying out a frequency sweep, it is
recommend to do a calibration for each frequency point in the sweep.

Calibration Steps
-----------------

The following are the steps involved for calibrating the HSTIA Gain resistor:

- Configure switch matrix to connect RCAL between the Excitation buffer and the
  HSTIA as per below figure:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/calibration_routines/hstia_rtiacal.jpg
   :width: 600px

- Generate a sine wave with required frequency using the waveform generator,
  HSDAC and Excitation amplifier.
- The signal path is highlighted in above image.
- The P_Node and N_Node are connectted to the ADC mux and the DFT of the voltage
  is measured.
- Then, maintaining the same excitation voltage, the HSTIA_P and HSTIA_N nodes
  are connected to the ADC mux. A DFT of the voltage is calculated again.
- The real and imaginary parts of the DFT results are used to calculate the
  value of the Rtia with the following equations:

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad5940/calibration_routines/rtia_equation.png
   :width: 200px

- This value of Rtia is then saved by the host controller and used for
  calculating impedance"s.

Using the HSTIA Rtia Calibration Function in the SDK
----------------------------------------------------

The following function is an example on how to calibrate the HSTIA gain
resistor:

::

   static AD5940Err AppRtiaCal(void)
   {
      HSRTIACal_Type hsrtia_cal;
      hsrtia_cal.AdcClkFreq = AppBIACfg.AdcClkFreq;
      hsrtia_cal.ADCSinc2Osr = AppBIACfg.ADCSinc2Osr;
      hsrtia_cal.ADCSinc3Osr = AppBIACfg.ADCSinc3Osr;
      hsrtia_cal.bPolarResult = bTRUE; /*We need magnitude and phase here*/
      hsrtia_cal.DftCfg.DftNum = AppBIACfg.DftNum;
      hsrtia_cal.DftCfg.DftSrc = AppBIACfg.DftSrc;
      hsrtia_cal.DftCfg.HanWinEn = AppBIACfg.HanWinEn;
      hsrtia_cal.fRcal= AppBIACfg.RcalVal;
      hsrtia_cal.HsTiaCfg.DiodeClose = bFALSE;
      hsrtia_cal.HsTiaCfg.HstiaBias = HSTIABIAS_1P1;
      hsrtia_cal.HsTiaCfg.HstiaCtia = AppBIACfg.CtiaSel;
      hsrtia_cal.HsTiaCfg.HstiaDeRload = HSTIADERLOAD_OPEN;
      hsrtia_cal.HsTiaCfg.HstiaDeRtia = HSTIADERTIA_TODE;
      hsrtia_cal.HsTiaCfg.HstiaRtiaSel = AppBIACfg.HstiaRtiaSel;
      hsrtia_cal.SysClkFreq = AppBIACfg.SysClkFreq;
      if(AppBIACfg.SweepCfg.SweepEn == bTRUE)
      {
         uint32_t i;
         AppBIACfg.SweepCfg.SweepIndex = 0;  /*Reset index*/
         for(i=0;i<AppBIACfg.SweepCfg.SweepPoints;i++)
         {
            AD5940_SweepNext(&AppBIACfg.SweepCfg, &hsrtia_cal.fFreq);
            AD5940_HSRtiaCal(&hsrtia_cal, AppBIACfg.RtiaCalTable[i]);
            printf("Freq:%.2f,Mag:%.2f,Phase:%fDegree\n", hsrtia_cal.fFreq, AppBIACfg.RtiaCalTable[i][0],
            AppBIACfg.RtiaCalTable[i][1]*180/MATH_PI);
          }
          AppBIACfg.RtiaCurrValue[AppBIACfg.SweepCfg.SweepIndex] = AppBIACfg.RtiaCalTable[i][0];
          AppBIACfg.RtiaCurrValue[AppBIACfg.SweepCfg.SweepIndex] = AppBIACfg.RtiaCalTable[i][0];
          AppBIACfg.SweepCfg.SweepIndex = 0;  /*Reset index*/
      }
      else
      {
         hsrtia_cal.fFreq = AppBIACfg.SinFreq;
         AD5940_HSRtiaCal(&hsrtia_cal, AppBIACfg.RtiaCurrValue);
         printf("RtiaMag:%.2f,Phase:%fDegree\n", AppBIACfg.RtiaCurrValue[0],
         AppBIACfg.RtiaCurrValue[1]*180/MATH_PI);
      }
      return AD5940ERR_OK;
   }
