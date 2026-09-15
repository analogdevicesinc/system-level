.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon1-ebz/matlab_models

.. _ad-fmcmotcon1-ebz matlab_models:

Simulink Controller Models
==========================

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-retired
   :end-before: .. end-retired

The Vivado HDL design is provided with an integrated FOC and speed & torque
controller generated from a Simulink model provided by MathWorks. The controller
is designed in Simulink and the corresponding HDL code is generated using the
Mathworks HDL Coder.

Field Oriented Controller (FOC)
-------------------------------

The FOC controller model is provided by MathWorks and it is integrated in the
HDL design as a standalone IP core. Below is presented a top level diagram of
the controller"s Simulink model. For more information about the model check out
the MathWorks website.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/foc_simulink.png
   :width: 700px

The controller model is packaged into an IP core using the Simulink Workflow
Advisor. It exposes a set of AXI-Lite registers that can be used to control the
IP"s operation as well as a set of interface signals for encoder input, current
measurement data, inverter control and internal operations monitoring. All the
monitoring signals connect to an ADI IP which allows these signals to be
monitored from the Linux IIO Scope application. The AXI-Lite registers exposed
by the controller IP core can be directly accessed through an uio driver present
in the ADI Linux distribution for Zynq. The table below lists the exposed
AXI-Lite registers.

.. list-table::
   :header-rows: 1

   * - Register name
     - Address
     - Data format
     - Type
     - Description
   * - axi_controller_mode
     - 0x100
     - 2 bit word
     - W
     - Sets the controller"s operation modes: 3 = open loop, 2 = closed loop, 1
       = standby
   * - axi_command
     - 0x104
     - Sigend fixed point 18.8
     - W
     - Motor reference speed in rad/s
   * - axi_velocity_p_gain
     - 0x108
     - Sigend fixed point 18.16
     - W
     - Proportional gain of the velocity PI controller
   * - axi_velocity_i_gain
     - 0x10C
     - Sigend fixed point 18.15
     - W
     - Integral gain of the velocity PI controller
   * - axi_current_p_gain
     - 0x110
     - Sigend fixed point 18.10
     - W
     - Proportional gain of the current PI controller
   * - axi_current_i_gain
     - 0x114
     - Sigend fixed point 18.12
     - W
     - Integral gain of the current PI controller
   * - axi_open_loop_bias
     - 0x118
     - Sigend fixed point 18.14
     - W
     - Open loop control command bias
   * - axi_open_loop_scalar
     - 0x11C
     - Sigend fixed point 18.16
     - W
     - Open loop control command gain
   * - axi_encoder_zero_offset
     - 0x120
     - Sigend fixed point 18.14
     - W
     - Encoder offset
   * - axi_electrical_pos_err
     - 0x124
     - Sigend fixed point 19.14
     - R
     - Error between actual electrical position and encoder position

The operation of the IP core is controlled through the *foc_script.sh* script
located under */usr/local/bin*. The script executes the following steps:

- Set the FOC controller in open loop mode and wait for the user to start the
  motor by clicking the Run checkbox in IIO scope
- Calibrate the encoder readings to remove the offset between the motor"s actual
  electrical position and the position read from the encoder
- Set the motor"s reference speed
- Start the FOC controller in closed loop mode

The IP core exposes a set of signals for interfacing with the rest of the
system. The table below lists the exposed interface signals.

.. list-table::
   :header-rows: 1

   * - Signal name
     - Direction
     - Width
     - Data format
     - Description
   * - adc_current1
     - I
     - 18
     - Signed fixed point 18.17
     - Phase A current measurement
   * - adc_current2
     - I
     - 18
     - Signed fixed point 18.17
     - Phase B current measurement
   * - encoder_a
     - I
     - 1
     - Boolean
     - Encoder channel A
   * - encoder_b
     - I
     - 1
     - Boolean
     - Encoder channel B
   * - encoder_index
     - I
     - 1
     - Boolean
     - Encoder index
   * - pwm_a
     - O
     - 1
     - Boolean
     - Phase A PWM control signal
   * - pwm_b
     - O
     - 1
     - Boolean
     - Phase B PWM control signal
   * - pwm_c
     - O
     - 1
     - Boolean
     - Phase C PWM control signal
   * - mon_phase_voltage_a
     - O
     - 32
     - Signed fixed point 32.12
     - Phase A voltage in Volts
   * - mon_phase_voltage_b
     - O
     - 32
     - Signed fixed point 32.12
     - Phase B voltage in Volts
   * - mon_phase_current_a
     - O
     - 32
     - Signed fixed point 32.15
     - Phase A current in Amps
   * - mon_phase_current_b
     - O
     - 32
     - Signed fixed point 32.15
     - Phase B current in Amps
   * - mon_rotor position
     - O
     - 32
     - Signed fixed point 32.14
     - Rotor mecahnical position in radians
   * - mon_electrical position
     - O
     - 32
     - Signed fixed point 32.14
     - Rotor electrical position in radians
   * - mon_rotor_velocity
     - O
     - 32
     - Signed fixed point 32.8
     - Rotor velocity in rad/s
   * - mon_d_current
     - O
     - 32
     - Signed fixed point 32.15
     - d current in Amps
   * - mon_q_current
     - O
     - 32
     - Signed fixed point 32.15
     - q current in Amps

Below is presented a picture containing the output of the script, the IIO Scope
settings and a controller monitored signals plot.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/mc_full_sc.png
   :width: 700px

Support
-------

.. note::

   - Questions? :ez:`Ask Help & Support <sw-interface-tools>`.
