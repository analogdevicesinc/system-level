.. _ad_fmcmotcon2_ebz eval:

AD-FMCMOTCON2-EBZ (Obsolete)
===============================================================================

Complete Motor Drive Evaluation System on an FMC Board.

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCMOTCON2-EBZ` is a complete motor drive system on an FMC board,
designed to demonstrate efficient and high dynamic control of three-phase PMSM,
BLDC, induction, and Stepper motors up to 48 V and 20 A. Two motors can be
driven simultaneously, each with a separate power supply.

The system incorporates high-quality power supplies; reliable power, control,
and feedback signal isolation; accurate measurement of motor current and voltage
signals; high-speed interfaces for control signals; industrial Ethernet
interfaces; Hall, Differential Hall, Encoder, and Resolver position sensor
interfaces; EnDat and BISS digital sensor interfaces; and a flexible FPGA/SoC
control interface.

The :adi:`AD-DYNO2-EBZ` dynamometer acts as an electronically adjustable load
for testing real-time motor control performance. It consists of two BLDC motors
directly coupled through a rigid connection.

The system consists of:

- :adi:`AD-FMCMOTCON2-EBZ` - Controller board, compatible with all AMD Xilinx FPGA
  platforms with FMC LPC or HPC connectors.
- :adi:`AD-DRVLV2-EBZ` - Low voltage drive board. Drives Brushed DC / BLDC /
  PMSM / Stepper motors up to 48 V and 20 A.
- :adi:`AD-DYNO2-EBZ` - Dynamometer drive system. Electronically adjustable
  load with two BLDC motors in a dyno setup (optional).

.. note::

   The Controller and Drive boards are provided as a kit and cannot be purchased
   separately. Both are distributed under the AD-FMCMOTCON2-EBZ part number.

.. figure:: images/mc2_system.jpg
   :alt: AD-FMCMOTCON2-EBZ motor control system
   :align: center
   :width: 600

   AD-FMCMOTCON2-EBZ motor control system

Features:

- Complete motor drive system for PMSM, BLDC, Brushed DC, and Stepper motors
  up to 48 V and 20 A
- Two motors driven simultaneously with independent power supplies
- Reliable power, control, and feedback signal isolation
- Accurate motor current and voltage measurement using isolated ADCs
- 2x Gbit Ethernet PHYs for high-speed industrial communication (RGMII)
- Hall, Differential Hall, Encoder, and Resolver position sensor interfaces
- EnDat and BISS digital sensor interfaces
- Flexible FPGA/SoC control interface (FMC LPC/HPC compatible)
- Complete HDL reference designs for AMD Xilinx FPGA/SoC platforms
- MathWorks Simulink FOC controller integration
- QDESYS EtherCAT and FOC IP support

Applications:

- Industrial motor control prototyping and development
- Multi-axis servo drive systems
- Real-time EtherCAT motor control demonstrations
- Algorithm verification before production
- Academic research and teaching

Where to buy:
:adi:`FMCMOTCON2 Evaluation Kit <design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-FMCMOTCON2.html>`

.. toctree::
   :hidden:

   prerequisites
   user-guide
   quickstart/index

Recommendations
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience
with things. However, like many things, documentation is never as complete as
it should be. If you have any questions, feel free to ask on our
:ez:`/`, but before that, please make sure you read our documentation
thoroughly.

Table of contents
-------------------------------------------------------------------------------

#. Using the evaluation board/full stack reference design that we offer:

   #. :ref:`Prerequisites <ad_fmcmotcon2_ebz prerequisites>`
   #. :ref:`Quick start guides <ad_fmcmotcon2_ebz quickstart>`

      #. :ref:`Supported carriers <ad_fmcmotcon2_ebz carriers>`
      #. :ref:`Hardware setup <ad_fmcmotcon2_ebz hardware-setup>`
      #. :ref:`Linux on ZedBoard <ad_fmcmotcon2_ebz zedboard_quickstart>`

   #. :ref:`User guide <ad_fmcmotcon2_ebz user-guide>`

      #. :ref:`Hardware guide <ad_fmcmotcon2_ebz hardware-guide>`

         #. :ref:`Controller board <ad_fmcmotcon2_ebz controller-board>`
         #. :ref:`Low voltage drive board <ad_fmcmotcon2_ebz lv-board>`
         #. :ref:`Signal measurement chain <ad_fmcmotcon2_ebz signal-chain>`
         #. :ref:`Dynamometer drive system <ad_fmcmotcon2_ebz dyno>`
         #. :ref:`Test procedure <ad_fmcmotcon2_ebz test>`

      #. :ref:`Software guide <ad_fmcmotcon2_ebz software-guide>`

         #. :ref:`AMD Xilinx HDL reference design <ad_fmcmotcon2_ebz hdl>`
         #. :ref:`IIO drivers <ad_fmcmotcon2_ebz linux-drivers>`
         #. :ref:`IIO Oscilloscope <ad_fmcmotcon2_ebz iio-scope>`
         #. :ref:`QDESYS motor control IP <ad_fmcmotcon2_ebz qdesys-ip>`

#. :ref:`Help and Support <help-and-support>`

Help and Support
-------------------------------------------------------------------------------

If you have any questions regarding the ADI motor drive solutions or are
experiencing any problems while using the boards or following any of the user
guides, feel free to ask on our support community :ez:`/`.

For questions regarding the hardware or the HDL reference design, post in the
:ez:`Motor Control Hardware Platforms <community/motor-control-hardware-platforms2>`
or :ez:`FPGA Reference Designs <community/fpga>` sub-communities. For
questions regarding the Linux drivers for any of the components on the motor
control boards, use the
:ez:`Linux Software Drivers <community/linux-software-drivers>`
sub-community.

When asking a question, please give a detailed description of your problem.
Always include which platform you are using with the AD-FMCMOTCON2-EBZ, the
steps you executed, the result you expected, and the result you actually got.

For more information also check:

- `VITA's FMC info <http://www.vita.com/fmc>`_

Warning
-------------------------------------------------------------------------------

.. esd-warning::
