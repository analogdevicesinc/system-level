.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcmotcon2-ebz/introduction

.. _ad-fmcmotcon2-ebz introduction:

ADI FMC Motor Drive System v2 Introduction
==========================================

**The ADI FMC motor drive v2 solution consist of the following products**

-
  :dokuwiki:`AD-FMCMOTCON2-EBZ <resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/controller_board>`
  - Controller board. Compatible with all Xilinx FPGA platforms with FMC LPC or
  HPC connectors.
-
  :dokuwiki:`AD-DRVLV2-EBZ <resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/lv_board>`
  - Low voltage drive board. Connects to the Controller board and has a power
  stage that can drive Brushed DC / BLDC / PMSM / Stepper motors up to 48V and
  20A.
-
  :dokuwiki:`AD-DYNO2-EBZ <resources/eval/user-guides/ad-fmcmotcon2-ebz/hardware/dyno>`
  - Dynamometer drive system. Acts as an electronically adjustable load with two
  BLDC motors connected in a dyno setup.

.. list-table::
   :header-rows: 1

   * - AD-FMCMOTCON2-EBZ
     - AD-DRVLV2-EBZ
     - AD-DYNO2-EBZ
   * - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/mc2_ctrl_single.jpg
          :width: 300px

     - .. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon2-ebz/mc2_lv_single.jpg
          :width: 400px

     - .. figure:: https://wiki.analog.com/_media//resources/eval/user-guides/ad-fmcmotcon2-ebz/mc2_dyno_single.jpg
          :width: 300px

.. note::

   The Controller and the Drive boards are provided as a kit and cannot be
   purchased separately. They are both distributed under the AD-FMCMOTCON2-EBZ
   part number.

**Purpose**

- Provide an efficient drive system for different types of electric motors
- Address power and isolation challenges encountered in motor control
  applications
- Provide accurate measurement of motor feedback signals
- Achieve flexible control with FPGA/SoC interface
- High speed industrial Ethernet interface

**Added Value**

- Complete control solution showing how to integrate hardware for

  * Power
  * Isolation
  * Measurement
  * Control

* Increased control flexibility due to FPGA interfacing capabilities
* Increased versatility to be able to control different types of motors
* Example reference designs showing how to use the control solution with Xilinx
  FPGAs

Where to Buy
------------

.. note::

   :adi:`FMCMOTCON2 Evaluation Kit <design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-FMCMOTCON2.html>`
