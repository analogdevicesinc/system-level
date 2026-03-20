AD-FMCMOTCON2-EBZ User Guide
============================

The :adi:`AD-FMCMOTCON2-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-FMCMOTCON2.html#eb-overview>` is a complete motor drive system on a FMC board. Information on the card, and how to use it, the design package that surrounds it, and the software which can make it work, can be found here.

The purpose of the AD-FMCMOTCON2-EBZ is to provide a complete motor drive system
demonstrating efficient and high dynamic control of three phase PMSM, BLDC,
induction and stepper motors up to 48V and 20A. Two motors can be driven at the
same time, each motor having its separate power supply. The kit consists of two
boards: a controller board and a drive board. The system incorporates high
quality power supplies; reliable power, control, and feedback signals isolation;
accurate measurement of motor current & voltage signals; high speed interfaces
for control signals to allow fast controller response; industrial Ethernet high
speed interfaces; single ended Hall, differential Hall, encoder and resolver
interfaces; digital position sensors interface; flexible control with a FPGA/SoC
interface.

The **AD-DYNO2-EBZ** dynamometer is provided as an extension of the drive system. This is a dynamically adjustable load system that can be used to test real-time motor control performance. It consists of two BLDC motors directly coupled through a rigid connection. One of the BLDC motors acts as a load and is controlled by the DYNO’s embedded control system while the second motor is driven by the AD-FMCMOTCON2-EBZ FMC board. The load can be driven also by the AD-FMCMOTCON2-EBZ to implement dynamic load profiles.

This platform is intended to be used as a prototyping system to verify the
hardware and the control algorithms before moving to the production stage. It
helps reduce the time needed to move a motor control system from concept to
production. Example reference designs showing how to use the platform with
Xilinx® FPGAs or SoCs and high performance control algorithms from Mathworks®
and Qdesys® are provided together with the hardware.

.. image:: images/mc2_system.jpg
   :align: right
   :width: 600

-  :doc:`Introduction </solutions/reference-designs/ad-fmcmotcon2-ebz/introduction>`
-  Quick Start Guides

   -  :doc:`Hardware Setup Guide </solutions/reference-designs/ad-fmcmotcon2-ebz/quickstart/lv_setup_guide>`
   -  :doc:`Linux on Zynq </solutions/reference-designs/ad-fmcmotcon2-ebz/quickstart/zynq>`

-  :doc:`Hardware </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware>`

   -  :doc:`Controller Board </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/controller_board>`
   -  :doc:`Low Voltage Drive Board </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/lv_board>`
   -  :doc:`Signal Measurement Chain </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/signal_chain>`
   -  :doc:`Dynamometer Drive System </solutions/reference-designs/ad-fmcmotcon2-ebz/hardware/dyno>`

-  :doc:`HDL Reference Design </solutions/reference-designs/ad-fmcmotcon2-ebz/reference_hdl>`
-  :doc:`Software </solutions/reference-designs/ad-fmcmotcon2-ebz/software>`

   -  :doc:`Linux Drivers </solutions/reference-designs/ad-fmcmotcon2-ebz/software/linux_drivers>`
   -  :doc:`IIO Scope </solutions/reference-designs/ad-fmcmotcon2-ebz/software/iio_scope>`

-  `Xilinx Zynq Intelligent Drives Support from Simulink <https://www.mathworks.com/hardware-support/zynq-motor-control.html>`_
-  :doc:`QDESYS Motor Control IP & EtherCAT Design </solutions/reference-designs/ad-fmcmotcon2-ebz/qdesys_ip>`
-  :doc:`Help and Support </solutions/reference-designs/ad-fmcmotcon2-ebz/help_and_support>`
