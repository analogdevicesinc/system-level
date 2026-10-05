.. _ad9084 user-guide:

User guide
===============================================================================

:adi:`EVAL-AD9084` top view:

.. image:: ../images/eval_ad9084_top_view.png
   :align: center
   :width: 500

The complete user guides of the evaluation board can be found at:

- :adi:`AD9084/AD9088 Software Development User Guide, UG-2300 (Rev. Prl) <media/en/technical-documentation/user-guides/ad9084-ad9088-device-ug-2300.pdf>`
- :adi:`EVAL-AD9084 User Guide, UG-2326 (Rev. 0) <media/en/technical-documentation/user-guides/eval-ad9084-ug-2326.pdf>`

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power supply comes from the FMC connector, given by the FPGA.

The VADJ values can be checked out in the README.md file of each combination
with an FPGA, at: :git-hdl:`projects/ad9084_fmca_ebz`.

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

- :ref:`iio-oscilloscope`
- :external+pyadi-iio:doc:`index`

Multi-Chip Synchronization (MCS)
-------------------------------------------------------------------------------

For synchronized multi-channel architectures utilizing multiple EVAL-AD9084
boards with parent ADF4030 clock distribution, refer to:

- :ref:`ad9084-multi-chip-sync` — Complete reference design for setting up
  multi-chip synchronization with 2x AD9084+VCU118 and parent ADF4030.

