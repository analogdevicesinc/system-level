.. _adrv9032 user-guide:

User guide
===============================================================================

The complete user guide of the evaluation board can be found at
:adi:`ADRV903x System Development User Guide (UG-2278) <media/en/technical-documentation/user-guides/adrv903x-ug-2278.pdf>`.

Hardware guide
-------------------------------------------------------------------------------

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA.

The VADJ values can be checked out in the README.md file of each combination
with an FPGA, at: :git-hdl:`projects/adrv903x`.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design files for the EVAL-ADRV9032 evaluation board include:

- Schematics
- PCB Layout
- Bill of Materials
- Design package

Please refer to the :adi:`ADRV9032R product page <ADRV9032R>` for
downloadable design files.

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported with the Libiio library. This library is
cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
MATLAB, and others. One easy to example that can be used with it is:

.. include-template:: ../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: true

.. include-template:: ../common/using-scopy.rst.jinja

