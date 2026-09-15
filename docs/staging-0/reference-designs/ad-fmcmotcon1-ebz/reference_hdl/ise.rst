.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon1-ebz/reference_hdl/ise

.. _ad-fmcmotcon1-ebz reference_hdl ise:

Xilinx ISE HDL Reference Design
===============================

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-retired
   :end-before: .. end-retired

This design is targeted for Zynq based FPGA systems.

Reference Design
----------------

The reference design contains HDL blocks for interfacing with the various
components of the motor control hardware:

- ADC Interface - Implements the communication with the AD7401 sigma delta
  modulators present on the AD-FMCMOTCON1-EBZ and also the SINC3 filters for
  demodulating the 1-bit digital stream provided by these parts.
- Controller - Implements the motor control algorithm. The algorithm is designed
  and simulated in Simulink from Matworks and afterwards translated to HDL using
  the Mathworks HDL Coder.
- Speed Sensor Interface - Implements the algorithm for converting Hall, BEMF
  and Encoder signals into speed and position data.

All the HDL blocks connect to Chipscope ILA and VIO modules which provide the
means to monitor and control their operation.

Details about the Chipscope interface and how to run the ISE project can be
found in the
:dokuwiki:`ISE Project with Chipscope Quick Start Guide </resources/eval/user-guides/ad-fmcmotcon1-ebz/quickstart/chipscope>`.

Downloads
---------

.. admonition:: Download

   :git-fpgahdl_xilinx:`ISE HDL Reference Design <motor_control/adi_zed_ise_rev2+>`
   :git-fpgahdl_xilinx:`Chipscope Project <motor_control/adi_zed_ise_rev2/Chipscope+>`

Support
-------

.. note::

   - Questions? :ez:`Ask Help & Support <fpga>`.
