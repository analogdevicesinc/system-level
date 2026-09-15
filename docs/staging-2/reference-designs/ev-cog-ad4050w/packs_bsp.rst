.. imported from: https://wiki.analog.com/resources/eval/user-guides/ev-cog-ad4050w/packs_bsp

.. _ev-cog-ad4050w packs_bsp:

Software Packs & Board Support Package
======================================

A modular software framework is provided for quick application prototyping.
Based on the application use case, developers need to download the respective
software packs.

.. note::

   There are no seperate toolchain,software packs and board support package for
   EV-COG-AD4050WZ, the toolchain,software packs and board support package for
   EV-COG-AD4050LZ works with EV-COG-AD4050WZ.The user needs to change only the
   pin muxing based on the application.For help regarding pinmapping refer to
   the Hardware Details section.

.. important::

   Please make sure you install either of the below toolchain before installing
   any of the below packs

   #. IAR Embedded Workbench for ARM 8.20.1 or higher
   #. CrossCore Embedded Studio 2.7.0 ® or higher

The Cog software development kit consists of the following packs:

-:dokuwiki:`Analog Devices ADuCM4x50 Device Support <resources/eval/user-guides/ev-cog-ad4050lz/software/aducm4x50>` -
  This is a bare minimum pack required to enable working with ADuCM4050 and develop simple applications using the on-chip drivers.

Version History

- **Version: 3.1.0** - Extended support for IAR Embedded Workbench and Keil
  uVision. **[Latest]**
- :dokuwiki:`Analog Devices EV-COG-AD4050 Off-Chip Drivers and Examples <resources/eval/user-guides/ev-cog-ad4050lz/software/eval-cog-ad4050lz>` -
  This pack along with the DFP is required to develop applications using the on-board drivers.
