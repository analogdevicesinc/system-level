.. _adaq2387:

ADAQ2387x and LTC2387 family SAR ADC Developer Resources
#########################################################

.. attention::

   This page is in development, in a deployed pull request. Feedback welcome in
   the PR comment section.

Family Overview
================

This page describes various hardware and software resources available for evaluating and developing with certain Analog Devices' single-channel, SPI-interface, successive-approximation (SAR) Analog to Digital Converters.

The evaluation and development boards across these devices use the industry-standard FMC connector, compatible with industry-standard and proprietary carrier (processor/FPGA) boards. The choice depends on the developer's needs; If the development flow involves software and HDL development on standard carrier boards, it is best to use either the Pmod or FMC boards. Review the example projects and their user guides for the various options in order to make the best choice.

Wherever possible, pre-built programming and boot files are provided for the various carrier / eval board combinations. These typically implement an IIO (Industrial Input-Output) server, compatible with a wide array of software tools and language bindings, easing development considerably.

Getting Started
===============

There are several combinations of evaluation and development boards and controller platforms, with different capabilities and associated software and device driver resources. Review the options and choose the one that best suits your needs. In general combinations fall into two categories: 

The FMC eval boards can target either the SDP-H1 board or standard development platforms, while the SDP eval boards can only target the SDP-B or SDP-H1 board. The eval boards can interface to legacy evaluation boards and software are geared toward performance evaluation, with Windows-based GUI software that computes typical metrics such as THD, SNR, linearity, etc. These are closed-source, and further development requires moving to other controller boards and software development environments.


The second category of development systems is based on commercially available development platforms running open-source software, firmware, and HDL. Examples for this family of ADCs are shown in :numref:`fig-2387_iio_systems`. These systems are based on the Linux Industrial Input/Output (IIO) framework and are much more flexible, with multiple cross-platform options for both evaluation software and development software.

.. _fig-2387_iio_systems:

.. figure:: 2387x_iio_systems_block_diags.png
   :align: center
   :width: 600px
   
   IIO-Based Development System

Evaluation Boards and Development Platforms
===========================================

FMC (FPGA Mezzanine Card)
-------------------------

This is an industry standard, also known as VITA57. FMC is a widely used standard for both COTS and development carriers and module cards. FMC evaluation boards on this page are supported on the ZedBoard carrier board as well as the ADI proprietary SDP-H1 board. Pre-built example projects for the ZedBoard are provided that implement an IIO server, compatible with ACE, Scopy, and any language supported by the libiio (C, C#, Python, MATLAB, etc.) Important: The SDP-H1 is ADI proprietary, and works in conjunction with ACE software or product-specific evaluation software package. It is not intended as a development platform, and source code is not provided.

Software Resources
==================

Standard Application Software
-----------------------------
The HDL, Linux, and no-OS example projects are typically based on the Linux Industrial Input-Output (IIO) framework. This maximizes flexibility, as the framework is cross-platform (Windows, Linux, Mac) and supports multiple languages (C, C++, C#, Python, MATLAB, and others). The projects are also supported by the ACE evaluation GUI, and the Scopy multi-purpose data acquisition GUI. 

HDL IP Core
-----------

The HDL for these devices is based on the SPI Engine IP core, user guide here: `AXI LTC2387 <https://analogdevicesinc.github.io/hdl/library/axi_ltc2387/index.html>`_, and PWM IP core, which generates the sample rate from the master clock.

The example project for these devices is described at `CN0577 HDL project <https://analogdevicesinc.github.io/hdl/projects/cn0577/index.html>`_. 

The example project targets the :adi:`CN0577 Analog Front End and Digital Interface for Serial LVDS SAR ADCs <cn0577>`, and can be parameterized for each device, and building the project generates a set of boot files that can be run on the target platform.

Linux Device Drivers
--------------------

The Linux driver for these devices is presently in development, with the goal of having a single, unified driver covering all devices and the associated HDL code.

The LTC2387 driver is in upstream review, source at https://github.com/analogdevicesinc/linux/blob/main/drivers/iio/adc/ltc2387.c

The device driver is compatible with the HDL example project, and provides a convenient programming interface for controlling the ADC and capturing data.



Board and Platform Summary
==========================

The various eval boards and their supported platforms are listed below. The standard platforms can be used for product performance evaluation using ACE software, software development, and system prototyping. The ADI proprietary platforms are more constrained, and only work with the software listed.