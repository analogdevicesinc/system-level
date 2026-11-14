.. _hsx-toolbox:

High Speed Converter Toolbox
============================

.. note::

   This section only gives an overview on the High Speed Converter Toolbox,
   for all details, see
   `the dedicated doc <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master>`__.

Analog Devices High Speed Converter Toolbox for MATLAB and Simulink is a
set of tools to model, interface, and target with ADI high-speed
converter devices within MATLAB and Simulink. These are combined into a single
Toolbox which contains a set of Board Support Packages (BSP). The list of
supported boards is provided :ref:`below <hsx-toolbox supported boards>`.

Quick Start with Toolbox
------------------------

The current stable Toolbox can be downloaded from the
:git-HighSpeedConverterToolbox:`releases+`.
Download the latest mltbx file then open that file within MATLAB. Opening the
file will automatically install the Toolbox, adding the necessary components to
your MATLAB path. The "Analog Devices, Inc. High Speed Converter Toolbox" will
appear in your :mw:`Add-Ons Explorer <help/matlab/matlab_env/manage-your-add-ons.html>`
within MATLAB.

.. admonition:: Download

   :git-HighSpeedConverterToolbox:`releases+`.

To interface and stream data with hardware will require installation of
:ref:`libiio` and one of two Hardware Support Packages from MathWorks. The
libiio library can be obtained from the :git-libiio:`/`.

Libiio Installer
~~~~~~~~~~~~~~~~

.. admonition:: Download

   Stable releases are available at :git-libiio:`releases+`.

These support packages provide the necessary libIIO MATLAB bindings used by
ADI's system objects. Starting in R2024a, the functionality of Communications
Toolbox Support Package for Xilinx Zynq-Based Radio is included in SoC Blockset
Support Package for AMD Devices.

.. admonition:: Download

   | For releases after R2024a:
   | :mw:`SoC Blockset Support Package for AMD FPGA and SoC Devices <matlabcentral/fileexchange/70616-soc-blockset-support-package-for-amd-fpga-and-soc-devices>`
   | For Releases R2023b and before, either:
   | :mw:`Communications Toolbox Support Package for Xilinx Zynq-Based Radio <matlabcentral/fileexchange/48491-communications-toolbox-support-package-for-xilinx-zynq-based-radio>`
   | :mw:`Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio <help/supportpkg/plutoradio/index.html>`

.. important::

   Skip the Zynq SDR or ADALM-PLUTO post-installation steps. They
   are not used.
   See :external+kuiper:doc:`Kuiper documentation <index>` for the FPGA
   carrier board SD card images.

Toolbox Dependencies
~~~~~~~~~~~~~~~~~~~~

Depending on your needs, different toolboxes will be required. For basic data
streaming into MATLAB or Simulink only the following MathWorks toolboxes are
required:

-  :mw:`Communications Toolbox <products/communications/>`
-  :mw:`DSP System Toolbox <products/dsp-system/>`
-  :mw:`Signal Processing Toolbox <products/signal/>`
-  :mw:`SoC Blockset <products/soc.html>`
-  :mw:`SoC Blockset Support Package for AMD FPGA and SoC Devices (FREE) <matlabcentral/fileexchange/70616-soc-blockset-support-package-for-amd-fpga-and-soc-devices>`

For HDL code generation the following are required:

-  :mw:`HDL-Coder <products/hdl-coder>`
-  :mw:`Xilinx Zynq Support from HDL Coder (FREE) <hardware-support/zynq-hdl-coder>`

Building the Toolbox Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The toolbox can only be built under Linux or with Cygwin on a Windows platform.
Conveniently, the entire process is automated with a Makefile located in the
CI/scripts folder of the repository. The following is required on the system
before the build process can be run:

-  A supported MATLAB version installed in the default location
   (*/usr/local/MATLAB*)
-  A supported Vivado version installed in the default location
   (*/opt/Xilinx*)
-  Packages: ``git`` ``zip`` ``unzip`` ``tar`` ``make`` ``wget`` ``sed``

.. warning::

   You should only manually build the toolbox if you require a custom
   branch or no toolbox installer is available.

First clone the repo and move into it:

.. shell::

   $git clone https://github.com/analogdevicesinc/HighSpeedConverterToolbox.git
   $cd HighSpeedConverterToolbox

To build the toolbox run the following:

.. shell::

   ~/HighSpeedConverterToolbox
   $make -C CI/scripts build

To create an installable ``tlbx`` file run:

.. shell::

   ~/HighSpeedConverterToolbox
   $make -C CI/scripts gen_tlbx

.. _hsx-toolbox supported boards:

Supported Boards
-------------------------------------------------------------------------------
The following have device-specific implementations in MATLAB and Simulink. If a
device has an IIO driver, MATLAB support is possible, but a device-specific
MATLAB or Simulink interface may not exist yet.

.. list-table:: Supported Parts
   :header-rows: 1
   :widths: 20 20 20 15 25

   * - Evaluation Card
     - FPGA Board
     - Streaming Support
     - Targeting
     - Variants and Minimum Supported Release
   * - DAQ2 (AD9680/AD9144)
     - ZC706
     - Yes
     - No
     - ADI (2019a)
   * - DAQ2 (AD9680/AD9144)
     - ZCU102
     - Yes
     - Yes
     - ADI (2019a)
   * - DAQ2 (AD9680/AD9144)
     - Arria10 SoC
     - Yes
     - No
     - ADI (2019a)
   * - DAQ3 (AD9680/AD9152)
     - ZC706
     - Yes
     - No
     - ADI (2021b)
   * - DAQ3 (AD9680/AD9152)
     - ZCU102
     - Yes
     - No
     - ADI (2021b)
   * - DAQ3 (AD9680/AD9152)
     - KCU105
     - Yes
     - No
     - ADI (2021b)
   * - DAQ3 (AD9680/AD9152)
     - Arria10 SoC
     - Yes
     - No
     - ADI (2021b)
   * - DualAD9213
     - Stratix 10
     - Yes
     - No
     - ADI (2021b)
   * - AD9081/AD9082
     - ZCU102
     - Yes
     - Yes
     - ADI (2020a)
   * - AD9081/AD9082
     - VCU118
     - Yes
     - No
     - ADI (2020a)
   * - AD9083
     - ZCU102
     - Yes
     - No
     - ADI (2021b)
   * - AD9084
     - VCU118
     - Yes
     - No
     - ADI (2023b)
   * - AD9084
     - VPK180
     - Yes
     - No
     - ADI (2023b)
   * - AD9084
     - VCK190
     - Yes
     - No
     - ADI (2023b)
   * - AD9084
     - FM87
     - Yes
     - No
     - ADI (2023b)
   * - AD9988/AD9986
     - ZCU102
     - Yes
     - Yes
     - ADI (2020a)
   * - AD9988/AD9986
     - VCU118
     - Yes
     - No
     - ADI (2020a)
   * - AD9209/AD9177
     - ZCU102
     - Yes
     - Yes
     - ADI (2020a)
   * - AD9209/AD9177
     - VCU118
     - Yes
     - No
     - ADI (2020a)
   * - QuadMxFE (AD9081 x4)
     - VCU118
     - Yes
     - No
     - ADI (2020a)
   * - AD9467
     - Zedboard
     - Yes
     - No
     - ADI (2018b)
   * - FMCJESDADC1
     - ZC706
     - Yes
     - No
     - ADI (2021b)
   * - FMComms11
     - ZC706
     - Yes
     - No
     - ADI (2021b)
   * - AD9265
     - ZC706
     - Yes
     - No
     - ADI (2021b)
   * - AD9434
     - ZC706
     - Yes
     - No
     - ADI (2021b)
   * - AD9656
     - ZCU102
     - Yes
     - No
     - ADI (2021b)
   * - AD9695
     - ZCU102
     - Yes
     - No
     - ADI (2021b)
   * - AD9739a
     - ZC706
     - Yes
     - No
     - ADI (2021b)
   * - AD9162
     - ZC706
     - Yes
     - No
     - ADI (2021b)
   * - AD9164
     - ZC706
     - Yes
     - No
     - ADI (2021b)
   * - AD9152
     - ZC706
     - Yes
     - No
     - ADI (2021b)

Useful Articles
---------------

-  `Installation <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/install/>`__
-  `Device control and streaming <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/streaming/>`__
-  `HDL targeting <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/targeting/>`__
-  `Behavioral simulations <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/models/>`__
-  `Supported hardware <https://analogdevicesinc.github.io/HighSpeedConverterToolbox/master/>`__
-  :ref:`matlab bsp-extend`

Further Reading
---------------

:adi:`Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio - Part 4 <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

Help & Support
---------------

Questions? :ez:`Ask Help & Support <linux-software-drivers>`.
