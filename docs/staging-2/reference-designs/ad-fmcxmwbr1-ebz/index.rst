.. imported from: https://wiki.analog.com/resources/eval/user-guides/ad-fmcxmwbr1-ebz

.. _ad-fmcxmwbr1-ebz:

AD-FMCXMWBR1-EBZ User Guide
===========================

Introduction
------------

The :adi:`AD-FMCXMWBR1-EBZ` is a FMC-compatible level translator and power
supply board. It provides a direct connection between a compatible
controller/FPGA device and `X-Microwave <https://www.xmicrowave.com/>`__ blocks.
It is powered from the FMC connector but has the option to add an external
supply for applications that require higher load currents. This increases
flexibility and allows for multiple supply voltages with high current
capability. These can be used to bias the X-MW blocks or other IC"s in a
prototype design, allowing multiple level translated digital communications
paths between the controller board and the front-end.

.. figure:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcxmwbr1-ebz_top.jpg
   :width: 400px

Features
--------

- FMC-compatible form factor
- Powered from FMC connector with external supply possibility
- Provides level translation and various supply values
- Compatible with RaspberryPi X-MW controller

Applications
~~~~~~~~~~~~

- RF and Microwave designs
- Voltage level translation
- General-purpose software radios
- Radar systems
- Point to point communication systems
- Multiple input/multiple output (MIMO) radios
-  Automated test equipment

Hardware
--------

Hardware details and schematics of the AD-FMCXMWBR1-EBZ can be found on the
:dokuwiki:`AD-FMCXMWBR1-EBZ Hardware <resources/eval/user-guides/ad-fmcxmwbr1-ebz/hardware>`
page

Kit Contents
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - FMC X-Microwave Bridge Kit
     -
   * - FMC X-Microwave Bridge board
     - FMC Card with level translators and power supplies
   * - FMC X-Microwave Protoplate board
     - Prototyping board with access to all signals of interest
   * - Ribbon cable
     - For signal rails
   * - Custom cable
     - For power rails

Example-using ADRV9009-ZU11EG RF-SOM
------------------------------------

AD-FMCXMWBR1-EBZ is compatible with various development platforms that have
FMC/FMC+ connectors, and also with RaspberryPi. The board itself does not need a
specific software design to be used, since it acts as a "bridge" between the
development platform and the setup. We developed an example on how to use the
AD-FMCXMWBR1-EBZ as a bridge between the ADRV9009-ZU11EG RF-SOM and a setup of
various
`X-MWblocks <https://www.xmicrowave.com/product-category/x-mwblocks/>`__.

- :dokuwiki:`Setup Guide <resources/eval/user-guides/ad-fmcxmwbr1-ebz/quickstart>`
- :dokuwiki:`Reference HDL Design <resources/eval/user-guides/ad-fmcxmwbr1-ebz/reference_hdl>`
- :dokuwiki:`Software <resources/eval/user-guides/ad-fmcxmwbr1-ebz/software>`

Based on this example, the user can modify the software and adapt it for their
specific development board and devices in the X-MW setup.

Videos
------

.. video:: https://www.youtube.com/watch?v=3MH8Y6joSeE

Production Testing Process
--------------------------

More information about the testing procedure is found on
:dokuwiki:`Production Testing Process <resources/eval/user-guides/ad-fmcxmwbr1-ebz/testing>`
page.

These resources can be used as a development example, showing how you can
control any device that has a
:dokuwiki:`linux driver <resources/tools-software/linux-drivers-all>` and can be
included in the device tree, even devices that are not embedded in X-MW block.

Help and Support
----------------

For questions and more information please contact us on the Analog Devices
Engineer Zone.

.. note::

   :ez:`EngineerZone </>`

.. todo:: .. include: /wiki/common.rst

   :start-after: .. start-esd-warning
   :end-before: .. end-esd-warning
