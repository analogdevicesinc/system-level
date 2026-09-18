.. _ad9081 user-guide:

User guide
===============================================================================

.. toctree::

   2to24ghz-mxfe-rf-front-end

:adi:`EVAL-AD9081` top view:

.. figure:: ../../images/eval_ad9081_top_view.png
   :align: center
   :width: 500

   EVAL-AD9081 top view

:adi:`EVAL-AD9082` top view:

.. figure:: ../../images/eval_ad9082_top_view.png
   :align: center
   :width: 500

   EVAL-AD9082 top view

The complete user guide of the evaluation board can be found at
:adi:`AD9081/AD9082 Software Development User Guide, UG-1578 (Rev. A) <media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`.

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   When using
   :intel:`A10SoC <content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>`
   in your setup, the following reworks are required **on the evaluation
   board**:

   - To avoid using an external clock source and fully rely on the HMC7044
     clock chip, rotate the C6D/C4D caps in C5D/C3D position
     (Please note: In the latest version of the board, this is now the
     default configuration, so this configuration step **might not
     be needed anymore**).
   - If LEDS V1P0_LED and VINT_LED are not on, please **depopulate R22M
     and populate R2M**

   For the carrier,
   :intel:`A10SoC <content/www/us/en/products/details/fpga/development-kits/arria/10-sx.html>`,
   the following reworks are mandatory:
   :ref:`FMC Pin Connection Configuration <ad9081 quickstart a10soc_changes>`

.. warning::

   For
   :intel:`FM87 <content/www/us/en/products/details/fpga/development-kits/agilex/si-agi027.html>`
   setups, the following reworks are required on the evaluation board:

   - C39B, C40B: 50 ohm

   For the carrier
   :intel:`FM87 <content/www/us/en/products/details/fpga/development-kits/agilex/si-agi027.html>`,
   the following reworks are required:

   - R1433, R1434: 50 ohm
   - R1777, R1778: 50 ohm
   - C2488, C4289:  0 ohm
   - R1231, R1234: 1k ohm
   - R1230, R1233: 1k ohm

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA.

The VADJ values can be checked out in the README.md file of each combination
with an FPGA, at: :git-hdl:`projects/ad9081_fmca_ebz`.

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The schematic can be found at
:adi:`ad9081-mxfe-fmca-revc-eval-board-schematic.pdf <media/en/technical-documentation/eval-board-schematic/ad9081-mxfe-fmca-revc-eval-board-schematic.pdf>`.

The archive
:adi:`ad9081-ad9082.zip <media/en/evaluation-documentation/evaluation-design-files/ad9081-ad9082.zip>`
contains the design files for :adi:`EVAL-AD9081` and :adi:`EVAL-AD9082`
evaluation boards.

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported with the Libiio library. This library is
cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
MATLAB, and others. Two easy examples that can be used with it are:

- :external+pyadi-iio:doc:`PyADI-IIO <index>`

.. include-template:: ../../common/using-iio-osc.rst.jinja

   has_linux: true
   has_no_os: true

About the IIO devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Main receivers RX1, RX2, RX3, and RX4 are handled by the axi-ad9081-rx-hpc IIO
device.

Channels:

- IIO device channel: ``axi-ad9081-rx-hpc``
- Receiver inputs:

  - {``voltage0_i``, ``voltage0_q``}: RX1
  - {``voltage1_i``, ``voltage1_q``}: RX2
  - {``voltage2_i``, ``voltage2_q``}: RX3
  - {``voltage3_i``, ``voltage3_q``}: RX4


.. include-template:: ../../common/using-scopy.rst.jinja
