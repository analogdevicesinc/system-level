.. _ad_fmcmotcon1_ebz eval:

AD-FMCMOTCON1-EBZ (Obsolete)
===============================================================================

Complete Motor Drive Evaluation System on an FMC Board.

.. warning::

   The :adi:`AD-FMCMOTCON1-EBZ` is a **legacy product** and is no longer
   actively supported. This documentation is provided for reference only.

Overview
-------------------------------------------------------------------------------

The :adi:`AD-FMCMOTCON1-EBZ` is a complete motor drive system on an FMC
board, designed to demonstrate efficient control of Brushed DC, BLDC, PMSM,
and Stepper motors. It consists of two boards - a controller board and a drive
board - and is optionally extended by a dynamometer module.

The system incorporates high-quality power sources; reliable power, control,
and feedback signal isolation; accurate measurement of motor current and
voltage signals; high-speed interfaces for control signals to allow fast
controller response; industrial Ethernet high-speed interfaces; and a flexible
FPGA/SoC control interface.

The platform is intended for prototyping and verifying hardware and control
algorithms before moving to production. Example reference designs for Xilinx
FPGAs/SoCs and MathWorks Simulink are provided with the hardware.

The system consists of:

- :adi:`AD-FMCMOTCON1-EBZ` - Controller board, compatible with all Xilinx
  FPGA platforms with FMC LPC or HPC connectors.
- :adi:`AD-DRVLV1-EBZ` - Low voltage drive board. Connects to the Controller
  board and drives Brushed DC / BLDC / PMSM / Stepper motors up to 48 V
  and 18 A.
- :adi:`AD-DYNO1-EBZ` - Dynamometer drive system. An electronically adjustable
  load with two BLDC motors in a dyno setup (optional).

.. figure:: images/mc_system.jpg
   :alt: AD-FMCMOTCON1-EBZ motor control system
   :align: center
   :width: 600

   AD-FMCMOTCON1-EBZ motor control system

Features:

- Efficient drive system for Brushed DC, BLDC, PMSM, and Stepper motors
- Power, control, and feedback signal isolation
- Accurate motor current and voltage measurement using isolated ADCs
- 2x Gbit Ethernet PHYs for high-speed industrial communication
- Hall, Differential Hall, Encoder, and Resolver position sensor interfaces
- Flexible FPGA/SoC control interface (FMC LPC/HPC compatible)
- Complete HDL reference designs for Xilinx FPGA/SoC platforms
- MathWorks Simulink FOC controller integration

Applications:

- Industrial motor control prototyping
- Servo drive systems development
- Algorithm verification before production
- Academic research and teaching

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

   #. :ref:`Prerequisites <ad_fmcmotcon1_ebz prerequisites>`
   #. :ref:`Quick start guides <ad_fmcmotcon1_ebz quickstart>`

      #. :ref:`Supported carriers <ad_fmcmotcon1_ebz carriers>`
      #. :ref:`Linux on ZedBoard <ad_fmcmotcon1_ebz zedboard_quickstart>`
      #. :ref:`ISE Project with Chipscope <ad_fmcmotcon1_ebz chipscope_quickstart>`

   #. :ref:`User guide <ad_fmcmotcon1_ebz user-guide>`

      #. :ref:`Hardware guide <ad_fmcmotcon1_ebz hardware-guide>`

         #. :ref:`Controller board <ad_fmcmotcon1_ebz controller-board>`
         #. :ref:`Low voltage drive board <ad_fmcmotcon1_ebz lv-board>`
         #. :ref:`Signal measurement chain <ad_fmcmotcon1_ebz signal-chain>`
         #. :ref:`Dynamometer drive system + testing <ad_fmcmotcon1_ebz dyno>`

      #. :ref:`Motor control theory <ad_fmcmotcon1_ebz introduction>`

         #. :ref:`Electric motor drives <ad_fmcmotcon1_ebz drives>`
         #. :ref:`Brushed DC motor control <ad_fmcmotcon1_ebz dc-control>`
         #. :ref:`Brushless DC motor control <ad_fmcmotcon1_ebz bldc-control>`

      #. :ref:`Software guide <ad_fmcmotcon1_ebz software-guide>`

         #. :ref:`Xilinx HDL reference design (Linux) <ad_fmcmotcon1_ebz hdl-linux>`
         #. :ref:`Xilinx ISE HDL reference design <ad_fmcmotcon1_ebz hdl-ise>`
         #. :ref:`Linux drivers <ad_fmcmotcon1_ebz linux-drivers>`
         #. :ref:`IIO Oscilloscope <ad_fmcmotcon1_ebz iio-scope>`
         #. :ref:`Simulink controller models <ad_fmcmotcon1_ebz matlab-models>`
         #. :ref:`QDESYS motor control IP <ad_fmcmotcon1_ebz qdesys-ip>`

#. :ref:`Help and Support <help-and-support>`

Videos
-------------------------------------------------------------------------------

ADI/Avnet/MathWorks/Xilinx design seminar:
`Watch on AnalogTV <https://www.analog.com/en/education/education-library/videos/3540825244001.html>`_

From ADI's 2013 Design Conference:
`YouTube: AD-FMCMOTCON1-EBZ Demo <https://www.youtube.com/watch?v=-7CscB5sUIw>`_

Help and Support
-------------------------------------------------------------------------------

If you have any questions regarding the ADI motor drive solutions or are
experiencing any problems while using the boards or following any of the user
guides, feel free to ask on our support community :ez:`/`.

For questions regarding the hardware or the HDL reference design, post in the
:ez:`FPGA Reference Designs <fpga>` sub-community. For questions
regarding the Linux drivers for any of the components on the motor control
boards, use the
:ez:`Linux Software Drivers <linux-software-drivers>`
sub-community.

When asking a question, please give a detailed description of your problem.
Always include which platform you are using with the AD-FMCMOTCON1-EBZ, the
steps you executed, the result you expected, and the result you actually got.

Before asking, also check if somebody else already asked the same question and
received an answer.

For more information also check:

- `VITA's FMC info <http://www.vita.com/fmc>`_

Warning
-------------------------------------------------------------------------------

.. esd-warning::
