ADI FMC Motor Drive System v2 Introduction
==========================================

**The ADI FMC motor drive v2 solution consist of the following products**

-  :doc:`AD-FMCMOTCON2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/controller_board>` - Controller board. Compatible with all Xilinx FPGA platforms with FMC LPC or HPC connectors.
-  :doc:`AD-DRVLV2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/lv_board>` - Low voltage drive board. Connects to the Controller board and has a power stage that can drive Brushed DC / BLDC / PMSM / Stepper motors up to 48V and 20A.
-  :doc:`AD-DYNO2-EBZ </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/dyno>` - Dynamometer drive system. Acts as an electronically adjustable load with two BLDC motors connected in a dyno setup.

=================== =============== ==============
AD-FMCMOTCON2-EBZ   AD-DRVLV2-EBZ   AD-DYNO2-EBZ
=================== =============== ==============
|AD-FMCMOTCON2-EBZ| |AD-DRVLV2-EBZ| |AD-DYNO1-EBZ|
=================== =============== ==============

.. note::

   The Controller and the Drive boards are provided as a kit and cannot be
   purchased separately. They are both distributed under the AD-FMCMOTCON2-EBZ
   part number.

**Purpose**

-  Provide an efficient drive system for different types of electric motors
-  Address power and isolation challenges encountered in motor control applications
-  Provide accurate measurement of motor feedback signals
-  Achieve flexible control with FPGA/SoC interface
-  High speed industrial Ethernet interface

**Added Value**

-  Complete control solution showing how to integrate hardware for

   -  Power

      -  Isolation
      -  Measurement
      -  Control

-  Increased control flexibility due to FPGA interfacing capabilities
-  Increased versatility to be able to control different types of motors
-  Example reference designs showing how to use the control solution with Xilinx
   FPGAs

Where to Buy
------------

.. container:: round box

   :adi:`FMCMOTCON2 Evaluation Kit <design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-FMCMOTCON2.html>`

.. |AD-FMCMOTCON2-EBZ| image:: images/mc2_ctrl_single.jpg
   :width: 300
.. |AD-DRVLV2-EBZ| image:: images/mc2_lv_single.jpg
   :width: 400
.. |AD-DYNO1-EBZ| image:: images/mc2_dyno_single.jpg
   :width: 300
