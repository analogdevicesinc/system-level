.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon2-ebz/software/iio_scope

.. _ad-fmcmotcon2-ebz software iio_scope:

AD-FMCMOTCON2-EBZ IIO User Guide
================================

IIO OSC
-------

ADI IIO oscilloscope is used for monitoring and controlling the
AD-FMCMOTCON2-EBZ board, when using the Linux operating system. A complete user
guide for the IIO oscilloscope can be found
:dokuwiki:`here <resources/tools-software/linux-software/iio_oscilloscope>`.

Signals monitoring
~~~~~~~~~~~~~~~~~~

The IIO Oscilloscope allows to monitor current, voltage, speed and control
signals from the system. Below is presented a description of the different
monitoring channels exposed by the IIO Oscilloscope.

.. list-table::
   :header-rows: 1

   * - Group
     - Channel
     - Description
   * - **ad-mc-adc**
     - voltage0
     - Not used
   * -
     - voltage1
     - Motor 1 Ia ADC raw data
   * -
     - voltage2
     - Motor 1 Ib ADC raw data
   * -
     - voltage3
     - Motor 1 VBus ADC raw data
   * - **ad-mc-adc-m2**
     - voltage0
     - Not used
   * -
     - voltage1
     - Motor 2 Ia ADC raw data
   * -
     - voltage2
     - Motor 2 Ib ADC raw data
   * -
     - voltage3
     - Motor 2 VBus ADC raw data
   * - **ad-mc-speed**
     - voltage0
     - Motor 1 speed. Number of counts in 10ns units between two motor
       commutations. In order to display the speed in RPM, the data should be
       processed by checking the 1/x option and multiply by 25.000.000
   * - **ad-mc-speed-m2**
     - voltage0
     - Motor 1 speed. Number of counts in 10ns units between two motor
       commutations. In order to display the speed in RPM, the data should be
       processed by checking the 1/x option and multiply by 25.000.000
   * - **ad-mc-ctrl**
     - Not used
     -
   * - **ad-mc-ctrl-m2**
     - Not used
     -

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/software/mc_iio_signals.png
   :width: 600px

Control
~~~~~~~

This dialog allows the control of the two motors in manual mode by directly
specifying the fill factor of the PWM signals applied used to control the 3
phase inverters. The motors are driven using a 6 step comutation algorithm.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/software/mc_manual_ctrl.png
   :width: 400px

.. list-table::
   :header-rows: 1

   * - Control
     - Description
   * - Run
     - Starts the motor
   * - Delta
     - Selects between driving the motor using a Star-like sequence or Delta
       sequence
   * - Direction
     - Selects between clockwise and counterclockwise rotation directions
   * - PWM
     - In Manual mode, the PWM can be set between 50% - 100%
